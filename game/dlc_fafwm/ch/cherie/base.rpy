init python:
    Event(**{
    "name": "cherie_give_phone_number",
    "label": "give_phone_number",
    "girl": "cherie",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(cherie,
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
    "name": "cherie_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "cherie",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(cherie,
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
    "name": "cherie_auto_greet",
    "label": "auto_greet",
    "girl": "cherie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(cherie,
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
    "name": "cherie_auto_chat",
    "label": "auto_chat",
    "girl": "cherie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(cherie,
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
    "name": "cherie_are_you_sick",
    "label": "are_you_sick",
    "girl": "cherie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(cherie,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (cherie, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "cherie_ask_out",
    "label": "ask_out",
    "girl": "cherie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(cherie,
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
    "name": "cherie_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "cherie",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(cherie,
            Not(IsHidden()),
            IsPresent(),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label cherie_greet:
    if renpy.has_label(f"cherie_greet_dialogues_{hero.gender}") and not cherie.flags.greeted:
        scene expression f"bg {game.room}"
        show cherie normal
        $ cherie.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        show cherie happy
        if result == 1:
            cherie.say "Hello, [hero.name]."
        elif result ==2:
            cherie.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                cherie.say "Good morning [hero.name]."
            elif game.hour < 19:
                cherie.say "Good afternoon [hero.name]."
            else:
                cherie.say "Good evening [hero.name]."
        show cherie normal
        call expression f"cherie_greet_dialogues_{hero.gender}" from _call_expression_529
        hide cherie
    return

label cherie_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Cherie."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Cherie."
        elif game.hour < 12:
            mike.say "Good morning Cherie."
        elif game.hour < 19:
            mike.say "Good afternoon Cherie."
        else:
            mike.say "Good evening Cherie."
    return

label cherie_bye(bye_outfit=None):
    call npc_bye_outfit (npc=cherie, bye_outfit=bye_outfit) from _call_npc_bye_outfit_26
    $ (day, h, activity, bye_outfit) = _return
    if not activity == cherie.activity:
        if day != game.week_day:
            $ cherie.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ cherie.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"cherie {bye_outfit}")
        show cherie talkative
        if activity["activity"] == "sleep":
            cherie.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            cherie.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            cherie.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            cherie.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            cherie.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            cherie.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            cherie.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            cherie.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            cherie.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            cherie.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            cherie.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            cherie.say "I'll go get dressed."
        elif activity["activity"] in ["rest"]:
            cherie.say "I'm a little tired, I'll take a little nap."
        elif activity["activity"] in ["golf"]:
            cherie.say "I'll got to the golf course."
        show cherie normal
        hide cherie
    return



































label cherie_kiss:
    scene expression f"bg {game.room}"
    show cherie normal
    "I feel like the moment is right, like things are happening naturally between us."
    show cherie normal close
    if cherie.love + hero.charm < 80 and not cherie.is_girlfriend and not game.active_date.score >= 75:
        "But when I lean in closer and begin to close my eyes, my lips only manage to brush Cherie's."
        "And that's because the moment we make contact, she stiffens and pulls away."
        show cherie stuned
        "Which leaves me hanging there, totally exposed and feeling like a complete fool."
        "I do the best I can to recover, sitting up and trying not to turn bright red with embarrassment."
        show cherie annoyed -close
        $ cherie.love -= 1
        "But what's worse is the way that Cherie seems to be totally ignoring me right now."
        "As if she can't deal with the situation or stand to even look me in the eye."
        "All of which only serves to add to the sense of shame that's filling me from head to toe."
        hide cherie
    elif not cherie.flags.kiss:
        hide cherie
        show cherie kiss
        with fade
        "A feeling that's confirmed when I feel Cherie's lips there to meet mine."
        "Everything just flows from there, and the kiss that results is totally mind-blowing."
        "I'm enjoying the sensations immensely, just gently easing myself into it."
        "But Cherie catches me off-guard a moment later by sliding her tongue into my mouth."
        "And from there the complexion of the kiss becomes ever more intense and passionate."
        "I might have been the one that initiated it, but she's now seemingly taken over entirely."
        "Not that I'm complaining for an instant, as the experience is totally thrilling."
        $ cherie.love += 5
        $ cherie.flags.kiss += 1
        if cherie.lesbian > MAX_LES_GUY_SEX:
            $ cherie.lesbian -= 1
        "I'm just happy to lie back and let her take whatever she wants."
        "And to endure this treatment until she decides that it's time is done."
        hide cherie kiss
        show cherie normal
        with fade
    else:
        hide cherie
        show cherie kiss
        with fade
        $ cherie.love += 2
        $ cherie.flags.kiss += 1
        if cherie.lesbian > MAX_LES_GUY_SEX:
            $ cherie.lesbian -= 1
        "If the first time kissing Cherie was awkward, she soon makes up for it."
        "Because now she seems to want to kiss me whenever and wherever the chance arises."
        "And we're not talking about chaste little pecks either, but long and passionate affairs."
        "Cherie places her hands on the side of my head and kisses me life her life depends on it."
        "Each one seeming to last longer and feel more intense than the last."
        hide cherie kiss
        show cherie normal
        with fade
    return









label cherie_cheated(action, cheat_npc=None):
    if cheat_npc and Harem.together(cheat_npc, cherie):
        show cherie happy blush
        cherie.say "Aren't you forgetting something?"
        show cherie normal
        "And without warning Cherie kisses me."
        $ cherie.love += 1
        $ cherie.flags.kiss += 1
    else:
        show cherie angry
        "The moment I open my eyes, I see Cherie, staring at me in horror!"
        show cherie normal
    return

label cherie_propose_male:
    show cherie a normal
    "I can feel the butterflies in my stomach as I wait for the right moment."
    "Part of me wants to turn and run away or forget all about the idea."
    "But another part of me knows that I'd never be able too forgive myself if I did that."
    "So I take a deep breath and thrust my hand into my pocket."
    "Because it looks like the perfect moment just arrived."
    "Getting down on one knee, I get ready to recite the line that I've been practicing."
    show cherie a stuned
    "Of course Cherie looks more than a little puzzled as she watches me."
    show cherie a surprised
    cherie.say "[hero.name], what are you..."
    show cherie a stuned
    "But then she seems to realise what's going on in front of her."
    show cherie b surprised blush
    cherie.say "Oh my goodness, are you really going to..."
    cherie.say "Oh yes, yes you are!"
    show cherie b stuned
    "The truth is that I can hardly hear a word Cherie's saying right now."
    mike.say "Cherie, will you..."
    mike.say "Will you marry me?"
    "I pull the ring out of my pocket and open the little box it came in."
    "Then I hold it up for her to see."
    "All the time hoping that she's not put off by the meagre size of the stone set into it."
    "I'm looking up at Cherie with hope in my eyes, waiting for her response."
    "And with each passing second I'm hoping that she's going to speak up soon."
    "Because if she doesn't, we're going to start attracting a crowd!"
    if cherie.love >= 195:
        "It takes me a moment to realise that Cherie's head is moving."
        "But somehow that manages to reach me far more effectively than her words."
        "Though when I see that she's nodding, I almost lose it all over again."
        show cherie happy
        cherie.say "Yes, [hero.name]..."
        cherie.say "Of course I will marry you!"
        show cherie a
        cherie.say "Please, put the ring on my finger - right now!"
        show cherie a smile
        "I'm totally surprised by the way Cherie thrusts her hand towards me."
        "And it's a miracle that I manage to leap up and do as she says."
        "But once the ring is firmly on her finger, reality starts to hit me."
        mike.say "Whoa..."
        mike.say "Wait..."
        mike.say "You said yes?"
        mike.say "You said yes!"
        "Cherie nods as I begin to do a little dance on the spot."
        "It's like the joy I'm feeling needs to be released somehow."
        "And doing a stupid jig is the only way that I can think of."
        show cherie happy
        cherie.say "Of course I said yes, [hero.name]."
        cherie.say "What else could I say!"
        show cherie smile
        mike.say "Well, I was worried, you know?"
        mike.say "What with you being married before, and him being such a jerk and all..."
        hide cherie
        show cherie kiss
        with fade
        "Cherie stops my questions with a kiss, totally wiping them from my mind."
        "Because while she's doing that, I'm incapable of doing anything else at all."
        $ cherie.set_fiance()
    else:
        "It takes me a moment to realise that Cherie's head is moving."
        "But somehow that manages to reach me far more effectively than her words."
        "Though when I see that she's shaking it from side to side, I'm totally devastated."
        show cherie whining
        cherie.say "No, [hero.name]..."
        $ cherie.love -= 25
        $ cherie.sub -= 25
        show cherie talkative
        cherie.say "I'm sorry, but the answer is no."
        show cherie sad
        "Suddenly I feel like the biggest idiot on the face of the earth."
        "I'm already getting back to my feet as Cherie says this."
        "And engaged in the act of clumsily shoving the ring back into my pocket."
        mike.say "Oh..."
        mike.say "Okay, Cherie..."
        mike.say "I guess I should have seen that one coming!"
        mike.say "I'm...I'm sorry I asked..."
        "Cherie reaches out, taking hold of my hand."
        show cherie whining
        cherie.say "No, [hero.name], please don't say that!"
        show cherie talkative
        cherie.say "It's nothing at all to do with you."
        show cherie whining
        cherie.say "It's because I don't have a lot of success when it comes to being married."
        show cherie talkative
        cherie.say "Things between Dwayne and me did not work out, you know?"
        show cherie whining
        cherie.say "So with you, I want it to be different."
        show cherie sadsmile
        "I do the best I can to nod in agreement."
        "Because what Cherie's saying makes perfect sense."
        "Or at least it would if I hadn't just been turned down in public."
        "Maybe once I've had a chance to recover, I'll agree with the sentiment."
        "Just not right here and right now."
    hide cherie
    return

label cherie_ask_date_male:






    call cherie_ask_date_alone_male from _call_cherie_ask_date_alone_male
    return _return

label cherie_ask_date_alone_male:
    mike.say "Cherie, would you like to go on a date with me?"
    if cherie.flags.nodate:
        cherie.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        cherie.say "Sure, it might be fun, when do you want us to go?"
        return True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
