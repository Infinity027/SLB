init python:
    Event(**{
    "name": "lexi_female_event_01",
    "label": "lexi_female_event_01",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsHour(18, 2),
        MinDaysPlayed(9),
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsRoom("map"),
            MinStat("money", 250),
            ),
        PersonTarget("lexi",
            IsFlag("delay", False)
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_female_event_02",
    "label": "lexi_female_event_02",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_01"),
        HeroTarget(
            IsRoom("coffeeshop"),
            IsGender("female"),
        ),
        PersonTarget(lexi,
            IsFlag("delay", False)
            ),
    ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_03",
    "label": "lexi_female_event_03",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_02"),
        IsDayOfWeek(6, 7),
        IsHour(12, 19),
        HeroTarget(
            HasRoomTag("home")
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 20),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_04",
    "label": "lexi_female_event_04",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_03"),
        Not(IsDone("lexi_female_event_04b")),
        IsSeason(0, 1),
        IsHour(20, 23),
        HeroTarget(
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 40),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_04b",
    "label": "lexi_female_event_04b",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_03"),
        Not(IsDone("lexi_female_event_04")),
        IsSeason(0, 2, 3),
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
            HasRoomTag("mall_southside"),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 40),
            MinStat("lesbian", 8),
            ),
    ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_05",
    "label": "lexi_female_event_05",
    "priority": 500,
    "duration": 1,
    "conditions": [
        Or(
            IsDone("lexi_female_event_04"),
            IsDone("lexi_female_event_04b"),
            ),
        HeroTarget(
            IsRoom("date_mall1"),
            ),
        PersonTarget(lexi,
            OnDate(),
            IsFlag("delay", False),
            MinStat("love", 60),
            ),
    ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_06",
    "label": "lexi_female_event_06",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_05"),
        HeroTarget(
            IsRoom("date_mall1"),
            OnDate(),
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 80),
            MinStat("lesbian", 8),
            OnDate(),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_07",
    "label": "lexi_female_event_07",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_06"),
        HeroTarget(
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
            ),
            Or(
                IsActivity("buy_a_round"),
                IsActivity("offer_a_drink"),
            ),
        ),
        PersonTarget(lexi,
            IsActive(),
            IsFlag("delay", False),
            MinStat("love", 100),
            MinStat("lesbian", 8),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_08",
    "label": "lexi_female_event_08",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_07"),
        HeroTarget(
            IsRoom("date_mall1"),
            OnDate(),
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 120),
            MinStat("lesbian", 8),
            OnDate(),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_09",
    "label": "lexi_female_event_09",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_08"),
        HeroTarget(
            IsRoom("university"),
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            IsFlag("suggested_university"),
            MinStat("love", 140),
            MinStat("lesbian", 8),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_09b",
    "label": "lexi_female_event_09b",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_08"),
        IsHour(20, 5),
        HeroTarget(
            IsRoom("map")
        ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            IsFlag("suggested_sex_work"),
            MinStat("love", 140),
            MinStat("lesbian", 8),
        ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_09c",
    "label": "lexi_female_event_09c",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_08"),
        IsHour(20, 22),
        HeroTarget(
            OnDate(),
        ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            IsFlag("paid_debt"),
            MinStat("love", 140),
            MinStat("lesbian", 8),
            OnDate(),
        ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_10",
    "label": "lexi_female_event_10",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_09"),
        HeroTarget(
            IsActivity("study_female")
            ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 160),
            MinStat("lesbian", 8),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_female_event_10_repeat",
    "label": "lexi_female_event_10",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_10"),
        HeroTarget(
            IsActivity("study_female")
            ),
        PersonTarget(lexi,
            MaxFlag("helped_study", 10),
            MinStat("love", 160),
            MinStat("lesbian", 8),
            ),
    ],
    "music": "music/roa_music/alley.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Activity(**{
    "name": "whore_work_with_lexi",
    "label": "whore_work_with_lexi",
    "conditions": [
        IsDone("lexi_female_event_09b"),
        IsTimeOfDay("evening", "night"),
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("fun", 3),
            Or(
                IsRoom("alley"),
                HasRoomTag("street"),
            ),
        ),
        PersonTarget(lexi,
        ),
    ],
    "music": "music/roa_music/alley.ogg",
    "once_day": True,
    "quit": False,
    "icon": "blowjob",
    "display_name": "Work the night with Lexi"
    })

    Event(**{
    "name": "lexi_female_event_10b",
    "label": "lexi_female_event_10b",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("lexi_female_event_09"),
        HeroTarget(
            IsActivity("whore_work_with_lexi")
        ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 160),
            MinStat("lesbian", 8),
        ),
    ],
    "music": "music/roa_music/alley.ogg",
    "once_day": True,
    "quit": False,
    "chances": 25
    })

    Event(**{
    "name": "lexi_female_event_11",
    "label": "lexi_female_event_11",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(
            HasRoomTag("pub"),
        ),
        PersonTarget(lexi,
            IsFlag("delay", False),
            MinStat("love", 180),
            MinStat("lesbian", 8),
            MinFlag("helped_study", 10),
            IsPresent(),
        ),
    ],
    "music": "music/roa_music/alley.ogg",
    "do_once": True,
    "quit": False
    })

    Event(**{
    "name": "lexi_female_event_11c",
    "label": "lexi_female_event_11c",
        "duration": 1,
        "conditions": [
            IsDone("lexi_female_event_09c"),
            HeroTarget(
                IsGender("female"),
                ),
            PersonTarget(lexi,
                Not(IsHidden()),
                MinStat("love", 180),
                IsFlag("delay", False),
                ),
            ],
        "music": "music/roa_music/alley.ogg",
        "do_once": True,
        "quit": False,
        })

label lexi_female_event_01:
    show bg street
    show lexi smile
    if not lexi.flags.walked_away:
        lexi.say "Hey there stranger."
        "I didn't expect her to be interested in talking with me. I mean...I know I'm attractive, but not so much to put her to shame, but maybe she's..."
        show lexi happy
        lexi.say "Well? Cat got your tongue or somethin'?"
        show lexi smile
        bree.say "No I...I'm not...sorry."
        show lexi normal
        lexi.say "Clearly."
        lexi.say "What's your name?"
        show lexi smile
        bree.say "[hero.name]... and yours?"
    else:
        "I honestly wasn't focusing on where I was going, just lost in my thoughts when she reappeared."
        show lexi happy
        lexi.say "[hero.name]!"
        show lexi smile
        bree.say "Oh...umm...hi. I'm sorry, I've forgotten your name..."
    show lexi normal
    lexi.say "The name's Lexi, hun."
    lexi.say "Were you out with your girlfriends, or friends tonight then?"
    show lexi wink
    show fx heart
    lexi.say "Or you're looking for someone to give you some pamperin'~"
    show lexi smile
    menu:
        "Out with friends":
            bree.say "Yeah basically."
        "Pamperin'":
            bree.say "Maybe. Maybe not. Why do you ask?"
            show lexi normal
            lexi.say "Just curious~"
    show lexi normal
    lexi.say "Did you have fun?"
    lexi.say "Did you, eh?"
    show lexi smile
    bree.say "Well uh...yeah. Yeah it was fun..."
    show lexi normal
    lexi.say "You seem like a cool gal to hang with, and I bet we can both party hard together..."
    show lexi smile
    menu:
        "Follow her":
            bree.say "Alright I'll bite, what you had in mind?"
            lexi.say "There's this underground party just further down this street."
            lexi.say "And my plus-one ditched, sooooo what say we not let it go to waste?"
            show lexi blank
            "There's at least 10 red flags in my head telling me \"BITCH RUN NOW\", but against my better judgement, what's my reason?"
            "Beats me, maybe it's because I'm new here and want to meet as many people as I can, maybe it's ‘cause the girl dragging me is hot enough for me to abandon all reason."
            bree.say "How far is this place?"
            show lexi normal
            lexi.say "It's just up ahead, don't worry, we're almost there."
            show lexi blank
            "As she kept dragging me I couldn't help myself but stare at her, especially her chest... A chest that easily puts any girl I know to shame."
            show lexi wink
            show fx heart
            lexi.say "Enjoying the view?"
            show lexi smile
            "Crap, I was so focused on her mountains I didn't see she noticed my staring."
            bree.say "Oh...uhm...I wasn't trying to stare...sorry..."
            "Smooth save, [hero.name]...nailed it, you dumb bitch."
            show lexi normal
            lexi.say "I know they were the first thing you looked at. It's okay, You don't have to be shy~"
            show lexi smile
            bree.say "Are you...sure?"
            lexi.say "I mean yeah. If we're being honest here, it ain't like you're lacking in that department either~"
            show lexi smile
            "She pointed towards my breasts as well with a playful smile, I guess she's no stranger to breast envy. Lucky me..."
            bree.say "Heh...you got me there. I was a little worried you'd take this the wrong way. After all, it's not like we even know each other that well-..."
            "She cuts me off before I finish."
            show lexi normal
            lexi.say "Oh come on, do we really have to?"
            lexi.say "I'll be honest, I usually ain't so forward with girls but...you seem to be worth the effort."
            show lexi smile
            bree.say "What about that party...?"
            show lexi normal
            lexi.say "It can wait, we're in no rush~"
            show lexi blank at right
            show danny at left
            with easeinright
            thug_say "Hey there, beautiful, how you doing?"
            lexi.say "Danny, thank god you're here!"
            $ thug_name = "Danny"
            bree.say "Lexi, the fuck is this? What is going on here?!"
            show lexi sadsmile
            lexi.say "Sorry Babe, nothing personal but I need the quick cash."
            show lexi blank
            bree.say "Wha-... Oh you bitch..."
            thug_say "Okay, I think it's about time we get this over with."
            if not hero.has_skill("martial_arts"):
                with vpunch
                "Before I can say anything else in the matter, I feel a hard smack on my face. This guy's size is no joke, and he hits like a brick. My fall is only softened by a few trash bags, my sight is blurry, sure, take my wallet, and hope you choke on it."
                if hero.money > 500:
                    $ hero.money -= 500
                else:
                    $ hero.money -= hero.money
                "In between my recovery I suddenly hear Lexi go of on the guy, not sure whether I'm hallucinating or not, I decide the best thing to do now is pretend I passed out and wait for them to move on."
                show lexi angry
                lexi.say "Danny what the fuck!"
                "She seems to sound angry, fucking seriously? You're upset at what exactly?!"
                thug_say "Lexi shut it! We got the money, now let's scram"
                show lexi annoyed
                lexi.say "You didn't have to hit her so hard, you could have just..."
                show lexi blank
                thug_say "Oh you care about that bitch now?! Either move your ass or stay here until the cops show, LETS GO!"
                "Lexi seems to weigh her options here, but in the end she follows Danny, but not before looking back at me with a concerned look... Definitely the weirdest night I ever had... I can't wait for this shitty night to be over."
                $ hero.grooming -= 5
                $ hero.energy -= 5
                $ hero.fun -= 5
            else:

                "All the training I had at the gym is not for nothing."
                play sound punch_hard
                pause 0.2
                show danny at vshake
                "I take a karate stance and hit him right in the stomach..."
                play sound body_fall
                hide danny with moveoutbottom
                "He falls to the ground like a sack of beans, vomiting his lunch..."
                thug_say "Urgh..."
                show lexi angry
                show fx exclamation at right
                lexi.say "Danny!"
                "As Danny was grabbing his gut and letting out a pained muffled scream, I kicked him in the crotch again just for good measure. Not taking the chance this fucker didn't have enough, and bolted out of that alley as fast as I could."
                lexi.say "Wait! [hero.name], Wait!"
                show lexi sad
                if hero.has_motor_vehicle:
                    bree.say "Oh fuck off, Lexi! There's no way I'm getting your friend here to the hospital."
                else:
                    bree.say "Oh fuck off, Lexi! There's no way I'm getting your friend here to the hospital. I don't even have a car."
                hide lexi with fade
                "I didn't even bother to listen to what else she was trying to say and just ran straight home, Jesus what a night."
                $ game.flags.thugfight += 1
                $ game.flags.danny_victory = True
            call injured from _call_injured_12
            $ lexi.flags.delay = TemporaryFlag(True, 1)
            return
        "Don't follow her":
            $ lexi.flags.walked_away = True
            $ lexi.flags.delay = TemporaryFlag(True, 1)
            hide lexi with fade
            "I leave the skank behind me as I walk away."
            $ hero.cancel_event()
            return

label lexi_female_event_02:
    show bg coffeeshop
    "The Legendary Sin, in liquid form. Nothing beats a good cup of coffee, especially after a wild night like I had."
    "Right after I received my order I got comfortable in those cozy sofa booths, because why not."
    "To be honest, I should do this more often, it's such a nice place...the atmosphere, the location, the people, the-wait what?!"
    show lexi
    lexi.say "One cappuccino to go with extra cream please!"
    "No way... that voice, Of all the places in this mall alone... right now all I can hope is to avoid any eye contact with her..."
    lexi.say "[hero.name]?!"
    "No. Freaking. Way..."
    bree.say "..."
    lexi.say "Oh shit! It's really you again!"
    show lexi smile casual at center, zoomAt (1.25, (640, 880)) with easeinright
    "I must be having a string of shitty luck or this is something karma is playing on me...she just *had* to notice me...and before I can even get up and make a run for it, there she comes to my direction, Hot-no Slutty as always!"
    show lexi at center, traveling (1.5, 0.3, (640, 1040))
    pause 0.3
    show lexi at center, zoomAt (1.5, (640, 1140)) with ease
    "Before I can even say anything she sat right in front of me, eyes beaming as if meeting me again was all she could think of in the last few hours' while I try my hardest not to slap her right there."
    show lexi normal
    lexi.say "So... Fancy meeting you here..."
    show lexi smile
    bree.say "What do you want?!"
    "All I can focus right now is how my blood boils at the gall she has. After what she pulled she has the nerve to walk to me and sit as if nothing happened!"
    "But for some reason, I'm not kicking her ass to the curb just yet, And as soon as she heard my tone she raised her hands in defense."
    show lexi sadsmile
    lexi.say "Hey! Easy easy, I swear I'm not here to cause trouble, I just wanna talk."
    show lexi blank
    bree.say "Talk? Last time you tried to \"talk\" to me ended with me pinned to a wall by your boy-toy an inch from getting mugged."
    if not game.flags.danny_victory:
        "Right before he kicked my ass and stole my wallet!"
    lexi.say "I know! And I'm sorry for that, I really am."
    if not game.flags.danny_victory:
        "Lexi pulls out my wallet and places it gently on the table in front of me."
        show lexi normal
        lexi.say "Here, I swear everything is there, besides your cash...Danny took that out and threw the rest after... Sorry."
        show lexi blank
        "I take my wallet back and go through it, yup everything is there, ID, driver's license...huh, what do you know, even my arcade membership card is still there."
        "Still, something feels off here, why would she go for all that trouble after she was part of stealing it in the first place?"
        bree.say "Why did you...?"
        "She cuts me off."
        show lexi normal
        lexi.say "Go for all that trouble after I was stealing from you?"
        lexi.say "I'll be honest... no idea, I just felt bad you got beaten up by Danny, especially after he said things won't get physical..."
        show lexi blank
        "The way she said the last sentence... almost as if she wasn't completely on board with Danny to begin with, still something tells me not to trust her at all because it'll be nothing but trouble down the line."
    else:
        bree.say "What do you want Lexi?"
        show lexi normal
        lexi.say "Listen, I've NEVER seen Danny take a beating like that, in fact I think you damaged his pride far worse than anything!"
        show lexi blank
        bree.say "Lucky me, so what? You're here to give me a heads up or something?"
        show lexi normal
        lexi.say "No you Dope! I already told you, I'm here to apologize! But it doesn't mean I can't give credit where it should."
        show lexi smile
        bree.say "Due."
        show lexi surprised
        lexi.say "What?"
        bree.say "The saying is ‘give credit where credit is due."
        show lexi wow
        lexi.say "Ohhhh...pretty and smart too..."
        show lexi smile
    bree.say "Lexi seriously, why do you think I want to be anywhere near you after last night?!"
    show lexi sadsmile
    lexi.say "...I didn't have a..."
    show lexi sad
    bree.say "Stop. Just stop. If you're going to say you didn't have a choice, just don't."
    show lexi sadsmile
    lexi.say "B-But it's true!"
    show lexi sad
    bree.say "Really?! What exactly wasn't your choice?! The seduction or the mugging?!"
    show lexi sadsmile
    lexi.say "I just...wanted... I'm not... I didn't..."
    show lexi blank
    "At this point we started to draw a bit of attention to ourselves, mainly due to me raising my voice."
    "Lexi goes quiet and just takes a few sips from her cup. She clearly doesn't know what to say to make me understand her side."
    "After what she put me through I have all the reasons to tell her to get out of my sight and never come back, but still..."
    if game.flags.danny_victory:
        "I'm not entirely sure I should, like something tells me I should give her another shot, after all what kind of a mugger come sit next to their target right after trying to mug them?"
    else:
        "I'm not entirely sure I should, like something tells me I should give her another shot, after all what kind of a mugger come sit next to their target right after mugging them?"
    menu:
        "Fuck off Lexi, I don't want to ever see you again":
            bree.say "You know what? Fuck Danny, and fuck you too! Get the hell away from me."
            show lexi sadsmile
            lexi.say "B-But... I swear I didn't mean to..."
            show lexi sad
            bree.say "Save it! Get the hell away from me, I never wanna see you or that piece of shit you have for a boyfriend again!"
            "Lexi gets up from the booth, defeated and clearly sad, I could swear I almost saw tears forming in her eyes, she looks at me one last time before going."
            show lexi sadsmile
            lexi.say "I'm really sorry... I am... I didn't want any of this to happen..."
            show lexi sad
            "I don't say anything to that, I just look away and avoid eye contact with her, but I can clearly hear the sadness in her voice, she was sincere... and just like that she's gone, back to what's going on with her life."
            "Whatever they may be, it's no longer my problem."
            $ lexi.set_gone_forever()
        "Fine, let's hear it":
            $ lexi.love += 4
            bree.say "...Fine."
            show lexi surprised
            lexi.say "F-Fine....what?"
            bree.say "Fine, I'll hear you out! But so help me if you bullshit me one more-"
            show lexi happy
            lexi.say "NO! Nothing like that I swear!"
            show lexi smile
            bree.say "So why the sudden change of heart?"
            show lexi sadsmile
            lexi.say "Danny said it'll be a simple mugging, nothing messy..."
            show lexi angry
            if game.flags.danny_victory:
                lexi.say "...But then he grabbed you and pinned you, if it wasn't for you being a badass I think he would have hit you."
            else:
                lexi.say "...But then he grabbed you and pinned you...after he punched you like that..."
            show lexi annoyed
            "Lexi rubs her shoulder and looks away."
            show lexi angry
            lexi.say "It didn't sit right with me... hitting a girl and all that..."
            show lexi sad
            bree.say "...Why is it so important? I think mugging is..."
            "Realization suddenly hit me like a pack of bricks."
            bree.say "Oh... Shit Lexi, he's..."
            show lexi bored
            lexi.say "Yeah... more than a few times."
            show lexi sad
            bree.say "Damn... he's scum."
            if game.flags.danny_victory:
                bree.say "Now I wish I had punched him harder."
                show lexi happy at startle
                "Lexi laughs lightly at my last remark. Strange, she's kinda cute now that I got a better look at her."
            show lexi normal
            lexi.say "So yeah, there's that. And I'll say it again, I'm so sorry for what happened, I hope you'll forgive me..."
            show lexi smile
            "Taking a moment to consider, Lexi does seems sincere in her apology, and when you add the fact that Danny was probably forcing her to be the bait for his little operations it all makes sense now."
            "I think she needs more positive people around her, plus if I'm being completely honest with myself, she IS cute... I just think we started on the wrong foot."
            bree.say "I'll forgive you on one condition..."
            show lexi blank
            "Lexi eyes me with suspicion, unsure of exactly what I mean, but I get the feeling it's not the first time she was given a condition before participating with something."
            "Well I'm not Danny."
            show lexi bored
            lexi.say "... which is?"
            show lexi blank
            bree.say "We get more coffee together, and often."
            show lexi surprised
            lexi.say "Do you mean...?"
            bree.say "Yup."
            show lexi happy at center, zoomAt(2.0, (640, 1340)) with vpunch
            $ lexi.love += 2
            "Without further warning, Lexi jumped from her seat and wrapped her arms around me, hugging me as tight as she could, her breasts squishing against mine."
            bree.say "(Damn she's gifted)"
            bree.say "H-Hey, easy! People are looking over here."
            show lexi smile at center, traveling(1.5, 0.3, (640, 1140))
            "She let's go of me smiling as if she just won something precious."
            show lexi normal
            lexi.say "Oh sorry! I just got excited is all."
            show lexi smile
            bree.say "I can tell."
            "As we get up and prepare to head out Lexi jumps for another quick hug again, before letting me go, but not before pickpocketing my phone from me."
            bree.say "Lexi..."
            show lexi normal
            lexi.say "Don't worry! I just want to put my number in your contacts"
            show lexi smile
            "She tries a few more times to unlock the phone, after a few attempts she just points the phone at me."
            show lexi normal
            lexi.say "Make it open!"
            show lexi smile
            "I just chuckle a bit and use my fingerprint to unlock it, she quickly turns the screen back to face her and types her number in."
            bree.say "Done?"
            show lexi normal
            lexi.say "Almost, just missing one thing..."
            show lexi smile
            bree.say "Which is?"
            hide lexi
            with screenshot
            play sound cameraclick
            show dick reactions nodick lexi smile nobreemc as lselfie zorder 2 at flip, center, zoomAt(1.2, (300, 860))
            show dick reactions nodick bree nobreemc mock as bselfie zorder 1 at center, zoomAt(1.2, (980, 860))
            "Without another word, she grabs me again, pressing her head next to mine and takes a selfie of the two of us with my phone."
            scene bg coffeeshop
            show lexi wink at center, zoomAt(1.5, (640, 1140))
            with fade
            lexi.say "There! Now it's perfect!"
            show lexi smile
            "She hands me back my phone with a smile."
            $ hero.smartphone_contacts.append("lexi")
            bree.say "Heh..."
            show lexi wink
            show fx heart
            lexi.say "Just don't drool all over it~ I know I'm irresistible, but try~"
            $ lexi.unhide()
            $ lexi.flags.noproposedate = True
            $ lexi.flags.delay = TemporaryFlag(True, 3)
    scene bg black with dissolve
    return


label lexi_female_event_03:
    show bg livingroom
    "After our meeting at the coffee shop, Lexi and I talked quite a bit. She seems like a good person in bad circumstances. She's lucky I find her both hot and cute."
    "But I do wonder if she feels the same? I wanna ask her out but I'm not sure whether or not it's a good idea."
    play sound cell_vibrate loop
    "My train of thought is derailed as my phone begins ringing. Speak of the Devil."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Lexi")
    if not result:
        $ hero.cancel_event()
        $ lexi.love -= 2
        return
    if lexi.love.max < 40:
        $ lexi.love.max = 40
    bree.say "Hey Lexi! What's up?"
    lexi.say "[hero.name]! Where are you at?"
    bree.say "Nowhere special; just at home watching a movie, why?"
    play sound door_knock
    "Before I get a reply I hear a knock on the door. I go to open it to see who it is..."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show lexi happy at center, zoomAt(1.25, (640, 900))
    with wiperight
    lexi.say "'Cause I came to hang out!"
    show lexi smile at center, traveling(2.0, 0.3, (640, 1340))
    "There she stands, arms in the air declaring her arrival before jumping on me for a hug. She's...just adorable when she wants to be, trying not to lose my balance I hug her back."
    bree.say "H-hey you, well that was unexpected. How have you been?"
    show lexi smile at center, traveling(1.5, 0.3, (640, 1040))
    "She released me from the hug and now faces me with a smile, that seductive smile... And those skinny tight outfits she always wears...Focus [hero.name]! Focus!"
    show lexi normal
    lexi.say "Great! I was in the neighbourhood and wanted to see you~"
    show lexi smile
    bree.say "Oh great, well I was about to do a marathon of The \"Star Battles\" movies. You're welcome to join me."
    show lexi surprised
    "Lexi looked at me with a puzzled look, something tells me watching sci-fi movies isn't exactly her thing."
    show fx question
    lexi.say "Star Battles? Isn't that like those super geeky-ass movies with flaming swords and stuff? Don't they have those new movies playing on cinema now?"
    show lexi blank
    bree.say "NO! No no no...those abominations have nothing to do with the ones I watching!"
    "And they never will."
    "The last thing I'll do is show Lexi those garbage movies."
    bree.say "I was about to order some pizza and open some beers, you joining?"
    show lexi normal
    lexi.say "Sure!"
    scene bg livingroom
    show watch tv lexi
    with fade
    "We sat down on the couch and started our \"Star Battles\" marathon, Lexi was sitting close to me, rather too close some would say but I don't mind...she's so cute."
    "**One awesome trilogy later**"
    "And there it was, that amazing trilogy all over again, as soon as the credits rolled up on the third movie, I snapped back to reality."
    "We both were into the movie so much I don't think either of us noticed the position we were in by the end of it. Lexi was leaning into me."
    scene bg livingroom
    show lexi blank at center, zoomAt(1.5, (640, 1040))
    with fade
    "She still hasn't said anything. The silence dragging on into awkwardness. Maybe she doesn't like those kinds of movies?"
    bree.say "So... what did you think?"
    show lexi surprised
    lexi.say "That..."
    lexi.say "was..."
    show lexi happy
    show fx exclamation
    lexi.say "Awesome!!!"
    show lexi smile
    "Ok...definitely not what I expected her to say."
    bree.say "R-Really? You liked that?"
    show lexi normal
    lexi.say "Liked it?! Babe, I LOVED it! I mean the battles, the characters, the twists?! I did NOT see half of this shit coming I swear!"
    show lexi smile
    bree.say "I'm glad to hear you enjoyed it so much, these are some of my most favourite movies."
    bree.say "Have you really never see them?"
    show lexi bored
    lexi.say "No, never. Danny usually sees movies that start and end the same...."
    show lexi annoyed
    bree.say "Fuck-ton of explosions, hot girls fucking hot dull guys, race cars, guns and drugs?"
    show lexi bored
    lexi.say "Bingo!"
    show lexi normal
    lexi.say "I can't believe it, I actually cared what happened to these guys!"
    show lexi smile
    "She catches me by surprise and gives me a kiss on the cheek."
    bree.say ".... I-I guess you really enjoyed our movie date.."
    show lexi wink
    show fx heart
    lexi.say "Get me drunker and we might find out how much I enjoy being with you~"
    show lexi normal blush
    lexi.say "I... I think I'll go back to my place, ya'know?"
    show lexi smile
    "I could swear I see a flustered Lexi before me. There's no hiding her blush, and I'm pretty sure I'm redder than a tomato."
    "Lexi never had any female friends before, she might just be grateful that we spend time together or maybe..."
    "Is she leading me on?"
    "Still I might be reading the situation wrong, and the last thing I want is to wreck our friendship when it's just started."
    "But something tells me she doesn't really want to go back to her place, maybe because of Danny? Or maybe she's just lonely? I..."
    menu:
        "You can stay, I don't mind":
            $ lexi.love += 4
            bree.say "Uhm Lexi... you're more than welcome to stay. In fact, I am totally down to turn this into a... sleepover?"
            show lexi surprised
            "As soon as I suggest that, Lexi's eyes shot up to me as if I offered her free money or something."
            show lexi happy
            lexi.say "C-Can I?! YAY!!!"
            show lexi at center, zoomAt(2.0, (640, 1340)) with hpunch
            "She jumped and hugged me again, making me lose balance and fall over on the couch again, there she is laying on top of me."
            bree.say "L-Lexi..."
            show lexi normal
            lexi.say "Yeah?"
            show lexi smile
            bree.say "Your boobs are pressing on mine..."
            show lexi normal
            lexi.say "I don't mind~ I wanna stay like that for a few..."
            show lexi smile
            bree.say "*sigh* I can't argue with you, can't I?"
            show lexi smile at center, traveling(1.5, 0.3, (640, 1040))
            "Lexi finally let go of me and helped me back to sit on the couch, we looked at each other and smiled."
            "After all, there's no need to rush our night, we went into my room and continued watching random movies until late into the evening."
        "Yeah it's getting late":
            bree.say "Yeah it's getting late, I didn't even notice the time."
            show lexi sadsmile
            lexi.say "Y-Yeah, but [hero.name], I gotta say, this was a blast of a hang out~"
            show lexi blank
            "She sounded a bit disappointed, as if she didn't want us to part so fast. Lexi collects her things and head to the door, naturally I escort her to the door."
            scene bg house
            show lexi normal at center, zoomAt(1.25, (640, 900))
            with fade
            lexi.say "Thanks for the awesome date [hero.name]!"
            show lexi smile
            "As she hugged me again, I could hear genuine appreciation in her voice. And date? She's always such a tease, but is she just teasing now?"
            bree.say "Oh? It was a date?~"
            show lexi bored blush
            lexi.say "D-Do you want it to be...?"
            show lexi blank
            bree.say "M-Maybe..."
            show lexi wink
            show fx heart
            lexi.say "Then I look forward for our next one~"
    $ lexi.flags.delay = TemporaryFlag(True, 3)
    $ lexi.flags.noproposedate = False
    scene bg black with dissolve
    return

