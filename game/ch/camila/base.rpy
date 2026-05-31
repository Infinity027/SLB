init python:
    Event(**{
    "name": "camila_give_phone_number",
    "label": "give_phone_number",
    "girl": "camila",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(camila,
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
    "name": "camila_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "camila",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(camila,
            Not(IsPresent()),
            Not(IsHidden()),
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
    "name": "camila_auto_greet",
    "label": "auto_greet",
    "girl": "camila",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(camila,
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
    "name": "camila_auto_chat",
    "label": "auto_chat",
    "girl": "camila",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(camila,
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
    "name": "camila_are_you_sick",
    "label": "are_you_sick",
    "girl": "camila",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (camila, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "camila_ask_out",
    "label": "ask_out",
    "girl": "camila",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
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
    "name": "camila_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "camila",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label camila_cheated(action, cheat_npc=None):
    show camila
    if cheat_npc and Harem.together(cheat_npc, camila):
        show camila flirt
        camila.say "Aren't you forgetting something?"
        show camila
        "And without warning Camila kisses me."
        $ camila.love += 1
        $ camila.flags.kiss += 1
    elif camila.sub >= 75:
        show camila blush
        show fx heart
        $ camila.sub += 1
        "I see Camila looking at me [action] someone else with envy and lust in her eyes."
    else:
        show camila sad
        show fx anger
        if cheat_npc:
            $ camila.flags.cheatedby = cheat_npc.id
        $ loss = 5
        if camila.flags.girlfriend or camila.flags.fiance:
            $ loss += 5
        $ camila.love -= loss
        "I see Camila looking at me [action] someone else with tears in her eyes..."
    hide camila
    return

label camila_bye(bye_outfit=None):
    call npc_bye_outfit (npc=camila, bye_outfit=bye_outfit) from _call_npc_bye_outfit_6
    $ (day, h, activity, bye_outfit) = _return
    if not activity == camila.activity:
        if day != game.week_day:
            $ camila.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ camila.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"camila {bye_outfit}")
        if activity["activity"] == "sleep":
            camila.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            camila.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            camila.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            camila.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            camila.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            camila.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            camila.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            camila.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            camila.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            camila.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            camila.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            camila.say "I'll go get dressed."
        hide camila
    return

label camila_greet:
    if renpy.has_label(f"camila_greet_dialogues_{hero.gender}") and not camila.flags.greeted:
        scene expression f"bg {game.room}"
        show camila
        $ camila.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            camila.say "Hello, [hero.name]."
        elif result ==2:
            camila.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                camila.say "Good morning [hero.name]."
            elif game.hour < 19:
                camila.say "Good afternoon [hero.name]."
            else:
                camila.say "Good evening [hero.name]."
        call expression f"camila_greet_dialogues_{hero.gender}" from _call_expression_217
        if camila.flags.submissive_interact:
            if randint(0, 1) == 0:
                camila.say "It's my duty to protect and serve, but your word is law, [hero.name]!"
            else:
                camila.say "Bad boy, bad boy, what ’ya gonna do?"
                camila.say "What ’ya gonna do when I'll come for you?"
        hide camila
    return

label camila_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Camila."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Camila."
        elif game.hour < 12:
            mike.say "Good morning Camila."
        elif game.hour < 19:
            mike.say "Good afternoon Camila."
        else:
            mike.say "Good evening Camila."
    return

label camila_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show camila naked
        if not camila.is_sex_slave:
            camila.say "[hero.name], can I... Can I spend the night?"
        elif camila.flags.daddy:
            camila.say "Daddy, can I... Can I please spend the night?"
        else:
            camila.say "Master, can I... Can I spend the night?"
        menu:
            "No":
                mike.say "No, you shouldn't; I have to get up early tomorrow."
                "The sex was beyond incredible."
                "Frowning a little, Camila straightens and collects her clothes in silence."
                if not camila.is_sex_slave:
                    camila.say "That's OK, sleep well!"
                elif camila.flags.daddy:
                    camila.say "That's OK, sleep well Daddy!"
                else:
                    camila.say "That's OK, sleep well Master!"
                "She then grins at me, before leaving."
                $ camila.love -= 3
                call sleep from _call_sleep_50
            "Yes":
                show cuddle camila
                mike.say "Of course you can."
                "I catch a brief moment of joy flash across her face, before she pulls me into a hug, nuzzling into me once again."
                camila.say "Thank you..."
                "I'm not sure why she seems so happy about this, but it looks like I picked the right answer."
                if not camila.is_sex_slave:
                    camila.say "Sleep well, [hero.name]."
                    mike.say "You too."
                elif camila.flags.daddy:
                    camila.say "Sleep well, Daddy."
                    mike.say "You too my cute little girl."
                else:
                    camila.say "Sleep well, Master."
                    mike.say "You too my cute little slave."
                "We both cuddle in silence, drifting off to sleep in each others arms."
                $ camila.love += 3
                call sleep ("camila") from _call_sleep_51
        $ game.room = "bedroom1"
    return

label camila_kiss:
    scene expression f"bg {game.room}"
    if camila.love < 25 and not camila.is_girlfriend and not game.active_date.score >= 75:
        show camila
        "Saying that I'm afraid of Camila wouldn't be telling the exact truth."
        "More like I'm afraid of coming on too strong with a girl as tough as her."
        "So it's with trepidation that I choose my moment and lean in to kiss her."
        "Camila stiffens, looking almost like I just pulled a knife!"
        "She yanks her lips out of the way of mine before I can make an excuse."
        "And I can already feel my cheeks starting to burn as I turn to look the other way."
        $ aletta.love -= 5
        $ aletta.sub -= 5
        hide camila
    elif not camila.flags.kiss:
        $ camila.flags.kiss += 1
        if camila.lesbian > MAX_LES_GUY_SEX:
            $ camila.lesbian -= 1
        "Kissing Camila should be no different to kissing any other girl, right?"
        "Sure, she's a tough cop that's probably more macho than I'll ever be."
        "But she's still a modern woman and I'm a modern guy, so shouldn't matter."
        "Which is why I throw caution to the wind and lean in to kiss her without warning."
        "As soon as our lips touch, I feel Camila stiffen, and I fear the worst."
        "But the, just as quickly, she melts into the kiss."
        "And from that point on, it's like noting I can describe!"
        hide camila
        show camila kiss
        $ camila.love += 5
        "I've seen Camila go for her gun, but it was never as fast as this!"
        "One moment she's looking away, and the next she's pounced on me."
        "Camila plants her lips on mine, kissing me with an intensity takes me by complete surprise."
        "I have no choice but to surrender and lean into it."
        "But I find myself loving it more with each second that it lasts!"
        "Is this what it feels like when you're swept off your feet?"
        hide camila kiss
    else:
        $ camila.flags.kiss += 1
        hide camila
        if camila.lesbian > MAX_LES_GUY_SEX:
            $ camila.lesbian -= 1
        show camila kiss
        "Once the barriers between Camila and me come down, there's no looking back."
        "We both lose any fear of showing the affection that we feel for each other."
        "And with every kiss that she steals from me, those feelings become more intense."
        "Before long, it's harder to keep from kissing her than not."
        "And Camila seems to be in the same predicament."
        "The tough, hardened cop can't keep her hands off me!"
        hide camila kiss
        hide camila
        $ camila.love += 2
    return

label camila_propose_male:
    show camila
    "I know that I want to take my relationship with Camila to the next level, and I want it badly."
    "No matter how hard I try to tell myself that what we already have is enough, it's not working."
    "I'm that seriously into her that I need to know we're committed to each other in the long term."
    "Nothing else is going to cut it - I feel like I have to ask her to marry me, and now!"
    "But the problem is that I don't know how to go about it."
    "I have this sneaking suspicion that Camila's not going to respond well if I do it the traditional way."
    "If I get down on one knee, I just know that she's going to pull her tough-cop act on me."
    "And if she goes into that mode, then she'll shoot be down for sure."
    "Well...I don't mean literally."
    "Just that if I do it in a public place she'll say no for fear of ruining her hardened image."
    "So what I need to do is put some serious thought into this."
    "That way I can spring it on her as a surprise."
    "I just hope that I don't end up getting shot in the process!"
    "So that's how I come to be waiting for the right moment."
    "I'm watching Camila like a hawk, waiting for the signs I need."
    "Luckily for me, she's one of those girls with a lot of little quirks."
    "Like pretending to cough whenever her stomach grumbles in hope of covering up the sound."
    show camila blush
    camila.say "Oooh..."
    camila.say "Sorry, [hero.name]!"
    camila.say "That last night shift I pulled..."
    camila.say "I guess it left me more beat than I thought!"
    "I smile at Camila's little white lie and raise an eyebrow."
    mike.say "Come on, Camila..."
    mike.say "Level with me - did you skip breakfast again?"
    show camila bored
    camila.say "What kind of a question is that?"
    camila.say "You're not the boss of me!"
    mike.say "No, Camila, I'm your boyfriend."
    mike.say "And I'm asking out of concern for you."
    mike.say "You're out there on the streets, putting yourself at risk."
    mike.say "So the least I can do is bug you to take care of your body!"
    show camila blush
    "Camila looks disarmed for a moment."
    "And I can see the look in her eyes, tell just what it is."
    "It's that moment when her tough demeanour slips."
    "Just long enough to know that she's grateful for my concern."
    "But then, just as quickly, her defences go back up again."
    camila.say "Ah..."
    camila.say "Quit trying to mother me, [hero.name]!"
    show camila normal
    camila.say "I had a cup of coffee at the end of my shift!"
    camila.say "What more do you want, huh?"
    mike.say "I dunno, Camila..."
    mike.say "I was thinking about what you might want."
    mike.say "Like maybe one of these little beauties right here?"
    "I choose that very moment to pull out the box from behind my back."
    "And then I lift the lid to reveal what's hidden inside."
    "Camila gazes down at the rows of fresh, sweet-smelling donuts."
    "But then she looks up at me, narrowing her eyes with suspicion."
    show fx question
    camila.say "What is this, [hero.name]?"
    camila.say "Is this some kind of joke?"
    camila.say "You actually think I'm gonna eat donuts in public?"
    hide fx
    mike.say "Oh, come on, Camila!"
    mike.say "You're not scared of that old cliche, are you?"
    mike.say "It's the twenty-first century, for god's sake!"
    mike.say "And it's just one donut!"
    "I pick one out and offer it to her."
    "And I can see that she's already beginning to crack."
    "Even I can hear Camila's stomach growling by now."
    "And I know that she loves donuts, even if she won't admit it."
    mike.say "Here..."
    mike.say "This one looks good!"
    show camila donut a
    "Camila's hand moves faster than my eye can follow it."
    "I guess she must be crazily fast on the draw!"
    "She's so fast that the donut seems to simply materialise in her hand."
    "As she goes to bite into it, I sense that my plan's about to end in disaster."
    mike.say "Camila, wait!"
    mike.say "What's that in the middle?"
    mike.say "There's something wedged in the hole!"
    show fx question
    "Camila holds up the donut, studying what she sees inside the hole."
    "Then she plucks it out, staring in amazement at the ring she's holding."
    camila.say "Huh?"
    hide fx
    show camila blush a
    show fx exclamation
    camila.say "What the hell?!?"
    "But when she looks in my direction, she's in for another surprise."
    "As I'm kneeling on the ground in front of her."
    "And I'm looking up with a nervous smile on my face."
    hide fx
    camila.say "[hero.name]..."
    camila.say "What are you..."
    mike.say "Camila..."
    mike.say "Will you marry me?"
    "The expression that appears on Camila's face is one I've never seen her pull before."
    "It's a combination of surprise, fear and utter helplessness."
    "For the first time, I see Camila floundering and lost for words!"
    if camila.love < 195:
        "She tears her eyes off of me and stares down and the ring in her hand."
        "But then I see Camila make a genuine effort to get a handle on her feelings."
        "And it seems to work as she takes a deep breath and shakes her head."
        $ camila.love -= 25
        $ camila.sub -= 25
        camila.say "Will you get the hell up off the ground?"
        camila.say "People are staring at you!"
        "I do as I'm told, beginning to feel more than a little self-conscious."
        show camila -donut
        "As soon as I'm back on my feet, Camila puts the donut back into the box."
        "And it doesn't escape my attention she makes sure to do the same with the ring too."
        mike.say "I..."
        mike.say "I take it that's a no?"
        "My voice is shaking with emotion as I ask the question."
        "I just can't help it, you know?"
        "I asked the girl I love to marry me and she turned me down."
        "I'm not a tough cop like Camila is!"
        "To my surprise, Camila's own toughness cracks as I show my emotions."
        "She looks genuinely worried that she's hurt me."
        "And that only makes the sense of rejection even worse."
        show camila sad
        camila.say "I can't, [hero.name] - you know that!"
        camila.say "It's like I'm married to the force already."
        show camila normal
        camila.say "Trust me, I've seen more than enough cop's spouses end up as widows!"
        mike.say "I...I guess that's a good point, Camila..."
        show camila bored
        camila.say "Oh, come on, [hero.name]!"
        camila.say "I'm not dumping your ass!"
        show camila flirt
        camila.say "We're still an item, yeah?"
        mike.say "Of course, Camila!"
        mike.say "And maybe you'll want to retire some day soon?"
        mike.say "You can marry me then, right?"
        show camila normal
        camila.say "Let's cross that bridge when we come to it, okay?"
        "I nod, eager to make Camila as happy as I possibly can."
        "Things might not have gone to plan with the proposal."
        "But at least we're still an item!"
    else:
        "She tears her eyes off of me and stares down and the ring in her hand."
        "I see Camila make a genuine effort to get a handle on her feelings."
        "But then one of her hands shoots up to her mouth as she makes a sound."
        "Was that...did she just sob?"
        "Are Camila's eyes actually tearing up right now?"
        "I'm just not used to seeing her show emotion like this."
        "And so it takes me a moment to shake off my amazement."
        "But the moment that I do, I'm on my feet, rushing to comfort Camila."
        mike.say "Camila?"
        mike.say "Are you okay?"
        "I take hold of her hands as I gaze into her eyes."
        "Camila nods, still not able to say a single word."
        "Now I can see for certain that there are tears in her eyes."
        "And when she finally manages to speak, it comes bursting out of her."
        camila.say "YES!"
        camila.say "Yes, yes, yes!"
        mike.say "Erm..."
        mike.say "Is that yes as in you're okay?"
        mike.say "Or yes as in you'll marry me?"
        show camila kiss -donut with vpunch
        $ camila.flags.kiss += 1
        "By way of answer, Camila throws her arms around my neck."
        "And the next thing I know, her lips are pressed against mine."
        "I wrap my own arms around her waist, almost picking her up off of her feet."
        "When the kiss is finally over, we're both left breathless."
        show camila close flirt -kiss
        mike.say "Oh..."
        mike.say "Oh wow..."
        mike.say "I was so scared you were going to say no!"
        mike.say "That you'd give me some speech about being married to the force!"
        camila.say "Phew..."
        camila.say "I...I would have..."
        camila.say "I always did that when someone got too close to me in the past."
        camila.say "But with you...it's weird..."
        camila.say "It's like I won't put off being with you for fear of losing you."
        camila.say "I never felt like that about anybody else!"
        "Camila holds out her hand, and I slide the ring onto her finger."
        "She holds it up and admires the way it looks on her hand."
        show camila happy
        camila.say "You'd better be ready for this, [hero.name]."
        camila.say "It's tough being a cop's wife!"
        mike.say "Husband - you mean a cop's husband!"
        show camila wink
        camila.say "I know what I mean, [hero.name]..."
        $ camila.set_fiance()
    hide camila
    return

label camila_ask_date_male:
    if Harem.find_by_name("criminal") and Harem.find_by_name("criminal").is_active(camila):
        menu:
            "Ask Camila on a date":
                call camila_ask_date_alone_male from _call_camila_ask_date_alone_male
            "Set up a date with Camila and Lexi" if "criminal_harem_event_03" in DONE and "criminal_harem_event_04" not in DONE and not hero.calendar.find(label="criminal_harem_event_04"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_12
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "criminal", ["camila", "lexi"], "criminal_harem_event_04", "Date (Camila & Lexi)", "missed_criminal_harem_date"))
                else:
                    call criminal_harem_event_04 from _call_criminal_harem_event_04
                    $ DONE["criminal_harem_event_04"] = game.days_played
                    call sleep from _call_sleep_71
                    $ game.pass_time(2)
                return
            "Set up a date with Camila and Lexi" if "criminal_harem_event_04" in DONE and not hero.calendar.find(label="criminal_harem_fuck_date"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_15
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "criminal", ["camila", "lexi"], "criminal_harem_fuck_date", "Date (Camila & Lexi)", "missed_criminal_harem_date"))
                else:
                    call criminal_harem_fuck_date from _call_criminal_harem_fuck_date
                    call sleep from _call_sleep_5
                    $ game.pass_time(2)
                return
    else:
        call camila_ask_date_alone_male from _call_camila_ask_date_alone_male_1
    return _return

label camila_ask_date_alone_male:
    mike.say "Camila, would you like to go on a date with me?"
    if camila.love < 50 or camila.flags.nodate:
        camila.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        camila.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
