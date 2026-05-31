init python:
    Event(**{
    "name": "lexi_give_phone_number",
    "label": "give_phone_number",
    "girl": "lexi",
    "conditions": [
        PersonTarget(lexi,
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
    "name": "lexi_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(16, 17),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(lexi,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "lexi",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_auto_greet",
    "label": "auto_greet",
    "girl": "lexi",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsActivity("None")),
        PersonTarget(lexi,
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
    "name": "lexi_auto_chat",
    "label": "auto_chat",
    "girl": "lexi",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(lexi,
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
    "name": "lexi_are_you_sick",
    "label": "are_you_sick",
    "girl": "lexi",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (lexi, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_ask_out",
    "label": "ask_out",
    "girl": "lexi",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(IsActivity("ask_date"))),
        PersonTarget(lexi,
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
    "name": "lexi_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "lexi",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "lexi_masturbation",
    "priority": 500,
    "label": "lexi_masturbation",
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(23, 3),
        HeroTarget(
            IsGender("male"),
            IsActivity("sleep"),
           ),
        PersonTarget(lexi,
            Not(IsHidden()),
            IsRoom("livingroom"),
            IsActivity("sleep"),
            ),
        "(game.days_played - lexi.sexperience.last) <= 7",
        ],
    "chances": 20,
    "do_once": False,
    "once_day": True,
    })

label lexi_bye(bye_outfit=None):
    call npc_bye_outfit (npc=lexi, bye_outfit=bye_outfit) from _call_npc_bye_outfit_14
    $ (day, h, activity, bye_outfit) = _return
    if not activity == lexi.activity:
        if day != game.week_day:
            $ lexi.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ lexi.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"lexi {bye_outfit}")
        if activity["activity"] == "sleep":
            lexi.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            lexi.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            lexi.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            lexi.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            lexi.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            lexi.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            lexi.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            lexi.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            lexi.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            lexi.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            lexi.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            lexi.say "I'll go get dressed."
        hide lexi
    return

label lexi_cheated(action, cheat_npc=None):
    show lexi flirt
    "I see Lexi looking at me [action] someone else with envy and lust in her eyes."
    $ lexi.love += 1
    hide lexi
    return

label lexi_greet:
    if renpy.has_label(f"lexi_greet_dialogues_{hero.gender}") and not lexi.flags.greeted:
        scene expression f"bg {game.room}"
        $ lexi.flags.greeted = TemporaryFlag(True, 1)
        show lexi
        $ result = randint(1, 3)
        if result == 1:
            lexi.say "Hello, [hero.name]."
        elif result == 2:
            lexi.say "Hi, [hero.name]."
        elif result == 3:
            lexi.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                lexi.say "Good morning [hero.name]."
            elif game.hour < 19:
                lexi.say "Good afternoon [hero.name]."
            else:
                lexi.say "Good evening [hero.name]."
        call expression f"lexi_greet_dialogues_{hero.gender}" from _call_expression_248
        if lexi.flags.submissive_interact:
            if randint(0, 1) == 0:
                lexi.say "Hey, [hero.name] - you wanna grab a piece of this?"
                "Lexi spanks loudly her own butt cheek."
            else:
                lexi.say "Which piece [hero.name]?"
                mike.say "Huh?"
                lexi.say "Which piece do you prefer dummy! Ass, tits or pussy?"
        hide lexi
    return

label lexi_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Lexi."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Lexi."
        elif game.hour < 12:
            mike.say "Good morning Lexi."
        elif game.hour < 19:
            mike.say "Good afternoon Lexi."
        else:
            mike.say "Good evening Lexi."
    return

label lexi_kiss_reaction_male:
    if lexi.lesbian > MAX_LES_GUY_SEX:
        $ lexi.lesbian -= 1
    return

label lexi_kiss_male:
    scene expression f"bg {game.room}"
    if lexi.love + hero.charm < 80 and not lexi.is_girlfriend and not game.active_date.score >= 75:
        show lexi
        "I've made the mistake of going in for a kiss with a girl and getting my nose put out of joint before."
        "But whenever I did, I was used to a disapproving look, a yelp of surprise, or even a slap in the most extreme of cases."
        "Yet when I see Lexi pull away, there's none of that."
        "Instead she fixes me with a wry smile, almost as if she's amused by my fumbling efforts."
        "She shakes her head and waves a finger in front of my face, telling me off for trying to get intimate."
        "All this leaves me with the impression that the timing was wrong, rather than the notion of kissing her."
        $ lexi.love -= 1
        hide lexi
    elif not lexi.flags.kiss:
        hide lexi
        call lexi_kiss_reaction_male from _call_lexi_kiss_reaction_male
        show lexi kiss
        "Nothing's exactly a traditional picture of romance or seduction with Lexi, as she's just not that kind of girl."
        "So it's no great surprise to me that our first kiss comes in a moment of awkward fumbling, rather than poetic grace."
        "There's hands in random places and body-parts rubbing against each other, and everything feels like a mess."
        "In the middle of all that, I feel my lips brush against Lexi's, and just decide to go for it."
        "She responds almost instantly, tongue pushing against my own lips as though desperate to be let in."
        "Like I said, there's no romance in it, but there's a hell of a lot of passion."
        "And maybe more lust..."
        hide lexi kiss
        $ lexi.flags.kiss += 1
        $ lexi.love += 5
    else:
        hide lexi
        call lexi_kiss_reaction_male from _call_lexi_kiss_reaction_male_1
        show lexi kiss
        "Lexi's never been shy, and she likes to make a show of every kiss we exchange - especially in public."
        "She'll smile sweetly, still sucking on her lollipop and pulling it out of her mouth in a suggestive manner."
        "And she always tastes of the flavour that she was just sucking on the moment before."
        "Sometimes, I think she enjoys being watched by people as she does this more than the actual kiss itself."
        "But that's something I try to keep from dwelling on too much."
        "And so I make an effort to guess the flavour that lingers on her lips each and every time."
        hide lexi kiss
        $ lexi.flags.kiss += 1
        $ lexi.love += 2
    return

label lexi_propose_male:
    "The prospect of actually asking a girl to marry me is a pretty scary one all on its own."
    show lexi normal
    "But when you throw in the complication that the girl in question just happens to be Lexi..."
    "Well, that takes it to an entirely new level, makes it almost terrifying."
    "Don't get me wrong, I'm not saying that Lexi's not like other girls."
    "She is and she isn't - if that makes sense."
    "Urgh..."
    "I'm not making any sense, am I?"
    "Okay, I'll try again..."
    "Lexi's had what you might call a chequered past, and we met under strained circumstances."
    "She was involved in more than a few shady schemes back then, mixing with shadier types too."
    "But together we've seen most of those things off and I feel like she's starting to move on."
    "Sure, she lives in a trailer park and comes from the wrong side of the tracks."
    "Yet none of that changes the fact she's fun and adventurous, exciting to be with."
    "Everything that she's been through means Lexi lives life to the full."
    "She seems to grab every chance, to live each day like it could be her last."
    "Shit..."
    "Now I've gone and made her sound like some kind of crazed adrenaline junkie!"
    "Look, I'm basically in love with Lexi."
    "There, I said it."
    "But I'm worried at how she'll react when I whip out the ring and pop the question."
    "I mean, will she see me as the handsome prince?"
    "The guy that's come along to carry her off on the back of his horse?"
    "Or is she beyond holding out for a happy ending?"
    "Is she going to see me as just another guy that wants to hold her down?"
    "Well, I guess there's only one way to find out."
    "And so I pull the ring out of my pocket and get down on one knee."
    mike.say "Ah, Lexi..."
    lexi.say "Huh..."
    "Lexi stares at me, more than a little puzzled to see me kneeling before her."
    show lexi bubblegum
    "She blows a large bubble, which pops with a crack made that much louder thanks to the silence."
    "And then she sucks it back into her mouth with another less than lady-like sound."
    show lexi normal
    lexi.say "What are you doing down there?"
    mike.say "Lexi..."
    mike.say "Will you marry me?"
    "I watch as realisation dawns upon her in the seconds that follow."
    show lexi surprised
    "Lexi's eyes go wide and her mouth hangs open in obvious surprise."
    "I have no idea what's going on inside of that head of hers."
    "And so all I can do is wait for her answer..."
    lexi.say "Y...you have to be joking...right?"
    lexi.say "You don't really want to marry me!"
    "Now it's my turn to become wide-eyed and lost for words."
    "At first, all I can do is shrug helplessly, feeling like an utter fool."
    mike.say "Y...yeah, Lexi..."
    mike.say "I...I...kinda do!"
    show lexi normal
    "Lexi falls silent for a second time."
    "But now she looks like she's teetering on the edge of something."
    "All I can guess is that it's finally dawning on her that I'm serious."
    if lexi.love < 195:
        "The moment breaks when she surprises me by bursting into peals of laughter."
        show lexi happy
        lexi.say "Oh, shit..."
        lexi.say "That's a good one, [hero.name]!"
        lexi.say "You really had me going for a second there!"
        "I laugh nervously, unsure of what else to do."
        mike.say "Ah, yeah, Lexi..."
        mike.say "I'm a funny guy!"
        show lexi normal
        lexi.say "I mean, how could WE ever get married?"
        lexi.say "What would we do?"
        lexi.say "Buy a house in the country?"
        lexi.say "Live happily ever after?"
        lexi.say "Ha...what a joke that is!"
        "I keep on laughing weakly as I shove the ring back into my pocket."
        "All the time it sounds hollow and empty."
        "Just like I feel on the inside right now."
        "But I force a smile onto my face."
        "And I hope that, with time, the feeling will pass."
        $ lexi.love -= 25
        $ lexi.sub -= 25
    else:
        "I can see the first hint of tears in the corner of Lexi's eyes as she speaks."
        show lexi sad
        lexi.say "Oh, [hero.name]..."
        lexi.say "You don't mean that, do you?"
        mike.say "I..."
        mike.say "Of course I do, Lexi!"
        mike.say "I love you and I want to marry you!"
        "Lexi shakes her head again and again."
        "It's almost like she can't understand what's happening to her."
        lexi.say "But...but..."
        lexi.say "I'm damaged goods, [hero.name]."
        lexi.say "Why would you want that?!?"
        "For a moment I'm lost for words."
        "And I end up shaking my head too."
        mike.say "So you have a past, Lexi - so what?"
        mike.say "All of that was just things you did, not who you are."
        mike.say "And...well...who you are is pretty great."
        mike.say "If you ask me, that is..."
        show lexi surprised
        "Lexi's looking at me in kind of a funny way."
        "Like she's weighing up all that I've said."
        lexi.say "Do...do you mean that?"
        mike.say "Of course I do, Lexi!"
        "The next thing I know, Lexi almost pounces on me."
        show lexi kiss
        $ lexi.flags.kiss += 1
        "She has me wrapped in her arms, pressing her lips against mine."
        "Lexi kisses me long and with an unashamed passion."
        hide lexi
        show lexi happy
        "And when she finally releases, I hear her whisper into my ear."
        lexi.say "Yeah, [hero.name]."
        lexi.say "Yeah, I'll marry you!"
        $ lexi.set_fiance()
    return

label lexi_ask_date_male:
    if (Harem.find_by_name("criminal") and Harem.find_by_name("criminal").is_active(lexi)) or (Harem.find_by_name("goodevil") and Harem.find_by_name("goodevil").is_active(lexi)) or (Harem.find_by_name("whore") and Harem.find_by_name("whore").is_active(lexi)):
        menu:
            "Ask Lexi on a date":
                call lexi_ask_date_alone_male from _call_lexi_ask_date_alone_male
            "Set up a date with Camila and Lexi" if Harem.find_by_name("criminal") and "criminal_harem_event_03" in DONE and "criminal_harem_event_04" not in DONE and not hero.calendar.find(label="criminal_harem_event_04"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_14
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "criminal", ["camila", "lexi"], "criminal_harem_event_04", "Date (Camila & Lexi)", "missed_criminal_harem_date"))
                else:
                    call criminal_harem_event_04 from _call_criminal_harem_event_04_1
                    $ DONE["criminal_harem_event_04"] = game.days_played
                    call sleep from _call_sleep_73
                    $ game.pass_time(2)
                return
            "Set up a date with Camila and Lexi" if Harem.find_by_name("criminal") and "criminal_harem_event_04" in DONE and not hero.calendar.find(label="criminal_harem_fuck_date"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_18
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "criminal", ["camila", "lexi"], "criminal_harem_fuck_date", "Date (Camila & Lexi)", "missed_criminal_harem_date"))
                else:
                    call criminal_harem_fuck_date from _call_criminal_harem_fuck_date_1
                    call sleep from _call_sleep_85
                    $ game.pass_time(2)
                return
            "Set up a date with Harmony and Lexi" if Harem.find_by_name("goodevil") and "goodevil_harem_event_01" not in DONE and not hero.calendar.find(label="goodevil_harem_event_01"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_19
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "goodevil", ["harmony", "lexi"], "goodevil_harem_event_01", "Date (Harmony & Lexi)", "missed_goodevil_harem_date"))
                else:
                    call goodevil_harem_event_01 from _call_goodevil_harem_event_01_1
                    $ DONE["goodevil_harem_event_01"] = game.days_played
                    call sleep from _call_sleep_86
                    $ game.pass_time(2)
                return
            "Set up a date with Harmony and Lexi" if Harem.find_by_name("goodevil") and "goodevil_harem_event_01" in DONE and not hero.calendar.find(label="goodevil_harem_fuck_date"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_20
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "goodevil", ["harmony", "lexi"], "goodevil_harem_fuck_date", "Date (Harmony & Lexi)", "missed_goodevil_harem_date"))
                else:
                    call goodevil_threesome_mikebedroom from _call_goodevil_threesome_mikebedroom_1
                    call sleep from _call_sleep_87
                    $ game.pass_time(2)
                return
            "Set up a date with Lexi and Reona" if game.season == 1 and Harem.find_by_name("whore") and "whore_harem_event_05" in DONE and not hero.calendar.find(label="whore_harem_beach_fuck_intro") and not ("whore_harem_event_06" in DONE and "whore_harem_event_07" in DONE and "whore_harem_event_08" not in DONE):
                call select_date_time (fixed_hour=14, fixed_season="summer") from _call_select_date_time_22
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "whore", ["lexi", "reona"], "whore_harem_beach_fuck_intro", "Date (Lexi & Reona)", "missed_whore_harem_date"))
                else:
                    call whore_harem_beach_fuck_intro from _call_whore_harem_beach_fuck_intro
                    $ game.pass_time(2)
                return
            "Set up a date with Lexi and Reona" if Harem.find_by_name("whore") and "whore_harem_event_06" in DONE and "whore_harem_event_07" in DONE and "whore_harem_event_08" not in DONE and not hero.calendar.find(label="whore_harem_event_08"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_23
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "whore", ["lexi", "reona"], "whore_harem_event_08", "Date (Lexi & Reona)", "missed_whore_harem_date"))
                else:
                    call whore_harem_event_08 from _call_whore_harem_event_08
                    $ DONE["whore_harem_event_08"] = game.days_played
                    call sleep from _call_sleep_119
                    $ game.pass_time(2)
                return
    else:
        call lexi_ask_date_alone_male from _call_lexi_ask_date_alone_male_1
    return _return

