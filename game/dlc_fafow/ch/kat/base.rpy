init python:
    Event(**{
    "name": "kat_give_phone_number",
    "label": "give_phone_number",
    "girl": "kat",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(kat,
            Not(IsHidden()),
            IsPresent(),
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
    "name": "kat_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "kat",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(kat,
            Not(IsHidden()),
            Not(IsPresent()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kat_auto_greet",
    "label": "auto_greet",
    "girl": "kat",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(kat,
            Not(IsHidden()),
            IsPresent(),
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
    "name": "kat_auto_chat",
    "label": "auto_chat",
    "girl": "kat",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kat,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "kat_are_you_sick",
    "label": "are_you_sick",
    "girl": "kat",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(kat,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (kat, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kat_ask_out",
    "label": "ask_out",
    "girl": "kat",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(kat,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            IsFlag("schedule", "default"),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "kat_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "kat",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(kat,
            Not(IsHidden()),
            IsPresent(),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label kat_greet:
    if renpy.has_label(f"kat_greet_dialogues_{hero.gender}") and not kat.flags.greeted:
        scene expression f"bg {game.room}"
        show kat
        $ kat.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            kat.say "Hello, [hero.name]."
        elif result ==2:
            kat.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                kat.say "Good morning [hero.name]."
            elif game.hour < 19:
                kat.say "Good afternoon [hero.name]."
            else:
                kat.say "Good evening [hero.name]."
        call expression f"kat_greet_dialogues_{hero.gender}" from _call_expression_456
        hide kat
    return

label kat_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Kat."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Kat."
        elif game.hour < 12:
            mike.say "Good morning Kat."
        elif game.hour < 19:
            mike.say "Good afternoon Kat."
        else:
            mike.say "Good evening Kat."
    return

label kat_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Kat."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Kat."
        elif game.hour < 12:
            bree.say "Good morning Kat."
        elif game.hour < 19:
            bree.say "Good afternoon Kat."
        else:
            bree.say "Good evening Kat."
    return

label kat_bye(bye_outfit=None):
    call npc_bye_outfit (npc=kat, bye_outfit=bye_outfit) from _call_npc_bye_outfit_23
    $ (day, h, activity, bye_outfit) = _return
    if not activity == kat.activity:
        if day != game.week_day:
            $ kat.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ kat.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"kat {bye_outfit}")
        if activity["activity"] == "sleep":
            kat.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            kat.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            kat.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            kat.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            kat.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            kat.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            kat.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            kat.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            kat.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            kat.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            kat.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            kat.say "I'll go get dressed."
        hide kat
    return

label kat_kiss:
    scene expression f"bg {game.room}"
    show kat
    "I keep trying to stop myself, but the urge is just too great."
    "I can't help licking my lips every time I steal a glance at Kat."
    "She just looks SO good to me, I can't contain my need for her!"
    "That's why I can feel myself already beginning to make a move."
    "The urge to kiss her is even stronger!"
    "I don't know if she's feeling the same way as me right now."
    "But I guess I'm about to find out."
    show kat at center, zoomAt(1.5, (640, 1040))
    "As the moment I begin to lean in for the kiss, Kat moves too."
    "She turns her head to face me just at the right time."
    "This is perfect!"
    if kat.love + hero.charm < 80 and not kat.is_girlfriend and not game.active_date.score >= 75:
        show kat annoyed
        "Or at least it would be, if she didn't have a look of annoyance on her face!"
        show kat at startle
        "Kat leans back as I lean forwards, leaving me to overshoot the mark."
        "Add to that the fact that my lips are all puckered up, and I look a total ass!"
        show kat confused
        kat.say "[hero.name]!"
        kat.say "What are you doing?"
        if hero.is_female:
            bree.say "I..."
            bree.say "I was going to kiss you, I guess?"
        else:
            mike.say "I..."
            mike.say "I was going to kiss you, I guess?"
        kat.say "Did I ask you to kiss me?"
        if hero.is_female:
            bree.say "Erm...no."
        else:
            mike.say "Erm...no."
        show kat angry
        kat.say "Then don't try to kiss me!"
        if hero.is_female:
            bree.say "Okay, okay - I'm sorry!"
        else:
            mike.say "Okay, okay - I'm sorry!"
        $ kat.love -= 1
        hide kat
    elif not kat.flags.kiss:
        show kat surprised
        "Kat has a look of surprise on her face."
        "But she makes no effort to pull away from me."
        hide kat
        show kat kiss
        with dissolve
        $ kat.love += 5
        $ kat.flags.kiss += 1
        if kat.lesbian > MAX_LES_GUY_SEX:
            $ kat.lesbian -= 1
        "In fact, she actually begins to lean into the kiss!"
        "Within seconds, things start to escalate."
        "And before long, there are even tongues involved too!"
        "Everything seems to fall into place as we kiss."
        "I swear I can feel the tension flowing out of Kat's body."
        "And I know that the same thing is happening to me too."
        "Questions are being answered and fears assuaged."
        "And neither of us is saying a single word."
        hide kat kiss
    else:
        show kat surprised at startle
        "Kat jumps a little in surprise."
        hide kat
        show kat kiss
        $ kat.flags.kiss += 1
        if kat.lesbian > MAX_LES_GUY_SEX:
            $ kat.lesbian -= 1
        "But then she giggles and leans into the kiss."
        "It feels like every time we do this it gets a little better."
        "A little more natural and a little more instinctive."
        "But I guess that's just a consequence of us getting to know each other."
        "That and our relationship maturing into something more special."
        hide kat kiss
        $ kat.love += 2
    return

label kat_sleep_date_fuck(location="hero"):
    show cuddle kat
    "The both of us are asleep before we can even consider cleaning up."
    call sleep ("kat") from _call_sleep_70
    $ game.room = "bedroom1"
    return

label kat_cheated(action, cheat_npc=None):
    if cheat_npc and Harem.together(cheat_npc, kat):
        show kat smile
        kat.say "Aren't you forgetting something?"
        show kat
        "And without warning Kat kisses me."
        $ kat.love += 1
        $ kat.flags.kiss += 1
    else:
        show kat angry
        kat.say "[hero.name], what are you doing - you're supposed to be with me, not her!"
    return

label kat_propose_male:
    if jack.flags.trouple_wedding:
        call kat_jack_propose_male from _call_kat_jack_propose_male
        return
    show kat
    "I have no idea what Kat's opinions on this kind of thing are."
    "I've never heard her say that she's for traditional forms of commitment."
    "But then I've never heard her say that she believes in free-love either!"
    "So that leaves me with the choice of either asking her what she wants."
    "Or else taking a more traditional, but equally risky course of action."
    "And in this case, it's the latter that I've chosen."
    "So here I am, armed with a ring in my pocket."
    "And looking for the perfect moment to get down on one knee."
    show kat smile at center, zoomAt(1.5, (640, 1040))
    "The problem is that Kat keeps giving me these funny looks."
    "I know that she's a pretty perceptive person."
    "Plus she can be very paranoid at times."
    "So I'm starting to worry that she's onto me!"
    "That's more than enough to force my hand."
    "And I find myself going down on one knee a moment later."
    "All out of fear that she's going to stop me before I can make a romantic gesture!"
    show kat confused
    kat.say "Wha..."
    kat.say "What are you..."
    mike.say "Kat..."
    mike.say "Will you marry me?"
    show kat surprised at startle
    "If I wanted something to stop Kat in her tracks, that certainly fits the bill."
    "She stares in amazement at the ring in my outstretched hand."
    "Now all I can do is wait for her to regain the power of speech!"
    if kat.love >= 195:
        "Kat seems to blink and then gasp."
        "And those signal her coming back to her senses."
        kat.say "You..."
        kat.say "You want me to marry you?!?"
        "I force a smile onto my face."
        "Doing the best I can to keep it from becoming a rictus."
        "And I add a nod, just for good measure."
        "This seems to be all Kat needs."
        show kat blush
        kat.say "Oh..."
        kat.say "Oh wow!"
        show kat happy
        kat.say "YES!"
        kat.say "Yes, I'll marry you!"
        "Kat thrusts her hand out towards me."
        "And it's all that I can do to fumble the ring onto her finger."
        show kat shy
        "Getting to my feet, I realise that we both look nervous as hell."
        "Like we can't actually believe this is happening."
        mike.say "Phew..."
        mike.say "I was worried you were going to say no!"
        show kat smile
        kat.say "More like I was worried you'd never ask!"
        show kat happy at startle
        "That leaves both of us laughing and shaking our heads."
        "But at least we know that we're on the same page now."
        $ kat.set_fiance()
    else:
        "Kat seems to blink and then gasp."
        "And those signal her coming back to her senses."
        kat.say "You..."
        kat.say "You want me to marry you?!?"
        "I force a smile onto my face."
        "Doing the best I can to keep it from becoming a rictus."
        mike.say "Erm..."
        mike.say "I'm on one knee, holding a ring..."
        mike.say "And I just asked that very question."
        mike.say "So I don't know what else I could be doing!"
        show kat confused
        "Kat frowns at my flippant answer."
        "And she crosses her arms over her chest."
        "Neither of which are good signs."
        $ kat.love -= 25
        $ kat.sub -= 25
        kat.say "You think it's funny?"
        mike.say "No, I hoped it was romantic."
        show kat angry
        kat.say "Well it certainly doesn't feel that way!"
        kat.say "And I don't appreciate being put on the spot either."
        show kat blush
        kat.say "People are staring at us!"
        show kat sad
        "I look around and see that she's right."
        "My cheeks burning, I shove the ring back into my pocket."
        "And then I get back to my feet."
        "I don't know what this means for Kat and me in going forwards."
        "But I do know that it's making me seethe with frustration right now."
    hide kat
    return

label kat_propose_female:
    show kat
    "I have no idea what Kat's opinions on this kind of thing are."
    "I've never heard her say that she's for traditional forms of commitment."
    "But then I've never heard her say that she believes in free-love either!"
    "So that leaves me with the choice of either asking her what she wants."
    "Or else taking a more traditional, but equally risky course of action."
    "And in this case, it's the latter that I've chosen."
    "So here I am, armed with a ring in my pocket."
    "And looking for the perfect moment to get down on one knee."
    show kat smile at center, zoomAt(1.5, (640, 1040))
    "The problem is that Kat keeps giving me these funny looks."
    "I know that she's a pretty perceptive person."
    "Plus she can be very paranoid at times."
    "So I'm starting to worry that she's onto me!"
    "That's more than enough to force my hand."
    "And I find myself going down on one knee a moment later."
    "All out of fear that she's going to stop me before I can make a romantic gesture!"
    show kat confused
    kat.say "Wha..."
    kat.say "What are you..."
    bree.say "Kat..."
    bree.say "Will you marry me?"
    show kat stuned at startle
    "If I wanted something to stop Kat in her tracks, that certainly fits the bill."
    "She stares in amazement at the ring in my outstretched hand."
    "Now all I can do is wait for her to regain the power of speech!"
    if kat.love >= 195:
        "Kat seems to blink and then gasp."
        "And those signal her coming back to her senses."
        show kat shocked
        kat.say "You..."
        kat.say "You want me to marry you?!?"
        show kat stuned
        "I force a smile onto my face."
        "Doing the best I can to keep it from becoming a rictus."
        "And I add a nod, just for good measure."
        "This seems to be all Kat needs."
        show kat blush
        kat.say "Oh..."
        kat.say "Oh wow!"
        show kat happy
        kat.say "YES!"
        kat.say "Yes, I'll marry you!"
        show kat smile
        "Kat thrusts her hand out towards me."
        "And it's all that I can do to fumble the ring onto her finger."
        show kat shy
        "Getting to my feet, I realise that we both look nervous as hell."
        "Like we can't actually believe this is happening."
        bree.say "Phew..."
        bree.say "I was worried you were going to say no!"
        show kat smile
        kat.say "More like I was worried you'd never ask!"
        show kat happy at startle
        "That leaves both of us laughing and shaking our heads."
        "But at least we know that we're on the same page now."
        $ kat.set_fiance()
    else:
        "Kat seems to blink and then gasp."
        "And those signal her coming back to her senses."
        show kat shocked
        kat.say "You..."
        kat.say "You want me to marry you?!?"
        show kat stuned
        "I force a smile onto my face."
        "Doing the best I can to keep it from becoming a rictus."
        bree.say "Erm..."
        bree.say "I'm on one knee, holding a ring..."
        bree.say "And I just asked that very question."
        bree.say "So I don't know what else I could be doing!"
        show kat confused
        "Kat frowns at my flippant answer."
        "And she crosses her arms over her chest."
        "Neither of which are good signs."
        $ kat.love -= 25
        $ kat.sub -= 25
        kat.say "You think it's funny?"
        bree.say "No, I hoped it was romantic."
        show kat angry
        kat.say "Well it certainly doesn't feel that way!"
        kat.say "And I don't appreciate being put on the spot either."
        show kat blush
        kat.say "People are staring at us!"
        show kat sad
        "I look around and see that she's right."
        "My cheeks burning, I shove the ring back into my pocket."
        "And then I get back to my feet."
        "I don't know what this means for Kat and me in going forwards."
        "But I do know that it's making me seethe with frustration right now."
    hide kat
    return

label kat_jack_propose_male:
    $ DONE["kat_jack_propose_male"] = game.days_played
    "Part of me still can't quite believe that I agreed to go along with this."
    "That I'm actually going to walk up to Kat and ask her to marry me."
    "Oh, and that Jack's going to be doing the same thing alongside me too!"
    "It sounded like such a great idea when he pitched it to me the other day."
    "But since then I've had the chance to actually go away and think about it."
    "And sure, I really want this thing to come off, for Kat to say yes."
    "Yet it all seems so crazy to me, asking a girl to marry not one guy, but two!"
    show jack blank casual at center, zoomAt(1.25, (640, 920)) with easeinright
    "Jack, on the other hand, doesn't seem to be worried in the slightest."
    "He's practically walking on air as we're on our way to meet Kat."
    "And he's smiling like he thinks this it's a foregone conclusion."
    show jack smile
    jack.say "Just let me do the talking, okay?"
    show jack blank
    mike.say "Are you sure that's a good idea, Jack?"
    mike.say "I mean, you're not exactly good at that kind of thing!"
    show jack surprised
    "Jack looks at me in amazement."
    "Like he can't believe what he's hearing."
    show jack angry
    jack.say "Hey!"
    jack.say "This was my idea in the first place, remember?"
    jack.say "Like, I'm the mastermind behind the whole thing."
    show jack normal
    mike.say "Whatever you say, Jack."
    mike.say "I just think we both need to have some kind of input."
    mike.say "After all, we are asking Kat to marry both of us!"
    "I can see that Jack's about to open his mouth to argue the point."
    hide jack
    show kat at center, zoomAt(1.25, (380, 880)) with easeinleft
    "But luckily for me, that's just when I see Kat up ahead."
    "So I don't hesitate to make use of the opportunity."
    mike.say "Hey, Kat!"
    mike.say "Wow..."
    mike.say "You look really great today!"
    "It's not like I never paid Kat a compliment before now."
    "But maybe I'd normally have waited a little while before doing so."
    show kat confused
    "Because right now it seems to make her look at me in a suspicious manner."
    show kat happy
    kat.say "Hey, [hero.name]..."
    kat.say "Someone's trying to be charming today, aren't they?!?"
    show kat smile
    "I'm about to brush the question off with a joke."
    show jack normal zorder 1 at center, zoomAt(1.25, (900, 920)) with easeinright
    "But Jack chooses that moment to leap into the conversation."
    show jack smile
    jack.say "Oh yeah, Kat..."
    jack.say "He's really laying it on thick today!"
    show jack happy
    jack.say "But he's right you know, you do look amazing!"
    show jack normal
    "I roll my eyes as Jack tries to side with Kat."
    "Yet in the next breath does the exact same thing that I did."
    mike.say "Yeah, yeah, yeah..."
    mike.say "Anyway, Kat..."
    mike.say "There's a reason we asked to meet you today."
    "As soon as I mention the purpose of the meeting, Kat's interest is piqued."
    show kat stuned
    "She raises her eyebrows, a look of intrigued surprise on her face."
    show kat surprised
    kat.say "There is?"
    show kat stuned
    mike.say "Yeah, we wanted to..."
    "I'm already reaching into my pocket as I'm saying this."
    "And I'm also beginning to get down on one knee too."
    "But as soon as he sees this, Jack wants in on the action too."
    show jack smile with hpunch
    jack.say "We wanted to ask you something..."
    show jack embarrassed
    "I feel Jack starting to jostle me on one side."
    "And a quick glance in his direction shows me why."
    show jack normal at center, zoomAt(1.25, (900, 1080)) with ease
    "He's trying to get down on one knee and pull out his ring too!"
    show jack smile
    jack.say "We wanted to ask you to..."
    show jack surprised with hpunch
    mike.say "To ask you to marry us!"
    "Jack shoots me a frown as I beat him to the punch."
    "But I think that we both manage to thrust out our hands at the same time."
    "Which means that Kat finds herself looking at two rings a moment later."
    show kat shocked
    kat.say "Wha..."
    kat.say "What's going on?!?"
    show kat stuned
    show jack smile
    jack.say "Isn't that obvious?"
    show jack sadsmile
    mike.say "We want you to marry us!"
    show kat shocked
    kat.say "Oh wow..."
    kat.say "How am I ever going to choose between you two?"
    show kat busted
    show jack worried
    "Jack and I exchange a confused glance at Kat's question."
    "Then we turn our attention back to her, shaking our heads."
    show jack whining
    jack.say "No, no, no..."
    jack.say "We don't want you to marry one of us."
    show jack normal
    mike.say "We want you to marry both of us..."
    mike.say "At the same time!"
    show kat shocked
    kat.say "Oh..."
    kat.say "Oh, I see..."
    kat.say "Oh crap!"
    show kat busted
    if kat.love >= 195 and kat.flags.mike_pleased >= 1 and kat.flags.jack_pleased >= 1:
        "Kat does a little jump on the spot."
        show kat smile zorder 2 at center, traveling(1.35, 0.3, (420, 980))
        "Then she reaches for my ring, but pauses."
        "Just long enough to reach for Jack's instead."
        "But then she stops and waves for us both to get up."
        show kat happy
        kat.say "Of course I'll marry you two idiots."
        kat.say "But get up first - you're embarrassing me!"
        show kat smile
        show jack happy at center, zoomAt(1.25, (900, 920)) with ease
        "Jack and I are all nods as we struggle to our feet."
        "And once we're standing, Kat holds out a hands to each of us."
        "I slide my ring onto one of them and Jack does the same to the other."
        show jack smile
        jack.say "Oh wow..."
        jack.say "You said yes..."
        jack.say "It's actually happening!"
        show jack normal
        "I'm not babbling like Jack is."
        "But I still feel just as thrilled."
        mike.say "I can't quite believe it, Kat."
        mike.say "That someone as great as you not only wants to marry me..."
        mike.say "But this guy too?!?"
        show jack angry
        jack.say "Hey!"
        show jack normal
        show kat happy
        "Kat chuckles and shakes her head."
        show kat talkative
        kat.say "Ah, it's not that crazy of me."
        kat.say "I've had more fun with you both these past few weeks than I have in years."
        kat.say "And sure, it's kind of spur of the moment..."
        kat.say "But some of the best things in life happen that way."
        show kat smile
        "My mind's racing the whole time that Kat's explaining herself."
        "I'm thinking about the plans that we're going to need to make."
        "All of the arrangements and things that'll have to be agreed."
        "But I tell myself that there's going to be plenty of time for that in the future."
        "Right now I should be focussing on celebrating with my partners-to-be."
        $ kat.set_fiance()
        $ hero.gain_item("wedding_ring")
        $ jack.set_fiance()
    elif kat.love >= 195 and kat.flags.mike_pleased >= 1:
        show kat smile at center, traveling (1.35, 0.3, (380, 980))
        "Kat surprises me by hurrying over to me."
        "And then she almost snatches the ring out of my hand."
        "I can't help grinning like a fool as she does this."
        "But then I realise Jack's still kneeling there beside me."
        "And he looks like he's waiting for Kat to take his ring too."
        show jack lying
        jack.say "Erm..."
        jack.say "Kat..."
        jack.say "Aren't you forgetting someone?"
        show jack sadsmile
        "Suddenly Kat turns to face Jack."
        show kat sad
        "And I can see that she has an awkward, almost pained look on her face."
        show kat whining
        kat.say "Oh, Jack..."
        kat.say "There's no easy way to say this..."
        kat.say "But I don't want to marry you!"
        show kat sad
        show jack surprised
        "Part of me wants to leap up and punch the air."
        "To make a big deal out of the fact that Kat chose me."
        "But I can already see the hurt spreading across Jack's face."
        "So instead I get slowly to my feet."
        "And then I hold out a hand to help him up too."
        mike.say "I'm sorry, buddy."
        mike.say "I really don't know what to say!"
        "I was expecting Jack to be upset at the rejection."
        show jack sad
        show kat stuned
        play sound spank
        with hpunch
        "But when he slaps my hand away, I'm still amazed."
        mike.say "Ouch..."
        mike.say "What the..."
        show jack angry
        jack.say "Don't 'sorry buddy' me!"
        jack.say "You knew this was going to happen, didn't you?!?"
        show jack sad at center, zoomAt(1.25, (900, 920)) with ease
        "Kat and I both take a step back as Jack fumes at us."
        mike.say "What are you talking about?"
        show jack angry
        jack.say "You planned this to make me look like an asshole."
        jack.say "And here I was, thinking you were my friends!"
        hide jack with easeoutright
        "Before either of us can say another word, Jack turns his back."
        "And then he runs off, leaving us standing there and speechless."
        $ Harem.leave_by_name("exclusive_fan", "jack")
        $ kat.set_fiance()
    elif kat.flags.jack_pleased >= 1:
        show kat smile zorder 2 at center, zoomAt(1.25, (440, 880)) with ease
        "Kat surprises me by hurrying over to where Jack's kneeling."
        "And then almost snatching the ring out of his hand."
        show jack normal blush
        "Of course Jack looks overjoyed as she does all of this."
        "But I'm still kneeling there, waiting for her to take my ring too."
        mike.say "Ah..."
        mike.say "Kat..."
        mike.say "Did you forget something?"
        "Suddenly Kat turns to face me."
        show kat sad
        "And I can see that she has an awkward, almost pained look on her face."
        show kat whining
        kat.say "Oh, [hero.name]..."
        kat.say "There's no easy way to say this..."
        kat.say "But I only want to marry Jack!"
        show kat sad
        show jack perv
        "As soon as Kat says all of this, Jack leaps to his feet."
        "Then he proceeds to punch the air, like he's celebrating a victory."
        show jack smile
        jack.say "YES!"
        jack.say "In your face!"
        jack.say "Kat turned you down, not me!"
        show jack guilty
        jack.say "Oh..."
        show jack lying
        jack.say "Sorry, buddy."
        show jack sadsmile
        "I feel stunned, battered from two directions at once."
        "All I can do is get slowly to my feet, shaking my head."
        mike.say "Yeah..."
        mike.say "Whatever..."
        mike.say "I think..."
        mike.say "I think I need some time alone..."
        hide jack
        hide kat
        with fade
        "I can hear Kat and Jack saying something to me as I walk away."
        "Even feel a hand on my shoulder, but I shrug it off and keep walking."
        "Because maybe that way I can forget what just happened to me."
        "Even if it's only for a short while."
        $ kat.set_gone_forever()
    else:
        show kat sad
        "Kat begins to shake her head, which can't be a good sign."
        show kat whining
        kat.say "Okay, okay..."
        kat.say "You guys both need to back up here."
        kat.say "Because I'm not wanting to marry you!"
        show jack sadsmile
        show jack surprised
        "Jack seems to be dumbfounded by Kat's response."
        "And it's not like I'm any less surprised myself."
        show jack whining
        jack.say "What do you mean, Kat?"
        show jack sadsmile
        mike.say "Are you saying you only want to marry one of us?"
        show jack whining
        jack.say "Are you, Kat?"
        jack.say "Because if you are, then you should totally marry me!"
        show jack sadsmile
        mike.say "Hey!"
        mike.say "Way to throw me under the bus!"
        "Kat's still shaking her head as Jack and I begin to argue."
        "But she soon puts a stop to it by clarifying her answer."
        show kat offended
        show jack surprised
        kat.say "Will you two shut the hell up?"
        kat.say "What I mean is that I don't want to marry either of you."
        show kat talkative
        kat.say "We have something really fun going on right now."
        kat.say "But I don't know if that's how I want to spend the rest of my life."
        show kat sad
        "Feeling pretty foolish, I put my ring away."
        "And then I start to get back to my feet."
        "Jack, on the other hand, stays right where he is, looking puzzled."
        show jack sad at center, zoomAt(1.25, (900, 920)) with ease
        "That is until I slap him on the shoulder, making him follow my lead."
        $ kat.love -= 25
        $ kat.sub -= 25
        show kat whining
        kat.say "Sorry, guys..."
        kat.say "That's just the way I feel."
        kat.say "I have to be honest about stuff like this."
        show kat sad
        mike.say "It's okay, Kat..."
        mike.say "We understand - don't we, Jack?"
        show jack angry
        jack.say "No I don't!"
        jack.say "I...Urgh..."
        show jack surprised with hpunch
        "Jack groans as I elbow him in the ribs."
        "But that seems to do the trick."
        jack.say "Ow!"
        show jack worried
        jack.say "Yeah, yeah...I understand too!"
        show jack annoyed
        show kat smile
        "Kat smiles and nods, clearly glad to be able to drop the subject."
        "But I note that she smiles at me with a little more gratitude than she does Jack."
        "Which is at least a small consolation."
    return
































label kat_ask_date_male:
    if Harem.find(kat):
        menu:
            "Ask Kat on a date":
                call kat_ask_date_alone_male from _call_kat_ask_date_alone_male
            "Meet Kat and Bree" if Harem.find_by_name("gaming") and Harem.together(bree, kat, name="gaming"):
                call kat_ask_date_bree from _call_kat_ask_date_bree
            "Meet Anna, Emma and Kat at the beach" if Harem.find_by_name("petite") and Harem.together(anna, emma, kat, name="petite") and "petite_harem_event_04_sex" in DONE and game.season in [0, 1]:
                call kat_ask_date_anna_emma from _call_kat_ask_date_anna_emma
    else:
        call kat_ask_date_alone_male from _call_kat_ask_date_alone_male_1
    return _return

label kat_ask_date_alone_male:
    mike.say "Kat, would you like to go on a date with me?"
    if kat.flags.nodate:
        kat.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        kat.say "Sure, it might be fun, when do you want us to go?"
        return True

label kat_ask_date_bree:
    $ renpy.dynamic("date_choice")
    mike.say "Do you want to get together with Bree and have some fun?"
    kat.say "I'd love to."
    if "gaming_harem_event_04" in DONE:
        kat.say "Do you want to do something special?"
        menu:
            "Gaming cumpetition":
                $ date_choice = "gaming_harem_cumpetition_intro"
            "Simple fooling around":
                $ date_choice = "gaming_harem_threesome_intro"
    else:
        $ date_choice = "gaming_harem_threesome_intro"
    call select_date_time from _call_select_date_time_34
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call expression date_choice from _call_expression_518
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "gaming", ["bree", "kat"], date_choice))
    return


label kat_ask_date_anna_emma:
    mike.say "Do you want to have some fun at the beach with Anna and Emma?"
    kat.say "I'd love to."
    call select_date_time (fixed_hour=14, fixed_season="summer") from _call_select_date_time_35
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call petite_harem_foursome_intro from _call_petite_harem_foursome_intro_2
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "petite", ["anna", "emma", "kat"], "petite_harem_foursome_intro"))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
