init python:
    Event(**{
    "name": "mike_give_phone_number",
    "label": "give_phone_number",
    "girl": "mike",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(mike,
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
    "name": "mike_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            IsGender("female"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(mike,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "mike",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "mike_auto_greet",
    "label": "auto_greet",
    "girl": "mike",
    "priority": 100,
    "conditions": [
        HeroTarget(IsActivity("None")),
        PersonTarget(mike,
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
    "name": "mike_auto_chat",
    "label": "auto_chat",
    "girl": "mike",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(mike,
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
    "name": "mike_are_you_sick",
    "label": "are_you_sick",
    "girl": "mike",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(mike,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (mike, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "mike_ask_out",
    "label": "ask_out",
    "girl": "mike",
    "priority": 100,
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(mike,
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
    "name": "mike_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "mike",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(mike,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Activity(**{
    "name": "play_in_the_pool_with_mike_female",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with [mike.name]",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("female")),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(mike,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        PersonTarget(sasha,
            Not(IsPresent())
            ),
        ],
    "once_day": True,
    "label": "mike_play_pool_female",
    })

    Event(**{
    "name": "mike_livingroom_masturbation",
    "priority": 500,
    "label": "mike_livingroom_masturbation",
    "max_girls": 1,
    "fun": 2,
    "conditions": [
        IsHour(20, 3),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom")),
        PersonTarget(mike,
            Not(IsHidden()),
            IsRoom("livingroom"),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_week": True,
    })

label mike_tv_reaction:
    mike.say "Why not."
    return

label mike_porn_bad_reaction:
    mike.say "Sorry, I don't want to watch this sort of thing."
    return

label mike_play_pool_female:
    show playing water pool mike
    "I splash some water towards [mike.name]."
    mike.say "You have no idea what you've just started! Take that!"
    "After that he retaliates and we play in the water for a while..."
    mike.say "That was fun!"
    bree.say "It sure was."
    $ mike.love += 1
    $ mike.flags.greeted = TemporaryFlag(True, 1)
    return

label mike_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = mike.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = mike.get_activity(bye_hour)
    if not activity == mike.activity:
        if day != game.week_day:
            $ mike.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ mike.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"mike {bye_outfit}")
        if activity["activity"] == "sleep":
            mike.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            mike.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            mike.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            mike.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            mike.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            mike.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            mike.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            mike.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            mike.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            mike.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            mike.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            mike.say "I'll go get dressed."
        hide mike
    return

label mike_cheated(action, cheat_npc=None):
    show mike
    if Harem.together(mike, active_girl):
        show mike perv
        mike.say "Hey, That's unfair!"
        mike.say "I'd like to have some fun too!"
        show mike kiss
        $ mike.flags.kiss += 1
        "And without warning [mike.name] kisses me."
        $ mike.love += 1
    else:
        show mike sad
        $ loss = 5
        if mike.flags.boyfriend or mike.flags.fiance:
            $ loss += 5
        $ mike.love -= loss
        "I see [mike.name] looking at me [action] someone else sadly, tears welling up in his eyes..."
    hide mike
    return

label mike_beats_ryan_female:
label mike_beats_scottie_female:
label mike_beats_jack_female:
label mike_beats_shawn_female:
    if randint(1, 100) <= 50:
        return "abort"
    if active_girl.id == "ryan":
        "I can feel Ryan's lips against mine, his hands all over me."
    elif active_girl.id == "jack":
        "Jack's kissing me with a passion, squeezing me tight."
    elif active_girl.id == "shawn":
        "Shawn has me in his arms, kissing me like crazy."
    "I know that I should be stopping him, but it's so hard to resist!"
    mike.say "[hero.name]!"
    mike.say "What's going on here?!?"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show mike angry at right5
    $ renpy.show(f"{active_girl.id} angry", at_list=[left5])
    if active_girl.id == "ryan":
        "At the sound of [mike.name]'s voice, Ryan releases me from his grip."
    else:
        "At the sound of [mike.name]'s voice, [active_girl.name] leaps away from me."
    "I gasp and look around to see him standing there, visibly seething."
    bree.say "[mike.name], I..."
    bree.say "I can explain..."
    bree.say "This isn't what it looks like!"
    "[mike.name] shakes, cutting me off."
    mike.say "I believe you, [hero.name]."
    mike.say "But that's not going to stop me kicking someone's ass!"
    if active_girl.id == "ryan":
        mike.say "This is between me and Mister Slimy!"
    elif active_girl.id == "jack":
        mike.say "This is between me and fatty!"
    "I can't help gasping in surprise at [mike.name]."
    "He looks steely, determined and downright manly right now!"
    "Call me shallow, but he's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "What are you going to do about it, [mike.name]?"
        ryan.say "You already lost one girl to me - what's one more?"
    elif active_girl.id == "jack":
        jack.say "Hey, that's not nice!"
        jack.say "I've been working out - so if I put on weight, it's muscle-mass!"
    elif active_girl.id == "shawn":
        shawn.say "Hey, man, we can talk this out!"
        shawn.say "How about I give you a discount next time you're in the store?"
    "Before another word can be spoken, [mike.name] barrels into him."
    "With that, the fight is on!"
    "And I really do mean that it's a fight."
    "[active_girl.name] seems to be flailing and slapping for all he's worth."
    "But [mike.name]'s not pulling any punches - literally!"
    play sound punch_hard
    pause 0.2
    $ renpy.hide(f"{active_girl.id}")
    hide mike
    $ renpy.show(f"mike beats {active_girl.id}")
    with hpunch
    "And all it takes is a good hard one to the jaw for it to be over."
    "[active_girl.name]'s eyes roll back into his head, and he collapses into a heap."
    "[mike.name] stands over him, rubbing his bruised knuckles."
    mike.say "Let that be a lesson to you."
    mike.say "Nobody kisses those lips but me!"
    return

label mike_greet:
    if renpy.has_label(f"mike_greet_dialogues_{hero.gender}") and not mike.flags.greeted:
        scene expression f"bg {game.room}"
        $ mike.flags.greeted = TemporaryFlag(True, 1)
        show mike
        $ result = randint(1, 3)
        if result == 1:
            mike.say "Hello, [hero.name]."
        elif result == 2:
            mike.say "Hi, [hero.name]."
        elif result == 3:
            mike.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                mike.say "Good morning [hero.name]."
            elif game.hour < 19:
                mike.say "Good afternoon [hero.name]."
            else:
                mike.say "Good evening [hero.name]."
        call expression f"mike_greet_dialogues_{hero.gender}" from _call_expression_461
        hide mike
    return

label mike_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, [mike.name]."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello [mike.name]."
        elif game.hour < 12:
            bree.say "Good morning [mike.name]."
        elif game.hour < 19:
            bree.say "Good afternoon [mike.name]."
        else:
            bree.say "Good evening [mike.name]."
    return

label mike_kiss_female:
    scene expression f"bg {game.room}"
    if mike.love + hero.charm < 80 and not mike.is_girlfriend and not game.active_date.score >= 75:
        show mike
        "[mike.name] quickly takes a step back, and turns away."
        if mike.love < 40:
            $ mike.sub -= 1
        else:
            $ result = randint(1, 2)
            if result == 1:
                $ mike.love -= 1
        hide mike
    elif mike.love + hero.charm < 60 or game.active_date.score >= 75:
        hide mike
        show mike kiss
        if not mike.flags.kiss:
            "I watch [mike.name]'s eyes open wide in surprise, and for a moment I think he might back away."
            "Then our lips touches, for the longest time."
            hide mike kiss
        else:
            "I take a step closer to [mike.name], and rest my hands lightly on his shoulder."
            "For a brief moment he looks curious, but I catch sight of a moment of recognition in his eyes before my own drift shut."
            "After the kiss, I catch a glimpse of a small smile playing on his lips before he tries to hide it."
            hide mike kiss
        $ mike.flags.kiss += 1
        $ mike.love += 1
    else:
        hide mike
        show mike kiss
        if not mike.flags.kiss:
            "I feel my lips passing over [mike.name]'s as we embrace, my hands resting comfortably on his shoulders while his own had ventured to my hips."
            "He pushes into my embrace more than he has in the past, but also begin lightly tickling me with his tongue."
            "For a moment, I'm not sure if I'll reciprocate, but I part my lips and allow him access."
            "He let himself inside me, exploring every crevice of my mouth in earnest."
            "I feel rather tense at first, but let out a soft whimper of pleasure."
            hide mike kiss
        else:
            "Once again [mike.name] steps in closer to me, close enough that our bodies are very nearly touching."
            "He brings one hand to my chin, tilting me up to face him as he leans down to let our lips meet."
            "His tongue yet again pushes through the barrier that my lips form to begin exploring my mouth."
            "Before long, we pulled away from one another, breathless."
            hide mike kiss
        hide mike
        $ mike.flags.kiss += 1
        $ mike.love += 2
    return

label mike_ask_date_female:



    call mike_ask_date_alone_female from _call_mike_ask_date_alone_female
    return _return

label mike_ask_date_alone_female:
    if not mike.flags.hadadate:
        bree.say "We get on pretty well, right?"
        bree.say "I mean, we hang out in the house, play video-games and all that."
        bree.say "And we always have a good time when we go to the pub together."
        mike.say "I guess so, [hero.name]..."
        mike.say "Not sure why you're bringing it up now though!"
        bree.say "Well..."
        bree.say "I was wondering..."
        bree.say "Would you like to go out with just me?"
        bree.say "Like at a specific time and to a specific place?"
        mike.say "You mean...like...like a date?"
        bree.say "Well we don't have to call it that if calling it that's a problem."
        bree.say "Is calling it that a problem?"
        bree.say "But yeah, basically it would be a date!"
        bree.say "So what do you think?"
    else:
        bree.say "Hey [mike.name], wanna date?"
        bree.say "Just you and me... You know it's your destiny?"
    if mike.love < 50 or mike.flags.nodate:
        if not mike.flags.hadadate:
            mike.say "No way, [hero.name]!"
            mike.say "We're getting on really well right now."
            mike.say "But if we make it official, I just know it'll go wrong."
            mike.say "So let's leave things as they are, okay?"
        else:
            mike.say "Sorry [hero.name], maybe another time."
        $ date_choice = False
    else:
        mike.say "I think that's a great idea, [hero.name]!"
        mike.say "And I don't know why you didn't just ask me straight up."
        mike.say "I'd love to go on a date with you."
        $ mike.flags.hadadate = True
        $ date_choice = True
    return date_choice


label mike_livingroom_masturbation:
    "I know that we all do it, right?"
    "Everyone does stuff when they think they're alone."
    "The kind of stuff you'd never do if you thought anyone else was watching."
    "It's just weird when you catch someone else doing it."
    "Like right now, when I was just walking past the living room."
    "I see [mike.name] sitting there on the couch, like nothing's up."
    show bree peeping mike surprised at center, zoomAt (1.65, (1050, 720)) with fade
    "But then I notice he has his pants unzipped!"
    "And yeah, you guessed it - he has his cock on his hand too!"
    show bree peeping mike at center, traveling(1.0, 1.0, (640, 720))
    "That's what stopped me in my tracks, why I'm standing here watching him."
    "He thinks that he's alone and that there are no witnesses."
    "And as long as I keep quiet, he won't know otherwise!"
    "Part of me knows that I shouldn't be watching him, that I should sneak away."
    "But another part of me is wanting to stay and see what he does next."
    "I mean, I know what he's going to do next, of course!"
    "I just can't help being more than a little excited at the chance to see it."
    "I'm torn between doing what's right and what feels thrilling, even dangerous."
    "But I know that I have to make up my mind quickly!"
    menu:
        "Leave":
            "I really should leave [mike.name] alone to do what he's doing."
            "He thinks he's alone, and that's how it should stay."
            scene bg secondfloor with fade
            "And so I retrace my steps, being as quiet as I can."
            "Which lets me get away from the scene within a few moments."
            "And let's [mike.name] do what he feels the need to do."
            $ hero.morality += 1
            $ game.room = "secondfloor"
        "Watch":
            "I know that the right thing to do would be to sneak away."
            "[mike.name] obviously thinks that there's nobody to see what he's doing."
            "But somehow the desire to keep watching is too strong."
            "And so I stand still, trying to keep as quiet as I can."
            "Even my breathing sounds loud to me right now."
            "But [mike.name] shows no sign of hearing it."
            "He keeps right on playing with his cock."
            "And my eyes grow wider as it begins to get bigger."
            "Soon enough, it's standing tall and proud."
            "It's not the biggest one I've ever seen."
            "I mean you see freakishly huge ones in porn and stuff."
            "But it's still more than enough to be impressive."
            show bree peeping mike pleasure
            "I can feel my heart begin to race as [mike.name]'s hand moves."
            "He works the shaft, stroking it up and down."
            "And all the time he has his eyes closed."
            "Yet I can see from the look on his face that he's thinking."
            "He's picturing something that's getting him off right now."
            "And it seems to be working, as he's speeding up!"
            "[mike.name] groans and sighs as his pleasure builds."
            "His hand is squeezing his cock as he works it."
            "And I can't help wondering what he's thinking about."
            "I wonder...could it be Sasha he's picturing?"
            "Or even me?!?"
            "Suddenly my thoughts are curtailed as [mike.name] cries out."
            "It's not a loud or shrill cry, more a desperate grunt."
            show bree peeping mike cum with vpunch
            "And I watch as he cums, spurting into the air."
            "I barely have time to see it run down [mike.name]'s cock and onto his hands."
            scene bg secondfloor with fade
            "Because it's at that moment I turn and dart away from the door."
            "All I can do is pray that he doesn't hear me as I flee."
            "And that the image of what I just saw will eventually fade."
            "Because right now it's burned into my mind's eye!"
            $ game.room = "secondfloor"
            $ hero.morality -= 1
        "Watch and masturbate":
            "I know that the right thing to do would be to sneak away."
            "[mike.name] obviously thinks that there's nobody to see what he's doing."
            "But somehow the desire to keep watching is too strong."
            "And so I stand still, trying to keep as quiet as I can."
            "Even my breathing sounds loud to me right now."
            "But [mike.name] shows no sign of hearing it."
            "He keeps right on playing with his cock."
            "And my eyes grow wider as it begins to get bigger."
            "Soon enough, it's standing tall and proud."
            "It's not the biggest one I've ever seen."
            "I mean you see freakishly huge ones in porn and stuff."
            "But it's still more than enough to be impressive."
            show bree peeping mike pleasure
            "I can feel my heart begin to race as [mike.name]'s hand moves."
            "He works the shaft, stroking it up and down."
            "And all the time he has his eyes closed."
            "Yet I can see from the look on his face that he's thinking."
            "He's picturing something that's getting him off right now."
            "And it seems to be working, as he's speeding up!"
            "[mike.name] groans and sighs as his pleasure builds."
            "His hand is squeezing his cock as he works it."
            "And I can't help wondering what he's thinking about."
            "I wonder...could it be Sasha he's picturing?"
            "Or even me?!?"
            "I don't make a conscious effort to move my hands."
            "And the first thing I honestly feel is my fingers."
            show bree peeping mike down fingering pleasure
            "I feel them slipping into my pants."
            "I feel them finding their way between my thighs."
            "And before I know it, they're stroking my pussy."
            "I don't know why it makes me so excited."
            "But the mere thought of [mike.name] masturbating over me..."
            "It makes my lips wet within moments of it crossing my mind!"
            "I don't know it it's the sight of his cock getting so hard."
            "Or else the thought of what he might do with it."
            "But whatever the cause, I'm getting just as worked up as he is!"
            "One of my hands is tracing the folds of my pussy."
            "And the other one finds its way under my top."
            "But squeezing my nipples only seems to make things worse."
            "It does nothing at all to release the tension."
            "In fact it makes the desire that I'm feeling even more intense!"
            "Suddenly my thoughts are curtailed as [mike.name] cries out."
            "It's not a loud or shrill cry, more a desperate grunt."
            show bree peeping mike cum with vpunch
            "And I watch as he cums, spurting into the air."
            "I barely have time to see it run down [mike.name]'s cock and onto his hands."
            with vpunch
            "Because I cum a few seconds after he does."
            with vpunch
            "I bite down on my lip, but not before I moan in release."
            "And I swear the only reason I'm not heard is dumb luck."
            "Because [mike.name] is too out of it himself to hear me."
            scene bg secondfloor with fade
            "I turn and dart away from the door."
            "All I can do is pray that he doesn't hear me as I flee."
            "And that the image of what I just saw will eventually fade."
            "Because right now it's burned into my mind's eye."
            "And my pussy is still tender from the experience too!"
            $ game.room = "secondfloor"
            $ hero.morality -= 2
        "Give a blowjob" if hero.morality <= -25:
            "I know that the right thing to do would be to sneak away."
            "[mike.name] obviously thinks that there's nobody to see what he's doing."
            "But somehow the desire to keep watching is too strong."
            "And so I stand still, trying to keep as quiet as I can."
            "Even my breathing sounds loud to me right now."
            "But [mike.name] shows no sign of hearing it."
            "He keeps right on playing with his cock."
            "And my eyes grow wider as it begins to get bigger."
            "Soon enough, it's standing tall and proud."
            "It's not the biggest one I've ever seen."
            "I mean you see freakishly huge ones in porn and stuff."
            "But it's still more than enough to be impressive."
            show bree peeping mike pleasure
            "I can feel my heart begin to race as [mike.name]'s hand moves."
            "He works the shaft, stroking it up and down."
            "And all the time he has his eyes closed."
            "Yet I can see from the look on his face that he's thinking."
            "He's picturing something that's getting him off right now."
            "And it seems to be working, as he's speeding up!"
            "[mike.name] groans and sighs as his pleasure builds."
            "His hand is squeezing his cock as he works it."
            "And I can't help wondering what he's thinking about."
            "I wonder...could it be Sasha he's picturing?"
            "Or even me?!?"
            "That's what decides it for me."
            "It's the thought that flips a switch in my head."
            "For some reason I'm not happy to simply watch anymore."
            "I have to become a part of what's unfolding before me."
            scene bg livingroom
            show mike naked surprised at center, zoomAt(1.25, (640, 900)), vshake
            "As soon as he sees me slip into the room, [mike.name] panics."
            "He turns red and tries to stuff his cock back into his pants."
            show mike blush
            mike.say "[hero.name[0]]...[hero.name]..."
            mike.say "I...I can explain!"
            mike.say "This isn't what it looks like!"
            "I smile and shake my head."
            "And then I hold a finger to my lips to silence him."
            bree.say "Shh!"
            bree.say "Don't be silly, [mike.name]!"
            bree.say "What else could it be?"
            scene bg black
            show bree cinema bj mike livingroom naked
            with fade
            "I kneel down in front of him, holding his gaze."
            "And I take hold of his cock without asking for permission."
            bree.say "Now then..."
            bree.say "Let me take care of that..."
            "[mike.name] stops trying to resist as I begin to lick the tip."
            "And within seconds, his cock is harder then ever."
            "He lays back and lets me have my way with him."
            "And I don't waste any time in doing so."
            "His cock feels just as good as I thought it would."
            show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
            "It fills my mouth as I swallow it and suck him hard."
            "My ears are filled with the sound of him gasping."
            "And I busy my hands at the same time."
            "One stroking his shaft and the other playing with his balls."
            "I can feel myself getting wet too, wanting him inside of me."
            "The idea of making [mike.name]'s little self-indulgence special is so hot."
            "Making his fantasy come true if he was thinking of me."
            "And even better, making sure he will be the next time he does it too!"
            "Suddenly my thoughts are curtailed as [mike.name] cries out."
            "It's not a loud or shrill cry, more a desperate grunt."
            "But it lets me know what's coming."
            show bree cinema bj cum
            menu:
                "Spit":
                    show bree cinema bj cum
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    with vpunch
                    "[mike.name] shoots his entire load into my mouth a second later."
                    with vpunch
                    "It's almost too much for me to handle, but I hold on to the end."
                    with vpunch
                    "And once he's done, I let his cock slide out of my mouth."
                    "I smile at him as the cum drips from my lips."
                    "Then I spit it out onto the floor beside me."
                "Swallow":
                    show bree cinema bj cum
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    with vpunch
                    "[mike.name] shoots his entire load into my mouth a second later."
                    with vpunch
                    "It's almost too much for me to handle, but I hold on to the end."
                    with vpunch
                    "And once he's done, I let his cock slide out of my mouth."
                    show bree cinema bj -cum
                    show sexinserts head bree -cum zorder 1 at center, zoomAt(1, (720, 810))
                    "Then I make a point of swallowing it while he watches."
                    "Even licking the last drops from my lips."
                "Facial":
                    scene couch fun
                    show couch fun bree
                    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
                    with fade
                    "At the last moment, I slide his cock out of my mouth."
                    show couch fun cumshot with vpunch
                    "And then I close my eyes as he shoots his load into my face."
                    show couch fun cumshot facial with vpunch
                    "His cum feels crazily hot as it paints my cheeks."
                    show couch fun -cumshot
                    "And I'm sure to keep my eyes closed and mouth open the whole time."
                    "I only reverse the arrangement when I'm sure he's finally spent."
            hide sexinserts
            "[mike.name] opens his mouth to speak."
            "But I put a finger to his lips, silencing him."
            "And while he's lost for words, I slip out of the room."
            $ hero.morality -= 2
            $ mike.love += 2
    $ game.pass_time(1)
    return

label mike_pregnancy_congratulations:
    "[mike.name]'s been staring at me for a while now."
    "Like there's something different about me."
    show mike down
    "But he can't quite put his finger on it."
    "In the end, I decide to help him out."
    bree.say "I'm pregnant, [mike.name]!"
    bree.say "That's what's different."
    "[mike.name]'s eyes go wide at this, like he's genuinely surprised."
    show mike surprised
    "He blinks a couple of times, but then a smile spreads over his face."
    mike.say "Congratulations, [hero.name]!"
    show mike happy
    mike.say "Wow..."
    mike.say "I can't believe that one of my housemates is having a baby!"
    bree.say "Yeah, well..."
    bree.say "It came as quite a surprise to me too!"
    mike.say "So..."
    show mike normal
    mike.say "What are you planning to do about..."
    mike.say "Well...about everything?"
    bree.say "I dunno, [mike.name]."
    bree.say "I'm just trying to get my head around being pregnant right now."
    $ mike.love += 1
    return

label mike_propose_female:
    show mike
    "I've always had a rule that I'd stop and pinch myself when I started to get serious feelings for someone."
    "Well, not literally pinch myself...but stop and really think things out, you know?"
    "Because in the past I've been guilty of letting myself get carried away by my feelings."
    "And let's just say that it never seems to turn out for the best when that happens."
    "So when I first found myself getting those deep and serious feelings for [mike.name], I kept doing just that."
    "I'd take the time to pause and really reflect on where our relationship was and where it could go next."
    "But right now that's proving harder than ever to do."
    "Because I think we've reached the point where things could go to the next level."
    "I feel like I want to be the one to bring it up too."
    "Mainly because while [mike.name]'s a great guy, he's not too clued up on that kind of thing."
    "Like, he might be feeling the exact same way as I am right now."
    "But that doesn't mean he'd know how to act on those feelings."
    "So I kind of need to step in and make sure that things go as they should."
    "And that's what makes up my mind in the end - the fact that I'm being the responsible one here."
    show mike at center, zoomAt(1.5, (640, 1040)) with fade
    "So when the right moment comes along, I take a deep breath and then just go for it."
    bree.say "[mike.name]..."
    mike.say "Erm..."
    mike.say "Yeah, [hero.name]?"
    bree.say "Where do you see us going?"
    show mike annoyed
    mike.say "Nowhere in particular, [hero.name]."
    show mike down
    mike.say "I thought we were just strolling around for a while."
    show mike normal
    mike.say "Why do you ask?"
    mike.say "Is there somewhere you wanted to go in particular?"
    "I do the best I can not to facepalm right in front of [mike.name]."
    "And I force a smile onto my face while wondering how guys can be so dumb sometimes."
    bree.say "No, [mike.name]..."
    bree.say "I meant our relationship."
    bree.say "Where do you see it going?"
    show mike surprised
    "Surprise shows on [mike.name]'s face as he realises what I mean."
    show mike sad
    "And then I see genuine fear in his eyes."
    mike.say "[hero.name]..."
    mike.say "You're..."
    mike.say "You're not dumping me, are you?!?"
    with vpunch
    bree.say "WHAT?!?"
    bree.say "No, [mike.name]..."
    bree.say "Of course I'm not dumping you!"
    bree.say "I'm doing the exact opposite, you dummy!"
    bree.say "I'm trying to ask if...if you'll marry me?"
    show mike surprised
    if mike.love < 195:

        "Suddenly the surprise is back on [mike.name]'s face again."
        "And if anything, the fear in his eyes is even more intense!"
        hide mike
        show mike surprised
        "He even takes a step backwards and away from me."
        "Waving his hands in the air as if he's actually afraid."
        mike.say "You can't be serious, [hero.name]!"
        mike.say "That's way worse than wanting to break up with me!"
        mike.say "Please, tell me that you're joking?"
        "I'm starting to feel a strange cocktail of emotions right now."
        "For example I know that hurt and disappointment are in there."
        "But they're being overshadowed by the amazement I'm feeling at [mike.name]'s reaction."
        bree.say "Jesus, [mike.name]..."
        bree.say "What are you even talking about?"
        bree.say "How can me proposing be worse than breaking up with you?!?"
        "I don't know if [mike.name] actually hears what I'm saying."
        "Because it doesn't seem like he has an answer to my question."
        mike.say "I...I can't deal with this, [hero.name]..."
        mike.say "It's too much for my brain to handle!"
        mike.say "I have to get away!"
        show mike at right with ease
        "Before I can say another word, [mike.name] turns on his heel."
        hide mike with easeoutright
        "And then he hurries away, not stopping to look back."
        "Which leaves me standing alone and speechless."
        "Because I can't honestly understand what I did wrong."
        "Apart from actually asking him to marry me!"
        $ mike.love -= 25
    else:

        "Suddenly the surprise is back on [mike.name]'s face again."
        "But this time the look in his eyes is very different."
        "If anything, they're filled with what looks like amazement."
        "And he adds to the impression my blinking several times before he can actually speak a word."
        mike.say "Wha..."
        mike.say "What did you just say?"
        bree.say "I..."
        bree.say "I said...will you marry me?"
        "At first I think [mike.name]'s nodding because he recognises that was what I did just say."
        "But then it dawns on me that he's still nodding, and he doesn't show any sign of stopping!"
        show mike happy
        show fx heart
        mike.say "Of course I will!"
        mike.say "I...I mean, yes!"
        mike.say "Yes, I'll marry you, [hero.name]!"
        "Now it's my turn to have the same reaction as [mike.name] did before."
        "My head starts nodding, my eyes go wide."
        "And I can't stop myself grinning like a fool."
        "Neither of us seems to be able to say anything after that."
        "At least nothing that makes any kind of sense."
        "So instead we throw our arms around each other."
        hide mike
        show mike kiss
        with fade
        $ mike.flags.kiss += 1
        "And in the embrace that follows, we kiss with a genuine passion."
        "Because maybe this is the way that we're both far better at communicating."
        "Simple and intimate, yet also deep and instinctual in nature."
        "Whatever the truth of the matter, that's not what's important right now."
        "What is important is that I got the answer I was hoping for."
        $ mike.set_fiance()
    hide mike
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
