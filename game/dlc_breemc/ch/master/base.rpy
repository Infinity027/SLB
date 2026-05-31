init python:
    Event(**{
    "name": "master_auto_greet",
    "label": "auto_greet",
    "girl": "master",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "master_give_phone_number",
    "label": "give_phone_number",
    "girl": "master",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            Not(ContactKnown()),
            Not(IsActivity("sleep")),
            MinStat("love", 40),
            ),
        ],
    "chances": 25,
    "do_once": True,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "master_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(master,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "master",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "master_are_you_sick",
    "label": "are_you_sick",
    "girl": "master",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (master, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "master_auto_chat",
    "label": "auto_chat",
    "girl": "master",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "master_ask_out",
    "label": "ask_out",
    "girl": "master",
    "priority": 100,
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "master_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "master",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label master_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = master.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = master.get_activity(bye_hour)
    if not activity == master.activity:
        if day != game.week_day:
            $ master.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ master.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"master {bye_outfit}")
        if activity["activity"] == "sleep":
            master.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            master.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            master.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            master.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            master.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            master.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            master.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            master.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            master.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            master.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            master.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            master.say "I'll go get dressed."
        hide master
    return

label master_cheated(action, cheat_npc=None):
    show master
    if not master.sub >= 75:
        show master sad
        show fx anger
        $ loss = 5
        if master.flags.boyfriend or master.flags.fiance:
            $ loss += 5
        $ master.love -= loss
        "I see Master looking at me [action] someone else with a painful hurting face..."
    else:
        show master perv
        show fx heart
        $ master.sub += 1
        "I see Master looking at me [action] someone else with envy and lust in his eyes."
    hide master
    return

label master_beats_ryan_female:
label master_beats_scottie_female:
label master_beats_jack_female:
label master_beats_shawn_female:
label master_beats_mike_female:
label master_beats_danny_female:
label master_beats_dwayne_female:
label master_beats_victor_female:
    if randint(1, 100) <= 20:
        return "abort"
    if active_girl.id == "ryan":
        "I can feel Ryan's lips against mine, his hands all over me."
    elif active_girl.id == "jack":
        "Jack's kissing me with a passion, squeezing me tight."
    elif active_girl.id == "shawn":
        "Shawn has me in his arms, kissing me like crazy."
    elif active_girl.id == "mike":
        "[mike.name] pulls me closer, kissing me more intensely all the time."
    elif active_girl.id == "danny":
        "Danny grabs me and pulls me in for a rough, but passionate kiss."
    elif active_girl.id == "dwayne":
        "Dwayne holds me tight and places a confident kiss on my lips."
    elif active_girl.id == "victor":
        "Victor kisses me like a troubled, brooding hitman, and it's so intoxicating!"
    "I know that I should be stopping him, but it's so hard to resist!"
    master.say "Hello, hello..."
    master.say "My dear..."
    master.say "Whatever is happening here?"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show master casual angry at right5
    $ renpy.show(f"{active_girl.id} casual angry", at_list=[left5])
    if active_girl.id == "ryan":
        "At the sound of The Master's voice, Ryan releases me from his grip."
    elif active_girl.id == "danny":
        "At the sound of The Masters's voice, Danny turns around to glare at him."
    elif active_girl.id == "dwayne":
        "At the sound of The Masters's voice, Dwayne turns around and raises a single eyebrow."
    elif active_girl.id == "victor":
        "At the sound of The Masters's voice, Victor turns around and raises a quizzical eyebrow."
    else:
        "At the sound of The Master's voice, [active_girl.name] leaps away from me."
    bree.say "Master, I..."
    bree.say "I can explain..."
    bree.say "This isn't what it looks like!"
    "The Master waves a hand in the air, dismissing my words."
    master.say "No need to explain, my dear..."
    master.say "Any man would be ensnared by your wondrous charms!"
    show master noglasses
    master.say "This is a matter of honour..."
    if active_girl.id == "ryan":
        master.say "Between me and this clod!"
    elif active_girl.id == "jack":
        master.say "Between me and this corpulent clod!"
    elif active_girl.id == "shawn":
        master.say "Between me and this dull jumped-up salesman!"
    elif active_girl.id == "mike":
        master.say "Between me and this dull failure!"
    elif active_girl.id == "danny":
        master.say "Between me and this thug!"
    elif active_girl.id == "dwayne":
        master.say "Between me and this bald-headed buffoon!"
    elif active_girl.id == "victor":
        master.say "Between me and this wannabe hitman!"
    "I can't help gasping in surprise at the Master."
    "He looks steely, determined and downright manly right now!"
    "Call me shallow, but he's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "Erm...how old is this guy?"
        ryan.say "I mean, he really looks ancient!"
    elif active_girl.id == "jack":
        jack.say "Whoa...I'm being insulted by an old geezer!"
        jack.say "This is so weird!"
    elif active_girl.id == "shawn":
        shawn.say "Hey, I'm cool with old people!"
        shawn.say "I sell them TVs all the time!"
    elif active_girl.id == "mike":
        mike.say "Whoa..."
        mike.say "This guy must be like a hundred years old!"
    elif active_girl.id == "danny":
        danny.say "Are you fucking kidding me?!?"
        danny.say "You know I'm not afraid to beat up an old geezer!"
    elif active_girl.id == "dwayne":
        dwayne.say "Are you kidding me?"
        dwayne.say "Your head's as smooth as mine, old man!"
    elif active_girl.id == "victor":
        victor.say "Wow...this is pretty crazy!"
        victor.say "An old man wants to fight me?"
    "But it doesn't look like the Master's in the mood to listen."
    "Instead he squares up to his opponent, fists raised."
    show master at mostright4
    with ease

    master.say "{cps=20}Kaaaa -{/cps}{w=0.85}{nw}"
    master.say "{cps=20}meeee -{/cps}{w=0.85}{nw}"
    master.say "{cps=20}haaaa -{/cps}{w=0.85}{nw}"
    master.say "{cps=20}doooo -{/cps}{w=0.85}{nw}"
    play sound punch_hard
    pause 0.2
    $ renpy.hide(f"{active_girl.id}")
    hide master
    $ renpy.show(f"master beats {active_girl.id}")
    master.say "{cps=30}KEEEEEEEEEEEEEEEEEENNN!!!{/cps}" with hpunch
    "The fireball hits [active_girl.name] square in the chest, and he crashes to the ground."
    "Then he steps over his defeated opponent and towards me."
    master.say "Come, my dear..."
    master.say "Let's leave this coward to wallow in defeat."
    return

