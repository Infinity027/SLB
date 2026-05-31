init python:
    Event(**{
    "name": "ryan_auto_greet",
    "label": "auto_greet",
    "girl": "ryan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(ryan,
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
    "name": "ryan_give_phone_number",
    "label": "give_phone_number",
    "girl": "ryan",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(ryan,
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
    "name": "ryan_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(ryan,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "ryan",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "ryan_are_you_sick",
    "label": "are_you_sick",
    "girl": "ryan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(ryan,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (ryan, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "ryan_auto_chat",
    "label": "auto_chat",
    "girl": "ryan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(ryan,
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
    "name": "ryan_ask_out",
    "label": "ask_out",
    "girl": "ryan",
    "priority": 100,
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(ryan,
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
    "name": "ryan_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "ryan",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(ryan,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "ryan_kiss_me_female",
    "label": "ryan_kiss_me_female",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(ryan,
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

label ryan_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = ryan.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = ryan.get_activity(bye_hour)
    if not activity == ryan.activity:
        if day != game.week_day:
            $ ryan.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ ryan.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"ryan {bye_outfit}")
        if activity["activity"] == "sleep":
            ryan.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            ryan.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            ryan.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            ryan.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            ryan.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            ryan.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            ryan.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            ryan.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            ryan.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            ryan.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            ryan.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            ryan.say "I'll go get dressed."
        hide ryan
    return

label ryan_cheated(action, cheat_npc=None):
    show ryan
    if not ryan.sub >= 75:
        show ryan angry
        show fx anger
        $ loss = 5
        if ryan.flags.boyfriend or ryan.flags.fiance:
            $ loss += 5
        $ ryan.love -= loss
        "I see Ryan looking at me [action] someone else with a painful hurting face..."
    else:
        show fx heart
        $ ryan.sub += 1
        "I see Ryan looking at me [action] someone else with envy and lust in his eyes."
    hide ryan
    return

label ryan_greet:
    if renpy.has_label(f"ryan_greet_dialogues_{hero.gender}") and not ryan.flags.greeted:
        scene expression f"bg {game.room}"
        $ ryan.flags.greeted = TemporaryFlag(True, 1)
        show ryan
        $ result = randint(1, 3)
        if result == 1:
            ryan.say "Hello, [hero.name]."
        elif result == 2:
            ryan.say "Hi, [hero.name]."
        elif result == 3:
            ryan.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                ryan.say "Good morning [hero.name]."
            elif game.hour < 19:
                ryan.say "Good afternoon [hero.name]."
            else:
                ryan.say "Good evening [hero.name]."
        call expression f"ryan_greet_dialogues_{hero.gender}" from _call_expression_462
        hide ryan
    return

label ryan_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Ryan."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Ryan."
        elif game.hour < 12:
            bree.say "Good morning Ryan."
        elif game.hour < 19:
            bree.say "Good afternoon Ryan."
        else:
            bree.say "Good evening Ryan."
    return

label ryan_pregnancy_congratulations:
    show ryan
    "As soon as I see Ryan, I notice the smug grin on his face."
    "At first I think he's going to brag about something."
    "Because let's face it, that's usually his thing!"
    "But then he makes a point of looking down at my belly."
    ryan.say "Looks like my sources were correct!"
    ryan.say "Congratulations, [hero.name]..."
    ryan.say "You're practically glowing!"
    "I smile and nod, trying to be nice to Ryan."
    "Sure, he can be an unctuous prick most of the time."
    "But he is trying to be nice."
    "Or at least what passes for nice in his mind."
    bree.say "Thank you, Ryan."
    bree.say "I'm kind of excited and scared in equal measures!"
    ryan.say "Well, you would be, [hero.name]!"
    ryan.say "Me, I've had it all planned out for years."
    ryan.say "But not many people are as prepared as I am!"
    "Amazing, just bloody amazing!"
    "I'm the one standing here expecting a baby."
    "And this guy still finds a way to make it all about him!"
    bree.say "Yeah..."
    bree.say "Thanks for that, Ryan!"
    $ ryan.love += 1
    return

label ryan_kiss_female:
    scene expression f"bg {game.room}"
    if ryan.love < 25 and not ryan.is_boyfriend and not game.active_date.score >= 75:
        show ryan
        "I keep looking at Ryan when I think I can get away with it."
        "And every time he turns to look at me I turn my head away."
        "Right up until the moment that I can't bear to do it any longer."
        "That's when I finally have to make my move."
        "Either that, or I swear that I'll explode!"
        "This time, when Ryan turns to look at me, I lean in closer."
        show ryan annoyed at center, zoomAt (1.5, (640, 1040)) with hpunch
        "Only to find his hand in then way of my lips!"
        "I pull back, almost too confused to actually speak."
        bree.say "Wha..."
        bree.say "What happened?!?"
        show ryan smile
        "Ryan chuckles and shakes his head."
        "A look of arrogant superiority on his face."
        ryan.say "Oh dear!"
        ryan.say "Looks like someone's being a little presumptuous."
        ryan.say "I mean, I can't blame you for wanting to kiss me, [hero.name]."
        ryan.say "But I do have a say in it too!"
        "I can feel my cheeks flushing with colour."
        "And right now, I wish the ground would open and swallow me up!"
        $ ryan.love -= 5
        $ ryan.sub -= 5
        hide ryan with fade
    elif not ryan.flags.kiss:
        show ryan
        "I keep looking at Ryan when I think I can get away with it."
        "And every time he turns to look at me I turn my head away."
        "Right up until the moment that I can't bear to do it any longer."
        "That's when I finally have to make my move."
        "Either that, or I swear that I'll explode!"
        show ryan at center, traveling (1.5, 0.5, (640, 1040))
        "This time, when Ryan turns to look at me, I lean in closer."
        hide ryan
        show ryan kiss
        with fade
        "A moment later I feel out lips meet."
        "And before I know it, the thing is actually happening!"
        "I'm kissing Ryan, and he's kissing me back."
        "The whole thing seems like a surprise on one level."
        "But on another it feels like the most natural thing in the world."
        "And as it goes on, that feeling just becomes ever more real."
        "Soon I can't believe that I was ever nervous about trying this."
        "Ryan seems to be of the same persuasion too."
        "As he doesn't appear to be keen on ending the kiss anytime soon."
        "Which is fine with me."
        "I've waited so long for it to happen, I could keep going until I pass out!"
        hide ryan with fade
        $ ryan.flags.kiss += 1
    else:
        hide ryan
        show ryan kiss
        with fade
        "I can't honestly believe that I was ever so nervous about kissing Ryan."
        "Because now that line's been crossed, it seems to get easier every time."
        "In fact, I find that I have to stop myself from doing it too often!"
        "Not that Ryan does anything to discourage me from indulging myself."
        "He seems perfectly happy to press lips with me whenever the whim arises."
        "So much so that I start to get worried people will begin to stare."
        "But all the same, that fear is always outweighed by my desire to kiss him."
        "And what do I care about the people watching us?"
        "They're probably just jealous of us anyway!"
        "After all, I waited for this long enough, didn't I?"
        "I think I deserve a reward for being so patient."
        "Which is why I take every chance that comes along to kiss Ryan."
        "Feeling more passion and desire for him each and every time."
        hide ryan with fade
        $ ryan.love += 2
        $ ryan.flags.kiss += 1
    return

label ryan_kiss_me_female:
    show ryan
    "I'm just minding my own business, thinking about something and nothing."
    "Then I happen to catch something moving in the corner of my eye."
    show ryan at center, traveling (1.5, 0.5, (640, 1040))
    "That makes me turn my head without a conscious thought."
    "And much to my surprise, I find myself eye-to-eye with Ryan."
    hide ryan
    show ryan kiss
    with fade
    $ ryan.flags.kiss += 1
    "Before I can even react, he presses his lips against mine."
    "And just like that, we're kissing!"
    "My mind is suddenly racing, trying to make sense of it all."
    "But it doesn't take long for my body to take over."
    "I lean into the kiss."
    "Returning it with as much passion as Ryan is putting into it."
    "And that's when I know there's no chance of me breaking it off."
    "A moment ago I had no idea that this was going to happen."
    "Hell, I had no idea if I wanted it to happen or not!"
    "But now I'm becoming more committed to it with each passing second."
    "I don't know what inspired Ryan to do it."
    "There's no way that I can read his mind to find out."
    "But I'm doing all I can to show him that I want it too."
    "And I think that he's getting the message!"
    hide ryan with fade
    return

label ryan_ask_date_female:



    call ryan_ask_date_alone_female from _call_ryan_ask_date_alone_female
    return _return

label ryan_ask_date_alone_female:
    if not ryan.flags.hadadate:
        show ryan
        "I feel like things between Ryan and I have been going in the right direction recently."
        "We're getting on like a proverbial house on fire, and spending a lot of time together too."
        "So this feels like the right point in our relationship to take things a step further."
        "Or at least is does to me!"
        "The moment I even start thinking about asking Ryan to go on a real date, the nerves set in."
        "I mean, what if I'm wrong and he's not on the same page as I am right now?"
        "That could lead to be making a massive error in asking him out."
        "Hell, it could even make him rethink the whole thing!"
        "But then he might be right where I think we are in terms of our relationship."
        "Even worse, he might be waiting for me to make the first move!"
        "In the end I decide that I have to go ahead and do it, regardless of the outcome."
        "Because not knowing would be worse than finding out it's bad news, right?"
        show ryan at center, zoomAt (1.5, (640, 1040)) with fade
        "So here goes nothing..."
        bree.say "Ryan..."
        bree.say "I have something I want to ask you..."
        "Ryan looks up, interest evident in his eyes."
        ryan.say "Hmm..."
        ryan.say "You want to ask me something, [hero.name]?"
        ryan.say "Then ask away - I'd love to hear it!"
        bree.say "Well, I was thinking..."
        bree.say "We're good friends."
        bree.say "Maybe more than good friends..."
        bree.say "So how about we make it formal?"
        bree.say "You know, go on an official date?"
    else:
        bree.say "Hey Ryan, wanna date?"
        bree.say "Just you and me... You know it's your destiny?"
    if ryan.love < 50 or ryan.flags.nodate:
        if not ryan.flags.hadadate:
            show ryan annoyed
            "I see a frown spread across Ryan's face."
            "And the sight of it makes my mood sink."
            ryan.say "Urgh..."
            ryan.say "I was having such a good time hanging-out with you, [hero.name]."
            ryan.say "I really wish you hadn't brought that up!"
            "I shake my head as Ryan says all of this."
            "Trying as best I can to back-peddle in the idea."
            bree.say "It doesn't have to be an actual date, Ryan!"
            bree.say "We can call it something else, yeah?"
            bree.say "That'd work for me!"
            "Ryan lets out a sigh and then shakes his own head."
            ryan.say "No, [hero.name]..."
            ryan.say "It's out there now, it's been said."
            ryan.say "You want to start dating, and I'm just not ready for that."
            ryan.say "It's clear to me now that we both want very different things."
            ryan.say "Now I'm going to have to re-evaluate our entire friendship."
            "I open my mouth to say more."
            "But Ryan holds up his hand to cut me off."
            "So it seems like the discussion is over."
            hide ryan with fade
        else:
            show ryan annoyed
            ryan.say "Sorry [hero.name], maybe another time."
            hide ryan with fade
        $ date_choice = False
    else:
        if not ryan.flags.hadadate:
            show ryan annoyed
            "Ryan looks thoughtful for a moment."
            "And I find myself staring at him intently, wondering where this is going."
            show ryan smile
            "But then his expression lightens and he nods his head."
            ryan.say "That's a great idea, [hero.name]."
            ryan.say "In fact, I'm amazed I didn't think of it myself!"
            bree.say "You really mean that, Ryan?"
            bree.say "You want to start dating me?"
            ryan.say "Of course I do."
            ryan.say "I wouldn't have said it if I didn't meant it!"
            "I can't keep a smile off my face."
            "But the truth is that I'm feeling more than a little overwhelmed."
            "And that's because of the relief I can feel flooding my insides."
            bree.say "That's great, Ryan!"
            bree.say "Because I was worried that you weren't ready for it."
            bree.say "Or that we weren't on the same page yet."
            bree.say "Or that..."
            "I stop myself as I realise that I'm beginning to babble."
            "And then I make an effort to pull myself together."
            bree.say "Ahem..."
            bree.say "What I mean to say is - that's great news!"
            hide ryan with fade
            $ ryan.flags.hadadate = True
        else:
            show ryan smile
            ryan.say "Of course I do."
            hide ryan with fade
        $ date_choice = True
    return date_choice

label ryan_propose_female:
    show ryan
    if randint(1, 2) == 2:
        "Ryan and I have been dating for a while now, and things have been going great."
        "I feel like every time we go out together, we're taking a big step forwards."
        "And obviously that also means that we're getting ever closer to the next stage of our relationship."
        "The logical thing for us is to get engaged, right?"
        "But the problem is that Ryan doesn't seem to be about to pop the question."
        "I'm pretty sure that's because he's just waiting for the exact right moment to do it."
        "Or else there's some other perfectly legitimate reason that he's putting it off."
        "The problem is that I can't just come right out and ask him what that could be."
        "So after having a long, hard think about it, I've come up with a solution."
        "I'm going to come right out and ask him to marry me."
        "I suppose I'm really going to be doing him a massive favour."
        "Because I understand the pressure this kind of thing must be putting on him."
        "So by taking it out of his hands, I'm also releasing all of that pressure, right?"
        "He's obviously going to be delighted with that, isn't he?"
        show ryan at center, zoomAt (1.5, (640, 1050)) with fade
        "So as soon as the right opportunity presents itself, I make my move."
        bree.say "Ryan..."
        show ryan smile
        ryan.say "Oh..."
        ryan.say "Yeah, [hero.name]?"
        show ryan normal
        bree.say "There's something I wanted to ask you."
        show ryan smile
        ryan.say "Okay, [hero.name]..."
        ryan.say "I'm listening."
        show ryan normal
        bree.say "It's something really important, yeah?"
        bree.say "Something that I've wanted to ask you for a long time."
        show ryan smile
        ryan.say "Like I said, [hero.name], that's fine."
        ryan.say "Ask away!"
        show ryan normal
        "I nod and take a deep breath."
        bree.say "Ryan, I think we need to take things to the next level."
        bree.say "Like, we're at a stage in our relationship where commitment is important..."
        "Ryan's nodding patiently as I say all of this."
        "But I realise that I'm not getting to the point."
        "So I just come out with it."
        bree.say "Ryan..."
        bree.say "Will you marry me?"
        if ryan.love < 195:
            show ryan annoyed
            "The moment I ask the question, Ryan starts to shake his head."
            show ryan annoyed at center, traveling(1.25, 0.5, (640, 900))
            "And he even backs away from me too, like he's physically repulsed!"
            show ryan whining
            ryan.say "Oh no!"
            ryan.say "No way, [hero.name]!"
            ryan.say "You could literally have asked me for anything else..."
            ryan.say "And I'd have said yes without hesitation."
            ryan.say "But not that!"
            show ryan sad
            "I'm more than a little shocked to hear Ryan say no."
            "And in addition, to be saying it in such strong terms too."
            bree.say "But why, Ryan?"
            bree.say "I thought we were getting on so well?"
            show ryan whining
            ryan.say "We were, [hero.name]..."
            ryan.say "But that was while things were casual."
            ryan.say "While we were dating and there were no strings attached."
            ryan.say "I already got married and divorced once."
            ryan.say "I don't want to start down that path all over again!"
            show ryan sad
            "I can only nod and bite my lip."
            "Because Ryan's got a pretty good point."
            "His last marriage ended in a really messy way."
            "Why didn't I think of that?"
            "I guess I was just blinded by my own desires."
            "And I'll have to learn to be more sensitive in future."
            $ ryan.love -= 25
        else:
            show ryan blank
            "Ryan looks taken aback by the question, like he didn't see it coming."
            "And that makes me worry that he's going to say on sheer instinct alone."
            show ryan smile
            "But then the expression on his face changes, and I see him smile."
            ryan.say "That's a great idea, [hero.name]."
            ryan.say "Why didn't I think of that myself?"
            show ryan normal
            "For a moment I can't quite take in what Ryan just said."
            "So I end up staring at him in stunned silence until it sinks in."
            "And even then I can't quite believe it."
            bree.say "Wait..."
            bree.say "Did you just..."
            bree.say "Did you just say yes?"
            "Ryan nods."
            show ryan smile
            ryan.say "I sure did, [hero.name]."
            ryan.say "I mean, I know that I was married and divorced before."
            ryan.say "But that doesn't mean I can't do it again."
            ryan.say "And better this time!"
            show ryan normal
            "Now I'm nodding too, even more eagerly than Ryan."
            "And I know that I should really be saying something."
            "But that's all I can manage right now."
            "Because my mind is too full of ideas and plans."
            "We're getting married - it's really happening!"
            $ ryan.set_fiance()
    else:
        "I feel like Ryan and I have been together for long enough that this thing is real, you know?"
        "Like, we've gone way beyond the stage of sneaking around behind certain people's backs."
        "Then we endured all of the faux outrage that we dared to admit our feelings for each other."
        "And now we're through all that, starting to create the relationship that we want to have."
        "So what better way to cement all of that than with a spontaneous proposal?"
        "I went out and found a ring, which I have stashed in my pocket."
        "I've rehearsed what I'm going to say a hundred times in my head."
        "And now I'm just waiting for the right moment to pop the question."
        "The only problem is that it seems my nerves are getting the better of me."
        show ryan at center, zoomAt (1.5, (640, 1050)) with fade
        "Because Ryan's giving me one of those funny looks right now."
        show ryan smile
        if ryan.sub >= 50:
            ryan.say "[hero.name], are you feeling okay?"
        elif ryan.sub <= -50:
            ryan.say "What's the matter, [hero.name]?"
        else:
            ryan.say "Penny for your thoughts, [hero.name]?"
        show ryan normal
        "Suddenly spurred on by the attention, I leap into action."
        "Without a conscious thought, I pull the ring out of my pocket."
        "And then I hold it up for Ryan to see, half going down on one knee."
        "The problem is that I don't know if I should be kneeling or not."
        "So instead I end up doing a weird kind of crouch in front of him."
        if hero.morality >= 25:
            bree.say "Ryan, will you marry me...please?"
        elif hero.morality <= -25:
            bree.say "How about it, big boy - wanna get wed?"
        else:
            bree.say "Hey, Ryan - will you do me the honour?"
        if ryan.love >= 195:
            show ryan blank
            "For all of his usual arrogance and swagger, Ryan seems genuinely stunned."
            "He stares at the ring for almost a minute in complete silence."
            "Which means that I'm left there, holding it and waiting for an answer."
            "And it feels like I'm going to have to prod him if I want one."
            "But then, to my great relief, Ryan seems to snap out of it."
            show ryan smile
            if ryan.sub >= 50:
                ryan.say "Oh wow, [hero.name]..."
                ryan.say "Of course I'll marry you!"
            elif ryan.sub <= -50:
                ryan.say "You know what, [hero.name], I was about to ask you the same thing."
                ryan.say "So you kind of answered my question with your's!"
            else:
                ryan.say "You really caught me off-guard there, [hero.name]..."
                ryan.say "But yeah, I'd love to marry you!"
            show ryan normal
            "My head is spinning as Ryan offers me his hand."
            "And it's all that I can do to push the ring onto his finger."
            "Part of me is still struggling to believe that he actually said yes."
            "And I think it's going to take a while for me to really believe it."
            "But there's the ring, sitting on the guy's finger."
            "That should be all the proof I need that this is for real."
            $ ryan.set_fiance()
        else:
            show ryan blank
            "For all of his usual arrogance and swagger, Ryan seems genuinely stunned."
            "He stares at the ring for almost a minute in complete silence."
            "Which means that I'm left there, holding it and waiting for an answer."
            "And it feels like I'm going to have to prod him if I want one."
            "But then, to my great relief, Ryan seems to snap out of it."
            show ryan whining
            if ryan.sub >= 50:
                ryan.say "Oh wow, [hero.name]..."
                ryan.say "I'm not ready for that kind of commitment!"
            elif ryan.sub <= -50:
                ryan.say "I think I should be the one to ask that question, [hero.name]."
                ryan.say "And don't worry, I'll let you know when the time comes."
            else:
                ryan.say "Don't get me wrong, [hero.name] - I'm totally into you."
                ryan.say "I just don't think we're quite there yet."
            show ryan sad
            "I feel like I've suddenly been struck dumb by the answer."
            "And I don't know if I could get the words out if I tried."
            "But as it is, all I can do is push the ring back into my pocket."
            "All the time feeling like I want the ground to open and swallow me up."
            "Because I really wonder if I'll ever be able to find the courage to do that again."
            "The effort took everything out of me, and now I just feel like giving up."
    hide ryan with fade
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