label lexi_female_event_04:
    show bg livingroom
    bree.say "It's so freaking hot, I swear this weather just keeps getting worse by the week."
    "[mike.name] and Sasha almost decided to put a rule around the house regarding our A/C Unit in the shared spaces."
    "That thing is a truly amazing, but we don't want to end up with an electricity bill through the roof."
    "As I arrive home my phone rings; it's Lexi."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Lexi")
    if not result:
        $ hero.cancel_event()
        $ lexi.love -= 2
        return
    if lexi.love.max < 60:
        $ lexi.love.max = 60
    bree.say "Hey Lexi! How are you?"
    lexi.say "Where're you at?"
    bree.say "I just got home, why?"
    lexi.say "I thought I'll come over and we could hang out."
    "Now that I take a moment to consider it, the house is empty. [mike.name] is at a dinner party with his company, and Sasha is out for the night. The house is all at my disposal..."
    bree.say "(It's so quiet)"
    bree.say "Sure, come on over."
    stop music fadeout 0.1
    play sound hitting_bushes fadein 0.2 fadeout 0.2
    "As I'm about to hang up, I suddenly hear some noise coming from the pool area outside."
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    if hero.morality < 0:
        bree.say "The fuck?"
    else:
        bree.say "The hell?"
    lexi.say "What is it?"
    bree.say "Think I heard something from our yard, mind staying on call with me?"
    lexi.say "S-sure... what do you think it is?"
    bree.say "It's probably nothing but I still wanna check it out."
    lexi.say "Ok I'm with you."
    show bg pool with fade
    "I step outside to light the backyard, there's that noise again. I probably watched too many horror movies, but this is the part where I'm getting murdered... or decapitated..."
    if hero.morality < 0:
        "Gee, thanks brain... fucking asshole. As soon as I press the light switch my heart stops."
    else:
        "Gee, thanks brain... so helpful. As soon as I press the light switch my heart stops."
    play sound hitting_bushes
    show lexi a angry nophone at dark, dark, center, zoomAt(1.5, (640, 1040)), hshake
    lexi.say "BOO!"
    with vpunch
    if hero.morality < 0:
        bree.say "HOLY FUCKSHIT, NOT TODAY!"
    else:
        bree.say "HOLY CRAP, NOT TODAY!"
    hide lexi
    show lexi a angry nophone at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "Lexi jumps out from behind the hot tub and surprises me. I swear I see my life flash before my eyes."
    play music "music/roa_music/alley.ogg" loop
    show lexi happy at startle
    "Meanwhile this stunning bitch is giggling at her successful prank... stupid, childish... Adorable..."
    bree.say "Jesus Christ Lexi, you nearly gave me a heart attack!"
    "Still chuckling softly to herself Lexi straightens up and turns to me."
    show lexi normal
    lexi.say "Sorry, I got here before you, and thought this was an excellent opportunity to scare ya a bit~"
    lexi.say "You know like in that movie where she goes out to the backyard and that masked fella was going to town on her."
    show lexi smile
    bree.say "You know that doesn't narrow down the list of movies you wanted to reference..."
    show lexi a happy at center, zoomAt(2.5, (640, 1640)) with hpunch
    "Lexi hugs me and rubs her cheek against mine."
    show fx heart
    lexi.say "Sorry, I'm sorry~ please forgive me."
    show lexi smile
    bree.say "Alright, alright..."
    bree.say "How did you get in anyway?"
    show lexi a normal at center, zoomAt(1.5, (640, 1040))
    lexi.say "I bumped into Sasha before she left, she was cool with letting me stay and wait for you in the house."
    show lexi happy
    lexi.say "Don't worry I didn't steal anything~"
    show lexi happy at startle
    "She giggled, making me chuckle a little at that remark."
    show lexi smile
    "I scan the table next to the pool and notice that Lexi has already made herself comfortable, she's been here for a while it seems. And that she also has brought some beers and snacks and....a bag of weed?"
    bree.say "Lexi is that...?"
    show lexi normal
    lexi.say "Oh.... Yeah, it's just weed I swear, I'm not doing any hardcore drugs... I thought we might... smoke some and go swimming~"
    show lexi smile
    "I never really tried weed before, but at this point it's as popular as alcohol. Still I'm not sure I wanna try it, but Lexi does seem to want to smoke some with me. I..."
    menu:
        "Sure, roll one":
            $ lexi.flags.smokedweed = True
            bree.say "Sure why not, might as well be with you."
            show lexi normal
            lexi.say "You're the best!~"
            $ hero.morality -= 4
        "I'll pass":
            $ lexi.flags.smokedweed = False
            bree.say "I'll pass Lexi, but go right ahead and roll one for you'. I'll just drink extra~"
            show lexi sadsmile
            lexi.say "Oh.. Alright, no biggie, if it's not your thing then it's not your thing."
            $ hero.morality += 2
    show lexi smile
    "Lexi starts rolling a joint as I put my bag aside and open two beers. Placing one next to her and start drinking mine, I'm about to head inside to switch to a bikini when Lexi stops me."
    scene bg livingroom
    show lexi normal nophone at center, zoomAt(1.5, (640, 1040))
    with fade
    lexi.say "Where are you going?"
    show lexi smile
    bree.say "Inside to switch to a bikini, did you bring one?"
    show lexi wink
    lexi.say "I wasn't planning on wearing one~"
    show lexi smile
    bree.say "Y-You mean you want us to..."
    "That devious minx. I gotta give her credit for that, seducing is one of her best qualities."
    show lexi happy
    lexi.say "Yyyyep~ I want us to go on a little skinny dipping~"
    show lexi smile
    bree.say "Really?"
    show lexi normal
    lexi.say "Really really."
    scene smoking pot
    show smoking pot lexi lexismoke
    with fade
    "Before I can say anything else, she lights up her crafted roll, takes a big puff from it and passes it to me."
    if lexi.flags.smokedweed:
        show smoking pot lexi lexiexhale lexiopen breesmoke -lexismoke
        "I take a few puffs and choke a bit on it, making her giggle a little bit."
    else:
        show smoking pot lexi lexiexhale lexiopen breehold -lexismoke
        "I just hold it for safekeeping."
    scene bg livingroom
    show lexi smile underwear nophone
    with fade
    "Lexi then begins to strip naked..."
    bree.say "(gods above)"
    show lexi naked with dissolve
    if lexi.flags.smokedweed:
        "Just when I thought she couldn't get more beautiful... she gently takes the joint back from my lips and goes sit by the poolside."
    else:
        "Just when I thought she couldn't get more beautiful... she gently takes the joint back from me and goes sit by the poolside."
    "I quickly lose my own clothes and move to join her; not before catching her looking me over, and loving what she's seeing..."
    show lexi flirt
    lexi.say "Anyone ever told you you're hot as hell?"
    show lexi smile blush
    bree.say "Anyone ever told you the same?"
    show lexi happy at startle
    "I couldn't help but blush at her comment, we both laughed together over our shitty inside joke."
    scene bg pool
    show lexi naked smile nophone
    with fade
    if lexi.flags.smokedweed:
        "Right now I'm loving this, and the weed started to kick in as well. Everything seems so...chill all of a sudden."
    else:
        "This is definitely a fun experience, kinda makes me wonder how I would have felt if I was smoking with her too now."
        "Lexi then leans on me. I can feel her breasts rubbing on the side with mine..."
        bree.say "(this is... nice)"
    show lexi normal
    lexi.say "It's kicking in~"
    show lexi smile
    if lexi.flags.smokedweed:
        bree.say "Yeah I'm feeling it too."
        show lexi normal
        lexi.say "Just in time, we're almost done with the joint. I'm hopping in the water."
    play sound water_splash
    hide lexi with moveoutbottom
    "Lexi jumps into the pool, diving a bit before surfacing. Looking at me and motioning for me to join her, I finish the last of my beer and do just that."
    scene swimmingrace_bg_03 at center, zoomAt(1.75, (1000, 1040)), blur(5) with fade
    if lexi.flags.smokedweed:
        "Before joining her I'm just floating on the water, everything feels good...that weed really calmed me down immensely. My relaxation suddenly stops as I feel something biting me... on the ass."
    else:
        "Before joining her I'm just floating on the water, everything feels good. I'm just relaxing...right up until I feel something biting me... on the ass."
    with vpunch
    bree.say "Ouch! What the hell!?!"
    show lexi a naked happy nophone at center, zoomAt (2.0, (640, 1300)) with moveinbottom
    show lexi a at vshake, center, zoomAt (2.0, (640, 1300))
    "Lexi pops up from the water giggling, that bitch just bit me in the ass... R-Really?"
    show lexi a at startle, center, zoomAt (2.0, (640, 1300))
    lexi.say "Shark attack, Muhahaha!"
    bree.say "Bitch..."
    with hpunch
    "I say mid chuckle and splash her, laughing for a second before getting splashed back myself, we go back and forth splashing each other, before I grab both her arms."
    show lexi normal
    lexi.say "Oh noooo, I'm all caught! Save me~"
    show lexi a smile
    "We both look at each other for a few seconds, not saying a word to each other...just smiling."
    show lexi a normal blush
    lexi.say "H-Have you ever been... like this... with a girl?"
    show lexi smile
    bree.say "N-not really. Have you?"
    show lexi sadsmile
    lexi.say "Not exclusively... y'know always as a part of..."
    show lexi smile
    bree.say "Right..."
    show lexi normal
    lexi.say "[hero.name]... I really like this... this might be the weed talking but I-I... I kinda want you to kiss me.."
    show lexi smile
    "Did she seriously just ask that? I mean, I'm still not sure what we really are, but whenever I'm with her, everything feels right. Like it's supposed to happen the way I wanted it to happen, eh to hell with it, I'm going for it."
    hide lexi
    show lexi kiss naked
    with fade
    $ lexi.flags.kiss += 1
    "Without much thinking I pressed my lips against her, they're so soft, so tender..."
    "Lexi wastes no time and shoves her tongue into my mouth, wrapping her arms around me to pull me deeper as she grinds against me."
    "My hands begin tracing her up and all over, caressing her butt, her back, the back of her head."
    hide lexi
    show lexi a naked nophone smile blush at center, zoomAt (2.0, (640, 1300))
    with fade
    "We break away and gaze into each other's eyes, her smile lighting up her face."
    show lexi normal
    lexi.say "You're a great kisser... it's almost addicting."
    show lexi smile
    bree.say "You're not so bad yourself."
    show lexi normal
    lexi.say "I-I'm sorry... if it feels forced... I just... I really..."
    show lexi smile
    menu:
        "Take it further":
            "I can understand her second thoughts, just shows Lexi really doesn't want to mess things up with... whatever it is we have going on."
            "But I'd be lying if I said I don't want her, I want more of her... and this is one of those crossroads where I'm giving a choice, like those RPG games, and if I learned one things is that you always need to risk it to get biscuit, even if you might fail."
            bree.say "Lexi...Honey, I want you to sit on the poolside again."
            show lexi surprised
            lexi.say "W-what?"
            bree.say "Do you trust me?"
            lexi.say "Y-yeah, what's this about [hero.name]?"
            bree.say "I'm going to show you I'm serious about this... and that I want it just as much as you do."
            $ lexi.love += 1
            "I give her a smile."
            bree.say "Now be the adorable good girl that you are, and sit on the poolside."
            lexi.say "Yes... baby."
            scene bree cunnilingus lexi
            show bree cunnilingus lexi backward nomc pool
            with fade
            "Lexi obeys and sit on the poolside again, her wet naked body is just everything I want right now, seeing those huge naked breasts of hers, her beautiful butt and that wet... Focus [hero.name]!"
            bree.say "Spread your legs, show me that beautiful pussy..."
            "Lexi smiles seductively and opens up her legs, showing me all of herself. She's so beautiful. She's so sexy..."
            "And she's mine. I smile back up at her before going down to do my work. Gently I kiss along on the sides, slowly making my way lower from her leg towards that sexy shaved entrance."
            show bree cunnilingus lexi lick -nomc
            "She's moaning slightly, letting them escape every few seconds. Finally reaching her prize, I kiss her lips over and over, licking, probing at the entrance."
            show bree cunnilingus lexi lick up
            "She is beginning to shake and shudder. I reach up, and interlock her hand with mine; she knows I'm with her, she knows I'm there to love her."
            $ lexi.love += 1
            show bree cunnilingus lexi lick middle
            lexi.say "Ohhhh.... Ahhhh... [hero.name].... D-Don't... stop... don't you dare stop"
            show bree cunnilingus lexi lick down
            "It's all I need to hear, I pick up the pace and lick her more, letting my tongue slip inside before pushing two of my fingers inside gently. Thank God I did my nails before!"
            show bree cunnilingus lexi lick middle
            lexi.say "AHHHH, yes! I love this! [hero.name] I love it so much!"
            show bree cunnilingus lexi lick up pleasure
            "Lexi looks at me and I meet her gaze as well, while her pussy is still in my mouth, I kiss her down there a few more times before stopping, and smiling at her."
            show bree cunnilingus lexi lick middle
            bree.say "Still think you're forcing anything?"
            show bree cunnilingus lexi lick down
            lexi.say "No babe... B-But I do want more."
            bree.say "Coming right up~"
            lexi.say "You have no idea how... AIIIEEE!!!"
            "Without much of a warning I pick back up where I left off, picking up the pace while I'm at it."
            "My tongue traces over her folds, my fingers go back and forth. Lexi is just laying back as her whole body is twitching, I can tell she's close..."
            show bree cunnilingus lexi lick middle frontward ahegao with vpunch
            lexi.say "[hero.name] I-....I'm CUMMING!"
            "I give her a thumbs up with my free hand and giving her the one final show to send her to a galaxy far far away. She jolts upright, grabbing the back of my head and pushing me deeper into her pussy and between her legs."
            show bree cunnilingus lexi lick back with vpunch
            "With a yelp and a moan, she releases all over my mouth. Laying back down on the concrete floor on the poolside, panting and trying to regain her breath."
            "I step out of the pool and lay next to her, and then over her. Rubbing my body against hers, pressing myself on top of her, I lean in to kiss her, my mouth is dripping with her fluids. The kiss deepens for a moment, and then I break away."
            show bree cunnilingus lexi nomc front frontward pleasure
            lexi.say "T-that...was..."
            bree.say "Me too~"
            scene bg pool
            show lexi normal blush naked nophone at center, zoomAt (2.0, (640, 1300))
            with fade
            lexi.say "C-can I...?"
            bree.say "You always can, besides... you're gonna return the favor in the shower~"
            show lexi surprised
            bree.say "Yeah I can tease back too."
            show lexi happy
            lexi.say "For you babe... Any time and always."
            show lexi smile
            "I smile gently, leaning in for another kiss. This is by far the best nightly swim I ever had."
            $ lexi.sexperience += 1
        "Reassure her" if hero.charm >= 20:
            $ lexi.love -= 1
            bree.say "I'm flattered, I really am. but I'm not sure if I'm ready for this."
            show lexi sad
            "Lexi looks away briefly, but I can see she's not too hurt by my words."
            show lexi smile
            "Hopefully this won't sour the rest of our evening."
        "Be awkward" if hero.charm < 20:
            bree.say "I-it's okay, I just don't feel ready for this yet..."
            show lexi sadsmile
            "She looks down with a sad smile, but accepts my words. Backing off, we spend the night in a bit more calm a fashion than perhaps she had intended."
            $ lexi.love -= 4
    scene bg black with dissolve
    $ lexi.flags.nodate = False
    $ lexi.flags.nokiss = False
    $ lexi.flags.delay = TemporaryFlag(True, 1)
    return

label lexi_female_event_04b:
    if lexi.love.max < 60:
        $ lexi.love.max = 60
    scene bg mall1
    "The Mall's always this busy when it's getting so close to the festive season."
    "The place is packed with shoppers, bustling this way and that, laden with gifts."
    "I've been here a hundred times before when it was this bustling and noisy."
    "But today feels just a little bit different, and that's because of who's with me."
    "I'd normally have asked one of my housemates to come along for some company."
    "But Sasha's at band practice and [mike.name] has some dumb corporate event to attend."
    "So rather than go alone, I called Lexi up and she jumped at the chance to come."
    show lexi a casual smile at center, zoomAt(1.5, (640, 1040)) with dissolve
    "I thought it might be awkward at first, you know?"
    "I don't really know Lexi that well, and my feelings for her are a little confused."
    "But this is the perfect chance to change all of that, to get to know her better."
    "And so far it's working out great."
    "Lexi and I are flitting from store to store, chatting like old friends."
    "We gaze through the window of one store and then dip into the next."
    "Anyone watching us would think that we'd know each other since forever."
    bree.say "Ooh..."
    bree.say "I need to nip in here, Lexi!"
    bree.say "They do this make-up that Sasha just loves to death!"
    show lexi a happy at startle
    "Lexi giggles at this and cocks her head on one side."
    lexi.say "That figures - she looks like death most of the time too!"
    show lexi a normal
    lexi.say "So what kind of make-up is it?"
    lexi.say "The stuff they use on corpses in the morgue?"
    show lexi smile
    "At first I stare at Lexi in silence, my mouth hanging open."
    show lexi a happy
    "But then, as hard as I try, I realise that I can't help laughing."
    "I know what Lexi just said wasn't really fair to poor Sasha."
    "But it's such a thrill to hear someone saying what they think for a change."
    "Lexi doesn't live with Sasha twenty-four seven."
    "I guess that means she doesn't have to bite her tongue when she talks about her either!"
    show lexi a normal
    bree.say "Lexi!"
    bree.say "That is so mean!"
    bree.say "But...I guess Sasha DOES wear some crazy make-up!"
    bree.say "All that black around her eyes...sometimes she reminds me of a racoon!"
    show lexi a happy at startle
    "Now it's Lexi's turn to burst out laughing."
    lexi.say "Sasha the Trash Panda!"
    lexi.say "I love it!"
    show lexi smile
    "I still feel more than a little guilty."
    "But I'm having so much fun with Lexi that I can't help myself."
    bree.say "Okay, okay, okay..."
    "I use a hand to fan my face, trying to calm down again."
    bree.say "Back to the serious business of shopping, Lexi."
    bree.say "[mike.name] said his underwear was wearing out on him."
    bree.say "So I figured I'd get him some nice new shorts, yeah?"
    show lexi surprised
    lexi.say "Hmm..."

    lexi.say "Did you ask him what size he takes?"
    show lexi blank
    if not mike.sexperience:
        "As soon as I hear Lexi's question, I'm stumped."
        bree.say "No...I didn't!"
        bree.say "I suppose we'll just have to guess."
        show lexi smile
        "Lexi shakes her head and smiles."
        show lexi normal
        lexi.say "Ah, he'd have lied about the size of his junk anyway."
        lexi.say "And who's got a microscope in their pocket to check?!?"
        show lexi wink
        "Lexi crooks her little finger and squints her eyes at it."
        show lexi smile
        "And again I find myself laughing at her making fun of my housemates."
        "I cover my mouth, failing miserably to hide my laughter."
        bree.say "Oh god..."
        bree.say "[mike.name]'s so obsessed with his cock!"
        bree.say "I swear, it's like his second brain or something!"
        show lexi happy
        lexi.say "His only brain, more like!"
        show lexi smile
    else:
        bree.say "Well..."
        if hero.morality <= -25:
            if mike.flags.dicksize == "hung":
                bree.say "There's no wonder he's wearing out his shorts."
                bree.say "His cock's such a monster, it's a wonder they can even handle it!"
            elif mike.flags.dicksize == "smalldick":
                bree.say "Take my advice and look for the smallest size they've got."
                bree.say "Because he's not packing much of punch down there, believe me!"
            else:
                bree.say "I mean, it's nothing special..."
                bree.say "At least in terms of size!"
        elif hero.morality >= 25:
            if mike.flags.dicksize == "hung":
                bree.say "It's...erm...well..."
                bree.say "I suppose that it is quite large!"
            elif mike.flags.dicksize == "smalldick":
                bree.say "Okay, don't ask me how I know this..."
                bree.say "But I don't think he needs the larger sizes!"
            else:
                bree.say "Oh, I haven't seen too many of them."
                bree.say "But I think his is a pretty ordinary size."
        else:
            if mike.flags.dicksize == "hung":
                bree.say "I mean...it is really big."
                bree.say "So I wonder if he has trouble finding shorts big enough to fit!"
            elif mike.flags.dicksize == "smalldick":
                bree.say "Oh, I wouldn't bother looking at the larger sizes."
                bree.say "Take it from me - he doesn't need them!"
            else:
                bree.say "We shouldn't have too much trouble finding some that fit."
                bree.say "I mean, he's not exactly exceptional in that department."
    "I shake my head, deciding it's time we stopped this."
    "Sure, I'm having a great time joking with Lexi."
    "But I don't want to make a habit of this."
    show lexi smile with fade
    "So I stop in front of a shop selling cute underwear."
    bree.say "Oh..."
    bree.say "I wish I had a figure like your's, Lexi."
    bree.say "You could SO pull something like that off!"
    show lexi normal
    lexi.say "HA!"
    lexi.say "Stop trying to put yourself down, [hero.name]!"
    lexi.say "Your tits are every bit as big as mine!"
    show lexi smile
    bree.say "I...I didn't mean..."
    show lexi normal
    lexi.say "Well I DO mean it."
    lexi.say "You're one hot chick, [hero.name]!"
    show lexi smile
    "I can already feel myself beginning to blush."
    "I always thought that Lexi might be into girls as well as guys."
    "So does that mean that...that she might be into me too?"
    bree.say "Thanks, Lexi!"
    bree.say "You're pretty sexy too!"
    bree.say "I mean pretty...I mean sexy!"
    show lexi wow
    lexi.say "Oops..."
    show lexi flirt
    lexi.say "This just got weird, didn't it?"
    show lexi smile
    "I give Lexi a nod and a pained smile."
    "She nods too, and we hurry off to do the rest of our shopping."
    scene bree_lick_lexi_bg_park with fade
    pause 0.2
    show lexi a casual smile at center, zoomAt(1.5, (680, 1040)) with easeinright
    "Neither of us mentions it again until we're in the parking lot."
    "That's when Lexi stops in her tracks."
    show lexi normal
    lexi.say "Hey, I just remembered..."
    lexi.say "I have something that'll take the edge off!"
    show lexi blank
    bree.say "Erm..."
    bree.say "I thought the rest of the shopping was supposed to do that, right?"
    bree.say "I mean, things are less weird now, aren't they?"
    "Lexi seems to be ignoring me as she roots around in her bag."
    "And then she triumphantly holds up what she was looking for."
    show lexi normal
    lexi.say "Tada!"
    show lexi smile
    bree.say "Is...is that what I think it is?"
    bree.say "Is that cannabis?!?"
    show lexi normal
    lexi.say "Aw, come on, [hero.name] - lighten up!"
    show lexi bored
    lexi.say "It's like the smallest joint in the world."
    show lexi normal
    lexi.say "You won't even know you smoked it, trust me."
    show lexi smile
    menu:
        "Sure, roll one":
            $ lexi.flags.smokedweed = True
            "I'm really not sure whether this is a good idea or not."
            "But then Lexi's got to be more experienced with this kind of stuff, right?"
            "And if she thinks it's okay, then it probably really is okay."
            bree.say "O...okay, Lexi."
            bree.say "I'll give it a try."
            show lexi normal
            lexi.say "Sure you will, [hero.name]!"
            show lexi smile
            "I watch as Lexi lights the..."
            "What did she call it - a joint?"
            "She takes a couple of puffs and holds the smoke in her lungs."
            "Then she lets it out and passes the joint to me with a sigh."
            show lexi normal
            lexi.say "Man...I needed that!"
            show lexi smile
            "I smile and try my best to copy what Lexi just did."
            with vpunch
            with vpunch
            "It makes my eyes water, and I can't help coughing."
            "But at least I don't puke up after one lungful."
            bree.say "Huh..."
            bree.say "I don't feel any..."
            bree.say "Whoa...my head...it's floating!"
            show lexi happy at startle
            "Lexi laughs and takes a second pull on the joint."
            lexi.say "Don't worry, [hero.name]."
            lexi.say "That's supposed to happen!"
            show lexi smile
            $ hero.morality -= 4
        "I'll pass":
            $ lexi.flags.smokedweed = False
            "I like Lexi a hell of a lot, but I'm not doing drugs with her."
            "And definitely not in the mall parking lot either!"
            bree.say "Nah, Lexi - I'll pass."
            bree.say "But you go right ahead."
            show lexi normal
            show fx question
            lexi.say "You sure?"
            lexi.say "Okay, whatever..."
            show lexi smile
            "I watch as Lexi lights the..."
            "What did she call it - a joint?"
            "She takes a couple of puffs and holds the smoke in her lungs."
            "Then she lets it out and passes the joint to me with a sigh."
            show lexi normal
            lexi.say "Man...I needed that!"
            show lexi smile
            $ hero.morality += 2
    "Smoking some of the joint really seems to have helped Lexi relax."
    "She seems more chilled out and at ease than she has all day."
    scene bree_lick_lexi_bg_park at center, zoomAt (1.4, (580, 1000))
    show lexi a smile at center, zoomAt (1.0, (680, 720))
    with dissolve
    "Lexi leans back against a car and regards me with a knowing look in her eye."
    show lexi normal
    lexi.say "So, [hero.name]..."
    show lexi smile
    bree.say "Ah, yeah, Lexi?"
    show lexi normal
    lexi.say "Isn't it time we talked about this thing we have going on?"
    show lexi wink
    "Lexi raises a knowing eyebrow as she says this."
    show lexi smile
    "Oh god...she knows...she knows that I have feelings for her!"
    "Well, maybe not feelings exactly..."
    "But she knows how she makes me feel!"
    "All I can think to do is play dumb."
    bree.say "I..."
    bree.say "I don't know what you mean, Lexi!"
    show lexi flirt
    lexi.say "Oh, so you're one of THOSE girls, huh?"
    lexi.say "The kind that need a girl like me to do something like this?"
    show lexi smile blush
    "Lexi doesn't hesitate or give me a chance to answer."
    "Instead she leans forwards and kisses me."
    scene bree_lick_lexi_bg_park at center, zoomAt (2.0, (580, 1300))
    show lexi kiss at flip
    with fade
    $ lexi.flags.kiss += 1
    "And I don't mean she pecks me on the cheek."
    "She full-on plants her lips on mine!"
    "My eyes are wide open with the shock of it."
    "And I know just what I have to do next."
    menu:
        "Go down on Lexi":
            "The sensation of Lexi kissing me just feels so right."
            "It's like it answers all of my questions at once."
            "I part my lips and feel her tongue dart into my mouth."
            "And then I'm kissing her back, with just as much passion."
            "Lexi's hands are all over me, stroking and caressing."
            "Soon enough I'm returning the favour, exploring her body too."
            "When I touch her below the waist, she breaks off the kiss."
            hide lexi
            show lexi a nophone sadsmile blush at center, zoomAt (2.0, (640, 1300))
            with fade
            "I hear her panting, almost desperate for my touch."
            lexi.say "Oh shit...[hero.name]..."
            lexi.say "You're so fucking hot..."
            lexi.say "I'm SO wet for you!"
            "Now all I can think about is what lies between Lexi's legs!"
            hide lexi
            show bree lick lexi
            with fade
            "And so I push her gently up against a nearby car."
            "Then I kneel down in front of her."
            "I feel like I have no control over my actions."
            "Like I couldn't stop myself, even if I tried."
            show bree lick lexi lexi_underwear with dissolve
            "A moment later I have Lexi's panties exposed."
            show bree lick lexi naked with dissolve
            "Then I pull them down as I lean forwards..."
            "Lexi gasps, but she makes no attempt to stop me."
            "The scent of her pussy fills my senses."
            "It's musky and sweet, impossible to resist."
            "I close my eyes before the tip of my tongue touches her."
            "So all I have to go on is touch and taste."
            "That and the sounds that Lexi makes as I begin to lick at her."
            "They're not words exactly, more like whimpering sounds."
            "And they urge me on, mingling with the taste of her on my tongue."
            "I don't take my time, I can't as we're in a public place."
            "So I lap and lick at Lexi with a desperation and hunger."
            "I can't resolve the unspoken attraction between us with words."
            "But I seem to be able to use my tongue in another way entirely."
            "And it's already getting me results!"
            "Lexi is having to hold herself up against the car."
            "She's breathing like she just ran a marathon too."
            "I admit I'm not an expert when it comes to this kind of thing."
            "So I simply try to do to Lexi what I'd like to experience in her position."
            "Almost the same moment I plunge my tongue into her pussy, she starts to quiver."
            "I don't know if it's my attentions that make her cum so quickly."
            "Or if the excitement of being eaten out in a public place does it for her."
            "Either way I allow myself a smile as Lexi loses it in front of me."
            lexi.say "F...fuck..."
            lexi.say "[hero.name[0]]...[hero.name]..."
            lexi.say "Where'd you learn to do that?!?"
            "I stand up and lean in close, helping Lexi make herself decent."
            "Her hands are shaking, and she's still gasping for breath."
            bree.say "Aw...I can't share all my secrets with you, Lexi."
            bree.say "That'd spoil the fun of trying them out on you!"
        "Reassure her" if hero.charm >= 20:
            hide lexi
            show lexi a nophone surprised at center, zoomAt (2.0, (640, 1300))
            with fade
            "I pull away from Lexi, but force a smile onto my face at the same time."
            bree.say "Whoa, Lexi..."
            bree.say "I'm really flattered."
            bree.say "But I'm not ready for this...not yet!"
            show lexi sad
            "Lexi looks like she's about to protest."
            "But then she turns her head away and nods."
            show lexi normal
            lexi.say "Yeah..."
            lexi.say "Maybe I'm getting a little ahead of myself..."
            scene bree_lick_lexi_bg_park at center, zoomAt (1.4, (580, 1000))
            show lexi a nophone normal at center, zoomAt (1.5, (640, 1040))
            with fade
            "We exchange awkward smiles, and Lexi seems to get over it."
            "But I can't help worrying that I've hurt Lexi with my reaction."
            $ lexi.love -= 1
        "Be awkward" if hero.charm < 20:
            "I can't stop myself from reacting in a panic."
            "Which means I end up shoving Lexi away from me."
            scene bree_lick_lexi_bg_park at center, zoomAt (1.4, (580, 1000))
            show lexi a nophone blank blush at center, zoomAt (1.5, (640, 1040))
            with hpunch
            "She staggers back a few feet, looking shocked too."
            bree.say "Whoa, Lexi..."
            bree.say "What...what are you doing?!?"
            show lexi sad
            "Lexi looks like she's about to protest."
            "But then she turns her head away and nods."
            show lexi sadsmile
            lexi.say "Yeah..."
            lexi.say "I guess I read that one wrong..."
            show lexi smile
            "We exchange awkward smiles."
            show lexi blank
            "And yet I get the feeling Lexi's not over it."
            "In fact, I think I hurt her badly with the way I reacted just now."
            $ lexi.love -= 4
    $ lexi.flags.nodate = False
    $ lexi.flags.nokiss = False
    $ lexi.flags.delay = TemporaryFlag(True, 1)
    return

