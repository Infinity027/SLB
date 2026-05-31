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
            IsGender("male"),
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
            IsGender("male"),
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
    "money_gain": {"attributes": ["charm", "knowledge"], "mult": (1.5,), "bonus": ("promoted",)},
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
    "name": "shiori_teaser",
    "label": "shiori_teaser",
    "conditions": [
        HeroTarget(
            IsGender("male"),
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
    "I pick up the phone to call the accountant, but before I do I go over in my head what I know about him."
    "I know that according to Cassidy, he's the guy who rigged this whole thing."
    "I know that Cassidy has blackmail material on him."
    "I'm pretty sure he's sleeping with Cassidy."
    "That means my best course of action is to start off nice, but threaten to tell his wife about his girlfriend. That will put him in a rough spot."
    "It could make things worse, but I'm feeling desperate here."
    "I take a deep breath and call his extension."
    "Jeff" "Hello, this is Jeff in Accounting."
    "Judging from his voice, Jeff is older than I realized. At least 50, unless he's just spent too much of his life smoking and drinking."
    mike.say "Hi, Jeff! My name is [heroname] [hero.family_name]. I think you might know what this is about."
    "There is a pause, and I can hear him swallow."
    "Jeff" "Mister [hero.family_name], we should only be speaking if we have questions for you. At this time, we do not have any questions for you."
    mike.say "No? No questions for me at all? You mean, you don't want to ask me where the money went? Oh right, it's because you already know."
    "Jeff" "I'm sure I don't know what you're talking about."
    mike.say "I'm quite sure you do, Jeff."
    "Jeff" "I'm going to hang up now. Goodbye, Mister [hero.family_name]."
    mike.say "Wait, Jeff. Before you do, Cassidy sends her regards. I was just wondering, how do I reach your wife?"
    "There is another pause, and I can feel my blood pressure skyrocketing while I wait to see if he takes the bait."
    "Jeff" "W-w-w-why would you want to reach my wife?"
    mike.say "Oh, I just thought your wife and your lover might have something to talk about."
    "Jeff" "NO! No, it's not like that!"
    mike.say "No? Then what is it like?"
    "Jeff" "That's none of your business!"
    mike.say "Jeff, listen to me very carefully. Your slam-piece is trying to nail my balls to the wall, and she's using you to do it."
    mike.say "She already threatened to tell Caroline -- that's your wife's name, isn't it?"
    "Jeff" "I--I--I'm not going to answer any of these questions."
    mike.say "Fine, Jeff. Don't answer. But what will Caroline say? Aren't you old enough to be Cassidy's father?"
    "Jeff" "Please don't do this!"
    mike.say "Then stop this!"
    "Jeff" "I--I can't. I can't stop any of this."
    mike.say "Look, Jeff. I can't make this any more clear: If I go down, I'm taking you with me. You can stop this."
    "Jeff" "I. Please!"
    "Jeff's voice breaks, and I can hear a sob."
    "Jeff" "Please, Mister [hero.family_name], she won't let me stop. It was just once, but then she had pictures, and she makes me..."
    "Jeff" "Oh God, I can't talk about it."
    mike.say "Then help me stop her. I have something on her. With your help, I can get us both out of this."
    "Where Jeff's voice was confident and at the beginning of the conversation, by now he sounds desperate. I'm pretty sure I have him, and I just need to reel him in."
    "Jeff" "I don't believe you."
    mike.say "You don't have to believe me. If you don't help me, you're going down. Do you believe that?"
    "Jeff" "W-w-what do you want me to do?"
    mike.say "I just need you to throw off the investigation. I'm going to find out where the money actually went, and the fucker who did this is going to pay."
    "Jeff" "I already know who did this, and you can't make him pay."
    mike.say "You do? Who!?"
    "Jeff" "You can do whatever you want to me, but he can do worse. I'm not saying."
    mike.say "Damn it, Jeff! Don't wimp out on me here. Your family is at stake!"
    "Jeff" "Look, I'll do what I can. I'll push some different numbers. But I can't do too much. He'll figure it out, and he'll screw me worse than you possibly can."
    "Jeff" "You can take my family from me, but he can take everything. Everything."
    mike.say "You'd better. You'd better fix this for me. Or else."
    "Jeff" "No promises, Mister [hero.family_name]. But I'll see what I can do."
    "I hang up the phone. I can only hope and pray that he puts enough wrenches in the investigation to at least make it inconclusive."
    call investigation_points (20) from _call_investigation_points
    return

label investigation_hire_pi:
    "I don't know which is the worst thing about being hit with a suspension from work."
    "Knowing that someone went to all the trouble of framing me for embezzlement."
    "Or the fact that I'm now sitting around with nothing to do but brood on it."
    "But then maybe I'm looking at this whole thing the wrong way."
    "Sure, this is one of those situations when life gives you lemons."
    "So maybe I need to start trying to make some lemonade?"
    "Maybe I should be using all of this free time to fight back?"
    "All it takes is a little digging around online, a few searches."
    "And within the hour I have the number of a PI based right here in the city."
    "It feels weird doing something like this, and so I hesitate before calling."
    "Hiring a PI always feels like the kind of thing that happens in a movie."
    "But then so does being framed for embezzlement."
    "And so I shake off my reservations and dial the number."
    "It rings a couple of times, and I start to think that nobody will answer."
    "If the call goes to voicemail, at least I can say that I tried - right?"
    "Investigator" "Hello?"
    "Investigator" "Who is this?"
    "The tone of the voice on the other end of the line is serious."
    "For a moment I think that I must have dialled the wrong number."
    "But then I realise that I haven't said a word yet."
    "Whoever this is, they're likely starting to think this is a prank call!"
    mike.say "Is..."
    mike.say "Is this the private dick?"
    "There's a pause on the other end of the line."
    "And I hear the speaker sigh heavily."
    "Investigator" "This is Jake Powers - Private Investigator."
    "Investigator" "Don't call me a dick, okay?"
    "Investigator" "In this business, that joke gets old real quick."
    mike.say "Oops..."
    mike.say "Sorry, Mister Powers."
    "There's another momentary pause."
    "But when the PI speaks again, he sounds more calm and professional."
    "Which is a relief for me."
    "Investigator" "No problem."
    "Investigator" "Now, was there something I can do for you?"
    mike.say "Oh...oh yes!"
    mike.say "I have a problem at work."
    mike.say "You see I've been accused of stealing from the company."
    "Investigator" "Let me guess - it's not a couple of bucks here and there?"
    mike.say "No, it's not."
    mike.say "We're talking about a serious amount of money here."
    mike.say "And I'm completely innocent!"
    "I hear the PI chuckle on the other end of the line."
    "Investigator" "Well, that's not really my concern, sir."
    "Investigator" "All I'm worried about is if you can pay my fee!"
    "Investigator" "I'm sending you over a text with my charges."
    "Investigator" "Take a look and let me know how it hits you."
    "My phone buzzes a moment later to announce the arrival of the text."
    "I put the PI on hold as I open the message and read its contents."
    "And the moment I do, my eyes go wide at the figures I see in there!"
    menu:
        "Hire him" if hero.money >= 500:
            "The number that I read hits me like a punch in the gut."
            "I think about telling the PI that he can shove his services."
            "But then I stop myself and actually think about the alternative."
            "Maybe I shouldn't be worrying about the price at a time like this?"
            mike.say "You're not cheap, Mister Powers."
            mike.say "But I really need your help."
            mike.say "So you're hired."
            "Investigator" "Believe me, you get what you pay for!"
            "Investigator" "And look at it this way..."
            "Investigator" "If you're innocent, your employer will have to compensate you."
            "Investigator" "And If you're guilty, you already have a pile of dirty money."
            "Investigator" "Either way you can afford to pay for me to save your ass!"
            "Not the way I would have chosen to put it, that's for sure."
            "But he does make a pretty good point."
            mike.say "So what happens now?"
            "Investigator" "What happens now is that I send you over the paperwork."
            "Investigator" "You read it, sign on the dotted line and then leave it to me."
            "Investigator" "How does that sound?"
            mike.say "It sounds like a start."
            "Investigator" "Okay, I'll be in touch."
            "And with that, he ends the call."
            "I don't feel like the weight of the world is off my shoulders."
            "But it does start to feel like I've taken a positive step forwards."
            "I just hope this guy is as good as the reviews on his website!"
            call investigation_points (10) from _call_investigation_points_8
        "Don't hire him":
            "What does this guy think?"
            "That I'm some kind of millionaire?!?"
            "I take the PI off hold and give him a piece of my mind."
            mike.say "Are you crazy?"
            mike.say "I don't have that kind of money just lying about!"
            "Rather than being annoyed or offended, the PI chuckles again."
            "Investigator" "Well, that's just too bad, isn't it."
            "Investigator" "If only you had stolen the money."
            "Investigator" "Maybe then you could have afforded my services!"
            "I end the call before I say something that I might regret."
            "And then I let out a sigh of frustration."
            "As I'm right back where I started again."
    return

label shiori_teaser:
    show alexis casual b at center, zoomAt(1.5, (640, 1140)), blacker with fade
    "The sound of coughing from across the desk comes out of the blue, snapping me back to reality."
    "It's a stark change from the sound of the droning voice that's nearly put me to sleep."
    "And as I shake off its effects, I realise I have absolutely no idea what was being said."
    "All I can do is smile at the girl that's now staring at me, an expectant look on her face."
    "Shit, of course - I'm interviewing the new secretarial position."
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
    "Someone real that's not got the whiff of insincerity about them?"
    "Call me a sexist too, but they've all been so painfully normal in the looks department too."
    "Sure, they were all fairly pretty, but I couldn't pick any of them out of a police line-up."
    "Not even if my life depended on it..."
    play sound door_knock
    "A knock at my office door brings my wallowing in self-pity to an abrupt end."
    "I groan wearily and scrub the palms of my hands over my face."
    mike.say "Yeah - come on in!"
    show shiori work _a talkative at center, zoomAt(1, (440, 720)) with easeinleft
    "Shiori" "Is...is this the right place?"
    "Shiori" "I'm here about the secretary position?"
    show shiori normal _a
    "The word 'position' makes my mind summon an image worthy of an adolescent boy."
    "But the voice is so small and timid that I shake my head, already dismissing her."
    mike.say "Sorry, you'll have to come back tomorrow..."
    "And that's when I look up and see her for the first time."
    "She's a petite girl, Asian by descent, with large eyes and black hair."
    "All of that and what could be the largest rack I've ever seen!"
    show shiori surprised _a
    "Shiori" "Oh...oh dear..."
    show shiori stuned a
    mike.say "Ah...f...forget what I just said."
    mike.say "I must have gotten the times mixed up, that's all!"
    show shiori _a smile at center, zoomAt(1, (640, 720)) with ease
    "She smiles, but with real emotion."
    "She seems genuinely happy to be given a chance."
    "She bows at the waist, just a little."
    show shiori _a happy
    "Shiori" "My name is Shiori."
    show shiori _a talkative
    shiori.say "And you must be Mister [hero.family_name]."
    show shiori _a normal
    "I realize that, as she bowed, I couldn't help staring down her top."
    mike.say "YES...I mean, yes - that's who I am."
    "I tear my eyes away from Shiori's breasts and gesture to a seat."
    mike.say "Sit down and tell me all about yourself...Shiori."
    show shiori _a at center, traveling(1.5, 0.5, (640, 1040))
    pause 0.5
    show shiori _a at center, traveling(1.5, 0.3, (640, 1140))
    "The name sounds so pleasing when I say it out loud."
    show shiori _a smile
    "And the smile she gives me at hearing it..."
    "No, must focus - be professional!"
    "It's then that I notice she's blushing a little."
    "Something that only seems to make her that much more adorable..."
    show shiori _a talkative
    shiori.say "I...I have to be honest, Mister [hero.family_name]."
    shiori.say "I don't have the greatest CV in the world."
    shiori.say "But if I'm under the right man - then you wouldn't believe what I can do..."
    show shiori _a normal
    "I feel myself tugging at my collar."
    mike.say "Is...is that right, Shiori?"
    show shiori _a talkative
    shiori.say "Oh yes, Mister [hero.family_name]."
    shiori.say "You can put me in almost any position you like."
    shiori.say "I'm told that I'm very flexible."
    show shiori _a normal
    "It's all I can do to keep from chuckling to myself."
    "Almost everything out of her mouth sounds like an innuendo."
    show shiori _a talkative
    shiori.say "Ah, is something wrong, Mister [hero.family_name]?"
    shiori.say "Did I make a mistake?"
    show shiori _a normal
    menu:
        "No (Never meet Shiori again)":
            mike.say "No, Shiori - nothing's wrong."
            "Shiori begins to fidget in her seat, avoiding eye-contact."
            "Oh shit - she thinks I'm making fun of her!"
            "This is going south, and fast."
            "And beginning to panic, I can only think of one sure way out of this mess."
            mike.say "Ah...well, Shiori."
            mike.say "I'm sorry to say that I won't be offering you the position."
            show shiori _a sad
            "She nods, too eagerly for it to be genuine."
            show shiori _a at center, traveling(1.5, 0.3, (640, 1040))
            pause 0.3
            show shiori _a at center, traveling(1.0, 0.3, (0, 720))
            pause 0.5
            hide shiori with easeoutleft
            "A moment later, she's on her feet and almost running out of the office."
            "I watch her hips sway and her breasts bounce as she goes."
            "And I can't help thinking that I just passed on something special."
        "I like it when you call me sir.":
            mike.say "It's nothing, Shiori."
            mike.say "I...I just kind of like it when you call me 'Mister [hero.family_name]', that's all."
            show shiori _a talkative
            shiori.say "Oh...I...I had no idea!"
            show shiori _a normal blush
            "She blushes and looks away in a disarmingly demure fashion."
            "And I feel it almost like a physical blow."
            show shiori _a talkative
            shiori.say "I'd get to do it all the time - if you hired me, Mister [hero.family_name]!"
            show shiori _a normal
            "Is she...is she flirting with me?!?"
            "I...I have to keep a level head here, be professional!"
            mike.say "Y...you better get used to being at my beck and call, Shiori."
            mike.say "Because I think you'd be perfect for the job."
            "Shiori stares at me, her huge eyes wide with surprise."
            show shiori _a talkative
            shiori.say "R...really?!?"
            shiori.say "That was a VERY short interview, Mister [hero.family_name]!"
            show shiori _a normal
            "I shake my head and shrug, trying to look as nonchalant as I can manage."
            mike.say "I just have a good feeling about you, Shiori - you know?"
            mike.say "I can see this working out well - with me on top of you..."
            mike.say "I...I mean with you under me...working under me, that is!"
            "For all of my blustering, Shiori seems not to notice the sexual tension I'm feeling."
            show shiori _a talkative
            shiori.say "Me too, Mister [hero.family_name] - I really can't wait for you to put me to work!"
            shiori.say "When do I start?"
            show shiori _a normal
            mike.say "As soon as possible - how does tomorrow morning sound?"
            show shiori _a happy at startle
            shiori.say "Of course, Mister [hero.family_name]!"
            show shiori _a smile
            "Shiori jumps up like a Jack-in-the-box."
            "And the effect on her chest is quite something."
            show shiori _a talkative
            shiori.say "Then I'll see you in the morning, Mister [hero.family_name] - bright and early!"
            show shiori _a at center, traveling(1.5, 0.3, (640, 1040))
            "I watch Shiori as she makes her way out of my office."
            show shiori _a at center, traveling(1.0, 0.3, (0, 720))
            pause 0.5
            hide shiori with easeoutleft
            "Her hips sway and her breasts bounce as she goes."
            "And I know that I'll have her on my mind until I see her again tomorrow morning."
            $ game.flags.hiringshiori = True
    hide shiori
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
