init python:
    
    Event(**{
        "name": "dwayne_female_event_01",
        "label": "dwayne_female_event_01",
        "duration": 1,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                IsActivity("None"),
                ),
            PersonTarget(mike,
                Not(IsHidden()),
                HasRoomTag("work"),
                MinStat("love", 30),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_event_02",
        "label": "dwayne_female_event_02",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_event_01"),
            HeroTarget(
                IsGender("female"),
                Or(
                    IsRoom("map"),
                    HasRoomTag("street"),
                    ),
                ),
            PersonTarget(dwayne,
                HasRoomTag("street"),
                Not(IsHidden()),
                MinStat("love", 20),
                ),
            ],
        "do_once": True,
        })
    
    
    Event(**{
        "name": "dwayne_female_event_03",
        "label": "dwayne_female_event_03",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_event_02"),
            HeroTarget(
                IsGender("female"),
                IsRoom("date_nightclub"),
                ),
            PersonTarget(mike,
                OnDate()
                ),
            PersonTarget(dwayne,
                IsRoom("vip"),
                Not(IsHidden()),
                MinStat("love", 40),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_event_04",
        "label": "dwayne_female_event_04",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_event_03"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                IsActivity("None"),
                ),
            PersonTarget(mike,
                Not(IsHidden()),
                HasRoomTag("work"),
                MinStat("love", 40),
                ),
            PersonTarget(dwayne,
                Not(IsHidden()),
                HasRoomTag("work"),
                MinStat("love", 60),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_event_05",
        "label": "dwayne_female_event_05",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_event_04"),
            IsNotDone("dwayne_female_event_05_alt"),
            HeroTarget(
                IsGender("female"),
                Or(
                    IsRoom("map"),
                    HasRoomTag("street"),
                    ),
                ),
            PersonTarget(dwayne,
                HasRoomTag("street"),
                Not(IsHidden()),
                MinStat("love", 80),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_event_05_alt",
        "label": "dwayne_female_event_05_alt",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_event_04"),
            IsNotDone("dwayne_female_event_05"),
            IsTimeOfDay("morning", "afternoon"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                IsActivity("None"),
                ),
            PersonTarget(dwayne,
                Not(IsHidden()),
                HasRoomTag("work"),
                MinStat("love", 80),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_preg_talk",
        "label": "dwayne_preg_talk",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                IsFlag("pregnancy_father", "dwayne"),
                Or(
                    MinCounter("pregnant", 60),
                    IsFlag("foundpreg"),
                    ),
                ),
            PersonTarget(dwayne,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })
    
    Event(**{
        "name": "dwayne_kiss_me_female",
        "label": "dwayne_kiss_me_female",
        "max_girls": 1,
        "conditions": [
            HeroTarget(IsGender("female")),
            PersonTarget(dwayne,
                Not(IsHidden()),
                IsPresent(),
                MinFlag("kiss", 1),
                MinStat("love", 150),
                ),
            ],
        "chances": 20,
        "once_day": True,
        "do_once": False,
        "quit": False,
        })
    
    
    Event(**{
        "name": "dwayne_find_out_pregnancy",
        "label": "dwayne_find_out_pregnancy",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                MinCounter("pregnant", 30),
                CounterChanceChecker("pregnant", 50)
                ),
            PersonTarget(dwayne,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],

        "do_once": False,
        })
    
    Event(**{
        "name": "dwayne_female_job_event_01",
        "label": "dwayne_female_job_event_01",
        "duration": 1,
        "conditions": [
            Or(
                IsDone("dwayne_female_event_05"),
                IsDone("dwayne_female_event_05_alt"),
                ),
            HeroTarget(
                IsGender("female"),
                IsActivity("work_office_female"),
                IsFlag("office_boss", "dwayne"),
                IsFlag("job_day", "office"),
                ),
            PersonTarget(dwayne,
                HasRoomTag("work"),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_job_event_02",
        "label": "dwayne_female_job_event_02",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_job_event_01"),
            HeroTarget(
                IsGender("female"),
                IsActivity("work_office_female"),
                IsFlag("office_boss", "dwayne"),
                IsFlag("job_day", "office"),
                ),
            PersonTarget(dwayne,
                HasRoomTag("work"),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_job_event_03",
        "label": "dwayne_female_job_event_03",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_job_event_02"),
            HeroTarget(
                IsGender("female"),
                IsActivity("work_office_female"),
                IsFlag("office_boss", "dwayne"),
                IsFlag("job_day", "office"),
                ),
            PersonTarget(dwayne,
                HasRoomTag("work"),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_job_event_04",
        "label": "dwayne_female_job_event_04",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_job_event_03"),
            HeroTarget(
                IsGender("female"),
                IsActivity("work_office_female"),
                IsFlag("office_boss", "dwayne"),
                IsFlag("job_day", "office"),
                ),
            PersonTarget(dwayne,
                HasRoomTag("work"),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "dwayne_female_job_event_05",
        "label": "dwayne_female_job_event_05",
        "duration": 1,
        "conditions": [
            IsDone("dwayne_female_job_event_04"),
            HeroTarget(
                IsGender("female"),
                IsActivity("work_office_female"),
                IsFlag("office_boss", "dwayne"),
                IsFlag("job_day", "office"),
                ),
            PersonTarget(dwayne,
                HasRoomTag("work"),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })

label dwayne_female_event_01:
    "I'm just kicking around the house, doing nothing in particular."
    "I see that it's [mike.name], so at least I'm not going to be talking to a stranger."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "[mike.name]")
    if not result:
        $ hero.cancel_event()
        $ mike.love -= 5
        return
    "And who knows, he might just have something interesting to tell me."
    "I'm certainly getting bored sitting around here with nothing to do!"
    bree.say "Hey, [mike.name]..."
    bree.say "What's up?"
    mike.say "Ah..."
    mike.say "Hey, [hero.name]..."
    "The way he's pausing and hesitating instantly sets off alarm bells."
    bree.say "Okay, [mike.name]..."
    bree.say "What do you want?"
    "[mike.name] makes a strange kind of spluttering sound on the other end."
    mike.say "Urgh..."
    mike.say "What are you talking about, [hero.name]?"
    mike.say "I didn't even say anything to you yet!"
    bree.say "Oh spare me, [mike.name]!"
    bree.say "I can tell from the tone of your voice."
    bree.say "That and the way you're being all evasive."
    mike.say "Okay, okay..."
    mike.say "You got me, [hero.name]."
    mike.say "I need you to do me a favour, yeah?"
    "I feel a warming sensation of triumph as [mike.name] admits his intentions."
    "And it makes me feel a little more inclined to indulge him as a result."
    "But maybe not enough to actually give him what he wants."
    "Speaking of which..."
    bree.say "Come on then, [mike.name]..."
    bree.say "Spit it out already!"
    mike.say "Here's the thing, [hero.name]..."
    mike.say "I left some papers on the kitchen table this morning."
    mike.say "They're super important and I need then here ASAP."
    "I glance over, seeing the papers that he must be talking about."
    bree.say "So?"
    bree.say "Just come back home and grab them."
    mike.say "I would if I could."
    mike.say "But if I do that, people are going to know I forgot them."
    mike.say "And that's going to make me look bad!"
    "I can feel the groan building up inside of me."
    "Because there's only one place this can be leading."
    bree.say "So I guess that means you need me to bail you out, huh?"
    mike.say "Please, [hero.name]!"
    mike.say "You'd be saving my life if you'd bring them to my office."
    "I think about it for a moment, weighing my options."
    "Telling [mike.name] to shove it would be pretty satisfying."
    "And it'd teach him not to be such a forgetful asshole in future."
    "But putting myself out to save his ass would mean he was in my debt."
    "And I could really use that kind of leverage around here."
    menu:
        "Fine":
            "What the hell."
            "I'm not really doing anything right now."
            bree.say "Okay, [mike.name]."
            bree.say "But you owe me big time for this!"
            mike.say "Thanks, [hero.name]."
            mike.say "I'll make it up to you, I promise."
            "I shake my head as I end the call."
            "He sure better make it up to me!"
            "Grabbing the papers, I head out of the house."
            scene bg street with fade
            "I actually make good time in getting to [mike.name]'s office building."
            scene bg office with fade
            "But as I walk into the place, I realise there's a problem."
            "I have absolutely no idea where [mike.name]'s office actually is."
            "I think about calling him back."
            "But then I see the reception desk in the lobby."
            "They should be able to tell me where to find him."
            "Or maybe they can take the papers to him for me."
            "I start towards the reception desk."
            "But then I find my way blocked by a tall guy that's build like a brick wall."
            show dwayne with dissolve
            dwayne.say "Excuse me, miss..."
            dwayne.say "But I couldn't help noticing that you look a little lost."
            show dwayne smile
            dwayne.say "My name's Dwayne."
            "I look up at the guy's face, which is broad, with a beaming smile."
            "And I almost blush as I realise that he's handsome."
            "By which I mean he's REALLY handsome!"
            if hero.morality >= 25:
                bree.say "Oh...I..."
                bree.say "Y...yeah, I'm looking for someone."
                bree.say "Do you know a guy called [mike.name]?"
            if hero.morality <= -25:
                bree.say "Not anymore..."
                bree.say "I think I found what I'm looking for!"
                bree.say "Urgh...wait a minute - I have to find [mike.name]!"
                bree.say "Do you know him?"
            "Dwayne nods."
            show dwayne -smile
            dwayne.say "Sure I do!"
            dwayne.say "I know everyone here - you have to when you're the boss!"
            show dwayne smile
            "As he says this, Dwayne's smile becomes even bigger."
            "Now it's showing off his huge, perfectly aligned teeth."
            "And I guess I'm supposed to be impressed that he's the boss."
            show dwayne -smile
            dwayne.say "Nerdy guy, spiky hair, kinda goofy?"
            dwayne.say "That's the one, right?"
            "It's an accurate description of [mike.name], I guess."
            "But not a very flattering one."
            bree.say "I think that's him."
            bree.say "My name's [hero.name], I'm his housemate."
            bree.say "I need to get these papers to him."
            bree.say "It's kind of an emergency!"
            dwayne.say "That sounds just like the [mike.name] I'm thinking of."
            show dwayne annoyed
            dwayne.say "He's always screwing stuff up around here."
            dwayne.say "Sometimes I think that's why I don't fire his ass."
            dwayne.say "I'm too eager to see what he'll fuck up next!"
            menu:
                "He's my friend!":
                    bree.say "Hey!"
                    bree.say "I don't think you should talk about [mike.name] like that."
                    bree.say "He might have his faults, but he's a good person!"
                    show dwayne -annoyed
                    "Dwayne backs off a little as I chide him."
                    "And he raises a quizzical eyebrow too."
                    "I can sense his demeanour changing."
                    "Like he's realising he misjudged the situation."
                    dwayne.say "Oh, come on, [hero.name]."
                    dwayne.say "That was all just banter."
                    dwayne.say "If [mike.name] were here, he'd be laughing too."
                    "I shoot a sideways glance at Dwayne, not totally convinced."
                    "But I decide that the best thing is to let it go."
                    "After all, I just need to drop off the papers."
                    "Not to get involved in an argument with [mike.name]'s boss."
                "Imagine living with him!":
                    bree.say "You should be grateful you don't have to live with him."
                    bree.say "He's just as bad at home - maybe worse!"
                    show dwayne smile
                    show dwayne at startle(0.14,-20)
                    pause 0.2
                    show dwayne at startle(0.14,-20)
                    pause 0.2
                    show dwayne at startle(0.14,-20)
                    "Dwayne bellows with laughter."
                    "Evidently he's delighted that I agree with him."
                    dwayne.say "Oh really?"
                    dwayne.say "It's that bad?"
                    "I nod as I feel myself getting into my flow."
                    "It's hard to resist Dwayne's charm."
                    "And I feel like all of his attention is focused on me right now."
                    bree.say "Yeah, he's terrible!"
                    bree.say "Leaves his dirty shorts around the house."
                    bree.say "Never does his share of the housework."
                    bree.say "And the state of the bathroom when he's been in there - eww!"
                    show dwayne smile
                    show dwayne at startle(0.14,-20)
                    pause 0.2
                    show dwayne at startle(0.14,-20)
                    pause 0.2
                    show dwayne at startle(0.14,-20)
                    "Dwayne throws his head back and laughs again."
                    dwayne.say "HA!"
                    dwayne.say "What an asshole!"
            bree.say "So..."
            bree.say "You were going to tell me where I can find [mike.name]?"
            show dwayne smile
            "Dwayne's smile becomes extra large again."
            "And he holds out his hand."
            dwayne.say "Let me take those."
            show dwayne -smile
            dwayne.say "I can pass them to him myself."
            menu:
                "Give him the papers":
                    "I think about it for a moment."
                    "And then I nod as I had the papers over."
                    if hero.morality >= 25:
                        bree.say "I suppose that makes sense."
                        bree.say "You must know this place better than me!"
                    if hero.morality <= -25:
                        bree.say "What a gentleman!"
                        bree.say "You really know how to treat a lady, Dwayne."
                    dwayne.say "My pleasure, [hero.name]."
                    show dwayne smile
                    dwayne.say "And it was a pleasure to meet you too."
                    hide dwayne with easeoutleft
                    "Dwayne winks as he turns and walks away."
                    "Which leaves me free to head home."
                "I'll give them to [mike.name]":
                    "I almost hand the papers straight over to Dwayne."
                    "But then I pull my hand back and shake my head."
                    bree.say "No, Dwayne."
                    bree.say "[mike.name] asked me to bring them straight to him."
                    bree.say "I'm sure you're just trying to help."
                    bree.say "But he said they were important."
                    bree.say "So he might not want anyone else to see them."
                    "I can see that Dwayne wants to challenge me."
                    "But something makes him think better of it."
                    "And he backs off, nodding as he does so."
                    dwayne.say "Whatever you say, [hero.name]."
                    dwayne.say "Let me fill you in on where to find him..."
                    scene bg door office private at center, zoomAt(1, (640, 720)) with fade
                    "Dwayne points me in the right direction."
                    show bg door office private at center, traveling(1.5, 0.3, (640, 1040))
                    pause 0.3
                    play sound door_knock
                    "And I soon find myself knocking on the door of [mike.name]'s office."
                    bree.say "[mike.name]!"
                    bree.say "Are you in there?"
                    scene bg black with dissolve
                    pause 0.5
                    scene bg personal
                    show mike work
                    with wipeleft
                    "The door opens and I see [mike.name]'s face peeking out."
                    "At first he looks anxious and harassed."
                    "But as soon as he sees the papers in my hand, he seems to calm down."
                    show mike happy
                    mike.say "Oh, [hero.name]!"
                    mike.say "Thank god you made it!"
                    if hero.morality >= 25:
                        bree.say "No worries, [mike.name]."
                        bree.say "I got here as soon as I could."
                    if hero.morality <= -25:
                        bree.say "Yeah, I really saved your ass."
                        bree.say "So remember, you owe me one."
                        bree.say "I'll just have to think how you can repay me!"
                    show mike normal
                    "[mike.name] hurries back into his office, desperate to get back to work."
                    "Which leaves me with nothing to do but start making my way back home."
            $ dwayne.unhide()
        "No (Never meet Dwayne again)":
            "Ah, screw it."
            "I don't need to be able to lord it over [mike.name] that badly."
            bree.say "Nah, I don't think so, [mike.name]."
            bree.say "If you need them that badly, you can come get them yourself."
            mike.say "[hero.name]!"
            mike.say "Are you serious?"
            mike.say "I really need your help here!"
            "It sounds bad, but I'm actually enjoying the sound of [mike.name] squirming."
            "But I can't keep him hanging on forever."
            bree.say "Well you're not going to get it."
            bree.say "Why don't you try calling Sasha?"
            bree.say "Or send one of those bimbos you work with the get the papers?"
            bree.say "You're always bragging about how they hang on your every word."
            $ mike.love -= 10
            "With that final jab, I end the call."
            "[mike.name] tries to call back a moment later."
            "But I let it go to voicemail."
            "And I let him handle his own problems too."
    return

label dwayne_female_event_02:
    if dwayne.love.max <= 40:
        $ dwayne.love.max = 40
    scene expression f"bg {game.room}"
    "I normally wouldn't give a second glance to a big, expensive car passing me on the street."
    "Because sure, they look impressive - but once you've seen a couple, you kind of get used to it."
    "If a limo passes you, then you know it's going to have some rich douche inside of it."
    "Or worse, it's been hired to drive a load of drunk girls around on a hen party."
    "So when one drives past as I'm making my way down the sidewalk, I hardly look up."
    "It's only when I see that it's actually pulled up a little ahead that I begin to pay attention."
    "But even then I'm only doing that so I can look at the black glasses hiding the passenger at the back of the car."


    show dwayne carwindow date up with fade
    "This makes me slow down a little, and pay closer attention."

    "As I draw level with the limo and the window starts to go down, I take the chance to look inside."
    show dwayne carwindow middle with dissolve
    "And as soon as I do so, I recognise the person sitting in the back."
    bree.say "Dwayne?"
    show dwayne carwindow down with dissolve
    dwayne.say "Hello there, [hero.name]!"
    dwayne.say "How are you doing?"
    "I can't bring myself to answer the question straight away."
    "And that's because I'm still surprised to see someone I know in a limo."
    "Even if it is a guy that can probably afford it."
    bree.say "I...I'm good, Dwayne."
    bree.say "And you..."
    if hero.morality >= 25:
        bree.say "You're looking...prosperous?"
    if hero.morality <= -25:
        bree.say "You're looking like a true alpha!"
    "Dwayne nods happily, showing off that million-dollar smile of his."
    dwayne.say "What can I say, [hero.name]."
    dwayne.say "Times are good and I'm reaping the profits!"
    "I nod slowly, still wondering what's going on here."
    if hero.morality >= 25:
        bree.say "So..."
        bree.say "Was there something I can do for you?"
    if hero.morality <= -25:
        bree.say "Now then, big guy..."
        bree.say "Is there something I can do for you?"
        bree.say "Or do to you?"
    "Dwayne nods again."
    dwayne.say "I was just on my way to grab a bite to eat, [hero.name]."
    dwayne.say "Then I saw you as we were driving past."
    dwayne.say "And I thought that I should share a little of my prosperity with you."
    dwayne.say "So how about it?"
    dwayne.say "You want to hop in and come for a meal?"
    "At first I don't know what to say."
    "This isn't the kind of thing that happens to me on a regular basis - or ever!"
    "But then I regain a measure of control, and I know what my answer should be."
    menu:
        "I can eat something":
            $ dwayne.love += 2
            "I know that this could look a little sketchy to some people."
            "But all Dwayne's asking me to do is go grab some food with him."
            "Plus it's not like I don't know the guy, because we already met."
            "And I also know where he works, that he's the boss of a big company."
            "Surely I can trust him knowing all that?"
            if hero.morality >= 25:
                bree.say "That's so kind of you, Dwayne."
                bree.say "I'd love to go to dinner with you."
            if hero.morality <= -25:
                bree.say "How can I refuse an offer like that?"
                bree.say "A guy like you always gives me an appetite!"
            scene expression f"bg {game.room}" zorder 1 at center, zoomAt (1.25, (640, 330))
            show dwayne limo dwayne ddate right zorder 2
            "Dwayne smiles happily and pats the seat beside him."
            show dwayne limo bree date
            with vpunch
            "Then he makes a little more room as I hop in and sit down."
            play sound car_door
            "As the chauffeur closes the door, I notice that there's plenty of space."
            "Which means that I don't really need to be sitting so close to Dwayne."
            if hero.morality >= 25:
                "But it seems rude to move now that I'm sat down."
            if hero.morality <= -25:
                "But I'm enjoying the chance to get so close to him."
            "So I stay put as the limo pulls away from the sidewalk."
            "Dwayne leans back against the seat as we get moving."
            "And he stretches his arms, as though trying to work out a kink."
            "He's not going to..."
            "He wouldn't be so obvious, would he?"
            "I watch as Dwayne then tries to settle an arm over my shoulders."
            "At the last moment I make a point of moving."
            scene expression f"bg {game.room}" zorder 1 at center, zoomAt (1.5, (540, 420))
            show dwayne limo as limo zorder 2 at center, zoomAt(1.75, (420, 1220))
            show dwayne annoyed date zorder 3 at center, zoomAt(1.75, (840, 1220))
            "This means that he's forced to abort the manoeuvre."
            "And instead he settles his arm on the back of the seat."
            show dwayne -annoyed
            dwayne.say "Trust me, [hero.name]..."
            dwayne.say "You're going to love this place."
            dwayne.say "I take girls to get eaten out here all the time!"
            if hero.morality >= 25:
                bree.say "WHAT?!?"
                bree.say "Don't you mean you take girls to eat out here all the time?"
            if hero.morality <= -25:
                bree.say "To get eaten out, huh?"
                bree.say "That sounds like a lot of fun!"
            dwayne.say "Oh, sorry!"
            dwayne.say "Slip of the tongue, [hero.name]!"
            "Dwayne's words might sound sincere."
            show dwayne smile
            "But he winks at me as he says them."
            "And makes a point of licking his lips too."
            scene bg door restaurant with fade
            "Soon enough we arrive at the restaurant."
            "The chauffeur opens the door and Dwayne leads me inside."
            scene bg restaurant with fade
            "We're greeted by a smartly-dressed waiter."
            "But Dwayne doesn't give the man a chance to speak."
            show dwayne date at right5 with easeinright
            dwayne.say "I want my usual table."
            dwayne.say "And bring us over some oysters while we look at the menu."
            "Ouch - that wasn't a request."
            "It sounded more like an order!"
            "But much to my surprise, the waiter just nods and shows us to the table."
            show dwayne at center with ease
            "Dwayne pulls out my chair for me, then sits down and gestures around us."
            scene bg black
            show restaurant meal dwayne
            with fade
            dwayne.say "Well?"
            dwayne.say "What do you think?"
            if hero.morality >= 25:
                bree.say "This place is amazing."
                bree.say "It must be very expensive!"
            if hero.morality <= -25:
                bree.say "This is SO fancy, Dwayne!"
                bree.say "A girl could get used to this kind of thing!"
            "As we're talking, the waiter returns to the table."
            "He deposits a plate of oysters."
            "But he also produces what looks like a bottle of champagne."
            "Dwayne takes this and pops the cork, making me jump."
            "Then he starts to pour two glasses."
            menu:
                "Ooh champagne!":
                    "I take the glass that Dwayne offers me."
                    "And hold it up when he proposes a toast."
                    dwayne.say "To new friends."
                    show restaurant meal dwayne blush
                    dwayne.say "And who knows, maybe more!"
                    if hero.morality >= 25:
                        bree.say "Erm...friends for sure."
                        show restaurant meal dwayne -blush
                        bree.say "I don't know about anything else..."
                    if hero.morality <= -25:
                        bree.say "Of hell yeah!"
                        bree.say "And I hope a lot more."
                        show restaurant meal dwayne happy
                        bree.say "You know what I mean?!?"
                    $ dwayne.love += 2
                    $ hero.set_flag("drinks", 1, "day", mod="+")
                "Just water please":
                    "I quickly reach out and cover my glass with a hand."
                    "And Dwayne only just manages to keep from pouring champagne over it."
                    bree.say "Not for me, thanks."
                    bree.say "I'll just stick with water."
                    show restaurant meal dwayne bored
                    $ dwayne.sub += 1
                    "I can see that Dwayne looks disappointed with this."
                    "But he still keeps his manners in check, nodding in response."
                    dwayne.say "Sure, [hero.name]."
                    show restaurant meal dwayne happy
                    dwayne.say "Maybe you'll feel like one later."
                    bree.say "Or maybe not!"
            "I turn my attention to the menu next."
            show restaurant meal dwayne -happy
            "But then I see that the entire thing is in French!"
            bree.say "Erm..."
            bree.say "I think we got the wrong menu."
            bree.say "Can we get one in English?"
            dwayne.say "This is a REALLY fancy restaurant, [hero.name]."
            dwayne.say "Trust me, they don't have it in English."
            dwayne.say "Would you like me to order for you?"
            menu:
                "Yes, please":
                    "Basically I can let my pride get the better of me."
                    "Which means there's a risk of ordering something vile."
                    "Or I can swallow it and let Dwayne order for me."
                    "And I choose the latter, so shoot me!"
                    bree.say "Yeah..."
                    bree.say "I think that might be the best thing."
                    "Dwayne looks almost surprised by my answer."
                    "Like he was expecting me to be more stubborn."
                    show restaurant meal dwayne happy
                    "But he shakes it off quickly and orders."
                    "I have no idea what he's asked for."
                    "So once the waiter's out of earshot, I have to ask."
                    bree.say "What was that?"
                    dwayne.say "I just ordered the fish, [hero.name]."
                    show restaurant meal dwayne -happy
                    dwayne.say "Trust me, you'll love it."
                    $ dwayne.love += 1
                    $ dwayne.sub -= 1
                    "And when the food arrives, I have to admit that he's right."
                    "It's some of the best damn fish I've ever had."
                "I'll do it by myself":
                    "The mere suggestion of having Dwayne order for me gets my blood boiling."
                    bree.say "I most certainly do not!"
                    bree.say "I can order my own food, thank you!"
                    show restaurant meal dwayne bored
                    $ dwayne.sub -= 2
                    "Looking down the menu, it seems pretty hopeless."
                    "So I just pick something at random and hope for the best."
                    bree.say "I'll have the..."
                    bree.say "Es...car...got?"
                    "Waiter" "The escargot, madam?"
                    "Waiter" "Really?"
                    "I nod and smile."
                    "Which gets me the same in return."
                    show restaurant meal dwayne -bored
                    "When our food turns up, I notice Dwayne watching me closely."
                    dwayne.say "How is it, [hero.name]?"
                    bree.say "Mmm..."
                    bree.say "Kind of chewy...but nice!"
                    "Dwayne chuckles to himself and shakes his head."
                    show restaurant meal dwayne happy
                    "I think about asking him what's up."
                    "But then I decide to leave it alone and just enjoy my meal."
            $ game.pass_time(1)
            scene bg restaurant
            show dwayne date
            with fade
            "Once we're done, Dwayne takes care of the bill."
            "And there's no way I'm going to argue about splitting it."
            "Not in a place as fancy as this!"
            scene expression f"bg {game.room}" zorder 1 at center, zoomAt (1.5, (540, 420))
            show dwayne limo as limo zorder 2 at center, zoomAt(1.75, (420, 1220))
            show dwayne annoyed date zorder 3 at center, zoomAt(1.75, (840, 1220))
            with fade
            play sound car_door
            "Soon we're back in the limo and he's dropping me off where he picked me up."
            show dwayne shout
            dwayne.say "I had a good time with you, [hero.name]."
            dwayne.say "We should do this again."
            show dwayne annoyed
            menu:
                "I'd like that":
                    if hero.morality >= 25:
                        bree.say "Me too, Dwayne."
                        bree.say "We should definitely do it again."
                        bree.say "And soon too!"
                    if hero.morality <= -25:
                        bree.say "I had a great time, Dwayne."
                        bree.say "Maybe we could do something more private next time?"
                        bree.say "And more intimate too!"
                    show dwayne smile
                    "Dwayne nods and smiles."
                    dwayne.say "Now I like the sound of that!"
                    $ dwayne.love += 2
                    play sound car_door
                    scene bg black
                    show dwayne carwindow date up
                    with hpunch
                    "I hop out of the limo and wave goodbye as it pulls away."
                    scene expression f"bg {game.room}" with fade
                    "And just like that, I'm back to my normal life."
                "I'll think about it":
                    bree.say "I don't know about that, Dwayne."
                    bree.say "Maybe we need to leave it a while."
                    show dwayne shout
                    "Dwayne opens his mouth to protest."
                    play sound car_door
                    scene bg black
                    show dwayne carwindow date up
                    with hpunch
                    "But I hop out and walk away before he can speak."
                    $ dwayne.sub += 1
                    scene expression f"bg {game.room}" with fade
                    "Maybe this way he'll finally take the hint."
        "Nah, I'm not hungry":
            "There's nothing about this that doesn't seem sketchy."
            "Like I'm supposed to believe that Dwayne just happened to be driving past."
            "And he just happened to spot me amongst all the other people on the sidewalk."
            "Also, I'm sure I remember being told something about not getting into cars with strange men!"
            bree.say "Thanks for the offer, Dwayne."
            bree.say "But I already had lunch."
            "Dwayne's smile fades a little."
            $ dwayne.love -= 4
            "And I can see that he looks a tad confused."
            "I guess this guy's not used to being told no."
            dwayne.say "Don't screw around, [hero.name]."
            dwayne.say "Just jump in and let me take you for a ride."
            dwayne.say "I only patronise the finest restaurants in town."
            bree.say "I already told you that I've eaten."
            bree.say "So why would I want to go to a restaurant with you?"
            dwayne.say "Forget about the restaurant, [hero.name]."
            dwayne.say "We can go someplace else - anywhere you want!"
            "I force a smile onto my face and shake my head."
            bree.say "I'm going to have to pass, Dwayne."
            bree.say "See you around."
            scene expression f"bg {game.room}" with fade
            $ dwayne.sub += 2
            "With that I make a point of turning my back on him."
            "And I walk off down the street without a backwards glance."
            "For a moment I'm worried that Dwayne will just follow me."
            "Even that he'll keep on harassing me from the open window of the limo."
            "But to my relief, I see the car drive past and then take a turn up ahead."
            "I guess that's the key with a guy like Dwayne."
            "You just have to be firm with them and stick to it."
    scene bg black with dissolve
    return

label dwayne_female_event_03:
    $ dwayne.flags.nokiss = False
    scene bg nightclub
    "It's been one of those weeks when you think the shit's never going to end."
    "But I've finally made it through the worst, and so it's time to let off some steam."
    "Luckily for me I'm not alone, [mike.name] feels like he's in the same boat as me."
    "So when he suggested that we hit a nightclub together, I jumped at the chance."
    "Now we're here, drinks in hand and surveying the crowded dancefloor."
    "There's a great atmosphere in the place tonight."
    "So we should have an equally great time."
    show mike date normal with dissolve
    mike.say "So..."
    mike.say "You want to dance?"
    bree.say "Oh yeah!"
    bree.say "But I just want to wait for the right track, okay?"
    mike.say "Yeah, I..."
    show mike surprised
    "Shady guy" "Ahem..."
    "Shady guy" "Excuse me..."
    show mike annoyed at left
    show victor at flip, right4, blacker
    with easeinright
    "[mike.name] and I turn around at the same moment."
    "And we see a well-dressed guy standing behind us."
    bree.say "Erm..."
    bree.say "Are you talking to us?"
    "The guy nods."
    "Shady guy" "To be more precise, I'm talking to you, madam."
    "Shady guy" "I've been asked to extend an invite to the VIP section."
    show mike surprised
    mike.say "Whoa..."
    mike.say "Have you seen the VIP section in this place, [hero.name]?"
    show mike down
    mike.say "You can't turn down an offer like that!"
    if hero.morality >= 25:
        bree.say "I don't know, [mike.name]..."
        bree.say "Maybe we can just go check it out?"
        bree.say "So long as you stay with me, okay?"
    if hero.morality <= -25:
        bree.say "Of course I'm going to accept the offer, [mike.name]!"
        bree.say "I've heard about the things that go on in there."
        bree.say "And I want to get in on it myself!"
    show mike normal at center
    show victor at flip, top_mostright, blacker
    with ease
    "[mike.name] and I follow the guy across the club."
    show mike at right5
    show victor at flip, top_mostright, blacker
    with ease
    "And he leads us straight to the VIP section."
    "He lifts the cord that ropes it off from the rest of the club, then stands to the side."
    "Then I walk through and [mike.name] makes to follow me."
    "But before he can step through, the guy put a hand on his chest."
    show mike angry at hshake
    mike.say "Hey!"
    bree.say "Yeah, what are you doing?"
    "Shady guy" "Sorry, sir."
    "Shady guy" "But the invitation was for the lady, not you."
    show mike surprised at right4 with ease
    "I turn back to [mike.name], realising what this means"
    "But he speaks up before I can say anything."
    show mike normal
    mike.say "You're not going in there without me..."
    mike.say "Are you, [hero.name]?"
    menu:
        "Wait for me here":
            if dwayne.love.max <= 60:
                $ dwayne.love.max = 60
            "I shrug and walk further into the VIP section."
            if hero.morality >= 25:
                bree.say "Don't worry, [mike.name]."
                bree.say "I won't be long."
                bree.say "I'm just curious to see who invited me, that's all."
            if hero.morality <= -25:
                bree.say "Of course I am, [mike.name]."
                bree.say "You said it yourself..."
                bree.say "I CAN'T turn down an offer like that!"
            "[mike.name] doesn't look pleased with my choice or my explanation."
            "And he pretty much starts to sulk as soon as it sinks in."
            show mike angry
            $ mike.love -= 5
            mike.say "If that's what you want to do, then fine."
            mike.say "But don't be surprised if I'm not here when you get back!"
            if hero.morality >= 25:
                "I almost change my mind as I hear [mike.name]'s words."
                "But then I reason that I can be super quick."
                "And he can't go far in that time, so it should be okay."
            if hero.morality <= -25:
                "I shake my head and snort a laugh at [mike.name]'s reaction."
                "He's just being childish because he's jealous."
                "And I bet he won't go far, because he'll want to know what happened."
            scene bg vip with fade
            "I follow the guy that lead me here until he reaches a private booth."
            "And it's then that I see a familiar face sitting inside."
            show dwayne date at center, zoomAt (1.0, (640, 740)) with dissolve
            bree.say "Dwayne?"
            dwayne.say "The very same, [hero.name]!"
            "Dwayne's alone in the booth, leaning back and smiling."
            "And he's holding a glass of champagne, which he offers to me."
            dwayne.say "I saw you come in and I thought you might want to join me."
            dwayne.say "It's much nicer in here, away from all the scum."
            show dwayne smile
            dwayne.say "Don't you think?"
            menu:
                "Stay a while":
                    "I guess one little glass of champagne can't hurt."
                    "So I put on a smile as I take it and sit down."
                    "Dwayne seems to take this as some kind of personal victory."
                    "As his own smile becomes broader still."
                    "And somehow his teeth seem bigger and whiter than ever."
                    dwayne.say "There you go, [hero.name]."
                    dwayne.say "That wasn't so hard, was it?"
                    "I find that all I can do in response is shake my head."
                    "Because the champagne is really nice."
                    "Probably the best that I've ever had."
                    "And the booth is nice too."
                    "Far nicer than having to stand in the crowded part of the nightclub."
                    show dwayne -smile
                    if hero.morality >= 25:
                        bree.say "Thanks for the champagne, Dwayne."
                        bree.say "But I'm still not sure what I'm doing here."
                        bree.say "If you saw me come in, then you had to see [mike.name] too."
                        bree.say "And you must know that we're here on a date!"
                    if hero.morality <= -25:
                        bree.say "Okay, Dwayne..."
                        bree.say "What do you want?"
                        bree.say "And your answer had better be good."
                        bree.say "Because you're in danger of costing me a ride on [mike.name]'s cock tonight!"
                    show dwayne smile
                    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
                    pause 0.2
                    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
                    pause 0.2
                    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
                    "Dwayne lets out a booming laugh at the mere mention of [mike.name]'s name."
                    "He shakes his head like it's the funniest thing imaginable."
                    dwayne.say "Who cares about that loser, [hero.name]?"
                    show dwayne smile
                    dwayne.say "You obviously don't if you came in here without him!"
                    dwayne.say "I invited you in here because you're better than he is, [hero.name]."
                    dwayne.say "You deserve to be here in the VIP section."
                    dwayne.say "You deserve to be in here with a guy like me."
                    menu:
                        "Go back to [mike.name]":
                            "I might have been willing to indulge Dwayne had he been nicer about it."
                            "But he just basically called [mike.name] scum and a loser!"
                            bree.say "You can keep your champagne, Dwayne."
                            bree.say "And you can keep your VIP section too!"
                            show dwayne annoyed
                            bree.say "I came here to spend time with [mike.name], not you."
                            "The moment I'm done talking, I toss the champagne in his face."
                            "Dwayne splutters and gasps, his expression becoming enraged."
                            "But I've already turned my back and begun to walk away."
                            hide dwayne
                            scene bg nightclub
                            show mike date
                            with fade
                            "[mike.name] sees me coming and smiles."
                            "But then he sees Dwayne waving his fist in the air."
                            mike.say "It was Dwayne?!?"
                            mike.say "Oh man..."
                            show mike down
                            mike.say "He looks pissed!"
                            bree.say "Never mind him."
                            bree.say "He's been drinking too much champagne."
                            show mike happy
                            bree.say "And I think the bubbles have gone up his nose..."
                            $ mike.love += 5
                            $ game.active_date.score += 30
                        "Stay just a little longer":
                            show dwayne -smile
                            if hero.morality >= 25:
                                "I do the best I can to look like I'm listening."
                                "But at the same time I'm trying not to look like I agree."
                                "Maybe if I work on him, I can get Dwayne to change his mind."
                                "Maybe I can convince him [mike.name]'s not a loser after all."
                            if hero.morality <= -25:
                                "I can't help laughing and nodding."
                                "Dwayne's flattering me for sure."
                                "But he's the kind of guy that's worth indulging."
                                "And I owe it to myself to see where this is going."
                            "Dwayne seems to be really liking the way this is going."
                            show dwayne at center, zoomAt(1.5, (640, 1040)) with dissolve
                            "He's closed the short distance between us, pressing up close to me."
                            "And I can tell from the look on his face that he's briming with confidence."
                            dwayne.say "It's not just the champagne and comfy seats that make this this place special."
                            dwayne.say "You know that, [hero.name]?"
                            dwayne.say "It's that these booths are totally private."
                            dwayne.say "You can literally do whatever you want in here, and nobody'd ever know."
                            show dwayne smile
                            dwayne.say "Even the management would turn a blind eye."
                            "It's just as Dwayne's finished speaking that I feel something on the back of my neck."
                            "And it doesn't take a genius to realise that it's the hand not holding the champagne glass."
                            "At first it just feels like he's caressing me, trying to get me used to physical contact."
                            "That's unexpected for sure, but nothing I can't handle."
                            "But then I feel him begin to apply pressure, pushing me forwards."
                            "At the same time I hear him put his glass down on the table."
                            "And a quick glance shows me that his other hand is now headed for his groin."
                            "Which is the exact same place that he's currently trying to guide my head!"
                            "Instinctively I stiffen up and resist."
                            "Something that Dwayne notices straight away."
                            "But thankfully he's not crude or stupid enough to force the issue."
                            "Instead he releases me, holding up his hands in a gesture of surrender."
                            dwayne.say "Whoa..."
                            show dwayne -smile
                            dwayne.say "Wait a moment, [hero.name]."
                            dwayne.say "There seems to have been some sort of misunderstanding!"
                            menu:
                                "No kidding!":
                                    if hero.morality >= 25:
                                        bree.say "You don't say!"
                                        bree.say "I wasn't aware the price of entry was a blow-job!"
                                    if hero.morality <= -25:
                                        bree.say "You bet there has!"
                                        bree.say "I'll be the one to decide if and when you get a BJ from me!"
                                    show dwayne smile
                                    "Dwayne's smiling now, shaking his head."
                                    "I can see that he's going into full-on crisis-management mode."
                                    dwayne.say "That was my mistake, [hero.name]."
                                    dwayne.say "I promise it won't happen again."
                                    if hero.morality >= 25:
                                        bree.say "You bet it won't!"
                                        bree.say "Or you'll be in serious trouble."
                                    if hero.morality <= -25:
                                        bree.say "See that it doesn't."
                                        bree.say "Or else you won't be seeing anymore of me!"
                                    "I make a point of draining the last of the champagne in my glass."
                                    hide dwayne with dissolve
                                    "And then I get up and walk out of the booth."
                                    scene bg nightclub
                                    show mike date annoyed
                                    with fade
                                    "Once I'm out, I see [mike.name] still waiting for me."
                                    show mike date happy
                                    "He looks pissed, but when he sees me coming he smiles."
                                    "But then he sees Dwayne standing in the doorway of the booth."
                                    show mike surprised
                                    mike.say "It was Dwayne?!?"
                                    mike.say "Oh man..."
                                    show mike date normal
                                    mike.say "Huh, he looks pretty pleased with himself."
                                    bree.say "Never mind him."
                                    bree.say "He's been drinking too much champagne."
                                    bree.say "And I think the bubbles have gone up his nose..."
                                    $ mike.love += 2
                                    $ game.active_date.score += 20
                                "Give him a blow-job":
                                    if hero.morality >= 25:
                                        bree.say "D...Dwayne!"
                                        bree.say "If that's what you wanted..."
                                        bree.say "Then...why didn't you just ask?"
                                    if hero.morality <= -25:
                                        bree.say "Whoa, there, Dwayne!"
                                        bree.say "We can play that way for sure."
                                        bree.say "But you have to ask nicely!"
                                    "I watch as realisation dawns on Dwayne."
                                    "His expression changes subtly before my eyes."
                                    "Now he's no longer trying to look conciliatory."
                                    "Instead his smile is becoming ever more sly."
                                    show dwayne -smile
                                    dwayne.say "Oh, so that's how it is?"
                                    dwayne.say "Sure thing, [hero.name]..."
                                    dwayne.say "We can do things that way."
                                    "Dwayne leans back and slowly unzips his flies."
                                    "Then he leans back, arms on the back of the seat."
                                    dwayne.say "Over to you!"
                                    "Okay, [hero.name]..."
                                    "You were the one that agreed to this."
                                    "Now you have to put your money where your mouth is."
                                    "Or to be more precise, I have to put it right there!"
                                    "Smoothing my hair behind my ears, I lower myself down."
                                    scene bg black
                                    show dwayne blowjob vip surprised mid limp date mc_date
                                    with fade
                                    "There's no good way to do this sitting on the seat."
                                    "And so I have no choice but to kneel on the floor in front of Dwayne."
                                    "I do the best I can not to look up at him as I do this."
                                    "Because I know that he must be revelling in every moment."
                                    "Instead I concentrate on the task at hand, reaching into his pants."
                                    "But the second my fingers touch it, I can't help gasping."
                                    "And when I pull it out, my eyes go wide."
                                    "I mean, I've seen big ones before now."
                                    "And I might even have seen bigger than this."
                                    "But trust me, when you whip one out of a guy's pants..."
                                    "Well, it can still take you by surprise!"
                                    "I hear the sound of Dwayne chuckling."
                                    "No doubt he's amused at my reaction."
                                    "I don't want to give him the satisfaction of looking up."
                                    show dwayne blowjob opened
                                    "So instead I begin to stroke the shaft with one hand."
                                    "And I keep my head in a spot where I know it'll be of use."
                                    "Teasing Dwayne's cock until it stands up, I manage to judge it just right."
                                    show dwayne blowjob up surprised
                                    pause 0.05
                                    show dwayne blowjob hard onface with hpunch
                                    "Which means that as it gets hard, it rises to meet my lips."
                                    "All I need to do is part them and lower my head a little..."
                                    show dwayne blowjob closed suck
                                    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
                                    "And just like that, I have him in my mouth."
                                    "That's when the dynamic changes between us."
                                    "Before now I was the one pretty much at Dwayne's mercy."
                                    "But now the most vulnerable part of his body is in my power."
                                    "It's surrounded by my tongue and lips, but also by my teeth."
                                    "I could bite down at any time, but instead I choose to caress."
                                    "Maybe it's that feeling of power that's pushing me onwards now."
                                    "Or hell, maybe I just get a thrill from doing this kind of thing."
                                    "Either way, I don't hesitate to work Dwayne as best I can."
                                    show dwayne blowjob mid
                                    pause 0.3
                                    show dwayne blowjob up
                                    pause 0.3
                                    show dwayne blowjob mid
                                    pause 0.3
                                    show dwayne blowjob up
                                    pause 0.3
                                    show dwayne blowjob mid
                                    pause 0.3
                                    show dwayne blowjob up
                                    "My guess is that he's not interested in anything subtle."
                                    "So I keep it simple and make sure I have an impact."
                                    "Which means massaging him as hard as I can."
                                    "That and taking him as deep as possible as soon as I'm able."
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob down
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob up
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob down
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob up
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob down
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob up
                                    "Dwayne seems to respond just as I expected."
                                    "He gives me total freedom to do whatever I see fit."
                                    "Because I imagine he's sitting there feeling like the king of the world."
                                    "It's the knowledge that I'm the one in control which keeps me going."
                                    "Knowing that, for all his grandstanding, I could stop any second."
                                    "And if I did that, he'd be the one begging me for more."
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob down
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob up
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob down
                                    pause 0.175
                                    show dwayne blowjob mid
                                    pause 0.175
                                    show dwayne blowjob up
                                    dwayne.say "Uh..."
                                    show dwayne blowjob mid dwaynehand
                                    pause 0.15
                                    show dwayne blowjob down
                                    pause 0.15
                                    show dwayne blowjob mid
                                    pause 0.15
                                    show dwayne blowjob up
                                    pause 0.15
                                    show dwayne blowjob mid
                                    pause 0.15
                                    show dwayne blowjob down
                                    pause 0.15
                                    show dwayne blowjob mid
                                    pause 0.15
                                    show dwayne blowjob up
                                    pause 0.15
                                    show dwayne blowjob mid
                                    pause 0.15
                                    show dwayne blowjob down
                                    pause 0.15
                                    show dwayne blowjob mid
                                    pause 0.15
                                    show dwayne blowjob up
                                    dwayne.say "Ungh..."
                                    "The sounds that Dwayne's making are out of character for him."
                                    "Animalistic grunts and groans that he can't possibly be in control of."
                                    "They let me know that he's losing it, that he can't hold on much longer."
                                    "And that in turn makes me all the more sure that I have him right where I want him."
                                    "Sure enough, I feel the tell-tale signs of his end coming."
                                    "And I decide how I want to finish this thing off."
                                    menu:
                                        "Swallow his cum":
                                            "I've got Dwayne so deep in my mouth that it seems a no-brainer."
                                            "And swallowing's a much safer option in such a public place."
                                            "So I prepare myself and wait for the moment it happens."
                                            show dwayne blowjob mid
                                            pause 0.15
                                            show dwayne blowjob down with vpunch
                                            pause 0.15
                                            show dwayne blowjob mid
                                            pause 0.15
                                            show dwayne blowjob up
                                            pause 0.15
                                            show dwayne blowjob mid
                                            pause 0.15
                                            show dwayne blowjob down with vpunch
                                            pause 0.145
                                            show dwayne blowjob mid
                                            pause 0.135
                                            show dwayne blowjob up
                                            pause 0.13
                                            show dwayne blowjob mid
                                            pause 0.125
                                            show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                                            show dwayne blowjob down cum surprised with vpunch
                                            "This means that when Dwayne cums, I can swallow it down with relative ease."
                                            "Not to say that it's anything like casually sipping a glass of water."
                                            show dwayne blowjob up out closed swallow limp -onface -dwaynehand
                                            "Dwayne all but explodes in my mouth, taxing my ability to swallow."
                                            "But I've done this kind of thing before, and I manage to pull it off again."
                                            show sexinserts head bree -cum zorder 1 at center, zoomAt(1, (720, 810))
                                            show dwayne blowjob opened tongueout
                                            "Each spurt of cum disappears down my throat, from the first to the last."
                                        "Pull his cock out":
                                            show dwayne blowjob mid
                                            pause 0.15
                                            show dwayne blowjob down with vpunch
                                            pause 0.15
                                            show dwayne blowjob mid
                                            pause 0.15
                                            show dwayne blowjob up
                                            pause 0.15
                                            show dwayne blowjob mid
                                            pause 0.15
                                            show dwayne blowjob down with vpunch
                                            pause 0.145
                                            show dwayne blowjob mid
                                            pause 0.135
                                            show dwayne blowjob up
                                            pause 0.13
                                            show dwayne blowjob mid
                                            pause 0.125
                                            show dwayne blowjob down
                                            "At the last possible moment I pull my head back."
                                            "This drags Dwayne's cock out of my mouth in one smooth motion."
                                            "But there's only a moment for me to catch a breath before it happens."
                                            show dwayne blowjob down opened
                                            pause 0.35
                                            show dwayne blowjob mid
                                            pause 0.35
                                            show dwayne blowjob up out tongueout -onface -dwaynehand
                                            pause 0.35
                                            show dwayne blowjob closed cum with vpunch
                                            "Dwayne's cock is still bobbing in front of my face as he shoots his load."
                                            "And I make sure that I take it square on the nose."
                                            "Warm, sticky cum hit's me in the face, making me close my eyes."
                                            show dwayne blowjob opened tongueout mouthcum limp
                                            show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                                            "Then it begins to run downwards, reaching my lips and chin."
                                    "Dwayne sits back in his seat, gasping for breath."
                                    "But I take the chance to clean myself off as I stand up."
                                    hide sexinserts
                                    scene bg vip
                                    show dwayne date
                                    with fade
                                    "As I turn to leave, Dwayne holds up his hand."
                                    "He still seems incapable of speaking."
                                    "But it's obvious he wants me to stay."
                                    bree.say "I think I just repaid you for inviting me in here, Dwayne."
                                    bree.say "So I'm going to leave before I overstay my welcome."
                                    scene bg nightclub
                                    show mike date annoyed
                                    with fade
                                    "Once I'm out, I see [mike.name] still waiting for me."
                                    show mike date happy
                                    "He looks pissed, but when he sees me coming he smiles."
                                    "But then he sees Dwayne standing in the doorway of the booth."
                                    show mike surprised
                                    mike.say "It was Dwayne?!?"
                                    mike.say "Oh man..."
                                    show mike date normal
                                    mike.say "Huh, he looks pretty pleased with himself."
                                    bree.say "Never mind him."
                                    bree.say "He's been drinking too much champagne."
                                    bree.say "And I think the bubbles have gone up his nose..."
                                    $ mike.love -= 2
                                    $ game.active_date.score -= 10
                                    $ game.active_date.stay = False
                "Go back in the 'scum' section":
                    "I might have been willing to indulge Dwayne had he been nicer about it."
                    "But he just basically called [mike.name] and me scum!"
                    bree.say "You can keep your champagne, Dwayne."
                    show dwayne -smile
                    bree.say "And you can keep your VIP section too!"
                    bree.say "I came here to spend time with [mike.name], not you."
                    show dwayne smile
                    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
                    pause 0.2
                    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
                    pause 0.2
                    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
                    "At the mention of [mike.name]'s name, Dwayne laughs."
                    dwayne.say "You really want to spend time with that loser?"
                    dwayne.say "Crammed in there with all those other losers too?"
                    dwayne.say "Well, I guess that makes you a loser too!"
                    "I think about hurling an insult back at Dwayne."
                    "But then another thought occurs to me."
                    "I put a smile on my face and look down at the glass of champagne."
                    bree.say "Actually, Dwayne..."
                    bree.say "I am kind of a sucker for champagne!"
                    "Dwayne senses his chance and hands me the glass."
                    show dwayne -smile
                    dwayne.say "Only the best when you're with me, [hero.name]."
                    dwayne.say "I knew you'd come to your senses!"
                    bree.say "I never lost them, Dwayne!"
                    show dwayne annoyed at startle
                    "The moment I'm done talking, I toss the champagne in his face."
                    show dwayne angry
                    "Dwayne splutters and gasps, his expression becoming enraged."
                    "But I've already turned my back and begun to walk away."
                    scene bg nightclub
                    show mike date happy
                    with fade
                    "[mike.name] sees me coming and smiles."
                    "But then he sees Dwayne waving his fist in the air."
                    show mike date annoyed
                    mike.say "It was Dwayne?!?"
                    mike.say "Oh man..."
                    show mike date normal
                    mike.say "He looks pissed!"
                    bree.say "Never mind him."
                    bree.say "He's been drinking too much champagne."
                    bree.say "And I think the bubbles have gone up his nose..."
                    $ mike.love += 5
                    $ game.active_date.score += 30
        "I'm not going anywhere":
            "The moment [mike.name] asks the question, I step back out of the VIP section."
            "The guy makes no effort to stop me, just closes the barrier behind me."
            if hero.morality >= 25:
                bree.say "Sorry, but I'm here on a date with [mike.name]."
                bree.say "So I'm going to have to say no."
            if hero.morality <= -25:
                bree.say "Hmm..."
                bree.say "It would have been fun."
                bree.say "But I've got all the real fun I need right here with [mike.name]!"
            "The guy shrugs, as though he doesn't care either way."
            "Shady guy" "Your loss, madam."
            "Shady guy" "I'll let the person that invited you know."
            hide victor
            show mike at center
            with easeoutright
            "With that, [mike.name] and I walk back into the public area of the club."
            show mike happy
            $ mike.love += 5
            $ game.active_date.score += 40
            mike.say "Thanks for staying with me, [hero.name]."
            mike.say "Some girls would have just gone in there alone."
            if hero.morality >= 25:
                bree.say "Don't worry, [mike.name]."
                bree.say "I'm not that kind of girl!"
            if hero.morality <= -25:
                bree.say "I meant what I said, [mike.name]..."
                "I squeeze his groin to make my point."
                "I really do have all the fun I need right here!"
            $ hero.cancel_event()
    $ game.active_date.skip_nightclub = True
    return

label dwayne_female_event_04:
    play sound cell_vibrate
    "My phone rings and I see that the caller is [mike.name]."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "[mike.name]")
    if not result:
        $ hero.cancel_event()
        $ mike.love -= 5
        return
    scene expression f"bg {game.room}" at blur(5), dark with dissolve
    "And it's all that I can do to keep from starting the conversation with a groan."
    bree.say "What is it now, [mike.name]?"
    mike.say "Huh?!?"
    mike.say "[hero.name]..."
    mike.say "How did you know I needed something?"
    "I can't suppress a chuckle at [mike.name]'s clueless response."
    bree.say "Oh, [mike.name]..."
    bree.say "You only ever seem to call me when you want something!"
    bree.say "And I'm right, aren't I?"
    bree.say "You need me to do something for you, right?"
    "There's a few moments of silence on the other end of the line."
    "And I can almost picture [mike.name] as he tries to think up an excuse."
    "But I guess one doesn't spring into his mind."
    "As when he finally responds, he just comes out and admits it."
    mike.say "Okay, [hero.name], you got me."
    mike.say "I forgot a file again."
    bree.say "Oh, [mike.name]!"
    bree.say "Not again?!?"
    mike.say "I know, I know..."
    mike.say "But I REALLY need this one, [hero.name]!"
    mike.say "Do you think you could bail me out one more time?"
    menu:
        "Harumph... Fine...":
            "I want to tell him to find someone else to run his errands."
            "But then my conscience gets the better of me."
            "[mike.name] probably wouldn't kid about something like this."
            "So he must really need my help."
            bree.say "Urgh..."
            bree.say "I must be dumb as a box of rocks!"
            bree.say "Okay, [mike.name] - where is it and where do I need to take it?"
            "I hear [mike.name] breath a sight of relief on the other end of the line."
            "And by the sound of it, he's one hundred percent serious."
            mike.say "Thank you, [hero.name]!"
            mike.say "Thank you so much!"
            mike.say "It's on the desk in my room - you can't miss it."
            mike.say "Just bring it to reception when you get here."
            mike.say "Someone will get it to me."
            scene expression f"bg {game.room}" with dissolve
            "I end the call, still wondering if I'm doing the right thing."
            scene bg bedroom6 with fade
            "But I go to [mike.name]'s room and find the file all the same."
            scene bg office with fade
            "Then I make my way to his office building just like he asked."
            "Just like he said, there's no problem handing over the file."
            "But then a thought occurs to me."
            "I wonder if Dwayne's in his office right now?"
            if hero.morality >= 25:
                "He seems like a really nice guy."
                "And it'd be a shame not to say hi."
            if hero.morality <= -25:
                "I got the feeling he really has the hots for me."
                "And a little bit of harmless flirting would really hit the spot right now."
                "Who knows, he might even be in the mood for something more!"
            "It's not hard to find my way to Dwayne's office."
            "I just look for the biggest, most impressive one on the highest floor."
            scene bg door private at center, zoomAt(1, (640, 720)) with fade
            "And there it is, his name on the door!"
            show bg door private at center, traveling(1.5, 0.3, (640, 1040))
            pause 0.3
            play sound door_knock
            "I rap my knuckles on the wood, and then try the handle."
            "To my surprise, it's not locked and swings right open."
            bree.say "Erm..."
            bree.say "Dwayne?"
            bree.say "Are you in there?"
            scene bg black with dissolve
            pause 0.5
            scene bg ceo with wipeleft
            "The first thing I see is the exact kind of office I was expecting."
            "It's palatial, easily the size of a small studio apartment."
            "And one of the walls is formed by a floor-to-ceiling window."
            "The desk is, of course, huge."
            scene alexis_ntr_office_bg as bg zorder 1 at center, zoomAt(1.45, (440, 1460)), rotation(7)
            show dwayne zorder 2 at center, zoomAt(1.5, (980, 1140))
            "And Dwayne's sitting right behind it."
            "At first I think he's napping or something."
            "But as I walk into the office, I see that his eyes are open."
            "He seems to see me, but they're kind of glazed over."
            bree.say "Dwayne?"
            bree.say "Are you feeling okay?"
            show dwayne annoyed
            dwayne.say "Uurgh..."
            aletta.say "Grugh..."
            aletta.say "What's that?"
            aletta.say "Who's there?"
            show aletta naked noglasses upset zorder 3 at center, zoomAt(1.4, (680, 1300)) with easeinbottom
            "To my surprise I see a head pop up from under the desk."
            "It's a woman with long, dark hair and a face I vaguely recognize."
            "She's someone that works with [mike.name]."
            "Alexa...I think that was her name."
            show aletta noglasses angry
            aletta.say "Who...who are you?"
            aletta.say "How dare you barge in here?"
            show aletta noglasses angry blush
            aletta.say "We were...in the middle of an important meeting!"
            scene
            show dwayne office blowjob female nomc
            with fade
            "All it takes is one glance down for me to see that's a lie."
            "Dwayne's flies are open and his cock is standing up straight!"
            if hero.morality >= 25:
                bree.say "Oh dear!"
                bree.say "Dwayne, you fucking pig!"
            menu:
                "Dive in":
                    if dwayne.love.max <= 80:
                        $ dwayne.love.max = 80
                    "I don't stop long enough for Dwayne to regain the power of speech."
                    "Instead I stride straight around the side of his desk."
                    "And I make a point of pushing that damn Alexa girl aside as I kneel down too."
                    show dwayne office blowjob female -nomc with fade
                    aletta.say "HEY!"
                    dwayne.say "[hero.name], this isn't what it looks like!"
                    dwayne.say "Hey...what ARE you doing?"
                    if hero.morality >= 25:
                        bree.say "I won't let her take you away from me, Dwayne!"
                        bree.say "I'll prove that I'm better than her!"
                    if hero.morality <= -25:
                        bree.say "How long has this bitch been at it, Dwayne?"
                        bree.say "Forget about her, and let me show you how it's done!"
                    aletta.say "Excuse me!"
                    aletta.say "Are you questioning my abilities?"
                    bree.say "Yeah, Alexa..."
                    bree.say "That's exactly what I'm doing!"
                    aletta.say "I'll show you..."
                    aletta.say "You...you rude little cow!"
                    aletta.say "And for the record, it's Aletta."
                    aletta.say "Not Alexa!"
                    "The look on Dwayne's face has changed now."
                    "Becoming one of amusement as he realises what's happening."
                    dwayne.say "Ladies, please!"
                    dwayne.say "There's no need to argue."
                    dwayne.say "This can all be solved with a little friendly competition!"
                    dwayne.say "Both of you do your best to please me."
                    dwayne.say "And I'll decide who's the winner!"
                    "Aletta and I share a sideways glance through narrowed eyes."
                    "And then we both try to pounce on Dwayne at the same time."
                    show dwayne office blowjob female alettatongue
                    "I'd like to say that Aletta and I work together like a well-oiled machine."
                    "But what follows is a round of pushing and slapping as we fight over his cock."
                    show dwayne office blowjob female alettablow
                    "I'm not sure how it happens, but she gets their first."
                    "Which means I'm forced to prowl around the edges, waiting for my chance."
                    show dwayne office blowjob female alettablow closed
                    "In the meantime I focus my attention on Dwayne's balls."
                    "I can use my mouth on those as easily as I can his cock."
                    "Sucking, squeezing and even biting, I get straight to work."
                    "And I like to think that most of the sounds and movements he makes are because of me."
                    show dwayne office blowjob female alettablow opened
                    "Aletta's crazily possessive of her position, not budging an inch."
                    "Plus she's going at it like crazy too."
                    "She must also have burnt off a lot of energy before I got here."
                    "Because I can soon detect hints that she's starting to flag."
                    "Her pace starts to slow, and her eyes are glazing over."
                    show dwayne office blowjob female -alettablow
                    "Finally she's forced to stop, releasing Dwayne's cock as she gasps for breath."
                    "Sensing my chance has come, I elbow her out of the way."
                    "And I'm on Dwayne before she can protest."
                    show dwayne office blowjob female mcblow
                    "His cock slides into my mouth, still slick from Aletta's."
                    "And from that point I don't look back."
                    "Now I'm the one with the upper hand, and I'm going for it."
                    "I can feel Aletta pushing and shoving as soon as she's able."
                    "But I have the advantage of being fresher than her."
                    "And there's nothing she can do to dislodge me."
                    "I've already talked a good fight in front of Dwayne and Aletta."
                    "Now it's time for my mouth to cash the cheques it's been writing."
                    "I'm calling on every scrap of experience I have."
                    "Using every trick that I've come across."
                    "All of it in the hope that it's better than what Aletta's capable of."
                    "Pushing everything else aside, I focus solely on pleasing Dwayne."
                    "My head goes up and down, my lips and tongue work tirelessly."
                    "And I swear that I can feel my efforts beginning to pay off."
                    "Dwayne's cock is twitching like crazy in my mouth."
                    "It's so deep by now that I'm afraid it's going to trigger my gag reflex."
                    "So it comes as some relief that those movements seem to be the first signs of him losing it."
                    "I guess this is going to be the acid test, the proverbial moment of truth."
                    "However Dwayne chooses to end this thing will let us know who's come out on top."
                    "But all I can do right now is keep on going and hope for the best."

                    menu:
                        "I should swallow":
                            "I feel Dwayne letting go inside my mouth."
                            "Which I guess means that I'm being rewarded."
                            "I'm as ready for it as I can hope to be."
                            show dwayne office blowjob female mcblow mcmouth with vpunch
                            "And for the most part I manage to swallow it all."
                            with vpunch
                            "I only falter to the smallest degree, handling it like a pro."
                        "Aletta should swallow":
                            "At the last moment, I feel Dwayne move."
                            show dwayne office blowjob female -mcblow
                            "And much to my dismay, he pulls out of my mouth."
                            "Before I can recover my senses, Aletta realises what's happening."
                            "Her mouth is open even before Dwayne turns in her direction."
                            show dwayne office blowjob female alettablow closed with vpunch
                            "And she closes her lips around the head just in time."
                            show dwayne office blowjob female alettablow opened with vpunch
                            "Aletta coughs and gags, unprepared to swallow so much so quickly."
                            show dwayne office blowjob female alettamouth
                            "But she stubbornly holds on all the same, her eyes watering with the effort."
                        "I should have my face stained":
                            "At the last moment, I feel Dwayne move."
                            show dwayne office blowjob female -mcblow
                            "And much to my dismay, he pulls out of my mouth."
                            show dwayne office blowjob female cumshot with vpunch
                            "But before I can recover my senses, he shoots his load."
                            show dwayne office blowjob female mcface with vpunch
                            "And it hits me square in the face."
                            show dwayne office blowjob female -cumshot dickcum
                            "A moment later, my face is painted with lines of white."
                        "Aletta should have her face stained":
                            "At the last moment, I feel Dwayne move."
                            show dwayne office blowjob female -mcblow
                            "And much to my dismay, he pulls out of my mouth."
                            show dwayne office blowjob female cumshot with vpunch
                            "Before I can recover my senses, Aletta realises what's happening."
                            show dwayne office blowjob female alettaface with vpunch
                            "She makes sure she's straight at Dwayne's cock as he shoots his load."
                            show dwayne office blowjob female -cumshot dickcum
                            "Which means that her entire face is painted with lines of white."
                        "We should have our both faces stained":
                            "At the last moment, I feel Dwayne move."
                            show dwayne office blowjob female -mcblow
                            "And much to my dismay, he pulls out of my mouth."
                            show dwayne office blowjob female cumshot with vpunch
                            "Before I can recover my senses, Aletta realises what's happening."
                            with vpunch
                            "She makes sure she's straight at Dwayne's cock as he shoots his load."
                            show dwayne office blowjob female alettaface mcface with vpunch
                            "But Dwayne pulls me into range at the last moment."
                            show dwayne office blowjob female -cumshot dickcum
                            "Which means that both our faces are painted with lines of white."
                    scene bg ceo
                    show aletta work at left5
                    show dwayne at right5
                    with fade
                    "Afterwards, Aletta and I clean ourselves up."
                    "All the time we're still glaring at each other."
                    "But Dwayne seems to think things turned out for the best."
                    show dwayne happy
                    dwayne.say "There's really no need for you two to fight."
                    dwayne.say "I think I just proved that I can handle the both of you!"
                    dwayne.say "So next time, let's all get together as friends, okay?"
                    show dwayne smile
                    "I force myself to nod and smile."
                    "But I'm not happy with the idea at all."
                    "And from the hardness of her eyes, I'd say Aletta feels the same way too."
                "Get out of here (Never meet Dwayne again)":
                    "I don't stop long enough for Dwayne to regain the power of speech."
                    "My cheeks are already burning as I rush out of his office."
                    scene bg office with fade
                    "I'm feeling a combination of embarrassment and anger right now."
                    "And I don't know if I'm madder with Dwayne or myself."
                    "Sure, it's horrible to walk in on him while he's being blown by another girl."
                    "But what was I thinking, strolling straight into his office like that?"
                    "I mean, I already knew that Dwayne was no boy scout or saint."
                    "How could I have been so dumb?"
                    "I don't hear any voices behind me."
                    scene bg street with fade
                    "And nobody tries to stop me as I leave the building."
                    "Which I guess isn't surprising."
                    "Dwayne's in a compromising position."
                    "And that Alexa slut probably does that kind of thing all the time!"
                    "All I know is that I need to get as far away from here as possible."
                    "And that's just what I do, heading straight home to hide."
                    "I also promise myself that I'm never running an errand for [mike.name] again!"
                    $ dwayne.set_gone_forever()
        "No (Never meet Dwayne again)":
            "I don't hesitate before giving him my answer."
            bree.say "No way, [mike.name]."
            bree.say "You can handle it yourself this time."
            mike.say "B...b...but, [hero.name]!"
            mike.say "My ass is on the line here!"
            mike.say "And you helped me out last time, remember?"
            mike.say "So why not now?!?"
            "I take a deep breath, hold it for a moment and then let it out."
            "Once that's done, I feel like I'm ready to lay it on the line to [mike.name]."
            bree.say "Because I feel like you're starting to take me for granted, that's why."
            bree.say "Every time you're in trouble, you call me."
            bree.say "I've never once known you call Sasha!"
            "I can hear the desperation in [mike.name]'s voice as he replies."
            mike.say "That's because you're the responsible one, [hero.name]!"
            mike.say "Sasha would probably lose the file on the way to my office."
            mike.say "Or else she'd swap it for a jar of magic guitar picks!"
            bree.say "Oh really?"
            bree.say "How about I tell her that next time I see her, huh?"
            mike.say "[hero.name]!"
            mike.say "Will you help me or not?"
            bree.say "Look, [mike.name]..."
            bree.say "If it's as important as you say it is, you'll find a way."
            bree.say "And if it's not, then you're taking the piss!"
            $ mike.love -= 10
            scene expression f"bg {game.room}" with dissolve
            "With that I end the call and put my phone away."
            "And you know what - it kind of feels good!"
            "[mike.name] can sort out his own mess for once."
            "And I can deal with my own problems instead."
            $ dwayne.set_gone_forever()
    return

label dwayne_preg_talk:
    $ dwayne.flags.toldpreg = True
    $ dwayne.flags.know_is_father = True
    show dwayne at center, zoomAt (1.0, (640, 740))
    "I feel my heart sink the moment that I see Dwayne walking towards me."
    "He has that same swagger about him, the one that's normally so hot."
    "And the one that got me into this situation in the first place!"
    "He gives me a confident smile as he stops in front of me."
    "Which has the opposite effect on me."
    dwayne.say "Hey, [hero.name]..."
    dwayne.say "You don't look so good!"
    dwayne.say "Is there something wrong?"
    "I reach down deep inside for the strength that I need right now."
    "And though I don't feel like I find as much as I'd like, I press on regardless."
    "There's no way I can back out of telling Dwayne the news that I have for him."
    bree.say "Yeah, Dwayne..."
    bree.say "There's something I need to tell you..."
    bree.say "But I don't know if it's wrong or right!"
    "Dwayne raises a quizzical eyebrow."
    "He seems intrigued by the statement."
    dwayne.say "Well now, [hero.name]..."
    dwayne.say "Now you've got me intrigued!"
    dwayne.say "Now I just have to hear it!"
    "I take a deep breath and force myself to come out with it."
    "And I keep telling myself that it'll be okay once I do."
    "Dwayne's a successful businessman, not some dumb teenage boy."
    "Surely he knows how to handle something like this?"
    bree.say "There's no easy way to say this, Dwayne..."
    bree.say "I was late this month, so I took a test."
    bree.say "It came back positive, and you're the father."
    "Dwayne nods his head as I tell him all of this."
    "He listens carefully and lets me finish before he says a word."
    dwayne.say "You're sure about that, [hero.name]?"
    dwayne.say "You're sure the child is mine?"
    "I'd expected an emotional response out of him."
    "But somehow this is far worse."
    "I feel like Dwayne is putting me under the microscope right now!"
    bree.say "Y...yeah, Dwayne."
    bree.say "I'm sure as I can be."
    bree.say "Well, without a DNA test or something like that!"
    dwayne.say "Hmm..."
    dwayne.say "Well, that can always be arranged."
    dwayne.say "But let's focus on the matter at hand for now."
    if dwayne.love >= 150:
        "Dwayne takes me by surprise as he grabs my hands and kisses them."
        dwayne.say "This is fantastic news, [hero.name]!"
        "I take a step backwards, shaking my head."
        "Part of me can't believe what Dwayne is saying."
        bree.say "It...it is?!?"
        bree.say "I thought you'd be angry with me!"
        bree.say "That you'd think we made a mistake!"
        show dwayne smile
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        "Dwayne lets out a booming laugh."
        "Then he shakes his head and gives me a wry smile."
        dwayne.say "I don't make mistakes, [hero.name]."
        dwayne.say "And I take responsibility for my actions too!"
        dwayne.say "Sure, we didn't plan for this to happen."
        dwayne.say "But it's a blessing, [hero.name] - a sign we're good together."
        "I find myself smiling without even realising it."
        "I can't remember seeing Dwayne this positive before."
        "He's practically bubbling over with confidence."
        "And when he's like this, it's almost impossible to resist him."
        bree.say "You...you want to keep it?"
        dwayne.say "Of course I do, [hero.name]!"
        dwayne.say "This child is a symbol of our love!"
        dwayne.say "If it's a boy, he'll be as much of an alpha as me!"
        dwayne.say "And if it's a girl, she'll be as beautiful as you!"
        "I'm smiling and blushing now, totally charmed by Dwayne's enthusiasm."
        "And I can already see visions of us together as a family."
        "I just hope that some of what I'm seeing is real."
        "And not just me getting high on my attraction to Dwayne!"
    else:
        "Dwayne takes me by surprise as he pulls out his wallet."
        "He opens it up to reveal a startlingly large wad of notes."
        dwayne.say "How much do you need right now, [hero.name]?"
        dwayne.say "I don't expect you to have decided whether you want a termination or not at this stage."
        dwayne.say "So just see this as a down payment, something to keep you happy and quiet, okay?"
        "I take a step backwards, shaking my head."
        "Part of me can't believe what Dwayne is suggesting."
        bree.say "Y...you're offering me money?"
        bree.say "What do you think, Dwayne?"
        bree.say "That I'm doing this to bribe you?!?"
        "Dwayne lets out a weary sigh as he puts his wallet away."
        "But he tries to make the his expression sympathetic as he does so."
        dwayne.say "Oh, [hero.name]..."
        dwayne.say "Bribe is such an ugly word."
        dwayne.say "I'm just offering to pay to put things right, that's all!"
        bree.say "But..."
        bree.say "I want you to take responsibility, Dwayne."
        bree.say "Not to buy me off!"
        "Dwayne chuckles and shakes his head."
        dwayne.say "Come on, [hero.name], grow-up."
        dwayne.say "You think you're the first girl I've gotten pregnant?"
        dwayne.say "You're just the latest, and you won't be the last either!"
        dwayne.say "So just do what all the others before you did."
        dwayne.say "Be a good little girl, take the money and get the hell out of my life!"
        "With that, Dwayne turns on his heel and starts to walk away."
        dwayne.say "Oh, and do me a favour..."
        dwayne.say "When you come to your senses, contact my secretary about the money."
        dwayne.say "Because you'll find I've already blocked your number!"
        $ dwayne.breakup()
    return

label dwayne_kiss_me_female:
    show dwayne
    "I'm just nodding and smiling at all of Dwayne's stories."
    "And I'm telling myself that I'm not going to fall for his bullshit."
    "But that's easier said than done, because he's so damn good at it!"
    "Seriously, Dwayne's a genuine lady-killer when he's on a roll."
    "And with every minute that passes, I can feel my ability to resist ebbing away."
    "It's like every new compliment and joke knocks ten points off my IQ."
    "Before too long I'm giggling and rolling my eyes like a bimbo."
    "Then he has a hold of my hand, kissing it."
    "Then he raises one eyebrow and leans in closer."
    "Ah, what the hell - it's just a silly little kiss!"
    hide dwayne
    show dwayne kiss
    $ dwayne.flags.kiss += 1
    "But the moment Dwayne's lips touch mine, I know it's nothing of the kind."
    "I feel myself almost melting in his arms - in those strong arms!"
    "Oh god - this feels so good!"
    "I don't want it to stop!"
    hide dwayne kiss
    return

label dwayne_find_out_pregnancy:
    $ dwayne.flags.toldpreg = True
    show dwayne at center, zoomAt(1.5, (640, 1040))
    "I'm totally unprepared for Dwayne striding up to me and fixing me with those eyes of his."
    "And just to seal the deal, he raises one eyebrow as he gazes at me, letting me know he means business."
    show dwayne annoyed
    dwayne.say "[hero.name]..."
    dwayne.say "When were you going to tell me you were pregnant?"
    dwayne.say "Or were you just going to show me the kid when you finally gave birth?"
    "I blink and stare at Dwayne, totally stunned by what he just said."
    "I honestly didn't think I was showing at all yet."
    "And I thought guys were supposed to be blind to the more subtle signs."
    bree.say "H...how did you know?"
    bree.say "I haven't told anybody yet!"
    show dwayne smile
    show dwayne at center, zoomAt (1.0, (640, 1040)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 1040)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 1040)), startle(0.14,-20)
    "Dwayne laughs and shakes his head."
    dwayne.say "Oh please, [hero.name]..."
    dwayne.say "I'm already a father, remember?"
    dwayne.say "I've seen the whole process from start to finish."
    show dwayne normal
    "I nod, still more than a little stunned."
    bree.say "Well, yeah..."
    bree.say "I am pregnant, Dwayne..."
    bree.say "But that's not all..."
    menu:
        "It's yours":
            $ dwayne.flags.know_is_father = True
            bree.say "It's your baby, Dwayne..."
            bree.say "You're the father!"
            show dwayne annoyed
            "At this revelation, Dwayne raises his eyebrow further still."
            "I mean seriously, it's almost on top of his head by now!"
            if dwayne.love >= 160:
                dwayne.say "Why didn't you tell me it was mine first, [hero.name]?"
                dwayne.say "That changes everything!"
                "I shake my head, not understanding what I'm hearing."
                bree.say "What's that supposed to mean?"
                dwayne.say "If the kid was someone else's..."
                dwayne.say "Or you didn't know who's it was..."
                dwayne.say "Well, then I'd have dropped you like a bad habit!"
                show dwayne smile
                dwayne.say "But this is MY child, [hero.name]!"
                show dwayne normal
                "I blink, still not fully comprehending Dwayne's meaning."
                bree.say "You mean..."
                bree.say "You're okay with it?"
                show dwayne smile
                dwayne.say "I'm better than okay with it, [hero.name]!"
                dwayne.say "I'm over the moon!"
                dwayne.say "Even more so if it's the son I always wanted."
                show dwayne normal
                bree.say "Oh god...that's a relief!"
                bree.say "I was scared you were going to dump me!"
                show dwayne smile
                "Dwayne looks at me in amazement."
                dwayne.say "Hell no!"
                dwayne.say "My children are the most important thing in the world to me."
                dwayne.say "And this one is going to be no different!"
            else:
                show dwayne smile at startle
                dwayne.say "Ha, ha..."
                dwayne.say "Nice try, [hero.name]."
                dwayne.say "But no dice!"
                show dwayne normal
                "I shake my head, not understanding what I'm hearing."
                bree.say "What's that supposed to mean, Dwayne?"
                bree.say "You got me pregnant."
                bree.say "Now you have to take responsibility!"
                show dwayne annoyed
                dwayne.say "No, [hero.name] - YOU let yourself get pregnant."
                dwayne.say "So that's your problem, not mine."
                dwayne.say "You have no proof that I'm the father."
                dwayne.say "For all I know, you could be lying."
                dwayne.say "You could have been sleeping with a hundred guys I don't know about!"
                "I'm so shocked by Dwayne's casual dismissal that I stagger backwards."
                "I can't believe that he's coming out with all of this!"
                bree.say "You...you bastard!"
                bree.say "You can't leave me like this!"
                show dwayne angry
                "Dwayne's face hardens as I say this."
                "And when he speaks again, his tone is colder than I've ever heard it."
                dwayne.say "Don't tell me what I can and can't do, little girl."
                dwayne.say "And don't go calling me again, period."
                dwayne.say "Or else you'll be hearing from my lawyers."
                hide dwayne with easeoutright
                "With that, Dwayne turns on his heel and strides away."
                $ dwayne.set_gone_forever()
        "It's not yours":
            bree.say "You're not the father, Dwayne."
            bree.say "I'm pregnant with someone else's baby!"
            show dwayne annoyed
            "At this revelation, Dwayne raises his eyebrow further still."
            "I mean seriously, it's almost on top of his head by now!"
            if dwayne.love >= 140:
                dwayne.say "I respect you telling me the truth, [hero.name]."
                dwayne.say "Admitting something like that takes balls."
                dwayne.say "You could have tried to tell me it was mine."
                show dwayne normal
                dwayne.say "But you didn't."
                "I nod slowly."
                bree.say "So..."
                bree.say "Where do we go from here?"
                bree.say "I could really use your help, yeah?"
                bree.say "With the baby?"
                "Dwayne takes a long, deep breath."
                "He holds it for a moment as he looks me in the eye."
                "Then he lets it out in one go."
                "And I know that he's reached a decision."
                menu:
                    "Ask Dwayne to help with the baby":
                        if dwayne.love >= 160:
                            show dwayne smile at startle
                            "Dwayne lets out a snort and shakes his head."
                            dwayne.say "I can't believe I'm doing this..."
                            show dwayne normal
                            dwayne.say "But okay, [hero.name]."
                            dwayne.say "I want to keep you that badly."
                            dwayne.say "And I guess a mother and child come as one package."
                            "I feel a sense of relief flooding my entire body."
                            bree.say "Oh, Dwayne..."
                            bree.say "Thank you!"
                            bree.say "You won't regret this, I promise!"
                            show dwayne smile
                            dwayne.say "Be sure I don't, [hero.name]."
                            show dwayne normal
                            dwayne.say "Because I don't have it in me to forgive you twice!"
                        else:
                            show dwayne annoyed
                            "Dwayne shakes his head."
                            show dwayne angry
                            dwayne.say "I'm not paying to raise another man's child, [hero.name]."
                            dwayne.say "I'm willing to keep out relationship alive."
                            dwayne.say "But the baby's not mine, so I won't pay for it."
                            show dwayne annoyed
                            "I open my mouth to argue the point."
                            "But then I see the steely look in Dwayne's eyes."
                            "And I know that I can't ask him to do that."
                            "He's right, this isn't his child."
                            "And I got pregnant by fooling around behind his back."
                            "If he had dropped me on the spot, he'd have been well within his rights."
                            bree.say "Okay, Dwayne."
                            bree.say "You got it."
                            $ dwayne.breakup()
                    "I won't bother you about it":
                        pass
            else:
                show dwayne smile at startle
                dwayne.say "Ha, ha..."
                dwayne.say "Nice try, [hero.name]."
                dwayne.say "But no dice!"
                show dwayne normal
                "I shake my head, not understanding what I'm hearing."
                bree.say "What's that supposed to mean, Dwayne?"
                bree.say "I'm pregnant, and I need help!"
                show dwayne annoyed
                dwayne.say "No, [hero.name] - YOU let yourself get pregnant."
                dwayne.say "So that's your problem, not mine."
                dwayne.say "For all I know, you could be lying."
                dwayne.say "You could have been sleeping with a hundred guys I don't know about!"
                "I'm so shocked by Dwayne's casual dismissal that I stagger backwards."
                "I can't believe that he's coming out with all of this!"
                dwayne.say "Either way, none of this is my problem."
                bree.say "Please, Dwayne..."
                bree.say "You can't leave me like this!"
                show dwayne angry
                "Dwayne's face hardens as I say this."
                "And when he speaks again, his tone is colder than I've ever heard it."
                dwayne.say "Don't tell me what I can and can't do, little girl."
                dwayne.say "And don't go calling me again, period."
                dwayne.say "Or else you'll be hearing from my lawyers."
                hide dwayne with easeoutright
                "With that, Dwayne turns on his heel and strides away."
                $ dwayne.set_gone_forever()
    return

label dwayne_female_event_05:
    $ dwayne.flags.nodate = False
    if dwayne.love.max <= 100:
        $ dwayne.love.max = 100
    scene expression f"bg {game.room}"
    "I'm normally pretty good at looking where I'm going, you know?"
    "Like I might look at my phone as much as the next person."
    "But I can normally spot when I'm about to walk into someone."
    "And I almost always manage to hop out of the way before it's too late."
    "But not today, apparently..."
    show dwayne at center, zoomAt (2.0, (640, 1300)) with vpunch
    bree.say "Oof..."
    bree.say "What the..."
    show dwayne shout
    dwayne.say "Whoa!"
    show dwayne annoyed
    dwayne.say "Slow down there, girl!"
    "I find myself bouncing off what I first think is a wall."
    show dwayne at center, zoomAt (1.5, (640, 1040))
    "But then I stagger back a little and see a face starting down at me!"
    "It's a huge guy, way taller and broader than most of the guys I know."
    "And he's smiling at me with two rows of huge, white teeth too."
    "Even with my head spinning like it is, I still recognise him."
    "It can only be Dwayne, [mike.name]'s boss and the big cheese at his company too."
    bree.say "Oh..."
    bree.say "Hi, Dwayne!"
    "Dwayne seems to recover from having me collide with him in the blink of an eye."
    "But part of me thinks that has a lot to do with the fact that I'm female."
    show dwayne happy
    "Because I can almost sense the fact he's trying to put on the charm with me."
    show dwayne smile
    dwayne.say "Got it in one, little lady!"
    dwayne.say "And I think I recognise you too."
    dwayne.say "Aren't you [mike.name]'s housemate?"
    dwayne.say "Sasha?"
    dwayne.say "He's always talking about you!"
    "Somehow him mistaking me for Sasha makes me prickle with irritation."
    bree.say "No, no, no!"
    bree.say "I'm [hero.name]!"
    bree.say "Sasha's all pale, with black hair and clothes!"
    show dwayne normal
    "Dwayne cradles his chin in one hand as he looks me up and down."
    "I can't help noticing how strong that jawline is."
    "Or the appraising look he's giving me right now..."
    dwayne.say "Apologies, [hero.name]..."
    dwayne.say "I see my mistake now."
    dwayne.say "The girl [mike.name] was talking about wasn't as beautiful as you!"
    dwayne.say "So he must have been talking about whoever this Sasha is!"
    "Urgh..."
    "That's such a practiced line!"
    "I should be chewing this guy out for using it on me right now."
    "But there's just something about his confidence and the way he talks."
    "Not to mention the fact that he's put together under that expensive suit."
    "And...well...he IS pretty handsome!"
    bree.say "Erm..."
    bree.say "Thanks..."
    bree.say "I guess!"
    show dwayne smile
    "Dwayne flashes me another winning smile."
    "And then he waves away my thanks with one hand."
    dwayne.say "Ah, come on, [hero.name]..."
    dwayne.say "You must get that all the time!"
    "I can't help shaking my head and beginning to blush."
    dwayne.say "But I'm guessing those guys miss what's on the inside, right?"
    dwayne.say "Because I'm betting you're a pretty smart cookie behind those good looks!"
    "I keep on nodding as my cheeks burn."
    "This guy's such a charmer!"
    show dwayne normal
    dwayne.say "Wait a minute..."
    dwayne.say "I'm in the market for a new PA."
    dwayne.say "And I think you'd fit the role perfectly."
    dwayne.say "So what do you say, [hero.name]?"
    dwayne.say "You want to come work under me?"
    show dwayne happy
    dwayne.say "Oops...I mean, work FOR me?"
    show dwayne normal
    menu:
        "Accept (change day job)":
            "I feel like I have to gather up all of my strength to make my answer."
            "Like I'm fighting against all of Dwayne's charm to say what I have to say."
            with vpunch
            bree.say "YES!"
            bree.say "I...I mean..."
            bree.say "Yes, thank you very much, Dwayne."
            bree.say "I would very much like to come work under you!"
            show dwayne smile
            "Dwayne begins to smile as soon as he hears the word yes."
            "But his grin becomes wider still when he hears that last line."
            "Because it lets him know that we're both on the same wavelength."
            show dwayne happy
            dwayne.say "That's great, [hero.name]!"
            dwayne.say "You won't regret this - I promise you!"
            show dwayne at center, zoomAt (1.65, (640, 1140))
            "Dwayne reaches out and shakes my hand."
            "Which looks kind of silly as his swallows mine up."
            show dwayne normal
            "But at the same time I can see that he's looking me up and down."
            "And I can't help feeling like he's sizing up his latest acquisition."
            "The sensation makes me feel more than a little afraid."
            "But that fear is dwarfed by the thought of what Dwayne might have in mind for me."
            "Though for now I just have to push those thoughts to the back of my head."
            "I need to make this thing look as legit as possible."
            bree.say "So what?"
            bree.say "You'll call me?"
            show dwayne happy
            show dwayne at center, zoomAt (1.0, (640, 1140)), startle(0.14,-20)
            pause 0.2
            show dwayne at center, zoomAt (1.0, (640, 1140)), startle(0.14,-20)
            pause 0.2
            show dwayne at center, zoomAt (1.0, (640, 1140)), startle(0.14,-20)
            "Dwayne throws his head back and bellows with laughter."
            show dwayne at center, zoomAt (1.0, (640, 1140)), startle(0.14,-20)
            pause 0.2
            show dwayne at center, zoomAt (1.0, (640, 1140)), startle(0.14,-20)
            pause 0.2
            show dwayne at center, zoomAt (1.0, (640, 1140)), startle(0.14,-20)
            dwayne.say "HA, HA, HA!"
            dwayne.say "That's a good one, [hero.name]!"
            show dwayne annoyed
            dwayne.say "But of course not."
            dwayne.say "Someone from HR will be in touch."
            dwayne.say "So I'll be seeing more of you soon."
            dwayne.say "A hell of a lot more!"
            hide dwayne with easeoutright
            "With that, Dwayne turns on his heel and strides away."
            "Which leaves me alone to think about what I just signed myself up for!"
            $ hero.flags.office_boss = "dwayne"
            $ game.flags.job_day = "office"
            $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 5)
        "Refuse for now":
            "I feel like I have to gather up all of my strength to make my answer."
            "Like I'm fighting against all of Dwayne's charm to say what I have to say."
            bree.say "N...no..."
            bree.say "No thank you!"
            show dwayne shout
            "Dwayne looks puzzled by my response."
            show dwayne at center, zoomAt (1.25, (640, 900))
            "He even takes a step back and shakes his head."
            dwayne.say "Whoa..."
            show dwayne annoyed
            dwayne.say "Wait a minute..."
            dwayne.say "Did you just say...no?"
            "The look on his face and the tone of his voice are pretty clear."
            "This guy's not at all used to being told no!"
            bree.say "Erm...yeah!"
            bree.say "That's what I said, Dwayne."
            show dwayne upset
            "Dwayne nods his head slowly as he regards me."
            "And I feel like he's actually seeing me for the first time."
            "You know, like he's really sizing me up!"
            show dwayne normal
            dwayne.say "And just why would you say no, [hero.name]?"
            dwayne.say "If you don't mind me asking!"
            bree.say "Because I'm a student, Dwayne."
            bree.say "I already have a part-time job."
            bree.say "And I can only keep that because it's flexible."
            bree.say "I get the feeling you need someone that's totally dedicated."
            bree.say "Someone that can handle anything you throw at them."
            show dwayne shout
            dwayne.say "And that's not you?"
            show dwayne normal
            bree.say "No, it's not."
            "Dwayne draws himself up to his full height."
            "And he crosses his arms over his chest too."
            show dwayne annoyed
            dwayne.say "Well, [hero.name]..."
            dwayne.say "If that's the way you feel."
            dwayne.say "But be sure to keep the offer in mind."
            show dwayne smile
            dwayne.say "Because it's always open."
            "Before I can even ask how that would even work, Dwayne turns on his heel."
            hide dwayne with easeoutleft
            "And then he strides away, leaving me thankful he finally left me alone."
    $ Room.find("office").unhide()
    return

label dwayne_female_event_05_alt:
    "I'm just minding my own business when I feel my phone vibrating."
    "And as nothing else in particular is going on, I pull it out to see who's calling."
    $ result = renpy.call_screen("smartphone_choice", "Dwayne")
    if not result:
        $ do_event.flags.canceled = True
        $ dwayne.love -= 5
        return
    if dwayne.love.max <= 100:
        $ dwayne.love.max = 100
    "Noting that the caller ID says it's Dwayne, I decide to answer it."
    "Because it's not like he's going to want to talk to me about anything boring, is it?"
    "At the very least he's going to want to flirt with me or show off about something."
    "Which is just the kind of distraction that I could do with right now."
    bree.say "Hi, Dwayne..."
    bree.say "How are you doing?"
    dwayne.say "Hey there, [hero.name]..."
    dwayne.say "Always better for hearing your voice!"
    "I barely manage to stifle a chuckle as Dwayne piles on with the charm."
    "Sometimes he can be so predictable, it's like he's a character with scripted lines!"
    bree.say "Okay, Dwayne..."
    bree.say "What are you after?"
    "I hear Dwayne chuckle on the other end of the line."
    "Like he's pretending to be shocked at the implication that he's after something."
    dwayne.say "Oh come on, [hero.name]..."
    dwayne.say "Do you ask all of your friends that question when they call you up?"
    dwayne.say "As it happens I did want to ask you something..."
    dwayne.say "But I'm hurt that you'd think that was all I called you for!"
    "Now we're well and truly into the act of verbally sparring for fun."
    "So I feel like I can let out a giggle of my own and fully join in."
    bree.say "Oh no, poor Dwayne..."
    bree.say "What can I do to make it up to you?"
    dwayne.say "I can think of a hundred things I'd like you to do for me, [hero.name]."
    dwayne.say "But right now I just want you to step into my office and hear me out, okay?"
    "Although Dwayne can't see me right now, I still find myself shrugging nonchalantly."
    bree.say "Okay, Dwayne..."
    bree.say "I'll be there as soon as I can."
    dwayne.say "As soon as you can?"
    dwayne.say "You do realise that I'm kind of a big deal?"
    dwayne.say "Which means I'm used to most people dropping everything when I call, yeah?"
    bree.say "Yeah, yeah..."
    bree.say "But I'm not most people, am I?"
    "I end the call before Dwayne can respond, a smug smile on my face as I do so."
    "Even though I got the last word and left him hanging, I'm not going to torture Dwayne."
    scene bg office with fade
    "So I really do head over to his office as soon as I can make it."
    "A quick knock on the massive doors gets me a response from inside."
    dwayne.say "If that's you, bree..."
    dwayne.say "Then come on in!"
    "I push the doors, expecting them to be heavy and hard to move."
    "But to my surprise, they swing open easily."
    "Like they're on oiled hinges or even counterweights."
    "In fact they're moving so fast that I'm worried they're not going to stop."
    "But there's no way I can grab both of them, so I just make a grab for one."
    "And then I hold on, being dragged into the room by the door."
    "Realising that there's no hope of me slowing it down, I close my eyes and wait for the inevitable impact."
    "But it doesn't come, and so I open one eye, glancing around to see what happened."
    scene bg ceo with fade
    show dwayne happy
    dwayne.say "Well I have to say, [hero.name]..."
    dwayne.say "Most people just walk in through the doors."
    dwayne.say "You're the first person I've ever seen ride them!"
    show dwayne normal
    "Letting go of the door handle, I do the best I can to hide my embarrassment."
    bree.say "Ah, yeah..."
    bree.say "Well, that's me, Dwayne..."
    bree.say "Always thinking outside of the box, coming at you from an unexpected angle!"
    show dwayne smile
    "Dwayne gives me a smile that doesn't really tell me much."
    "He could be amused by the quip I just made or simply humouring me."
    show dwayne normal
    "But then he gestures to the chair on the other side of his desk."
    show dwayne shout
    dwayne.say "Take a seat, [hero.name]..."
    dwayne.say "Because it's always best to be sitting down when I make you an offer."
    show dwayne normal at center, zoomAt (1.5, (640, 1080)) with fade
    "I nod and hurry over to the seat, planting myself in it."
    "From this position I can really see how Dwayne's whole office is supposed to work."
    "Reclining in the massive chair on the other side of the desk, he doesn't look like a boss."
    "He looks more like some kind of king, sitting on a throne in the middle of his huge castle."
    bree.say "Erm..."
    bree.say "So, Dwayne..."
    bree.say "This offer of yours?"
    "Dwayne nods and gestures around the office."
    show dwayne shout
    dwayne.say "You can see how big of an operation this is, can't you?"
    dwayne.say "And I'm the guy that's in charge of it all, the place where the buck stops."
    dwayne.say "Which means I need people to work under me, [hero.name]."
    show dwayne normal
    "My eyes bulge in their sockets and I find myself gaping at Dwayne."
    bree.say "You want me to work under you?"
    bree.say "Like, with you on top of me?!?"
    "Dwayne lets out a booming laugh."
    show dwayne happy
    show dwayne at center, zoomAt (1.0, (640, 1080)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 1080)), startle(0.14,-20)
    dwayne.say "HA HA!"
    dwayne.say "That's a good one, [hero.name]!"
    dwayne.say "What I mean is that I have an opening for a part time PA."
    show dwayne shout
    dwayne.say "And I think that you'd be the perfect person for the job."
    show dwayne therock
    "Dwayne raises an eyebrow as he says this."
    "Making me think that he's very keen on me accepting his offer."
    menu:
        "Accept (change day job)":
            "I've been looking around the office the whole time that Dwayne's pitching the job to me."
            "And I have to say that I'm starting to like the look of the place more with every passing moment."
            "Plus I've also always kind of had a thing for Dwayne, with his swaggering manner and godlike physique."
            "So when it comes to my answer, it's kind of a no-brainer."
            bree.say "Sounds good to me, Dwayne..."
            bree.say "I could use the extra money, you know?"
            bree.say "And I'm guessing working with you has it's perks?"
            bree.say "Like, it could open doors for me, yeah?"
            show dwayne smile
            "I can see that Dwayne's more than a little pleased with my answer."
            "He leans back in his chair, his smile larger than ever."
            "And it's only now I realise how big and white his teeth really are."
            show dwayne happy
            dwayne.say "That's what I like to hear, [hero.name]..."
            dwayne.say "I knew you'd be able to see a good deal for what it was!"
            show dwayne smile
            bree.say "So..."
            bree.say "I guess I go home and wait to hear from you?"
            bree.say "Your HR people are gonna need to send me letters and stuff, right?"
            show dwayne normal
            "Dwayne shakes his head at this."
            show dwayne shout
            dwayne.say "I wouldn't know, [hero.name]..."
            dwayne.say "I don't handle small details like that."
            dwayne.say "I have a more hands on approach to recruitment."
            show dwayne normal
            "I nod as I begin to get up from my seat, thinking the interview is over."
            "But as I do so, Dwayne motions for me to stop."
            show dwayne shout
            dwayne.say "Whoa..."
            dwayne.say "Sit down, [hero.name]..."
            dwayne.say "We're not done yet!"
            show dwayne normal
            bree.say "Huh?"
            bree.say "What do you mean?"
            "Dwayne nods downwards, his eyes travelling down to his groin."
            show dwayne shout
            dwayne.say "Let's just say there's a practical element to the interview process!"
            show dwayne happy
            dwayne.say "So how about you come over here and demonstrate your oral skills?"
            show dwayne smile
            menu:
                "Give him a blow-job" if hero.morality <= -25:
                    "I stop in my tracks, doing all I can to keep from licking my lips."
                    "Because the mere thought of Dwayne's manhood is making me hungry!"
                    "And it doesn't seem too much for him to ask of me, you know?"
                    "Not when we're going to be working so close together from now on."
                    bree.say "I guess that makes sense, Dwayne..."
                    bree.say "This is kind of my try-out for the roll!"
                    "The smile on Dwayne's face only gets bigger as I hurry around the side of his desk."
                    $ dwayne.love += 2
                    "And he makes no effort to get involved in the process either."
                    "Which let's me know that I'm going to be doing all the work on my own."
                    "Wanting to get down to business, I kneel on the floor in front of Dwayne."
                    "Then I put my elbows on his knees and lean in closer."
                    "Almost the same moment I begin to unzip Dwayne's flies, I can feel his manhood in there."
                    "It's almost like the thing has a mind of it's own and is trying to escape from his pants."
                    scene
                    show dwayne blowjob ceo mid mc_casual
                    with fade
                    "Dwayne's cock springs out and almost hits me in the face, like it's on a spring or something."
                    "But I do the best I can not to let that get to me, and instead I focus on the task at hand - if you'll pardon the pun!"
                    "I throw myself into it, figuring that Dwayne want's gratification, right now, rather than to be teased."
                    show dwayne blowjob closed suck
                    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
                    "That's why I take a firm hold of the shaft and stick the head straight into my mouth."
                    "My guess is that he's been hard and wanting this all the time I've been in his office."
                    "So there shouldn't be much for me to do except getting him off."
                    "Still, that doesn't mean I'm going to be lazy about it."
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    "Instead I do all that I can to pleasure Dwayne as soon as I can."
                    "My tongue and lips are in constant motion as my head bobs up and down."
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob down
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob up
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob down
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob up
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob down
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob up
                    "At the same time one hand is shooting up and down the length of his shaft."
                    "The other one I use to play with his balls, tickling and pinching."
                    "And it seems that my efforts are beginning to pay off too."
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob down
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob up
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob down
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob up
                    "I can hear the sound of Dwayne's hands grabbing the arms of his chair."
                    "That and the chair itself creaking as he leans back in it."
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob down
                    pause 0.175
                    show dwayne blowjob mid
                    pause 0.175
                    show dwayne blowjob up with vpunch
                    dwayne.say "Mmm..."
                    dwayne.say "That's it, [hero.name]..."
                    dwayne.say "You're really...selling yourself!"
                    "Determined to do even better, I relax the muscles of my throat."
                    "This means that I can take Dwayne even deeper than before."
                    "And it doesn't take long for this to excite him even more."
                    show dwayne blowjob mid dwaynehand
                    pause 0.15
                    show dwayne blowjob down
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    "In fact it's not long before I can feel the signs that he's about to lose it."
                    "Which means that I have to decide how I want this thing to end."
                    menu:
                        "Swallow his cum":
                            "Deciding that swallowing is the cleanest option, I keep right on going."
                            show dwayne blowjob mid
                            pause 0.15
                            show dwayne blowjob down with vpunch
                            pause 0.15
                            show dwayne blowjob mid
                            pause 0.15
                            show dwayne blowjob up
                            pause 0.15
                            show dwayne blowjob mid
                            pause 0.15
                            show dwayne blowjob down with vpunch
                            pause 0.145
                            show dwayne blowjob mid
                            pause 0.135
                            show dwayne blowjob up
                            pause 0.13
                            show dwayne blowjob mid
                            pause 0.125
                            "And when Dwayne finally shoots his load, I'm more than ready for it."
                            show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                            show dwayne blowjob down cum surprised with vpunch
                            "Easily managing to swallow everything, I don't miss a beat."
                        "Pull his cock out":
                            show dwayne blowjob mid
                            pause 0.15
                            show dwayne blowjob down with vpunch
                            pause 0.15
                            show dwayne blowjob mid
                            pause 0.15
                            show dwayne blowjob up
                            pause 0.15
                            show dwayne blowjob mid
                            pause 0.15
                            show dwayne blowjob down with vpunch
                            pause 0.145
                            show dwayne blowjob mid
                            pause 0.135
                            show dwayne blowjob up
                            pause 0.13
                            show dwayne blowjob mid
                            pause 0.125
                            show dwayne blowjob down
                            "In a split second I decide that I want to take it in the face."
                            "It's the messier option, but probably the more impressive of the two."
                            show dwayne blowjob down opened
                            pause 0.35
                            show dwayne blowjob mid
                            pause 0.35
                            show dwayne blowjob up out tongueout -onface -dwaynehand
                            "So I let Dwayne's cock slide smoothly out of my mouth."
                            show dwayne blowjob closed with vpunch
                            "And then I wait patiently as he explodes in my face."
                            show dwayne blowjob closed cum with vpunch
                            "All the time remembering to keep smiling as he spatters my features with his load."
                    hide sexinserts
                    scene bg ceo
                    show dwayne at center, zoomAt(1.75, (640, 1240))
                    with fade
                    "Afterwards I hurry to clean myself up and Dwayne zips up his pants."
                    show dwayne happy
                    dwayne.say "I gotta say, [hero.name]..."
                    show dwayne smile
                    dwayne.say "There's a really bright future ahead of you here!"
                    "I nod and smile, already beginning to think of the possibilities."
                    "As well as what else I can do to make Dwayne see me as indispensable."
                    if hero.morality > -65:
                        $ hero.morality -= 1
                "Leave":
                    "I can't help bursting out with a peal of laughter as Dwayne makes the suggestion."
                    "Partly because it just seems to ridiculous for him to be calling it something like that."
                    "But also because I was expecting him to be a little more slick in trying to get me to do stuff like that."
                    bree.say "Oh come on, Dwayne..."
                    bree.say "You're going to have to do better than that!"
                    bree.say "Sure, I took the job..."
                    show dwayne normal
                    bree.say "But you could at least try courting me a little first, maybe?"
                    scene bg office with fade
                    "With that I turn on my heel and walk straight out of Dwayne's office."
                    "I'm waiting for him to get up and try to stop me."
                    "Or at least to call after me."
                    "But the fact he chooses to do neither tells me that I've made my point."
                    "And that makes me feel a whole lot more comfortable about taking the job."
                    "Because now Dwayne's made it totally plain that he's trying to get into my pants."
                    "But I've managed to stand up to him and he hasn't tried to challenge me on it."
                    "Which means, going forward, that I have a real measure of power in the relationship."
                    "And making use of that is going to be fun."
                    $ hero.morality += 2
            $ hero.flags.office_boss = "dwayne"
            $ game.flags.job_day = "office"
            $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 5)
        "Refuse for now":
            "I knew the second I looked around this office and at Dwayne in the middle of it that I didn't want to be here."
            "So the idea of accepting a job that would see me in and out if here all day long is totally not going to happen."
            "Which is why I start standing up even before I've managed to say a single word."
            bree.say "Oh no, Dwayne..."
            bree.say "I couldn't possibly take the job."
            show dwayne shout
            bree.say "I have so many commitments at the moment - college, other jobs, you know?"
            bree.say "You need someone that can totally devote themselves to the position."
            show dwayne annoyed
            "I was pretty sure that Dwayne wouldn't just take no for an answer."
            "So it comes as no surprise that he's out of his chair a second after I stand up."
            "And then he follows me towards the door as I make to leave."
            show dwayne shout
            dwayne.say "Don't you think you're being a little hasty, [hero.name]?"
            dwayne.say "I'm a very flexible employer, very understanding and accommodating."
            dwayne.say "We can try you in that position to begin with..."
            show dwayne happy
            dwayne.say "And if it doesn't work, then we can try another until we find one that does."
            show dwayne normal
            "There's so much talk about positions and working under people going on right now."
            "And the effect is that I'm not sure we're even discussing job vacancies anymore."
            "For all I know, Dwayne could have dropped all pretensions and be openly asking me to have sex with him!"
            bree.say "I said no, Dwayne..."
            bree.say "And I mean it, okay?"
            show dwayne upset
            bree.say "Thanks for the offer, but I'm not interested!"
            show dwayne annoyed
            "I see that Dwayne's already opening his mouth to make another attempt at convincing me."
            scene bg office with fade
            "So without pausing, I turn my back on him and stride through the doors of his office."
            "Sure, that might not have been the most polite way to excuse myself."
            "And I probably just burned a few bridges too."
            "But at least I got myself out of there before it was too late."
            $ dwayne.love -= 2
    $ game.room = "street"
    $ Room.find("office").unhide()
    return

label dwayne_female_job_event_01:
    "I've been working as Dwayne's secretary for a short while now, really getting a feel for the job."
    "And the thing that strikes me most about it is how little I actually seem to be doing for him."
    "Sure, I'm answering the phone and typing emails whenever there's a need, but that seems to be it."
    "There's no filing to do, as this is the twenty-first century, and nobody keeps records on paper anymore."
    "So a lot of the time I find myself at a loose end and trying to look busy."
    "Because if Dwayne or anyone else important catches me just sitting at my desk..."
    "Well, I'm afraid they'll fire me on the spot!"
    "So when I get a call from Dwayne's office in the middle of my working day, I hastily pick up the phone."
    "The chance to do anything of importance is also a chance to escape being bored for a short while."
    bree.say "Hello?"
    bree.say "How can I help?"
    dwayne.say "Would you mind stepping in here for a moment, [hero.name]?"
    dwayne.say "I have something that I could use your help with."
    "Dwayne sounds perhaps a little more strained and stressed than normal."
    "But surely that's to be expected, as he is the guy in charge around here."
    bree.say "Yes, sir!"
    bree.say "I'll be in right away."
    bree.say "Oh..."
    bree.say "Should I bring a pen and a notepad?"
    "There's a pause on the other end of the line, which is strange."
    "As that's not exactly a question that should be hard to answer."
    "But then Dwayne seems to recover and he speaks up again."
    dwayne.say "No need, [hero.name]..."
    dwayne.say "It's not that kind of a thing."
    "With that, he puts the phone down on me."
    "Which seems a little rude."
    "But I decide to ignore Dwayne's lack of manners."
    "Instead I focus on dealing with whatever task he has for me."
    "Getting up from my desk, I hurry over to his office door."
    scene bg ceo with fade
    "And then I let myself in."
    bree.say "Here I am, mister..."
    "The words die in my throat as I see what's waiting for me in Dwayne's office."
    show dwayne at center, zoomAt(1.75, (640, 1240)) with dissolve
    "Sure, there he is, sitting at his desk just like usual."
    "But the last time I was in here, I'm pretty sure his cock was inside of his pants!"
    "I mean, I think I'd have noticed something so big, sticking up from behind his desk."
    show dwayne happy
    dwayne.say "Ah, [hero.name]..."
    dwayne.say "There you are."
    show dwayne smile
    "Part of me thinks I should be looking Dwayne in the eye right now."
    "But I can't tear my gaze away from the sight of his big, hard member."
    bree.say "Y...yes..."
    bree.say "Here I am."
    show dwayne normal
    dwayne.say "I think you can see what my problem is, right?"
    bree.say "I..."
    bree.say "I think I can guess!"
    show dwayne annoyed
    dwayne.say "Look, [hero.name]..."
    dwayne.say "I'm massively stressed right now."
    dwayne.say "So I need a massive release to handle it."
    "Oh god - is he using the word 'massive' on purpose?"
    show dwayne normal
    dwayne.say "So I want you to come over here and give me oral relief."
    dwayne.say "And I want it right now."
    menu:
        "Give him a blow-job":
            "Sure, I'm more than a little shocked at the sight of Dwayne with his manhood out."
            "Though I can't say that I'm totally surprised he would do something like this."
            "And I guess that I also knew this kind of thing might happen when I took the job."
            "So with a quick look over my shoulder, I hurry over to where he's waiting for me."
            bree.say "Okay, boss..."
            bree.say "Whatever you say!"
            "Dwayne doesn't say a word in response."
            "But I can see that he has a huge smile on his face."
            $ dwayne.love += 2
            "That and the fact that he's nodding his head too."
            "I keep my eyes focussed on the task at hand, and on his cock as well."
            scene
            show dwayne blowjob ceo surprised mid mc_date
            with fade
            "Already kneeling on the floor in front of his chair."
            "I always suspected that Dwayne would have a massive one."
            "And what's standing up, straight and proud before me, certainly is."
            "It's totally in scale with the rest of him too!"
            "Before I was thinking that this could be hard."
            "But now that I'm up close, it seems as easy as can be."
            "All I have to do is reach out and take hold of it..."
            show dwayne blowjob opened
            "As soon as I feel my fingers close around the shaft, something just clicks."
            "It's almost like instinct takes over and I go onto autopilot."
            "My fingers move without the need for conscious thought."
            "And my head leans in closer too, waiting for the right moment."
            "At first all I do is stroke and massage, moving up and down."
            "But when I sense that the moment is just right..."
            show dwayne blowjob closed suck
            show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
            "Then I open my mouth and begin to tease the tip with my lips."
            "The tip of my tongue comes into play too, sliding here and there."
            "I can only hear the vaguest impression of what Dwayne's doing."
            "Muffled sounds that seem to let me know he approves of my actions."
            "Soon enough they seem to fade into the background."
            "And now I'm going on pure instinct alone."
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            "Little by little I take more of him into my mouth and for longer."
            "The speed at which my head is moving increasing too."
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            "So far I've been nothing but gentle with him."
            "But now it's time to introduce my teeth into the mix."
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            "As soon as I bite down, Dwayne lets out a gasp of surprise."
            "It's loud enough for me to hear, but not loud enough to make me stop."
            "In fact the small doses of pain only seem to make him like it all the more."
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up with vpunch
            "I feel Dwayne twitch and jump in his seat, trying to anticipate my next move."
            show dwayne blowjob mid dwaynehand
            pause 0.15
            show dwayne blowjob down
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob up
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob down
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob up
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob down
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob up
            "And that's to take him deeper than ever, pushing him harder too."
            "It's then that I hear him make a groaning sound."
            "And that let's me know that he's about to lose it."
            menu:
                "Swallow his cum":
                    "I'm totally ready for it when Dwayne starts to cum."
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.145
                    show dwayne blowjob mid
                    pause 0.135
                    show dwayne blowjob up
                    pause 0.13
                    show dwayne blowjob mid
                    pause 0.125
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    show dwayne blowjob down cum surprised with vpunch
                    "And though it's a big load from a big man, I can handle it."
                    show dwayne blowjob up out closed swallow limp -onface -dwaynehand with vpunch
                    "Pacing myself, I swallow as much as I can manage at a time."
                    show sexinserts head bree -cum zorder 1 at center, zoomAt(1, (720, 810))
                    show dwayne blowjob opened tongueout
                    "And I take a certain pride in not spilling a drop too."
                "Pull his cock out":
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.145
                    show dwayne blowjob mid
                    pause 0.135
                    show dwayne blowjob up
                    pause 0.13
                    show dwayne blowjob mid
                    pause 0.125
                    show dwayne blowjob down
                    "As soon as I feel Dwayne's about to cum, I pull back."
                    show dwayne blowjob down opened
                    pause 0.35
                    show dwayne blowjob mid
                    pause 0.35
                    show dwayne blowjob up out tongueout -onface -dwaynehand
                    "His cock slides smoothly out of my mouth and bobs a little before my face."
                    show dwayne blowjob closed with vpunch
                    "Then I close my eyes and wait for the inevitable to happen."
                    show dwayne blowjob closed cum with vpunch
                    "A moment later I feel stripes of hot cum hitting my face."
            hide sexinserts
            scene bg ceo
            show dwayne date at center, zoomAt(1.75, (640, 1240))
            with fade
            "Once he's spent, Dwayne sags back in his chair."
            "And he lets out a groan of satisfaction."
            show dwayne happy
            dwayne.say "Urgh..."
            dwayne.say "That was just what I needed, [hero.name]."
            dwayne.say "Now I feel like I can handle anything!"
            show dwayne smile
            "I nod and smile as I get to my feet."
            "Feeling happy to have proven my worth."
            bree.say "You're welcome, boss."
            bree.say "Will there be anything else?"
            "Dwayne shakes his head as he stuff his cock back into his pants."
            show dwayne happy
            dwayne.say "No, no..."
            dwayne.say "Just make sure you close the door on the way out."
            dwayne.say "And that you clean yourself up, okay?"
            show dwayne smile
            "I nod and then turn on my heel, walking out of his office."
            "And as I do so, I can't help thinking this job might be more fun than I expected."
            if hero.morality > -65:
                $ hero.morality -= 1
            $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 3)
        "No!":
            "For a moment I'm totally dumbfounded by the nature of Dwayne's request."
            "That and the sight of him with his cock out serve to leave me stunned."
            "But he keeps on looking at me, waiting for an answer."
            dwayne.say "Come on, [hero.name]!"
            dwayne.say "What are you waiting for?"
            "Finally I manage to shake it off and regain control of my senses."
            "And the first thing I do is to shake my head."
            bree.say "No way, Dwayne..."
            bree.say "That's not in my job description!"
            show dwayne upset
            "Dwayne's face darkens as he hears my answer."
            "And he leans forwards, putting his hands on the desk."
            show dwayne angry
            dwayne.say "Oh, I'm sorry, [hero.name]..."
            dwayne.say "Did that sound like a request?"
            dwayne.say "Because it was actually an order!"
            show dwayne upset
            "I take a step backwards, beginning to shake my head."
            bree.say "I don't think so, Dwayne."
            bree.say "In fact I think I'll be leaving."
            "Dwayne leans back in his chair."
            "His eyes narrowing as he watches me go."
            show dwayne angry
            dwayne.say "If you won't do what I need you to do, [hero.name]..."
            dwayne.say "Then you're of no use to me at all."
            dwayne.say "And if you walk out of that door, you're fired!"
            show dwayne annoyed
            "I hear every word that Dwayne says as he spits them after me."
            "But somehow I manage to keep holding my head up high."
            "And I also manage to walk out of the door without stopping too."
            "Which I guess means that I'm out of a job."
            "But who needs a job where you're expected to degrade yourself like that?"
            "Certainly not me!"
            $ hero.morality += 5
            $ hero.flags.office_boss = None
            $ hero.flags.office_fired_dwayne = True
            $ game.flags.job_day = False
    return

label dwayne_female_job_event_02:
    "I've started to feel more comfortable in my position as Dwayne's secretary recently."
    "Ever since he called me into his office and asked that I give him a certain kind of 'stress relief'."
    "Yeah, I know that would have been enough to make some girls quit on the spot."
    "But I always kind of knew Dwayne was going to be one of those guys."
    "And it sounds weird, but as soon as it was all out in the open, it somehow made the whole thing easier for me."
    "Now I kind of know how things really are around here, and I'm finding that I'm okay with it."
    "Dwayne's the sort of guy that I'd find attractive in any other setting."
    "And doing stuff with him in his office isn't exactly hard for me."
    "Plus the pay check is also helping me out a hell of a lot at the end of the month."
    "So I'm sort of winning twice over with this arrangement."
    "And when the phone on my desk rings, I don't hesitate to pick it up."
    bree.say "Hello?"
    dwayne.say "Hey, [hero.name]..."
    dwayne.say "I'm feeling pretty fucking stressed again."
    bree.say "Oh no, boss!"
    bree.say "Is there anything I can do for you?"
    "I can't help my voice sounding excited and more than a little mischievous as I say this."
    "And I have to keep myself from giggling, as I remember what happened the last time."
    dwayne.say "I think you know what I need from you, [hero.name]."
    dwayne.say "The same as last time - that dealt with the problem pretty damn well."
    bree.say "Okay, boss..."
    bree.say "I'll be right in!"
    "The last thing I remember being on Dwayne's agenda was a meeting."
    "And it was with a pretty important client too."
    "That must have come to an end by now, and taken it out of him as well."
    "No wonder he wants me to come in there and give him some relief!"
    bree.say "Here I am."
    bree.say "I came as quickly as I..."
    scene bg ceo with fade
    show ryan tux at left, dark, dark, dark, zoomAt(1.75, (250, 1240))
    show dwayne at center, zoomAt(1.75, (640, 1240))
    "As I open the door and walk into Dwayne's office, I get a real shock."
    "Because the client is still there, sitting on the other side of the desk!"
    "He's looking over his shoulder at me as Dwayne waves for me to come closer."
    dwayne.say "Right over here, [hero.name]..."
    dwayne.say "Just like the last time, okay?"
    "Dwayne pushes his chair back from the desk and gestures to his groin."
    "All of this makes it perfectly obvious that he wants me to give him oral."
    "But the client is right there, looking from one of us to the other."
    dwayne.say "[hero.name]..."
    dwayne.say "Is there some kind of problem here?"
    dwayne.say "Did you not hear what I just said?"
    menu:
        "As you wish boss":
            "It was a surprise to walk into Dwayne's office and be asked for oral the first time."
            "But on that occasion there was only the two of us in here, so it was a private affair."
            "This time I have the client staring right at me, as amazed at the request as I am."
            "It's obvious that Dwayne's doing this to flex on the guy."
            "To show off just how much loyalty and obedience he demands from those beneath him."
            "And that's what makes me hurry to do as he commands."
            bree.say "Yes, boss..."
            bree.say "Of course..."
            bree.say "Whatever you say!"
            "Nodding my head, I make my way past the other guy."
            scene
            show dwayne blowjob ceo surprised mid mc_date
            with fade
            "Then I kneel down in front of Dwayne as he unzips his pants."
            show dwayne blowjob opened
            "From that point on, all of my attention is on Dwayne."
            "On him and the need to carry out the task he's set for me."
            "But I can almost feel the eyes of the client on me the whole time."
            "I know that he has to be watching me intently, unable to believe what he's seeing."
            "And that's where the largest part of the thrill comes from for me."
            "I don't hesitate to reach out and take hold of Dwayne's cock the moment it emerges."
            "My hands are all over it in an instant, stroking and squeezing in order to get it hard."
            "Luckily for me, that's not something that takes long, as he's excited at the prospect too."
            "As soon as Dwayne's cock is as hard as I can get it, I lean my head in closer."
            show dwayne blowjob closed suck
            show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
            "Parting my lips, I take the head straight into my mouth and get down to business."
            "On another occasion I might have taken longer about it or been more gentle."
            "But my guess is that this whole thing is about making a lasting impression on the client."
            "That's why I go straight for the throat, in a manner of speaking."
            "Using my lips, tongue and teeth, I go hard at Dwayne right from the start."
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            "And he seems to appreciate my efforts too, grunting with appreciation."
            "But pretty soon I can hear him beginning to speak again."
            "I'm too engrossed in the task at hand to hear exactly what he's saying."
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            "But it sounds like he's restarted his conversation with the client."
            "It's even more impossible to tell what the other guy is saying."
            "Because his responses seem to come in tense bursts of sound."
            "That leads me to believe that what I'm doing is having the desired effect."
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob down
            pause 0.175
            show dwayne blowjob mid
            pause 0.175
            show dwayne blowjob up
            "This mingles with the thrill I'm getting from knowing there's someone watching."
            "And knowing how I'm being used to Dwayne's advantage spurs me on even more."
            "Head bobbing up and down ever faster, I work him for all I'm worth."
            "Soon enough I have Dwayne's cock almost all the way into my throat."
            show dwayne blowjob mid dwaynehand
            pause 0.15
            show dwayne blowjob down
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob up
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob down
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob up
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob down
            pause 0.15
            show dwayne blowjob mid
            pause 0.15
            show dwayne blowjob up
            "And then I hear him start to grunt again, like he's reaching his limit."
            "In that moment I know that I have to make a decision as to who to end this thing."
            menu:
                "Swallow his cum":
                    "I don't want to interrupt whatever Dwayne's saying right now."
                    "Plus swallowing his load would make him look even better, right?"
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.145
                    show dwayne blowjob mid
                    pause 0.135
                    show dwayne blowjob up
                    pause 0.13
                    show dwayne blowjob mid
                    pause 0.125
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    show dwayne blowjob down cum surprised with vpunch
                    "So I keep my head down and press on until the inevitable happens."
                    show dwayne blowjob up out closed swallow limp -onface -dwaynehand with vpunch
                    "That preparation means that I can handle him cuming without issue."
                    show sexinserts head bree -cum zorder 1 at center, zoomAt(1, (720, 810))
                    show dwayne blowjob opened tongueout
                    "I swallow the whole lot down, one gulp after another."
                "Pull his cock out":
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.145
                    show dwayne blowjob mid
                    pause 0.135
                    show dwayne blowjob up
                    pause 0.13
                    show dwayne blowjob mid
                    pause 0.125
                    show dwayne blowjob down
                    "Pulling Dwayne's cock out of my mouth might draw attention to myself."
                    "But surely taking it in the face makes him look even better, right?"
                    show dwayne blowjob down opened
                    pause 0.35
                    show dwayne blowjob mid
                    pause 0.35
                    show dwayne blowjob up out tongueout -onface -dwaynehand
                    "So when the time comes, I do just that, sitting patiently and waiting."
                    show dwayne blowjob closed with vpunch
                    "And when Dwayne finally shoots his load, I take it square in the face."
                    show dwayne blowjob closed cum with vpunch
                    "Not making a sound or flinching even once."
            hide sexinserts
            scene bg ceo
            show ryan at dark, dark, dark, zoomAt(1.75, (100, 1240))
            show dwayne at center, zoomAt(1.75, (640, 1240))
            with fade
            "When he's done, Dwayne pushes his cock back into his pants."
            "Then he waves for me to leave the room."
            dwayne.say "Thank you, [hero.name]..."
            show dwayne happy
            dwayne.say "That'll be all, for now."
            show dwayne smile
            "I do exactly as I'm told, getting up and nodding politely."
            "Then I walk straight out of his office without looking back once."
            "Sure, I need to clean myself up once I get back to my desk."
            "But it all feels worthwhile, knowing that I just helped Dwayne out."
            "Not to mention the excitement that I can still feel coursing through me."
            "And I can't help wondering when I'll be called on to do something like that again."
            if hero.morality > -65:
                $ hero.morality -= 1
            $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 3)
        "We're not alone mister":
            "It was a surprise to walk into Dwayne's office and be asked for oral the first time."
            "But on that occasion there was only the two of us in here, so I had that in my favour."
            "This time I have the client staring right at me, as amazed at the request as I am."
            "It's obvious that Dwayne's doing this to flex on the guy."
            "To show off just how much loyalty and obdience he demands from those beneath him."
            "And that's what makes my reaction different this time around."
            "Gathering all of my strength, I shake my head."
            bree.say "I heard what you said."
            bree.say "But I won't do it."
            bree.say "That's not part of my job description."
            show dwayne upset
            "I see Dwayne's face darken as I refuse to do as he asks."
            "And the look on the client's face becomes one of awkwardness and confusion too."
            "Before this was a chance for Dwayne to impress the guy, to come across as the big man."
            "But my refusal turns it into a tense and embarrassing exchange."
            dwayne.say "You might want to rethink your answer, [hero.name]."
            dwayne.say "Especially if you want to keep your position around here."
            show dwayne angry
            "It's not like Dwayne to resort to making straight-up threats like that."
            "Yet there's nothing else he can really do in order to save face."
            "The problem is that my mind's already made up."
            "I'm not going to do what he wants, and that's the end of it."
            bree.say "If this is the way I'm going to be treated, then so be it."
            bree.say "I'll go and collect my things right now."
            "With that, I turn on my heel and walk back the way I came."
            show dwayne upset
            dwayne.say "[hero.name]..."
            dwayne.say "You get back here right now!"
            dwayne.say "I swear that if you don't, you'll regret it!"
            show dwayne annoyed
            "It's not like I don't find all of Dwayne's threats scary."
            "Hell, I'm practically shaking by the time I make it out of his office."
            "I just keep telling myself that he's making all of them in front of a witness."
            "Which also means that he's making a rod for his own back when it all comes out later."
            "Even so, I don't wait around to see what happens next."
            "Instead I clear out my desk and sweep all of my things into my bag."
            "Then I walk out of there without stopping to look back."
            "I can deal with the fallout later."
            "Right now I just need to put as much distance between myself and Dwayne as possible."
            $ hero.morality += 5
            $ hero.flags.office_boss = None
            $ hero.flags.office_fired_dwayne = True
            $ game.flags.job_day = False
    return

