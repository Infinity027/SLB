init python:
    Activity(**{
    "name": "watch_tv_with_samantha",
    "duration": 2,
    "fun": 3,
    "icon": "tv",
    "display_name": "Watch TV with Samantha",
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("fun", 0)),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            ),
        InvalidActivities("watch_tv_with_everyone_male"),
        ],
    "max_girls": 1,
    "label": "samantha_tv",
    })

    Event(**{
    "name": "samantha_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(10, 20),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(samantha,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "samantha",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_auto_greet",
    "label": "auto_greet",
    "girl": "samantha",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(samantha,
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
    "name": "samantha_auto_chat",
    "label": "auto_chat",
    "girl": "samantha",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(samantha,
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
    "name": "samantha_are_you_sick",
    "label": "samantha_are_you_sick",
    "girl": "samantha",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (samantha, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_ask_out",
    "label": "ask_out",
    "girl": "samantha",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(samantha,
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
    "name": "samantha_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "samantha",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label samantha_bye(bye_outfit=None):
    call npc_bye_outfit (npc=samantha, bye_outfit=bye_outfit) from _call_npc_bye_outfit_18
    $ (day, h, activity, bye_outfit) = _return
    if not activity == samantha.activity:
        if day != game.week_day:
            $ samantha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ samantha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"samantha {bye_outfit}")
        if activity["activity"] == "sleep":
            samantha.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            samantha.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            samantha.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            samantha.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            samantha.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            samantha.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            samantha.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            samantha.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            samantha.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            samantha.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            samantha.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            samantha.say "I'll go get dressed."
        hide samantha
    return

label samantha_cheated(action, cheat_npc=None):
    if ("samantha_event_A04" in DONE and not samantha.flags.nonexclusive) or "samantha_event_A04" not in DONE:
        show samantha angry
        $ loss = 15
        if samantha.flags.girlfriend or samantha.flags.fiance:
            $ loss += 15
        $ samantha.love -= loss
        samantha.say "I can't believe you would do that to me..."
    elif samantha.lesbian < 9 or samantha.sub < 90:
        show samantha normal
        if cheat_npc:
            "I spot Samantha watching at me [action] [cheat_npc.name], but once she realises I've seen her she turns away without saying anything."
        else:
            "I spot Samantha watching at me [action] someone else, but once she realises I've seen her she turns away without saying anything."
    else:
        show samantha flirt
        $ samantha.love += 2
        if cheat_npc:
            "I spot Samantha watching at me [action] [cheat_npc.name], softly biting her lip with a small smile."
        else:
            "I spot Samantha watching at me [action] someone else, softly biting her lip with a small smile."
    hide samantha
    return

label samantha_tv:
    call samantha_greet from _call_samantha_greet
    if hero.charm >= 40 - samantha.love or samantha.activity_name == "tv":
        call watch_tv_with (samantha) from _call_watch_tv_with_4
    else:
        show samantha
        samantha.say "Sorry, I don't have time right now."
        $ hero.cancel_activity()
        hide samantha
    return

label samantha_tv_reaction:
    samantha.say "Why not."
    return

label samantha_porn_bad_reaction:
    samantha.say "Sorry, I don't want to watch this sort of thing."
    return


label samantha_greet:
    if renpy.has_label(f"samantha_greet_dialogues_{hero.gender}") and not samantha.flags.greeted:
        scene expression f"bg {game.room}"
        show samantha
        $ samantha.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 4)
        if result == 1:
            samantha.say "Hey, [hero.name]."
        elif result == 2:
            samantha.say "[hero.name], hi."
        elif result == 3:
            samantha.say "It's been a while [hero.name]."
        else:
            if game.hour < 6:
                samantha.say "Hello [hero.name]."
            elif game.hour < 12:
                samantha.say "Mornin' [hero.name]."
            elif game.hour < 19:
                samantha.say "Good afternoon [hero.name]."
            else:
                samantha.say "Good evening [hero.name]."
        call expression f"samantha_greet_dialogues_{hero.gender}" from _call_expression_260
        if samantha.flags.submissive_interact:
            samantha.say "Oops...I need my daily dose of vitamins - which means your cock, [hero.name]!"
        hide samantha
    return

label samantha_greet_dialogues_male:
    if randint(1, 10) == 10 and samantha.love > 4:
        $ name = randchoice(["Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Sarah", "Kimberly", "Deborah", "Shirley", "Cinthia"])
        $ name2 = randchoice(["Margaret", "Dorothy", "Lisa", "Nancy", "Karen", "Betty", "Helen", "Sandra", "Donna", "Carol", "Ruth", "Sharon", "Michelle", "Laura"])
        mike.say "[name]?"
        mike.say "Oh, [name2]!"
        mike.say "Sorry, you totally sounded like [name]."
        "Samantha sighs, looking half-annoyed, half-amused by my joke."
        samantha.say "It's Samantha."
        if samantha.flags.nickname == "cupcake":
            mike.say "Oh, Cupcake hello."
        else:
            mike.say "Oh, Samantha hello."
        $ samantha.love += 1
    else:
        $ result = randint(1, 3)
        if result == 1:
            if samantha.flags.nickname == "cupcake":
                mike.say "Hello, Cupcake."
            else:
                mike.say "Hello, Samantha."
        elif result == 2:
            mike.say "Hi."
        else:
            if game.hour < 12:
                if samantha.flags.nickname == "cupcake":
                    mike.say "Good morning Cupcake."
                else:
                    mike.say "Good morning Samantha."
            elif game.hour < 19:
                if samantha.flags.nickname == "cupcake":
                    mike.say "Good afternoon Cupcake."
                else:
                    mike.say "Good afternoon Samantha."
            else:
                if samantha.flags.nickname == "cupcake":
                    mike.say "Good evening Cupcake."
                else:
                    mike.say "Good evening Samantha."
    return

label samantha_kiss:
    show samantha
    if samantha.flags.knows_ryancheats:
        $ dif = 80
    else:
        $ dif = 140
    if samantha.love + hero.charm < dif and not samantha.is_girlfriend and not game.active_date.score:
        "Samantha pushes me away."
        "I could say that I get the sudden, spontaneous urge to kiss Sam - but that'd be a lie."
        "It's an urge that's always been there, hiding just below the surface."
        "But then maybe that's where it should have remained."
        "My move to kiss Sam is pretty clumsy and faltering, so she sees it coming a mile off."
        "There's no slap or disapproving look, she just moves out of range and shakes her head."
        samantha.say "Don't ever do that again..."
        if samantha.flags.engaged and not samantha.flags.knows_ryancheats:
            samantha.say "You know I am with Ryan."
        "In the end, I'm left feeling as though what went wrong was more a matter of timing than anything else."
        "Maybe I just need to wait until the right moment comes along?"
        $ samantha.love -= 20
    elif samantha.love + hero.charm <= dif + 20 or (samantha.love <= 80 and not samantha.flags.knows_ryancheats) or (game.active_date.score >= 75 and not samantha.love + hero.charm < dif + 20):
        hide samantha
        if samantha.lesbian > MAX_LES_GUY_SEX:
            $ samantha.lesbian -= 1
        show samantha kiss
        if not samantha.flags.kiss:
            $ samantha.love += 5
            "I used to daydream about kissing Sam back when we were all living under the same roof."
            "Lame, I know - but she just had that much of an effect on me back then."
            "And I guess she still does now, based on how it feels to lean in and put my lips to hers."
            "There's no grand plan to it, and everything just seems to happen naturally."
            "Before either of us are truly aware of what's going on, we're sharing a gentle and searching kiss."
            "But nothing that I imagined could ever have compared to what this actually feels like."
            "It was definitely worth the wait..."
            hide samantha kiss
            show samantha
            if samantha.flags.knows_ryancheats:
                samantha.say "I don't know why you did that.\nBut you need to do it more."
            else:
                samantha.say "We shouldn't have done that."
            "After that line she turns around and leaves."
            $ samantha.flags.kiss += 1
        else:
            $ samantha.love += 2
            $ samantha.flags.kiss += 1
            show samantha kiss
            "I can't believe that something I used to dream of doing has become so natural and normal."
            "But that's not to say that sharing a kiss with Sam has lost its allure with repetition."
            "Each and every time she puts her lips to mine, it's like a little jolt of electricity."
            "A little shock to remind me of just how crazy it is to finally have this girl in my life as more than a friend."
            "Sam's always casual and free when it comes to showing her affection."
            "And I wonder if she realises just how much of a big deal each and every kiss actually is to me..."
            hide samantha kiss
            if not samantha.flags.knows_ryancheats:
                show samantha
                samantha.say "Stop doing that!"
    else:
        hide samantha
        if samantha.lesbian > MAX_LES_GUY_SEX:
            $ samantha.lesbian -= 1
        show samantha kiss
        if not samantha.flags.kiss:
            $ samantha.love += 5
            $ samantha.flags.kiss += 1
            "I used to daydream about kissing Sam back when we were all living under the same roof."
            "Lame, I know - but she just had that much of an effect on me back then."
            "And I guess she still does now, based on how it feels to lean in and put my lips to hers."
            "There's no grand plan to it, and everything just seems to happen naturally."
            "Before either of us are truly aware of what's going on, we're sharing a gentle and searching kiss."
            "But nothing that I imagined could ever have compared to what this actually feels like."
            "It was definitely worth the wait..."
            hide samantha
            hide samantha kiss
            if samantha.flags.knows_ryancheats:
                show samantha close
                samantha.say "It seems that I waited for that kiss for far too long.\nI hope that there is more coming my way."
            else:
                show samantha
                samantha.say "We shouldn't have done that."
            "After that line she turns around and leaves."
        else:
            $ samantha.love += 2
            $ samantha.flags.kiss += 1
            "I can't believe that something I used to dream of doing has become so natural and normal."
            "But that's not to say that sharing a kiss with Sam has lost its allure with repetition."
            "Each and every time she puts her lips to mine, it's like a little jolt of electricity."
            "A little shock to remind me of just how crazy it is to finally have this girl in my life as more than a friend."
            "Sam's always casual and free when it comes to showing her affection."
            "And I wonder if she realises just how much of a big deal each and every kiss actually is to me..."
            hide samantha
            hide samantha kiss
            if not samantha.flags.knows_ryancheats and not Harem.find(samantha, name='home'):
                show samantha close
                samantha.say "We should stop doing that."
    hide samantha
    return

label samantha_propose_male:
    "I'd like to be able to say that I'm not very good at this kind of thing, using my stock excuse to explain potentially making a mess of something important ahead of time."
    "But it really doesn't apply to this situation, as I can't ever recall having been in the position of trying to pluck up the courage to ask a girl to marry me before now."
    "Then again, as much of a cliche as it sounds, I can't remember feeling the same way about any other girl that I do about Sam right now."
    "And it's not just because of the fact that I know what Ryan was doing behind her back when they were supposed to be getting married."
    "Having Sam come back into my life, even as a friend, in recent times has made me more aware of ever of exactly how she makes me feel."
    "Being single and, at least trying, to play the field was fun while it lasted."
    "But lately I just can't think of any girl other than Sam, and it's been slowly threatening to drive me crazy unless I do something about it."
    "So I went out on a whim one day and bought a ring, one that I think is pretty nice and doesn't look cheap."
    "One way or another, I have to know if she feels the same way as I do."
    "If she says yes, then I can hopefully look forward to having her in my life for a long time to come."
    "And if she says no...well, at least I can move on and maybe put it behind, given time...maybe."
    show samantha
    "I have the ring sitting inside of the nice box it came in, feeling like it weighs a literal ton in my pocket the next time Sam and I meet up."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake - how are you doing?"
    else:
        mike.say "Hey, Sam - how are you doing?"
    samantha.say "The usual - how about you, [hero.name]?"
    samantha.say "Say, are you okay?"
    samantha.say "You look a little bit like you're on edge today!"
    "I rub the back of my head with my hand, trying to look as casual as I can manage."
    mike.say "Well...huh, I guess you could say that I've got something on my mind right now."
    mike.say "Something that's been eating me up for the past few days."
    "To her credit, Sam looks instantly concerned for me."
    "Her face, if anything, looks even more beautiful when she's thinking of people other than herself."
    "Shit, she's so perfect - how did a jerk like me ever get this close to a girl like this one?"
    samantha.say "Is it something I can help you work out?"
    samantha.say "Maybe something you'd like to talk about?"
    mike.say "Sort of yes, on both counts!"
    "I feel like someone about to jump into dark water and unable to see the bottom."
    "But I can't go on like this any longer."
    "Either I have to know that Sam feels the same way as I do."
    "Or else I need to get the hell away from her before I go crazy on her account."
    "I just have to accept that today, I'm Mr Cliche."
    "So I take a deep breath."
    "I reach into my pocket."
    "And I kneel down in from of Sam."
    samantha.say "[hero.name], what are you doing?"
    "I look up at her, feeling more afraid than I can ever recall feeling before."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake...will...will you marry me?"
    else:
        mike.say "Sam...will...will you marry me?"
    "Sam returns my gaze, her face oddly blank, as if she doesn't fully realise what's going on."
    "Then, all of a sudden, she seems to catch up with the moment."
    "Her eyes widen and she actually tries to speak at least a couple of times before she manages to get a single word out."
    if samantha.flags.engaged and "samantha_event_B01" in DONE and not samantha.is_visibly_pregnant and not samantha.sexperience:
        samantha.say "Erm, [hero.name], unless you'd forgotten - I'm kind of already married!"
        "She smiles wryly whilst brandishing her wedding ring in front of me for effect."
        if samantha.flags.nickname == "cupcake":
            mike.say "Yeah, Cupcake, I was there too, remember?"
        else:
            mike.say "Yeah, Sam, I was there too, remember?"
        "Sam looks at me sideways, and I can see that she's not offended by my gesture, more intrigued and keen to hear more."
        samantha.say "Go on, this should be good!"
        "I look at her in a certain amount of visible exasperation, unhappy that she seems determined to turn the whole thing into a joke."
        "But that's one of the things I love about her, that quirky sense of humour."
        if samantha.flags.nickname == "cupcake":
            mike.say "Straight up, Cupcake - you shouldn't be married to that asshole, he doesn't deserve you."
        else:
            mike.say "Straight up, Sam - you shouldn't be married to that asshole, he doesn't deserve you."
        samantha.say "So says you - why not tell me this before I married him?"
        if samantha.flags.nickname == "cupcake":
            mike.say "Because I already upped and told you he was cheating on you, Cupcake."
        else:
            mike.say "Because I already upped and told you he was cheating on you, Sam."
        mike.say "You were betrayed and vulnerable, and the last thing you needed right then was someone confessing their undying love for you!"
        samantha.say "And that's what you're doing now - confessing your undying love for me?"
        "That stops me for a moment - damn her!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Yes, I suppose it does - I love you, Cupcake...and I want to be with you for the rest of my life!"
        else:
            mike.say "Yes, I suppose it does - I love you, Sam...and I want to be with you for the rest of my life!"
        if samantha.love < 195:
            samantha.say "Yeah, well maybe I feel the same way...but not like this, at least not right now!"
            "Sam must be able to see my heart sink at her refusing my proposal, as she shakes her head instantly."
            samantha.say "Whoa, whoa - I'm not saying never, just not here and now!"
            samantha.say "I'm not out of one marriage that turned out to be a bad idea yet, so I'm certainly not eager to sign up for another at such short notice."
            samantha.say "What do you say we try it on for a while first, see how we like the fit?"
            mike.say "So it's not a yes?"
            samantha.say "It's not a no, either - would you settle for a maybe?"
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "Yes."
            mike.say "You don't have to answer right now..."
            samantha.say "Yes!"
            mike.say "I mean, if you need time..."
            samantha.say "YES!!!"
            mike.say "Did you just say what I thought you said?!?"
            "Sam smiles and drapes her arms around my shoulders."
            samantha.say "Yes, you idiot - I said yes!"
            $ samantha.set_fiance()
    elif samantha.flags.engaged and "samantha_event_B01" in DONE and not samantha.is_visibly_pregnant:
        samantha.say "So, you want to make it official, huh?"
        samantha.say "Kick Ryan's ass right out of the old marital bed?"
        samantha.say "Is fucking me behind my husband's back not getting you hard enough anymore?"
        "Sam winks and lets out a laugh that's all the more sexy for coming out of her usually pristine mouth."
        if samantha.flags.nickname == "cupcake":
            mike.say "You've never been just a casual fuck, Cupcake - you're much more than that to me!"
        else:
            mike.say "You've never been just a casual fuck, Sam - you're much more than that to me!"
        "Sam looks down for a moment, and I can see just how much seeing me behind her cheating husband's back has reinvigorated her as a woman."
        "While Ryan made her feel unwanted by his actions, what we've done has given her way more than revenge."
        "It's made her feel like she's worth something again, that there's someone out there that wants her that badly."
        "I just hope that she's not become so high on the feeling that she can't see us being anything else."
        "Because I want us to become a full-time thing, rather than just something that stands for revenge."
        "I didn't start screwing Sam just to hit back at Ryan, and I'm hoping that she feels the same way too."
        samantha.say "Well, I already have a wedding dress and a ring..."
        samantha.say "Suspenders and matching underwear too..."
        samantha.say "And here I was thinking of letting you fuck me in them just for the sake of it!"
        "As she jokes, Sam's face is utterly inscrutable."
        if samantha.love < 195:
            samantha.say "I'm going to have to say no - at least for the time being."
            "I can't hide my disappointment, and it shows."
            samantha.say "Look, [hero.name] - I want to end it with Ryan, and I don't want to give up what we have either."
            samantha.say "But I can't jump from one marriage straight into another."
            samantha.say "I'm saying no, but I'm not saying never."
            samantha.say "Just let me get my head straight and figure out what I want."
            samantha.say "If you really do love me, is that too much to ask?"
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "Yes...I'll marry you!"
            "I'm lost for words, wrapping my arms around her and kissing her before she can say another word."
            samantha.say "Hey, hey...wait a minute!"
            samantha.say "Just so long as you wait until the divorce is final before we go public?"
            "She's said yes, and we both know that it's official now - so why care if nobody else does just yet?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Of course, Cupcake - I've waited this long for you."
            else:
                mike.say "Of course, Sam - I've waited this long for you."
            mike.say "So I can wait a little longer to tell everyone else."
            $ samantha.set_fiance()
    elif samantha.flags.engaged and "samantha_event_B01" in DONE and samantha.is_visibly_pregnant:
        "Sam strokes the curve of her belly, letting me know without saying a word that this decision involves our unborn child, as much as either of us."
        "For all that I might have thought being pregnant with my baby would have counted in my favour right now, she seems to be mulling it over rather deeply all the same."
        samantha.say "Urgh, it's so frustrating to have almost everything that I want in life and yet still be married to that shit!"
        "I can't argue with her on that one, but I'm hoping that her knowing I want to make a commitment to her will be enough."
        if samantha.flags.nickname == "cupcake":
            mike.say "Don't think of it like that, Cupcake."
        else:
            mike.say "Don't think of it like that, Sam."
        mike.say "Stop thinking of what you don't have and focus on what you do instead."
        mike.say "We have each other, and soon we'll have a child we both love too."
        mike.say "Whatever happens with Ryan and the divorce, it can't take any of that away."
        "Sam smiles at me, a little sadness evident in her eyes, but the happiness she finds in my words visible too."
        samantha.say "You're right...you're right."
        samantha.say "I need to be less fixated on material things."
        samantha.say "Also on getting one over on people that don't give a shit."
        samantha.say "When I should be thinking about the people that do!"
        "That's great to hear - but it's still not an answer."
        if samantha.love < 195:
            samantha.say "There's just so much that's up in the air right now."
            samantha.say "Until we get things sorted, I don't think either of us should be making rash commitments."
            mike.say "You mean..."
            "Sam smiles at me again, wanly this time, putting her hand atop mine to cover up the ring."
            samantha.say "What I'm saying is, that for now at least, it's a no."
            "I can't keep my nod from being sad, but I hope that it's not the end of us altogether."
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "Hmm...I can't believe that I didn't see what was important before."
            samantha.say "You know, what was REALLY important?"
            "She smiles at me again, more affirmed in her emotions this time."
            if samantha.flags.NPCpregnancy == "ryan":
                samantha.say "As long as I have you and our baby, I don't need anything else in the whole world."
            else:
                samantha.say "As long as I have you, I don't need anything else in the whole world."
            samantha.say "Yes, [hero.name], I will marry you!"
            $ samantha.set_fiance()
    elif not samantha.flags.engaged and "samantha_event_B01" in DONE and not samantha.is_visibly_pregnant:
        samantha.say "Wow, that is not something that I expected to be happening to me again anytime soon!"
        "She must see the instant distress that her comment causes to show in my eyes, as she hurries to comfort me."
        samantha.say "[hero.name], please don't think anything of what I just said."
        samantha.say "I'm still reeling a little bit from the stress of the divorce and trying to get Ryan out of my life for good."
        mike.say "I'm sorry, it's too soon - it was insensitive of me..."
        samantha.say "No, it was insensitive of me - I've been nothing but self-obsessed since I left Ryan."
        samantha.say "And you've been there, every step of the way, whenever I needed anything."
        samantha.say "You gave me support, and never asked for anything in return that I wasn't willing to give."
        "I look her in the eye, still amazed at how beautiful she is, even now."
        if samantha.flags.nickname == "cupcake":
            mike.say "You gave me the chance to be with you, Cupcake."
        else:
            mike.say "You gave me the chance to be with you, Sam."
        mike.say "If I have that, what else can you give me that's better?"
        mike.say "I'm not asking you to marry me because I want to possess you."
        mike.say "I'm asking because I just want you to stay with me and know that I want to be with you."
        "I hope she says something quickly, before this turns into a sickly romantic scene!"
        if samantha.love < 195:
            samantha.say "[hero.name], you're not going to lose me, if that's what's behind all of this."
            samantha.say "Please don't worry about that!"
            mike.say "But..."
            samantha.say "But I'm not ready to make a commitment like that and go through another wedding just yet."
            "I nod, not able to keep my disappointment from being apparent."
            samantha.say "Keep the ring and let's see how we feel a little way down the road, okay?"
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "Yes, [hero.name], I'll marry you!"
            mike.say "Really?"
            mike.say "I thought you were going to say that it was too soon!"
            samantha.say "I did think about that - but this is different to the last time."
            samantha.say "I've changed since then, and you're totally another kind of guy to Ryan."
            samantha.say "We shouldn't let the past dictate the future."
            $ samantha.set_fiance()
    elif not samantha.flags.engaged and "samantha_event_B01" in DONE and samantha.is_visibly_pregnant:
        samantha.say "A shotgun wedding - how quaint and rustic!"
        samantha.say "Should we make the plans now, or wait until I'm the size of a whale so it's really obvious?"
        "She has a wicked smile on her face as she asks me this, making it clear that she's joking."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake, I'd have proposed to you whether you were pregnant or not - even if you looked like a space-hopper!"
        else:
            mike.say "Sam, I'd have proposed to you whether you were pregnant or not - even if you looked like a space-hopper!"
        samantha.say "Now there's a mental image that sticks with me - maybe if I were, you could ride me to work and back every day!"
        "I fix her with a serious stare, and she shakes her head to acknowledge that it's time to talk like proper adults."
        if samantha.flags.nickname == "cupcake":
            mike.say "For real, Cupcake - we're both single in the eyes of the law, and we're committed enough to be having a kid together."
        else:
            mike.say "For real, Sam - we're both single in the eyes of the law, and we're committed enough to be having a kid together."
        mike.say "What's wrong with going that one step further and making it legal?"
        samantha.say "What's wrong with leaving things as they are?"
        samantha.say "I'm serious, [hero.name] - that next step's a big one, and we're pretty good right where we are."
        samantha.say "Aren't we?"
        "I nod, not wanting to give her the impression that I'm dissatisfied with our current relationship."
        mike.say "Of course we are..."
        mike.say "There's just an old-fashioned part of me that wants to be able to call you my wife."
        if samantha.love < 195:
            samantha.say "I just don't think that we should get married for the sake of making a statement like that."
            samantha.say "Your name will be on the baby's birth certificate and we're not talking about breaking up."
            samantha.say "Are we?"
            mike.say "No, of course not!"
            samantha.say "Then what's the problem?"
            samantha.say "We can always get married when we both feel we're ready."
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "Maybe you do have a point..."
            samantha.say "If it doesn't matter that much whether we get married or not, then surely doing it's as simple as not doing it?"
            mike.say "Well, that's not how I'd have put it..."
            samantha.say "And it would tie up everything neatly if we did it before the baby was born..."
            samantha.say "Okay...yes...let's do it!"
            $ samantha.set_fiance()
    elif not samantha.flags.engaged and not "samantha_event_B01" in DONE and not samantha.is_visibly_pregnant:
        samantha.say "Wait a minute - didn't I just dodge getting married once already?"
        samantha.say "And if I remember correctly, you were instrumental in making that happen too!"
        "If there was a response that I'd been anticipating, that was certainly not it."
        mike.say "I just thought that, you know, as we'd been seeing so much of each other and it was going so well..."
        mike.say "Oh shit - is it not going well and I haven't noticed?"
        "Sam tries to calm me down without starting to laugh."
        samantha.say "It's been going fine!"
        samantha.say "It's just as I said though."
        samantha.say "When you've left one guy at the altar under circumstances like that, you're not ready to jump at the chance to do it all again."
        mike.say "It'd be different this time - it'd me you and me, not you and some cheating jerk."
        samantha.say "Well, at least we've got that in our favour."
        "I nod, hoping that this is going somewhere positive."
        mike.say "So, what do you say?"
        if samantha.love < 195:
            samantha.say "Sorry, [hero.name], but I'm not ready to make that commitment yet."
            samantha.say "Calling it off with Ryan was pretty much the most painful thing I've ever had to do."
            samantha.say "Even the thought of having that much at stake again emotionally is really scary."
            "I look down, obviously disappointed."
            mike.say "Oh...okay...if that's how you feel."
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "I'm being stupid about this!"
            samantha.say "I've been letting what happened with Ryan hold me back for too long."
            samantha.say "Yes, I'll marry you!"
            mike.say "You will?"
            samantha.say "That's what I said, isn't it?"
            $ samantha.set_fiance()
    elif not samantha.flags.engaged and not "samantha_event_B01" in DONE and samantha.is_visibly_pregnant:
        samantha.say "Whoa, things are going very quickly around here!"
        samantha.say "First I'm marrying Ryan, then I'm not."
        samantha.say "Next thing I know, we're an item and then I'm pregnant."
        samantha.say "Now you're proposing to me!"
        "I shrug and shake my head in surprise."
        mike.say "It felt like the natural thing to do...I just wanted to be with you, and make it official."
        samantha.say "Sorry - I guess that after what happened with Ryan I'm still a little phobic of all the trappings of marriage."
        mike.say "I thought that, what with us expecting a baby, it'd be nice to make a commitment to each other."
        samantha.say "It's not like we need a piece of paper and an expensive ceremony to do that."
        mike.say "I guess not..."
        "I'm running out of things to say fast here."
        "I always thought women were the ones that had the big dreams of their wedding days!"
        mike.say "So, what's your answer?"
        if samantha.love < 195:
            samantha.say "I can't, [hero.name]...at least not yet."
            "Sam must see my disappointment, as she puts a hand on my arm in a show of support."
            samantha.say "But that doesn't mean that we have to call it all off in terms of us either."
            samantha.say "We've managed just fine without being married so far."
            "I suppose she's right - she got her fingers burned with Ryan, and it's not something worth losing her over."
            "I nod in agreement."
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            samantha.say "I suppose that I should think of Ryan as a practice run, a chance to shake out the kinks."
            samantha.say "I got a lucky escape there, but why should it keep me from trying again?"
            mike.say "You mean..."
            samantha.say "Yes, [hero.name], I mean that I will marry you!"
            show samantha kiss
            $ samantha.flags.kiss += 1
            "Before she can say another word, I'm up and kissing her as though my life depends on it."
            $ samantha.set_fiance()
    else:
        samantha.say "[hero.name]...what are you talking about?"
        samantha.say "I mean...I really value your friendship."
        samantha.say "But you know that I'm already married - and to Ryan, your friend!"
        "I can sense that Sam's surprised by my proposal, but not actually upset or angry with what I've done."
        "I could pile on the pressure by telling her all about Ryan's cheating before they were married."
        "But that would be trying to pressure her, rather than having her come round to the idea of her own accord."
        "Plus, she could just as easily turn the tables on me and demand to know why I let her marry the guy when I knew about his being unfaithful."
        if samantha.flags.nickname == "cupcake":
            mike.say "Of course I know all that, Cupcake...I was there on the day you got married."
        else:
            mike.say "Of course I know all that, Sam...I was there on the day you got married."
        mike.say "But I was there before that, and I realised on your wedding day that I should have spoken up sooner."
        mike.say "I guess I thought that if you and Ryan went off together, then I'd just forget about it in time."
        mike.say "Thing is that, what with us getting close again, that kind of didn't happen."
        mike.say "I feel like we've been making up for lost time...but I want more."
        mike.say "I just need to know if there's any chance you feel the same way too?"
        if samantha.love < 195:
            samantha.say "Ahh, [hero.name] - you've put me in a terrible spot here!"
            "I can see that Sam's not trying to make me feel bad, her expression is genuinely conflicted."
            samantha.say "Do me a favour next time you feel like this - tell the girl BEFORE she marries your friend!"
            "She sighs, and I already think I can sense what's coming next."
            samantha.say "How can I marry you when I'm still married to Ryan?"
            samantha.say "If I break up one marriage to start another, what kind of a basis is that for the future?"
            samantha.say "I'm sorry, [hero.name] - but I have to say no."
            $ samantha.love -= 25
            $ samantha.sub -= 25
        else:
            show samantha close happy
            "Sam falls silent again as my words sink in, and I can see that she's been visibly shaken."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, are you okay?"
            else:
                mike.say "Sam, are you okay?"
            samantha.say "Yes, yes...I'm getting there!"
            mike.say "Sorry...I shouldn't have done this...it was stupid of me to think..."
            samantha.say "No, don't say it was stupid...you really feel like that, so strongly about me?"
            mike.say "Yeah, I do - and I just had to see what you felt."
            "Sam looks away for a moment, thinking quickly and in silence."
            samantha.say "I always thought you just saw me as a friend, that's why I never tried to be anything more to you."
            samantha.say "If I leave Ryan now, won't that make you think I'm unfaithful, not worth trusting?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, I'd trust you with my life!"
            else:
                mike.say "Sam, I'd trust you with my life!"
            samantha.say "Then yes...yes, I'll marry you!"
            $ samantha.flags.set_fiance()
    "Afterwards I'm actually more shaky and nervous than I was beforehand."
    "My thoughts are all out of order, and it's hard to remember exactly what's happened or how we got here."
    "But what I do recall is Sam's answer, and all of the things that are going to happen as a result of it."
    hide samantha
    return

label samantha_ask_date_male:
    if Harem.find(samantha):
        menu:
            "Ask Samantha on a date":
                call samantha_ask_date_alone_male from _call_samantha_ask_date_alone_male
            "Ask Samantha and Emma on a date" if Harem.together(emma, samantha, name="friendly"):
                call samantha_ask_date_emma_samantha from _call_samantha_ask_date_emma_samantha
    else:
        call samantha_ask_date_alone_male from _call_samantha_ask_date_alone_male_1
    return _return

label samantha_ask_date_emma_samantha:
    mike.say "Do you want to get together with Emma and have some fun?"
    if "emma_samantha_threesome" in DONE:
        samantha.say "I'd love to."
        call select_date_time from _call_select_date_time_10
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            call emma_samantha_threesome_now_intro ("samantha") from _call_emma_samantha_threesome_now_intro_1
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "friendly", ["emma", "samantha"], "emma_samantha_threesome_appointment_intro"))
    else:
        samantha.say "I am sorry [hero.name], I'd prefer to have you for me alone."
        call samantha_ask_date_alone_male from _call_samantha_ask_date_alone_male_2
        return _return
    return


label samantha_ask_date_alone_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake, let's go on a date."
    else:
        mike.say "Samantha, would you like to go on a date with me?"
    if samantha.love <= 80 or (samantha.love <= 120 and not samantha.flags.knows_ryancheats) and hero.charm <= 60:
        if not samantha.flags.knows_ryancheats:
            samantha.say "It wouldn't be fair to Ryan. And he is your friend."
        else:
            samantha.say "I am sorry [hero.name], I don't see you that way."
        return False
    else:
        samantha.say "With pleasure."
        if not samantha.flags.knows_ryancheats:
            samantha.say "But as friends..."
        return True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
