init python:
    Event(**{
    "name": "emma_give_phone_number",
    "label": "give_phone_number",
    "girl": "emma",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(emma,
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
    "name": "emma_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(12, 13),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(emma,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "emma",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "emma_auto_greet",
    "label": "auto_greet",
    "girl": "emma",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(emma,
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
    "name": "emma_auto_chat",
    "label": "auto_chat",
    "girl": "emma",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(emma,
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
    "name": "emma_are_you_sick",
    "label": "are_you_sick",
    "girl": "emma",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (emma, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "emma_ask_out",
    "label": "ask_out",
    "girl": "emma",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(emma,
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
    "name": "emma_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "emma",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label emma_bye(bye_outfit=None):
    call npc_bye_outfit (npc=emma, bye_outfit=bye_outfit) from _call_npc_bye_outfit_8
    $ (day, h, activity, bye_outfit) = _return
    if not activity == emma.activity:
        if day != game.week_day:
            $ emma.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ emma.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"emma {bye_outfit}")
        if activity["activity"] == "sleep":
            emma.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            emma.say "I have to go to the bathroom, don't you dare peek!"
        elif activity["activity"] in ["meal"]:
            emma.say "I am so hungry..."
        elif activity["activity"] in ["watch"]:
            emma.say "I think I'm going to go catch a movie."
        elif activity["activity"] in ["drink"]:
            emma.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            emma.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            emma.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            emma.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            emma.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            emma.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            emma.say "I'll go get dressed."
        hide emma
    return

label emma_cheated(action, cheat_npc=None):
    show emma sad
    "Emma sees me with another woman and her eyes get big. Disappointment is written all over her face."
    $ emma.love -= 10
    $ emma.flags.cheatcount += 1
    hide emma
    return

label emma_greet:
    if renpy.has_label(f"emma_greet_dialogues_{hero.gender}") and not emma.flags.greeted:
        scene expression f"bg {game.room}"
        show emma
        $ emma.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 4)
        if result == 1:
            emma.say "Hey, [hero.name]."
        elif result == 2:
            emma.say "[hero.name], hi!"
        elif result == 3:
            if emma.love < 100:
                emma.say "It's been a while [hero.name]."
            else:
                emma.say "Hey you!"
        else:
            if emma.love < 25:
                emma.say "Heya."
            elif emma.love < 100:
                emma.say "Nice to see you, [hero.name]!"
            elif emma.love < 150:
                emma.say "It's always good to see you, [hero.name]!"
            else:
                emma.say "I've missed you!"
        call expression f"emma_greet_dialogues_{hero.gender}" from _call_expression_225
        if emma.flags.submissive_interact:
            if randint(0, 1) == 0:
                emma.say "I'm the girl of your dreams, [hero.name] - but all your dreams are SO dirty!"
            else:
                emma.say "Oh [hero.name], seeing you is like living in a dream."
        hide emma
    return

label emma_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Emma."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 12:
            mike.say "Good morning Emma."
        elif game.hour < 19:
            mike.say "Good afternoon Emma."
        else:
            mike.say "Good evening Emma."
    return

label emma_kiss:
    scene expression f"bg {game.room}"
    show emma
    if emma.flags.breakup:
        emma.say "I don't think so."
        $ emma.love -= 1
        return

    if emma.flags.nokiss and emma.flags.samgirlfriend:
        emma.say "I'd never do that to Samantha!"
        return

    if emma.flags.nokiss or emma.love < 60:
        emma.say "I, um. I don't...no let's not, okay?"
        return


    if not emma.flags.kiss and (not game.active_date.on_date(emma) or game.active_date.score < 75 or emma.love < 60):
        emma.say "I don't...I'm not...maybe I'm not quite ready for that, okay?"
        return

    "I step toward Emma, intent upon giving her a kiss, and she doesn't pull away."
    if not emma.flags.kiss:
        "Neither does she react with full-throated enthusiasm, either."
        "I can't let that stop me."
        show emma blush
        "As I wrap my arms around her shoulders, her eyes go wide, and her cheeks redden."
        "I wait a few seconds before proceeding. I'm not completely sure if this is what she wants or not, but..."
        "She is stiff, but she doesn't pull away."
        "I pull her close to me, very nearly lifting her off her feet, and I touch my lips to hers. At first she doesn't respond at all."
        hide emma
        show emma kiss
        "But then her eyes close and she relaxes."
        "As our lips touch, I feel her entire body press into mine, and she squeezes me tightly."
        "The kiss itself is a little awkward, like she isn't sure what to do. But what makes it special is how we hold each other."
        "After a moment or two we part."
        hide emma kiss
        show emma blush
        "Emma looks up at me, seemingly a little dazed."
        $ emma.love += 5
    elif emma.flags.kiss < 5:
        "Instead, she slips her arms beneath mine, curling her hands around my shoulders."
        hide emma
        show emma kiss
        "She's still awkward but she's into it."
        "When our lips touch, Emma explores the very act of kissing. She tests her lips, her tongue, my tongue."
        "She experiments with how to hold me, moving her fingers, exploring for the most comfortable, the most intimate position."
        hide emma kiss
        show emma happy
        "When it's over, Emma looks at me with an expression of pure delight."
        $ emma.love += 2
    else:
        "With a practiced motion, Emma slips her arms beneath mine, curling her hands around my shoulders."
        hide emma
        show emma kiss
        "Her lips meet mine, readily. Her tongue brushes against mine, but the real fun is from her lips and the way her breasts press up against my chest."
        "She touches her teeth to my lower lip, nibbling just slightly, and then returning to enjoying the closeness of our lips."
        "All too soon, it's over."
        hide emma kiss
        show emma happy
        "But the sheer contentment on her face as she steps back from me makes it all worthwhile."
        $ emma.love += 2
    $ emma.flags.kiss += 1
    hide emma
    return

label emma_propose_male:
    show emma
    "I never thought that one day I'd be literally proposing the girl of my dreams."
    "Hell, I never even thought that there was a girl like that out there waiting for me!"
    "But here I am, a bag of nerves as I wait for the right moment to pop the question."
    "I'm not worried that Emma's going to say no."
    "I'm actually scared that I won't have the nerve to go through with it!"
    "I mean, she has to say yes, doesn't she?"
    "Emma's the actual girl of my dreams, the one I saw while I was sleeping."
    "So how on earth could this not have been the divine plan all along?"
    "Luckily for me, Emma doesn't seem to notice how nervous I am right now."
    "Which also raises more than a few questions."
    "I'm sweating like crazy here - surely I don't look like this all the time?"
    "I try to push those thoughts out of my head."
    "And I keep right on pretending to listen to what Emma's saying."
    "I can't keep on nodding and shaking my head like this for much longer."
    "Sooner or later I'm going to nod when I should have shaken or vice-versa."
    "So as soon as Emma pauses for breath, I make my move..."
    show fx question
    emma.say "Oh, [hero.name]..."
    emma.say "Whatever are you doing?"
    hide fx
    "I ignore Emma's question long enough to get down on one knee."
    "And then I look up at her as I pull out the ring hidden in my pocket."
    mike.say "Emma..."
    mike.say "You're the girl of my dreams!"
    mike.say "Will you become my wife as well?"
    "For the first time today, Emma falls silent."
    "She blinks in confusion and her lips move."
    "But she says nothing and I can't read anything in the way she moves her head."
    "So all I can do is wait patiently while she gathers her wits and gives me an answer."
    emma.say "I..."
    emma.say "[hero.name], I..."
    if emma.love >= 195:
        show emma happy
        emma.say "Oh, [hero.name]!"
        emma.say "Of course I will!"
        "For a moment I can't actually believe what I'm hearing."
        "But then it finally sinks in and I leap to my feet."
        mike.say "YOU WILL?!?"
        mike.say "I...I mean...you will?"
        "Emma nods eagerly as I slip the ring onto her finger."
        "Then she holds her hand out, admiring the look of it."
        emma.say "I had NO idea you were going to do that!"
        emma.say "It was the biggest, bestest surprise ever!"
        show emma close
        "Emma throws her arms around me, squeezing me tight."
        "I return the embrace, feeling the warmth of her body against mine."
        "Part of me still can't believe this is actually happening."
        "Emma's real, not a figment of my imagination or a half-remembered dream."
        "And better than that, she's going to be my wife!"
        show emma kiss -close
        $ emma.flags.kiss += 1
        "Without warning, I feel her lips press against mine."
        "We kiss with genuine passion, almost with desperation."
        "And it's like neither of us wants that embrace to end."
        $ emma.set_fiance()
    else:
        show emma annoyed
        emma.say "Oh, [hero.name]!"
        emma.say "I'm so sorry - but I can't marry you!"
        "I find myself blinking and shaking my head in confusion."
        mike.say "Wh..."
        mike.say "What do you mean, Emma?"
        mike.say "You're the girl of my dreams!"
        mike.say "Aren't we supposed to be together?"
        show emma normal
        $ emma.love -= 10
        $ emma.sub -= 10
        emma.say "But we ARE together, [hero.name]!"
        emma.say "I don't remember anything in your dream saying we had to be married!"
        "I glance around, beginning to feel like a fool."
        "Emma's right, nothing was ever that specific."
        "Am I taking this whole dream thing too far?"
        "Have I let it cloud my judgement when it comes to our relationship?"
        show emma happy
        "Seeming to sense the confusion that's gripping me, Emma smiles."
        "She helps me to my feet, holding my hands tightly as she does so."
        emma.say "Don't get the wrong idea, [hero.name]."
        emma.say "I'm not saying I want to break-up with you."
        show emma normal
        emma.say "Just that I'm not ready for such a massive commitment just yet!"
        "I nod, still feeling more than a little shell-shocked."
        "But it doesn't take long for me to come round to her way of thinking."
        "I nod again, more firmly this time."
        mike.say "Y...yeah..."
        mike.say "Sorry, Emma!"
        mike.say "I guess I just got carried away!"
        emma.say "It's okay, [hero.name]."
        emma.say "It happens to us all."
    hide emma
    return

label emma_ask_fuck_date_male:
    if game.active_date.score >= (100 - emma.flags.drinks*5):
        if hero.stamina:
            mike.say "Do you want to come back to my place?"
            if emma.flags.dates == 1 or emma.flags.insists > 0:
                emma.say "I'm not ready for that just yet."
            elif emma.flags.dates == 2:
                emma.say "I think...no not yet."
            elif emma.flags.dates == 3:
                emma.say "You're a great guy, [hero.name], but I'm not ready for that."
            elif emma.flags.dates <= 5:
                emma.say "I...think maybe...Okay sure, just, um. Yeah okay!"
                return "hero"
            else:
                emma.say "Sure!"
                return "hero"
            menu:
                "I insist":
                    mike.say "I insist!"
                    show emma angry
                    emma.say "In that case definitely not!"
                    $ emma.flags.insists += 1
                "Okay. Next time?":
                    mike.say "Okay. Next time?"
                    emma.say "Maybe!"
                    if emma.flags.insists >= 1:
                        $ emma.flags.insists -= 1
        else:
            emma.say "It was really nice."
        return False
    else:
        emma.say "It was really nice."
        return False

label emma_ask_date_male:
    if Harem.find(emma):
        menu:
            "Ask Emma on a date":
                call emma_ask_date_alone_male from _call_emma_ask_date_alone_male
            "Ask Emma and Samantha on a date" if Harem.together(emma, samantha, name="friendly"):
                call emma_ask_date_emma_samantha from _call_emma_ask_date_emma_samantha
            "Meet Anna, Emma and Kat at the beach" if Harem.find_by_name("petite") and Harem.together(anna, emma, kat, name="petite") and "petite_harem_event_04_sex" in DONE and game.season in [0, 1]:
                call emma_ask_date_anna_kat from _call_emma_ask_date_anna_kat
    else:
        call emma_ask_date_alone_male from _call_emma_ask_date_alone_male_1
    return _return

label emma_ask_date_emma_samantha:
    mike.say "Do you want to get together with Samantha and have some fun?"
    if "emma_samantha_threesome" in DONE:
        emma.say "I'd love to."
        call select_date_time from _call_select_date_time_5
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            call emma_samantha_threesome_now_intro ("emma") from _call_emma_samantha_threesome_now_intro
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "friendly", ["emma", "samantha"], "emma_samantha_threesome_appointment_intro"))
    else:
        emma.say "I am sorry [hero.name], I'd prefer to have you for me alone."
        call emma_ask_date_alone_male from _call_emma_ask_date_alone_male_2
        return _return
    return

label emma_ask_date_anna_kat:
    mike.say "Do you want to have some fun at the beach with Anna and Kat?"
    emma.say "I'd love to."
    call select_date_time (fixed_hour=14, fixed_season="summer") from _call_select_date_time_30
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call petite_harem_foursome_intro from _call_petite_harem_foursome_intro_1
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "petite", ["anna", "emma", "kat"], "petite_harem_foursome_intro"))
    return

label emma_ask_date_alone_male:
    mike.say "Emma, would you like to go on a date with me?"
    if emma.flags.nodate and emma.flags.samgirlfriend:
        emma.say "I'd never do that to Samantha!"
        $ date_choice = False
    elif emma.love < 60 or emma.flags.nodate:
        emma.say "I don't see you that way, I'm sorry."
        $ date_choice = False
    else:
        if emma.love < 100 or emma.flags.dates < 3:
            emma.say "Sure, we can try that..."
        else:
            emma.say "Yes! When do you want to go?"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
