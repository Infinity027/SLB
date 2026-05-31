init python:
    Event(**{
    "name": "dwayne_auto_greet",
    "label": "auto_greet",
    "girl": "dwayne",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(dwayne,
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
    "name": "dwayne_give_phone_number",
    "label": "give_phone_number",
    "girl": "dwayne",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(dwayne,
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
    "name": "dwayne_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(dwayne,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "dwayne",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "dwayne_are_you_sick",
    "label": "are_you_sick",
    "girl": "dwayne",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(dwayne,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (dwayne, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "dwayne_auto_chat",
    "label": "auto_chat",
    "girl": "dwayne",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(dwayne,
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
    "name": "dwayne_ask_out",
    "label": "ask_out",
    "girl": "dwayne",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("ask_date")),
            ),
        PersonTarget(dwayne,
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
    "name": "dwayne_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "dwayne",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(dwayne,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label dwayne_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = dwayne.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = dwayne.get_activity(bye_hour)
    if not activity == dwayne.activity:
        if day != game.week_day:
            $ dwayne.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ dwayne.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"dwayne {bye_outfit}")
        if activity["activity"] == "sleep":
            dwayne.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            dwayne.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            dwayne.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            dwayne.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            dwayne.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            dwayne.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            dwayne.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            dwayne.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            dwayne.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            dwayne.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            dwayne.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            dwayne.say "I'll go get dressed."
        hide dwayne
    return

label dwayne_cheated(action, cheat_npc=None):
    show dwayne
    if not dwayne.sub >= 75:
        show dwayne annoyed
        show fx anger
        $ loss = 5
        if dwayne.flags.boyfriend or dwayne.flags.fiance:
            $ loss += 5
        $ dwayne.love -= loss
        "I see Dwayne looking at me [action] someone else with a painful hurting face..."
    else:
        show fx heart
        $ dwayne.sub += 1
        "I see Dwayne looking at me [action] someone else with envy and lust in his eyes."
    hide dwayne
    return

label dwayne_beats_ryan_female:
label dwayne_beats_scottie_female:
label dwayne_beats_jack_female:
label dwayne_beats_shawn_female:
label dwayne_beats_mike_female:
label dwayne_beats_danny_female:
    if randint(1, 100) <= 90:
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
    "I know that I should be stopping him, but it's so hard to resist!"
    dwayne.say "Well, well..."
    dwayne.say "What do we have here?"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show dwayne angry at right5
    $ renpy.show(f"{active_girl.id} angry", at_list=[left5])
    if active_girl.id == "ryan":
        "At the sound of Dwayne's voice, Ryan releases me from his grip."
    elif active_girl.id == "danny":
        "At the sound of Dwayne's voice, Danny turns around to glare at him."
    else:
        "At the sound of Dwayne's voice, [active_girl.name] leaps away from me."
    bree.say "Dwayne, I..."
    bree.say "I can explain..."
    bree.say "This isn't what it looks like!"
    "Dwayne raises a single eyebrow."
    "And somehow that's enough to cut everyone else off."
    dwayne.say "No need to explain, [hero.name]."
    dwayne.say "I've had to fight for everything I wanted in my life."
    dwayne.say "And you're no different."
    dwayne.say "So you just stand back and watch me lay some smack down on these jabronies!"
    "I can't help gasping in surprise at Dwayne."
    "He looks steely, determined and downright manly right now!"
    "Call me shallow, but he's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "W...wait!"
        ryan.say "Don't do this - I'll pay you whatever you want!"
    elif active_girl.id == "jack":
        jack.say "Oh shit!"
        jack.say "This is just like some scene from a movie!"
    elif active_girl.id == "shawn":
        shawn.say "Wait, I work in an electronics store..."
        shawn.say "How about I give you a discount next time you're in the area?"
    elif active_girl.id == "mike":
        mike.say "Wait...I should be the one saying shit like that!"
        mike.say "I always had the strangest feeling that I was the main character in this story!"
    elif active_girl.id == "danny":
        danny.say "Hey - stop it with the badass lines already!"
        danny.say "I'm supposed to be the tough guy around here!"
    "But for all the pleading, Dwayne's just not in the mood to listen."
    $ renpy.hide(f"{active_girl.id}")
    hide dwayne
    $ renpy.show(f"dwayne beats {active_girl.id}")
    with hpunch
    "He strides into the fight with a confidence that's pretty scary."
    "And it seems to be scaring the other guy too."
    "Because it's a pretty one-sided affair."
    "Dwayne punches, kicks and head-butts his way to a quick Vincenty."
    "Then Dwayne lifts [active_girl.name] into the air and slams him down onto the ground."
    bree.say "Oh, Dwayne - you killed him!"
    dwayne.say "Nah, [hero.name]..."
    dwayne.say "This loser's just in lala land!"
    return

label dwayne_greet:
    if renpy.has_label(f"dwayne_greet_dialogues_{hero.gender}") and not dwayne.flags.greeted:
        scene expression f"bg {game.room}"
        $ dwayne.flags.greeted = TemporaryFlag(True, 1)
        show dwayne
        $ result = randint(1, 3)
        if result == 1:
            dwayne.say "Hello, [hero.name]."
        elif result == 2:
            dwayne.say "Hi, [hero.name]."
        elif result == 3:
            dwayne.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                dwayne.say "Good morning [hero.name]."
            elif game.hour < 19:
                dwayne.say "Good afternoon [hero.name]."
            else:
                dwayne.say "Good evening [hero.name]."
        call expression f"dwayne_greet_dialogues_{hero.gender}" from _call_expression_453
        hide dwayne
    return

label dwayne_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Dwayne."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Dwayne."
        elif game.hour < 12:
            bree.say "Good morning Dwayne."
        elif game.hour < 19:
            bree.say "Good afternoon Dwayne."
        else:
            bree.say "Good evening Dwayne."
    return

label dwayne_kiss_female:
    scene expression f"bg {game.room}"
    if dwayne.love < 25 and not dwayne.is_boyfriend and not game.active_date.score >= 75:
        show dwayne
        "Dwayne's doing his usual thing of talking while waving his arms around."
        "He's really into the story he's telling, hands moving up and down."
        "And yeah, I hate to admit it - but he's got me hanging on his every word!"
        "Ooh...I hate that he can be so charming!"
        "Then he leans forwards, and I don't really know what happens."
        "My subconscious mind seems to take over, or maybe my suppressed desires."
        "Either way I lean forwards, expecting Dwayne to plant a kiss on my lips."
        show dwayne annoyed
        "But at the last moment he pulls away, a huge smile on his face."
        "I can feel my cheeks flushing red, because he knows what just happened."
        "Dwayne shakes his head and waves a finger at me."
        "He's clearly enjoying watching me squirm right now!"
        show dwayne -annoyed
        $ dwayne.love -= 1
    elif not dwayne.flags.kiss:
        show dwayne
        "There are times when I hate Dwayne for how charismatic he can be."
        "It's like I know that he's also a massive jerk, I totally do."
        "But his charm somehow overrides the rational part of my brain."
        "And that smile - it makes me feel like a giggling bimbo!"
        "So when I finally lean in close, he raises one eyebrow..."
        "Oh god - there's no way that I was ever going to be able to resist!"
        hide dwayne
        show dwayne kiss
        "Kissing Dwayne for the first time feels like such a relief."
        "Like I'm thirsty and I finally got to take a long, cool drink!"
        "It lasts a very long time, and neither of us is keen for it to stop."
        "God...I know he's a jerk."
        "But I don't want him to stop kissing me all the same!"
        hide dwayne kiss
        $ dwayne.flags.kiss += 1
        $ dwayne.love += 5
    else:
        show dwayne
        "Part of me hates the way that Dwayne only has to glance in my direction."
        "That he only needs to raise his eyebrow in that way he has."
        "Because then my heart starts beating faster, and I can't help myself."
        "I know that he wants to plant a kiss on me, and that I want it too!"
        hide dwayne
        show dwayne kiss
        "I find myself hurrying over to him and almost throwing myself into his arms."
        "Oh god, he's an arrogant asshole!"
        "But he's so damn sexy with it too!"
        "I just can't wait to be in his arms."
        "That and kissing him like my life depended on it!"
        hide dwayne kiss
        $ dwayne.flags.kiss += 1
        $ dwayne.love += 5
    return

label dwayne_propose_female:
    show dwayne at center, zoomAt(1, (640, 740))
    "I've been dating Dwayne for quite some time now, and I feel like it shouldn't be the case."
    "But the truth is that I still find him more than a little intimidating at times."
    "I mean, I know it's a lot - the teeth, the shaved head and that bod!"
    "Sometimes it's like I'm staring at a demi-god!"
    "Sorry, sorry...I know how crazy that must make me sound."
    "The thing is that I also know that I have real feelings for Dwayne."
    "The kind of feelings that have gone way beyond just liking his company and digging his body."
    "In fact...I think that I'm seriously in love with the guy!"
    "So much that I have to do something about it."
    "In the movies, it's always the guy getting down on one knee in front of the girl."
    "But Dwayne doesn't seem to be about to do that with my any time soon."
    "And that's a pretty old-fashioned thing anyway, right?"
    "The girl waiting for the guy to make the first move?"
    "A modern woman like me shouldn't have to do that."
    "And a modern guy would respect me for taking the initiative too."
    "At least that's what I'm hoping will be the case as I put my plan into action."
    bree.say "Erm..."
    bree.say "Dwayne..."
    show dwayne annoyed
    dwayne.say "Hmm..."
    show fx question
    dwayne.say "What's the matter, [hero.name]?"
    "Oh god...I don't even know what I'm supposed to be doing right now!"
    "I've half started to get down on one knee already."
    "But then I stop because I realise that I don't have a ring on me."
    "So what in the hell am I doing that for?"
    "Yet now I look like I'm curtseying in front of Dwayne!"
    bree.say "I..."
    bree.say "I wanted to ask you something..."
    bree.say "Yeah, that's it!"
    bree.say "I wanted to ask you something."
    show dwayne therock
    "I straighten myself up as Dwayne looks on with interest in his eyes."
    "And I just hope that it's enough to make him ignore how awkward I've made things already."
    dwayne.say "Well, [hero.name]..."
    dwayne.say "What is it?"
    dwayne.say "What did you want to ask me?"
    bree.say "We get on well, yeah?"
    bree.say "You and me, we have a lot of fun..."
    bree.say "Don't we?"
    show dwayne happy
    dwayne.say "Of course we do, [hero.name]."
    dwayne.say "Is that all you wanted to ask me?!?"
    show dwayne normal
    "I shake my head and stumble on."
    bree.say "No...of course not..."
    bree.say "What I mean to say is...I like you, a lot!"
    show dwayne happy
    dwayne.say "I like you too, [hero.name]."
    dwayne.say "I'd have thought that was obvious!"
    show dwayne annoyed
    bree.say "Urgh..."
    bree.say "I'm trying to say that I like you enough to want more."
    bree.say "To want to make a serious commitment to you."
    bree.say "Oh to hell with it!"
    bree.say "Dwayne..."
    bree.say "Will you marry me?"
    if dwayne.love > 195:
        show dwayne smile
        "I watch as a smile spreads across Dwayne's face and those huge teeth are revealed in the process."
        "And when he starts to nod his head too, I feel the sensation of my heart leaping in my chest."
        dwayne.say "You know what, [hero.name]..."
        dwayne.say "That's a great idea."
        dwayne.say "In fact, I should have thought of it myself!"
        "By now I'm nodding too."
        "And I'm trapped in that awful state of thinking something might actually be true."
        "But still needing the other person to plainly state that's the case."
        bree.say "What are you saying, Dwayne?"
        bree.say "Is that a yes or a no?"
        "Dwayne looks at me with a quizzical expression on his face."
        show fx question
        dwayne.say "You need me to say it, [hero.name]?"
        bree.say "Erm...yeah!"
        bree.say "I really do!"
        show dwayne happy
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        "Dwayne lets out one of his typically booming laughs."
        show dwayne smile
        dwayne.say "Okay, [hero.name]..."
        dwayne.say "If that's what you want."
        "I'm nodding eagerly the whole time that he's saying this."
        show dwayne happy
        dwayne.say "Yes, [hero.name]..."
        dwayne.say "I will marry you."
        show dwayne smile
        "As soon as I hear those words, I don't know what comes over me."
        "I was expecting to say something in response."
        "But instead I find myself leaping forwards."
        "And then I'm throwing my arms around Dwayne."
        "Well...I'm throwing them as far around him as I can manage."
        "My arms aren't that long!"
        bree.say "Yay!"
        bree.say "We're getting married!"
        bree.say "I...I mean, I'm so happy."
        show dwayne happy
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        "Dwayne lets out another round of booming laughter."
        show dwayne at center, traveling(1.5, 1.0, (640, 1040))
        pause 1
        with vpunch
        pause 0.1
        with vpunch
        pause 0.1
        with vpunch
        "And as I'm pressed tight against him, I feel it reverberate through my entire body!"
        "Then I feel his arms wrapping around me too."
        "And his are more than long enough to go all the way around me!"
        $ dwayne.set_fiance()
    else:
        "I watch as a smile spreads across Dwayne's face and those huge teeth are revealed in the process."
        "And as it's happening, I allow myself to think that it must mean I'm about to get the answer I want."
        "But then I see that Dwayne's also shaking his head, and his eyes are telling a different story."
        dwayne.say "Oh, [hero.name]!"
        dwayne.say "I get, it."
        dwayne.say "I understand where you're coming from."
        bree.say "You..."
        bree.say "You do?"
        show dwayne happy
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
        "Dwayne lets out a booming laugh."
        show dwayne therock
        dwayne.say "Of course I do."
        dwayne.say "You want to make sure you hold onto all of this for as long as possible."
        "As he says this, Dwayne points to himself with both thumbs."
        show dwayne annoyed
        dwayne.say "But I've already been there and done that."
        dwayne.say "Hell, I even got a daughter along the way!"
        show fx drop
        dwayne.say "So the last thing that I want is to do it all again."
        bree.say "So...that's a no?"
        bree.say "You won't marry me?"
        show dwayne therock at hshake
        "Dwayne waves a hand in the air, dismissing my question."
        dwayne.say "My marrying days are behind me, [hero.name]."
        dwayne.say "All I want to do from now on is have a good time."
        dwayne.say "Doesn't that sound better than being my wife?"
        "I nod and do the best I can to force a smile onto my face."
        "Because it looks like that's the best offer I'm going to get right now."
        bree.say "I guess so, Dwayne."
        bree.say "I guess so..."
        $ dwayne.love -= 25
    hide dwayne
    return

label dwayne_ask_date_female:



    call dwayne_ask_date_alone_female from _call_dwayne_ask_date_alone_female
    return _return

label dwayne_ask_date_alone_female:
    if not dwayne.flags.hadadate:
        bree.say "Dwayne..."
        dwayne.say "Yeah, [hero.name]?"
        bree.say "You like hanging out with me, right?"
        bree.say "Like, we have a good time together?"
        dwayne.say "I wouldn't call it hanging out, [hero.name]."
        dwayne.say "That's what teenagers and adult losers do!"
        dwayne.say "But yeah, we have a good time when we're together."
        dwayne.say "What's your point?"
        bree.say "Well...I was wondering if you wanted to hang out..."
        bree.say "I...I mean spend time with me?"
        bree.say "With JUST me?"
        dwayne.say "Oh, you mean you want to go on a date with me?"
        bree.say "YES!"
        bree.say "Yes...I mean, yes...if you want to?"
    else:
        bree.say "Wanna go on a date?... If you want to?"
    if dwayne.love < 50 or dwayne.flags.nodate:
        if not dwayne.flags.hadadate:
            dwayne.say "Ah...I don't think so, [hero.name]."
            dwayne.say "We're not exactly on the same page."
        else:
            dwayne.say "Negative."
        $ date_choice = False
    else:
        dwayne.say "Sure thing, [hero.name]!"
        dwayne.say "That sounds like a great idea."
        $ dwayne.flags.hadadate = True
        $ date_choice = True
    return date_choice

label dwayne_pregnancy_congratulations:
    "Dwayne walks straight up to me with a smile on his face."
    "And he doesn't hesitate to address the elephant in the room."
    dwayne.say "Looks like congratulations are in order, [hero.name]."
    show dwayne smile at center, zoomAt (1.0, (640, 740))
    dwayne.say "How far along are you right now?"
    "I blink in genuine surprise."
    bree.say "How did you know I was pregnant?"
    bree.say "Most guys just don't notice."
    bree.say "Or else they think I put on weight all of a sudden!"
    show dwayne smile
    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
    pause 0.2
    show dwayne at center, zoomAt (1.0, (640, 740)), startle(0.14,-20)
    "Dwayne laughs and shakes his head."
    dwayne.say "Oh come on, [hero.name]..."
    dwayne.say "You have the same glow about you that Cherie did."
    dwayne.say "The one she had when she was carrying Cassidy."
    bree.say "I wish I felt as confident as you sound, Dwayne."
    bree.say "To be honest, it's all a little scary!"
    show dwayne -smile
    dwayne.say "Nonsense, [hero.name]..."
    dwayne.say "I'm sure you can handle it."
    dwayne.say "You'll do just fine, you'll see."
    $ dwayne.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
