init python:
    Event(**{
    "name": "cassidy_preg_talk",
    "label": "cassidy_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_start",
    "label": "cassidy_start",
    "priority": 500,
    "conditions": [
        IsDone("office_party"),
        HeroTarget(
            IsActivity("work_personal", "workhard_personal"),
            IsFlag("officepartyDelay", False),
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_start_investigation",
    "label": "cassidy_start_investigation",
    "priority": 1000,
    "conditions": [
        IsDone("cassidy_start", "aletta_event_05"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal")),
        PersonTarget(cassidy,
            Not(IsHidden()),
            IsFlag("startinvestigation")),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_setup_meeting",
    "label": "cassidy_setup_meeting",
    "priority": 1000,
    "conditions": [
        Not(IsSpecialDate("christmas")),
        IsDayOfWeek("123456"),
        IsHour(6, 14),
        PersonTarget(cassidy,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("setupmeeting"),
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_investigation_complete",
    "label": "cassidy_investigation_complete",
    "priority": 1000,
    "conditions": [
        IsHour(8, 20),
        PersonTarget(cassidy,
            Not(IsHidden()),
            IsFlag("finishinvestigation")
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_new_assistant",
    "label": "cassidy_new_assistant",
    "conditions": [
        IsDone("cassidy_investigation_complete"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("assistantdelay", False),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_bad_day",
    "label": "cassidy_bad_day",
    "conditions": [
        IsDone("cassidy_new_assistant"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_overhear_argument",
    "label": "cassidy_overhear_argument",
    "conditions": [
        IsDone("cassidy_bad_day"),
        HeroTarget(IsActivity("coffee_break")),
        PersonTarget(cassidy,
            Not(IsHidden()),
            Not(IsFlag("dwaynefightDelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_dwayne_fight_fallout",
    "label": "cassidy_dwayne_fight_fallout",
    "conditions": [
        IsDone("cassidy_overhear_argument"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            Not(IsFlag("dwaynefalloutDelay")),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_dwayne_visit",
    "label": "cassidy_dwayne_visit",
    "conditions": [
        IsDone("cassidy_dwayne_fight_fallout"),
        HeroTarget(HasRoomTag("mcoffice")),
        'cassidy.status == "pet"',
        PersonTarget(cassidy,
            Not(IsPresent()),
            Not(IsHidden()),
            Not(IsFlag("dwaynevisitDelay")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_aletta_fight",
    "label": "cassidy_aletta_fight",
    "conditions": [
        Or(
            And(
                'cassidy.status == "pet"',
                IsDone("cassidy_dwayne_visit")
                ),
            And(
                'cassidy.status != "pet"',
                IsDone("cassidy_dwayne_fight_fallout")
                ),
            ),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_needs_comfort",
    "label": "cassidy_needs_comfort",
    "conditions": [
        IsDone("cassidy_aletta_fight"),
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(cassidy,
            Not(IsFlag("needscomfortDelay"))
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_aletta_make_nice",
    "label": "cassidy_aletta_make_nice",
    "conditions": [
        IsDone("cassidy_needs_comfort"),
        HeroTarget(
            IsActivity("work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(cassidy,
            Not(IsHidden()),
            Not(IsFlag("makeniceDelay"))
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_arrange_party",
    "label": "cassidy_arrange_party",
    "conditions": [
        IsDone("cassidy_aletta_make_nice"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            Not(IsFlag("arrangepartyDelay"))
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_cherie_next_steps",
    "label": "cassidy_cherie_next_steps",
    "conditions": [
        IsDone("cherie_first_meeting_appointment"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            ),
        HeroTarget(
            IsFlag("cherie_missed", False)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_cherie_missed_party",
    "label": "cassidy_cherie_missed_party",
    "conditions": [
        IsDone("cherie_first_meeting_appointment_missed"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            ),
        HeroTarget(
            IsFlag("cherie_missed")
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_chat_about_cherie",
    "label": "cassidy_chat_about_cherie",
    "conditions": [
        IsDone("cherie_cold_call"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_chat_about_cherie2",
    "label": "cassidy_chat_about_cherie2",
    "conditions": [
        IsDone("cherie_first_call"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_cherie_no_help",
    "label": "cassidy_cherie_no_help",
    "conditions": [
        IsDone("cherie_second_meeting"),
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            ),
        HeroTarget(
            IsFlag("cherie_helping", False)
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_dwayne_denouement",
    "label": "cassidy_dwayne_denouement",
    "conditions": [
        HeroTarget(IsFlag("dwaynedead")),
        PersonTarget(cassidy,
            Not(IsHidden()),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_dom_boredom",
    "label": "cassidy_dom_boredom",
    "duration": 1,
    "conditions": [
        IsNotDone("cassidy_aletta_fight"),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            MinCounter("boredom", 45),
            )
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_dom_oral",
    "label": "cassidy_dom_oral",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            MaxStat("sub", -50),
            ),
        ],
    "chances": 25,
    "once_day": True,
    })

    Event(**{
    "name": "cassidy_humiliation_decay",
    "label": "cassidy_humiliation_decay",
    "conditions": [
        PersonTarget(cassidy,
            MinFlag("humiliation", 1)),
        ],
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_humiliation_growth",
    "label": "cassidy_humiliation_growth",
    "conditions": [
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("status", "pet", "sex slave"),
            Or(
                IsFlag("facecum"),
                IsFlag("wet"),
                IsFlag("topless"),
                IsFlag("bottomless"),
                ),
            ),
        ],
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_humiliation_check",
    "label": "cassidy_humiliation_check",
    "conditions": [
        PersonTarget(cassidy,
            IsFlag("status", "pet", "sex slave"),
            MinFlag("humiliation", 50),
            ),
        ],
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_humiliated_01",
    "label": "cassidy_humiliated_01",
    "conditions": [
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            MinFlag("humiliated", 1)
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_humiliated_02",
    "label": "cassidy_humiliated_02",
    "conditions": [
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            MinFlag("humiliated", 2)
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_outfit_picker",
    "label": "cassidy_outfit_picker",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })





















    Event(**{
    "name": "cassidy_sub_01",
    "label": "cassidy_sub_01",
    "duration": 0,
    "conditions": [
        IsDone("hanna_sub_event_02"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 90),
            IsFlag("status", "pet", "sex slave"),
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_sub_02a",
    "label": "cassidy_sub_02a",
    "duration": 1,
    "conditions": [
        IsDone("cassidy_sub_01"),
        IsHour(1, 4),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom", "kitchen"),
            Not(OnDate()),
            ),
        PersonTarget(cassidy,
            MinStat("sub", 90),
            IsFlag("status", "pet", "sex slave"),
            IsFlag("collared"),
            IsFlag("agree_walk_outside"),
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_spanking_start",
    "label": "cassidy_spanking_start",
    "priority": 200,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(cassidy,
            Not(IsHidden()),
            MinStat("love", 90),
            MinStat("sub", 25),
            ),
        ],
    "music": "music/roa_music/no_regrets.ogg",
    "do_once": True,
    })

label cassidy_outfit_picker:
    if randint(1, 3) == 1:
        $ cassidy.flags.gold = True
    else:
        $ cassidy.flags.gold = False
    return

label cassidy_humiliation_check:
    $ cassidy.set_flag("humiliated", 1, mod="+")
    return

label cassidy_humiliation_decay:

    $ cassidy.set_flag("humiliation", min(cassidy.flags.humiliation, 5 + cassidy_love // 10), mod="-")
    return

label cassidy_humiliation_growth:
    if cassidy.flags.topless and (cassidy.love < 80 or cassidy.sub < 60):
        $ cassidy.set_flag("humiliation", 1, mod="+")

    if cassidy.flags.bottomless and (cassidy.love < 100 or cassidy.sub < 70):
        $ cassidy.set_flag("humiliation", 1, mod="+")

    if cassidy.flags.wet and (cassidy.love < 120 or cassidy.sub < 80):
        $ cassidy.set_flag("humiliation", 1, mod="+")
        if randint(1, 3) == 1:

            $ cassidy.flags.wet = False

    if cassidy.flags.facecum and (cassidy.love < 160 or cassidy.sub < 90):
        $ cassidy.set_flag("humiliation", 1, mod="+")
        if randint(1, 3) == 1:

            $ cassidy.flags.facecum = False
    return

label cassidy_humiliated_01:
    show cassidy annoyed
    cassidy.say "I'm sorry, [hero.name], but I can't take this anymore."
    show cassidy sad
    mike.say "Take what?"
    show cassidy whining
    cassidy.say "Being your sex slave! You're humiliating. You make me hang around in here with cum on my face, or without my top, suck you whenever you want."
    cassidy.say "I can't take it anymore. I need out."
    show cassidy sad
    mike.say "Well, you know what will happen."
    show cassidy cry
    cassidy.say "Please, please don't do that!"
    menu:
        "Offer to back off":
            mike.say "Okay, maybe I'll back off a little, if you stay?"
            "Cassidy sniffles a little bit, while giving me a look filled with mistrust."
            show cassidy annoyed
            cassidy.say "I don't know."
            mike.say "Well, what do you need?"
            cassidy.say "I don't know. Just...be nicer to me, maybe?"
            mike.say "That's it? Be nicer?"
            cassidy.say "Maybe not quite so many blowjobs?"
            mike.say "There still has to be blowjobs."
            show cassidy whining
            cassidy.say "Fine, but come on."
            show cassidy sad
            mike.say "Okay, fewer blowjobs."
            show cassidy annoyed
            cassidy.say "And don't make me walk around with cum on my face. That gets nasty and gross really fast."
            show cassidy sad
            mike.say "You'd rather swallow?"
            show cassidy talkative
            cassidy.say "Oh God, yes I would."
            show cassidy normal
            mike.say "Fine."
            show cassidy talkative
            cassidy.say "You promise?"
            show cassidy normal
            mike.say "I promise."
            show cassidy talkative
            cassidy.say "Okay. I'm trusting you, [hero.name]."
            show cassidy normal
            mike.say "You still have to call me Master, though."
            show cassidy talkative
            cassidy.say "Fine, I'm trusting you, Master."
            $ cassidy.love += 1
            $ cassidy.sub += 1
            $ cassidy.flags.humiliation = 0
        "Refuse":
            mike.say "Nope, this is your punishment for being a bitch. Take it or leave it. I have no problem turning your father in."
            show cassidy angry
            cassidy.say "Fuck you, [hero.name]. Do whatever you want."
            show cassidy upset
            "Cassidy heads for the exit. I grab her arm as she goes by and she yanks it away from me."
            show cassidy angry
            cassidy.say "{b}Don't touch me, [hero.name]{/b}. Don't touch me {b}ever again{/b}!!"
            show cassidy upset
            "And with that she runs for the exit. I guess I have to figure out what to do about Dwayne, now."
            $ game.flags.firedwayne = True
            $ cassidy.set_gone_forever()
    return

label cassidy_humiliated_02:
    show cassidy whining
    cassidy.say "You {b}promised{/b}, [hero.name]! You promised me you'd back off, but, ugh! I'm done with this! Done!"
    show cassidy sad
    mike.say "Cassidy, wait!"
    show cassidy angry
    cassidy.say "Fuck you, [hero.name]. Do whatever you want."
    show cassidy upset
    "Cassidy heads for the exit. I grab her arm as she goes by and she yanks it away from me."
    show cassidy angry
    cassidy.say "{b}Don't touch me, [hero.name]{/b}. Don't touch me {b}ever again{/b}!!"
    show cassidy upset
    "And with that she runs for the exit. I guess I have to figure out what to do about Dwayne, now."
    $ game.flags.firedwayne = True
    $ cassidy.set_gone_forever()
    return

label cassidy_birthday_date_male:
    $ DONE["cassidy_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg mansionentrance with fade
    "It's always hard to muster up the courage to pick up a girl from her parent's house."
    "But imagine for a moment that the house in question is a massive mansion in the richest area of town."
    if not game.flags.dwaynedead:
        "And if that's not bad enough, the guy that lives in the mansion also just happens to be your boss!"
        "Oh yeah, I almost forgot - you're taking his little princess out to celebrate her birthday too!"
        "So as I walk up to the gates of Dwayne's mansion to pick up Cassidy, I'm more than a little nervous."
        "Like for starters, how am I even supposed get into this place?"
    "The fence around it must be twenty feet high!"
    "I look around for a clue, and it's then that I see an intercom by the gate."
    "So I press the button and wait for someone to answer."
    cassidy.say "Oh..."
    cassidy.say "Hi there, [hero.name]!"
    cassidy.say "I'll be out in the blink of an eye, okay?"
    if not game.flags.dwaynedead:
        menu:
            "Wait patiently":
                "I feel a pang of annoyance at being asked to wait outside."
                "But then I remember that it means I don't have to actually go in there."
                "And that also means that I won't be running into Dwayne either."
                "So maybe waiting here isn't so bad after all."
                mike.say "No problem, Cassidy."
                mike.say "You take your time."
                mike.say "I'll be right here waiting for you."
                "There's a short pause before Cassidy answers."
                "Just long enough to make me wonder what's causing the hold-up."
                "But then I hear her voice on the intercom again."
                cassidy.say "Okay, [hero.name]..."
                cassidy.say "I'll be right out - I promise!"
                "That leaves me to wait just like I said I would."
                show cassidy date with dissolve
                "A short while later, Cassidy appears and lets herself out."
                $ game.active_date.score += 15
                show cassidy talkative
                cassidy.say "Sorry about that, [hero.name]."
                cassidy.say "My dad was breathing down my neck the whole time."
                cassidy.say "I think he was looking for an excuse to chew you out!"
                show cassidy normal
                "I nod and smile, trying to act like it's nothing to me."
                "But the truth is I feel a surge of relief at the knowledge."
                "Hopefully the fact that Dwayne kept out of it is a good thing."
                "Maybe even proof that he approved of the way I treated his daughter."
            "Complain":
                "Huh?"
                "Is she for real?"
                "Am I not good enough to actually come in there?"
                mike.say "You're not even going to invite me in?"
                mike.say "You expect me to wait out here while you take your time?!?"
                "It takes a moment for Cassidy to respond to this."
                "And at first I think it's because she's shocked by my response."
                "But then I hear another voice through the intercom."
                "And I realise what the problem is."
                dwayne.say "Now you listen here, you punk..."
                dwayne.say "Nobody talks to my daughter like that!"
                cassidy.say "Please, Daddy..."
                cassidy.say "It's okay..."
                cassidy.say "He didn't mean it!"
                cassidy.say "Did you, [hero.name]?"
                mike.say "Ah...no..."
                mike.say "Oh course not."
                dwayne.say "Well he'd better not have meant it!"
                dwayne.say "Otherwise I'll make his ass disappear!"
                "With that the intercom goes dead."
                show cassidy date upset with dissolve
                "A short while later, Cassidy appears and lets herself out."
                $ game.active_date.score -= 10
                show cassidy angry
                cassidy.say "Thanks for that, [hero.name]."
                cassidy.say "Now I have my dad breathing down my neck!"
                cassidy.say "Let's just get the hell out of here."
                cassidy.say "Before he does something we'll all regret!"
                show cassidy upset
    "Now that I've actually been able to pick up my date, we can actually get going."
    "And Cassidy seems more than a little interested in where we're headed."
    scene bg street
    show cassidy date talkative
    with fade
    cassidy.say "I still don't understand why you won't tell me where we're going!"
    cassidy.say "Like, did you really plan something?"
    cassidy.say "Or are you just not telling me because you're winging it?"
    show cassidy normal
    mike.say "Of course I have a plan, Cassidy!"
    mike.say "And it's supposed to be a surprise."
    mike.say "That's why I'm not telling you anything."
    scene bg mall1 with fade
    pause 0.1
    show cassidy date surprised at left with easeinleft
    cassidy.say "But this is the mall!"
    cassidy.say "You can't go on a date to the mall!"
    show cassidy stuned
    mike.say "Ah, but that's where you're wrong, Cassidy!"
    mike.say "Of course you can go on a date to the mall."
    mike.say "You can make a date anywhere special!"
    show cassidy annoyed at center with ease
    "Cassidy frowns and shakes her head."
    "She looks less than convinced."
    cassidy.say "How is that even supposed to work?"
    if hero.charm >= 75:
        mike.say "You like all those movies from back in the day, right?"
        mike.say "The ones where the girl starts out thinking everything sucks?"
        mike.say "But then she realises that it's really a lot of fun?"
        "Cassidy thinks about it for a moment."
        show cassidy talkative
        cassidy.say "Like the one where the lady falls off the boat and loses her memory?"
        cassidy.say "But she falls for the poor guy because he's hot and makes her laugh?"
        show cassidy normal
        mike.say "Yeah, I guess..."
        mike.say "Kinda like you can have fun without splashing the cash."
        mike.say "And it's rebelling a little too."
        if not game.flags.dwaynedead:
            show cassidy talkative
            cassidy.say "Well..."
            cassidy.say "Daddy would be pretty mad if he caught me hanging out at the mall."
            cassidy.say "He's always saying that I need to act like a sophisticated young lady."
        $ game.active_date.score += 15
        show cassidy happy
        cassidy.say "So yeah...that does sound like fun!"
    else:
        mike.say "You've just got to use your imagination, Cassidy."
        mike.say "Step outside of the bubble of privilege you're used to."
        mike.say "You know, leave it behind and live in the real world for once?"
        "It takes a moment for what I'm saying to sink in."
        "But when it does, I don't get the reaction I was expecting."
        show cassidy upset
        "Instead, Cassidy's frown deepens."
        $ game.active_date.score -= 10
        show cassidy angry
        cassidy.say "Hey!"
        cassidy.say "Who are you calling privileged?!?"
        cassidy.say "I'll have you know my life can be pretty damn hard!"
        cassidy.say "Like, just the other day my maid was off sick."
        cassidy.say "And I had to make a sandwich - all on my own!"
        show cassidy upset
        mike.say "No, no, no..."
        mike.say "That's not what I meant at all!"
        show cassidy angry
        cassidy.say "Well that sure is what it sounded like!"
        cassidy.say "And I'm starting to think this is one crummy date too!"
        show cassidy upset
    mike.say "Just think of how much stuff there is to do here."
    mike.say "And it's all under one roof too."
    "For a moment, I think that Cassidy's going to argue with me."
    show cassidy a sadsmile
    "But then she puts a hand on her stomach."
    show fx drop
    show cassidy whining
    cassidy.say "Ooh..."
    cassidy.say "I didn't eat much today."
    hide fx
    cassidy.say "Because I thought you might be taking me to a fancy restaurant!"
    show cassidy sadsmile
    mike.say "Oops!"
    mike.say "Maybe we should get something to eat then?"
    mike.say "There's a place in the food-court that does pizza."
    mike.say "Let's go grab a slice."
    show cassidy normal
    cassidy.say "Hmm..."
    show cassidy whining
    if not game.flags.dwaynedead:
        cassidy.say "Daddy doesn't like me eating junk-food."
        cassidy.say "So I don't get to eat hot-dogs much."
    else:
        cassidy.say "Daddy didn't like me eating junk-food."
        cassidy.say "So I didn't get to eat hot-dogs much."
    show cassidy talkative
    cassidy.say "And I really love them!"
    show cassidy normal
    menu:
        "Insist on getting pizza":
            mike.say "Trust me, Cassidy..."
            mike.say "This is great pizza."
            mike.say "The best you'll ever have at a mall!"
            show cassidy surprised
            cassidy.say "But you can get pizza in a fancy restaurant!"
            cassidy.say "Aren't we supposed to be slumming it?"
            show cassidy stuned
            mike.say "Not when it comes to pizza!"
            show cassidy whining
            cassidy.say "Well..."
            cassidy.say "Okay, I guess..."
            scene bg coffeeshop at center, zoomAt(1.5, (960, 940)), blur(5)
            show cassidy date at center, zoomAt(1.5, (640, 1140))
            with fade
            "I don't waste any time in dragging Cassidy to the pizza place."
            "Where I proceed to buy us two slices of cheese and tomato pizza."
            "The slices are huge and pretty greasy, but they taste amazing."
            "Or at least they do to me."
            mike.say "What's the matter, Cassidy?"
            mike.say "Aren't you enjoying your pizza?"
            show cassidy surprised
            cassidy.say "What?"
            show cassidy whining
            cassidy.say "Oh yes..."
            $ game.active_date.score -= 10
            cassidy.say "It's very nice."
            show cassidy sadsmile
            "Cassidy smiles, but I can see that she's putting it on."
            "But I console myself with the taste of the pizza."
            "And that she'll eventually see I was right."
        "Agree to getting hot-dogs":
            mike.say "Well..."
            mike.say "I do love that pizza, Cassidy."
            mike.say "But it's your birthday - so hot-dogs it is!"
            show cassidy happy
            "Cassidy smiles and claps her hands in delight."
            $ game.active_date.score += 15
            cassidy.say "Yay!"
            cassidy.say "Let's go find some!"
            show cassidy normal
            "Cassidy practically drags me to the food-hall."
            "And we quickly find a vendor selling hot-dogs."
            "We order two huge ones, with onions and mustard."
            scene bg coffeeshop at center, zoomAt(1.5, (360, 940)), blur(5)
            show cassidy date at center, zoomAt(1.5, (640, 1140))
            with fade
            "Then we find somewhere to sit down and eat them."
            show cassidy happy
            cassidy.say "Mmm!"
            cassidy.say "I can't wait to get this much meat in my mouth!"
            show cassidy normal
            "I can't help sniggering at Cassidy as she says this."
            "And she looks up at me in surprise."
            show cassidy talkative
            cassidy.say "Hey!"
            cassidy.say "What's so funny?"
            show cassidy normal
            mike.say "Just you eating a huge sausage, Cassidy."
            mike.say "It's quite a memorable image!"
            show cassidy talkative a
            cassidy.say "Oh, I see!"
            cassidy.say "Yeah, if my Daddy could see me with this..."
            show cassidy wink b
            cassidy.say "With a big one in my mouth..."
            cassidy.say "I just know that he'd flip out!"
            show cassidy normal
            "I nod, trying to keep from spitting out my own hot-dog."
            "Afraid that I'll never be able to stop laughing."
    scene bg mall1
    show cassidy normal date
    with fade
    "Once we've eaten, Cassidy and I take a slow stroll around the mall."
    "As usual the place is packed with people as well as different stores."
    "So we divide our attention between window-shopping and people watching."
    if randint(0, 1) == 0:
        "That is until Cassidy spots something that interests her outside the arcade."
        show cassidy surprised
        cassidy.say "Ooh..."
        cassidy.say "What's that?"
        show cassidy stuned
        mike.say "It's one of those dancing games, Cassidy."
        mike.say "You copy the moves on the screen."
        mike.say "And you hit the panels under your feet."
        show cassidy talkative
        cassidy.say "It looks like fun, [hero.name]."
        cassidy.say "Let's have a game!"
        show cassidy normal
        "I shrug and nod my head."
        scene bg arcade with fade
        pause 0.1
        show cassidy date at right with easeinright
        "Then we walk over to the machine."
        show cassidy at center with ease
        "I pump some coins into the slot."
        "And then we're ready to go."
        "The screen comes to life in front of us."
        "Two pixelated dancers appearing and showing off the moves."
        "Then the music hits and Cassidy launches herself into the routine."
        show cassidy talkative
        cassidy.say "Come on, [hero.name]!"
        cassidy.say "Try to keep up."
        cassidy.say "This is pretty basic stuff!"
        show cassidy normal
        if hero.fitness >= 45:
            "I watch Cassidy's moves for a moment."
            "And it doesn't take long to see that she's pretty good."
            "I guess daddy paid for some pretty decent dancing classes!"
            "But let's see if she's got the stamina to match."
            "I turn my head and focus on the screen."
            "And pretty soon I'm dancing for all I'm worth."
            "Sure, I'm not as polished as Cassidy."
            "But I can still keep up the same pace as her."
            "Maybe even more so, as I seem to be pulling ahead."
            "When the game ends, Cassidy seems genuinely impressed."
            show cassidy surprised
            cassidy.say "Wow!"
            $ game.active_date.score += 15
            show cassidy talkative
            cassidy.say "You've really got some moves, [hero.name]."
            cassidy.say "I was struggling to keep up at the end!"
            show cassidy normal
            mike.say "Ah, it's no big deal, Cassidy."
            mike.say "I just like to keep myself in shape, that's all!"
        else:
            "I do the best I can to match the movements."
            "But my eyes are constantly drawn away from the screen."
            "And instead they're watching Cassidy as she dances."
            "She moves without ease and grace, just like a professional."
            "And then it hits me - of course she's had dancing lessons!"
            "Her parents are loaded and they have aspirations for their little princess."
            "But me, I'm just some jerk from the suburbs."
            "Apparently also one with no coordination or stamina either!"
            "All of which means that Cassidy out-dances me with little effort."
            show cassidy annoyed
            cassidy.say "Are you okay, [hero.name]?"
            show cassidy sadsmile
            mike.say "Urrgh..."
            mike.say "Yeah...fine..."
            mike.say "Just...need... to..."
            mike.say "Catch...my...breath!"
            $ game.active_date.score -= 10
    else:
        "That is until Cassidy spots something that interests her outside the arcade."
        show cassidy surprised
        cassidy.say "Ooh..."
        cassidy.say "What's that?"
        scene bg arcade with fade
        pause 0.1
        show cassidy date stuned at right with easeinright
        mike.say "It's one of those indoor crazy golf ranges."
        mike.say "You want to play a round, Cassidy?"
        show cassidy whining at center with ease
        cassidy.say "Oh..."
        cassidy.say "I don't know about that..."
        cassidy.say "I left my clubs at home!"
        show cassidy sadsmile
        "I can't help smiling."
        "Figures that Cassidy would have her own set of clubs."
        mike.say "Don't worry about it, Cassidy."
        mike.say "You can hire a club!"
        show cassidy surprised
        cassidy.say "But will it be an iron or a wedge?!?"
        show cassidy stuned
        mike.say "I don't think that's anything to worry about!"
        if hero.has_skill("golf"):
            "I should say that I'm not really intimidated by Cassidy's talk of her own clubs."
            "I've been playing golf long enough to be aware of my skill-level and my limits."
            "And this looks like a pretty basic crazy golf course as well."
            show cassidy surprised
            cassidy.say "Oh my..."
            cassidy.say "This isn't like playing at the club!"
            cassidy.say "Or using the range!"
            show cassidy normal
            "Nevertheless, she seems to pick it up quickly."
            "But I'm rather more interested in her reaction to my game."
            "From the start I can see Cassidy watching my form."
            "And I can tell that she's seriously impressed."
            "As we wrap up the game, she can't contain her curiosity any longer."
            show cassidy surprised
            cassidy.say "[hero.name]..."
            cassidy.say "You never told me that you played golf too!"
            show cassidy normal
            mike.say "Well, you never asked!"
            mike.say "And it's not like I'm a professional or anything."
            "My being humble doesn't seem to do anything to put Cassidy off."
            "And she persists in talking about my skills with a club."
            show cassidy talkative
            cassidy.say "Seriously though..."
            $ game.active_date.score += 15
            cassidy.say "You should come play at the golf club with me some time soon."
            show cassidy happy
            cassidy.say "It doesn't matter if you're not a member."
            cassidy.say "I can get you in as my personal guest."
            show cassidy normal
            mike.say "That sounds like a great idea, Cassidy."
            mike.say "Let's do that soon."
        else:
            "I'm pretty confident as we start the game."
            "After all, this is only crazy golf."
            "It's not like we're playing on a fancy private course."
            show cassidy surprised
            cassidy.say "Oh my..."
            cassidy.say "This isn't like playing at the club!"
            cassidy.say "Or using the range!"
            show cassidy normal
            "Nevertheless, she seems to pick it up quickly."
            "Which is more than can be said for me."
            "No matter how hard I try, I can't catch a break."
            "The ball always seems to go the opposite direction to the one I want."
            "Or else it comes up short, missing every time."
            show cassidy normal
            "Cassidy finishes the course long before me."
            "And so I have to accept limping home in second place."
            show cassidy talkative
            cassidy.say "Did you finally finish?"
            show cassidy normal
            mike.say "Yes, Cassidy..."
            mike.say "I finally finished."
            $ game.active_date.score -= 10
            show cassidy talkative
            cassidy.say "You really are bad at this, huh?"
            show cassidy normal
            mike.say "Yes, Cassidy..."
            mike.say "I really am bad at this."
            mike.say "Now can we please do something else?"
    scene bg mall1
    show cassidy date happy
    with fade
    "Cassidy seems to be really enjoying herself right now."
    "Like she's fully into the spirit of our date at the mall."
    show cassidy surprised at startle
    "As we walk past a particular store, she suddenly stops dead."
    cassidy.say "Oh..."
    cassidy.say "My..."
    cassidy.say "God..."
    show cassidy normal
    "I stop too, puzzled by what's going on."
    mike.say "What's up, Cassidy?"
    show cassidy talkative
    cassidy.say "I just had THE best idea."
    cassidy.say "Something really spontaneous and crazy."
    show cassidy happy
    cassidy.say "I'm going to get a TATTOO!"
    show cassidy normal
    "It's only now that I realise the store is the tattoo parlour."
    "And from the look on Cassidy's face, I can see that she's serious!"
    menu:
        "Encourage her to get inked":
            if not game.flags.dwaynedead:
                "Part of me is sure that her dad'll be mad if he finds out."
                "But then I remind myself that's only if he does find out."
                "And even then Dwayne can't actually blame me for it, can he?"
                "Maybe this is just the kick up the ass he needs."
                "Something to remind him once and for all that Cassidy's an adult."
                "That she's not his property."
            mike.say "Wow..."
            mike.say "That is a pretty crazy idea, Cassidy!"
            show cassidy talkative
            cassidy.say "But is that crazy good, or crazy bad?"
            show cassidy normal
            mike.say "Crazy good, obviously!"
            $ game.active_date.score += 15
            show cassidy happy
            "Cassidy smiles as she walks into the tattoo parlour."
            scene bg tattooshop with fade
            pause 0.1
            show cassidy date talkative at center with easeinright
            cassidy.say "Hi..."
            cassidy.say "I'd like that pink heart please."
            cassidy.say "And I want you to put it right here..."
            scene bg tattooshop at center, zoomAt(1.5, (640, 740))
            show cassidy a date at center, zoomAt(1.5, (640, 740))
            with vpunch
            "I gape in surprise as Cassidy points to her right buttock."
            "But it seems that she's not kidding around."
            "And before I know it, I'm watching the inking happen!"
        "Encourage her not to get inked":
            if not game.flags.dwaynedead:
                "Oh great, now she wants to get a tattoo!"
                "Imagine if her dad found out that it happened on our date too."
                "Forget firing me - Dwayne would fucking kill me!"
            mike.say "Erm..."
            mike.say "There's crazy, like living in the moment."
            mike.say "And then there's crazy, like literally insane!"
            show cassidy upset
            "Cassidy's face wrinkles up as she frowns at me."
            "And I can see that's not the response she was expecting."
            show cassidy whining
            cassidy.say "What do you mean?"
            cassidy.say "That I shouldn't do it?"
            cassidy.say "Like, you think it's a bad idea?"
            show cassidy sad
            mike.say "It's not like dying your hair, Cassidy!"
            mike.say "You can't just let it grow out if you decide you don't really like it."
            mike.say "You have to pay someone to burn it off you with a goddamn laser!"
            "Cassidy's frown becomes more pronounced."
            "And she makes a little huffing noise too."
            $ game.active_date.score -= 10
            cassidy.say "Hmpf..."
            show cassidy angry
            cassidy.say "That's so boring of you, [hero.name]."
            if not game.flags.dwaynedead:
                cassidy.say "You're starting to sound just like Daddy!"
    scene bg mall2
    show cassidy b date sad at center, zoomAt(1.5, (640, 1040))
    with fade
    "We stop for a moment, just to take stock and figure out where to go next."
    "But I can tell that there's something else on Cassidy's mind."
    "She's trying to hide it as best she can, but it's not working."
    "So I decide to call her out."
    mike.say "What's up, Cassidy?"
    show cassidy surprised at startle
    show fx question
    cassidy.say "What?"
    cassidy.say "What do you mean?"
    hide fx
    cassidy.say "Why would you ask me that?"
    cassidy.say "Why would you think there was anything up?"
    show cassidy stuned
    "Cassidy seems to realise how crazy she sounds."
    "And so she stops talking and lets out a sigh."
    show cassidy whining
    cassidy.say "Okay, you got me."
    cassidy.say "I was wondering if..."
    show cassidy sadsmile
    cassidy.say "Well...if you got me anything for my birthday?"
    if not hero.has_gifts:
        "Damn it!"
        "I totally forgot to get Cassidy a birthday present!"
        "It must have slipped my mind while I was worrying about pulling this off."
        mike.say "What do you mean, Cassidy?"
        mike.say "This date IS your gift!"
        mike.say "Because happy memories are priceless."
        mike.say "The kind of thing money can't buy!"
        show cassidy annoyed
        cassidy.say "Huh..."
        cassidy.say "But they're not like something you can wear, are they?"
        $ game.active_date.score -= 10
        show cassidy angry
        cassidy.say "They won't make me look pretty!"
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_7
        if _return != "done":
            if _return not in ["None", "exit"]:
                "Right now I'm glad that I remembered Cassidy's birthday present."
                "And this feels like the perfect moment to whip it out too."
                mike.say "Of course I did, Cassidy."
                mike.say "Here you go."
                mike.say "Happy birthday!"
                show cassidy happy
                cassidy.say "Oh thanks, [hero.name]!"
                cassidy.say "You didn't have to..."
                cassidy.say "But I'm glad you did!"
                show cassidy normal
                play sound [paper_ripping_1, paper_ripping_2]
                "Cassidy wastes no time in tearing off the wrapping paper."
                if _return:
                    show cassidy surprised
                    "And as soon as she sees what's inside, her face lights up."
                    cassidy.say "Oh my god..."
                    cassidy.say "Oh my god..."
                    show cassidy normal
                    mike.say "Erm..."
                    mike.say "Are you okay, Cassidy?"
                    show cassidy happy
                    $ game.active_date.score += 15
                    cassidy.say "Of course I am!"
                    cassidy.say "This is like...like the best gift ever!"
                    show cassidy normal
                    "I can't help smiling at Cassidy's reaction to the gift."
                    "Especially as she's literally the girl who has everything."
                    "So being able to find something she loves on my salary is no mean feat!"
                else:
                    show cassidy sad
                    "But her face falls as soon as she sees what's inside."
                    cassidy.say "Oh..."
                    $ game.active_date.score -= 10
                    cassidy.say "Oh great..."
                    mike.say "What's wrong?"
                    show cassidy whining
                    cassidy.say "Well...it's a bit lame, isn't it!"
                    show cassidy sadsmile
                    mike.say "I...I guess so..."
                    "It's a slap in the face to know that Cassidy doesn't appreciate my gift."
                    "But a total punch in the gut to have her actually come out and say as much!"
            else:
                "Damn it!"
                "I totally forgot to get Cassidy a birthday present!"
                "It must have slipped my mind while I was worrying about pulling this off."
                mike.say "What do you mean, Cassidy?"
                mike.say "This date IS your gift!"
                mike.say "Because happy memories are priceless."
                mike.say "The kind of thing money can't buy!"
                show cassidy annoyed
                cassidy.say "Huh..."
                cassidy.say "But they're not like something you can wear, are they?"
                $ game.active_date.score -= 10
                show cassidy angry
                cassidy.say "They won't make me look pretty!"
    scene bg mall1
    show cassidy date
    with fade
    "It feels like our date's coming to a natural end."
    "We're walking towards the exit of the mall without conscious effort."
    "And I'm fine with that, as I feel we've had a pretty good time."
    if not bree.is_gone_forever and bree.flags.schedule == "working":
        "But on the way, we happen to pass the Maid Cafe."
        "And by sheer coincidence, [bree.name] just happens to be outside."
        "She's in full uniform, collecting up empties from the tables out there."
        "I'm not sure whether to say hi or not, worried about Cassidy's reaction."
        "But then [bree.name] happens to look up and spots me, and she instantly waves with a smile."
        show cassidy surprised
        show bree maid at mostright4
        with easeinright
        bree.say "Hey, [hero.name]!"
        bree.say "Fancy seeing you here."
        show cassidy normal at left
        show bree at right
        with ease
        bree.say "Ooh...who's your friend?"
        bree.say "Are you here on a date or something?"
        "I glance over to see that Cassidy's staring at [bree.name]."
        "And it doesn't look like she's very impressed."
        menu:
            "Side with Cassidy":
                "I know that [bree.name]'s always friendly and eager to meet new people."
                "But maybe this isn't the right scenario to introduce her to Cassidy."
                "It's just too good of a chance for my date to revert to type and be a snob!"
                mike.say "Yeah, [bree.name]..."
                mike.say "This is Cassidy."
                mike.say "We're on a date, but we're also running a little late!"
                mike.say "So we can't stop to chat."
                "[bree.name] shrugs and smiles, waving away my apology."
                bree.say "Don't worry about it, [hero.name]."
                bree.say "I've got my hands full with work anyway."
                bree.say "You can tell me all about it at home later."
                hide bree with moveinright
                "[bree.name] goes back to clearing the tables."
                "Which leaves Cassidy and I to continue walking towards the exit."
                show cassidy annoyed at center with ease
                cassidy.say "Hmm..."
                cassidy.say "Where do you know that girl from?"
                mike.say "She's my housemate."
                mike.say "But you can meet her some other time."
                mike.say "Right now I don't want to be distracted from our date."
                $ game.active_date.score += 15
                show cassidy happy
                "Cassidy nods and smiles, like she approves of my priorities."
            "Side with [bree.name]":
                "But that's probably because she's used to being spoiled the whole time."
                "[bree.name] hasn't done anything wrong here, just said hello to a friend."
                "Cassidy could do with learning a lesson in manners and politeness!"
                mike.say "Yeah, [bree.name]..."
                mike.say "This is Cassidy."
                mike.say "Cassidy, this is [bree.name]."
                mike.say "She's one of my housemates."
                show bree happy
                "[bree.name] smiles sweetly."
                show cassidy annoyed
                "But Cassidy makes a sniffing sound."
                cassidy.say "So..."
                cassidy.say "You have to work with your hands?"
                show cassidy talkative
                cassidy.say "I guess that means you're pretty poor, yes?"
                show cassidy normal
                show bree angry
                "[bree.name]'s eyes flare with anger and she squares up to Cassidy."
                show bree at startle
                bree.say "HEY!"
                "I step between them before the argument can go any further."
                "And then I grab hold of Cassidy's hand, pulling her away from the cafe."
                mike.say "That was pretty rude, Cassidy!"
                show cassidy annoyed
                cassidy.say "I was just being honest."
                cassidy.say "If you don't like that..."
                $ game.active_date.score -= 10
                show cassidy angry
                cassidy.say "Then don't introduce me to your blue-collar, low-rent friends!"
    scene bg street
    show cassidy date
    with fade
    "At the exit to the mall, we stop."
    "There's an awkward silence as we wait for each other to speak."
    "And in the end, it falls to be to be the one to say something."
    mike.say "So..."
    mike.say "I had a great time today, Cassidy."
    mike.say "Are you going to be heading home?"
    mike.say "Or do you want to go somewhere else?"
    if game.active_date.score >= 80 and cassidy.sexperience >= 1:
        "Cassidy nods her head."
        show cassidy talkative
        cassidy.say "I had a great time."
        cassidy.say "And I'm not ready to go home yet!"
        show cassidy normal
        "The mere mention of Cassidy's home causes me to feel a pang of fear."
        if not game.flags.dwaynedead:
            "Mainly because it's also Dwayne's home."
            "And I can already imagine him waiting impatiently for her return."
        mike.say "Are you sure, Cassidy?"
        mike.say "You don't have, like...a curfew?"
        show cassidy happy at startle
        "Cassidy laughs and grabs hold of my hand."
        if not game.flags.dwaynedead:
            cassidy.say "Leave Daddy to me, [hero.name]."
            cassidy.say "I've been wrapping him around my little finger since I was a little girl."
            show cassidy normal
        "As she pulls me after her, I realise that she's doing the same thing to me as an adult too."
        "But it's not like I'm about to start complaining!"
        call cassidy_birthday_sex from _call_cassidy_birthday_sex
    else:
        "Cassidy shakes her head."
        show cassidy talkative
        cassidy.say "I had a good time too."
        show cassidy whining
        cassidy.say "But I need to get home soon."
        if not game.flags.dwaynedead:
            cassidy.say "If I don't, Daddy will make my life hell."
            show cassidy sadsmile
            "At the mere mention of Dwayne, I feel a pang of fear in my gut."
            mike.say "And for me too!"
        show cassidy sadsmile
        mike.say "Okay, Cassidy..."
        mike.say "Let's get you a taxi home!"
        hide cassidy with dissolve
        play sound car_door
        "As soon as Cassidy is safely in the taxi, I feel a flood of relief."
        "Sure, she called an end to the date herself."
        "But she also said that she had a good time."
        "And if she makes it back on time, Dwayne can't be mad at me."
        "So I'll have managed to keep them both happy."
    return

label cassidy_birthday_sex:
    show cassidy date normal at center, zoomAt(1.5, (640, 1040))
    "I'm thinking that Cassidy's going to come up with some exciting place for us to go."
    "That as soon as we're in the taxi, she'll name-drop an exclusive club I've never heard of."
    "But once we're in there, she just gives me a knowing smile and stays quiet."
    "It's like she's waiting for me to say something, but I don't know what that is."
    mike.say "Erm..."
    mike.say "My place...I guess?"
    "Much to my surprise, this seems to delight Cassidy."
    "She nods her head and clings onto my arm as we drive to my house."
    "And it's only as I open the door to let her inside that she reveals her true motive."
    scene bg livingroom
    show cassidy date stuned
    with fade
    mike.say "Well..."
    mike.say "Here we are, Cassidy."
    mike.say "Welcome to my pad!"
    "Cassidy walks into the hallway, turning and gazing around as she does so."
    show cassidy surprised
    cassidy.say "Wow!"
    cassidy.say "I've never been in a house this small before!"
    cassidy.say "I mean, I've been driven past them a hundred times."
    cassidy.say "But this is the first time I've ever been in one!"
    show cassidy stuned
    mike.say "Erm...okay, Cassidy."
    mike.say "I get that this is a bit of a culture shock for you."
    mike.say "My room's this way..."
    "I wave for Cassidy to follow me and set off for my room."
    show cassidy normal
    "She comes along with me, still apparently marvelling at my home."
    "Well, at least at how small it is."
    scene bg bedroom1
    show cassidy date
    with fade
    "I open the door and usher her inside, then I close it behind us."
    show cassidy surprised
    cassidy.say "Oh my..."
    cassidy.say "My maid has a bigger room than this!"
    cassidy.say "Where do you find the space for your servants?"
    show cassidy normal
    mike.say "Servants?"
    mike.say "I don't have any servants!"
    show cassidy stuned
    "Cassidy blinks at me, like she doesn't quite understand."
    "But then realisation dawns on her and she shakes her head in amazement."
    show cassidy surprised
    cassidy.say "Oh..."
    cassidy.say "My..."
    cassidy.say "God..."
    show cassidy happy
    cassidy.say "You are SO amazing, [hero.name]!"
    cassidy.say "I bet you can do absolutely anything, can't you?"
    show cassidy normal
    "Suddenly Cassidy incredulous amazement totally flips for me."
    "Before I was finding her patronising and more than a little annoying."
    "But now I realise that she's actually kind of in awe of how self-reliant I am."
    mike.say "Well..."
    mike.say "When you put it like that..."
    mike.say "I guess I do know how to handle myself!"
    "Cassidy nods as she holds my eye, and I can see how impressed she is."
    show cassidy topless with dissolve
    "Then I notice that she's also beginning to take off her clothes."
    "Slowly and almost unconsciously, as if she can't help herself."
    show cassidy talkative
    cassidy.say "You know..."
    cassidy.say "I bet you're just as handy in the bedroom, yeah?"
    cassidy.say "I bet you know all kinds of tricks and techniques."
    cassidy.say "You know, I'd really like to make love to a guy like that!"
    show cassidy normal
    mike.say "I...I think that could be arranged!"
    "I'm stripping off too, getting naked on impulse."
    "An impulse that gets stronger with the more of Cassidy that I can see."
    show cassidy naked -topless with dissolve
    "So by the time she's taken off all of her clothes, I'm almost out of control."
    show bg bedroom1 at center, traveling(2.0, 0.3, (640, 1340))
    show cassidy surprised at center, traveling(2.0, 0.3, (640, 1340))
    pause 0.3
    with vpunch
    "Cassidy lets out a squeal of surprise as I all but pounce on her."
    "Luckily the bed is right there to catch us as we fall."
    "There's time for us to bounce only once."
    hide cassidy
    show cassidy kiss naked
    with fade
    $ cassidy.flags.kiss += 1
    "Because after that, I have hold of Cassidy."
    "And I'm not about to let go before the act is done."
    "I'm all over Cassidy, my hands tracing lines across her body."
    "At the same time my lips are caressing her wherever they can reach."
    "The only choice that she has is to lie there and surrender to me."
    "But I can easily tell from the sounds she's making that this is what she wants."
    cassidy.say "Unh..."
    cassidy.say "Y...yeah..."
    cassidy.say "Please..."
    cassidy.say "Just...just like that..."
    "For a while I feel like I'm going to be the one in the driver's seat here."
    "That Cassidy is going to be happy to just lie back and let me take the lead."
    "But then I gasp in surprise as I feel her reach down and take hold of my cock!"
    mike.say "Ungh..."
    mike.say "C...Cassidy..."
    mike.say "Not so...hard!"
    "I have no idea if Cassidy hears me or not."
    "And even if she does, she shows no sign of listening to me."
    show cassidy missionary out with fade
    "Instead she presses the head hard against the lips of her pussy."
    "If Cassidy's not going to do as I tell her, then I have two choices."
    "I can put on the breaks and try to assert myself."
    "Or I can just forget about my ego and go with it."
    "Obviously I choose the latter of the two."
    "It's the path of least resistance."
    "And the only resistance that I want to deal with is that from Cassidy's lips."
    "So I put all of my efforts into giving her exactly what she wants."
    show cassidy missionary vaginal mouth_hurt eyes_ahegao
    "Pushing downwards, I make sure that all of my weight is behind my cock."
    "The result is slow and steady, progress coming a little at a time."
    "But all the same I can feel them opening to me."
    show cassidy missionary eyes_close mouth_normal
    "And as soon as they do, I begin to slide inside."
    "Only when that happens does Cassidy release her grip on me."
    "Because she can't exactly get what she wants if she doesn't, now can she?"
    "Freed from her grasp, I can finally begin to get back to what I had in mind."
    "Which was to give her an experience to remember."
    show cassidy missionary eyes_open mouth_pleasure
    "I'm sure to start out slow, keeping my movement shallow too."
    "With each thrust into her, I add a little speed and a little depth."
    "This means that each time, Cassidy gets a bit more of what she wants."
    "And yet she's still not being indulged as much as she would like."
    "I know that Cassidy's well used to getting what she wants in life."
    "So I'm willing to bet that she's the same way in the bedroom too."
    "I can feel myself being proven right as she wriggles beneath me."
    "And I can feel the frustration in her growing all with each passing moment."
    "The problem that Cassidy has is that I'm giving her a little more each time."
    "So her frustration can never grow to the point where it overtakes her pleasure."
    "Only when I've gone as deep into her as I can by subtle degrees do I change it up."
    "I linger there, filling Cassidy completely and letting her feel the sensation of it."
    show cassidy missionary vaginal mouth_hurt eyes_close at startle(0.05,-10)
    "And then I finally begin to move fast and hard."
    "The change catches her totally off-guard."
    show cassidy missionary at startle(0.05,-10)
    "Which means Cassidy is swept along before she knows it."
    "Before she was struggling and demanding more."
    "But now it seems like she's getting more than she can hope to handle."
    show cassidy missionary at startle(0.05,-10)
    "Now that the pace has changed, so does my attitude to indulging Cassidy."
    "Before I was trying to ration everything that I gave her."
    "Yet now I feel the urge to give her all that she can handle."
    show cassidy missionary at startle(0.05,-10)
    "My speed and intensity just seem to keep on building."
    "And I can feel that I'm pushing myself to see if she's able to keep up."
    show cassidy missionary at startle(0.05,-10)
    "I don't have to wait long for my answer either."
    "I feel Cassidy's arms and legs wrapping around me."
    show cassidy missionary at startle(0.05,-10)
    "And she starts to whimper as her muscles twitch too."
    "I don't need to be told that she's in the throes of an orgasm."
    with hpunch
    "And I don't need to ask permission to let myself go either."
    show cassidy missionary eyes_ahegao mouth_pleasure cum with vpunch
    "Shooting my load into Cassidy only makes the whole thing that much more intense."
    with vpunch
    "But it also uses up the last of my strength too."
    with vpunch
    "I only just manage to collapse to the side of her, rather than on top."
    show cassidy missionary eyes_ahegao mouth_pleasure out
    "And then I just lie there, panting and exhausted."
    "Cassidy does the same, all thought of getting her home forgotten."
    "It doesn't matter what Dwayne can threaten me with."
    "It'd be worth it for the sake of what we just did."
    $ cassidy.sexperience += 1
    return

label cassidy_start:
    "I am deep in the middle of the last thing I need to do on this task when my door bursts open and a stunning brunette walks right in, as though it was her office, not mine."
    play sound door_slam
    show cassidy casual normal with moveinleft
    "She slams the door closed behind her, and for a moment I am too stunned -- both by her boldness and by her beauty -- to say anything."
    show cassidy whining
    cassidy.say "You, what's-your-name, my valet is sick and I need a replacement."
    show cassidy normal
    mike.say "What do you -- I'm sorry, what?"
    show cassidy talkative
    cassidy.say "Well you're obviously not that bright. Should I use smaller words?"
    show cassidy normal
    "The conversation is definitely getting weirder, but I have to get it together and say something intelligible or this is going to go from weird to embarrassing."
    mike.say "I understand the words, whoever you--"
    "Oh shit. I was halfway through that sentence when I recognized her from the office party. That's Cassidy. The daughter of the CEO."
    mike.say "--I mean Cassidy."
    show cassidy happy
    cassidy.say "Oh good. The car is downstairs, we can run by my house and then go to the airport and then we can go to Switzerland. The jet's scheduled to leave in an hour, so there's no time to waste, and we've got a busy schedule there. Get moving!"
    show cassidy normal
    "Cassidy places her hands at her hips and taps her foot, waiting for me to go to the car, I guess."
    mike.say "Switzerland?!"
    "I really should be able to do better than that."
    show cassidy annoyed
    cassidy.say "Yes, Switzerland. Are you hard of hearing or just stupid?"
    show cassidy upset
    mike.say "Cassidy, I think there's a misunderstanding here."
    show cassidy surprised
    cassidy.say "Oh yes? What is it that you don't understand?"
    show cassidy stuned
    mike.say "No, it's you that doesn't understand. I'm not your valet. I don't work for you."
    show cassidy normal
    "Cassidy points one long finger at me, and then my desk."
    show cassidy talkative
    cassidy.say "You work at this company, right?"
    show cassidy normal
    mike.say "Yes, this is my desk and my office."
    show cassidy talkative
    cassidy.say "Right. And Dwayne runs this company, right?"
    show cassidy normal
    mike.say "Yes, he's the CEO."
    show cassidy talkative
    cassidy.say "Good, then you work for Dwayne which means you work for me. Now get moving!"
    show cassidy normal
    menu:
        "I have important work to do (Never meet Cassidy again)":
            mike.say "I'm afraid that's just not going to be possible right now."
            show cassidy upset
            "Cassidy's eyes go wide as she realises that I just said no to her demand."
            show cassidy angry
            cassidy.say "Did...did you just say what I think you said?"
            cassidy.say "Because if you did..."
            show cassidy upset
            mike.say "I think you'll find that I merely made a statement of fact."
            mike.say "At the moment I'm working on a file of significant importance."
            mike.say "So much so that to be diverted from it would put the company in serious jeopardy."
            show cassidy angry
            cassidy.say "I don't care about any of that..."
            show cassidy upset
            "Cassidy splutters with rage."
            "So much so that I think she's actually going to stamp her foot."
            "But I make no sign that I'm even aware of the fact she's steaming away in front of me."
            "Instead I calmly pick up the largest file that's within reach and slam it down on my desk."
            "Then I open it at a random page and run my finger down the first document that I see."
            mike.say "Do you see this here - right there?"
            "Cassidy glances down at the page, still frowning."
            show cassidy annoyed
            cassidy.say "What the hell are you talking about?"
            cassidy.say "That's just a dumb piece of paper with words on it!"
            "I let out a dry laugh and shake my head."
            mike.say "Oh dear..."
            mike.say "Oh dear, oh dear!"
            mike.say "This isn't a dumb piece of paper."
            mike.say "This is a vital document which described our relationship with a vital client."
            mike.say "I have to check this for accuracy, go through it with a fine-toothed comb."
            mike.say "Because if one word of it is wrong, it could spell disaster for this company."
            mike.say "We'd be setting litigant against litigator, plaintiff against pontiff!"
            mike.say "It could summon a bureaucratic entity of the highest order!"
            "Cassidy blinks as she listens to what I'm saying."
            show cassidy normal
            "And then she starts to shake her head like she doesn't understand any of it."
            "Which is understandable, as most of it's bullshit I just made up on the spot!"
            show cassidy angry
            cassidy.say "Urgh..."
            cassidy.say "I don't have time for this!"
            cassidy.say "Later, loser!"
            show cassidy upset
            "And just like that, she's gone."
            "I let out a sigh of relief and lean back in my chair."
            "But then I look down at the piles of work on my desk."
            "And I'm not sure if I just dodged a bullet, or talked myself out of a genuine adventure."
            "I guess my job's just not the kind that inspires thoughts of excitement and romance."
            $ cassidy.set_gone_forever()
        "I will drop you off at the airport":
            mike.say "Okay look if you really need, I'll drive you to the airport, but I'm not going to Switzerland."
            show cassidy angry
            cassidy.say "Did you just disobey me?"
            show cassidy upset
            "Cassidy does not look like the sort who is used to having someone tell her no. I need to find a way to get out of this without losing my job."
            mike.say "Look, let me find you a valet. I know a service I can call..."
            show cassidy happy
            cassidy.say "No, I want YOU. Look, if it's about the money I'll tell Daddy to give you a bonus. And if you're really good maybe I'LL give you a bonus."
            show cassidy normal
            mike.say "No, it's not about the money, it's--"
            "Wait, what did she mean by giving me a bonus herself?"
            show cassidy annoyed
            cassidy.say "Well, what's it about then?"
            "I take a deep breath and think as fast as I can."
            mike.say "I have a lot of work to do here. I can't leave, there's nobody else here who can do it, and it has to be done by tomorrow. Or the company could lose a lot of money, and Dwayne will be pissed."
            "I really hope my skill at lying is up to the task, because that is one of the biggest lines of bullshit I've ever fed a girl."
            show cassidy angry
            cassidy.say "Nobody says no to me...whatever your name is. Nobody. Call whatever service you've got, have someone meet me downstairs in 10 minutes. And he'd better be as hot as you are."
            cassidy.say "And I'm going to make you regret this."
            hide cassidy with moveoutleft
            play sound door_slam
            "With that, she turns on her heel and marches back out of my office, slamming the door behind her."
            "I quickly call a car service and it costs a lot of money, but I got someone to agree to it."
            "There's no way anyone will be down there in ten minutes, though. This...this could come back to haunt me."
            $ cassidy.flags.investigationDelay = TemporaryFlag(True, 7, hook=[hook_set_flag, {"girl": cassidy, "flag": "startinvestigation", "value": True}])
            $ cassidy.unhide()
    return

label cassidy_preg_talk:
    $ cassidy.flags.toldpreg = True
    show cassidy talkative
    cassidy.say "Hey, [hero.name], can we talk?"
    show cassidy normal
    mike.say "Sure, Cassidy. What's up?"
    show cassidy talkative
    cassidy.say "So you know how a few days ago you didn't use a condom? Well, you know how it works."
    show cassidy normal
    "Cassidy puts her hand on her belly."
    show cassidy talkative
    cassidy.say "There's a little [hero.name] growing inside of me."
    show cassidy sadsmile
    mike.say "Oh, oh. Oh wow. I mean..."
    if cassidy.love < 200:
        show cassidy whining
        cassidy.say "Look, [hero.name], I don't want it. I'm not ready to have a baby. I'm going to have an abortion."
        show cassidy sadsmile
        menu:
            "No! You can't!":
                if cassidy.status == 'pet':
                    show cassidy whining
                    cassidy.say "No, [hero.name], our arrangement doesn't cover this. I'm not giving you a choice."
                    show cassidy sad
                    "Do I really want her to keep the child? She seems pretty adamant, but...it's my baby! And she's my pet!"
                    menu:
                        "Insist":
                            mike.say "No, Cassidy. you can't abort the baby. I forbid it."
                            show cassidy cry
                            cassidy.say "[hero.name], you can do whatever you want, then. I quit."
                            if cassidy.flags.collared:
                                $ cassidy.collared = False
                                "She reaches toward her neck and unfastens the collar from her neck, tossing it roughly aside."
                            cassidy.say "We are done."
                            hide cassidy with moveoutleft
                            "And then she runs past me as quickly as she can. Gone. Just like that. Cassidy AND my baby."
                            $ cassidy.set_gone_forever()
                            $ cassidy.unpreg()
                            $ game.flags.firedwayne = True
                        "Let it go":
                            mike.say "Okay. I guess. It's your body, but...damn it."
                            show cassidy cry at center, zoomAt (1.25, (650, 850))
                            "Cassidy steps toward me and puts her hand on my face. She speaks through tears that slowly drip down her cheeks."
                            cassidy.say "Look, maybe...someday, okay? But not today. Not now."
                            $ cassidy.love += 10
                            $ cassidy.unpreg()
                            cassidy.say "And thank you for being reasonable. I'm sorry this happened. Next time, wrap it up, okay?"
                            mike.say "Yeah, I guess."
                else:
                    show cassidy angry
                    cassidy.say "Fuck off, [hero.name]. My body, my rules. I don't want kids, and if you don't like it, you can fuck right the hell off."
                    show cassidy upset
                    "Cassidy's vehemence takes me by surprise, though I guess it really shouldn't surprise me all that much."
                    mike.say "Fine, I guess. You're in charge. But just know that it makes me sad."
                    show cassidy talkative
                    $ cassidy.love += 2
                    $ cassidy.sub -= 2
                    cassidy.say "Fine, it makes you sad. Use a fucking rubber next time."
                    show cassidy sadsmile
                    if cassidy.status == 'mistress':
                        mike.say "Yes, Mistress."
                    else:
                        mike.say "Yeah, I guess."
                    $ cassidy.unpreg()
            "It's for the best":
                mike.say "I guess it's for the best. Our arrangement would be a little weird, with kids."
                if cassidy.love > 120:
                    show cassidy kiss
                    $ cassidy.flags.kiss += 1
                    "Cassidy launches herself at me and wraps herself around my neck. There's a long, slow kiss."
                    $ cassidy.love += 5
                    hide cassidy
                    show cassidy at center, zoomAt (1.5, (650, 1050))
                    cassidy.say "Maybe someday, [hero.name]. Okay?"
                    mike.say "Sure."
                else:
                    cassidy.say "Yeah, can you imagine what our kid would be like? Would probably be a troll."
                    mike.say "Hey, a sexy troll, at least."
                    if hero.fitness > 60:
                        cassidy.say "Okay, yes, two sexy parents, how could it not?"
                    else:
                        cassidy.say "Only if it takes after me. If it takes after you, it'd be the ugly troll."
                        mike.say "Harsh, Cassidy. Harsh!"
                $ cassidy.unpreg()
    else:
        show cassidy whining
        cassidy.say "Sweetie, I don't...I don't know if I'm ready for a baby."
        show cassidy sadsmile
        mike.say "But--"
        show cassidy whining
        cassidy.say "Let me finish!"
        show cassidy sadsmile
        mike.say "Okay."
        show cassidy whining
        cassidy.say "Look, I didn't ever see myself as a mom. It's just not something I ever wanted. But the thing is..."
        show cassidy talkative
        cassidy.say "I love you, [hero.name]. I think...I might. I might be willing to, you know."
        cassidy.say "Be a mom. With you. If you want?"
        show cassidy normal
        if cassidy.status == 'mistress':
            mike.say "You're giving me a choice?"
            show cassidy talkative
            cassidy.say "What we have is fun, but this...this would be forever. So yeah, I want your complete and unconditional buy-in."
        show cassidy sadsmile
        menu:
            "Yes":
                mike.say "Yes, my love. Yes. Yes!! Let's do this, let's have a baby. Let's be a family."
                show cassidy happy at center, zoomAt (1.5, (650, 1050))
                "Cassidy throws herself at me and envelops me in a hug. I can feel the wet from the tears streaming down her face as she presses against me."
                cassidy.say "You'll make a great dad, [hero.name]!"
                mike.say "I love you!"
            "No":
                mike.say "Cassidy, I don't think...I don't think this is a good idea."
                show cassidy cry
                cassidy.say "I know, it's not, but...no, you're right. I thought maybe if you wanted, but you're right."
                show cassidy at center, zoomAt (1.5, (650, 1050))
                "I step up and wrap my arms around Cassidy while she babbles. Her words go incoherent as her face presses against my shoulder, and we hold each other tight."
                mike.say "Maybe another time, when we're both more mature?"
                "She nods into my chest, sobbing, but in agreement."
                $ cassidy.unpreg()
    return

label investigation_points(points):
    $ game.flags.workinvestigation += points
    $ NOTIFICATIONS.append(["{image=gui/icons/icon_investigation.png} +" + str(points), 2])
    return

label cassidy_start_investigation:
    $ game.flags.suspended = True
    $ game.flags.underinvestigation = True
    $ cassidy.flags.investigationDelay = TemporaryFlag(True, 7, hook=[hook_set_flag, {"girl": cassidy, "flag": "finishinvestigation", "value": True}])
    $ cassidy.flags.meetingDelay = TemporaryFlag(True, 2, hook=[hook_set_flag, {"girl": cassidy, "flag": "setupmeeting", "value": True}])
    show aletta sad with moveinleft
    "Aletta comes into my office with a worried expression on her face. I know it's serious when she closes the door softly behind her."
    show aletta whining
    aletta.say "[hero.name], I've got some bad news for you."
    "I stand up from my chair. The look on her face and the tone of her voice has me especially worried now."
    show aletta sad
    mike.say "What's going on, Aletta?"
    if aletta.love >= 100:
        call investigation_points (20) from _call_investigation_points_3
        "Aletta hands me a folder."
        show aletta whining
        aletta.say "I'm not supposed to give you this, but, you're one of my best people..."
        show aletta sad
        "I open the folder and quickly flip through it. I'm quickly lost in a sea of numbers, row upon row of transactions."
        "But then things start to look familiar. These are accounts for my department's purchases and expenses."
        "Some of the numbers are circled, and at the bottom of the page I see the number 2,787,000{image=gui/icons/icon_money.png} written in red ink."
        mike.say "What the hell is this?"
        show aletta whining
        aletta.say "[hero.name], there's some money missing from this department's accounts. A lot of money missing. And your accounts have been flagged."
        show aletta sad
        mike.say "Missing? Wait, that's what this...holy shit. Are you telling me they think I stole almost three million dollars?"
        show aletta whining
        aletta.say "They don't know, [hero.name]. But until they find out, I have to put you on an administrative leave."
        show aletta sad
        "I nearly shout, my voice filled with a combination of surprise, anger, and a feeling of betrayal. How could Aletta think I'd do this?"
        mike.say "What?!"
        show aletta whining
        aletta.say "Calm down, [hero.name]!"
        show aletta sad
        mike.say "You don't seriously think I did this, Aletta?!"
        show aletta whining
        aletta.say "No, [hero.name], I do not. But someone thinks you might have."
        show aletta sad
        "I sink back into my chair, deflated."
        mike.say "What are my options here?"
        show aletta embarrassed
        aletta.say "If the investigation reveals that you stole the money, you could be fired. They would refer the matter to the district attorney."
        show aletta whining
        aletta.say "For numbers this big, you could go to jail, [hero.name]."
        show aletta sad
        mike.say "Jail? I didn't do anything! I certainly didn't steal three million dollars!"
        show aletta talkative
        aletta.say "I know, and I'll tell them that, but I don't think that will be enough. You're going to have to figure out what happened."
        show aletta normal
        "I sigh."
        show aletta whining
        aletta.say "And you don't have much time. If I had to guess, I'd say they'll finish the investigation in a week. If you're cleared, you'll get your job back."
        mike.say "And if not, I go to jail."
        mike.say "Well, this sucks."
        show aletta whining
        aletta.say "I don't know how this happened. But I promise I'll find out."
        aletta.say "In the mean time, I'll cover for your work here as much as I can."
        show aletta sad
        mike.say "Thanks, I guess. I suppose if I get fired, I won't care much about that, will I?"
        show aletta normal
        "Aletta chuckles ruefully."
        show aletta talkative
        aletta.say "No, I suppose not."
        hide aletta with moveoutleft
        "After Aletta leaves, I look through the folder she gave me. At least having the list of accounts and the numbers they're investigating will be a start."
    else:
        show aletta whining
        aletta.say "[hero.name], accounting has found some irregularities in your purchase and expense reports."
        show aletta sad
        mike.say "Irregularities? What does that mean?"
        show aletta whining
        aletta.say "It means the numbers don't add up, [hero.name]. A lot of numbers aren't adding up."
        show aletta sad
        mike.say "What kind of numbers?"
        show aletta whining
        aletta.say "Two point seven million numbers."
        show aletta sad
        "Whoa. That's a lot of numbers."
        mike.say "In my accounts? How is that even possible?"
        mike.say "Missing? Wait, that's what this...holy shit. Are you telling me they think I stole almost three million dollars?"
        show aletta whining
        aletta.say "They don't know, [hero.name]. But until they find out, I have to put you on an administrative leave."
        show aletta sad
        "I nearly shout, my voice filled with a combination of surprise, anger, and a feeling of betrayal. How could Aletta think I'd do this?"
        mike.say "What?!"
        show aletta whining
        aletta.say "Calm down, [hero.name]!"
        show aletta sad
        mike.say "You don't seriously think I did this, Aletta?!"
        show aletta whining
        aletta.say "I don't know, [hero.name], I really don't."
        show aletta sad
        mike.say "What are my options here?"
        show aletta annoyed
        aletta.say "If the investigation reveals that you stole the money, you could be fired. They would refer the matter to the district attorney."
        aletta.say "For numbers this big, you could go to jail, [hero.name]."
        show aletta sad
        mike.say "Jail? I didn't do anything! I certainly didn't steal three million dollars!"
        show aletta talkative
        aletta.say "I'd like to believe you didn't, [hero.name], but I don't know. You're going to have to figure out what happened."
        show aletta normal
        "I sigh."
        show aletta whining
        aletta.say "And you don't have much time. If I had to guess, I'd say they'll finish the investigation in a week. If you're cleared, you'll get your job back."
        mike.say "And if not, I go to jail."
        mike.say "Well, this sucks."
        show aletta whining
        aletta.say "I don't know how this happened. But I promise I'll find out."
        aletta.say "In the mean time, I'll cover for your work here as much as I can."
        mike.say "Thanks, I guess. I suppose if I get fired, I won't care much about that, will I?"
        show aletta sadsmile
        "Aletta chuckles ruefully."
        show aletta talkative
        aletta.say "No, I suppose not."
        aletta.say "Well, good luck with it. I'm rooting for you."
        hide aletta with moveoutleft
        "After Aletta leaves, I take a long look at my desk. I have to figure out a way to head this off before I get fired."
    return

label cassidy_setup_meeting:
    if "cassidy" not in hero.smartphone_contacts:
        $ hero.smartphone_contacts.append("cassidy")
    play sound cell_vibrate loop
    "My phone buzzes, and when I pull it out to look at it, the caller ID says that it's Cassidy."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Cassidy")
    if not result:
        $ hero.cancel_event()
        $ cassidy.love -= 5
        return
    "The daughter of the CEO is calling me. In the middle of this investigation."
    "And when we met in my office, she told me I was going to regret spurning her."
    mike.say "Hello?"
    cassidy.say "Hey, [hero.name]. What's happening?"
    "Her voice is cheerful and mischievous. There is suddenly no doubt in my mind that she is related to this investigation."
    mike.say "Uh, nothing, much."
    cassidy.say "Oh good, that means you've got time to meet me."
    mike.say "I can't, I have...work to do."
    cassidy.say "Oh, Sweetie, we both know that's not true."
    "Her voice absolutely drips with delight. I play innocent."
    mike.say "What do you mean?"
    cassidy.say "Sweetie, you really have to stop pretending."
    "And then her voice drops, and turns...husky. It's somehow evil and sexy at the same time."
    cassidy.say "Do you want to keep your job?"
    mike.say "Uh, yes, yes I do."
    cassidy.say "Good. If you want to keep your job, then I might be able to help you. If, of course, you're willing to help me out."
    mike.say "Uh, what kind of help do you need?"
    cassidy.say "From what I hear about you, it's the kind of help you're very, very good at. Let's talk about this...in person."
    mike.say "Okay. Where at?"
    cassidy.say "Let's say...your office. At eleven. Tonight."
    mike.say "Midnight? Can you make this sound any sketchier?"
    cassidy.say "Oh, don't worry Sweetie. You won't have to do anything illegal. Well, much. And you'll enjoy it, too. I know I will."
    mike.say "Does it involve Switzerland?"
    cassidy.say "It might! Well, we'll see when we get that far. Now, are you going to meet me or do you kiss your job good-bye?"
    "For emphasis, Cassidy makes an exaggerated kissing sound into the phone."
    "I really have to think about this. If she's got a hand in this investigation, the truth may not matter. I almost certainly will lose my job."
    "But if I do what she wants, I could end up in worse trouble. Is it worth it?"
    menu:
        "No":
            mike.say "No, I think I'll pass on your help."
            "She doesn't answer immediately, and when she does she sounds disappointed."
            cassidy.say "Are you sure? I promise I'll make it all worth your while, Sweetie. I saw you staring at my ass the other day. I know what you want."
            mike.say "Wait, are you offering--"
            cassidy.say "Meet me in your office at eleven tonight and find out. Otherwise, I hope you can find those millions of dollars."
        "Yes":
            mike.say "Fine, Cassidy. I'll meet you tonight."
            cassidy.say "Good. Oh I can't wait for this, it's going to be so much fun!"
            cassidy.say "Remember, Sweetie. Tonight. Eleven. Your office."
    cassidy.say "Come alone. And wear something...sexy."
    "And with that she hangs up."
    "This situation just gets worse and worse. But maybe there's an opportunity here. If she's up to something, maybe she'll give some some evidence I can use."
    "I just need to find a way to get that evidence, before the meeting."
    $ renpy.dynamic("appointment")
    $ appointment = LabelAppointment(23, "cassidy", "Meeting Cassidy", "cassidy_hold_meeting", "cassidy_hold_meeting_missed")
    $ hero.calendar.add(game.days_played, appointment)
    return

label cassidy_hold_meeting(appointment=None):
    $ DONE["cassidy_hold_meeting"] = game.days_played
    $ game.room = "personal"
    scene bg personal
    show cassidy casual normal
    "When I open the door, she's already there, looking like the proud cat that caught the proverbial mouse. In this case, me."
    if game.flags.cassidycameraplaced:
        "Knowing that this is being recorded, I try to keep my expression neutral. I throw in a touch of fear, but that's not hard. I really am afraid."
        $ game.flags.cassidyrecorded = True
    show cassidy talkative
    cassidy.say "Oh, you came, Sweetie! I was worried you weren't going to take my offer seriously."
    show cassidy normal
    "Once again, her voice turns sultry."
    show cassidy talkative
    cassidy.say "And it would be so unfortunate if you decided not to take me...seriously."
    show cassidy normal
    "Was that an innuendo?"
    mike.say "Yes, Cassidy. I'm taking you seriously. What do you want?"
    show cassidy talkative
    cassidy.say "Before we get to that, don't you want to know what I can...do to you? Or for you?"
    show cassidy normal
    mike.say "Uh, let's start with...what can you do for me?"
    "Cassidy rests her shapely ass against the edge of my desk and relaxes."
    show cassidy casual happy
    cassidy.say "Well, my dear. My daddy owns this company. And I can make this whooooole investigation go away."
    show cassidy normal
    mike.say "Just like that?"
    "She snaps her fingers."
    "Just so."
    mike.say "Okay, ah. And what's the catch?"
    show cassidy talkative
    cassidy.say "The catch, of course, is that we change your job description around just a leeetle bit. In addition to your normal work, you'll become my personal valet."
    show cassidy normal
    "Sigh. She's still on that valet thing."
    show cassidy talkative
    cassidy.say "...and my personal sex toy."
    show cassidy normal
    mike.say "Say what now?"
    show cassidy talkative
    cassidy.say "You know. My toy. My cabana boy. My personal massager. You'll make that big dick of yours available to me, when I want, how I want, where I want."
    show cassidy normal
    mike.say "I don't think--"
    show cassidy talkative
    cassidy.say "No, thinking is definitely not part of your job, Sweetie."
    show cassidy normal
    mike.say "No I mean that doesn't seem like--"
    show cassidy angry
    cassidy.say "Shut up. It's this or be fired and maybe go to jail."
    show cassidy upset
    mike.say "Uh."
    if game.flags.cassidycameraplaced:
        "Crap. This isn't going to be enough to nail her. I need to get her to talk more or this is not going to work."
        "Also did I just say nail her? Because despite being terrified, this is also kind of turning me on."
        call cassidy_meeting_loop from _call_cassidy_meeting_loop
        return
    show cassidy talkative
    cassidy.say "Now you've got two choices, Sweetie."
    cassidy.say "One, don't believe me, walk out of here, and prepare your ass for jail."
    cassidy.say "Or two, get down on your knees, kiss my feet, call my Mistress, and beg me to make this all go away for you."
    show cassidy normal
    menu:
        "Refuse":
            "There is no way I'm going to get on my knees for this bitch, I don't care what happens."
            "So without another word, I turn and walk out."
            hide cassidy
            "As I walk out, I can just faintly hear her call out after me."
            cassidy.say "Enjoy jail, bitch! I hope you like getting fucked in the ass, because you're going to get a lot of it!"
            "Ugh. That's not a pleasant thought."
        "Accept":
            $ cassidy.flags.acceptedoffer = True
            "I hesitate, but after a moment I nod and agree to her demands."
            call cassidy_first_dom from _call_cassidy_first_dom
    return

label cassidy_hold_meeting_missed:
    $ DONE["cassidy_hold_meeting_missed"] = game.days_played
    "I didn't go to Cassidy's meeting. I hope that doesn't cause me trouble later."
    return

label cassidy_meeting_loop(done_items=[]):
    menu:
        "Why should I believe you?" if "why" not in done_items:
            mike.say "Look, why should I believe you?"
            show cassidy talkative
            cassidy.say "I don't see that you have a choice. But for what it's worth, I'm a girl of my word, as long as you're a boy who will do as he is told."
            show cassidy normal
            $ done_items.append("why")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items) from _call_cassidy_meeting_loop_1
                return
        "What do you know about the investigation?" if "what" not in done_items:
            show cassidy talkative
            cassidy.say "I know that you're in a whole lot of trouble."
            show cassidy normal
            mike.say "Oh come on, you know more than that."
            show cassidy talkative
            cassidy.say "I do."
            show cassidy normal
            mike.say "Well, if you want this, tell me what you know. Because right now, I don't believe you can stop this, and I'll just get fucked for nothing."
            show cassidy talkative
            cassidy.say "Fine. You want to know? I set this all up."
            show cassidy normal
            mike.say "Why?"
            show cassidy happy
            cassidy.say "Because you need to be on your knees."
            show cassidy normal
            mike.say "What the hell for?"
            show cassidy talkative
            cassidy.say "Nobody says no to me. Nobody. Especially not someone like you."
            show cassidy normal
            mike.say "Damn, you're one fucked up bitch."
            show cassidy talkative
            cassidy.say "I'm going to put that one on your tab. You'll pay for it. Later."
            show cassidy normal
            $ done_items.append("what")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items) from _call_cassidy_meeting_loop_2
                return
        "Does your daddy know?" if "what" in done_items and "daddyknows" not in done_items:
            mike.say "Does your Daddy know what your hobbies are? Ski trips to Switzerland and coercing young men into doing sexual favors for you?"
            show cassidy talkative
            cassidy.say "Oh, well. Maybe not the sexual favors part. I don't think he wants to know about that."
            cassidy.say "But other than that, Daddy gives me whatever I want."
            show cassidy happy
            cassidy.say "And I want you!"
            show cassidy normal
            $ done_items.append("daddyknows")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items) from _call_cassidy_meeting_loop_3
                return
        "You didn't just ask daddy" if "what" in done_items and "daddy" not in done_items:
            mike.say "You didn't just ask your daddy to do all this for you. Are you trying to tell me you set all this up yourself?"
            show cassidy talkative
            cassidy.say "Oh, well. I have had a bit little help. Here and there. A girl like does have to have a few minions, after all."
            show cassidy normal
            "She leans toward me and uses the sultry, sexy voice again."
            cassidy.say "Like you!"
            $ done_items.append("daddy")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items) from _call_cassidy_meeting_loop_4
                return
        "Who are you working with?" if "what" in done_items and "who" not in done_items:
            if "daddy" not in done_items:
                show cassidy talkative
                cassidy.say "What makes you think I'm working with anyone?"
                show cassidy normal
                mike.say "Because I don't think you know enough about the business to pull this off yourself. Sure you're the CEO's daughter."
                mike.say "You have a lot of money and power, but I don't see you here every day, really in the system. No you have to have someone on the inside."
            show cassidy talkative
            cassidy.say "Why should I tell you?"
            show cassidy normal
            mike.say "Because you'd rather get what you want than have me walk out of here and get fired, and it doesn't cost you anything."
            "As soon as the words are out of my mouth, I can't imagine there's any way she'll buy that. But..."
            show cassidy talkative
            cassidy.say "Fine, Jeff, the accountant doing the investigation. He's married, you know. And he doesn't want his wife to know about...us."
            show cassidy normal
            mike.say "So, you're banging an accountant? Is that as boring as it sounds?"
            "She shrugs."
            show cassidy talkative
            cassidy.say "Well, he certainly isn't you, that's for sure. I mean to look at."
            show cassidy happy
            cassidy.say "He's one hell of a lot smarter than you, though."
            show cassidy normal
            "Oh, that bitch. She has no idea."
            mike.say "I see, so I'm just the dumb cute guy, huh?"
            show cassidy happy
            cassidy.say "Pretty much!"
            show cassidy normal
            $ game.flags.toldjeff = True
            call investigation_points (10) from _call_investigation_points_4
            $ done_items.append("who")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items) from _call_cassidy_meeting_loop_5
                return
        "Where is the money?" if "what" in done_items and "where" not in done_items:
            mike.say "So where's the money? I didn't steal it. Did you steal 3 million dollars and set me up just to put me in my place?"
            show cassidy talkative
            cassidy.say "No! I didn't steal anything!"
            show cassidy normal
            mike.say "Where is it, then?"
            show cassidy talkative
            cassidy.say "How should I know?"
            show cassidy normal
            mike.say "What? You set all this up, that money is missing. Are you telling me you set me up and you don't even know who really took the money?"
            mike.say "It seems like that's a great recipe to get fucked."
            show cassidy talkative
            cassidy.say "It doesn't matter, okay? That money was already gone, and they promised me it would be handled, and that I don't want to know about it."
            show cassidy normal
            mike.say "They, huh? So you're not the mastermind here. You're just the patsy!"
            show cassidy talkative
            cassidy.say "No, Sweetie. You're the patsy here. Unless you do exactly what I tell you."
            show cassidy normal
            call investigation_points (10) from _call_investigation_points_5
            $ done_items.append("where")
            if len(done_items) < 3:
                call cassidy_meeting_loop (done_items) from _call_cassidy_meeting_loop_6
                return
    show cassidy angry
    cassidy.say "Enough of your questions! I'm the one in charge here!"
    show cassidy talkative
    cassidy.say "Now you've got two choices, Sweetie."
    cassidy.say "One, don't believe me, walk out of here, and prepare your ass for jail."
    cassidy.say "Or two, get down on your knees, kiss my feet, call me Mistress, and beg me to make this all go away for you."
    show cassidy normal
    "I should have enough in the recording to deal with her, but I don't really know for sure."
    "If I refuse, they might push the 'investigation' through. Maybe I have enough, maybe I don't."
    "If I accept, I don't know what she'll ask me to do. Can I handle begging a little?"
    menu:
        "Refuse":
            "There is no way I'm going to get on my knees for this bitch, I don't care what happens."
            "So without another word, I turn and walk out."
            hide cassidy
            "As I walk out, I can just faintly hear her call out after me."
            cassidy.say "Enjoy jail, bitch! I hope you like getting fucked in the ass, because you're going to get a lot of it!"
            "Ugh. That's not a pleasant thought."
        "Accept":
            $ cassidy.flags.acceptedoffer = True
            "I hesitate, but after a moment I nod and agree to her demands."
            call cassidy_first_dom from _call_cassidy_first_dom_1
    return

label cassidy_first_dom:
    cassidy.say "Good, good. Now, for a down payment on our little arrangement, I want you to strip out of your clothes."
    mike.say "What?"
    cassidy.say "None of that! No hesitating, no acting incredulous. Get out of your fucking clothes right now, bitch."
    "I grit my teeth but accede to her demand and start taking my clothes off."
    "First my shirt."
    "Then my pants."
    show cassidy happy
    "Finally my underwear."
    show cassidy normal
    "Cassidy looks me up and down, approvingly."
    show cassidy talkative
    cassidy.say "Oh, I do like a man who's well hung. Now, get down on your knees."
    show cassidy normal
    "I stand there for a moment."
    show cassidy angry
    cassidy.say "Now, bitch! And while you're down there, call me Mistress."
    show cassidy normal
    "Fuck, this is actually starting to turn me on."
    "I get down on my knees, as asked. But I take my time about it."
    show cassidy talkative
    cassidy.say "And? What else did I tell you to do?"
    show cassidy normal
    mike.say "Call you Mistress."
    show cassidy talkative
    cassidy.say "Well?"
    show cassidy normal
    mike.say "Yes, Mistress."
    show cassidy happy
    cassidy.say "Good. Now I want you to jerk yourself off for me."
    show cassidy normal
    mike.say "Wh--"
    show cassidy talkative
    cassidy.say "If you persist in that behavior, I'm going to have to really punish you. Do as you're told, bitch."
    show cassidy normal
    "I sigh, and put my hand on my cock. It's only half erect, so it comes up fairly slowly."
    mike.say "It would help, if...it would help, Mistress, if you would maybe, give me a hand?"
    show cassidy angry
    cassidy.say "Fuck that, I'm in charge here, you don't get to ask me for a handy."
    show cassidy upset
    mike.say "I meant, maybe...give me something to look at? To help get its attention?"
    show cassidy talkative
    cassidy.say "I see. Well. Are you being a good boy?"
    show cassidy normal
    mike.say "Yes, Mistress, I'm being a good boy!"
    show cassidy casual topless with dissolve
    "Cassidy removes her top and casually casts it aside. Will this do?"
    "My cock immediately stiffens in my hand."
    mike.say "Yes, Mistress."
    show cassidy talkative
    cassidy.say "Sweetie, do better than that."
    show cassidy normal
    mike.say "Yes, Mistress, thank you, Mistress. I love seeing your boobs, Mistress."
    "It's true. I do love seeing her boobs."
    show cassidy happy
    "And while I work my now fully erect cock, she watches with no small amount of lust. After a few moments of this, her hand goes under her skirt."
    "She starts to finger herself where I can't see."
    mike.say "Can I watch, Mistress?"
    show cassidy talkative
    cassidy.say "No. You have enough to go on."
    show cassidy normal
    mike.say "Yes, Mistress. Thank you, Mistress."
    "After a few more strokes, pre-cum starts to leak out the tip, getting my fingers wet."
    "The extra wetness makes my cock slippery, which adds to the sensation. Almost unexpectedly, a big, thick burst of semen shoots out and hits the floor, near her feet."
    "Damn. I really wanted to get it up to her chest, but I wasn't fast enough."
    "Cassidy bends over, touches the glop of goo on the floor with her finger and touches it to her mouth."
    show cassidy casual topless wet with dissolve
    "And where she pulled her hand out from under her skirt is quite wet."
    show cassidy talkative
    cassidy.say "Mmm. That's what I'm talking about."
    cassidy.say "You may go."
    show cassidy normal
    mike.say "That's it?"
    show cassidy talkative
    cassidy.say "Go. Now. Don't worry we'll talk again later."
    show cassidy normal
    "I want to argue, but think better of it. Like it or not, she has my balls in her hands now. Literally and figuratively."
    $ cassidy.sub -= cassidy_sub + 10
    $ cassidy.love += 2
    return

label cassidy_investigation_complete:

    $ cassidy.flags.assistantdelay = TemporaryFlag(True, 1)
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Office")
    if not result:
        $ hero.cancel_event()
        return
    "A voice I don't recognize tells me to come into Aletta's office right away."
    "I'm on my way to Aletta's office when I spy Cassidy in my office. When she sees me, she beckons me to come in by curling one finger toward her."
    show bg personal with fade
    show cassidy casual happy
    cassidy.say "Good morning, Sweetie!"
    show cassidy talkative
    cassidy.say "I just wanted to give you one last chance, before you meet with Daddy. Are you going to play nice? Are you going to be my sweet, delicious boy?"
    show cassidy normal
    if game.flags.workinvestigation > 99:
        call cassidy_investigation_good_ending from _call_cassidy_investigation_good_ending
    else:




        if game.flags.cassidyrecorded:
            call cassidy_investigation_blackmail from _call_cassidy_investigation_blackmail
        else:
            call cassidy_investigation_bad_ending from _call_cassidy_investigation_bad_ending
    return

label cassidy_investigation_good_ending:
    mike.say "Funny, I was actually going to say the same thing to you."
    show cassidy annoyed
    "Her expression drops."
    show cassidy whining
    cassidy.say "Whatever do you mean, Sweetie?"
    show cassidy sad
    mike.say "You see, it turns out I know three things, and I can prove them all."
    show cassidy upset
    mike.say "First, that your daddy is an embezzling criminal, and once I show the data to everyone, this won't be his company anymore."
    mike.say "Second, that your much-too-old-for-you sex toy named Jeff in accounting set all this up, and I can show where he personally moved the money that they claim I stole."
    mike.say "Third, that you're a blackmailing bitch who's too stupid to look for cameras, and I have our midnight meeting on video. I think that one is going to play really well."
    mike.say "So, *Sweetie*, are you going to play nice? Or do I send your whole criminal family to jail."
    show cassidy angry
    cassidy.say "You're lying."
    show cassidy upset
    "I toss a file onto my desk."
    mike.say "The proof is right there."
    if game.flags.cassidyrecorded:
        "Cassidy picks up the file and starts to flip through it. It's apparent she has no idea what she's looking at, until she gets to the pictures of herself in my office."
    else:
        "Cassidy picks up the file and starts to flip through it."
    show cassidy annoyed
    cassidy.say "Fuck."
    show cassidy upset
    mike.say "Yes. Fuck indeed."
    show cassidy angry
    cassidy.say "Fine. What do you want?"
    show cassidy upset
    mike.say "You're going to do whatever I want. You're going to break up with all of your boyfriends. Every single one of them."
    mike.say "You're going to get a job here at the office as my personal assistant. And then you're going to...assist me."
    show cassidy angry
    cassidy.say "No! No way, fuck you and fuck that."
    show cassidy upset
    "I shrug, then take the file from her hands."
    mike.say "If that's the way you want it."
    "I start walking toward the door, but I only get two steps before she stops me."
    show cassidy whining
    cassidy.say "Wait! Please don't get Daddy fired."
    show cassidy sad
    "I turn back around and look at her."
    mike.say "So we have a deal? I'll put this data away, and in exchange, you'll go in there, get your Daddy to end this investigation right here. Pin it on Jeff and give him an early retirement."
    mike.say "And you'll do whatever the fuck I want."
    show cassidy annoyed
    "Cassidy purses her lips, but doesn't say anything."
    mike.say "Well?"
    show cassidy whining
    cassidy.say "Nothing painful. No blood. I wouldn't have done anything to hurt you, I ask...I just ask the same."
    show cassidy sad
    mike.say "Done."
    show cassidy talkative
    cassidy.say "So...I guess. I guess I'll go see Daddy now and..."
    show cassidy sadsmile
    mike.say "I wouldn't tell him too much about what you're doing. He doesn't need to know you're saving his ass. Just make it clear I keep my job, or he goes to jail."
    show cassidy talkative
    cassidy.say "Fine, yes."
    show cassidy sadsmile
    mike.say "You mean, 'Yes, Master'. You should get used to calling me Master right now."
    "Cassidy winces and looks like she's going to say something rude, but thinks better of it."
    show cassidy talkative
    cassidy.say "Yes...Master."
    show cassidy sadsmile
    if cassidy.sub.max < 100:
        $ cassidy.sub.max = 100
    $ cassidy.sub.val = 50
    $ cassidy.sub.min = 50
    $ cassidy.status = "pet"
    $ cassidy.flags.schedule = "assistant"
    $ cassidy.flags.nokiss = False
    $ cassidy.flags.mikeNickname = "Master"
    hide cassidy with moveoutleft
    "Cassidy walks out. After a few moments, I'm called in to Aletta's office."
    scene bg alettaoffice with dissolve
    show aletta work normal a at left
    show dwayne happy work at right
    dwayne.say "So, [hero.name], Aletta here tells me that you're her best employee."
    show dwayne normal
    mike.say "Well, one of her best employees. She has quite a few good employees."
    show aletta happy
    aletta.say "Oh don't undersell yourself, [hero.name]. This company is much better off with you here."
    show aletta normal
    show dwayne happy
    dwayne.say "Well, then. In any case, the investigation has come up inconclusive. While there is some evidence that you might have stolen the money, we think it could have been someone else."
    dwayne.say "So effective immediately, you are reinstated to your position. Accounting is going to keep a very, very close eye on your reports from here on out."
    dwayne.say "But since it seems you're most likely innocent, you have nothing to worry about as long as you keep your nose clean."
    show dwayne normal
    mike.say "Thank you, Dwayne. I'm glad to hear that."
    "It's pretty clear to both Aletta and me that he's not happy about how this situation has turned out, and is doing his best to put on a good face."
    show dwayne happy
    dwayne.say "Mm, yes. Well, I think I'm done here. Carry on."
    dwayne.say "And it goes without saying, [hero.name], neither of us will talk to anyone outside this room about this?"
    show dwayne normal
    mike.say "Yes, sir."
    show dwayne happy
    dwayne.say "Good, good."
    show dwayne normal at top_mostright with move
    "As Dwayne leaves, looks troubled and...maybe a little bit scared."
    hide dwayne with moveoutright
    aletta.say "Well, [hero.name], I don't know how you pulled that off. And I don't want you to tell me, whatever happened it's best I don't know anything."
    show aletta happy
    aletta.say "But I'm happy to have you back, [hero.name]. Seriously!"
    $ aletta.love += 5
    $ game.flags.underinvestigation = False
    $ game.flags.suspended = False
    $ game.room = "personal"
    return

label cassidy_investigation_successful:
    mike.say "Funny, I was actually going to say the same thing to you."
    show cassidy normal
    "Her expression drops."
    show cassidy talkative
    cassidy.say "Whatever do you mean, Sweetie?"
    show cassidy normal
    mike.say "You see, it turns out I know two things, and I can prove them all."
    show cassidy upset
    mike.say "First, that your daddy is an embezzling criminal, and once I show the data to everyone, this won't be his company anymore."
    mike.say "Second, that your much-too-old-for-you sex toy named Jeff in accounting set all this up, and I can show where he personally moved the money that they claim I stole."
    mike.say "So, *Sweetie*, are you going to play nice? Or do I send your whole criminal family to jail."
    show cassidy angry
    cassidy.say "You're lying."
    show cassidy upset
    "I toss a file onto my desk."
    mike.say "The proof is right there."
    "Cassidy flips through it. Her eyes quickly glaze over at the rows and rows of numbers. She doesn't know anything about business."
    "She turns back to look at me."
    show cassidy angry
    cassidy.say "Go ahead, do what you want. My Daddy is much smarter than you. You'll never make any...whatever this is stick."
    show cassidy upset
    "She throws the file back down onto my desk, and walks out in a huff."
    hide cassidy
    "I wasn't expecting that. I mean, I know she doesn't have any idea what was actually in this file, but I had hoped to come to an arrangement without using it. Now...well I guess we'll see."
    scene bg alettaoffice with dissolve
    show aletta work normal a at left
    show dwayne work vangry at right
    dwayne.say "[hero.name], the investigation has determined your complicity in theft from my company. You are terminated, effective immediately."
    show dwayne upset
    mike.say "Aletta, before you act on that, I think you should look in this file."
    "I hand Aletta the file, who quickly thumbs through the sheaf of papers. After a brief moment, her eyebrows shoot up."
    show aletta surprised
    aletta.say "Dwayne, according to this, you're the one who's been embezzling the money. This shows how a subsidiary...Deewah holdings. Deewah? Really Dwayne?"
    show aletta normal
    show dwayne shout
    dwayne.say "I have no idea what you're talking about, Aletta."
    show dwayne upset
    show aletta angry
    aletta.say "It doesn't matter. When the board of directors sees this, and if this data holds up, you're going to be fired, Dwayne."
    show aletta normal
    show dwayne shout
    dwayne.say "That's...that's not possible."
    show dwayne upset
    show aletta angry
    aletta.say "You'd better go deal with this, Dwayne."
    show aletta normal
    hide dwayne with moveoutright
    show aletta talkative
    aletta.say "Oh, and [hero.name], you can ignore what he said about you being fired. I'm taking charge of this investigation, as of now."
    aletta.say "If this turns out to be true, you're going to get a nice promotion."
    show aletta normal
    mike.say "Thanks, Aletta."
    show aletta happy
    aletta.say "Oh, no, thank {b}you{/b}. This, this is some of your best work. I hope you can keep this up."
    $ game.set_flag("promoted", 5, mod="+")
    $ game.flags.worksatisfaction = 0
    $ aletta.love += 5
    $ game.flags.underinvestigation = False
    $ game.flags.suspended = False
    $ cassidy.set_gone_forever()
    $ game.flags.dwaynefired = True
    return

label cassidy_investigation_blackmail:
    mike.say "Funny, I was actually going to say the same thing to you."
    show cassidy upset
    "Her expression drops."
    show cassidy whining
    cassidy.say "Whatever do you mean, Sweetie?"
    show cassidy sad
    mike.say "I have you on video, trying to extort me into playing your twisted little game. And on this video, you admit this whole thing is a setup."
    mike.say "I'm going to send this video to everyone in the company, and a few of your dad's friends. Maybe a Senator or two."
    show cassidy annoyed
    "Cassidy blanches."
    mike.say "Of course, I might be willing to avoid all that...ugliness."
    show cassidy whining
    cassidy.say "Really. And what do you want?"
    show cassidy sad
    mike.say "To turn the tables. You do for me what you wanted me to do for you."
    show cassidy surprised
    cassidy.say "Huh. You want me to be your personal valet?"
    show cassidy stuned
    mike.say "Let's call it assistant. You can...assist me."
    show cassidy talkative
    cassidy.say "Hm. Yeah, let's see. You can release that and the fallout will blow over inside a year. I'll be fine, and a few people will know how ruthless I am and appreciate that."
    show cassidy normal
    mike.say "Really? That easy?"
    "Cassidy shrugs, carefully keeping her expression neutral. I do my best to judge if she's bluffing or not."
    mike.say "I'm pretty sure this will put you in jail."
    show cassidy talkative
    cassidy.say "Nah, I didn't steal anything."
    show cassidy normal
    mike.say "Fine, but your pet accountant will take the fall. Then you won't have him to entertain you anymore."
    show cassidy talkative
    cassidy.say "Fuck him."
    show cassidy normal
    mike.say "I see. Well, I guess that's that, then, because I'm not getting fired for you."
    show cassidy talkative
    cassidy.say "Well, wait a second now. I'm sure there's...some other arrangement we could come to."
    show cassidy sadsmile
    "I take a moment to think about that. I can think of all kinds of things I wouldn't mind doing to this gorgeous woman, but I'm not sure how willing I am to negotiate."
    show cassidy talkative
    cassidy.say "Give me the video and I'll get the investigation called off. You'll get your job back."
    show cassidy normal
    mike.say "After all this, that's it? Status quo? This week has been hell. Thank you, but no, I'd rather see you pay for this."
    "Cassidy looks at me for a second, thoughtful."
    show cassidy annoyed
    cassidy.say "Okay, fine. You deserve a little payback. What do you want. Me on my knees?"
    show cassidy upset
    "I lick my lips, and try not to tip my hand, but I can't hide how much that thought appeals to me."
    "She takes a step toward me, swaying her hips exaggeratedly as she does so."
    show cassidy annoyed
    cassidy.say "I can do that. I'll give you the best damn blowjob you've ever had. I'll tell Daddy to call off the investigation. And you'll hand over the video."
    show cassidy upset
    mike.say "I think I'll be holding onto the video. I have no way of knowing if you'll find some other way to screw me once that's gone."
    show cassidy annoyed
    cassidy.say "And how do I know you won't keep extorting me for more?"
    show cassidy upset
    mike.say "I guess we're at an impasse, then."
    show cassidy talkative
    cassidy.say "Come on, Sweetie. Be reasonable."
    show cassidy sadsmile
    mike.say "Fuck reasonable. You did this. I don't see any reason to be reasonable."
    "Cassidy stares at me intently for a few moments. I swear if she had superpowers, my head would burst into flames."
    show cassidy talkative
    cassidy.say "Fine, you can keep your video. But if you release that even after I've given you what you asked for, I will spend the rest of my life destroying you."
    cassidy.say "And I have the money and power to do a lot worse to you than just cost you your job."
    show cassidy normal
    mike.say "Great, it sounds like we have a deal then."
    show cassidy talkative
    cassidy.say "I'll go get your meeting fixed up. You wait here."
    hide cassidy with moveoutleft
    "Cassidy walks out. After a few moments, I'm called in to Aletta's office."
    scene bg alettaoffice with fade
    show aletta work normal a at left
    show dwayne happy at right
    dwayne.say "So, [hero.name], Aletta here tells me that you're one of her best employees."
    show dwayne normal
    mike.say "That's very kind of her."
    show aletta happy
    aletta.say "Don't sell yourself short, [hero.name]. You absolutely are."
    show aletta normal
    show dwayne happy
    dwayne.say "Anyhow, [hero.name], I've got news for you. It seems that the investigation is inconclusive. There isn't enough evidence to take action."
    dwayne.say "Effective immediately, you're reinstated to your position. We will continue to investigate as needed, but as of now we are looking in other areas."
    show dwayne shout
    dwayne.say "But be warned: if any other irregularities occur in your accounts, we'll be keeping a very, very close eye on you."
    show dwayne normal
    mike.say "Ah, of course. Thank you."
    hide dwayne with moveoutright
    aletta.say "Well, [hero.name], I don't know how you pulled that off. And I don't want you to tell me, whatever happened it's best I don't know anything."
    show aletta happy
    aletta.say "But I'm happy to have you back, [hero.name]. Seriously!"
    $ aletta.love += 5
    $ game.flags.underinvestigation = False
    $ game.flags.suspended = False
    "I thank Aletta, but I admit I'm in a bit of a hurry to get back to my office, and see if Cassidy is really going to pay up."
    scene bg personal
    show cassidy casual talkative
    with fade
    cassidy.say "Well, hello again, Sweetie."
    show cassidy normal
    mike.say "Hello yourself, sexy. I believe we had a deal. Get down on your knees."
    show cassidy talkative
    cassidy.say "Of course. Why don't you sit down in your chair here?"
    show cassidy normal
    call cassidy_tittyfuck from _cassidy_investigation_blackmail
    show cassidy talkative
    cassidy.say "And now, Sweetie, I think we're even. Good luck with the job."
    show cassidy normal
    "And without another word, and without even cleaning herself up, she marches out of my office."
    "As awesome as that was, I find myself wondering if I could have done better. Having those lips and those tits on my dick every day would be...amazing."
    $ cassidy.set_gone_forever()
    return

label cassidy_investigation_bad_ending:
    "I don't have any evidence to save me. If I tell her no, I'll certainly get fired. If I tell her yes, I don't know that she won't play with me and get me fired anyway. But what am I going to do?"
    menu:
        "I can always get another job":
            mike.say "No, Cassidy, you can go fuck yourself. I don't need this job badly enough to be your bitch."
            show cassidy talkative
            cassidy.say "Are you sure? How about if I promise it won't be painful. No blood, no pain, just you getting on your knees."
            show cassidy normal
            "She leans forward and her voice turns husky."
            show cassidy talkative
            cassidy.say "I promise I'll take good care of you, Sweetie, as long as you take good care of my needs."
            cassidy.say "So. Last chance!"
            show cassidy normal
            menu:
                "No, not worth it":
                    mike.say "No, you're not worth it."
                    call cassidy_mike_fired from _call_cassidy_mike_fired
                "Fine, you win":
                    call cassidy_dom_path from _call_cassidy_dom_path
        "How bad can being her bitch be?":
            call cassidy_dom_path from _call_cassidy_dom_path_1
    return

label cassidy_mike_fired:
    scene bg alettaoffice
    show aletta work sad a at left
    show dwayne upset at right
    with fade
    "Aletta and Dwayne both look grim."
    show dwayne shout
    dwayne.say "Hello, [hero.name]. Thanks for coming in."
    show dwayne upset
    mike.say "Sure."
    show dwayne shout
    dwayne.say "The investigation has shown conclusively that you're responsible for the money disappearing. The good news for you is that we've determined that this is due to negligence, and not embezzling."
    show dwayne upset
    mike.say "How is that good news?"
    show dwayne shout
    dwayne.say "It means we won't be suing you to recover the money."
    show dwayne upset
    mike.say "Ahh. And my job?"
    show dwayne shout
    dwayne.say "You're terminated, effective immediately."
    show dwayne upset
    mike.say "Oh."
    show dwayne shout
    dwayne.say "Aletta, please escort Mister [hero.family_name] from the premises."
    show dwayne upset
    show aletta whining
    aletta.say "I'm sorry, [hero.name]. I really am."
    show aletta sad
    "I nod. Aletta walks me to the exit, but there doesn't appear to be much for either of us to say."
    $ game.room = "map"
    scene bg street
    show aletta a work whining
    with fade
    aletta.say "Keep in touch, [hero.name], okay? I hope we can still be friends."
    show aletta a sad
    mike.say "Yeah, sure. I guess."
    "I'm not really trying to brush her off, but this is pretty depressing."
    "She gives me a brief hug, then disappears back into the office building."
    $ Room.find("office").hide()
    $ cassidy.set_gone_forever()
    $ game.flags.fired = True
    $ game.flags.job_day = False
    $ aletta.love -= 10
    $ lavish.love -= 10
    $ shiori.love -= 10
    $ game.flags.underinvestigation = False
    $ game.flags.suspended = False
    "Now what am I going to do? Maybe I can get a job in the mall to keep the rent paid, or something."
    return

label cassidy_dom_path:
    $ cassidy.sub.max = 0
    $ cassidy.sub.min = -100
    $ cassidy.status = "mistress"
    $ cassidy.sub.val = 0
    $ cassidy.sub -= 10
    $ cassidy.flags.schedule = "assistant"

    $ cassidy.set_counter("boredom")
    "I take a deep breath. This sucks, but I have to do it."
    mike.say "Yes, Cassidy. I'll be your valet."
    show cassidy happy
    cassidy.say "Oh good! We're going to have so much fun! I promise, this will be fun for you. I mean, you get to fuck the CEO's daughter, right?"
    show cassidy normal
    "She's not wrong. That part might be fun, but honestly I'm used to being the one in charge for that."
    mike.say "Sure. It'll be fun, I guess."
    show cassidy whining
    cassidy.say "Wrong answer! Try something better, like 'Yes, Mistress, it will be fun!'"
    show cassidy normal
    "Ugh."
    mike.say "Yes, Mistress, it will be fun."
    "Clearly I didn't sound terribly into it."
    show cassidy talkative
    cassidy.say "Try that again, with more enthusiasm, slave."
    show cassidy normal
    "That one makes me scowl."
    mike.say "I'm not your slave. I'll be your valet but I'm not your slave."
    show cassidy talkative
    cassidy.say "Would you rather be my bitch?"
    show cassidy normal
    menu:
        "Bitch":
            mike.say "Yes, I'd rather be your bitch."
            $ cassidy.flags.mikeNickname = "Bitch"
        "Slave":
            mike.say "Fine, slave is better than bitch."
            $ cassidy.flags.mikeNickname = "Slave"
    show cassidy talkative
    cassidy.say "Now that we've got that cleared up, try that with more enthusiasm, {b}[hero.name]{/b}"
    show cassidy normal
    "I work up all the enthusiasm I can."
    mike.say "It will be fun, Mistress!"
    show cassidy happy
    cassidy.say "Great. Wait here, I'll go get this fixed."
    hide cassidy with moveoutleft
    "After a few moments, I'm called into Aletta's office."
    scene bg alettaoffice
    show aletta work normal a at left
    show dwayne happy at right
    with fade
    dwayne.say "So, [hero.name], Aletta here tells me that you're one of her best employees."
    show dwayne normal
    mike.say "That's very kind of her."
    show aletta happy
    aletta.say "Don't sell yourself short, [hero.name]. You absolutely are."
    show aletta normal
    show dwayne happy
    dwayne.say "Anyhow, [hero.name], I've got news for you. It seems that the investigation is inconclusive. There isn't enough evidence to take action."
    dwayne.say "Effective immediately, you're reinstated to your position. We will continue to investigate as needed, but as of now we are looking in other areas."
    show dwayne shout
    dwayne.say "But be warned: if any other irregularities occur in your accounts, we'll be keeping a very, very close eye on you."
    show dwayne normal
    mike.say "Ah, of course. Thank you."
    hide dwayne with moveoutright
    show aletta talkative
    aletta.say "Well, [hero.name], I don't know how you pulled that off. And I don't want you to tell me, whatever happened it's best I don't know anything."
    show aletta happy
    aletta.say "But I'm happy to have you back, [hero.name]. Seriously!"
    show aletta normal
    $ aletta.love += 5
    $ game.flags.underinvestigation = False
    $ game.flags.suspended = False
    $ cassidy.flags.nokiss = False
    $ hero.smartphone_contacts.append("cassidy")
    "I thank Aletta, and head back to my office."
    $ game.room = "personal"
    scene bg personal
    show cassidy casual talkative
    with fade
    cassidy.say "Well, hello again, Sweetie."
    show cassidy normal
    mike.say "Hello, Cas--Mistress."
    show cassidy happy
    cassidy.say "Oh very good, you caught yourself! I hope that means you'll be a quick learner."
    show cassidy normal
    "I shrug."
    show cassidy talkative
    cassidy.say "So, how good are you with your tongue?"
    show cassidy normal
    mike.say "What do you mean?"
    show cassidy talkative
    cassidy.say "You look like a dude who's licked a few pussies in your life. Are you any good at it?"
    show cassidy normal
    menu:
        "I'm great at it":
            mike.say "Oh yeah, I'm great at it. I love eating a girl out! They always squirm with delight!"
            $ cassidy.love -= 2
            show cassidy talkative
            cassidy.say "Oh yeah? Let's see if you can live up to your big words."
            show cassidy normal
        "I need more practice":
            show cassidy talkative
            mike.say "If I'm being strictly honest, I probably could use more practice."
            $ cassidy.love += 2
            cassidy.say "Well then, let's do it."
            show cassidy normal
    call cassidy_dom_oral from _call_cassidy_dom_oral_2
    return

label cassidy_dom_oral:
    show cassidy talkative
    cassidy.say "Get over here and get down on your knees, [hero.name]!"
    show cassidy normal
    menu:
        "Obey":
            "I do as I'm told without a word, walking right up to her and dropping to my knees."
            $ cassidy.sub -= 3
            $ cassidy.love += 1
            "I look up at her, expectantly."
        "Resist, playfully":
            "I smile, just slightly, but don't move."
            show cassidy talkative
            cassidy.say "Now, [hero.name], or do I have to punish you?"
            show cassidy normal
            mike.say "Oooh, punishment? What're you going to do to me if I don't play nice?"
            show cassidy talkative
            cassidy.say "Are you looking for a spanking, Sweetie?"
            show cassidy normal
            mike.say "Oh, you going to spank me?"
            show cassidy talkative
            cassidy.say "Would you rather get fired?"
            show cassidy normal
            "I grin, and I figure I've pushed that one as far as I dare to. So I walk up to her--slowly--and put my hands on her hips."
            $ cassidy.sub -= 1
            $ cassidy.love += 3
            "Then I sink down to my knees and look up at her."
        "Resist, impudently":
            "I stand where I am. Maybe if I make this hard for her, she won't have any fun and will give up."
            show cassidy talkative
            cassidy.say "Now, [hero.name], or do I have to punish you?"
            show cassidy normal
            mike.say "Really? You're going to punish me?"
            show cassidy talkative
            cassidy.say "Do you want to keep your job?"
            mike.say "Yes."
            show cassidy angry
            cassidy.say "Then get down on your fucking knees and do what you're fucking told."
            show cassidy upset
            "I narrow my eyes and calculate just how far it's safe to push her. I decide this is far enough...for now."
            "So I walk up to her and sink to my knees, glaring at her the entire time."
            $ cassidy.love -= 5
            $ cassidy.sub += 1
    show cassidy wink bottomless
    show pussy_insert cassidy zorder 1 at zoomAt(0.65, (20, 60))
    with dissolve
    "Cassidy sits on my desk and hikes her skirt up around her hips, giving me a very close up view of her pussy."
    hide cassidy
    show bg black
    with dissolve
    pause 0.3
    show cassidy cunnilingus hurt
    with dissolve
    "She puts her hands on the back of my head and pulls me roughly toward her. I have to put my hands on her thighs just to keep from losing my balance, but it also has the effect of pushing her legs further apart."
    "I have to close my eyes as she pushes me right in; my nose gets covered with her juices, and her pubes feel kind of funny across my cheeks and forehead."
    "Her thick, musty scent fills my nose. It's almost overpowering at first, but that sensation subsides in just a moment."
    "Since she seems to want to be in control, I let her. She moves my face up and down against her, and her soft pussy lips open up for me."
    show cassidy cunnilingus happy
    cassidy.say "Use your tongue!"
    show cassidy cunnilingus hurt at stepback(speed=0.1, h=-10, v=0)
    "I tighten my grip on her thighs and stick my tongue out. She's wet and ready, and I'm filled with her unique flavor."
    "I find her clitoris and focus the tip of my tongue there, pulling it between my lips and sucking on it, just for a second, before letting it go again."
    show cassidy cunnilingus at stepback(speed=0.1, h=-10, v=0)
    "She moans softly at that, her hands pushing me tighter into her. I repeat the motion, and her second moan is even louder."
    "While I go at her, I release my primary hand from her thigh and slide it underneath her, sliding in between her ass cheeks."
    show cassidy cunnilingus at stepback(speed=0.1, h=-10, v=0)
    "She yelps when I stink my finger into her anus, but doesn't stop me."
    "I continue to eat her out, while pushing my finger in first to one knuckle, then the other, careful to keep my fingernail from scraping her delicate flesh."
    show cassidy cunnilingus happy
    "She lets out another gasp."
    show cassidy cunnilingus pleasure
    cassidy.say "More. More, [hero.name]! {b}More!{/b}"
    show cassidy cunnilingus hurt at stepback(speed=0.1, h=-10, v=0)
    "I can't really use my tongue any more, as she's pushing my head up and down with her hands, so it's all I can do just to keep everything in a good place, making sure I stimulate her clit when I can."
    show cassidy cunnilingus wide happy
    with hpunch
    cassidy.say "YES!!"
    show cassidy cunnilingus hurt
    "I push my finger all the way into her anus."
    play sexsfx1 squirt_short
    hide pussy_insert
    show cassidy cunnilingus pleasure ahegao squirt
    with hpunch
    "And then she orgasms; if I thought she was wet before, this was almost like having a bucket of sticky goo thrown right in my face. It drips off me, staining my clothes and her thighs."
    play sexsfx1 squirt_short
    with hpunch
    "She lets go of me and I pull back so I can look up at her."
    show cassidy cunnilingus -squirt with hpunch
    mike.say "Wow."
    "Cassidy's chest heaves in mighty breaths while she looks down at me. Her face is an expression of pure delight."
    show cassidy cunnilingus pleasure happy
    if cassidy.love < 120:
        cassidy.say "Fuck, [hero.name], you are just about the second best I've ever had."
        show cassidy wide hurt
        mike.say "{b}Second{/b} best?"
        "She winks at me."
        "Maybe you can work your way up to being all best."
    else:
        cassidy.say "Fuck, [hero.name], you are the best I've ever had. I'm going to keep you forever."
        cassidy.say "Oh God, maybe you can move in with me."
        show cassidy cunnilingus wide hurt
        mike.say "Maybe someday."
        "She smiles down at me, an expression filled with love and unexpected kindness."
    scene expression "bg {}".format(game.room)
    show cassidy wink wet bottomless
    with fade
    "I stand up and work on cleaning her love juices off my face."
    show cassidy talkative
    cassidy.say "Oh that was so good. I can't wait to do that again!"
    show cassidy normal
    return

label cassidy_new_assistant:
    $ hero.smartphone_contacts.append("cassidy")
    $ cassidy.flags.nodate = False
    $ cassidy.flags.birthdayknown = True
    if cassidy.love.max < 80:
        $ cassidy.love.max = 80
    show aletta talkative at left
    if cassidy.status == 'pet':
        show cassidy casual normal at right
    else:
        show cassidy casual happy at right
    aletta.say "Hi [hero.name]! I got a call from Dwayne last night, and he's decided he wants his daughter to get some business training."
    show aletta happy
    aletta.say "So as of today, Cassidy is your new personal assistant. You're going to be showing her the ropes, and training her on everything there is to know about the company."
    show aletta normal
    if cassidy.status == 'mistress':
        show cassidy talkative
        aletta.say "And if she does a good job, she will eventually be our new boss."
        aletta.say "She'll also be keeping a bit of an eye on you, to make sure nothing funny happens with your accounts again."
        show cassidy happy
        "Cassidy gives me a big smile. She already knows who the boss is."
    else:
        show aletta talkative
        aletta.say "And if she does a good job, there may be a permanent place for her at the company."
        show aletta normal
    mike.say "Wow, Aletta, that was quick!"
    "I turn to Cassidy."
    mike.say "I guess we'll have to see what you can do, right?"
    show aletta talkative
    aletta.say "Right, I'll let you get to it."
    show aletta normal
    "As Aletta heads past me out the door, she puts her hand on my arm and leans close to whisper."
    show aletta whining
    aletta.say "Be careful, [hero.name]. She's got a reputation."
    show aletta sadsmile
    mike.say "I know. It'll be okay, Aletta. And thanks, I appreciate the warning. It's good to know you care."
    $ aletta.love += 2
    hide aletta with easeoutleft
    show cassidy at center, zoomAt(1.0, (640, 720)) with ease
    if cassidy.status == 'mistress':
        show cassidy talkative
        cassidy.say "Oh yes, [hero.name]. You're definitely going to have your work cut out for you for the next few months."
        cassidy.say "I look forward to your training."
        show cassidy normal
        menu:
            "I'm doing the training":
                mike.say "Aletta just said I'm the one doing the training."
                $ cassidy.love -= 1
                $ cassidy.sub += 1
                show cassidy talkative
                cassidy.say "I think I already know all I need to know about business. It's you that needs to learn. You don't know your place yet."
                cassidy.say "But you will. If you know what's good for you."
                show cassidy happy
                cassidy.say "I hold your life in my hands!"
            "Yes, Mistress":
                $ cassidy.sub -= 1
                $ cassidy.love += 1
                mike.say "Yes, Mistress. I look forward to the training too."
        show cassidy talkative
        cassidy.say "Now, lesson one. Who is your mistress?"
        show cassidy normal
        mike.say "You are."
        show cassidy happy
        cassidy.say "Excellent. Are you going to be an obedient boy?"
        mike.say "Yes."
        show cassidy talkative
        cassidy.say "Yes, what?"
        show cassidy normal
        mike.say "Yes...Mistress."
        show cassidy talkative
        cassidy.say "Very good. Keep this up and I'll reward you."
        show cassidy normal
        mike.say "What kind of reward?"
        show cassidy happy
        cassidy.say "We'll see! Trust me, you'll like it. But that's for another time."
        show cassidy normal
    else:
        show cassidy whining
        cassidy.say "So. So now what?"
        show cassidy sad
        mike.say "Are you okay? You look upset."
        "With visible effort, the slightly sad look she had disappears."
        show cassidy talkative
        cassidy.say "Yeah, I'm fine. I just...I was going to go to Paris today."
        show cassidy normal
        mike.say "Ah. Yes, I expect with this new job, your schedule is going to be very different."
        "She sighs."
        menu:
            "It'll be okay.":
                mike.say "Hey, it'll be okay. This job will be good for you. You've never had to work a day in your life, have you?"
                show cassidy talkative
                cassidy.say "What do you know about my work? Keeping up appearances to all of Daddy's social friends is a full time job!"
                show cassidy sadsmile
                mike.say "Ah, I guess it is."
                show cassidy talkative
                cassidy.say "I have no idea how I'll manage that."
                show cassidy sadsmile
                mike.say "You're doing exactly what your Daddy needs you to do, right now. So forget about all that for now."
                mike.say "Just stick around here, learn the job, and do what I ask. I promise I won't hurt you."
                $ cassidy.love += 1
                $ cassidy.sub += 1
                show cassidy talkative
                cassidy.say "Okay, I guess."
                show cassidy normal
            "Suck it up, Buttercup":
                mike.say "Suck it up, Buttercup! You did this to yourself."
                $ cassidy.love -= 1
                $ cassidy.sub -= 1
                show cassidy angry
                cassidy.say "No, you're doing this to me!"
                show cassidy upset
                mike.say "None of this would be happening if you didn't try to fuck with me. Otherwise we could be sitting in a bar, getting drinks, swapping stories."
                mike.say "You made your bed, now you're going to fuck me in it."
                show cassidy normal
                "Cassidy squirms at that."
                show cassidy angry
                cassidy.say "Yeah, but do you have to be such an asshole about it?"
                show cassidy upset
                mike.say "Learn to behave and maybe I'll be nicer."
                show cassidy talkative
                cassidy.say "Fine."
                show cassidy sadsmile
        mike.say "Now, how about a kiss?"
        show cassidy at center, traveling (1.5, 0.5, (650, 1050))
        "Almost reluctantly, Cassidy steps up to me. I put my hands on her hips and pull her close."
        hide cassidy
        show cassidy kiss
        with fade
        $ cassidy.flags.kiss += 1
        "She tries to make the kiss short, but I hold her close, adding some heat to the kiss. After a few moments, she finally responds in kind."
        "And just about then, I decide that's enough for the moment."
        hide cassidy
        show cassidy casual normal at center, zoomAt (1.5, (650, 1050))
        with fade
        mike.say "Mm, that's excellent. We'll definitely be wanting more of that in the future."
        show cassidy talkative
        cassidy.say "Of course, Master."
        show cassidy sadsmile
    return

label cassidy_dom_boredom:
    $ cassidy.set_counter("boredom", None)
    show cassidy casual talkative
    cassidy.say "You know, [hero.name], I may not have told you this, but I only ever intended our little arrangement here to be temporary."
    cassidy.say "I usually get bored with a guy after a couple of months."
    show cassidy normal
    mike.say "You never mentioned that."
    if cassidy.love < 160:
        show cassidy talkative
        cassidy.say "And I'm going to be honest, you've been kind of fun but I think I'm pretty much done with you."
        show cassidy normal
        mike.say "What are you saying, Mistress?"
        show cassidy talkative
        cassidy.say "You don't have to call me that any more. You're free. I'm quitting this \"job\"."
        show cassidy normal
        menu:
            "No, don't go!":
                mike.say "But Mistress, wait! Please don't go! Have I not been good enough for you?"

                $ cassidy.love += 10
                if cassidy.love > 160 and cassidy.sub < -80:
                    show cassidy talkative
                    cassidy.say "Well, you have been fun. And you have been a good boy."
                    cassidy.say "You really want me to keep you?"
                    show cassidy normal
                    mike.say "Oh yes, Mistress. This has been the best thing that's ever happened to me."
                    show cassidy kiss with fade
                    $ cassidy.flags.kiss += 1
                    "Cassidy wraps her arms around me and pulls me in close for a kiss, which I am happy to oblige."
                    hide cassidy
                    show cassidy casual talkative at center, zoomAt (1.5, (650, 1050))
                    with fade
                    cassidy.say "Ok, [hero.name], you've earned yourself another few weeks."
                    show cassidy normal
                    mike.say "Thank you, Mistress! You won't regret it!"
                    return
                show cassidy talkative
                cassidy.say "That's sweet, [hero.name], but I'm just losing interest in you. It's me, not you. You know what, fuck that, I suck at the breakup speech. We're done, you need to move on."
                hide cassidy with easeoutleft
                "She walks out the door, leaving me absolutely speechless. What did I do wrong? Would she have stayed if I had been done a better job? I guess I'll never know."
            "Free at last!":
                mike.say "Oh thank God, I'm free of you!"
                show cassidy angry
                cassidy.say "Oh, well now, if you're going to be like that, maybe I'll stick around and keep you on your knees for a little bit longer."
                show cassidy normal
                mike.say "Oh, uh. I mean, thank you for my freedom, Mistress?"
                show cassidy happy
                "Cassidy laughs."
                show cassidy kiss with fade
                $ cassidy.flags.kiss += 1
                "She steps up to me and wraps her arms around my neck, pulling me in for a kiss. It is deep and long, one of the most passionate she's ever given me, and in that moment, I'm actually just a little bit said."
                "Whatever was going on, she is always fantastic in bed."
                hide cassidy
                show cassidy casual talkative
                with fade
                cassidy.say "I guess this is goodbye. Thanks for everything, [hero.name]. And good luck with the job."
                hide cassidy with moveoutleft
                "And with that, she's gone from my life, just as swiftly as she entered it. A tornado, probably off to wreak havoc on some other dude's life. I don't know if I envy or pity him. Maybe both."
        $ cassidy.set_gone_forever()
        $ cassidy.flags.schedule = None
    else:
        show cassidy talkative
        cassidy.say "But you know what? Something's different with you. I've never been with anyone that I've actually come to care about."
        cassidy.say "So I've decided I'm going to keep you. That is...if you want me to."
        show cassidy normal
        call cassidy_dom_boredom_keep from _call_cassidy_dom_boredom_keep
    return

label cassidy_dom_boredom_keep(bg=True):
    menu:
        "Yes!":
            mike.say "Yes, my Mistress, I want that. I want to be yours. I didn't at first, but my time with you...I cherish this."
            show cassidy talkative
            cassidy.say "Tell me you love me."
            show cassidy normal
            "I answer without hesitation."
            mike.say "I love you, Mistress. With all my heart and my soul."
            show cassidy casual at center, zoomAt (1.5, (650, 1050)) with hpunch
            "She practically throws herself at me, wrapping her arms around my neck and hugging me so tightly it's hard to breathe."
            show cassidy talkative
            cassidy.say "I love you too, [hero.name]!"
            cassidy.say "And you'll always, always be mine."
            show cassidy normal
            "I reflect, while being held too tightly in her embrace, on the path that led to this. Did I just commit my entire life to her?"
            "I did, and I think that it's going to be okay."
            return
        "No thanks":
            mike.say "Cassidy, you're amazing, and this thing we had has actually been fun. But...I've got goals and dreams, and being your sex slave isn't compatible with that."
            show cassidy sad
            mike.say "Sooner or later I'd have found a new job. And then you wouldn't have anything to hold over me."
            mike.say "And I'd be gone then anyway. If you're...getting attached, maybe it's better we end this now."
            show cassidy cry
            cassidy.say "I'm...I'm sorry, [hero.name]. I thought...I was sure you felt the same way I did."
            mike.say "Only because I had to, hon. Look, if it helps, when this started I thought you were a total conniving bitch, and I've learned that you're just a girl who has everything and that's not enough."
            mike.say "Whatever it is you're looking for, it's not me. I'm sorry."
            "She sobs, then nods. She tries to speak, but the noises that come out aren't words."
            "This seems to upset her even more, and she runs out the door."
            hide cassidy with moveoutleft
            "I guess this means I'm free, now?"
            $ cassidy.set_gone_forever()
            $ cassidy.flags.schedule = None
        "Boyfriend/girlfriend instead?":
            mike.say "How about we do this as boyfriend/girlfriend instead of this master/slave thing?"
            show cassidy talkative
            cassidy.say "I don't think I'm interested in just being one of your girlfriends. I want to keep you, but only if you want that."
            show cassidy normal
            call cassidy_dom_boredom_keep (False) from _call_cassidy_dom_boredom_keep_1
    return

label cassidy_bad_day:
    show cassidy talkative
    cassidy.say "[hero.name], what do you know about Aletta?"
    show cassidy normal
    mike.say "Aletta, as in our boss?"
    show cassidy talkative
    cassidy.say "Yeah, her."
    show cassidy normal
    mike.say "Why do you want to know?"
    "Cassidy shrugs and waves her hands. She's being evasive."
    show cassidy talkative
    cassidy.say "Just...it's not important, I guess. I want to know more about the company?"
    show cassidy normal
    "That's probably the worst lie I've ever heard her tell, but it doesn't seem a big deal to humor her."
    menu:
        "She's my sex slave" if aletta.flags.collared and aletta.sub > 50:
            mike.say "Well, she's kind of my sex slave."
            if cassidy.status == 'mistress':
                show cassidy talkative
                cassidy.say "So wait, if you're my sex slave, and she's your sex slave, does that make her my sex slave?"
                show cassidy normal
                mike.say "I...don't think she'll see it that way."
                show cassidy talkative
                cassidy.say "Huh. Maybe I should find out."
                show cassidy normal
            show cassidy talkative
            cassidy.say "Are you the only one she's banging?"
            show cassidy normal
            mike.say "I better be!"
            show cassidy talkative
            cassidy.say "But you don't know for sure?"
            show cassidy normal
            mike.say "I guess I'm not with her every minute. Why?"
        "She's someone I care about very much" if aletta.love > 160:
            mike.say "Well, she's someone I care about very much. It's weird to say that about your boss, but..."
            show cassidy talkative
            cassidy.say "Are you sleeping with her?"
            show cassidy normal
            mike.say "None of your business!"
            if cassidy.status == 'mistress':
                show cassidy talkative
                cassidy.say "Oh yes, where your dick goes is very much my business, [hero.name]!"
                show cassidy normal
                if aletta.sexperience:
                    mike.say "Fine, yes, I've fucked her. Happy?"
                else:
                    mike.say "No, I'm not sleeping with her."
            show cassidy talkative
            cassidy.say "Do you know if she's sleeping with anyone else?"
            show cassidy normal
            mike.say "No, I don't think so. At least, I hope not!"
        "She's a total bitch":
            mike.say "She's an overbearing, mean-spirited bitch of a boss."
            show cassidy talkative
            cassidy.say "Huh. Do you know if she has a boyfriend?"
            show cassidy normal
            mike.say "Why, are you looking for a girl?"
            show cassidy happy
            cassidy.say "Haha, fuck off. Seriously, is she seeing anyone?"
            show cassidy normal
            mike.say "Honestly, I have no idea."
        "She's a great boss":
            mike.say "She's a great boss. She's hard, sure, but she keeps the department running well, she doesn't let people slide by on nothing, and she rewards those who do good work."
            show cassidy talkative
            cassidy.say "Huh. Do you know if she has a boyfriend?"
            show cassidy normal
            mike.say "Why, are you looking for a girl?"
            show cassidy talkative
            cassidy.say "Haha, fuck off. Seriously, is she seeing anyone?"
            show cassidy normal
            mike.say "Honestly, I have no idea."
    show cassidy talkative
    cassidy.say "But you don't know for sure?"
    show cassidy normal
    mike.say "I guess I'm not with her every minute. Why?"
    show cassidy talkative
    cassidy.say "It's just...it's something I overheard. It's probably nothing."
    show cassidy normal
    mike.say "Tell me."
    show cassidy talkative
    cassidy.say "Let me find out if it's real first, okay?"
    show cassidy normal
    $ cassidy.flags.dwaynefightDelay = TemporaryFlag(True, 1)
    hide cassidy
    return

label cassidy_overhear_argument:
    "I'm on my way to the break room when I walk by Dwayne's office. Usually the door is closed and locked, because he's never actually here."
    "But today it's open, just a crack, and I can hear raised voices coming from inside the room."
    dwayne.say "I don't understand what's wrong, Cassidy."
    cassidy.say "What's wrong? You're cheating on her!"
    dwayne.say "I thought you'd be happy. You always hated Cherie."
    cassidy.say "Sure, Cherie's a giant bitch but you're supposed to be better than that."
    "The voices drop, and then I hear footsteps. I decide to hightail it away before either of them realize I've overheard that conversation."
    $ hero.cancel_activity()
    $ cassidy.flags.dwaynefalloutDelay = TemporaryFlag(True, 1)
    return

label cassidy_dwayne_fight_fallout:
    if cassidy.status == 'pet':
        $ cassidy.flags.dwaynevisitDelay = TemporaryFlag(True, 7)
    else:
        $ cassidy.flags.alettafightDelay = TemporaryFlag(True, 7)
    show cassidy upset
    "Normally when we're not busy playing, Cassidy hangs around the office, mostly kind of bored, but actually doing something resembling the work she's supposed to be doing."
    "But right now she's sitting in her chair, just glaring at the paperwork in front of her. Not touching it, just glaring."
    mike.say "Hey, Cassidy, are you okay?"
    if cassidy.status == 'pet':
        "Cassidy doesn't answer."
        mike.say "Hey! Earth to Cassidy, are you there?"
        show cassidy whining
        cassidy.say "Oh. Yeah, I'm okay, I guess."
        show cassidy upset
    else:
        show cassidy angry
        cassidy.say "Fuck off, [hero.name]."
        show cassidy upset
        mike.say "I just...I might have overheard something earlier and you seem upset. Do you need someone to talk to?"
        show cassidy angry
        cassidy.say "No."
        show cassidy upset
    if cassidy.love.max < 120:
        $ cassidy.love.max = 120
    menu:
        "Leave her alone":
            "I decide in the mood she's in to just give her some space. Maybe she'll talk about it later, or maybe she won't."
        "Insist":
            mike.say "Hey, Cass..."
            show cassidy annoyed
            cassidy.say "Don't call me that."
            show cassidy upset
            mike.say "What, Cass?"
            show cassidy angry
            cassidy.say "Yeah, that's what...that's what Daddy calls me."
            show cassidy upset
            mike.say "Oh. I can't call you that?"
            show cassidy angry
            cassidy.say "You haven't earned it."
            show cassidy upset
            mike.say "I see. You're right. Cassidy, then. I don't mean to pry or be nosey, but you really seem like you need someone to talk to."
            show cassidy annoyed
            "Cassidy sighs."
            show cassidy whining
            cassidy.say "Fine, if it'll shut you up."
            show cassidy sad
            "She turns and looks at me directly for the first time."
            show cassidy whining
            cassidy.say "I just found out my dad is cheating on my step-mom. I went to confront him about it, and...I don't know what I expected. Maybe him to lie about it, or to be sorry about it, but he's not."
            cassidy.say "He told me he thought I'd be happy."
            show cassidy upset
            mike.say "Why would you be happy?"
            show cassidy angry
            cassidy.say "Because Cherie -- his wife -- is kind of a bitch. She tried to come in and replace my Mom and she was terrible at it. She spends half her time stoned, and the other half making sure her makeup is perfect."
            cassidy.say "And, well, she wasn't {b}my{/b} Mom, you know?"
            show cassidy upset
            mike.say "Yeah. So what happened to your Mom, anyway?"
            show cassidy whining
            cassidy.say "I don't know. She left. Packed up her stuff one day, told me she had to go away, and I never heard from her again."
            cassidy.say "Daddy said it wasn't my fault, but. She never called. She never answered when I called her. Didn't answer my letters."
            cassidy.say "Daddy said she was sick, and she had to. But I always wondered."
            cassidy.say "I think he was cheating on her with Cherie, and that's why she left. But I never understood why she left me too."
            cassidy.say "How could any mother just leave her daughter like that? Even if she was sick!"
            show cassidy cry
            mike.say "I don't know. I wish I knew. Is there any way to find out?"
            cassidy.say "Maybe. I guess I'd have to find her and make her talk to me."
            show cassidy cry
            mike.say "You should do that."
            show cassidy sadsmile
            "Cassidy nods, slowly, then wipes the tears off her cheeks."
            show cassidy talkative
            $ cassidy.love += 5
            cassidy.say "I guess. Yeah, maybe I'll do that. Thanks, [hero.name]."
            show cassidy sadsmile
            mike.say "Let me know what happens."
            show cassidy talkative
            cassidy.say "Sure."
            show cassidy sadsmile
    return

label cassidy_dwayne_visit:
    $ cassidy.flags.alettafightDelay = TemporaryFlag(True, 7)
    play sound door_knock
    "I'm working at my desk when I hear a knock at the door. Without waiting for me to reply, Dwayne opens the door and steps in."
    show dwayne shout with easeinleft
    dwayne.say "[hero.name], I need to speak with you."
    show dwayne normal
    mike.say "Uh, sure Dwayne."
    show dwayne shout
    dwayne.say "Look, [hero.name], I agreed to put Cassidy in this position to train her up in how to do business. I thought that finally she'd come around and she's going to focus on important things."
    show dwayne angry
    dwayne.say "Instead, you're using her as some kind of sex toy, I hear. All while she's yelling at me about my indiscretions."
    if cassidy.flags.collared:
        dwayne.say "For God's sake, you've got her, my daughter, running around in a collar like she's some kind of pet!"
    dwayne.say "I think the way you're treating her is inhuman, and I won't stand for it."
    show dwayne upset
    mike.say "I see. Well, Dwayne, you're missing a couple of really important facts here."
    mike.say "The first one, of course, is that I know exactly what was really going on in that cooked-up investigation you ran a few weeks ago."
    mike.say "And what you may or may not know is that your innocent daughter was trying to get {b}me{/b} to be {b}her{/b} sex toy by blackmailing me into doing favors for her or else you'd fire me."
    mike.say "But more important, I know--and can prove--that you're the one who stole that money, Dwayne."
    mike.say "So really, you should be thanking her."
    mike.say "Every time I cum into your daughter's mouth, that's one more day that you get to keep this company."
    mike.say "Every time she calls me Master, that's her way of saying how much she loves you."
    mike.say "Frankly, you don't deserve her, what she's doing for you."
    "Dwayne pales as I speak. If my proof weren't rock solid already, the look in his eyes absolutely confirms what I already knew: Dwayne is guilty as sin."
    mike.say "Well, boss, do you have anything to say for yourself?"
    show dwayne shout
    dwayne.say "I should fire you."
    show dwayne upset
    mike.say "Go ahead. Send me packing. I'll sue you for every penny you have. And I'll win. And you know it."
    show dwayne at left with ease
    "He scowls at me, then turns toward the door."
    mike.say "You'd better keep her happy, Dwayne. She's the only thing standing between you and oblivion."
    mike.say "I'd like to think that every time I fuck her, I'm really fucking you."
    if cassidy.sub > 75 and cassidy.love > 100:
        mike.say "But you know what? I think she's coming around to liking it."
    hide dwayne with moveoutleft
    play sound door_slam
    "Dwayne has nothing more to say, apparently. He slams the door on the way out."
    "I'd better watch myself. I have rock solid proof, but he's got gobs of money."
    return

label cassidy_aletta_fight:
    "When I enter my office, I'd normally expect Cassidy to be there. But she's not. Maybe she's just taking a break, I figure."
    "But then I hear muffled voices from Aletta's office, and one of them is Cassidy's. And they sound angry."
    "Given the conversation we had about Aletta a couple weeks ago, it might be prudent for me to intervene. So I steel myself up and go into Aletta's office."
    scene bg alettaoffice
    show cassidy angry at right
    show aletta upset at left
    with fade
    cassidy.say "...be sleeping with a married man!"
    show cassidy upset
    show aletta angry
    aletta.say "Why do you even care?"
    show aletta upset
    show cassidy angry
    cassidy.say "Because he's my father!"
    show cassidy upset
    show aletta angry
    aletta.say "He was barely there for you, Cassidy! In an average week, when you were a teenager, how often did you see him? Twice? Once? Did you even see him at all during the week?"
    show aletta upset
    show cassidy angry
    cassidy.say "Don't try to sidetrack me! This is about you stealing my father from my step-mother!"
    show cassidy upset
    show aletta angry
    aletta.say "I'm not stealing him! She can keep that asshole for all I care."
    show aletta stuned
    show cassidy stuned
    "The two girls finally notice me."
    show aletta surprised
    aletta.say "Oh fuck, [hero.name]. I didn't hear you come in."
    show aletta stuned
    mike.say "Do I need to call a timeout?"
    show cassidy angry
    cassidy.say "You need to keep this bitch away from my Daddy, is what you need to do!"
    show cassidy upset
    mike.say "Whoa, Ca--"
    aletta.say "You don't know what the fuck you're talking about, Cassidy!"
    show aletta upset
    show cassidy angry
    cassidy.say "The fuck I don't! You're fucking my Dad, my Dad's going to divorce my step-mom and it's {b}all your fault{/b}!"
    show aletta whining
    aletta.say "Oh, Cassidy, you really don't know your father at all, do you?"
    aletta.say "I'm not fucking your father because I want to! I'm fucking your father because I don't have a choice."
    if cassidy.status == 'pet':
        aletta.say "I don't have any more choice than you have with [hero.name]."
    else:
        aletta.say "I don't have any more choice than you give [hero.name] here."
    aletta.say "If I don't put out for him, that's it, I'm done here. And he can make sure I never work in the industry again."
    aletta.say "Do you have any idea what it's like?"
    show aletta sad
    show cassidy surprised
    cassidy.say "Seriously? You're saying Daddy is using you as his personal sex toy?"
    show cassidy stuned
    mike.say "Wow. The apple doesn't fall far from the tree, does it, Cassidy?"
    show cassidy angry
    pause 1
    show cassidy sad
    "Cassidy shoots me a look. It's angry at first, but as she thinks about it, she realizes it's absolutely true."
    "She then looks back at Aletta."
    show cassidy angry
    cassidy.say "Why should I believe you?"
    show cassidy upset
    show aletta angry
    aletta.say "Fuck, do you think I'd make something like that up just to get you to stop yelling at me?"
    show aletta upset
    "Aletta turns and looks at me."
    show aletta whining
    aletta.say "[hero.name], does that sound like something I'd do?"
    show aletta sad
    mike.say "None of it sounds like you, Aletta. Bending over for a guy like that?"
    show aletta whining
    aletta.say "Dwayne knows how much I love my job. That's how this all started. I thought...well, at first it was kind of fun. But..."
    show aletta upset
    "She sighs."
    show aletta whining
    aletta.say "Cassidy, I'd dump your father tomorrow if I could. But know that there's no way the divorce is because of me. I'm not the sort he wants to marry. I'm not a young fashion model. I'm too smart to make good wife material for him."
    show aletta sad
    show cassidy angry
    cassidy.say "Did you just call my mother dumb?!"
    show cassidy upset
    show aletta whining
    aletta.say "No! No, that's not what I meant. But they're not..."
    show aletta upset
    "Aletta waves her hand at her office."
    show aletta whining
    aletta.say "...capable of this."
    show aletta upset
    "Cassidy glares at Aletta for a few long, seconds. She doesn't speak, and the tension starts to get really uncomfortable."
    "Then she turns and stomps out of Aletta's office."
    hide cassidy with easeoutright
    show aletta talkative at center with ease
    aletta.say "You'd better go talk to her, [hero.name]. She might do something...not very smart."
    show aletta sadsmile
    mike.say "Yeah."
    scene bg personal
    show cassidy cry
    with fade
    mike.say "Hey, Cassidy. You okay?"
    show cassidy whining
    cassidy.say "Leave me alone, [hero.name]!"
    show cassidy sad
    "I start to say something, but she glares daggers at me, and I decide I'm only liable to make it worse."
    show cassidy whining
    cassidy.say "I'm taking a break for awhile. I'll be back in a couple of days."
    hide cassidy with moveoutleft
    $ cassidy.counters.boredom = None
    $ cassidy.hide()
    $ cassidy.flags.needscomfortDelay = TemporaryFlag(True, 3)
    return

label cassidy_needs_comfort:
    play sound door_bell
    "The doorbell rings unexpectedly. When I answer it, I'm surprised to see Cassidy."
    scene bg house
    show cassidy whining
    with wiperight
    cassidy.say "Hi, [hero.name]."
    show cassidy sad
    mike.say "Cassidy! I was starting to think maybe you were gone for good. Are you okay?"
    show cassidy whining
    cassidy.say "Yeah, I'm fine. No. I'm not fine. I don't...fuck."
    show cassidy sad
    menu:
        "Comfort her":
            mike.say "You're not okay. Why don't you come in?"
            scene bg livingroom
            show cassidy sad at center, zoomAt (1.25, (650, 850))
            with fade
            "When Cassidy comes in, she wraps her arms around me and gives me a tight hug, burying her face into my shoulder. I put my arms on her back and caress her gently."
            mike.say "Hey, hon. Wow, this is really bad, isn't it."
            show cassidy cry
            "She nods into my shoulder, then sobs."
            mike.say "Okay. Listen, you just let it out, okay? I'm here for you right now."
            "When I say that, the dam bursts and she cries for real. I hold her for a good long time, doing my best to be comforting."
            show cassidy sad
            "Eventually, the sobs start coming less often, and her breathing gets more under control."
            show cassidy whining
            cassidy.say "I found my mom."
            show cassidy sad
            mike.say "Oh. Was it bad?"
            show cassidy whining
            cassidy.say "Yeah. It was terrible."
            show cassidy sad
            mike.say "What happened?"
            show cassidy whining
            cassidy.say "She...Daddy told me she just left, that she was sick and needed help."
            cassidy.say "It wasn't entirely a lie. She was sick, and she did go into rehab. And when she got out, she found out that Daddy was cheating on her."
            cassidy.say "And she got a lawyer, and was going to sue him. And then...I didn't really understand this part, but his lawyer did something, and she said she was going to go to jail."
            cassidy.say "And they worked something out so she left. He gave her a lot of money, and made her promise to never speak to me again."
            show cassidy angry
            cassidy.say "And she {b}did it{/b}, that bitch! She took his money and left."
            show cassidy cry
            "With those words, she starts to cry again."
            mike.say "Hey, it sounds like things were pretty bad for her."
            show cassidy whining
            cassidy.say "I asked her if she thought about taking me with her. And you know what she said?"
            show cassidy sad
            mike.say "What's that?"
            show cassidy whining
            cassidy.say "She said she tried, and I didn't want to go! But that's not true! She never tried!"
            show cassidy sad
            mike.say "Are you sure?"
            show cassidy whining
            cassidy.say "What do you mean, am I sure? I'd remember something like that!"
            show cassidy sad
            mike.say "How old were you?"
            show cassidy whining
            cassidy.say "Eleven. Just eleven years old."
            show cassidy sad
            mike.say "Memory is a funny thing. Maybe she tried but she couldn't tell you what was really going on. So she didn't ask you the right questions."
            show cassidy whining
            cassidy.say "No! No way. She didn't...no."
            show cassidy sad
            mike.say "None of that matters, now. Now you know what happened."
            show cassidy whining
            cassidy.say "Yeah, my father is a guy who uses women and throws them away. Like dolls. Or like pets."
            show cassidy sad
            mike.say "What are you going to do?"
            show cassidy whining
            cassidy.say "I don't know."
            show cassidy sad
            if cassidy.status == 'pet':
                mike.say "I can destroy him, you know. You're the only thing stopping me from doing that. All you have to do is say the word."
                "She looks up at me with big, red-rimmed eyes."
                show cassidy whining
                cassidy.say "I need to think about it."
                show cassidy sad
                mike.say "Okay."
            else:
                mike.say "We need to do something about him."
                show cassidy whining
                cassidy.say "I guess. What do we do, though?"
                show cassidy sad
                mike.say "I don't know, yet. Let's think about it, and see what we can come up with."
                show cassidy whining
                cassidy.say "Okay."
                show cassidy sad
            mike.say "And I think maybe you should talk with Aletta. She's hurting too. Maybe that would help?"
            show cassidy angry
            cassidy.say "That bitch!"
            show cassidy upset
            mike.say "Is she, though? If she's a bitch, it's only because she's {b}his{/b} bitch. And you know what? That's killing her."
            show cassidy angry
            cassidy.say "Fuck. You're right."
            hide cassidy
            show cassidy kiss
            with fade
            $ cassidy.flags.kiss += 1
            "Cassidy turns her face up and gives me a long, passionate kiss. This one isn't our usual dom-sub thing, but it's almost like we're equals, maybe even loving partners."
            "Maybe it's just because she's so distraught right now, but this is seriously the closest to her I've ever felt."
            hide cassidy
            show cassidy talkative at center, zoomAt (1.25, (650, 850))
            with fade
            cassidy.say "I'm going to go check on some things. I'll see you at the office?"
            show cassidy normal
            mike.say "So you're coming back?"
            show cassidy talkative
            cassidy.say "Yeah. I'm coming back."
            show cassidy happy
            if cassidy.love.max < 160:
                $ cassidy.love.max = 160
            $ cassidy.unhide()
            $ cassidy.love += 5
            $ cassidy.flags.makeniceDelay = TemporaryFlag(True, 1)
            if game.hour >= 19:
                "For the first time tonight, she smiles, albeit weakly. And then she grabs my butt before running out through the front door."
            elif game.hour >= 12:
                "For the first time this afternoon, she smiles, albeit weakly. And then she grabs my butt before running out through the front door."
            else:
                "For the first time today, she smiles, albeit weakly. And then she grabs my butt before running out through the front door."
            hide cassidy
            mike.say "Cheeky."
        "Get rid of her":
            mike.say "Cassidy, what are you doing? I don't think this is what our relationship really is."
            show cassidy whining
            cassidy.say "I know, it's just...I don't have anyone else to talk to."
            show cassidy sad
            mike.say "Maybe if you didn't try to turn every guy you like into your personal fucktoy you'd have more friends."
            show cassidy whining
            if cassidy.status == 'pet':
                cassidy.say "Yes, you've very effectively taught me that lesson already, {b}Master{/b}."
            else:
                cassidy.say "I guess you're right."
            show cassidy sad
            mike.say "Look, I'm sorry you're fighting with your father, but given who he is and who I am, I feel I shouldn't be involved in that."
            show cassidy whining
            cassidy.say "Fine."
            $ cassidy.set_gone_forever()
    return

label cassidy_aletta_make_nice:
    show aletta upset at left
    show cassidy upset at right
    with fade
    "I look up from my desk, and Aletta and Cassidy are both standing there together. They both look very angry."
    show aletta angry
    aletta.say "Cassidy came to me early this morning, and we had a long talk."
    aletta.say "I need to get out from under Dwayne's thumb."
    if cassidy.status == 'pet':
        aletta.say "And you have the means to make that happen."
        show aletta upset
    else:
        aletta.say "And so do you."
        show aletta upset
        mike.say "For my part, Cassidy is the one holding the cards there. That's why we're in this...arrangement."
    show cassidy angry
    cassidy.say "The more I find out about what he's done, the more I need to be free from him."
    show cassidy upset
    if cassidy.status == 'pet':
        mike.say "What if I don't want to let you go, Cassidy?"
        show cassidy angry
        cassidy.say "Well, what's holding me to you is Dwayne, and I want Dwayne to suffer. I don't see how you could stop that."
        show cassidy upset
        if cassidy.love > 120 and cassidy.sub > 75:
            show cassidy angry
            cassidy.say "But this hasn't been all bad. Maybe when this is over, I'll listen to your pitch about why I should stay with you."
            show cassidy upset
            if aletta.sexperience > 2 and aletta.love > 120:
                show aletta upset
                "Aletta glares at Cassidy, obviously jealous."
    else:
        mike.say "You're willing to let me go?"
        show cassidy angry
        cassidy.say "When this is over, I won't have your job as leverage, it's true. But...well, we'll talk when it's done, okay?"
        show cassidy upset
        if aletta.sexperience > 2 and aletta.love > 120:
            show aletta angry
            aletta.say "We might have to have words about that too."
            show aletta upset
    mike.say "Okay, Aletta. What's your plan?"
    show aletta talkative
    aletta.say "It's pretty simple. I go to the board of directors with everything you and Cassidy both have."
    show aletta normal
    show cassidy annoyed
    cassidy.say "I don't think that will be enough. Just getting him in trouble with the board might cost him his position here, but...I think we need him in jail."
    show cassidy upset
    show aletta surprised
    aletta.say "Really?"
    show aletta stuned
    show cassidy whining
    cassidy.say "Yeah. He's got politicians in his pocket, he's got expensive lawyers, and he'll get revenge. If you want this to work, you need enough to put him in jail."
    show cassidy sad
    show aletta sadsmile
    mike.say "We might have enough for that."
    show cassidy talkative
    cassidy.say "Maybe, but it's a big risk. But I think I know how to get what we need. He has a safe in his office, and he keeps a lot of dirty secrets in that safe."
    cassidy.say "I'm not sure what's really in there, but he's said he can blackmail a lot of people with it."
    show cassidy normal
    mike.say "Huh. Okay. How do we get into a safe?"
    show aletta whining
    aletta.say "That's out of my wheelhouse. I don't know anything about breaking into safes."
    show aletta sadsmile
    show cassidy talkative
    cassidy.say "Cherie can get into it."
    show cassidy normal
    mike.say "Your step-mom."
    show cassidy whining
    cassidy.say "Yeah. But I don't think she'll do it for me. She doesn't trust me."
    show cassidy talkative
    cassidy.say "You'll have to talk her into it, [hero.name]."
    show cassidy normal
    mike.say "I don't even know her!"
    show cassidy talkative
    cassidy.say "We can set something up. You can use your charms. You do have charms, right?"
    if hero.charm < 75:
        show aletta talkative
        aletta.say "He might have to work on that."
        show aletta normal
        "I ignore Aletta."
    mike.say "Okay, so let me get all this right. I need to meet Cherie, charm her, and get her to get me into Dwayne's private safe, so I can look at his secrets and see if there's enough to bring him down?"
    show cassidy talkative
    cassidy.say "That's about it."
    show cassidy normal
    mike.say "I'm not sure I should be doing this..."
    show aletta talkative
    aletta.say "[hero.name], God help me, you're going to do this or I'll shoot you myself."
    show aletta normal
    mike.say "Your argument is compelling."
    show cassidy happy
    cassidy.say "Great. I'll figure out how to set something up with Cherie. It might take a little while."
    show cassidy normal
    mike.say "And until then?"
    show aletta whining
    aletta.say "Status quo, sadly. Until we can take him down completely, I'm still his bitch."
    show aletta sad
    if cassidy.status == 'mistress':
        show cassidy talkative
        cassidy.say "And you're still mine."
        show cassidy normal
    else:
        show aletta talkative
        aletta.say "And she's still yours."
        show aletta normal
    mike.say "Okay then."
    $ hero.cancel_activity()
    $ cassidy.flags.arrangepartyDelay = TemporaryFlag(True, 7)
    return

label cassidy_arrange_party:
    show cassidy talkative
    cassidy.say "Hey [hero.name], I got a way to get you to Cherie. There's a small event at the house and I got you an invitation. Daddy might be there, though, so you may have to deal with him, but I'll distract him."
    show cassidy normal
    if cassidy.status == 'pet':
        mike.say "Distract him, how?"
        show cassidy talkative
        cassidy.say "I'm a hot girl, you figure it out."
        show cassidy normal
        mike.say "But you're his daughter?"
        show cassidy talkative
        cassidy.say "Trust me, that doesn't make a difference."
        show cassidy normal
        mike.say "Ew!"
        show cassidy talkative
        cassidy.say "Oh, it's not that bad!"
        show cassidy normal
        "This conversation is making me uncomfortable. Time to change the subject."
        mike.say "He's already pretty suspicious of me. He came by to have a talk about how I'm treating you, and how he doesn't like it."
        show cassidy happy
        cassidy.say "Aw, is he being protective of his little girl?"
        show cassidy normal
        mike.say "Oh yes. I told him what would happen if he tried anything, though."
        show cassidy talkative
        if cassidy.love < 120:
            cassidy.say "Well, that means you should treat me better."
            show cassidy normal
            menu:
                "You're right":
                    mike.say "You're right, but not because of him."
                    $ cassidy.love += 3
                "You deserve it":
                    mike.say "You deserve every bit of how I treat you."
                    $ cassidy.love -= 3
                    $ cassidy.sub -= 3
        else:
            show cassidy talkative
            cassidy.say "Typical. He doesn't care what I want, only what he wants."
            show cassidy normal
            mike.say "So you like being my pet?"
            show cassidy talkative
            if cassidy.love < 80:
                cassidy.say "No."
            elif cassidy.love < 180:
                cassidy.say "Let's just say I don't hate it."
            else:
                cassidy.say "I love you and I love the way you make me feel."
            show cassidy normal
    else:
        mike.say "You'll have to keep him distracted for quite awhile. It is going to take some time to convince Cherie to trust me, I imagine."
        show cassidy talkative
        cassidy.say "I can be very distracting."
        show cassidy normal
        mike.say "Sure, to a guy like me, but he's your father."
        show cassidy talkative
        cassidy.say "Yeah, and as it happens, he's a guy like you."
        show cassidy normal
        mike.say "Whoa, hold up. You're going to flirt with your own father to distract him?"
        show cassidy angry
        cassidy.say "As far as I'm concerned, he's not my father anymore. Just a guy who uses everyone around him. So yeah, I'm going to use him right back."
        show cassidy upset
        mike.say "Be careful. If he actually...does anything with you that could have some serious consequences."
        show cassidy happy
        cassidy.say "Don't worry about me, Sweetie. Do your job, I'll do mine, and we'll nail his ass."
        show cassidy normal
        mike.say "Yeah, just don't let him nail your ass."
        show cassidy talkative
        cassidy.say "What's the matter, [hero.name], you turned on by the idea?"
        show cassidy normal
        mike.say "Whoa, look, you may have me by the balls but I don't think it's going to work like that with Dwayne the CEO."
        show cassidy talkative
        cassidy.say "So you don't think it'd be fun to have a threesome?"
        show cassidy normal
        mike.say "With your father?!?!"
        show cassidy talkative
        cassidy.say "What, you'd rather have Aletta?"
        show cassidy normal
        mike.say "Hey hey hey now, let's stay on plan. You're getting delusional."
        show cassidy happy
        cassidy.say "You're so much fun to tease."
        show cassidy normal
        mike.say "Ugh."

    mike.say "Okay, so when's the party?"
    show cassidy talkative
    cassidy.say "Next Saturday night. It's not very big, but these days Cherie will find the quietest corner she can, after she holds court."
    cassidy.say "She can't leave until all the guests are gone. So once most everyone has settled in, and she's given everyone a few minutes of face time, that's when you need to grab her."
    cassidy.say "Be charming, but not overbearing."
    if hero.fitness > 80:
        cassidy.say "You're cute, so you've got that in your favor."
    elif hero.charm > 80:
        cassidy.say "You're pretty good with the pickup lines, so work that. She's lonely and she loves the attention, so as long as you don't scare her off you should have no problem."
    elif hero.knowledge > 80:
        cassidy.say "Your best attribute is your smarts, which honestly won't help you much with her. She likes money, sexy guys and her liquor."
    else:
        cassidy.say "Look, I'm going to be honest with you, you really need to work on your charm before you go. You should practice."
    cassidy.say "So get her drunk and flatter her. If you have to seduce her, just...don't tell me about it, okay?"
    show cassidy normal
    mike.say "Wait, you want me to fuck her?"
    show cassidy annoyed
    "Cassidy makes a disgusted face."
    if cassidy.love > 160:
        cassidy.say "No, I don't {b}want{/b} you to fuck her, but if you have to to get her loose, then do what you need to do. I just prefer not to think about that, okay? She's my step-mom after all."
    else:
        cassidy.say "I don't really care who you fuck, I just don't want to think about my step-mom having sex."
    cassidy.say "And I heard enough of that when I was a teen."
    show cassidy sad
    mike.say "Oh really?"
    show cassidy whining
    cassidy.say "Yeah. She's...uh, loud when she's excited, and my bedroom was next door."
    show cassidy sad
    "Cassidy shifts uncomfortably, but it's not exactly revulsion."
    mike.say "Wait, did you actually...listen to them?"
    show cassidy surprised blush
    cassidy.say "No!"
    show cassidy sadsmile
    mike.say "Yes you did!"
    show cassidy normal
    "Cassidy crosses her arms across her chest."
    show cassidy talkative
    cassidy.say "So what if I did? I was fourteen, okay? I'd just started figuring out about sex, and Daddy still fucked her like twice a day when he was home. Yeah, it was hot, okay?"
    show cassidy stuned
    mike.say "Did you masturbate?"
    "She already looked embarrassed, but that question turned her furious blushing into overdrive."
    show cassidy angry
    cassidy.say "Not your business!"
    show cassidy upset
    mike.say "Did you actually want to be Cherie?!"
    show cassidy surprised
    cassidy.say "I was fourteen!"
    show cassidy upset
    mike.say "You're looking forward to this aren't you?"
    show cassidy talkative
    if cassidy.love > 180:
        cassidy.say "No, you're the one I want, now."
    else:
        cassidy.say "Look, if I can ruin him {b}and{/b} get him to fuck his only daughter that's just delicious irony."
        show cassidy normal
        menu:
            "Please don't do that":
                mike.say "Seriously, Cassidy, that's messed up. I get you having a crush on him when you were fourteen, but you're past that now. You're hot, you can have any guy you want. You already have me. Please don't do that."
                $ cassidy.love += 5
                show cassidy talkative
                cassidy.say "I'll think about it."
            "That's hot! I want pictures":
                mike.say "If you do that, I want pictures. If you get him to tie you up we can claim he raped you. Plus it's hot."
                $ cassidy.sub += 5
                show cassidy talkative
                cassidy.say "I had no idea you were turned on by the idea of me fucking other guys."
                show cassidy normal
                mike.say "Just him."
            "No, you belong to me" if cassidy.status == 'pet':
                mike.say "No way, you're mine. Nobody else touches you."
                show cassidy talkative
                cassidy.say "Not even a little revenge porn?"
                show cassidy normal
                mike.say "Not even that."
                if cassidy.love > 180:
                    show cassidy talkative
                    cassidy.say "As you wish, Master."
                else:
                    "Cassidy folds her arms in front of her and looks at me crossly."
                    show cassidy talkative
                    cassidy.say "Don't be possessive. Look, I know we have this arrangement, but I'm going to do what's necessary. Besides, if this succeeds you won't have anything to hold over me anyway."
                    show cassidy normal
                    menu:
                        "I care about you":
                            mike.say "Cassidy, this isn't me being possessive. I care about you, and I don't want to see you hurt."
                            $ cassidy.love += 5
                            show cassidy talkative
                            cassidy.say "You need to do a better job showing me you care, then."
                        "Until then, you're my property":
                            mike.say "And until that happens, you're my property and you'll remember that your body belongs to me. And I won't have {b}Dwayne{/b} touching your pussy. It's mine."
                            $ cassidy.sub += 5
                            show cassidy talkative
                            cassidy.say "What if it was both of you?"
                            show cassidy normal
                            mike.say "I might be up for a threesome with you but not with him."
                            if cassidy.sub > 80:
                                show cassidy talkative
                                cassidy.say "No? I'd make a good love slave. I could suck you while he fucks me, or fuck you while I take his cock down my throat. Or would you rather his cock in my ass while you take my pussy?"
                                show cassidy normal
                                menu:
                                    "Gross!":
                                        mike.say "He's your {b}father{/b}! No!"
                                        $ cassidy.love += 5
                                    "Okay, that's hot":
                                        mike.say "Okay, that {b}is{/b} hot, but...just not so sure I'm thrilled with your daddy's dick in your cunt."
                                        show cassidy talkative
                                        cassidy.say "Well it's sure turned me on."
                                        show cassidy normal
                                        mike.say "If that's something you want, we'll discuss it, okay?"
            "As you wish, but..." if cassidy.status == 'mistress':
                mike.say "As you wish, my mistress, but...if this is just you needing more dick in your life, that's my job, right?"
                $ cassidy.love += 5
                $ cassidy.sub -= 5
                show cassidy talkative
                cassidy.say "And I do like your dick."
                show cassidy normal
                mike.say "Then please take mine instead of his?"
                show cassidy talkative
                cassidy.say "How about both?"
                show cassidy normal
                menu:
                    "Gross!":
                        mike.say "But he's your {b}father{/b}!"
                        show cassidy talkative
                        cassidy.say "So it'd be okay with someone else?"
                        show cassidy normal
                        mike.say "I guess?"
                    "I live to serve":
                        mike.say "If that's what you want, I'm here to serve."
                        $ cassidy.love += 5
                        $ cassidy.sub -= 5
                        show cassidy talkative
                        cassidy.say "Oh,well, I'll have to see what I can arrange then!"
                        show cassidy normal
                        mike.say "Someone else, though? He's...not really going to be good for us, you know?"
                        show cassidy talkative
                        cassidy.say "But it's so...no, you're right."
    show cassidy normal
    mike.say "Okay, so anyway, Saturday night. I'll get ready."
    $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), LabelAppointment(18, [], "Dwayne's Mansion Party", "cherie_first_meeting_appointment", "cherie_first_meeting_appointment_missed"))
    return

label cassidy_cherie_next_steps:
    show cassidy talkative
    cassidy.say "How did your meeting with Cherie go? She had...an interesting look on her face when she left."
    show cassidy normal
    mike.say "It could have gone better."
    show cassidy talkative
    cassidy.say "Did you get anything?"
    show cassidy normal
    mike.say "Just something about destroyed souls. Seems like your Daddy is pretty hard on people who flirt with his wife."
    show cassidy talkative
    cassidy.say "Oh yeah, a few years back she had an affair with the pool guy. I know, that sounds like something out of a bad porno. With that accent he looked and sounded like something out of a porno, too."
    cassidy.say "Anyway after I told him about it, we never saw the pool guy again. Cherie didn't talk to me for like 3 months after that."
    show cassidy normal
    mike.say "Holy shit, what did Dwayne do to the guy?"
    show cassidy talkative
    cassidy.say "I don't know for sure but I think he got deported."
    show cassidy normal
    mike.say "That seems overly cruel."
    show cassidy talkative
    cassidy.say "Seemed right at the time. She was cheating on him!"
    show cassidy normal
    mike.say "Cheating seems to be a family trait."
    show cassidy angry
    cassidy.say "Hey! I've never cheated on you!"
    show cassidy upset
    mike.say "Honestly, I'm surprised!"
    if cassidy.love > 120:
        show cassidy whining
        cassidy.say "Is that really how you see me?"
        show cassidy sad
        mike.say "I guess when we started. But...you've changed a bit since then."
        $ cassidy.love += 2
    else:
        if cassidy.status == 'pet':
            show cassidy talkative
            cassidy.say "I guess the way you've treated me, I'm kind of surprised, myself, I haven't."
            show cassidy normal
        else:
            show cassidy talkative
            cassidy.say "I guess I haven't quite gotten bored of you yet. But you're not making it easy."
            show cassidy normal
    mike.say "Anyway, what next?"
    show cassidy talkative
    cassidy.say "I guess you've got to try again. I saw the way she looked at you. You should call her."
    show cassidy normal
    mike.say "I don't have her number."
    show cassidy talkative
    cassidy.say "Hmm. You could drop by. Just make sure to do it when Daddy is out."
    show cassidy normal
    mike.say "Simple as that? Drop by that giant mansion, unannounced?"
    show cassidy talkative
    cassidy.say "Got any better ideas?"
    show cassidy normal
    mike.say "No."
    show cassidy talkative
    cassidy.say "I'd say do it in the early afternoon on a weekday. He'll always be out. She'll probably not be too drunk yet."
    show cassidy normal
    mike.say "Yet?"
    show cassidy talkative
    cassidy.say "Unless there's some event she has to be presentable for, she'll get started pretty early and be slobberingly drunk before dinner time."
    show cassidy normal
    mike.say "Yikes."
    show cassidy whining
    cassidy.say "Honestly it's one of the many reasons I always hated her. But now that I think on that, she didn't do that at first. That only came later."
    show cassidy sad
    "Cassidy sighs and looks away from me, uncomfortable."
    show cassidy whining
    cassidy.say "But she probably started drinking so much when Daddy stopped having sex with her and...I know it sounds shitty but I was so happy when that happened."
    show cassidy sad
    mike.say "Why?"
    show cassidy whining
    cassidy.say "I thought she was a bitch and she didn't deserve him. I guess it turned out the other way around."
    show cassidy sad
    mike.say "Sounds like you have some apologizing to do."
    show cassidy whining blush
    cassidy.say "Yeah. If she'll even listen."
    show cassidy sad
    mike.say "You won't know if you don't try."
    show cassidy whining
    cassidy.say "Sure, sure. Look let's stay on plan. Once this is all over, well, we'll see if she'll listen to me. This will make her life better too, hopefully."
    show cassidy sad
    mike.say "Okay."
    show cassidy whining
    cassidy.say "If it's okay, I need to be alone for a bit."
    show cassidy sad
    mike.say "Sure."
    hide cassidy
    return

label cassidy_cherie_missed_party:
    show cassidy angry
    cassidy.say "You useless son of a bitch!!"
    mike.say "What? What are you talking about?"
    cassidy.say "You didn't go to the party!! Why the fuck didn't you go?"
    menu:
        "I forgot":
            mike.say "I'm sorry, I forgot!"
            cassidy.say "{b}You forgot? YOU FORGOT?!?{/b}"
        "I got held up":
            mike.say "I'm sorry, I got held up."
            cassidy.say "Oh, so that's it? I'm not important enough for you?"
        "Make up a reason":
            mike.say "[bree.name] hurt herself trying to cook for everyone, and I had to get her to the hospital. By the time we figured out she was okay, it was too late."
            cassidy.say "You're a shitty liar, [hero.name]!"
    cassidy.say "I can't believe you. Maybe this is just a game to you, but this is my life, and my family! If I can't rely on you, then fuck you and fuck this."
    mike.say "What? What are you saying?"
    cassidy.say "We are through, asshole. I was only sticking around because I thought we had something."
    if cassidy.love >= 120:
        mike.say "But we do have something!"
        cassidy.say "I thought so too, but if I can't rely on you for the important stuff, I can't rely on you at all."
    else:
        mike.say "I...don't know what we had."
    if cassidy.collared:
        "Cassidy unclasps the collar from her neck and throws it onto my desk."
    cassidy.say "I'm leaving the country. Don't call me, don't write me, don't do anything. I don't care what you do. You'll never have to see or hear from me again."
    hide cassidy with moveoutleft
    play sound door_slam
    "Cassidy steps out the door and slams it behind her. The sound echoes through my office with a note of finality."
    $ cassidy.set_gone_forever()
    return

label cassidy_cherie_no_help:
    show cassidy
    mike.say "Cassidy..."
    cassidy.say "Uh oh, I don't like that tone in your voice."
    mike.say "Yeah. Look. I fucked up, I think. Cherie isn't going to help."
    show cassidy annoyed
    cassidy.say "Well, then we're screwed."
    mike.say "There's got to be something else we can do."
    cassidy.say "Yeah. I can go get my Mom and go somewhere that Dwayne will never find us."
    mike.say "What?!"
    cassidy.say "Don't try to follow me, [hero.name]!"
    mike.say "What?!"
    cassidy.say "Yeah, you keep saying what. Good luck with Aletta and Dwayne."
    hide cassidy with moveoutleft
    "Well. Fuck, that went by really fast. I knew she'd be upset, but that upset?"
    $ cassidy.set_gone_forever()
    return

label cassidy_chat_about_cherie:
    show cassidy talkative
    cassidy.say "So, you went to see her?"
    show cassidy normal
    mike.say "I did."
    show cassidy talkative
    cassidy.say "And?"
    show cassidy normal
    "I shrug. I want to say it went well, but truthfully, I don't know if it did go well. Plus I'm flirting with Cherie pretty heavily, and Cassidy isn't going to want to hear that."
    mike.say "It went okay, I guess."
    show cassidy talkative
    cassidy.say "Okay? You guess? That's it?"
    show cassidy normal
    mike.say "Yeah. That's it."
    show cassidy talkative
    cassidy.say "Okay, spill. Give me the details. All the details."
    show cassidy normal
    mike.say "Uh. I don't think I should...that you want to--"
    show cassidy talkative
    cassidy.say "[hero.name], don't make me do something you'll regret."
    show cassidy normal
    "I sigh."
    mike.say "Look, you told me not to tell you about it, before. So which is it?"
    show cassidy talkative
    cassidy.say "You seduced her!!"
    show cassidy normal
    mike.say "No! Well, I flirted with her a lot. I tried. She's...pretty terrified of your father, though. I don't know how successful I was."
    "Now it's Cassidy's turn to sigh."
    show cassidy talkative
    cassidy.say "Look, what exactly did she say?"
    show cassidy normal
    mike.say "We had lunch. The butler eavesdropped on the entire conversation. But she called it a {i}not date{/i} at least twice, and when I asked when I would see her again, she said she'd call me."
    show cassidy talkative
    cassidy.say "She said that? That she'd call you?"
    show cassidy normal
    mike.say "When she is ready."
    "Cassidy nibbles on her lip and looks thoughtful."
    show cassidy talkative
    cassidy.say "That's good."
    show cassidy normal
    mike.say "And what if I have to fuck her to get her to get me into Dwayne's vault?"
    "Cassidy shrugs."
    show cassidy talkative
    if cassidy.status == "mistress":
        cassidy.say "Then you'll be doing what I tell you to do, like our arrangement has always been."
    else:
        cassidy.say "Then you'll have yet another beautiful woman writhing in pleasure beneath you. I don't see what the problem is?"
    show cassidy normal
    mike.say "I don't understand you. You didn't want to think about me and her?"
    show cassidy talkative
    cassidy.say "Yeah, well. And then I told you about my teenage fantasies and I got to thinking."
    show cassidy normal
    mike.say "Thinking what?"
    show cassidy talkative
    if cassidy.love >= 180:
        cassidy.say "That I love you, and I trust you. And you'll do what's right."
    elif cassidy.love >= 120:
        cassidy.say "That you and I will do what we have to to get through this, and when it's all over we'll figure out if it matters that you fucked someone else."
    elif cassidy.love >= 70:
        cassidy.say "It...it doesn't matter."
    else:
        cassidy.say "I don't really care who you fuck, all right? Yeah, she's my step mom and it's kind of weird, but..."
    show cassidy normal
    mike.say "Okay, fine. But there's just one other problem."
    show cassidy whining
    cassidy.say "And that is?"
    show cassidy sad
    mike.say "She doesn't really deserve to get hurt in all this. And if I have to do...that, and it's just to get dirt on her husband, she's probably going to be devastated."
    show cassidy angry
    cassidy.say "Look, she's got a long list of people she's hurt. Maybe she doesn't {b}deserve{/b} to get hurt for this, but she's no more innocent than I am."
    show cassidy upset
    mike.say "Okay."
    show cassidy talkative
    cassidy.say "So we're agreed, then? You're not getting cold feet on me?"
    mike.say "No."
    if cassidy.status == "mistress":
        show cassidy talkative
        cassidy.say "Good. Look, if this works out, I'll think about letting you keep her, when this is all done. If she's amenable, that is."
        cassidy.say "I...kind of like the idea of taking Daddy's trophy from him."
        show cassidy normal
        mike.say "And making her my trophy?"
        show cassidy talkative
        cassidy.say "No, you idiot. {b}My{/b} trophy! You'd fuck her at my pleasure. Get it? Your pleasure for my pleasure."
        cassidy.say "Besides, I know where Dwayne keeps the sex toys."
        cassidy.say "Let's just say in the right drawer there's a collar that says Cherie on it, with two little hearts, and a leash."
        show cassidy normal
        mike.say "You're really twisted, Cassidy. First your dad, now your step mom?"
        show cassidy happy
        "Cassidy laughs."
        cassidy.say "Maybe both?"
        show cassidy normal
        mike.say "Oh fuck no. I'm not going anywhere near Dwayne's cock."
        show cassidy talkative
        cassidy.say "Oh stop, you're turning me on now!"
        show cassidy normal
        mike.say "Ugh!"
    elif cassidy.sub >= 80 and cassidy.love >= 120 and cassidy.lesbian >= 5:
        show cassidy talkative
        cassidy.say "Good. Hey, if this works out, who knows. Maybe you'll have both of us?"
        show cassidy normal
        mike.say "I ... what?!"
        show cassidy talkative
        cassidy.say "I guess I don't have any idea for sure but, I did peek on them a few times. Daddy liked to do kinky things to her, and she definitely liked it."
        show cassidy normal
        mike.say "Like what?"
        show cassidy talkative
        cassidy.say "Let's just say in the right drawer there's a collar that says Cherie on it, with two little hearts, and a leash."
        show cassidy normal
        mike.say "Holy shit. No wonder she doesn't just leave him."
        show cassidy happy
        cassidy.say "Yeah, and wouldn't it be amazing to take {b}that{/b} from him?"
        show cassidy normal
        "I'm momentarily dumbfounded while I imagine it. Sure, Cherie's a bit older, but she's still smokin' hot."
        mike.say "I, uh."
        show cassidy talkative
        cassidy.say "Do you need a moment? Or maybe, should I...help you out down there?"
        show cassidy normal
        mike.say "I, uh."
        "Yeah. I'm at a loss for words."
        show cassidy talkative
        cassidy.say "Well, you know, all you have to do is ask, right?"
        show cassidy normal
    else:
        show cassidy talkative
        cassidy.say "Good. Do what you have to do, and let's get this all over with, okay?"
    mike.say "So anyway, the other thing is that the butler was eavesdropping. So your dad is going to know I'm up to something."
    show cassidy annoyed
    cassidy.say "Yeah, that could be a problem."
    show cassidy sad
    mike.say "What should we do about that?"
    show cassidy whining
    cassidy.say "I don't know, honestly. What can he do? It's not like he's going to come beat you up."
    show cassidy sad
    mike.say "I guess I better go work out a little, then."
    show cassidy whining
    cassidy.say "Good luck with that, he's got arms made of iron."
    show cassidy sadsmile
    mike.say "Yeah."
    show cassidy talkative
    cassidy.say "I don't think he'll do that. He's more likely to hire someone to do that."
    show cassidy sadsmile
    mike.say "That does {b}not{/b} make me feel better."
    show cassidy talkative
    cassidy.say "It'll be fine, Sweetie. Take a breath."
    show cassidy normal
    "Great, now I have to watch my back all the time, not just at work."
    return

label cassidy_chat_about_cherie2:
    show cassidy talkative
    cassidy.say "Hello, [hero.name]!"
    show cassidy normal
    if cassidy.flags.mikeNickname in nickname_master or cassidy.status == "mistress":
        mike.say "Hello, my slave!"
    elif cassidy.status == "mistress":
        mike.say "Hello, Mistress!"
    else:
        mike.say "Hello to you too!"
    show cassidy talkative
    cassidy.say "You seem awfully chipper."
    show cassidy normal
    mike.say "Well, I might have received that call from Cherie, finally. And...I think she's intrigued."
    show cassidy happy
    cassidy.say "Oh! I was starting to worry that this whole plan was going to go straight to nowhere!"
    show cassidy normal
    mike.say "Well, it still could. Once again I'm waiting for her call, but...she was definitely flirting. And...I heard something in her voice."
    show cassidy talkative
    cassidy.say "Oh? Something good?"
    show cassidy normal
    menu:
        "I'm worried this is going to hurt her":
            mike.say "She's been living a hollow shell of a life for a lot of years. She likes having someone pay attention to her."
            mike.say "But...I don't know if that will work out the way she wants."
            show cassidy talkative
            cassidy.say "I understand, but remember, even if it hurts, getting out from under his thumb will be good for her."
            show cassidy normal
            mike.say "She won't see it that way."
            show cassidy talkative
            cassidy.say "Maybe she won't, but if her life is better, even if she hates you, that's still a win for her, right?"
            show cassidy normal
            mike.say "Maybe."
        "She wants me and I want her":
            mike.say "She's sweet, and sexy, and...she pretty clearly wants me. And I kind of want her."
            show cassidy talkative
            if cassidy.love < 100:
                cassidy.say "Good for her, I guess?"
            else:
                cassidy.say "But what about me?"
                mike.say "Yes, what about you? What do you want?"
                if cassidy.love > 160:
                    show cassidy talkative
                    cassidy.say "I think...I think I'm in love with you."
                    show cassidy normal
                    mike.say "Wow."
                    show cassidy talkative
                    cassidy.say "You know I want you to do whatever it takes, but...I don't want to lose you."
                    show cassidy normal
                    mike.say "I see. So you want me to hurt her?"
                    show cassidy talkative
                    if cassidy.lesbian >= 5:
                        cassidy.say "Not really. I just. I don't know what to think, okay? This whole situation is more than I know how to deal with."
                    else:
                        cassidy.say "If you have to. I don't want to see her hurt, but...if it's that or lose you?"
                        mike.say "Can it be both?"
                        show cassidy talkative
                        cassidy.say "I don't know. I can't really think about that right now."
                    show cassidy normal
                cassidy.say "I don't...I don't really know."
                show cassidy normal
                mike.say "Well, you're going to have to figure that out, one way or another, before this is all done."
        "I think I want the both of you" if (cassidy.sub >= 80 and cassidy.love >= 120 and cassidy.lesbian >= 5) or cassidy.status == "mistress":
            mike.say "So she said something on the phone, and I couldn't stop imagining her, in passion."
            mike.say "And you said you knew about some of their sex toys. And I started thinking about you at the same time."
            mike.say "And...that's fucking hot."
            show cassidy talkative
            if cassidy.status == "mistress":
                cassidy.say "So you're thinking I could have both of you? That {b}is{/b} kind of sexy, Sweetie, I have to admit."
            else:
                cassidy.say "And you imaged both of us at your feet?"
            show cassidy normal
            mike.say "Yeah."
            "Cassidy shrugs, though her expression shows she's at least interested."
            show cassidy talkative
            cassidy.say "We will see where this goes."
    cassidy.say "But none of this matters if she doesn't get you into that vault."
    show cassidy normal
    mike.say "I know."
    show cassidy talkative
    cassidy.say "So do what you have to do. For my sake, for your sake. For Aletta and Cherie's sakes too. There's a lot of people you're saving with this."
    show cassidy normal
    mike.say "Yeah. Assuming he doesn't straight up murder me, first."
    show cassidy talkative
    cassidy.say "He wouldn't go that far."
    show cassidy normal
    mike.say "I wouldn't be so sure. He came here a couple days ago and I thought he was going to pound me into the floor."
    show cassidy talkative
    cassidy.say "Well, he is possessive, it's true. But actually kill someone?"
    show cassidy normal
    mike.say "If he figures out what I'm after, yeah. He might."
    show cassidy talkative
    cassidy.say "If he comes after you, he'll have to come through me."
    show cassidy normal
    mike.say "You can't be there twenty-four/seven and not to be mean, but he'd brush you aside like a piece of cardboard."
    show cassidy talkative
    cassidy.say "He wouldn't dare lay a finger on his little girl!"
    show cassidy normal
    "I can only shrug at that."
    mike.say "Let's hope we don't have to find out."
    show cassidy talkative
    cassidy.say "I think I'm going to buy a gun, just in case."
    show cassidy normal
    mike.say "Do you know how to use one of those things?"
    show cassidy talkative
    cassidy.say "Aletta offered to teach me."
    show cassidy normal
    menu:
        "Good idea":
            mike.say "That's a good idea. It might come down to violence."
            $ cassidy.love += 2
            show cassidy talkative
            cassidy.say "Then I'm doing it."
        "Bad idea":
            mike.say "That's a bad idea. If you end up shooting him, you'll be the one in jail, not him."
            $ cassidy.sub += 2
            show cassidy talkative
            cassidy.say "I'll...think about that before I do anything."
    show cassidy normal
    if cassidy.status in ["pet", "sex slave"]:
        mike.say "And now, more waiting. At least you're here. Maybe we can have some fun to relieve the tension."
        show cassidy talkative
        if cassidy.love >= 120:
            cassidy.say "I'm all yours!"
        else:
            cassidy.say "I guess? Maybe if you got me more flowers, first..."
        show cassidy normal
    else:
        show cassidy talkative
        cassidy.say "And now you should get to work."
        show cassidy normal
        mike.say "Yes, Mistress!"
    return

label cassidy_dwayne_denouement:
    $ cassidy.flags.forceLocation = (game.days_played, game.hour, "house")
    scene bg house
    show cassidy normal
    with fade
    "When I arrive at my home, Cassidy is already there."
    "Holy shit, how am I going to tell her what happened?"
    show cassidy surprised
    cassidy.say "Oh my God, [hero.name]! Your face, what happened?!"
    mike.say "I, uh. Dwayne, uh, your father."
    show cassidy angry
    cassidy.say "He did this to you?! I'll fucking kill him!!"
    show cassidy upset
    mike.say "No, no! I mean yes, he did, but, it's...you can't."
    "I realize I'm having a little bit of trouble forming the right words. I think I might be in a little bit of shock."
    show cassidy whining
    cassidy.say "[hero.name], you don't look so good. We'd better get you inside."
    show cassidy sad
    mike.say "Yeah, I, um."
    scene bg house at blur(16), dark, dark with dissolve
    "Without warning, everything goes dark."
    $ game.room = "bedroom1"
    scene bg bedroom1 at blur(8), dark
    show cassidy annoyed at center, blur(8), dark
    with dissolve
    pause 0.5
    scene bg bedroom1
    show cassidy annoyed
    with dissolve
    $ game.pass_time(4, needs=True)
    "When I open my eyes, I'm in my own bed, and Cassidy is looking over me, concern written all over her face."
    mike.say "What happened?"
    show cassidy whining
    cassidy.say "You started spouting gibberish. Nothing like sensible words. I managed to get you to your room here, and you passed out."
    show cassidy sad
    mike.say "Oh."
    show cassidy whining
    cassidy.say "You might have a concussion. You probably need a doctor."
    show cassidy sad
    mike.say "No! No, I can't!"
    show cassidy surprised
    cassidy.say "Why not?"
    show cassidy stuned
    mike.say "I...oh fuck. Cassidy. You have to know."
    show cassidy surprised
    cassidy.say "Know what?"
    show cassidy sad
    mike.say "I, he. Damn. You have to understand, he was about to kill me. I was going to die."
    show cassidy stuned
    "Cassidy's expression goes from concerned to confused."
    show cassidy whining
    cassidy.say "From those bruises, it sure looks like he was going to."
    show cassidy sad
    mike.say "He was, he totally was."
    show cassidy whining
    cassidy.say "Then why didn't he?"
    show cassidy sad
    "How do I tell her? I know she's angry with him over what he did, but this...this wasn't in the plans."
    "But I have to. I have to just say the words."
    mike.say "I...he."
    "I take a deep breath."
    mike.say "He's dead, Cass. Aletta shot him before he could kill me."
    show cassidy surprised
    cassidy.say "What?!"
    show cassidy stuned
    mike.say "He was going to pulverize me!"
    show cassidy surprised
    cassidy.say "Are you sure he's...I mean he's been shot before!"
    show cassidy stuned
    mike.say "Yeah. He's dead. For sure. No chance of anything else."
    mike.say "I hope...Oh my God, Cassidy, please don't hate me."
    show cassidy surprised
    cassidy.say "What?"
    show cassidy stuned
    mike.say "I wasn't expecting...he wasn't even supposed to be there."
    show cassidy whining
    cassidy.say "Okay."
    show cassidy sad
    mike.say "You're taking this...better than I expected."
    show cassidy whining
    cassidy.say "I..."
    show cassidy sad
    "Cassidy trails off, without actually forming a sentence."
    "There is a moment of silence between us. I can't tell if Cassidy is thinking about it, or has just stopped thinking altogether."
    show cassidy whining
    cassidy.say "Tell me what happened."
    show cassidy sad
    mike.say "Cherie gave me the book. I had what I needed. Have what I need, actually, I took it."
    show cassidy whining
    cassidy.say "Go on."
    show cassidy sad
    mike.say "And then Dwayne came in. The first thing he did was hit Cherie, and then he promised to kill me."
    show cassidy whining
    cassidy.say "He hit her?"
    show cassidy sad
    mike.say "Knocked her right out. I thought he killed her, at the time."
    show cassidy angry
    cassidy.say "Then what?"
    show cassidy upset
    mike.say "Then he came after me, and...I thought I had a chance. I've trained, but...he's bigger, stronger. Meaner."
    mike.say "I thought I was dead. But Aletta must've suspected something was going to go wrong."
    mike.say "I didn't even know she was there."
    mike.say "And she shot him in the back of the head."
    show cassidy sad
    mike.say "Shot him dead. I can still see the blood. I would've been horrified if I wasn't so relieved to not be dead."
    show cassidy whining
    cassidy.say "Yeah."
    show cassidy sad
    mike.say "When it was done, I woke Cherie up, and we talked a bit. Cherie took the gun and told Aletta and I to go."
    show cassidy whining
    cassidy.say "Why did she do that?"
    show cassidy sad
    mike.say "She's going to tell the police that she shot him after he hit her."
    show cassidy whining
    cassidy.say "That's a big risk for her."
    show cassidy sad
    mike.say "Yeah. It is."
    show cassidy whining
    cassidy.say "And that's it?"
    show cassidy sad
    mike.say "That's it."
    show cassidy whining
    cassidy.say "So now what?"
    show cassidy sad
    mike.say "I guess...it's all over. Unless Cherie goes to jail. Then, I don't know. If she does I think I may have to...I don't know."
    show cassidy whining
    cassidy.say "I can't believe he's..."
    show cassidy cry
    mike.say "Yeah. Me either. It wasn't supposed to go like this."
    "Cassidy starts to cry, but as soon as the first tears roll down her cheeks, she gets ahold of herself and wipes them away."
    show cassidy whining
    cassidy.say "I don't even know how to feel about this. He's my father, but what he did to my mother. And Cherie..."
    show cassidy cry
    mike.say "Yeah."
    show cassidy whining
    cassidy.say "And us. What about us?"
    show cassidy cry
    mike.say "What do you want to do?"
    show cassidy whining
    cassidy.say "I've been thinking about that."
    if cassidy.love >= 150:
        cassidy.say "I love you, [hero.name]. It...I wasn't expecting to. But I do. I love you."
    elif cassidy.love >= 120 and cassidy.status in ["pet", "sex slave"]:
        cassidy.say "Being with you hasn't been as bad as I thought it would be."
    elif cassidy.love >= 120 and cassidy.status == "mistress":
        cassidy.say "Having you as my sex toy has been fun."
    else:
        cassidy.say "Being with you has been...a learning experience for me. But it may be time to move on."
    cassidy.say "What about you?"
    show cassidy sad
    menu cassidy_dwayne_denouement_menu:
        "We should move on from each other":
            mike.say "I think that we should move on from each other."
            show cassidy surprised
            cassidy.say "So. Friends?"
            show cassidy stuned
            mike.say "Yeah."
            if cassidy.love >= 150:
                show cassidy whining
            else:
                show cassidy talkative
            cassidy.say "I see. I guess that's...for the best."
            $ cassidy.breakup()
            cassidy.say "Good luck with...everything, I guess."
            call sleep from _cassidy_dwayne_denouement
            $ game.room = "bedroom1"
            return
        "I want to keep you as my slave" if cassidy.status in ["pet", "sex slave"]:
            mike.say "I like having you as my slave."
            if cassidy.sub < 95 or cassidy.love < 150:
                show cassidy whining
                cassidy.say "But I don't want to be your slave, [hero.name]."
                show cassidy sad
                mike.say "Oh."
                $ cassidy.flags.topless = False
                $ cassidy.flags.bottomless = False
                $ cassidy.flags.naked = False
                $ cassidy.status = "friend"
                jump cassidy_dwayne_denouement_menu
            show cassidy whining
            cassidy.say "I...you want this to be permanent? No blackmail, just me...serving you?"
            show cassidy sadsmile
            mike.say "Yes."
            show cassidy talkative
            cassidy.say "I guess...I guess I don't hate it. And I do love you."
            cassidy.say "So okay. If that's what you really want. As long as...do you love me?"
            show cassidy normal
            mike.say "Yes, my beautiful slave. I love you!"
            $ cassidy.flags.nobreakup = False
        "I want to stay your slave" if cassidy.status == "mistress":
            mike.say "I like being your slave."
            if cassidy.sub > -95 or cassidy.love < 150:
                show cassidy whining
                cassidy.say "But I don't think you really do, [hero.name]."
                show cassidy sad
                mike.say "Oh."
                $ cassidy.flags.topless = False
                $ cassidy.flags.bottomless = False
                $ cassidy.flags.naked = False
                $ cassidy.status = "friend"
                jump cassidy_dwayne_denouement_menu
            else:
                show cassidy talkative
                cassidy.say "Good. I like our relationship. I'm glad you do too."
                cassidy.say "And I'll make sure to take good care of you, my love."
                cassidy.say "Now tell me you love me!"
                mike.say "I love you, Mistress!"
                show cassidy normal
        "You should be my girlfriend" if cassidy.status != "girlfriend":
            mike.say "We don't need this master/slave, business. But I want to stay with you. Be my girlfriend."
            show cassidy talkative
            cassidy.say "Your girlfriend, hmm?"
            show cassidy normal
            "Cassidy puts one hand on my chest."
            if cassidy.love >= 150:
                show cassidy talkative
                cassidy.say "I love you. Of course I'll be your girlfriend!"
            elif cassidy.love > 120:
                show cassidy talkative
                cassidy.say "It has been quite a ride. Maybe without being your plaything, I'll see you differently."
            else:
                show cassidy whining
                cassidy.say "I...no. I don't think I feel that way about you."
                jump cassidy_dwayne_denouement_menu
            $ cassidy.flags.nobreakup = False
            $ cassidy.set_girlfriend()
        "I want you to stay my girlfriend" if cassidy.status == "girlfriend":
            mike.say "Despite all that has happened, I still care for you, and want you to stay with me"
            show cassidy happy
            cassidy.say "Of course I'll stay with you!"
            cassidy.say "I love you [hero.name]."
            show cassidy kiss with fade
            $ cassidy.flags.kiss += 1
            $ cassidy.flags.nobreakup = False
    if cassidy.love.max < 200:
        $ cassidy.love.max = 200
    show cassidy happy
    cassidy.say "So that just leaves one question."
    show cassidy normal
    mike.say "What's that?"
    show cassidy talkative
    if aletta.love > 120 or aletta.sexperience > 1:
        cassidy.say "What about you and Aletta? And you and Cherie for that matter?"
    else:
        cassidy.say "What about you and Cherie?"
    show cassidy normal
    mike.say "What about her?"
    show cassidy talkative
    if cassidy.status == "mistress":
        cassidy.say "Well, if I'm going to be your Mistress..."
    elif cassidy.status in ["pet", "sex slave"]:
        cassidy.say "Well, if I'm going to be your slave..."
    else:
        cassidy.say "Well, if I'm going to be your girlfriend..."
    cassidy.say "Then I want to know you'll dedicate yourself to me."
    show cassidy normal
    menu:
        "I won't leave Cherie all alone":
            mike.say "And leave Cherie all alone? You and she both lost someone today. She's going to need support."
            show cassidy talkative
            cassidy.say "Yeah, but...support from your dick?"
            show cassidy normal
            mike.say "Maybe."
            if cassidy.lesbian >= 9 or cassidy.sub == 100:
                show cassidy talkative
                cassidy.say "Well. You're not wrong, she's had a pretty rough go of it. But why you?"
                show cassidy normal
                mike.say "It's our fault, Cassidy."
                show cassidy talkative
                cassidy.say "So?"
                show cassidy normal
                mike.say "She deserves better than what she's gotten."
                show cassidy angry
                cassidy.say "That bitch? She was awful to me from the moment I met her."
                show cassidy upset
                mike.say "Was she, though? To hear her take on it, you were a spoiled princess and she was never good enough to replace your mom."
                show cassidy angry
                cassidy.say "But..."
                show cassidy upset
                mike.say "And I can say with no hesitation that you {b}used to be{/b} a spoiled princess."
                show cassidy whining
                cassidy.say "But..."
                show cassidy sad
                mike.say "Now you have a chance to do better."
                $ cassidy.flags.cherieok = True
                show cassidy talkative
                cassidy.say "Fine. But...just promise you won't hurt me. Or her. Or either of us."
                show cassidy normal
                mike.say "You have my word."
            else:
                show cassidy angry
                cassidy.say "Absolutely not. If you want that, then you can't have me."
                show cassidy upset
                mike.say "But..."
                show cassidy angry
                cassidy.say "{b}No buts{/b}."
                show cassidy upset
                mike.say "Fine."
                show cassidy angry
                cassidy.say "Which is it, then?"
                show cassidy upset
                mike.say "You, of course."
                show cassidy talkative
                cassidy.say "It better be!"
        "But Aletta is special" if aletta.love > 120 or aletta.sexperience > 1:
            mike.say "Aletta is...something special, though. Look at what your father did to her."
            show cassidy talkative
            cassidy.say "I think she got her revenge."
            show cassidy normal
            mike.say "Sure, revenge, but she shot him, Cassidy. To save my life. She's going to need my support."
            show cassidy talkative
            cassidy.say "Fine. Your support. But does she need your {b}dick{/b}?"
            show cassidy normal
            mike.say "Maybe."
            show cassidy normal
            "Cassidy sighs."
            show cassidy talkative
            cassidy.say "But what if I don't want to share?"
            show cassidy normal
            if cassidy.lesbian >= 9 or cassidy.sub == 100:
                if cassidy.status in ["pet", "sex slave"]:
                    mike.say "That's part of being my slave."
                else:
                    mike.say "I know, it's complicated, but. A lot has happened. To all of us."
                $ cassidy.flags.alettaok = True
                show cassidy talkative
                cassidy.say "Fine. But...just promise you won't hurt me. Or her. Or either of us."
                show cassidy normal
                mike.say "You have my word."
            else:
                show cassidy angry
                cassidy.say "Absolutely not. If you want that, then you can't have me."
                show cassidy upset
                mike.say "But..."
                show cassidy angry
                cassidy.say "{b}No buts{/b}."
                show cassidy upset
                mike.say "Fine."
                show cassidy angry
                cassidy.say "Which is it, then?"
                show cassidy upset
                mike.say "You, of course."
                show cassidy talkative
                cassidy.say "It better be!"
        "They both need me too" if aletta.love > 120 or aletta.sexperience > 1:
            mike.say "They both have been through so much. Cherie lost her husband. Aletta shot him, and saved my life."
            mike.say "They're going to need my support."
            show cassidy talkative
            cassidy.say "Yeah, but...support from your dick?"
            show cassidy normal
            mike.say "Maybe."
            "Cassidy sighs."
            show cassidy talkative
            cassidy.say "But what if I don't want to share?"
            show cassidy normal
            if cassidy.lesbian >= 9 or cassidy.sub == 100:
                if cassidy.status in ["pet", "sex slave"]:
                    mike.say "That's part of being my slave."
                else:
                    mike.say "I know, it's complicated, but. A lot has happened. To all of us."
                $ cassidy.flags.cherieok = True
                $ cassidy.flags.alettaok = True
                show cassidy talkative
                cassidy.say "Fine. But...just promise you won't hurt me. Or her. Or either of us."
                show cassidy normal
                mike.say "You have my word."
            else:
                show cassidy angry
                cassidy.say "Absolutely not. If you want that, then you can't have me."
                show cassidy upset
                mike.say "But..."
                show cassidy angry
                cassidy.say "{b}No buts{/b}."
                show cassidy upset
                mike.say "Fine."
                show cassidy angry
                cassidy.say "Which is it, then?"
                show cassidy upset
                mike.say "You, of course."
                show cassidy talkative
                cassidy.say "It better be!"
        "Of course, my love":
            mike.say "Of course. It's just you and me."
            show cassidy talkative
            cassidy.say "I love you so much!"
    show cassidy normal
    mike.say "I think...I think I need to sleep now."
    show cassidy talkative
    cassidy.say "Yeah. You took a pretty sound beating."
    show cassidy normal
    "She squeezes my hand and stands up. I'm asleep before she even gets to the door."
    call sleep from _cassidy_dwayne_denouement2
    $ game.room = "bedroom1"
    return













































































































































































































label cassidy_sub_01:
    cassidy.say "[hero.name]!"
    cassidy.say "There you are..."
    "I turn at the sound of a familiar voice calling my name."
    "Because I can clearly hear that it's a girl doing so."
    show cassidy upset at center, zoomAt(1.25, (640, 880)) with dissolve
    "But my heart sinks as soon I see Cassidy hurrying towards me."
    "Mainly on account of the fact she's got a face like thunder."
    "And she looks like she really means business!"
    mike.say "Erm..."
    mike.say "Hi, Cassidy..."
    mike.say "What a nice surprise - I wasn't expecting to see you today!"
    "Cassidy comes to a halt right in front of me."
    "And she instantly plants one balled fist on her hip."
    "The other hand she uses to jab a finger towards my face."
    "In fact it's so close to my nose that I can't help taking a step backwards."
    "But even as I do so, Cassidy follows, staying right on me."
    show cassidy angry
    cassidy.say "Don't give me that crap, mister..."
    cassidy.say "I know exactly what you've been getting up to behind my back!"
    show cassidy upset
    "Okay, okay...so I was afraid when Cassidy came storming up to me."
    "But now I'm actually starting to sweat as she starts throwing accusations my way."
    "And no, it doesn't help that she's not being specific right now."
    "Because I'm no saint."
    "And you know that I have a couple of skeletons in my closet."
    if not hero.has_item("danny_corpse") or not hero.has_item("dwayne_corpse"):
        "Metaphorically speaking, of course!"
    mike.say "Whoa, whoa, whoa..."
    mike.say "Slow down there, Cassidy."
    mike.say "It might help if you actually told me what you think I've done?"
    "There, you see?"
    "Even under pressure I can keep my cool and think clearly."
    "I'm not just going to start confessing to or denying stuff."
    "Not before I know what I need to confess or deny!"
    "Unfortunately, Cassidy doesn't seem all that impressed."
    show cassidy angry
    cassidy.say "You know very well what I mean, [hero.name]..."
    cassidy.say "I saw you the other day - with that slut of a girl!"
    show cassidy upset
    "Okay, so now I know that Cassidy's accusing me of cheating on her."
    "The problem is that I need more specific information than that."
    "Because I don't want to admit to seeing one other girl on the side only to find she's talking about another!"
    "Oh come on, don't act so surprised."
    "I can have more than two girls on the go at once."
    "You know that I'm a hot prospect that's always in demand!"
    mike.say "Girl, Cassidy?"
    mike.say "What girl?"
    show cassidy angry
    cassidy.say "Don't you play dumb with me..."
    cassidy.say "I saw you with her in the park the other night!"
    cassidy.say "And what's worse, you were..."
    show cassidy annoyed blush
    cassidy.say "You were..."
    show cassidy upset blush at center, traveling(1.5, 0.3, (640, 1040))
    "As Cassidy struggles to get her words out, she starts to lean in closer to me."
    "And it's pretty clear that she doesn't want anyone to overhear what she's about to say."
    "Which is a gift for me, as it means that pretty much figure out exactly what she's talking about."
    mike.say "Oh..."
    mike.say "You mean you saw me doing a little...dog walking?"
    mike.say "Is that it?"
    show cassidy sad
    "The moment the words are out of my mouth, I sense a change in the air."
    "It's like a subtle shifting of balance in the exchange between Cassidy and me."
    "Before now she was the one laying into me, accusing me of something."
    "But now that a taboo subject's been raised, she's caught on the backfoot."
    "And I have the advantage of calling her on the evident embarrassment it's causing her."
    show cassidy annoyed
    cassidy.say "Is..."
    cassidy.say "Is that...what you call it?"
    show cassidy angry
    cassidy.say "[hero.name] - that girl was totally naked!"
    show cassidy upset
    "Cassidy looks around as she says the words."
    "Checking nobody could hear her say them out loud."
    mike.say "That's not strictly true, Cassidy."
    mike.say "If you looked that closely you'd have seen she has a collar on."
    mike.say "How else was she supposed to be attached to the leash?"
    show cassidy sad
    "For a moment it seems like I've got Cassidy totally on the retreat."
    "She's refusing to meet my eye, and struggling to find her words."
    "But then she seems to get back to the core of the matter."
    "And that gives her another boost of confidence."
    show cassidy -blush
    cassidy.say "None of that matters, [hero.name]..."
    show cassidy angry
    cassidy.say "It doesn't change the fact you were out with another girl."
    cassidy.say "A naked girl too!"
    show cassidy upset
    "So it seems that I'm not going to be able to quell Cassidy with the taboo element."
    "And so we're going to have to lock horns over the issue of the other girl instead."
    "So I hold up my hands in a gesture of surrender."
    mike.say "I can't deny it, Cassidy..."
    mike.say "I was with another girl that night."
    show cassidy surprised
    mike.say "But the real question is what does that mean for us?"
    "Oddly, the question seems to throw Cassidy off a little."
    "Almost like it wasn't the thing she was driving for from me."
    "Sensing a chink in her armour, I decide to press the point."
    mike.say "Come on, Cassidy..."
    mike.say "Are you okay with me seeing other girls besides you?"
    mike.say "Or does this relationship have to be exclusive for it to work?"
    mike.say "Hell, does this mean you're ending it?!"
    mike.say "What's the score?"
    show cassidy sad blush
    "Cassidy still looks more than a little flushed."
    "But somehow she finds the will to answer my questions."
    show cassidy b surprised -blush
    cassidy.say "No, no, no..."
    cassidy.say "I'm not mad that you were with another girl."
    show cassidy b annoyed
    cassidy.say "Fucking hell, [hero.name]..."
    cassidy.say "I'm not even mad you were walking her naked on a leash!"
    show cassidy sad
    "I keep the pressure up on Cassidy."
    "Because I'm determined to keep her from changing the subject."
    mike.say "Then what, Cassidy?"
    mike.say "What exactly is the problem here?!?"
    mike.say "Because I'm not getting it!"
    show cassidy a angry
    cassidy.say "The point?!?"
    show cassidy a annoyed blush
    cassidy.say "The point is I'm jealous..."
    show cassidy surprised
    cassidy.say "Jealous it wasn't me!"
    "I can't help smiling as I come to understand what's really going on here."
    "By comparison, Cassidy is standing there with her jaw hanging open."
    "She seriously looks like she's been stunned by the admission."
    "Or at least by the fact she's said it out loud."
    show cassidy upset
    "Cassidy lowers her head as she addresses me now."
    show cassidy normal
    cassidy.say "So..."
    cassidy.say "Will you do it?"
    show cassidy sadsmile
    cassidy.say "Will you walk me...like a...like a dog?"
    "Now I know what she wants, I can give her an honest answer."
    menu:
        "Only because it's you then":
            "I don't even have to think about it."
            show cassidy surprised -blush
            mike.say "Yes, Cassidy..."
            mike.say "Yes, I will!"
            "This is the best of both worlds."
            "I don't see how things could have turned out better for me."
            "Not only have I gotten away with walking another girl, I get to do it to Cassidy too!"
            "And she's delighted at the prospect, clapping her hands together with glee."
            $ cassidy.love += 2
            show cassidy happy
            cassidy.say "Oh...my...god!"
            cassidy.say "This is going to be the craziest thing I've ever done."
            if not cassidy.collared:
                cassidy.say "And I cannot wait to get that collar around my neck!"
                show cassidy normal
                "I nod eagerly, keen to encourage Cassidy all I can."
                mike.say "Me too, Cassidy, me too!"
            $ cassidy.flags.agree_walk_outside = True
        "I won't do that":
            if not hero.flags.isceo and not game.flags.dwaynedead:
                "Had it been any other girl, I'd have said yes in an instant."
                "But Cassidy isn't just any girl, she's my boss's daughter!"
                "Even if she wants this badly, I'm a dead man should he find out."
                "And the very fact Cassidy spotted me the last time is a warning."
                "As it means I've not been nearly as careful as I thought I had."
            show cassidy sad -blush
            mike.say "No way, Cassidy."
            if not game.flags.dwaynedead:
                mike.say "You know I can't risk that."
                show cassidy sadsmile
                cassidy.say "It's because of my dad, isn't it?"
                cassidy.say "I knew you'd say that, so I already figured it all out."
                show cassidy wink
                cassidy.say "I know lots of fancy parks and gardens we can use."
                cassidy.say "Places where nobody would ever see us!"
                "It's pretty fucking tempting."
                "But I stick to my guns, and shake my head."
                show cassidy sad
                mike.say "No, Cassidy..."
                mike.say "My mind's made up."
            show cassidy at center, traveling(1.25, 0.3, (640, 880))
            "Cassidy takes a step backwards."
            $ cassidy.love -= 2
            show cassidy upset
            "And I can see that she has a determined look on her face."
            "She turns to go, getting the last word as she does so."
            cassidy.say "This isn't over, [hero.name]..."
            cassidy.say "And you should know..."
            show cassidy angry
            cassidy.say "I'm used to getting what I want!"
            hide cassidy with easeoutleft
            "With that, Cassidy walks away."
            "Which leaves me alone and pondering what she could mean."
            $ cassidy.flags.agree_walk_outside = False
    return

label cassidy_sub_02a:
    play sound door_knock
    scene expression f"bg {game.room}" with fade
    "As soon as I hear the sound of someone knocking at the door, I hurry into the hallway."
    "I put my eye to the peephole, straining to see who's standing out there on the porch."
    "It's dark outside, but the streetlights provide enough illumination for me to be sure."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show cassidy casual sad at center, zoomAt(1.0, (640, 720))
    with wiperight
    "And the moment I recognise the person out there is Cassidy, I open the door as quickly as I can."
    mike.say "Hey, Cassidy..."
    mike.say "Glad you could make..."
    show cassidy at center, traveling(1.25, 0.3, (640, 880))
    pause 0.3
    hide cassidy with easeoutleft
    mike.say "Oof..." with hpunch
    "I'm trying to greet Cassidy one moment, and the next I'm shoved backwards into the hallway."
    "It's all very confusing as I try to keep myself from falling onto my ass."
    play sound door_slam
    scene bg livingroom
    show cassidy casual sad at center, zoomAt(1.25, (1040, 880))
    with hpunch
    "But then I see Cassidy is in the house and currently engaged in the act of slamming the door."
    "Which means she must have hustled her way past me the moment I opened it."
    mike.say "Erm..."
    mike.say "Just make yourself at home, Cassidy..."
    mike.say "Me casa, su casa...you know?"
    "Cassidy doesn't stop what she's doing or even acknowledge me until she's done locking the door."
    show cassidy upset at center, zoomAt(1.25, (640, 880)) with ease
    "Only then does she turn around and look me in the face."
    show cassidy angry
    cassidy.say "What was that?"
    show cassidy sadsmile
    cassidy.say "Oh...oh yeah..."
    cassidy.say "Hi, [hero.name]…"
    cassidy.say "Sorry, I was just keen to get inside before someone saw me."
    "I haven't forgotten what I agreed to do with Cassidy tonight."
    "And so her nerves are something that I can totally understand."
    mike.say "It's okay, Cassidy..."
    mike.say "There's not going to be anyone to see you out there right now."
    mike.say "And when we're actually going out there later..."
    mike.say "Well, it'll be so dark that everyone else should be in bed."
    "Cassidy nods, like she's trying to find reassurance in my words."
    "But she still looks worried, and I can't really change the subject."
    "So I decide to focus on a different part of it instead."
    "And that's something that begins with pulling out my phone."
    show cassidy surprised
    cassidy.say "What are you doing, [hero.name]?"
    show cassidy blush
    cassidy.say "You don't want to take pictures of me, do you?!?"
    mike.say "No, Cassidy..."
    mike.say "This is just to check the weather report, yeah?"
    mike.say "Oh, and the temperature too."
    mike.say "Kind of essential when you're doing something like this."
    show cassidy normal -blush
    "Cassidy nods at this."
    cassidy.say "It seems warm out there?"
    cassidy.say "At least a pretty mild night."
    show cassidy sadsmile
    "Cassidy seems to be saying all the right things."
    "But she's still looking around all the time."
    "Like she thinks someone's going to jump out at her any moment."
    "And it's then that the thought hits me."
    mike.say "It's okay, Cassidy..."
    mike.say "My housemates are all sleeping right now."
    show cassidy normal
    "Cassidy looks instantly relieved."
    cassidy.say "They are?"
    show cassidy sadsmile blush
    cassidy.say "I mean, I guessed they would be..."
    cassidy.say "But I didn't know if..."
    "I hold up a hand to show Cassidy that it's okay."
    "And she seems to get the idea."
    mike.say "So..."
    mike.say "Now that you know we're alone..."
    mike.say "Shall we get started?"
    show cassidy normal -blush
    "Cassidy nods."
    cassidy.say "So what happens first?"
    mike.say "Well..."
    show cassidy surprised blush
    mike.say "You should probably get naked!"
    "Cassidy looks surprised for a moment."
    "But then she seems to remember what the point of all this is."
    show cassidy normal
    "And she nods, beginning to pull her top over her head."
    "I do the best I can to keep myself busy while Cassidy strips off."
    "Like, I select a leash that I think will work for her."
    "And I go over the route that I have planned in my head a couple of times."
    show cassidy topless with dissolve
    "But I still can't keep from watching Cassidy as she undresses."
    "Part of me can't actually believe she was the one that wanted this."
    "That her jealousy would be so strong as to make her desire it."
    "And I try in vain to make myself feel like I'm just making one of her dreams a reality."
    "But who am I trying to kid?"
    "This is a dream come true for me, as well as for Cassidy!"
    if not hero.flags.isceo and not game.flags.dwaynedead:
        "I'm getting to put a leash on my boss's hot, bratty daughter."
    else:
        "I'm getting to put a leash on my former boss's hot, bratty daughter."
    "And lead her around naked, treating her like a dog."
    "With every new piece of clothing Cassidy removes, I feel my excitement grow."
    show cassidy naked -topless with dissolve
    "Until she's finally naked and standing there before me."
    show cassidy sadsmile blush
    cassidy.say "Okay, [hero.name]…"
    cassidy.say "I'm ready."
    "Trying to control my breathing, I step forwards and hold up the leash."
    "Cassidy takes it from me and turns it over in her hands."
    "I can see that her eyes are wide, as if with wonder."
    cassidy.say "Would you mind?"
    "I nod and take hold of it, attaching it on Cassidy's collar."
    mike.say "There you go, Cassidy..."
    mike.say "How does it feel?"
    cassidy.say "It feels...good!"
    show cassidy happy
    cassidy.say "Yeah, [hero.name]…"
    cassidy.say "It feels good!"
    "I wave a finger in the air at this, shaking my head."
    show cassidy surprised -blush
    mike.say "That's not what you call me, Cassidy..."
    mike.say "Not while you're on that leash."
    "Cassidy looks confused for a moment."
    "But then realisation seems to dawn on her."
    "And she nods her head."
    show cassidy sadsmile blush
    cassidy.say "Yes...master?"
    mike.say "Now there's a good girl!"
    $ cassidy.sub += 2
    show cassidy happy
    "The praise has the desired effect on Cassidy."
    "As I see a smile spreading across her face."
    show cassidy normal
    "And without the need to be told, she begins to crouch down on the floor."
    "I watch as Cassidy gets onto all fours, marvelling at how good she looks."
    "That perfect body, naked save for the collar around her neck."
    "And when she notices me watching her, the smile gets bigger still."
    show cassidy happy
    cassidy.say "Are we ready, master?"
    cassidy.say "Is it time for my walkies?"
    show cassidy normal
    "I blink and shake my head, wondering if it would help to pinch myself."
    "Because part of me still refuses to believe this is really happening."
    mike.say "Yeah, Cassidy..."
    mike.say "It's time for your evening walk."
    show cassidy happy -blush
    "Cassidy nods happily as I give a gentle tug on the leash while opening the door."
    "I'm expecting Cassidy to object as she feels the pull."
    show cassidy normal
    "But instead she leaps to obey, eagerly crawling out and onto the porch."
    "I've tried to be nothing but confident for Cassidy's benefit tonight."
    scene bg house
    show cassidy naked at center, zoomAt(1.25, (640, 880))
    with fade
    "But there's no way I can stop the butterflies in my stomach as I close the door behind us."
    "And that's because I'm always nervous of the dangers of being seen."
    "All I can do is balance them against the thrill of what we're doing."
    "It's my usual method of coping, and it soon begins to pay off."
    "Because by the time we get to the sidewalk, I'm smiling and holding my head up high."
    show new petplay back cassidy leash_cassidy with fade
    "But that doesn't mean my eyes aren't on Cassidy most of the time."
    "The fact I could probably walk the route blindfolded really pays off."
    "As it means that I can spend a lot of time staring down at her as we go."
    "Of course I need to keep my pace slow to compensate for her being on all fours."
    "But Cassidy's enthusiasm seems to be making her go pretty fast too."
    "Though the strangest thing is how much she's obviously enjoying herself."
    "By the time we reach the park, I'm shaking my head in amazement."
    "Because the Cassidy I know can be a bit of a spoiled brat at times."
    "Quite unlike the girl on the end of the leash."
    "The one that seems to be relishing the chance to behave like a dog!"
    "Cassidy's butt wiggles from side to side as she saunters onto the grass."
    "And I'm pretty sure that she's aware of just how closely I'm watching her."
    "Because she looks back over her shoulder a moment later and winks."
    show new petplay walk
    cassidy.say "Master..."
    cassidy.say "Please may I be let off my lead?"
    cassidy.say "I so want to stretch my legs!"
    "Cassidy somehow manages to make her voice at once needy and seductive."
    "So much so that I can't help but give her what she wants."
    "Leaning down, I unclip the leash and then step back."
    mike.say "Okay, girl..."
    show new petplay -leash_cassidy
    mike.say "Off you go."
    mike.say "But not too far now!"
    "Cassidy nods happily, then turns her back to me."
    show new petplay -cassidy
    "And I watch as she hurries off into the deeper grass."
    "She really shouldn't be able to move very gracefully at all."
    "But somehow the sight of her cavorting out there is...quite something!"
    "And I feel like my heart-rate is rising in sympathy with Cassidy's."
    "I know that she's doing this deliberately, showing off for attention."
    "But that doesn't mean I'm going to be able to take my eyes off her."
    "Or that I'll want to for an instant."
    "I keep following Cassidy at a discreet distance."
    "Letting her explore to her heart's content as I keep an eye out."
    "It's only when she comes to a stand of trees that she stops and looks straight at me."
    "Cassidy holds my eye as she leans her head forward, nose touching the nearest tree."
    "For a moment I can't figure out what she's actually doing."
    "But then I realise she's sniffing at the trunk!"
    "And once she seems to be done with that, Cassidy lifts her leg too."
    "I can't help looking away as I hear the tinkling sound of liquid."
    "Maybe that means I've found my limit for this kind of stuff?"
    "Or maybe it's more that I'm embarrassed Cassidy cocked her leg."
    "Because it suggests she doesn't know an essential difference between a dog and an actual bitch!"
    show new petplay cassidy
    "A few seconds later it seems to be over, as Cassidy comes bounding back over to me."
    "I watch as she runs in circles around the spot I'm standing on."
    show new petplay leash_cassidy
    "And when I hook the leash back onto her collar, she seems happier than ever."
    show new petplay back
    "Together we make a slow circuit of the park, taking it at our leisure."
    "All the time we're walking, Cassidy is quieter and appears more content than I've ever seen her before."
    "Every time I give even the slightest tug on the leash, she hurries to obey me too."
    "Almost like she's taking to being a dog better than she does dealing with her normal, human life."
    "I'm starting to think that there might be some deeper philosophical point to all of this."
    "Some way that Cassidy is being able to cast off the things that hold her back in the space of an average day."
    "But then I catch sight of just how good her breasts look as they're swaying beneath her."
    "And suddenly I lose track of where the previous thought was going."
    "Because now all I have on my mind is how boobies go bounce!"
    scene bg street with dissolve
    "Cassidy's still beaming as I turn away from the park and lead us back to the street."
    "In fact she's placid and perfectly behaved all the way back to the house too."
    show bg livingroom
    show cassidy naked at center, zoomAt(1.25, (640, 880))
    with fade
    "So it comes as a minor disappointment to have to slip inside and take off the leash."
    "But I keep my thoughts to myself as Cassidy gets dressed."
    "Because the last thing I want to do is ruin it all by saying something dumb at the end of a perfect night."
    $ cassidy.love += 5
    $ cassidy.flags.walk_outside = True
    return


label cassidy_sub_02b:
    $ DONE["cassidy_sub_02b"] = game.days_played








































    "As usual I have Hanna on a standard leash."
    "But as we're stepping out of the door, I reach for the extendable one too."
    "I just grab the thing on a whim, thinking that she might want to roam more freely than usual."
    "Though I almost drop the thing as Hanna begins to tug impatiently on her leash."
    "Stuffing the second leash into my pocket, I hurry to follow her out the door."
    show new petplay back hanna leash_hanna with fade
    "Once we're in the park, Hanna seems to settle down and begin to enjoy herself."
    "By now she knows the route we take off by heart, and we're totally alone as we walk."
    "All of which means there's nothing to stop me enjoying the sight of her in motion."
    "Sometimes I think that I could do the entire route without once looking ahead of me."
    "Complete the whole circuit whilst just gazing down at Hanna's beautiful ass."
    "In fact the amount of attention I'm paying to it means I'm totally distracted."
    play sound hitting_bushes
    scene bg park with fade
    "And I only snap out of it once I hear an unfamiliar sound up ahead."
    "Based on past experience, we should be alone."
    "But there's always the rare chance of running into someone or something on these walks."
    "Maybe a drunk taking a shortcut home through the park, or even an actual stray dog."
    "Hanna's already retreated until she's crouched at my side."
    "And as I scan our surroundings for the source of the sound, she begins to hide behind me."
    "There's no clear plan agreed between us for moments like this."
    "Just the vague plan to run back to my place if we're close enough to make it."
    "Otherwise it basically comes down to hiding in the bushes to escape detection."
    "And after that, I guess it'd be up to me to defend Hanna's honour."
    "Or try to explain the whole thing to the cops..."
    mike.say "Just stay behind me, Hanna..."
    mike.say "It was probably just fox or something."
    "Female voice" "Arr...ruff!"
    "Female voice" "Ruff, ruff!"
    "That was obviously a human voice mimicking a dog, which is weird enough."
    "Says the guy walking a naked girl on a leash!"
    "But things get stranger still once I see who the voice belongs to."
    show cassidy naked happy at center, zoomAt(1.25, (640, 1080)) with easeinright
    "Because suddenly there's another naked girl, and she's bounding towards us."
    "Well, bounding as well as she can on all fours."
    "It's obviously dark out this late, and there's very little lighting in the park."
    "So it takes until she's almost on top of us for me to realise that I know her."
    mike.say "Cassidy?"
    mike.say "Is...is that really you?!?"
    show cassidy normal
    "Cassidy doesn't answer the question with words."
    "She seems so committed to the act she's putting on that she remains silent."
    show cassidy happy at center, traveling(1.5, 0.3, (640, 1280))
    "But all the same she crawls right up to me and begins to rub herself against my leg."
    "All the time she's whining and whimpering, really trying to sell the idea that she's a dog."
    "I'm totally stunned by what I'm seeing play out before me."
    "That is until I feel Hanna pulling on her leash."
    "A quick glance down at her lets me know that she's just as puzzled as me right now."
    "But I can also tell that she's eyeing Cassidy with more than surprise and suspicion."
    "I know Hanna well enough to be able to tell that she's beginning to get jealous too!"
    menu:
        "Put her on the spare leash":
            "But then I remember which one of us is wearing a collar and leash."
            "And I give Hanna a gentle tug, just to remind her of the fact too."
            mike.say "Settle down, girl..."
            mike.say "It's just a poor, stray little bitch."
            mike.say "And she looks like she could use some friends."
            show cassidy blush
            "Cassidy smiles happily at this, rubbing up against me all the more."
            "For her part, Hanna seems less pleased, but she doesn't protest."
            "So I pull out the extendable lead and clip it onto Cassidy's collar."
            show new petplay walk hanna cassidy leash_hanna leash_cassidy cassidy_collar with fade
            "Then I take a leash in each hand, and continue to walk around the park."
            "Of course this means that Cassidy is instantly in her element."
            "She walks happily on all fours to one side of me the whole time."
            "Hanna seems less pleased at first, holding back and refusing to look at Cassidy."
            "But soon enough she seems to realise that her sulking isn't going to work."
            "And so she slowly lets it drop, beginning to behave herself too."
            show new petplay back
            "So much so that by the time we're on the way back to my place, everything is going well."
            "In fact I'm getting so into the walk that I've totally forgotten that Cassidy turned up out of nowhere."
            "And I'm assuming that she's going to tell me she has her clothes stashed somewhere close by."
            "Because if not, I have absolutely no idea how she's going to get home in her current state!"
            $ cassidy.flags.walk_outside = True
        "Shoo her away":
            "Not wanting to have to deal with Hanna's weapons-grade jealousy, I act quickly."
            "Which means making a serious effort to shoo Cassidy away."
            show cassidy surprised
            mike.say "Get out of here..."
            mike.say "Go on, go away!"
            "Cassidy looks up at me with genuine shock on her face."
            "And it's not hard for me to understand why either."
            "Doing all of this was a massive risk on her part."
            "She must have been hoping that I'd be impressed by her boldness."
            "It's just a shame that things aren't going to play out like that."
            mike.say "You heard me..."
            mike.say "We don't want any strays around here."
            mike.say "So get lost, before I call the dog-warden!"
            show cassidy sad
            "Cassidy seems to be catching onto the fact her efforts aren't paying off."
            "And so she risks one last, pleading look up at me as she turns her body."
            "But I keep the same hard expression on my face, making my feelings plain."
            hide cassidy with moveoutright
            "I have to keep it up until she finally takes the hint and begins to retreat."
            "And it's only when she disappears back into the bushes that I can let it go."
            "Which means letting out a sigh of relief and instantly turning on my heel."
            show new petplay walk hanna leash_hanna with fade
            "I'm so eager to get out of the park that I accidentally yank Hanna's leash harder than usual."
            "She's dragged a little way, but then hurries to keep up with me as we retrace our steps."
            show new petplay back
            "And all the way home I make sure not to stop or look back over my shoulder once."
            "All for fear of seeing Cassidy following us home."
    return

label cassidy_spanking_start:
    "Believe it or not, I'm actually trying to get my head down and do some serious work."
    play sound door_knock
    "That's why I look up and roll my eyes at the sound of a knock on the door of my office."
    "With a sigh I stop what I'm doing, hoping that I can deal with whatever it is quickly."
    mike.say "Okay, okay..."
    mike.say "Come in - but this had better be important!"
    show cassidy annoyed at center, zoomAt (1.1, (340, 800)) with easeinleft
    cassidy.say "Hey!"
    show cassidy sadsmile
    cassidy.say "Don't be mean to me!"
    cassidy.say "That's not nice!"
    show cassidy normal
    "As Cassidy slips into my office, I feel my mood changing."
    "And by the time she's closed the door, annoyance has given way to interest."
    mike.say "Cassidy?"
    mike.say "What are you doing here?!?"
    show cassidy happy at startle
    "Cassidy hears the sudden interest in my voice and giggles."
    show cassidy normal
    cassidy.say "What do you think I'm doing?"
    cassidy.say "I'm sneaking in to see you, silly!"
    "Obviously I'm flattered by this and intrigued at the possibilities."
    "But there's still a part of me that's worried we might get caught."
    mike.say "You have to be quiet, Cassidy."
    mike.say "We could both get in trouble if anyone finds out you're here!"
    cassidy.say "I know, right!"
    show cassidy wink
    cassidy.say "I'm such a bad girl!"
    cassidy.say "I think it was because my daddy never spanked me enough..."
    show cassidy normal at center, traveling (1.5, 1.0, (640, 1040))
    "As if to make her point, Cassidy leans on my desk and shakes her ass."
    "And at the same time she raises her eyebrows in a provocative manner."
    mike.say "Ah...well..."
    mike.say "Maybe we could make up for lost time?"
    "I say this as I push back my chair and get to my feet."
    hide cassidy
    show slap cassidy happy
    with fade
    "Cassidy's ass is pulling me in, drawing me closer like a magnet."
    cassidy.say "Oh, I don't know about that..."
    cassidy.say "You'd have to spank me real hard to make up for all that time!"
    "Cassidy keeps right on shaking her ass as I grab the hem of her skirt."
    show slap cassidy happy
    "And she adds a dirty little chuckle as I lift it up too."
    "Her ass is perfect, round and aching to be touched."
    play sound spank
    show slap cassidy angry slapping
    with hpunch
    "Even so, she's not ready for the first slap."
    show slap cassidy angry -slapping
    cassidy.say "Ooh...ouch!"
    cassidy.say "No fair - I wasn't ready!"
    mike.say "Don't talk back, Cassidy!"
    mike.say "Or else I'll only spank you harder!"
    "Cassidy gasps at my words, turning her head away from me."
    play sound spank
    show slap cassidy angry slapping
    with hpunch
    "I take this as permission to continue, and I slap her buttocks again."
    show slap cassidy happy
    "Cassidy yelps and moans as I paddle her ass with my hand."
    show slap cassidy -slapping
    "But somehow she still manages to blurt out some words along the way."
    cassidy.say "Oh...I'm such a bad girl..."
    cassidy.say "Spank me harder..."
    cassidy.say "I deserve this SO badly..."
    play sound spank
    show slap cassidy slapping
    with hpunch
    pause 0.2
    show slap cassidy -slapping
    pause 0.1
    play sound spank
    show slap cassidy slapping
    with hpunch
    pause 0.2
    show slap cassidy -slapping
    pause 0.1
    play sound spank
    show slap cassidy slapping
    with hpunch
    "I don't stop until my hand is numb and Cassidy's buttocks are red."
    "Then I flop down in my chair, panting and exhausted."
    hide slap cassidy
    show cassidy wink blush at center, zoomAt (1.5, (640, 1040))
    with fade
    show cassidy at center, traveling (1.1, 1.0, (340, 800))
    $ cassidy.sub += 1
    $ cassidy.love += 1
    "Cassidy smiles as she pulls down her skirt and makes for the door."
    cassidy.say "Mmm..."
    cassidy.say "Thanks for that, [hero.name]."
    cassidy.say "My butt's going to be stinging for days!"
    hide cassidy with easeoutleft
    "I smile and watch Cassidy as she slips out of my office."
    "The only problem is that now I have to get my mind back onto work."
    "Which is hard when it's filled with images of Cassidy's pert little ass!"
    return


label cassidy_male_ending:




    if renpy.has_label("cassidy_achievement_3") and not game.flags.cheat:
        call cassidy_achievement_3 from _call_cassidy_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "To say that I'm feeling nervous right now would be a massive understatement."
    "I thought that I was used to wearing a suit and tie thanks to my work life."
    "But the one I have on at the moment feels more like a straight-jacket!"
    "And I don't know if I'm sweating from the tight clothes or the pressure I'm under."
    "On reflection, maybe it's more on account of the fact I'm standing at the altar."
    "That and I'm waiting with baited breath for Cassidy to come walking down the aisle!"
    "Part of me doesn't even believe that this is actually happening."
    "In fact...just let me try pinching myself..."
    "OUCH!"
    "Well, that proves it - I'm not dreaming!"
    "Cassidy and I are really about to tie the knot!"
    "I take a moment to glance around the chapel, trying to occupy myself."
    "Everything looks perfect, just how Cassidy wanted it to be."
    "The decor is just so and even the guests look like they've been hand-picked and styled."
    "But what else would you expect from a girl like Cassidy?"
    "Yeah, know that she's pretty spoilt and used to getting her own way."
    "But when she's the girl that you love more than anything in the world..."
    "Well, let's just say that you kind of like making sure she gets what she wants."
    "Because if she's happy, then you're happy."
    "That's just how love seems to work!"
    "And speaking of love, I hear the music that Cassidy chose to come down the aisle to!"
    "As soon as the sound fills the chapel, everyone in the place seems to hold their breath."
    "I don't know if that's actually what the guests are doing, because I'm not looking at them."
    "Because the only person I have eyes for is the one walking down the aisle right now."
    show cassidy wedding normal blush at center, zoomAt (1.0, (640, 730)) with dissolve
    "Cassidy sweeps into view, looking every inch the princess everyone jokes about her being."
    "But all I can see is the most beautiful girl in the world."
    "And even crazier is the fact that I'm the one that's marrying her!"
    "The dress that she has on looks amazing, just amazing."
    "It complements her figure so well, I guess because it was made for her!"
    if cassidy.is_visibly_pregnant:
        "And if I didn't know she was pregnant, I doubt I'd have spotted it."
    else:
        "And part of me is glad I have no idea how much it cost!"
    show cassidy wedding at center, traveling(1.5, 3.0, (640, 1040))
    "I can't help grinning like a fool as Cassidy reaches the altar."
    show cassidy happy at startle
    "And that earns me a giggle and a shake of the head in return."
    show cassidy talkative
    cassidy.say "Stop grinning, you big dope!"
    cassidy.say "This is supposed to be serious!"
    show cassidy normal
    mike.say "I can't help it, Cassidy."
    mike.say "I feel like the luckiest guy in the world!"
    show cassidy happy at startle
    "Cassidy giggles again."
    "And now she's grinning too."
    show cassidy talkative
    cassidy.say "Well...you kind of are!"
    cassidy.say "So you go ahead and smile, [hero.name]!"
    show cassidy normal
    "Priest" "Ahem..."
    "Priest" "If you two are finished chatting?"
    show cassidy upset
    "At the sound of the priest's voice, I snap back to reality."
    "I feel pretty embarrassed at his having to remind me what's actually happening here."
    "But the same can't be said for Cassidy, who looks him straight in the eye."
    show cassidy angry
    cassidy.say "Excuse me!"
    cassidy.say "But you do remember who's paying for all of this, don't you?"
    cassidy.say "We'll be finished when we're finished okay?"
    show cassidy upset
    "Priest" "Erm...okay?"
    show cassidy happy
    cassidy.say "Good!"
    show cassidy talkative
    cassidy.say "Now we're finished!"
    show cassidy normal
    show wedding cassidy with fade
    "The priest gives me a look before he begins the ceremony."
    "The kind that says 'I hope you know what you're letting yourself in for, buddy!'"
    show wedding cassidy priest with dissolve
    "Priest" "Ah..."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two...people...in the bonds of holy matrimony."
    "Cassidy's words seem to have had the desired effect on the priest."
    "He works his way through the ceremony without pause or hesitation."
    "Before I know it, we're already at the part where we exchange vows."
    "Priest" "Do you, Cassidy, take this man [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    cassidy.say "I do."
    "Priest" "And do you, [hero.name], take this...woman...Cassidy..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "I do."
    "The priest gives me another one of those looks before he goes on."
    "Priest" "I now call on those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these two should not be joined in the bonds of holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause and ripple of nervous laughter from the guests."
    "And I can see Cassidy scanning the chapel with the eyes of a hawk."
    "Woe betide anybody that chooses to open their mouth right now!"
    "Priest" "Very good."
    "Priest" "It is therefore my pleasure to pronounce you husband and wife."
    "Priest" "You probably want to kiss the bride right about now..."
    show wedding cassidy -priest with dissolve
    "I barely have the chance to hear what the priest is saying."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show cassidy kiss wedding
    with fade
    $ cassidy.flags.kiss += 1
    "Because Cassidy pounces on me like a woman possessed."
    "I do the best I can to return the gesture, holding her tight."
    "But she's almost too much for me to handle!"
    "That doesn't worry me though."
    "As we have the rest of our lives together for me to get used to all of that!"
    hide cassidy
    scene cassidy ending
    with fade
    cassidy.say "I always looked up to my father, thought he was best thing in the world."
    "And yeah, I was the cliche daddy's little girl for so long it's crazy."
    cassidy.say "I never thought that there'd be another man in my life that I loved as much as him."
    cassidy.say "Problem is that as I grew up, I started to notice all of those little flaws, you know?"
    cassidy.say "Like why mom was always crying and had drink in her hand."
    cassidy.say "How he was never around too, and throwing money at our problems."
    cassidy.say "Don't get me wrong, presents make it all better when you're a kid."
    cassidy.say "It just doesn't work the same way when you're all grown up."
    cassidy.say "So yeah, I wasn't too high on my dad by the time [hero.name] came along."
    cassidy.say "At first he was just another random guy that worked for my dad."
    cassidy.say "Sure, he was one of the cuter ones."
    cassidy.say "But he was still just another guy."
    cassidy.say "That was until I saw the way my dad was around him."
    cassidy.say "You know that he acted all macho and alpha-male around [hero.name]."
    cassidy.say "But there's little hints, things that he does differently."
    cassidy.say "And he only does them when the other guy threatens him."
    cassidy.say "So that made [hero.name] instantly more interesting."
    cassidy.say "I mean, I MIGHT have started flirting with him to annoy my dad."
    cassidy.say "But that was only at the start."
    cassidy.say "Pretty soon I realised that I actually liked [hero.name] for real!"
    cassidy.say "And things just built from there."
    cassidy.say "I went from girlfriend to fiancee to wife."
    cassidy.say "I mean, it wasn't that fast."
    cassidy.say "But it felt like no time at all."
    cassidy.say "It seemed like our relationship helped [hero.name] out too."
    cassidy.say "He started climbing the corporate ladder almost as soon as we were an item."
    cassidy.say "And I have to admit that it felt good to see him snapping at dad's heels!"
    cassidy.say "But the best thing was the way that he handled what happened to my dad."
    cassidy.say "The way [hero.name] stepped up to the plate and rose to the challenge."
    cassidy.say "It made me so proud of him, and it made me realise how much I loved him too."
    cassidy.say "He was the perfect guy to take over running dad's company."
    cassidy.say "And he's the perfect replacement for him as the man in my life too!"
    if cassidy.is_visibly_pregnant:
        cassidy.say "And we're well on the way to making our lives complete."
        cassidy.say "Especially now that Sophia have come along."
        cassidy.say "He's the best dad in the world to them - far better than mine ever was!"
    else:
        cassidy.say "And we'll soon be in the way to making our lives complete."
        cassidy.say "Because we're going to start a family of our own."
        cassidy.say "I know that he'll be the best dad in the world too - far better than mine ever was!"
    cassidy.say "So things really couldn't have turned out better for me."
    cassidy.say "I got to step out from under my dad's shadow."
    cassidy.say "I got to marry the man of my dreams."
    cassidy.say "And I'm pretty sure my mom loves him too!"
    cassidy.say "Daddy's such a great guy!"
    cassidy.say "Oops...I mean [hero.name]'s such a great guy, obviously!"
    cassidy.say "That was just a little slip of the tongue back there!"
    cassidy.say "Anyway, all that matters is the fact we're together."
    cassidy.say "And we have the rest of our lives ahead of us too."
    cassidy.say "I don't know what the future has in store for us."
    cassidy.say "But I'm sure that it's going to be amazing!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not cassidy.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_7
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_7
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
