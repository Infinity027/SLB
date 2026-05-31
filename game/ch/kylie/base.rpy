init python:
    Event(**{
    "name": "kylie_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(12, 13),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(kylie,
            Not(IsPresent()),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ContactKnown(),
            MinStat("love", 50),
            Not(IsFlag("schedule", "jail"))
            ),
        ],
    "fun": 1,
    "girl": "kylie",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kylie_auto_greet",
    "label": "auto_greet",
    "girl": "kylie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsActivity("None")),
        PersonTarget(kylie,
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
    "name": "kylie_auto_chat",
    "label": "auto_chat",
    "girl": "kylie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kylie,
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
    "name": "kylie_are_you_sick",
    "label": "are_you_sick",
    "girl": "kylie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (kylie, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kylie_ask_out",
    "label": "ask_out",
    "girl": "kylie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("ask_date"))),
        PersonTarget(kylie,
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
    "name": "kylie_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "kylie",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label kylie_bye(bye_outfit=None):
    call npc_bye_outfit (npc=kylie, bye_outfit=bye_outfit) from _call_npc_bye_outfit_12
    $ (day, h, activity, bye_outfit) = _return
    if not activity == kylie.activity:
        if day != game.week_day:
            $ kylie.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ kylie.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"kylie {bye_outfit}")
        if activity["activity"] == "sleep":
            kylie.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            kylie.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            kylie.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            kylie.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            kylie.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            kylie.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            kylie.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            kylie.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            kylie.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            kylie.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            kylie.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            kylie.say "I'll go get dressed."
        hide kylie
    return

label kylie_cheated(action, cheat_npc=None):
    if cheat_npc and Harem.together(kylie, cheat_npc):
        $ kylie.sub += 1
        $ kylie.yandere -= 1
    else:
        $ gain = 5
        if kylie.flags.girlfriend or kylie.flags.fiance:
            $ gain *= 2
        if kylie.flags.target and cheat_npc and kylie.flags.target == cheat_npc.id:
            $ gain *= 2
        $ kylie.yandere += gain
        if kylie.yandere >= 50:
            show kylie yandere
        else:
            show kylie angry
        if cheat_npc:
            $ kylie.flags.target = cheat_npc.id
            "I see Kylie looking at me [action] [cheat_npc.name] with a strange, scary look in her eyes."
        else:
            "I see Kylie looking at me [action] someone else with a strange, scary look in her eyes."
        hide kylie
    return

label kylie_yandere(val=1):
    if Harem.together(kylie, active_girl):
        $ kylie.sub += 1
        $ kylie.yandere -= 1
    else:
        if kylie.flags.girlfriend or kylie.flags.fiance:
            $ val *= 2
        $ kylie.yandere += val
    return

label kylie_greet:
    if renpy.has_label(f"kylie_greet_dialogues_{hero.gender}") and not kylie.flags.greeted:
        scene expression f"bg {game.room}"
        $ kylie.flags.greeted = TemporaryFlag(True, 1)
        show kylie
        $ result = randint(1, 3)
        if result == 1:
            kylie.say "Hello, [hero.name]."
        elif result == 2:
            kylie.say "Hi, [hero.name]."
        elif result == 3:
            kylie.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                kylie.say "Good morning [hero.name]."
            elif game.hour < 19:
                kylie.say "Good afternoon [hero.name]."
            else:
                kylie.say "Good evening [hero.name]."
        call expression f"kylie_greet_dialogues_{hero.gender}" from _call_expression_244
        if kylie.flags.submissive_interact:
            if randint(0, 1) == 0:
                kylie.say "Hmm...hnn...ahh...so...so good to see you, [hero.name]!"
            else:
                kylie.say "[hero.name] you know how people say I'm crazy?"
                mike.say "Hum... Maybe?"
                kylie.say "It's true, I'm crazy... Crazy about you..."
        hide kylie
    return

label kylie_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Kylie."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Kylie."
        elif game.hour < 12:
            mike.say "Good morning Kylie."
        elif game.hour < 19:
            mike.say "Good afternoon Kylie."
        else:
            mike.say "Good evening Kylie."
    return

label kylie_kiss_reaction_male:
    if kylie.lesbian > MAX_LES_GUY_SEX:
        $ kylie.lesbian -= 1
    return

label kylie_kiss_male:
    scene expression f"bg {game.room}"
    if kylie.love + hero.charm < 80 and not kylie.is_girlfriend and not game.active_date.score >= 75:
        show kylie
        "I honestly thought I'd been right on top of the signals that Kylie was giving out, reading them perfectly."
        "But when I make a move to kiss her, thinking I'd picked just the right moment, she jerks away from me."
        "The look on her face is hard to make sense of right now."
        "She looks genuinely shocked, but not in the kind of horrified way that'd mean I got it badly wrong."
        "It's almost as though she's not adverse to the idea of me kissing her."
        "But my trying to take the lead's caught her off-guard."
        "Though why that would be a problem, I just can't say..."
        $ kylie.love -= 1
        hide kylie
    elif not kylie.flags.kiss:
        hide kylie
        call kylie_kiss_reaction_male from _call_kylie_kiss_reaction_male
        show kylie kiss
        "It's a definite no-brainer that I want to plant a kiss on Kylie, and I'm pretty sure that she's not going to reject me when I do."
        "So when I lean in and place an experimental peck on her lips, I'm banking on my hunch being correct."
        "And much to my relief, I see her eyes go wide with delight as soon as she realises what's happening."
        "Kylie returns the kiss with more passion that I was prepared for, and soon she's wrapped her arms around me in a tight embrace."
        "I can already feel her tongue as it pushes between my lips, as though she won't hold back for an instant."
        "It's almost as though she's been waiting for this to happen, and now it actually has, she wants to savour every single moment."
        "And with passion like this, what's not to like on my part?"
        $ kylie.flags.kiss += 1
        hide kylie kiss
        $ kylie.love += 5
    else:
        hide kylie
        call kylie_kiss_reaction_male from _call_kylie_kiss_reaction_male_1
        show kylie kiss
        "The sheer passion and enthusiasm that Kylie showed for our first kiss still seems to be there every time we repeat the gesture."
        "She's eager, maybe even a little too eager, to show her affection for me."
        "It makes no difference whether it's in public or private either."
        "Kylie kisses me with a single-minded determination that feels like she's almost marking her territory."
        "But that's okay, as I feel pretty much the same way."
        "I'm more than happy to have people know that Kylie's with me."
        hide kylie kiss
        $ kylie.flags.kiss += 1
        $ kylie.love += 2
    return

label kylie_ask_date_male:
    if Harem.find(kylie):
        menu:
            "Ask Kylie on a date":
                call kylie_ask_date_alone_male from _call_kylie_ask_date_alone_male
            "Ask Kylie and Ayesha on a date" if Harem.together(ayesha, kylie, name="taming"):
                call kylie_ask_date_ayesha_kylie from _call_kylie_ask_date_ayesha_kylie
    else:
        call kylie_ask_date_alone_male from _call_kylie_ask_date_alone_male_1
    return _return

label kylie_ask_date_alone_male:
    mike.say "Kylie, would you like to go on a date with me?"
    if kylie.love < 50 or kylie.flags.nodate:
        kylie.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        kylie.say "Sure, it might be fun, when do you want us to go?"
        return True

label kylie_ask_date_ayesha_kylie:
    mike.say "You want to get together with Ayesha and have some fun?"
    if game.flags.tamingDatesNumber >= 2:
        kylie.say "Sure, it might be fun, when do you want us to go?"
        mike.say "Let's meet at home."
        return HaremAppointment(20, "taming", ["ayesha", "kylie"], "taming_threesome_fuck", fixed_hour=True)
    else:
        kylie.say "I don't feel like it, sorry."
        return False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