label master_greet:
    if renpy.has_label(f"master_greet_dialogues_{hero.gender}") and not master.flags.greeted:
        scene expression f"bg {game.room}"
        $ master.flags.greeted = TemporaryFlag(True, 1)
        show master
        $ result = randint(1, 3)
        if result == 1:
            master.say "Hello, [hero.name]."
        elif result == 2:
            master.say "Hi, [hero.name]."
        elif result == 3:
            master.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                master.say "Good morning [hero.name]."
            elif game.hour < 19:
                master.say "Good afternoon [hero.name]."
            else:
                master.say "Good evening [hero.name]."
        call expression f"master_greet_dialogues_{hero.gender}" from _call_expression_460
        hide master
    return

label master_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Master."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Master."
        elif game.hour < 12:
            bree.say "Good morning Master."
        elif game.hour < 19:
            bree.say "Good afternoon Master."
        else:
            bree.say "Good evening Master."
    return

label master_kiss_female:
    scene expression f"bg {game.room}"
    if master.love < 25 and not master.is_boyfriend and not game.active_date.score >= 75:
        show master
        "I don't know why I get the urge to do it."
        "But once it's in my head, I can't get it out."
        "Part of me wants to lean forwards and kiss the master."
        "Like, maybe if I do it when he's at his most zen."
        "When he's meditating and looks like a real martial artist."
        "Maybe then it'll cure him of his creepy ways?"
        "But almost the same moment that I try it, the master pulls back."
        "He doesn't say a word or even shake his head."
        "But the message is clear all the same."
        "And I can feel my cheeks flushing red."
        "Looks like I misjudged that one pretty badly!"
        $ master.love -= 1
        hide master
    elif not master.flags.kiss:
        show master
        "This is going to sound so weird, maybe even a little gross - but hear me out!"
        "Ever since I've been training with the master, and more so since we started hanging out socially..."
        "I...I've kinda found myself starting to feel an attraction to him."
        "I know, I know - he's an old guy, and he can be really creepy sometimes."
        "But there's also a serenity about him that you don't see at first."
        "Maybe it's because I'm learning martial arts from him."
        "Or because I'm actually getting to know him for who he really is."
        "Either way, I keep feeling like I want to kiss the guy!"
        hide master
        show master kiss
        with fade
        "I wait for a time when he's not being creepy, when he's at his most zen."
        "And then I lean in and put my lips against his."
        "For all of his lascivious talk, he seems surprised."
        "And he actually kisses me gently, making it a sensual experience!"
        hide master kiss with fade
        $ master.flags.kiss += 1
        $ master.love += 5
    else:
        hide master
        show master kiss
        with fade
        "Oh god...I think I'm turning into a female version of the master!"
        "Every time he looks at me and smiles, I feel a surge of desire well up in me."
        "I used to think that he was crazy, that he had sex on the brain."
        "But now I can see that he was just on a higher plane of sexuality."
        "And that's the place I want to be taken to as well!"
        "I never seem to be able to turn down the offer of a kiss from him."
        "And every one makes me feel like I'm meditating on a cloud!"
        "What's happening to me?"
        "Even that grin pulls and the wink..."
        "They just make me giggle and bite my lip at the thought of him!"
        hide master kiss with fade
        $ master.flags.kiss += 1
        $ master.love += 5
    return