label lexi_female_event_05:
    if lexi.love.max < 80:
        $ lexi.love.max = 80
    "I've been looking forward to the chance to take Lexi shopping for a while now."
    "And today's the day that she's finally agreed to come meet me for some retail therapy."
    if hero.morality >= 25:
        "Plus, this is a chance for me to give her some tips on how to dress."
        "Because there's no need to show off as much skin as she does!"
    elif hero.morality <= -25:
        "Plus, this is a great chance for me to get to know her better."
        "I'm sure there's far more to her than the party-girl she pretends to be most of the time."
    else:
        "Plus, this is a chance for me to prove to Lexi that she's not so wild."
        "I know that, given the chance, I can give her a good run for her money in those stakes!"
    "The only problem is that we were supposed to be meeting right here."
    "Specifically right here and maybe ten minutes ago."
    "But there's no sign of Lexi yet, and I'm starting to get worried."
    "I keep on pulling out, looking for a missed call or a text."
    "And the fact I'm not seeing either means that something must be wrong."
    "Because you'd have to be really rude not to let someone know you were running late, right?"
    lexi.say "SURPRISE!" with vpunch
    bree.say "AAARGH!" with vpunch
    "The sound of someone shouting straight into my ear scares the hell out of me."
    "So much so that I let out a cry of alarm and leap up into the air."
    show lexi happy zorder 1 at center, zoomAt(1.5, (640, 1040)) with fade
    "But when I finally regain control of my senses, I see Lexi standing there."
    show lexi happy at startle
    "Or to be more specific, laughing and looking very pleased with herself."
    show lexi wink
    lexi.say "What's the matter, [hero.name]?"
    lexi.say "Shit yourself?"
    show lexi smile
    if hero.morality >= 25:
        bree.say "LEXI!"
        bree.say "That is not cool..."
        bree.say "You could have given me a heart-attack!"
    elif hero.morality <= -25:
        bree.say "LEXI!"
        bree.say "If you're gonna sneak up on me like that..."
        bree.say "At least make sure it's to do something more fun next time!"
    else:
        bree.say "Urgh..."
        bree.say "Are you pleased with yourself, Lexi?"
        bree.say "Because that was pretty cheap!"
    show lexi happy at startle
    "Lexi's still laughing by the time I'm done telling her off."
    "She shakes her head, like she's not in the least bit affected by my words."
    show lexi normal
    lexi.say "Ah, lighten up!"
    lexi.say "Don't tell me you're going to be as stiff while we're shopping too."
    show lexi smile
    "I take a deep breath and hold it in for a moment, trying to gather up all of my negative emotions."
    "Then I let it all out in one go, picturing the emotions being dragged along with it."
    "And then I nod, seeing this as a fresh start for the shopping spree ahead."
    bree.say "Okay, Lexi..."
    bree.say "Whatever..."
    bree.say "Let's hit the shops before they shut, okay?"
    show lexi normal
    lexi.say "That's what I've been saying, [hero.name]..."
    lexi.say "Let's go already!"
    show lexi smile
    "With a nod I set off in the direction of the first store that I want to visit."
    "Which is the sportswear place just around the corner from here."
    show lexi blank
    "Lexi has to hurry to keep up with me, and her annoyance shows."
    show lexi annoyed
    lexi.say "Hey..."
    lexi.say "Wait for me!"
    lexi.say "Oh...you want to go in there?"
    show lexi blank
    "I nod as we walk in through the doors."
    show bg clothesshop with fade
    bree.say "I need some new workout gear for the gym."
    bree.say "The stuff I have is almost worn out!"
    show lexi annoyed
    lexi.say "Huh..."
    show lexi bored
    lexi.say "I don't need any special clothes to get my exercise."
    lexi.say "And I don't have to be a member of a fancy gym either!"
    if hero.morality >= 25:
        bree.say "Oh, Lexi..."
        bree.say "I don't think that counts as exercise!"
    elif hero.morality <= -25:
        bree.say "You want to try working out too, Lexi."
        bree.say "More stamina means you can go longer and harder too!"
    else:
        bree.say "Well, Lexi..."
        bree.say "That's one way to burn off the calories!"
    show lexi blank
    "I make my way straight over to where the workout gear is located."
    "And I begin to look through the racks, occasionally holding something against me to check the size."
    "At first Lexi seems to be doing the exact same thing."
    "But then I hear her calling to me."
    show lexi normal
    lexi.say "[hero.name]..."
    lexi.say "Hey, [hero.name]..."
    lexi.say "You should get this, it's perfect!"
    show lexi smile
    "I look around to see Lexi holding up a leotard in a shockingly bright colour."
    "It looks to me like one of the things you see in eighties workout videos."
    show lexi normal
    lexi.say "See what I mean?"
    lexi.say "Great way to show off the goods while you pump iron."
    show lexi wink
    lexi.say "And guaranteed to get you pumped with something else in the showers later too!"
    show lexi smile
    "I shake my head at Lexi's suggestion."
    "And I hold up my own choice instead."
    if hero.morality >= 25:
        "Which is a pair of baggy sweatpants and matching hoody."
        bree.say "It's the gym, Lexi..."
        bree.say "Not the swimming pool."
        bree.say "No need for skin-tight lycra."
    elif hero.morality <= -25:
        "Which is a pair of extremely short shorts and a tube-top barely wider than a bra."
        bree.say "That might have been the best you could get away with in the eighties."
        bree.say "But this is the twenty-first century, Lexi."
        bree.say "You can afford to be a little more daring than that."
    else:
        "Which is a pair of leggings and a fitted T-shirt."
        bree.say "I don't mind showing off my figure a little, Lexi."
        bree.say "But things have moved on from leg-warmers and lycra."
        bree.say "After all, this is the twenty-first century."
    "I don't think Lexi's pleased that I torpedoed her idea like that."
    "But she does seem to be impressed by the way I stood my ground."
    "Because she doesn't keep pushing her case, instead letting it drop."
    show lexi normal
    lexi.say "Fine, [hero.name]..."
    lexi.say "You've got to wear it, not me."
    show lexi blank
    "I respond to that with what I hope is a polite nod."
    "And then I walk over to the cash register to make my purchases."
    show bg mall1 with fade
    "Once we're outside, I can see that Lexi's already looking around."
    "Like she's restless to make it to the next store."
    show lexi normal
    lexi.say "Where next, [hero.name]?"
    show lexi blank
    if hero.morality >= 25:
        bree.say "Don't read anything into this, Lexi..."
        bree.say "But I need to buy some underwear."
    elif hero.morality <= -25:
        bree.say "Oh, you're gonna love this, Lexi..."
        bree.say "I gotta buy some underwear!"
    else:
        bree.say "Try to keep yourself under control, if you can..."
        bree.say "Because I have to buy some underwear!"
    show lexi smile
    "Lexi's face lights up the moment she hears what I have to say."
    "And she's practically on my heels from that point on."
    show bg clothesshop at flip with fade
    "Almost pushing me into the store where I want to buy the underwear."
    show lexi normal
    lexi.say "I know you, [hero.name]..."
    lexi.say "You want something that says sexy, but not slutty."
    show lexi wink
    lexi.say "Am I right?"
    show lexi smile
    if hero.morality >= 25:
        "I do the best I can to hide the fact that I'm already blushing."
        "And I pick up the most conservative pack of panties I can find."
        "Truth is, they look uncomfortable, but Lexi's kind of spooked me."
        bree.say "No, no..."
        bree.say "These will do me fine."
        show lexi annoyed
        lexi.say "Urgh..."
        lexi.say "Granny pants!"
    elif hero.morality <= -25:
        bree.say "My thoughts exactly, Lexi..."
        bree.say "So how about crotchless?"
        bree.say "They look respectable, but they're hiding a big surprise!"
        show lexi wow
        lexi.say "Whoa, [hero.name]..."
        show lexi happy
        lexi.say "It's like you're reading my mind!"
    else:
        bree.say "Maybe sexy and understated, Lexi?"
        bree.say "You know, rather then out and out slutty?"
        "I pick up a set of lingerie that I feel fits the bill."
        "And I hold it up for Lexi to see."
        show lexi normal
        lexi.say "They're okay, I guess."
        show lexi wink
        lexi.say "But I'd have gone for crotchless instead!"
    show lexi smile
    "I'm very happy with what I've picked out, so I head to the register again."
    "This time Lexi hangs back, still browsing the racks as I pay."
    scene bg mall1
    show lexi casual blank zorder 1 at center, zoomAt(1.5, (640, 1040))
    with fade
    "Then she meets me by the entrance to the store."
    show lexi normal
    lexi.say "Okay, [hero.name]..."
    lexi.say "You've picked two stores in a row."
    show lexi wink
    lexi.say "Now it's my turn."
    show lexi smile
    "I shrug and shake my head."
    bree.say "That sounds fair."
    bree.say "So where are we headed next?"
    show lexi happy
    "Lexi's face breaks into a broad smile as she starts to lead the way."
    show bg street
    show lexi smile casual
    with fade
    "And I manage to keep an open mind until we take a turn down a side-street."
    "Because I think I'm starting to recognise where she's taking me."
    "And when Lexi stops in front of a certain store and strikes a pose, I know I was right."
    show bg alley
    show lexi happy casual
    with fade
    lexi.say "Ta da!"
    lexi.say "Here we are!"
    show lexi smile
    bree.say "Lexi..."
    bree.say "This is the sex shop!"
    show lexi normal
    lexi.say "You think I don't know that?"
    lexi.say "I went in all the stores where you needed shit, didn't I?"
    show lexi smile
    bree.say "You expect me to believe you really need stuff from in there?!?"
    show lexi wink
    lexi.say "A girl's got needs, [hero.name]..."
    lexi.say "Don't pretend like you don't know that!"
    show bg sexshop
    show lexi casual smile
    with fade
    "Lexi shakes her head as she pushes open the door and holds it for me."
    "Which leaves me no choice but to follow her into the sex shop."
    show lexi blush
    "Once we're inside, Lexi acts like she's in some kind of wonderland."
    "Flitting from one thing to another, eyes wide in genuine amazement."
    show lexi wow
    lexi.say "Wow..."
    show lexi normal
    lexi.say "Imagine wearing that..."
    show lexi flirt
    lexi.say "Or being done by one of those..."
    show lexi normal
    lexi.say "Or doing someone with one of those strapped on!"
    show lexi smile
    "Finally Lexi seems to settle on a rack of dildos and vibrators."
    "Which is when she beckons me over."
    show lexi normal
    lexi.say "Come on, [hero.name]..."
    lexi.say "I need your help to choose!"
    lexi.say "Now I like this one..."
    show lexi smile
    "Lexi holds up a pretty huge-looking specimen, which sways an inch from my nose."
    show lexi normal
    lexi.say "But what do you think?"
    show lexi smile
    if hero.morality >= 25:
        "I instantly start backing off, waving my hands in the air."
        bree.say "Whatever you think, Lexi..."
        bree.say "I need to get some fresh air!"
    elif hero.morality <= -25:
        "I grab the dildo from Lexi's hand and toss it aside."
        bree.say "Are you kidding me?"
        bree.say "You want something at least this big!"
        "I hand a dildo almost twice the size to Lexi."
        show lexi surprised
        "Feeling smug as her eyes almost pop out of her head."
    else:
        "I take the dildo from Lexi, looking it up and down."
        bree.say "Looks like a good size to me, Lexi."
        bree.say "But I get the impression you like them on the larger side!"
    scene bg alley with fade
    "While Lexi grabs a couple more things and pays, I step outside."
    "And I wait a few minutes for her to come out to me."
    with fade
    show lexi casual blank at center, zoomAt(1.5, (640, 1040)) with easeinright
    "When she does, I realise this is the only place where she bought anything."
    bree.say "You need to go anywhere else, Lexi?"
    bree.say "You have to need more than what you got in there."
    "Lexi shakes her head at this, holding up her bag."
    show lexi normal
    lexi.say "Oh no, [hero.name]..."
    lexi.say "I've been helping myself to a little something as we went along."
    show lexi smile
    "Looking into the bag, I can see all of the outfits Lexi suggested to me."
    "The only possible explanation being that she's sneaked them out of the stores."
    if hero.morality >= 25:
        bree.say "Lexi..."
        bree.say "You can't just steal things!"
        bree.say "Maybe if you take them back and apologise..."
        show lexi annoyed
        lexi.say "Fuck that, [hero.name]..."
        lexi.say "They won't miss any of this shit."
    elif hero.morality <= -25:
        bree.say "Fuck..."
        bree.say "You might have told me, Lexi!"
        bree.say "You could have stolen my shit too."
        show lexi happy
        lexi.say "Don't worry about it, [hero.name]..."
        lexi.say "There's always next time!"
    else:
        bree.say "Treating yourself to a five-finger discount, eh?"
        bree.say "Just don't get caught, okay?"
        bree.say "Because if you do, I don't know you!"
        show lexi normal
        lexi.say "Don't worry, [hero.name]..."
        lexi.say "I'm too good to get caught."
    show lexi smile with fade
    "All in all, shopping with Lexi's been a mixed-bag."
    "But I feel like it went as well as could have been expected."
    "That and I got to hang out with her alone too."
    "Which can only be a good thing for our relationship."
    $ hero.replace_activity()
    $ lexi.love += 2
    $ lexi.flags.delay = TemporaryFlag(True, 1)
    scene bg black with dissolve
    return


label lexi_female_event_06:
    if lexi.love.max < 100:
        $ lexi.love.max = 100
    scene bg street with fade
    "I had a lot of fun going shopping with Lexi the last time that we met up."
    "So much so in fact, that this time I've suggested that we take it to the next level."
    "Which means meeting up at the mall to spend some quality time there."
    show lexi b casual yawn at center, zoomAt(1.25, (340, 880)) with dissolve
    "But when I finally make it there and spot Lexi, she doesn't look very excited."
    bree.say "Hey, Lexi..."
    bree.say "Why the long face?"
    show lexi a smile at center, traveling(1.5, 1.0, (640, 1040))
    "At the sound of my voice, Lexi turns to face me."
    show lexi happy
    "She looks pleased to see me, for sure."
    "But I can still sense that underlying mood beneath it."
    "Almost like she'd rather be somewhere else right now."
    show lexi normal
    lexi.say "Oh..."
    lexi.say "Hi, [hero.name]..."
    lexi.say "You noticed that, huh?"
    show lexi smile
    "I nod, as I feel a tight smile forming on my face."
    "I want to hear what's the matter with Lexi, because I obviously care about her."
    "But at the same time I'm worried that what she has to say might sink this outing."
    "You know, bring it to an end even before it gets started?"
    bree.say "It's okay, Lexi..."
    bree.say "You can tell me what the problem is."
    show lexi blank
    "Lexi kind of shrugs and purses her lips."
    show lexi bored
    "Then she lets out a sigh and begins to explain herself."
    show lexi sadsmile
    lexi.say "Okay, the thing is..."
    lexi.say "I don't get why we're here, you know?"
    lexi.say "We went shopping the last time we hooked up."
    lexi.say "So isn't this just more of the same?"
    show lexi sad
    "I'm so amazed at what I'm hearing that I can't hide my surprise."
    "And I find myself shaking my head as I try to explain why Lexi's dead wrong."
    bree.say "Oh no, Lexi..."
    bree.say "What we did before was just go shopping."
    bree.say "This is a trip to the mall, a cornerstone of modern Western culture!"
    show lexi surprised
    "Lexi stares at me like a dog that's been shown a card-trick."
    lexi.say "Erm..."
    lexi.say "It's the mall, [hero.name]..."
    lexi.say "Just a bunch of shops in one big building."
    lexi.say "You make it sound like a frickin' art gallery or something!"
    show lexi blank
    "I'm still shaking my head when Lexi's finished speaking."
    "Because I can't believe she's that naïve."
    bree.say "Don't you watch movies or TV series, Lexi?"
    bree.say "Going to the mall is a right of passage, a sacred ritual!"
    bree.say "Generations have forged their cultural identities here."
    bree.say "In the future, they'll dig these places up like they do ancient monuments!"
    "Now it's Lexi's turn to shake her head."
    show lexi normal
    lexi.say "Okay, [hero.name]..."
    lexi.say "You sound totally crazy right now."
    lexi.say "Let's go grab a slushie, before you start foaming at the mouth!"
    show lexi smile
    "I swallow down the urge to argue and follow Lexi into the mall."
    scene bg mall1
    show lexi casual smile at center, zoomAt(1.5, (640, 1040))
    with fade
    "Once we're inside, she makes good on her promise, leading me to a slushie stand."
    "And I soothe my bruised ego with a raspberry flavour slushie."
    show lexi normal
    lexi.say "So..."
    lexi.say "What exactly are we supposed to do now we're here?"
    lexi.say "Normally I'd just wander around the place, looking at stuff that takes my fancy."
    lexi.say "But you seem to think we should be doing some kind of weird pilgrimage shit!"
    show lexi blank
    "I take a long suck on my slushie, letting Lexi's words sink in."
    "And only when I feel like I'm ready do I respond."
    bree.say "Okay, Lexi..."
    bree.say "Maybe I got a little carried away before."
    bree.say "But that's basically what we're here to do."
    bree.say "We wander around, looking at nice things."
    bree.say "Then we daydream about being able to afford them."
    show lexi smile
    "I'm pleased to see that this seems to be clicking with Lexi."
    show lexi happy
    "She's beginning to look happier than she did before."
    "Like she's finally getting into the spirit of the day."
    show lexi normal
    lexi.say "I get you, [hero.name]..."
    show lexi wink
    lexi.say "Then you check the security guard's not looking."
    lexi.say "And you stash the stuff you want in your panties, right?"
    show lexi smile
    if hero.morality >= 25:
        bree.say "Oh my god..."
        bree.say "You can't do that, Lexi..."
        bree.say "We could get into serious trouble, even arrested by the police!"
    elif hero.morality <= -25:
        bree.say "Hell, Lexi..."
        bree.say "You really are bad to the bone!"
        bree.say "Just make sure you steal something for me too, yeah?"
    else:
        bree.say "Oh, Lexi..."
        bree.say "That is so you!"
        bree.say "But maybe leave off the shop-lifting, just for today?"
    show lexi blank
    "Lexi shrugs off my comments with a wave of her hand."
    show lexi normal
    lexi.say "Ah, hell..."
    lexi.say "Maybe I'll forget about it, just this once."
    lexi.say "I work best when I'm alone, at least when it comes to that kind of stuff."
    show lexi smile with fade
    "We spend a good long while after that, wandering from store to store."
    "All the while slurping loudly on our slushies and talking about whatever comes to mind."
    "And the vibe between us is getting better all the time too."
    "Lexi really seems to be warming to the idea of mall-time as a thing."
    "A social ritual that means far more than it would seem on the surface of things."
    "Though I have to admit that the casual comments about shop-lifting are still playing on my mind."
    "Which is why I try to subtly steer us away from any stores with small items on open display."
    "I figure that if we're looking at large, bulky things, Lexi can't possibly fit them into her underwear."
    "Though the whole idea of that is kind of fascinating."
    "Maybe I'll ask her for a demonstration some time..."
    show lexi happy
    lexi.say "Oh yeah..."
    lexi.say "We are so doing that!"
    show lexi smile
    "Lexi's exclamation snaps me back to reality."
    "And I crane my neck to see what she's talking about."
    bree.say "Huh?"
    bree.say "What are we doing now?!?"
    "I follow the direction in which Lexi's pointing."
    "And that's when I see the tattoo and piercing parlour."
    bree.say "Lexi..."
    bree.say "That's a..."
    show lexi normal
    lexi.say "I know what it is, [hero.name]..."
    lexi.say "Come on, we're going in there right now!"
    show lexi smile at center, zoomAt(1.5, (540, 1040)) with ease
    "Lexi grabs hold of my wrist and begins to pull me towards the tattoo parlour."
    show lexi surprised at center, zoomAt(1.5, (640, 1040)) with hpunch
    "But I resist, more out of confusion than a genuine aversion to going in there."
    bree.say "Wait a minute, Lexi..."
    bree.say "I'm not getting a tattoo on impulse!"
    bree.say "I'll only end up having it lasered off my butt!"
    show lexi wink
    lexi.say "Nah, [hero.name]..."
    lexi.say "You're not getting a tattoo."
    lexi.say "I want you to get your nipples pierced - that'll look so hot!"
    show lexi smile
    if hero.morality >= 25 and not hero.piercings.nipples.worn:
        "I can't actually believe what I'm hearing."
        "Or that Lexi would just assume I'd be cool with it too."
        "So finding a hidden reserve of strength, I stand my ground."
        show lexi surprised at center, zoomAt(1.25, (640, 880)) with hpunch
        "And I pull my arm away from her too."
        "Lexi turns to face me, a confused look on her face."
        lexi.say "Huh?"
        lexi.say "What's the problem, [hero.name]?"
        lexi.say "It's not like it hurts too much."
        show lexi normal
        lexi.say "Here, look..."
        lexi.say "I already got mine done!"
        show lexi smile topless with dissolve
        "Lexi's pulling up her shirt as she says all of this."
        show lexi -topless with vpunch
        "And I have to leap into action to pull it back down again."
        "Because otherwise she'd have been flashing her breasts in public!"
        bree.say "That's not the issue, Lexi."
        bree.say "I just don't want to get my nipples pierced, that's all."
        show lexi annoyed
        lexi.say "Why not?!?"
        lexi.say "I already told you I got mine done!"
        show lexi blank
        "I blink in sheer amazement at Lexi's statement."
        bree.say "Good for you, Lexi..."
        bree.say "But what's that got to do with me getting it done?"
        bree.say "If I want piercings, then I'll get them."
        bree.say "Until then, these nipples will remain unpierced!"
        show lexi bored
        lexi.say "Urgh..."
        lexi.say "Whatever, [hero.name]..."
        lexi.say "Be a square forever!"
        show lexi blank
        "Lexi rolls her eyes and tries to make it sound like I'm being a killjoy."
        show lexi normal
        "But I note that she lets the matter drop very quickly after that."
        $ lexi.love += 3
        "Which makes me think that I might have been able to gain a little respect from standing up to her like that."
    elif hero.morality < 25 and not hero.piercings.nipples.worn:
        "Lexi manages to pull me perhaps a metre before I dig in my heels."
        with hpunch
        "And once she finds that she can't hope to make me budge, she gives in."
        show lexi annoyed
        "Letting go of my hand and turning to face me, Lexi looks a little pissed."
        lexi.say "Huh?"
        lexi.say "What's the problem, [hero.name]?"
        lexi.say "It's not like it hurts too much."
        show lexi normal
        lexi.say "Here, look..."
        lexi.say "I already got mine done!"
        show lexi smile topless
        "Lexi's pulling up her shirt as she says all of this."
        show lexi -topless with vpunch
        "And I have to leap into action to pull it back down again."
        "Because otherwise she'd have been flashing her breasts in public!"
        bree.say "That's not the issue, Lexi."
        bree.say "It's more that you're kind of pushing me into it!"
        show lexi sad
        "Lexi looks more than a little embarrassed as I point this out."
        show lexi sadsmile
        "And though she tries to brush it off, I can see she's been a little humbled."
        lexi.say "I...I just thought you'd be up for it, that's all."
        show lexi wink
        lexi.say "And I think it'd look hot on you too."
        show lexi smile
        menu:
            "Agree to get my nipples pierced":
                "I'm just about to tell Lexi that it's not going to happen."
                "But then I realise I'm just rejecting the idea on impulse."
                "Which is almost as bad as her wanting me to do it on impulse too."
                "So instead I take a moment to actually think it over."
                bree.say "You know what, Lexi..."
                bree.say "I thought about having it done once before."
                bree.say "And I came really close, but then chickened-out."
                bree.say "Maybe if I have you with me, I won't be so scared this time?"
                show lexi happy
                "Lexi nods happily at this."
                lexi.say "Sure thing, [hero.name]..."
                lexi.say "I'll hold your hand the whole time, I promise!"
                show lexi smile
                "I think it's more Lexi's enthusiasm that makes up my mind."
                "Rather than a genuine desire to have it done."
                scene bg tattooshop
                show lexi casual smile at center, zoomAt(1.5, (640, 1040))
                with fade
                "But we walk into the tattoo parlour and go through with it all the same."
                scene bg black
                show tattooparlor bree topless
                with fade
                "It hurts a little more than I was expecting it to."
                "But Lexi's as good as her word, holding my hand throughout."
                scene bg mall1
                show lexi casual flirt at center, zoomAt(1.5, (640, 1040))
                with fade
                "And when we walk out of the place, she's still staring at my chest."
                $ hero.piercings.nipples.pierced = True
                $ hero.piercings.nipples.worn = True
                $ lexi.love += 5
                lexi.say "Fuck me, [hero.name]..."
                lexi.say "Those things make your tits looks so hot!"
                lexi.say "When am I gonna get to see them again?"
                show lexi smile
                bree.say "Hmm..."
                bree.say "Well, Lexi, that might be pretty soon."
                bree.say "Depending on how good of a girl you can be!"
            "Refuse to get my nipples pierced":
                "I think about going through with it for a moment."
                "Even if it's just for the sake of appeasing Lexi."
                "But then I get to thinking that could be the start of a slippery slope."
                "And who knows where that could end up leading?"
                bree.say "I get what you're saying, Lexi."
                bree.say "But this kind of thing has to be my choice alone."
                bree.say "Until then, these nipples will remain unpierced!"
                show lexi annoyed
                lexi.say "Urgh..."
                lexi.say "Whatever, [hero.name]..."
                lexi.say "Be a square forever!"
                show lexi smile
                "Lexi rolls her eyes and tries to make it sound like I'm being a killjoy."
                "But I note that she lets the matter drop very quickly after that."
                show lexi normal
                $ lexi.love += 3
                "Which makes me think that I might have been able to gain a little respect from standing up to her like that."
    else:
        "Lexi manages to pull me perhaps a metre before I dig in my heels."
        with hpunch
        "And once she finds that she can't hope to make me budge, she gives in."
        "Letting go of my hand and turning to face me, Lexi looks a little pissed."
        show lexi annoyed
        lexi.say "Huh?"
        lexi.say "What's the problem, [hero.name]?"
        lexi.say "It's not like it hurts too much."
        show lexi normal
        lexi.say "Here, look..."
        lexi.say "I already got mine done!"
        show lexi smile
        "Lexi's pulling up her shirt as she says all of this."
        "But she's not fast enough to get the job done in time."
        "Not before I've done the same thing and faster too."
        show sexinserts chest bree as breetits zorder 1 at center, zoomAt(1.25, (-180, 1100))
        show expression "sexinserts_add_piercing_insert_chest_bree_nipples" zorder 2 at center, zoomAt(1.25, (-180, 1100))
        show lexi surprised
        with dissolve
        "Which leaves Lexi staring at my naked breasts, perhaps an inch from her face."
        bree.say "You get it now, Lexi?"
        bree.say "You understand why I can't get my nipples pierced?"
        show lexi flirt
        $ lexi.love += 4
        "Lexi nods slowly, but her attention is fixed on my breasts."
        "Hell, I can even see her eyes moving in perfect imitation of how they're swaying right now!"
        show lexi normal
        lexi.say "Oh yeah, [hero.name]..."
        lexi.say "I get it now..."
        lexi.say "I totally get it!"
        lexi.say "You already got those bad-girls done!"
        show lexi smile
        "Suddenly I become aware of just where we are right now."
        hide breetits
        hide expression "sexinserts_add_piercing_insert_chest_bree_nipples"
        with dissolve
        "And pleased as I am with Lexi's reaction, I hurry to cover myself up again."
        "This seems to do the trick in terms of snapping Lexi out of it too."
        "She shakes her head, as if sobering up."
        show lexi normal
        lexi.say "Ah, [hero.name]..."
        lexi.say "You're gonna let me see them again, right?"
        show lexi smile
        bree.say "Hmm..."
        bree.say "Maybe, Lexi, maybe."
        bree.say "Depending on how good of a girl you can be!"



































    scene bg street
    show lexi casual smile at center, zoomAt(1.5, (640, 1040))
    with fade
    "By the time we're walking out of the mall, I feel like I've made my point."
    "Lexi and I have had a great time, and we've bonded a little more too."
    "I'm starting to feel more comfortable around Lexi now."
    "Like I'm getting used to the rough edges of her personality."
    "Hell, some of her weird quirks are actually starting to seem cute!"
    "I just hope we can keep it up and get to know each other better."
    "Because I know for sure that I really have the hots for her!"
    "And playing it cool is getting harder all the time."
    $ lexi.flags.delay = TemporaryFlag(True, 3)
    $ game.active_date.score = 75
    $ game.active_date.stay = False
    return

