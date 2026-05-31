init python:
    Event(**{
    "name": "alexis_give_phone_number",
    "label": "give_phone_number",
    "girl": "alexis",
    "conditions": [
        HeroTarget(IsGender("male")),
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
            IsGender("male"),
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
            IsGender("male"),
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
            IsGender("male"),
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
            IsGender("male"),
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
            IsGender("male"),
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
            IsGender("male"),
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
    if renpy.has_label(f"alexis_greet_dialogues_{hero.gender}") and not alexis.flags.greeted:
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
        call expression f"alexis_greet_dialogues_{hero.gender}" from _call_expression_206
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
            "Are you supposed to know when the moment's right for something like this, or is it just a matter of trusting to instinct?"
            "When the time's right, you're supposed to know it, but even that knowledge has to be instinctive!"
            "Either way, I can't keep from leaning in closer towards Alexis right now, turning so that I'm at just the right angle for our lips to meet."
            "She's facing slightly away from me as I do this, meaning that she doesn't see me until the moment that she turns in my direction."
            "All I can see is the fluttering of her blonde hair and the outline of her cheek, and then the shape of her lips."
            "I wonder if they'll feel familiar to kiss after all this time, or if it'll be possible for me to recall their feel at all."
            "I close my eyes in anticipation of feeling them press against mine..."
            "But then all I feel is the curve of her cheek, as Alexis instinctively pulls away from me and pushes me back at the same time."
            "All I get is the scent of her hair and the instant sense of embarrassment that comes with knowing that my advances have been rejected."
            "I mumble something vague about being sorry, and turn away to keep Alexis from seeing that my face has coloured from the experience."
            "And she in turn mutters something equally bland about it not being a big deal, timing and all those other things that don't really help matters."
        else:
            "I'll be honest - it's not like in all the time we were apart, I ever really forgot what it was like to be with Alexis."
            "Or in this case, what it was like to kiss her."
            "Maybe that's what leads to me making a mess of it this time around."
            "Maybe I'm so used to the memory of kissing her that I just assume she'll be okay with it."
            "Whatever the reason, as soon as I make my move, Alexis recoils like she's been stung."
            "Of course, she apologises straight after, but I still think it was me that was likely in the wrong..."
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
            "Don't ask me how I know - but I know!"
            "There's just something in the way that Alexis's gaze lingers on me as she turns away for a moment."
            "It's not visible desire or anything so obvious, more a warmth in her eyes that tells me she wants something more."
            "I don't say anything, as this isn't a matter of saying the right thing either."
            "This is about instincts and cues that are far older than words."
            "When Alexis turns back to me, I lean in and place my lips against hers."
            "This is one of those moments when the world is no larger than the two of you, and it's perfect while something impermanent lasts."
            "She returns the kiss immediately, gently at first, and then with a growing sense of confidence as we come together."
            "I can't remember how we used to kiss when we were teenagers, and truth be told, I don't care to."
            "The Alexis from back then is gone, and I only care about the one that's here, in my arms right now."
            "It seems to last for the longest time, but in truth I guess that we could only have been kissing for perhaps a minute at the most."
            "And in that brief moment, I begin to feel like the years that we were apart were only a brief interlude between then and now."
            "As though I've been waiting for her to come back to me, and now that she has, I can start living again."
        else:
            "I've been wondering about this moment, ever since Alexis came back into my life."
            "What will it be like to kiss her again, after so much time has passed?"
            "Will it be just like I remember, back when we were kids?"
            "Will it be better now that we're both so much more mature and sure of ourselves?"
            "I've even worried that it might be worse, a disappointment compared to my precious memories..."
            "But when the time finally does come, it's nothing like what I remembered."
            "It doesn't feel at all like I recall, but like something completely new."
            "I can't help but think that's a good sign, like we're starting over, with the chance to get it right this time."
        hide alexis kiss
        if alexis.love >= 60:
            show alexis
            alexis.say "Um, I think we should talk about this later, alright?"
        else:
            show alexis
            alexis.say "Oh uh... I've got to go..."
            "Before I can object, Alexis begins in the opposite direction."
            "She seemed a little uncomfortable, did I do something wrong?"
        $ alexis.flags.kiss += 1
    else:
        hide alexis
        show alexis kiss
        if randint(1, 2) == 1:
            "I know now just when Alexis is leaning into me with that very specific angle to her head and the right look in her eye."
            "I don't hesitate to match her movements so that our lips meet at just the right point for me to feel that spark of excitement."
            "No matter how many times we kiss like this, it never seems to become boring or routine."
            "A part of the thrill that I felt the very first time we kissed after Alexis came back into my life seems to always linger on my lips afterward as well."
            "I seem to be taking every single chance that I can get to kiss her now as well."
            "Now that we're entwined, I risk gently pushing my tongue between her lips."
            "My reward is to have her own tongue come to meet it, caressing and exploring as it slips into my mouth."
            "Our bodies mirror this same movement, as we wrap our arms around each other and pull closer together still."
            "At times like this I find it hard to remember just where we are, as the world around us just seems to lose all importance."
            "We could be alone or in the middle of a crowded room, and the only person on my mind would still be Alexis."
            "I don't know exactly when we became one of those couples that people walk past and tut at for spending all their time kissing."
            "But the reality of the matter is that, when I'm with her, I hardly care."
        else:
            "I honestly think I'm starting to forget what it used to be like kissing Alexis."
            "At least what it was like to do that back when we were both just teenage kids."
            "Somehow the feeling of her stealing a kiss from me in the here and now is just so much better than anything I remember."
            "And she seems to want to do it as many times as she can manage too."
            "Sometimes it's a peck on the lips and others it's a longer, much more involved affair."
            "But every single time it's memorable enough to feel like it's pushing one of the older memories out and taking its place."
            "Which is fine with me, as I can use all the pleasant memories I can get."
            "So long as they replace the older, more unpleasant ones..."
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
                show cuddle alexis
                mike.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                show cuddle alexis
                "We curl up spooning together in bed, drifting toward sleep."
                $ alexis.love += 1
                call sleep ("alexis") from _call_sleep_6
    $ game.room = "bedroom1"
    return

label alexis_propose_male:
    "I was all prepared for this moment, hell knows I've gone over it a thousand - no, a million times in my head!"
    "In fact, I even thought about how I'd go about doing this when Alexis and I were together in high school."
    "But now that I've committed myself to popping the question, I've turned into a mess of nerves and cliches!"
    "I'm sweating bullets, stumbling over my words and constantly worrying that I've managed to lose the damn ring."
    "And all of this is before I've even chosen the moment to get down on one knee and actually ask her to marry me!"
    "Alexis keeps looking at me sideways, and I just know that she's starting to get suspicious."
    show alexis confused with fade
    alexis.say "Ah, [hero.name]..."
    alexis.say "What's with you today?"
    alexis.say "You look like a guy waiting bad news!"
    "Oh great - she's calling me out!"
    "I do the best I can to recover and look like there's nothing on my mind."
    "But from the look on Alexis's face, I'm guessing that it's not working."
    mike.say "What?!?"
    mike.say "Don't be silly, Alexis!"
    mike.say "I'm fine, just fine!"
    show alexis normal
    "Okay, this is it - now or never."
    "Time to go with one of the contingency plans I cooked up."
    mike.say "Oh..."
    mike.say "Ah shoot..."
    mike.say "I think I dropped something around here..."
    "I make a show of crouching down and pretending to search on the ground."
    "Alexis steps back a little, either trying to give me room or else humouring me."
    "And I take this as my chance to move to the next stage of the plan."
    "So, while taking a deep breath, I pull out the ring."
    "Then I look up at her, holding it in my hand."
    mike.say "Alexis..."
    mike.say "Will...will you marry me?"
    show alexis surprised
    "The effect on Alexis is instant and more dramatic than I'd expected."
    "I always thought that she'd be as cool as can be when I asked her to marry me."
    "But she looks genuinely shocked, as if it was the last thing she expected to hear."
    "Maybe she is surprised, or maybe she just can't control her reaction to something so important."
    "Either way, Alexis claps her hands over her mouth, and her eyes go wide in the same moment."
    if alexis.love >= 195:
        "Without a word of warning, Alexis grabs the hand holding the ring."
        "And then, with a surprising show of strength, she yanks me to my feet."
        "Her eyes are still wide, but now I can see that they're also welling with tears too!"
        mike.say "Ah..."
        mike.say "Alexis..."
        mike.say "Are you okay?"
        "Alexis shakes her head and waves her hands in front of her face."
        "It's like she's trying to overcome the emotions that she's feeling right now."
        show alexis happy
        alexis.say "I...I'm okay..."
        alexis.say "This is...this is just a shock!"
        alexis.say "I...I never thought that...that you'd want to..."
        "I keep nodding, trying to follow Alexis as she begins to babble."
        alexis.say "Oh...of course I will, [hero.name]!"
        alexis.say "Of course I'll marry you!"
        "Now it's my turn to be surprised and left at a loss."
        "It's the answer that I wanted to hear, sure it is."
        "But suddenly I don't know what I'm supposed to do next."
        "Luckily for me, Alexis come to my aid a moment later."
        "She thrusts one hand forwards while using the other to wipe her eyes."
        "And I jump to attention, pushing the ring onto her finger."
        "As soon as I do so, I feel a weight lifted off my shoulders."
        "It's a weight I hadn't realised was there."
        "It's the weight of the past, of the things that broke us up back in high-school."
        "None of that seems to matter anymore, in fact, it seems crazy that it ever did."
        "No, what matter is here and now, that and where we're going in the future."
        "Or to be more precise, that we're going there together."
        "Alexis keeps a hold of my hand as she kisses me full on the lips."
        "And that gesture, as much as the ring on her finger, tells me this is going to work."
        "It was a long journey getting here, but it was worth the struggles along the way."
        $ alexis.set_fiance()
    else:
        "But when Alexis finally gives me some kind of sign, it's not the one I wanted."
        "At first she doesn't say a word, just shakes her head, slowly at first and then faster."
        "And I don't need to be told what that means."
        "I can already feel the sensation of my heart snapping in two."
        "She's done it to me again - broken my heart twice!"
        show alexis sad
        alexis.say "Oh god..."
        alexis.say "I'm so sorry, [hero.name]!"
        alexis.say "But I can't marry you...I just can't."
        "I'm still on my knees, and I know I should get up."
        "But I just can't stop myself responding."
        "Even though I know it makes me look pathetic, like I'm pleading with Alexis."
        "Well...I guess I really am pleading with her!"
        "I just don't seem to be able to stop myself."
        mike.say "But..."
        mike.say "But why, Alexis?"
        mike.say "I thought we'd both moved on, put the past behind us?"
        mike.say "Haven't we been getting on better than we ever did before?"
        "Alexis shakes her head at this, and I can see she's torn by what I'm saying."
        "This gives me a faint glimmer of hope."
        "As it means the problem may not be our relationship."
        show alexis sadsmile
        alexis.say "That's exactly why we're working now, [hero.name]!"
        alexis.say "Don't you see that?"
        alexis.say "You're not hung up about stuff that doesn't matter anymore."
        alexis.say "We've kept it cool and casual, and it's working!"
        alexis.say "Our problem was always too much commitment, not enough!"
        "It's not what I wanted to hear, not at all."
        "But as I listen to Alexis explain herself, I find myself nodding in agreement."
        "She's not wrong when she says we're both different people now, more laid back."
        "And there's been none of the old bullshit that came between us in the past."
        "Maybe this isn't the time to be thinking about making it official?"
        "Slowly getting back to my feet, I let out a sigh of defeat."
        mike.say "Okay, Alexis..."
        mike.say "Point taken."
        mike.say "I just wish I hadn't gone down on one knee before you said all that!"
        "Alexis gives me a pained smile and a kiss on the cheek."
        "It doesn't make everything better, but it does give me hope."
        "Hope that we still have a future together."
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
