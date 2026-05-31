init python:
    Event(**{
    "name": "palla_give_phone_number",
    "label": "give_phone_number",
    "girl": "palla",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(palla,
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
    "name": "palla_send_text",
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
        PersonTarget(palla,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "palla",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_auto_greet",
    "label": "auto_greet",
    "girl": "palla",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            IsFlag("talksex", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_auto_chat",
    "label": "auto_chat",
    "girl": "palla",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(palla,
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
    "name": "palla_are_you_sick",
    "label": "are_you_sick",
    "girl": "palla",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (palla, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_ask_out",
    "label": "ask_out",
    "girl": "palla",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(palla,
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
    "name": "palla_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "palla",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label palla_bye(bye_outfit=None):
    call npc_bye_outfit (npc=palla, bye_outfit=bye_outfit) from _call_npc_bye_outfit_17
    $ (day, h, activity, bye_outfit) = _return
    if not activity == palla.activity:
        if day != game.week_day:
            $ palla.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ palla.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"palla {bye_outfit}")
        if activity["activity"] == "sleep":
            palla.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            palla.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            palla.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            palla.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            palla.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            palla.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            palla.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            palla.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            palla.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            palla.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            palla.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            palla.say "I'll go get dressed."
        hide palla
    return

label palla_cheated(action, cheat_npc=None):
    show palla blush
    "I see Palla looking at me [action] someone else with envy and lust in her eyes."
    $ palla.love += 1
    hide palla
    return

label palla_greet:
    if renpy.has_label(f"palla_greet_dialogues_{hero.gender}") and not palla.flags.greeted:
        scene expression f"bg {game.room}"
        $ palla.flags.greeted = TemporaryFlag(True, 1)
        show palla
        palla.say "..."
        call expression f"palla_greet_dialogues_{hero.gender}" from _call_expression_258
        if palla.flags.submissive_interact:
            palla.say "H...hi, y...you sick bastard...I...I'm a bitch in heat...and I love it...there, you made me say it - happy now, [hero.name]?"
        hide palla
    return

label palla_greet_dialogues_male:
    $ renpy.dynamic("greeting", "timeofday")
    $ greeting = randint(1, 3)
    if game.hour < 6:
        $ timeofday = "Hello"
    elif game.hour < 12:
        $ timeofday = "Good morning"
    elif game.hour < 19:
        $ timeofday = "Good afternoon"
    else:
        $ timeofday = "Good evening"
    if palla_love < 40:
        if greeting == 1:
            palla.say "Oh, it's you, asshole."
            mike.say "Yeah, hi to you too, bitch."
        elif greeting == 2 and hero.grooming < 6:
            palla.say "Ugh, you stink, [hero.name], go shower!"
            mike.say "Join me?"
            palla.say "Gross!"
        else:
            palla.say "Hi, I guess."
            mike.say "You guess?"
            palla.say "Fine, I take it back."
    elif palla_love < 120:
        if greeting == 1:
            palla.say "[timeofday], [hero.name]."
            mike.say "Wait you said hello without being mean."
            palla.say "Yeah? Sorry, I meant \"Hi there, fuckface\""
        elif greeting == 2 and hero.grooming < 6:
            palla.say "Ugh, you stink, [hero.name], go shower!"
            mike.say "Join me?"
            palla.say "You'd have to force me."
        else:
            palla.say "'Sup, asshole?"
            mike.say "Nothing much, bitch!"
            "She smiles sweetly."
    elif palla_love < 199:
        if greeting == 1:
            "Palla stares at me hungrily. When I look her way our eyes meet for a split second, then she looks away and pretends not to see me."
        else:
            palla.say "[timeofday], Handsome!"
            mike.say "Hey sexy!"
    else:
        palla.say "[timeofday], Handsome!"
        mike.say "Hey sexy!"
    return

label palla_kiss:
    scene expression f"bg {game.room}"
    if palla.flags.nokiss or palla.love < 20 or (palla.love + hero.charm < 80 and not palla.is_girlfriend and not game.active_date.score >= 75):
        show palla
        "Palla quickly takes a step back, and turns away."
        if palla.love < 40:
            palla.say "Ugh, no, gross!"
            $ palla.sub += 1
        else:
            $ result = randint(1, 2)
            if result == 1:
                palla.say "Nuh uh, you haven't earned that yet."
                $ palla.love -= 1
            else:
                palla.say "I'm sorry, but I have to go..."
            "Before I can react, Palla turns and rushes away."
        hide palla
    elif palla.love + hero.charm < 60 or game.active_date.score >= 75:
        hide palla
        if palla.lesbian > MAX_LES_GUY_SEX:
            $ palla.lesbian -= 1
        show palla kiss
        if not palla.flags.kiss:
            $ palla.love += 5
            "I watch Palla's eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide palla kiss
            if palla.love >= 60:
                show palla
                palla.say "Um, I think we should talk about this later, alright?"
            else:
                show palla
                palla.say "Oh uh... I've got to go..."
                "Before I can object, Palla begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
        else:
            $ palla.love += 2
            "I take a step closer to Palla, and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide palla kiss
        $ palla.flags.kiss += 1
    else:
        hide palla
        show palla kiss
        if not palla.flags.kiss:
            $ palla.love += 5
            "I feel my lips passing over Palla's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As is, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Palla with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            $ palla.flags.kiss += 1
            hide palla kiss
            if palla.love >= 60:
                show palla
                palla.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show palla
                palla.say "Um... I should go..."
                "Before I can object, Palla turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            $ palla.love += 2
            if randint(1, 2) == 2:
                "Yet again I feel my lips passing over Palla's as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling Palla with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to Palla, close enough that our bodies are very nearly touching."
                "I bring one hand to Palla's chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring Palla's mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            $ palla.flags.kiss += 1
            hide palla kiss
            if hero.charm >= 160 - palla.love:
                show palla
                palla.say "Stop doing that."
        hide palla
    return

label palla_propose_male:
    show palla
    "I've been psyching myself up for this moment ever since I made the decision I had to do it."
    "I've gone back and forth, feeling like I'm ready and then chickening out at the last second."
    "But today's the day that I'm determined to see it through, no matter what happens."
    "I have the ring in my pocket and the lines memorised, everything planned out in my mind."
    "Now all I have to do is actually get down on one knee and ask Palla to marry me!"
    "Any other girl and that might sound like a simple thing to do."
    "But with Palla, she's just so focused and self-aware."
    "She always seems to know her own mind and be sure of just what she wants."
    "Which makes proposing to her such an intimidating prospect."
    "But I guess all that I can do is follow Palla's example, you know?"
    "She always knows what she wants, and in this case so do I."
    "I know that my feelings for her are real."
    "And I know that I want to spend the rest of my life with her too."
    "I just have to hope that she feels the same way!"
    "So here goes nothing."
    "I get down on one knee and pull out the ring..."
    show fx question
    palla.say "[hero.name]..."
    palla.say "What are you doing down there?"
    mike.say "Palla..."
    mike.say "I...I love you..."
    mike.say "And I have to know - will you marry me?"
    "Palla looks genuinely shocked at the sight of me down on one knee."
    "But the surprise is doubled as soon as I show her the ring and ask the question."
    "Her cheeks flush red and she looks this way and that, unable to speak at first."
    "All I can do is kneel there, smiling and waiting for her to find the words to answer me."
    if palla.love < 195:
        "Palla's turning her head soon transforms into her shaking it instead."
        "At the same time, her look of surprise turns into one of embarrassment."
        show palla annoyed
        palla.say "Will you put that thing away and get up?!?"
        palla.say "You're making a scene!"
        palla.say "Everyone's staring at us - for the wrong reason!"
        "At first I can't process what Palla's saying to me."
        "I spent so long working myself up for this, gathering my courage."
        "I guess I never thought of what I'd do if she turned me down!"
        mike.say "B...but, Palla..."
        mike.say "I just asked you to..."
        "As I mutter in confusion, Palla takes matters into her own hands."
        "She grabs hold of me and roughly pulls me back to my feet."
        "And it's the experience of being manhandled that snaps me out of it."
        mike.say "I take it that's a no, Palla?"
        mike.say "You're not going to marry me?"
        palla.say "No, [hero.name], I'm not going to marry you."
        show palla normal
        palla.say "At least not like this!"
        "Am I hearing things?"
        "Or was that not a complete rejection of the idea?"
        mike.say "So you're not saying no?"
        mike.say "You're just saying not now?"
        palla.say "Yes..."
        palla.say "No..."
        palla.say "I don't know!"
        "Palla lets out a sigh of genuine frustration."
        palla.say "Look, [hero.name]..."
        palla.say "I've got a lot of stuff I want to achieve in my lifetime."
        palla.say "And I don't have a whole lot of time to get it all done."
        palla.say "So a commitment like marriage is something I need to be able to plan around, okay?"
        "I nod at this, trying to hide my disappointment."
        palla.say "We're doing pretty well right now just dating."
        palla.say "So how about we stick to that, okay?"
        mike.say "Okay, Palla."
        "I shove the ring back into my pocket and force a smile onto my face."
        "Sure, it's not the answer that I wanted."
        "But it did prod Palla into opening up about what she wants."
        "And even better, it let me know that I figure pretty large in her plans for the future."
        "Which had got to be a good thing."
        $ palla.love -= 25
        $ palla.sub -= 25
    else:
        "Palla's turning her head soon transforms into her nodding it instead."
        "At the same time she begins to choke up with emotion too."
        show palla annoyed
        palla.say "Are you serious?!?"
        palla.say "I mean..."
        palla.say "This isn't a joke, right?"
        "At first I can't process what Palla's saying to me."
        "I spent so long working myself up for this, gathering my courage."
        "I guess I never thought of what I'd do if she didn't believe me!"
        mike.say "Of course I'm serious, Palla!"
        mike.say "You've made me the happiest guy in the world."
        mike.say "And I want to spend the rest of my life with you!"
        "Palla puts her hands over her mouth."
        "And I can see that she's actually starting to tear up too!"
        show palla happy
        palla.say "YES!"
        palla.say "Yes, I will!"
        palla.say "I will marry you!"
        "I almost leap to my feet as soon as I hear Palla's answer."
        "She holds out her hand, letting me slide the ring onto her finger."
        "Palla gazes at it for a moment, then kisses me on the lips."
        show palla kiss
        $ palla.flags.kiss += 1
        "The kiss doesn't last long, as she's in a flustered state."
        "She waves her hands in the air, as if trying to fan herself."
        hide palla kiss
        show palla happy
        palla.say "Oh god!"
        palla.say "I never thought this would happen!"
        palla.say "I always thought I'd need to plan out getting married."
        palla.say "You know, make sure it fitted in with all the stuff I want to do with my life?"
        mike.say "So what happened, Palla?"
        mike.say "You didn't hold back when I asked!"
        palla.say "I guess it's something about you, [hero.name]."
        palla.say "Something about the way you make me feel."
        palla.say "It just makes me impulsive!"
        "That sounds pretty good to me."
        "That I can make a control-freak like Palla act on impulse!"
        "In fact, it makes me wonder what else I could make her do..."
        $ palla.set_fiance()
    hide palla
    return

label palla_ask_date_male:
    if Harem.find_by_name("bitchy") and Harem.find_by_name("bitchy").is_active(palla):
        menu:
            "Ask Palla on a date":
                call palla_ask_date_alone_male from _call_palla_ask_date_palla
            "Ask Palla and Audrey on a date" if Harem.together(palla, audrey, name="bitchy"):
                call palla_ask_date_palla_audrey from _call_palla_ask_date_palla_audrey
            "Ask Palla, Cassidy and Audrey on a date" if "bitchy_harem_nightclub_encounter" in DONE:
                call palla_ask_date_audrey_cassidy_palla from _call_palla_ask_date_audrey_cassidy_palla
    else:
        call palla_ask_date_alone_male from _call_palla_ask_date_palla_1
    return _return

label palla_ask_date_palla_audrey:
    mike.say "Do you want to get together with Audrey and have some fun?"
    if palla.love >= 160 and palla.lesbian >= 9:
        palla.say "Fuck yeah!"
        mike.say "Let's meet at home."
        call select_date_time from _call_select_date_time_21
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            mike.say "I tell Audrey to meet us home."
            call palla_and_audrey from _call_palla_and_audrey_2
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "bitchy", ["palla", "audrey"], "palla_and_audrey"))
            return
    else:
        palla.say "I don't feel like it, sorry."
        return False

label palla_ask_date_audrey_cassidy_palla:
    mike.say "Do you want to get together with Audrey and Cassidy and have some fun?"
    if palla.love >= 160 and palla.lesbian >= 9:
        palla.say "Fuck yeah!"
        call select_date_time from _call_select_date_time_9
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            call bitchy_harem_foursome_appointment_intro from _call_bitchy_harem_foursome_appointment_intro_2
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "bitchy", ["audrey", "cassidy", "palla"], "bitchy_harem_foursome_appointment_intro"))
        return
    else:
        palla.say "I don't feel like it, sorry."
        return False

label palla_ask_date_alone_male:
    mike.say "Palla, would you like to go on a date with me?"
    if palla.love < 40:
        palla.say "Gross! No!"
        return False
    elif palla.love < 50 or palla.flags.nodate:
        palla.say "Sorry [hero.name], we're not there yet."
        return False
    else:
        if palla.sexperience < 3:
            palla.say "Okay, but no promises. When do you want to go?"
        else:
            palla.say "Of course! When do you want to go?"
        return True

label palla_ask_fuck_date_male:
    $ game.play_music("music/roa_music/city_nights.ogg")
    if game.active_date.score >= (100 - palla.flags.drinks*5):
        if palla.sexperience < 3:
            if hero.stamina:
                mike.say "Do you want to come back to my place?"
                palla.say "I don't know..."
                mike.say "Did you have fun?"
                palla.say "I guess. Sure, as long as your place isn't too much of a shithole."
            else:
                palla.say "It was really nice."
                return False
        else:
            palla.say "Let's go back to your place, [hero.name]."
            menu:
                "Yes" if hero.stamina:
                    mike.say "I would love that."
                "I'd prefer to go at your place" if hero.stamina and renpy.has_label("palla_apartment_sex"):
                    palla.say "Great idea."
                    call palla_apartment_sex from _call_palla_apartment_sex
                    $ game.room = "street"
                    return False
                "No" if hero.stamina:
                    $ palla.love -= 5
                    mike.say "Sorry but I am tired."
                    return False
                "No. I'm exhausted." if not hero.stamina:
                    "I had too much 'hot coffee' lately, I should rest."
                    $ palla.love -= 5
                    mike.say "Sorry but I am tired."
                    return False
        return "hero"
    else:
        palla.say "It was really nice."
        return False

label palla_pill_talk:
    mike.say "Palla, you should stop taking the pill."
    if palla.flags.pillchat:
        palla.say "[hero.name], we've already talked about this. I am not ready for children."
        return
    "Palla looks at me with an expression that can best be described as a mix of surprise and horror."
    palla.say "{b}Whyever{/b} would I want to do that?"
    mike.say "Why wouldn't you want to do that?"
    if palla.flags.minealone:
        palla.say "So I don't have to squeeze out your sprog!"
    else:
        palla.say "So I don't have to squeeze out someone's sprog!"
    mike.say "Would that be such a bad thing?"
    palla.say "Wait, are you for serious?"
    mike.say "Sure."
    palla.say "Okay, let me first list all the reasons why it's a bad idea."
    palla.say "First, we're not married and I'm not enthused about being a single mom."
    palla.say "Second, single moms are too busy being single moms to work, and we're not married so now I have to find a way to work {b}and{/b} raise a child."
    palla.say "Third, you don't strike me as the settling down type."
    palla.say "Fourth, I loathe children. I mean, little screechy things that demand your attention all the time? Sure I like holding someone else's baby, that can be fun, but then I get to hand the little brat back."
    mike.say "Really, you hate children?"
    palla.say "Oh yeah. Seriously, can't stand the little rugrats."
    if not palla.flags.minealone:
        palla.say "And lastly, we're not exclusive, so how do you know any kid I have would even be yours? If you want kids, that changes the rules of our relationship, dude."
    palla.say "So how about this. No, fuck no, and Jesus fucking Christ on a crutch what kind of an idiot are you, anyway?"
    mike.say "I, uh. I guess I'm the idiot that fell in love with a bitch like you. Guess I should have known better."
    "Palla takes a deep breath."
    palla.say "Look, [hero.name], if you want to have kids...we're going to have to be in a different place."
    if "palla_event_13" in DONE:
        palla.say "I'll need to have my career sorted out."
    palla.say "And we need to be...wow."
    palla.say "And look, before you call me a fucking bitch again, I'm flattered, okay? This took me by surprise, and...oh fuck. You really want kids? I guess we'll have to see. I'll think about what needs to happen."
    palla.say "No promises, though, okay?"
    "I can only shrug."
    mike.say "If you say so."
    $ palla.flags.pillchat = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