label master_ask_date_female:



    call master_ask_date_alone_female from _call_master_ask_date_alone_female
    return _return

label master_ask_date_alone_female:
    bree.say "Master..."
    if not master.flags.hadadate:
        bree.say "Do you ever think about us doing something else together?"
        "At this, the old man's eyes light up and he nods eagerly."
        master.say "Oh yes, my dear!"
        master.say "There's one thing in particular I imagine us doing."
        master.say "I think about it all the time!"
        bree.say "Erm...okay..."
        bree.say "I was more thinking about us going out together?"
        bree.say "Like on a date?"
    else:
        bree.say "Are you okay to go out on a date with me?"
    if master.love < 50 or master.flags.nodate:
        if not master.flags.hadadate:
            master.say "Hmm..."
            master.say "I don't think that would be a good idea, my dear."
            master.say "We need to keep our relationship pure in that sense."
            master.say "It's on the physical plane that we need to become closer."
            master.say "Social ties will only get in the way of achieving that union."
        else:
            master.say "Sorry my dear, I cannot fulfill your desires right now."
        $ date_choice = False
    else:
        master.say "Oh..."
        master.say "Oh, I see!"
        master.say "Yes, my dear - that's an excellent idea!"
        master.say "It would bring us more into alignment with one another."
        master.say "And who knows where else it might lead..."
        $ master.flags.hadadate = True
        $ date_choice = True
    return date_choice

label master_pregnancy_congratulations:
    master.say "What's this, my dear..."
    master.say "I sense the presence of a second energy here!"
    master.say "And it's coming from inside of you!"
    "I nod and smile, trying to look like I'm indulging him."
    "Because it's pretty easy to spot the fact that I'm pregnant right now!"
    bree.say "You're right, Master."
    bree.say "I'm going to have a baby!"
    show master happy
    "The old man nods happily at this."
    master.say "Of course, of course..."
    master.say "You're practically overflowing with the power of new life!"
    master.say "Congratulations to you, my dear."
    master.say "And to the father of your child too."
    master.say "Because there's a man who's efforts I truly envy!"
    bree.say "Erm..."
    bree.say "Thank you."
    bree.say "I think..."
    $ master.love += 1
    return

