init python:
    Event(**{
    "name": "alexis_give_phone_number",
    "label": "give_phone_number",
    "girl": "alexis",
    "conditions": [
        PersonTarget(alexis,
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
    "name": "alexis_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "alexis",
    "conditions": [
        IsHour(12, 13),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(alexis,
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
    "name": "alexis_auto_greet",
    "label": "auto_greet",
    "girl": "alexis",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsActivity("None")),
        PersonTarget(alexis,
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
    "name": "alexis_auto_chat",
    "label": "auto_chat",
    "girl": "alexis",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(alexis,
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
    "name": "alexis_are_you_sick",
    "label": "are_you_sick",
    "girl": "alexis",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (alexis, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "alexis_ask_out",
    "label": "ask_out",
    "girl": "alexis",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("ask_date"))),
        PersonTarget(alexis,
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
    "name": "alexis_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "alexis",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label alexis_bye(bye_outfit=None):
    call npc_bye_outfit (npc=alexis, bye_outfit=bye_outfit) from _call_npc_bye_outfit_1
    $ (day, h, activity, bye_outfit) = _return
    if not activity == alexis.activity:
        if day != game.week_day:
            $ alexis.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ alexis.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"alexis {bye_outfit}")
        if activity["activity"] == "sleep":
            alexis.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            alexis.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            alexis.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            alexis.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            alexis.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            alexis.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            alexis.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            alexis.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            alexis.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            alexis.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            alexis.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            alexis.say "I'll go get dressed."
        hide alexis
    return

label alexis_cheated(action, cheat_npc=None):
    show alexis
    if cheat_npc and Harem.together(cheat_npc, alexis):
        show alexis flirt
        alexis.say "Aren't you forgetting something?"
        show alexis
        "And without warning Alexis kisses me."
        $ alexis.love += 1
        $ alexis.flags.kiss += 1
    elif alexis.sub >= 75:
        show alexis flirt
        show fx heart
        $ alexis.sub += 1
        "I see Alexis looking at me [action] someone else with envy and lust in her eyes."
    else:
        show alexis angry
        show fx anger
        $ loss = 5
        if alexis.flags.girlfriend or alexis.flags.fiance:
            $ loss += 5
        $ alexis.love -= loss
        "I see Alexis looking at me [action] someone else with a scary look on her face..."
    hide alexis
    return

label alexis_greet:
    if renpy.has_label(f"alexis_greet_dialogues_male") and not alexis.flags.greeted:
        scene expression f"bg {game.room}"
        $ alexis.flags.greeted = TemporaryFlag(True, 1)
        show alexis
        $ result = randint(1, 3)
        if result == 1:
            alexis.say "Hello, [hero.name]."
        elif result == 2:
            alexis.say "Hi, [hero.name]."
        elif result == 3:
            alexis.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                alexis.say "Good morning [hero.name]."
            elif game.hour < 19:
                alexis.say "Good afternoon [hero.name]."
            else:
                alexis.say "Good evening [hero.name]."
        call expression f"alexis_greet_dialogues_male" from _call_expression_206
        if alexis.flags.submissive_interact:
            if randint(0, 1) == 0:
                alexis.say "I need your cock inside of me so bad, [hero.name]!"
            else:
                alexis.say "[hero.name], I need it [hero.name]."
                alexis.say "I need your cock in me!"
        hide alexis
    return

label alexis_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Alexis."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Alexis."
        elif game.hour < 12:
            mike.say "Good morning Alexis."
        elif game.hour < 19:
            mike.say "Good afternoon Alexis."
        else:
            mike.say "Good evening Alexis."
    return

label alexis_kiss:
    scene expression f"bg {game.room}"
    if alexis.love < 25 and not alexis.is_girlfriend and not game.active_date.score >= 75:
        show alexis
        if randint(1, 2) == 1:
            "I lean in, angling for her lips. She turns at the last second. My mouth meets her cheek instead."
            "She pulls back at once. I catch the scent of her hair and the sharp sting of rejection."
            "I mumble an apology and look away, face burning. She mutters that it’s fine, timing and all that."
        else:
            "I move to kiss her, certain the old memory still holds. She recoils like she’s been stung."
            "She apologises a heartbeat later, but the damage is done. I was the one who misread the moment."
        hide alexis
        $ alexis.love -= 5
        $ alexis.sub -= 5
    elif not alexis.flags.kiss:
        hide alexis
        $ alexis.love += 5
        if alexis.lesbian > MAX_LES_GUY_SEX:
            $ alexis.lesbian -= 1
        show alexis kiss
        if randint(1, 2) == 1:
            "Her gaze lingers a moment longer than necessary. When she turns back I lean in and kiss her."
            "She answers at once, gentle at first, then surer. The years apart shrink to nothing while our lips stay pressed together."
            "It feels like a first time all over again."
        else:
            "I have wondered how it would feel to kiss her after so long. When it finally happens it is nothing like the old memory."
            "It is new. That seems like the right way to start."
        hide alexis kiss
        show alexis
        if alexis.love >= 60:
            alexis.say "Um, I think we should talk about this later, alright?"
        else:
            alexis.say "Oh uh... I've got to go..."
            "She slips away before I can answer. She looked uneasy. Did I push too soon?"
        $ alexis.flags.kiss += 1
    else:
        hide alexis
        show alexis kiss
        if randint(1, 2) == 1:
            "I know the angle of her head and the look in her eye. Our lips meet and the spark is still there."
            "I slip my tongue between her lips. Hers meets it. Arms tighten around each other. The rest of the room fades."
            "Kissing her never turns routine."
        else:
            "The old teenage kisses are fading. These new ones are better. Sometimes a quick peck, sometimes longer."
            "Each one pushes an older memory aside. I don’t mind. The new ones are the ones I want to keep."
        hide alexis
        $ alexis.love += 2
        $ alexis.flags.kiss += 1
    return

label alexis_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show alexis naked
        alexis.say "So I'm staying the night right?"
        menu:
            "You should leave":
                mike.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Alexis straightens and shrugs, then goes to collect her clothes from where she'd let it fall earlier."
                "She then heads up the stairs."
                $ alexis.love -= 1
                $ alexis.sub += 1
                call sleep from _call_sleep_23
            "You should sleep here":
                show alexis sleep
                mike.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                show alexis sleep
                "We curl up spooning together in bed, drifting toward sleep."
                $ alexis.love += 1
                call sleep ("alexis") from _call_sleep_6
    $ game.room = "bedroom1"
    return

label alexis_propose_male:
    "I’ve rehearsed this a thousand times. Now that the moment is here, I’m a mess of nerves."
    "Sweating, stumbling over words, terrified I’ve lost the ring. Alexis keeps glancing at me."
    show alexis confused with fade
    alexis.say "Ah, [hero.name]..."
    alexis.say "What’s with you today?"
    alexis.say "You look like a guy waiting for bad news!"
    "She’s calling me out. I try to play it cool."
    mike.say "What?!?"
    mike.say "Don’t be silly, Alexis!"
    mike.say "I’m fine, just fine!"
    show alexis normal
    "Now or never."
    mike.say "Oh..."
    mike.say "Ah shoot..."
    mike.say "I think I dropped something around here..."
    "I crouch, pretending to search. She steps back. I pull out the ring and look up."
    mike.say "Alexis..."
    mike.say "Will... will you marry me?"
    show alexis surprised
    "Her hands fly to her mouth. Eyes wide. Genuine shock."
    if alexis.love >= 195:
        "Without a word she grabs my hand and yanks me to my feet. Tears well in her eyes."
        mike.say "Ah..."
        mike.say "Alexis..."
        mike.say "Are you okay?"
        "She waves her hands, fighting the emotion."
        show alexis happy
        alexis.say "I... I’m okay..."
        alexis.say "This is... this is just a shock!"
        alexis.say "I never thought that you’d want to..."
        "I nod, following her babble."
        alexis.say "Oh... of course I will, [hero.name]!"
        alexis.say "Of course I’ll marry you!"
        "I’m the one stunned now. She thrusts her hand forward. I slide the ring on."
        "A weight lifts—the old high-school break-up, all of it. None of it matters anymore."
        "What matters is now, and that we’re going forward together."
        "She keeps hold of my hand and kisses me. The ring and the kiss both say the same thing: this will work."
        $ alexis.set_fiance()
    else:
        "She shakes her head, slow at first, then faster. My heart snaps."
        show alexis sad
        alexis.say "Oh god..."
        alexis.say "I’m so sorry, [hero.name]!"
        alexis.say "But I can’t marry you... I just can’t."
        "I’m still on my knees. I can’t stop myself."
        mike.say "But..."
        mike.say "But why, Alexis?"
        mike.say "I thought we’d both moved on?"
        mike.say "Haven’t we been getting on better than ever?"
        "She shakes her head, torn."
        show alexis sadsmile
        alexis.say "That’s exactly why we’re working now, [hero.name]!"
        alexis.say "Don’t you see?"
        alexis.say "We’ve kept it cool and casual, and it’s working!"
        alexis.say "Our problem was always too much commitment, not enough!"
        "It hurts, but she’s not wrong. We’re different people now. No old bullshit."
        "Maybe this isn’t the time."
        "I stand, sighing."
        mike.say "Okay, Alexis..."
        mike.say "Point taken."
        mike.say "I just wish I hadn’t gone down on one knee first!"
        "She gives me a pained smile and a kiss on the cheek. Not enough to fix it, but enough for hope."
        $ alexis.love -= 25
        $ alexis.sub -= 25
    return

label alexis_ask_date_male:
    if Harem.find_by_name("thot") and Harem.find_by_name("thot").is_active(alexis):
        menu:
            "Ask Alexis on a date":
                call alexis_ask_date_alone_male from _call_alexis_ask_date_alone_male
            "Set up a date with Alexis and Reona" if Harem.together(alexis, reona, name="thot") and alexis.love >= 200 and alexis.sub >= 90 and reona.love >= 200 and reona.sub >= 90 and not reona.hidden and audrey.love >= 200 and audrey.sub >= 90 and not audrey.hidden and "thot_harem_event_04" in DONE and not "thot_harem_event_05" in DONE and not hero.calendar.find(girl=alexis, date_only=True) and not hero.calendar.find(girl=reona, date_only=True) and not hero.calendar.find(girl=audrey, date_only=True):
                call alexis_ask_date_thot_harem_05 from _call_alexis_ask_date_thot_harem_05
            "Meet Alexis and Reona for some pool fun" if Harem.together(alexis, reona, name="thot") and game.season in [0, 1]:
                call alexis_ask_date_reona from _call_alexis_ask_date_reona
            "Meet Alexis, Audrey and Reona for a 'hot coffee'" if Harem.together(alexis, audrey, reona, name="thot"):
                call alexis_ask_date_audrey_reona from _call_alexis_ask_date_audrey_reona
    else:

        call alexis_ask_date_alone_male from _call_alexis_ask_date_alone_male_1
    return _return

label alexis_ask_date_alone_male:
    mike.say "Alexis, would you like to go on a date with me?"
    if alexis.love < 40 or alexis.flags.nodate:
        alexis.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        alexis.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice

label alexis_ask_date_thot_harem_05:
    mike.say "Hey Alexis. Are you okay to spend the night with Reona and I?"
    if alexis.flags.nodate:
        alexis.say "I don't feel like it, sorry."
        return False
    else:
        alexis.say "Of course [hero.name]! You already have a place in mind?"
        mike.say "Yeah, let's meet at the nightclub opening."
        return HaremAppointment((22, 23), "thot", ["alexis", "reona"], "thot_harem_event_05", fail_label="missed_thot_harem_event_05")

label alexis_ask_date_reona:
    mike.say "Do you want to have some fun around the pool with Reona?"
    alexis.say "I'd love to."
    call select_date_time (fixed_season=["spring", "summer"]) from _call_select_date_time_25
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call thot_harem_pool_fuck_intro from _call_thot_harem_pool_fuck_intro
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "thot", ["alexis", "reona"], "thot_harem_pool_fuck_intro"))
    return

label alexis_ask_date_audrey_reona:
    mike.say "Do you want to get together with Audrey and Reona and have some fun?"
    alexis.say "I'd love to."
    call select_date_time from _call_select_date_time_26
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call thot_harem_foursome_intro from _call_thot_harem_foursome_intro
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "thot", ["alexis", "audrey",  "reona"], "thot_harem_foursome_intro"))
    return
return