label lexi_female_event_07:
    if lexi.love.max < 120:
        $ lexi.love.max = 120
    scene bg pub
    show drink_room_pub
    show lexi a blush smile nophone at flip, center, zoomAt(1.65, (440, 1040))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with vpunch
    "I can't help jumping in surprise as a drink is unceremoniously shoved into my face."
    bree.say "Wha..."
    show lexi a normal
    lexi.say "Don't be such a lightweight, [hero.name]!"
    lexi.say "We've only had a couple of drinks, for sake's fuck..."
    show lexi a sadsmile
    lexi.say "I mean...for fuck's sake!"
    show lexi a smile
    "I take the drink that Lexi's offering me and lift it to my lips to take a sip."
    "The truth is that I already feel like I might have had a little too much to drink."
    "But it's kind of hard to say no to Lexi, mainly because we're getting on so well right now."
    "Plus the fact that she just keeps on buying me more, even if I do say no!"
    bree.say "So..."
    bree.say "So..."
    bree.say "So what were we talking about just now?"
    show lexi a bored
    lexi.say "I dunno, [hero.name]..."
    lexi.say "I was getting more booze!"
    show lexi a smile
    bree.say "I mean before that..."
    bree.say "Before you got more booze!"
    show lexi a blank
    "Lexi stops talking and screws up her face."
    "Doing that thing where people under the influence try to think hard."
    "As if the expression on their features is really going to help matters."
    show lexi a angry
    lexi.say "I have no fucking idea!"
    show lexi a normal
    lexi.say "But it probably involved sex..."
    lexi.say "I always end up talking about sex when I drink!"
    show lexi a smile
    "I narrow one eye as I look at Lexi."
    "Almost like I can't concentrate on her if I don't."
    bree.say "Huh..."
    bree.say "You talk about it a lot when you're sober too, you know?"
    show lexi a surprised
    "Lexi looks surprised by this revelation."
    "Almost like she's shocked she could do something like that."
    lexi.say "I do?"
    show lexi a normal
    lexi.say "Well I talk about it more when I'm drunk..."
    lexi.say "And I feel drunk now - so let's talk about fucking, yeah?"
    show lexi a smile
    if hero.morality >= 25:
        "I can already feel my cheeks starting to flush with colour."
        "But I also feel too drunk to be able to protest."
        bree.say "Oh..."
        bree.say "I guess so!"
    elif hero.morality <= -25:
        "I nod my head with genuine enthusiasm."
        "Because this is a subject I can really get my teeth into."
        bree.say "I thought you'd never ask!"
        bree.say "Go ahead, Lexi - ask me anything."
        "I can see that Lexi's warming to the idea already."
    else:
        "I shrug and then give a nod."
        "Because it's not like Lexi isn't going to confess to more than I ever would."
        bree.say "Sure thing, Lexi..."
        bree.say "But what exactly are we going to talk about?"
    show lexi a flirt -blush
    "She regards me with a sly glance, then nods her head."
    show lexi a normal blush
    lexi.say "Okay, [hero.name]..."
    lexi.say "You're a big girl, one that's been round the block, right?"
    lexi.say "I'm guessing you've been with guys and girls alike?"
    lexi.say "So which is your favourite?"
    lexi.say "Or do you like a bit of both?"
    show lexi a smile
    menu:
        "I like guys":
            if hero.morality >= 25:
                bree.say "Oh..."
                bree.say "I suppose that I like guys the best of all."
                bree.say "At least I've been with more of them!"
            elif hero.morality <= -25:
                bree.say "I've had more than a few of both, Lexi."
                bree.say "Some of them were great and some of them were the shits."
                bree.say "But I just seem to always want a cock inside of me!"
            else:
                bree.say "Don't get me wrong, Lexi..."
                bree.say "I've met some girls that were really fun to be around."
                bree.say "But I always seem to find myself going back to the guys."
            if lexi.lesbian <= MAX_LES_GUY_SEX:
                "Lexi nods eagerly as I explain my preferences."
                show lexi a normal
                lexi.say "Me too, [hero.name], me too!"
                lexi.say "You can have fun with a girl - a whole lot of fun."
                lexi.say "But there's nothing like getting fucked good and hard by a real cock!"
                show lexi a smile
            elif lexi.lesbian >= MIN_LES_GIRL_SEX:
                "Lexi shakes her head as I explain my preferences."
                show lexi a normal
                lexi.say "I like a hard cock as much as the next girl."
                lexi.say "But I think a girl knows how to please a girl, yeah?"
                lexi.say "No guy ever had to handle a pussy!"
                show lexi a smile
            else:
                "Lexi shakes her head as I explain my preferences."
                show lexi a normal
                lexi.say "It's kind of cute that you like one and not the other, [hero.name]."
                lexi.say "But me, I don't see why I should limit my options like that."
                lexi.say "I might hook up with a girl, or I might hook up with a guy."
                lexi.say "Hell, I might hook up with both at once!"
                show lexi a smile
        "I like girls":
            if hero.morality >= 25:
                bree.say "Oh..."
                bree.say "This is going to sound so naughty..."
                bree.say "But I think that I actually like girls better than guys!"
            elif hero.morality <= -25:
                bree.say "Don't get me wrong, cock is good."
                bree.say "But I've had more orgasms with girls."
                bree.say "So I tend to go with them more often."
            else:
                bree.say "I've been with some guys that were amazing in the past."
                bree.say "But I've got to say that more girls have blown my mind."
                bree.say "So I guess that means I like them better."
            if lexi.lesbian <= MAX_LES_GUY_SEX:
                "Lexi shakes her head as I explain my preferences."
                show lexi a normal
                lexi.say "I like someone who knows where my clit is, [hero.name]."
                lexi.say "And you can have fun with a girl - a whole lot of fun."
                lexi.say "But there's nothing like getting fucked good and hard by a real cock!"
            elif lexi.lesbian >= MIN_LES_GIRL_SEX:
                "Lexi nods her head eagerly as I explain my preferences."
                show lexi a normal
                lexi.say "I like a hard cock as much as the next girl."
                lexi.say "But I think a girl knows how to please a girl, yeah?"
                lexi.say "No guy ever had to handle a pussy!"
                show lexi a smile
            else:
                "Lexi shakes her head as I explain my preferences."
                show lexi a normal
                lexi.say "It's kind of cute that you like one and not the other, [hero.name]."
                lexi.say "But me, I don't see why I should limit my options like that."
                lexi.say "I might hook up with a girl, or I might hook up with a guy."
                lexi.say "Hell, I might hook up with both at once!"
                show lexi a smile
        "I like both guys and girls":
            if hero.morality >= 25:
                bree.say "Oh..."
                bree.say "This is going to sound so naughty..."
                bree.say "But I think that I actually like both of them!"
            elif hero.morality <= -25:
                bree.say "Don't get me wrong, cock is good."
                bree.say "But you get more orgasms with girls."
                bree.say "So how are you supposed to choose between them?"
            else:
                bree.say "Don't get me wrong, Lexi..."
                bree.say "I've been with some guys that were amazing in the past."
                bree.say "And definitely with some girls that have blown my mind."
                bree.say "So I can't really choose - I guess I like both!"
            if lexi.lesbian <= MAX_LES_GUY_SEX:
                "Lexi shakes her head as I explain my preferences."
                show lexi a normal
                lexi.say "I like someone who knows where my clit is, [hero.name]."
                lexi.say "And you can have fun with a girl - a whole lot of fun."
                lexi.say "But there's nothing like getting fucked good and hard by a real cock!"
                show lexi a smile
            elif lexi.lesbian >= MIN_LES_GIRL_SEX:
                "Lexi shakes her head as I explain my preferences."
                show lexi a normal
                lexi.say "I like a hard cock as much as the next girl."
                lexi.say "But I think a girl knows how to please a girl, yeah?"
                lexi.say "No guy ever had to handle a pussy!"
                show lexi a smile
            else:
                "Lexi nods her head eagerly as I explain my preferences."
                show lexi a normal
                lexi.say "It's kind of cute when someone says they like one and not the other, [hero.name]."
                lexi.say "But me, I don't see why I should limit my options like that."
                lexi.say "I might hook up with a girl, or I might hook up with a guy."
                lexi.say "Hell, I might hook up with both at once!"
                lexi.say "And it's great to know that you feel the same way too."
                show lexi a smile
    "The fact that we've both just opened ourselves up like that seems to weigh on us a little."
    "And once it's all out in the open, the conversation turns towards less controversial subjects."
    "I'm not sure if sharing so much with Lexi is going to turn out to be a good thing or a bad thing."
    "But one thing is for sure, and that's the fact I know a lot more about what makes her tick now."
    "So long as I remember all of it when I wake up in the morning!"
    $ lexi.flags.delay = TemporaryFlag(True, 3)
    return

label lexi_female_event_08:

    "Today is one of those days when my sixth sense is totally there and picking up on everything."
    "Because I keep noticing all these weird little things that Lexi's doing here and there."
    "Like, she keeps on acting like she's going to buy something, but then changing her mind."
    "As though she remembers something that stops her from doing it."
    show lexi a smile at center, zoomAt(1.25, (640, 880)) with fade
    "In the end I feel like I have to call her on it, because it's starting to make me worry."
    bree.say "Lexi..."
    bree.say "Is there something wrong?"
    bree.say "Like, something you'd like to talk about?"
    show lexi a surprised
    "Lexi looks at me in genuine surprise when I ask the question."
    "Like she had no idea that it was so obvious."
    show lexi a sadsmile
    lexi.say "Y...yeah, [hero.name]..."
    lexi.say "I kinda do."
    show lexi a surprised
    lexi.say "But how did you know?"
    show lexi a blank
    "A magician never reveals her tricks."
    "So I just offer Lexi a shrug."
    bree.say "Oh, I just have a knack for that kind of thing."
    bree.say "So what's bothering you, Lexi?"
    bree.say "Penny for your thoughts?"
    "I just tossed the phrase in without thinking."
    show lexi a happy at startle
    "But for some reason it gets an ironic laugh from Lexi."
    show lexi a normal
    lexi.say "How about twenty-five thousand dollars, [hero.name]?"
    lexi.say "That'd be more helpful right about now!"
    show lexi a smile
    "I can't help blinking in amazement at the mere mention of that much money."
    bree.say "What do you mean, Lexi?"
    show lexi a happy at startle
    "Lexi laughs again."
    show lexi a normal
    lexi.say "What do you think I mean?"
    lexi.say "I owe someone twenty-five grand!"
    show lexi a smile
    "I'm still shaking my head in amazement at the sheer size of the figure."
    "Finding it hard to imagine that amount of money, let alone owe it."
    bree.say "What did you do?"
    bree.say "Take out a loan to buy a house?"
    show lexi a sadsmile
    lexi.say "Of course not, [hero.name]..."
    lexi.say "Would you loan me money for that?!?"
    show lexi a blank
    bree.say "Then what did you do?"
    "Lexi shrugs at the question."
    show lexi a sadsmile
    lexi.say "Well..."
    lexi.say "I might have borrowed a little money off of my pimp..."
    show lexi a blank
    "I really should be shocked and appalled hearing something like that."
    "But this is Lexi, and you kind of get used to it from her after a while."
    bree.say "Your pimp lent you twenty-five grand?!?"
    show lexi a sadsmile
    lexi.say "Not all at once!"
    lexi.say "Just a little bit here and a little bit there, you know?"
    lexi.say "I didn't think he was keeping track of it, so neither did I."
    show lexi a blank
    bree.say "But I guess he was?"
    "Lexi nods."
    show lexi a sadsmile
    lexi.say "And now he says that he wants it back - every last dime!"
    lexi.say "[hero.name], you have to help me!"
    show lexi a sad
    bree.say "How am I supposed to do that, Lexi?"
    bree.say "I don't just happen to have that amount of money lying around!"
    show lexi a smile
    "Lexi clasps her hands together and wrings them in front of my face."
    "Almost like she's begging me to help her out of this mess."
    show lexi a normal
    lexi.say "You're smart, [hero.name]..."
    lexi.say "So use your brains to think of something, please!"
    show lexi a sadsmile
    lexi.say "Otherwise I don't know what my pimp's gonna do to me!"
    show lexi a blank
    "I can tell that Lexi's being totally serious right now."
    "And if she's really in danger, then I should do what I can to help."
    "Because I am supposed to be her friend."
    menu:
        "Suggest you do sex-work together" if game.flags.job_day == "prostitute" or game.flags.job_night == "prostitute":
            "I don't have the means to pay off the debt for Lexi."
            "And even if I did, I'm not sure that would help in the long-run."
            "What she really needs is someone to help her make more money."
            "And I know someone that's perfectly qualified to make that happen."
            bree.say "You need to maximise your potential earnings, Lexi."
            bree.say "Take on a business partner and expand your operation."
            show lexi a annoyed
            "Lexi frowns at this, like she doesn't understand my meaning."
            lexi.say "I'm a pro, [hero.name]..."
            lexi.say "Not a stockbroker!"
            show lexi a blank
            "I shake my head."
            bree.say "No, no, no..."
            bree.say "I mean work with another pro."
            bree.say "With me, Lexi!"
            show lexi a surprised
            "Realisation dawns on Lexi all of a sudden."
            "And she gapes at me in amazement."
            lexi.say "You mean you?"
            bree.say "Yes."
            lexi.say "Coming out and doing tricks?"
            bree.say "Right."
            lexi.say "With me?"
            bree.say "Uh-huh."
            lexi.say "For money?"
            bree.say "That's about the size of it."
            show lexi a smile
            "Lexi's already nodding with growing enthusiasm."
            "Like this is the greatest idea of all time."
            show lexi a happy
            lexi.say "That might just work, [hero.name]."
            lexi.say "Two blondes taking on the world..."
            lexi.say "We could make a fortune!"
            show lexi a smile
            bree.say "Let's just focus on making that twenty-five grand, okay?"
            $ lexi.flags.suggested_sex_work = True
        "Suggest that Lexi goes to university":
            "I don't have the means to pay off the debt for Lexi."
            "And even if I did, I'm not sure that would help in the long-run."
            "What she really needs is something to break her out of the rut she's in."
            "And I think I know just the thing."
            bree.say "You need to change things up, Lexi..."
            bree.say "Come down to the uni with me tomorrow morning."
            "Lexi listens with interest to what I have to say."
            show lexi a normal
            lexi.say "Why, [hero.name]?"
            lexi.say "You think I could get some business from the professors and students?"
            show lexi a blank
            bree.say "No, Lexi!"
            bree.say "I want you to sign up for a course, to improve yourself."
            show lexi a annoyed
            "As soon as the words are out of my mouth, Lexi looks doubtful."
            "She shakes her head, as if already dismissing the idea."
            show lexi a sadsmile
            lexi.say "Oh no, [hero.name]..."
            lexi.say "You need to be smart to go to uni."
            show lexi a smile
            bree.say "And that's what you are, Lexi..."
            bree.say "You've just had people telling you that you're not so long you believe it!"
            bree.say "Get an education and it'll open doors for you."
            bree.say "Then you can make money with your brain, not your body."
            "Lexi nods slowly, like she's still not sure."
            "But she's coming round to the idea as I keep on at her."
            show lexi a normal
            lexi.say "Okay, [hero.name]..."
            lexi.say "I'll give it a try."
            lexi.say "It's not like I have anything to lose!"
            show lexi a smile
            $ lexi.flags.suggested_university = True
        "Give Lexi the money she owes" if hero.money >= 25000:
            "I know that I already said I don't have the money to help out."
            "But that's what I tell anyone who comes to me with a sob story."
            "The truth is that I have enough squirrelled away right now to pay off the debt."
            "And it seems that doing so would be the best thing for Lexi too."
            "As it would get the pimp off her back, and mean she was out of danger."
            bree.say "Okay, Lexi..."
            bree.say "I'm going to give you the twenty-five grand."
            bree.say "But I need to know that you'll use it to pay the debt, okay?"
            show lexi a surprised
            "Lexi blinks in sheer amazement."
            "Like she can't believe what she's hearing."
            lexi.say "But, [hero.name]..."
            lexi.say "You just said..."
            show lexi a smile
            bree.say "Never mind what I just said."
            bree.say "You want me to pay the debt, yeah?"
            lexi.say "Yeah, of course I do."
            show lexi a smile
            bree.say "Then you don't need to know where the money came from."
            bree.say "Just that it's been paid-off, right?"
            show lexi a surprised
            "Lexi nods, still looking like she's stunned."
            lexi.say "Y...yeah, [hero.name]..."
            lexi.say "I owe you one - a big one!"
            show lexi a smile
            bree.say "To be more precise, you're going to owe me twenty-five grand."
            bree.say "But seeing as I'm your friend, I'll be more reasonable than your pimp!"
            $ hero.money -= 25000
            $ lexi.flags.paid_debt = True
    if lexi.love.max < 140:
        $ lexi.love.max = 140
    $ hero.cancel_activity()
    $ game.active_date.abort = True
    $ lexi.flags.delay = TemporaryFlag(True, 3)
    return

label lexi_female_event_09:
    scene bg university
    show lexi a smile zorder 2 at center, zoomAt(1.25, (640, 880))
    with fade
    "Part of me still can't believe that Lexi actually took me up on my suggestion."
    "That I'm taking her onto the uni campus to begin the process of enrolling on a course."
    "But I find myself snapped back to reality when I get a look at what Lexi's chosen to wear."
    if hero.morality >= 25:
        bree.say "Oh my goodness, Lexi..."
        bree.say "This is a university, not a nightclub!"
    if hero.morality <= -25:
        bree.say "Damn it, Lexi..."
        bree.say "Why didn't you tell me you were wearing so little today?"
        bree.say "Now I look like a total prude in comparison!"
    else:
        bree.say "Oh geez, Lexi..."
        bree.say "Uni's a pretty liberated kind of place."
        bree.say "But there's still a limit on how little you can wear!"
    "If my comments have any effect on Lexi, then she doesn't show it."
    show lexi a at center, traveling(1.5, 1.0, (640, 1040))
    "Instead she breezes past me, grabbing my hand as she does so."
    "Which means I'm dragged along in her wake, hurrying to keep up."
    show lexi a normal
    lexi.say "Ah, forget about it, [hero.name]."
    lexi.say "I might be doing a course here, but that's not gonna change me."
    lexi.say "In fact, I might be the one to change things around here, you know?"
    lexi.say "I've seen the movies, I know what these places are like."
    show lexi a smile
    "I feel myself bristle at Lexi's attitude, how arrogant she's being."
    "And also a little irritated, as I'm supposed to be the one showing her around."
    "Instead she's breezing onto the campus like she owns the place."
    bree.say "Don't be silly, Lexi."
    bree.say "You can't believe everything you see in films."
    "That was supposed to be me putting Lexi in her place."
    show lexi a happy at startle
    "But instead she lets out a snort of laughter and shakes her head."
    lexi.say "Ha!"
    show lexi a normal
    lexi.say "Come on, [hero.name]..."
    lexi.say "You know these places are full of stuffy academics and total nerds."
    lexi.say "Look, there's a bunch of them now!"
    show lexi a smile
    "I wince as Lexi's not even trying to keep her voice down as she says all of this."
    "Plus she's pointing at the group of students in question."
    "And I'm sure they've heard her too!"
    "I push her arm down and pull her after me as we get closer to the enrolment office."
    "But I do have to admit that the students she was pointing too were a tiny bit geeky."
    if hero.morality >= 25:
        bree.say "You can't go around saying things like that, Lexi."
        bree.say "You'll end up hurting people's feelings."
    elif hero.morality <= -25:
        bree.say "Urgh..."
        bree.say "I know they're total nerds, Lexi."
        bree.say "But you at least have to pretend that you like them!"
    else:
        bree.say "It's not cool to point out someone's a nerd, Lexi."
        bree.say "Even if it's totally obvious they are one."
    "Lexi allows me to hurry her along without protest."
    "But she doesn't seem to be impressed with my little lecture."
    show lexi a bored
    lexi.say "Nah, [hero.name]..."
    lexi.say "That's how it works, yeah?"
    show lexi a normal
    lexi.say "They're the nerds and we're the cool, outrageous kids."
    lexi.say "All we need now are the hot, dumb jocks and everyone's accounted for."
    show lexi a smile at center, traveling(1.5, 0.5, (1140, 1040))
    show bg classroom at center, zoomAt(1.5, (940, 900)) with hpunch
    "I'm just about hauling Lexi through the door of the enrolment office as she finishes saying all of this."
    show shawn work at center, zoomAt(1.25, (640, 1080)), blacker
    show board_games_table_01 as fg at center, zoomAt(1.25, (940, 1135)), blacker
    with dissolve
    "Which saves me the embarrassment of having the member of staff sitting behind the desk hear it."
    show shawn at center, zoomAt(1.0, (640, 1080)), blacker, startle
    "Staff member" "Good morning..."
    "Staff member" "How can I help you today?"
    "I give my usual smile."
    "The one I reserve for dealing with situations like this."
    "One filled with bland pleasantness and inoffensive charm."
    bree.say "Oh, hello..."
    bree.say "My friend here would like to speak to someone about enrolling?"
    bree.say "She's all geared up and ready to improve herself!"
    show lexi a normal at center, zoomAt (1.5, (940, 1040)) with MoveTransition(0.1)
    lexi.say "Hey!"
    lexi.say "Who said anything about me needing improvement?!?"
    show lexi a smile
    "I do the best I can to ignore Lexi's little outburst."
    "And I keep smiling at the person behind the desk."
    "Who, bless them, seems to be taking the exact same approach."
    show shawn at center, zoomAt(1.0, (640, 1080)), blacker, startle
    "Staff member" "Well we can certainly help with that."
    "Staff member" "I'll just fetch the appropriate forms."
    "Staff member" "What course was your friend hoping to sign up for?"
    "I open my mouth to answer."
    "But then I realise that I have no idea."
    "So instead I turn to Lexi, waiting for her to speak up."
    show lexi a normal
    lexi.say "Oh yeah, I've been thinking about that..."
    lexi.say "And I wanna study law."
    show lexi a smile
    "I might have had no idea what Lexi wanted to study."
    "But it still comes as a genuine surprise to find out it's Law!"
    bree.say "Law?"
    bree.say "Are you sure about that, Lexi?"
    show lexi a
    "Lexi shrugs and cocks her head on one side."
    show lexi a normal
    lexi.say "Well, I've been on the 'wrong side' of it more times than I can count."
    lexi.say "And I already know quite a bit about it thanks to that."
    lexi.say "So I figure that'll give me a head-start."
    show lexi a smile
    "I stop to think about what Lexi's saying."
    "And I have to admit that it makes sense."
    "In fact, it's kind of inspiring."
    "The kind of inspiring that makes a person do impulsive things."
    bree.say "You know what..."
    bree.say "Get me an application form too."
    bree.say "I'm switching over to study law as well."
    show lexi a surprised
    "For the first time since we got here, Lexi actually looks surprised."
    lexi.say "What are you doing, [hero.name]?"
    lexi.say "You don't have to take the same course as me."
    lexi.say "Don't you already have all this stuff figured out?"
    show lexi a blank
    "I shake my head, keen to let Lexi know it's okay."
    if hero.morality >= 25:
        bree.say "I want to do this, Lexi."
        bree.say "You've inspired me to make a change in my life!"
    elif hero.morality <= -25:
        bree.say "Ah, I never really liked my course anyway."
        bree.say "This way we can spend more time together."
        bree.say "Probably make more money at the end of it too!"
    else:
        bree.say "I know what I'm doing, Lexi."
        bree.say "This is one of those things that just feels right."
    show lexi a happy
    "Lexi shrugs again and takes her forms from the member of staff."
    show lexi a smile
    "As soon as I get mine, I fill it in, helping Lexi out here and there too."
    "We hand the forms back and then walk out of the enrolment office."
    scene bg university
    show lexi a normal at center, zoomAt (1.5, (340, 1040))
    with fade
    "And as we emerge into the open air, it feels like a new beginning."
    show lexi a normal
    lexi.say "This is going to be so cool, [hero.name]..."
    lexi.say "I bet you we end up being kick-ass lawyers and shit!"
    show lexi b happy blush
    "I nod and smile, eager to brighten Lexi's mood."
    "I figure she needs it, in light of the problems that brought her here."
    "Maybe she's right and we will make a success of this thing."
    "But even if not, it's a step towards getting her away from her former life."
    "Which has to be a good thing for everyone involved."
    if lexi.love.max < 160:
        $ lexi.love.max = 160
    $ lexi.flags.delay = TemporaryFlag(True, 3)
    return