label dwayne_female_job_event_03:
    "I'm starting to feel much more comfortable in my job as Dwayne's personal secretary."
    "And no small part of that is because I now know the kind of special duties expected of me."
    "Sure, for some people being asked to give the boss oral relief in times of stress would be a deal-breaker."
    "But the fact is that I kind of had the hots for Dwayne even before I took the job."
    "So it's not that big of a deal for me to accept him asking me to do that kind of thing."
    "Plus there's the very real thrill of knowing he might want it whenever he calls me up."
    "I do have to admit that him asking me to do it in front of a client was a bit of a shock."
    "But I still managed to pull it off, and I helped him psyche the guy out into the bargain."
    "Which means that I'm proving my worth around here, right?"
    "Another good thing is that all of this really balances out how boring the rest of the job is."
    "And more than once I find myself staring at the phone on my desk."
    "Hoping that it'll ring and the voice on the other end will be Dwayne's."
    play sound phone_ring loop
    "So when I do hear it ring, I drop what I'm doing and hurry over to answer the call."
    stop sound
    bree.say "Hello..."
    bree.say "[hero.name] here..."
    bree.say "How can I service you?"
    bree.say "I...I mean, how can I be of service to you?"
    "There's a slight pause before the person on the other end answers."
    "As if they're puzzling over my slip up, or else laughing to themselves about it."
    dwayne.say "I'm going to need you to step into my office, [hero.name]."
    "I feel a surge of relief as I hear Dwayne's voice on the other end."
    "Somehow I don't feel as bad about being humiliated in front of him as I would anyone else."
    bree.say "Okay, boss..."
    bree.say "I'll be right there!"
    bree.say "Oh..."
    bree.say "Are you feeling stressed-out again?"
    "Again there's a slight pause before Dwayne responds."
    dwayne.say "Let's just say the problem is definitely stress-related, [hero.name]."
    dwayne.say "I'll fill you in as soon as you get your ass in here."
    "I don't hesitate to put the phone down and hurry towards the door."
    "And then I go straight to Dwayne's office, already preparing myself for what lies ahead."
    "But as soon as I open the doors and walk in there, I'm greeted with an unexpected sight."
    scene bg ceo
    show ryan tux at center, blacker, zoomAt(1.65, (250, 1240))
    show dwayne at center, zoomAt(1.75, (640, 1240))
    with fade
    "I'd been assuming that Dwayne would be on his own, that his appointments were finished for the day."
    "Yet now I see that there's another guy sitting in the seat before his desk."
    "And as soon as I close the door behind me, he turns in my direction."
    "There's no way of hiding the fact that he's checking me out too."
    "I can practically feel his eyes sliding all over me."
    "And I just know that he likes what he's seeing too."
    bree.say "Erm..."
    bree.say "Here I am, boss..."
    show dwayne smile
    "Dwayne's smile is as broad as I've ever seen it right now."
    "He nods as I come to a stop a few feet from his desk."
    show dwayne happy
    dwayne.say "That's right, [hero.name] - there you are!"
    "I watch as he turns to the client sitting across from him."
    dwayne.say "You see what I mean now?"
    dwayne.say "How can you get a lick of work done with something like that on the end of the phone?"
    show dwayne smile
    "The man nods and lets out an amused chuckle, letting Dwayne know that he agrees."
    "But at the same time he doesn't say a word, or take his eyes off of me for an instant."
    show dwayne happy
    dwayne.say "[hero.name], I've been telling my friend here how good you are when it come to...relieving stress."
    dwayne.say "You see, he's in a very high-pressure position over at his own company."
    dwayne.say "And I told him that you'd be able to help out with that."
    dwayne.say "If you know what I mean?"
    dwayne.say "In fact, it's the thing that convinced him to give me the deal I wanted."
    dwayne.say "So I need you to seal it for me."
    show dwayne smile
    "All of a sudden the reality of the situation dawns on me."
    "This time Dewayne doesn't want me to go down on him in front of the client."
    "He wants me to go down on the client instead!"
    show dwayne shout
    dwayne.say "So what are you waiting for, [hero.name]?"
    dwayne.say "Get to it!"
    dwayne.say "Relieve the man's stress!"
    show dwayne normal
    menu:
        "As you wish boss":
            "Every time Dwayne's done this to me, he's subtly upped the ante."
            "First it was just him and me alone in here."
            "Then it was us with a stranger watching the proceedings."
            "And now it's me doing it to a stranger with Dwayne watching."
            "Every time I told myself that was as far as I could push it too."
            "But somehow I don't feel the urge to say no or turn and run away."
            "Instead I can feel a deep and powerful thrill building up inside of me."
            "Like we're about to do something that will really change things."
            "Like if we break this taboo, who knows where this thing could go next!"
            bree.say "Sure thing, boss..."
            bree.say "I'll get right on it!"
            "I add a nod, just to make sure that I get the message across."
            "And then I walk the rest of the short distance to where the client is sitting."
            show ryan at center, blacker, zoomAt(1.0, (250, 1240)), startle
            "He looks the most surprised out of the three of us right now."
            "As though he wasn't sure this thing would come off at all."
            "And now that it is, he's still not quite ready to believe it."
            "All the same, it's happening."
            "I know that for sure!"
            "Luckily for me, the guy pushed his chair back when I first came in."
            "That means I already have enough room to work with."
            scene bg black
            show bree cinema bj bree date office
            with fade
            "So I waste no time in kneeling down in front of him."
            "I don't wait for his permission before I reach out and open his flies."
            "And I don't pause as I reach inside, taking hold of his cock a moment later."
            "I'm relieved to find that it feel like one of a good size."
            "Plus he's already getting excited at the prospect of what's in store."
            "Both of those are good signs, meaning that I won't have my work cut out for me."
            "I figure that the best option is to get straight down to business, if you'll pardon the pun."
            "Not to mess around with a lot of teasing and foreplay."
            "So as soon as I have the guy's cock out of his pants, I get to it."
            "Leaning in close, I open my mouth and put the head straight inside."
            "At the same time I'm stroking the shaft with one hand."
            "And squeezing his balls with the other."
            show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810)) with dissolve
            "My lips and tongue don't need to be told what to do."
            "They spring straight into action as instinct takes over."
            "And my teeth come into play when the time feels right too."
            "Pretty soon I hit my stride, my head bobbing up and down."
            "The room seems to fade away as I close my eyes, losing myself."
            "And I can't hear anything that's being said in the office around me."
            "The only sounds that reach me are those of the client gasping."
            "That and the vague impression of Dwayne chuckling away to himself in the background."
            "I choose to take both as signs that I'm doing well."
            "But for the most part, I focus my attention on the task at hand."
            "I don't know if it's my skill that's responsible."
            "Or else the circumstances making the client extra sensitive."
            "But either way I can soon sense that he's on the verge of losing it."
            "Which means that I have to make a decision as to how this is going to end."
            "Keeping up the idea of being all business, I don't change a thing."
            show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
            show bree cinema bj cum
            with vpunch
            "I just keep on going until the moment the client shoots his load."
            with vpunch
            "And then I swallow every single drop without complaint."
            "Because what else would an efficient personal assistant do?"
            "As soon as it's over, I get up and nod to Dwayne."
            scene bg ceo
            show dwayne smile at center, zoomAt(1.75, (640, 1240))
            with fade
            bree.say "Will there be anything else?"
            "Dwayne shakes his head, unable to hide his pleasure at how things went down."
            show dwayne happy
            dwayne.say "No, [hero.name]..."
            dwayne.say "I think you took care of everything."
            show dwayne smile
            "I nod and then turn on my heel, walking out of the office."
            "I don't even bother to glance in the client's direction even once."
            scene bg office with fade
            $ game.room = "office"
            "As soon as I'm back in my own office, I clean myself up."
            "And then I do the best I can to get back to my work."
            "Which is hard, because I'm still buzzing from the excitement of what I just did."
            if hero.morality > -65:
                $ hero.morality -= 1
            $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 3)
        "You think I’m your toy !!?":
            "Okay, so it was one thing for Dwayne to ask me for oral at work."
            "And yeah, it was going even further for him to get me to do it in front of a client."
            "But both of those times it was between me and him."
            "Even if the other guy was watching the second time around."
            "This is something different though, this is him demanding I do it to other guys."
            "And that is definitely not cool with me!"
            bree.say "You know what, boss..."
            bree.say "I don't think that's going to happen."
            show dwayne upset
            "The client looks at Dwayne, raising his eyebrows as he does so."
            "It's clear that he's asking an unspoken question."
            "Presenting Dwayne with the chance to assert himself."
            show dwayne shout
            dwayne.say "I don't think I heard you right, [hero.name]."
            dwayne.say "For a moment I thought you said you were calling the shots here..."
            dwayne.say "That you were saying how things were going to happen?"
            show dwayne upset
            "I do the best I can to ignore how deep Dwayne's voice is."
            "And to ignore just how large of a frame he has."
            "As well as how he uses them both to intimidate."
            bree.say "When it comes to my body..."
            bree.say "That's exactly how it is."
            "I take a step backwards, meaning to start making my exit."
            hide ryan with dissolve
            show dwayne smile at center, zoomAt(1.75, (640, 1240)) with ease
            "As soon as I do, Dwayne leans forwards and fixes me with a mean stare."
            show dwayne angry
            dwayne.say "[hero.name]..."
            dwayne.say "Think very carefully about what you do next."
            dwayne.say "Because if you disobey me, there's no future for you in my employ!"
            show dwayne upset
            "I wait just long enough to give this a nod."
            "Then I turn on my heel and march straight out of there."
            "Any moment I expect Dwayne to say something else."
            "Or maybe even to get up and come after me."
            "I can feel my heart beating faster with each step I take."
            "And by the time I reach the doors, it's hammering like crazy."
            "I manage to hold it in until the doors are closed behind me."
            scene bg office with fade
            "Then my nerve finally breaks, and I rush back into my own office."
            "I don't stop to catch my breath, not even for a moment."
            "Instead I thrust all of my things into my bag."
            scene bg street with fade
            $ game.room = "street"
            "And then I hurry out of there, rushing straight out of the building."
            "Because I'm not going to give Dwayne the chance to fire me."
            "Not when I can quit myself and escape with a little of my dignity intact."
            $ hero.morality += 5
            $ hero.flags.office_boss = None
            $ hero.flags.office_fired_dwayne = True
            $ game.flags.job_day = False
    return

