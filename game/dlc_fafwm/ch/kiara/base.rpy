init python:
    Event(**{
    "name": "kiara_give_phone_number",
    "label": "give_phone_number",
    "girl": "kiara",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(kiara,
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
    "name": "kiara_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "kiara",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(kiara,
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
    "name": "kiara_auto_greet",
    "label": "auto_greet",
    "girl": "kiara",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(kiara,
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
    "name": "kiara_auto_chat",
    "label": "auto_chat",
    "girl": "kiara",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kiara,
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
    "name": "kiara_are_you_sick",
    "label": "are_you_sick",
    "girl": "kiara",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(kiara,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (kiara, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kiara_ask_out",
    "label": "ask_out",
    "girl": "kiara",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(kiara,
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
    "name": "kiara_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "kiara",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(kiara,
            Not(IsHidden()),
            IsPresent(),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label kiara_greet:
    if not kiara.flags.greeted:
        scene expression f"bg {game.room}"
        show kiara
        $ kiara.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            kiara.say "Hello, [hero.name]."
        elif result ==2:
            kiara.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                kiara.say "Good morning [hero.name]."
            elif game.hour < 19:
                kiara.say "Good afternoon [hero.name]."
            else:
                kiara.say "Good evening [hero.name]."
        call expression f"kiara_greet_dialogues_{hero.gender}" from _call_expression_540
        hide kiara
    return

label kiara_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Kiara."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Kiara."
        elif game.hour < 12:
            mike.say "Good morning Kiara."
        elif game.hour < 19:
            mike.say "Good afternoon Kiara."
        else:
            mike.say "Good evening Kiara."
    return

label kiara_bye(bye_outfit=None):
    call npc_bye_outfit (npc=kiara, bye_outfit=bye_outfit) from _call_npc_bye_outfit_28
    $ (day, h, activity, bye_outfit) = _return
    if not activity == kiara.activity:
        if day != game.week_day:
            $ kiara.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ kiara.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"kiara {bye_outfit}")
        if activity["activity"] == "sleep":
            kiara.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            kiara.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            kiara.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            kiara.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            kiara.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            kiara.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            kiara.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            kiara.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            kiara.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            kiara.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            kiara.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            kiara.say "I'll go get dressed."
        hide kiara
    return

label kiara_kiss:
    scene expression f"bg {game.room}"
    show kiara
    "I feel like the energy between Kiara and myself is building to a peak right now."
    "Like when you rub a balloon against your sweater and the static is ready to discharge."
    "Hell, I could believe that my hair is actually standing on end from the sensation of it."
    "And the only thing that I can do to bleed it off is to lean in close and pucker my lips."
    "Because a kiss is the equivalent of a lightning rod in this situation."
    show kiara close
    "Something sure to drawn off the energy and the natural progression of one moment to the next."
    "And at the same time I can feel my heart beginning to beat faster inside of my chest."
    "I can feel the pressure building in my ears, threatening to make them burst."
    "Hell, I swear that I can even feel the blood pulsing in my veins!"
    if kiara.love + hero.charm < 80 and not kiara.is_girlfriend and not game.active_date.score >= 75:
        scene bg black with fade
        "So I close my eyes, preparing myself for the moment that our lips finally touch."
        "But instead of feeling Kiara's lips against mine, there's something else there instead."
        "It's thinner and being pressed into them with just enough force to make me open my eyes."
        scene expression f"bg {game.room}"
        show kiara surprised
        "And when I do, I see that it's the index finger of Kiara's hand."
        "Puzzled and disoriented, my eyes struggle to focus on it."
        show kiara angry
        $ kiara.love -= 1
        kiara.say "No, no, no, [hero.name]..."
        kiara.say "No kisses for you right now!"
        kiara.say "But maybe later, when the time is right."
        "I nod as Kiara pulls her finger away, feeling more than a little humiliated."
        "All I can do is take note of the mischievous grin on her face right now."
        "One that suggests she was amused by my attempt to kiss her, rather than offended."
        hide kiara
    elif not kiara.flags.kiss:
        hide kiara
        show kiara kiss
        with dissolve
        "As soon as Kiara's lips touch my own, the electricity between us is released."
        "I feel like every muscle in my body is suddenly charged with that same energy."
        "And there's nothing on my mind but leaning into the kiss and making it still more intense."
        $ kiara.love += 5
        $ kiara.flags.kiss += 1
        if kiara.lesbian > MAX_LES_GUY_SEX:
            $ kiara.lesbian -= 1
        "All of this is made that much more powerful by the fact that there's no hesitation on Kiara's part."
        "Every move I make she matches or exceeds in her own eagerness."
        "In fact it doesn't take long for me to feel like she's the one in control!"
        "Kiara seems to demand more from me the longer that the kiss lasts too."
        "And in the end it's almost like I need to surface for air in order to survive!"
        "But even when I break away for a moment, she doesn't stop kissing me."
        "Instead planting gentler kisses on my lips and sighing with contentment."
        hide kiara kiss
    else:
        hide kiara
        show kiara kiss
        $ kiara.love += 2
        $ kiara.flags.kiss += 1
        if kiara.lesbian > MAX_LES_GUY_SEX:
            $ kiara.lesbian -= 1
        "After the intensity of that first kiss, it becomes natural to be so intimate with Kiara."
        "And she doesn't hesitate to place her lips against mine whenever the urge takes her."
        "But these kisses are gentler and more relaxed, at least to begin with."
        "The same smouldering heat and desire is always there in the background."
        "It's held back at the start, like we're doing all we can to remain calm."
        "Though the longer the kiss lasts, the harder it is to restrain ourselves."
        "And before long, the inevitable happens and the beast slips its chains."
        "From that point on there's not holding either of us back from our passion."
        "Lips part and tongues dart forth, as if we want to devour each other."
        "And I honestly think we'd be going at it like animals if there were no other witnesses!"
        hide kiara kiss
    return

label kiara_sleep_date_fuck:
    show cuddle kiara
    show bg black with dissolve
    "The both of us are asleep before we can even consider cleaning up."
    call sleep ("kiara") from _call_sleep_130
    $ game.room = "bedroom1"
    return

label kiara_cheated(action, cheat_npc=None):
    if cheat_npc and Harem.together(cheat_npc, kiara):
        show kiara flirt
        kiara.say "Aren't you forgetting something?"
        show kiara kiss
        "And without warning kiara kisses me."
        $ kiara.love += 1
        $ kiara.flags.kiss += 1
    else:
        show kiara angry
        "As soon as the kiss ends and I open my eyes, I see Kiara staring at me, a look of horror on her face."
    hide kiara
    return

label kiara_propose_male:
    show kiara
    "I always read about proposals in books and saw them play out in movies."
    "The nervous guy getting down on one knee in front of his prospective bride."
    "Getting out a ring and prosing while she blushes and acts like she's totally shocked."
    "So that's what I have in my head as I feel the moment is right for me to do the same."
    "I choose to do it when Kiara's half-distracted with something else."
    "So by the time she turns her attention back to me, I'm already on one knee."
    "And yeah, she looks pretty surprised right now, while I'm a bag of nerves."
    "So it's going just like in the movies and all of the books."
    show kiara surprised
    kiara.say "[hero.name]..."
    kiara.say "Are you doing what I think you're doing?"
    show kiara stuned
    "Kiara's question only serves to make my nerves that much worse."
    "As though she's trying to assert control over the situation."
    "And that send my brain into a spiral of panic."
    mike.say "Kiara..."
    mike.say "Will you..."
    mike.say "Will you marry me?"
    "Even though she looked like she knew the score, Kiara still seems shocked."
    "She gasps and blinks, looking this way and that."
    "And as she does so, the smile on my face begins to turn into a rictus."
    "Because I'm getting worried about just how long I'm going to be kneeling down here."
    if kiara.love >= 195:
        "Almost as soon as the words are out of my mouth, Kiara takes hold of my hand."
        "And then she almost pulls me to my feet in her efforts to bring the ring closer to herself."
        mike.say "Whoa..."
        mike.say "Steady on there!"
        "Before I can get myself balanced and steady, Kiara's wriggling her fingers."
        "Almost like she's trying to get the ring on there herself."
        mike.say "Kiara!"
        mike.say "Are you...are you saying yes?"
        "Kiara stops what she's doing and looks at me with a stunned expression."
        show kiara surprised at startle(0.1, 5)
        kiara.say "What?"
        show kiara smile
        kiara.say "Oh...oh yes!"
        kiara.say "Yes, I will marry you."
        show kiara flirt
        kiara.say "I am sorry, [hero.name], I just saw the ring and realised what it meant."
        kiara.say "Then I couldn't help myself, I just wanted to get it on my finger."
        kiara.say "Because it would mean that we are to be married!"
        show kiara smile
        "I'm nodding as I hastily slide the ring onto Kiara's finger."
        "Still kind of stunned that she'd be eager enough to forget herself."
        mike.say "Well there you go, Kiara..."
        mike.say "Now it's official - we're getting married!"
        "Kiara stares at the ring on her finger for a moment."
        "Almost like she doesn't believe it's real and it might vanish any moment."
        "Then she throws her arms around my neck and pulls me into a tight embrace."
        "The kiss that follows is long and intense, as we're both in a complete state."
        "But the reality of the situation is slowly beginning to sink in for me."
        "I asked the question and she said yes - Kiara and I are actually getting married!"
        $ kiara.set_fiance()
    else:
        show kiara serious with dissolve
        "Almost as soon as the words are out of my mouth, Kiara starts shaking her head."
        "And that's taking up so much of my attention that I hardly notice she's also taken a step backwards."
        "Out of sheer instinct, I begin to stand up and move after her."
        "But all this seems to do is make her move that much faster."
        mike.say "Kiara..."
        mike.say "Are you okay?"
        show kiara whining
        kiara.say "I..."
        kiara.say "I am in shock!"
        kiara.say "I was not prepared for this, [hero.name]."
        show kiara uninterested
        mike.say "Well, that's kind of the idea, you know?"
        show kiara serious
        mike.say "A surprise proposal?"
        "Kiara blinks at this, but she keeps on shaking her head."
        "Which pretty much sinks my hope that this is all because of the surprise element."
        show kiara whining
        kiara.say "Oh yes..."
        kiara.say "But I cannot do it, [hero.name]."
        kiara.say "I cannot marry you - this is not the right time."
        show kiara serious
        $ kiara.love -= 25
        $ kiara.sub -= 25
        "I can almost feel the sensation of my heart fracturing inside of my chest."
        "All of my hopes being crumpled up into a ball and tossed aside."
        "But somehow my brain seems to just keep trundling along."
        "And the smile that appears on my face is totally automatic."
        mike.say "Oh..."
        mike.say "Okay, Kiara - sorry about all that."
        "I feel myself stuffing the ring back into my pocket."
        "Doing the best I can to put a brave face on things."
        "I can see that Kiara looks concerned, but she doesn't say anything."
        "Instead we endure the most awkward moment that I can imagine."
        "All the while I'm wishing that the ground would open and swallow me up."
        "Anything to escape the feeling of hopeless dread that's hanging over me."
    hide kiara
    return

label kiara_ask_date_male:






    call kiara_ask_date_alone_male from _call_kiara_ask_date_alone_male_1
    return _return

label kiara_ask_date_alone_male:
    mike.say "kiara, would you like to go on a date with me?"
    if kiara.flags.nodate:
        kiara.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        kiara.say "Sure, it might be fun, when do you want us to go?"
        return True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