label lexi_female_event_09b:
    scene bg taxi with fade
    "I find myself standing outside the hotel where Lexi told me to meet her."
    "And I have to say that my first impressions aren't all that bad."
    "When Lexi said she knew a place where we could rent a room, I was sceptical."
    "Because with her reputation, I was expecting a complete and utter shit-hole."
    "Instead this place is pretty nice, maybe a little rundown and past its prime."
    "But even so, I'd probably stay here if the rates were cheap enough."
    lexi.say "Hey, [hero.name]..."
    lexi.say "Are you ready to get rocked?"
    lexi.say "Are you pumped to get pumped?"
    show lexi a sexydate smile nophone at flip, center, zoomAt(1.25, (640, 880)) with easeinleft
    "I turn to see Lexi walking towards me, dressed for the occasion."
    "And not for the first time I find myself getting jealous of her wardrobe."
    bree.say "Damn it, Lexi..."
    bree.say "Where do you find outfits like that?"
    bree.say "I swear that thing has less material than a handkerchief!"
    show lexi a happy
    "Lexi smiles as she accepts the compliment."
    show lexi b smile at stepback
    "And she does a little turn on the spot to show herself off too."
    show lexi a normal
    lexi.say "The smaller the outfit, the shorter the time to get out of it!"
    lexi.say "You really should let me sort out your wardrobe, [hero.name]."
    lexi.say "I mean, don't get me wrong, you do dress pretty slutty."
    lexi.say "But with a little more effort, you could look like a complete whore!"
    show lexi a smile
    "I can't help smiling as Lexi returns my compliment."
    bree.say "You really think so?"
    bree.say "Because I have been trying to look more whorish recently."
    "Lexi and I keep on chatting about the subject as we walk into the hotel."
    show bg restaurant at flip, center, blur(5) with fade
    "But once we're in the lobby, she holds up a hand to silence me."
    "Then she begins looking this way and that."
    show lexi a normal
    lexi.say "We're bang on time for the appointment."
    lexi.say "And I told the punter to meet us in here."
    lexi.say "So where in the hell is he?"
    show lexi a smile
    "I join in the act of looking around too."
    "And soon my eyes settle on a pretty average-looking guy on the other side of the lobby."
    "He's doing the best he can to look like he's just standing there without a care in the world."
    "But he's one of those guy's that just ends up looking awkward and uncomfortable instead."
    bree.say "What about Anxious Arnold over there?"
    "Lexi looks in the direction that I'm pointing."
    "And then she nods her head."
    show lexi a normal
    lexi.say "Oh yeah..."
    lexi.say "He's got punter written all over him!"
    lexi.say "Okay, [hero.name], just follow my lead."
    show lexi a smile
    bree.say "Don't worry, Lexi..."
    bree.say "We want him to think he ordered two blonde bombshells."
    bree.say "Not a couple of blonde bomb-sites!"
    show bg restaurant at flip, center, blur(5) with fade
    show ryan at center, zoomAt(1.25, (940, 920)), blacker
    with fade
    show lexi a sexydate smile nophone at flip, center, zoomAt(1.25, (340, 880)) with easeinleft
    "Lexi strides over to where the guy's standing, with me just behind her."
    "And the moment he sees us, I read trepidation and excitement in his eyes."
    show ryan at center, zoomAt(1.0, (940, 920)), blacker, startle
    "Punter" "Are..."
    "Punter" "Are you Lexi and [hero.name]?"
    "Punter" "The girls I'm supposed to be meeting?"
    "Lexi goes into her professional act as soon as she opens her mouth."
    show lexi a at flip, center, zoomAt(1.25, (480, 880)) with ease
    "Leaning in close to the guy so he can get a good look at the merchandise."
    "I stay back, but I do the best I can to strike a sexy pose too."
    show lexi a normal
    lexi.say "That's right, sugar..."
    lexi.say "I'm Luscious Lexi, and this is Bountiful [hero.name]!"
    show lexi a smile
    "I'm not exactly sold on the of being described as 'bountiful'."
    "But as Lexi's the veteran here, I decide the best thing is to play along."
    "So I give the guy a little wave as he glances over in my direction."
    bree.say "Hey there..."
    bree.say "Great to meet you!"
    "The guy's nerves seem to be fading as he stares at Lexi and me."
    "Instead, I can almost feel the lust beginning to build up inside of him."
    "Punter" "Great..."
    "Punter" "That's great..."
    "Punter" "And I get both of you, right?"
    "Punter" "For the price we already agreed?"
    "As if to prove he has the cash, the guy pulls out a wad of notes."
    play sound woosh_punch
    show lexi a at center, zoomAt(1.0, (480, 880)), stepback(speed=0.1, v=100, h=-20)
    "But before he can say another word, Lexi pounces on it."
    "Which leaves him staring in amazement at his now empty hand."
    show lexi a normal
    lexi.say "Cash up front, sugar!"
    $ hero.money += 500
    lexi.say "Is all of it here?"
    show lexi a smile
    "Punter" "Yes..."
    "Punter" "But that's more than we agreed!"
    show lexi a normal
    lexi.say "You're giving us a tip?"
    lexi.say "So kind of you!"
    show lexi a smile
    "Punter" "But, but..."
    "Punter" "How will I get home?"
    bree.say "Don't worry about it."
    bree.say "With all that dough, we can afford to lend you the taxi fare!"
    show ryan at center, zoomAt(1.25, (840, 920)), blacker
    show lexi a sexydate smile nophone at center, zoomAt(1.25, (540, 880))
    with ease
    "Before the guy can argue, Lexi hustles him over to the elevator."
    "And we take a cramped, silent ride up a couple of floors."
    "Then Lexi leads the way to the room that we're renting."
    scene bg hotelroom
    show ryan at center, zoomAt(1.25, (840, 920)), blacker
    show lexi a sexydate smile nophone at flip, center, zoomAt(1.25, (540, 880))
    with fade
    "Once we're inside, I lock the door firmly."
    hide ryan
    show lexi a at flip, center, zoomAt(1.25, (640, 880))
    with easeoutleft
    "And Lexi pushes the guy down onto the bed."
    "Punter" "Whoa!"
    show lexi a normal
    lexi.say "Hold on, sugar..."
    lexi.say "Because you're in for a wild ride!"
    lexi.say "[hero.name], get your pert little butt over here already."
    lexi.say "It's time to go to work!"
    show lexi a smile
    "I do as I'm told, stripping off my clothes as I hurry to the bed."
    show lexi a naked with dissolve
    "Lexi's already removed hers and is undressing the punter just as quickly."
    scene bg hotelroom at center, blur(5), dark
    show lexi c blush smile naked at center, zoomAt(1.25, (640, 880))
    with fade
    "I watch as she takes hold of his dick, which I have to admit is surprisingly big."
    "And then begins to work it with her hand, ensuring it gets bigger still."
    "Lexi motions towards the guy's head, then points between my thighs."
    "Which tells me all I need to know about what's expected of me."
    show lexi c zorder 2 at center, zoomAt(1.5, (640, 1040)) with vpunch
    "Clambering onto the bed, I crawl over to the punter."
    "And then I straddle his chest, pinning his arms to the mattress."
    "He's looking up at me in sheer amazement as I do this."
    show sexinserts bottom bree as breepusssy at center, zoomAt(1.0, (1840, 780))
    show sexinserts bottom bree as breepusssy at center, traveling(1.0, 15.0, (-840, 780))
    "But once I lower myself onto his face, he disappears from view."
    "I'm expecting to have to give the guy detailed instructions."
    "But he takes me by surprise, beginning to probe with his tongue within seconds."
    "I feel it exploring the outer edge of my pussy, then sliding inwards."
    bree.say "Oh fuck..."
    bree.say "This is..."
    bree.say "This is some good shit!"
    show lexi happy
    "Lexi looks up from what she's doing, a wide smile on her face."
    show lexi c normal
    lexi.say "I told you so, [hero.name]..."
    lexi.say "The work is fun and the money is just great!"
    show lexi c wink
    "With that, she offers me a wink."
    show sexinserts head lexi as leximouth at center, zoomAt(1.0, (-520, 780))
    show sexinserts head lexi as leximouth at center, traveling(1.0, 10.0, (1840, 780))
    hide lexi with easeoutbottom
    "Then opens her mouth as she leans back in towards the guy's dick."
    show sexinserts chest lexi as lexiboobs at center, zoomAt(1.0, (-100, 2000))
    show sexinserts chest bree as breeboobs at center, zoomAt(1.0, (600, -500))
    show sexinserts chest lexi as lexiboobs at center, traveling(1.0, 5.0, (-100,-500))
    show sexinserts chest bree as breeboobs at center, traveling(1.0, 5.0, (600, 2000))
    show sexinserts head bree as breemouth at center, zoomAt(1.0, (1840, 880))
    show sexinserts head bree as breemouth at center, traveling(1.0, 7.0, (-520, 880))
    "What follows is a blur of intense pleasure and erotic discovery."
    "I feel like I've had the guy's dick in every possible hole more than once."
    "And in Lexi's case, it goes into places I never thought possible!"
    scene bg hotelroom
    show lexi c naked smile nophone zorder 1 at center, zoomAt(1.5, (640, 1040))
    with fade
    "When we're done, the punter is lying on his back, gasping for breath."
    "Lexi and I perch on the edge, almost as worn out as he is."
    bree.say "Is..."
    bree.say "Is it always this intense?"
    show lexi a normal
    lexi.say "Nah, this is just your first time, [hero.name]."
    lexi.say "You learn to pace yourself pretty quickly."
    lexi.say "Plus you build up stamina, and that helps too."
    show lexi a smile
    "I look at the bundle of notes in Lexi's hand."
    bree.say "I guess we're nowhere near close to paying off your debt?"
    show lexi a normal
    lexi.say "Oh, I don't know about that."
    lexi.say "I already did a couple of punters before you got here."
    lexi.say "So we're not looking too bad for the first day on the job."
    show lexi a smile
    "I shake my head in amazement, unable to believe Lexi's stamina."
    "Punter" "Erm..."
    "Punter" "So..."
    "Punter" "I'll be going then?"
    show lexi a naked smile nophone at flip, center, traveling(1.25, 0.2, (640, 880))
    show ryan naked at center, zoomAt(1.25, (840, 920)), blacker with easeinbottom
    "Lexi leaps up and begins to hustle the half-dressed guy out of the room."
    "She doesn't seem in the least bit concerned that she's naked as she does so."
    show lexi a at flip, center, zoomAt(1.25, (1140, 880))
    hide ryan
    with easeoutright
    "And the fact actually seems to help spur the guy on to flee into the corridor."
    "Punter" "Wait..."
    "Punter" "What about my taxi fare?!?"
    show lexi a angry
    lexi.say "What do we look like to you?"
    lexi.say "A fucking charity?"
    lexi.say "Go suck a dick for it!"
    show lexi a smile
    play sound door_slam
    "I can't help laughing as Lexi slams the door in his face."
    "Because I'm actually starting to think that this thing might work."
    "And I'm looking forward to the chance to have some fun with Lexi too."
    if lexi.love.max < 160:
        $ lexi.love.max = 160
    if "lexi_female_event_09b" not in DONE:
        $ lexi.flags.delay = TemporaryFlag(True, 3)
    return


label whore_work_with_lexi:
    if randint(0, 100) <= 25 and not game.flags.whore_work_delay:
        $ renpy.dynamic(customer=randchoice(list(Guy.all())).id)
        $ game.flags.whore_work_delay = TemporaryFlag(True, 15)
        scene bg_taxi_back_night
        show lexi sexydate lollipop at center, zoomAt(1.0, (640, 720))
        with fade
        "Lexi and I are back at work in front of the hotel, on the look out for potential customers."
        "And I have to say that I'm really starting to get into the swing of this whole thing."
        "At first I was letting Lexi take the lead and following her example."
        "But by now I'm really starting to feel like I get the idea and I'm catching on."
        show lexi at center, traveling(1.5, 0.3, (640, 1040))
        "So when the next potential client shuffles into view, I give Lexi a subtle nod."
        bree.say "How about this guy?"
        show lexi blank nophone with fade
        "Lexi casts her gaze in the same direction, her eyes settling on the man in question."
        "And I can see her sizing him up in a mere matter of seconds."
        show lexi smile
        lexi.say "Hmm..."
        show lexi normal
        lexi.say "Not bad, [hero.name]."
        lexi.say "You're getting the hang of this, aren't you?"
        show lexi smile
        "I can't help smiling as Lexi praises me."
        "Because it feels good to be winning her respect in matters like this."
        bree.say "Thanks, Lexi..."
        bree.say "So..."
        bree.say "What do we do next?"
        "Lexi nods her head in the direction of the potential customer."
        show lexi normal
        lexi.say "Well, he's already headed our way."
        lexi.say "So all we have to do is reel him in."
        if hero.morality <= -95:
            show lexi annoyed
            "Suddenly I see Lexi's expression become thoughtful."
            "Like something just occurred to her for the first time."
            show lexi normal
            lexi.say "Say, [hero.name]..."
            lexi.say "Why don't you take this one?"
            show lexi smile
            bree.say "Me?"
            bree.say "Are you sure?"
            "Lexi nods."
            show lexi normal
            lexi.say "Sure, [hero.name]..."
            lexi.say "I think you're ready."
            lexi.say "So what do you say?"
            show lexi smile
            menu:
                "I'll do it":
                    "I'm nodding my head almost as soon as Lexi's done asking the question."
                    "Because I instinctively know that ready for the responsibility."
                    bree.say "You got it, Lexi..."
                    bree.say "It's time I stepped up to the plate!"
                    "Lexi nods as she puts a reassuring hand on my shoulder."
                    show lexi normal
                    lexi.say "Just remember the basics, [hero.name]..."
                    lexi.say "You're the one doing him a favour, not the other way around."
                    show lexi wink
                    lexi.say "And make sure that he feels like he's paying to be taken to heaven and back, yeah?"
                    show lexi smile
                    "Now I'm the one nodding."
                    show lexi at center, traveling(1.25, 0.3, (1140, 880))
                    show expression f"{customer}" at blacker with easeinleft
                    "But my eyes are fixed on the potential client as he gets closer."
                    bree.say "Erm..."
                    bree.say "H...hey there..."
                    bree.say "Are you looking for a good time?"
                    "Okay, I know that's not the most original opening line."
                    "But it's my first attempt, so cut me some slack!"
                    "The guy looks up at the sound of my voice."
                    "And I can instantly see that he looks more nervous than I am."
                    "Guy" "Erm..."
                    "Guy" "Well, yeah..."
                    "Guy" "Of course I am!"
                    "Guy" "Why else would I be here if I wasn't?"
                    menu:
                        "Let me think":
                            "I think about it for a moment."
                            "And then it occurs to me."
                            bree.say "You might be looking to book a room for the night."
                            bree.say "Or you could have come here to meet someone, I guess..."
                            "The guy's looking at me with increasing incredulity."
                            "But by now my brain's wrapped itself around the question."
                            "And my nerves are fuelling the rubbish coming out of my mouth."
                            bree.say "I suppose there's any number of reasons you might have come in here."
                            bree.say "So I guess I shouldn't just assume you want to hire sex-workers!"
                            "At the mere mention of the word sex, the guy visibly flinches."
                            hide expression f"{customer}" with easeoutleft
                            "And without another word, he scuttles off in the opposite direction."
                            show lexi sexydate blank at center, traveling(1.5, 0.3, (840, 1040))
                            "As I watch him go, Lexi leans in close."
                            show lexi sadsmile
                            lexi.say "Well..."
                            lexi.say "That could have gone better!"
                            show lexi blank
                            bree.say "I'm sorry, Lexi..."
                            bree.say "I just kinda panicked."
                            show lexi smile
                            "Lexi smiles and pats me on the shoulder."
                            show lexi normal
                            lexi.say "Don't beat yourself up over it, [hero.name]."
                            lexi.say "You'll do better next time."
                            $ game.flags.story_hasworked = True
                            $ game.flags.hasworked = TemporaryFlag(True, "day")
                            return
                        "Let me show you" if hero.charm >= 75:
                            "I nod and smile, doing the best I can to look seductive as I do so."
                            bree.say "Well you came to the right place."
                            bree.say "My friend and I are more than ready to please."
                            "I gesture to myself and then to Lexi."
                            show lexi sexydate c
                            "Who obliges me by pulling off a pretty provocative pose."
                            "And it seems to work too."
                            "Because the guy's eyes almost pop out of their sockets."
                            "Guy" "I..."
                            "Guy" "I can have you both?!?"
                            "I nod and drape an arm over his shoulder."
                            bree.say "If you can pay the asking price..."
                            bree.say "You can have us both."
                            bree.say "Together, or one after the other."
                            bree.say "Hell, you can even watch us with each other."
                            scene bg restaurant at flip, center, blur(5)
                            show expression f"{customer}" at blacker, center, zoomAt(1.25, (440, 900))
                            show lexi sexydate smile at center, zoomAt(1.25, (840, 880))
                            with fade
                            "The next thing I know, the guy is nodding as we lead him to the elevator."
                            "Seems like I sealed the deal without Lexi even needing to say a word!"
                            "But now I have to back it up by putting on the performance of a lifetime."
                            "Something that I'm determined to do."
                            "Because it'll mean I can land the client and then deliver the goods too."
                "I prefer if you do it":
                    "I'm shaking my head almost as soon as Lexi's done asking the question."
                    "Because I instinctively know that I'm just not ready for so much responsibility."
                    bree.say "No, Lexi..."
                    bree.say "Not this time, okay?"
                    bree.say "Just let me watch you work your magic one more time."
                    bree.say "Then I'm sure that I'll be ready for the next one."
                    "For a moment I think that Lexi's going to insist that I do it."
                    "But then she smiles and nods her head."
                    show lexi smile
                    lexi.say "No worries, [hero.name]..."
                    show lexi wink
                    lexi.say "Just watch the master at work!"
                    show lexi smile at center, traveling(1.25, 0.3, (840, 880))
                    show expression f"{customer}" at blacker, center, zoomAt(1.25, (440, 900)) with easeinleft
                    "I feel a surge of relief as Lexi steps forwards."
                    "She does so just as the potential customer reaches us."
                    show lexi normal
                    lexi.say "Hey, baby..."
                    lexi.say "Where have you been all this time?"
                    show lexi smile
                    "The guy seems more than a little surprised by this line."
                    "He looks around the lobby, like he suspects a trap."
                    "Guy" "Huh?"
                    "Guy" "Wha...what are you talking about?"
                    show lexi flirt at center, traveling(1.15, 0.3, (720, 840))
                    "Lexi gives him a lazy grin as she leans forwards."
                    "Then she drapes herself over the guy, almost putting her head on his shoulder."
                    show lexi normal
                    lexi.say "I mean where have you been all of my life, sugar?"
                    lexi.say "Because me and my friend here..."
                    show lexi smile
                    "Lexi makes sure that the guy sees her pointing in my direction."
                    show lexi flirt
                    lexi.say "We've been waiting for you our entire lives!"
                    "I can see that the guy's already getting flustered."
                    "His eyes keep darting between Lexi and me."
                    "Guy" "I..."
                    "Guy" "I can have you both?!?"
                    "Lexi let's out a chuckle."
                    show lexi happy at startle
                    lexi.say "Ha, ha..."
                    lexi.say "Oh, sugar..."
                    lexi.say "For the right price, you can have anything you want!"
                    scene bg restaurant at flip, center, blur(5)
                    show expression f"{customer}" at blacker, center, zoomAt(1.25, (440, 900))
                    show lexi sexydate smile at center, zoomAt(1.25, (840, 880))
                    with fade
                    "The next thing I know, the guy is nodding as we lead him to the elevator."
                    "Seems like Lexi sealed the deal without me even needing to say a word!"
                    "But now I have to make up for it by putting on the performance of a lifetime."
                    "Something that I'm determined to do, so as to keep up my side of the bargain."
        else:
            show lexi smile at center, traveling(1.25, 0.3, (840, 880))
            show expression f"{customer}" at blacker, center, zoomAt(1.25, (440, 900)) with easeinleft
            "Lexi steps forwards."
            "She does so just as the potential customer reaches us."
            show lexi normal
            lexi.say "Hey, baby..."
            lexi.say "Where have you been all this time?"
            show lexi smile
            "The guy seems more than a little surprised by this line."
            "He looks around the lobby, like he suspects a trap."
            "Guy" "Huh?"
            "Guy" "Wha...what are you talking about?"
            show lexi flirt at center, traveling(1.15, 0.3, (720, 840))
            "Lexi gives him a lazy grin as she leans forwards."
            "Then she drapes herself over the guy, almost putting her head on his shoulder."
            show lexi normal
            lexi.say "I mean where have you been all of my life, sugar?"
            lexi.say "Because me and my friend here..."
            show lexi smile
            "Lexi makes sure that the guy sees her pointing in my direction."
            show lexi flirt
            lexi.say "We've been waiting for you our entire lives!"
            "I can see that the guy's already getting flustered."
            "His eyes keep darting between Lexi and me."
            "Guy" "I..."
            "Guy" "I can have you both?!?"
            "Lexi let's out a chuckle."
            show lexi happy at startle
            lexi.say "Ha, ha..."
            lexi.say "Oh, sugar..."
            lexi.say "For the right price, you can have anything you want!"
            scene bg restaurant at flip, center, blur(5)
            show expression f"{customer}" at blacker, center, zoomAt(1.25, (440, 900))
            show lexi sexydate smile at center, zoomAt(1.25, (840, 880))
            with fade
            "The next thing I know, the guy is nodding as we lead him to the elevator."
            "Seems like Lexi sealed the deal without me even needing to say a word!"
            "But now I have to make up for it by putting on the performance of a lifetime."
            "Something that I'm determined to do, so as to keep up my side of the bargain."
    else:
        show chibi whore_with_lexi
        "I spend an evening working the night with Lexi."
    $ hero.money += 500
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return