label dwayne_female_job_event_04:
    "I'm kind of liking the feeling of working for Dwayne this morning, you know?"
    "Like I'm getting a good vibe as I wander around the office doing this and that."
    "Plus the amount of work that's landing on my desk doesn't seem to be all that crazy."
    "At this rate I should be able to do whatever Dwayne's expecting of me."
    "And without flogging myself to death by the end of the day too."
    if hero.name.lower() in ['bree']:
        aletta.say "Gouda?"
    else:
        aletta.say "Bree?"
    "All of a sudden I hear what sounds like someone naming a random cheese."
    show aletta work at center, zoomAt(1.25, (640, 880)) with dissolve
    "And when I look up, I see that one of my new colleagues is standing in front of me."
    "She's the tall, bossy one that always looks like she has a hair up her ass."
    "Aletta...or at least I think that's her name."
    "Before I can say a word, she does it a second time."
    show aletta talkative
    if hero.name.lower() in ['bree']:
        aletta.say "Gouda?!?"
    else:
        aletta.say "Bree?!?"
    show aletta normal
    "Now she's really staring at me hard."
    "Like there's something important that I'm not getting."
    show aletta angry
    if hero.name.lower() in ['bree']:
        aletta.say "Didn't you hear me, Gouda?!?"
    else:
        aletta.say "Didn't you hear me, Bree?!?"
    show aletta upset
    "More than a little confused, I give her the only response that seems to make sense."
    bree.say "Wensleydale?"
    show aletta stuned
    "Aletta's eyes go wide with surprise."
    bree.say "Cheddar?"
    "Nope, that doesn't seem to do it either."
    bree.say "Monterey Jack?"
    show aletta annoyed
    "Aletta makes a snorting sound at this."
    "And I see that she's clenching her fists too."
    show aletta surprised
    if hero.name.lower() in ['bree']:
        aletta.say "Gouda, for god's sake..."
    else:
        aletta.say "Bree, for god's sake..."
    aletta.say "Why are you naming cheeses?!?"
    show aletta stuned
    "I shrug and shake my head."
    bree.say "You started it, Aletta!"
    show aletta angry
    aletta.say "I most certainly did not!"
    show aletta upset
    bree.say "Yes you did."
    bree.say "You just walked up to me and shouted 'Gouda' for no good reason!"
    show aletta angry
    aletta.say "Well, isn't that your name?!?"
    show aletta upset
    "I blink in sheer amazement."
    bree.say "Of course not!"
    bree.say "My name's '[hero.name]'!"
    show aletta stuned
    "Aletta looks like I just slapped her in the face."
    "But she soon recovers enough to ask another question."
    show aletta embarrassed
    aletta.say "Wait..."
    if hero.name.lower() in ['bree']:
        aletta.say "Is that spelled B...R...I...E?"
        show aletta normal
        bree.say "No, that's the cheese!"
        bree.say "It's B...R...E...E!"
    show aletta normal blush
    "I watch as this seems to sink in, and Aletta slowly turns a bright shade of red."
    "Though I'm not sure it it's from embarrassment or anger."
    show aletta embarrassed
    aletta.say "I think I know what's happened here...[hero.name]."
    show aletta annoyed
    "Aletta looks back over her shoulder, and I follow her gaze."
    "Just in time to see two heads poking around a corner."
    "One's unmistakably [mike.name], and the others one of the other girls who works with him."
    "It's not the pretty one called Lavish, or the shy Asian girl called Shiori."
    "So that means it must be Audrey."
    "And as they're both laughing right now, I guess that tells me a lot about her personality too!"
    show aletta whining -blush
    aletta.say "I'm sorry, [hero.name]."
    show aletta talkative
    aletta.say "Save to say I won't be relying on [mike.name] or Audrey for my information anytime soon."
    aletta.say "What I wanted to say was that Dwayne's called a meeting in a couple of minutes."
    show aletta normal
    "As soon as I hear that, I scoop up my notebook and pen."
    bree.say "Sure thing, Aletta..."
    bree.say "Is it in the big boardroom?"
    "Aletta raises an eyebrow, as if impressed by my enthusiasm."
    show aletta happy
    aletta.say "Yes, [hero.name]..."
    show aletta talkative
    aletta.say "But there's no need for you to sit in on it."
    aletta.say "We don't need notes taking this time."
    aletta.say "Though we could use a cafetiere of coffee bringing in."
    aletta.say "Do you have the time to make one up?"
    show aletta normal
    "I nod as I put my notepad down."
    "Sure, it's not a glamorous job."
    "But I'm doing sod all else at the moment."
    bree.say "Okay, Aletta."
    show aletta talkative
    aletta.say "Thank you, [hero.name]..."
    aletta.say "You're a lifesaver."
    hide aletta normal with easeoutleft
    "As soon as Aletta strides off into the boardroom, I glare over at [mike.name] and Audrey."
    show mike work smile at center, zoomAt(1.0, (640, 760))
    show audrey work at center, zoomAt(1.0, (240, 720))
    with easeinleft
    "They're already sauntering over in this direction, probably on the way to the meeting too."
    if hero.morality >= 25:
        bree.say "[mike.name]..."
        bree.say "That wasn't very nice of you!"
        "[mike.name] waves my protests away, and Audrey seems unimpressed too."
    elif hero.morality >= -25:
        bree.say "Very funny, [mike.name]!"
        bree.say "You'll be sending me to get some tartan paint next."
        "[mike.name] waves my protests away without hesitation."
        "But I notice Audrey watching me with more caution."
    else:
        bree.say "That wasn't very original, [mike.name]..."
        bree.say "I thought you'd at least manage to work a pussy reference in there somewhere!"
        "[mike.name] waves my protests away without hesitation."
        "But I notice Audrey watching me with something that looks more like interest."
    show mike happy
    mike.say "Ah, come on, [hero.name]..."
    mike.say "Everyone gets pranked when they're new."
    show mike smile
    show audrey mock
    audrey.say "He's right, it's a tradition!"
    hide audrey normal
    hide mike
    with easeoutleft
    "With that, they both follow Aletta into the boardroom."
    "Which leaves me to get up and see to that coffee."
    scene bg black
    show shiori_sleep_office_bg
    with fade
    "Although I pause to lean over my desk first."
    "Because I want to make sure everything is arranged just so."
    dwayne.say "Mmm...mmm!"
    dwayne.say "The sun is definitely out this morning."
    dwayne.say "Or maybe the full moon didn't set just yet!"
    scene bg office
    show dwayne smile at center, zoomAt(1.0, (340, 760))
    with hpunch
    "At the sound of Dwayne's voice, I spin around."
    "And I can't help the instinct to pull down my skirt too."
    bree.say "Oh..."
    bree.say "Good morning, Mister Dwayne!"
    "The moment I say it, I want to kick myself."
    "I mean, what kind of a moron would call him that?!?"
    "Luckily for me, Dwayne seems to be in too good of a mood to even notice."
    show dwayne happy
    dwayne.say "Good morning to you too, Miss [hero.name]!"
    dwayne.say "Hold my calls while I'm in this meeting and then for half an hour afterwards, okay?"
    hide dwayne smile with easeoutleft
    "I nod and smile as Dwayne turns on his heel, then strides off towards the boardroom."
    "Again I find myself alone at my desk, but this time I don't hang around."
    scene bg breakroom with fade
    "Instead I head straight over to the small kitchen located nearby."
    "Once there, I set about making the cafetiere of coffee Aletta asked for."
    "And as I wait for it to be done, enjoying the aroma, I fix a jug of water too."
    "I mean sure, nobody asked for it."
    "But it doesn't hurt to show some initiative, right?"
    "As soon as everything is done, I arrange it on a tray."
    "Then I carry it into the boardroom, praying the whole time that I don't drop the whole thing."
    show shiori_stretch_bg
    show dwayne shout at center, zoomAt(1.5, (640, 1060))
    with fade
    dwayne.say "Don't give me that, [mike.name]..."
    dwayne.say "You sound like you have shit for brains!"
    show dwayne normal
    "I do the best I can to ignore the meeting that's in progress as I walk through the door."
    "But there's no way to stop everyone looking up at me as I do so."
    "And I can't help feeling a little thrill as I catch Dwayne in the middle of chewing [mike.name] out."
    "Sliding the tray onto the table along the nearest wall, I turn to walk out again."
    show dwayne happy
    dwayne.say "Ah, [hero.name]..."
    dwayne.say "Would you do me a favour?"
    show dwayne normal
    bree.say "Erm..."
    bree.say "Sure, Dwayne."
    bree.say "What is it?"
    show dwayne happy
    dwayne.say "I'd be obliged if you'd pour me a cup of that fine-smelling coffee there."
    show dwayne normal
    "I nod and turn to do as Dwayne asked."
    "And as I do so, I'm expecting the meeting to resume."
    aletta.say "So..."
    aletta.say "Where were we?"
    audrey.say "I believe we were discussing [mike.name] having shit for brains."
    mike.say "HEY!"
    show dwayne angry
    dwayne.say "Ssshh!"
    show dwayne vangry
    dwayne.say "Shut up, all of you."
    dwayne.say "You're ruining my appreciation of that fine, fine..."
    "I'm waiting for Dwayne to say 'coffee'."
    "But then he says something else entirely."
    show dwayne happy
    dwayne.say "Ass..."
    dwayne.say "Oh yeah, that's one of the best we've had around here in a long while!"
    show dwayne smile
    "My eyes go wide as I realise that Dwayne must be talking about me."
    "And when I turn around, I see that all of them are staring in my direction."
    aletta.say "Dwayne..."
    aletta.say "I hardly think this is an appropriate topic of conversation!"
    "Still looking straight at me, Dwayne dismisses her with a wave of his hand."
    show dwayne shout
    dwayne.say "Shut your hole, Aletta..."
    dwayne.say "You lost your right to comment when you let your ass go to rack and ruin."
    show dwayne normal
    "Aletta gasps and looks horrified."
    "[mike.name] looks more than a little confused."
    "Audrey lets out a wicked chuckle of amusement."
    "But Dwayne turns on her in an instant."
    show dwayne shout
    dwayne.say "You better can it too, Audrey..."
    dwayne.say "As your ass is starting to look like a sack of shit too!"
    show dwayne normal
    "Before I was surprised, but now I'm totally shocked."
    "And the only thing I can think to do is keep on performing the task at hand."
    "So I walk the short distance to the table, and put the coffee down in front of Dwayne."
    bree.say "Here's your coffee, sir."
    show dwayne smile
    "Dwayne's smile reappears in an instant."
    "He picks up the cup and takes in a hearty nose-full of the aroma."

    hide dwayne
    show slap dwayne dwayne_casual at center, zoomAt (1.5, (740, 720))
    with fade
    "But then I feel his other hand clamp down on one of my buttocks!"
    dwayne.say "Mmm..."
    dwayne.say "Now that's what a man need to motivate him in the workplace..."
    dwayne.say "A beautiful, soft buttock to get him good and hard!"
    "As he's saying all of this, I feel Dwayne kneading my butt-cheek."
    "And boy, is he ever going for it."
    "At this rate he'll leave me with a bruise the shape of his hand!"
    menu:
        "Make Dwayne stop":
            "I don't pause or hesitate to pull away from Dwayne's grasp."
            hide slap
            show dwayne therock at center, zoomAt(1.5, (640, 1060))
            with hpunch
            "He tries the best he can to reach out and get hold of me again."
            "But I manage to avoid his groping hands this time."
            "[mike.name], Audrey and Aletta are all staring at me in amazement too."
            "Though I can see that each of them is surprised for a different reason."
            "[mike.name] looks shocked, but his eyes are wide too, like he's unconsciously excited."
            "Aletta looks more jaded than anything else, as though she's seen all of this before."
            "But Audrey appears to be intrigued by what she's seeing, drawn to the drama of it all."
            if hero.morality >= 25:
                "Whatever the case, I'm not staying here a second longer than I have to."
                "I don't care what any of them think, I have to get out of there."
                "So I dash straight out, tears streaming down my face."
                scene bg office with fade
                "And once I'm back at my desk, I sink into my chair."
                "Then I pray that nobody else sees me before the end of my working day."
            elif hero.morality >= -25:
                "Without thinking, I turn and point a finger in Dwayne's face."
                bree.say "You keep your filthy hands to yourself."
                bree.say "And next time, get your own damn coffee!"
                "Then I turn and walk straight out of the room."
                scene bg office with fade
                "And once I'm back at my desk, I sink into my chair."
                "Then I pray that nobody else sees me before the end of my working day."
            else:
                "I raise an eyebrow and cross my arms over my chest."
                "Then I shake my head at Dwayne."
                bree.say "Oh man, you can cut that shit right out."
                bree.say "Undressing me with your eyes is one thing, Dwayne."
                bree.say "But until you're paying me way more, you can keep your filthy hands to yourself!"
                "With that, I turn and walk straight out of the room."
                scene bg office with fade
                "And once I'm back at my desk, I sink into my chair."
                "Resolving to stay there until the end of my working day."
            $ hero.morality += 5
            $ dwayne.love -= 2
        "Let Dwayne continue":

            "Part of me knows that I should have done something to stop him by now."
            "Yelled, or slapped him across the face as soon as his hand touched me."
            "Hell, I bet someone else would have straight up dumped the coffee onto his big, bald head!"
            "But I'm just too shocked to be able to move a muscle at first."
            "And by the time it feels like the shock is past, it's just too late."
            "[mike.name], Audrey and Aletta are all staring at me in amazement too."
            "And it's as if their stares are rooting me to the spot."
            if hero.morality >= 25:
                "I stand there for a few more second, feeling filthy and used."
                "Then it all gets to be too much for me, and I just burst into tears."
                "I don't care what any of them think, I have to get out of there."
                "So I dash straight out, tears streaming down my face."
                scene bg office with fade
                "And once I'm back at my desk, I sink into my chair."
                "Then I pray that nobody else sees me before the end of my working day."
            elif hero.morality >= -25:
                "I want to turn and run straight out of there."
                "But for some reason the fear keeps me standing there."
                "And all the time Dwayne is feeling up my ass."
                "I don't know how long it lasts, only that it feels like forever."
                "When it's finally over, I turn and shuffle out of there."
                scene bg office with fade
                "And once I'm back at my desk, I sink into my chair."
                "Then I pray that nobody else sees me before the end of my working day."
            else:
                "I stand there feeling filthy and used, my cheeks burning with shame."
                "But the odd thing is that I don't even think of pulling away for a second."
                "The feeling of being manhandled and treated like an object."
                "The sensation of their eyes on me all the time it's happening."
                "All of it combines to make me feel a powerful thrill."
                "More than that, a genuinely sexual excitement."
                "When it's finally over, I turn and shuffle out of there."
                scene bg office with fade
                "And once I'm back at my desk, I sink into my chair."
                "Trying to resist the urge to reach under my skirt and relieve the frustration I'm feeling."
            $ hero.morality -= 5
            $ dwayne.love += 2
            $ mike.love += 1

    return

