init python:
    Event(**{
    "name": "aletta_give_phone_number",
    "label": "give_phone_number",
    "girl": "aletta",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(aletta,
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
    "name": "aletta_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(10, 11),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(aletta,
            Not(IsHidden()),
            Not(IsPresent()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "aletta",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "aletta_auto_greet",
    "label": "auto_greet",
    "girl": "aletta",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(aletta,
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
    "name": "aletta_auto_chat",
    "label": "auto_chat",
    "girl": "aletta",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(aletta,
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
    "name": "aletta_are_you_sick",
    "label": "are_you_sick",
    "girl": "aletta",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (aletta, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "aletta_ask_out",
    "label": "ask_out",
    "girl": "aletta",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(aletta,
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
    "name": "aletta_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "aletta",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })


label aletta_bye(bye_outfit=None):
    call npc_bye_outfit (npc=aletta, bye_outfit=bye_outfit) from _call_npc_bye_outfit
    $ (day, h, activity, bye_outfit) = _return
    if not activity == aletta.activity:
        if day != game.week_day:
            $ aletta.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ aletta.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"aletta {bye_outfit}")
        if activity["activity"] == "sleep":
            aletta.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            aletta.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            aletta.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            aletta.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            aletta.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            aletta.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            aletta.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            aletta.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            aletta.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            aletta.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            aletta.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            aletta.say "I'll go get dressed."
        hide aletta
    return

label aletta_cheated(action, cheat_npc=None):
    show aletta
    if cheat_npc and Harem.together(cheat_npc, aletta):
        show aletta flirt
        aletta.say "Aren't you forgetting something?"
        show aletta
        "And without warning Aletta kisses me."
        $ aletta.love += 1
        $ aletta.flags.kiss += 1
    elif aletta.sub >= 75:
        show aletta flirt
        show fx heart
        $ aletta.sub += 1
        "I see Aletta looking at me [action] someone else with envy and lust in her eyes."
    else:
        show aletta angry
        show fx anger
        $ loss = 5
        if aletta.flags.girlfriend or aletta.flags.fiance:
            $ loss += 5
        $ aletta.love -= loss
        "I see Aletta looking at me [action] someone else with a scary look on her face..."
    hide aletta
    return

label aletta_greet:
    if renpy.has_label(f"aletta_greet_dialogues_{hero.gender}") and not aletta.flags.greeted:
        scene expression f"bg {game.room}"
        $ aletta.flags.greeted = TemporaryFlag(True, 1)
        show aletta
        $ result = randint(1, 3)
        if result == 1:
            aletta.say "Hello, [hero.name]."
        elif result == 2:
            aletta.say "Hi, [hero.name]."
        elif result == 3:
            aletta.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                aletta.say "Good morning [hero.name]."
            elif game.hour < 19:
                aletta.say "Good afternoon [hero.name]."
            else:
                aletta.say "Good evening [hero.name]."
        call expression f"aletta_greet_dialogues_{hero.gender}" from _call_expression_204
        hide aletta
    return

label aletta_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Aletta."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Aletta."
        elif game.hour < 12:
            mike.say "Good morning Aletta."
        elif game.hour < 19:
            mike.say "Good afternoon Aletta."
        else:
            mike.say "Good evening Aletta."
    return

label aletta_kiss:
    scene expression f"bg {game.room}"
    if aletta.love < 25 and not aletta.is_girlfriend and not game.active_date.score >= 75:
        show aletta
        "It can be hard to get a handle on just how a girl as strong-willed and forceful as Aletta is feeling from one moment to the next."
        "And it's harder still to be sure of what she wants me to do as a man when we're together."
        "With a less intimidating girl, I probably wouldn't think twice about taking a chance on being wrong."
        "But there's always that sense of fear with Aletta, worrying that doing the wrong thing at the wrong time could result in disaster."
        "All of which is made so much worse by the fact that she's already got me so desperate to take things to the next level with her."
        "This all comes to a head when I feel the insatiable urge to lean forward and try to give Aletta what I hope will be our first kiss."
        "I feel like the moment is right, everything feels right - at least from my point of view."
        "The first indication I get to tell me that I'm very wrong is the feeling of something firm and hard thumping me in the middle of the chest."
        "My mouth still stupidly poised to kiss Aletta, I look down in surprise to see her hand placed in the centre of my ribcage."
        "A moment later, the other hand is pushed into my face, turning my head away from her and puckering my lips at the same time."
        "And there I have perhaps the most neat evidence of my miss-reading Aletta, as well as the consequences for doing so."
        $ aletta.love -= 5
        $ aletta.sub -= 5
        hide aletta
    elif not aletta.flags.kiss:
        hide aletta
        $ aletta.love += 5
        if aletta.lesbian > MAX_LES_GUY_SEX:
            $ aletta.lesbian -= 1
        show aletta kiss
        "I don't want to find that I've mistimed this, picked the wrong moment and misread the cues that I think Aletta's been sending me just now."
        "But I just can't keep sitting on the feelings that she inspires in me any longer, and so to hell with the consequences."
        "At some point in my life, I need to actually stand up and make an effort to grab what I want, even if it might mean missing when I do so."
        "Normally I'd try to gently lean in to kiss a girl, with subtlety and a light touch being required."
        "But while I know that Aletta's certainly not made of steel and stone, she's also wilful and stubborn as well."
        "So this is why I choose to make the bold (and possibly also disastrous) move of cupping her cheeks in my hands."
        "Even as I do this, I can already see the look of surprise and then sudden indignation spreading across Aletta's face."
        "Well, it's now or never!"
        "I pull her closer and kiss her, full on the lips and with no attempt to be gentle."
        "I feel her twist and her muscles tense instinctively, but I choose to ignore these physical cues and press on."
        "For a moment I fear that I've totally misjudged the situation."
        "But then I almost literally feel Aletta melt in my arms."
        "It's not that the fight goes out of her, rather that the same strength and passion is suddenly channelled into our embrace instead."
        "Now her arms are wrapping around me and she's returning the kiss with a passion that almost overwhelms me!"
        hide aletta kiss
        $ aletta.flags.kiss += 1
    else:
        hide aletta
        $ aletta.love += 2
        show aletta kiss
        "If I was under the impression that breaking the ice with Aletta and having our first kiss together was going to be like bursting a damn, then I was proven wrong pretty quickly."
        "The ice queen of the office didn't seem about to melt quite that easily, and she was keen on the idea of rationing kisses even after that."
        "But then there is something to be said for keeping things a little special, and Aletta was a revelation when she did give into her urges."
        "We quickly got into the habit of ducking into doorways and behind obstacles that would hide us sight, and then she would all but pounce on me."
        "Aletta was no prude, just careful to preserve the image that she had spent so long cultivating, that of being an iron bitch."
        "It was well hidden, but her insides were metal too - only they were liquid metal, hot, glowing and able to burn you up in a second."
        "If I wasn't forceful enough when we kissed, Aletta would become the one to make the demands and push until she got what she wanted."
        "She would claw, slap and even bite at me if I were not giving her what she wanted, quickly enough or in sufficient amounts to satisfy her."
        "But you can get used to cuts and bruises around the mouth, and you can always deal with the pain."
        "Especially when it's being inflicted right along with the kind of kisses that Aletta gives to me."
        hide aletta kiss
        $ aletta.flags.kiss += 1
    return

label aletta_propose_male:
    show aletta
    "Back when we first met, I could only have thought of being nervous around Aletta for a bad reason."
    "She's a pretty intimidating woman, good at her job and not the kind to suffer fools gladly."
    "I've come to know the other side of her, the one that's a lot more loving and passionate."
    "But she still has the ability to make me quake in my boots when I need to ask her for something."
    "And today, I've resolved to ask her for something very special indeed."
    "I'm going to ask for her hand in marriage!"
    "I've picked out the ring."
    "I've planned what I'm going to say to her."
    "I've chosen the day for it all to go down on too."
    "All I have to do now is pluck up the courage to go through with it!"
    "The weight of it's starting to get to me though."
    "And I can see that Aletta's starting to get suspicious."
    aletta.say "[hero.name]..."
    aletta.say "Is there something wrong?"
    "Oh shit - she's going to rumble me!"
    "It's now or never!"
    "Hastily getting down on one knee, I fumble for the ring."
    "Aletta's eyes go wide as I hold it up for her to see."
    mike.say "A...Aletta..."
    mike.say "Will you marry me?"
    show aletta surprised
    "For a moment at least, Aletta seems genuinely surprised and lost for words."
    "But then she shakes it off and regains her usual level of composure again."
    "Which is good, because I know it means she's about to give me her answer!"
    if aletta.love < 195:
        show aletta sad
        aletta.say "Oh, [hero.name]."
        aletta.say "Silly, romantic, [hero.name]."
        aletta.say "You know that I can't marry you!"
        "I stare blankly at Aletta for an extended moment."
        "All the while I'm trying to fathom what she means."
        mike.say "I...I do?"
        "Aletta gives me an almost condescending smile as she nods."
        show aletta happy
        aletta.say "Of course you do."
        aletta.say "At least deep down you do."
        aletta.say "You've seen how hard it is for a woman to get promoted in the office."
        aletta.say "And do you know what percentage of female executives are married?"
        "I'm forced to shrug as I admit my ignorance."
        mike.say "Erm..."
        mike.say "No, Aletta."
        mike.say "I guess not!"
        aletta.say "My point exactly!"
        aletta.say "So while I appreciate to offer, and I don't see our relationship ending."
        aletta.say "I think it's best if we just chalk this down as you making a gesture, okay?"
        aletta.say "A sweet, well-meaning, but impossible gesture."
        "I nod slowly, withdrawing the ring and getting back to my feet."
        "Aletta nods too, and with that the whole matter seems to be settled."
        "Although I can't help feeling that I don't really understand what just happened..."
        $ aletta.love -= 25
        $ aletta.sub -= 25
    else:
        show aletta normal
        aletta.say "Oh, [hero.name]."
        aletta.say "Silly, romantic, [hero.name]."
        aletta.say "Of course I will!"
        "I stare blankly at Aletta for an extended moment."
        "All the while I'm trying to fathom what she means."
        mike.say "Y...you will?"
        "Aletta gives me an almost condescending smile as she nods."
        aletta.say "Yes, [hero.name], I will!"
        mike.say "That's great, Aletta!"
        "I almost leap to my feet as I push the ring onto her finger."
        "Shaking my head in amazement, the words start to tumble out of me."
        mike.say "I...I was so nervous, you have no idea!"
        mike.say "I was sure you'd say no."
        mike.say "Tell me all about married women not getting promoted!"
        "Aletta makes a quizzical sound as she studies the ring on her finger."
        aletta.say "Hmm..."
        aletta.say "That IS true, [hero.name]."
        aletta.say "But I feel like I can beat the odds with you at my side."
        aletta.say "I think we have what it takes to be a corporate power-couple!"
        "I nod eagerly, keen to show my approval."
        mike.say "I'm up for that, Aletta!"
        show aletta happy
        aletta.say "Good, very good."
        aletta.say "And if you do end up holding me back..."
        aletta.say "Well, you can always take early retirement and be a house-husband!"
        "I let out a nervous laugh at this, not sure if Aletta's joking or not."
        "But all she does is raise a single eyebrow, letting me know that she's not telling."
        $ aletta.set_fiance()
    hide aletta
    return

label aletta_work_with:
    if "aletta_stress_2" in DONE and game.week_day % 3 == 0 and Person.is_not_hidden("audrey") and Person.is_not_hidden("lavish") and Person.is_not_hidden("shiori"):
        "Once again, I need to present some bullshit to the whole team."
        call aletta_stress_meeting from _call_aletta_stress_meeting
    else:
        scene workingwith
        show workingwith aletta
        "I help out Aletta with her work."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