label lexi_female_event_09c:
    scene bg street with fade
    "I'm waiting to meet Lexi with what I can only describe as trepidation filling me."
    "That's because she's told me that she has a surprise in store for me tonight."
    "Now with anyone else, that would have filled me with curiosity and excitement."
    "But Lexi's one of those people with whom you can never quite be sure."
    "I mean, yeah, what she has planned could turn out to be amazing."
    "But there's always the chance it could be something equally awful too."
    "Like maybe she's decided to ignore my advice about the whole debt problem."
    "And instead she's hired someone to bump the pimp off instead."
    show lexi a smile sexydate nophone at center, zoomAt(1.25, (640, 880)) with easeinright
    "So when she turns up not spattered in someone else's blood, it's quite a relief."
    show lexi a normal
    lexi.say "Hey, [hero.name]..."
    lexi.say "Glad you could make it."
    show lexi a smile
    "I open my mouth to greet Lexi."
    show lexi a at center, zoomAt(1.5, (640, 1040)), top_to_bottom
    "But then I stop to look her up and down."
    show lexi a normal
    lexi.say "What's the matter, [hero.name]?"
    lexi.say "Don't you recognise me or something?"
    "I shake my head at the question, because that's not it."
    "What's got me so amazed is the outfit that Lexi has on tonight."
    show lexi a smile at center, zoomAt(1.5, (640, 1040)), bottom_to_top
    "Sure, it's totally revealing and looks like she could have found it in a dumpster."
    "But for her, it's almost conservative!"
    if hero.morality >= 25:
        bree.say "Your outfit, Lexi..."
        bree.say "I'm used to it being so much smaller!"
    elif hero.morality <= -25:
        bree.say "What's with the outfit, Lexi?"
        bree.say "You're practically dressed up like a nun!"
    else:
        bree.say "You're covering up more than usual, Lexi..."
        bree.say "Are you starting to feel the cold or something?"
    "I'm expecting Lexi to shoot back with an insult of some kind."
    "Or at the very least a cutting comment about why I'm wrong."
    "But instead she surprises me by looking away for a moment."
    hide lexi
    show lexi a annoyed blush sexydate nophone at center, zoomAt(1.5, (640, 1040))
    "And if it were anyone else, I'd have thought she was embarrassed."
    show lexi a normal blush
    lexi.say "Ah..."
    lexi.say "Lay off, [hero.name]..."
    lexi.say "A girl doesn't always have to wear next to nothing!"
    show lexi a smile
    "Again I find myself almost gob-smacked by what I'm hearing."
    "The Lexi that I know always tries to wear as little as she can get away with."
    "But I can see that the subject is making Lexi uncomfortable, so I let it drop."
    bree.say "So..."
    bree.say "What did you have in mind for tonight, Lexi?"
    bree.say "You want to grab some junk-food?"
    bree.say "Then maybe hit some bars afterwards?"
    bree.say "Round it all off with a trip to a night-club?"
    show lexi a blank -blush
    "Lexi shakes her head at all of this."
    "Which is odd, because that's pretty much her idea of a good night out."
    show lexi a normal
    lexi.say "Nah..."
    lexi.say "I thought we could do something a little more relaxed tonight."
    lexi.say "So I booked us a table at that restaurant over there."
    show lexi a smile
    "Lexi points to the restaurant a few doors down the street."
    "But I'm too busy staring at her to be able to notice."
    bree.say "Okay, lady..."
    bree.say "Who in the hell are you?"
    bree.say "And what have you done with the real Lexi?"
    show lexi wink
    "Lexi rolls her eyes at this, chuckling to herself."
    show lexi at center, traveling(1.75, 0.2, (640, 1190))
    "But as she puts her arm in mine, I can still sense that odd nervous energy around her."
    show lexi a normal
    lexi.say "Stop it, [hero.name]!"
    lexi.say "I'm not doing anything crazy."
    lexi.say "What's wrong with me wanting to eat at a nice restaurant for once?"
    show lexi a smile
    bree.say "Okay, Lexi..."
    bree.say "You remember all the times I wanted to do that?"
    bree.say "You were the one telling me what was wrong with it back then!"
    scene bg restaurant
    show ryan at center, zoomAt(1.25, (640, 900)), blacker
    with fade
    show lexi a smile sexydate nophone at center, zoomAt(1.25, (940, 880)) with easeinright
    "By now we're walking into the restaurant."
    "And Lexi strides straight over to the maître de."
    show lexi a normal
    lexi.say "I have a reservation for two."
    lexi.say "Would you mind checking the list?"
    show lexi a smile
    "This is greeted with an obedient nod."
    "And mere moments later we're escorted to a pretty sweet table."
    show restaurant meal lexi sexydate nomeals with fade
    "As soon as we're sat down, menus are handed over for our perusal."
    "Then the maître de leaves us to make our selections."
    "The moment he's gone, I lean over the table."
    if hero.morality >= 25:
        bree.say "Okay, Lexi..."
        bree.say "You're really starting to scare me now!"
        bree.say "What's going on?"
    elif hero.morality <= -25:
        bree.say "Spill the beans, Lexi..."
        bree.say "Did you land a seriously loaded new client?"
        bree.say "Because this place looks really expensive!"
    else:
        bree.say "Alright, Lexi..."
        bree.say "Start talking and don't stop until I'm not confused anymore."
        bree.say "What's going on here?"
    "Lexi glances around the restaurant before she answers me."
    "Almost as if she's worried that someone will overhear what she has to say."
    "Which does nothing to calm my fears about what's going on."
    show restaurant meal happy
    lexi.say "Okay, okay..."
    lexi.say "We're kind of here to celebrate."
    lexi.say "Because I have a big announcement to make."
    show restaurant meal -happy
    "I hold my breath in anticipation of what's coming next."
    "Waiting for my worst fears to be confirmed."
    "For Lexi to tell me that she's had her pimp taken out by a hitman or something like that."
    show restaurant meal happy
    lexi.say "I listened to the advice you gave me the other day, [hero.name]."
    lexi.say "Then I went away and thought about it, really turned it over in my head."
    lexi.say "And I decided that all of my problems are caused by what I do to make money."
    show restaurant meal -happy
    "I nod along with all that Lexi's saying."
    "I could be saying I told you so."
    "But that would make me look totally petty right now."
    show restaurant meal happy
    lexi.say "So I've decided to stop turning tricks."
    lexi.say "And I haven't done a single one since."
    show restaurant meal -happy hold
    "I reach across the table and take hold of Lexi's hand."
    if hero.morality >= 25:
        bree.say "Oh, Lexi..."
        bree.say "That's such great news."
        bree.say "I'm really proud of you."
    elif hero.morality <= -25:
        bree.say "That's so brave of you, Lexi."
        bree.say "I mean, you can still get all the cock you want."
        bree.say "But you can always do something else to pay the bills."
    else:
        bree.say "Well done, Lexi..."
        bree.say "I promise you won't regret this."
    show restaurant meal blush
    "Lexi seems genuinely touched by my response."
    "She turns her hand over and intertwines her fingers with mine."
    lexi.say "Thanks, [hero.name]..."
    lexi.say "I could never have done it without your advice."
    lexi.say "And your support as a friend."
    show restaurant meal -blush -hold order with fade
    show restaurant_meal_waiter_pose03 as man zorder 1 at right4 with easeinright
    "Our conversation is interrupted by the arrival of the waiter."
    "So we order our food and chat while waiting for it's arrival."
    show restaurant meal -blush -nomeals eat with fade
    hide restaurant_meal_waiter_pose03 as man with easeoutright
    "The meal that follows is pretty much like an average meal in a restaurant."
    "It's only Lexi's presence and new-found manners that make it feel a little strange."
    show restaurant meal nomeals askbill with fade
    "And when the time comes to pay the bill, the strangeness only seems to continue."
    bree.say "What do you say we split the bill, Lexi?"
    show restaurant meal bored normal
    lexi.say "Oh no..."
    lexi.say "Not tonight, [hero.name]."
    show restaurant meal -bored happy
    lexi.say "I'll take care of it."
    show restaurant meal -happy
    "I hold up my hands, letting Lexi snatch up the bill."
    "But I stay alert, as this is the point where the old Lexi would have done a dine and dash."
    "Yet as I watch, she does exactly as she promised, pulling out the money and handing it over."
    "She even includes a pretty generous tip!"
    scene bg street
    show lexi b smile sexydate nophone at center, zoomAt(1.5, (640, 1040))
    with fade
    "Lexi and I walk out of the restaurant together, chatting away."
    "And as we stroll off down the street, I feel like something new is beginning."
    "Like I'm getting to see the birth of a totally new Lexi."
    "One that keeps all of the good stuff from the original."
    "But dumps all of the old bad habits and leaves them in the past."
    if lexi.love.max < 180:
        $ lexi.love.max = 180
    $ lexi.flags.delay = TemporaryFlag(True, 3)
    $ game.active_date.score = 100
    $ game.active_date.stay = False
    $ game.pass_time(2)
    return


label lexi_female_event_10:
    scene bg classroom
    show studywith lexi nonpc
    with fade
    "I'm sitting at my desk, doing the best I can to wrap my head around the subject at hand."
    "But my concentration is broken when someone drops a veritable mountain of books in front of me."
    with vpunch
    bree.say "Aargh!"
    show lexi nophone zorder 3 at flip, center, zoomAt(1.35, (360, 850)) with easeinleft
    lexi.say "Whoa, [hero.name]..."
    lexi.say "Don't shit yourself - it's only me!"
    "I look up at Lexi, and then around at all the disapproving looks my outburst has earned me."
    "Then I do the best I can to flatten myself against the top of the desk in the hope of hiding."
    bree.say "Okay, okay..."
    bree.say "Just don't drop a ton of books on my head next time, yeah?"
    hide lexi
    show studywith lexi -nonpc
    with fade
    "Lexi rolls her eyes as she slumps down in the seat next to me."
    "Then she reaches out and idly flicks through the pages of the book atop the pile."
    scene studywith_bg as bg zorder 1 at flip, center, zoomAt(2.1, (1250, 1300))
    show lexi a annoyed nophone zorder 2 at flip, center, zoomAt(2.0, (640, 1300))
    with fade
    lexi.say "Urgh..."
    lexi.say "I never knew I'd have to read so many books to get a law degree!"
    lexi.say "And none of these have pictures, I already checked."
    lexi.say "But I figure if I start reading them now, I'll be done that much sooner."
    show lexi a sad
    "I can't help frowning at this."
    "Because it just doesn't sound right."
    bree.say "Erm, Lexi..."
    bree.say "You do know that's just the reading list for this semester, right?"
    bree.say "And there's going to be a new one for the next semester?"
    show lexi a annoyed
    "Lexi looks at me like I just told her we're going to be shot at dawn."
    "She slumps back in her chair and throws up her arms."
    show lexi a bored
    lexi.say "I'm doomed, [hero.name]..."
    lexi.say "They're going to bury me under a mountain of books!"
    lexi.say "What am I gonna do?!?"
    show lexi a sad
    "I can't help letting out a chuckle at Lexi's protestations."
    "But she doesn't seem to see my laughter in the way it's intended."
    show lexi a angry
    lexi.say "Oh yeah, laugh it up..."
    lexi.say "Some friend you are!"
    show lexi a annoyed
    bree.say "Stop being such a drama-queen, Lexi!"
    bree.say "It's not like you have to read all of those books from cover to cover."
    bree.say "Look at the study-guide they gave us, yeah?"
    bree.say "Certain chapters are highlighted for different classes and assignments."
    show lexi a surprised
    "Lexi looks surprised by this."
    "And she leans in to take a closer look."
    lexi.say "What?"
    lexi.say "Why didn't anyone tell me that?!?"
    show lexi a blank
    bree.say "They did, Lexi..."
    bree.say "But I think that was the time you were staring at the professor the whole lesson!"
    show lexi a sadsmile
    lexi.say "Oh come on, [hero.name]..."
    lexi.say "You can't blame me for that - he was a total hottie."
    lexi.say "If I fail his class, I hope he wants to give me some corporal punishment!"
    show lexi a smile
    "I do the best I can to ignore Lexi's lascivious ways."
    "And instead I take out her notebook and some coloured pens."
    bree.say "What you need is a study-plan, Lexi!"
    bree.say "So let's get you set up with one."
    scene bg classroom
    show studywith lexi
    with fade
    "Together, Lexi and I figure out a timetable for her."
    "Allocating times when she's going to be studying and attending classes."
    "And I'm also sure to include plenty of periods when she can do fun stuff too."
    scene studywith_bg as bg zorder 1 at flip, center, zoomAt(2.1, (1250, 1300))
    show lexi a surprised nophone zorder 2 at flip, center, zoomAt(2.0, (640, 1300))
    with fade
    lexi.say "Huh..."
    show lexi a happy
    lexi.say "Now it's all chopped up into bite-sized chunks, it doesn't look so bad."
    show lexi a smile
    bree.say "I told you so, Lexi..."
    bree.say "Now let's get our heads down for the rest of the period."
    bree.say "Or that professor of yours is going to be spanking us both!"
    show lexi a happy
    lexi.say "Fuck sake, [hero.name]..."
    lexi.say "You're supposed to be encouraging me to work harder..."
    lexi.say "Not give me reasons to slack off even more!"
    $ hero.knowledge += 3
    $ lexi.flags.helped_study += 1
    if lexi.flags.helped_study >= 10 and lexi.love.max < 180:
        $ lexi.love.max = 180
    return


label lexi_female_event_10b:
    scene bg restaurant at flip, center, blur(5)
    show lexi casual smile nophone at center, zoomAt(1.5, (640, 1040))
    with fade
    "Lexi and I have just kicked another satisfied customer out of the hotel lobby."
    "And we're totally engrossed in the act of counting up the money we just made."
    "I have the wad of crumpled notes we relieved the guy of in my hand."
    "And Lexi watches eagerly as I count them up."
    bree.say "Fifty, sixty, seventy..."
    show lexi normal
    lexi.say "Oh yeah..."
    lexi.say "Keep going, [hero.name]!"
    show lexi smile
    bree.say "Eighty, ninety, one hundred..."
    show lexi normal
    lexi.say "Oh man..."
    show lexi wink
    lexi.say "I swear counting money turns me on more than any cock ever could!"
    show lexi smile
    "I allow myself a wicked little giggle before I start counting again."
    "And that's when I hear the sound of a far deeper laugh behind me."
    show lexi blank at center, zoomAt(1.5, (840, 1040)) with ease
    "Lexi and I turn around, instinctively trying to hide the money."
    show danny casual shout at center, zoomAt(1.0, (240, 740)) with easeinleft
    danny.say "Aw..."
    danny.say "What'd have to go and do that for?"
    show danny joke
    danny.say "All that money was getting me nice and hard too!"
    show danny smile
    show lexi annoyed
    "As soon as Lexi recognises the guy, she curls her lip in almost growls."
    show lexi angry
    lexi.say "Danny..."
    lexi.say "What the fuck are you doing here?!?"
    show lexi annoyed
    "Of course it's Danny, Lexi's long-time pimp."
    "I should have guessed that he'd show up sooner or later."
    bree.say "Yeah, you deadbeat..."
    bree.say "This operation is all ours."
    bree.say "And you've got no business being here!"
    "I didn't think that we were going to be able to intimidate Danny into leaving us alone."
    "But I was hoping that we might have at least been able to convince him we're serious."
    show danny joke at startle
    "Instead our efforts earn us another round of laughter as he shakes his head."
    show danny shout at center, traveling(1.25, 0.5, (340, 920))
    danny.say "Heh..."
    danny.say "I can see why Lexi chose to go into business with you, [hero.name]."
    danny.say "You're one tough little bitch, and that's for sure."
    danny.say "I see you making me a hell of a lot of money in the future."
    show danny smile
    "Now I'm feeling doubly insulted."
    "And I can't keep from firing back at him."
    bree.say "Make money for you?"
    bree.say "What's that supposed to mean?!?"
    bree.say "We already told you this is an independent venture."
    show lexi normal
    lexi.say "Yeah, Danny..."
    show lexi angry
    lexi.say "You'll get your damn money."
    lexi.say "Don't worry about that!"
    show lexi annoyed
    "Danny shakes his head at this, still looking amused."
    show danny shout
    danny.say "You two skanks need to realise something..."
    danny.say "When you're one of my girls, I own your ass."
    danny.say "That means I own everything you do as well."
    danny.say "You could go start whoring your ass at the North Pole, Lexi..."
    danny.say "But what you make would still be mine!"
    show danny smile
    "Now I'm the one shaking my head, trying to interject myself."
    bree.say "That might be the case with Lexi."
    bree.say "But it isn't with me, Danny."
    bree.say "We'll make sure you get a good percentage of our profits."
    bree.say "At the rate we're going, you'll be paid back in no time."
    show danny upset
    "Danny's expression finally changes, and his features darken."
    show danny at center, traveling(1.5, 0.3, (440, 1080))
    show lexi at center, traveling(1.25, 0.3, (1040, 880))
    "He turns his attention to me, looming over me as he does so."
    show danny shout
    danny.say "You need to understand how business works in my world, [hero.name]."
    danny.say "If I say I own both your asses, then I own those pert little tushies."
    danny.say "The only way that changes is if someone comes along that can change my mind."
    danny.say "It's the law of the jungle, sweet-cheeks - and I'm the big, scary lion in that jungle!"
    show danny upset
    "I look to Lexi for support."
    "But to my dismay, all she can offer is a helpless shrug."
    "My guess is that she's more than used to being in this situation with Danny."
    "And if I want to come up with a novel solution, then I'll have to do it myself."
    menu:
        "Give in to Danny":
            "I'm getting worried about the way the fights gone out of Lexi right now."
            "Normally I'd just see a guy like Danny as a bully and want to stand up to him."
            "But I know how tough Lexi is, and if she won't fight, then I need to take note."
            bree.say "What do you say, Lexi?"
            bree.say "You're the one that owes him the money."
            bree.say "And maybe this would pay it off quicker?"
            "Danny begins to smile as I say all of this."
            "Probably because he can sense the conflicting emotions inside of me."
            show danny joke
            danny.say "You should listen to her, Lexi..."
            danny.say "She's obviously way smarter than you!"
            show danny smile
            "I do the best I can to ignore Danny."
            "And instead I focus all of my attention on Lexi."
            show lexi sadsmile
            lexi.say "I guess so, [hero.name]..."
            lexi.say "There's no other way to get rid of the creep."
            show lexi sad
            "Danny seems happy to take this as confirmation of his victory."
            "He snatches the notes out of my hand and begins to count them for himself."
            "When he's done, Danny hands me back a pathetically small portion of them."
            "He pockets the rest, nodding his head as though he's finally satisfied."
            show danny shout
            danny.say "That's how this is going to go from now on."
            danny.say "All the money you make, you bring to me."
            danny.say "I'll decide how much I keep, and no arguments."
            show danny smile
            "From somewhere I find the courage to speak up."
            bree.say "And what you take gets deducted from Lexi's debt?"
            show danny shout
            danny.say "Some of it, but not all of it."
            danny.say "I ain't letting you turn tricks just to service the debt."
            danny.say "I'll be taking my normal cut before anything goes towards what Lexi owes."
            show danny smile
            "I can't believe what I'm hearing."
            "Because it means Danny has us wrapped around his finger."
            "But Lexi puts a hand on my arm before I can speak."
            show lexi sadsmile
            lexi.say "Okay, Danny, okay..."
            show lexi angry
            lexi.say "You got what you wanted."
            lexi.say "Now how about you fuck off?"
            show lexi annoyed
            "Danny doesn't seem in the least bit insulted by this."
            "Instead he treats us to another crooked smile."
            hide danny with easeoutleft
            "Then he turns on his heel and walks out of the hotel."
            "Waving the wad of notes in the air as he goes."
            bree.say "Urgh..."
            bree.say "Did we really let him just walk in here and take over?!?"
            show lexi bored at center, traveling(1.5, 0.3, (640, 1040))
            lexi.say "Let it go, [hero.name]..."
            show lexi sadsmile
            lexi.say "We got off lightly, believe me."
            lexi.say "I've seen Danny do far worse to other girls."
            show lexi blank
            "I sense there's no point in arguing anymore."
            "So I just resign myself to the situation."
            "But I also vow to be on the lookout for any solutions that might present themselves along the way."
            $ lexi.flags.submitted_to_danny = True
        "Stand up to Danny":
            "If Lexi's not going to stand up to this guy, then I guess I will."
            "He looks like a bully, the kind of guy used to throwing his weight about to get his way."
            bree.say "You know that a lioness is deadlier than a lion, right?"
            bree.say "They do all the killing, while the male lions just laze around."
            bree.say "They even kick their asses when they step out of line too!"
            show lexi surprised
            "Lexi looks at me like she can't believe what she's hearing."
            show lexi sad
            "I feel her put a hand on my arm, and I see that she's shaking her head."
            "But I've already gone too far now to be able to back down."
            "If I did, we'd practically have to grovel in front of Danny to make it up to him."
            show danny shout
            danny.say "Is that so, [hero.name]?"
            show danny angry
            danny.say "Sounds like you're fixing to start a fight!"
            show danny upset
            bree.say "You got that, did you, Danny?"
            bree.say "I was worried I'd have to explain it with sock-puppets!"
            show danny shout
            danny.say "Nah, [hero.name]..."
            danny.say "I got it."
            danny.say "But you should know something..."
            show danny angry
            danny.say "I ain't afraid of hitting a woman!"
            show danny psycho
            bree.say "And I'm not afraid of hitting a piece of shit!"
            show danny joke at startle
            "Danny laughs and turns a little way to the side."
            "But then I catch a sudden movement in my peripheral vision."
            show lexi surprised
            lexi.say "[hero.name.upper()]..."
            lexi.say "LOOK OUT!"
            "I barely have time to leap out of the way as Danny tries to sucker-punch me."
            "And just like that, the fight is on!"
            if hero.has_skill("martial_arts"):
                call lexi_female_event_11b from _call_lexi_female_event_11b
            else:
                call lexi_female_event_11d from _call_lexi_female_event_11d
    if lexi.love.max < 200:
        $ lexi.love.max = 200
    return


label lexi_female_event_11b:
    $ DONE["lexi_female_event_11b"] = game.days_played
    "Danny's chuckling to himself as I take up a fighting stance, and try to look tough."
    "All the time I'm praying that the martial arts classes I took are going to pay off."
    "Because he really doesn't seem to be taking me seriously at all!"
    show danny shout
    danny.say "Where'd you learn to stand like that, [hero.name]?"
    show danny joke
    danny.say "Some ladies self-defence class?"
    show danny normal
    "I can feel my blood starting to boil in my veins by now."
    "And I really want to be able to prove the jerk wrong."
    bree.say "Shut your mouth, Danny..."
    bree.say "You're nothing but a big bully!"
    "Danny doesn't seem in the least bit impressed with my threats."
    "Instead he keeps right on laughing."
    "Hell, he even sticks out his chin as an open invitation!"
    show danny shout
    danny.say "Tell you what..."
    danny.say "Why don't you make me, huh?"
    show danny normal
    "That's it, the final straw."
    "I feel my patience snap and my temper reach its limit."
    "Then I swing what I hope is my best punch at Danny's chest."
    bree.say "Take that, you pig!"
    play sound punch_hard
    pause 0.2
    hide lexi
    hide danny
    show danny punched hit
    with hpunch
    "I feel the blow connect."
    "And I wince, because it bloody well hurts me!"
    "But a moment later I have the immense comfort of knowing that it did the same to Danny too."
    "Because I see his head snap around from the blow."
    "Hell, he even staggers backwards."
    danny.say "Ouch..."
    hide danny punched
    show lexi casual blank nophone at center, zoomAt (1.25, (940, 880))
    show danny surprised at center, zoomAt (1.25, (340, 920))
    with hpunch
    danny.say "Hey!"
    show danny upset
    danny.say "You fucking bitch, that really hurt!"
    show danny upset
    "I can feel my confidence beginning to rise with each passing second."
    "So much so that I manage to raise an eyebrow and try to look cocky."
    bree.say "Well that's the whole idea, dumbass!"
    bree.say "Getting punched is supposed to hurt!"
    "I throw Lexi a knowing grin."
    show lexi smile
    "And she returns the gesture."
    show lexi surprised
    "But then I see her eyes go wide, and she points at something."
    lexi.say "[hero.name]..."
    lexi.say "Behind you!"
    play sound woosh_punch
    hide lexi
    hide danny
    show danny faceslap missed
    with hpunch
    "I react just in time, lurching out of the way as Danny swings for me."
    "He was trying to sucker-punch me, but then what else would you expect?"
    "Danny's a scumbag to start with, and he just got his bell rung by a girl!"
    hide danny
    show lexi casual blank nophone at center, zoomAt (1.25, (940, 880))
    show danny surprised at center, zoomAt (1.25, (340, 920))
    with hpunch
    danny.say "Wha..."
    danny.say "Hold still and let me hit you, dammit!"
    show danny upset
    "Now it's my turn to laugh, shaking my head at Danny."
    bree.say "You know what, Danny..."
    bree.say "Even if I did that, I don't think it'd help you!"
    "I can feel the lessons that I took in martial arts kicking in."
    "And I'm almost reacting without even having to think about it."
    "Like, Danny's stance is totally sloppy, and his guard is even worse."
    play sound punch_hard
    pause 0.2
    hide lexi
    hide danny
    show danny punched hit with hpunch
    "So it's easy as hell for me to land another couple of punches."
    "Each one seems to surprise him more than the last."
    play sound punch_hard
    pause 0.2
    show danny punched hit with hpunch
    "Danny's head bounces from side to side as I hit him."
    "And every blow makes his expression that much more vacant."
    play sound punch_hard
    pause 0.2
    show danny punched hit with hpunch
    danny.say "Huh..."
    danny.say "Wha..."
    danny.say "Wut..."
    play sound punch_hard
    pause 0.2
    show danny punched hit with hpunch
    "Finally his head is down so low that I can even use my knees."
    "And I don't hesitate to slam it into the underside of his jaw."
    "Danny staggers from this, totally unable to defend himself."
    "So I give him another punch to the side of the head."
    play sound punch_hard
    pause 0.2
    show danny punched hit with hpunch
    "Which is enough to send him crashing to the floor."
    hide danny
    show danny angry at center, zoomAt (1.25, (340, 920))
    show lexi casual blank nophone at center, zoomAt (1.25, (940, 880))
    show lexi at center, zoomAt (1.25, (640, 880)) with MoveTransition(0.1)
    "Before I can even catch my breath, Lexi rushes over."


    show danny surprised at center, zoomAt (1.25, (340, 920)), vshake
    pause 0.1
    show lexi casual blank at center, zoomAt (1.25, (940, 880)) with MoveTransition(0.1)
    hide danny with easeoutbottom
    "She plants a vicious kick into Danny's groin, then throws her arms around me."
    lexi.say "Oh, [hero.name]..."
    hide lexi
    hide danny
    show lexi kiss casual
    with hpunch
    lexi.say "You're my hero!"
    "And when she plants a kiss on my lips, I don't object in the slightest."
    "The kiss is extremely pleasant, and I'd have liked it to last longer."
    "But then, out of the corner of my eye, I see Danny beginning to move."
    hide lexi kiss
    show lexi casual smile nophone at center, zoomAt (1.5, (640, 1040))
    with fade
    "Breaking away, I stand over the defeated pimp, arms crossed and frowning."
    bree.say "Keep on crawling, you scum."
    bree.say "And don't ever come back."
    show lexi angry
    lexi.say "Yeah, you heard her, Danny..."
    lexi.say "Fuck right off!"
    show lexi smile
    "Danny seems to be doing exactly as he's told."
    "Crawling towards the doors, he doesn't even look back once."
    show lexi at center, zoomAt (1.5, (440, 1040)) with MoveTransition(0.1)
    "Lexi follows, planting a foot in his ass as he reaches the exit."
    "Then she uses it to push him out of the door and down the stairs."
    show lexi at center, zoomAt (1.5, (640, 1040)) with MoveTransition(0.1)
    bree.say "Good riddance to bad rubbish!"
    show lexi happy
    lexi.say "Yeah..."
    lexi.say "We finally flushed that piece of shit!"
    show lexi smile
    "Laughing and congratulating ourselves, we walk back into the lobby."
    "Making a point of waving the wads of cash we've made as we do so."
    "Now that we dealt with Danny, there's nothing to stand in our way."
    "Lexi and I are free to do as we please."
    "And all the money we make along the way is ours alone."
    $ lexi.flags.fought_danny_won = True
    return