label dwayne_female_job_event_05:
    "I'm just sitting at my desk, minding my own business and pretending to work."
    play sound phone_ring loop
    "And that's when my phone starts to ring, making me look up in genuine surprise."
    "Seriously, it's been so long since I used anything that wasn't a mobile."
    "That's why it takes me a moment to shake of my surprise and actually pick up the receiver."
    stop sound
    bree.say "Erm..."
    bree.say "Hello..."
    bree.say "This is [hero.name]!"
    "I hear an unmistakable chuckle on the other end of the line."
    "It's deep, rumbling and totally masculine."
    "Which kind of means there's only one person it can be."
    dwayne.say "Hello, [hero.name]..."
    dwayne.say "This is Dwayne!"
    "I feel a flush of embarrassment as Dwayne imitates me."
    "But I still do the best I can to ignore it and do my job."
    bree.say "Hey, Dwayne..."
    bree.say "Was there something you wanted me to do for you?"
    bree.say "Or did you just want to have a little chat?"
    "Dwayne chuckles again."
    "Like my little dig disguised as a joke didn't even land."
    dwayne.say "Would you mind stepping into my office for a moment, [hero.name]?"
    dwayne.say "Something just came up, and I could use your help with it."
    "I can't help nodding."
    "Even though I know Dwayne can't see me right now."
    bree.say "Okay, Dwayne..."
    bree.say "I'll be right there."
    "As soon as I put the phone down, I'm up and out of my chair."
    "But as I make it to the doors that lead to Dwayne's office, something occurs to me."
    "He never actually said what the thing he needed help with was."
    "For a moment I think about calling him back, but then I dismiss the idea."
    "Whatever it is, I can always come back to my desk for anything I might need."
    "So taking a deep breath, I push open the doors to Dwayne's office."
    scene bg ceo with fade
    "And then I step inside, ready to be a good, helpful employee."
    show dwayne at center, zoomAt(1.25, (940, 1000)) with dissolve
    "Dwayne's sitting at his desk."
    "The same one that I'm sure is deliberately made to look like a bloody throne."
    "And he looks up as soon as the sound of me walking in reaches him."
    show dwayne happy
    dwayne.say "Get over here, [hero.name]..."
    dwayne.say "Come on!"
    show dwayne smile
    "Normally this wouldn't be an issue for me."
    "But the problem is that Dwayne's office is fucking huge!"
    "So from here there's no chance of being able to see what he's doing."
    show bg ceo at center, traveling(1.5, 0.5, (340, 940))
    show dwayne at center, traveling(1.75, 0.5, (640, 1240))
    "This means I have to hurry over there, almost at a jog."
    "And when I finally get to his desk, I stop there, waiting to be told what he needs of me."
    "But instead, Dwayne motions for me to come closer still."
    show dwayne happy
    dwayne.say "No, [hero.name]..."
    dwayne.say "Closer than that."
    dwayne.say "Come around to my side of the desk."
    show dwayne smile at center, zoomAt(1.75, (640, 1240))
    "I obey without really thinking about it."
    "And as I walk around the desk, I naturally look down at Dwayne."
    "Which is when I see that there's something sticking up in front of him."
    "My expression must change as I realise just what the thing actually is."
    show dwayne smile
    show dwayne at center, zoomAt (1.0, (640, 1240)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 1240)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 1240)), startle(0.14,-20)
    "Because I can hear Dwayne begin to laugh again."
    bree.say "Is that..."
    bree.say "Are you..."
    bree.say "Is it really..."
    show dwayne happy
    dwayne.say "Yeah, [hero.name] - that's my dick!"
    dwayne.say "And don't you worry."
    dwayne.say "The sight of it tends to have that effect on people!"
    show dwayne smile

    "It is not the first time I see it but..."
    "I'm still more than stunned to be staring at Dwayne's fully erect manhood."
    "There it is, larger than life and bulging out of his open flies."
    bree.say "What's going on here, Dwayne?"
    if hero.morality >= 25:
        bree.say "Why are you showing me that...that thing?!?"
    show dwayne happy
    if hero.morality >= 25:
        dwayne.say "Because this is what came up, [hero.name]!"
        dwayne.say "And I'm going to need you to handle it for me."
    dwayne.say "I'm going to need you to handle it for me."
    dwayne.say "So why don't you get down on your knees and take care of that bad boy?"
    show dwayne normal
    menu:
        "Tell Dwayne to get lost":
            "I'm already shaking my head and backing away as Dwayne's saying all of this."
            bree.say "Oh no..."
            bree.say "I think you'll find that is NOT in my job description!"
            show dwayne vangry
            dwayne.say "Hey..."
            dwayne.say "Where'd you think you're going?"
            dwayne.say "Your job description is whatever the hell I say it is!"
            show dwayne upset
            "I don't stop for a second, not even when Dwayne starts making threats."
            "I just turn around and walk straight out of his office."
            scene bg office with fade
            "And then I go back to my desk and the task of trying to look busy."
            "Because Dwayne can threaten me all he likes, even fire me."
            "But I am not letting him use me for sexual relief in the workplace!"
            $ hero.morality += 5
        "Agree to suck Dwayne's cock":
            if hero.morality >= 25:
                "I have to admit that I'm totally shocked by the demand."
                "But at the same time, I want to keep my job."
                "So what other choice do I have?"
                bree.say "O...okay, Dwayne..."
                bree.say "If that's really what you want..."
            elif hero.morality >= -25:
                "This is all coming as a bit of a shock."
                "But then maybe I should have suspected Dwayne would pull something like this on me."
                "I mean, it's kind of forward on his part...but it does look pretty inviting!"
                bree.say "Okay, Dwayne..."
                bree.say "But don't get the idea this is going to be a regular thing!"
            else:
                "I just can't take my eyes on the Dwayne's magnificent manhood."
                "And all this is happening just as I was thinking this job was totally boring."
                "I can't believe I'm finally getting paid to do this kind of thing!"
                bree.say "No need to beat about the bush, Dwayne..."
                bree.say "Next time you want this, just call me up and ask!"
            $ hero.morality -= 1
            show dwayne smile
            "Dwayne nods and gives me an extra-wide smile as I approach him."
            "And I begin to get down onto my knees, reaching out for it with one hand."
            "Oh man...it's even bigger up close!"
            "How in the hell am I going to fit this monster into my mouth?"
            scene bg black
            show dwayne blowjob ceo casual
            with fade
            "I lean my head forwards and get myself into position."
            "But now I can see how big the space under Dwayne's desk is."
            "So I scoot under it, thinking that nobody else will see me there."
            show dwayne blowjob suck
            "And then I open my mouth, beginning to take the head between my lips."
            "Now that I'm fully committed to the act, that seems to settle my nerves."
            "I manage to tune everything else out and just concentrate on the task at hand."
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            "And pretty soon my head is bobbing up and down smoothly."
            "At the same time I'm using my tongue and teeth to add to the experience."
            "All the while knowing that I'm doing a damn good job too."
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            "Because I can feel Dwayne leaning back in his seat as I pleasure him."
            "That and hear the sound of him gasping and moaning at my efforts."
            play sound door_open
            "Suddenly there's the sound of the office doors opening."
            show dwayne blowjob down surprised with vpunch
            "And I feel Dwayne jerk in his seat, pushing his cock further down my throat!"
            "Not prepared in the slightest, I almost choke on the damn thing."
            show dwayne blowjob mid closed
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            pause 0.3
            show dwayne blowjob mid
            pause 0.3
            show dwayne blowjob up
            "But somehow I manage to recover and keep on going."
            "Though I'm also straining to hear what's going on above me too."
            "Because someone definitely just walked into Dwayne's office."
            "And he doesn't seem to be handling it well at all."
            show dwayne blowjob mid opened
            "I can hear him arguing with a woman."
            "One that sounds like she's got a foreign accent."
            dwayne.say "Wha..."
            dwayne.say "What are you doing here?!?"
            cherie.say "Well, isn't that a nice way to greet your wife?"
            cherie.say "Especially when I've come all the way here to surprise you!"
            dwayne.say "Goddamit, Cherie..."
            dwayne.say "I told you before, you can't just come barging in here whenever you feel like it!"
            "Of course, that must be Cherie, his wife!"
            "Oh man, any other circumstances and I'd be laughing at him right now."
            "The idea of Dwayne, the swaggering CEO of the company, getting brow-beaten by his wife!"
            "Or at least I would be laughing if I didn't have her husband's cock in my mouth!"
            menu:
                "Stop sucking Dwayne's cock":
                    "I'm pretty sure that there's no way Dwayne's wife can see me down here."
                    "But at the same time, I know I can't just keep on going while she's in the room."
                    show dwayne blowjob up out
                    "So with that in mind, I let Dwayne's cock slide out of my mouth."
                    "And I rack my brain for some kind of way to get out of this mess."
                    "It's about then that I see something on the floor."
                    "It's in a far corner under the desk and kind of tangled in the carpet pile."
                    "But I can see that it's glinting, so I tug it loose and examine my find."
                    "And you can imagine my delight when I see it's a cufflink."
                    "Not only that, but an expensive-looking one with Dwayne's initials on it."
                    "Now this is going to mean taking a risk."
                    "But I think I can guess who bought it for him."
                    "And if I'm right, it might be just what I was looking for."
                    bree.say "Found it!"
                    "I stick a hand up from under the desk as I shout this out."
                    scene bg ceo
                    show cherie stuned at center, zoomAt(1.1, (340, 760))
                    show dwayne therock at center, zoomAt(1.75, (940, 1240))
                    with fade
                    "The effect seems to be pretty instant as I emerge a moment later."
                    "Dwayne looks almost as shocked as his wife."
                    "And both of them are staring at me right now."
                    show cherie surprised at center, zoomAt(1.0, (340, 760)), startle
                    cherie.say "DWAYNE!"
                    cherie.say "Why is there a young girl under your desk?"
                    cherie.say "What was she doing down there?!?"
                    show cherie upset
                    "Dwayne doesn't look like he's going to answer the question any time soon."
                    "So I step up to the challenge."
                    "Putting on my best surprised look as I turn to face Cherie."
                    bree.say "Oh..."
                    bree.say "Hello, madame."
                    bree.say "I was just looking for something my boss mislaid."
                    "I hold out the cufflink for her to see."
                    bree.say "He's been searching for it all morning."
                    bree.say "Telling me how important it was that we find it."
                    show cherie annoyed
                    "Cherie struggles to see what I have in the palm of my hand."
                    show cherie stuned
                    "But when sees the cufflink clearly, her eyes go wide."
                    "And then she plucks it up before I can say another word."
                    show cherie surprised
                    cherie.say "Mon Dieu!"
                    show cherie happy
                    cherie.say "This is one of the cufflinks I bought for him..."
                    cherie.say "To mark the anniversary of our wedding day!"
                    show cherie smile
                    show dwayne annoyed
                    "I steal a glance at Dwayne while his wife is marvelling at the cufflink."
                    "And for a brief moment I see the usual swaggering confidence is gone."
                    "In it's place is the pale face of a guy that knows he was about to get caught."
                    show dwayne smile
                    "But all it takes is a shake of the head, and the old Dwayne is back again."
                    show dwayne happy
                    dwayne.say "That's why I didn't want you in here, Cherie..."
                    dwayne.say "I wanted to find the cufflink first."
                    dwayne.say "You know, so that you wouldn't be upset I'd mislaid it?"
                    show dwayne smile
                    "Cherie turns her attention to Dwayne, and she seems to be buying it."
                    "Because she hands the cufflink to him and nods happily."
                    "Then she nods to me, before turning on her heel and walking away."
                    hide cherie with easeoutleft
                    "Once she's gone, Dwayne turns his attention to me."
                    show dwayne smile
                    dwayne.say "That was some real quick thinking there, [hero.name]..."
                    dwayne.say "And never let it be said that I don't reward those who help me out in a jam."
                    dwayne.say "You'll find my thanks in the form of a bonus when you get your next paycheck."
                    scene bg office with fade
                    "I can't help smiling as I leave his office."
                    "Because that's probably the easiest bonus I ever made!"
                    $ hero.money += 500
                "Keep on sucking Dwayne's cock":
                    "I'm pretty sure that there's no way Dwayne's wife can see me down here."
                    "And I'm not about to stand up and try to explain myself to her either."
                    "So I figure that the best thing I can do is just keep right on going."
                    show dwayne blowjob mid closed
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    "Sure, stopping the blow-job might sound like the more sensible choice."
                    "But if I do that, Dwayne might jerk in his seat or jump up in surprise."
                    "And that would surely give the game away to his wife."
                    "The craziest idea I can come up with is that he might react badly if I stop too."
                    "Like deliberately let her see what I'm doing and then blame the whole thing on me."
                    "I mean, I don't know his wife at all."
                    "She might be the kind of woman that would believe him if he told her I seduced him or something!"
                    show dwayne blowjob mid closed
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    "So that's why I just keep right on going, working away on his as best I can."
                    "At the same time I can hear them going back and forth."
                    "But the level of concentration required means that I can't make any of the bickering out."
                    show dwayne blowjob mid closed
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    pause 0.3
                    show dwayne blowjob mid
                    pause 0.3
                    show dwayne blowjob up
                    "Soon enough the sound of it fades, and I take that to mean Dwayne's wife has left."
                    "And it seems to have had an effect on him too, as I feel him twitching a second later."
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob up
                    pause 0.15
                    show dwayne blowjob mid
                    pause 0.15
                    show dwayne blowjob down with vpunch
                    pause 0.145
                    show dwayne blowjob mid
                    pause 0.135
                    show dwayne blowjob up
                    pause 0.13
                    show dwayne blowjob mid
                    pause 0.125
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    show dwayne blowjob down cum surprised with vpunch
                    "Dwayne gasps as he lets himself go in my mouth, and I struggle to swallow it all."
                    with vpunch
                    "As soon as he's done, I let his cock slide out of my mouth."
                    "Then I climber out from under the desk, trying to make myself look vaguely decent."
                    scene bg ceo
                    show dwayne smile at center, zoomAt(1.75, (640, 1240))
                    with fade
                    "Dwayne leans back in his chair as he pushes his cock back into his pants."
                    "And he gives me a satisfied smirk as he zips up his flies."
                    show dwayne happy
                    dwayne.say "Apologies for the unscheduled interruption there, [hero.name]."
                    dwayne.say "Cherie has a habit of bursting in on me unannounced."
                    dwayne.say "But I have to say, you handled that like a pro!"
                    show dwayne smile
                    "Not really sure how to take the compliment, I just nod."
                    bree.say "Thank you, Dwayne..."
                    bree.say "I try my best."
                    "I can feel Dwayne's eyes on me as I turn and walk out his office."
                    "And I get the distinct impression that this kind of thing might be more common that I thought around here."
    $ hero.flags.dwayne_office_job_delay = TemporaryFlag(True, 3)
    return

