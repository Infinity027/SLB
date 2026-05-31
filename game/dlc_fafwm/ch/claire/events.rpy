init python:
    Event(**{
    "name": "claire_event_01",
    "label": "claire_event_01",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("street"),
            IsActivity("None"),
            ),
        IsHour(9, 11),
        IsDayOfWeek("7"),
        ],
    "priority": 1000,
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_02",
    "label": "claire_event_02",
    "conditions": [
        IsDone("claire_event_01"),
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsActivity("None"),
            ),
        PersonTarget("claire",
            MinStat("love", 20),
            IsFlag("clairedelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_03",
    "label": "claire_event_03",
    "conditions": [
        IsDone("claire_event_02"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        IsHour(20, 22),
        PersonTarget("claire",
            MinStat("love", 40),
            IsFlag("clairedelay", False),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_04",
    "label": "claire_event_04",
    "conditions": [
        IsDone("claire_event_03"),
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
            IsGender("male"),
            IsActivity("None"),
            Or(
                HasRoomTag("mall_southside"),
                HasRoomTag("mall_northside"),
                ),
            ),
        PersonTarget("claire",
            MinStat("love", 60),
            IsFlag("clairedelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_05",
    "label": "claire_event_05",
    "conditions": [
        IsDone("claire_event_04"),
        IsTimeOfDay("morning"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget("claire",
            MinStat("love", 80),
            IsFlag("clairedelay", False),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })


    Event(**{
    "name": "claire_event_06",
    "label": "claire_event_06",
    "conditions": [
        IsDone("claire_event_05"),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            Not(HasRoomTag("home")),
            Not(HasRoomTag("work")),
            Not(IsRoom("map")),
            ),
        PersonTarget("claire",
            MinStat("love", 100),
            IsFlag("clairedelay", False),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_07",
    "label": "claire_event_07",
    "conditions": [
        IsDone("claire_event_06"),
        IsTimeOfDay("morning"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            IsRoom("coffeeshop"),
            ),
        PersonTarget("claire",
            MinStat("love", 120),
            IsFlag("clairedelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_08",
    "label": "claire_event_08",
    "conditions": [
        IsDone("claire_event_07"),
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget("claire",
            MinStat("love", 140),
            IsFlag("clairedelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_event_09",
    "label": "claire_event_09",
    "conditions": [
        IsDone("claire_event_08"),
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            Not(HasRoomTag("work")),
            ),
        PersonTarget("claire",
            MinStat("love", 160),
            IsFlag("clairedelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_preg_talk",
    "label": "claire_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsActivity("None"),
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(claire,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/focus.ogg",
    })

    Event(**{
    "name": "claire_sub_event_01",
    "label": "claire_sub_event_01",
    "priority": 500,
    "conditions": [
        IsDone("claire_event_04"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            ),
        MinDateScore(90),
        PersonTarget(claire,
            OnDate(),
            MinStat("sub", 25),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "claire_sub_event_02",
    "label": "claire_sub_event_02",
    "priority": 500,
    "conditions": [
        IsDone("claire_event_06"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            ),
        MinDateScore(90),
        PersonTarget(claire,
            OnDate(),
            MinStat("sub", 50),
            MinStat("sexperience", 3),
            IsFlag("subevent", False),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "claire_sub_event_03",
    "label": "claire_sub_event_03",
    "priority": 500,
    "conditions": [
        IsDone("claire_event_08"),
        HeroTarget(
            IsGender("male"),
            IsActivity("run_park"),
            ),
        PersonTarget(claire,
            MinStat("sub", 75),
            MinStat("sexperience", 5),
            IsFlag("subevent", False),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })


label claire_event_01:
    scene expression f"bg {game.room}" with fade
    "I'm not one of those guys that's always wanting to go back home, you know?"
    "It's not that I have a load of unresolved trauma associated with my childhood."
    "Well...no more than any ordinary person does these days..."
    "But to me it always feels like you're wallowing in nostalgia wanting to go home all the time."
    "So it's going to take a lot to make me get up off my ass and travel all the way out to the sticks."
    "Something big, like maybe a childhood friend finally announcing that they're about to tie the knot."
    "Which, coincidentally, is exactly how I've come to find myself walking up the path to a certain front-door."
    scene bg clairehouse house with fade
    "I recognise the fancy house in front of me as the one that my old friend Adam grew up in."
    "Sure, there have been some small cosmetic changes, an extension here and new windows there."
    show bg clairehouse house at blur(5) with dissolve
    "But it's still the place where we used to play with action figures in the rockery."
    play sound door_bell
    "So as I ring the door-bell, you can be sure that my head is already filled with vivid memories."
    show bg clairehouse house at blur(10) with dissolve
    play sound door_open
    "In fact I'm so distracted that my gaze is still on the garden when the door actually opens."
    claire.say "Hello?"
    claire.say "Oh...oh my goodness!"
    claire.say "[hero.name], is that really you?"
    claire.say "My, my - you really have grown!"
    scene bg clairehouse house with hpunch
    "I recognise the voice in an instant, and that's enough to snap me back to reality."
    "Because now even more memories are coming flooding back."
    "Specifically ones related to my most awkward teenage years."
    "Memories of barely contained desires and secret fantasies."
    scene bg door double at center, zoomAt(1.8, (640, 1020))
    show claire at center, zoomAt(1.6, (640, 1020))
    with blinds
    "I turn my head towards the door, already excited to see the person I know is standing there."
    mike.say "Claire..."
    mike.say "It's great to see..."
    show claire b at center, traveling(4, 0.2, (640, 1920))
    pause 0.2
    show claire b at center, zoomAt(4, (640, 1920))
    mike.say "Mmmph...mmmph!" with hpunch
    "My intention was to turn around in a confident, controlled manner."
    "Because I know that it's Adam's step-mom that's answered the door."
    "And, of course, I want her to make the best impression possible."
    "But that's kind of hard when you suddenly find your face buried in a whole lot of cleavage!"
    "Claire has her arms wrapped tightly around me, and she's far stronger than I remember her being."
    "I can't be trapped there for more than a couple of seconds, but to me it feels like a lifetime."
    show claire a at center, traveling(2, 0.5, (640, 1220))
    "And when she finally loosens her grip, my head pops up, a stunned look on my face."
    mike.say "Wha..."
    mike.say "What happened?"
    mike.say "And why do I have a sudden craving for milk?"
    show claire surprised at hshake
    claire.say "Oops!"
    claire.say "Sorry about that, [hero.name]."
    show claire talkative
    claire.say "I suppose I've been getting a little carried away."
    claire.say "Seeing so many of Adam's old friends..."
    claire.say "Well, it's making me all nostalgic."
    scene bg clairehouse kitchen
    show claire a happy
    with fade
    play sound door_close
    "I make a point of nodding as I step into the hallway and Claire closes the door behind me."
    "But the truth is that I'm actually using it as a chance to pull myself back together."
    "Time must have dulled my memories of Claire, or at least that's how it feels."
    "Because right now she looks even more stunning than I remember."
    menu:
        "Keep things respectful":
            mike.say "Yeah, I know what you mean, Claire..."
            mike.say "As soon as I walked up to your place, I was just the same."
            mike.say "And now I'm starting to wonder why I left it so long to come back."
            show claire talkative
            claire.say "Oh, that's so sweet of you!"
            show claire normal
            "I'm doing the best I can to keep my comments neutral and polite."
        "Compliment Claire's appearance":
            mike.say "I don't know about that, Claire..."
            mike.say "My memory must be failing me."
            mike.say "Because I don't remember you being this beautiful!"
            show claire talkative
            claire.say "Oh, my goodness - you actually think so?"
            show claire normal
            "Okay, so maybe that was a little on the nose."
            $ claire.love += 2
    "But at the same time I can't wholly keep from gazing at Claire."
    "She's just so amazingly hot that it's impossible to be totally chaste around her."
    "And what makes things even harder is the fact that I'm sure she kinda knows it too."
    "Because I swear I catch Claire giving me subtle little smiles as we chat."
    show hector angry teaser at center, zoomAt(1, (800, 720)) with easeinright
    show claire embarrassed
    "Hector" "Geez, Claire..." with hpunch
    show hector at startle(0.1, -5)
    show claire disappointed at center, zoomAt(1, (480, 720)) with ease
    "Hector" "Are you gonna stand there gassing with [hero.family_name] all day, or what?"
    show claire bored
    show hector normal
    with dissolve
    "And just like that, the spell is broken and the moment shattered."
    "The delicate sense of reconnection that I felt Claire and I were sharing is ruined."
    "All of the damage done by the appearance of yet another familiar face."
    "And trust me, I could never forget a face like this one!"
    "I always remember Adam's dad being one of those boorish, irritable guys."
    "He was never an oil-painting, even back when we were all kids."
    "But where time seems to have been kind to Claire, it's done a number on her husband."
    if hero.charm >= 75 and hero.fitness >= 75 and hero.knowledge >= 75:

        mike.say "Hello, Hector..."
        mike.say "Long time, no see."
        show hector angry at startle(0.1, -5)
        "Hector" "Hey, where'd you get off calling me by my first name?"
        "Hector" "Aren't you kids supposed to at least call me 'Sir' or something?"
        show hector normal
        "I raise an eyebrow and curl the corner of my mouth as I look Hector up and down."
        "And it's clear to me that he really is one of those sad, frustrated old guys."
        "The world's clearly passed him by, and now he's taking it out on everyone around him."
        mike.say "I think you've been watching too many TV shows from the nineteen fifties, Hector."
        mike.say "And just for the record, I'm not a kid anymore!"
        "Hector looks me up and down, like he's sizing me up."
        "And then he seems to decide that poking me too hard would be a mistake."
        show hector angry at startle(0.1, -5)
        "Hector" "Huh..."
        "Hector" "You sure got bigger, kid..."
        "Hector" "Your mouth more than the rest of you!"
        show hector normal
        $ claire.love += 2
        $ claire.sub += 3
    else:

        mike.say "Hi, Mister Adamson..."
        mike.say "Good to see you again."
        show hector at startle(0.1, -5)
        "Hector" "Oh yeah?"
        "Hector" "Well I don't see what's so good about it!"
        "I do the best I an to keep a smile on my face as Hector pours his bile onto the conversation."
        "All the time being reminded of the fact that he was never a pleasant kind of person to be around."
        "Which makes the fact he's married to such a stunning woman that much harder to believe."
        mike.say "Sorry to ruin your buzz."
        mike.say "I just wanted to say hi before I found Adam."
        "Hector shrugs and vaguely waves a hand in the direction of the living-room."
        show hector at startle(0.1, -5)
        "Hector" "Ah..."
        "Hector" "The two of them are in there."
        "Hector" "Go talk to them and quit bothering me."
    show claire furious at startle(0.1, -5)
    claire.say "Hector, you could at least be polite to [hero.name]."
    claire.say "After all, he is a guest in this house."
    show claire bored
    "I feel a sense of relief as Claire interjects on my behalf."
    "But that soon turns to one of sympathy as Hector responds."
    show hector at startle(0.1, -5)
    "Hector" "Oh yeah?"
    "Hector" "And just who was it paid for this house, Claire?"
    "Hector" "And who's getting the bill for all the food and drink people are hoovering up?"
    "I watch as Claire seems to shrink back from her husband's verbal tirade."
    "And pretty soon she's looking straight down at the ground to avoid his eye."
    show claire annoyed at startle(0.1, -5)
    claire.say "Y...yes, dear..."
    claire.say "I didn't mean to be disrespectful."
    show hector at startle(0.1, -5)
    "Hector" "Ah, whatever..."
    "Hector" "I'm going to get another beer!"
    "Hector storms off, leaving me alone with Claire once more."
    hide hector with easeoutleft
    "And I'm all ready to offer her sympathy, to ask if she wants to talk about what just happened."
    "But then she surprises me by just looking up with a broad smile on her face."
    show claire startle at center, traveling(2, 0.5, (640, 1220))
    claire.say "Come on then, [hero.name]…"
    claire.say "I'm sure you're dying to see Adam again."
    claire.say "And to meet Lily too!"
    show claire happy
    "Much to my amazement, Claire just carries on like nothing is amiss."
    "In a way it's kind of creepy, almost like she's a robot that's been reprogrammed."
    hide claire with easeoutleft
    "And there's no time for me to ask any questions, as she's now walking off to the living-room."
    "I have no choice but to hurry along after her, and there's no chance for me to challenge her."
    "Because a moment later we're surrounded by familiar faces and the sound of conversation."
    "And I can see so many familiar faces that, just for the moment, I forget all about Claire and Hector's marital issues."
    angela.say "Hi there, honey!"
    show angela smile at center, zoomAt(1, (200, 720)) with easeinleft
    "As soon as I hear the sound of my mom's voice, I turn around with a smile on my face."
    show angela happy zorder 99 at center, traveling(2, 2, (600, 1320))
    "Because the sight of her walking towards me really does make me feel like I'm back home."
    show angela smile at center, zoomAt(2, (600, 1320))
    mike.say "Hi, mom!"
    mike.say "It feels so weird being back here."
    mike.say "Like, so much has changed while I was away."
    "My mom nods with enthusiasm, smiling as she surveys the room."
    show angela happy at startle(0.1, -5)
    angela.say "You have no idea how true that is."
    angela.say "But this isn't the time or the place to talk about it."
    angela.say "Not when you should be catching up with Adam."
    show angela smile
    "With that, she nods in the direction of a larger knot of people."
    "And I return the gesture, walking towards them and leaving her behind."
    "I've almost made it all the way over to where Adam's standing in the middle of all those people."
    "But before I can even try to make my presence known, I find someone standing in my way."
    scene bg clairehouse diningroom
    show lily teaser human zorder 1 at center, zoomAt(1, (440, 720))
    with PushMove(1.0, "pushright")
    play sound crowd_theater loop fadein 1
    "Girl" "Hey, handsome..."
    "Girl" "Who does your soul belong to?"
    "I find myself looking straight into the eyes of a girl I never met before."
    show bg clairehouse diningroom at center, zoomAt(1.2, (540, 820))
    show lily teaser at center, zoomAt(1.4, (640, 920))
    with hpunch
    "She's cute and pretty curvy too, a black bob giving her a slightly bratty look."
    show bg clairehouse diningroom at center, traveling(1.2, 1, (540, 720))
    show lily teaser at center, traveling(1.4, 1, (640, 720))
    pause 1
    show bg clairehouse diningroom at center, traveling(1.2, 1, (540, 820))
    show lily teaser at center, traveling(1.4, 1, (640, 920))
    pause 1
    "And she doesn't seem to be too keen on wearing anything too concealing either."
    "All in all, a neat little package that's worthy of some serious attention."
    "But maybe not before I've managed to say hello to one of my oldest friends."
    menu:
        "Flirt with her":
            "Though it does look like I'm going to have to wait my turn over there."
            "So killing a little time talking to someone else couldn't possibly hurt."
            mike.say "My soul?"
            mike.say "Huh...that's a pretty weird line use on a guy!"
            "The girl doesn't seem to be in the least bit thrown by my reaction."
            "In fact, from the look on her face, I could almost believe she's serious."
            show lily teaser at startle(0.1, -5)
            "Girl" "Not where I come from it isn't."
            "Girl" "Especially when it comes to a guy like you."
            "All the time she's saying this, the girl is looking me up and down."
            "Like she's openly and shamelessly checking me out!"
            mike.say "A guy like me?"
            mike.say "What's that supposed to mean?"
            show lily teaser at startle(0.1, -5)
            "Girl" "Oh, you know...a mortal guy."
            "Girl" "One that's from around here."
            "Suddenly it all seems to make sense."
            "The girl must be foreign, used to a whole different set of customs."
            "Hell, English probably isn't her first language too."
            "Which would explain all of the weird stuff she's said."
            mike.say "Okay, okay..."
            mike.say "Let's get the basics dealt with first."
            mike.say "I'm [hero.name], the apparently mortal dude."
            mike.say "And you are?"
        "Try to get to Adam":
            "I do the best I can to give the girl a polite smile."
            "But at the same time I'm also trying to sneak past her."
            mike.say "Erm..."
            mike.say "Maybe to the guy that directed Shoe Wars?"
            mike.say "I really don't know how to answer that question!"
            "The girl looks more than a little non-plussed by my answer."
            "But she still does the best she can to stay in front of me."
            "Stepping in the same direction as me every time I make a move."
            show lily teaser at startle(0.1, -5)
            "Girl" "You're a strange one, even for a mortal!"
            "Girl" "I wonder what my sister would make of you?"
            "By now I'm starting to get a little frustrated."
            "And so I can't help raising my voice a little too."
            mike.say "Look, Miss..."
            mike.say "I'm sorry, I didn't get your name..."
            mike.say "But I'd really like to get to my friend Adam over there."
            mike.say "I need to congratulate him on his getting engaged!"
    show lily teaser at startle(0.1, -5)
    "Girl" "I'm Lily..."
    "Girl" "Daughter of the Devil and Princess of Pandemonium." with hpunch
    "As soon as I hear the girl say that, it stops me in my tracks."
    "No, not the bit about the Devil and being a princess."
    "That's got to be something that I just misheard."
    "It's the name that strikes a chord, as I know that I've heard it somewhere before."
    "Somewhere very recent, in relation to where I am right now and why."
    "Adam" "Lily..."
    "Adam" "You found him!"
    show lily teaser human at center, traveling(1.2, 0.3, (940, 870))
    show adam teaser zorder 5 at center, zoomAt(1.2, (540, 870)) with easeinleft
    "Suddenly, Adam's not in the middle of the other group of people anymore."
    "Instead he's standing right beside Lily, his arm around her shoulder."
    "And from the way she instantly starts to wrap herself around him, I can guess just who she is."
    mike.say "Erm..."
    mike.say "Hey, Adam - it's been a while, huh?"
    show adam teaser normal at startle(0.2, 10)
    "Adam nods happily, looking from me and to Lily, then back again."
    show adam teaser happy at startle(0.1, -5)
    "Adam" "You bet it has, buddy!"
    show adam teaser talkative
    "Adam" "But I should have known that I'd find you talking to Lily here."
    "Adam" "I had a feeling that you two would hit it off the moment you met."
    show adam teaser normal
    "I can't help feeling more than a little embarrassed as Adam gushes in front of me."
    "Because just a few moments ago I was eyeing up the girl that it's now obvious is his fiancée."
    "But luckily for me, Lily doesn't seem to be the least bit interested in calling me out on it."
    "In fact she looks like she's now totally wrapped up in the act of clinging onto Adam."
    mike.say "Yeah, we bumped into each other a few minutes ago."
    mike.say "And I gotta say, Adam..."
    mike.say "She's totally out of this world!"
    "As soon as I add that last compliment, Adam seems to read something into it."
    "Because his eyes narrow and he looks at me with an intensity I wasn't expecting."
    show adam teaser surprised at startle(0.1, -5)
    "Adam" "What's that supposed to mean?"
    "Adam" "Do you know something about where Lily's from?!?"
    show adam teaser stuned
    "Totally taken aback by the sudden change in Adam's mood I hold up my hands."
    "And I even take a step backwards, trying to show him that I mean nothing by it."
    mike.say "Whoa!"
    mike.say "Settle down, man..."
    mike.say "I just meant that she's pretty special, that's all."
    mike.say "I mean, I figured that Lily's not from around here..."
    mike.say "What's the problem - is there an issue with her visa or something?"
    show adam teaser normal
    "Almost as quickly as his demeanour changed, Adam seems to flip back again."
    "Only now he looks genuinely relieved."
    "Even if he is trying to cover it up with nonchalance."
    show adam teaser happy at startle(0.1, -5)
    "Adam" "Oh..."
    "Adam" "Oh yeah..."
    show adam teaser talkative
    "Adam" "Something like that - but let's change the subject, okay?"
    show adam teaser normal
    "Even I can sense when someone's dropping a hint that heavily."
    "And so I'm more than happy to let Adam move the conversation on."
    "Pretty soon we're chatting about what we've been up to since we last met up."
    "Sharing anecdotes and stories that result in everyone bursting into peals of laughter."
    "But more than once I notice that Adam or Lily comes out with something that's a little odd."
    "And when they do, the other one is always there to elbow them in the ribs and explain it away."
    "In the end I just decide to chalk it up to there being something going on behind the scenes."
    "Something that's probably quite heavy, but also none of my business too."
    "And anyway, I get a distracted a moment later when I feel something pinching my butt!"
    mike.say "OUCH!"
    mike.say "What the hell?!?"
    "I spin around on the spot, hoping to catch the culprit in the act."
    "And I'm half expecting to have to chase them down as they flee the scene."
    "But instead, I find that they've decided to stand their ground."
    "Not only that, they're smiling at me too!"
    "Riley" "Ooh..."
    "Riley" "I don't remember that butt being so firm, [hero.name]..."
    "Riley" "Someone's been working out!"
    show riley teaser zorder 10 at center, zoomAt(1.2, (240, 820)) with easeinleft
    "The moment that I see who it was that goosed me on the arse, my mood totally changes."
    "Before I was irritated and more than a little annoyed, but now I'm positively beaming."
    mike.say "Riley?!?"
    mike.say "It's so good to see you!"
    "The cheeky smile on my old friend's face turns into one of genuine delight."
    show adam teaser at center, traveling(1.2, 0.5, (740, 870))
    pause 0.2
    show lily teaser human at center, traveling(1.2, 0.5, (1120, 870))
    pause 0.25
    show riley teaser at center, traveling(2.5, 1.5, (440, 1520))
    "And she runs over to where I'm standing, throwing her arms wide as she does so."
    "I make a point of doing the same thing, pulling her into a tight embrace."
    "But as soon as I feel Riley's body pressing against mine, I realise something else."
    "What I'm feeling isn't just relief at seeing an old friend after so long apart."
    "There's a genuine sensation of arousal building inside of me as I hug Riley."
    "Reminding me of the crush I used to have on her and how I never really got over it."
    show riley teaser at center, traveling(2.0, 1.0, (240, 1280))
    "Even when the hug breaks up, it's not like Riley puts any distance between us."
    "She keeps an arm around my shoulder, reminding me of Adam's intimacy with Lily just now."
    "And more than once I see her looking over at them, almost like she's a little jealous."
    mike.say "So..."
    mike.say "Adam getting married - how weird is that?"
    show riley teaser at startle(0.1, -5)
    "Riley" "Oh yeah, totally weird!"
    "Riley" "Oh, don't get me wrong..."
    "Riley" "I'm really happy for them."
    "Riley" "But it's hard to see one of your oldest friends getting hitched, you know?"
    mike.say "I do, I do..."
    mike.say "It's kind of like you're losing a little piece of them, isn't it?"
    mike.say "Like you'll still see them, but not the whole person you used to know."
    show riley teaser at startle(0.1, -5)
    "Riley" "That's it exactly!"
    "Riley" "Wow, [hero.name]..."
    "Riley" "You just reminded me of how much I miss having you around."
    "Riley" "Somehow you always seem to know just what to say to me."
    "I can't help smiling as Riley compliments me."
    "Because the truth is that I'm feeling the same way about her."
    mike.say "Well, it's not like we can't do something about that, Riley."
    mike.say "I could try to get home a little more often."
    mike.say "Or maybe you could come and stay with me in the city for a few days?"
    show riley teaser at startle(0.1, -5)
    "Riley" "Really?"
    "Riley" "I like the sound of that!"
    "I'm about to start suggesting possible dates to Riley."
    play sfx1 glass_wine
    "But before I can get the words out, there's a tinkling sound."
    play sfx1 glass_wine
    "And almost as one, everyone looks around to see Claire, tapping a knife against her glass."
    scene bg clairehouse kitchen
    show claire a talkative
    with dissolve
    play sfx1 glass_wine
    claire.say "Ahem..."
    claire.say "If I could have your attention please?"
    show claire happy
    "Claire seems to be struggling a little as she tries to make herself heard."
    "That is until Hector starts grunting and tutting at her side."
    show hector normal teaser at center, zoomAt(1, (400, 720)) with easeinleft
    "Hector" "Urgh..."
    "Hector" "Damn it, woman..."
    "Hector" "Have I got to do everything myself?"
    show hector angry at hshake
    show claire embarrassed
    stop sound fadeout 2
    "Hector" "SHUT YOUR DAMN HOLES!"
    show hector normal
    "Hector's bellowing seems to do the trick, as everyone falls silent."
    show claire disappointed with dissolve
    "But I can see that his insensitive words have really affected Claire."
    show claire sad at center, traveling(1, 0.5, (840, 720))
    "Because her voice now sounds weak and faltering."
    show claire talkative at startle(0.1, -5)
    claire.say "Th...thank you, dear..."
    claire.say "I won't take up too much of your time."
    claire.say "I just wanted to propose a toast..."
    claire.say "To Adam, and his lovely partner, Lily!"
    play sound crowd_yeah
    "Everyone raises their glasses and shouts words of congratulations to the happy couple."
    "But I see Riley shaking her head, and I catch her eye, trying to get her to spill the beans."
    scene bg clairehouse diningroom
    show riley teaser at center
    with PushMove(1.0, "pushright")
    mike.say "You don't agree with the toast?"
    show riley teaser at startle(0.1, -5)
    "Riley" "No way, [hero.name]!"
    "Riley" "I just don't know how Claire puts up with that fucking pig of a husband."
    "Riley" "He's always putting her down in front of people like that."
    "Riley" "If I were her, I'd have smothered him with a pillow ages ago!"
    "All I can do is nod my head as Riley shares her take on the situation with me."
    hide riley with easeoutleft
    "Because as drastic as that sounds, I can't help agreeing with her."
    "The toasts and speeches go on for a little while longer."
    "And to be honest, I start to tune them out before they come to an end."
    "Because by now I've reconnected with all the people that I wanted to."
    "So there's nothing more for me to do than hang around and make idle conversation to pass the time."
    "Soon enough, the party starts to wind down naturally, and I sense that it's time to leave."
    show claire at center, zoomAt(1.6, (640, 1020)) with easeinright
    "But as I head for the front-door, I happen to pass Claire in the hallway."
    show claire at startle(0.1, -5)
    claire.say "[hero.name]..."
    claire.say "Are you leaving so soon?"
    claire.say "It feels like you only got here a moment ago."
    "I offer Claire a shrug."
    mike.say "I'd stay longer, Claire..."
    mike.say "But I have to make it all the way back into the city."
    "She nods, as if accepting my excuse at face value."
    "But there's just something in her eyes that makes me pause."
    "Something that makes me feel like I owe it to her to say more."
    menu:
        "Keep things respectful":
            mike.say "But I'd like it not to be so long before we see each other again, Claire."
            mike.say "I really feel like we've reconnected, but there's more to catch up on."
            "The look of eagerness on Claire's face as she hears what I'm saying is plain to see."
            show claire embarrassed
            "And she nods her head quickly, almost like she's afraid someone else might notice."
            show claire a talkative at center, traveling(2, 0.5, (640, 1220))
            claire.say "I'd like that, [hero.name]..."
            claire.say "I'd like it a lot!"
            $ claire.love += 5
        "Offer Claire open support":
            mike.say "Okay, Claire..."
            mike.say "Stop me if you think I'm crossing a line here."
            mike.say "But I don't think you should have to put up with how Hector treats you."
            mike.say "It's demeaning, and it shows that he doesn't respect you at all!"
            show claire shy with dissolve
            "Claire's eyes seem to suddenly flare as she hears what I have to say."
            "And for a moment I think that she's going to agree with me."
            "But then she holds a finger to her lips, urging me to be quiet."
            show claire a at center, traveling(2, 0.5, (640, 1220))
            claire.say "Shhh!"
            claire.say "Please, [hero.name]..."
            claire.say "Don't let him hear you talking like that!"
            $ claire.sub += 3
    show claire happy
    pause 0.5
    scene expression f"bg {game.room}" with fade
    "I nod to Claire as I step out of the door and start to walk down the path to the street."
    "And even though I'm leaving, I have the feeling that it won't be long before I'm coming back again."
    "Certainly that there won't be as long between this as my next visit as there was between it and the last."
    call stop_all_sfx from _call_stop_all_sfx_51
    $ claire.unhide()
    $ claire.flags.clairedelay = TemporaryFlag(True, 2)
    scene bg black with fade
    return

label claire_event_02:
    if claire.love.max < 40:
        $ claire.love.max = 40
    "I'm just kind of pottering around the house, taking care of those little tasks that always seem to get forgotten."
    "And that means that my head is wandering, getting lost in thoughts of more interesting things."
    play sound door_knock
    "So when there's the sound of a knock at the door, it jolts me back to reality with a bit of a bump." with hpunch
    "I wasn't expecting anyone, and none of my housemates told me that they were either, so I have no idea who it could be."
    play sound door_open
    pause 0.2
    scene bg house
    show claire shy at center, zoomAt(1, (640, 720))
    with fade
    "But when I open the front-door, I find myself genuinely taken aback to see a familiar face smiling at me."
    show claire talkative at startle(0.1, -5)
    claire.say "Hi, [hero.name]…"
    claire.say "I'm so glad I managed to catch you in!"
    show claire normal
    "It takes me a couple of seconds to process the fact that Claire is actually standing on my porch right now."
    "Not because I thought I'd never see the mother of my old friend Adam again."
    "But rather because I didn't think it'd ever be this soon, you know?"
    "Oh, and then there's the oddness of seeing her here, rather than back in the neighbourhood I grew up in."
    "I mean, there's no reason that she shouldn't be here, I just never associated her with this part of my life."
    mike.say "Oh..."
    mike.say "Hi, Claire..."
    mike.say "To what do I owe the honour of your presence on my doorstep?"
    show claire happy with dissolve
    "Claire's smile becomes wider than ever as I make a point of greeting her in a friendly manner."
    "Almost like she was worried that I'd be hostile or start grilling her as to why she's here."
    "And before she answers that question, Claire produces what looks like a book from behind her back."
    show claire at startle(0.1, -5)
    claire.say "Well..."
    show claire talkative at center, traveling(2, 0.5, (640, 1220))
    claire.say "I was just passing when I remembered that you left this at our house."
    claire.say "So I thought that I'd stop and see if you were in, you know?"
    claire.say "So that I could return it to you?"
    show claire happy at startle(0.1, -5)
    "Claire holds the book out in front of her, obviously meaning for me to take it."
    "And as I reach out to do so, I can't help shaking my head in confusion."
    mike.say "Huh..."
    mike.say "That's really weird..."
    mike.say "I don't remember bringing a book with me to Adam's engagement party."
    "Taking the book from Claire, I see that it's actually a graphic novel."
    "Or to be more precise, it's a volume of collected comics, one I used to read as a kid."
    "It's old too, and I don't really recognise it at first."
    "At least not as something that I've been reading recently."
    show claire talkative at startle(0.1, -5)
    claire.say "That's because you didn't..."
    claire.say "Bring it to the engagement party, that is..."
    claire.say "No, you left that at our house the last time you came over before you left for college."
    show claire normal
    "All of a sudden I remember where the book is from, that I had it back before I even moved out."
    mike.say "Wait a minute..."
    mike.say "You mean this has been at your place all that time?"
    mike.say "That means I haven't seen it literally in..."
    show claire startle at startle(0.1, -5)
    claire.say "Years?"
    claire.say "Oh yes, it has been gathering dust at my house for a long time!"
    show claire normal
    "I can't help narrowing my eyes at Claire as she explains all of this to me."
    "Because it's all starting to sound pretty weird from where I'm standing."
    mike.say "So let me get this straight..."
    mike.say "You just happened to be passing?"
    show claire talkative at startle(0.1, -5)
    claire.say "Yes."
    show claire normal
    mike.say "And you also just happened to have a comic-book from when I was a teenager on you too?"
    show claire shy with dissolve
    "Claire's smile becomes broader than ever, and I can see that she wants to nod."
    "But then she kind of seems to realise how crazy she's starting to sound."
    "Her smile becomes more than a little pained, and the mask seems to slip."
    show claire dazed at hshake
    claire.say "Okay, maybe I wasn't really passing..."
    claire.say "Maybe it was more like I drove over here specifically."
    claire.say "And maybe seeing you the other day reminded me that we still had your book."
    claire.say "But also maybe I didn't want to leave it years until we saw each other again."
    show claire shy
    "I can see that I've forced Claire onto the backfoot here."
    "That she's struggling to justify her coming out here in the first place."
    "And I can't help remembering just how much I enjoyed catching up with her the other day."
    "So the reality is that I should really be flattered she made the effort on my behalf."
    mike.say "You know what, Claire..."
    mike.say "You're one hundred percent correct."
    mike.say "And it'd be rude of me not to ask you to come in for a coffee."
    mike.say "Especially after you went to all the trouble of driving over here."
    "I step aside and gesture for Claire to step into the hallway."
    "And she does so eagerly, a genuine look of delight on her face."
    "Which, of course, is something that only serves to make her look even prettier than usual."
    show claire talkative at startle(0.1, -5)
    claire.say "That's so kind of you, [hero.name]."
    claire.say "I can't stay for too long, as I have some other errands to run."
    claire.say "But a cup of coffee would certainly go down a treat!"
    play sound door_close
    scene bg livingroom
    show claire normal at center, zoomAt(1, (840, 720))
    with fade
    "Once I've closed the door, I show Claire through the house and to the kitchen."
    "I hadn't intended to take her on any kind of tour of the place."
    "But she insists on stopping off along the way more than once."
    "Making comments and offering opinions on the décor, furniture and various other things."
    show claire startle at startle(0.1, -5)
    claire.say "Oh, very modern!"
    claire.say "I'd like to do something like that with the sitting-room."
    claire.say "But you know my Hector - he'd only moan and complain!"
    hide claire with easeoutright
    scene bg kitchen
    show bg kitchen at center, zoomAt(1, (640, 720))
    show claire pleased at center, zoomAt(1, (440, 720))
    with PushMove(1.0, "pushleft")
    play sound coffee
    "Once we're in the kitchen, I put coffee in the machine and grab two cups."
    "All the time I'm making the drinks, Claire makes a point of staring at me."
    "Smiling as if I'm performing some kind of impressive feat for her benefit."
    stop sound fadeout 1
    mike.say "Okay..."
    mike.say "There you go, Claire."
    mike.say "There's milk and sugar on the counter, if you want any."
    "Claire takes the cup from me and inhales deeply."
    show claire talkative at startle(0.1, -5)
    claire.say "Mmm…"
    claire.say "That's some good joe!"
    claire.say "I should have known a cool dude like you would have a hippy coffee machine."
    show claire wink
    pause 0.2
    show claire normal with dissolve
    "I think that Claire's trying to sound like she's speaking my language."
    "Or at least what she thinks my language would sound like."
    "But what she's coming out with is so awkward that I can't help laughing."
    show claire shy blush with dissolve
    "And the moment I do so, she blushes from the embarrassment."
    show claire dazed at startle(0.1, -5)
    claire.say "Oh dear..."
    claire.say "That's not what the kids are saying at all, is it?"
    claire.say "I'm sorry, [hero.name], but I don't get out much."
    show claire pleased -blush with dissolve
    "I wave a hand to dismiss Claire's apology."
    mike.say "Don't apologise, Claire..."
    mike.say "And don't take this the wrong way - but that was kind of cute!"
    show claire surprised
    claire.say "REALLY?!?"
    show claire pleased with dissolve
    "Claire's eyes go wide at the compliment, and she takes a sip of her coffee."
    "Though I get the impression that's more to hide her reaction than out of thirst."
    show claire startle at center, traveling(1, 1, (840, 720))
    claire.say "So..."
    show claire startle at center, traveling(1, 2, (640, 720))
    claire.say "Do you have this whole place to yourself?"
    show claire normal
    "Claire asks the question as soon as she seems to have recovered from my compliment."
    "And I see her looking around the room, like she's sizing the place up."
    mike.say "What?"
    mike.say "On my salary?!?"
    mike.say "Oh no, I share it with a couple of housemates."
    show claire startle
    claire.say "I see, I see..."
    show claire at startle(0.1, -5)
    claire.say "Would those be boys, or girls?"
    show claire normal
    "The question strikes me as a little more personal than I'd normally be comfortable with."
    "But I get the impression that Claire thinks she's cleverly pumping me for information."
    "And I have to admit that I like being the centre of her attention too."
    "So I decide to play along and see where this is headed."
    mike.say "Oh, I've had a mixture of guys and girls in the past."
    mike.say "But right now I'm sharing with a couple of girls."
    show claire sad at startle(0.2, 10)
    "Claire makes a point of nodding, as if she's just taking it all in."
    "But for some reason I can see that she's not too keen on that last detail."
    "And if I were a more egotistical kind of guy, I might even think she was a little jealous."
    show claire talkative at startle(0.1, -5)
    claire.say "That's nice, [hero.name]…"
    show claire at center, traveling(1.2, 1, (640, 820))
    claire.say "I bet they really like having a big, handsome man around the place."
    show claire at center, traveling(1.4, 1, (640, 920))
    claire.say "I know that's something I'd like to have!"
    show claire shy
    "Claire says this as she's looking me straight in the eye."
    "And there's an odd twinkle in her eye as she compliments me too."
    "So much so that now it's my turn to blush a little."
    mike.say "Big?"
    mike.say "Handsome?"
    show claire pleased
    mike.say "Me?!?"
    show claire happy
    "Claire seems to be enjoying the sudden change in our relative positions."
    "Because her smile is back, and it's more warm and beautiful than ever."
    show claire talkative at startle(0.1, -5)
    claire.say "Oh, now don't be so silly, [hero.name]!"
    claire.say "I've known you since you were a little boy."
    claire.say "And you've grown into a fine, handsome young man."
    show claire normal
    mike.say "Okay, okay..."
    mike.say "I think I can handle you thinking I'm handsome, Claire!"
    mike.say "But you already have a big, strong man in your life, don't you?"
    mike.say "What about Hector?"
    mike.say "He's certainly big!"
    show claire pout
    "The moment I mention Hector's name, I can't help thinking that I've made a mistake."
    "Because in that same moment, Claire's smile vanishes and her brows furrow into a frown."
    "Then she slams her coffee cup down on the counter so hard that I can't help flinching."
    show claire furious at startle(0.1, -5)
    claire.say "He's a big, fat pig - that's what he is!"
    show claire annoyed
    mike.say "Erm..."
    mike.say "Okay, that's obviously a touchy subject - sorry for bringing it up."
    show claire angry
    "Claire shakes her head, obviously embarrassed by her own sudden outburst."
    show claire pained at startle(0.1, -5)
    claire.say "I..."
    claire.say "I'm sorry, [hero.name]…"
    claire.say "I shouldn't be talking about my husband like that - not in front of you."
    show claire sad
    "I can't help feeling an instant and deep sympathy for Claire."
    "Because anyone that knows her also probably knows Hector too."
    "And the way she just described him is pretty neat and accurate."
    mike.say "It's okay, Claire, really..."
    "I realise that I'm taking a big risk doing it, but I reach out my hand."
    show bg kitchen at center, traveling(1.1, 1, (640, 770))
    show claire at center, traveling(2, 1, (640, 1220))
    "Then I gently place it atop Claire's on the counter, trying to show support."
    "And much to my relief, not to mention delight, she twines her fingers with mine."
    mike.say "You can talk to me about anything that you need to."
    mike.say "Because I feel like you're not just one of my friends mom's..."
    mike.say "I feel like we're friends too, yeah?"
    show claire shy at startle(0.2, -10)
    "Claire nods and gives my hand a reassuring squeeze."
    show claire talkative at startle(0.1, -5)
    claire.say "Of course we are!"
    claire.say "And you've been around Hector for a long time, haven't you?"
    claire.say "So you know exactly what he can be like, don't you?"
    show claire shy
    "I make a point of nodding, rather than saying anything out loud."
    "Because I get the feeling that Claire really needs to get this out."
    show claire mad at startle(0.1, -5)
    claire.say "It's not just that he has a short fuse and a bad temper either."
    claire.say "In a way the things he says and does when he's calm are worse."
    show claire pained
    claire.say "The way he constantly criticises me and undermines me - humiliates me in front of people!"
    show claire sad at hshake
    "By now Claire's voice is trembling as she recounts her husband's behaviour."
    "And I can remember seeing all of this stuff happen back when I was a kid too."
    "But then it wasn't something that I could have said or done anything about."
    "Not like now - now I can really tell Claire what I think of her asshole spouse."
    "And I can offer her advice too, tell her what I believe she should do about it."
    menu:
        "Offer Claire empathy and understanding":
            "But it seems most obvious to me that what Claire really needs right now is a friend."
            "One that's prepared to listen to her without judgement and offer support."
            mike.say "Well you're not going to get any of that here, Claire..."
            mike.say "Because you've got a friend in me, and I'm here whenever you need me."
            mike.say "You can tell me anything, and I'll keep it in the strictest confidence."
            mike.say "And I'll give you my mobile number so that you can call me, okay?"
            mike.say "Come over here for a coffee whenever you feel the need - or we can meet somewhere else, if you like."
            "Claire's watching me closely the whole time that I'm talking."
            "Looking deep into my eyes, as though she's exploring me thoroughly."
            "And all the while I can feel her squeezing my hand tightly."
            show claire whining at startle(0.1, -5)
            claire.say "Oh, [hero.name]…"
            claire.say "It's so kind of you to offer..."
            claire.say "But I'd be imposing on you..."
            show claire sad
            mike.say "No, Claire - I insist."
            mike.say "You were always one of the coolest moms when I was young."
            mike.say "And...well...I really want to get to know you as an adult now."
            show claire sad at center, traveling(2.2, 1, (640, 1320))
            "By now I can feel that Claire's kind of caressing my hand."
            "And she's still looking into my eyes, smiling as she does so."
            "Man...she's so hot!"
            "How did I miss that she was this hot when I was a teenager?!?"
            $ claire.love += 5
        "Take charge and tell Claire what to do":
            "It seems obvious to me that Claire needs a strong man in her life."
            "But the real problem is that, so far, she's chosen the wrong one."
            mike.say "You need to stop apologising, Claire..."
            mike.say "Because I already know that none of this is your fault."
            "I make sure that my tone of voice is confident and commanding as I say all of this."
            "And I can see an almost instant change in Claire's mood as she hears the change too."
            "She seems to sit up straighter and look at me with all of her attention."
            "Almost like my assertiveness is overriding her nerves and anxiety."
            show claire whining
            claire.say "You...you do?"
            show claire startle at startle(0.1, -5)
            claire.say "I...I mean, of course you do!"
            claire.say "You're not like that pig, you're intelligent and sensitive and..."
            show claire shy
            "I can sense that Claire's starting to get overwhelmed by her emotions again."
            "So I put my other hand atop hers too, lifting it up to my face."
            "And then I plant a gentle kiss on the back of it."
            mike.say "Shh..."
            mike.say "What I am is your friend, Claire."
            mike.say "You can tell me anything, and I'll keep it in the strictest confidence."
            mike.say "And I'll give you my mobile number so that you can call me, okay?"
            mike.say "Come over here for a coffee whenever you feel the need - or we can meet somewhere else, if you like."
            "Claire's nodding all the time I'm explaining this to her."
            "Her eyes wide as she stares into mine without looking away."
            "As if she's hanging on my every word."
            $ claire.sub += 3
    show claire startle
    claire.say "Thank you, [hero.name]…"
    claire.say "But I should be getting off, you know?"
    claire.say "My useless husband will be wondering where I've gotten to!"
    hide claire with easeoutleft
    "Claire slips her hand out of mine as she straightens up and prepares to leave."
    scene bg livingroom
    show bg livingroom at center, zoomAt(1, (640, 720))
    show claire bothered at center, zoomAt(1, (440, 720))
    with PushMove(1.0, "pushright")
    mike.say "Huh?"
    mike.say "I thought you said that you had more errands to run?"
    "Claire looks worried for a moment, like she's been caught out."
    "But then she just smiles and shakes her head, as if it's nothing."
    show claire startle at startle(0.1, -5)
    claire.say "Errands, appointments, commitments - what's the difference?"
    claire.say "Anyway, thank you for the coffee and the sympathetic ear."
    claire.say "We should do this again, and soon!"
    show claire normal
    play sound door_open
    "With that, I get the impression that the visit is officially over."
    scene bg house
    show claire c
    with fade
    "So I show Claire back to the front-door and wave as she walks down the path."
    hide claire with dissolve
    "All the time wondering what's happening with her and where this thing between us is really going."
    call stop_all_sfx from _call_stop_all_sfx_52
    $ claire.flags.clairedelay = TemporaryFlag(True, 3)
    scene bg black with fade
    return

label claire_event_03:
    if claire.love.max < 60:
        $ claire.love.max = 60
    play sound cell_vibrate loop
    "I feel my phone vibrating in my pocket, and naturally assume that it's going to be a notification or a text message."
    "But when the vibrating doesn't stop, I realise that it has to be someone actually calling me."
    "And that's something that happens so rarely that I instantly think it's got to be something important, maybe even an emergency."
    "Pulling the phone out of my pocket, I check the screen, expecting to see a call from my folks wanting to tell be about a death in the family."
    "But then I see that the call is from Claire, and that means I have to answer it out of sheer intrigue."
    stop sound
    show screen expression "smartphone_calling" pass ("claire")
    show mike happy at center, zoomAt(2.6, (740, 1820))
    with fade
    mike.say "Hey, Claire..."
    mike.say "What's up?"
    show mike normal
    "There's a pause on the other end of the line before Claire responds."
    "And even when she does, her tone suggests that she's not totally prepared."
    "You know, like she's nervous to be speaking to me or something."
    claire.say "Oh..."
    claire.say "Hi, [hero.name]…"
    claire.say "It's nothing really, nothing crazily important."
    claire.say "I mean, I would have sent you a text message, but I'm clueless when it comes to that kind of thing!"
    claire.say "And you did say that I could call you any time that I needed to, remember?"
    "Okay, I've only been on the phone with Claire for a few seconds, and it already sounds like she's babbling."
    "But she is right when she says that I told her she could call me any time she wanted."
    "So I guess that I only have myself to blame, and I should listen if I really want to be a friend to her."
    show mike happy
    mike.say "Yeah, Claire..."
    mike.say "I guess that I did."
    mike.say "So...was there anything you did want to talk to me about?"
    mike.say "Or are you just wanting to have a general chat?"
    show mike normal
    claire.say "Oh no, I wanted to ask if you're free later?"
    claire.say "And maybe if you'd like to come over for a bite to eat?"
    "Okay, I wasn't expecting Claire to ask me something like that."
    "Especially after we spent time talking about how awful her husband is."
    show mike happy
    mike.say "What's the occasion?"
    show mike normal
    claire.say "Oh, no special occasion - I just wanted to say thank you for the other day."
    claire.say "That little talk we had perked me up to no end, and this is my way of returning the favour."
    "So my instinct is to say no, because I don't want to lay eyes on Hector, let alone have a meal with him."
    "But if I really want to be a friend to Claire, I guess this is the kind of sacrifice it's going to take."
    show mike happy
    mike.say "Okay, Claire..."
    mike.say "I'll be there as soon as I can."
    mike.say "You want me to bring anything?"
    show mike normal
    claire.say "Oh no - just yourself!"
    hide screen smartphone_calling
    hide mike
    with fade
    "Claire chuckles as she ends the call, leaving me shaking my head."
    "And I'm still thinking about the oddness of the conversation as I head over there."
    show bg clairehouse house at dark with timelaps
    play ambience rainfall loop
    "Walking up the path to Claire's front door, I feel the first drops of rain beginning to fall."
    "And so I run the last few steps up to the door and knock frantically, hoping to avoid getting drenched."
    "To my surprise, the door swings open almost as soon as I start knocking and so I dart inside."
    play sound door_open
    scene bg door double at center, dark, zoomAt(1.8, (640, 1020))
    with fade


    show claire b date talkative at center, zoomAt(1.4, (640, 920))
    claire.say "There you are, [hero.name]!"
    show bg door double at center, traveling(1.8, 1, (640, 820))
    show claire a at center, traveling(1.4, 1, (640, 720))
    claire.say "I'm so glad that you could make it, because..."
    show bg door double at center, traveling(1.8, 1, (640, 1020))
    show claire evil at center, traveling(1.4, 1, (640, 920))
    "Claire's words peter off as she seems to notice me staring at her."
    show claire startle at startle(0.1, -5)
    claire.say "Erm..."
    claire.say "Is there something wrong?"
    show claire normal
    "Okay, I admit that right now I'm staring at Claire with my mouth hanging open."
    "But that's just because she looks so damn gorgeous in the outfit she has on."
    mike.say "What?"
    mike.say "Oh...oh no..."
    mike.say "You just look...well, you look stunning, Claire!"
    show claire evil
    "Claire puts on a coy smile and shakes her head, waving a hand to dismiss my compliment."
    "The only thing is that the gesture looks more than a little practised to me."
    "Like she knew all too well the effect that her choice of outfit was going to have."
    show claire surprised at startle(0.1, -5)
    claire.say "What?"
    show claire a talkative
    claire.say "This old thing?"
    show claire b happy
    claire.say "It's just something that I threw on at the last minute!"
    scene bg clairehouse kitchen at dark
    show claire c date at flip, center, zoomAt(1.4, (600, 920))
    play sound door_close
    $ renpy.music.set_audio_filter("ambience", af.Lowpass(1440), replace=True)
    with fade
    "Claire closes the door behind me and gestures for me to follow her."
    "And it's only now that I see the house is pretty quiet, the lights turned down low."
    "There's soft music in the air and what looks like...yeah, those are actual candles!"
    mike.say "Are you sure it's okay me being here, Claire?"
    show claire c at flip, center, traveling(1.2, 1, (400, 820))
    mike.say "Looks and sounds to me like you're all set for an intimate evening."
    show claire c at flip, center, traveling(1.0, 1, (200, 720))
    mike.say "I kinda feel like I'm going to be a third wheel, you know?"
    hide claire with easeoutleft
    pause 0.3
    scene bg clairehouse diningroom
    show bg clairehouse diningroom at center, zoomAt(1, (640, 720))
    show claire a date happy at center, zoomAt(1.2, (320, 820))
    with PushMove(1.0, "pushright")
    "Claire shakes her head as she leads the way into the dining-room."
    "Which I see is similarly cosy, with two places set at the table."
    show claire startle at startle(0.1, -5)
    claire.say "Oh, didn't I already say?"
    claire.say "Hector's out on business, and he won't be back either."
    claire.say "So tonight it's just going to be you and me - a quiet little dinner for two friends."
    show claire talkative
    claire.say "I do hope you're okay with that?"
    show claire happy
    "I know that my head should be filled with alarm bells right now."
    "Because I'm alone in romantic surroundings with another man's wife."
    "And all the signs are that Claire's doing this in order to seduce me."
    "But the problem is that she's just so damn beautiful, I can't say no."
    mike.say "Sure thing, Claire..."
    mike.say "I mean, we all get lonely, right?"
    mike.say "And that's what friends are for."
    "Claire's smile is more than enough to make me forget about all of my misgivings."
    "I offer no resistance as she guides me into one of the seats at the table."
    "And the food on the plates smells so good that Hector might as well not exist at all."
    show claire talkative at startle(0.1, -5)
    claire.say "I know that I wasn't totally honest with you about tonight, [hero.name]…"
    claire.say "And maybe I should have told you that Hector wasn't going to be here..."
    claire.say "But the truth is that I so desperately needed your company, and I was afraid you might not come."
    show claire normal
    mike.say "Meant what I said, Claire - we're friends, and I'll always be there for you."
    "Claire nods."
    show claire startle at startle(0.1, -5)
    claire.say "I know, I know..."
    claire.say "But I've never been able to be honest with anyone, until you came along - not even with myself."
    claire.say "There was always an emptiness inside of me, and I couldn't explain it before Adam and Lily came to visit."
    claire.say "Seeing them so happy together, that made me realise that it was loneliness."
    claire.say "The worst thing of all is that I'm so envious of what they have."
    claire.say "And that makes me feel like a bad person!"
    show claire sad
    show bg clairehouse diningroom at center, traveling(1.2, 1.5, (740, 820))
    show claire at center, traveling(1.6, 1.5, (320, 1020))
    "Without a conscious thought on my part, I reach out with both hands and take Claire's into my own."
    "But this isn't like when she was over at mine for a coffee and I was just trying to show support."
    "Oh no, this time I hold them both and look her straight in the eye, wanting to offer her genuine comfort."
    mike.say "You're not, Claire, not at all!"
    mike.say "You didn't want to spoil Adam's happiness, did you?"
    mike.say "All you wanted was to be as happy as he was with Lily."
    show claire sadsmile at startle(0.3, 10)
    "Claire nods and puts on a smile."
    "But she can't help sniffling a little as she does so."
    show claire sad
    claire.say "Sniff…"
    show claire whining at startle(0.1, -5)
    claire.say "Oh, [hero.name]…"
    claire.say "Let's have a glass of wine, okay?"
    claire.say "That's something that always makes me feel a little better!"
    show claire normal
    "As Claire picks up the wine bottle, I notice the colour of the liquid inside the bottle."
    "And I realise that it's not really the kind that we should be drinking with what we're eating."
    menu:
        "Choose a different wine":
            "That seems to be just one more symptom of the state that Hector's gotten Claire into."
            "Because she'd never have made a silly little mistake like that if she were thinking clearly."
            "No, what she needs more than anything is for someone to step in and take control here."
            "So I reach out as Claire goes to fill my glass, gently taking hold of the bottle."
            mike.say "Wait a second..."
            mike.say "This is white, and we should be drinking red."
            show claire stuned
            "Claire's eyes go wide as I interfere, and for a moment I think she's going to resist."
            show claire normal with dissolve
            "But then she smiles and hands the bottle over to me."
            show claire startle at startle(0.1, -5)
            claire.say "Oh, I see that now..."
            claire.say "How silly of me..."
            show claire talkative
            claire.say "And how lucky you were here to put me right!"
            show claire normal
            "I see that there are more bottles on a side table, and so I fetch an appropriate vintage."
            "Then I pop the cork and pour us both a large glass before sitting back down."
            "Picking up my glass, I hold it out towards Claire."
            mike.say "Shall we have a toast?"
            show claire b happy at startle(0.3, 10)
            "Claire nods as she hurries to pick up her glass too."
            show claire talkative at startle(0.1, -5)
            claire.say "Ooh..."
            claire.say "What shall we drink to?"
            show claire normal
            mike.say "Oh, I don't know..."
            mike.say "Maybe to spending more intimate time with beautiful women?"
            "Claire's eyes go wide and she looks around, as if wondering who I could be talking about."
            show claire surprised at startle(0.1, -5)
            claire.say "You mean...me?!?"
            show claire stuned
            "I shrug and raise my eyebrows."
            show claire normal with dissolve
            mike.say "Do you see any other beautiful women around here?"
            play sound glass_wine
            "Claire hastily taps her glass against mine."
            "Then we both take a drink."
            "And I note that Claire swallows far more of the wine than I do!"
            show claire blush with dissolve
            "So that when she puts down her glass, her cheeks are flushed."
            show claire startle at startle(0.1, -5)
            claire.say "Whoo…"
            claire.say "I think this wine's a little stronger than I expected!"
            claire.say "It's in danger of making me behave in a distinctly un-ladylike manner!"
            show claire wink at startle(0.3, 10)
            show claire normal with dissolve
            "Claire underlines her point with a nod and a wink."
            "Though her tipsiness makes them seem exaggerated and a little clumsy."
            "But if I'm being honest, the wine is starting to affect me too."
            "That and the feeling of intimacy that I sense growing between the two of us."
            mike.say "I certainly hope it does!"
            "Claire starts to giggle like a girl half her age."
            show claire at center, traveling(1.8, 1.5, (320, 1120))
            "And she waves a hand in the air as she leans in closer."
            $ claire.sub += 3
        "Let Claire pour the wine":
            "But then what the hell am I worry about that for?"
            "The important thing is that Claire needs me and I'm here for her."
            "So who cares if we drink the wrong kind of wine?"
            show claire b at startle(0.1, -5)
            claire.say "There you go..."
            claire.say "Shall we have a toast?"
            claire.say "To new friends and being honest?"
            "I raise my glass, showing Claire that I approve."
            mike.say "I'll drink to that!"
            play sound glass_wine
            "We tap our glasses together gently, and then take a drink."
            "And I note that Claire swallows far more of the wine than I do!"
            show claire blush with dissolve
            "So that when she puts down her glass, her cheeks are flushed."
            show claire startle at startle(0.1, -5)
            claire.say "Whoo…"
            claire.say "I think this wine's a little stronger than I expected!"
            claire.say "If I were with any other man, I'd have to be careful."
            show claire wink at startle(0.3, 10)
            show claire normal with dissolve
            "Claire underlines her point with a nod and a wink."
            "Though her tipsiness makes them seem exaggerated and a little clumsy."
            "But if I'm being honest, the wine is starting to affect me too."
            "That and the feeling of intimacy that I sense growing between the two of us."
            mike.say "And what's that supposed to mean?"
            mike.say "You think I'm some kind of saint?"
            mike.say "That I don't see women in that way?"
            "Claire starts to giggle like a girl half her age."
            show claire at center, traveling(1.8, 1.5, (320, 1120))
            "And she waves a hand in the air as she leans in closer."
            show claire talkative
            claire.say "Of course not!"
            claire.say "And here's a confession, the wine loosening my tongue..."
            claire.say "But I kind of hope you see me in THAT way!"
            show claire happy
            $ claire.love += 5
    play sound thunder_single
    play sfx1 thunder_deep
    show bg black as flash zorder 1985:
        alpha 0.5
        matrixcolor InvertMatrix()
    with hpunch
    hide flash
    show bg clairehouse diningroom at dark, dark
    show claire a surprised at dark, hshake, center, zoomAt(1.8, (320, 1120))
    "But before either of us can say or do another thing, there's a sudden rumble that can only be thunder."
    "In the next second, the lights flicker and then go out completely, leaving only the candles to see by."
    show claire stuned at dark, center, traveling(2.8, 0.2, (640, 1670))
    "Claire lets out a squeal of alarm, then leaps out of her seat and straight into my arms."
    "I'm acting on instinct too, and so I can't help pulling her into a closer embrace and holding on tight."
    "Claire's head is on my shoulder, her bosom pretty much pressed onto my chest, legs drawn up into my lap."
    "I can feel her trembling in my arms, making me hold her as close as I can, and I have to admit that I like it."
    "Slowly she raises her head, looking me in the eye by the flickering candlelight."
    show claire startle at dark
    claire.say "Erm..."
    claire.say "That was just thunder and lightning, right?"
    show claire normal at dark
    mike.say "Sounded like it to me."
    show claire talkative at dark
    claire.say "So I shouldn't be scared, should I?"
    show claire normal at dark
    mike.say "Probably not."
    show claire talkative at dark
    claire.say "Damn it..."
    claire.say "That means you're going to have to stop holding me too, doesn't it?"
    show claire normal at dark
    mike.say "Believe me, Claire - I don't like it either."
    mike.say "But I don't think we have a choice!"
    "Claire lets out a sigh and sits up on my knee, unfolding herself as she does so."
    "But before she gets up, we look each other in the eye for a long, lingering moment."
    "Neither of us speaking a word the whole time it lasts, just holding the other's gaze."
    "And when it ends, I can't say how, but I just know that something has changed."
    "Some subtle thing between Claire and me has shifted, just enough to be important."
    "And when I walk out of there and set off home, I know we're never going to be just friends."
    $ claire.love += 10
    $ claire.flags.nokiss = False
    $ claire.flags.nodate = False
    $ claire.flags.clairedelay = TemporaryFlag(True, 2)
    call stop_all_sfx from _call_stop_all_sfx_53
    scene bg black with fade
    return

label claire_event_04:
    if claire.love.max < 80:
        $ claire.love.max = 80
    scene bg mall1 with fade
    "I've popped into the mall for the sake of killing a little time, you know?"
    "Picking up a few things that I need, but that my life doesn't depend upon."
    "And maybe doing a bit of idle window-shopping along the way too."
    "But I've only been wandering around for a couple of minutes when I hear a commotion up ahead."
    "There are raised voices, which wouldn't be too strange for the general hubbub of the mall."
    "The only problem is that I can instantly tell this isn't someone cheering or laughing too loudly."
    "Oh no, this is the voices of a man and a woman, and they're going back and forth at each other."
    "Normally I'd be dead set on avoiding the scene of someone else's domestic argument."
    "And the sound of breaking glass on top of the shouting would be more than enough to make up my mind."
    "But as I get closer, already wondering if I should do a one-eighty, something makes me keep going."
    "And that something is the fact that I could swear the voices are starting to sound familiar."
    "Man" "You dumb, fucking BITCH..."
    "Man" "I'm tired of you showing me up in public!"
    "Woman" "S...stay away..."
    "Woman" "Stay away from me!"
    "Man" "Oh yeah?"
    "Man" "And what are you going to do if I don't?"
    "Woman" "Don't tempt me, Hector..."
    "Woman" "You have no idea what I'm capable of doing!"
    "Man" "Ho, ho..."
    "Man" "You talk big, Claire, real big..."
    "Man" "Maybe I should call your bluff, see what you're really made of?!?"
    "Woman" "You're a fine one to talk, Hector..."
    "Woman" "Your talk's the only thing about you that's big!"
    "Man" "Why you..."
    "Now I'm sure it's Claire and her husband I can hear arguing."
    "So I dash around the corner without thinking."
    "The only thing on my mind is the need to make sure Claire's okay."
    "And I guess I'm pretty lucky that nobody was expecting me to turn up unannounced."
    scene mall2
    show bg mall2 at center, zoomAt(1, (640, 720))
    show hector teaser at center, zoomAt(1, (840, 770))
    show claire disappointed at center, zoomAt(1, (440, 720))
    with fade
    "Because the mere sight of me running towards them seems to stop Hector in his tracks."
    "All the more fortuitous on account of the fact he has his hand raised in the air."
    "Looking like he was just about to deliver a back-handed slap to Claire any second."
    show claire stuned
    mike.say "Stop right there, fat boy!"
    mike.say "Nobody puts their hands on Claire..."
    mike.say "Not while I'm around!"
    "Okay, okay...I know that I must sound like a character in a cheesy eighties action movie."
    "But it was the best that I could come up with in the heat of the moment."
    "And it seems to have the desired effect, because Hector looks totally flummoxed."
    show hector teaser angry at hshake
    "Hector" "What the actual fuck?!?"
    "Hector" "Hey..."
    "Hector" "I know you - you're Angela's punk-ass kid!"
    "I'm doing the best I can to ignore the fact that Hector's always been a big guy."
    "And even though I'm not a skinny teenager anymore, he's still got a good sixty or so pounds on me."
    "But all of my nerves seem to vanish the moment that I happen to glance over and see the look on Claire's face."
    "Seriously, she's gazing at me with what looks like hope mixed with actual hero-worship."
    "So I guess that means she's hoping I'll be her knight in shining armour."
    mike.say "Wrong, Hector..."
    mike.say "I used to be Angela's kid..."
    mike.say "But now I'm the grown man telling you to back off!"
    "I'm doing the best I can to make myself look big and sound confident."
    "But there's always the danger that Hector's going to call my bluff."
    "Though I'm banking on the notion that he's really just a bully."
    "That he's comfortable browbeating someone he knows won't fight back."
    "And that he'll fold before things actually come to a physical fight."
    "Because if he starts something, the worst case scenario is that I get my ass kicked in front of Claire."
    "And the best is that I give her husband a good kicking in front of her, which wouldn't be pleasant either."
    show hector teaser at startle(0.1, -5)
    "Hector" "You'd really fight me over that bitch?"
    "Hector tilts his head towards Claire."
    show bg mall2 at center, traveling(1.2, 1.5, (540, 820))
    show hector at center, traveling(1.6, 1.5, (740, 1120))
    show claire at center, traveling(1.6, 1.5, (40, 1020))
    mike.say "Any time, any place!"
    "Hector shakes his head."
    "Hector" "Then you're dumber than you look, kid..."
    "Hector" "And the pair of you deserve each other!"
    show hector teaser at slide(25, 0.5)
    "I keep my eyes on Hector and my fists clenched as he begins to back off."
    hide hector teaser with easeoutright
    "And I don't stop watching him until he's stormed off and is out of sight."
    "But the moment that happens, I let out a sigh of relief."
    show bg mall2 at center, traveling(1.2, 1.5, (760, 820))
    show claire at center, traveling(1.6, 1.5, (600, 1020))
    "Then I instantly turn my attention to Claire."
    mike.say "Claire, are you okay?"
    mike.say "Did he hurt you at all?"
    "I'm kind of tentatively reaching out towards Claire as I ask her these questions."
    "You know, trying to be all sensitive and supportive, aware of how shaken-up she could be?"
    "But I'm not prepared for her to throw her arms around my neck and drape herself all over me!"
    show claire cry at center, traveling(2.8, 0.2, (640, 1670))
    claire.say "Oh, [hero.name]…"
    show claire whining
    claire.say "I was so worried that he might hurt you."
    claire.say "But you stood up to him, you made him go away!"
    show claire sadsmile
    "I do the best I can to comfort Claire, gently patting her on the back."
    mike.say "Hey, Claire..."
    mike.say "I'm supposed to be the one worrying about you!"
    "I feel Claire take a deep breath, and then let out a sigh of relief of her own."
    "She slowly releases me from what's turned into a pretty tight embrace."
    "And I can see that she's doing the best she can to put on a brave face."
    "But it doesn't take a particularly keen eye to see that she's still shaken-up."
    menu:
        "Continue to comfort Claire":
            "If I were some kind of trained crisis counsellor, maybe I'd be talking Claire through this thing."
            "You know, telling her to control her breathing and focus on the sound of my voice?"
            "But the truth is that I'm not, and I'm feeling almost as shaken as she looks right now!"
            "So when the instinct takes me, I just pull Claire back into an embrace all over again."
            "And the moment I do so, I know it was the right decision, as she returns the gesture."
            "Neither of us seems to feel the need to say a word either, we just hold each other."
            "I can't explain where the urge comes from, but it just feels like the natural thing to do."
            "And I can feel Claire's body relaxing as it's pressed close against mine."
            "The same thing happening to me as I sense my fear and panic start to melt away."
            $ claire.love += 5
        "Help Claire to pull herself together":
            "My instinct is to just hold Claire close to me until she recovers."
            "But maybe what she really needs at a time like this is a different kind of support?"
            "Maybe she needs something that's not so soft and emotional?"
            "So with that in mind, I take a gentle but firm hold of her upper arms."
            "And I look her straight in the eye."
            mike.say "Okay, Claire..."
            mike.say "You're shaken and your heart is racing right now."
            mike.say "But I want you to concentrate on the sound of my voice."
            mike.say "And I want you to match your breathing to mine, yeah?"
            "Claire's eyes are still pretty wide as I'm saying all of this to her."
            "But I can see that she's listening and trying to do as I say."
            "And with a little patience, my advice begins to pay off too."
            "Her breathing slows as she gets it under control."
            "And soon enough a sense of calm seems to settle over her."
            $ claire.sub += 3
    "By now Claire seems to have recovered enough to take a step back from me."
    "But even as she does so, I note that she still keeps a tight hold on my hand."
    "And with the one that's free, she does what she can to wipe away the tears in her eyes."
    show claire whining at startle(0.1, -5)
    claire.say "Thank you, [hero.name]…"
    claire.say "You don't know how much what you just did means to me."
    claire.say "You're more than a friend, way more..."
    claire.say "You make me feel...safe!"
    show claire sadsmile with dissolve
    "Part of me feels like I should be playing down what Claire just said to me."
    "Saying that I was just doing what anyone one would have done in my place."
    "But the truth is that I can hear the genuine emotion in her voice as she says it."
    "And as well as knowing that she's being honest, I feel what it stirs inside of me too."
    "A complex web of emotions that I don't fully understand yet."
    "But that I know are real and are going to affect my relationship with her deeply."
    $ claire.flags.clairedelay = TemporaryFlag(True, 2)
    call stop_all_sfx from _call_stop_all_sfx_54
    scene bg black with fade
    return

label claire_event_05:
    if claire.love.max < 100:
        $ claire.love.max = 100
    "The truth is that after the run-in at the mall with Claire's husband, I'm kind of reluctant to see her again."
    "But at the same time I have a genuine fear of something bad happening to her when I'm not there to save her."
    "And so I find myself in a frustrating state of ambivalence when it comes to Claire and our relationship."
    "On the one hand I hate the messiness of it all, and on the other I hate even more being separated from her."
    play sound cell_vibrate loop
    "So when my phone rings and I see that it's Claire calling, I don't know whether to answer or let it ring."
    "Ah, who am I trying to kid?"
    "I have to answer the call and see what Claire's got to say to me."
    stop sound
    show screen expression "smartphone_calling" pass ("claire")
    show mike at center, zoomAt(2.6, (740, 1820))
    with fade
    show mike talkative
    mike.say "Hi, Claire..."
    mike.say "How are you doing?"
    show mike normal
    "There's a slight pause on the other end of the line."
    "Almost as if Claire doesn't quite know what to say to me."
    "And that makes my heart lurch in my chest, as I think that she could be just as conflicted as I am."
    claire.say "H...hi, [hero.name]…"
    claire.say "I wasn't sure that you'd want to talk to me!"
    claire.say "You know, after what happened at the mall?"
    "Even though we're speaking in the phone, I can't help shaking my head."
    show mike talkative
    mike.say "No way, Claire!"
    mike.say "If I'm honest, I've been pretty worried about you."
    mike.say "So it's a relief to hear your voice."
    show mike normal
    claire.say "You have?"
    claire.say "It is?"
    "The change in Claire's voice is impossible to miss as she replies."
    "As if my admission of interest and concern has totally woken her up."
    claire.say "I mean..."
    claire.say "That's very kind of you to say."
    claire.say "I did want to ask if you'd like to maybe come over?"
    claire.say "What happened at the mall was so chaotic..."
    claire.say "I don't feel like I got the chance to really thank you."
    "Oh man, there are times when Claire makes me feel like we're a couple of teenage kids."
    "You know, trying to dress-up inviting each other places with totally innocent motives?"
    "But that doesn't mean that I'm not a total sucker for any invitation that she sends my way."
    show mike talkative
    mike.say "Well, I'm definitely free to come over there."
    mike.say "So long as 'you know who' isn't home?"
    show mike normal
    "I hear Claire stifle a giggle on the other end of the line."
    "Something that makes her seem even more like a mischievous teenager."
    "And, of course, only makes me want to make it over there to be with her all the more."
    claire.say "Don't worry about Hector..."
    claire.say "He's out of town, supposedly on business."
    claire.say "And he won't be back for a LONG time."
    show mike talkative
    mike.say "Then how can I say no?"
    mike.say "I'll be there as soon as I can."
    hide screen smartphone_calling
    "I end the call with Claire and then hurry to make myself a little more presentable."
    scene bg clairehouse house at center, zoomAt(1.4, (640, 820))
    with timelaps
    "Then I make good on my promise, heading over to her place in the suburbs as quickly as I can make it."
    "But even with her word that Hector's out of town, I can't help looking over my shoulder."
    "Because there's always that fear that he's trying to catch us in the act."
    show bg clairehouse house at slide(250, 2.5)
    "So I'm eyeing every tree and bush that he could be hiding behind as I walk up the path."
    scene bg door double at center, zoomAt(1.8, (640, 1020))
    play sound door_open
    with hpunch
    "Which means that I can't help jumping when the door opens before I can knock on it."
    show claire at center, zoomAt(1.6, (640, 1020))
    mike.say "Wha…"
    mike.say "Argh!"
    show claire surprised at startle(0.1, -5)
    claire.say "[hero.name]…"
    claire.say "What's the matter?!?"
    show claire normal
    "I'm tensed and standing there with my fists raised in front of me."
    "But I can't help starting to feel foolish as Claire's standing in the doorway."
    mike.say "Oh..."
    mike.say "Sorry, Claire..."
    mike.say "I guess I'm just a little on edge, that's all."
    "Claire nods, letting me know that she understands."
    "At the same time she stands to one side and gestures for me to come in."
    show claire talkative at startle(0.1, -5)
    claire.say "It's okay, [hero.name]…"
    claire.say "Hector really is working away."
    claire.say "And he won't be coming back for ages, I promise."
    scene bg clairehouse kitchen
    show claire normal at center, zoomAt(1.2, (640, 820))
    with fade
    "I'm nodding as I step into the house, doing the best I can to look confident."
    "But the truth is that I'm still worried Hector could be lying in wait for me."
    mike.say "I know it's stupid of me to be worried."
    mike.say "But I'm not really fond of confrontations, you know?"
    mike.say "Normally I go out of my way to avoid them!"
    show claire talkative at startle(0.1, -5)
    claire.say "And yet when you heard that I was in trouble..."
    claire.say "You came running to save me!"
    show claire pleased
    "Claire says this as she closes the door behind me."
    "And when she turns to face me again, her smile is knowing."
    show claire c at flip, center, traveling(1.2, 1, (400, 820))
    "But rather than saying any more, she instead beckons for me to follow her."
    show claire c at flip, center, traveling(1.0, 1, (150, 720))
    "Claire leads me deeper into the house, walking into the sitting-room."
    hide claire with easeoutleft
    scene bg clairehouse diningroom
    show bg clairehouse diningroom at center, zoomAt(1, (640, 720))
    show claire a happy at center, zoomAt(1.2, (320, 820))
    with PushMove(1.0, "pushright")
    "When we get there I see there's already an open bottle of wine and two glasses."
    "And she doesn't hesitate to fill them without asking if I want one or not."
    "Though I take it and sip from the glass just as silently when Claire offers it to me."
    "Once she's taken a long sip, Claire lets out a sigh and shakes her head."
    show claire talkative at startle(0.1, -5)
    claire.say "Urgh..."
    claire.say "You know I used to think this house was like a castle, a sanctuary from the outside world."
    claire.say "But over time I came to realise that it's more like a prison."
    show claire normal
    "The comment seems to come out of nowhere, and I can't help raising my eyebrows."
    mike.say "You're serious?"
    mike.say "You really see this place as a prison?"
    "Claire nods as she takes another sip of her wine."
    "And I note that she's almost drained the glass already!"
    show claire careless zorder 99 at center, traveling(3, 0.7, (200, 2100))
    show bg black as back zorder 9 with dissolve
    claire.say "Yes, [hero.name], that's exactly what it is!"
    show bg clairehouse adambedroom as son zorder 9 at sepia
    show adam teaser zorder 19 at right, sepia
    with moveinleft
    claire.say "I've spent so many years here being a wife and a mother."
    claire.say "So long that everyone I know has forgotten who I really am."
    hide son
    hide adam teaser
    with moveoutright
    show claire mad
    show bg clairehouse kitchen as husband zorder 9 at sepia
    show hector teaser zorder 19 at right, sepia
    with moveinleft
    claire.say "They see me as one or the other, and that's all."
    hide hector teaser
    hide husband
    with moveoutright
    show claire careless
    show bg clairehouse house as house zorder 9 at sepia
    claire.say "I've worked so hard at it and given so much of myself that I've let my life become a prison too."
    scene bg black with dissolve
    show bg clairehouse diningroom
    show claire normal
    with dissolve
    "I'm listening to all that Claire has to say, letting her get it."
    "Because I can tell that she really needs to have someone hear her."
    "And I can feel myself beginning to understand just how isolated and lonely she is."
    mike.say "For what it's worth, Claire..."
    mike.say "I don't see you as a wife or a mother."
    mike.say "I'd like to think I look at you and see a friend."
    "Claire nods as I try to explain how I feel about her."
    show claire talkative at startle(0.1, -5)
    claire.say "Oh, I know that, I really do!"
    claire.say "In fact, you're the reason I'm saying all of this out loud for the first time."
    claire.say "It's only since you and I started to get close that I realised I was trapped."
    claire.say "That I was a prisoner of my own fear!"
    show claire sadsmile
    "Claire's looking down at her wine glass as she says all of this."
    "But once she's done, she looks straight up and into my eyes."
    "And in that instant I can almost feel the intensity of her emotions."
    "It's like she's waiting for me to say something in response."
    "Something that I get the feeling is going to steer where our relationship goes from here!"
    menu:
        "'I want to be more than just your friend, Claire'":
            "I know that I don't want to be anything like Hector was to Claire."
            "That I've come to cherish the way that we were friends before anything else."
            "And while I hope that we can soon become far more than that..."
            "I still want Claire and I to be equals in whatever we do become."
            mike.say "Just say that we can be together, Claire..."
            mike.say "Tell me that and I'll do all I can to make sure you're never afraid again."
            mike.say "Because I want to be more than just your friend..."
            mike.say "And I think you feel the same way about me too."
            "Claire now looks like she's hanging on my every word."
            "Nodding eagerly as I try to express myself to her."
            show claire talkative
            claire.say "Oh, [hero.name]…"
            claire.say "I've been waiting so long to hear you say that!"
            claire.say "And I do...I do feel the same way!"
            $ claire.love += 5
        "Tell her how it's going to be":
            "I can see that Claire's putting herself in my hands right now."
            "Looking to me for the strength she needs to break out."
            "To be able to escape the prison she's made for herself."
            "And so I reach out with one hand, gently cupping her chin."
            "As soon as I do so, Claire's eyes dart away, avoiding mine."
            mike.say "Claire..."
            mike.say "I know what you need, better than you do yourself."
            mike.say "And I need you to look me in the eye and admit it."
            mike.say "To admit that you want me to take control."
            "Claire's eyes slowly turn until they're looking in my direction."
            "And I can see that her pupils are massive circles of black."
            show claire talkative
            claire.say "I..."
            claire.say "I can't deny it, not any longer."
            claire.say "I want to be yours, [hero.name]…"
            claire.say "I want you to make me yours!"
            $ claire.sub += 3
    show claire kiss at center with fade
    "Without a conscious thought for the consequences, I throw my arms around Claire."
    "And then I pull her into a tight embrace, kissing her with a sudden, reckless passion."
    "She returns the gesture with just as much enthusiasm too, holding onto me and refusing to let go."
    "All of the caution and restraint that came before seems to vanish in that moment."
    "And I can almost feel things shifting between the two of us, changing irrevocably."
    "Because when this kiss is finally over, Claire and I won't be friends any longer."
    "Instead we'll be lovers, two people united by the love we feel for each other."
    "And there are going to be serious consequences that come along with all of that too."
    "But at least for now, the kiss and the embrace are more than enough."
    $ claire.love +=10
    $ claire.flags.clairedelay = TemporaryFlag(True, 2)
    call stop_all_sfx from _call_stop_all_sfx_55
    scene bg black with fade
    $ game.room = "street"
    return

label claire_event_06:
    if claire.love.max < 120:
        $ claire.love.max = 120
    scene expression f"bg {game.room}" with fade
    "At first it seemed to me like there were two really cool things happening in my life at the same time."
    "On the one hand, Adam getting engaged to that really hot girl called Lily meant they had the engagement party."
    "So I got to reconnect with one of my oldest friends and feel like we were making up for all that lost time."
    "And on the other, perhaps a little more guiltily, it got me back in touch with Claire too."
    "Rekindling another relationship I'd thought was long since dead and buried."
    "And in the case of this one, taking it in a direction that I'd never before dared to think was even possible."
    "Though maybe it's a measure of how truly dumb I am that I didn't think for a second that the two were connected."
    "I'd been trying to deal with all the stuff related to Claire and her shit of a husband on the one hand."
    "All the while imagining that I could reconnect with her stepson on the other and neither would affect the other."
    play sound cell_vibrate
    "So when the messages from Adam start to pop up on my phone, I just assume he's wanting to keep things going."
    "That he's texting me with ideas on a time and a place that we can meet up and chat about the good old days of our youth."
    $ nvl_mode = "phone"
    nvl clear
    adam_nvl "Hey, [hero.name]…"
    adam_nvl "This is gonna sound weird..."
    adam_nvl "But why are you hanging out with my stepmom?"
    "As soon as I read the message, my face falls."
    "And then my stomach starts to churn as I realise the game's up."
    "Adam's no moron, so he's bound to have noticed something going on at home."
    "Either Claire's let an incriminating detail slip into a conversation."
    "Or else Hector's been telling his son all about his suspicions."
    "Whatever the case, I need to get my story straight before I respond."
    "And so I don't answer the message straight away, as I rack my brains."
    "Wanting to be sure that I can satisfy Adam's curiosity when I do respond."
    "As well as keeping what's going on between Claire and me under wraps too."
    play sound cell_vibrate
    "But it seems that Adam's not going to let up, as my phone soon vibrates again."
    adam_nvl "Still waiting for an answer, bro..."
    adam_nvl "And I see you read the first message too..."
    adam_nvl "So you keeping quiet is starting to look pretty sus!"
    "I stop walking to ponder the position that Adam's trying to manoeuvre me into here."
    "Because surely I can come up with some kind of bullshit to get him off my back."
    "Not permanently, you understand?"
    "Just until I know what my story is going to be and I can stick to it."
    "Adam" "See..."
    "Adam" "I told you that I could see you'd read it!"
    "I'm so distracted that it takes a moment for me to realise I didn't read that last part."
    "That the screen in front of me hasn't updated and those last words were actually spoken out loud."
    $ nvl_mode = None
    show adam teaser normal
    "But then I look up and see Adam standing in my path, which makes me jump."
    with vpunch
    mike.say "Aargh!"
    show adam teaser surprised at startle(0.1, -5)
    "Adam" "Aargh!"
    show adam teaser stuned
    "As much as I wasn't expecting to see Adam, it seems he wasn't expecting me to jump and yell either."
    "Because he pretty much mirrors my own reaction, letting out a yelp of his own and jumping backwards too."
    mike.say "Fucking hell, Adam..."
    mike.say "Are you trying to give me a heart-attack, or what?"
    mike.say "And why the scream on top of it all?!?"
    show adam teaser happy
    "Adam" "I only screamed because you did!"
    show adam teaser normal
    mike.say "Well who's fault is that?"
    mike.say "You're the one that jumped out on me!"
    "Adam" "Well what choice did you give me?"
    "Adam" "I could see that you were ignoring my texts!"
    "For a moment, all I can do is stare at him in utter amazement."
    "Then I manage to shake my head as my brain begins to work again."
    mike.say "You...you were watching me reading them?"
    mike.say "Seriously, Adam - when did you turn into a stalker?!?"
    mike.say "A normal person would have just shouted or waved or something."
    mike.say "I mean, how did you even know I was walking by here just now?"
    show adam teaser sad
    "As soon as I ask the question, Adam's expression becomes worried."
    "And I can see that he's starting to get evasive too."
    show adam teaser whining
    "Adam" "Erm..."
    "Adam" "Lily helped me to find you."
    "Adam" "She's...good at that kind of thing."
    show adam teaser sadsmile
    "I cross my arms over my chest and raise an eyebrow at this revelation."
    "Sensing my chance to turn the tables on Adam for the first time since the conversation started."
    mike.say "Oh..."
    mike.say "Is that so?"
    mike.say "Is she also good at getting you to send pushy text messages?"
    mike.say "And what about spying on old friends - that one of her talents too?"
    "That last question seems to be the one that finally does it."
    "The one that makes Adam realise how crazy this whole situation actually is."
    "Because he takes a step backwards and holds his hands up in a 'time-out' gesture."
    show adam teaser talkative
    "Adam" "Okay, look..."
    "Adam" "Texting you from over there and then jumping out on you..."
    "Adam" "I admit that was kind of a mad thing do to."
    show adam teaser whining
    "Adam" "But I've been under a lot of stress lately, yeah?"
    "Adam" "And I just need a straight answer from you, man..."
    "Adam" "You and my stepmom...what's going on there?"
    show adam teaser sad
    "I think about trying to play it off or change the subject."
    "But from the look on Adam's face, I can tell he's not going to let it go."
    "So I take a deep breath and give him my answer."
    menu:
        "Tell Adam that I have feelings for Claire":
            mike.say "I'm going to level with you, man..."
            mike.say "Claire and I started out as friends."
            mike.say "But we've become much more than that."
            show adam teaser stuned
            "Adam's eyes go wide as he stares at me in amazement."
            show adam teaser surprised
            "Adam" "No..."
            "Adam" "You mean that..."
            "Adam" "The two of you are..."
            show adam teaser sadsmile
            "Adam makes a vague gesture with his hands."
            "One that looks kind of like someone trying to shove one thing into another."
            mike.say "We're still trying to figure out exactly what we are."
            mike.say "But for convenience, you can say we're an item."
            mike.say "I'm sorry, dude..."
            mike.say "It just kind of...happened."
            mike.say "And for what it's worth, it feels really right."
            show adam teaser upset
            "For a moment, Adam looks like he's about to explode."
            "But then, much to my relief, all the anger seems to drain out of him."
            show adam teaser talkative
            "Adam" "You don't know how long I've been expecting to hear that about Claire."
            "Adam" "I just never expected to be hearing it from you!"
            show adam teaser sadsmile
            "All I can do is shrug."
            mike.say "Like I said, I'm sorry."
            mike.say "I wasn't trying to wreck their marriage or anything."
            mike.say "She needed a shoulder to lean on, and then we realised there was more to it."
            "Adam shakes his head."
            show adam teaser talkative
            "Adam" "Nah, I get it."
            "Adam" "She's a great person, and super-hot too!"
            "Adam" "In a way I'm glad that it's you, and not some total stranger."
            show adam teaser normal
            "I nod and smile, relieved to have everything out in the open."
            mike.say "You want to go grab a coffee and talk about it?"
            show adam teaser talkative
            "Adam" "No, no..."
            "Adam" "I think I just need some space to think."
            "Adam" "You know, some time to myself?"
            show adam teaser normal
            "Before I can say another word, Adam turns on his heel and walks away."
            "And it's yet another relief, as really didn't want to talk about it."
            "I'm just glad that I can tick a potential enemy off the list."
            $ hero.flags.adam_in_confidence = True
        "Tell Adam to mind his own business":
            mike.say "What's going on?"
            mike.say "She needed someone to talk to, that's what's going on."
            mike.say "I kind of thought she might be able to talk to you!"
            "Okay, so I know that's not the whole truth."
            "But it's a significant part of the truth."
            "And it's the root of what's going on between Claire and me."
            show adam teaser whining
            "Adam" "Yeah, yeah..."
            "Adam" "I know that she's lonely."
            "Adam" "And that my dad's an asshole too!"
            show adam teaser upset
            "Adam throws his hands up in exasperation."
            show adam teaser whining
            "Adam" "I just...had my own life to lead, you know?"
            "Adam" "Like, you moved away to the big city too."
            "Adam" "But somehow your folks seem to cope fine."
            "Adam" "I dunno, sometimes it's like your dad's cast a magic spell over them..."
            show adam teaser sad
            "Adam seems to be drifting off as he says this."
            "So I snap my fingers in front of his face to regain his attention."
            show adam teaser stuned
            mike.say "Magic spells?"
            mike.say "What are you talking about?"
            mike.say "Look, man..."
            mike.say "Your stepmom's lonely and your dad's a prick."
            mike.say "All I've done is try to be a friend to her."
            mike.say "If that's too much in your book, then I'm sorry!"
            show adam teaser sadsmile
            "Adam's head sags as he lets out a sigh."
            show adam teaser talkative
            "Adam" "I'm sorry, dude..."
            "Adam" "I guess I was just paranoid, you know?"
            show adam teaser normal
            "I nod and give him a pat on the shoulder."
            mike.say "I know."
            mike.say "Just let me text you back next time, okay?"
            show adam teaser happy
            pause 0.3
            hide adam teaser with easeoutright
            "Adam nods and gives me a smile as he turns to walk away."
            "And I wave as he does so, knowing I've only postponed the inevitable."
            "I just hope that when he finally does find out, I have a better explanation for him."
    $ claire.flags.clairedelay = TemporaryFlag(True, 1)
    call stop_all_sfx from _call_stop_all_sfx_56
    scene bg black with fade
    return

label claire_event_07:
    if claire.love.max < 140:
        $ claire.love.max = 140
    scene bg coffeeshop with fade
    play ambience crowd_theater loop
    "Normally I'd be more than happy to be meeting up with Claire for a coffee."
    "This is usually the stage in a new relationship when you're desperate to be with a girl."
    "That you're taking any opportunity that you can to sit down and find out more about her."
    "But after the run-in that I just had with Adam about my relationship with his stepmom..."
    "Well, you can imagine that I'm feeling more than a little edgy by the time I get to the coffee shop."
    "A feeling that isn't helped by the fact that I scan the place and instantly spot Claire."
    "And it's not because I recognise her from across the room, because of course I do."
    "It's more on account of the headscarf and large pair of sunglasses that she's wearing."
    "All while being sat inside the coffee shop too!"
    "Hurrying over to the table where she's sitting, I slide into the chair across from her."
    show claire
    show claire -idle upset zorder 3 at center, zoomAt(4, (840, 2500))
    show master_glasses zorder 6 at center, zoomAt(4.6, (870, 2880))
    show claire_acc_head_ab_wedding zorder 9 at dark, center, zoomAt(4, (920, 2270))
    with fade
    mike.say "Erm..."
    mike.say "Hey, Claire..."
    mike.say "Is there any particular reason you're trying to draw attention to yourself today?"
    mike.say "Because I'm not paranoid, but everyone in here is looking at you right now!"
    show master_glasses zorder 6 at center, traveling(4.6, 0.7, (870, 2940))
    "Claire pulls down her sunglasses so that she can look at me over the top of them."
    show claire talkative
    claire.say "What are you talking about, [hero.name]?"
    show claire pissed
    claire.say "Can't you see that I've come in disguise?"
    show claire wink
    pause 0.2
    show claire talkative with dissolve
    claire.say "It's really important that I'm not recognised!"
    show claire normal
    show master_glasses zorder 6 at center, traveling(4.6, 0.7, (870, 2880))
    mike.say "Claire, that disguise is not working..."
    mike.say "Unless you think you're hiding out in a movie from the nineteen fifties?"
    mike.say "And if that's the case, we've got bigger problems than some one recognising you!"
    "For a moment I think that Claire's going to argue her case."
    show claire bored casual zorder 3 at center, zoomAt(4, (840, 2500))
    hide master_glasses
    hide claire_acc_head_ab_wedding
    with Pixellate(1.0, 5)
    "But then she lets out a sigh, pulls off the sunglasses and unties the headscarf."
    show claire whining
    claire.say "Sorry, sorry..."
    claire.say "I suppose that I am getting a little carried away."
    show claire annoyed
    claire.say "But it's not like I don't have good reason to be paranoid!"
    show claire upset
    "Claire can't seem to help raising her voice as she says this."
    "Causing more than a few people at the nearby tables to turn their heads in our direction."
    mike.say "Sssh!"
    mike.say "So..."
    mike.say "I take it that you've had a word with Adam recently?"
    "Claire nods and leans in closer before answering me."
    "As if now she's suddenly concerned with being overheard."
    show claire whining
    claire.say "Yes..."
    claire.say "Yes I have!"
    claire.say "Whatever did you tell him?"
    show claire upset
    if hero.flags.adam_in_confidence:
        mike.say "I told him the truth, Claire..."
        mike.say "Because even if I didn't, he's have figured it out in the end."
    else:
        mike.say "Well I certainly didn't tell him we were an item."
        mike.say "But he'll probably figure that out on his own soon enough."
    "Claire waves a hand in the air, dismissing my concerns."
    show claire furious
    claire.say "Well, I'm sure that's right..."
    claire.say "But it's not Adam that I'm worried about."
    show claire upset
    "I can't help furrowing my brows as I realise that she can only be talking about one person."
    mike.say "Hector?"
    mike.say "Is that why you wanted to meet up?"
    mike.say "Because you're worried about him?"
    "Claire nods, looking around as if she expects her husband to appear out of nowhere."
    "Like he could be hiding around a corner or lurking under one of the nearby tables."
    show claire mad
    claire.say "Of course I am!"
    claire.say "I mean, Hector's always been paranoid about me not being faithful."
    claire.say "He's just that kind of a man, you know?"
    show claire upset
    "Now it's my turn to nod."
    show claire furious
    claire.say "Well now all of those things he used to accuse me of doing..."
    claire.say "I really am doing them - with you!"
    claire.say "And I'm certain that he already suspects us."
    show claire upset
    "I'm making a point of listening to everything that Claire's telling me."
    "And I'm just as concerned about Hector finding out about us as she is."
    "But the problem is that I'm not hearing any actual evidence in what she's saying."
    mike.say "Claire..."
    mike.say "I'm not saying that we shouldn't be careful about things."
    mike.say "But you know better than I do how much of an old windbag Hector is."
    mike.say "I mean, look at what happened when I challenged him at the mall the other day."
    "I can see the strain that my argument is causing Claire."
    "The battle going on inside of her is written all over her face."
    "It's like she wants desperately to believe me, for it to all be okay."
    "But there's just something that won't let her be comforted by my words."
    show claire furious
    claire.say "Oh..."
    claire.say "I know all of that, [hero.name]…"
    claire.say "It's just that...well, I have a bad feeling about it."
    show claire upset
    "I can see that just playing down Claire's worries isn't going to cut it."
    "That, on this occasion, it's going to take something more than that."
    "So I reach out and put my hand atop hers."
    "And as soon as I do so, she looks up, hope flaring in her eyes as they meet mine."
    menu:
        "We can face Hector together":
            "I make sure to hold Claire's eyes as I say what I have to say."
            "As well as squeezing her hand gently as I speak."
            "All the time keeping my voice level and confident."
            mike.say "I'm not worried about what Hector might think or do, Claire."
            mike.say "Because I know that we have something he doesn't."
            mike.say "We have each other, right?"
            show claire talkative
            claire.say "Oh, [hero.name]…"
            claire.say "Of course we do!"
            show claire happy with dissolve
            "I nod and smile, doing all I can to encourage Claire."
            "Tightening the grip that I have on her hand without crushing it."
            mike.say "So long as we stay together..."
            mike.say "So long as we support each other..."
            mike.say "I just know that he'll be no match for us!"
            "Claire's nodding too by now."
            "Holding my hand as if her life depends on it."
            show claire talkative
            claire.say "You got it!"
            show claire normal
            $ claire.love += 6
        "I promise I can handle Hector myself":
            "I make sure that I have a confident expression on my face."
            "And that my voice is as masculine and deep as I can make it."
            "At least without making myself sound ridiculous."
            mike.say "There's nothing for you to worry about, Claire..."
            mike.say "I'll be the one to handle Hector, come what may."
            mike.say "Just leave all the details to me and forget about it."
            show claire whining
            claire.say "But, [hero.name]…"
            claire.say "What if..."
            show claire upset
            "I press a finger to Claire's lips, pressing them together and silencing her."
            mike.say "Uh, uh, uh..."
            mike.say "No more questions."
            mike.say "Like I already said, just leave it all to me."
            "By now Claire's eyes have kind of glazed over."
            "And she's staring at me with undisguised admiration."
            show claire talkative
            claire.say "If you say so, [hero.name]."
            show claire normal
            $ claire.sub += 3
    "My efforts to reassure Claire seem to have worked out just as I'd hoped they would."
    "Because the worry has now vanished from her eyes and she seems to be hanging on my every word."
    "But as I make to get up and order us some fresh coffee, a little of it creeps back into her expression."
    show claire furious
    claire.say "I believe you, [hero.name]…"
    claire.say "I'm sure that we'll get through this."
    claire.say "But I still think that Hector's onto us."
    claire.say "And I'm still sure that he might do something desperate."
    show claire upset
    "I nod, being sure not to let my confidence slip, even for a moment."
    "And I make a mental note of everything that Claire's telling me."
    "Storing the information away for a time when it might come in handy."
    $ claire.flags.clairedelay = TemporaryFlag(True, 2)
    call stop_all_sfx from _call_stop_all_sfx_57
    scene bg black with dissolve
    return

label claire_event_08:
    if claire.love.max < 160:
        $ claire.love.max = 160
    scene expression f"bg {game.room}" with fade
    "Even though I left Claire with multiple assurances that there was nothing to worry about, I'm still on high alert."
    "Almost every time that my phone vibrates, I grab for it with a genuine terror beginning to clutch at my heart."
    "One that's only staved off when I see that the message I've received isn't from her and has nothing to do with Hector."
    "And when I get a text that's from an unknown number, I get ready to feel that little surge of relief once more."
    "That is until I see the first line of the actual message itself, and then my anxiety really does begin to spike."
    $ nvl_mode = "phone"
    nvl clear
    unknown_nvl "[hero.name], it's me, Claire..."
    unknown_nvl "You have to come quickly..."
    unknown_nvl "I need your help, right now!"
    "I stare at the message on the screen, as if doing so is going to answer any of the myriad questions running around inside my head."
    "But, of course, the text just remains right there on the screen once I've read it, offering no more clues whatsoever."
    "In fact I must have been staring at it for longer than I thought, as the typing icon appears at the bottom of the message."
    "And in a few seconds more, another message appears beneath the first."
    unknown_nvl "[hero.name], are you there?!?"
    unknown_nvl "I'm in serious danger here!"
    "Okay, now I feel like I've had a fire lit under my ass."
    "And I leap into action, typing a response as quickly as I can manage."
    mike_nvl "Okay, okay..."
    mike_nvl "How do I know this is really you, Claire?"
    mike_nvl "Like, how do I know it's not your fat bastard of a husband using your phone?"
    "There's a short pause before the typing icon reappears."
    "And I reflect that if it is Hector on the other end of the line, I probably just made him hopping mad with that little insult."
    unknown_nvl "Of course it's me!"
    unknown_nvl "I got myself one of those burning phones..."
    unknown_nvl "You know, so that Hector wouldn't know about it?"
    "Now I'm starting to get more sure that this is Claire I'm messaging."
    "Only someone of her generation would call a 'burner phone' a 'burning phone'."
    "Though I can't help wondering why she never mentioned to me that she had one."
    "It would have made convincing me she was the one messaging far easier if she had done."
    mike_nvl "What's the matter, Claire?"
    mike_nvl "What did that disgusting pig do to you now?"
    "Again there's pause before the answer comes through."
    "As if Claire's struggling to be able to type her response."
    unknown_nvl "He knows, [hero.name]…"
    unknown_nvl "Hector found out about us!"
    unknown_nvl "I think he's coming home right now - to get me!"
    mike_nvl "Don't worry, Claire..."
    mike_nvl "I'll be there as soon as I can!"
    $ nvl_mode = None
    "Shoving my phone into my pocket, I make good on my promise."
    "And then I drop everything to hot-foot it over to Claire's place."
    scene bg clairehouse house with timelaps
    "Arriving breathless and with my mind in a state of utter disarray."
    show bg clairehouse house at center, zoomAt(1, (640, 720))
    show bg clairehouse house at center, traveling(1.4, 1.7, (440, 820))
    "I head straight up the path towards the front-door, looking this way and that."
    "Suddenly aware that I have no idea if she's in the house or the garden."
    "Hell, I don't even know what state I'm going to find her in either!"
    mike.say "CLAIRE?"
    mike.say "Claire, where are you?"
    "Hector" "Hah!"
    "Hector" "I knew it..."
    "Hector" "I just knew you'd take the bait!"
    "I feel a sinking sensation in the pit of my stomach at the sound of that voice behind me."
    "But all the same I make a point of stopping in my tracks and turning around slowly."
    "Unconsciously clenching my hands into fists as I do so, ready for the confrontation ahead."
    "Of course it's Hector, stepping out of the bushes and onto the path behind me."
    "His normally sour expression has been replaced with one of utter rage."
    "And I can see that he's clenched his hands into fists as well."
    "Though from where I'm standing, they look far bigger and meatier than mine."
    show hector teaser angry zorder 5 at center, zoomAt(1, (740, 720)) with easeinright
    mike.say "Hector..."
    mike.say "Just calm down, yeah?"
    mike.say "Take a deep breath and let's talk about this."
    "I'm not seriously expecting my pleas to work on Hector, not really."
    "But I feel like I at least have to try to be reasonable and talk to him."
    "Even if it's a wasted effort and he tries to charge at me in the next few seconds."
    "Hector" "Calm down?" with hpunch
    "Hector" "Talk?!?" with hpunch
    show hector teaser angry at center, traveling(1.4, 2, (740, 970))
    "Hector" "Urgh...that's what I hate most about your fucking generation."
    "Hector's bellowing his words by now, spitting them out in quick succession."
    "His face is already as red as a tomato and getting darker by the second."
    "And I swear that I can actually see the veins starting to stand out on his bald head."
    "Hector" "You'll come into my home, eat my food and drink my booze, no problem."
    "Hector" "You'll smile to my face while you're jumping into bed with my damn wife."
    "Hector" "But as soon as I stand the fuck up to you, all you want to do is talk!"
    "Hector lunges at me as he spits the last few words out, a meaty fist arcing through the air."
    "Luckily for me, he's about as slow and cumbersome as he looks, missing me by a good margin."
    "So it's no problem for me to leap backwards and avoid the blow, making him stumble forwards."
    "Hector" "Urgh..." with hpunch
    "Hector" "Stay still, you little shit..."
    "Hector" "Stand there and fight me like a man!"
    "The only thing that manages to hit me is a couple of droplets of sweat."
    "Ones that were flung from Hector's forehead and he span around just now."
    "And as disgusting as that is, I note that he's really perspiring like crazy."
    show claire surprised zorder 1 at center, zoomAt(1, (140, 720)) with easeinleft
    claire.say "[hero.name]!"
    claire.say "Hector!"
    claire.say "What are you two doing?!?"
    show bg clairehouse house at center, traveling(1.4, 0.3, (840, 820))
    show hector angry teaser at center, traveling(1.4, 0.3, (1140, 970))
    show claire surprised at center, traveling(1, 0.3, (540, 720))
    "At the sound of Claire's voice, I can't help turning my head in her direction."
    show claire surprised at center, traveling(1.4, 1, (540, 920))
    "And I just about have time to make out that she's running down the path towards us."
    show hector teaser angry at center, traveling(2, 0.5, (840, 1370))
    play sound woosh_punch
    queue sound punch_hard
    pause 0.5
    scene bg blank with vpunch
    pause 0.5
    scene bg black with dissolve
    "That is before I feel a sudden and very painful impact on the side of my jaw."
    "Hector using the distraction of Claire's arrival to sucker-punch me."
    scene bg clairehouse house
    show bg clairehouse house at center, zoomAt(1.4, (440, 820))
    show hector teaser angry zorder 5 at center, zoomAt(1.4, (740, 970))
    show claire mad zorder 1 at left
    with Pixellate(1.0, 5)
    mike.say "Argh!"
    claire.say "Hector, you brute..."
    claire.say "Leave him alone!"
    show claire bored
    show hector at hshake
    "Hector" "Ah, shut your yap, Claire."
    "Hector" "I'm just taking out the trash."
    "Hector" "And once I'm done with him, you're next!"
    "Until now I've been able to contain my anger towards Hector."
    "To keep a hold of my temper for fear of inadvertently harming Claire."
    "But the moment I hear him make a threat aimed at her..."
    "Well, every ounce or restraint drains away in the blink of an eye."
    mike.say "Don't you touch her..."
    mike.say "You fat fuck!"
    "I don't know where the punch comes from, as it's definitely not planned."
    play sound woosh_kick
    queue sound punch_hard
    pause 0.5
    show hector at hshake
    pause 0.3
    show hector at center, traveling(1, 0.5, (740, 720))
    "All I know is that my right fist flies through the air and connects."
    "Then it's Hector's turn to groan and stagger backwards."
    show hector
    "Hector" "FUCK!"
    "Hector" "Now that's more like it!"
    "Hector" "Now I've really got an excuse to end you."
    "Without any further warning, Hector launches himself at me."
    play sound woosh_kick
    queue sound round_one
    show hector angry at center, traveling(1.4, 0.3, (740, 970))
    pause 0.1
    show bg clairehouse house at center, zoomAt(1, (440, 820)), sepia, blur(10)
    show claire stuned -idle at blur(5)
    with dissolve
    "And I only have a fraction of a second to decide what I'm going to do about it."
    show hector teaser angry at center, traveling(2, 10, (740, 1370))
    menu:
        "Try to fend off Hector":
            "Luckily for me, Hector seems to need me to be distracted to land a decent blow."
            scene bg clairehouse house at center, zoomAt(1.4, (440, 820))
            show hector teaser angry zorder 5 at center, zoomAt(2, (740, 1370))
            show claire stuned zorder 1 at center, zoomAt(1, (320, 720))
            with fade
            "Because the moment that all of my attention is focussed on him, he swings and misses."
            play sound woosh_punch
            show bg clairehouse house at center, traveling(1.4, 0.2, (400, 820))
            show hector teaser angry at center, traveling(2, 0.2, (440, 1370))
            show claire stuned at center, traveling(1, 0.2, (300, 720))
            "Lumbering after me as I make light work of dodging out of the way of his fists."
            play sound woosh_punch
            show bg clairehouse house at center, traveling(1.4, 0.2, (480, 820))
            show hector teaser angry at center, traveling(2, 0.2, (1040, 1370))
            show claire stuned at center, traveling(1, 0.2, (340, 720))
            "Puffing and blowing, he still keeps coming after me, trying to follow up that one lucky punch."
            mike.say "Give it up, Hector..."
            mike.say "You're just making a fool of yourself."
            show hector teaser sweat vapor
            "Hector" "Hunff…"
            "Hector" "Gurnph…"
            "Hector" "I'm gonna...fix you...fucking kid!"
            show claire mad
            claire.say "For god's sake, Hector..."
            claire.say "Stop it before you kill yourself!"
            show claire bored
            "But no matter what Claire and I say, none of it gets through to Hector."
            "As he just keeps on lunging for me and missing, staggering around the whole time."
            $ claire.love += 4
        "Fight !":
            "Luckily for me, Hector can't seem to land a punch once I'm defending myself."
            "But I still feel the best way to handle the situation is to end it as quickly as possible."
            "And the swiftest way to do that would be to knock the fat old bastard out."
            "Or onto his ass, whichever comes first."
            scene bg clairehouse house at center, zoomAt(1.4, (440, 820))
            show hector teaser angry zorder 5 at center, zoomAt(2, (740, 1370))
            show claire stuned zorder 1 at left
            with fade
            "So I raise my own fists and proceed to punch Hector square in the face."
            play sound woosh_kick
            queue sound punch_hard
            pause 0.5
            show hector teaser sweat blush at hshake
            "The blow lands right on his nose, which crumples with a sickening crunch."
            "Hector" "Aargh!"
            "Hector" "My nose...my fucking nose!"
            mike.say "You ready to talk yet, Hector?"
            mike.say "Or do I have to make you even uglier than you already are?"
            show claire mad
            claire.say "For god's sake, Hector..."
            claire.say "Stop it before you kill yourself!"
            show claire bored
            "But no matter what Claire and I say, none of it gets through to Hector."
            "As he just keeps on lunging for me and missing, staggering around the whole time."
            "Blood streaming from his ruined nose and dripping from his chin."
            $ claire.sub += 3
    show hector teaser sweat blush vapor at center, traveling(1.4, 1, (740, 970))
    "By now Hector's face has gone from tomato red to zucchini purple."
    "And I can hear him gasping as he strains to keep on breathing."
    "But none of it seems to have dampened his enthusiasm for the fight."
    "As he raises a fist in the air and prepares to make another swing."
    "Only he never manages to follow through, as his eyes suddenly go wide."
    "At the same time, his other hand clutches desperately at his chest."
    show hector at hshake
    "Hector" "Urgh..."
    show hector at hshake
    "Hector" "F...F...Fuck!"
    show hector at hshake
    show claire upset
    "Claire and I watch in silent horror as Hector staggers forwards a step."
    hide hector with easeoutbottom
    pause 0.25
    play sound body_fall
    show claire stuned
    "Then he collapses onto his knees, still clutching at his own chest."
    "And before either of us can summon the will to move, he falls forwards and onto his face."
    mike.say "Fucking hell!" with hpunch
    mike.say "Is he..."
    mike.say "Is he dead?!?"
    "I can't help being cautious as I edge my way towards where Hector's lying."
    "Keeping my fists up in a defensive posture as I tap him with my foot."
    "Because part of me is still expecting him to be playing possum."
    "That he might pop up any moment to deliver the final, knockout blow."
    "But luckily for him, Claire's brain isn't functioning through the haze of combat."
    show claire at center, zoomAt(1, (320, 720))
    show claire at center, traveling(1.4, 0.7, (540, 1120))
    pause 0.7
    show claire c
    "Which means that she quickly kneels down beside her fallen husband."
    "Checking for a pulse and shaking her head as she looks him over."
    show claire whining
    claire.say "Oh no, he's alive alright."
    claire.say "Looks like it was his damn blood pressure."
    claire.say "The number of times I told him to eat better and get some exercise!"
    claire.say "Come and help me get him into the recovery position, then we'll call an ambulance."
    show claire sad
    "Everything seems to happen in a blur from that moment on."
    "And I can't really remember which one of us it is that calls the ambulance."
    "But by the time the paramedics arrive, there's a crowd of neighbours watching what's going on."
    "Dozens of eyes looking on as Hector's put on a stretcher and loaded into the back of the ambulance."
    scene bg clairehouse house
    show claire at center, zoomAt(1, (640, 720))
    with timelaps
    mike.say "So..."
    mike.say "Do you think he's going to be alright?"
    show claire whining
    claire.say "The paramedics told me he was lucky."
    claire.say "Just a minor stroke, a warning that he needs to sort himself out."
    show claire sad
    mike.say "Yeah..."
    mike.say "Sounds like he's going to have to make some changes."
    show claire whining
    claire.say "He sure is - and not just to his eating habits either!"
    show claire sad
    "I look at Claire in genuine surprise as she sums up Hector's fate."
    "Aware that I'd been deliberately trying to avoid talking about us."
    "You know, about what happens next in terms of our relationship?"
    mike.say "You mean that..."
    show claire whining
    claire.say "I mean it's over, [hero.name]…"
    claire.say "This is the wake-up call I needed."
    claire.say "Tomorrow morning, I'm calling a lawyer."
    claire.say "It's time to get the wheels turning on my divorce!"
    show claire sad
    "I find myself staying quiet as Claire explains what she plans to do next."
    "Obviously I'm thrilled that she's going in that particular direction."
    "But it feels like my saying anything positive would strike the wrong note."
    "That it'd make me look like I was gloating over the death of her marriage."
    "So I decide to keep my thoughts to myself and just offer support where I can."
    "Trusting that Claire already knows how I feel and where my heart lies."
    $ claire.flags.clairedelay = TemporaryFlag(True, 4)
    call stop_all_sfx from _call_stop_all_sfx_58
    scene bg black with dissolve
    return

label claire_event_09:
    if claire.love.max < 200:
        $ claire.love.max = 200
    scene expression f"bg {game.room}" with fade
    "After the confrontation with Hector the other day, Claire's house is the last place that I want to be right now."
    "But on the other end of the scale, I can't deny the fact that her husband, as much of a shit as he is, ended up in hospital."
    "And so when she calls me up and asks for me to come over, I don't hesitate to agree and get there as soon as I can."
    show bg clairehouse house at center, zoomAt(1, (640, 720)) with timelaps
    "Even though walking up the front path instantly brings back unpleasant memories of the last time I was here."
    "I feel like I can see curtains twitching in the windows of all the other houses on the street, neighbours watching my every move."
    "And I can't help jumping as I reach the point on the path where Hector was lying in wait for me too."
    "All of the emotions that I felt on that day come rushing back in that moment, making me hurry on to the front-door."
    scene bg clairehouse house at center, zoomAt(1, (640, 720))
    show claire at center, zoomAt(1.2, (640, 820))
    "Where I'm relieved to see that Claire is already waiting for, standing in the doorway and looking surprisingly well."
    mike.say "Erm..."
    mike.say "Hi, Claire..."
    mike.say "I came as fast as I could."
    mike.say "Is...is everything okay?"
    scene bg clairehouse kitchen
    show claire c sad
    with fade
    play sound door_close
    "Claire nods and smiles, standing to one side to let me into the hallway and then closing the door behind me."
    show claire a furious
    claire.say "Hello, [hero.name]…"
    claire.say "And I think we both know everything's not okay!"
    claire.say "But thanks for at least trying to pretend it might be."
    show claire bored
    "I nod as Claire leads the way into the house, following close behind her."
    "All the time I'm doing the best I can to keep my head clear of negative thoughts."
    "Telling myself that I need to wait for her to start explaining herself to me."
    "But the problem is that my brain's already started to fill in those gaps itself."
    "I mean, what else is it going to do?"
    "I've been seeing an older, married woman and her husband just found out about the affair."
    "The end result of which is that he tried to fight me in front of pretty much all of the neighbours."
    "Then his heart gave out on him and he had a stroke, right there on the front lawn of the house."
    "What else is Claire likely to be about to tell me?"
    "Other than that she wants to cool things off between us?"
    "So when we sit down together, I'm already bracing myself for what she's going to say."
    show claire furious
    claire.say "Okay, [hero.name]…"
    claire.say "I think that, under the circumstances, we need to talk."
    show claire bored
    "Okay, here we go!"
    mike.say "Sure thing, Claire..."
    mike.say "I think I know what you're going to say anyway."
    show claire upset with dissolve
    "Claire raises her eyebrows in surprise."
    show claire surprised at center, traveling(1.6, 3, (640, 1120))
    claire.say "You know that I'm going to ask you to give me more of your time?"
    claire.say "Oh, [hero.name]…"
    claire.say "That's a real relief to hear!"
    show claire normal
    "I shake my head, still trying to process what Claire just said."
    mike.say "No, Claire..."
    mike.say "I thought that you were going to say you wanted us to take a break!"
    mike.say "You know, that you'd been too hasty about the whole divorce thing?"
    mike.say "I mean, isn't Hector going to need to come back here from the hospital?"
    "Claire shakes her head at this."
    show claire talkative
    claire.say "No, [hero.name]…"
    claire.say "If anything, all of this has made me realise that I need it to happen faster."
    show claire at center, traveling(2, 5, (640, 1320))
    claire.say "And I'm going to need your help to be able to get through what lies ahead."
    claire.say "Of course Hector's going to need care, but he won't be getting it from me."
    claire.say "Most likely he'll have to use his share of the house to fund it after the divorce."
    claire.say "No, what I need from you is to know that you'll be there for me."
    "Claire reaches out, putting her hand atop mine to emphasize her point."
    claire.say "So what do you say?"
    claire.say "Can you make me that promise?"
    menu:
        "I'll be there for you, Claire":
            "I don't even have to hesitate long enough to think."
            "The words just come gushing out of my mouth unprompted."
            menu:
                "Pledge to help":
                    mike.say "Of course I can, Claire..."
                    mike.say "You know that I'm here for you whenever you need me."
                    mike.say "Just say the word and let me know what I can do to help."
                    "I see the smile spreading across Claire's face as soon as I make my promise to her."
                    "Confirming that we're both on the same wavelength and committed to the same goals."
                    claire.say "Thank you, [hero.name]…"
                    claire.say "I can't tell you how glad I am to hear you say that!"
                    $ claire.love += 6
                "Pledge to be Claire's rock":
                    mike.say "I'll do better than that, Claire..."
                    mike.say "I'll get the ball rolling for you, yeah?"
                    mike.say "Because you're going to need a new man in your life."
                    mike.say "Someone to step into Hector's shoes - but do it better."
                    "I see the smile spreading across Claire's face as soon as I make my promise to her."
                    "Confirming that we're both on the same wavelength and committed to the same goals."
                    claire.say "Thank you, [hero.name]…"
                    claire.say "I can't tell you how glad I am to hear you say that!"
                    $ claire.sub += 3
        "Spontaneously propose to Claire" if hero.has_item("wedding_ring"):
            "I know that Claire's just asking me to basically reaffirm my commitment to our relationship."
            "But the truth is that I've been thinking about taking things to the next level for a while now."
            "And so the opportunity seems to be pretty much perfect to ask a question of my own."
            "One that I need to get down on one knee in front of Claire to ask properly."
            claire.say "Oh..."
            claire.say "[hero.name]…"
            claire.say "What are you doing?"
            menu:
                "Let's face it together":
                    mike.say "Claire..."
                    mike.say "You know that I'm here for you whenever you need me."
                    mike.say "Just say the word and let me know what I can do to help."
                    mike.say "Say you'll marry me, and we'll face it all together."
                    "I see the smile spreading across Claire's face as soon as I make my proposition to her."
                    "Confirming that we're both on the same wavelength and committed to the same goals."
                    claire.say "Thank you, [hero.name]…"
                    claire.say "I can't tell you how glad I am to hear you say that!"
                    claire.say "Yes, of course I'll marry you!"
                    $ claire.flags.engagedmike = True
                    $ claire.love += 10
                "I will take care of you":
                    mike.say "I'll do better than that, Claire..."
                    mike.say "I'll get the ball rolling for you, yeah?"
                    mike.say "Because you're going to need a new man in your life."
                    mike.say "Someone to step into Hector's shoes - but do it better."
                    mike.say "Just say that you'll marry me, and I'll make all of that happen."
                    "I see the smile spreading across Claire's face as soon as I make my proposal to her."
                    "Confirming that we're both on the same wavelength and committed to the same goals."
                    claire.say "Thank you, [hero.name]…"
                    claire.say "I can't tell you how glad I am to hear you say that!"
                    claire.say "Yes, of course I'll marry you!"
                    $ claire.flags.engagedmike = True
                    $ claire.sub += 5
    "My head still feels like it's spinning, just like it did when I first turned up at Claire's house."
    "But now it's doing so more because of all that I've found out and the promises that I've made."
    "Though I know that I've made the right choice, because I can feel it in my gut."
    "A warm sensation is spreading outwards from there, filling me with a feeling of serene satisfaction."
    "Enough to make me begin to think of the future in positive, maybe even potentially rosy terms."
    call stop_all_sfx from _call_stop_all_sfx_59
    scene bg black with dissolve
    return

label claire_male_ending:

    if renpy.has_label("claire_achievement_3") and not game.flags.cheat:
        call claire_achievement_3 from _call_claire_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I know that it's kind of a cliché to say that you feel like you're living in a waking dream."
    "Especially when you find yourself standing at the altar in a chapel, dressed in a restrictive suit."
    "All of that whilst waiting for the woman you call the truest love of your life to make her entrance."
    "But the truth is that today I really do feel like that's right where I am, living a dream."
    show jack date zorder 1 at center, zoomAt(0.8, (120, 720)) with dissolve
    "After I asked Claire to marry me and she said yes, things just seemed to start happening at hyper-speed."
    show shawn date noglasses zorder 2 at center, zoomAt(0.8, (300, 720)) with dissolve
    "The plans were made, the dates set and all of the invitations sent out to make sure the chapel would be full."
    show bree date zorder 3 at center, zoomAt(0.8, (200, 720)) with dissolve
    show sasha date zorder 4 at center, zoomAt(0.8, (540, 720)) with dissolve
    "And looking back over my shoulder, I can certainly say that part of the plan came off."
    "Almost every inch of the pews in the place are filled with the backsides of friends and family."
    show minami date zorder 5 at center, zoomAt(0.85, (70, 720)) with dissolve
    show angela date zorder 6 at center, zoomAt(0.85, (440, 720)) with dissolve
    "On my side I can see my mom and dad, as well as Minami, all dressed up to the nines."
    "There's my housemates, sitting with friends like Jack and Shawn too."
    "Claire's side of the chapel is no less filled with people from her life too."
    show lily teaser zorder 7 at center, zoomAt(0.85, (1140, 720)) with dissolve
    show adam teaser zorder 8 at center, zoomAt(0.85, (940, 720)) with dissolve
    "But the main ones that I recognise are her stepson and my childhood friend Adam."
    "Who I see is sitting with Lily, his rather fine bride-to-be."
    "And I'm obviously glad that Hector is nowhere to be seen."
    "Claire's former husband apparently still not having recovered from his minor stroke."
    "Which means that there's one less thing for me to have to worry about in the grand scheme of things."
    "My eyes are still wandering over the assembled guests a moment later, when music suddenly fills the air."
    "As one, the people in the chapel turn their heads to the doors, which swing open right on cue."
    "Of course, all of this is to allow Claire to sweep into the place and down the aisle."
    show claire wedding zorder 99 at center, zoomAt(1.2, (640, 820)) with dissolve
    "Generating gasps and whispered comments of admiration as the guests see her dress for the first time."
    "It's also the first time I've set eyes on the wedding dress too, as Claire insisted on being old-fashioned."
    "Determined that there was no way I'd catch even a glimpse of it until the actual ceremony was underway."
    "And I have to say that, now I have seen it, I totally understand her choice."
    "Sure, you know that I'm going to say Claire looks stunning in the thing."
    "That I've never seen her looking as lovely as she does right now."
    "But that's the honest truth of it - she looks more perfect than I could ever have imagined."
    if claire.is_visibly_pregnant:
        "The cut of her dress is flattering her in every way possible."
        "Especially around the curve of her belly, where she's really starting to show."
        "And as it always does, the merest thought of the child we're expecting fills me with hope."
        "As I imagine the possibilities of raising a family of our own together."
    else:
        "Part of me was worried that the dress wouldn't seem special somehow."
        "As if the fact that Claire had already walked down the aisle once would make a difference."
        "But now I can see how wrong I as to think like that."
        "Because she looks simply radiant as she makes her way towards me."
    "As soon as Claire makes it to the altar, I feel the urge to start talking to her."
    "That I have a hundred and one things on my mind that I'd like to tell her or questions I want to ask."
    "But before I can even open my mouth, someone else beats me to it and asserts their authority instead."
    "Priest" "Alright..."
    "Priest" "Shall we get this show on the road?"
    show wedding claire zorder 100 with fade
    "I find myself surprised by what the priest just said to get our attention."
    "Because it sounds like such an odd thing to say in a formal situation like this."
    "But it's not like I get the chance to say anything about it."
    "As the priest seems to take our silence as unspoken agreement."
    show wedding claire priest with dissolve
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To witness the joining of these two people..."
    "Priest" "In the bonds of holy matrimony."
    "We rehearsed the ceremony more than once in order to make sure things would go off without a hitch."
    "And every time we did so, it seemed to drag on for a crazily long amount of time."
    "But now that we're doing it for real, the opposite seems to be true, as it speeds by."
    "Before I know it, the priest has got to the actual vows!"
    "Priest" "Do you, Claire..."
    "Priest" "Take this man, [hero.name]…"
    "Priest" "To be your lawful, wedded husband?"
    "Claire nods her head, answering without hesitation."
    claire.say "I do."
    "Priest" "Very good..."
    "Priest" "And do you, [hero.name]…"
    "Priest" "Take this woman, Claire..."
    "Priest" "To be your lawful, wedded wife?"
    "I'm almost tripping over myself as I try to give my response."
    "Feeling like my tongue is getting knotted inside of my mouth."
    mike.say "I..."
    mike.say "I do!"
    "Priest" "Also good."
    "The priest nods and turns to the guests filling the chapel."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these two people may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "As you'd expect, this gets the usual round of smiles and chuckles from the guests."
    "But for a moment I feel like I'm holding my breath, just waiting for it to be over."
    "Because I'm afraid that Hector might not be as ill as he claimed to be."
    "Or that Adam could be secretly harbouring plans to scupper his stepmom's second wedding."
    "So when the priest nods again and gets things moving, my relief is immense."
    "Priest" "Alright then..."
    "Priest" "By the powers vested in me..."
    "Priest" "I now pronounce you husband and wife."
    "Priest" "You may kiss the bride."
    show wedding claire -priest with dissolve
    "It's not like Claire and I need any encouragement to do that."
    "As we come together almost before the priest is done speaking the words."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show claire kiss wedding
    with fade
    $ claire.flags.kiss += 1
    "And the kiss that follows is probably a little too risqué for the chapel."
    "But again, it's not like that seems to have any effect on Claire and me."
    "Because we're too busy wrapping our arms around each other."
    "That and pressing our lips together in the most passionate manner imaginable."
    "All to celebrate the fact that we're now officially a married couple."

    scene claire ending with fade
    claire.say "You're sure?"
    claire.say "You really want me to do the talking?"
    claire.say "Well, if you're sure, then I suppose I'll give it a try."
    claire.say "I mean, this was always going to be a strange thing to explain, [hero.name] and myself."
    claire.say "And before you ask the inevitable question - the answer is no, I didn't see him grown up."
    claire.say "I married Hector and became Adam's stepmother when he and [hero.name] were already teenagers."
    claire.say "So it was more a case of meeting them for the first time when they were young men, you see?"
    claire.say "And even then it wasn't as if I fell madly in love with [hero.name] and just kept my distance."
    claire.say "No, to me he was one of Adam's friends, just one of the ones that I thought was the nicest."
    claire.say "They were in and out of the house all the time back then, doing all the things teenage boys do."
    claire.say "I suppose that I suspected [hero.name] might have had a little bit of a crush on me at the time."
    claire.say "It's a perfectly natural phase that most boys seem to go through, and I thought it was flattering."
    claire.say "I always tried to keep from encouraging it in him, mainly because he would doubtless grow out of it."
    claire.say "But also because I didn't think it was healthy for me to take pleasure in his admiration either."
    claire.say "After all, I was the adult and he was, technically, still a child back then."
    claire.say "And that's exactly what I thought had happened, [hero.name] grew into a man and moved away."
    claire.say "Of course I missed having him around, but I just told myself he'd matured and moved on in life."
    claire.say "And it wasn't like I didn't have concerns of my own to deal with too."
    claire.say "Hector didn't go to bed one night as a kind, caring husband and wake up the next morning as a bitter grouch."
    claire.say "He'd always had that unpleasant, sour side to his nature, ever since we first met."
    claire.say "But the passage of time seemed to see it taking over more of him with every year."
    claire.say "Until by the time Adam started to bring his new fiancée home, it had consumed him totally."
    claire.say "I think that's when it all started to get to be too much for me."
    claire.say "Before I'd been able to tell myself that my situation wasn't anything unusual."
    claire.say "That most married women that stayed at home weren't happy with their lot in life."
    claire.say "But I had a home and a husband that paid the bills, so what was there to complain about?"
    claire.say "Then I saw the relationship that Adam had with Lily, and it changed everything."
    claire.say "Adam had always been a better person than his father, especially in the way he treated women."
    claire.say "I could tell that he saw Lily as his friend, his companion, and most importantly - his equal."
    claire.say "There was no sense of him expecting her to defer to him, or to pander to his insecurities."
    claire.say "In short, it was plain to see just how much he adored her."
    show claire ending pie with dissolve
    claire.say "I was instantly jealous of Lily, but of course I hid it behind smiles, like always."
    claire.say "And the truth was that I didn't hate her, I just longed for what she had with Adam."
    claire.say "Then, when we threw the engagement party for the two of them, [hero.name] was on the guest-list."
    claire.say "To be honest, I had consigned the young man I knew back then to my memory when he moved away."
    claire.say "Angela might have passed on little bits of information about how he was getting on."
    claire.say "But he still seemed to have changed so much when I saw him walking across the lawn that day."
    claire.say "[hero.name] wasn't the boy I remembered anymore - now he was a man!"
    claire.say "I tried as best I could to behave just like I had in the past, to be his friend's stepmom."
    claire.say "But I could see the way he was looking at me even then, bringing back all the memories of his former crush."
    claire.say "Of course I told myself that I was just being stupid, an old woman indulging in a pleasing fantasy."
    claire.say "It was only when we started to chat and catch up that I became sure that I wasn't mistaken."
    claire.say "[hero.name] really was flirting with me!"
    show claire ending pie sides with dissolve
    claire.say "By now I was becoming smitten with the idea, but trying to tell myself that we could just be friends."
    claire.say "So I made excuses to drop in on him and spend time in his company."
    claire.say "And it just grew from there, a friendship that soon became much more."
    claire.say "At the same time Hector's suspicions only grew, and I guess I was careless."
    claire.say "Because soon enough the two of them were confronting each other over me."
    claire.say "And I'd be lying if I said that it wasn't thrilling - two men butting heads for my affections!"
    claire.say "But in the end, the young buck was always the one that was going to win out."
    claire.say "Years of bad diet, booze and stress felled Hector before he could harm [hero.name]."
    claire.say "And with him out of the way, we were finally free to begin planning a life together."
    claire.say "As soon as the divorce was finalised, we got married and [hero.name] moved in with me."
    show claire ending pie sides chicken mike with dissolve
    claire.say "Together we bought out Hector's share of the house, and the money paid for his ongoing care."
    claire.say "And now I get to live in the house I always liked with a man that I actually love."
    claire.say "[hero.name] is slowly adapting to the suburban life too."
    claire.say "He's still climbing the corporate ladder at work, keeping us well."
    claire.say "But he's also mastering the art of the cook-out."
    claire.say "And he keeps talking about coaching the neighbourhood softball team too."
    if claire.is_visibly_pregnant:
        show claire ending pie sides chicken mike claire girl boy with dissolve
        claire.say "All of this on top of being the best father in the world to little Mikey Junior too."
        claire.say "The footsteps of a child in the house giving me something that I never had before."
        claire.say "The chance to raise a family that's truly my own, truly born out of our love for each other."
    else:
        show claire ending pie sides chicken mike claire with dissolve
        claire.say "And he keeps dropping hints about how big the house is and all the extra space."
        claire.say "As well as suggesting which of the rooms would make the best nursery."
        claire.say "All the time thinking that I don't catch on to how much he wants to start a family of our own."
    claire.say "I mean, sometimes I do screw-up and call him 'Hector' by mistake."
    claire.say "Which makes him suck in his gut and pat the back of his head."
    claire.say "And then I have to reassure him it was just a little slip of the tongue."
    claire.say "That he's not expanding around the middle, and the bald-spot isn't really noticeable."
    claire.say "I'm sure that Hector turned out the way he did because of the person he was inside."
    claire.say "Not because of the life he was leading for all those years."
    claire.say "And even if [hero.name] is going through some middle-age changes a little early..."
    claire.say "Well, he's still the same man - the one that I love."
    claire.say "Needing to let out his pants a few sizes isn't going to change that!"
    call stop_all_sfx from _call_stop_all_sfx_60

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not claire.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_25
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_25
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label claire_preg_talk:
    $ claire.flags.toldpreg = True
    show claire sad at center, zoomAt(1.0, (640, 720))
    "The moment that I set eyes on Claire, I can see that there's something wrong."
    "She has an almost haunted look on her face and her eyes are red-rimmed."
    show claire at center, traveling(1.5, 0.5, (640, 1040))
    "In fact she looks like she hasn't gotten a wink of sleep since the last time I saw her."
    mike.say "Claire..."
    mike.say "Are you okay?"
    mike.say "Is there something wrong?"
    "Claire looks at me like she wants to shake her head and nod it at the same time."
    "Like there's a dozen things running around inside of her head right now."
    "And she really doesn't know the best way to answer even a basic question like that."
    show claire whining
    claire.say "Yes..."
    claire.say "No..."
    claire.say "I...I don't know!"
    show claire sad
    "Wanting to do whatever I can to help, I reach out and take hold of Claire's hand."
    "This seems to do the trick, as she instantly returns the gesture, holding on tightly."
    "And I think I can see a little calm beginning to return to her."
    mike.say "It's okay, Claire..."
    mike.say "Just take your time, okay?"
    mike.say "Whatever it is, I'm listening."
    show claire sadsmile
    "Claire nods as I say all of this."
    "And I can see that she's trying to pull herself together."
    "Soon enough she nods, as if she feels like she's ready to talk."
    show claire talkative
    claire.say "Okay, okay..."
    claire.say "So, I took a test this morning..."
    claire.say "And the result was positive!"
    show claire sadsmile
    "For a moment the reality of what Claire's telling me doesn't seem to sink in."
    "I hear the words and somehow my brain interprets them in the most illogical manner."
    mike.say "Well..."
    mike.say "Isn't that good?"
    mike.say "After all, it's important to be positive."
    show claire stuned
    "I can see that Claire's now staring at me in total amazement."
    "Like she can't actually believe what she's hearing."
    "And that's when my brain seems to finally catch up with itself."
    mike.say "Oh..."
    mike.say "Wait..."
    mike.say "When you said a test - you meant, like, a pregnancy test?!?"
    show claire surprised
    claire.say "Of course I meant a pregnancy test!"
    claire.say "What other kind of test could I possibly have meant?"
    show claire sad
    "By now I'm starting to get why Claire looks so worried and worn-out."
    "And to be honest, I quickly starting to feel the same way too."
    if claire.flags.still_maried:
        "Without thinking, I blurt out the first thing that pops into my head."
        mike.say "Erm..."
        mike.say "You didn't tell a certain person about this, did you?"
        show claire stuned
        "Claire looks at me like I'm stupid for a second time."
        show claire surprised
        claire.say "I didn't tell him about the two of us having an affair, [hero.name]…"
        claire.say "So do you honestly think I'm going to tell Hector about this?!?"
        show claire stuned
        mike.say "No, no..."
        mike.say "Of course not."
        show claire annoyed
        "Claire shakes her head, obviously annoyed at my struggling to keep up."
        show claire whining
        claire.say "So, as I see it, we've got two problems on our hands."
        claire.say "One, we have to get rid of it."
        claire.say "And two, we have to do it without my husband finding out."
    else:
        "But I guess that Claire's already gone through what's playing out in my head."
        "Because it doesn't take her long to cut to the chase."
        show claire whining
        claire.say "I need you to focus, [hero.name]…"
        claire.say "Because you've got to help me get rid of it!"
    show claire sad
    "I'm only just starting to process the idea of Claire being pregnant."
    "Let alone get my head around the fact that I'm the father too."
    "But now she's dealt me another blow that's staggered my poor, over-taxed brain."
    mike.say "Wait...what?"
    mike.say "You mean..."
    mike.say "You want to get an abortion?"
    show claire whining
    claire.say "Of course I do!"
    claire.say "I'm way too old to have a child."
    if claire.flags.still_maried:
        claire.say "Especially with my lover, rather than my husband!"
    show claire sad
    "Claire's looking at me like I'm supposed to be agreeing with her right now."
    "But all of this is happening so fast that I feel like my head is spinning."
    "And the problem is that I know I have to say something, and fast."
    menu:
        "It might be a wise decision, yeah...":
            "Part of me hates the very idea of doing this, thinks that it's cowardly."
            "But I can see the anxiety written all over Claire's face."
            "And I want to do anything that I can to help make it go away."
            "So I decide that there's no other way out of this mess."
            mike.say "Okay, Claire..."
            mike.say "If that's what you want, then that's what we'll do."
            mike.say "I...I don't know how this kind of thing works though!"
            "I kind of falter as I make the admission."
            "But the relief that I see on Claire's face can't be anything but real."
            show claire whining
            claire.say "Neither do I."
            claire.say "But between the two of us, I think we can work it out!"
            show claire sadsmile
            "I nod and squeeze Claire's hand tighter than ever."
            "And I try to put a literal brave face on for her sake."
            "Even though the truth is that I feel more than a little scared myself."
            "I don't know what lies ahead."
            "But I get the impression we're going to need each other like never before."
            $ claire.love += 10
            $ claire.unpreg()
        "But I would love to hear Adam call me step-father!":
            "I can see that Claire's convinced herself an abortion is the only way out of this."
            "But I can't help seeing things differently, like there might be a future in it."
            mike.say "I don't think we need to do anything that extreme, Claire."
            mike.say "I think that we could make a go of it, you know?"
            mike.say "You, me and the baby - we could be a family."
            show claire stuned
            "Claire's eyes get wider the whole time I'm explaining myself."
            "And as soon as I'm done speaking, she starts to shake her head."
            show claire surprised
            claire.say "Are you totally crazy?!?"
            claire.say "I already spent most of my life doing the whole family thing!"
            claire.say "And do you need me to spell out how much that sucked?"
            show claire stuned
            "Now it's my turn to shake my head, as I try to change Claire's mind."
            mike.say "No, Claire..."
            mike.say "You spent that time doing the family thing with Hector."
            mike.say "I promise you that trying again with me will be totally different."
            mike.say "Because we love each other, and we'll both love our child."
            "Claire stares at me as I make my pitch."
            "And I feel a glimmer of hope that I'm getting through to her."
            show claire surprised
            claire.say "You mean..."
            claire.say "We could start over?"
            claire.say "We could start anew?"
            show claire stuned
            mike.say "Yeah, Claire - that's exactly what I mean!"
            if claire.love >= 150:
                "Claire fixes me with a serious stare."
                "One that makes me feel like she's looking straight into my soul."
                show claire surprised
                claire.say "Are you serious, [hero.name]?"
                claire.say "Do you really understand what that means?"
                claire.say "You'd have to be a husband AND a father."
                show claire stuned
                "The fact that Claire's even discussing the idea instantly fills me with hope."
                "Before she was all doom and gloom, with no hope of there being a happy ending."
                "But now I have to prove to her that I'm serious, and this isn't just a fantasy."
                mike.say "I'm ready, Claire..."
                mike.say "And you know that I'll be everything you need."
                mike.say "Because this is like a dream come true for me."
                "Claire actually looks surprised by my enthusiasm."
                show claire surprised
                claire.say "But..."
                claire.say "You're getting saddled with a middle-aged woman and a kid!"
                claire.say "Most guys would think that was a nightmare."
                show claire sadsmile
                mike.say "Then those guys are morons!"
                mike.say "Because I'm getting to raise a kid with the woman I love."
                show claire normal
                "Claire leans herself against me, putting her head on my shoulder."
                show claire talkative
                claire.say "Oh, [hero.name]…"
                claire.say "All of this is so crazy."
                claire.say "But the craziest thing of all is that I think it might actually work!"
                show claire happy
                $ claire.love += 5
                $ claire.sub += 5
            else:
                "Claire seems to be listening to what I'm saying very intently."
                "And once I'm done, there's a moment of silence while I wait for her answer."
                "But then her former demeanour seems to return, and she shakes her head."
                show claire whining
                claire.say "No, [hero.name]…"
                claire.say "I'm sorry, but that's not going to happen."
                claire.say "Maybe in another lifetime..."
                show claire sad
                "Claire underlines her point by letting go of my hand."
                "And then she pulls away, turning on her heel."
                show claire whining
                claire.say "And if you're not going to help me..."
                claire.say "Then I'll have to make the arrangements on my own."
                show claire sad
                "I know that I should say something right now."
                "That I should be offering Claire support."
                "But the truth is that I'm too shocked and stunned to do anything of the kind."
                "Maybe later I'll be able to pull myself together and actually offer her help."
                "But here and now, all I can do is stand there and watch her walking away."
                $ claire.sub -= 10
                $ claire.unpreg()
    return

label claire_sub_event_01:
    if claire.sub.max < 50:
        $ claire.sub.max = 50
    scene tv_bg
    show claire c sad at center, zoomAt(2.4, (340, 1520))
    with fade
    "I feel like Claire and I are becoming closer each time we're together."
    "That I'm starting to really understand what makes her tick and what she wants."
    "Of course, I already know what I want, and that's to be with her!"
    "But she's really beginning to open up to me now, to let me into her inner world."
    "So when I'm already sitting down and Claire hurries to be at my side, it comes as no surprise to me."
    "Though I do have to confess that what I was expecting to follow was a pleasant little cuddle."
    "You know, maybe even with a tender kiss or too thrown in for good measure?"
    "But it takes me by surprise when Claire leans her head on my shoulder."
    show claire sad at center, traveling(2.6, 2, (340, 1620))
    "And I feel the unmistakable sensation of her quaking as she presses herself against me."
    mike.say "Hey..."
    mike.say "Claire..."
    mike.say "What's the matter?"
    "Claire doesn't offer me an answer at first, which really doesn't surprise me."
    "If she's in such an emotional state, then she's going to need a little time to collect herself."
    "So I wait patiently for Claire to respond, listening closely when she finally does."
    show claire pained at startle(0.1, 5)
    claire.say "I..."
    show claire dazed
    claire.say "I've been thinking, [hero.name]…"
    claire.say "Since I started telling you all about my problems with Hector..."
    show claire sad
    "I nod slowly, making sure that Claire feels the motion of my head moving as I do so."
    "Because I want to do all that I can to help her open up to me even more than she already has."
    mike.say "It's okay, Claire..."
    mike.say "I know that talking about this kind of thing isn't easy."
    mike.say "You can go as slow or as fast as you like..."
    mike.say "But you need to tell me what's on your mind."
    "Now I can feel the sensation of Claire nodding her head as it rests on my shoulder."
    "And I know that my encouragement has had the desired effect in terms of making her open up."
    show claire dazed
    claire.say "The thing is, [hero.name]…"
    claire.say "I never really thought about how much control Hector had over me before."
    claire.say "I guess I'm pretty old-fashioned when it comes to things like that."
    claire.say "But I just assumed that, as he was my husband, he was supposed to be in charge."
    claire.say "You know, that he should be the one making all the decisions?"
    show claire sad
    mike.say "I get that, Claire."
    mike.say "But did you ever wonder if the control was really the problem?"
    "I feel Claire's body move as she reacts to my question."
    "And when she makes to sit up, I allow her to do so."
    "Then she turns so that she can look me straight in the eye."
    show claire dazed
    claire.say "What do you mean?"
    claire.say "You think what, that I'm weak?"
    claire.say "That I need a man to control me?"
    show claire sad
    "I make a point of smiling and putting my hands on either side of Claire's face."
    "Holding her in way that should make her feel comfortable and protected from harm."
    "But one that also serves as a subtle assertion of my authority."
    mike.say "Wanting someone to be in control doesn't make you weak, Claire."
    mike.say "In fact the truth is that it's the total opposite."
    mike.say "Admitting that you want another person to take charge requires a lot of strength."
    mike.say "No, the problem you had in the past wasn't surrendering control."
    mike.say "It was surrendering it to someone that you didn't trust, to someone that didn't truly love you."
    "Claire looks at me as she cocks her head on one side."
    "Almost like she's trying to make what I'm saying make sense by doing so."
    show claire startle at startle(0.1, 5)
    claire.say "What are you saying?"
    claire.say "That I was letting myself be controlled in the wrong way?"
    show claire upset
    mike.say "What I'm saying is that you gave your trust to the wrong person."
    mike.say "But when you find the right one, you'll obey without even needing to think about it."
    "Claire still doesn't look convinced by my explanation."
    "So I decide that a practical demonstration is required."
    mike.say "Claire..."
    mike.say "I want you to kneel down in front of me."
    show claire evil
    "Claire looks me straight in the eye as I issue the command."
    "And for a moment I think that she's going to refuse to obey."
    show claire a shy at center, zoomAt(2.6, (640, 1620)) with dissolve
    "But then, without even seeming to realise she's doing it, she slides off the sofa."
    show claire a at center, traveling(2.6, 2, (640, 1820))
    "And the next thing I know, she's knelt in front of me, looking eagerly upwards."
    mike.say "Good girl!"
    mike.say "You see?"
    mike.say "Doesn't it feel better to do what comes naturally?"
    "Claire nods hastily, as if she's now keener than ever to please me."
    mike.say "Now, Claire..."
    mike.say "It's best if you're totally honest with me from now on."
    mike.say "So I want you to confess your desires to me, okay?"
    mike.say "I want you to tell me all of the things you've been holding back."
    show claire blush
    "I see the colour starting to spread across Claire's cheeks as she looks up at me."
    "A sure sign that there's an emotional battle going on inside of her right now."
    "But she seems to do all she can to race ahead of it, beginning to speak quickly."
    show claire dazed
    claire.say "I..."
    claire.say "I want to be secure, more than I want to be free."
    claire.say "And I know that people will hate me for that..."
    claire.say "That they'll say I should be a modern, independent woman."
    claire.say "I'm afraid that's one of the reasons I said yes to Hector..."
    claire.say "That I never loved him, just thought he could protect me."
    claire.say "I hate feeling guilty and anxious all the time."
    claire.say "I just want someone to make life simple for me!"
    show claire shy
    "By now Claire's wringing her hands in front of me, her elbows on my knees."
    "And the whole thing is starting to feel almost like a religious confession."
    "I feel compelled to reach out and hold her hands in mine."
    "Offering a gesture of solidarity and support in her moment of need."
    mike.say "You're a good girl, Claire."
    show claire sadsmile
    mike.say "Now, don't you feel better for getting all that off your chest?"
    "Rather than answering with words, Claire leans forwards."
    show claire kiss at center, zoomAt(1.4, (640, 920))
    show fg_dreamy as foreground
    with fade
    "And she kisses me, full on the lips with a genuine passion."
    play sound heartbeat
    "I can almost feel an electrical charge passing between us as she does so."
    "And when the kiss ends, I'm left breathless and, my heart racing."
    stop sound
    hide claire kiss
    show claire idle talkative at center, zoomAt(2.6, (640, 1620))
    claire.say "Ah..."
    claire.say "Oh..."
    claire.say "Please, [hero.name]…"
    claire.say "Tell me what to do next?"
    $ claire.sub += 4
    $ claire.flags.subevent = TemporaryFlag(True, 3)
    call stop_all_sfx from _call_stop_all_sfx_68
    scene bg black with fade
    return

label claire_sub_event_02:
    if claire.sub.max < 75:
        $ claire.sub.max = 75
    scene tv_bg at blur(15)
    show fg_dreaming as dreamfx zorder 9
    show fg_dreamy as lovefx zorder 8
    show claire -idle pat sadsmile a at center, zoomAt(2.6, (640, 1820))
    with Pixellate(1, 5)
    play sound heartbeat loop
    "I can't get the image of Claire down on her knees in front of me out of my head."
    "It's been one that I've come back to over and over again in the time since it happened."
    "And now that we're back together again, I can hardly think of anything else at all."
    "Plus the fact that we're currently alone is only serving to make matters that much worse."
    "The knowledge that I could just ask Claire to do something like that for me right here and now."
    "Oh man...it's almost impossible to keep my mind on the conversation that we're having."
    claire.say "[hero.name]?"
    claire.say "Are you listening to me?"
    claire.say "Did you hear what I just said?"
    "All of a sudden I feel my most basic male survival instincts kicking in."
    "The woman that I'm on a date with is asking me if I'm paying her attention."
    "So even in such a distracted state, I start struggling to prove that I am."
    scene expression f"bg {game.room}" at center, zoomAt(2, (640, 1020))
    show claire at center, zoomAt(1.4, (640, 920))
    stop sound
    with hpunch
    mike.say "Huh?"
    mike.say "Oh...oh yeah, Claire..."
    mike.say "I'm totally listening to you."
    "Now that my head is almost fully back in the room, I can see the expression on Claire's face."
    "And luckily for me it's not one of obvious irritation as I'd feared it would be."
    "Instead I'm starting to see that she's looking at me with genuine concern instead."
    show claire whining
    claire.say "Are you sure?"
    claire.say "Because it's kind of important to me that you hear this."
    show claire startle
    claire.say "You know, that I want to get out of having to make decisions?"
    show claire shy
    "That last question is all I need to fully snap back to reality."
    "Because it instantly connects with the obsessions running around inside of my head."
    mike.say "You...you mean like the last time?"
    mike.say "Like when I started telling you what to do?"
    mike.say "Not just stuff like choosing what to have for lunch?"
    "My questions must sound pretty dumb, because Claire begins to smile."
    "And she shakes her head, dismissing my concerns."
    show claire talkative
    claire.say "Of course I mean like the last time!"
    claire.say "The truth is that I haven't been able to stop thinking about it."
    claire.say "I felt so liberated, so free..."
    claire.say "And I want to feel like that again."
    show claire normal
    "I do the best I can to make it look like I'm considering what Claire has to say."
    "And not like I'm mentally chomping at the bit to get down to that kind of thing again."
    mike.say "Oh yeah..."
    mike.say "I got a lot out of it too."
    mike.say "So it's definitely something I'd want to do again."
    "Claire nods eagerly as I explain my own feelings."
    show claire at center, traveling(2, 2, (640, 1270))
    "And she moves as close to me as she can possibly get."
    "An intensity beginning to show in her eyes as she does so."
    show claire talkative
    claire.say "You do?"
    claire.say "That's marvellous news!"
    claire.say "But when, [hero.name]?"
    claire.say "When could we do it again?!?"
    show claire normal
    "By now I'm pretty much starting to sweat with the need to look cool."
    "Trying to keep that air of control that's needed for this kind of thing to work."
    "After all, I can't subtly dominate Claire if I'm giving off desperate vibes, can I?"
    mike.say "Well that's the interesting thing, Claire..."
    mike.say "Seeing as how we're both consenting adults..."
    mike.say "We can do something like that anytime we like."
    mike.say "Just so long as both of us are on the same page."
    "Before I can say another word, Claire's on the move."
    show expression f"bg {game.room}" at center, traveling(2, 2, (640, 720))
    show claire at center, traveling(2, 2, (640, 1220))
    "And just like before, she slides down onto her knees."
    "Looking up at me from below, eyes burning with an obvious need."
    show claire talkative
    claire.say "Please, [hero.name]…"
    claire.say "I'm ready to do whatever you desire of me."
    claire.say "Just say the word, and it'll be done!"
    show claire evil
    "Again I feel myself doing the best I can to keep a handle on my feelings."
    "Wanting to show the desire that Claire's kindling in me right now."
    "But knowing that I need to play the part that she's wanting of me."
    "What I need is something to use as a prop, something exciting."
    "And luckily for me, when I reach into my pocket, I feel the silk handkerchiefs in there."
    "The same ones that Claire lent me to dry myself off when I was caught in the rain at her place."
    "So I take hold of them, pulling them out of my pocket with a little flourish."
    "But it's still enough to make Claire gasp and clap her hands together."
    show claire startle at startle(0.1, 5)
    claire.say "Ooh..."
    show claire talkative
    claire.say "Are you going to tie me up with those?!?"
    show claire evil
    "I hold up a hand and give Claire a little shake of the head."
    "Letting her know that asking questions isn't the done thing."
    show claire pleased at startle(0.2, -10)
    "And it seems to work, as she looks down and nods her own head."
    show claire startle
    claire.say "Sorry...master..."
    show claire talkative
    claire.say "I'm ready to be told what to do now."
    show claire normal
    mike.say "That's more like it, Claire."
    mike.say "So..."
    mike.say "First things first - take off your clothes."
    "Claire nods again, already hurrying to do as she's told."
    "But I make a point of adding one little thing to my orders."
    mike.say "But not too quickly though..."
    mike.say "I want to be able to enjoy the show!"
    "Claire nods for a third time, looking up slightly as she does so."
    "Just enough for me to be able to see the burning look in her eyes."
    "Letting me know that she's seriously enjoying what I'm making her do right now."
    "But the cerebral thrill of it all soon pales as the physical reality sets in."
    "Claire begins by easing her top off slowly, revealing her shoulders a little at a time."
    show claire underwear with dissolve
    "And then she pulls it away, so that she's kneeling before me with her bra on show."
    "Next she shuffles her skirt downwards, her breasts swaying as she does so."
    "I can see the cups of her bra struggling to contain those awesome orbs."
    "And yet at the same time my eyes are being drawn down towards her thighs."
    "Because the long, graceful sweep of them is now becoming visible too."
    "My eyes drink in the sight as Claire's skirt slips lower still."
    "And then they retrace their steps back up again, settling on her panties."
    "With one hand, Claire reaches up behind her back and unhooks her bra."
    "While the other slides her panties down just like her skirt before them."
    show claire naked with dissolve
    "As soon as they're freed, Claire's breasts succumb to gravity."
    "And yet somehow they look even better as they settle naturally upon her chest."
    "Now that she's totally naked, I make to get up from my seat."
    "A task that's made that much more difficult because of the fact I'm hard as a rock by now."
    show claire c
    "And I gently take hold of Claire's arms, putting them behind her back."
    "She offers no resistance as I use the first of the silk scarves to tie her wrists together."
    "Then I slide my hands down the length of her legs, all the way to the ankles."
    "Where I use a second scarf to bind them together as well."
    "Now that she's bound, I lean in close and whisper in Claire's ear."
    mike.say "Now hold still while I tease you."
    mike.say "You get extra points for staying silent too."
    "In reality I have no idea how any kind of points system would work in a situation like this."
    "And part of me is kind of hoping that Claire's actually going to make a whole bunch of sexy noises."
    "I just feel like that's the kind of thing someone in my position should be saying to someone in hers."
    "Claire nods, her eyes wide as she watches me."
    "I decide that we're not ready for me to do anything seriously intense."
    "And I need to build Claire's trust before I do anything like taking her in this position."
    "So I limit myself to placing my hands gently on her haunches at first and gauging her reaction."
    "But even with so soft of a touch, I instantly feel Claire shudder and let out a desperate moan."
    "Encouraged by her reaction, I begin to move my hands over her body, palms flat against her skin."
    "I'm also sure to make my touch teasing, as well as intimate, playing with her the whole time."
    "The tips of my fingers brush the very edge of Claire's pussy for a second."
    "And then they pass close enough to her nipples to touch, but not linger."
    "With every little tease I make, I can feel her arousal build."
    show claire pleased
    "Like Claire's constantly on the brink of feeling the relief that she craves."
    "And my task is to keep her there for as long as I possibly can."
    "Making her teeter on the edge of release, increasing her need for it as I do so."
    "All the while I can feel a growing understanding of the dynamics at play here."
    "The subtle power that I have over Claire and how best to use it."
    "But in the end it seems to be too much for her to bear any longer."
    show claire pained at hshake
    "As she curls up into a ball, desperately trying to bring herself off."
    "And I judge that this is the point where I should cease touching her."
    "Instead picking at the knots until her wrists and ankles are freed."
    show expression f"bg {game.room}" at center, traveling(2, 2, (640, 1020))
    show claire normal at center, traveling(1.4, 2, (640, 920))
    show claire underwear with dissolve
    "Claire slowly collects herself, sitting up and beginning to put her clothes back on."
    show claire a casual with dissolve
    "And once she's done, she comes to sit at my side, still more than a little subdued."
    show claire talkative at center, traveling(2, 2, (640, 1270))
    claire.say "Thank you, [hero.name]."
    claire.say "Being yours like this..."
    claire.say "It...makes me feel free."
    claire.say "I know that sounds like it shouldn't make sense, but it does!"
    claire.say "And I think that I want more of it, if you're willing?"
    show claire normal
    "I nod my head, already thinking of the possibilities."
    "Imagining what it will be like to have Claire obey my every word."
    "And all of the things that I've always dreamed about asking her to do for me...and to me!"
    $ claire.sub += 4
    $ claire.flags.subevent = TemporaryFlag(True, 3)
    call stop_all_sfx from _call_stop_all_sfx_69
    scene bg black with fade
    return

label claire_sub_event_03:
    if claire.sub.max < 100:
        $ claire.sub.max = 100
    claire.say "[hero.name]!"
    claire.say "[hero.name], there you are..."
    claire.say "I'm so glad that I found you!"
    "At the sound of Claire's voice, I turn around to see her running towards me."
    if game.room == "park":
        scene bg pond at center, zoomAt(1, (640, 720))
        show claire sad at center, zoomAt(1, (640, 720))
        with PushMove(1.0, "pushleft")
        $ game.room = "pond"
    elif game.room == "pond":
        scene bg park at center, zoomAt(1, (640, 720))
        show claire sad at center, zoomAt(1, (640, 720))
        with PushMove(1.0, "pushright")
        $ game.room = "park"
    "And when I see how flustered and dishevelled she looks, I hurry to meet her."
    show expression f"bg {game.room}" at center, traveling(1.2, 1, (640, 820))
    show claire sadsmile at center, traveling(2.6, 1, (640, 1570))
    pause 1
    with hpunch
    mike.say "Claire..."
    mike.say "What's wrong?"
    mike.say "Did that bastard put his hands on you?!?"
    "Claire shakes her head as she runs into my open arms, wrapping her own around me."
    "And when she answers my questions, her voice is muffled as she's resting her head on my shoulder."
    show claire a whining
    claire.say "No..."
    claire.say "No, he didn't - but I'm worried that he might."
    claire.say "Oh, [hero.name]...I only feel safe when I'm with you!"
    show claire sadsmile
    "I make a point of not saying anything in response to Claire's emotional declaration."
    "Instead I hold her close to me, stroking her hair and comforting her without hesitation."
    "Knowing that what she needs right now is to be sure that there's someone to protect her."
    "It's only when I feel that Claire's stopped shaking that I even think of speaking."
    "Feeling her body begin to support it's own weight totally for the first time since she showed up."
    mike.say "There's nothing to worry about, Claire..."
    mike.say "Not while you're with me."
    mike.say "I'll make sure that piece of shit husband of yours can't hurt you."
    "Claire nods gratefully, taking a half a step back to continue pulling herself together."
    show claire talkative
    claire.say "I...I know that now, [hero.name]…"
    claire.say "Or should I call you 'Master'?"
    show claire b
    claire.say "Because I need you so much!"
    show claire pleased
    "I've been getting ever more used to being the strong one in my relationship with Claire."
    "And yet I still can't deny the thrill that I feel when she calls me something like that."
    "The strange mixture of total power and endless affection it stirs up inside of me."
    "Knowing that she's putting herself completely in my hands, totally submitting to me."
    show claire a talkative
    claire.say "If only there were some way, Master..."
    claire.say "Some way to mark me out as yours."
    show claire shy
    "I can sense that this is one of those really rare moments in a relationship."
    "Where things are teetering on a knife-edge, and action needs to be taken."
    "And that's when I remember that I still have something on me that I could use."
    "The necklace that I brought along to Adam's engagement party with Claire in mind."
    "Thinking that I could give it to her as a present if the chance arose to do so discreetly."
    "I never had an opportunity to do that, as the party was a pretty chaotic affair."
    "But now seems like the perfect time to whip it out and put it to use."
    mike.say "As luck would have it, Claire..."
    mike.say "I just so happen to have the very thing!"
    "Claire looks on in genuine amazement as I produce the necklace from my pocket."
    "Sure, it's not the most exquisite piece of jewellery either of us have ever seen."
    "But it's not trash either, and it's just appeared out of nowhere, as far as she's concerned."
    "So the effect is a pretty impressive one, all things considered."
    show claire talkative
    claire.say "For me, Master?"
    claire.say "To show that I'm yours?"
    show claire normal
    mike.say "Exactly, Claire..."
    mike.say "But if you accept it, that seals the deal, okay?"
    mike.say "Once this thing is around your neck, you're mine."
    mike.say "You are one hundred percent devoted to me, with total submission."
    mike.say "Do you understand?"
    "Claire nods her head desperately, refusing to raise her eyes as she does so."
    "Hands clasped together in front of her, almost like she's praying."
    show claire careless
    claire.say "Yes, Master..."
    claire.say "I understand completely."
    claire.say "And I want nothing more than that - to be yours!"
    show claire c normal
    "I step behind Claire and unfasten the necklace, noting that she holds her breath."
    "It only takes a few seconds to put the thing around her neck and fasten it again."
    "Yet as soon as it's in place, Claire lets out a dramatic sight and her shoulders sag."
    "As if she's been holding her breath for as long as physically possible."
    show claire careless
    claire.say "Aaah…"
    show claire eating
    claire.say "Mmm…"
    "I can certainly understand Claire's reaction to what just happened."
    "Because the air feels somehow thicker and heavier with emotion to me too."
    "And I know that it's not just in my head either."
    "As my cock is threatening to snap the elastic in the waistband of my shorts right now!"
    "So, with that in mind, my thoughts turn to experimenting with my newly collared toy."
    show claire normal
    mike.say "Okay, Claire..."
    mike.say "Let's try a little experiment, yeah?"
    "Claire looks back over her shoulder at me, eyes wide with expectation."
    "And I get the impression that she's working hard to keep from saying a word."
    "The only response that I get from her being an eager nod."
    mike.say "I want you to take off your panties, right now."
    "For a moment I think that Claire's going to refuse the command."
    "Or at least that she's going to challenge me on the specific details of it."
    "But the she surprises me by bending over and reaching under her skirt."
    "And then I watch with mounting excitement as she proceeds to obey me."
    "Pulling down her panties and letting them drop around her ankles."
    "Claire steps out of them and then stoops to pick them up."
    "And as she does so, I see the briefest flash of something between her legs."
    "Something that inspires the next thing that comes out of my mouth."
    mike.say "No, Claire..."
    mike.say "Don't get up."
    mike.say "Get down on your hands and knees instead."
    show expression f"bg {game.room}" at center, traveling(1.2, 0.5, (640, 720))
    show claire at center, traveling(2.8, 0.5, (640, 720))
    pause 0.5
    show claire at center, zoomAt(2.8, (640, 720))
    "Quick as a flash, Claire hurries to do as she's told."
    "And soon enough, she's down on all fours in front of me."
    "Her eyes follow me as I start to walk slowly around her, taking it all in."
    "My mind racing, still trying to come to terms with just how obedient she's being."
    mike.say "Now I want you to play with yourself."
    mike.say "Put your hand between your thighs and play with your pussy."
    mike.say "Finger yourself so that I can see the look on your face."
    "Claire's still looking me straight in the eye as I tell her all of this."
    "And I can't begin to imagine the thoughts that are racing through her head right now."
    "But I make sure to keep my expression firm and not to blink as I wait for her to comply."
    "Because if this is going to work, then she needs to obey me without question."
    "Even when she's being asked to do something as extreme as this."
    "I watch with fascination as Claire lifts one of her hands from the floor."
    "And then uses it to reach under her skirt for a second time."
    show claire careless
    claire.say "Ah..."
    claire.say "Mmm…"
    show claire at hshake
    claire.say "F...fuck..."
    "Claire's eyes close as her mouth opens, lips parting to moan."
    "I can't see what her hand is doing underneath her skirt."
    "But I can see the way that her whole body is starting to quiver."
    "Claire's thighs shake as she strokes her own pussy in front of me."
    "Every pass making her more aroused and caught up in the act."
    "Where before there was the flush of embarrassment on her cheeks, now there's something else."
    "A more intense and submissive kind of acceptance of what she's doing and its implications."
    "As if she's truly coming to terms with what it means to be a true submissive."
    "And it looks like she could make herself climax from her efforts at any moment."
    "A thought that spurs me into action, not wanting to remain a passive observer any longer."
    "So much so that I have my flies unzipped before the first word is out of my mouth."
    mike.say "Hold it right there, Claire..."
    mike.say "I told you to play with yourself..."
    mike.say "But I didn't give you permission to make yourself cum."
    mike.say "That's a privilege that I'm keeping for myself."
    "I'm down on my knees now, right behind Claire."
    "Reaching out to take hold of her as I explain what I'm planning to do."
    mike.say "So I'm going to lift up your skirt."
    mike.say "And then I'm going to fuck you."
    mike.say "I'm going to fuck you until you cum."
    show claire naked with dissolve
    "Claire lets out a yelp as my hands flip up her skirt, then grab her by the haunches."
    "But she makes no effort to resist as I pull her backwards a moment later."
    "In fact she nods her head, pushing her backside towards me as much as she can."
    "I'm already achingly hard by now, my cock between her thighs."
    "And the moment that I feel it make contact with her pussy, I can't help smiling."
    "Because Claire's previous efforts have done all the work for me."
    "So the only thing that's left is to pull her backwards as I thrust forwards."
    "There's almost no resistance there as my cock slides straight into Claire."
    "She's wet, soft and totally yielding, pussy spreading to let me all the way in."
    "But that doesn't mean I'm planning on doing this in a laid-back manner."
    "Oh no, because all the exertion that would have gone into getting inside is now fuelling my movements."
    "And instantly I begin to thrust in and out of Claire with increasing speed and intensity."
    "Luckily for her, she's already worked herself up into a state of arousal."
    "So the sudden rush of sensation doesn't totally overwhelm her senses."
    "Instead it merely serves to keep the same level of stimulation going."
    "There's on art or poetry to what I'm doing, just basic, animal lust."
    "I've watched Claire submit to my will, and now I'm taking that to the only logical conclusion."
    "I'm sealing the deal by mounting her and claiming her as mine, demonstrating my dominance."
    "And the sentiment doesn't seem to be lost on her, as she lowers her head almost to the floor."
    "At the same time, Claire raises her ass in the air, presenting herself to me with nothing held back."
    "The sounds that she's making don't even vaguely resemble words any longer."
    "More the guttural sounds of an animal caught in the middle of rutting."
    "Of course there's no way for me to pace myself either, not in such a headlong rush."
    "And so with an animalistic grunt of my own, I suddenly explode inside of Claire."
    "Shooting my load into her until she's full, and the excess spurts out of her pussy."
    "Then runs down the inside of her thighs and onto the floor by her knees."
    "Exhausted, I let go of Claire and fall backwards onto my ass."
    "I hear her whimper as my cock is pulled out of her pussy in the process."
    "And then she collapses too, falling sideways and curling into a ball."
    "From there, Claire crawls slowly around and towards me, reaching out until I embrace her."
    "Then she burrows herself into my arms, clinging onto me as if her life depended on my touch."
    scene expression f"bg {game.room}"
    show claire a talkative
    with fade
    claire.say "Now you really are my master..."
    claire.say "And I need you to guide me always."
    claire.say "To show me the way!"
    $ claire.sub += 10
    show claire normal
    call stop_all_sfx from _call_stop_all_sfx_70
    scene bg black with fade
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
