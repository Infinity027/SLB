init python:
    Room(**{
    "name": "personal",
    "display_name": "My Office",
    "exits": ["office", "alettaoffice", "breakroom", "map"],
    "hours": (8, 20),
    "conditions": [
        IsDayOfWeek("123456"),
        Or(
            IsHour(8, 20),
            And(
                IsDone("cherie_event_06"),
                IsNotDone("cherie_event_07_1"),
                IsTimeOfDay("evening", "night"),
                ),
            ),
        IsDone("work_promoted"),
        HeroTarget(
            Not(IsFlag("isceo"))
        )
        ],
    "music": "music/roa_music/fly_high.ogg",
    "valid": False,
    "outfit": "work",
    "tags": ["work", "mcoffice"],
    })

    Activity(**{
    "name": "work_place_spy_camera",
    "display_name": "Place spy camera",
    "max_girls": 0,
    "rooms": "mcoffice",
    "conditions": [
        IsDone("cassidy_setup_meeting"),
        HeroTarget(
            IsFlag("underinvestigation"),
            IsFlag("cassidycameraplaced", False),
            ),
        InInventory("spy_camera"),
        ],
    "label": "work_place_spy_camera",
    "icon": "spycamera",
    "once_day": True,
    })

    Activity(**{
    "name": "work_place_spy_camera_2",
    "display_name": "Place spy camera",
    "max_girls": 0,
    "rooms": ("alettaoffice", "office"),
    "conditions": [
        IsDone("cassidy_setup_meeting"),
        HeroTarget(
            IsFlag("underinvestigation"),
            IsFlag("cassidycameraplaced", False),
            ),
        InInventory("spy_camera"),
        ],
    "label": "work_place_spy_camera_2",
    "icon": "spycamera",
    "once_day": True,
    })

    Activity(**{
    "name": "work_call_the_accountant",
    "display_name": "Call Jeff the accountant",
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99),
            IsFlag("toldjeff"),
            ),
        ],
    "label": "work_call_the_accountant",
    "icon": "investigate",
    "do_once": True,
    })

    Activity(**{
    "name": "investigation_hire_pi",
    "display_name": "Hire a private investigator",
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99),
            ),
        ],
    "label": "investigation_hire_pi",
    "icon": "investigate",
    "do_once": True,
    })

    Activity(**{
    "name": "work_personal",
    "money_gain": {"attributes": ["charm", "knowledge"], "bonus": ("promoted",)},
    "duration": 4,
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("suspended", False),
            IsFlag("fired", False),
            ),
        ],
    "display_name": "Work",
    "label": "work",
    "icon": "work",
    "say": [
        "All work and no play makes [hero.name] a dull boy.",
        ],
    })

    Activity(**{
    "name": "workhard_personal",
    "money_gain": {"attributes": ["charm", "knowledge"], "mult": (2,), "bonus": ("promoted",)},
    "fun": -2,
    "duration": 4,
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            MinStat("energy", 4),
            MinStat("hunger", 4),
            MinStat("grooming", 4),
            MinStat("fun", 4),
            IsFlag("suspended", False),
            IsFlag("fired", False),
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
    "name": "shiori_teaser",
    "label": "shiori_teaser",
    "conditions": [
        HeroTarget(
            IsActivity("work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        ],
    "do_once": True,
    })

label work_place_spy_camera:
    show chibi spy
    "It takes a little while, but I find a good spot for the camera that can see the entire office, and is nearly impossible to see if you're not looking for it."
    $ game.flags.cassidycameraplaced = True
    $ hero.lose_item("spy_camera")
    return

label work_place_spy_camera_2:
    show chibi spy
    "It takes a little while, but I find a good spot for the camera that can see the entire office, and is nearly impossible to see if you're not looking for it."
    $ hero.lose_item("spy_camera")
    return

label work_call_the_accountant:
    "Before I dial, I run through what I know: Jeff rigged the whole thing for Cassidy, she has blackmail material on him, and they're almost certainly sleeping together."
    "My plan — start civil, then threaten to tell his wife. Desperate, but I'm out of better options."
    "I dial his extension."
    "Jeff" "Hello, this is Jeff in Accounting."
    "Older than I expected. At least fifty, judging by that voice."
    mike.say "Hi, Jeff. My name is [heroname] [hero.family_name]. I think you know what this is about."
    "A pause. I hear him swallow."
    "Jeff" "Mister [hero.family_name], we should only be speaking if we have questions for you. At this time, we don't."
    mike.say "No questions? Not even about where the money went? Right — because you already know."
    "Jeff" "I'm sure I don't know what you're talking about."
    mike.say "I'm quite sure you do, Jeff."
    "Jeff" "I'm going to hang up now. Goodbye."
    mike.say "Wait. Cassidy sends her regards. How do I reach your wife?"
    "Another pause. I hold my breath."
    "Jeff" "W-why would you want to reach my wife?"
    mike.say "I thought she and Cassidy might have a lot to talk about."
    "Jeff" "NO — it's not like that!"
    mike.say "Then what is it like, Jeff? Because from where I'm standing, Cassidy is using you to bury me — and she's already threatened to tell Caroline. That is your wife's name, isn't it?"
    "Jeff" "I'm not answering these questions."
    mike.say "Fine. But aren't you old enough to be Cassidy's father? What's Caroline going to think?"
    "Jeff" "Please don't do this!"
    mike.say "Then stop this."
    "Jeff" "I can't. I can't stop any of it."
    mike.say "Jeff — if I go down, you go down with me. That's not a threat, it's just how this ends."
    "Jeff's voice breaks. I can hear him starting to lose it."
    "Jeff" "She won't let me stop. It was just once, and then she had pictures... she makes me..."
    "Jeff" "Oh God. I can't talk about it."
    mike.say "Then help me stop her. I have something on her. Together we can both walk away from this."
    "He sounds desperate now. I'm close — I just need to reel him in."
    "Jeff" "I don't believe you."
    mike.say "You don't have to. But if you don't help me, you're going down regardless. Do you believe that?"
    "Jeff" "W-what do you want me to do?"
    mike.say "Throw off the investigation. Buy me time. I'll find out where the money really went, and the person who did this will pay."
    "Jeff" "I already know who did it. And you can't touch him."
    mike.say "Who is it?"
    "Jeff" "He can do worse to me than you ever could. I'm not saying."
    mike.say "Jeff, your family is on the line here."
    "Jeff" "You can take my family. He can take everything."
    "A beat of silence."
    "Jeff" "I'll push some numbers around. But not too much — he'll notice. No promises, Mister [hero.family_name]. I'll see what I can do."
    "I hang up. All I can do now is hope he muddies things enough to keep the investigation inconclusive."
    call investigation_points (20) from _call_investigation_points
    return

label investigation_hire_pi:
    "Suspension. Nothing to do but sit here and stew over the fact that someone framed me for embezzlement."
    "Or — maybe I should be using this time to fight back."
    "A quick search online turns up a PI based right here in the city. Within the hour I have his number."
    "Hiring a private investigator feels like something out of a film. Then again, so does being framed for embezzlement."
    "I shake off the hesitation and dial."
    "Investigator" "Hello? Who is this?"
    "Clipped, serious. I haven't even spoken yet — he must think it's a prank call."
    mike.say "Is... is this the private dick?"
    "A long pause. Then a heavy sigh."
    "Investigator" "This is Jake Powers — Private Investigator. Don't call me a dick. That joke gets old fast."
    mike.say "Sorry, Mister Powers."
    "He settles, his tone shifting back to calm and professional."
    "Investigator" "No problem. What can I do for you?"
    mike.say "I've been accused of stealing from my company. A serious amount of money. And I'm completely innocent."
    "Investigator" "Let me guess — not a couple of bucks here and there?"
    mike.say "Not even close."
    "The PI chuckles."
    "Investigator" "Well, your innocence isn't really my concern. What matters is whether you can pay my fee. I'm sending you a text with my rates — take a look."
    "My phone buzzes. I put him on hold and open the message."
    "My eyes go wide."
    menu:
        "Hire him" if hero.money >= 500:
            "It's a gut punch of a number. For a second I consider telling him where he can stick it."
            "But then I think about the alternative — doing nothing — and that's worse."
            mike.say "You're not cheap, Mister Powers. But I need your help. You're hired."
            "Investigator" "You get what you pay for. And look at it this way — if you're innocent, your employer will have to compensate you. If you're guilty, you've already got dirty money to spare. Either way, you can afford me."
            "Not how I'd have put it. But he's not wrong."
            mike.say "So what happens now?"
            "Investigator" "I send you the paperwork. You sign on the dotted line and leave the rest to me."
            mike.say "Sounds like a start."
            "Investigator" "I'll be in touch."
            "He hangs up. I don't feel like the weight has lifted — but for the first time, it feels like I've actually done something."
            "I just hope his website reviews are accurate."
            call investigation_points (10) from _call_investigation_points_8
        "Don't hire him":
            "Who does this guy think I am? A millionaire?"
            "I take him off hold."
            mike.say "Are you crazy? I don't have that kind of money."
            "Investigator" "That's too bad. If only you'd actually stolen the money — then you could have afforded me."
            "I hang up before I say something I'll regret."
            "Back to square one."
    return

label shiori_teaser:
    show alexis casual at center, zoomAt(1.5, (640, 1140)), blacker with fade
    "The sound of coughing from across the desk comes out of the blue, snapping me back to reality."
    "It's a stark change from the sound of the droning voice that's nearly put me to sleep."
    "And as I shake off its effects, I realise I have absolutely no idea what was being said."
    "All I can do is smile at the girl that's now staring at me, an expectant look on her face."
    "She's finished her spiel and now it's my turn to say something."
    mike.say "Wow, that's some pitch!"
    mike.say "Leave it with me, and you should hear back in about a week's time."
    mike.say "Thanks for coming in."
    show alexis at center, traveling(1.5, 0.3, (640, 1040)), blacker
    "We exchange forced, professional smiles."
    "But I think we both already know she's not going be getting the job."
    show alexis at center, traveling(1.0, 0.3, (0, 720)), blacker
    pause 0.5
    hide alexis with easeoutleft
    "I lean back in my chair, groaning as I survey the pile of applications on the desk before me."
    "I lost count after the third candidate."
    "And now they're all starting to merge into one!"
    "Punctual, efficient, professional and annoyingly perky."
    "Basically a long line of clones, all telling me what they think I want to hear."
    "Is it so hard to find an honest to god human being?"
    play sound door_knock
    "A knock at my office door brings my wallowing in self-pity to an abrupt end."
    mike.say "Yeah - come on in!"
    show shiori talk at center, zoomAt(1, (440, 720)) with easeinleft
    "Shiori" "Is...is this the right place?"
    "Shiori" "I'm here about the secretary position?"
    show shiori normal
    "The word 'position' makes my mind summon an image worthy of an adolescent boy."
    "But the voice is so small and timid that I shake my head, already dismissing her."
    mike.say "Sorry, you'll have to come back tomorrow..."
    "And that's when I look up and see her for the first time."
    "She's a petite girl, Asian by descent, with large eyes and black hair."
    show shiori surprised
    "Shiori" "Oh...oh dear..."
    mike.say "Ah...f...forget what I just said."
    mike.say "I must have gotten the times mixed up, that's all!"
    show shiori smile at center, zoomAt(1, (640, 720)) with ease
    "She smiles, but with real emotion."
    "She bows at the waist, just a little."
    show shiori talk
    "Shiori" "My name is Shiori."
    shiori.say "And you must be Mister [hero.family_name]."
    show shiori normal
    "I realize that, as she bowed, I couldn't help staring down her top."
    mike.say "YES...I mean, yes - that's who I am."
    "I tear my eyes away from Shiori's breasts and gesture to a seat."
    mike.say "Sit down and tell me all about yourself...Shiori."
    show shiori at center, traveling(1.5, 0.5, (640, 1040))
    pause 0.5
    show shiori at center, traveling(1.5, 0.3, (640, 1140))
    "The name sounds so pleasing when I say it out loud."
    show shiori smile
    "And the smile she gives me at hearing it..."
    "No, must focus - be professional!"
    show shiori talk
    shiori.say "I...I have to be honest, Mister [hero.family_name]."
    shiori.say "I don't have the greatest CV in the world."
    shiori.say "But if I'm under the right man - then you wouldn't believe what I can do..."
    show shiori normal
    "I feel myself tugging at my collar."
    mike.say "Is...is that right, Shiori?"
    show shiori talk
    shiori.say "Oh yes, Mister [hero.family_name]."
    shiori.say "You can put me in almost any position you like."
    shiori.say "I'm told that I'm very flexible."
    show shiori normal
    "It's all I can do to keep from chuckling to myself."
    "Almost everything out of her mouth sounds like an innuendo."
    show shiori talk
    shiori.say "Ah, is something wrong, Mister [hero.family_name]?"
    shiori.say "Did I make a mistake?"
    show shiori normal
    menu:
        "No (Never meet Shiori again)":
            mike.say "No, Shiori - nothing's wrong."
            "Shiori begins to fidget in her seat, avoiding eye-contact."
            "Oh shit - she thinks I'm making fun of her!"
            mike.say "Ah...well, Shiori."
            mike.say "I'm sorry to say that I won't be offering you the position."
            show shiori sad
            "She nods, too eagerly for it to be genuine."
            show shiori at center, traveling(1.5, 0.3, (640, 1040))
            pause 0.3
            show shiori at center, traveling(1.0, 0.3, (0, 720))
            pause 0.5
            hide shiori with easeoutleft
            "A moment later, she's on her feet and almost running out of the office."
            "I watch her hips sway and her breasts bounce as she goes."

        "I like it when you call me sir.":
            mike.say "It's nothing, Shiori."
            mike.say "I...I just kind of like it when you call me 'Mister [hero.family_name]', that's all."
            show shiori talk
            shiori.say "Oh...I...I had no idea!"
            show shiori blush
            "She blushes and looks away in a disarmingly demure fashion."
            "And I feel it almost like a physical blow."
            show shiori talk
            shiori.say "I'd get to do it all the time - if you hired me, Mister [hero.family_name]!"
            show shiori normal
            "Is she...is she flirting with me?!?"
            "I have to keep a level head here, be professional!"
            mike.say "Y...you better get used to being at my beck and call, Shiori."
            mike.say "Because I think you'd be perfect for the job."
            "Shiori stares at me, her huge eyes wide with surprise."
            show shiori talk
            shiori.say "R...really?!?"
            shiori.say "That was a VERY short interview, Mister [hero.family_name]!"
            show shiori normal
            "I shake my head and shrug, trying to look as nonchalant as I can manage."
            mike.say "I just have a good feeling about you, Shiori - you know?"
            mike.say "I can see this working out well - with me on top of you..."
            mike.say "I...I mean with you under me...working under me, that is!"
            "For all of my blustering, Shiori seems not to notice the sexual tension I'm feeling."
            show shiori talk
            shiori.say "Me too, Mister [hero.family_name] - I really can't wait for you to put me to work!"
            shiori.say "When do I start?"
            show shiori normal
            mike.say "As soon as possible - how does tomorrow morning sound?"
            show shiori happy at startle
            shiori.say "Of course, Mister [hero.family_name]!"
            show shiori smile
            "Shiori jumps up like a Jack-in-the-box."
            "And the effect on her chest is quite something."
            show shiori talk
            shiori.say "Then I'll see you in the morning, Mister [hero.family_name] - bright and early!"
            show shiori at center, traveling(1.5, 0.3, (640, 1040))
            "I watch Shiori as she makes her way out of my office."
            show shiori at center, traveling(1.0, 0.3, (0, 720))
            pause 0.5
            hide shiori with easeoutleft
            "Her hips sway and her breasts bounce as she goes."
            $ game.flags.hiringshiori = True
    hide shiori
    return
return