label dwayne_birthday_date_female:
    $ DONE["dwayne_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg map with fade
    "I've known for a while now that Dwayne's birthday was coming up."
    "And more than once I tried to suggest something we could do to celebrate."
    "But he always dumped on my ideas and then suggested the same thing."
    "That we meet up at his place to celebrate instead of going out."
    "I kept on racking my brain to think up other stuff."
    "And Dwayne kept right on shooting them down too, right up until the last minute."
    "Which makes me think that was his plan all along, as now it's the only option left."
    scene bg mansionentrance at center, zoomAt(1.0, (640, 720)) with fade
    "So with all of that in mind, I find myself standing outside the gates to his place."
    "Or to be more precise, with them looming over me."
    "There's nothing else to do but press the button on the intercom and wait."
    "I definitely heard the thing buzz, but nothing seems to happen."
    "So I press it again and wait a second time."
    "And finally I hear a voice on the other end."
    dwayne.say "Well, hello there, [hero.name]!"
    dwayne.say "Don't stand around out there."
    dwayne.say "Come on in..."
    "A moment later the gates start to move, swinging inwards to let me enter."
    "There's a click from the intercom."
    "Which I take to mean that Dwayne's no longer on the other end."
    show bg mansionentrance at center, traveling(1.25, 1.0, (540, 820))
    "So left with no other choice, I start the long walk up the driveway."
    scene bg door mansionentrance
    show dwayne smile at center, zoomAt(1.25, (640, 920))
    with fade
    "And when I finally reach the front of the house, Dwayne's there waiting for me."
    show dwayne happy
    dwayne.say "Hey, [hero.name]..."
    dwayne.say "Great to see you finally made it up here."
    show dwayne normal
    bree.say "Phew..."
    bree.say "Yeah, Dwayne..."
    bree.say "Your driveway's pretty long."
    show dwayne shout
    dwayne.say "I wouldn't know, [hero.name]..."
    dwayne.say "I always have my chauffer drive me wherever I want to go."
    show dwayne normal
    "I don't know if Dwayne's doing it on purpose."
    "But he's really starting to rub me up the wrong way."
    menu:
        "Grit my teeth and ignores my irritation":
            bree.say "That must be very nice, Dwayne."
            bree.say "Pity you don't have a something to get you up to the house without walking."
            bree.say "You know, like ski-lift or a little train - something like that?"
            "I'm joking, obviously."
            "Trying to make light of the awkward situation."
            "But Dwayne doesn't seem to pick up on that."
            "Instead he strokes his chin."
            "Clearly considering the idea."
            dwayne.say "Hmm..."
            show dwayne shout
            dwayne.say "That's an interesting suggestion, [hero.name]."
            dwayne.say "Nobody in this neighbourhood has anything like that."
            dwayne.say "I wonder what that kind of thing would actually cost?"
            show dwayne normal
            $ game.active_date.score += 10
        "Give Dwayne a little piece of my mind":
            bree.say "Cut it out, Dwayne!"
            bree.say "You already kept me waiting at the gate for ages."
            show dwayne smile
            "Dwayne shakes his head and smiles."
            "Which with teeth like his is quite a sight."
            show dwayne happy
            dwayne.say "That wasn't deliberate, [hero.name]."
            dwayne.say "This is a big place."
            dwayne.say "So it takes me a while to get to the intercom."
            show dwayne normal
            bree.say "Okay, okay..."
            bree.say "I get it - you have a big house."
            bree.say "You don't have to keep reminding me!"
            $ game.active_date.score -= 10
    "Dwayne makes a sweeping gesture with one arm towards the double front door."
    "One that I take to mean I'm supposed to follow him inside."
    "And also on account of him being too pompous to just come out and say it."
    scene bg mansion with fade
    pause 0.2
    show dwayne at center, zoomAt(1.25, (640, 920)) with easeinright
    "Once we are inside, I feel like I'm walking into another world."
    "The place looks like the homes you see on that TV show."
    "The one where rappers and rockstars show people around their cribs."
    show dwayne shout
    dwayne.say "I can see that you're impressed, [hero.name]."
    show dwayne normal
    bree.say "I'm staggered by the size of the place for sure."
    "Luckily for me, Dwayne seems happy to take that as an affirmative."
    "He chuckles as we stroll from one huge room to the next."
    show dwayne shout
    dwayne.say "It might seem strange to want to celebrate in my own home, [hero.name]."
    dwayne.say "But you see this place is so vast that I seldom visit every room in the space of a month."
    dwayne.say "So showing you at least some of it is almost like a vacation for me!"
    dwayne.say "Don't worry though, I'm only going to show you the highlights."
    dwayne.say "Otherwise we'd be at it all day!"
    show dwayne normal
    "I roll my eyes in despair as I follow Dwayne along."
    "But I make sure that there's no way he can see me doing it."
    "At first, Dwayne shows me rooms that really don't grab my attention."
    "I mean sure, they're big and filled with expensive stuff."
    "But they don't really impress me that much."
    with fade
    "Though that changes when we walk into what looks like the sitting-room."
    "And I see what's hooked up to the obligatory giant TV."
    bree.say "WHOA!"
    bree.say "You...you have them..."
    bree.say "You have them all!"
    bree.say "A Z-Box...a Gamesation...even a Play Square!"
    "Dwayne shrugs and shakes his head."
    show dwayne shout
    dwayne.say "They're really more for my daughter."
    dwayne.say "And I wouldn't want her to miss out on a game she wants."
    dwayne.say "So I make sure she has all the consoles on the market."
    show dwayne normal
    bree.say "Do you play yourself?"
    dwayne.say "Hmm..."
    show dwayne shout
    dwayne.say "I dabble when Cassidy asks me to play and I have time."
    dwayne.say "She tells me I'm pretty good...for an adult!"
    show dwayne normal
    bree.say "You want to play a game with me?"
    show dwayne therock
    "Dwayne looks more than a little surprised at the request."
    show play console dwayne at flip, center, zoomAt(1.25, (640, 900)) with fade
    "But he nods and settles down, picking up a joypad."
    dwayne.say "Why not - let's do it!"
    "I choose a game that I think we'll both enjoy."
    "And pretty soon we're battling it out together."
    dwayne.say "You'd better be ready for this, [hero.name]..."
    dwayne.say "Because I won't go easy on you!"
    bree.say "No worries, Dwayne..."
    bree.say "I've got no problem beating your ass on your birthday!"
    menu:
        "Try hard for the win":
            "I mean what I said."
            "I genuinely do the best I can to win."
            "And I get the feeling that Dwayne is doing the same too."
            "But somehow nothing seems to go right for him."
            "Whereas on the other hand, I'm having all the luck."
            "Whatever I do, it just comes off every time."
            "More then once I think Dwayne's going to make a comeback."
            "And I can almost feel the tides turning in his favour."
            "But on each occasion I just leave him in the dirt."
            hide play console
            show dwayne upset
            with fade
            "By the time the game is over, Dwayne's looking less than pleased."
            bree.say "Erm..."
            bree.say "Bad luck, Dwayne..."
            bree.say "But well played, I guess?"
            dwayne.say "Humph..."
            show dwayne shout
            dwayne.say "How do you know I didn't let you win, [hero.name]?"
            show dwayne normal
            bree.say "Ah...did you let me win?"
            show dwayne happy
            dwayne.say "Ha, ha...that's be telling!"
            show dwayne normal
            $ game.active_date.score -= 10
        "Let Dwayne win":
            "I mean what I said."
            "And I genuinely do the best I can to win."
            "But somehow nothing seems to go right for him."
            "Whereas on the other hand, I'm having all the luck."
            "Whatever I do, it just comes off every time."
            "But I prefer to take it on"
            "Dwayne is not a regular player like me"
            "And today is his day"
            "I try to give him a chance to win without him noticing"
            "I feel like it works"
            "Dwayne smiles every time he knocks me down"
            hide play console
            show dwayne smile
            with fade
            "And when the game is over, I feel like my exercise was more complete to accomplish than any competition that I could do"
            show dwayne happy
            dwayne.say "What did I tell you, [hero.name]?"
            dwayne.say "I'm not pulling my punches."
            dwayne.say "I'm just that good!"
            show dwayne normal
            bree.say "Yeah, yeah..."
            bree.say "I get the picture."
            bree.say "Can we do something else now?"
            $ game.active_date.score += 10
    show dwayne normal with fade
    "Once we've had our fill of videogames, the tour continues."
    "As before, most of the rooms seem to just be huge spaces."
    "And all the expensive stuff crammed in them blends into one."
    "That is until we come to a particularly large room."
    show dwayne shout
    dwayne.say "This is the kitchen."
    dwayne.say "You like?"
    show dwayne normal
    bree.say "Wow..."
    bree.say "You could fit the whole first floor of my house in here!"
    bree.say "What's it like to cook in a place like this?"
    show dwayne shout
    dwayne.say "That's cute, [hero.name]!"
    dwayne.say "But how would I know?"
    dwayne.say "The chef makes all of the meals in the staff kitchen downstairs."
    dwayne.say "In fact, I don't know if anyone's ever cooked a single thing in here!"
    show dwayne normal
    "I stare at Dwayne with a blank expression while that statement sinks in."
    "But no matter what I do, I can't make it sink in all the way."
    "So I just shake my head and try to forget about it."
    menu:
        "Give Dwayne a cake made home":
            bree.say "Anyway..."
            bree.say "Seeing as how we're in the kitchen..."
            "I reach into my bag and pull out a nondescript box."
            bree.say "Surprise!"
            bree.say "I made you a birthday cake."
            show dwayne shout
            dwayne.say "Well, well..."
            dwayne.say "Aren't you full of surprises!"
            show dwayne normal
            "I nod and smile, putting the cake down on the table."
            "Dwayne hands me a knife and I cut him a slice."
            "He accepts it with a smile of his own."
            "Then proceeds to take a large bite."
            if hero.has_skill("cooking"):
                "I watch as Dwayne starts to chew."
                "But I start to get worried a few seconds later."
                "Because that's when his eyes widen."
                bree.say "What's the matter, Dwayne?"
                bree.say "Is there something wrong with the cake?"
                "By way of answer, Dwayne shakes his head."
                "And at the same time he takes a second bite of the cake."
                show dwayne smile
                "When he speaks, it's through a mouthful of the same."
                show dwayne shout
                dwayne.say "Something wrong with it?"
                show dwayne happy
                dwayne.say "[hero.name], this is the best cake I ever had!"
                dwayne.say "You have to let me get the recipe for this."
                dwayne.say "I'm going to have my chef make it for me every damn day!"
                show dwayne normal
                "I'm more than a little overwhelmed by Dwayne's reaction."
                "But I do the best I can to take it modestly."
                "Smiling and blushing a little."
                "While all the time I feel a sense of triumph inside."
                $ game.active_date.score += 10
            else:
                "I watch as Dwayne starts to chew."
                "But I start to get worried a few seconds later."
                "Because that's when his eyes widen."
                "And they start to bulge out of their sockets too!"
                bree.say "What's the matter, Dwayne?"
                bree.say "Is there something wrong with the cake?"
                show dwayne therock
                "By way of answer, Dwayne snatches up a napkin."
                "And then he proceeds to spit the mouthful of cake into it."
                show dwayne shout
                dwayne.say "Urgh..."
                dwayne.say "Argh..."
                dwayne.say "Whoa..."
                dwayne.say "Maybe...maybe a little less salt next time?"
                show dwayne normal
                "I nod, trying to take that as constructive criticism."
                "Then I take the rest of the cake and dump it in the trash."
                $ game.active_date.score -= 10
        "Notice a plate cover and ask for what is under":
            "Dwayne walks over to one of the many islands in the kitchen."
            "And then he whips the cover off of a plate in the middle of it."
            show dwayne happy
            dwayne.say "Ta da!"
            dwayne.say "I had my chef whip this up for the occasion."
            dwayne.say "What do you think?"
            show dwayne normal
            "I look at the cake Dwayne's pointing to."
            "And I have to admit, it's pretty impressive."
            bree.say "That looks amazing."
            "Dwayne nods and smiles, clearly approving of my praise."
            "He grabs a knife and proceeds to cut me a slice."
            "I take it with a smile of my own, biting into the cake."
            "All while Dwayne is cutting himself a slice and doing the same."
            if hero.has_skill("iron_stomach"):
                "I keep on smiling as I chew on the cake."
                "And boy, is it ever chewy!"
                "Sure, it's not the best cake I ever tasted."
                "But I'm sure I've had worse."
                "I look up to see how Dwayne's doing."
                "But what I see comes as a real surprise."
                bree.say "What's the matter, Dwayne?"
                bree.say "Is there something wrong with the cake?"
                "By way of answer, Dwayne snatches up a napkin."
                "And then he proceeds to spit the mouthful of cake into it."
                show dwayne angry
                dwayne.say "Urgh..."
                dwayne.say "Argh..."
                dwayne.say "Whoa..."
                show dwayne normal
                bree.say "Oops!"
                bree.say "I didn't think it was that bad!"
                show dwayne shout
                dwayne.say "Not that bad?!?"
                dwayne.say "[hero.name], it tastes like liquid polymer!"
                dwayne.say "I'm going to be having a serious chat with the chef about this!"
                show dwayne normal
                $ game.active_date.score += 10
            else:
                "I do the best I can to keep on smiling as I chew."
                "But it becomes impossible to keep it up as I actually taste the cake."
                "And that's because the taste is uniquely vile."
                "In fact, it keeps on getting worse the longer it's in my mouth."
                "Pretty soon I can't stand it anymore."
                "So I grab a napkin and spit the contents of my mouth into it."
                "I look up, about to apologise to Dwayne."
                "But then I see that he's coughing into a napkin of his own."
                show dwayne angry
                dwayne.say "Urgh..."
                dwayne.say "Argh..."
                dwayne.say "Whoa..."
                show dwayne normal
                bree.say "Yeah..."
                bree.say "That was pretty gross!"
                show dwayne shout
                dwayne.say "Don't worry, [hero.name]..."
                dwayne.say "I'm going to be having a serious chat with the chef about this!"
                $ game.active_date.score -= 10
    scene bg cinemaroom at flip, zoomAt(1.5, (900, 350))
    show dwayne normal at center, zoomAt(1.25, (640, 920))
    with fade
    "The next room that Dwayne shows me into really does blow me away."
    "And that's because I feel like we just walked into a cinema."
    "Sure it's smaller than the last real cinema I was in."
    "But there are multiple rows of plush, reclining seats."
    "And the screen at the far end of the room isn't an extra large TV."
    "It really is a projector screen covering the entire wall!"
    show dwayne shout
    dwayne.say "You like the movie theatre, [hero.name]?"
    show dwayne normal
    bree.say "Of course I do!"
    bree.say "But what about that massive TV back in the games-room?"
    show dwayne happy
    dwayne.say "The clue's in the name - that's for gaming."
    dwayne.say "When I want to watch a movie, this is how I do it!"
    dwayne.say "You want to try it out?"
    show dwayne normal
    bree.say "You bet I do!"
    "Dwayne nods and scoops up a large remote control."
    "Then he gestures to a couple of the huge chairs."
    show dwayne shout
    dwayne.say "Here we are, [hero.name]..."
    dwayne.say "Best seats in the house!"
    show watch movie dwayne with fade
    "A few seconds later the lights go down."
    "And then the film begins."
    "The picture and the sound are as amazing as I expected them to be."
    "But it doesn't take long for something to distract me."
    "Looking down I can see what it is straight away."
    "Dwayne's hand is on my thigh, and it's creeping ever higher!"
    menu:
        "Let Dwayne touch me up":
            "Don't get me wrong, the movie is good."
            "But it's not good enough to turn something like this down."
            "So I lean back and wait for Dwayne's hand to reach it's destination."
            "And when it starts to inch under my skirt, I have to bite my lip."
            "Then it's sliding into my panties, and I can hardly keep quiet."
            "Dwayne spends the rest of the movie teasing me down there."
            "His huge, powerful fingers exploring every inch of my pussy."
            "The deeper they get, the more I want to cry out at the sensation."
            "But somehow I dig down deep, finding the willpower to stay silent."
            "I'm sure that I must have come more than once."
            "Because by the time the end credits roll, I'm soaked down there."
            "Dwayne doesn't say a word as he slides his hand out from under my skirt."
            "But when the lights come up again, he coughs lightly."
            hide watch movie
            show dwayne shout at center, zoomAt(1.25, (640, 920))
            with fade
            dwayne.say "Ahem..."
            dwayne.say "There's a bathroom through there, [hero.name]."
            dwayne.say "If you want to go freshen up."
            show dwayne normal
            play sound woosh_punch
            hide dwayne with easeoutleft
            "I nod and hurry off in the direction he indicates."
            "My cheeks flushed from the sensations he caused me to feel."
            "And my whole body still tingling from my last orgasm too."
            $ game.active_date.score += 20
        "Slap Dwayne's hand away":
            "Don't get me wrong, I'm no prude."
            "But I really am trying to watch the film."
            "And the last thing I need is Dwayne fiddling around with me."


            "So I reach down and give his hand a good, hard slap."
            hide watch movie
            show dwayne shout at center, zoomAt(1.25, (640, 920))
            dwayne.say "Ouch!"
            dwayne.say "What was that for?!?"
            show dwayne normal
            bree.say "No time for that kind of thing now."
            bree.say "I want to watch this!"
            show dwayne shout
            dwayne.say "Are you kidding me?"
            dwayne.say "Fine, [hero.name]..."
            dwayne.say "Have it your way."
            show dwayne normal
            "Dwayne's hand retreats back into his own seat."
            "Which leaves me free to watch the rest of the movie in peace."
            $ game.active_date.score -= 20
    scene bg mansion
    show dwayne normal at center, zoomAt(1.25, (640, 920))
    with fade
    pause 0.5
    hide dwayne with easeoutleft
    "Dwayne leads me towards the back of the house and then outside."
    scene bg pool at flip, zoomAt(2.75, (1700, 600))
    show dwayne normal at center, zoomAt(1.25, (640, 920))
    with fade
    "After the darkness of the movie-room, I blink at the sudden light."
    "And once my vision has cleared, I see we're standing by an impressive pool."
    show dwayne shout
    dwayne.say "I thought we could chill by the pool a while, [hero.name]."
    dwayne.say "What do you think?"
    show dwayne normal
    bree.say "Sounds good to me."
    "Dwayne nods and walks over to one of the sun-loungers."
    "He lies down and gestures for me to take the one next to his."
    "Once we're both settled in, he gives me a sideways glance."
    show dwayne shout
    dwayne.say "So, [hero.name]..."
    dwayne.say "What did you get me for my birthday?"
    dwayne.say "I'm always interested to see what people get the man who has everything!"
    show dwayne normal
    if not hero.has_gifts:
        "Ah shit!"
        "I knew there was something I was supposed to remember!"
        "Okay, okay...think, [hero.name]..."
        "Maybe there's a way I can wriggle out of this one."
        bree.say "Oh, I didn't get you one, Dwayne."
        bree.say "I figured with all the stuff you have already..."
        bree.say "It'd...it'd just be kind of an insult to add more to it."
        "Dwayne looks at me with an odd expression on his face."
        "But then he shrugs and shakes his head."
        show dwayne shout
        dwayne.say "Okay, [hero.name]."
        dwayne.say "Of all the explanations in the world..."
        dwayne.say "That's definitely one of them."
        show dwayne normal
        $ game.active_date.score -= 20
        $ dwayne.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_27
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I pull out the gift that I brought for Dwayne."
                "And I hand it over to him with a shrug."
                bree.say "I have no idea, Dwayne."
                bree.say "So I just bought you something I thought you might like."
                if _return:
                    play sound [paper_ripping_2, paper_ripping_1]
                    "Dwayne makes short work of the wrapping paper."
                    show dwayne therock
                    "But when he opens the box, he makes an odd sound."
                    "Like he's genuinely surprised by what he sees."
                    bree.say "What's the problem?"
                    bree.say "Have you already got one?"
                    show dwayne happy
                    dwayne.say "No, [hero.name]..."
                    dwayne.say "I really don't!"
                    dwayne.say "And I can't remember the last time this happened."
                    dwayne.say "The last time someone actually gave me something I didn't already have!"
                    show dwayne normal
                    $ game.active_date.score += 20
                else:
                    play sound [paper_ripping_2, paper_ripping_1]
                    "Dwayne makes short work of the wrapping paper."
                    "But when he opens the box, he makes a non-committal sound."
                    bree.say "What's the problem?"
                    bree.say "Have you already got one?"
                    show dwayne upset
                    dwayne.say "Of course I have, [hero.name]."
                    dwayne.say "And thanks to you, I now have one more."
                    dwayne.say "Another one that I'm never going to use."
                    show dwayne normal
                    $ game.active_date.score -= 10
            else:
                "Ah shit!"
                "I knew there was something I was supposed to remember!"
                "Okay, okay...think, [hero.name]..."
                "Maybe there's a way I can wriggle out of this one."
                bree.say "Oh, I didn't get you one, Dwayne."
                bree.say "I figured with all the stuff you have already..."
                bree.say "It'd...it'd just be kind of an insult to add more to it."
                show dwayne upset
                "Dwayne looks at me with an odd expression on his face."
                "But then he shrugs and shakes his head."
                dwayne.say "Okay, [hero.name]."
                dwayne.say "Of all the explanations in the world..."
                dwayne.say "That's definitely one of them."
                show dwayne normal
                $ game.active_date.score -= 20
                $ dwayne.love -= 10
    show dwayne happy
    dwayne.say "You know what we should do now, [hero.name]?"
    show dwayne normal
    "I honestly think that Dwayne's about to suggest that we fuck."
    "But I decide to play along, just for the sake of being nice."
    bree.say "No, Dwayne, I don't."
    bree.say "What are you thinking?"
    show dwayne happy
    dwayne.say "We should go for a swim!"
    show dwayne normal
    "I blink in surprise."
    "Because I genuinely wasn't expecting that."
    "But before I can answer, Dwayne leaps up from his lounger."
    show dwayne swimsuit with fade
    "And he strips off his clothes in the blink of an eye."
    "Seriously, it reminds me of those male strippers with the velcro in their pants!"
    "But I'm quite relieved to see that he had his trunks on underneath."
    "So at least he's not intending on going naked."
    show dwayne happy
    dwayne.say "So what do you say, [hero.name]?"
    dwayne.say "Will you join me?"
    show dwayne smile
    bree.say "Erm..."
    bree.say "I didn't bring a swimming costume."
    show dwayne shout
    dwayne.say "No worries - you're about the same size as Cassidy."
    dwayne.say "And she's got plenty of swimming costumes she's never even worn."
    show dwayne normal
    menu:
        "Agree to go swimming":
            bree.say "Okay, Dwayne..."
            bree.say "That sounds cool."
            "Dwayne's as good as his word."
            with fade
            "And pretty soon I'm decked out in a swimming costume."
            "It's so new that it still has the tags from the store on it."
            "But I do wonder if it really belongs to Dwayne's daughter."
            "Because it's way more revealing that stuff I'd have worn as a teenager."
            "Dwayne nods and walks to the edge of the pool."
            show dwayne at startle
            pause 1
            hide dwayne
            with easeoutbottom
            pause 0.2
            play sound water_splash
            show swimmingrace dwayne swimsuit
            "Then he makes a point of diving straight into the water."
            "I try to make it look like I'm only half watching him."
            "Because I can tell that he's doing his best to show-off."
            "I make a point of lowering myself into the water with less ceremony."
            "And then I devote my attention to actually swimming."
            "Getting the chance to exercise my muscles and relax my body at the same time."
            $ game.active_date.score += 20
        "Refuse to go swimming":
            bree.say "Nah, I'm cool."
            bree.say "But you go right ahead."
            show dwayne shout
            dwayne.say "Are you sure, [hero.name]?"
            dwayne.say "You're just going to sit there and watch?"
            show dwayne normal
            "I nod and lie back on my lounger."
            "Which seems to be enough to convince Dwayne that I'm serious."
            "He shrugs and walks to the edge of the pool."
            show dwayne at startle
            pause 1
            hide dwayne
            with easeoutbottom
            pause 0.2
            play sound water_splash
            show swimmingrace dwayne swimsuit nomc
            "Then he makes a point of diving straight into the water."
            "I try to make it look like I'm only half watching him."
            "Because I can tell that he's doing his best to show-off."
            "But I have to admit that the water does look really tempting."
            "So I bite down on it and do the best I can to ignore that fact."
            "I'm not about to admit that I might have been wrong in front of Dwayne!"
            $ game.active_date.score -= 10
    hide swimmingrace
    show dwayne normal swimsuit at center, zoomAt(1.25, (640, 920))
    with fade
    "Once the fun involving the pool is over, I finally notice the time."
    bree.say "Oh wow..."
    bree.say "I didn't know it was getting so late!"
    bree.say "Should I be thinking about getting home?"
    if game.active_date.score >= 60 and dwayne.sexperience >= 1:
        show dwayne therock
        "Dwayne frowns as he thinks about what I just said."
        dwayne.say "Hmm..."
        show dwayne shout
        dwayne.say "I was hoping you'd stay a little longer."
        dwayne.say "There's still one room I didn't get to show you."
        show dwayne normal
        "I shrug and put on my best interested face."
        bree.say "Really?"
        bree.say "That sounds great."
        show dwayne smile
        bree.say "But I was kind of worried your daughter might be coming home!"
        show dwayne happy
        dwayne.say "Don't worry, [hero.name]..."
        dwayne.say "The house is big enough to go days without seeing anyone else."
        dwayne.say "That's one of the reasons I like living here."
        dwayne.say "Come on, follow me..."
        show dwayne normal
        "I gather up my things and hurry after Dwayne."
        "Eager to see what else he has to show me."
        call dwayne_birthday_sex from _call_dwayne_birthday_sex
    else:
        show dwayne therock
        "Dwayne frowns as he thinks about what I just said."
        dwayne.say "Hmm..."
        show dwayne shout
        dwayne.say "I hate to be a party-pooper, [hero.name]."
        dwayne.say "But you're probably right."
        dwayne.say "Cassidy will be home soon."
        dwayne.say "And it's easier for everyone if she doesn't run into my lady-friends!"
        show dwayne normal
        "I nod and begin to gather my things."
        bree.say "Well..."
        bree.say "I had a good time, Dwayne."
        show dwayne happy
        dwayne.say "I'm glad to hear that, [hero.name]."
        dwayne.say "Now let's see about calling you a cab..."
        show dwayne normal
    return

label dwayne_birthday_sex:
    scene bg mansion with fade
    pause 0.3
    show dwayne normal at center, zoomAt(1.25, (640, 920)) with easeinright
    "I'm pretty intrigued to see this last room that Dwayne wants to show me."
    "And my excitement only increases as he walks up the sweeping staircase to the first floor."
    "Most of the doors up here seem to be closed, but a scarce few are open or ajar."
    "And glancing into the rooms beyond I see glimpses of opulent beds and bathrooms."
    "Finally we reach the end of a long corridor, stopping in front of a pair of double doors."
    "Dwayne pauses for a moment, before flinging them open in a typically dramatic gesture."
    show dwayne happy
    dwayne.say "This is where the magic happens!"
    dwayne.say "So, [hero.name]..."
    dwayne.say "What do you think?"
    show dwayne normal
    "It's hard to answer the question at first."
    "And that's because I'm still trying to take in the sight of the room ahead."
    "It's a huge space, but then of course it is - what else should I have expected?"
    "And the bed that dominates it is in keeping with those same proportions too."
    "Seriously, I'm not one hundred percent sure..."
    "But I think it's bigger than my bedroom back home!"
    "At least the mattress seems to cover more square feet than my floor does."
    bree.say "Wow, Dwayne..."
    bree.say "Is this the marital bedroom?"
    bree.say "Like, you share it with Cherie?"
    "It feels odd talking about Dwayne's wife like this."
    "But from the way he behaves, I get the impression it's a marriage of convenience."
    "Or at least it's become that way over time."
    show dwayne shout at center, traveling(1.5, 10.0, (640, 1080))
    dwayne.say "Oh no, [hero.name]..."
    dwayne.say "Cherie's bedroom is on the other side of the house."
    dwayne.say "Out of sight and out of mind, you know what I mean?"
    dwayne.say "What you're looking at right now is my bedroom."
    show dwayne normal
    bree.say "So you're saying this place is totally private?"
    show dwayne shout
    dwayne.say "It is."
    show dwayne normal
    bree.say "That nobody else is going to come in here?"
    show dwayne shout
    dwayne.say "They won't."
    show dwayne normal
    bree.say "And we can do whatever the hell we want?"
    show dwayne shout
    dwayne.say "We can."
    show dwayne normal
    "Dwayne's been walking towards me the whole time we've been talking."
    "Taking a step at a time so that he draws closer, little by little."
    "So when we're done talking, he's looming over me."
    "And that impressive chest is going up and down in time with his breathing."
    "Damn it - I know that I'm supposed to be an empowered, modern woman."
    "But right now, all I know is that I'm going weak at the knees."
    "And that I want to rest my head on those amazing pectoral muscles!"
    "So when Dwayne reaches out and scoops me up in his arms, I don't resist for a second."
    "Instead I find my head filled with images from all those silly old romantic movies."
    "The ones where the silly, helpless girl is swept off her feet by the male lead."
    "Hell, Dwayne even lays me down on the bed, just like what happens in the films too!"
    "But I think the effect is a little spoiled by the way I can't stop giggling."
    "That and my less than graceful efforts to pull down my panties once he lets me go!"
    "Because now all that I have on my mind is what Dwayne's about to do to me."
    "All the different possibilities and how each of them might feel."
    "Dwayne doesn't seem in the least bit put off my antics however."
    show dwayne naked with dissolve
    "Now that his shirt is off, he unbuckles his belt and pulls down his pants."
    "He's not wasting any time either, as he pulls his shorts down at the same time."
    "And that means I get a good view of his manhood as he does so."
    "There it is, as big and impressive as I remember it."
    "I can't help squeezing my legs together in anticipation."
    "Thinking of how it's going to feel to have that thing inside of me!"
    scene dwayne missionary zorder 2
    show bg black zorder 1
    show dwayne missionary dwayne_bedroom zorder 2
    with fade
    "I've managed to pull my clothes off by now, so that I'm naked on the bed."
    "And I can see that Dwayne's checking me out, nodding at what he sees."
    "It's not just his expression that gives it away either."
    "As he climbs onto the bed, I take the chance to glance down."
    "And I see his cock starting to stir, growing and rising slowly upwards!"
    "Neither of us seems to need to say a word."
    "We both know where this is going and what's about to happen."
    "All I have to do now is lie back and wait."
    "Wait as Dwayne lowers himself down and onto me."
    "Well, I almost lie back and let it happen."
    "But at the last minute I get the urge to touch it."
    "My hands reach down and take hold of Dwayne's cock."
    "I don't know if my intention was to guide him home."
    "Or else merely to caress it as he took care of that himself."
    "And in reality I end up doing a little of both."
    "Dwayne nods in approval as I steer the head between my thighs."
    "Then I push it hard against the lips of my pussy."
    "They're still resisting, refusing to open."
    "In spite of that, they're getting slicker by the second."
    "Which means I know that they can't deny us what we want for much longer."
    "A moment later, Dwayne adds a push of his own into the mix."
    "And that seems to be what was needed to get things moving."
    "My muscles relax a little."
    "Not a great deal, but enough for him to begin to sink into me."
    "And once he has that proverbial foot in the door, Dwayne's got all he needs."
    "For the first time I feel him push seriously hard."
    "And the effect is instant, changing the whole complexion of what I'm feeling."
    show dwayne missionary vaginal up
    "Dwayne doesn't make it all the way inside of me on the first push."
    "But the sensation is still enough to almost overwhelm me."
    "Even before I can come to terms with it, I feel him push a second time."
    "Now he really does make it as deep into me as he can go."
    show dwayne missionary blush
    "And I can feel myself beginning to writhe on the bed beneath him."
    show dwayne missionary vaginal down hurt
    "Not only is he filling me up down there, I feel like he's pinning me down."
    "That any moment he might go all the way through me and into the mattress below!"
    "I don't know if I could move off this spot, even if I wanted to try."
    show dwayne missionary inout open
    "Again, Dwayne doesn't wait for me to be able to process all of this."
    show dwayne missionary poke hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke open
    "Because he then starts to thrust in and out of me."
    "All of that weight is behind the movements too."
    "And I can tell you that it's almost all solid muscle."
    show dwayne missionary poke hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke open
    "Dwayne is working away like a machine atop me."
    show dwayne missionary poke hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke open
    "It only takes him a couple of seconds to get up to speed."
    show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed up
    "And from what I can feel, he has stamina to match the power."
    show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed up
    "Pretty soon Dwayne's managed to reduce me to a helpless state."
    show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed up
    "I feel like a quivering mess laid there on the bed."
    show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed up
    "But for all of that, he's not nearly done with me."
    "I want to reach up as he makes love to me."
    show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed up
    "To touch the rock-hard muscles of his body."
    "And caress the sturdy shape of his limbs."
    show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed
    "Yet there's no strength in my own limbs and muscles."
    "It's like Dwayne's cock isn't just pinning me down in a metaphorical sense."
    show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.2
    show dwayne missionary -poke -speed
    "I could swear that he's actually putting me in a state of pleasurable paralysis."
    "That he's plugged directly into my nervous system, and he's overloading it."
    show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "Dwayne's going at me in the same way I imagine he attacks his work-out at the gym."
    "And I think that I'm getting the benefit of the same exercise myself too."
    show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "I wish that I could go on soaking this up forever."
    "That I could never get my fill of what Dwayne's giving me."
    show dwayne missionary poke up speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "But I'm only human, and so I can only take so much."
    "I can feel my body being pushed towards a climax."
    show dwayne missionary poke up speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "And I know that my orgasm is mere seconds away."
    "Yet there's no way I can tell Dwayne, no way I can plead for mercy."
    show dwayne missionary poke up speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "I can't form a single syllable with my lips, never mind actually speaking words."
    "And my limbs still steadfastly refuse to move, save for jerking in passive passion."
    show dwayne missionary poke up speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "That means that when it finally happens, I'm helpless to resist."
    show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "I cum with a sensation that crashes over me like a wave."
    "Those previously uncooperative muscles begin to twitch and twinge."
    show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "Not least the those in my pussy, that squeeze Dwayne harder than ever."
    "I had no conscious intention of making it happen."
    show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
    pause 0.1
    show dwayne missionary -poke -speed
    "But the pressure has much the same effect on Dwayne."
    "And a moment later, I feel him stiffen."
    show dwayne missionary cum with hpunch
    "Then he shoots his load, deep inside of me and without warning."
    with hpunch
    "If I was helpless before, I'm left delirious now."
    with hpunch
    "I genuinely don't know where I am or what's happening."
    "Only that Dwayne just exploded inside of me."
    "My sensations are like white noise, impossible to describe."
    "And they only become comprehensible to me as they finally begin to fade."
    "I think that I can make out Dwayne as he pulls out of me."
    "Then he reclines next to me on the bed, likely checking out his handiwork."
    "But all I can do is lay there, waiting for sensations to return to normal."
    "Which takes longer than I can ever remember in the past."
    "And yet even afterwards, I can still feel the lingering effects."
    "Like an echo, still faintly audible on the very edge of earshot."
    $ dwayne.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
