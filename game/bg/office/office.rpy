init python:
    Room(**{
    "name": "office",
    "hours": (8, 20),
    "conditions": [
        Or(
            And(
                IsDayOfWeek("123456"),
                IsHour(8, 20),
                HeroTarget(
                    IsGender("female"),
                ),
                Or(
                    PersonTarget("mike",
                        Not(IsHidden()),
                    ),
                    PersonTarget("dwayne",
                        Not(IsHidden()),
                    ),
                ),
            ),
            And(
                Or(
                    IsDayOfWeek("123456"),
                    And(
                        IsDone("aletta_kink_05"),
                        Not(IsDone("aletta_kink_06")),
                    ),
                ),
                Or(
                    IsHour(8, 20),
                    And(
                        IsDone("cherie_event_06"),
                        IsNotDone("cherie_event_07_1"),
                        IsTimeOfDay("evening", "night"),
                    ),
                ),
                Not(IsSpecialDate("christmas")),
                HeroTarget(IsGender("male"),
                    Not(OnDate()),
                ),
            ),
        ),
    ],
    "display_name": "Office",
    "exits": ["map", "personal", "ceo", "alettaoffice", "breakroom"],
    "music": "music/roa_music/fly_high.ogg",
    "outfit": "work",
    "tags": ["work"],
    })

    Activity(**{
    "name": "work",
    "money_gain": {
        "attributes": ["charm", "knowledge"],
        "bonus": ["promoted"],
        },
    "duration": 4,
    "rooms": "office",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("promoted", False),
            IsFlag("suspended", False),
            IsGender("male"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    "label": "work",
    "say": [
        "All work and no play makes [hero.name] a dull boy.",
        ],
    })

    Activity(**{
    "name": "workhard",
    "money_gain": {
        "attributes": ["charm", "knowledge"],
        "bonus": ["promoted"],
        "mult": [1.5],
        },
    "fun": -2,
    "duration": 4,
    "rooms": "office",
    "conditions": [
        HeroTarget(
            MinStat("energy", 4),
            MinStat("hunger", 4),
            MinStat("grooming", 4),
            MinStat("fun", 4),
            IsFlag("promoted", False),
            IsFlag("suspended", False),
            IsGender("male"),
            ),
        ],
    "display_name": "Work hard",
    "label": "workhard",
    "icon": "work_hard",
    "say": [
        "All work and no play makes [hero.name] a dull boy.",
        ],
    })

    Event(**{
    "name": "work_random_events",
    "label": "work_random_events",
    "priority": 0,
    "conditions": [
        HeroTarget(IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        ],
    "chances": 20,
    "do_once": False,
    "once_week": True,
    })

    Event(**{
    "name": "work_promoted",
    "label": "work_promoted",
    "priority": 1000,
    "conditions": [
        HeroTarget(
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinFlag("worksatisfaction", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "work_promoted_2",
    "label": "work_promoted_2",
    "conditions": [
        IsDone("work_promoted"),
        HeroTarget(
            IsRoom("office", "personal", "ceo"),
            MinFlag("worksatisfaction", 100),
            ),
        ],
    "do_once": False,
    })

label work_promoted:
    show aletta happy
    aletta.say "[hero.name], management has decided to give you a promotion."
    mike.say "Thanks, I'm very grateful."
    show aletta talkative
    aletta.say "Don't be, it comes with greater responsibilities and higher expectations."
    aletta.say "Welcome to management, you will have your own office from now on."
    show aletta normal
    $ Room.find("personal").unhide()
    $ game.flags.promoted = 4
    $ game.flags.worksatisfaction = game.flags.worksatisfaction - 50
    hide aletta
    return

label work_promoted_2:
    $ promotion_cap = 15
    if hero.has_skill("work"):
        $ promotion_cap += 5
    if game.flags.promoted < promotion_cap or (hero.flags.isceo and game.flags.promoted < promotion_cap * 2):
        "My salary has been raised!"
        $ game.flags.promoted += 1
        $ game.flags.worksatisfaction = game.flags.worksatisfaction - 100
    elif not game.flags.capped_promotion:
        $ game.flags.capped_promotion = True
        "I've already reached my highest level of incompetence."
        "No more promotions for me in my current job."
    return

label work_random_events:
    $ r = randint(1, 13)
    if r == 1 and Person.is_not_hidden("aletta") and not game.flags.isceo:
        show aletta work normal at left with moveinleft
        "Aletta walks toward me."
        show aletta talkative at center with move
        aletta.say "[hero.name], we have to finish this by tomorrow, I'd like you to stay for a couple more hours."
        aletta.say "Of course, you'll receive a bonus."
        show aletta normal
        menu:
            "Accept":
                mike.say "Okay, no problem boss."
                "I work for two more hours."
                $ game.pass_time(2, needs=True)
                show aletta happy
                aletta.say "Well done [hero.name], we finished just in time!"
                show aletta normal
                $ game.flags.worksatisfaction += 10
                if hero.has_skill("work"):
                    $ game.flags.worksatisfaction += 10
                $ hero.money += 50
            "Refuse":
                mike.say "Sorry boss, I have plans."
        hide aletta with moveoutleft
    elif r == 2 and Person.is_not_hidden("aletta") and not game.flags.isceo:
        show aletta work upset at left with moveinleft
        "Aletta walks toward my desk."
        show aletta angry at center with move
        aletta.say "[hero.name], we have an emergency! We need to fix this bug as soon as possible."
        show aletta talkative
        aletta.say "I'd like you to stay until you solve it."
        aletta.say "Of course, you'll receive a bonus."
        show aletta normal
        if hero.knowledge < 25:
            menu:
                "Accept":
                    mike.say "Okay, no problem."
                    "I work for two more hours."
                    $ game.pass_time(2, needs=True)
                    show aletta happy
                    aletta.say "Well done [hero.name], we finished just in time!"
                    show aletta normal
                    $ game.flags.worksatisfaction += 10
                    if hero.has_skill("work"):
                        $ game.flags.worksatisfaction += 10
                    $ hero.money += 100
                "Refuse":
                    mike.say "Sorry boss, I have plans."
                    $ game.flags.worksatisfaction -= 1
        else:
            mike.say "I already solved it, boss."
            show aletta happy
            aletta.say "Wow, as impressive as ever, [hero.name]!"
            show aletta normal
            $ hero.money += 100
            $ game.flags.worksatisfaction += 20
            if hero.has_skill("work"):
                $ game.flags.worksatisfaction += 20
        hide aletta with easeoutleft
    elif r == 3 and Person.is_not_hidden("audrey"):
        show audrey work sad at right with moveinright
        "Audrey comes to my desk with an apologetic look on her face."
        show audrey whining at center with move
        audrey.say "I messed up big time."
        audrey.say "I erased all the data on this project and can't find the backup, could you help me?"
        show audrey sad
        menu:
            "Accept":
                mike.say "Okay, no problem."
                "I work for 2 hours, trying to clean up Audrey's mess."
                $ game.pass_time(2, needs=True)
                show audrey happy
                audrey.say "Thanks, you're a lifesaver."
                show audrey normal
                $ audrey.love += 1
            "Refuse":
                if audrey.flags.nickname == "toy":
                    mike.say "Sorry little Toy, I don't have time."
                else:
                    mike.say "Sorry Audrey, I don't have time."
        hide audrey with easeoutright
    elif r <= 4:
        "My attention's focused on my computer screen as the phone on the desk rings."
        "I fumble for it and try to hold it to my ear with my shoulder as continue to type."
        mike.say "Hello, [hero.name] here?"
        "Shady guy" "Yeah, this is the IT department - we've got reports that someone's been downloading porn on the desktop in your office."
        "Oh shit, I can already feel my arsehole puckering up in fear!"
        menu:
            "Admit it":
                mike.say "Erm...yeah...that might have been me."
                mike.say "It was an honest mistake...I can explain..."
                "Shady guy" "Hey, man - my job is to deal with the facts, not the shades of grey!"
                "Shady guy" "Look out for it being brought up in your next quarterly review, okay?"
                $ game.flags.worksatisfaction -= 1
            "Deny it":
                mike.say "Geez, I wouldn't know anything about that!"
                "Shady guy" "Really...well, in that case, does anyone else have access to your desktop?"
                if Person.is_not_hidden("shiori"):
                    mike.say "Erm...yeah - a member of my team called Shiori uses it quite a lot."
                    "Shady guy" "Hmm...okay, you should warn her to look out for it being brought up at her next quarterly review, yeah?"
                else:
                    mike.say "Erm...yeah - a member of my team called Audrey uses it quite a lot."
                    "Shady guy" "Hmm...okay, you should warn her to look out for it being brought up at her next quarterly review, yeah?"
                $ game.flags.worksatisfaction -= 2
        mike.say "Yeah...sure."
        "I put the phone down slowly, vowing to myself that I'll never look at porn in the office again."
        "Or at least until I can figure out a means of getting away with it..."
    elif r == 5:
        "It's getting pretty close to lunchtime, and I can already hear my stomach growling in anticipation."
        "But the only problem is that I'm way too busy to leave my desk and go out to grab something to eat."
        "Even worse, I can't see anyone else around right now that'd nip out and pick me up some lunch either."
        "Desperate to find something edible, I hurry over to the break room and start rooting around in the fridge."
        "It's then that I see a pretty nice-looking sandwich jammed in there alongside the milk."
        "Home-made and stuffed with the kind of fillings that I'd never even have in at my house, I'm instantly tempted..."
        menu:
            "Eat the sandwich":
                "There might have been a note pinned to the cellophane the sandwich is wrapped in declaring it someone's property."
                "But I can't see one anywhere on it, or even on the shelf that it's sitting on."
                "Trying to ignore the guilt I'm feeling right now, I grab the sandwich and skulk back to my desk."
                "I eat the whole thing as fast as I can, almost giving myself indigestion in the process."
                $ hero.hunger += 10
                $ game.flags.worksatisfaction -= 1
            "Don't eat the sandwich":
                "I want to eat the thing, really I do."
                "But what happens when its true owner finds out and goes on the hunt for his missing sandwich?"
                "Who's going to look more suspicious than the guy who was ravenous five minutes ago, but swears he's fine right now?"
                "I walk back to my desk, resigning myself as I do so to an afternoon of hunger pangs and a grumbling stomach."
    elif r == 6:
        "I swear that I had no idea that it was about to happen, even as I was waiting for the lift and then stepping into it."
        "Now I'm trapped in here, cheek by jowl with more than a dozen other people that work in the same building as me."
        "I feel like everyone's deliberately pressing against me, that if they just gave me space, I could keep a lid on things."
        "But then, between floors, there's the inevitable sound, like an balloon's drawn out death-rattle."
        "Oh god - why doesn't it end?"
        "And why does it smell like a burning tire?"
        "I honestly haven't eaten Mexican or Indian food in weeks!"
        "People are covering their noses now, muttering and mumbling in disgust."
        menu:
            "Admit it":
                "I don't know why I feel compelled to confess to being the one that dealt it."
                "I just feel like any moment someone will finger me as the culprit anyway."
                mike.say "I...I'm sorry..."
                "I get a round of harsh stares and hard looks as people get out at the next floor."
                "How am I ever going to live this down?!?"
                python:
                    for g in ["aletta", "audrey", "lavish", "shiori"]:
                        if Person.is_not_hidden(g):
                            Person.find(g).love -= 2
            "Keep quiet":
                "It's only a couple of floors until I get out of the lift - I just need to keep quiet."
                "All around me, people are still complaining, some even choking and making retching sounds."
                "I find myself joining in, perhaps with a little too much enthusiasm, in the hope of looking innocent."
                "As soon as the lift reaches my floor, I pile out and take a deep, exquisite breath of pure air."
                $ hero.fun -= 5
    elif r == 7:
        "The last thing that I need to have happen, even on an average day at work, is my computer screwing up."
        "It's not that I dread being unable to work on the thing, more that I loathe having to call the IT department to get it fixed."
        "Picking up the phone, I grit my teeth and prepare to hear the disagreeable tones on the other end."
        "Shady guy" "Hello, IT department."
        mike.say "Yeah, hi - listen, my computer's playing up..."
        "Shady guy" "Urrggh...have you tried turning it off and on again?"
        "Here we go again!"
        if hero.charm >= 50:
            mike.say "Well...no, actually, I haven't."
            "Shady guy" "Then you should, as that can usually fix like ninety-nine percent of problems, you know?"
            "I moderate my breathing and bite my lip at his arrogant reply."
            mike.say "Okay, thanks...I'll give that a try and call you back if it doesn't work."
        else:
            mike.say "Of course I've tried that, what kind of a moron do you think I am?"
            "Shady guy" "Erm, the kind that needs to bug me with calls to fix something an average pre-school kid could figure out?"
            mike.say "Look here, you glorified nerd - just send someone up here to fix my damn computer, okay?"
            "I can almost hear his colleagues snickering in the background."
            "Has he actually got me on speaker-phone for them to listen in?"
            "Shady guy" "Take a chill pill, man - I'll send someone up as soon as we can spare 'em..."
            $ game.flags.worksatisfaction -= 1
    elif r == 8:
        "While I'm not sitting on the board of directors at work, I'm not exactly the bottom of the heap either."
        "That means I'm not usually the person in the office that ends up doing the really shitty jobs, like photocopying and shredding."
        "Unless, that is, almost everyone happens to be on annual leave, off sick or for whatever reason just isn't around when it needs doing."
        "And right now, I'm all alone here, looking like I've tried to make a fort out of the stacks of paper on my desk that should already have been shredded."
        "There's no point putting it off any longer, so I grab as much as I can carry and make for the shredder."
        "I shove the first load in and start the machine."
        "But then I feel something suddenly pulling me down towards the razor-sharp blades below."
        "Shit, my tie's caught in there - why couldn't I have waited until dress-down day!"
        if hero.knowledge <= 50:
            "Grabbing desperately at what's left of my tie, I brace myself against the shredder and pull with all my might."
            "It's touch and go for a while, and I can see the whirring blades getting ever closer."
            "But then the adrenaline finally kicks in and I somehow find the strength to pull so hard that I hear something strain and then break inside the machine."
            "Mercifully it grinds to a stop, leaving me alive, but also needing to explain how I just managed to break an expensive office appliance thanks to my own stupidity."
            $ game.flags.worksatisfaction -= 1
        else:
            "I can feel myself starting to panic, but then I suddenly recall that the power switch for the shredder is at chest level for just this very reason."
            "Flailing a hand out towards the wall, I manage to flip the switch off just as I feel myself being dragged downwards."
            "The shredder grinds to a halt, and I can finally breathe a sigh of relief as I reach out to grab a nearby pair of scissors."
            "Snipping the remains of my tie in order to free myself, I reflect that I never really liked it that much anyway."
    elif r == 9:
        "I don't know how it always manages to happen, but it does, every time there's a departmental meeting to sit through."
        "It's either that I've been out and overdone it the night before, or else I've had to pull an all-nighter to get shit done for the meeting itself."
        "Either way, the day of the meeting always finds me utterly exhausted and struggling to stay awake."
        "Today's a perfect example, nothing to look forward to but hours of boring presentations and slides of info-graphics turning my brain to mush."
        "Luckily, I've managed to bag a seat where no one can really see me that well, and I can already feel my head starting to droop forwards."
        "I'm going to have to fight hard if I want to stay awake."
        if hero.fitness <= 50:
            "Ah, screw it - I haven't got a presentation of my own to give and nobody can see me."
            "I make no effort to fight off the drowsiness, and soon I'm lost in a fuzzy-headed dream."
            "This goes on until I swear that I can hear someone calling my name."
            mike.say "Wha...what...what the...I am awake...I have got my pants on!"
            "I wake up to the sight of the entire room looking at me in amused horror, as people try to stifle the urge to laugh."
            $ game.flags.worksatisfaction -= 1
        else:
            "No, this is a matter of personal pride - I won't fall asleep in front of these people!"
            "I fight with all of my will to stay awake, almost nodding off a couple of times only to jerk back into wakefulness."
            "A couple of my colleagues in the meeting note what's happening, and I get elbowed in the ribs more than once."
            "In the end, I manage to struggle through the entire meeting, even getting a little round of applause at the end."
            "It seems my efforts were appreciated by someone, even if it wasn't me."
    elif r == 10:
        "I don't normally snack between meals, it's a bad habit to get into and it really screws with your diet in the long-run."
        "But today I had to run out of the house without eating breakfast, and it's hours before lunchtime."
        "I can feel my stomach growling, and it's keeping me from being able to concentrate on anything in the slightest bit work-related."
        "That's how I find myself in the corridor, desperately stuffing bills into the vending machine to get something to stuff into my face."
        "I punch the buttons for some kind of granola energy bar, thinking that it's not as shameful as chocolate or other sugary junk."
        "But then the nightmare happens - the bar drops forwards and wedges against the glass, an inch from my face."
        "It's like I'm being mocked!"
        if hero.charm >= 50:
            "I could lose my shit, but it's just a cheap granola bar and lunch really isn't that far away."
            "Taking a deep breath, I resolve to tough it out for just a little bit longer."
            "After all, I'd only have felt guilty about snacking anyway."
        else:
            "That's the last straw, really it is!"
            "In a fit of hunger-induced rage, I set to attacking the vending machine, pounding on the glass with my fists and trying to shake the granola bar loose."
            "Suddenly the alarm built into the machine to deter just such an act of primitive violence goes off, turning every head on the floor in my direction."
            "Still hungry and now thoroughly ashamed of myself, I hurry back to my desk, even the sound of the alarm not being enough to drown out the growls of my stomach."
            $ game.flags.worksatisfaction -= 1
    elif r == 11:
        "It's bad enough that my team had to provide cover for one of the women who works on another while she went off on maternity leave for what seemed like a decade."
        "But now she seems to want to compound the inconvenience and irritation that she caused by turning up at the office in order to show off the ultimate result of her efforts."
        "I mean, if I went around showing people the things that came out of my body and expecting to get praised for it, they'd lock me up and throw away the key!"
        "And then, of course, as soon as her bladder (which has apparently been destroyed by the pregnancy) demands her attention, she looks around for someone to hold the baby."
        "I will her to choose one of the women currently standing around and cooing, but she looks straight at me."
        if hero.charm <= 50:
            "I instantly shake my head and begin to back away from the proffered infant as though it had the plague."
            mike.say "Oh no...no, no, no...I'd be afraid of...of dropping it...that's it - I might drop your baby!"
            "The mother shrugs at my odd outburst, and mercifully moves on to choose someone else instead."
            $ game.flags.worksatisfaction -= 1
        else:
            "What harm can holding a baby do for a couple of minutes?"
            mike.say "Okay, hand the little bugger over!"
            "The baby is more than half-asleep anyway, and does little more than stare around and wriggle until its mother comes back to claim it from me."
            "But what I do note is the number of interested glances this little act of paternal indulgence is winning me from many of the other women in the office right now."
    elif r == 12:
        "I'm not proud to have to confess this, but I've gotten into the habit of waiting until I get to work on a morning to visit the bathroom for a sit down - if you know what I mean."
        "It dates back to being a student and having so little money that I had to seriously think about how much toilet roll I could afford to buy every week."
        "Usually it's not a problem, but this morning I go through my usual routine and go to leave after the necessary flush."
        "But then I just happen to look back and notice that this hasn't managed to do the trick."
        "Embarrassed and beginning to panic a little, I hastily grab handfuls of toilet roll to cover up the evidence while I think of what to do."
        menu:
            "Walk away":
                "I know what happens when something like that refuses to take the hint after one flush."
                "Repeating the same course of action won't shift it, and more drastic measures need to be taken."
                "And that's not something that I'm prepared to even contemplate at my place of work."
                "So I duck out of the bathroom as quickly and casually as I can possibly manage."
            "Flush it again":
                "As soon as I hear the sound of the cistern refilling come to a cease, I begin to hammer away at the flush once again."
                "But in the meantime, I've been stuffing so much toilet roll down there that it immediately causes a blockage."
                "As the bowl begins to overflow and water spreads across the tiled floor, I flee the scene of the crime."
                "All I can do is slink back to my desk, hoping that no one can link me to the monster currently flooding the bathroom."
                python:
                    for g in ["aletta", "audrey", "lavish", "shiori"]:
                        if Person.is_not_hidden(g):
                            Person.find(g).love -= 2
    elif r == 13:
        "I don't usually make a habit of getting dressed in the dark, but today I overslept and was in such a hurry to get out of the house that I did just that."
        "Nothing seems out of place at first, but as I'm waiting for the lift in the lobby, I can hear people beginning to laugh as they walk past and glance down."
        "This starts a snowballing of the attention I'm getting, until everyone seems to be staring at my feet and trying to suppress their amusement at what they're seeing."
        "I look down and find myself stunned and horrified to see that I'm wearing odd shoes - not just that, but one has laces and the other is a slip-on!"
        menu:
            "Bear with it":
                "I step into the lift, trying to ignore the laughter around me and focus on the day ahead."


                $ hero.fun -= 5
            "Removes your shoes":
                "I make an immediate dash for the nearest bathroom, running into a cubicle and pulling off my odd shoes."
                "The rest of the day I spend walking here and there in nothing but my socks."
                "Which attracts some odd looks too, but is infinitely preferable to the ones I was getting beforehand."
    return

label work:
    if game.flags.suspended:
        return
    scene expression f"bg {game.room}"
    menu:
        "Chat with Shiori" if Person.is_not_hidden("shiori") and Room.has_tag(shiori.room, "work"):
            show shiori work
            call expression shiori.get_chat from _call_expression_76
            hide shiori
        "Chat with Aletta" if Person.is_not_hidden("aletta") and Room.has_tag(aletta.room, "work"):
            show aletta work
            call expression aletta.get_chat from _call_expression_77
            hide aletta
        "Chat with Audrey" if Person.is_not_hidden("audrey") and Room.has_tag(audrey.room, "work"):
            show audrey work
            call expression audrey.get_chat from _call_expression_78
            hide audrey
        "Chat with Lavish" if Person.is_not_hidden("lavish") and Room.has_tag(lavish.room, "work"):
            show lavish work
            call expression lavish.get_chat from _call_expression_176
            hide lavish
        "Slack off":
            if randint(1, 100) < hero.charm:
                show chibi workslack
                "Nobody notices that I slack off."
                $ hero.fun += 2
                if hero.has_skill("work"):
                    $ game.flags.worksatisfaction += 5
                $ game.flags.worksatisfaction += 5
            else:
                show aletta
                aletta.say "You think I don't see you slacking off, [hero.name]."
                $ game.flags.worksatisfaction -= 1
                hide aletta
        "Work normally":
            show chibi work
            mike.say "I work a little bit."
            if hero.has_skill("work"):
                $ game.flags.worksatisfaction += 5
            $ game.flags.worksatisfaction += 5
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label workhard:
    if game.flags.suspended:
        return

    $ r = randint(1, 3)
    menu:
        "Chat with Shiori" if Person.is_not_hidden("shiori") and Room.has_tag(shiori.room, "work"):
            show shiori work
            call expression shiori.get_chat from _call_expression_79
            hide shiori
        "Chat with Aletta" if Person.is_not_hidden("aletta") and Room.has_tag(aletta.room, "work"):
            show aletta work
            call expression aletta.get_chat from _call_expression_80
            hide aletta
        "Chat with Audrey" if Person.is_not_hidden("audrey") and Room.has_tag(audrey.room, "work"):
            show audrey work
            call expression audrey.get_chat from _call_expression_81
            hide audrey
        "Chat with Lavish" if Person.is_not_hidden("lavish") and Room.has_tag(lavish.room, "work"):
            show lavish work
            call expression lavish.get_chat from _call_expression_177
            hide lavish
        "Work fast":
            show chibi workhard
            if hero.knowledge == 100 or randint(1, 100) < hero.knowledge:
                "I manage to do twice the amount of work!"
                $ game.flags.worksatisfaction += 15
                if hero.has_skill("work"):
                    $ game.flags.worksatisfaction += 15
            else:
                hide chibi
                show aletta
                aletta.say "What are you doing, [hero.name]? You made so many mistakes we have to start over again..."
                hide aletta
        "Work normally":
            show chibi workhard
            "I work a good deal."
            $ game.flags.worksatisfaction += 10
            if hero.has_skill("work"):
                $ game.flags.worksatisfaction += 10
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
