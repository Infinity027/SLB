init python:
    Event(**{
    "name": "audrey_give_phone_number",
    "label": "give_phone_number",
    "girl": "audrey",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(audrey,
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
    "name": "audrey_send_text",
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
        PersonTarget(audrey,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "audrey",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "audrey_auto_greet",
    "label": "auto_greet",
    "girl": "audrey",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(audrey,
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
    "name": "audrey_auto_chat",
    "label": "auto_chat",
    "girl": "audrey",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(audrey,
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
    "name": "audrey_are_you_sick",
    "label": "are_you_sick",
    "girl": "audrey",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (audrey, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "audrey_ask_out",
    "label": "ask_out",
    "girl": "audrey",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(audrey,
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
    "name": "audrey_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "audrey",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label audrey_bye(bye_outfit=None):
    call npc_bye_outfit (npc=audrey, bye_outfit=bye_outfit) from _call_npc_bye_outfit_3
    $ (day, h, activity, bye_outfit) = _return
    if not activity == audrey.activity:
        if day != game.week_day:
            $ audrey.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ audrey.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"audrey {bye_outfit}")
        if activity["activity"] == "sleep":
            audrey.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            audrey.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            audrey.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            audrey.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            audrey.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            audrey.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            audrey.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            audrey.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            audrey.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            audrey.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            audrey.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            audrey.say "I'll go get dressed."
        hide audrey
    return

label audrey_cheated(action, cheat_npc=None):
    show audrey
    $ gain = 1
    if audrey.flags.girlfriend or audrey.flags.fiance:
        $ gain += 1
    $ audrey.love += gain
    "I see Audrey looking at me [action] someone else with envy and lust in her eyes."
    hide audrey
    return

label audrey_greet:
    if renpy.has_label(f"audrey_greet_dialogues_{hero.gender}") and not audrey.flags.greeted:
        scene expression f"bg {game.room}"
        $ audrey.flags.greeted = TemporaryFlag(True, 1)
        show audrey
        $ result = randint(1, 3)
        if result == 1:
            audrey.say "Hello, [hero.name]."
        elif result == 2:
            audrey.say "Hi, [hero.name]."
        elif result == 3:
            audrey.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                audrey.say "Good morning [hero.name]."
            elif game.hour < 19:
                audrey.say "Good afternoon [hero.name]."
            else:
                audrey.say "Good evening [hero.name]."
        call expression f"audrey_greet_dialogues_{hero.gender}" from _call_expression_210
        if audrey.flags.submissive_interact:
            if randint(0, 1) == 0:
                "Play with me, [hero.name] - make me your toy?"
            else:
                audrey.say "[hero.name], please, please..."
                audrey.say "Play with me some more."
        hide audrey
    return

label audrey_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        if audrey.flags.nickname == "toy":
            mike.say "Hello, my little Toy."
        else:
            mike.say "Hello, Audrey."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            if audrey.flags.nickname == "toy":
                mike.say "Hello, my little Toy."
            else:
                mike.say "Hello Audrey."
        elif game.hour < 12:
            if audrey.flags.nickname == "toy":
                mike.say "Good morning my little Toy."
            else:
                mike.say "Good morning Audrey."
        elif game.hour < 19:
            if audrey.flags.nickname == "toy":
                mike.say "Good afternoon my little Toy."
            else:
                mike.say "Good afternoon Audrey."
        else:
            if audrey.flags.nickname == "toy":
                mike.say "Good evening my little Toy."
            else:
                mike.say "Good evening Audrey."
    return

label audrey_kiss:
    scene expression f"bg {game.room}"
    if audrey.love < 25 and not audrey.is_girlfriend and not game.active_date.score >= 75:
        show audrey
        "Sometimes when you look back on a situation that you misread, it's pretty obvious, in retrospect, just what you did wrong."
        "But at the same time there are still those incidents that you find yourself genuinely scratching your head over hours, even days later."
        "Audrey just put me in that very situation, making me wonder how I could have elicited such a reaction from her, especially based on the tone of her behaviour towards me."
        "She leans in close to me, making one of her typically outrageous and obviously provocative comments."
        "Normally I would have tried my best to either ignore the flirtation or take her to task over some other imagined transgression."
        "But for some reason that I can't readily explain, I just feel the urge to stop pushing back on this occasion."
        "So instead of protesting and telling Audrey that he behaviour isn't appropriate, I lean in closer too."
        "All I had in mind was kissing her quickly, maybe just a peck on the lips."
        "But she surprises me by instantly sensing my intentions and jerking her head back, moving her lips well out of range."
        audrey.say "Uh-uh...I don't think so!"
        "And with that, she skips away, wagging her finger at me and tutting in a disapproving manner."
        "All of which leaves me more confused than I was when the whole thing began."
        "I always thought that the point of Audrey's flirting was to entice me into her web."
        "Is it possible that there's more too it than that?"
        "Or is she just swinging from one extreme to the other in order to further confuse me?"
        $ audrey.love -= 5
        $ audrey.sub -= 5
        hide audrey
    elif not audrey.flags.kiss:
        hide audrey
        $ audrey.love += 5
        if audrey.lesbian > MAX_LES_GUY_SEX:
            $ audrey.lesbian -= 1
        show audrey kiss
        "I feel like I can only keep on fighting the same fight over and again for so long before I start going mad."
        "And it feels like I've been battling against Audrey for as long as she's been a part of my life, without a pause in the hostilities."
        "It seems as though this antagonism between us has become the main source of consternation in my daily life."
        "The constant flirting and provocative behaviour is probably better described as a form of sexual harassment."
        "But even though it's the twenty-first century, I'd still feel like an idiot were I to report it to human resources."
        "I guess that's why one day I just think, fuck it."
        "And rather than shying away from her as she makes her usual round of manipulative statements and thinly veiled threats, I decide to call her bluff."
        "When Audrey leans forwards to rub in the latest one of her manipulative tricks, I simply mirror her move and place my lips firmly against her own."
        "Instantly, I see her eyes grow wide and almost swell with shock."
        "In fact, she seems to be so taken by surprise that it's almost a full minute before I can feel her begin to relax and return the kiss."
        "I can't guess what the consequences of finally giving in to Audrey are going to be."
        "But for the moment, I have to admit that by keeping on resisting the temptation that she represented, I've been denying myself something that feels really sensational."
        hide audrey kiss
        $ audrey.flags.kiss += 1
    else:
        $ audrey.love += 2
        hide audrey
        show audrey kiss
        "I'm not sure what really changed once I finally gave in and Audrey's games of teasing and little threats became a thrill in my life, rather than a constant source of torture and torment."
        "But whenever the point that it all changed did come, things have been getting steadily better for me ever since then."
        "Of course, Audrey still seems to be intent upon playing the very same kind of games with me as she did before."
        "Yet now I'm a more than willing participant, and I actually look forward to discovering what mischief she has planned for me when I see her next."
        "Where before I would have been cringing away or else at the very least trying to shout her down, I now can't wait to have the chance to catch Audrey and pull her into my arms for a passionate kiss whenever the chance arises."
        "All of the spite and spice that used to be channelled into her antics around trying to seduce me can now be diverted into making our stolen moments together something to remember afterwards."
        "There are even times when the girl that was once using all of her slyness and seductive charms to try to draw me into her web is actually the one that finds herself now seeking to avoid being caught."
        "I guess there's something to the idea of being careful what you wish for, as well as realising that what you really want is sometimes right in front of you the whole time."
        hide audrey kiss
        $ audrey.flags.kiss += 1
    return

label audrey_propose_male:
    show audrey
    "Having a ring in your pocket and waiting for just the right moment to get down on one knee."
    "Some might say that's one of the most stressful things that a guy can have to do in a given day."
    "But then most of the people that say so probably never met a girl like Audrey before."
    "She's the kind of girl that I never imagined I'd be trying to propose to like this."
    "Hell, when I first met her, I never imagined I'd propose to her at all."
    "In fact, I could have more easily believed that I'd end up pushing her down a lift-shaft!"
    "But what can I say?"
    "Except perhaps for it's funny how things turn out in the end."
    "Not only did I come to have feelings for Audrey, I actually fell in love with her too!"
    "I guess it helps matters that I finally managed to figure her out on a basic level."
    "You know, to learn that her teasing was actually a form of affection?"
    "After that, none of her little quirks seemed to matter anymore."
    "So, I figure that there's no time like the present."
    "And as soon as I get the chance, I make my move..."
    if audrey.flags.nickname == "toy":
        mike.say "Little Toy..."
    else:
        mike.say "Audrey..."
    mike.say "There's something I wanted to ask you..."
    show audrey frown
    audrey.say "Huh?"
    audrey.say "What's up, [hero.name]?"
    "Audrey looks around in surprise."
    "And then she sees what I have in my hand."
    show audrey annoyed
    audrey.say "Is...is that what I think it is?"
    show fx question
    audrey.say "Are you going to..."
    "By now, I'm already going down on one knee."
    show fx exclamation
    audrey.say "Oh shit, you are!"
    audrey.say "You really are doing it!"
    if audrey.flags.nickname == "toy":
        mike.say "Little Toy..."
    else:
        mike.say "Audrey..."
    mike.say "Will you marry me?"
    "I take a deep breath and hold it in, waiting for her answer."
    show audrey normal
    "Audrey lets out a peal of laughter and shakes her head."
    "At first I don't know if she's just caught off-guard."
    "That or if the idea itself is something she finds laughable."
    "But then Audrey opens her mouth to answer me..."
    if audrey.love < 195:
        audrey.say "This had better be a joke, [hero.name]."
        audrey.say "Because otherwise it's not funny!"
        show audrey angry
        "I look around as Audrey says this, beginning to feel foolish."
        "If this is a joke, then it's one of the most expensive I've ever pulled off."
        mike.say "Ah..."
        mike.say "I take it that's a no?"
        show fx exclamation
        audrey.say "Of course it's a no!"
        audrey.say "Jesus, [hero.name]!"
        audrey.say "Put that thing away and get up - you're embarrassing me."
        "I nod slowly, doing as I'm told."
        "Shoving the ring back into my pocket, I try to force a smile onto my face."
        "So what if Audrey doesn't want to marry me?"
        "It's as if not the end of the world."
        "And all I did was make myself look like a fool in public..."
        $ audrey.love -= 25
        $ audrey.sub -= 25
    else:
        audrey.say "Yeah, [hero.name] - why not?"
        show audrey flirt
        audrey.say "If you think you can cope?"
        audrey.say "So don't say I didn't warn you!"
        "Audrey thrusts out her hand towards me as she says this."
        "And I smile up at her as I slip the ring onto her finger."
        if audrey.flags.nickname == "toy":
            mike.say "I already managed to put up with you this long, little Toy."
        else:
            mike.say "I already managed to put up with you this long, Audrey."
        mike.say "So I must be building up an immunity to your teasing."
        mike.say "At least that's the way I figure it!"
        "I get back to my feet."
        "But I see a wicked smile appear on Audrey's face."
        show audrey happy
        audrey.say "Oh, you'd better hope that's how it is, [hero.name]."
        audrey.say "Because you're signing up for the long-haul."
        audrey.say "And that means I'm going to be working on you the whole time!"
        "Audrey winks as she says this."
        "And then she leans in for a kiss."
        "Which leaves me wondering if she's serious or not!"
        $ audrey.set_fiance()
    hide audrey
    return

label audrey_ask_date_male:
    if Harem.find(audrey):
        menu:
            "Ask Audrey on a date":
                call audrey_ask_date_alone_male from _call_audrey_ask_date_alone_male
            "Ask Audrey and Palla on a date" if Harem.together(audrey, palla, name="bitchy"):
                call audrey_ask_date_audrey_palla from _call_audrey_ask_date_audrey_palla
            "Ask Audrey, Cassidy and Palla on a date" if "bitchy_harem_nightclub_encounter" in DONE:
                call audrey_ask_date_audrey_cassidy_palla from _call_audrey_ask_date_audrey_cassidy_palla
            "Meet Alexis, Audrey and Reona for a 'hot coffee'" if Harem.find_by_name("thot") and Harem.together(alexis, audrey, reona, name="thot"):
                call audrey_ask_date_alexis_reona from _call_audrey_ask_date_alexis_reona
    else:
        call audrey_ask_date_alone_male from _call_audrey_ask_date_alone_male_1
    return _return

label audrey_ask_date_audrey_palla:
    mike.say "Do you want to get together with Palla and have some fun?"
    if audrey.love >= 160 and audrey.lesbian >= 9:
        audrey.say "Fuck yeah!"
        mike.say "Let's meet at home."
        call select_date_time from _call_select_date_time_2
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            mike.say "I tell Palla to meet us home."
            call palla_and_audrey from _call_palla_and_audrey_1
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "bitchy", ["palla", "audrey"], "palla_and_audrey"))
            return
    else:
        audrey.say "I don't feel like it, sorry."
        return False

label audrey_ask_date_audrey_cassidy_palla:
    mike.say "Do you want to get together with Cassidy and Palla and have some fun?"
    if audrey.love >= 160 and audrey.lesbian >= 9:
        audrey.say "Fuck yeah!"
        call select_date_time from _call_select_date_time_3
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            call bitchy_harem_foursome_appointment_intro from _call_bitchy_harem_foursome_appointment_intro
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "bitchy", ["audrey", "cassidy", "palla"], "bitchy_harem_foursome_appointment_intro"))
        return
    else:
        audrey.say "I don't feel like it, sorry."
        return False

label audrey_ask_date_alexis_reona:
    mike.say "Do you want to get together with Alexis and Reona and have some fun?"
    audrey.say "I'd love to."
    call select_date_time from _call_select_date_time_28
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call thot_harem_foursome_intro from _call_thot_harem_foursome_intro_1
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "thot", ["alexis", "audrey",  "reona"], "thot_harem_foursome_intro"))
    return

label audrey_ask_date_alone_male:
    mike.say "Audrey, would you like to go on a date with me?"
    if audrey.love < 50 or audrey.flags.nodate:
        audrey.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        audrey.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
