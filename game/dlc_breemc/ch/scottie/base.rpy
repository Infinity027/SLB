init python:
    Event(**{
    "name": "scottie_give_phone_number",
    "label": "give_phone_number",
    "girl": "scottie",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(scottie,
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
    "name": "scottie_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(12, 13),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(scottie,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "scottie",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })


    Event(**{
    "name": "scottie_auto_chat",
    "label": "auto_chat",
    "girl": "scottie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(scottie,
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
    "name": "scottie_are_you_sick",
    "label": "are_you_sick",
    "girl": "scottie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(scottie,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (scottie, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "scottie_ask_out",
    "label": "ask_out",
    "girl": "scottie",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("ask_date"))
            ),
        PersonTarget(scottie,
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
    "name": "scottie_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "scottie",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(scottie,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label scottie_bye(bye_outfit=None):
    call npc_bye_outfit (npc=scottie, bye_outfit=bye_outfit) from _call_npc_bye_outfit_20
    $ (day, h, activity, bye_outfit) = _return
    if not activity == scottie.activity:
        if day != game.week_day:
            $ scottie.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ scottie.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"scottie {bye_outfit}")
        if activity["activity"] == "sleep":
            scottie.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            scottie.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            scottie.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            scottie.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            scottie.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            scottie.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            scottie.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            scottie.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            scottie.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            scottie.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            scottie.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            scottie.say "I'll go get dressed."
        hide scottie
    return

label scottie_cheated(action, cheat_npc=None):
    show scottie
    "I see Scottie looking at me [action] someone else with envy and lust in his eyes."
    $ scottie.love += 1
    hide scottie
    return

label scottie_beats_ryan_female:
    if randint(1, 100) <= 60:
        return "abort"
    "I can feel Ryan's lips against mine, his hands all over me."
    "I know that I should be stopping him, but it's so hard to resist!"
    scottie.say "[hero.name]?"
    scottie.say "Why are you kissing that creep?"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show scottie angry at right5
    show ryan angry at left5
    "At the sound of Scottie's voice, Ryan releases me from his grip."
    "I gasp and look around to see him standing there, a puzzled look on his face."
    bree.say "Scottie, I..."
    "But before I can try to explain myself, Ryan cuts me off."
    ryan.say "Don't worry about it, [hero.name]..."
    ryan.say "Just leave this simian throwback to me!"
    "I can't help gasping in surprise as Ryan squares up to Scottie."
    "I mean, I know he's confident, even kind of cocky."
    "But Scottie's way more beefy than him."
    "And he's a more physical kind of guy too."
    scottie.say "Who are you calling simian?"
    scottie.say "And what the hell does that even mean?!?"
    play sound punch_hard
    pause 0.2
    show scottie surprised with hpunch
    "Ryan answers the question by punching Scottie in the face."
    "Not square on, but kind of from the side, like a sucker punch."
    "Scottie's head snaps around, and then back again."
    "And he looks more confused than anything."
    "But I don't know if it's from pain or sheer surprise that Ryan hit him!"
    show scottie angry
    "Either way, Ryan doesn't get a chance to land a second blow."
    $ renpy.hide(f"{active_girl.id}")
    hide scottie
    $ renpy.show(f"scottie beats {active_girl.id}")
    "Scottie throws himself at Ryan, and the fight is on!"
    play sound punch_hard
    pause 0.2
    with hpunch
    "Actually, it's more of a one-sided beating than an actual fight."
    "Because it seems like Ryan's seriously out of his depth."
    play sound punch_hard
    pause 0.2
    with hpunch
    "Scottie keeps on punching and kicking him."
    play sound punch_hard
    pause 0.2
    with hpunch
    "And Ryan can't seem to do anything to hurt him in return."
    play sound spank
    with hpunch
    "The fight seems to end when Scottie lands a hard slap on Ryan's cheek."
    "This spins him around and sends him tumbling onto his butt."
    ryan.say "Ow..."
    ryan.say "That really hurt, you asshole!"
    scottie.say "Yeah, well...it was supposed to!"
    scottie.say "That's what happens when you mess with my [hero.name]."
    return

label scottie_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Scottie."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Scottie."
        elif game.hour < 12:
            bree.say "Good morning Scottie."
        elif game.hour < 19:
            bree.say "Good afternoon Scottie."
        else:
            bree.say "Good evening Scottie."
    return

label scottie_ask_date_female:



    call scottie_ask_date_alone_female from _call_scottie_ask_date_alone_female
    return _return

label scottie_ask_date_alone_female:
    if not scottie.flags.hadadate:
        bree.say "We've been having a great time hanging out together..."
        bree.say "Right, Scottie?"
        scottie.say "Huh?"
        scottie.say "Oh...yeah, [hero.name]."
        scottie.say "You're a lot of fun to be around!"
        "I swallow audibly, gathering my strength to go on."
        "I know that I have to get this next bit just right."
        bree.say "So I was thinking..."
        bree.say "Since we're getting on so well..."
        bree.say "Why don't we go someplace, just you and me?"
        bree.say "Like a specific place at a specific time?"
        "Scottie stares at me blankly for a moment."
        "And I think that I've pitched my question over his head."
        "But then he blinks and a light of recognition seems to come on behind his eyes."
        scottie.say "Oh...OH!"
        scottie.say "You mean like a date?"
        scottie.say "Right, [hero.name]?"
        bree.say "Yeah, Scottie - exactly like a date!"
    else:
        bree.say "You're doing something Scottie? Might want to go on a date with me perhaps?"
    if scottie.love < 50 or scottie.flags.nodate:
        if not scottie.flags.hadadate:
            scottie.say "Why didn't you just come right out and say it, [hero.name]?"
            scottie.say "That way I could have just told you no way!"
            scottie.say "This way you tortured my poor brain before you got there."
            scottie.say "Anyway, it's a no from me - I can't handle that level of commitment!"
            bree.say "What, like one lousy date?"
            scottie.say "It sure would be a lousy date for me!"
        else:
            scottie.say "Nope, can't do."
        $ date_choice = False
    else:
        scottie.say "Why didn't you just come right out and say it, [hero.name]?"
        scottie.say "Sure thing - a date sounds like a great idea!"
        scottie.say "You work out all the details, okay?"
        scottie.say "Then just let me know the time and the place."
        bree.say "That's great, Scottie...I think..."
        $ scottie.flags.hadadate = True
        $ date_choice = True
    return date_choice


label scottie_kiss_female:
    scene expression f"bg {game.room}"
    if scottie.love + hero.charm < 80 and not scottie.status in ["boyfriend", "sex slave"] and not game.active_date.score >= 75:
        show scottie
        if randint(0, 1) == 0:
            "Scottie quickly takes a step back, and turns away."
            if scottie.love < 40:
                scottie.say "Sorry but... I don't really feel comfortable with that."
                $ scottie.sub += 1
            else:
                $ result = randint(1, 2)
                if result == 1:
                    scottie.say "Sorry [hero.name], but let's just not."
                    $ scottie.love -= 1
                else:
                    scottie.say "I'm sorry, but I have to go..."
                "Before I can react, Scottie turns and rushes away."
        else:
            "I've been wanting to kiss Scottie for a while now, I have to admit."
            "Can you really blame me when he's such a hottie?"
            "And those muscles too!"
            "But yeah, a little bit of it is because I want to know what it's like."
            "And a part of me wants to know what Sasha was getting before they split up too!"
            "I mean...Sasha's not that much prettier than me, right?"
            "But when I swallow my fear and take a chance, Scottie throws me a curve-ball."
            "I'm smiling as I lean in towards him, my best and sweetest smile."
            "The one that almost always works with a guy too."
            show scottie at startle
            "But he jerks his head back, like he's been pricked with a pin!"
            "I feel a stab of rejection in my gut in that moment."
            "But I still do the best I can to cover it up and pretend nothing happened."
            $ scottie.love -= 1
            $ scottie.sub -= 1
        hide scottie
    elif scottie.love + hero.charm < 60 or game.active_date.score >= 75:
        if not scottie.flags.kiss:
            if randint(0, 1) == 0:
                hide scottie
                show scottie kiss
                with dissolve
                "I watch Scottie's eyes open wide in surprise, and for a moment I think he might back away, or even run, but slowly his eyelids close as he cautiously returns the affection."
                "His lips are remarkably soft, I can even taste a hint of strawberry as we meet."
                "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
                "No matter what comes next, something tells me that I will never forget this moment."
                hide scottie kiss
                if scottie.love >= 60:
                    show scottie
                    with dissolve
                    scottie.say "Um, I think we should talk about this later, alright?"
                else:
                    show scottie
                    with dissolve
                    scottie.say "Oh uh... I've got to go..."
                    "Before I can object, Scottie begins in the opposite direction."
                    "He seemed a little uncomfortable, did I do something wrong?"
            else:
                "I feel so guilty admitting that I'm getting the hots for Scottie."
                "I mean, he and Sasha are one hundred percent over, right?"
                "So it's not like I'm going behind her back with the guy, is it?"
                "Yeah, I know he's kinda dumb and he can he a jerk sometimes."
                "But can you really blame me when he's such a hottie?"
                "And those muscles too!"
                "But yeah, a little bit of it is because I want to know what it's like."
                "And a part of me wants to know what Sasha was getting before they split up too!"
                "I mean...Sasha's not that much prettier than me, right?"
                "I try to push all of that out of my mind as I lean in towards Scottie."
                hide scottie
                show scottie kiss
                with dissolve
                "Right up until the moment that our lips touch..."
                "And then I don't have to even try to clear my mind!"
                "He hesitates for a moment, taken my surprise."
                "But then Scottie realises what's happening, and he kisses me back!"
                "Oh god - it's everything I hope it would be."
                hide scottie kiss with dissolve
            $ scottie.flags.kiss += 1
        else:
            hide scottie
            show scottie kiss
            with dissolve
            "I take a step closer to Scottie, and rest my hands lightly on his shoulder."
            "For a brief moment he looks curious, but I catch sight of a moment of recognition in his eyes before my own drift shut."
            "I stop just short of meeting his lips, letting his lean forwards to meet mine, and letting his soft lips dance across mine at his pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on his lips before she tries to hide it, a blush covering his complexion."
            hide scottie kiss with dissolve
        $ scottie.love += 1
    else:
        if not scottie.flags.kiss:
            hide scottie
            show scottie kiss
            with dissolve
            "I feel my lips passing over Scottie's as we embrace, my hands resting comfortably on his hips while his own had ventured to my shoulders, looping around my neck."
            "As is, I feel particularly adventurous, and not only do I push into his embrace more than I have in the past, but also begin lightly tickling Scottie with my tongue."
            "For a moment, I'm not sure if he'll reciprocate, but I feel his lips parting and allowing me access."
            "I let myself inside his, exploring every crevice of his mouth in earnest even if he himself seems hesitant to return the treatment."
            "I let my eyes open to gauge his reaction, and although he seems rather tense, my ears pick up on a soft whimper of pleasure that tells me he's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste his on my tongue."
            hide scottie kiss
            if scottie.love >= 60:
                show scottie
                with dissolve
                scottie.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon his face through the thick blush that adorns his cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show scottie
                with dissolve
                scottie.say "Um... I should go..."
                "Before I can object, Scottie turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            if randint(0, 1) == 0:
                hide scottie
                show scottie kiss
                with dissolve
                if randint(1, 2) == 2:
                    "Yet again I feel my lips passing over Scottie's as we embrace, my hands resting comfortably on his hips while his own had ventured to my shoulders, looping around my neck."
                    "Today however, I feel particularly adventurous, and not only do I push into his embrace more than I have in the past, but also begin lightly tickling Scottie with my tongue."
                    "For a moment, I'm not sure if he'll reciprocate, but I feel his lips parting and allowing me access."
                    "I let myself inside his, my organ exploring every crevice of his mouth in earnest even if he himself seemed hesitant to return the treatment."
                    "I let my eyes open to gauge his reaction, and although he seems rather tense, my ears pick up on a soft whimper of pleasure that tells me he's at least enjoying the treatment."
                    "My eyes drift closed once more, and before long we part, although I can still taste his on my tongue."
                else:
                    "Once again I step in closer to Scottie, close enough that our bodies are very nearly touching."
                    "I bring one hand to Scottie's chin, tilting his up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                    "My tongue yet again pushes through the barrier that his lips form to begin exploring Scottie's mouth, while he cautiously met me, letting me lead the dance our tongues engaged in."
                    "Before long, we pulled away from one another, breathless."
                hide scottie kiss
                if hero.charm >= 160 - scottie.love:
                    show scottie
                    with dissolve
                    scottie.say "Stop doing that."
            else:
                hide scottie
                show scottie kiss
                with dissolve
                "Oh my...now I know what it's like to be kissed by Scottie!"
                "And it's like everything else about him - simple, wild and hot as hell!"
                "I don't think I've ever been kissed like this before."
                "It's like every time he's as passionate as the first time we kissed."
                "And at the same time he's trying to kiss me like it might be the last time too!"
                "I...I can't let Sasha see him kissing me like that!"
                "What would she think of me if she did?"
                "But...I can't resist the chance to kiss the big dope!"
                "Every time I see him, it's all I can think about!"
                hide scottie kiss with dissolve
        hide scottie with dissolve
        $ scottie.flags.kiss += 1
        $ scottie.love += 2
    return

label scottie_pregnancy_congratulations:
    scottie.say "Whoa..."
    scottie.say "Someone's been skipping the gym!"
    scottie.say "Yeah, [hero.name]?"
    "I look at Scottie and roll my eyes."
    "How can this guy be so dumb?"
    bree.say "Actually, Scottie..."
    bree.say "I'm pregnant, okay?"
    "Scottie's eyes go wide and he takes a step backwards."
    "It looks like he's actually afraid of something."
    scottie.say "But, but..."
    show scottie blush
    scottie.say "I'm not the father, right?"
    "I frown at this, shaking my head."
    bree.say "How could you possibly be the father, Scottie?"
    bree.say "We're not even seeing each other!"
    "Scottie nods with evident relief."
    show scottie -blush
    scottie.say "Oh yeah - lucky me!"
    scottie.say "Oh...and lucky you too, [hero.name]."
    scottie.say "Congratulations on getting knocked-up!"
    $ scottie.love += 1
    return

label scottie_propose_female:
    show scottie
    "I normally know when things are going well with a guy."
    "You know what I mean?"
    "Like, I can tell when we're connecting and it's going somewhere."
    "And with most guys you can tell where their head is too."
    "But there's a problem when it comes to Scottie."
    "Which is that it's hard to tell if there's anything going on in his head at all."
    "I mean, I'm seriously into the guy, even with all of the faults that he has."
    "And I want to be able to make a meaningful commitment to him."
    "But I'm not sure what kind of a reaction I'm going to get out of him."
    "All I know is that I feel like I have to try."
    "Because if I don't, then I'm always going to wonder about what might have been."
    "So that's why I steel myself to go ahead with my plans."
    "And I wait for what feels like just the right moment."
    show scottie at center, zoomAt(1.5, (640, 1040)) with fade
    "Then I go ahead and ask the question."
    bree.say "Scottie..."
    show scottie surprised
    scottie.say "Uh..."
    show scottie normal
    scottie.say "Yeah, [hero.name]?"
    bree.say "There's something I've been wanting to ask you."
    scottie.say "Well what are you waiting for?"
    scottie.say "Ask away!"
    "I force a smile onto my face as I take a deep breath."
    "Okay, here goes..."
    bree.say "The thing is, Scottie..."
    bree.say "We've been getting on great, haven't we?"
    bree.say "Having a real good time on our dates and all that, right?"
    show scottie joke
    "Scottie nods, a typically big dumb smile on his face."
    bree.say "In fact, we've been getting on so well that..."
    bree.say "Well...it's made me want to spend the rest of my life with you, Scottie!"
    bree.say "I can't hold it in any more - I have to ask you..."
    bree.say "Will you marry me?"
    show scottie surprised
    "Scottie stares at me blankly for a moment."
    "Almost like he doesn't understand the question."
    if scottie.love < 195:

        "But then his mouth curls into a smirk."
        show scottie happy at startle
        "And he starts to laugh."
        scottie.say "Erm..."
        scottie.say "How about no, [hero.name]?"
        scottie.say "I mean, why would I want to get married?"
        "Now it's my turn to stare at Scottie."
        "And that's because I feel like I've been slapped in the face."
        "I was almost prepared for the fact that he might say no."
        "That he might be scared of commitment, like some guys are."
        "But I really wasn't prepared for him to laugh at the idea."
        bree.say "Because we're in love with each other, Scottie?"
        bree.say "Maybe because we want to show the world that we feel that way?"
        show scottie annoyed
        "Scottie furrows his brows, like he's just not getting it."
        scottie.say "Huh..."
        scottie.say "Why would I care what other people think, [hero.name]?"
        scottie.say "And we're already doing it, aren't we?"
        scottie.say "So it's not like I need to marry you so we can do it!"
        bree.say "Well, when you put it like that, Scottie!"
        show scottie joke
        "Totally misreading my meaning, Scottie smiles happily."
        scottie.say "Great, [hero.name]..."
        scottie.say "I knew you'd see things my way!"
        "I have to look away to keep from letting Scottie see my real feelings."
        "And I can't help thinking I need to seriously reconsider some elements of my life too."
        $ scottie.love -= 25
    else:

        show scottie happy
        "But then he nods."
        scottie.say "Okay, [hero.name]..."
        scottie.say "That sounds good to me."
        "Now it's my turn to stare at Scottie."
        "And that's because I'm not sure I heard him correctly."
        bree.say "Wait a minute..."
        bree.say "Did you just..."
        bree.say "Did you just agree to marry me?"
        show scottie joke
        "Scottie looks at me with a smile and a nonchalant shrug."
        scottie.say "Erm..."
        scottie.say "Yeah, [hero.name]!"
        scottie.say "Wait, that is what you asked me, right?"
        bree.say "Yeah, Scottie..."
        bree.say "I just somehow thought you'd take more convincing."
        show scottie embarrassed
        "Scottie looks thoughtful for a moment."
        "Which is a truly rare and unusual thing."
        scottie.say "Oh yeah..."
        scottie.say "That is pretty weird, [hero.name]."
        show scottie blush
        scottie.say "I guess it must mean that I really love you."
        scottie.say "Because sometimes my brain realises something before I do."
        "I nod and throw in a smile of my own."
        "Because while Scottie's explanation makes no sense, it still works for me!"
        "It means that I got the answer I was hoping for."
        $ scottie.set_fiance()
    hide scottie
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