label lexi_female_event_11d:
    $ DONE["lexi_female_event_10d"] = game.days_played
    "Danny's chuckling to himself as I take up a fighting stance, and try to look tough."
    "All the time I'm praying that the martial arts classes I took are going to pay off."
    "Because he really doesn't seem to be taking me seriously at all!"
    show danny shout
    danny.say "Where'd you learn to stand like that, [hero.name]?"
    show danny joke
    danny.say "Some ladies self-defence class?"
    show danny normal
    "I can feel my blood starting to boil in my veins by now."
    "And I really want to be able to prove the jerk wrong."
    bree.say "Shut your mouth, Danny..."
    bree.say "You're nothing but a big bully!"
    "Danny doesn't seem in the least bit impressed with my threats."
    show danny joke at startle
    "Instead he keeps right on laughing."
    "Hell, he even sticks out his chin as an open invitation!"
    show danny shout
    danny.say "Tell you what..."
    show danny angry
    danny.say "Why don't you make me, huh?"
    show danny normal
    "That's it, the final straw."
    "I feel my patience snap and my temper reach its limit."
    "Then I swing what I hope is my best punch at Danny's jaw."
    bree.say "Take that, you pig!"
    play sound punch_hard
    pause 0.2
    hide danny
    hide lexi
    show danny punched missed
    with hpunch
    "I feel the blow connect."
    "And I wince, because it bloody well hurts me!"
    "But the most it seems to do to Danny is turn his head perhaps an inch."
    hide danny
    show lexi casual sad nophone zorder 1 at center, zoomAt (1.25, (940, 880))
    show danny joke zorder 2 at center, zoomAt (1.25, (340, 920))
    danny.say "What in the hell was that supposed to be?!?"
    danny.say "I thought I told you to hit me?"
    show danny smile
    "All I can do is stare in disbelief as Danny mocks me."
    "What on earth was that guy even teaching me during all those damn lessons?"
    "I might as well have been tapping Danny with a stick of limp celery for all the good that punch did!"
    bree.say "I..."
    bree.say "I'll make sure the next one hurts!"
    "With that, I lurch at Danny a second time."
    "My intention was to hit him again, and harder this time."
    "But he doesn't seem to be taking me seriously anymore."
    show danny at center, traveling(1.5, 0.3, (640, 1080))
    "Because instead of trying to defend himself, Danny just steps neatly aside."
    "That sends me tumbling past him, carried on by my own momentum."
    show danny joke
    danny.say "Oops!"
    danny.say "Were you trying to hit me or something?"
    danny.say "I guess you fucked that up, [hero.name]!"
    show danny upset
    "It's all that I can do to keep myself from landing on my face."
    "But Danny's not about to let the humiliation end any time soon."
    play sound punch_hard
    pause 0.2
    hide danny
    hide lexi
    show danny faceslap hit
    with hpunch
    "He launches a fist to me, catching me in just the right spot."
    "And I tumble into a heap on the ground before him."
    hide danny
    show danny angry at center, zoomAt(1.5, (640, 1080)) with vpunch
    "Danny adds insult to injury by kicking me up the ass a moment later."
    "So I roll ass over tit into the corner of the lobby."
    with vpunch
    show danny joke
    danny.say "Oh man..."
    danny.say "This is priceless, [hero.name]!"
    danny.say "Somebody better be filming this on their phone..."
    danny.say "Because I want to watch it all over again!"
    show danny smile
    "I'm watching what's happening upside down by now."
    "My head tucked somewhere in the region of my ass."
    "And that's when I see Lexi try to intervene."
    show lexi angry casual at center, zoomAt (1.25, (1040, 880)) with easeinright
    lexi.say "Leave her alone, Danny..."
    lexi.say "You made your point, yeah?"
    lexi.say "You'll get your fucking money!"
    show lexi sad
    "In the time it takes to snap your fingers, Danny's mood changes totally."
    "He rounds on Lexi, leaning over her and making her cringe backwards."
    show danny angry
    danny.say "Oh, you bet I will, Lexi..."
    danny.say "Both of you bitches better understand that by now."
    danny.say "Because if I have to remind you again..."
    danny.say "Let's just say I won't be so pleasant the next time."
    hide danny with easeoutleft
    "With that, Danny turns on his heel and walks out of the lobby."
    "Once she's sure that he's gone, Lexi hurries over to help me up."
    show lexi sadsmile at center, traveling(1.5, 0.3, (640, 1040))
    lexi.say "I get what you were trying to do, [hero.name]..."
    lexi.say "But I gotta say, that was kind of dumb!"
    show lexi sad
    bree.say "Ah..."
    bree.say "Ouch..."
    bree.say "I know that now, Lexi..."
    bree.say "I just wish I didn't have to learn it the hard way!"
    "Neither of us seems to feel much like talking after that."
    "Because we both know the reality of the situation, and it's pretty grim."
    "Now we have Danny muscling in on our operation, taking most of the money."
    "And there doesn't seem to be any hope of shaking the bastard off."
    $ lexi.flags.fought_danny_lost = True
    return


label lexi_female_event_11:
    scene bg pub with fade
    "I kind of feel sorry for everyone that's already in the Winchester when Lexi bursts through the doors."
    show lexi smile nophone at center, zoomAt(1.0, (940, 720)) with easeinright
    "Because as soon as she does so, the volume of noise in the place seems to go through the roof."
    show lexi happy at center, traveling(1.25, 1.0, (640, 900))
    lexi.say "Hey, hey, hey..."
    show lexi normal
    lexi.say "What's happening, party people?"
    lexi.say "I hope you're up for a seriously good fucking time?!?"
    show lexi smile
    "Part of me wants to turn tail and run before anyone realises that I'm supposed to be with Lexi."
    "But somehow the part of me that wants to try keeping her out of trouble is the one that wins out."
    "So I find myself walking into the pub in her wake, already offering everyone apologetic smiles."
    bree.say "Erm..."
    bree.say "Sorry about the noise!"
    bree.say "My friend's just got some really good news, that's all."
    show lexi at center, traveling(1.0, 1.0, (840, 720))
    "Lexi makes it to the bar before me, and seems to be well into the act of ordering us drinks."
    hide lexi with dissolve
    "And I'm doing the best I can to follow on her heels, already anticipating embarrassment."
    if not mike.is_gone_forever:
        "But before I can make it there, someone steps neatly into my path."
        show mike happy b at center, zoomAt(1.5, (640, 1080)) with easeinleft
        mike.say "Hey, [hero.name]..."
        mike.say "Are you two celebrating something or what?"
        mike.say "Because Lexi looks like she's on top of the world!"
        show mike smile
        "He turns to look at where Lexi's standing."
        "And my eyes follow his, almost popping out of my head."
        "Because I can see that Lexi's currently trying to climb onto the bar!"
        bree.say "Oh hell..."
        bree.say "[mike.name], would you mind?"
        bree.say "I think I'm going to need a hand here!"
        show mike normal
        "[mike.name] seems to pick up on my meaning pretty quickly."
        "He gives me a nod and then hurries with me to the bar."
        scene bg pub at center, zoomAt(1.75, (200, 1180))
        show lexi smile nophone at center, zoomAt(1.3, (640, 780))
        with fade
        pause 0.3
        show mike b upset zorder 2 at center, zoomAt(1.5, (340, 1080)) with easeinleft
        pause 0.3
        show lexi surprised at center, zoomAt(1.3, (740, 940)) with MoveTransition(0.1)
        pause 0.1
        show lexi surprised at center, zoomAt(1.3, (740, 940))
        show mike a smile
        with vpunch
        "Once there, we both grab hold of Lexi, preventing her from scaling it."
        lexi.say "Whoa..."
        lexi.say "What the..."
        bree.say "Look who I found, Lexi..."
        bree.say "[mike.name]'s here, and he wants to hear all about our news!"
        show lexi angry
        "At first Lexi seems a little pissed at being manhandled."
        "But then I see her expression change as she recognises [mike.name]."
        show lexi happy at center, traveling(1.5, 0.3, (880, 1040))
        show mike smile at center, traveling(1.5, 0.3, (400, 1080))
        if mike.name == "Mike":
            lexi.say "Hey, big Mikey!"
        else:
            lexi.say "Hey, big [mike.name]!"
        show lexi normal
        lexi.say "[hero.name] and I got our results today."
        lexi.say "And we passed - so we're gonna be big time fucking lawyers!"
        show lexi smile
        "[mike.name]'s more than used to Lexi's propensity for foul language."
        "Which means he does a pretty good job of focussing on the real issue at hand."
        show mike happy
        mike.say "Oh yeah!"
        mike.say "I remember you were taking law at college."
        mike.say "That really is great news for the both of you!"
        mike.say "Let me buy you a drink to celebrate."
        show mike smile
        "Lexi seems delighted with [mike.name]'s offer, taking the drink eagerly."
        "But I do the best I can to behave with a little more decorum."
        hide lexi
        show mike smile at center, zoomAt(1.5, (640, 1080))
        with easeoutright
        bree.say "Thank you, [mike.name]..."
        bree.say "That's very kind of you."
        show mike happy
        mike.say "Don't mention it, [hero.name]."
        mike.say "I'm sure you're going to make a brilliant lawyer."
        mike.say "But I'm amazed Lexi turned out to be so smart too."
        mike.say "You really have brought out the best in her."
        show mike smile
        "I wasn't prepared for [mike.name]'s compliments."
        "And they catch me off-guard, making me blush."
        bree.say "Oh, I think most of it was down to Lexi herself."
        bree.say "All I did was give her a little push in the right direction."
        show mike happy at startle
        "[mike.name] laughs at this, shaking his head."
        mike.say "Be modest if you want, [hero.name]..."
        mike.say "But we both know that Lexi was on a bad path before she met you."
        mike.say "And she'd still be on it now if you weren't a part of her life."
        show mike smile
        "I'm about to say something in response."
        "But then I hear the sound of clattering at the bar."
        if not sasha.is_gone_forever:
            "And I see Lexi hammering back shots with Sasha!"
        else:
            "And I see Lexi hammering back shots she has just received from the bartender"
        bree.say "Excuse me, [mike.name]..."
        bree.say "I just have to..."
        hide mike with easeoutleft
        "[mike.name] nods and steps aside, seeming to understand."
        "Which leaves me free to dart over to the bar."
    elif not sasha.is_gone_forever:
        "Lexi, it seems, has wasted no time lining up shots with Sasha, slamming them back at an incredible rate."
    else:
        "Lexi, it seems, has wasted no time organising the bartender to pour a ton of shots, slamming them back at an incredible rate."
        lexi.say "Bet you never met a lawyer who could do that before?"
    if not sasha.is_gone_forever:
        scene bg pub at center, zoomAt(1.75, (1120, 1180))
        show lexi happy nophone at center, zoomAt(1.5, (400, 1080))
        show sasha annoyed at center, zoomAt(1.5, (840, 1080))
        with fade
        lexi.say "Hah..."
        show lexi normal
        lexi.say "I beat you again, Sasha..."
        lexi.say "Bet you never met a lawyer who could do that before?"
        show lexi smile
        bree.say "Sasha..."
        bree.say "What are you doing?!?"
        show sasha annoyed at center, zoomAt(1.5, (880, 1080)) with ease
        "Sasha takes a step back from the bar."
        "And I can see that she looks pretty annoyed with my question."
        show sasha whining
        sasha.say "What am I doing?"
        sasha.say "Last time I checked, I was the one being forced to do shots!"
        sasha.say "I only came to the bar to get a bag of chips."
        sasha.say "The next thing I know, your friend here tells me we're having a competition!"
        show sasha sadsmile
        show lexi at center, zoomAt(1.5, (420, 1080)) with ease
        "Lexi's leaning on the bar as Sasha explains all of this to me."
        "And when she's done, Lexi lets out a dismissive grunt."
        show lexi bored
        lexi.say "Phnarr…"
        show lexi sadsmile
        lexi.say "I didn't hear you saying no!"
        show lexi smile
        "Sasha seems to only half hear what Lexi has to say."
        "Instead her attention seems to be focussed on me."
        show sasha shout
        sasha.say "So is it true what she said?"
        sasha.say "Like, you're both lawyers now?"
        show sasha normal
        bree.say "We have our qualifications, if that's what you mean."
        bree.say "It's not like we've set up an actual law practice yet."
        show sasha shout
        sasha.say "But you're going to, right?"
        sasha.say "Because I was thinking my band could use some legal representation."
        sasha.say "Keep us from getting shafted when we're hammering out contracts, yeah?"
        sasha.say "And you two are like, the most rock and roll lawyers I've ever met."
        hide sasha with easeoutright
    else:
        "The bartender chuckles softly before grinning at the both of us."
        "Bartender" "You two are definitely the most rock and roll lawyers I've ever met."
    show lexi smile a nophone at center, zoomAt(1.5, (640, 1080)) with ease
    "Lexi seems to like the sound of that."
    "Because she brandishes a shot in the air and knocks it straight back."
    show lexi happy
    lexi.say "Rock and roll lawyers!"
    lexi.say "I'll drink to that."
    show lexi normal
    lexi.say "No, wait..."
    lexi.say "That's totally what we should call ourselves!"
    show lexi smile
    bree.say "Well it's certainly original."
    bree.say "But let's add it to the list of possibilities for now, okay?"
    if not dwayne.is_gone_forever:
        show lexi surprised
        dwayne.say "Oh, I don't know about that, [hero.name]..."
        dwayne.say "I think it pays to stand out in business."
        dwayne.say "A name like that would really get you some attention!"
        with vpunch
        "I can't help jumping in surprise at the familiar, manly voice in my ear."
        "Unfortunately I jump backwards, and Dwayne's standing right behind me."
        scene bg pub at center, zoomAt(1.75, (640, 1180))
        show dwayne happy at center, zoomAt(1.5, (940, 1080))
        show lexi surprised nophone at center, zoomAt(1.3, (340, 940))
        with hpunch
        "Which means that I bounce off him awkwardly, almost falling flat on my face."
        bree.say "Oh..."
        bree.say "Hi, Dwayne..."
        bree.say "What are you doing here?"
        bree.say "I've never seen you in The Winchester before?"
        show dwayne therock
        "Dwayne does that thing where he smiles and raises one eyebrow."
        show dwayne shout
        dwayne.say "I heard your news, [hero.name]..."
        dwayne.say "And I wanted to come down here and congratulate you in person."
        show dwayne smile
        "I can't help frowning at this."
        bree.say "But how did you find out?"
        bree.say "The college doesn't release the results until tomorrow morning."
        bree.say "Only the students and the faculty are supposed to know right now."
        show dwayne shout
        dwayne.say "Oh, you can thank [mike.name] for that."
        show dwayne normal
        "Dwayne points to where my erstwhile housemate is standing."
        "And he gives us an obliging wave, probably ignorant of what we're talking about right now."
        show dwayne shout
        dwayne.say "He seldom hears something he doesn't post on social media."
        dwayne.say "So when I saw it, I happened to be passing on my way home."
        dwayne.say "No big deal to take a few minutes out to drop in."
        show dwayne normal
        bree.say "Well, thanks, Dwayne..."
        bree.say "But we're just graduates, that's all."
        bree.say "Your company must use some real high-powered practices!"
        show dwayne happy
        dwayne.say "We do, we do..."
        show dwayne shout
        dwayne.say "But it's more a case of using the right tools for the job, [hero.name]."
        dwayne.say "And there are some times a smaller outfit with a fresh take on things works best."
        dwayne.say "So that's why I'd like to keep in contact."
        show dwayne smile
        "Dwayne reaches into his pocket and pulls out a business card."
        "I take it, noting that the details on there are his own, not those of his company."
        bree.say "But this is your home address, Dwayne..."
        bree.say "Don't you want me to talk to someone at your office?"
        show dwayne shout
        dwayne.say "No, [hero.name]..."
        dwayne.say "I get the feeling you'd be more use to me on a personal basis."
        show dwayne smile
        show lexi flirt at center, zoomAt(1.3, (540, 940)) with ease
        lexi.say "Geez..."
        lexi.say "I know how I could use you on a personal basis!"
        show dwayne therock
        "Dwayne's eyebrows rise as Lexi leans around his side."
        "Then he glances behind his back, staring down at his own ass."
        show dwayne happy
        dwayne.say "I take it this is Lexi?"
        dwayne.say "Does she always introduce herself by grabbing people's asses?"
        show dwayne smile
        bree.say "LEXI!"
        bree.say "Behave yourself!"
        show lexi happy
        lexi.say "How am I supposed to do that around a hunk of manhood like this?!?"
        show lexi smile
        "Lexi waves her hands up and down, indicating to Dwayne."
        "But rather than being offended, he lets out a booming laugh."
        show dwayne happy
        show dwayne at center, zoomAt (1.0, (940, 1080)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (940, 1080)), startle(0.14,-20)
        pause 0.2
        show dwayne at center, zoomAt (1.0, (940, 1080)), startle(0.14,-20)
        dwayne.say "Ha, ha!"
        dwayne.say "I predict working with you girls is going to a LOT of fun!"
        show dwayne smile
        "With that, Dwayne turns on his heel and walks over to [mike.name]."
        hide dwayne
        show lexi flirt at center, zoomAt(1.3, (640, 940)) with ease
        with easeoutright
        "But Lexi watches him go, all but salivating as she does so."
        show lexi normal blush
        lexi.say "Oh man..."
        lexi.say "I wonder if he'd pay his bills in sexual favours?"
        lexi.say "I wouldn't mind getting a big, hard bonus from him!"
        show lexi smile
        bree.say "Oh, Lexi..."
        bree.say "You haven't changed that much, have you?"
        show lexi blank -blush
        "Lexi shrugs."
        show lexi normal
        lexi.say "Nah, not really."
        show lexi happy
        lexi.say "But I can charge much more by the hour as a lawyer than I could as a hooker!"
        show lexi smile
    "I shake my head, wondering what I'm getting myself in for."
    "But it's too late to go getting cold feet now."
    "Lexi and I put so much work into getting our degrees."
    "Now we have to set about making them pay us back for it."
    $ lexi.flags.lawyer = True
    if lexi.love.max < 200:
        $ lexi.love.max = 200
    return


label lexi_female_event_11c:
    if lexi.love.max < 200:
        $ lexi.love.max = 200
    show lexi casual smile at center, zoomAt(1.0, (640, 720))
    "It seems like Lexi and I have been spending almost every waking moment together recently."
    "But guess that's just the natural consequence of me helping her out of the mess she was in."
    "And then there's the fact that I chose to change my major and study law with her too."
    show lexi happy
    "All this time I feel like we've been getting closer and closer in a totally natural way."
    show lexi smile
    "Hell, when we discuss what we're going to do with our newly-won qualifications, it always together."
    "Like the both of us have simply assumed that we're going to be going into practicing law as a partnership."
    "It's also meant that our personal relationship's advanced leaps and bounds too."
    "Before we were just starting to think about getting serious."
    "But all of the stress and hard work's thrown us together more intensely."
    show lexi wink
    "So much so that now I feel as though Lexi and I have been a couple forever."
    show lexi smile
    "As if all we've been through has served to strengthen our bonds to a crazy degree."
    "It's almost like we're already living the life of a married couple."
    show lexi at center, traveling(1.25, 0.3, (640, 880))
    "Which is why it comes as a surprise when Lexi asks me a question out of the blue."
    show lexi normal
    lexi.say "[hero.name]..."
    lexi.say "I wanna ask you something, yeah?"
    show lexi smile
    bree.say "Well what are you waiting for, Lexi?"
    bree.say "I'm right here - so ask away!"
    "Lexi nods, but I can see there's something making her stumble."
    "And that's so unlike her I can just tell there's more to this than meets the eye."
    show lexi sadsmile
    lexi.say "Okay, [hero.name]..."
    lexi.say "The thing is..."
    lexi.say "I wondered if you..."
    show lexi normal
    lexi.say "If you like to, maybe...marry me?"
    show lexi smile
    "I was expecting Lexi to come out with something serious."
    "But the question comes straight out of nowhere."
    "And it catches me totally off-guard."
    bree.say "I'm sorry, Lexi..."
    bree.say "I must have had a funny turn for a moment back there."
    bree.say "Because I could have sworn you asked me to marry you!"
    show lexi blank blush
    "The expression on Lexi's face becomes more than a little awkward."
    "And she even seems to be getting embarrassed too."
    "Which lets me know that I've totally screwed-up."
    "Because Lexi almost never gets embarrassed about anything."
    show lexi sadsmile
    lexi.say "Don't be mean to me, [hero.name]!"
    lexi.say "This isn't some kind of joke..."
    lexi.say "I'm putting my heart on the line here!"
    show lexi blank
    "Okay, so now I feel like the worst human being on the face of the planet!"
    "And I instantly start to backpedal, trying to make it up to Lexi."
    bree.say "Oh my god..."
    bree.say "I am SO sorry, Lexi!"
    bree.say "That was totally out of order."
    bree.say "I...I just wasn't prepared for the question, that's all."
    show lexi surprised
    lexi.say "Huh..."
    lexi.say "I thought that was how you were supposed to do it?"
    show lexi normal
    lexi.say "Pop the question when they're not expecting it, yeah?"
    lexi.say "That's how people do it in the movies and on TV!"
    show lexi smile
    "Lexi crosses her arms over her chest."
    "And I can see that she's already beginning to pout."
    show lexi bored
    lexi.say "So?"
    show lexi blank
    bree.say "So what?"
    show lexi sadsmile
    lexi.say "So do you want to marry me or not?!?"
    lexi.say "You already made me feel like a fucking chump."
    lexi.say "The least you could do is give me an answer!"
    show lexi blank
    menu:
        "Agree to marry Lexi":
            "I don't hesitate to come out with my answer."
            "And I know that I'm not doing it to console Lexi either."
            "Because I just come straight out with it."
            "Not taking the time that I'd have needed to think it over in any depth."
            bree.say "Of course I want to marry you, Lexi..."
            bree.say "I'm one hundred percent in love with you."
            bree.say "So yeah, let's do it!"
            show lexi smile
            "My answer seems to be enough to totally change Lexi's mood."
            show lexi happy
            "Suddenly she's all smiles and manic laughter."
            show lexi at center, traveling(1.75, 0.2, (640, 1200))
            "Lexi throws her arms around me, squeezing me until I wheeze."
            show lexi normal with hpunch
            lexi.say "Yes, yes, yes..."
            lexi.say "I get to marry my hot, lawyer girlfriend!"
            lexi.say "This is the perfect, fairy-tale ending!"
            show lexi smile
            "I'm not sure I'd agree with that last sentiment."
            "But I nod and smile all the same."
            "Because I'm totally excited and over the moon."
            "Sure, all of this is happening crazily fast."
            "Yet isn't that how life always seems to be with Lexi around?"
            "She never really thinks things through, just jumps in feet first."
            "And so far that's put me in a really wonderful place."
            "So I'm going to bet the house on this doing the same thing too."
            $ lexi.love += 5
            $ lexi.set_fiance()
        "Do not agree to marry Lexi":
            "Urgh..."
            "Looks like it sucks to be me today!"
            "First I insult Lexi when she's bearing her soul to me."
            "And now I have to explain why I can't say yes to her question too."
            bree.say "I'd love to marry you, Lexi..."
            show lexi surprised
            lexi.say "You would?!?"
            show lexi sad
            bree.say "But..."
            "Lexi's face falls as she hears me add the word."
            show lexi sadsmile
            lexi.say "Oh man!"
            lexi.say "Why's there always got to be a but?!?"
            show lexi sad
            bree.say "Because I think now would be totally the wrong time."
            "Lexi shakes her head."
            show lexi blank
            "Clearly puzzled by my explanation."
            show lexi surprised
            lexi.say "Why so, [hero.name]?"
            lexi.say "One, I'm off the game for good."
            lexi.say "Two, we totally got rid of Danny."
            lexi.say "Three, we both got our law qualifications."
            lexi.say "Everything's going our way!"
            show lexi blank
            "Now it's my turn to shake my head."
            bree.say "All of that's true, Lexi..."
            bree.say "But these have been crazy times."
            bree.say "And none of the dust has had time to settle."
            bree.say "I think we need to see where we are when it does, that's all."
            show lexi annoyed
            "I can see that Lexi's far from convinced."
            "But she doesn't seem ready to argue with me."
            show lexi angry
            lexi.say "Aww, [hero.name]!"
            lexi.say "Why'd you always have to do that?"
            show lexi sadsmile
            lexi.say "Be the sensible one and make me agree with you?!?"
            show lexi smile
            bree.say "Lexi, we just qualified as lawyers - that's what we do now!"
            "Lexi mutters under her breath for a while."
            "But at least now she seems to be willing to let idea go."
            $ lexi.love -= 5
    scene bg black with dissolve
    return


