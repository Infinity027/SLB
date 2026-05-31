init python:
    Event(**{
    "name": "danny_auto_greet",
    "label": "auto_greet",
    "girl": "danny",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(danny,
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
    "name": "danny_give_phone_number",
    "label": "give_phone_number",
    "girl": "danny",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(danny,
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
    "name": "danny_send_text",
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
        PersonTarget(danny,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "danny",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "danny_are_you_sick",
    "label": "are_you_sick",
    "girl": "danny",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(danny,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (danny, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "danny_auto_chat",
    "label": "auto_chat",
    "girl": "danny",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(danny,
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
    "name": "danny_ask_out",
    "label": "ask_out",
    "girl": "danny",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("ask_date")),
            ),
        PersonTarget(danny,
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
    "name": "danny_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "danny",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(danny,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label danny_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = danny.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = danny.get_activity(bye_hour)
    if not activity == danny.activity:
        if day != game.week_day:
            $ danny.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ danny.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"danny {bye_outfit}")
        if activity["activity"] == "sleep":
            danny.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            danny.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            danny.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            danny.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            danny.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            danny.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            danny.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            danny.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            danny.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            danny.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            danny.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            danny.say "I'll go get dressed."
        hide danny
    return

label danny_cheated(action, cheat_npc=None):
    show danny
    if not danny.sub >= 75:
        show danny annoyed
        show fx anger
        $ loss = 5
        if danny.flags.boyfriend or danny.flags.fiance:
            $ loss += 5
        $ danny.love -= loss
        "I see Danny looking at me [action] someone else with a painful hurting face..."
    else:
        show fx heart
        $ danny.sub += 1
        "I see Danny looking at me [action] someone else with envy and lust in his eyes."
    hide danny
    return

label danny_kiss_female:
    scene expression f"bg {game.room}"
    if danny.love < 25 and not danny.is_boyfriend and not game.active_date.score >= 75:
        show danny
        "I've been teetering on the edge of doing this for what feels like forever."
        "But it's never felt as right as it does in this particular moment."
        "So I feel like I haven't got a choice other than to act on it straight away."
        "The next time Danny looks my way, I take a deep breath and lean in close."
        show danny at center, zoomAt(1.5, (640, 1040))
        "My lips must come within a fraction of an inch of his."
        "But then he pulls back, a look of confusion on his face."
        hide danny
        show danny annoyed
        with hpunch
        danny.say "Urgh..."
        danny.say "[hero.name]..."
        danny.say "Wadda yah doin?"
        bree.say "I..."
        bree.say "Erm..."
        bree.say "Nothing, Danny...nothing at all!"
        "Danny looks at me with suspicion in his eyes."
        hide danny with easeoutright
        "Then he shrugs and turns away."
        "Leaving me to curl up and die on the inside."
        if danny.love < 40:
            $ danny.sub += 1
        else:
            if randint(1, 2) == 1:
                $ danny.love -= 1
        hide danny
    elif not danny.flags.kiss:
        show danny
        "I know that I shouldn't be doing this, that it's a bad idea."
        "But every time the chance comes along to kiss Danny, I get butterflies!"
        "And I know that I can't keep avoiding it forever, or I'll go insane!"
        show danny at center, zoomAt(1.5, (640, 1040))
        "So this time, when he leans in close to say something to me, I go for it."
        hide danny
        show danny kiss
        with fade
        "I lean in close and press my lips against his!"
        "At first there's a sound from him that seems to be total surprise."
        "And for a moment I think he's going to pull away."
        "Or worse, push me away and ask me what the hell I think I'm doing."
        "But then I feel a chance in Danny."
        "Is he..."
        "Yes, he is!"
        "He's kissing me back!"
        "Pretty soon he's really leaning into it too."
        "Then tongues get involved, and it's pretty hot!"
        "Just like I hoped it would be."
        "Oh my god...I'm kissing the bad guy!"
        "And it feels SO good!"
        hide danny kiss
        $ danny.flags.kiss += 1
        $ danny.love += 5
    else:
        hide danny
        show danny kiss
        "Almost as soon as I've had that magical first kiss with Danny, the floodgates break."
        "And it's like a barrier has come down between us, one we'll never let go up again."
        "Now he seems to be revelling in the fact that he can lean over and kiss me whenever he wants."
        "And I know how bad this sounds, but I even sometimes come when he snaps his fingers too!"
        "Because I feel so naughty, running over to lock lips with my own real bad boy!"
        "Every kiss is as exciting for me as the first one was."
        "And I try to make them last as long too."
        "Why does he have that effect on me?"
        "It's like a drug that I'm totally addicted to."
        "Oh god..."
        "Just the thought of it makes me go weak at the knees!"
        hide danny kiss
        $ danny.flags.kiss += 1
        $ danny.love += 5
    return

label danny_beats_ryan_female:
label danny_beats_scottie_female:
label danny_beats_jack_female:
label danny_beats_shawn_female:
label danny_beats_mike_female:
    if randint(1, 100) <= 95:
        return "abort"
    if active_girl.id == "ryan":
        "I can feel Ryan's lips against mine, his hands all over me."
    elif active_girl.id == "jack":
        "Jack's kissing me with a passion, squeezing me tight."
    elif active_girl.id == "shawn":
        "Shawn has me in his arms, kissing me like crazy."
    elif active_girl.id == "mike":
        "[mike.name] pulls me closer, kissing me more intensely all the time."
    "I know that I should be stopping him, but it's so hard to resist!"
    danny.say "What the fuck!"
    danny.say "I said - WHAT THE FUCK!"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show danny angry at right5
    $ renpy.show(f"{active_girl.id} angry", at_list=[left5])
    if active_girl.id == "ryan":
        "At the sound of Danny's voice, Ryan releases me from his grip."
    else:
        "At the sound of Danny's voice, [active_girl.name] leaps away from me."
    "I gasp and look around to see him standing there, visibly seething."
    bree.say "Danny, I..."
    bree.say "I can explain..."
    bree.say "This isn't what it looks like!"
    "Danny shakes his head, cutting me off."
    "But all the time he's looking straight at [active_girl.name]."
    danny.say "Nah, [hero.name]..."
    danny.say "You don't got to explain nothin'!"
    danny.say "It's me that's gonna be doing the explaining here!"
    "I can't help gasping in surprise at Danny."
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
    "But for all the pleading, Danny's just not in the mood to listen."
    $ renpy.hide(f"{active_girl.id}")
    hide danny
    $ renpy.show(f"danny beats {active_girl.id}", at_list=[center, zoomAt(1.2, (740, 720))])
    with vpunch
    "He grabs his victim by the collar and gets straight to work."
    "And I do mean victim, not opponent!"
    "Because it's a pretty one-sided affair."
    "Danny punches, kicks and head-butts his way to a quick Vincenty."
    "And once [active_girl.name] falls to his knees, Danny grabs his throat with both hands."
    bree.say "Stop it, Danny!"
    bree.say "You're going to kill him!"
    danny.say "Don't worry, [hero.name] - I've done this a hundred times before."
    danny.say "I'm just putting this asshole to sleep, that's all!"
    "With that he lets go, allowing his supposed rival to slump to the ground."
    return

label danny_greet:
    if renpy.has_label(f"danny_greet_dialogues_{hero.gender}") and not danny.flags.greeted:
        scene expression f"bg {game.room}"
        $ danny.flags.greeted = TemporaryFlag(True, 1)
        show danny
        $ result = randint(1, 3)
        if result == 1:
            danny.say "Hello, [hero.name]."
        elif result == 2:
            danny.say "Hi, [hero.name]."
        elif result == 3:
            danny.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                danny.say "Good morning [hero.name]."
            elif game.hour < 19:
                danny.say "Good afternoon [hero.name]."
            else:
                danny.say "Good evening [hero.name]."
        call expression f"danny_greet_dialogues_{hero.gender}" from _call_expression_459
        hide danny
    return

label danny_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Danny."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Danny."
        elif game.hour < 12:
            bree.say "Good morning Danny."
        elif game.hour < 19:
            bree.say "Good afternoon Danny."
        else:
            bree.say "Good evening Danny."
    return


label danny_propose_female:
    if game.week_day % 2 == 0:
        show danny
        "I always kind of flattered myself into thinking that I was a sensible kind of girl."
        "Not straight-laced or a goodie-goodie kind of person, nothing boring like that."
        "More that I was smart and maybe even a little bit more clued-up than average."
        "I guess my dad being a cop was part of it, because on the one hand he was pretty strict."
        "But on the other he was keen to make sure I was street-wise enough to take care of myself."
        "So why did all of that go out the window the moment I started dating Danny?"
        "Urgh...he's the kind of guy that my dad wouldn't piss on if he was on fire!"
        "He's sleazy, disrespectful and probably into all kinds of illegal shit."
        "But there's just something about him that I can't resist."
        "Like he's catnip that only seems to work on me!"
        "And don't worry, I'm not convinced that I can straighten him out either."
        "I'm not one of those delusional girls that thinks she can change a guy like that."
        "On no, what I want more than anything is to jump onto his chopper."
        "And then ride away with him into the sunset!"
        "The problem is that I have no idea what he thinks about commitment."
        "I feel like the only thing that will make me happy is getting him to marry me."
        "But what if he just laughs in my face when I ask him?"
        "No...I can't let that kind of negative thinking stop me."
        "Because the only thing worse than him saying no would be never to ask at all."
        "That way I'm just asking to spend the rest of my life wondering what might have been."
        "So I resolve to face my fears and ask the question."
        "And if Danny does say no, then so be it."
        show danny at center, zoomAt(1.5, (640, 1040)) with fade
        "But even then, when the right moment seems to arrive, I almost choke."
        bree.say "D...Danny..."
        bree.say "I...erm..."
        bree.say "I..."
        "Danny frowns at me and shakes his head."
        show danny annoyed
        danny.say "Jesus Christ, [hero.name]..."
        danny.say "What in the hell's the matter with you?"
        danny.say "If you got something to say, then spit it out already."
        danny.say "Otherwise shut up and don't waste your breath!"
        "Oh great work, [hero.name]."
        "You didn't even pop the question yet."
        "And he's already getting pissed off!"
        show danny normal
        bree.say "Okay, okay..."
        bree.say "Danny, you know that I love you, right?"
        "Danny's face breaks into a cocky smile."
        "And he nods his head slowly while raising one eyebrow."
        danny.say "Oh, sure thing, babe..."
        danny.say "I know that!"
        bree.say "Well, I was thinking..."
        bree.say "How about we make it official?"
        show danny surprised
        bree.say "How about we get married?"
        if danny.love < 195:

            "Danny shakes his head almost as soon as I'm done talking."
            "And I can already feel my hopes fading as he does so."
            danny.say "Whoa!"
            show danny annoyed
            danny.say "No can do, [hero.name]."
            danny.say "That's not gonna happen."
            bree.say "But why, Danny?"
            bree.say "Don't you feel the same way about me that I do about you?"
            bree.say "Don't you love me?!?"
            show danny normal
            "Danny holds up his hands and waves them about."
            "Making a gesture for me to calm down."
            danny.say "What are you talking about, [hero.name]?"
            danny.say "Of course I do!"
            bree.say "Then why won't you marry me?!?"
            "I'm almost wailing as I demand an explanation from Danny."
            "But the one that I get from him stops me in my tracks."
            danny.say "Because I think I'm already married, [hero.name]."
            bree.say "You're serious?"
            danny.say "Oh yeah!"
            danny.say "I married some crooked broad a while back."
            danny.say "It was probably part of some scheme she had going on, you know?"
            bree.say "Erm..."
            bree.say "I'll take your word for it."
            danny.say "Anyway, I never got a divorce - so it'd be bigamy!"
            "I nod and begin to think of a way to change the subject."
            "Because this is definitely a rabbit-hole I don't want to go down."
            $ danny.love -= 25
        else:

            "Danny looks thoughtful for a moment."
            "And I'm sure that he's going to say no."
            "But then he surprised me by nodding."
            danny.say "Sure, [hero.name]..."
            show danny smile
            show fx heart
            danny.say "Why not!"
            bree.say "Really?"
            bree.say "I was sure you were going to say you were married to a life of crime."
            bree.say "Or something else like that, you know?"
            danny.say "Oh yeah, there is one thing..."
            danny.say "I married some crooked broad a while back."
            danny.say "It was probably part of some scheme she had going on, you know?"
            bree.say "Erm..."
            bree.say "I'll take your word for it."
            show danny sneaky
            danny.say "Anyway, I never got a divorce."
            danny.say "But it doesn't matter, because we didn't use our real names."
            danny.say "And she's probably dead by now anyway."
            show danny normal
            danny.say "So don't sweat it."
            "I nod and smile, trying to push all thoughts of Danny's former wife aside."
            "That and the notion of just how many other skeletons might be lurking in his closet too."
            "And instead I start thinking about the more appealing subject of planning our eventual wedding."
            $ danny.set_fiance()
        hide danny
    else:
        show danny
        "Part of me wonders why in the hell I'd even think of doing something like this."
        "I mean, Danny's the kind of guy that hangs around in sleazy bars with even sleazier people."
        "He looks, sounds and acts like the biggest bad guy you could imagine."
        "But somehow I'm still here, waiting for the chance to pop the question to him."
        "And by that I don't mean the kind of questions that he usually like to here."
        "Such as 'Would you like a beer, Danny'."
        "Or 'You want some of this hot ass, Danny?'."
        "This is more along the lines of 'Want to grow up and settle down, Danny?'."
        "So you can probably see why I'm more than a little worried."
        "But what can I do about it?"
        "I feel for a bad boy."
        "And now I want to put a ring on it to seal the deal."
        "So as soon as the chance presents itself, I gather all of my courage."
        "And I just decide to go for it."
        "Because the worst thing he can say is no."
        "That's the truth, right?"
        "Like, there's really nothing worse than he can say?"
        "Is there?"
        show danny at center, zoomAt(1.5, (640, 1040)) with fade
        bree.say "Danny..."
        show danny upset
        danny.say "Oh no!"
        danny.say "What did I do now?"
        bree.say "Huh?"
        bree.say "What are you talking about, Danny?"
        bree.say "You didn't do anything!"
        show danny surprised
        "Danny looks puzzled by this."
        danny.say "Are you sure, [hero.name]?"
        danny.say "Because when I have done something..."
        danny.say "That's the way someone always says my name, you know?"
        show danny normal
        danny.say "And well...I've usually done something."
        danny.say "Maybe not what they're mad about right there and then."
        danny.say "But something all the same!"
        "I shake my head, trying to dismiss what Danny just said."
        bree.say "No, Danny!"
        bree.say "I just want to ask you something, that's all."
        show danny smile
        danny.say "Oh, that's okay then - ask away!"
        bree.say "Okay, Danny..."
        bree.say "Here goes..."
        bree.say "Will you marry me?"
        show danny surprised
        "As soon as Danny hears my question, his eyes almost pop out of his head."
        if danny.love < 195:
            "But then something seems to dawn on Danny."
            "Because his expression changes completely."
            show danny smile
            danny.say "Ha!"
            danny.say "Good one, [hero.name]..."
            danny.say "You almost had me there!"
            danny.say "The idea of me getting married - I mean, what the fuck?!?"
            "I keep on staring at Danny as he comes out with all of this."
            "And I guess it must become more obvious that I'm not joking the more he goes on."
            show danny normal
            "Because by the time he's finished, Danny looks a lot less sure of himself."
            danny.say "Erm..."
            danny.say "You are joking, right?"
            bree.say "No, Danny..."
            bree.say "I kinda wasn't."
            bree.say "Sure wish I had been now though!"
            show danny annoyed
            danny.say "Ouch!"
            danny.say "That's kind of awkward..."
            show danny smile
            danny.say "For you, I mean!"
            hide danny with easeoutright
            "With that he laughs again and turns his back on me."
            "All of which leaves me wondering what the fuck too."
            "Like, why the fuck did I even bother?"
            $ danny.love -= 25
        else:
            "But then something seems to dawn on Danny."
            "Because his expression changes completely."
            show danny smile
            show fx heart
            danny.say "Yeah, [hero.name]..."
            danny.say "That sounds like a great idea!"
            "I nod and force a smile onto my face."
            "Not really hearing what Danny actually said."
            bree.say "It's okay, Danny..."
            bree.say "Probably a dumb idea on my part anyway!"
            bree.say "W...wait a minute..."
            bree.say "Did you actually say yes?!?"
            show danny surprised
            "Danny stares at me in a state of confusion."
            danny.say "Yes...I said yes."
            danny.say "Why?"
            danny.say "Was that the wrong answer?"
            danny.say "Or was it a trick question or something?"
            bree.say "No, no, no!"
            bree.say "That's the right answer!"
            show danny smile
            "I nod and smile, doing all I can to impress that fact on Danny."
            "But at the same time my head is kind of spinning too."
            "Because it's really happening - we're getting married!"
            $ danny.set_fiance()
    return

label danny_ask_date_female:



    call danny_ask_date_alone_female from _call_danny_ask_date_alone_female
    return _return


label danny_ask_date_alone_female:
    show danny
    "Danny and I have been hanging out a lot recently."
    "Sometimes with other people there, but more often just the two of us."
    "And I credit myself with being able to read how things are between us."
    "My gut tells me that it's not by chance either."
    "I feel there's something growing between us."
    "You know, that we're becoming more than friends?"
    "And I think it's fast approaching the time when one of us needs to admit as much."
    "To make the next move and progress our relationship to the place it should be going."
    "Which is all a long-winded way of saying that I'm going to ask Danny out on a date."
    "I know, I know..."
    "He looks more like the kind of guy you'd ask to a bar-room brawl!"
    "But that'd be judging a book by its cover."
    "Who knows, he might be a big softie at heart!"
    show danny at center, zoomAt(1.5, (640, 1040)) with fade
    "So as soon as the opportunity presents itself, I resolve to ask the question."
    bree.say "Erm..."
    bree.say "Danny?"
    danny.say "Huh?"
    danny.say "What's up, [hero.name]?"
    bree.say "Well...I was thinking..."
    bree.say "We're hanging out together a lot..."
    bree.say "So would you want to do it some time at a specific time and place?"
    show danny surprised
    "Danny looks puzzled for a moment."
    "He scratches his chin as he ponders my words."
    danny.say "Time and place...specific?"
    danny.say "Like a date?"
    bree.say "Yeah, Danny - just like that!"
    bree.say "So what do you say?"
    if danny.love < 50 or danny.flags.nodate:
        show danny normal
        "Danny chuckles and shakes his head."
        "Which makes me think I know what's coming next."
        danny.say "Why would we want to do that, [hero.name]?"
        danny.say "We're just buddies, right?"
        show danny smile
        danny.say "And buddies hang-out together."
        danny.say "They don't go on dates!"
        "Well, I guess that answers the question as to how Danny sees me!"
        "And if he thinks we're just friends, then he's just acting accordingly."
        "Sure, I feel kind of crushed by the revelation."
        "But now I have to at least try to save face."
        bree.say "Oh..."
        bree.say "Sure, Danny..."
        bree.say "You're probably right."
        bree.say "We're buddies, you and me..."
        bree.say "Just great buddies!"
        "Please, kill me now!"
        $ date_choice = False
    else:
        show danny psycho
        "Danny does this weird thing with his fingers."
        "Kind of steepling them and staring down at them too."
        "If I didn't know him better, I'd say he looked a little put out."
        danny.say "Oh...erm..."
        show danny smile
        danny.say "Well, yeah, [hero.name]..."
        danny.say "That'd be great!"
        "I wait for him to say more."
        "But when he doesn't, I feel the need to prod him along."
        bree.say "I get the feeling there's a but in there somewhere, Danny!"
        bree.say "Am I right?"
        show danny normal
        danny.say "Aw shucks, [hero.name]..."
        danny.say "It's just that...I was gonna ask you for a date!"
        show danny smile
        danny.say "I was all psyched up for it too."
        danny.say "Then you went and beat me to it!"
        "I kind of feel a mixture of amusement and relief."
        "Here's this big, tough guy and he's too bashful to ask me out on a date!"
        "But I'm relieved that we're kind of on the same page too."
        bree.say "Well, I say we focus on the positives, Danny."
        bree.say "We both want to go on a date."
        bree.say "So let's go on a date."
        "Danny nods and smiles, relief showing on his face too."
        $ date_choice = True
    return date_choice

label danny_pregnancy_congratulations:
    show danny sneaky
    "Danny walks straight up to me, clapping his hands together."
    "And I can see that he has a lascivious look in his eye too."
    show danny smile
    danny.say "Ho, ho, ho..."
    danny.say "Somebody's been having some serious fun!"
    danny.say "How come I wasn't in on it too?"
    "I can feel myself blushing at the way Danny's talking to me."
    "And I can't keep from cradling my belly in a protective manner."
    "But he's also making me more than a little annoyed too."
    bree.say "Don't you have any respect, Danny?"
    bree.say "Here I am, about to be a mom."
    bree.say "And you're talking to me like that!"
    "Danny lets out typically filthy chuckle."
    "But I note that he also holds up his hands."
    "And he backs off a little too."
    show danny scared
    danny.say "Heh..."
    danny.say "Relax, [hero.name] - I was just kidding around."
    show danny normal
    danny.say "Phew...those hormones must be kicking in right about now, yeah?"
    show danny smile
    danny.say "Well don't worry, I'm sure you'll do fine."
    danny.say "In fact, If I ever accidentally fathered a kid..."
    danny.say "I'd hope the girl was one like you!"
    bree.say "Erm..."
    bree.say "Thanks, Danny..."
    bree.say "I think!"
    $ danny.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
