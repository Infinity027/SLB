init python:
    Event(**{
    "name": "claire_give_phone_number",
    "label": "give_phone_number",
    "girl": "claire",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(claire,
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
    "name": "claire_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "claire",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(claire,
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
    "name": "claire_auto_greet",
    "label": "auto_greet",
    "girl": "claire",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(claire,
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
    "name": "claire_auto_chat",
    "label": "auto_chat",
    "girl": "claire",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(claire,
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
    "name": "claire_are_you_sick",
    "label": "are_you_sick",
    "girl": "claire",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(claire,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (claire, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "claire_ask_out",
    "label": "ask_out",
    "girl": "claire",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(claire,
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
    "name": "claire_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "claire",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(claire,
            Not(IsHidden()),
            IsPresent(),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label claire_greet:
    if not claire.flags.greeted:
        scene expression f"bg {game.room}"
        show claire
        $ claire.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            claire.say "Hello, [hero.name]."
        elif result ==2:
            claire.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                claire.say "Good morning [hero.name]."
            elif game.hour < 19:
                claire.say "Good afternoon [hero.name]."
            else:
                claire.say "Good evening [hero.name]."
        call expression f"claire_greet_dialogues_{hero.gender}" from _call_expression_538
        hide claire
    return

label claire_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Claire."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Claire."
        elif game.hour < 12:
            mike.say "Good morning Claire."
        elif game.hour < 19:
            mike.say "Good afternoon Claire."
        else:
            mike.say "Good evening Claire."
    return

label claire_bye(bye_outfit=None):
    call npc_bye_outfit (npc=claire, bye_outfit=bye_outfit) from _call_npc_bye_outfit_27
    $ (day, h, activity, bye_outfit) = _return
    if not activity == claire.activity:
        if day != game.week_day:
            $ claire.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ claire.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"claire {bye_outfit}")
        if activity["activity"] == "sleep":
            claire.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "wash"]:
            claire.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            claire.say "I'm working right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            claire.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            claire.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            claire.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            claire.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            claire.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            claire.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            claire.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            claire.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            claire.say "I'll go get dressed."
        hide claire
    return





































label claire_kiss:
    scene expression f"bg {game.room}"
    show claire normal
    "I've been longing for the moment to be right almost since the first moment I Claire came back into my life."
    "And even before that I can remember looking longingly at those full, sensual lips of hers and dreaming."
    "Imagining what it would be like to just lean in and place mine against them, to kiss her with a passion."
    "But now that we're spending so much time together and making a real connection, things are different, right?"
    "Now it's just a case of waiting for the opportunity to present itself, for the kiss to occur naturally."
    "And even as those same thoughts are passing through my mind, the moment semes to occur right in front of me."
    "Claire's eyes catch mine, and there's a seductive smile on her face as she regards me."
    "Then she leans slightly towards me, a movement that's really no more than the tilting of her head."
    "But to me it's an open invitation to make my move, and instinct kicks in no more than a second later."
    "I instinctively close my eyes and slightly part my lips, knowing that she's close enough for it to happen."
    "Then all I can do is wait for what seems like an eternity as I will everything to come together just right."
    "As I wait for the long anticipated kiss to actually happen."
    if claire.love + hero.charm < 80 and not claire.is_girlfriend and not game.active_date.score >= 75:
        show claire surprised
        claire.say "Whoa..."
        claire.say "Settle down there, stud!"
        show claire stuned
        "Suddenly the sound of Claire's voice breaks the spell and my eyes snap open."
        $ claire.love -= 1
        "At the same time I realise that she's pulled back, well out of my reach."
        "This leaves me overstretched and totally exposed, basically looking like a complete fool."
        "As quickly as I can, I struggle to at least regain my balance and not fall over."
        "Because any chance to preserve my dignity has long since vanished."
        "Just like the chance to enjoy a sweet, sensual kiss with Claire."
        hide claire
    elif not claire.flags.kiss:
        hide claire
        show claire kiss
        with fade
        "The moment the kiss begins, I realise that all of my speculation was pointless."
        "Because I could never have imagined that kissing Claire would feel like this."
        "I have no idea how simple contact between our lips can create such a sensation."
        "Something that sends shivers thorough the whole of my body, making my hair stand on end."
        "And it comes close to blowing my mind as well, making my brain feed back on itself."
        "Oh, and please don't get the impression that this is me flailing on one end of the kiss."
        "Because Claire is really leaning into it too, her arms pulling me closer all the time."
        "And I swear that I can feel the sensation of her heart beating in her chest."
        "Maybe even the pulsing of her blood in the veins beneath the surface of her skin too."
        "She's hot, agitated and every bit as lost in the moment as I am right now."
        "And neither of us seems to be in the least bit interested in ending the kiss."
        "Instead it goes on, as if compensating for the years I've been waiting for it to happen."
        "Neither of us willing to be the one that brings it to an end."
        $ claire.love += 5
        $ claire.flags.kiss += 1
        if claire.lesbian > MAX_LES_GUY_SEX:
            $ claire.lesbian -= 1
        hide claire kiss
        show claire normal
        with fade
    else:
        hide claire
        show claire kiss
        with fade
        $ claire.love += 2
        $ claire.flags.kiss += 1
        if claire.lesbian > MAX_LES_GUY_SEX:
            $ claire.lesbian -= 1
        "I can't believe that I waited so long to be able to kiss Claire for the first time."
        "And now it feels like she turns and puts her lips to mine whenever the chance presents itself."
        "The kisses are all different, some long and lingering, others short and passionate."
        "But what really leaves me breathless is the sheer number of them."
        "Claire seems to be even hungrier to put her lips to mine than I ever was to kiss her."
        "And don't worry about the novelty of being able to kiss a woman I've desired for so long fading."
        "Because each and every one of those kisses feels almost as intense and passionate as the first."
        hide claire kiss
        show claire normal
        with fade
    return

label claire_sleep_date_fuck:
    show cuddle claire
    show bg black with dissolve
    "The both of us are asleep before we can even consider cleaning up."
    call sleep ("claire") from _call_sleep_127
    $ game.room = "bedroom1"
    return

label claire_cheated(action, cheat_npc=None):
    if cheat_npc and Harem.together(cheat_npc, claire):
        show claire happy blush
        claire.say "Aren't you forgetting something?"
        show claire normal
        "And without warning Claire kisses me."
        $ claire.love += 1
        $ claire.flags.kiss += 1
    else:
        show claire pained
        "The kiss is short and sweet, but infinitely passionate - yet when it ends, I see Claire, staring at me with horror contorting her face."
        show claire sad
    return

label claire_propose_male:
    show claire normal
    "Just getting to reconnect with Claire as an adult was a thrill for me."
    "And back then I never imagined we'd become anything more than friends."
    "So when it started to become clear she had feelings for me like I did for her..."
    "Well, you can imagine that I felt like I was having my mind blown!"
    "I couldn't have foreseen that we'd actually start dating each other."
    "And that we would quickly realise that we were totally compatible too."
    "From there it just feels like everything started to fall into place."
    "Like what we have is totally natural and keeps on growing as a result."
    "So much so that it took me a while to realise that I wanted to take it to the next level."
    "That I needed to do something that would make the relationship between us formal."
    "So now here I am, feeling the weight of a ring in my pocket."
    "And waiting with baited breath for the right moment to arrive."
    "Claire doesn't seem to notice just how nervous I am."
    "Or if she does, then she's doing a good job of hiding it from me."
    "All the same, my mind is clear enough to know when the moment comes."
    "And almost without thinking, I get down onto one knee and pull out the ring."
    show claire surprised
    claire.say "[hero.name]..."
    claire.say "What..."
    claire.say "What are you doing?"
    show claire stuned
    "Holding up the ring, I look Claire straight in the eye."
    "And I do the best I can to keep my voice level as I ask the question."
    mike.say "Claire..."
    mike.say "We've only been together a short while, I know."
    mike.say "But in that time, you've made me happier than I can ever remember being."
    mike.say "And I want to keep that feeling forever - so, will you marry me?"
    if claire.love >= 195:
        "Claire stares at me in silence, her eyes wide and filled with shock."
        "And for a few terrible seconds I think that she's going to say no."
        show claire happy
        "But then I see that she's nodding her head, and I feel a flood of relief wash over me."
        show claire talkative
        claire.say "YES!"
        claire.say "Yes, I will."
        claire.say "Of course I'll marry you!"
        show claire happy
        "I find myself almost leaping to my feet as I hear the answer that I wanted."
        "And in my eagerness to shove the ring onto Claire's finger, I almost drop it."
        "But with her help, I finally manage to slide the thing into place."
        "Then I take a step back, my head still spinning as I watch her admiring it."
        show claire normal
        mike.say "Phew..."
        mike.say "I was worried..."
        mike.say "Worried that you might say no."
        "Claire looks up from the ring and her eyes meet mine."
        "And in that moment I can feel myself blushing from the look she's giving me."
        "Because it's one of genuine surprise and disbelief."
        show claire talkative
        claire.say "Whatever gave you that idea?"
        show claire normal
        mike.say "Well...you have been down this road before."
        mike.say "And it didn't really end all that well - did it?"
        show claire happy
        "The smile that spreads over Claire's face almost makes me catch my breath."
        show claire talkative
        claire.say "[hero.name], you're not Hector."
        claire.say "In fact, you're about as far from him as it's possible to be!"
        claire.say "And our marriage is going to be very different too."
        claire.say "Now let's get our thinking caps on."
        claire.say "Because we've got a wedding to plan!"
        $ claire.set_fiance()
    else:
        "Almost the same moment that Claire sets eyes on the ring, I feel a pang of disappointment."
        "Because as she sees what I have in my hand, her expression changes to one of disapproval."
        "And before I can say another word, she's shaking her head and taking a step backwards."
        show claire whining
        claire.say "Oh no..."
        claire.say "You can't be asking me that, [hero.name]..."
        claire.say "Seriously, you can't!"
        show claire sad
        $ claire.love -= 25
        $ claire.sub -= 25
        "Without thinking I begin to get up from where I'm kneeling."
        "My instinct to comfort Claire drawing me closer to her."
        "But I still have the ring held out in front of me."
        "And it's presence seems to make her draw further back and away from me."
        "At least until I realise the problem and stuff it back into my pocket."
        mike.say "Claire, I know that it's a big thing to ask."
        mike.say "But I just feel like this is the natural next step for us."
        show claire whining
        claire.say "Maybe it is for you, [hero.name]."
        claire.say "But I only just got out of a marriage that went wrong."
        claire.say "And sure, I know that you're not at all like Hector."
        claire.say "But I still don't want to be trapped like that again."
        show claire sad
        "I can see from the look in Claire's eyes that she's totally serious."
        "There's genuine emotion in them - anxiety, trepidation and pain."
        "And the last thing that I want is to add to them in any way."
        "So I just nod my head, resigning myself to doing what's best for her."
        "That and hoping that, in time, she might come to change her mind."
    hide claire
    return

label claire_ask_date_male:






    call claire_ask_date_alone_male from _call_claire_ask_date_alone_male_1
    return _return

label claire_ask_date_alone_male:
    mike.say "Claire, would you like to go on a date with me?"
    if claire.flags.nodate:
        claire.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        claire.say "Sure, it might be fun, when do you want us to go?"
        return True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
