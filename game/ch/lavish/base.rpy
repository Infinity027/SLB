init python:
    Event(**{
    "name": "lavish_give_phone_number",
    "label": "give_phone_number",
    "girl": "lavish",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(lavish,
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
    "name": "lavish_send_text",
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
        PersonTarget(lavish,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "lavish",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "lavish_auto_greet",
    "label": "auto_greet",
    "girl": "lavish",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(lavish,
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
    "name": "lavish_auto_chat",
    "label": "auto_chat",
    "girl": "lavish",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(lavish,
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
    "name": "lavish_are_you_sick",
    "label": "are_you_sick",
    "girl": "lavish",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(lavish,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (lavish, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "lavish_ask_out",
    "label": "ask_out",
    "girl": "lavish",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(lavish,
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
    "name": "lavish_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "lavish",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(lavish,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label lavish_bye(bye_outfit=None):
    call npc_bye_outfit (npc=lavish, bye_outfit=bye_outfit) from _call_npc_bye_outfit_13
    $ (day, h, activity, bye_outfit) = _return
    if not activity == lavish.activity:
        if day != game.week_day:
            $ lavish.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ lavish.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"lavish {bye_outfit}")
        if activity["activity"] == "sleep":
            lavish.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            lavish.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            lavish.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            lavish.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            lavish.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            lavish.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            lavish.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            lavish.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            lavish.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            lavish.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            lavish.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            lavish.say "I'll go get dressed."
        hide lavish
    return

label lavish_cheated(action, cheat_npc=None):
    show lavish
    if cheat_npc and Harem.together(cheat_npc, lavish):
        show lavish flirt
        lavish.say "Aren't you forgetting something?"
        show lavish
        "And without warning Lavish kisses me."
        $ lavish.love += 1
        $ lavish.flags.kiss += 1
    elif lavish.sub >= 75:
        show fx heart
        $ lavish.sub += 1
        "I see Lavish looking at me [action] someone else with envy and lust in her eyes."
    else:
        show fx anger
        $ loss = 5
        if lavish.flags.girlfriend or lavish.flags.fiance:
            $ loss += 5
        $ lavish.love -= loss
        "I see Lavish looking at me [action] someone else with a sad look on her face..."
    hide lavish
    return

label lavish_greet:
    if renpy.has_label(f"lavish_greet_dialogues_{hero.gender}") and not lavish.flags.greeted:
        scene expression f"bg {game.room}"
        $ lavish.flags.greeted = TemporaryFlag(True, 1)
        show lavish
        $ result = randint(1, 3)
        if result == 1:
            lavish.say "Hello, [hero.name]."
        elif result == 2:
            lavish.say "Hi, [hero.name]."
        elif result == 3:
            lavish.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                lavish.say "Good morning [hero.name]."
            elif game.hour < 19:
                lavish.say "Good afternoon [hero.name]."
            else:
                lavish.say "Good evening [hero.name]."
        call expression f"lavish_greet_dialogues_{hero.gender}" from _call_expression_246
        if lavish.flags.submissive_interact:
            if randint(0, 1) == 0:
                lavish.say "I'm one hundred percent professional, [hero.name] - when it comes to pleasing you."
            else:
                lavish.say "You know [hero.name]..."
                lavish.say "I shouldn't probably say this kind of things..."
                lavish.say "I mean..."
                lavish.say "I don't know how to react, the thing is... I want you... Now!"
        hide lavish
    return

label lavish_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Lavish."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Lavish."
        elif game.hour < 12:
            mike.say "Good morning Lavish."
        elif game.hour < 19:
            mike.say "Good afternoon Lavish."
        else:
            mike.say "Good evening Lavish."
    return

label lavish_ask_date_male:



    call lavish_ask_date_alone_male from _call_lavish_ask_date_alone_male
    return _return

label lavish_ask_date_alone_male:
    mike.say "Lavish, would you like to go on a date with me?"
    if lavish.love <= 60:
        lavish.say "I don't think that would be appropriate, [hero.name]!"
        if lavish.flags.sleaze < 10:
            $ lavish.flags.sleaze += 1
        $ date_choice = False
    elif lavish.flags.nodate:
        lavish.say "I would like to, but I think we might get in trouble."
        if lavish.flags.sleaze < 10:
            $ lavish.flags.sleaze += 1
        $ date_choice = False
    else:
        lavish.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice

label lavish_kiss:

    scene expression f"bg {game.room}"
    show lavish
    if lavish.flags.nokiss or (lavish.love + hero.charm < 80 and not lavish.is_girlfriend and not game.active_date.score >= 75):
        "Really, what else was I supposed to think?"
        "I've caught Lavish gazing at me so many times since she started working with me in the office."
        "Always with those huge, innocent eyes looking at me so intently."
        "And then darting away again the moment that she realises I've noticed her watching me."
        "And the blushes that spread across her cheeks when she does that too!"
        "So when we're alone together, and I feel the time is right - why wouldn't I lean in and try to kiss her?"
        "It's always a gamble when someone's not laid it on the line and told you their intentions."
        "But isn't being prepared to take that leap a good thing?"
        "Well, evidently not in this particular case, as all it earns me is a flat palm meeting my questing lips."
        "She ducks underneath me and twists deftly out of the way."
        "Before I can recover my balance, let alone explain or even think of apologising, Lavish is gone."
        "So there I am, left all alone and wondering how I could have misread her coy glances as badly as I just did."
        "Have I crossed a line with Lavish thanks to what I just tried to do?"
        "Is she on her way to HR right now, setting the wheels in motion for my ultimate downfall?"
        $ lavish.love -= 1
    else:


        hide lavish
        show lavish kiss
        if lavish.lesbian > MAX_LES_GUY_SEX:
            $ lavish.lesbian -= 1
        if not lavish.flags.kiss:
            $ lavish.love += 5
            "I feel so self-conscious as I reach out to take Lavish's hand."
            "But as she looks up at me in response, I suddenly feel much of my trepidation being washed away."
            "She's just so different to the other women that I work with."
            "So quiet and retiring that I almost failed to see how utterly beautiful she actually is."
            if Person.is_not_hidden("aletta") and Person.is_not_hidden("audrey") and Person.is_not_hidden("shiori"):
                "Lavish isn't loud and arrogant like Aletta, manipulative like Audrey or needy like Shiori."
            "But the most amazing thing of all is that she actually seems to be genuinely attracted to me."
            "There's no freaky behaviour or emotional bullshit involved either."
            "Tentatively, I reach out and smooth her hair away from her eyes with my other hand."
            "But she surprises me by gently taking hold of it and pressing it to her lips."
            "Encouraged by this show of affection, I lean in and kiss her softly."
            "Lavish sighs happily, returning the kiss with equal tenderness."
            "Only when I feel her arms wrap themselves around me do I dare to kiss her with more vigour."
            "She folds herself into me almost totally, the rest of the world seeming to fade away into nothingness."
            "Really, while I'm holding her and feeling her lips against mine like this, what else is there?"
            "I honestly don't know what turns me on more about her..."
            "The fact that she's finally mine to hold and kiss, or the feeling of her amazing body as she moves against me."
            "Either would be incredible, but both together is almost enough to blow my mind."
        else:
            $ lavish.love += 2
            "I manage to catch Lavish gently around the waist as she walks past me."
            "She's not expecting it, and suddenly finds herself pulled into my arms and looking me in the eye."
            "Her cheeks flush with colour at the surprise of it all, but she's smiling all the same and not fighting me in the slightest."
            "I pause for a couple of seconds, enjoying the sensation of her body pressed against mine and the smell of her hair so close to me."
            "As I finally kiss her, I can feel Lavish knot her hands at the base of my spine and hold onto me."
            "It's such a small gesture to look at, but I know that it's just her own subtle way of returning my affections, of binding herself to me."
            "I really should keep this whole thing brief, but in that moment, she comes alive in my arms."
            "Lavish's tongue darts between my lips, as though she's only now realised how much she wants to be kissed and is afraid of the chance being taken away from her."
            "When I make the mistake of trying to ease off before ending the kiss, she makes a sighing noise, almost like a distressed puppy and tries to press herself on me with yet more intensity."
            "What can I do in the face of that, knowing that she's so keen to keep herself in my arms?"
            "All I can do is return her affections with the same amount of enthusiasm."
        $ lavish.flags.kiss += 1
    hide lavish kiss
    return

label lavish_propose_male:
    show lavish
    "I'm super paranoid and on edge about what I have to do today."
    "I need it all to go right or else I'm sure everything will go wrong."
    "I've picked out what I think is the perfect ring for the occasion."
    "And I've chosen a moment to pop the question that seems just right."
    "With so much care and attention paid to the details, how can I fail?"
    "Now all I have to do is just get down on one knee."
    "Get down on one knee and actually ask Lavish to marry me!"
    lavish.say "And so I said as much to her."
    lavish.say "I just told her they don't pay me enough to do that!"
    show lavish annoyed
    lavish.say "[hero.name]?"
    lavish.say "Are you even listening to me?!?"
    "I can feel myself almost shaking from nerves as I get down on one knee."
    "Hasn't it occurred to Lavish yet?"
    "What I'm doing right in front of her?"
    mike.say "Lavish..."
    mike.say "Will you..."
    mike.say "Will you marry me?"
    show lavish surprised
    "Finally it seems to dawn on Lavish what's happening here."
    "Her eyes go wide and she claps her hands over her mouth."
    "I'm going to take the surprise and shock as a good sign."
    "And so I keep on smiling up at her the whole time."
    "I mean, she has to give me an answer soon, right?"
    if lavish.love < 195:
        show lavish normal
        lavish.say "Oh, [hero.name]!"
        lavish.say "That's so sweet of you!"
        "I nod, thinking that there must be more to come."
        "What Lavish just said sounds pretty positive to me."
        "But there wasn't actually a yes in there."
        "At least not one that I heard."
        lavish.say "But you already know that I can't marry you!"
        mike.say "I...I do?"
        show lavish happy
        "Lavish lets out a giggle and shakes her head."
        lavish.say "Of course I can't!"
        show lavish normal
        lavish.say "Do you even know how much time getting married would take?"
        lavish.say "How much of my focus it would take away from my working life?"
        lavish.say "It would totally alter the trajectory I have worked out for my career!"
        mike.say "It...it would?"
        lavish.say "Sure it would, [hero.name]!"
        lavish.say "I always swore that I'd be an executive before I became a wife."
        lavish.say "And that's why I'm going to write this off as a token gesture."
        "What does she mean by that?"
        mike.say "Huh?"
        lavish.say "You know, [hero.name] - a way to show how much you love me."
        lavish.say "But one where I can say no without any consequences."
        lavish.say "Because we both know that we couldn't have got married anyway!"
        "I nod my head slowly as I put the ring away and get to my feet."
        "In truth, I really don't think I understand what Lavish means."
        "She never actually said no."
        "But I'm pretty sure we're not getting married all the same."
        "Part of me thinks that I should be unhappy."
        "Maybe that I should even be more than a little pissed-off."
        "But I'm confused and Lavish seems to be happy with how it all played out."
        "So in the end, I just smile and go along with it."
        $ lavish.love -= 25
        $ lavish.sub -= 25
    else:
        show lavish happy
        lavish.say "Oh, [hero.name]!"
        lavish.say "Of course I will!"
        "I keep on smiling up at Lavish for a couple more seconds."
        "And that's because it takes so long for what she said to sink in."
        show lavish normal blush
        lavish.say "Ah, [hero.name]..."
        lavish.say "Please say something."
        lavish.say "You're starting to scare me!"
        "All of a sudden I seem to snap out of it."
        "I leap to my feet and begin putting the ring on Lavish's finger."
        mike.say "Sorry...sorry..."
        mike.say "You kind of took me by surprise there!"
        "Lavish looks at me with a quizzical expression on her face."
        show lavish annoyed -blush
        lavish.say "Erm..."
        lavish.say "I thought I was the one that's supposed to be surprised?"
        mike.say "I guess I was just worried you might say no, Lavish."
        mike.say "What with you being so devoted to your career."
        mike.say "I know how hard it is for a woman trying to get ahead."
        show lavish normal blush
        "Lavish smiles at this, blushing a little."
        "I can see that she's flattered by my understanding of her predicament."
        "But then she shakes her head."
        show lavish -blush
        lavish.say "I...I thought so too."
        lavish.say "But you showed me there's more to life than work."
        show lavish happy
        lavish.say "And who says I can't have a husband and a career?"
        "I can't help nodding with enthusiasm as Lavish says all of this."
        "As it puts to rest my fears that I rank lower than her climbing the corporate ladder."
        show lavish flirt
        lavish.say "After all, who says I have to be the one to give up work and raise the kids!"
        "Lavish laughs as my eyes pop open at this statement."
        "But I note that she doesn't tell me she's joking either!"
        $ lavish.set_fiance()
    hide lavish
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