label lexi_ask_date_alone_male:
    mike.say "Lexi, would you like to go on a date with me?"
    if lexi.love < 50 or lexi.flags.nodate:
        lexi.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        lexi.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice


label lexi_masturbation:
    $ hero.cancel_activity()
    $ result = randint(1, 2)
    if result == 1:
        $ game.hour += 1
        show bg bedroom1 at dark
        with fade
        "I kind of feel like things happen around the house without any of us really agreeing to it, if that makes sense?"
        "Like, since Lexi got involved with the three of us, she's been hanging around here almost constantly."
        "And then just the other night I walk into the sitting-room and there she is, asleep and snoring on the sofa!"
        "I mean, we never sat down and had a discussion about whether or not it was a good idea for her to move in here."
        "But there she is, sprawled out in her underwear and making a sound like a backed up logging-mill!"
        "And she's at it again tonight, snoring so loud that I can hear it through the walls of my room."
        "Don't get me wrong, it's not that I don't like having Lexi around the place, because I do."
        "It's just that I'd also like to be able to get a good night's sleep too."
        "So when it becomes clear that she's not going to stop any time soon, I throw back the covers and swing my legs off the mattress."
        "Then I pad to the door, opening it as quietly as I can and slip out, headed in the direction of the sitting-room."
        "To be perfectly honest, I'm not sure what I'm going to say or do when I get there."
        "But just lying in bed and listening to Lexi snoring is sure to drive me insane."
        scene bg livingroom at dark
        show bg livingroom lexi_sleep at center, zoomAt(1, (640, 720))
        show bg black as foreground at center, zoomAt(1, (640, 720))
        with fade
        "By the time I make it to the door, Lexi seems to have started grunting and muttering to herself."
        "And I can't help being intrigued by the idea of just what she could be saying in her sleep."
        play sound door_slam
        "In my hurry to get closer, I accidentally kick the door with my foot."
        "The sound isn't all that loud, but it seems to be enough to make Lexi stir."


        show bg black as foreground at center, traveling(1, 1.1, (540, 720))
        "I freeze as she does so, staring through the crack in the door."


        show bg black as foreground at center, traveling(1, 0.7, (0, 720))
        "Any moment I'm sure that she's going to leap up and discover me watching her."
        "But my fears seem to be misplaced, as instead Lexi wriggles herself further down on the sofa."
        hide bg black as foreground with wipeleft
        "Though I can see from the look on her face that she seems a little frustrated."
        "I watch as Lexi tosses and turns on the sofa, as though unable to get comfortable again."
        "And then her frustration apparently reaches a critical point."
        show bg livingroom at center, traveling(1.2, 3, (640, 770))
        "As Lexi grabs hold of the sheet covering her and tosses it aside."
        "The moment that happens, I feel like I'm rooted to the spot."
        show bg livingroom at center, traveling(1.4, 3, (640, 820))
        "Because I'd naturally assumed she was sleeping in her underwear beneath the sheet."
        "But now I can see that wasn't the case at all - Lexi's totally naked!"
        show bg livingroom at center, traveling(1.6, 3, (640, 870))
        "Which makes the fact she's wriggling and shifting about on the sofa all the more compelling."
        "Getting as close to the door as I can, my eyes strain to take it all in."
        show bg livingroom at center, traveling(1.8, 3, (640, 920))
        "And it's then that I realise Lexi's not just trying to get comfortable again."
        "Her hands are starting to roam all over her body, and in a sensuous manner too."
        show bg livingroom at center, traveling(2, 3, (640, 970))
        "Is she..."
        "Is she going to start playing with herself?"
        "Well, I guess that's one way of trying to get back to sleep."
        "The effort itself is sure to use up her last reserves of energy."
        "And the chemicals an orgasm releases really would relax her a hell of a lot too."
        $ result = randint(1, 2)

        if result == 1:
            scene lexi mast at dark
            show lexi mast closed close up
            with fade
            "Part of me knows that I should have turned around and walked away by now."
            "But somehow the fact that I've seen Lexi's naked body leaves me unable to move."
            show lexi mast rtit finger with dissolve
            "And now as one of her hands slides between her thighs, there's no hope of me tearing myself away."
            "I watch with growing interest as Lexi's hand begins to explore the outer edge of her pussy."
            "At the same time her eyes are closed and her head is rolling around on the sofa cushions."
            show lexi mast ltit with dissolve
            "But that makes perfect sense, as who knows the lay of the land down there better than Lexi herself?"
            "She must be able to pleasure herself blindfolded or in the middle of a blackout!"
            "Adjusting my position, I soon find an angle from which I have a far better view."
            "Specifically one that lets me see what Lexi's fingers are actually doing."
            "And boy oh boy, do I get a good look at everything when I do!"
            "Now I can see the way that her fingers are moving and where they're touching the folds of her pussy."
            "Of course Lexi's already more than a little wet down there, everything glistening in the low light."
            "But as I watch, her lips begin to surrender to the attention more with each passing second."
            show lexi mast ltit open with dissolve
            "And little by little, the tips of her fingers start to sink into her pussy."
            "Though it's not like she's just trying to stuff them as deep into herself as she possibly can."
            "Instead I see that her fingers are moving the whole time, stroking and sliding around."
            "What Lexi's doing to herself puts me in mind of a musician plucking a stringed instrument."
            "And I do all that I can to note the moves that she makes with those deft, dexterous fingers."
            "At the same time her free hand seems to be roaming over the curves of her naked body."
            "Almost like it's lost and looking for a way to get in on the action too."
            "When it finally settles on one of Lexi's breasts, it stays there."
            "It's hard to tear my eyes away from her pussy, but I manage it for a moment."
            "And my reward is the sight of that hand massaging the breast like a baker kneading bread."
            "I watch as the nipple stiffens and her fingertips squeeze it until it's harder still."
            "It comes as no surprise to me when Lexi starts to moan and groan a few moments later."
            "Because she's not holding anything back, pushing herself as hard as she can towards a climax."
            "With one last gasp, she seems to plunge over the edge, limbs going limp as she does so."
            show lexi mast up rtit with dissolve
            "Lexi's laid out on the sofa right now, naked and totally exposed."
            "And it seems like her efforts have done the trick too."

        elif result == 2:
            scene lexi mast at dark
            show lexi mast closed close up
            with fade
            "Part of me knows that I should have turned around and walked away by now."
            "But somehow the fact that I've seen Lexi's naked body leaves me unable to move."
            "Now I can see that she's reaching down for something under the sheet too."
            "And as soon as I see that it's a pretty powerful-looking vibrator, there's no chance of me moving an inch."
            "The thing is one of those appliances that you see advertised as a massager."
            "But there's no mistaking what it really is, or what Lexi intends to do with it."
            "Because as the head begins to vibrate, making a low humming sound, it's headed straight down south!"
            "Lexi parts her thighs, giving herself plenty of room to work with."
            show lexi mast sextoy boob with dissolve
            "And then she aims the vibrator right between her legs."
            "At the same time her eyes are closed and her head is rolling around on the sofa cushions."
            "But that makes perfect sense, as who knows the lay of the land down there better than Lexi herself?"
            "She must be able to pleasure herself blindfolded or in the middle of a blackout!"
            show lexi mast up with dissolve
            "Adjusting my position, I soon find an angle from which I have a far better view."
            "Specifically one that lets me see what the vibrator's doing down there."
            "And boy oh boy, do I get a good look at everything when I do!"
            "Now I can see where the head is going and where it's touching the folds of her pussy."
            "Of course Lexi's already more than a little wet down there, everything glistening in the low light."
            "But as I watch, her lips begin to surrender to the attention more with each passing second."
            show lexi mast boob open with dissolve
            "And little by little, the tip of the vibrator starts to sink into her pussy."
            "Though it's not like she's just trying to stuff the whole thing as deep into herself as she possibly can."
            "Instead I see that she keeps it moving the whole time, stroking and sliding around."
            "What Lexi's doing to herself puts me in mind of an artisan handling a very precise tool."
            "And I do all that I can to note the moves that she makes with the vibrator."
            "At the same time her free hand seems to be roaming over the curves of her naked body."
            "Almost like it's lost and looking for a way to get in on the action too."
            "When it finally settles on one of Lexi's breasts, it stays there."
            "It's hard to tear my eyes away from her pussy, but I manage it for a moment."
            "And my reward is the sight of that hand massaging the breast like a baker kneading bread."
            "I watch as the nipple stiffens and her fingertips squeeze it until it's harder still."
            "It comes as no surprise to me when Lexi starts to moan and groan a few moments later."
            "Because she's not holding anything back, pushing herself as hard as she can towards a climax."
            "With one last gasp, she seems to plunge over the edge, limbs going limp as she does so."
            show lexi mast up rtit squirt with dissolve
            "Lexi's laid out on the sofa right now, naked and totally exposed."
            "And it seems like her efforts have done the trick too."
        "As I can already hear the sound of her starting to snore again."
        "Luckily for me though, they sound softer and less penetrating this time."
        "But even as I turn around and begin to sneak back to my room, I'm not sure I'll be able to sleep myself."
        "Not with a head that's totally filled with images of what Lexi apparently gets up to when she's alone at night!"
    elif result == 2:
        show bg bedroom1
        with fade
        "I'm about to turn in for the night, in fact I'm literally on my way to my bedroom."
        "But that's when I hear a noise coming from the direction of the living room."
        "Funny, I thought that everyone was either asleep or out for the night."
        "I strain to make out what the sound is, trying to keep myself calm as I do so."
        "Call me paranoid, but the last thing I want to do is bump into an intruder!"
        "But as soon as I take a couple of steps towards the source, I can guess what it is."
        "What I can hear has to be the muffled sound of the TV in the living room."
        "Somebody must have left it on and forgotten all about it."
        "Hell, it might even have been me, I am pretty tired right now!"
        "I really should switch it off before I go to bed."
        scene bg livingroom at dark, center, zoomAt(1, (640, 720))
        show bg livingroom lexi_sleep
        show bg black as foreground at center, zoomAt(1, (640, 720))
        with fade
        "But as I get closer to the living room door, I can make out something else."
        "It's almost like someone breathing, but not quite."
        "More like they're gasping or panting."
        play sound door_slam
        "I'm starting to feel anxious, I accidentally kick the door with my foot."
        "For a moment I think about backing off and calling the cops."
        "Maybe even picking up something I can swing as an improvised weapon!"
        "But then reality hits me, and I guess that I should take a look first."


        show bg black as foreground at center, traveling(1, 1.1, (540, 720))
        "Creeping ever closer, I peer around the edge of the door..."


        show bg black as foreground at center, traveling(1, 0.7, (0, 720))
        "I was right, there is somebody in there!"
        hide bg black as foreground with wipeleft
        "But I breathe sight of relief when I recognise Lexi sitting, cross-legged on the sofa."
        "I can only see her in profile, so it's a little hard to tell what she's actually doing."
        "And the TV screen is too far away for me to have a hope of seeing what she's watching too."
        show bg livingroom at dark, center, traveling(1.2, 3, (640, 770))
        "Her head seems to be leant against the back of the sofa, turning from side to side."
        "The fact that her eyes are closed makes me think that she might have fallen asleep."
        show bg livingroom at dark, center, traveling(1.4, 3, (640, 820))
        "But then I see that her hands are moving."
        "In fact they're moving around between her thighs..."
        show bg livingroom at dark, center, traveling(1.6, 3, (640, 870))
        "Oh wow...that would explain the sounds that she's making."
        "It looks like Lexi's playing with herself!"
        show bg livingroom at dark, center, traveling(1.8, 3, (640, 920))
        "On the sofa and in the middle of the living room!"
        "She's actually masturbating - and I'm watching it happen!"
        show bg livingroom at dark, center, traveling(2, 3, (640, 970))
        "Erm...wait a minute..."
        "Should I really be doing this?"
        "I mean, Lexi's a pretty out there kind of girl."
        "But she must think there's nobody around to see what she's doing, right?"
        menu:
            "Leave":
                "Of course I shouldn't be watching her doing this kind of thing!"
                "Why in the hell am I even having to ask myself that question?!?"
                "Lexi's already been exploited by a sleazy jerk."
                "And I don't want to be anything like that creep Danny!"
                "Shaking my head, I turn away from the door."


                show bg black as foreground with wiperight
                "Then, as quietly as possible, I start walking towards my room."
                scene bg bedroom1 at dark
                with fade
                "I just hope that Lexi didn't suspect I was there."
                "Though I don't think I'll be able to get the image of her out of my head."
                "That's going to be with me for a very long time to come!"
            "Watch Lexi masturbate" if not hero.has_skill("low_libido"):
                "Ah, why am I being such a prude?"
                "Lexi's not some fragile little flower that needs me to look out for her."
                "In fact, she'd probably laugh in my face if I told her I backed off from watching!"
                "Whatever the case, I'm already leaning in closer."
                scene lexi mast at dark
                show lexi mast finger rtit closed close
                with fade
                "Which means I can see more of what she's doing in there."
                "Lexi clearly has one hand inside of her panties."
                "It's working away hard and fast down there too."
                "And she's panting more with each passing second."
                "The hand that's not inside of her panties isn't idle either."
                show lexi mast ltit finger with dissolve
                "It seems to be roaming around Lexi's entire body."
                "I watch as it visits each of her erogenous zones in turn."
                "One moment it's stroking between her thighs."
                show lexi mast rtit boob with dissolve
                "The next it's squeezing Lexi's breasts through her top."
                "And then her lips are sucking on its fingers."
                "I can feel my cock getting harder and harder in my shorts."
                "It's almost aching at the thought of what Lexi's doing to herself."
                "That and the idea of being inside of her right now!"
                show lexi mast ltit finger open with dissolve
                "All of a sudden, Lexi begins to jerk in her seat."
                "She moans louder than ever, head rolling around as she does so."
                "This must be it - she's about to make herself cum!"
                "Lexi all but curls into a ball as her orgasm hits."
                "She whimpers and almost mews, hand still between her thighs."
                "Then she slowly begins to unwind herself, still breathing heavily."
                show lexi mast up rtit with dissolve
                "I see her pull her hand out from her panties."
                "And then she licks at her fingers, tasting her own juices."
                "That's it, that's all I can take."
                "I turn and make off for the safety of my bedroom."
                "Can't let Lexi catch me watching her now the show's over."
                "That and I need to keep the mental image of her fresh."
                "How else am I going to be able to relieve my own tension?"
            "Masturbate while watching her" if hero.has_skill("sneaky"):
                "Ah, why am I being such a prude?"
                "Lexi's not some fragile little flower that needs me to look out for her."
                "In fact, she'd probably laugh in my face if I told her I backed off from watching!"
                "Whatever the case, I'm already leaning in closer."
                scene lexi mast at dark
                show lexi mast finger rtit closed close
                with fade
                "Which means I can see more of what she's doing in there."
                "Lexi clearly has one hand inside of her panties."
                "It's working away hard and fast down there too."
                "And she's panting more with each passing second."
                "The hand that's not inside of her panties isn't idle either."
                show lexi mast ltit finger with dissolve
                "It seems to be roaming around Lexi's entire body."
                "I watch as it visits each of her erogenous zones in turn."
                "One moment it's stroking between her thighs."
                show lexi mast rtit boob with dissolve
                "The next it's squeezing Lexi's breasts through her top."
                "And then her lips are sucking on its fingers."
                "I can feel my cock getting harder and harder in my shorts."
                "It's almost aching at the thought of what Lexi's doing to herself."
                show lexi mast ltit finger open with dissolve
                "That and the idea of being inside of her right now!"
                "My hand is inside my shorts before I know what I'm doing."
                "Then I'm going as fast as I can, trying to catch up with Lexi."
                "She's like the pied fucking piper, but with jerking off!"
                "It's all I can do to keep from gasping loud enough to be heard."
                "At this rate, I'm going to shoot my load before she's done!"
                show lexi mast rtit finger high higher with dissolve
                "All of a sudden, Lexi begins to jerk in her seat."
                show lexi mast ltit finger ahegao with dissolve
                "She moans louder than ever, head rolling around as she does so."
                "This must be it - she's about to make herself cum!"
                "Lexi all but curls into a ball as her orgasm hits."
                "She whimpers and almost mews, hand still between her thighs."
                "Then she slowly begins to unwind herself, still breathing heavily."
                show lexi mast up rtit up open closed with dissolve
                "I see her pull her hand out from her panties."
                "And then she licks at her fingers, tasting her own juices."
                "That's when I realise that I can feel my own cum on my hand."
                "It's warm as it runs between my fingers and down my leg."
                "I stand there for a moment, trying to catch my breath."
                show bg livingroom lexi_sleep at dark, center, zoomAt(1, (640, 720)) with irisout
                pause 1


                show bg black as foreground with wiperight
                "And then I turn and make for the safety of my bedroom."
                scene bg bedroom1 at dark
                with fade
                "Once there, I close the door behind me and think about getting cleaned up."
                "But all that's on my mind is the image of Lexi playing with herself on the sofa."
            "Join in" if hero.has_skill("high_libido"):
                "Just then the answer strikes me, and it's so simple."
                "Why stand out here feeling guilty about watching Lexi?"
                "Much better to walk in there and get involved in what's going down."
                "So that's exactly what I do."
                show tv_bg as background at dark, center, zoomAt(1, (640, 720))
                show lexi a naked nophone at center, zoomAt(1.4, (640, 870))
                with fade
                "Lexi doesn't notice me until I actually sit down beside her on the sofa."
                "Then her eyes pop open and she lets out a yelp of genuine surprise."
                show lexi surprised
                lexi.say "Ahh!"
                show lexi angry
                lexi.say "Oh fuck..."
                lexi.say "You scared me half to death, you prick!"
                "I smile as I look Lexi in the eye."
                "But then our gazes are drawn downwards."
                show lexi sadsmile
                "She smiles too as she sees me looking at her hand inside of her panties."
                show lexi smile c
                "Without apology, Lexi starts to rub at her pussy again."
                "She's looking me straight in the eye as she does this too!"
                show lexi normal
                lexi.say "Let's see..."
                lexi.say "Where was I?"
                show lexi b flirt
                lexi.say "Oh yeah - I was rubbing my clit until I cum!"
                show lexi wink
                "She raises her eyebrows, as if challenging me."
                "It's like Lexi wants to see what I'll do next."
                show lexi normal grope
                "Not wanting to seem intimidated, I reach out with one hand."
                show lexi c with dissolve
                "As I slide it into Lexi's panties, I hear her breath catch."
                "This makes me go all the way for fear of her stopping me."
                "But the moment that I touch the soft folds of her pussy, Lexi nods eagerly."
                show lexi a flirt -grope finger
                "She pulls her own hand out, leaving me to feel how wet and warm she is down there."
                "Seriously, her pussy is almost hot to the touch!"
                show lexi smile
                lexi.say "Mmm..."
                show lexi bored
                lexi.say "Don't stop now!"
                show lexi wow
                lexi.say "It's always better when somebody else does it for me!"
                lexi.say "Come on, [hero.name], don't you wanna be the one to make me cum?"
                "In response, I push my fingers between Lexi's lips."
                "She moans as they sink slowly into her, nodding the whole time."
                "What follows isn't gentle or delicate, it's more like a free-for-all."
                "I push my fingers in and out of Lexi, going faster with each passing second."
                "My thumb rubs against her clit at the same time, making her squirm with pleasure."
                "Lexi yanks at her top, pulling it up while she pulls her bra down."
                "This makes her breasts spill out, bouncing and jiggling like crazy."
                lexi.say "Play with me, [hero.name]!"
                lexi.say "Fucking play with me!"
                show lexi flirt grope with dissolve
                "My free hand does all that it can to obey."
                "I squeeze and pinch handfuls of breasts whenever I can."
                show lexi finger -grope with dissolve
                "All of a sudden, Lexi begins to jerk in her seat."
                show lexi yawn
                "She moans louder than ever, head rolling around as she does so."
                "This must be it - she's about to make herself cum!"
                "Lexi all but curls into a ball as her orgasm hits."
                "Then she leans into me, thighs squeezing my hand."
                "Afterwards, Lexi giggles as she frees herself from me."
                show lexi -grope b normal
                lexi.say "Thanks for helping me out back there, [hero.name]."
                lexi.say "And let me know the next time you're flying solo, yeah?"
                show lexi wink
                lexi.say "That way I can return the favour!"
    scene bg black with fade
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