label lexi_female_ending:
    $ game.hour = 16
    $ game.room = "church"

    if lexi.flags.fought_danny_lost:
        scene bg church wedding at blur(5) with fade
        "I'm pretty sure that this is the day I've been waiting for."
        "I keep pinching myself to make sure that I'm awake and not dreaming."
        "Because when you're taking as much shit as I am, that can actually happen!"
        "And it takes a pretty hard pinch to snap me back to reality this time."
        show lexi a wedding blank nophone at center, zoomAt(1.25, (940, 880)), blur(5) with dissolve
        lexi.say "[hero.name]?"
        lexi.say "Hey, [hero.name]..."
        lexi.say "Are you even hearing what I'm saying to you right now?!?"
        show lexi a sadsmile
        show danny date scared at center, zoomAt(1.25, (940, 880)), (blur) with dissolve
        danny.say "Ah shit..."
        danny.say "How much of that stuff did you let her take?"
        danny.say "Didn't I tell you it was extra strong?"
        show danny upset
        "I shake my head, trying to clear the fog that's dulling my senses."
        "I can see that there are two people standing in front of me."
        "And their voices are familiar to me, like I should know them."
        bree.say "Huh?"
        bree.say "Where am I?"
        lexi.say "Oh thank god!"
        lexi.say "[hero.name], you have to snap out of it."
        lexi.say "We're supposed to be getting married!"
        scene bg church wedding
        show danny date at center, zoomAt(1.25, (340, 880))
        show lexi a wedding sad nophone at center, zoomAt(1.25, (940, 880))
        with dissolve
        "That's what finally does it, what snaps me back to reality."
        "Lexi and I are supposed to be getting married today!"
        "Suddenly reality rushes back in around me."
        "And just like that, I'm thrust back into the moment."
        bree.say "Oh yeah..."
        bree.say "Ha, ha..."
        bree.say "We're getting married, aren't we?"
        "Lexi's still staring at me, a worried look on her face."
        show danny annoyed
        "But Danny's looking more irritated and annoyed than concerned."
        show danny shout
        danny.say "So are we doing this thing or what?"
        danny.say "We got a chapel full of people waiting on us!"
        show danny normal
        "He gestures behind me, and I turn to see what he's pointing at."
        "It looks like we are in a chapel, and there are guests in the seats."
        "But the place is nowhere near full, most of the rows only half full at the most."
        "Plus the guests all look like Danny's friends and associates to me."
        "Almost every one of them is shifty and dressed like a low-life."
        if bree.is_visibly_pregnant:
            "I look down at myself, seeing that I'm in a wedding dress."
            "But then I also notice that I seem to be pregnant too!"
            bree.say "Aargh..."
            bree.say "When did that happen?!?"
            show lexi a sadsmile
            lexi.say "We already went through this, [hero.name]..."
            lexi.say "There's been so many guys that we can't find the father!"
            show lexi sad
        else:
            "I look down at myself, seeing that I'm in a wedding dress."
        bree.say "Wait a minute..."
        bree.say "Where's the priest?"
        bree.say "We can't get married if there's no priest."
        show danny joke
        "Danny lets out a filthy chuckle and shakes his head."
        "Then he pulls out a white collar, wrapping it around his neck."
        show danny sneaky
        danny.say "We don't need no stinking priest, [hero.name]..."
        danny.say "I went online and got myself ordained."
        danny.say "Just answered a couple of questions and made a payment."
        danny.say "And bam - I'm officially a minister!"
        show danny smile
        "Somehow, even in my dazed state of mind, that doesn't sound right."
        "I open my mouth, meaning to say something about that to Danny."
        show lexi annoyed
        "But then I see Lexi glancing sideways at me, shaking her head."
        "And I know that's the universal signal telling me to drop it."
        "So instead I nod and smile."
        bree.say "That sounds great, Danny..."
        bree.say "So are we going to get started or what?"
        show danny date at center, traveling(1.25, 0.3, (320, 880))
        show lexi a wedding smile nophone at center, traveling(1.5, 0.3, (640, 1040))
        "Danny nods and then begins to noisily clear his throat."
        show danny shout
        danny.say "Ahem..."
        danny.say "Ladies and germs..."
        danny.say "I got your asses here today to watch me marry these two hos."
        danny.say "Because they want to be an item or something like that."
        danny.say "So I gotta say a load of shit to make it official."
        show danny smile
        "Okay, okay - I know this doesn't exactly sound romantic."
        "But suspend your disapproval for a minute, okay?"
        "Aren't people always going on about appearances not really mattering?"
        "Saying that it's who you're with and how you feel about them that's important?"
        "Lexi and I are in love, and we want to get married."
        "So that's the important thing, right?"
        show danny shout
        danny.say "Alright..."
        danny.say "Do you, Lexi..."
        danny.say "Take [hero.name]..."
        danny.say "To be your lawful, wedded whore?"
        show danny smile
        lexi.say "I do!"
        "Now Danny turns his attention to me."
        show danny shout
        danny.say "And what about you, [hero.name]?"
        danny.say "Do you take Lexi..."
        danny.say "Blah, blah, blah..."
        show danny smile
        "Part of me bristles at the way Danny's tossing off the vows."
        "Like he thinks so little of us both that he just can't be bothered."
        "But I know better than to speak up and challenge him on the matter."
        "Especially when we're surrounded by his cronies too."
        "So I just do the best I can to ignore it and press on."
        bree.say "I do."
        "Danny nods again."
        show danny shout
        danny.say "Great..."
        danny.say "Now it says here that anyone that objects should speak up."
        danny.say "So if you think these two bitches shouldn't be married..."
        danny.say "Spit it out, or shut your yap."
        danny.say "And I should point out that if you do speak up, I'll fuck you up too!"
        show danny smile
        "There are a few wry chuckles from the assembled rogues gallery."
        "As well as a good number of surly mutterings too."
        "I guess the latter come from people that have felt Danny's wrath in the past."
        "But none of them actually choose to say anything out loud or to his face."
        show danny shout
        danny.say "Yeah, you bet nobody objects!"
        danny.say "So that's the matter settled."
        danny.say "[hero.name]..."
        danny.say "Lexi..."
        danny.say "You're married!"
        show danny smile
        "Instinctively, Lexi and I begin hugging each other."
        hide lexi
        show lexi kiss wedding
        with fade
        "And just as we're sharing a particularly sloppy kiss, I hear Danny speaking again."
        show danny shout
        danny.say "Ha..."
        danny.say "Look at the horny bitches!"
        danny.say "Okay, guys - you may fuck the brides!"
        show danny smile
        "Lexi and I only have a couple of seconds to let that sink in."
        hide lexi
        show lexi a wedding surprised nophone at center, zoomAt(1.5, (640, 1040))
        with fade
        "Because mere moments later, the guests are up and out of their seats."
        with hpunch
        "Then I feel hands all over my body, squeezing and pinching."
        "But most of all, I feel them pulling me away from Lexi."
        show lexi b wedding nophone at center, traveling(1.25, 0.5, (940, 880))
        "There's nothing I can do to stop them, and I wouldn't even if I could."
        "Because I know all too well the punishment for disobedience."
        "So I do what I always do, I just let whatever happens happen."
        "And all the time I keep on telling myself that everything will be okay."
    else:
        scene bg church wedding with fade
        "This is it, the big day is finally here!"
        "After all that we've been through together, Lexi and I are finally tying the knot."
        "The chapel is all decked out for the occasion."
        "And the place is packed to the rafters with guests too."
        "But Lexi and I aren't in there just yet, and the priest is alone at the altar."
        "That's because we made the decision to enter the chapel and walk down the aisle together."
        "We talked about one of us standing at the altar and waiting for the other to walk down it."
        "But neither of us felt that it'd be the right thing to do."
        "Because we got where we are today by working together, by being equal partners."
        "So doing this thing together seemed to be the only way that was appropriate."
        "And sure, it does mean that we've both technically seen each other before the wedding."
        "But we're already far from the traditional image of a married couple."
        "So I ask you, what in the hell does it matter?"
        lexi.say "Oh, man..."
        lexi.say "Are we actually doing this?!?"
        "At the sound of Lexi's voice, I turn to look in her direction."
        show lexi a wedding blank nophone at center, zoomAt(1.25, (940, 880)) with dissolve
        "And I can instantly see the familiar sense of disbelief written all over her face."
        "I say familiar because I can feel it inside of me too right now."
        "I guess this is what they call having butterflies in your stomach!"
        if bree.is_visibly_pregnant:
            "The mere thought of my stomach makes me look downwards."
            "And that's when I'm reminded of the fact that I'm visibly pregnant."
            "Luckily for me, my dress is made to flatter the bump."
            "But I'm still more than a little self-conscious."
        else:
            "I put a hand on my belly, hoping that the warmth will help."
            "And also relieved that it's only butterflies that I have to worry about."
        bree.say "I think so, Lexi..."
        bree.say "Unless you're getting cold feet?"
        show lexi smile at center, traveling(1.5, 0.5, (640, 1040))
        "By way of an answer, Lexi reaches out and takes hold of my hand."
        "She squeezes it tightly, and then I do the same in return."
        "And somehow that seems to answer all of the questions running around inside of my head."
        "Because almost as soon as I turn my head away from Lexi, everything begins to move."
        "I hear the music that we chose to walk down the aisle to begin playing."
        "Then the doors of the chapel open, and I hear the muffled voices of the guests."
        show lexi b with fade
        "Lexi keeps a tight hold on my hand as we take one step forwards, then another."
        show wedding lexi with fade
        "And before I know it, we're all the way down the aisle."
        "Then I see the priest standing in front of the altar."
        show wedding lexi priest with dissolve
        "Priest" "Hello there..."
        "Priest" "Are you ready to begin?"
        bree.say "I guess that we should."
        lexi.say "Well I certainly haven't got anywhere else to be right now!"
        "The priest nods and visibly starts getting himself into character."
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To join [hero.name] and Lexi, in the bonds of holy matrimony."
        "I feel Lexi jab me in the ribs as the priest speaks."
        "Then she leans in close to chuckle into my ear."
        lexi.say "Ha..."
        lexi.say "Bonds!"
        lexi.say "The kinky old goat!"
        bree.say "Oh, Lexi..."
        bree.say "Behave yourself!"
        "Luckily for us, the priest doesn't seem to hear what Lexi's whispering to me."
        "Or if he does, then he has the character to simply ignore it and press on."
        "As he's soon into the meat of the ceremony."
        "You know what I mean by that?"
        "All of the stuff that you could recite in your sleep."
        "Things only get interesting again when he comes to the vows."
        "Priest" "Do you, Lexi..."
        "Priest" "Take [hero.name]..."
        "Priest" "To be your lawful, wedded partner?"
        lexi.say "Oh, I do!"
        "Priest" "And do you, [hero.name]..."
        "Priest" "Take Lexi..."
        "Priest" "To be your lawful, wedded partner?"
        bree.say "I do."
        "The priest nods, and then turns to address the guests."
        "Priest" "I call upon those here present..."
        "Priest" "That if you know of any lawful reason..."
        "Priest" "Why these two people may not be joined in the bonds of holy matrimony..."
        "Priest" "Speak now, or forever hold your peace!"
        "There's the usual ripple of laughter from the guests as he asks the question."
        "But I'm feeling more than a little twitchy right now, and that for real."
        "Plus I can feel Lexi squeezing my hand more tightly than ever before."
        "And that's because we're both painfully aware of Lexi's chequered past."
        "The fear of some creep like Danny crashing the wedding is very real."
        "We even discussed what we should do if that actually happened."
        "But the best we could come up with was the idea to kick his ass!"
        "So it comes as a great relief to heart the priest starting to speak again."
        "Priest" "Very good..."
        "Priest" "Then by the power vested in me..."
        "Priest" "It gives me great pleasure to pronounce you married."
        "Priest" "You may kiss your partner, if you wish."
        show wedding lexi -priest with dissolve
        "I hardly hear what the priest is saying towards the end."
        "That's because I'm feeling totally overwhelmed by what all of this means."
        "And then I have the additional distraction of Lexi getting in my face."
        lexi.say "You heard the man, [hero.name]..."
        lexi.say "So pucker up already!"
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show lexi kiss wedding
        with fade
        "I barely have time to take in Lexi's words before she's kissing me."
        "But the surprise I'm feeling doesn't keep me still for too long."
        "And soon enough I'm returning the kiss with an equal measure of passion."
        "We did it, we actually got married!"
        "And now I get to spend the rest of my life with Lexi."
        "Maybe soon my head will stop spinning and I'll come back down to earth."
        "Or maybe this is what it feels like to be married."
        "And I'm going to have to get used to it being my new normal!"

    if lexi.flags.lawyer:
        scene bg black
        show lawyers ending bree lexi
        with fade
        lexi.say "So wait..."
        lexi.say "This is where I get to have my say?"
        lexi.say "It's me talking about, [hero.name] and not the other way around?"
        lexi.say "Oh man, this is going to be great - because I have a hell of a lot to say!"
        lexi.say "What?"
        lexi.say "I have to just keep it about my life with [hero.name]?"
        lexi.say "Okay, okay..."
        lexi.say "I get the message."
        lexi.say "So yeah, I guess that my life was pretty different before I met [hero.name]."
        lexi.say "I was kind of the poster-girl for being born on the wrong side of the tracks."
        lexi.say "I mean, I never really tried to fall from grace, you know?"
        lexi.say "I just kind of sauntered vaguely downwards."
        lexi.say "Trust me, when you grow up on a rough trailer-park, it's hard to notice that stuff."
        lexi.say "Everyone around you is either on something bad or into something bad."
        lexi.say "More often than not both at the same time!"
        lexi.say "I never really knew who my dad was, and my mom kind of saw me as a nuisance."
        lexi.say "Plus she was always with the worst possible kind of guys too, real scumbags."
        lexi.say "So I got out of there the first chance I had and struck out on my own."
        lexi.say "I feel in with guys like Danny, and they taught me the easiest ways to make money."
        lexi.say "And yeah, I get the irony of all that."
        lexi.say "Because I just became a carbon copy of my mom!"
        lexi.say "But there was never anything else in my life, and I thought I was happy."
        lexi.say "Or at least I told myself that I was until [hero.name] came along."
        lexi.say "At first I just saw her as another potential client."
        lexi.say "Or worse, someone that I could easily take advantage of."
        lexi.say "But [hero.name] seemed to see something really different in me."
        lexi.say "Like, most people just thought of me as a cheap whore."
        lexi.say "You know, total scum!"
        lexi.say "But not [hero.name], she actually treated me like a real person."
        lexi.say "She spoke to me like she was interested in what I thought and had to say."
        lexi.say "Of course at first I was sure the whole thing had to be a grift of some kind."
        lexi.say "Like she was working a long-con and trying to make me think she was nice."
        lexi.say "But every time I thought she was going to try to spring the trap, she didn't."
        lexi.say "Instead she just kept right on being kind and supportive, acting like a friend."
        lexi.say "Every time I went back to thinking she was putting in more effort."
        lexi.say "That she was trying to make the con even more convincing."
        lexi.say "Until one day I finally started to wonder - what if she was for real?"
        lexi.say "Then I sort of decided to go along with that, unless she proved me wrong."
        lexi.say "And you know what?"
        lexi.say "She still hasn't done that yet."
        lexi.say "[hero.name]'s been the best thing that ever happened to me."
        lexi.say "She was there when I decided to make the biggest change in my life of all."
        lexi.say "Together we stood up to Danny and kicked him to the curb for good."
        lexi.say "Then we went back to school together too, and we got our qualifications."
        lexi.say "Now we're big-time lawyers, kicking legal ass in the big city!"
        lexi.say "We have a big, swanky office in town."
        lexi.say "Plus our house is totally massive and one hundred percent not a trailer!"
        lexi.say "Seriously, you should see us in our suits and heels."
        lexi.say "We're battling in the courtroom every chance we get."
        lexi.say "It's like one of those TV series with a cool theme tune and everything!"
        if bree.is_visibly_pregnant:
            lexi.say "Sure, we have to juggle things with caring for little Johnny."
            lexi.say "But we can afford the best day-care that money can buy for him."
            lexi.say "And he's going to grow up with two totally unstoppable mommies."
            lexi.say "Maybe he'll even become a lawyer too, start up a legal dynasty!"
        else:
            lexi.say "Right now it feels like we're working every hour we're awake."
            lexi.say "But I think that we'll want to slow down some time in the future."
            lexi.say "You know, actually enjoy some of the money we're making?"
            lexi.say "And then we can start thinking about a family."
            lexi.say "Because we'd make great parents for any kid we tried to adopt."
        lexi.say "So yeah, I have more than I could ever have dreamed I'd end up with."
        lexi.say "But the only thing that I couldn't live without is [hero.name]."
        lexi.say "Hell, I'd even be happy if it were just the two of us back in the trailer-park."
        lexi.say "Though don't tell her I said that, as she might think she can slack off!"
        lexi.say "And this girl's become well and truly used to the luxury in which she's been living!"

    elif lexi.flags.fought_danny_won:
        scene bg black
        show escorts ending bree lexi
        with fade
        lexi.say "So wait..."
        lexi.say "This is where I get to have my say?"
        lexi.say "It's me talking about, [hero.name] and not the other way around?"
        lexi.say "Oh man, this is going to be great - because I have a hell of a lot to say!"
        lexi.say "What?"
        lexi.say "I have to just keep it about my life with [hero.name]?"
        lexi.say "Okay, okay..."
        lexi.say "I get the message."
        lexi.say "So yeah, I guess that my life was pretty different before I met [hero.name]."
        lexi.say "I was kind of the poster-girl for being born on the wrong side of the tracks."
        lexi.say "I mean, I never really tried to fall from grace, you know?"
        lexi.say "I just kind of sauntered vaguely downwards."
        lexi.say "Trust me, when you grow up on a rough trailer-park, it's hard to notice that stuff."
        lexi.say "Everyone around you is either on something bad or into something bad."
        lexi.say "More often than not both at the same time!"
        lexi.say "I never really knew who my dad was, and my mom kind of saw me as a nuisance."
        lexi.say "Plus she was always with the worst possible kind of guys too, real scumbags."
        lexi.say "So I got out of there the first chance I had and struck out on my own."
        lexi.say "I feel in with guys like Danny, and they taught me the easiest ways to make money."
        lexi.say "And yeah, I get the irony of all that."
        lexi.say "Because I just became a carbon copy of my mom!"
        lexi.say "But there was never anything else in my life, and I thought I was happy."
        lexi.say "Or at least I told myself that I was until [hero.name] came along."
        lexi.say "At first I just saw her as another potential client."
        lexi.say "Or worse, someone that I could easily take advantage of."
        lexi.say "But [hero.name] seemed to see something really different in me."
        lexi.say "Like, most people just thought of me as a cheap whore."
        lexi.say "You know, total scum!"
        lexi.say "But not [hero.name], she actually treated me like a real person."
        lexi.say "She spoke to me like she was interested in what I thought and had to say."
        lexi.say "Of course at first I was sure the whole thing had to be a grift of some kind."
        lexi.say "Like she was working a long-con and trying to make me think she was nice."
        lexi.say "But every time I thought she was going to try to spring the trap, she didn't."
        lexi.say "Instead she just kept right on being kind and supportive, acting like a friend."
        lexi.say "Every time I went back to thinking she was putting in more effort."
        lexi.say "That she was trying to make the con even more convincing."
        lexi.say "Until one day I finally started to wonder - what if she was for real?"
        lexi.say "Then I sort of decided to go along with that, unless she proved me wrong."
        lexi.say "And you know what?"
        lexi.say "She still hasn't done that yet."
        lexi.say "Plus she taught me a really valuable lesson."
        lexi.say "[hero.name] taught me that I might be a whore, but I'm not a cheap one!"
        lexi.say "When I was most in need of help, she stepped in and saved me."
        lexi.say "Together we set up a racket making some real money turning tricks."
        lexi.say "More money than I'd ever thought I could make in a lifetime."
        lexi.say "And when Danny came sniffing around, trying to get some of it for himself..."
        lexi.say "Well, [hero.name] kicked him to the curb."
        lexi.say "And I really do mean that!"
        lexi.say "She beat his ass up and tossed him out the door."
        lexi.say "Since then, we've never looked back, not once."
        lexi.say "Nowadays they have to call us escorts, and all the fancy folks are nice to us too."
        lexi.say "Because we command a high price for our services, and we're always listening as well."
        lexi.say "So we know all about the dirty little secrets that the rich and influential are hiding."
        if bree.is_visibly_pregnant:
            lexi.say "Sure, our busy schedules mean we can't always be there for little Johnny."
            lexi.say "But we can afford the best day-care that money can buy for him."
            lexi.say "And we take time off to spend with him whenever we possibly can."
            lexi.say "And he's going to grow up with two totally cool mommies."
            lexi.say "But we're both kind of hoping that he grows up to be a lawyer or a doctor!"
        else:
            lexi.say "Right now it feels like we're working every hour we're awake."
            lexi.say "But I think that we'll want to slow down some time in the future."
            lexi.say "You know, actually enjoy some of the money we're making?"
            lexi.say "And then we can start thinking about a family."
            lexi.say "Because we might not look like ideal parents on paper."
            lexi.say "But we do have the money to grease all the right palms."
        lexi.say "So yeah, I have more than I could ever have dreamed I'd end up with."
        lexi.say "But the only thing that I couldn't live without is [hero.name]."
        lexi.say "Hell, I'd even be happy if it were just the two of us back in the trailer-park."
        lexi.say "Though don't tell her I said that, as she might think she can slack off!"
        lexi.say "And this girl's become well and truly used to the luxury in which she's been living!"

    elif lexi.flags.fought_danny_lost:
        scene bg black
        show whores ending
        with fade
        lexi.say "So wait..."
        lexi.say "This is where I get to have my say?"
        lexi.say "It's me talking about, [hero.name] and not the other way around?"
        lexi.say "Oh man, this is going to be great - because I have a hell of a lot to say!"
        lexi.say "What?"
        lexi.say "I have to just keep it about my life with [hero.name]?"
        lexi.say "Okay, okay..."
        lexi.say "I get the message."
        lexi.say "So yeah, I guess that my life was pretty different before I met [hero.name]."
        lexi.say "I was kind of the poster-girl for being born on the wrong side of the tracks."
        lexi.say "I mean, I never really tried to fall from grace, you know?"
        lexi.say "I just kind of sauntered vaguely downwards."
        lexi.say "Trust me, when you grow up on a rough trailer-park, it's hard to notice that stuff."
        lexi.say "Everyone around you is either on something bad or into something bad."
        lexi.say "More often than not both at the same time!"
        lexi.say "I never really knew who my dad was, and my mom kind of saw me as a nuisance."
        lexi.say "Plus she was always with the worst possible kind of guys too, real scumbags."
        lexi.say "So I got out of there the first chance I had and struck out on my own."
        lexi.say "I feel in with guys like Danny, and they taught me the easiest ways to make money."
        lexi.say "And yeah, I get the irony of all that."
        lexi.say "Because I just became a carbon copy of my mom!"
        lexi.say "But there was never anything else in my life, and I thought I was happy."
        lexi.say "Or at least I told myself that I was until [hero.name] came along."
        lexi.say "At first I just saw her as another potential client."
        lexi.say "Or worse, someone that I could easily take advantage of."
        lexi.say "But [hero.name] seemed to see something really different in me."
        lexi.say "Like, most people just thought of me as a cheap whore."
        lexi.say "You know, total scum!"
        lexi.say "But not [hero.name], she actually treated me like a real person."
        lexi.say "She spoke to me like she was interested in what I thought and had to say."
        lexi.say "Of course at first I was sure the whole thing had to be a grift of some kind."
        lexi.say "Like she was working a long-con and trying to make me think she was nice."
        lexi.say "But every time I thought she was going to try to spring the trap, she didn't."
        lexi.say "Instead she just kept right on being kind and supportive, acting like a friend."
        lexi.say "Every time I went back to thinking she was putting in more effort."
        lexi.say "That she was trying to make the con even more convincing."
        lexi.say "Until one day I finally started to wonder - what if she was for real?"
        lexi.say "Then I sort of decided to go along with that, unless she proved me wrong."
        lexi.say "And you know what?"
        lexi.say "She still hasn't done that yet."
        lexi.say "Hell, she even helped me out when I owed Danny that huge pile of money!"
        lexi.say "And for a while there, it actually looked like we were gonna get away from him too."
        lexi.say "But I guess I should have known that was never going to work out the way we wanted."
        lexi.say "Danny's too much of a controlling asshole to ever let me escape his clutches."
        lexi.say "The real problem though was that he managed to catch [hero.name] at the same time too."
        lexi.say "We thought that we were being pretty smart, cutting Danny out of the money we were making."
        lexi.say "But then he turned up, and things got physical."
        lexi.say "After that, [hero.name] and I just has to accept that he was the one in charge."
        lexi.say "That the both of us were working for him and we had no choice in the matter."
        lexi.say "Yeah, I know that sounds totally bleak."
        lexi.say "But for me it was more like going back to the life I already knew."
        lexi.say "The real difference was that this time I had [hero.name] there to keep me company."
        lexi.say "I mean sure, Danny was a lot tougher on us from that point on."
        lexi.say "I guess he felt like he didn't have any choice to keep us in line."
        lexi.say "And the drugs do kinda help to dull the pain, you know?"
        lexi.say "Just so long as he keeps them coming."
        lexi.say "But it's not all bad, and Danny's not a complete monster."
        lexi.say "I mean, he let me and [hero.name] get married, didn't he?"
        lexi.say "Hell, he even organised everything and performed the ceremony himself."







        if not bree.is_visibly_pregnant:
            lexi.say "Sometimes I actually find myself wishing one of us would have an accident."
            lexi.say "That we'd forget to take the Pill or screw-up with the condoms along the way."
            lexi.say "Then we could raise the kid together, be like a proper little family."
            lexi.say "And I don't even think it'd matter if we knew who the father was or not."
        lexi.say "So there you have it."
        lexi.say "This isn't the life that I'd have chosen for myself."
        lexi.say "And I'm pretty sure it's a thousand miles from the one [hero.name] wanted."
        lexi.say "But it could be much worse, you know?"
        lexi.say "We could have a pimp that never let us see a cent of our money."
        lexi.say "Or we could be out on the streets, living in a fucking cardboard box!"
        lexi.say "And like I said, it's that much better because I got [hero.name] to keep me company."
        lexi.say "So long as we're together, I know that I'll be able to keep on going."
    else:

        scene bg black
        show nice ending bree lexi
        with fade
        lexi.say "So wait..."
        lexi.say "This is where I get to have my say?"
        lexi.say "It's me talking about, [hero.name] and not the other way around?"
        lexi.say "Oh man, this is going to be great - because I have a hell of a lot to say!"
        lexi.say "What?"
        lexi.say "I have to just keep it about my life with [hero.name]?"
        lexi.say "Okay, okay..."
        lexi.say "I get the message."
        lexi.say "So yeah, I guess that my life was pretty different before I met [hero.name]."
        lexi.say "I was kind of the poster-girl for being born on the wrong side of the tracks."
        lexi.say "I mean, I never really tried to fall from grace, you know?"
        lexi.say "I just kind of sauntered vaguely downwards."
        lexi.say "Trust me, when you grow up on a rough trailer-park, it's hard to notice that stuff."
        lexi.say "Everyone around you is either on something bad or into something bad."
        lexi.say "More often than not both at the same time!"
        lexi.say "I never really knew who my dad was, and my mom kind of saw me as a nuisance."
        lexi.say "Plus she was always with the worst possible kind of guys too, real scumbags."
        lexi.say "So I got out of there the first chance I had and struck out on my own."
        lexi.say "I feel in with guys like Danny, and they taught me the easiest ways to make money."
        lexi.say "And yeah, I get the irony of all that."
        lexi.say "Because I just became a carbon copy of my mom!"
        lexi.say "But there was never anything else in my life, and I thought I was happy."
        lexi.say "Or at least I told myself that I was until [hero.name] came along."
        lexi.say "At first I just saw her as another potential client."
        lexi.say "Or worse, someone that I could easily take advantage of."
        lexi.say "But [hero.name] seemed to see something really different in me."
        lexi.say "Like, most people just thought of me as a cheap whore."
        lexi.say "You know, total scum!"
        lexi.say "But not [hero.name], she actually treated me like a real person."
        lexi.say "She spoke to me like she was interested in what I thought and had to say."
        lexi.say "Of course at first I was sure the whole thing had to be a grift of some kind."
        lexi.say "Like she was working a long-con and trying to make me think she was nice."
        lexi.say "But every time I thought she was going to try to spring the trap, she didn't."
        lexi.say "Instead she just kept right on being kind and supportive, acting like a friend."
        lexi.say "Every time I went back to thinking she was putting in more effort."
        lexi.say "That she was trying to make the con even more convincing."
        lexi.say "Until one day I finally started to wonder - what if she was for real?"
        lexi.say "Then I sort of decided to go along with that, unless she proved me wrong."
        lexi.say "And you know what?"
        lexi.say "She still hasn't done that yet."
        lexi.say "[hero.name]'s been the best thing that ever happened to me."
        lexi.say "She was there when I decided to make the biggest change in my life of all."
        lexi.say "Together we stood up to Danny and kicked him to the curb for good."
        lexi.say "Then [hero.name] went to college and got her qualifications."
        hide lexi
        show lawyers ending bree
        with fade
        lexi.say "Now she's a big-time lawyer, kicking legal ass in the big city!"
        lexi.say "She has a big, swanky office in town."
        lexi.say "Plus our house is totally massive and one hundred percent not a trailer!"
        lexi.say "Seriously, you should see [hero.name] in her suits and heels."
        lexi.say "She's battling in the courtroom every chance she gets."
        lexi.say "It's like one of those TV series with a cool theme tune and everything!"
        lexi.say "And me?"
        scene bg black
        show nice ending lexi
        with fade
        lexi.say "Well, I stay home and run the house, yeah?"
        lexi.say "Yup...I guess you're right."
        lexi.say "That does kind of make me a housewife!"
        lexi.say "But you think I'm going to complain about that?"
        lexi.say "When my partner makes enough money to keep us both ten times over?!?"
        if bree.is_visibly_pregnant:
            lexi.say "Sure, it means I have to do most of the caring for little Susy."
            lexi.say "But we can afford the best day-care that money can buy for her."
            lexi.say "So I can take time off when we get the chance."
            lexi.say "And she's going to grow up with two totally cool mommies."
            lexi.say "Maybe she'll even become a lawyer too, start up a legal dynasty!"
        else:
            lexi.say "Right now it feels like [hero.name]'s working every hour we're awake."
            lexi.say "But I think that we'll want to slow down some time in the future."
            lexi.say "You know, actually enjoy some of the money she's making?"
            lexi.say "And then we can start thinking about a family."
            lexi.say "Because we'd make great parents for any kid we tried to adopt."
        show nice ending bree lexi with dissolve
        lexi.say "So yeah, I have more than I could ever have dreamed I'd end up with."
        lexi.say "But the only thing that I couldn't live without is [hero.name]."
        lexi.say "Hell, I'd even be happy if it were just the two of us back in the trailer-park."
        lexi.say "Though don't tell her I said that, as she might think she can slack off!"
        lexi.say "And this girl's become well and truly used to the luxury in which she's been living!"
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
