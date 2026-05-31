init python:
    Event(**{
    "name": "jack_give_phone_number",
    "label": "give_phone_number",
    "girl": "jack",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(jack,
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
    "name": "jack_send_text",
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
        PersonTarget(jack,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "jack",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "jack_are_you_sick",
    "label": "are_you_sick",
    "girl": "jack",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(jack,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (jack, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "jack_auto_chat",
    "label": "auto_chat",
    "girl": "jack",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(jack,
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
    "name": "jack_ask_out",
    "label": "ask_out",
    "girl": "jack",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("ask_date")),
            ),
        PersonTarget(jack,
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
    "name": "jack_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "jack",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(jack,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label jack_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = jack.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = jack.get_activity(bye_hour)
    if not activity == jack.activity:
        if day != game.week_day:
            $ jack.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ jack.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"jack {bye_outfit}")
        if activity["activity"] == "sleep":
            jack.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            jack.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            jack.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            jack.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            jack.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            jack.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            jack.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            jack.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            jack.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            jack.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            jack.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            jack.say "I'll go get dressed."
        hide jack
    return

label jack_cheated(action, cheat_npc=None):
    show jack
    if not jack.sub >= 75:
        show fx anger
        $ loss = 5
        if jack.flags.boyfriend or jack.flags.fiance:
            $ loss += 5
        $ jack.love -= loss
        "I see Jack looking at me [action] someone else with a painful hurting face..."
    else:
        show jack perv
        show fx heart
        $ jack.sub += 1
        "I see Jack looking at me [action] someone else with envy and lust in his eyes."
    hide jack
    return

label jack_beats_ryan_female:
label jack_beats_scottie_female:
    if randint(1, 100) <= 20:
        return "abort"
    "I can feel [active_girl.name]'s lips against mine, his hands all over me."
    "I know that I should be stopping him, but it's so hard to resist!"
    jack.say "HEY!"
    jack.say "What the hell?!?"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show jack angry at left5
    $ renpy.show(f"{active_girl.id} angry", at_list=[right5])
    "At the sound of Jack's voice, [active_girl.name] releases me from his grip."
    "I gasp and look around to see him standing there, visibly seething."
    bree.say "Jack, I..."
    "But before I can try to explain myself, Jack cuts me off."
    jack.say "Quiet, [hero.name]..."
    jack.say "This is between me and this slimeball!"
    "I can't help gasping in surprise at Jack."
    "He looks steely, determined and downright manly right now!"
    "Call me shallow, but he's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "Who are you supposed to be, tubby?"
        ryan.say "A Jack Black tribute act?!?"
    elif active_girl.id == "scottie":
        scottie.say "Whoa, you remind me of that fat dude!"
        scottie.say "The one from the band with all the hilarious songs."
        scottie.say "You know the one I mean, right?"
    "Jack answers the question by stepping up and punching [active_girl.name]."
    "I mean it, he literally hits him square on the jaw!"
    "[active_girl.name] staggers back, clutching his mouth."
    "But I don't know if it's from pain or sheer surprise that Jack hit him!"
    "Either way, he doesn't get a chance to respond."
    "Jack throws himself at [active_girl.name], and the fight is on!"
    "Actually, it's more of a scuffle than an actual fight."
    "Because it seems like neither of them is a actually any good at it!"
    "Punches and kicks miss as often as they hit."
    "And the only decisive thing that happens does so by total accident."


    pause 0.2
    $ renpy.hide(f"{active_girl.id}")
    hide jack
    $ renpy.show(f"jack beats {active_girl.id}")
    with vpunch
    "Jack swings a kick and it connects squarely with [active_girl.name]'s groin."
    "He groans and doubles over, sinking slowly to his knees."
    if active_girl.id == "ryan":
        ryan.say "Aaargh..."
        ryan.say "My groin!"
    elif active_girl.id == "scottie":
        scottie.say "Urgh..."
        scottie.say "Dude, that is NOT cool!"
    jack.say "Take that, you asshole!"
    jack.say "That's what happens when you mess with my chick!"
    return

label jack_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Jack."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Jack."
        elif game.hour < 12:
            bree.say "Good morning Jack."
        elif game.hour < 19:
            bree.say "Good afternoon Jack."
        else:
            bree.say "Good evening Jack."
    return

label jack_kiss_female:
    scene expression f"bg {game.room}"
    if jack.love < 25 and not jack.is_boyfriend and not game.active_date.score >= 75:
        "I feel like the time is right, like Jack's giving me all the right signals."
        "But as soon as I lean in, trying to plant my lips on his, he pulls back."
        "Which leaves me exposed and embarrassed, having misread the situation."
        "Jack coughs nervously and looks away, trying to pretend it never happened."
        "Which leaves me looking the other way, burning with shame."
        $ jack.love -= 5
        $ jack.sub -= 5
        hide jack
    elif not jack.flags.kiss:
        hide jack
        show jack kiss
        "I...I'm going to do it - I'm going to take a chance!"
        "Before I can second-guess myself, I lean forwards."
        "Jack turns towards me at just the right moment."
        "Our lips meet, and then it happens!"
        "I think we're both surprised, me that I did it and him that it's happening."
        "But then something overrides all of the nerves and the fear."
        "After that, Jack leans into the kiss, giving it all he has."
        "And I feel myself melting as he does so, sinking into him."
        "Tongues get involved somewhere along the way, things getting hotter all the time."
        "But neither of us is thinking straight, just enjoying the thrill of the moment."
        hide jack kiss
        $ jack.flags.kiss += 1
    else:
        hide jack
        $ jack.love += 2
        show jack kiss
        "I lean in to place a kiss on Jack's lips, and he responds in kind."
        "It feels electric, like we're sharing something that's just between us."
        "I feel his tongue against my lips, and I want to giggle like a kid."
        "But instead I open my mouth a little wider and sigh with pleasure."
        "I'm kissing a geek - and it's crazy how hot it feels!"
        hide jack kiss
        $ jack.flags.kiss += 1
    return

label jack_propose_female:
    show jack
    "This is crazy, and part of me can't actually believe that I'm doing it."
    "Jacks a nerd, a great big...no, a HUGE nerd!"
    "Probably the most hardcore nerdy guy that I know - and I know [mike.name]!"
    "But he's the sweetest and funniest too."
    "And...and well, he's kinda strangely sexy, in a way I don't totally understand!"
    "All I know is that I want to spend as much time with him as I can."
    "In fact, I want to make sure he's around all the time."
    "Which is why pick my moment, and then I get down on one knee."
    jack.say "Huh?"
    jack.say "[hero.name], what's up?"
    "Jack looks down at me, concern in those big, puppy-dog eyes of his."
    "And for a moment I almost lose my nerve, thinking up an excuse to get out of it."
    "But then I shake it off and plunge in, to hell with the consequences!"
    bree.say "I...I don't know if this is how a girl's supposed to do it, Jack."
    bree.say "But...will..."
    bree.say "Will you marry me?"
    "Jack looks like he doesn't believe me at first."
    "Like he thinks that I'm pulling a prank on him."
    "But then the truth begins to dawn on him."
    jack.say "Are..."
    jack.say "Are you serious, [hero.name]?"
    bree.say "Of course I am, Jack!"
    bree.say "I love you and I want to marry you!"
    bree.say "So are you going to give me an answer or what?!?"
    if jack.love >= 195:
        jack.say "OF COURSE I WILL!"
        jack.say "[hero.name], I never thought you'd ask!"
        jack.say "I mean, a girl like you..."
        jack.say "And a guy like me..."
        "I can see that Jack's starting to babble with excitement."
        "So I come to his rescue by leaping to my feet and kissing him on the lips."
        "And it only takes a few seconds for him to stop talking and return the gesture."
        "The kiss is long, passionate and charged with emotion for the both of us."
        "And when it's over, we linger in each others arms, breathing heavily."
        bree.say "Oh, Jack..."
        bree.say "I was so nervous just now!"
        jack.say "Huh?!?"
        jack.say "Why's that, [hero.name]?"
        bree.say "Well..."
        bree.say "I thought you might say no!"
        jack.say "Do I look like I'm insane?"
        jack.say "When a hot, cool and smart girl is into me..."
        jack.say "And when she makes me feel like you do, [hero.name]..."
        jack.say "How was I ever going to say no?"
        "I bury my head into Jack's chest, almost crying with joy."
        "What did I ever do to deserve a guy this sweet and loving?"
        "And now I get to spend the rest of my life with him too!"
        $ jack.set_fiance()
    else:
        jack.say "I..."
        jack.say "I'm sorry, [hero.name]..."
        jack.say "But it's a no - I can't marry you!"
        "At first I can't believe what I'm hearing."
        "Yeah, I know that it's pretty big ego-trip on my part."
        "Assuming that the geeky guy is going to be bowled over by the offer of marriage."
        "But even when I start to be able to wrap my head around it, I'm still puzzled."
        bree.say "B...but why, Jack?"
        bree.say "I thought we were getting on great?"
        bree.say "That we were like best friends?"
        jack.say "Yeah, [hero.name], that's right."
        jack.say "And I think that's why we work so well together."
        jack.say "I'm worried that if we make it more formal, it'll stop being fun."
        "I nod sadly, trying to see Jack's side of things."
        "The truth is that I don't know if I can."
        "But I do my best in the hope of keeping our relationship alive."
        "Even if right now it feels like it's kind of on life-support!"
        bree.say "O...okay, Jack."
        bree.say "Good point!"
        "Jack smiles and nods, accepting my answer."
        "But it still feels like he's sticking a knife into my guts."
        $ jack.love -= 25
        $ jack.sub -= 25
    hide jack
    return

label jack_ask_date_female:



    call jack_ask_date_alone_female from _call_jack_ask_date_alone_female
    return _return

label jack_ask_date_alone_female:
    if not jack.flags.hadadate:
        bree.say "We're having a good time together, right?"
        bree.say "I mean, like - we hang out all the time, yeah?"
        "Jack looks at me with a confused expression."
        "It's like he understands the words I'm using."
        "But they don't make sense right here and now."
        jack.say "Erm...yeah, [hero.name]."
        jack.say "I think so too."
        bree.say "So if I asked you to actually do something just with me..."
        bree.say "Like just the two of us in a specific place at a specific time?"
        jack.say "What...you mean...like...like a DATE?"
        "I feel a nervous smile spreading across my face."
        "But I nod and try to look positive all the same."
        bree.say "Yeah, Jack - exactly like that!"
        bree.say "So what do you say?"
        bree.say "You wanna go on a date with me?"
    else:
        bree.say "Hey Jack, you want to join me so we can seek fun together?"
    if jack.love < 50 or jack.flags.nodate:
        if not jack.flags.hadadate:
            jack.say "Erm...no, [hero.name]."
            jack.say "I don't think I'm ready for that."
            jack.say "It's kind of a big commitment."
            jack.say "Can't we just stay friends?"
            bree.say "Erm...I guess so, Jack..."
        else:
            jack.say "Sorry [hero.name], I don't feel like it."
        $ date_choice = False
    else:
        jack.say "Are you frikin kidding, [hero.name]?!?"
        jack.say "Of course I do!"
        jack.say "I just thought you'd never ask."
        jack.say "I thought you might see me as just a friend, you know?"
        bree.say "Oh no, Jack - I see you as more than that!"
        $ jack.flags.hadadate = True
        $ date_choice = True
    return date_choice

label jack_pregnancy_congratulations:
    jack.say "Oh, [hero.name]..."
    show jack smile
    jack.say "You're pregnant?"
    jack.say "How did I only notice just now?"
    "I look up to see Jack hurrying over to me."
    "And the expression on his face is one of genuine interest."
    "So I give him a smile and a shrug."
    bree.say "I don't know, Jack..."
    bree.say "I guess I only started showing recently."
    "He nods, staring at my belly with evident fascination."
    "But then he looks up at me, realising that I'm watching him too."
    show jack -smile
    jack.say "Oh..."
    jack.say "Sorry, [hero.name]!"
    jack.say "I'm not used to being around pregnant women!"
    jack.say "Congratulations though."
    show jack happy
    jack.say "I'm sure you'll be a great mom!"
    "I can't help smiling at Jack's natural enthusiasm."
    "Not to mention the trouble he has in concealing his emotions!"
    bree.say "Thanks, Jack..."
    bree.say "That means a lot!"
    $ jack.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