label master_propose_female:
    show master
    "I've been building up my confidence for today, preparing myself for the right moment."
    "All because I just know that I have to get everything right if I want to pull it off."
    "I mean, I know that asking someone to marry you is always kind of a stressful thing."
    "But in this case there's the added complication of the guy I'm asking being a little different."
    "For one thing, the Master is a lot older than me, definitely a mature kind of guy."
    "Though that's not the main thing making me nervous."
    "It's more the fact that we started out as pupil and teacher."
    "I know that we soon became closer than that."
    "Hell, we ended up as a couple!"
    "But somehow asking him to marry me seems far more of a leap than that."
    "Part of me is worried that he'll just turn around and say that he's forbidden to get married."
    "That his sacred vows to pursue the martial arts prevents him settling down with a partner."
    "But maybe that's just me getting him confused with the magic monk guys from that sci-fi franchise?"
    "Whatever the case, I have to keep telling myself this is the right thing to do."
    "That if I chicken out now, I'm going to regret it for the rest of my life."
    "Better to ask and be told no than not to ask and never know, right?"
    show master noglasses at center, zoomAt(1.5, (640, 1040)) with fade
    "So as soon as the chance presents itself, I go for it."
    bree.say "Master..."
    master.say "Yes, my dear?"
    bree.say "There was something I wanted to ask you..."
    show master surprised noglasses
    "The Master's expression suddenly changes."
    "He shakes his head and looks at me with serious eyes."
    show master upset noglasses
    master.say "Did someone from the police department contact you?"
    master.say "If they did, it's very important that you don't believe them."
    master.say "You see the elastic in my shorts was defective..."
    master.say "And I genuinely had forgotten to put on underwear!"
    bree.say "Erm..."
    bree.say "No..."
    bree.say "That's not what I meant!"
    show master surprised noglasses
    master.say "Oh..."
    show master happy noglasses
    master.say "Well forget everything I just said then!"
    master.say "Just erase it from your memory!"
    show master normal noglasses
    "I nod slowly, making sure to file all of this away for future reference."
    bree.say "Anyway..."
    bree.say "What I really wanted to ask you was..."
    bree.say "Would you marry me?"
    show master surprised noglasses
    "The question seems to hit the Master like an unexpected attack."
    "He reels from the impact of my words as if punched in the jaw!"
    if master.love < 195:

        "But the moment that he recovers his balance, the Master shakes his head."
        "And when I see that, I can already feel my spirits plummeting."
        master.say "Marry you?"
        show master sad noglasses
        master.say "But, my dear..."
        master.say "You can't be serious?"
        bree.say "I kind of was!"
        bree.say "Is it really that crazy?"
        bree.say "The idea of us getting married?"
        "The Master is still shaking his head."
        "And now he's started waving his arms in the air too."
        "Which can't be a good sign."
        show master normal noglasses
        master.say "Don't you understand..."
        master.say "I am already wed?"
        master.say "Married to the martial arts around which I have based my entire life?"
        "Ah shit..."
        "Looks like I'm getting told no."
        "And it's because of the martial arts mumbo-jumbo too."
        "But there's no consolation in my having called it."
        bree.say "Are you sure you really mean that?"
        bree.say "You kind of spend all your time hanging around at the beach."
        bree.say "Just watching people from the grass on the dunes."
        bree.say "I really don't see you getting a better offer anytime soon!"
        show master normal -noglasses with dissolve
        "The Master doesn't seem to hear what I'm saying."
        "Or else he just chooses to ignore it."
        "Either way the result is the same."
        $ master.love -= 25
    else:

        "But the moment that he recovers his balance, the Master nods his head."
        "And when I see that, I can already feel my spirits soaring."
        master.say "Marry you?"
        master.say "Oh my..."
        show master happy noglasses
        master.say "What a good idea!"
        master.say "Why didn't I think of that myself?"
        bree.say "So is that..."
        bree.say "Is that a yes?"
        "The master is still nodding his head."
        "And he's waving his arms in the air too."
        "Which I choose to take as a good sign."
        master.say "Yes!"
        master.say "Of course it is..."
        master.say "Yes to both those questions!"
        bree.say "Phew..."
        bree.say "That's a relief!"
        show master normal noglasses
        bree.say "I thought you were going to tell me you were married to martial arts!"
        "The Master looks at me like I'm not making any sense."
        master.say "Of course not!"
        master.say "I only come out with stuff like that when I want to get out of something."
        show master happy noglasses
        master.say "And this definitely isn't one of those things!"
        show master normal noglasses
        "I'm still nodding and smiling the whole time he's saying all of this."
        "But I make sure to file that little revelation away in the back of my mind."
        "Though for now I have other things to occupy my thoughts."
        "Lots of planning to be done and decisions to be made."
        "Because I'm getting married!"
        $ master.set_fiance()
    hide master
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
