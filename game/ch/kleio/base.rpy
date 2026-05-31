

init python:
    Event(**{
    "name": "kleio_give_phone_number",
    "label": "give_phone_number",
    "girl": "kleio",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(kleio,
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
    "name": "kleio_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(15, 16),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "kleio",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kleio_auto_greet",
    "label": "auto_greet",
    "girl": "kleio",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(kleio,
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
    "name": "kleio_auto_chat",
    "label": "auto_chat",
    "girl": "kleio",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(kleio,
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
    "name": "kleio_are_you_sick",
    "label": "are_you_sick",
    "girl": "kleio",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (kleio, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "kleio_ask_out",
    "label": "ask_out",
    "girl": "kleio",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(kleio,
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
    "name": "kleio_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "kleio",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label kleio_bye(bye_outfit=None):
    call npc_bye_outfit (npc=kleio, bye_outfit=bye_outfit) from _call_npc_bye_outfit_11
    $ (day, h, activity, bye_outfit) = _return
    if not activity == kleio.activity:
        if day != game.week_day:
            $ kleio.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ kleio.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"kleio {bye_outfit}")
        if activity["activity"] == "sleep":
            kleio.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            kleio.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            kleio.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            kleio.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            kleio.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            kleio.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            kleio.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            kleio.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            kleio.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            kleio.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            kleio.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            kleio.say "I'll go get dressed."
        hide kleio
    return

label kleio_cheated(action, cheat_npc=None):
    show kleio
    if active_girl.id == "morgan" and Harem.together(kleio, active_girl):
        show fx heart
        $ kleio.sub += 1
    elif cheat_npc and Harem.together(cheat_npc, kleio):
        show kleio blush
        show fx heart
        kleio.say "I want some too!"
        show kleio kiss
        $ kleio.flags.kiss += 1
        "And without warning Kleio kisses me."
        $ kleio.love += 1
    else:
        show kleio angry
        show fx anger
        $ loss = 5
        if kleio.flags.girlfriend or kleio.flags.fiance:
            $ loss += 5
        $ kleio.love -= loss
        "I see Kleio looking at me [action] someone else angrily..."
    hide kleio
    return

label kleio_greet:
    if renpy.has_label(f"kleio_greet_dialogues_{hero.gender}") and not kleio.flags.greeted:
        scene expression f"bg {game.room}"
        $ kleio.flags.greeted = TemporaryFlag(True, 1)
        show kleio
        $ result = randint(1, 4)
        if result == 1:
            kleio.say "Hello, [hero.name]."
        elif result == 2:
            kleio.say "Hi, [hero.name]."
        elif result == 3:
            kleio.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                kleio.say "Good morning [hero.name]."
            elif game.hour < 19:
                kleio.say "Good afternoon [hero.name]."
            else:
                kleio.say "Good evening [hero.name]."
        call expression f"kleio_greet_dialogues_{hero.gender}" from _call_expression_242
        if kleio.flags.submissive_interact:
            if randint(0, 1) == 0:
                kleio.say "I hate that you made me say it, Loverboy - but I NEED your cock in me so bad!"
            else:
                kleio.say "Do you know what I want [hero.name]?"
                kleio.say "I want to feel you, inside me... Deep inside me!"
        hide kleio
    return

label kleio_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Kleio."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Kleio."
        elif game.hour < 12:
            mike.say "Good morning Kleio."
        elif game.hour < 19:
            mike.say "Good afternoon Kleio."
        else:
            mike.say "Good evening Kleio."
    return

label kleio_kiss:
    scene expression f"bg {game.room}"
    if kleio.love < 25 and not kleio.is_girlfriend and not game.active_date.score >= 75:
        show kleio
        "It happens so quickly that I hardly know what's going on."
        "One moment Kleio and I are laughing our asses off at some random, dumb shit."
        "The next I get a crazy impulse, and decide to act on it and to hell with the consequences."
        "I try to plant a kiss on Kleio's lips, just loving the way they look as she's laughing."
        "But I never even manage to get close enough to make it a reality."
        show kleio annoyed
        "Kleio stops me dead with a firm hand on my chest, her lips now twisted into an expression of serious displeasure."
        $ kleio.love -= 5
        $ kleio.sub -= 5
        hide kleio
    elif not kleio.flags.kiss:
        hide kleio
        $ kleio.love += 5
        if kleio.lesbian > MAX_LES_GUY_SEX:
            $ kleio.lesbian -= 1
        show kleio kiss
        "Whether I do this or not, there's a chance that I'll live to regret it."
        "If I do it, then I might regret it within the space of the next couple of minutes."
        "But if not, then I may well regret it for many years to come."
        "And I know which one is the worse prospect of the two."
        "That's why I go with my gut, and kiss Kleio full on the lips."
        "She jumps a little, then giggles with her lips against my own."
        "But then she gives in to the kiss, and my gamble seems to be paying off."
        hide kleio kiss
        $ kleio.flags.kiss += 1
    else:
        hide kleio
        $ kleio.love += 2
        show kleio kiss
        "There's nothing submissive or feminine about the way in which Kleio likes to be kissed."
        "That part of her personality that simply refuses to be dominated comes right to the fore."
        "But if you've never been embraced and kissed by a girl that's got so much passion, then you're missing out."
        "I just can't keep from thinking that here's a woman capable of busting a guy's balls."
        "And yet she's draping herself around me and letting herself be held and kissed without protest."
        "It's a turn on just to think of the next time I'll get to do it with her."
        hide kleio kiss
        $ kleio.flags.kiss += 1
    return

label kleio_propose_male:
    show kleio
    "Back when I first met her, if you'd told me that I'd end up in a position like this with Kleio..."
    "Well, let's just say that the very least I'd have done was laugh in your face for suggesting it."
    "But here I am, the weight of a ring feeling like it's the heaviest thing in the entire world."
    "My head a mess of worry and worst case scenarios, brain feeling like it's completely frazzled."
    "And all because I've convinced myself that the time is finally right to pop the question to Kleio."
    "No, wait - I take that last one back."
    "I honestly don't know if there would ever be a right time to propose to a girl like her."
    "And not least because there ARE no other girls like Kleio!"
    "Part of me's worried that she'll laugh in my face, or else toss the ring straight down a sewer-grate."
    "But there's a larger part of me that knows I'm crazy about her, quirks, spikey bits and all."
    "And if I don't pop the question, then I'll just be left wondering what might have been."
    "If it were almost any other girl, I'd have planned it down to the last second."
    "But with Kleio, all I can do is try to judge whether she's in a good enough mood."
    "And once I think she's there, throw caution to the wind and just do it..."
    "Which is why Kleio ends up turning her head one way, looking away from me."
    "But then finds me gone when she turns it back a couple of seconds later."

    show fx question
    kleio.say "Huh...what the fuck?"
    kleio.say "Where'd you go, Loverboy?"
    "Not exactly the way I'd envisioned this going down, I admit."
    "But what the hell - let's just go with it."
    mike.say "Ah..."
    mike.say "Down here, Kleio."
    "She looks down at this, eyes widening at the sight of me down on one knee."
    "My guess is that she must know what this is about, surely."
    "But all the same, I can see Kleio's not going to make this easy for me."
    show kleio annoyed
    kleio.say "What the hell are you doing?"
    kleio.say "You drop something?"
    kleio.say "Or did you find a really fascinating pile of dog turds?"
    "It's now that I choose to pull out the ring and hold it up to Kleio."
    "As there's nothing to be gained by firing back at her."
    "And so I just stick to the script in my head."
    mike.say "Ah...no, Kleio."
    mike.say "I...I wanted to ask if..."
    mike.say "If you'd marry me?"
    show kleio normal
    "For the first time that I can recall, Kleio actually looks lost for words."
    "Her eyes go wide as she stares down at me in silence."
    "All of which does nothing at all to help relieve my feelings of trepidation."
    "Or to stop the churning that I can feel in the pit of my stomach."
    if kleio.love < 195:
        show kleio sad
        kleio.say "Oh no..."
        kleio.say "Oh, [hero.name], no..."
        kleio.say "I thought you knew me better than that!"
        "I can already see that this thing is going pear-shaped on me."
        "And so I scramble to save something from the mess it's turning into."
        mike.say "I...I know this is all kind of sudden, Kleio."
        mike.say "But you can think about it if you like."
        mike.say "There's no law against taking some time before you say yes!"
        "Kleio shakes her head at me, looking this way and that in clear embarrassment."
        "The next thing I know, she's gotten hold of my wrists and is pulling me to my feet."
        show kleio annoyed
        kleio.say "Will you stop - you're showing the both of us up!"
        kleio.say "And put that damn thing away too!"
        "I can't help looking at her in askance as she says this, my mouth hanging open."
        "But then I shake off the surprise of her rejection and begin to stuff the ring back into my pocket."
        mike.say "Yeah...of course..."
        mike.say "I...I don't know what I was thinking, Kleio."
        mike.say "I'm so sorry..."
        show kleio sad
        "When I look into her eyes again, I can see an odd, unfamiliar emotion in them."
        "It's almost as though Kleio actually regrets what she did."
        "Like she knows how much her harsh words hurt me just now."
        kleio.say "Look, [hero.name]...I'm...sorry, okay?"
        kleio.say "I could have handled that better."
        "I nod slowly, still feeling the sting of her rejection."
        "But I also know how hard it is for Kleio to admit she's wrong."
        mike.say "It's okay, Kleio."
        mike.say "I'm not the first guy to get turned down."
        mike.say "And I won't be the last."
        show kleio normal
        kleio.say "Hey, this doesn't mean I'm dumping you, Loverboy!"
        kleio.say "At least, it doesn't have to..."
        kleio.say "I mean...I don't want it to!"
        "I nod again, not totally prepared for what's happening right now."
        mike.say "I hear you, Kleio."
        mike.say "I guess I just need a little time for the sting to fade, that's all."
        "Kleio smiles at this, but I can see the pain and worry in her eyes."
        "And I can't do anything to reassure her, as I was being honest when I said that just now."
        $ kleio.love -= 25
        $ kleio.sub -= 25
    else:
        "Kleio takes me completely by surprise as she makes a grab for the ring."
        "She practically snatches it out of the box and rams it onto her finger."
        "And then she holds it up like a trophy, waving her hand in the air the whole time."
        show kleio happy
        kleio.say "HAH...YES...YES!"
        kleio.say "Someone DOES want to marry me!"
        kleio.say "In your face Mom...shove it Dad..."
        "She stops dead as she realises that I'm staring at her in shock."
        "Slowly, Kleio lowers her hand."
        "But I note that she still holds the ring against her chest."
        "Almost as if she's afraid someone might take it away from her."
        kleio.say "What?!?"
        kleio.say "Can't a girl be happy a guy wants to marry her anymore?!?"
        mike.say "Y...yeah, Kleio, I guess it's okay."
        mike.say "I just kind of thought you might have a problem with it."
        mike.say "After all, you're not exactly the traditional kind of girl, are you?"
        show kleio blush
        "Kleio looks back at me with wide eyes, her cheeks actually flushing with colour."
        "Is she embarrassed, this tough, uncompromising girl that I've come to adore so much?"
        kleio.say "Well..."
        kleio.say "Maybe I just met someone that was worth making an exception for..."
        "I raise an eyebrow, intrigued by the implications of what she's saying."
        mike.say "Kleio, does that mean what I think it means?"
        mike.say "Is your answer yes?"
        "Kleio's cheeks are now burning red, and all she can do is nod her head quickly."
        "It's kind of strange that, even now, she can't force herself to actually come out and say it."
        "But what the hell do I care about hearing her say the word out loud?"
        "I want to have her in my life, weird habits, hang-ups and all."
        "And I've discovered that the good in her outweighs the bad by a long measure."
        mike.say "Kleio, you just made me the happiest guy in the world!"
        show kleio normal
        "The unguarded schmaltz of this pronouncement makes some of the colour fade from Kleio's cheeks."
        "And I can see that she's regained some of her usual composure as well."
        kleio.say "I call bullshit, Loverboy!"
        kleio.say "But I can make you as happy as I possibly can."
        kleio.say "And that's a fucking promise!"
        show kleio happy
        show fx heart
        "The next thing I know, she's gotten hold of my wrists and is pulling me to my feet."
        "Kleio wraps her arms around my waist and pulls me close to her."
        "And I return the embrace, relieved to have pulled it off and excited at what our future might hold..."
        $ kleio.set_fiance()
    hide kleio
    return

label kleio_ask_date_male:
    if Harem.find_by_name("band") and Harem.find_by_name("band").is_active(kleio):
        menu:
            "Ask Kleio on a date":
                call kleio_ask_date_alone_male from _call_kleio_ask_date_alone_male
            "Meet Kleio and Anna for a 'hot coffee'" if Harem.together(anna, kleio, name="band"):
                mike.say "Do you want to get together with Anna and have some fun?"
                kleio.say "I'd love to."
                call select_date_time from _call_select_date_time_7
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day == "now":
                    call kleio_anna_threesome from _call_kleio_anna_threesome_3
                else:
                    $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna"], "kleio_anna_threesome"))
                return
            "Meet Kleio, Anna and Sasha for a 'hot coffee'" if Harem.together(anna, kleio, sasha, name="band"):
                mike.say "Do you want to get together with Anna and Sasha and have some fun?"
                kleio.say "I'd love to."
                call select_date_time from _call_select_date_time_8
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                menu:
                    "See you in Sasha's room":
                        if day == "now":
                            call kleioannafoursome from _call_kleioannafoursome_1
                        else:
                            $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome"))
                    "Let's meet in my room" if "kleioannafoursome2" in DONE:
                        if day == "now":
                            call kleioannafoursome2 from _call_kleioannafoursome2_2
                        else:
                            $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome2"))
                return
    else:
        call kleio_ask_date_alone_male from _call_kleio_ask_date_alone_male_1
    return _return

label kleio_ask_date_alone_male:
    mike.say "Kleio, would you like to go on a date with me?"
    if kleio.love < 50 or kleio.flags.nodate:
        kleio.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        kleio.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
