init python:
    Event(**{
    "name": "anna_give_phone_number",
    "label": "give_phone_number",
    "girl": "anna",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(anna,
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
    "name": "anna_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(anna,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "anna",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "anna_auto_greet",
    "label": "auto_greet",
    "girl": "anna",
    "priority": 100,
    "conditions": [
        HeroTarget(IsActivity("None")),
        PersonTarget(anna,
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
    "name": "anna_auto_chat",
    "label": "auto_chat",
    "girl": "anna",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(anna,
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
    "name": "anna_are_you_sick",
    "label": "are_you_sick",
    "girl": "anna",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (anna, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "anna_ask_out",
    "label": "ask_out",
    "girl": "anna",
    "priority": 100,
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(anna,
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
    "name": "anna_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "anna",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label anna_bye(bye_outfit=None):
    call npc_bye_outfit (npc=anna, bye_outfit=bye_outfit) from _call_npc_bye_outfit_2
    $ (day, h, activity, bye_outfit) = _return
    if not activity == anna.activity:
        if day != game.week_day:
            $ anna.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ anna.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"anna {bye_outfit}")
        if activity["activity"] == "sleep":
            anna.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            anna.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            anna.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            anna.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            anna.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            anna.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            anna.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            anna.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            anna.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            anna.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            anna.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            anna.say "I'll go get dressed."
        hide anna
    return

label anna_cheated(action, cheat_npc=None):
    show anna



    if cheat_npc and Harem.together(cheat_npc, anna):
        show anna blush
        anna.say "Hey, That's unfair!"
        anna.say "I wanna have some fun too!"
        show anna kiss
        "And without warning Anna kisses me."
        $ anna.love += 1
        $ anna.flags.kiss += 1
    else:
        show anna cry
        $ loss = 5
        if anna.flags.girlfriend or anna.flags.fiance:
            $ loss += 5
        $ anna.love -= loss
        "I see Anna looking at me [action] someone else sadly, tears welling up in her eyes..."
    hide anna
    return

label anna_greet:
    if renpy.has_label(f"anna_greet_dialogues_{hero.gender}") and not anna.flags.greeted:
        scene expression f"bg {game.room}"
        $ anna.flags.greeted = TemporaryFlag(True, 1)
        show anna
        $ result = randint(1, 3)
        if result == 1:
            anna.say "Hello, [hero.name]."
        elif result == 2:
            anna.say "Hi, [hero.name]."
        elif result == 3:
            anna.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                anna.say "Good morning [hero.name]."
            elif game.hour < 19:
                anna.say "Good afternoon [hero.name]."
            else:
                anna.say "Good evening [hero.name]."
        call expression f"anna_greet_dialogues_{hero.gender}" from _call_expression_208
        if anna.flags.submissive_interact:
            if randint(0, 1) == 0:
                anna.say "You can use the front door or the back, [hero.name] - as long as you cum inside!"
            else:
                anna.say "Front or back [hero.name], it's your choice."
                mike.say "What?"
                anna.say "You choose [hero.name], fuck me front or back!"
        hide anna
    return

label anna_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Anna."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Anna."
        elif game.hour < 12:
            mike.say "Good morning Anna."
        elif game.hour < 19:
            mike.say "Good afternoon Anna."
        else:
            mike.say "Good evening Anna."
    return

label anna_kiss:
    scene expression f"bg {game.room}"
    if anna.love < 25 and not anna.is_girlfriend and not game.active_date.score >= 75:
        show anna
        "When Anna's up, she's seriously up and it's hard not to get swept along with her mood too."
        "Right now she's practically bouncing with good vibes and infecting me with the same."
        "So can you really blame me for trying to kiss her when she leans in close to me a moment later?"
        "How was I to know that she just wanted to whisper something and make sure that I heard it?"
        "But no matter what she was wanting to say to me, it's soon forgotten in the wake of my own mistake."
        "And if you want to know what'll kill a good mood in Anna, then look no further than what I just did!"
        $ anna.love -= 5
        $ anna.sub -= 5
        hide anna
    elif not anna.flags.kiss:
        hide anna
        $ anna.love += 5
        if anna.lesbian > MAX_LES_GUY_SEX:
            $ anna.lesbian -= 1
        show anna kiss
        "It's embarrassing to admit, but I've actually been preoccupied with kissing Anna for the first time."
        "Not that the act itself worries or frightens me, just the mechanics of managing to bend down and make it happen."
        "She's so petite that I just don't know how it'll go when I commit to the act!"
        "But in the end, it kind of makes it better."
        "Seeing that cute face looking up at me as I take the plunge, those huge eyes wide with anticipation."
        "Anna goes on her tip-toes, even jumps a little to meet me halfway."
        "And the effort we both have to put in makes the moment that much more special."
        hide anna kiss
        $ anna.flags.kiss += 1
    else:
        hide anna
        $ anna.love += 2
        show anna kiss
        "Sure, I can lean in to plant one on Anna or answer her call when she wants to kiss me."
        "But what I really enjoy are the times when we can get away with doing something that levels us out."
        "When the coast is clear, Anna hops into my arms, almost clinging to me."
        "Or else she sits on my lap and drapes her arms around my neck."
        "Say what you like about tall, elegant women and what they're capable of."
        "None of it compares to the charms of a laptop..."
        hide anna kiss
        $ anna.flags.kiss += 1
    return

label anna_propose_male:
    show anna
    "It should have been the most straight-forward thing in the world to just come out and ask Anna the question."
    "I mean, we've been spending almost every free moment that we have together for quite some time now."
    "Even when we're not together, she's constantly on my mind until the next time we can meet up."
    "And I know full well that this isn't just an infatuation on my part too."
    "Anna calls me up every chance she gets, and failing that, messages me constantly."
    "Normally that kind of neediness, someone clinging to me the whole time..."
    "Well, it'd feel pretty annoying, maybe even creepy."
    "But with Anna, somehow it never does."
    "And I find myself looking forward to each and every time she reaches out to me."
    "I guess the explanation is really quite simple - I love her."
    "I couldn't deny it, not even if I wanted to."
    "Which is why I feel that I'm doing exactly the right thing when I get down on one knee in front of Anna."
    "The effect is kind of spoiled by the fact that she's looking away when I do it."
    "Meaning that when she turns her head back in my direction, there's an awkward moment of confusion."

    show fx question
    anna.say "Ah...[hero.name]?"
    anna.say "Where'd you go?"
    mike.say "I'm down here, Anna."
    "Anna looks down at me."
    "And then jumps slightly at finding me so close and yet out of her field of vision."
    anna.say "Ooh, there you are!"
    anna.say "What's the matter - did you drop something?"
    "By now I have a smile held on my face, determined to make this come off as I envisioned it."
    mike.say "Erm, no..."
    mike.say "Not exactly, Anna."
    mike.say "I wanted to ask..."
    mike.say "I mean, I've been trying to pluck up the courage..."
    "I watch as understanding seems to dawn upon Anna, her eyes flashing with sudden recognition."
    "It comes as some relief."
    "Making me think that I can get up off of my knee soon and slip the ring on her finger."
    anna.say "You're being silly, [hero.name]."
    show anna wink
    anna.say "You don't have to kneel down to ask me that!"
    mike.say "I...I don't?"
    "At this, Anna leans in closer and whispers conspiratorially into my ear."
    anna.say "No - you already know how much I LOVE it when you take me up the ass!"
    "Ah, I see the problem here."
    "It seems as though Anna's got the wrong end of a totally different stick!"
    mike.say "No, Anna, no!"
    mike.say "I wanted to ask if you'd marry me!"
    show anna surprised
    "Instantly Anna's face becomes a mask of absolute horror."
    anna.say "Oh no...oh no!"
    anna.say "You must think I'm such a stupid cow!"
    anna.say "And that I'm a complete pervert as well!"
    anna.say "Urgh - Anna, how could you BE so dumb?!?"
    anna.say "Dumb, dumb, dumb!"
    mike.say "Whoa there, Anna, please!"
    mike.say "It was just a simple misunderstanding, that's all."
    mike.say "I don't think you're dumb."
    mike.say "I...I think you're amazing, actually."
    mike.say "And that's why I want to marry you..."
    "It's at this precise moment in time that I produce the ring, offering it to her as I do so."
    if anna.love < 195:
        show anna annoyed
        "Anna shakes her head at me, already starting to back away."
        "I reach out my hands, trying to appeal for her to stay."
        "But she holds out her own hands in front of her, waving me off."
        anna.say "No, [hero.name]!"
        anna.say "I...I can't marry you."
        anna.say "I'm a fucking mess."
        anna.say "I'd...I'd just embarrass you!"
        "By now, I'm shaking my head too."
        "I get up off of my knees, still trying to plead with Anna the whole time."
        mike.say "Anna, I've never been embarrassed of you."
        mike.say "How could I be?"
        show anna -annoyed
        anna.say "I know what you're trying to do, [hero.name]."
        anna.say "But it won't work."
        anna.say "I won't let you let me screw up your life!"
        "And with that, Anna turns and dashes away as fast as she's able."
        "My first instinct is to run straight after her, as catching her wouldn't exactly be a challenge."
        "But then I stop myself from doing it, remembering how adamant she was just now."
        "Maybe it's better to let her run away, at least for a little while."
        "The chance to clear her head and really think about my proposal might be just what she needs."
        "I only hope that Anna's notoriously ditzy brain can come down from where she is right now for long enough."
        $ anna.love -= 25
        $ anna.sub -= 25
    else:
        show anna dazed close
        anna.say "Ooh..."
        anna.say "So that's what you meant, silly."
        anna.say "That's way better than anal!"
        "Anna pauses for a second, clearly considering what she just said."
        show anna wink
        anna.say "Well, maybe not better."
        anna.say "But as good as..."
        mike.say "So..."
        mike.say "Is that a yes?"
        "Anna looks at me for a moment as if stunned."
        "Then she shakes her head as she recalls what's actually going on right now."
        show anna happy
        anna.say "Oh, yeah, sorry, [hero.name]!"
        anna.say "Yes..."
        anna.say "I mean yes, it's a yes..."
        anna.say "You know what I mean, right?"
        "I can't help shaking my own head a little and chuckling."
        "That's my girl alright!"
        mike.say "Yeah, Anna, I do."
        "And with that, I stand up and slip the ring onto Anna's finger."
        "She has a grin a mile wide on her face the whole time, almost hopping with excitement."
        show fx heart
        anna.say "Yay...I'm going to get married!"
        anna.say "Married to you!"
        mike.say "Well, yes, Anna - that was kind of the idea!"
        "Anna throws her arms around my waist, hugging me with all of her strength."
        "And I return the gesture, enjoying the sensation of her pressed against me."
        "A sensation that's made all the more pleasant by the knowledge that she said yes."
        "The knowledge that I should get to do this with her for the rest of my life."
        $ anna.set_fiance()
    hide anna
    return

label anna_ask_date_male:
    if Harem.find(anna):
        menu:
            "Ask Anna on a date":
                call anna_ask_date_alone_male from _call_anna_ask_date_alone_male
            "Meet Anna and Kleio for a 'hot coffee'" if Harem.together(anna, kleio, name="band"):
                call anna_ask_date_kleio from _call_anna_ask_date_kleio
            "Meet Anna, Kleio and Sasha for a 'hot coffee'" if Harem.together(anna, kleio, sasha, name="band"):
                call anna_ask_date_kleio_sasha from _call_anna_ask_date_kleio_sasha
            "Meet Anna, Emma and Kat at the beach" if Harem.find_by_name("petite") and Harem.together(anna, emma, kat, name="petite") and "petite_harem_event_04_sex" in DONE and game.season in [0, 1]:
                call anna_ask_date_emma_kat from _call_anna_ask_date_emma_kat
    else:
        call anna_ask_date_alone_male from _call_anna_ask_date_alone_male_1
    return _return

label anna_ask_date_alone_male:
    mike.say "Anna, would you like to go on a date with me?"
    if anna.love < 50 or anna.flags.nodate:
        anna.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        anna.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice

label anna_ask_date_kleio:
    mike.say "Do you want to get together with Kleio and have some fun?"
    anna.say "I'd love to."
    call select_date_time from _call_select_date_time
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call kleio_anna_threesome from _call_kleio_anna_threesome_1
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna"], "kleio_anna_threesome"))
    return

label anna_ask_date_kleio_sasha:
    mike.say "Do you want to get together with Kleio and have some fun?"
    anna.say "I'd love to."
    call select_date_time from _call_select_date_time_1
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    menu:
        "See you in Sasha's room":
            if day == "now":
                call kleioannafoursome from _call_kleioannafoursome
            else:
                $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome"))
        "Let's meet in my room" if "kleioannafoursome2" in DONE:
            if day == "now":
                call kleioannafoursome2 from _call_kleioannafoursome2
            else:
                $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome2"))
    return

label anna_ask_date_emma_kat:
    mike.say "Do you want to have some fun at the beach with Emma and Kat?"
    anna.say "I'd love to."
    call select_date_time (fixed_hour=14, fixed_season="summer") from _call_select_date_time_27
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call petite_harem_foursome_intro from _call_petite_harem_foursome_intro
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "petite", ["anna", "emma", "kat"], "petite_harem_foursome_intro"))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
