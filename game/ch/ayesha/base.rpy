init python:
    Event(**{
    "name": "ayesha_give_phone_number",
    "label": "give_phone_number",
    "girl": "ayesha",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(ayesha,
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
    "name": "ayesha_auto_greet",
    "label": "auto_greet",
    "girl": "ayesha",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsActivity("None")),
        PersonTarget(ayesha,
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
    "name": "ayesha_auto_chat",
    "label": "auto_chat",
    "girl": "ayesha",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(ayesha,
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
    "name": "ayesha_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "ayesha",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(ayesha,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label ayesha_ask_date_male:
    if Harem.find(ayesha):
        menu:
            "Ask Ayesha on a date":
                call ayesha_ask_date_alone_male from _call_ayesha_ask_date_alone_male
            "Ask Ayesha and Kylie on a date" if Harem.together(ayesha, kylie, name="taming"):
                call ayesha_ask_date_ayesha_kylie from _call_ayesha_ask_date_ayesha_kylie
    else:


        call ayesha_ask_date_alone_male from _call_ayesha_ask_date_alone_male_1
    return _return

label ayesha_ask_date_alone_male:
    mike.say "Ayesha, would you like to go on a date with me?"
    if "ayesha_event_02" in DONE and not ("ayesha_event_03" in DONE or "ayesha_event_03b" in DONE) and game.season in [0, 2, 3]:
        ayesha.say "Sure, it might be fun, when do you want us to go?"
        return True
    elif ayesha.love < 50 or ayesha.flags.nodate:
        ayesha.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        ayesha.say "Sure, it might be fun, when do you want us to go?"
        return True

label ayesha_ask_date_ayesha_kylie:
    mike.say "You want to get together with Kylie and have some fun?"
    if game.flags.tamingDatesNumber >= 2:
        ayesha.say "Sure, it might be fun, when do you want us to go?"
        mike.say "Let's meet at home."
        return HaremAppointment(20, "taming", ["ayesha", "kylie"], "taming_threesome_fuck", fixed_hour=True)
    else:
        ayesha.say "I don't feel like it, sorry."
        return False

label ayesha_ask_fuck_date_male:
    if (game.active_date.score >= (100 - ayesha.flags.drinks * 5)):
        ayesha.say "Maybe I could, you know..."
        ayesha.say "Come for a hot coffee."
        menu:
            "Yes" if hero.stamina:
                mike.say "I would love that."
                if "ayesha_event_02" in DONE and not ("ayesha_event_03" in DONE or "ayesha_event_03b" in DONE) and game.season in [0, 2, 3]:
                    call ayesha_event_03b from _call_ayesha_event_03b
                return "hero"
            "No" if hero.stamina:
                $ ayesha.love -= 5
                mike.say "Sorry but I am tired."
                if "ayesha_event_02" in DONE and not ("ayesha_event_03" in DONE or "ayesha_event_03b" in DONE) and game.season in [0, 2, 3]:
                    mike.say "But let me walk you back home."
                    ayesha.say "Hmm... Okay."
                    call ayesha_event_03b from _call_ayesha_event_03b_1
                return False
            "No. I'm exhausted." if not hero.stamina:
                "I had too much 'hot coffee' lately, I should rest."
                $ ayesha.love -= 5
                mike.say "Sorry but I am tired."
                if "ayesha_event_02" in DONE and not ("ayesha_event_03" in DONE or "ayesha_event_03b" in DONE) and game.season in [0, 2, 3]:
                    mike.say "But, let me walk you back home."
                    ayesha.say "Hmm... Okay."
                    call ayesha_event_03b from _call_ayesha_event_03b_2
                return False
    else:
        ayesha.say "It was really nice."
        if "ayesha_event_02" in DONE and not ("ayesha_event_03" in DONE or "ayesha_event_03b" in DONE) and game.season in [0, 2, 3]:
            mike.say "Let me walk you back home."
            ayesha.say "Hmm... Okay."
            call ayesha_event_03b from _call_ayesha_event_03b_3
        return False

label ayesha_cheated(action, cheat_npc=None):
    show ayesha
    if cheat_npc and Harem.together(cheat_npc, ayesha):
        show ayesha blush
        ayesha.say "Aren't you forgetting something?"
        show ayesha
        "And without warning Ayesha kisses me."
        $ ayesha.love += 1
        $ ayesha.flags.kiss += 1
    elif ayesha.sub >= 75:
        show ayesha blush
        show fx heart
        $ ayesha.sub += 1
        "I see Ayesha looking at me [action] someone else with envy and lust in her eyes."
    else:
        show ayesha sad
        show fx anger
        $ ayesha.flags.cheatedby = active_girl.name
        $ loss = 5
        if ayesha.flags.girlfriend or ayesha.flags.fiance:
            $ loss += 5
        $ ayesha.love -= loss
        "I see Ayesha looking at me [action] someone else with tears in her eyes..."

    hide ayesha
    return

label ayesha_bye(bye_outfit=None):
    call npc_bye_outfit (npc=ayesha, bye_outfit=bye_outfit) from _call_npc_bye_outfit_4
    $ (day, h, activity, bye_outfit) = _return
    if not activity == ayesha.activity:
        if day != game.week_day:
            $ ayesha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ ayesha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"ayesha {bye_outfit}")
        if activity["activity"] == "sleep":
            ayesha.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            ayesha.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            ayesha.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            ayesha.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            ayesha.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            ayesha.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            ayesha.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            ayesha.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            ayesha.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            ayesha.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            ayesha.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            ayesha.say "I'll go get dressed."
        hide ayesha
    return

label ayesha_greet:
    if renpy.has_label(f"ayesha_greet_dialogues_{hero.gender}") and not ayesha.flags.greeted:
        scene expression f"bg {game.room}"
        show ayesha
        $ ayesha.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            ayesha.say "Hello, [hero.name]."
        elif result ==2:
            ayesha.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                ayesha.say "Good morning [hero.name]."
            elif game.hour < 19:
                ayesha.say "Good afternoon [hero.name]."
            else:
                ayesha.say "Good evening [hero.name]."
        call expression f"ayesha_greet_dialogues_{hero.gender}" from _call_expression_212
        if ayesha.flags.submissive_interact:
            if randint(0, 1) == 0:
                ayesha.say "I belong to you, [hero.name] - wanna fuck my face?"
            else:
                ayesha.say "[hero.name], you know I'm yours only, do you?"
                mike.say "Of course I know it."
                ayesha.say "Then use me right now!"
        hide ayesha
    return

label ayesha_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Ayesha."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Ayesha."
        elif game.hour < 12:
            mike.say "Good morning Ayesha."
        elif game.hour < 19:
            mike.say "Good afternoon Ayesha."
        else:
            mike.say "Good evening Ayesha."
    return

label ayesha_kiss_reaction_male:
    if ayesha.lesbian > MAX_LES_GUY_SEX:
        $ ayesha.lesbian -= 1
    return

label ayesha_kiss_male:
    scene expression f"bg {game.room}"
    if ayesha.love < 25 and not ayesha.is_girlfriend and not game.active_date.score >= 75:
        show ayesha
        "I don't think I've ever been so nervous about taking the lead and trying to kiss a girl before now."
        "Perhaps part of the problem is that I've never been this close to a girl like Ayesha before either."
        "Of course, I don't want to get it wrong, but I'm afraid that she might end up choking me out if she's not into it!"
        "But when I do finally pluck up the courage to lean in, I'm surprised to see what her reaction actually is."
        "Sure, she pulls away, refusing to let her lips meet mine."
        "But what's strange is that she does it in a shy, demure manner that seems so at odds with her stature..."
        $ ayesha.love -= 5
        $ ayesha.sub -= 5
        hide ayesha
    elif not ayesha.flags.kiss:
        hide ayesha
        $ ayesha.love += 5
        call ayesha_kiss_reaction_male from _call_expression_213
        show ayesha kiss
        "I've been worrying about trying to kiss Ayesha for so long now that I'm worried it's becoming some kind of problem for me."
        "She's just so different to most of the girls I've dated in the past."
        "And yet being with her is so much of a thrill for just that reason."
        "So in the end, I just think to hell with it, and plant a kiss on her lips."
        "I feel her stiffen straight away, and brace myself for the inevitable rejection."
        "But then she seems to melt under the touch of my lips, returning the kiss like she just can't resist."
        "Something so soft and gentle from someone so strong - it feels like she's opening up for the first time."
        hide ayesha kiss
        $ ayesha.flags.kiss += 1
    else:
        hide ayesha
        $ ayesha.love += 2
        call ayesha_kiss_reaction_male from _call_expression_214
        show ayesha kiss
        "After that first kiss, it's all that I can do to keep from returning for another every chance I get."
        "And it's not just that the kisses are so enjoyable either, which believe me, they are."
        "It's also the chance to see Ayesha shed some of her carefully created image as an Amazon too."
        "The touch of her lips is so soft and gentle, the way she holds me as we share an embrace."
        "She shines in those moments, the femininity that she normally hides coming to the fore."
        "Honestly, it makes me ashamed to have never seen that side of her before now."
        hide ayesha kiss
        $ ayesha.flags.kiss += 1
    return

label ayesha_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show ayesha naked
        if not ayesha.is_sex_slave:
            ayesha.say "[hero.name], can I... Can I please spend the night?"
        elif ayesha.flags.daddy:
            ayesha.say "Daddy, can I... Can I please spend the night?"
        else:
            ayesha.say "Master, can I... Can I please spend the night?"
        menu:
            "No":
                mike.say "No, you shouldn't; I have to get up early tomorrow."
                "The sex was beyond incredible."
                "Frowning a little, Ayesha straightens and collects her clothes in silence."
                ayesha.say "That's OK, sleep well!"
                "She then grins at me, before leaving."
                $ ayesha.love -= 3
                call sleep from _call_sleep_15
            "Yes":
                show cuddle ayesha
                mike.say "Of course you can."
                "I catch a brief moment of joy flash across her face, before she pulls me into a hug, nuzzling into me once again."
                ayesha.say "Thank you..."
                "I'm not sure why she seems so happy about this, but it looks like I picked the right answer."
                if not ayesha.is_sex_slave:
                    ayesha.say "Sleep well, [hero.name]."
                    mike.say "You too."
                elif ayesha.flags.daddy:
                    ayesha.say "Sleep well, Daddy."
                    mike.say "You too my cute little girl."
                else:
                    ayesha.say "Sleep well, Master."
                    mike.say "You too my cute little slave."
                "We both cuddle in silence, drifting off to sleep in each others arms."
                $ ayesha.love += 3
                call sleep ("ayesha") from _call_sleep_16
    $ game.room = "bedroom1"
    return

label ayesha_propose_male:
    show ayesha
    "I guess you never know when you're going to meet the girl that turns out to be 'the one'."
    "But I'm also willing to bet that nobody else ever met that girl in the same way I did."
    "I mean, who'd have thought that a relationship could start with her calling me 'fuck face'?"
    "But those were the first words that Ayesha ever spoke to me, and they were unforgettable!"
    "Even better is that fact that she turned out to be just as unforgettable herself."
    "Well, that and how she stopped calling me fuck face once we actually got to know each other!"
    "Since then I've been on a journey of discovery as our relationship's grown."
    "I could never have believed that there's so much to Ayesha, so much she keeps hidden."
    "She might look like a striding Amazon when she's working her gimmick in the wrestling ring."
    "And she really can be that tough - believe me, I should know!"
    "But underneath that character she's made for herself lies a far more complicated woman."
    "Ayesha's smart, sensitive and possessed of a gentle touch that beggars belief."
    "And of course, she's physically stunning too, put together like a goddess."
    "Some guys might be intimidated by that, think it makes them look like wimps."
    "But I couldn't care less what those morons think."
    "I don't need to be able to bench-press more than my date to feel like a real man!"
    "Okay, okay..."
    "I'm starting to ramble about just how much I adore Ayesha."
    "But I want you to know how I feel and why I need to do this, okay?"
    "Why I need to pick just the right moment to get down on one knee."
    "Then I can look up at her with the ring I picked out in my hand."
    "And I can finally ask the question..."
    mike.say "Ayesha..."
    show fx question
    ayesha.say "Yeah, [hero.name]..."
    ayesha.say "Wha..."
    show ayesha blush
    ayesha.say "What are you doing down there?"
    hide fx
    "Ayesha suddenly looks like a deer in the headlights as she gazes down at me."
    "All the confidence she usually walks around with in public vanishes without a trace."
    "In her confusion, she even seems to miss the ring that I'm holding up to her as well."
    mike.say "Ayesha..."
    mike.say "Will you marry me?"
    show fx exclamation
    "Ayesha blinks in sheer surprise as I ask the question."
    ayesha.say "Why?"
    ayesha.say "Why are you asking me that?!?"
    hide fx
    mike.say "Isn't it obvious, Ayesha?"
    mike.say "Because I love you!"
    mike.say "And I want you to be my wife!"
    "Suddenly the reality of the situation seems to rush in on Ayesha."
    "Her eye grow large and I can almost hear her heart begin to pound in her chest."
    "Ayesha's lips move and she seems to be trying to form words."
    "So I strain to hear what she's saying, hoping for the answer I want to hear..."
    if ayesha.love >= 195:
        ayesha.say "Oh god..."
        ayesha.say "You're serious!"
        ayesha.say "Yes...yes, of course I will!"
        "I'm already shaking my head as I get hastily to my feet."
        "Part of me can't actually believe what I just heard."
        "Did Ayesha really just say yes?!?"
        show ayesha happy
        "As if she can read my mind, Ayesha thrusts her hand at me."
        "I fumble to slip the ring onto her finger, my nerves making me clumsy and uncoordinated."
        "But once I get the damn thing on there, I can finally stand back and collect myself."
        "Well, at least that was the plan."
        "But then I see the look on Ayesha's face."
        "She's smiling...no, she's beaming!"
        "Her face is lit up with happiness like I've never seen it before!"
        mike.say "Ayesha..."
        mike.say "Are you okay?"
        "Ayesha doesn't say anything at first."
        "Instead she nods her head quickly, over and over again."
        "Then she manages to actually get her words out."
        ayesha.say "I...I've never been better!"
        ayesha.say "Oh god..."
        ayesha.say "I can't believe this is actually happening to me!"
        mike.say "What's so hard to believe, Ayesha?"
        mike.say "I love you and I want to marry you!"
        show ayesha normal
        ayesha.say "I...I just always thought, you know..."
        ayesha.say "What with me being so large and all..."
        show ayesha sad
        ayesha.say "And not feminine in the traditional sense of the word..."
        "Ayesha's starting to pick up speed as she says all of this."
        "I can sense that her nerves are getting the better of her."
        "And I try to settle her down, to stop her from babbling."
        mike.say "Don't talk like that, Ayesha."
        mike.say "Being feminine isn't about being petite and fragile."
        mike.say "Sure, your body's built strong."
        mike.say "But your touch is as gentle as a feather."
        show ayesha happy
        ayesha.say "Oh, [hero.name]..."
        ayesha.say "You always know just what to say to me!"
        hide ayesha
        show ayesha kiss
        $ ayesha.flags.kiss += 1
        "Ayesha leans in to kiss me, pulling me into her arms."
        "I return the gesture, loving the sensation of her body against mine."
        "I can't believe it - she said yes!"
        "I'm going to marry the most amazing girl in the world!"
        $ ayesha.set_fiance()
    else:
        ayesha.say "Oh god..."
        ayesha.say "I'm so sorry, [hero.name]..."
        ayesha.say "But I have to say no!"
        "I'm already shaking my head as I get hastily to my feet."
        "Part of me can't actually believe what I just heard."
        "Did Ayesha really just say no?"
        mike.say "Why not, Ayesha?"
        mike.say "What's the problem?"
        mike.say "I thought we were on the same page?"
        show ayesha sad
        "Ayesha's expression is pained as she tries to explain herself."
        "She holds up a hand to keep me back a little."
        "It's like she's afraid of me getting too close to her for some reason."
        ayesha.say "There's no problem, [hero.name]."
        ayesha.say "You have to know that."
        ayesha.say "I love you too - really I do!"
        mike.say "But you don't want to marry me?"
        show fx drop
        "I can see the frustration on Ayesha's face."
        "And I know that this is hurting her as much as it is me."
        hide fx
        ayesha.say "Marrying you sounds good, [hero.name]."
        show ayesha normal
        ayesha.say "But not right now, okay?"
        ayesha.say "I feel like I have some stuff I need to get done."
        ayesha.say "The kind of stuff I don't want to do before I settle down."
        mike.say "Like what, Ayesha?"
        ayesha.say "Like my martial arts, [hero.name]."
        ayesha.say "I want to see how far I can go with it!"
        ayesha.say "Look, I know you're in my metaphorical corner."
        ayesha.say "But I don't want you to be in my literal corner, okay?"
        "I nod slowly as I put the ring away in my pocket."
        "I feel kind of crushed, almost hollowed out."
        "But then I remember something else Ayesha just said."
        mike.say "So..."
        mike.say "This isn't really a no, is it?"
        mike.say "It's more of a not right now?"
        show ayesha happy
        "Ayesha rolls her eyes at me."
        "But she can't help smiling at the same time."
        ayesha.say "That's what I said, [hero.name]!"
        ayesha.say "And I'm not going anywhere, okay?"
        ayesha.say "So let's enjoy being together in the here and now!"
        "That's good enough for me."
        "So I nod and return the smile."
        "After all, it's not like waiting is going to be hard."
        "Not when I'm doing it with Ayesha around."
        $ ayesha.love -= 10
        $ ayesha.sub -= 15
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
