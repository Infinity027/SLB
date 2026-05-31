init python:
    Event(**{
    "name": "amy_give_phone_number",
    "label": "give_phone_number",
    "girl": "amy",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(amy,
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
    "name": "amy_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "amy",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(amy,
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
    "name": "amy_auto_greet",
    "label": "auto_greet",
    "girl": "amy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(amy,
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
    "name": "amy_auto_chat",
    "label": "auto_chat",
    "girl": "amy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(amy,
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
    "name": "amy_are_you_sick",
    "label": "are_you_sick",
    "girl": "amy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(amy,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (amy, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_ask_out",
    "label": "ask_out",
    "girl": "amy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(amy,
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
    "name": "amy_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "amy",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(amy,
            Not(IsHidden()),
            IsPresent(),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label amy_greet:
    if renpy.has_label(f"amy_greet_dialogues_{hero.gender}") and not amy.flags.greeted:
        scene expression f"bg {game.room}"
        show amy
        $ amy.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            amy.say "Hello, [hero.name]."
        elif result ==2:
            amy.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                amy.say "Good morning [hero.name]."
            elif game.hour < 19:
                amy.say "Good afternoon [hero.name]."
            else:
                amy.say "Good evening [hero.name]."
        call expression f"amy_greet_dialogues_{hero.gender}" from _call_expression_455
        hide amy
    return

label amy_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Amy."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Amy."
        elif game.hour < 12:
            mike.say "Good morning Amy."
        elif game.hour < 19:
            mike.say "Good afternoon Amy."
        else:
            mike.say "Good evening Amy."
    return

label amy_bye(bye_outfit=None):
    call npc_bye_outfit (npc=amy, bye_outfit=bye_outfit) from _call_npc_bye_outfit_22
    $ (day, h, activity, bye_outfit) = _return
    if not activity == amy.activity:
        if day != game.week_day:
            $ amy.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ amy.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"amy {bye_outfit}")
        if activity["activity"] == "sleep":
            amy.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            amy.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            amy.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            amy.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            amy.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            amy.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            amy.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            amy.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            amy.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            amy.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            amy.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            amy.say "I'll go get dressed."
        hide amy
    return
































label amy_kiss:
    scene expression f"bg {game.room}"
    show amy
    "This seems like as good of a time as any to make my move."
    show amy close
    "So taking a deep breath, I lean in to plant a kiss on Amy's lips..."
    if amy.love + hero.charm < 80 and not amy.is_girlfriend and not game.active_date.score >= 75:
        show amy surprised
        amy.say "Wha...what are you doing?!?"
        show amy angry -close with hpunch
        $ amy.love -= 1
        "Amy leans backwards at the same time as she pushes me away from her."
        "This leaves me reeling with a surprised look on my face."
        "And I can already feel my cheeks starting to burn with embarrassment too."
        hide amy
    elif not amy.flags.kiss:
        hide amy
        show amy kiss
        with dissolve
        "Amy's eyes are wide with surprise as her lips meet mine."
        "But it only takes a few seconds for her to surrender."
        $ amy.love += 5
        $ amy.flags.kiss += 1
        if amy.lesbian > MAX_LES_GUY_SEX:
            $ amy.lesbian -= 1
        "Then her eyes close and she leans into the kiss."
        "And from that point on, it gets better with every passing moment."
        hide amy kiss
    else:
        hide amy
        show amy kiss
        $ amy.love += 2
        $ amy.flags.kiss += 1
        if amy.lesbian > MAX_LES_GUY_SEX:
            $ amy.lesbian -= 1
        "Amy doesn't hesitate to return the kiss."
        "Her lips against mine, it's slow and sensual."
        "Then she really starts leaning into it too."
        "Tongues are getting involved now, and it's becoming intense!"
        "Almost like she's trying to make up for not being the one to get it started."
        hide amy kiss
    return

label amy_sleep_date_fuck(location="hero"):
    show cuddle amy
    show bg black with dissolve
    "The both of us are asleep before we can even consider cleaning up."
    call sleep ("amy") from _call_sleep_69
    $ game.room = "bedroom1"
    return

label amy_cheated(action, cheat_npc=None):
    if cheat_npc and Harem.together(cheat_npc, amy):
        show amy flirt
        amy.say "Aren't you forgetting something?"
        show amy
        "And without warning Amy kisses me."
        $ amy.love += 1
        $ amy.flags.kiss += 1
    else:
        show amy angry
        "The moment I open my eyes, I see Amy, staring at me in horror!"
    return

label amy_propose_male:
    show amy at center, zoomAt (1.0, (640, 720))
    "I can already feel the anxiety making my stomach churn and groan."
    "But I keep on telling myself that I have to see this thing through."
    "If I let my fear get the better of me now, then I'll regret it for the rest of my life!"
    "So I take a deep breath, and I wait for the perfect moment to do it..."
    show amy b puzzled at center, traveling (1.5, 0.5, (640, 1040))
    amy.say "Huh..."
    amy.say "[hero.name]?"
    amy.say "Where'd you...."
    show amy b surprised blush at center, zoomAt (1.0, (640, 1040)), startle
    show fx exclamation
    amy.say "Oh...oh wow!"
    "I smile as I look up at Amy from where I'm kneeling on the ground."
    "And I'm kind of hoping that the ring I'm holding is cluing her in on what's going on."
    "But just to be sure, I feel like I have to say the obligatory line too."
    hide fx
    mike.say "Amy..."
    mike.say "I have to know..."
    mike.say "Will you marry me?"
    "I was expecting a quirky, even spiky response from Amy."
    "But in reality, she seems completely floored by the question."
    if amy.love >= 195:
        amy.say "I..."
        show amy happy -blush
        amy.say "I...I will!"
        amy.say "I mean, yes...yes, I'll marry you!"
        show amy normal
        "Amy's still nodding as I start to get to my feet."
        "And she thrusts out her hand as soon as I'm vertical again."
        "I don't waste any time pushing the ring onto her finger."
        "It seems both of us are almost scared that someone will come along and stop us!"
        "I step back and Amy keeps her hand held out in front of her."
        "It's pretty clear to see that she's admiring how it looks on her finger."
        mike.say "Phew..."
        mike.say "I've got to tell you, Amy..."
        mike.say "I was pretty nervous asking you the question!"
        hide amy
        show amy a close flirt
        with vpunch
        "Amy throws her arms around me, pulling me close to her."
        "At the same time, she's burying her head into my shoulder."
        "And it feels so good that I almost forget what I just said to her."
        show amy blush
        amy.say "Aw..."
        amy.say "That's so sweet, [hero.name]."
        amy.say "I felt the exact same way when I saw the ring!"
        show amy happy -blush
        amy.say "But now I'm just feeling really good!"
        "I have to admit that I'm feeling the same way too."
        "My fear and anxiety are being replaced by excitement and anticipation."
        $ amy.set_fiance()
    else:
        amy.say "[hero.name]..."
        show amy -blush
        amy.say "I..."
        $ amy.love -= 25
        $ amy.sub -= 25
        show amy shy
        amy.say "I can't say yes."
        amy.say "I just can't."
        "The anxiety and fear in my stomach is suddenly gone."
        "But in it's place, I can feel disappointment and despair."
        "Slowly I get back to my feet and put the ring away again."
        mike.say "I'm...sorry, I guess?"
        mike.say "I really don't know what to say!"
        "I can see that Amy's not proud of the effect her answer is having."
        "She looks embarrassed and even worried about the way I'm reacting."
        "But there's nothing I can do about that right now."
        "I couldn't resist my emotions in choosing to propose to Amy."
        "So I can't just turn them off now in order to protect her feelings."
        show amy sad
        amy.say "I'm sorry, [hero.name]..."
        amy.say "It's...it's not you, it's me!"
        "Oh god, not that - anything but that!"
        mike.say "It's okay, Amy..."
        mike.say "You don't have to apologise."
        mike.say "I just misjudged the situation, that's all."
        "I try to smile and laugh it off."
        "But I have no idea where we go from here."
    hide amy
    return

label amy_ask_date_male:
    if Harem.find(amy) and "goth_harem_event_01" in DONE:
        menu:
            "Ask Amy on a date":
                call amy_ask_date_alone_male from _call_amy_ask_date_alone_male
            "Meet Amy and Violaine for a 'hot coffee'" if Harem.find_by_name("goth") and "goth_harem_event_01" in DONE:
                call amy_ask_date_violaine from _call_amy_ask_date_violaine
            "Meet Amy and Vincent for a 'hot coffee'" if Harem.find_by_name("goth") and "goth_harem_event_02" in DONE:
                call amy_ask_date_vincent from _call_amy_ask_date_vincent
            "Meet Amy, Vincent and Violaine for a 'hot coffee'" if Harem.find_by_name("goth") and "goth_harem_event_03" in DONE:
                call amy_ask_date_vincent_violaine from _call_amy_ask_date_vincent_violaine
    else:
        call amy_ask_date_alone_male from _call_amy_ask_date_alone_male_1
    return _return

label amy_ask_date_alone_male:
    mike.say "Amy, would you like to go on a date with me?"
    if amy.flags.nodate:
        amy.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        amy.say "Sure, it might be fun, when do you want us to go?"
        return True

label amy_ask_date_violaine:
    mike.say "Do you want to get together with Violaine and have some fun?"
    amy.say "Fine, but you'll join us home."
    mike.say "I can do that."
    call select_date_time (fixed_hour=20) from _call_select_date_time_31
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call goth_harem_threesome_violaine_intro from _call_goth_harem_threesome_violaine_intro
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "goth", ["amy"], "goth_harem_threesome_violaine_intro"))
    return

label amy_ask_date_vincent:
    mike.say "Do you want to get together with Vincent and have some fun?"
    amy.say "Fine, but you'll join us home."
    mike.say "I can do that."
    call select_date_time from _call_select_date_time_32
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call goth_harem_threesome_vincent_intro from _call_goth_harem_threesome_vincent_intro
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "goth", ["amy"], "goth_harem_threesome_vincent_intro"))
    return

label amy_ask_date_vincent_violaine:
    mike.say "Do you want to get together with Vincent and Violaine and have some fun?"
    amy.say "Fine, but you'll join us home."
    mike.say "I can do that."
    call select_date_time from _call_select_date_time_33
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call goth_harem_foursome_vincent_violaine_intro from _call_goth_harem_foursome_vincent_violaine_intro
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "goth", ["amy"], "goth_harem_foursome_vincent_violaine_intro"))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
