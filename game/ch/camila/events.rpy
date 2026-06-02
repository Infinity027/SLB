init python:

    Event(**{
    "name": "camila_event_02",
    "label": "camila_event_02",
    "priority": 500,
    "duration": 2,
    "conditions": [
        IsDone("camila_event_01"),
        HeroTarget(IsGender("male")),
        IsDayOfWeek(6, 7),
        IsTimeOfDay("afternoon"),
        PersonTarget(camila,
            Not(IsHidden()),
            IsFlag("camiladelay", False),
            MinStat("love", 20),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_03",
    "label": "camila_event_03",
    "priority": 500,
    "duration": 2,
    "conditions": [
        Or(
            IsDone("camila_event_02"),
            IsDone("camila_event_04_alt"),
            ),
        HeroTarget(IsGender("male")),
        IsTimeOfDay("afternoon"),
        PersonTarget(camila,
            Not(IsHidden()),
            IsFlag("camiladelay", False),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_04",
    "priority": 500,
    "label": "camila_event_04",
    "duration": 1,
    "conditions": [
        IsDone("camila_event_03"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mall_southside")),
        PersonTarget(camila,
            Not(IsHidden()),
            IsFlag("camiladelay", False),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_05",
    "priority": 500,
    "label": "camila_event_05",
    "duration": 1,
    "conditions": [
        IsDone("camila_event_04"),
        Not(IsDone("camila_event_05b")),
        IsSeason(3),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            IsRoom("date_park"),
            ),
        PersonTarget(camila,
            OnDate(),
            IsFlag("camiladelay", False),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_05b",
    "priority": 500,
    "label": "camila_event_05b",
    "duration": 1,
    "conditions": [
        IsDone("camila_event_04"),
        Not(IsDone("camila_event_05")),
        IsSeason(0, 1, 2),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            IsRoom("date_park"),
            ),
        PersonTarget(camila,
            OnDate(),
            IsFlag("camiladelay", False),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_06",
    "priority": 500,
    "label": "camila_event_06",
    "conditions": [
        Or(
            IsDone("camila_event_05"),
            IsDone("camila_event_05b"),
            ),
        HeroTarget(
            IsGender("male"),
            OnDate()),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("camiladelay", False),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_07",
    "priority": 500,
    "label": "camila_event_07",
    "conditions": [
        IsDone("camila_event_06"),
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            IsRoom("policestation")),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("camiladelay", False),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_08",
    "priority": 500,
    "label": "camila_event_08",
    "conditions": [
        IsDone("camila_event_07"),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(camila,
            Not(IsHidden()),
            Not(IsActive()),
            IsFlag("camiladelay", False),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_09",
    "label": "camila_event_09",
    "priority": 500,
    "conditions": [
        IsDone("camila_event_08"),
        HeroTarget(
            IsGender("male"),
            IsRoom("hospital"),
            ),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("camiladelay", False),
            IsFlag("schedule", "hospital"),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_10",
    "label": "camila_event_10",
    "priority": 500,
    "conditions": [
        IsDone("camila_event_09"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinema")
            ),
        PersonTarget(camila,
            OnDate(),
            MinStat("love", 160),
            MinStat("sexperience", 1),
            Not(IsFlag("schedule", "hospital")),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_10_repeatable",
    "label": "camila_event_10",
    "priority": 500,
    "conditions": [
        IsDone("camila_event_10"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinema")
            ),
        PersonTarget(camila,
            OnDate(),
            MinStat("love", 160),
            MinStat("sexperience", 1),
            Not(IsFlag("schedule", "hospital")),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "chances": 25,
    "do_once": False,
    "once_month": True,
    })

    InteractEvent(**{
    "name": "camila_event_11",
    "label": "camila_event_11",
    "priority": 500,
    "conditions": [
        IsDone("camila_event_10"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(camila,
            IsActive(),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_sub_event_01",
    "label": "camila_sub_event_01",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        MinDateScore(50),
        PersonTarget(camila,
            OnDate(),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "camila_sub_event_02",
    "label": "camila_sub_event_02",
    "priority": 500,
    "conditions": [
        IsDone("camila_event_07"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(camila,
            IsActive(),
            MinStat("sub", 50),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_sub_event_03",
    "label": "camila_sub_event_03",
    "priority": 500,
    "duration": 2,
    "conditions": [
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            Not(IsRoom("house")),
            HasStamina(),
            ),
        PersonTarget(camila,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("sub", 75),
            MinStat("sexperience", 4),
            Not(IsFlag("schedule", "hospital")),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "camila_sub_event_04",
    "label": "camila_sub_event_04",
    "priority": 500,
    "duration": 2,
    "conditions": [
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            IsRoom("policestation"),
            HasStamina(),
            ),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 90),
            MinStat("sexperience", 4),
            Not(IsFlag("schedule", "hospital")),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "camila_preg_talk",
    "label": "camila_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(camila,
            IsPresent(),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "camila_investigation_callback",
    "label": "camila_investigation_callback",
    "conditions": [
        IsNotDone("cassidy_investigation_complete"),
        IsHour(9, 22),
        PersonTarget(camila,
            Not(IsPresent()),
            MinCounter("investigationcallback", 2),
            ),
        ],
    "music": "music/roa_music/miss_summer.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "camila_event_01_alt",
    "label": "camila_event_01_alt",
    "duration": 1,
    "conditions": [
        IsNotDone("kylie_investigation_2"),
        IsHour(1, 3),
        IsWearing("fancy_clothes"),
        IsWearing("luxury_watch"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("alley"),
        ),
    ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/hero.ogg",
})

    Event(**{
    "name": "camila_event_02_alt",
    "label": "camila_event_02_alt",
    "duration": 1,
    "conditions": [
        IsDone("camila_event_01_alt"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("undercover", True),
            IsFlag("undercoverdelay", False),
            IsRoom("policestation"),
        ),
    ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/hero.ogg",
})

    Event(**{
    "name": "camila_event_03_alt",
    "label": "camila_event_03_alt",
    "duration": 1,
    "conditions": [
        IsDone("camila_event_02_alt"),
        IsHour(22, 2),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("undercover", True),
            IsRoom("street"),
        ),
    ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/hero.ogg",
})

    Event(**{
    "name": "camila_event_04_alt",
    "label": "camila_event_04_alt",
    "duration": 3,
    "conditions": [
        IsDone("camila_event_03_alt"),
        IsHour(16),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("policestation"),
            IsFlag("undercover", True),
        ),
    ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/hero.ogg",
})


    Activity(**{
    "name": "camila_redo_undercover",
    "label": "camila_redo_undercover",
    "display_name": "Go back undercover",
    "icon": "camila",
    "duration": 1,
    "conditions": [
        IsDone("camila_event_02_alt"),
        IsNotDone("camila_event_04_alt"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("undercover", False),
            IsRoom("policestation"),
        ),
    ],
    "priority": 500,
    "do_once": True,
})

    Event(**{
    "name": "camila_pregnant_request",
    "label": "camila_pregnant_request",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("status", "girlfriend"),
            MaxCounter("pregnant", 8),
            ),
        'game.days_played - camila.flags.girlfriend_day >= 7',
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "camila_collar_request",
    "label": "camila_collar_request",
    "priority": 500,
    "duration": 2,
    "conditions": [
        MinDateScore(50),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(camila,
            OnDate(),
            Not(IsFlag("collared")),
            MinStat("sub", 80),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

label camila_event_01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Camila")
    if not result:
        $ hero.cancel_event()
        return
    $ camila.unhide()
    "It's been a good space of time since I last heard anything from Camila, the cop on Kylie's case."
    "And I'd actually started to be able to move on a bit, beginning to get it off my mind."
    "So it comes as quite a surprise to see her name pop up on my phone when it rings out of the blue."
    "I hesitate for a moment, a little of the familiar fear creeping back at the memory of what happened."
    "But then I push those feelings as far down into the pit of my stomach as I can."
    "Because if I don't face these fears and beat them, I'll be scared for the rest of my life!"
    "So I take the call, trying to sound as nonchalant as possible."
    mike.say "Hey, Camila."
    mike.say "What can I do for you?"
    camila.say "[hero.name], are you free right now?"
    "There's no beating around the bush, as usual with Camila."
    "She's all business, getting straight to the point with no time for small talk."
    mike.say "Ah...yeah, I guess so."
    camila.say "Great, that's great."
    camila.say "Listen, I need you to meet me somewhere, okay?"
    camila.say "The multiplex in town - you know the place?"
    mike.say "Sure, Camila, I know it."
    camila.say "Be there in thirty minutes sharp."
    camila.say "You can make it, right?"
    "Already grabbing my stuff and heading for the door, I nod in agreement."
    "The fact that Camila can't actually see the gesture doesn't seem to matter to me."
    mike.say "Y...yeah, Camila..."
    mike.say "I'll be there as soon as I can!"
    camila.say "Good, that's good."
    camila.say "And don't be late!"
    "My mind is racing the whole way to the multiplex, confused by Camila's demands."
    "The cinema sounds a strange place to meet a cop, but what do I know?"
    "Maybe it's perfect to discuss the details of an ongoing case with the victim."
    "But what could it be about?"
    "Is Kylie being sentenced for what she did on that night?"
    "Or worse - could she have actually escaped from where they had her locked up?!?"
    "By the time I hurry into the lobby of the cinema, I'm already fearing the worst."
    "I can actually imagine Kylie lurking in the shadows some where, blade in hand!"
    scene bg cinema
    show camila casual
    with fade
    camila.say "There you are, [hero.name]!"
    camila.say "You only just made it!"
    "I see her walking towards me, a serious expression on her face."
    "But then I look down and see the popcorn and sodas in her hands."
    "Camila seems to notice the puzzled look now spreading over my own face."
    camila.say "I didn't know if you preferred sweet or salted, so I got both."
    camila.say "Well, don't just stand there - the movie's about to start!"
    "I feel my lips moving, but no sound seems to come out."
    "What in the hell is she talking about?"
    "We can't talk about the case inside of a movie theatre!"
    mike.say "Wait, Camila..."
    mike.say "What do you mean?"
    mike.say "We're not here to actually watch a movie - are we?!?"
    "Now it's Camila's turn to look at me in confusion."
    camila.say "Well, yeah, [hero.name]."
    show camila flirt
    camila.say "Isn't that what you do on a date?"
    menu:
        "Be amused":
            "I'm so surprised by what Camila just said that I burst out laughing."
            "She seems even more surprised to see me react like that."
            "But I just can't help myself, as it feels so crazy to me."
            show camila normal
            show fx question
            camila.say "What's so funny, huh?"
            camila.say "Is the idea of us seeing a movie such a joke to you?!?"
            "I wave her questions away with one hand, still trying to stop laughing."
            mike.say "No, Camila..."
            mike.say "That's not it, really!"
            "I let out a lungful of air as I finally manage to get myself under control."
            mike.say "I just thought..."
            mike.say "I thought you wanted to talk about the case?"
            mike.say "About Kylie, you know?"
            "Camila frowns at this, shaking her head."
            show fx question
            camila.say "Huh?"
            show fx exclamation
            camila.say "No way, [hero.name]!"
            camila.say "I'd have called you down to the station if that were the case."
            "The realisation of what's happened seems to be sinking in for Camila."
            "And I see the normally tough demeanour she shows slip just a little."
            "I swear that she almost blushes with embarrassment."
            "But then she shakes it off and rolls her eyes."
            show camila bored
            camila.say "Ah shit."
            camila.say "This is awkward..."
            "Now it's my turn to shake my head."
            mike.say "Don't worry about it, Camila."
            mike.say "It's actually a weight off my mind."
            mike.say "Now I know there's nothing to worry about."
            mike.say "You know, with Kylie?"
            "Camila nods, but I see her looking down at the snacks she's still holding."
            show camila normal
            camila.say "So..."
            camila.say "About that movie?"
            mike.say "It sounds like a great idea, Camila."
            mike.say "What are we seeing?"
            "Camila instantly seems to cheer up at my enthusiasm."
            "She smiles in a way that reminds me of just how cute she actually is."
            "Well, you know - under all that tough cop exterior."
            show camila happy
            camila.say "Action Cop Six - the Dawn of Justice!"
            show fx exclamation
            camila.say "I've been dying to see it for weeks now!"
            "I nod as we walk towards the movie theatre, listening to Camila talk."
            "And I'm more enthused by her words than the actual trailers I've seen of the movie!"
            $ camila.love += 2
            $ game.pass_time(3)
        "Get angry":
            "I can hardly believe my ears."
            "Did she actually just say this is supposed to be a date?!?"
            mike.say "I...I thought you wanted to talk to me?"
            mike.say "To talk about the case?"
            "Camila shakes her head at this, still looking confused."
            show camila normal
            show fx question
            camila.say "Huh?"
            camila.say "Why would you think that?"
            camila.say "I'd have told you to come down to the station for that!"
            "I was getting pretty annoyed before she said that."
            "But now I'm almost dumbstruck at her admission."
            mike.say "And you didn't think to tell me that?"
            "Camila shrugs, beginning to look a little awkward."
            show camila sad
            camila.say "No, [hero.name], I didn't."
            camila.say "I guess I just thought you'd know the difference."
            camila.say "Pretty funny we got our wires crossed, yeah?"
            mike.say "No, Camila, it's not!"
            mike.say "I was scared shitless just now."
            mike.say "I thought that psycho might have escaped or something!"
            "For a moment I can see the reality of the situation dawning on Camila."
            "And I think that she's about to apologise for what's happened."
            "But then a change comes over her face and she seems to harden her mood."
            show camila normal
            camila.say "Don't talk crazy, [hero.name]."
            camila.say "That fruit-loop's not getting out, trust me!"
            mike.say "Whatever, Camila."
            mike.say "But if it's all the same to you, I think I'll pass on the movie."
            "And with that, I make a point of turning on my heel and walking away."
            "I hear Camila begin to protest, but I ignore her and keep on walking."
            "Sure, she might be a tough cop and more than a little mad at me right now."
            "But I feel justified in snubbing her like that after what just happened."
            $ camila.love -= 2
            $ game.pass_time(1)
    hide camila
    $ camila.flags.camiladelay = TemporaryFlag(True, 2)
    return

label camila_event_02:
    $ game.room = "street"
    $ aletta.flags.forceLocation = (game.days_played, game.hour, "street")
    if camila.love.max < 40:
        $ camila.love.max = 40
    scene bg street at blur(8), dark with dissolve
    "I'm more than a little reluctant to take up Camila's offer of an invite to the local shooting-range."
    "It's not that I have some deep-seated problem with guns, at least when they're in the right hands."
    "But I'm no crazed gun-nut either, and the thought of firing off rounds isn't my idea of a fun time."
    "And before you say it, I know that the idea is for me to learn how to defend myself, not have fun."
    "But I'm still not sure what the time I'm spending with Camila really counts as in the scheme of things."
    "Sometimes it feels like she's training me up to be some kind of self-defence badass."
    "And then at others she'll catch me off-guard by suggesting that we do something fun, even romantic in nature!"
    "I guess what's important is that I enjoy spending the time with her either way."
    "So in the end, I just agree to meet her at the shooting-range and leave the rest to fate..."
    scene bg shootingrange
    show camila casual
    with dissolve
    camila.say "Hey, [hero.name]."
    camila.say "You ready to shoot your load?"
    mike.say "Shoot my what now?!?"
    show camila happy
    "Camila bursts into a snorting laugh that not in the least bit feminine."
    "And then she follows up by slapping me on the back - pretty hard too!"
    "I can't help groaning and staggering forwards a little from the force of the blow."
    camila.say "Don't worry, [hero.name]."
    camila.say "I'm just fucking with you, that's all!"
    "I try my best to sound like one of the tough, macho cops that she hangs around with."
    "But she managed to wind me a little, so my words come out quiet and wheezy instead."
    mike.say "Ah...okay, Camila."
    mike.say "I get it now - that's pretty funny!"
    camila.say "Yeah, I thought so!"
    camila.say "Come on, let's get inside."
    camila.say "We won't get any shooting done standing here with our dicks in our hands!"
    "With that, Camila strides off towards the door to the shooting-range."
    "She walks quickly and with the purpose that comes from being a no-nonsense cop."
    "And it's all I can do to scurry after her, trying as best I can to keep up."
    "Once we're inside, the staff greet Camila like she's an old friend."
    "Which lets me know that she must be one of their regular customers."
    "In no time at all we're provided with goggles and ear protectors."
    "Then Camila hands me my pistol and practically marches me to where I'll be shooting."
    show fx exclamation
    camila.say "Okay, rookie - let's see what you got!"
    "I nod at this, taking a deep breath as I raise the unfamiliar weapon and take aim..."
    if hero.has_skill("shooting"):
        "The pistol's one that I'm not used to shooting."
        "But I reckon that I can compensate for that."
        "It won't be as impressive as if I was using a more familiar piece."
        "But beggars can't be choosers, so I control my breathing and then fire."
        "One after one, the bullets find the target at the other end of the range."
        "I've done better in the past, but I'm not at all ashamed of my shooting."
        "And once I put down the pistol and face Camila, I can see she's impressed too."
        show camila flirt
        show fx exclamation
        camila.say "Where did you learn to shoot like that, [hero.name]?"
        camila.say "I thought you were a damn amateur!"
        mike.say "I've always kept up my shooting, Camila."
        mike.say "I'm just not crazy about the idea of carrying a gun around with me."
        "She nods her head slowly, as if weighing up my words."
        show camila happy
        camila.say "That's admirable, [hero.name]."
        camila.say "Just remember that the bad guys don't think the same as you do!"
        "I nod at this, not sure if I've impressed Camila or annoyed her."
        $ camila.love += 1
    else:
        "I honestly try my best, but my nerves must be getting the better of me."
        "As soon as I pull the trigger, the boom of the gun makes me jump in the air."
        "I let out a yelp of sheer terror and the bullet misses the target by a mile."
        "I turn my head to look at Camila, shrugging apologetically."
        show camila sad
        "She looks a little disappointed, but motions for me to try again."
        "I nod and do as I'm told, hoping the first shot was a fluke."
        "But my aim is still as poor while I shoot until the pistol is empty."
        "It's not a total humiliation, as I do manage to hit the target at least once."
        "All I can do is shake my head as I return to Camila, expecting a dressing down."
        mike.say "Sorry, Camila."
        mike.say "I guess I'm just not cut out to use one of these things."
        show camila normal
        camila.say "Don't beat yourself up, [hero.name]."
        camila.say "No one gets good at something the first time they try."
        camila.say "You just need more practice, that's all."
        "I nod and smile, finding her words reassuring."
    hide camila with easeoutright
    "As we're getting ready to leave, Camila hangs back for a moment."
    "I can see that she's talking to one of the staff, a guy she must know pretty well."
    if "aletta_event_04b" in DONE:
        "I kick my heels while I wait for Camila to wrap up her conversation."
        "It's none of my business who she talks to, I'm well aware of that."
        "But still I can't help being just a little curious."
        "I'm trying to discern what I can from a distance when I hear a familiar voice."
        aletta.say "Well hello, [hero.name]."
        aletta.say "Fancy bumping into you here!"
        show aletta happy casual with dissolve
        "I turn around to see Aletta standing there."

        mike.say "Oh, hi, Aletta."
        mike.say "Yeah, I haven't been here since that time we came together."
        mike.say "I...I'm just waiting for Camila over there."
        "Aletta follows my gaze to where Camila's standing."
        "She makes an odd kind of harumphing sound as she does so."
        show aletta normal
        "The kind of sound that usually means she's not at all impressed with what she sees."
        aletta.say "Oh yes, HER!"
        aletta.say "I saw her giving you some pointers just now."
        show aletta at left4
        show camila at right
        with easeinright
        "As Aletta finishes speaking, Camila makes it over to where we're standing."
        mike.say "Oh, Camila, this is Aletta."
        mike.say "We...ah...we work together!"
        "I see Aletta's eyes go wide at this."
        "She seems to bristle at only being introduced as my colleague and nothing more."
        camila.say "Hey, Aletta - are you a gun-nut too?"
        aletta.say "No, I'd describe myself more as an enthusiast."
        aletta.say "I shoot for sport."
        show camila happy
        "Camila smiles at this, nodding her head."
        camila.say "So you're an amateur then?"
        camila.say "When you're on the force, you need to be more of a professional!"
        show aletta happy
        aletta.say "White collar versus blue collar, dear."
        aletta.say "I think that's the distinction you're looking for!"
        "Wait a minute - are they exchanging insults?!?"
        mike.say "Ah, hey, you two..."
        mike.say "I'm sure you have a lot to talk about."
        mike.say "But maybe we can meet up some other time, huh?"
        "At the sound of my voice, both girls seem to suddenly snap out of it."
        "They exchange smiles that look less than sincere and nod their heads."
        show aletta normal
        show camila normal
        aletta.say "Of course, [hero.name]."
        aletta.say "I have other places to be."
        camila.say "Me too, [hero.name]."
        camila.say "Let's get out of here!"
        show camila at top_mostright with ease
        "I walk out of the place with Camila, trying to tell myself it's over."
        scene bg shootingrange
        show aletta normal casual
        with fade
        "But when I glance back over my shoulder, I see Aletta still staring in our direction."
        "She narrows her eyes before turning her back and walking away."
        hide aletta with fade
    else:
        "It takes Camila a couple of minutes to wrap up her conversation."
        "And I spend the time trying to look interested in the posters on the walls."
        "When she finally walks back over, I raise my eyebrows and give her a smile."
        show camila
        mike.say "Ah, who's that guy, Camila?"
        "She looks at me sideways with a crooked smile of her own."
        camila.say "Just a friend, [hero.name], that's all!"
        show fx question
        camila.say "What's it to you, anyway?"
        camila.say "Wouldn't happen to be jealous, would you?"
        mike.say "What...jealous?"
        mike.say "Why would I be jealous?"
        mike.say "I'm just curious, that's all!"
        show camila happy
        camila.say "Yeah, you're curious all right!"
        "Camila laughs, letting me know that she's amused by my questions."
        "All I can do is shrug it off, trying to explain myself."
        mike.say "Well, it's just that we came here together, you know?"
        mike.say "On a...well, maybe not a date, as such..."
        show camila normal
        camila.say "I never said this wasn't a date, [hero.name]."
        camila.say "Why can't a trip to the shooting range be a date?"
        mike.say "I...I guess it can, Camila!"
        mike.say "Wait a minute - are you saying this IS a date?"
        show camila bored
        camila.say "I don't remember saying that either!"
        "Camila smiles again as we walk out of the place."
        "I can see just how much she enjoys screwing around with me."
        "But what surprises me is just how much I like it too..."
    $ camila.love += 2
    $ camila.flags.camiladelay = TemporaryFlag(True, 3)
    hide camila
    return

label camila_event_03:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Camila")
    if not result:
        $ camila.love -= 5
        $ hero.cancel_event()
        return
    if camila.love.max < 60:
        $ camila.love.max = 60
    "I'm just going about my daily life, not particularly expecting anything out of the ordinary to happen."
    "And then I feel my phone vibrating in my pocket, which also is nothing exceptional or unusual."
    "But when I looks down to see who's calling, Camila's number is there on the screen."
    "Now that is something out of the ordinary - being called by a cop out of the blue."
    "Not to mention the fact that she's a particularly hot female cop too!"
    "So I don't hesitate to answer the call."
    mike.say "Hey, Camila - what's up?"
    camila.say "Ah, nothing much."
    camila.say "Just wondered if you could do me a favour?"
    "As nonchalant as she seems, there's something weird about Camila's voice."
    "She sounds a little wheezy, like she's winded or out of breath."
    "I say it's weird because she's crazy fit and tough to boot."
    "But I also know that she's proud, so I don't press her on it."
    mike.say "Sure, Camila."
    mike.say "I'm not doing anything I can't drop."
    camila.say "Great, great..."
    camila.say "So you can come pick me up from the hospital right away?"
    mike.say "The hospital?"
    mike.say "Camila, what the hell happened to you?!?"
    camila.say "Jesus, [hero.name] - calm down!"
    camila.say "I got shot, that's all!"
    "I don't really remember how the conversation ends."
    "But I'm on my way to the hospital the moment it does."
    "Once there, I hurry inside and ask frantic questions until I find Camila."
    scene bg hospital with fade
    "As soon as I set eyes on her, I hurry over to see if she's okay."
    show camila casual with dissolve
    mike.say "Camila, there you are."
    mike.say "I...I came as fast as I could!"
    "Camila shakes her head and chuckles at my worried tone."
    "But when she stands up, I see her wince in pain."
    "I hurry to help, but she waves me aside."
    camila.say "I'm okay, really."
    camila.say "It's not the first time I got shot!"
    mike.say "But still, Camila..."
    mike.say "Maybe you should sit back down?"
    mike.say "I could get a wheelchair or something..."
    with vpunch
    camila.say "NO..."
    "As soon as Camila raises her voice, everyone looks in her direction."
    "I see her waver for a moment, as if her tough cop act is shaken."
    "But then she recovers and she's Dirty Harriet again."
    camila.say "Look, [hero.name], I'll be fine."
    camila.say "The bullet went clean through my side."
    camila.say "In one end and out the other, nice and neat."
    "Laura" "Aren't you supposed to tell him the bullets bounce off of you?"
    "Laura" "Or isn't that part of your superhero bullshit anymore?"
    show laura teaser at left with dissolve
    "I look around to see a female doctor scribbling notes on a clipboard."
    "She has a brown bob and a tired, serious-looking face."
    "Camila lets out a loud sigh and nods in the doctor's general direction."
    camila.say "[hero.name], meet Laura."
    camila.say "Laura, meet [hero.name]."
    "Laura" "Nice to meet you, [hero.name]."
    "Laura" "Camila and I used to be close, back in the day."
    "Laura" "But now all I have to put up with is being her doctor."
    "Laura" "So I only have to stitch her back together in a physical sense!"
    show camila annoyed
    "I expect Camila to fire back in her usual manner any second."
    "But instead she looks away, as if Laura's words struck a nerve."
    "Laura" "I'm guessing you're looking out for her these days?"
    menu:
        "Side with Camila":
            "I don't know what the history between Camila and Laura amounts to."
            "But Camila's my friend, and she just got shot!"
            "So how does Laura get off talking to her like that?"
            mike.say "If by that you mean I care for her, then yes."
            mike.say "I rushed here the moment I heard she got shot."
            mike.say "I wish I could have been there when it happened too!"
            "Laura's face becomes grave at this, like she disapproves."
            "Laura" "Then I'd have been pulling a bullet out of you too."
            "Laura" "Maybe even worse!"
            "She's really getting my back up now."
            "And so I answer her without thinking it through."
            mike.say "Oh yeah?"
            mike.say "Well I'd take a bullet for her!"
            "Laura shakes her head."
            "Suddenly the fight seems to go out of her and she looks tired again."
            "Laura" "Look, all I'm saying is be careful."
            "Laura" "Or else you might get your wish!"
            $ camila.love += 2
        "Side with Laura":
            "My natural instinct is to leap to Camila's defence."
            "But all the same, Laura does have a point."
            "Camila does seem to have a cavalier attitude."
            "At least she does when it comes to her own safety."
            mike.say "I...I do what I can, I guess."
            mike.say "But I'm not used to seeing people I care about get shot."
            mike.say "It's pretty scary..."
            "Laura seems to soften at this admission."
            "Maybe she's realising that I'm not the one she needs to pick a fight with here."
            "She lets out a tired sigh and shakes her head."
            "Laura" "Look, you say you care about her."
            "Laura" "So just try to talk some sense into that thick head of hers."
            "Laura" "I don't want to find her in the morgue one of these days."
            $ camila.love -= 2
    "Camila mutters something under her breath."
    "And it takes me a moment to realise why."
    "It's because she doesn't want Laura to hear it."
    "Camila, the tough cop is actually muttering like a sullen child!"
    "Laura notices this and rolls her eyes before turning to go."
    "Laura" "Like I said, she's not my problem anymore."
    "Laura" "Just try to keep her alive, okay?"
    hide laura with easeoutleft
    "Once Laura's walked away, I turn to Camila."
    mike.say "You want to explain what that was all about?"
    "At first I think Camila's just going to brush me off."
    "But then she sighs too, and she starts to talk."
    show camila sad
    camila.say "Alright, alright..."
    camila.say "Laura and I were an item for a while."
    camila.say "But she broke it off because she couldn't handle my being a cop."
    "I nod, all the time thinking that there must be another side to the story."
    mike.say "That's tough, Camila."
    mike.say "Sounds like she still cares for you a little though."
    "Camila starts to nod, then shakes her head."
    "And then she waves away whatever she's thinking with one hand."
    show camila normal
    camila.say "I don't know, [hero.name]."
    camila.say "It was complicated and messy, all at the same time."
    camila.say "Plus the stick up Laura's ass always had a stick up it's ass!"
    "I can't help chuckling at Camila's tough demeanour."
    mike.say "Come on, Camila."
    mike.say "Let's get you home before the pole up Laura's ass gets any stiffer!"
    $ camila.love += 2
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    return

label camila_event_04:
    if camila.love.max < 80:
        $ camila.love.max = 80
    "It all happens so fast that I don't really have time to make any sense of it."
    "One minute I'm just walking along at the mall, minding my own business as usual."
    "And then the next thing I know, I hear a commotion starting up behind me."
    "People are shouting and gesticulating wildly, like something serious is happening."
    "I stop dead in my tracks, turning to glance over my shoulder as I do so."
    "Right now, I'm still too confused to get a handle on what the fuss is about."
    "But that soon changes as I begin to hear actual words and see what's going on."
    "Guy" "Hey, someone stop that guy!"
    "Girl" "That scumbag stole an old woman's purse!"
    "It's right about now that I lay my eyes on the guy they're yelling about."
    "He's a typically sleazy-looking sort, shifty and probably on something."
    "And he really does have what looks like an old woman's purse clutched to his chest."
    "But the reason that I can make all of this out is very simple."
    show danny as mugger at left, blacker with moveinleft
    "It's because he's running straight at me!"
    "I watch as the guy shoulders a couple of other guys out of his way."
    "It's not like he's huge."
    "But he uses his momentum and the element of surprise like a pro."
    "Nobody's expecting him to crash into them, and so they go flying to either side."
    "That's not going to work on me though."
    show danny as mugger at center, blacker with move
    "And that's because I'm standing right in his path."
    "That and the fact that I've already seen him coming too."
    "I estimate that I have maybe a fraction of a second to make a decision."
    "Do I throw myself out of the mugger's way?"
    "Or do I try and tackle him to the ground?"
    menu:
        "Tackle mugger" if hero.fitness >= 50:
            "Ah, what the hell."
            "The guy doesn't look that big up close."
            with hpunch
            "Without another thought, I throw myself at the mugger."
            "So far he's taken everyone by surprise as he barges past them."
            "But now it's his turn to be caught off-guard."
            "The guy was obviously thinking that I'd leap aside."
            "Which means that he's totally unprepared when I barrel into him!"
            play sound body_fall
            hide danny as mugger with moveoutbottom
            with vpunch
            "We both go down in a heap of limbs."
            "And I feel the impact of hitting the ground wind me a little."
            "But I'm still the only one that's got his wits about him."
            "So I use my weight to start grappling with the mugger."
            "It doesn't take long for him to snap out of it."
            "And then he starts to struggle for all he's worth."
            "I do my best, but I don't think that I'm going to be able to hold him..."
            camila.say "Alright, scumbag."
            camila.say "Hands where I can see them!"
            "The voice is so loud and full of authority that I obey without question."
            show camila work happy with easeinleft
            "Which is why Camila seems to be stifling a laugh as she cuffs the mugger."
            show camila work normal
            camila.say "Not you, [hero.name]!"
            "She begins to haul the mugger to his feet."
            "And I get up off the ground too."
            "Though I don't know which is wounded more."
            "My ass where I fell down on it."
            "Or my pride where I made a fool of myself in front of Camila!"
            camila.say "Thanks for the helping hand there."
            camila.say "You made catching this piece of shit so much easier!"
            mike.say "Ah, you know, Camila."
            mike.say "Anything I can do to help!"
            "Camila leans in close and whispers to me."
            camila.say "And just for the record."
            show camila flirt
            camila.say "If you want me to use my cuffs on you - just ask!"
            "As Camila hauls the mugger away, I can't help flushing a little for a second time."
            "But at the same time I'm thinking about taking her up on the offer..."
            $ camila.love += 2
        "Leap aside":
            play sound woosh_punch
            with hpunch
            "At the last moment I leap aside, landing hard on the ground."
            "I get the wind knocked out of me and I'll probably be sore in the morning."
            hide danny as mugger with moveoutright
            "But I see the mugger dash straight through the spot where I was just standing."
            "He doesn't slow down or look in my direction for a second."
            "Instead he runs straight past and disappears into the crowd."
            "It's only now that I see there was someone following close on his heels."
            "A familiar figure that seems intent upon closing the distance between them."
            show camila work with easeinleft
            "It's Camila, arms pumping and legs pounding the ground beneath her."
            "She doesn't stop either, but I'm sure she glances my way as she passes."
            "There's no way I can read the look on Camila's face."
            hide camila with easeoutright
            "But I still feel like she's caught me taking the coward's way out."
            "My cheeks are burning a little as I pick myself up off the floor."
            "I know that I shouldn't feel guilty about what I chose to do."
            "After all, I'm not a cop."
            "And that guy could have had a knife on him too!"
            "I just can't help feeling like I let Camila down somehow."
            $ camila.love -= 2
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    return

label camila_event_05:
    if camila.love.max < 100:
        $ camila.love.max = 100
    "Normally I'd be worried about inviting Camila for a walk somewhere like the local park."
    "Not because I don't want to spend time strolling and chatting with her."
    "But more because it can quickly turn into a guided tour of the town's seedy underbelly."
    "More than once she's spoiled a romantic moment by pointing out where she chased down and busted someone."
    "And let's just say that she's never shy of sharing the more graphic details as well!"
    "But today should be different, as it snowed overnight and there's a deep covering on the ground."
    "That means the park has been transformed into an unfamiliar wintery wonderland."
    "And it seems that the change is enough to take Camila's mind off of work for once too."
    "It even brings out a softer side of her, making her smile as we follow the path through the snow."
    "And when we stop at a particularly nice spot with a great view, she's positively beaming."
    show camila casual happy with dissolve
    camila.say "This was a great idea, [hero.name]."
    camila.say "Thanks for suggesting it!"
    "I shrug off the compliment as if it were nothing at all."
    "But secretly I feel a thrill at having pleased Camila."
    mike.say "Ah, you don't have to thank me, Camila."
    mike.say "It just seemed like a no-brainer."
    "Camila cocks her head on one side, like she knows I'm trying to play it cool."
    "But she doesn't call my bluff, for which I'm thankful."
    show camila normal
    camila.say "Seriously though, this is bringing back memories."
    camila.say "I remember, right over there..."
    "I feel my heart sink a little as Camila points in a particular direction."
    "Is this going to be another account of some scumbag getting their just deserts?"
    camila.say "That's where I used to go sledging when I was a kid!"
    "I let out a sigh of relief as Camila reminisces about her childhood."
    "Sometimes it's hard to imagine that she wasn't born a tough, macho cop!"
    "Like everyone else, there was a time when she was just an innocent, happy kid."
    "Camila opens her mouth to say more, and that's when it happens."
    show camila surprised at startle
    "A snowball hits her, right on the side of the head."
    "I see it burst and watch the expression of surprise and shock appear on her face."
    show camila annoyed at right4 with ease
    "And then, like a true professional, Camila spins on her heel."
    "She seems to know exactly which direction the missile came from."
    "And she's already zeroing in on the culprit responsible for throwing it too!"
    show camila angry
    camila.say "Who in the hell..."
    show camila surprised at right4, startle
    "Camila stops dead as her gaze falls upon a knot of kids standing close by."
    "None of them look to be ten years old at the most."
    "And they all look terrified of her."
    "Hastily they drop the incriminating snowballs in their hands."
    "Some of them are already starting to back away."
    "I find that I'm holding my breath, waiting to see what Camila does next."
    show camila normal at center, hshake
    "And then, quick as a flash, she bends down and grabs a handful of snow."
    "With incredible speed, she fashions it into a snowball of her own."
    "Then it's flying through the air, back at the nearest of the kids."
    "All at once the spell is broken as they realise they're off the hook."
    "Suddenly the air between Camila and the kids is full of snowballs and cries."
    "Even though they outnumber her, she seems to be able to hold her own."
    with screenshot
    with hpunch
    "And then I get a snowball to the face myself, an innocent bystander drawn into the fray!"
    "With that, I wade into the fight too, getting hit more often than I can hit my own target."
    "I try to help Camila out, but she seems to see me as fair game too."
    "And so it just ends up being a chaotic free-for-all."
    "By the time the snowball fight comes to a natural end, we're both panting and exhausted."
    show camila happy
    camila.say "What a bunch of little savages!"
    camila.say "But I think we held our own pretty well."
    "Though she's smiling, I can see something else in Camila's eyes."
    "It's almost like she's trying to hide the fact that she's actually feeling sad."
    menu:
        "Are you okay?":
            "I know how hard Camila seems to find talking about her feelings."
            "She's one of those tough types that's also emotionally constipated."
            "And sometimes those kind of people need a friend to draw it out of them."
            mike.say "Camila..."
            mike.say "Is something bothering you?"
            "At first I think she's just going to give me the brush-off."
            "But then Camila sighs and shakes her head."
            show camila normal
            camila.say "Those kids..."
            camila.say "They just reminded me of what happened with Laura and me."
            camila.say "What made her break it off between us, that is."
            "I nod, doing my best to look sympathetic."
            mike.say "What happened, Camila?"
            mike.say "You can tell me if you want."
            mike.say "I won't judge, I promise."
            camila.say "It's nothing special, [hero.name]."
            show camila sad
            camila.say "I wanted kids and she didn't, that's it."
            camila.say "I guess Laura was just more in love with her career than me!"
            mike.say "Wow, that's tough, Camila."
            mike.say "I'm sorry, for what it's worth."
            "Camila shakes her head and takes hold of my hand."
            "She squeezes it hard and pulls me after her as she starts to walk off."
            camila.say "It's worth something, [hero.name]."
            show camila normal
            camila.say "Because it makes me know you care!"
            "The rest of the walk passes quietly and without incident."
            "But I can feel the gratitude that Camila feels towards me for what I just said."
            "And it feels pretty good from my side of things to know that I helped, even a little."
            $ camila.love += 2
            $ game.active_date.score = 85
        "Ignore Camila":
            "If Camila's not going to come out and say how she's feeling, that's fine with me."
            "After all, we came out here to enjoy ourselves, not wallow in self-pity."
            mike.say "Yeah, Camila."
            mike.say "You sure showed them what happens when you mess with the law!"
            "Camila looks up at me and smiles."
            show camila bored
            camila.say "And you don't wanna mess with the law, right?"
            "I don't know if she was expecting me to dig deeper into how she's feeling."
            "But as she doesn't press the issue, I choose to take her words at face value."
            "And with that, we get on with finishing our walk through the park."
            $ camila.sub += 1
            $ game.active_date.score = 60
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    return

label camila_event_05b:
    if camila.love.max < 100:
        $ camila.love.max = 100
    scene bg forest
    "It seemed like a no-brainer to invite Camila along on a hike through the woods."
    "I mean, she's a tough, rugged cop - so she can handle anything nature has to offer, right?"
    "But when she agreed to come, I thought I sensed a hint of reluctance in her voice."
    "And now that we're out here, striding along on a glorious summer's day, I can see there's a problem."
    "Every time we have to cross a stream or step over something uneven, Camila flinches."
    "She's slowing us down too, meaning that we're not making good progress on the trail."
    "In the end I make the excuse of stopping to take a short break."
    "And once we do, I take the chance to ask Camila what's up."
    show camila annoyed with dissolve
    mike.say "Camila..."
    mike.say "Are you okay?"
    camila.say "Huh?"
    "She looks up at me from shaking a stone out of her boot."
    "And then she frowns, as if the question makes no sense."
    show camila normal
    camila.say "Of course I'm okay!"
    camila.say "Why wouldn't I be okay?!?"
    camila.say "All these miles out here in the wilderness."
    camila.say "So far away from civilisation, with no mobile signal..."
    "The reality of the situation suddenly begins to dawn on me."
    "And I can hardly believe it, shaking my head in disbelief."
    mike.say "Are...are you scared, Camila?"
    mike.say "Is being out here in the woods making you uneasy?"
    "Camila looks like she's about to say something."
    "Like she's about to chew me out for suggesting she's afraid."
    "But the words don't come out and I see her cheeks flush red."
    "I hate to admit it, but she looks pretty vulnerable in that moment."
    "And the novelty of seeing her with her guard down is striking."
    camila.say "I'm NOT scared, okay!"
    show camila annoyed
    camila.say "I'm...I'm just out of my element, okay?"
    camila.say "The woods can be a dangerous place."
    camila.say "And there are wild animals too - bears and even Bigfoot!"
    "Now I get it, and the whole thing is starting to make sense."
    "Camila's the apex predator back on the mean streets of the city."
    "But out here in nature, she doesn't know where to begin."
    "She's like a great white shark, plucked out of the ocean and dropped into the desert."
    "And it's weird for me to suddenly be the one that's more at ease with our situation."
    menu:
        "Reassure Camila":
            "I could easily make fun of Camila right now, have a joke at her expense."
            "And it'd feel good to be the tougher one for a change, but I won't do that."
            "It's more important to reassure her and put her mind at rest."
            mike.say "I don't think we're far enough out to be in any real danger, Camila."
            mike.say "But you're right to be aware of the dangers in the woods."
            mike.say "I just think you might be overdoing it a little!"
            "I try to keep my tone upbeat and not sound like I'm insulting Camila."
            "It seems to work, as she cracks a weak smile as she puts her boot back on."
            show camila normal
            camila.say "You come out here pretty often, don't you?"
            camila.say "You know your way around out here, huh?"
            mike.say "I wouldn't call myself the outdoors type."
            mike.say "But we went camping most summers when I was a kid."
            mike.say "And I never saw Bigfoot!"
            "Camila shakes her head, still looking embarrassed."
            "But I think I can see her confidence starting to return."
            camila.say "Thanks for understanding, [hero.name]."
            camila.say "When you're a cop, it's hard to admit you're even a little scared."
            camila.say "But I feel much safer knowing that you're looking out for me."
            $ camila.love += 2
        "Tease Camila":
            "I can't help smirking at the fact the big, tough cop's afraid of the woods."
            "This is too good to miss - I just have to make the most of it!"
            mike.say "Well..."
            mike.say "I wasn't going to say anything, Camila..."
            mike.say "But now that you mention Bigfoot..."
            "Almost as soon as I repeat the name of the infamous cryptid, Camila takes the bait."
            "Her eyes go wide and she struggles to pull her boot back on."
            "All the time she's glancing about the whole time."
            "It's as if she expects Bigfoot to pop out from behind a tree any second!"
            camila.say "What is it, [hero.name]?"
            show camila angry
            camila.say "You have to tell me!"
            camila.say "I saw a show about Bigfoot once."
            camila.say "And it was creepy as hell!"
            mike.say "Okay, Camila, I'll tell you."
            mike.say "But you have to promise not to panic."
            "Camila nods her head eagerly."
            show camila normal
            mike.say "Thing is, I saw some tracks a little way back..."
            mike.say "I wasn't sure at first, but..."
            mike.say "I think it was a Bigfoot!"
            "Camila looks genuinely worried now."
            "In fact, I've never seen her this shaken up."
            show camila annoyed
            camila.say "Oh shit..."
            camila.say "How big was it?!?"
            mike.say "Oh, I'd say it was at least a size ten!"
            camila.say "THAT BIG?!?"
            "Suddenly I see Camila narrow her eyes."
            camila.say "Wait a minute..."
            camila.say "I wear that size!"
            mike.say "You see - it was a big foot!"
            mike.say "I never knew you had such massive feet, Camila!"
            "Camila crosses her arms over her chest and frowns at me."
            show camila normal
            camila.say "You asshole!"
            camila.say "I was really frightened!"
            mike.say "Aw, come on, Camila - lighten up!"
            $ camila.sub += 2
    show camila normal
    "We press on with the hike, and Camila seems to be more at ease."
    "I don't know if I managed to talk her round when we stopped before."
    "Or if my words got under her skin and spurred her on."
    "Either way, we walk in silence for a good distance."
    "This gives me the chance to study Camila's expression."
    "And what I see written on her face makes me a little worried."
    "Though she's smiling, I can see something else in Camila's eyes."
    "It's almost like she's trying to hide the fact that she's actually feeling sad."
    menu:
        "Are you okay?":
            "I know how hard Camila seems to find talking about her feelings."
            "She's one of those tough types that's also emotionally constipated."
            "And sometimes those kind of people need a friend to draw it out of them."
            mike.say "Camila..."
            mike.say "Is something bothering you?"
            "At first I think she's just going to give me the brush-off."
            "But then Camila sighs and shakes her head."
            show camila normal
            camila.say "I was thinking about you going camping as a kid."
            camila.say "It was always something I saw myself doing with my kids too."
            camila.say "Then I got to thinking about Laura and me."
            camila.say "What made her break it off between us, that is."
            "I nod, doing my best to look sympathetic."
            mike.say "What happened, Camila?"
            mike.say "You can tell me if you want."
            mike.say "I won't judge, I promise."
            camila.say "It's nothing special, [hero.name]."
            show camila sad
            camila.say "I wanted kids and she didn't, that's it."
            camila.say "I guess Laura was just more in love with her career than me!"
            mike.say "Wow, that's tough, Camila."
            mike.say "I'm sorry, for what it's worth."
            "Camila shakes her head and takes hold of my hand."
            "She squeezes it hard as we walk down the trail together."
            camila.say "It's worth something, [hero.name]."
            show camila normal
            camila.say "Because it makes me know you care!"
            "The rest of the hike passes quietly and without incident."
            "But I can feel the gratitude that Camila feels towards me for what I just said."
            "And it feels pretty good from my side of things to know that I helped, even a little."
            $ camila.love += 2
            $ game.active_date.score = 85
        "Ignore Camila":
            "If Camila's not going to come out and say how she's feeling, that's fine with me."
            "After all, we came out here to enjoy ourselves, not wallow in self-pity."
            "The rest of the hike passes without incident and mostly in silence."
            "Maybe I should have pressed Camila to find out what was bugging her."
            "But I'm not her therapist, and she's a pretty tough case as well."
            "I doubt she'd have wanted me trying to solve her problems for her!"
            $ camila.sub += 1
            $ game.active_date.score = 60
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    return

label camila_event_06:
    if camila.love.max < 120:
        $ camila.love.max = 120
    $ camila.flags.haircut = True
    "Camila's not the kind of girl that springs a surprise on you, at least not usually."
    "It's not that she's boring or predictable in the normal way that some people can be."
    "As a cop, she's always full of energy and tougher than most guys I've met in my time."
    "I guess what I'm trying to say is that she's grounded, not given to making shallow statements."
    "Which is why the fact that she turns up for our date looking a little different to normal..."
    "Well, it kinda throws me a little!"
    show camila casual
    camila.say "Hey, [hero.name]."
    mike.say "Hey, Camila."
    show camila happy
    camila.say "I'm really looking forward to this, you know?"
    camila.say "Been thinking about our date all the time I was on shift!"
    "At first I can't actually tell what it is that's changed about her."
    "Camila's dressed just the same as normal, like she does at work off of it too."
    "She's not wearing any make-up, which is also perfectly normal for her."
    "She smells the same as well, no new perfume wafting my way."
    "And just for the record, that doesn't mean Camila smells bad at all!"
    "Simply that she smells of coffee and her own unique scent."
    "Which I happen to find very pleasant indeed."
    mike.say "Ah...yeah, Camila..."
    "It's about now that Camila seems to notice there's something up."
    "She studies me as I study her, obviously wondering what the hell's up."
    show camila normal
    camila.say "Erm, [hero.name]..."
    camila.say "Why are you staring at me like that?"
    camila.say "You're making me nervous!"
    "Just as Camila calls me out, I realise what's been bugging me."
    mike.say "Your hair - that's what it is!"
    mike.say "You're wearing it a different way!"
    "Camila looks to the left and right as I say this, almost like she's nervous."
    "At the same time, she unconsciously puts a hand against her head."
    camila.say "Geez, [hero.name], calm down already."
    camila.say "All I did was tie it up when I got off of work!"
    camila.say "I...I thought you might like it?"
    "Oops - looks like I could have handled that a little better than I did!"
    "Camila's looking me straight in the eye now."
    "I think she's expecting an answer to her question..."
    menu:
        "I love It":
            "I need to act quickly in order to keep Camila from thinking I hate it."
            "Because the truth of the matter is that I don't - I really like it."
            "It was just the surprise of seeing her make a change that threw me."
            mike.say "Like it?"
            mike.say "Camila, I love it!"
            mike.say "Anything's great that let's me see more of your smile!"
            "Camila's face breaks into an expression of confusion."
            show camila happy
            "But she's soon smiling all the same."
            camila.say "You really mean that, [hero.name]?"
            camila.say "I mean, it's not like I went and had a makeover or anything!"
            "The fact that Camila's trying to dismiss the compliment can only be a good sign."
            "It means that she's flattered without having to come out and fish for it."
            mike.say "You don't need a makeover, Camila."
            mike.say "You're great just the way you are!"
            "I see Camila flush a little, obviously touched."
            "She grabs hold of my arm with one hand and punches me playfully with the other."
            "But the very next moment, she pulls me close against her, pressing into my side."
            show camila flirt
            camila.say "Come on, [hero.name]."
            camila.say "Let's get this date going."
            camila.say "That way you can tell me more things you like about me!"
            mike.say "Sure thing, Camila."
            mike.say "You lead the way!"
            $ camila.love += 2
        "Meeeh...":
            "I think I know Camila pretty well by now."
            "At least well enough to know she doesn't like the smell of bullshit."
            "She appreciates the truth and would rather be told straight."
            "Rather that than be lied to for the sake of appearances."
            mike.say "To be honest, Camila..."
            mike.say "No, I don't like it."
            show camila sad
            "Camila looks instantly crestfallen, turning her eyes downwards at this."
            "Her reaction takes me by complete surprise, as it's not what I expected at all."
            "I'm used to Camila being the tough, no-nonsense cop she was when we first met."
            "But now I can see that she's beginning to feel safe around me."
            "Safe enough to drop her guard and even make an effort to look nice for me too."
            "And I just went and blew it - big time!"
            "But maybe I can salvage something from this?"
            mike.say "What I mean is that it's not a bad look for you, Camila."
            mike.say "I just like the look of your hair down, that's all."
            mike.say "That's how I'm used to seeing it, you know?"
            "Camila nods, but still looks like she's not totally convinced."
            camila.say "I guess that makes sense, [hero.name]."
            camila.say "I mean, I like my hair down too!"
            "We both fall silent for a moment, the mood turning a little awkward."
            "But then Camila seems to make an effort to shake it off."
            show camila normal
            camila.say "Come on - weren't we supposed to be on a date or something?"
            "She takes hold of my hand and leads me off."
            "And I make a mental note to be more careful with her feelings in future."
            $ camila.love -= 2
            $ camila.sub += 1
            $ camila.flags.haircut = False
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    return

label camila_event_07:
    if camila.love.max < 140:
        $ camila.love.max = 140
    scene bg policestation
    "I must have been bugging Camila about it for weeks now, asking her every chance I get."
    "At first I think she said no just because she hadn't gotten to know me well enough yet."
    "And then it was probably because she thought that I might not be able to handle it."
    "But I guess now she's decided that I am actually tough enough to take on a ridealong."
    "Either that or she's just plain run out of decent excuses to put it off!"
    scene bg alley night summer at center, zoomAt(2.5, (1600, 1240)), dark, blur(5) with fade
    play sound car_door
    "Whatever the reason, super excited to be climbing into the squad car alongside her tonight."
    "That and more than a little nervous to see the seedy underbelly of the town first-hand!"
    show camila a work annoyed at center, zoomAt(2.0, (940, 1340)) with fade
    play sound car_door
    "I recognise the face that Camila pulls the moment she climbs into the driver's seat."
    "It's one of resignation, and maybe more than a little resentment at me cramping her style."
    "But she does her best to bury it and put on a happy face."
    "After all, she could have turned me down flat."
    "So it's really her own fault that she's having to do this..."
    show camila normal
    camila.say "Okay, [hero.name], let's set some ground-rules."
    mike.say "Erm, sure thing, Camila."
    camila.say "You're not here as my partner or some kind of special deputy."
    camila.say "You're a civilian that's here to observe, not interfere."
    show camila angry
    camila.say "That means you don't touch anything inside of the cruiser."
    camila.say "And you stay inside of it unless I tell you otherwise."
    show fx question at right
    camila.say "You got all of that, huh?"
    "I nod eagerly, trying to show that I'm on the same page as Camila."
    mike.say "You got it, Camila."
    mike.say "You won't even know I'm here, honest!"
    show camila normal
    show fx exclamation at right
    camila.say "I'd better not!"
    camila.say "And one more thing."
    camila.say "You can talk all you like while we're driving."
    camila.say "But if I get on the radio or we have to stop and deal with something..."
    camila.say "Well, you button your lip and keep quiet."
    "I nod again."
    "And then Camila nods herself."
    camila.say "Okay, here we go."
    "Coming from anyone else, that little lecture might have made me feel threatened."
    "But hearing it from Camila, somehow the effect is very different indeed."
    "All it does is make me feel like she's doing all she can to keep me safe."
    "It's like I've come to accept that she's the one that's the tougher of the two of us."
    "And it really doesn't seem to bother me at all."
    play sound car_ignition
    "Camila turns the key and starts the engine of the squad car."
    scene bg street at dark
    show camila a work at center, zoomAt(2.0, (940, 1340))
    with fade
    "She pulls out of the precinct car park and into traffic."
    "And just like that, I'm riding along with an actual cop on patrol."
    "I know it shouldn't matter, as this is the twenty first century and all that."
    "But it's that much better because the cop is a seriously hot girl too!"
    "Right from the start I can see how people react as soon as they see the patrol car approach."
    "All eyes are on us, everyone suddenly aware of the need to be on their very best behaviour."
    "And Camila rides through all of it, like a queen surveying her domain as she passes."
    "I can't help looking at her in much the same way, impressed by her air of authority."
    "Camila glances over when we stop at an intersection, noticing my keen interest."
    "She rolls her eyes and shakes her head, trying to dismiss my obvious admiration."
    "But I can see that underneath it all, she's loving the way I'm looking at her!"
    show camila a work angry
    show fx question at right
    camila.say "What?"
    camila.say "Why in the hell are you looking at me like that?!?"
    mike.say "I can't help it, Camila."
    mike.say "It's like you're Judge Dredd, or Robocop, or something!"
    mike.say "This is so cool!"
    show camila normal
    camila.say "Thanks, I think..."
    camila.say "You know police work isn't all that glamorous, [hero.name]."
    camila.say "It can be pretty boring at times, and then there's the paperwork too!"
    mike.say "But being out on the streets like this - that's fun, right?"
    camila.say "Yeah, you got me there."
    camila.say "This is the best part of the job."
    camila.say "And that's because this is where the action happens!"
    "Which is the precise opposite of what happens as we drive around town."
    "I don't know if this is a particularly quiet night or not."
    "But all we do is cruise from one place to another without incident."
    "The only time that we stop, apart from for the lights, is so Camila can chat to a familiar face."
    "And then I keep my mouth shut, like I was told to."
    scene bg street at dark
    show camila a work at center, zoomAt(2.0, (940, 1340))
    with fade
    "It's only when I see that we're getting closer to the precinct where we started that I speak up."
    "Because I'm guessing that we're coming to the end of my ridealong."
    "And I haven't seen any action at all!"
    mike.say "Ah, Camila..."
    show camila a work
    camila.say "Hmm..."
    camila.say "What's up, [hero.name]?"
    mike.say "Be honest, okay - have you been sticking to safe places this whole time?"
    mike.say "I mean, you said it could be boring."
    mike.say "But we haven't even seen as much as a single jay-walker!"
    show camila a happy
    camila.say "Well, I MIGHT have avoided a couple of the worse neighbourhoods..."
    mike.say "Aw, Camila!"
    camila.say "Okay, okay, fine - if that's what you want."
    camila.say "We'll take a detour just up here."
    camila.say "There's a backstreet where some low lives like to hang out."
    camila.say "But all we're gonna do is drive past and put the wind up them."
    "I nod eagerly, happy to be getting even such a small slice of action before the night ends."
    scene bg alley at dark
    show camila a work at center, zoomAt(2.0, (940, 1340))
    with fade
    "As good as her word, Camila takes a turn and soon we're creeping down a shady-looking street."
    "Almost everyone we see eyes the squad car in a shifty manner or slinks away down an alley as we pass."
    show camila a work
    camila.say "Geez, will you look at these scumbags!"
    camila.say "Worthless, every last one of them."
    "She points to a group of scantily-clad girls standing on a street corner."
    camila.say "And they're some of the worst."
    camila.say "Like that bottom-feeding, trash-bag ho, right there!"
    "I follow her as she points out the subject of her particular disapproval."
    "And as soon as I see the girl she means, my eyes almost pop out of my head."
    scene bg alley
    show lexi casual
    with fade
    if game.flags.lexiStart:
        "It's Lexi!"
        "Of course, it HAD to be Lexi, didn't it!"
        "I turn my head away, hoping that she didn't see me."
        show fx exclamation
        lexi.say "[hero.name]!"
        lexi.say "[hero.name], is that you?!?"
        "Lexi hollers at the squad car from the kerb, waving her arms in the air as she does so."
        "I hear Camila snigger in the seat beside me, and I wish the ground would swallow me up!"
        show fx question
        camila.say "You know that girl, huh?"
        camila.say "Because she sure as hell seems to think she knows you!"
        menu:
            "It's Lexi":
                mike.say "I do know her as a matter of fact, Camila."
                mike.say "And she has a name too - she's called 'Lexi'."
                "Seemingly surprised by the admission, Camila slows the squad car."
                show lexi at center, zoomAt (1.5, (640, 940))
                "This means that Lexi catches up to us a few seconds later."
                "She taps on the window and then makes a motion for me to roll it down."
                "I turn to Camila and raise my eyebrows."
                "And still a little stunned, she nods and presses the button to wind down my window."
                show lexi happy
                lexi.say "Hey, [hero.name]!"
                lexi.say "Did you get busted, or what?"
                mike.say "No, Lexi, it's not like that!"
                mike.say "Camila here's a friend and she's taking me on a ridealong."
                show lexi bubblegum
                "Lexi raises her eyebrows and blows a bubble with her gum."
                "When it pops, she sucks the whole lot back into her mouth."
                show lexi surprised
                lexi.say "Wow, [hero.name]!"
                lexi.say "I wish I had friends on the force!"
                lexi.say "You know, maybe she could help me out?"
                lexi.say "I got a couple of outstanding..."
                scene bg alley at dark
                show camila annoyed a work at center, zoomAt(2.0, (940, 1340))
                camila.say "Ah..."
                camila.say "Is that the time?!?"
                camila.say "We really need to be getting back to the precinct."
                "With that, Camila rolls up the window and we pull away from the curb."
                "Lexi stands up and walks backwards with practiced ease."
                "The last I see of her as we turn a corner, she's blowing a kiss in our direction."
                show camila normal
                camila.say "You never told me you knew street people, [hero.name]."
                mike.say "What...you mean Lexi?"
                mike.say "She's actually quite nice when you get to know her."
                camila.say "I'll take your word for that..."
                "Camila falls silent for a minute or two."
                "But then she speaks up in a less forceful tone."
                "One that makes her sound almost vulnerable for the first time tonight."
                camila.say "You said I was a friend back there."
                show camila annoyed
                camila.say "Not that I was your girlfriend or that we were on a date."
                "Wait a minute, is she..."
                "Is Camila actually jealous of my relationship with Lexi?!?"
                mike.say "I just didn't think she needed to know stuff like that, Camila."
                mike.say "You know, as you're a cop and she's a...a..."
                show fx question at right
                camila.say "A street person?"
                mike.say "Yeah, Camila, that's it."
            "I don't know her":
                mike.say "NO!"
                mike.say "I mean...no, of course not!"
                mike.say "She must have mistaken me for someone else."
                scene bg alley at dark
                show camila a annoyed work at center, zoomAt(2.0, (940, 1340))
                "Camila sniggers again, clearly enjoying seeing me squirm."
                "For a long, torturous moment, I think that she's actually going to stop beside Lexi."
                "But then she puts her foot down and the squad car picks up speed."
                "In a mere matter of second, we leave Lexi far behind us."
    else:
        "Because sure, Camila's right in terms of how the girl is dressed."
        "And she's definitely hanging around on a street corner like a pro."
        "But there's no denying the fact that she's also smoking hot!"
        show fx exclamation
        lexi.say "Officer Camila!"
        lexi.say "Hey, Camila, is that you?!?"
        "Lexi hollers at the squad car from the kerb, waving her arms in the air as she does so."
        "I hear Camila snigger in the seat beside me."
        "Which I guess is fine for her, because she's a big, tough cop."
        "But I have no idea how I'm supposed to behave right now!"
        show fx question
        camila.say "Don't worry, [hero.name]..."
        camila.say "I know this girl from way back."
        camila.say "Her name's Lexi, or at least she claims it is!"
        camila.say "And I know how to handle her too."
        "Camila slows the squad car."
        show lexi at center, zoomAt (1.5, (640, 940))
        "This means that the girl catches up to us a few seconds later."
        "She taps on the window and then makes a motion for me to roll it down."
        "I turn to Camila and raise my eyebrows."
        "And with a wicked smile, she presses the button to wind down my window."
        show lexi happy
        lexi.say "Hey, you're not a cop!"
        lexi.say "Did you get busted, or what?"
        mike.say "No, it's not like that!"
        mike.say "Camila here's a friend and she's taking me on a ridealong."
        show lexi bubblegum
        "The girl raises her eyebrows and blows a bubble with her gum."
        "When it pops, she sucks the whole lot back into her mouth."
        show lexi surprised
        lexi.say "Wow, fella!"
        lexi.say "I wish I had friends on the force!"
        lexi.say "You know, maybe she could help me out too?"
        lexi.say "I got a couple of outstanding..."
        scene bg alley at dark
        show camila annoyed a work at center, zoomAt(2.0, (940, 1340))
        camila.say "Ah..."
        camila.say "Is that the time?!?"
        camila.say "We really need to be getting back to the precinct."
        "With that, Camila rolls up the window and we pull away from the curb."
        "The girl stands up and walks backwards with practiced ease."
        "The last I see of her as we turn a corner, she's blowing a kiss in our direction."
        show camila normal
        camila.say "You never told me you liked street girls, [hero.name]."
        mike.say "What...you mean Lexi back there?"
        mike.say "She's probably quite nice when you get to know her."
        camila.say "I'll take your word for that..."
        "Camila falls silent for a minute or two."
        "But then she speaks up in a less forceful tone."
        "One that makes her sound almost vulnerable for the first time tonight."
        camila.say "You said I was a friend back there."
        show camila annoyed
        camila.say "Not that I was your girlfriend or that we were on a date."
        "Wait a minute, is she..."
        "Is Camila actually jealous of my talking with Lexi?"
        "And me not mentioning that we're an item to her?!?"
        mike.say "I just didn't think she needed to know stuff like that, Camila."
        mike.say "You know, as you're a cop and she's a...a..."
        show fx question at right
        camila.say "A street person?"
        mike.say "Yeah, Camila, that's it."
    "All too soon we're pulling back into the precinct car park."
    scene bg policestation with fade
    "I climb out of the squad car feeling glad to be getting back to civilian life."
    "And I'm more than sure I could never do what Camila does on a daily basis!"
    $ game.pass_time(4, True)
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    return

label camila_event_08:
    play sound cell_vibrate loop
    "I'm distracted from what I was doing by the sound of my phone ringing."
    "Only half paying attention, I pull it out and look at the caller ID."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Camila")
    if not result:
        $ hero.cancel_event()
        $ camila.love -= 5
        return
    "But when I see that it's Camila calling, I snap out of it and pay attention."
    "That's partly because I'm always eager to talk to my hot, cop girlfriend."
    "But it's also because I was sure Camila told me she was on duty today."
    "And she doesn't usually call me until her shift ends, as she's too busy."
    "Who knows, maybe she got off early today?"
    "And she wants to hook up to burn off some of her stress!"
    mike.say "Hey, Camila..."
    mike.say "Didn't expect a call from you just yet!"
    mike.say "What's up?"
    camila.say "H...hey...[hero.name]..."
    camila.say "Ah...urgh..."
    camila.say "Ah shit...."
    "Camila seems to be having trouble getting her words out."
    "She's not slurring them or failing to make sense."
    "It's more like she's distracted by something."
    "And the sounds she's making are pretty weird too."
    "Like somebody struggling to move a piece of heavy furniture."
    mike.say "Are you okay, Camila?"
    mike.say "Because you don't sound like you're okay!"
    "My voice is starting to get higher and higher."
    "And that's because panic is creeping over me."
    camila.say "Yeah, yeah..."
    camila.say "I'm fine, [hero.name]..."
    camila.say "I just..."
    camila.say "I just ran into a little...trouble on patrol today, that's all!"
    "Suddenly my mind is filled with terrible images."
    "I can't help thinking of every single danger a cop faces on the beat."
    "And I see them all happening to Camila in grotesque detail."
    mike.say "Oh shit!"
    mike.say "Camila..."
    mike.say "What aren't you telling me?"
    mike.say "What's happened to you?!?"
    "I hear Camila let out a irritated grunt on the other end of the line."
    "Like my wittering down the phone is causing her physical discomfort."
    "Almost as much as whatever's actually happened to her is at the same time."
    camila.say "Geez, [hero.name]..."
    camila.say "Will you calm the hell down?"
    camila.say "I was the one that got my ass shot, not you!"
    mike.say "SHOT?!?"
    mike.say "You've been shot?!?"
    mike.say "Fucking Christ, Camila!"
    mike.say "Where are you right now?"
    mike.say "Don't worry - I'm coming to save you!"
    "Camila lets out a sniggering laugh at this."
    "But then she pays for it with a cry of genuine pain."
    camila.say "Ah...shit..."
    camila.say "Look, [hero.name]...I appreciate the offer, really I do!"
    camila.say "But they already brought me to the hospital."
    camila.say "I'm just waiting for the doctors to stitch me up."
    camila.say "Other than that I'm fine, okay?"
    mike.say "Oh..."
    mike.say "I see..."
    mike.say "So why did you call me?"
    "There's a pause on the other end of the line."
    "Almost like the question has thrown Camila for a moment."
    "I wait patiently for her to recover and offer an answer."
    camila.say "Well..."
    camila.say "They said I should call someone, yeah?"
    camila.say "Let my loved ones know what happened."
    camila.say "And...you were the only person I could think of..."
    camila.say "Actually, you were the first person I thought of!"
    "That admission hits me out of the blue."
    "And now it's my turn to be stunned into silence."
    camila.say "[hero.name]?"
    camila.say "Are you still there?"
    mike.say "Yeah, Camila, yeah!"
    mike.say "I'm still here - don't worry about that!"
    mike.say "So...when can I come over there and see you?"
    "Camila fills me in on the details."
    "Then, armed with the name of the hospital and the visiting hours, I set out to see her."
    "But all the time I'm worried about what kind of state I'll find her in."
    "She might be tough as nails, but Camila's got a habit of playing things down."
    "So I can't exactly trust her when she says that she's fine."
    $ camila.flags.camiladelay = TemporaryFlag(True, 1)
    $ camila.flags.schedule = "hospital"
    $ hero.calendar.find_and_remove(girl="camila")
    return

label camila_event_09:
    if camila.love.max < 160:
        $ camila.love.max = 160
    scene bg hospital
    "I hurry over to the hospital, arriving as soon as I can and in a state of serious agitation."
    "Luckily for me there's a small shop inside the entrance selling flowers and the like."
    "So I take a quick detour in there to grab a small bouquet and some fruit for Camila."
    "While I'm doing this, I manage to get my emotions a little more under control."
    "This means that as I make my way to the ward where she's on, I'm much calmer than before."
    show camila hospital with fade
    "But the moment I turn the corner and actually see Camila in the hospital bed..."
    "Well, most of that panic comes flooding right back again!"
    mike.say "Camila!"
    mike.say "There you are!"
    mike.say "Did they fix you up yet?"
    mike.say "Are you going to be okay?!?"
    "Camila turns to see me standing by her bed."
    "She rolls her eyes and shakes her head at me."
    show camila hospital smile
    "But I can see the smile tugging at the corner of her mouth."
    "And that lets me know that she's actually pretty pleased to see me."
    camila.say "Oh great, the drama queen's here!"
    camila.say "Hey, [hero.name]..."
    "Camila gestures to herself as she's laid on the bed."
    camila.say "Here I am, see?"
    camila.say "All of me in the same place and in one piece!"
    camila.say "So sit your ass down and stop fretting, okay?"
    "I nod and do as I'm told, trying to look reassured."
    show camila hospital -smile
    "But for all of Camila's bravado, she can't cover up what's plain to see."
    "Sure, she's whole and looks like there's no permanent damage been done to her."
    "But she has a drip hooked up to her arm, and she's visibly paler than usual."
    "Plus every time she moves, she winces in pain, cursing under her breath."
    mike.say "I...erm..."
    mike.say "I brought you some flowers..."
    mike.say "And some fruit too!"
    "Camila nods towards the cabinet at the side of her bed."
    "The effort costs her another wince of pain."
    "But she covers it up with more snarky comments."
    camila.say "Yeah, I saw."
    camila.say "Classic remedy for a gunshot wound!"
    camila.say "Just stick them over there, okay?"
    "I do as I'm told and then sit down next to Camila's bed."
    "It's only now that she seems to actually notice the look on my face."
    "Camila's good at reading people, as a cop she has to be."
    "And as soon as she realises that my concern is genuine, she changes her tune."
    "The tough cop act slips and her own expression softens noticeably."
    camila.say "Ah shit..."
    camila.say "Look, [hero.name]...I'm sorry, okay?"
    camila.say "I just don't like people fussing over me, that's all!"
    camila.say "Plus...it was kinda my fault that I ended up in here..."
    "Now she's perked my interest!"
    "I lean forwards, keen to hear more."
    "And for the first time, I feel my fears easing a little."
    "If Camila's well enough to feel guilty for being rude, then she must be okay."
    "Because I know how much effort it takes her to pull her head out of her ass!"
    mike.say "Oh yeah?"
    mike.say "What happened, Camila?"
    show camila hospital smile
    camila.say "Well..."
    camila.say "You promise to keep this to yourself?"
    mike.say "I promise, Camila - on my life!"
    camila.say "Okay, okay..."
    camila.say "I turned my back on a guy we were busting."
    camila.say "Just for a split second, right?"
    camila.say "And he shot me - the bastard shot me!"
    mike.say "So he shot you...in the back?"
    "At this, I see Camila's cheeks flushing red."
    "She looks away from me, not able to meet my eye."
    camila.say "No, [hero.name]..."
    camila.say "Not exactly..."
    "I look Camila up and down, searching for a wound."
    "I can't see one anywhere on her body, no matter how hard I try."
    mike.say "In the arm then?"
    mike.say "Or the leg?"
    "I follow Camila's eyes down to where she's sitting on the bed."
    "And it's only now that I realise there are a few cushions under her."
    mike.say "You're not serious?"
    mike.say "Are you, Camila?"
    camila.say "Yeah, [hero.name] - I am!"
    show camila hospital -smile
    camila.say "The bastard shot me in the ass!"
    "I splutter out a laugh a moment later."
    "Then instantly I put a hand over my mouth."
    mike.say "Oh shit..."
    mike.say "Oh, Camila..."
    mike.say "I'm SO sorry!"
    mike.say "That's terrible...I shouldn't be laughing."
    "Camila frowns for a moment, but then I see her break."
    show camila hospital smile
    "She shakes her head as she starts to laugh too."
    "And in a few moments, she's totally gone, laughing like a fool."
    camila.say "Yeah...I know!"
    camila.say "So why are we both laughing?!?"
    mike.say "But...you're going to be okay, right?"
    mike.say "Like...your butt will make a full recovery?"
    camila.say "Yes, [hero.name], it will!"
    camila.say "It might be a little scarred."
    camila.say "But it'll be back in full working order again!"
    "We spend the rest of visiting time chatting and joking."
    "And by the time I have to leave, Camila seems to be back to her old self."
    $ camila.love += 4
    hide camila with fade
    "I promise to come back the next day, and then I walk out of the hospital."
    "All the time I'm thinking - how am I going to explain this to anyone that asks?!?"
    "And I'm wondering what the scar on Camila's ass is going to look like too..."
    $ camila.flags.hospitaldelay = TemporaryFlag("hospital", 5, hook=[hook_set_flag, {"girl": camila, "flag": "schedule", "value": "default"}])
    return

label camila_event_10:
    if camila.love.max < 180:
        $ camila.love.max = 180
    scene bg cinema
    show camila normal
    with fade
    "I've promised Camila a trip to the cinema for our date tonight, and I've also sweetened the deal."
    "Well, at least I THOUGHT, I'd sweetened the deal with my subtle choice of the film we're seeing."
    "But the moment that we walk into the lobby and I point out the paster, she doesn't seem impressed."
    mike.say "Ta dah!"
    mike.say "'Mechacop Two - Cyborgs on Patrol'!"
    show camila weird
    show fx question
    camila.say "Mechawhat?!?"
    camila.say "I thought you said we were seeing a cop movie?"
    hide fx
    "I look at the poster and then back at Camila."
    "And all the time I'm trying not to look as confused as I feel right now."
    mike.say "But, but, but..."
    mike.say "Camila...this IS a cop movie!"
    mike.say "It's just that the cop happens to be a cutting-edge cyborg too!"
    show camila annoyed
    "Camila shakes her head at me."
    camila.say "[hero.name]!"
    camila.say "It's a nerd movie, and you know it!"
    camila.say "You promised me some hard-boiled action!"
    camila.say "Not shitty special effects and a guy wrapped up in tinfoil!"
    "I feel seriously wounded by Camila's total rejection of my choice."
    "Doesn't she know that this is the long awaited sequel to a genre classic?"
    "I thought everyone had heard of Mechacop?!?"
    mike.say "It's both, Camila!"
    mike.say "It's a cop movie AND a nerd movie..."
    mike.say "Sci-fi movie...I meant sci-fi movie!"
    mike.say "It's a cop movie and a sci-fi movie!"
    "Camila looks less than convinced my efforts to explain myself."
    show camila bored
    "She shrugs and then holds her hands up in a gesture of surrender."
    camila.say "Whatever, [hero.name]!"
    camila.say "I'm beat after my shift today."
    camila.say "I don't have the energy to argue!"
    show camila annoyed
    camila.say "But if this movie's the shits, then I'm out of here!"
    "That's as good as it's going to get."
    "So I just nod and hurry Camila into the theatre."
    scene bg cinemaroom with fade
    "Soon enough we're sitting down to watch the trailers."
    "I'm not kidding when I say that I've been looking forward to this film."
    "I really think the original is a classic, and I can't wait for the sequel."
    "But knowing that Camila's seriously not into it is a drag on the whole thing."
    "Part of me wants to say screw it and take her someplace else."
    "But we're here now, and she's promised to give it a shot."
    scene camila cinema bj with fade
    "Once the movie actually starts playing, I'm instantly hooked."
    "It's not as good as the original - it's even better!"
    "I'm totally transported into a world of sci-fi goodness!"
    "But the first time I sneak a sideways glance at Camila, my spirits sink."
    "She looks like she's being forced to watch paint dry!"
    "I lean over and whisper to her."
    mike.say "Camila..."
    mike.say "You're not feeling it?"
    camila.say "No, I'm not!"
    camila.say "This movie's dumb!"
    camila.say "The plot is crap."
    camila.say "And all the cops are one-dimensional characters that reinforce negative stereotypes in law enforcement!"
    mike.say "Whoa..."
    mike.say "That's a surprisingly insightful critique!"
    camila.say "But you're loving it, I can see that."
    camila.say "So I'm just going to have to make my own fun..."
    "I look at Camila in confusion, not knowing what she means."
    "And she smiles back at me, then begins to slide out of her seat."
    "Like a supple snake, she slithers onto the floor of our row."
    "Then she rears up in front of me, putting her hands on my thighs."
    "Suddenly I can't concentrate on the movie, only on Camila."
    "She grins as she starts to open my flies, putting a finger to her lips as she does so."
    "What in the hell does she think?"
    "That I'm going to shout for her to stop in the middle of a crowded theatre?"
    "That I'd interrupt the film by telling her to get the hell off my cock?!?"
    "Of course, Camila's well aware of all this."
    "That's why she has a huge grin on her face as she pulls it out of my pants."
    "She gives me one last casual glance, biting her lip for effect."
    "And then she opens her mouth and puts it to use down there."
    show camila cinema bj blow
    "Now lets get one thing straight, Camila's not a professional when it comes to these kind of things."
    "I know for a fact that you could find a lot of girls that are smoother at giving a guy a blowjob."
    "But that's one of the things that makes getting one from Camila so memorable."
    "She goes on instinct, doing whatever feels good to her in the moment."
    "And she pays attention to the effect she's having on me too."
    "What this means is that oral from her is instinctive and honest."
    "And it feels pretty fucking incredible, I can tell you!"
    show camila cinema bj blow mikepleasure
    "I do the best I can to keep watching the film as Camila goes down on me."
    "The place is dark and she's on the floor, so all I have to do is keep quiet."
    "But that proves harder than you might think thanks to her enthusiasm."
    show sexinserts head camila zorder 1 at center, zoomAt(1, (720, 910))
    "I can feel Camila kissing and licking around the base of my cock."
    "Her tongue and lips begin to climb it, but they go slowly and with intent."
    "I can feel every fraction of an inch as she progresses upwards."
    "So by the time she reaches the head, I'm clinging onto the arms of my seat."
    "Camila teases swallowing it, once, then twice."
    "Luckily for me, she actually does it right as a jump-scare hits!"
    mike.say "OH FUCK!"
    "My helpless cry is covered up and hidden by everyone else in the theatre screaming too."
    "A ripple of nervous laughter follows the screams, but Camila's still not done."
    "Her head is going up and down in my lap, her thick black hair falling down around it."
    "My cock is almost hitting the back of her throat as she does this."
    "It feels amazing, and Camila shows no signs of gagging either."
    "If anything, she's actually picking up speed!"
    "She's grunting with the effort, really putting some force into it."
    "I guess this is her way of relieving some of the stress she had to deal with."
    "It's like I'm being used to blow off the hassle she faces on the means streets."
    "The thought's pretty thrilling, and it makes me excited too."
    "So much so that I can feel myself starting to cum!"
    "Thankfully, Camila senses it too."
    "And she acts before it's too late."
    show camila cinema bj blow cum
    show sexinserts head camila zorder 1 at center, zoomAt(1, (720, 910))
    with vpunch
    $ camila.love += 1
    $ camila.sub += 1
    "Easing back a little, she eagerly swallows everything I have to give."
    with vpunch
    "Once it's over, she puts my cock away and slithers back to her seat."
    hide sexinserts
    scene camila cinema bj
    "We watch the rest of the movie in silence."
    "I'm enjoying a great film with the buzz of a blowjob on top of it."
    "And Camila seems to have calmed herself down by giving the same."
    "When it's done she takes my arm and lets me lead her out of the theatre."
    scene bg cinema
    show camila normal
    with fade
    mike.say "Camila..."
    mike.say "Did you take in any of that film?"
    camila.say "Nah...I can't say that I did."
    show camila blush
    camila.say "Maybe we can watch it again when they stream it?"
    camila.say "I'll be hungry for another dive into your pants by then!"
    return

label camila_event_11:
    if camila.love.max < 200:
        $ camila.love.max = 200
    show camila normal
    "I can tell that Camila has something on her mind from the very first moment that I see her."
    "Normally she's this tough, brusque cop that takes no shit and says whatever's on her mind."
    "But today, Camila seems quiet, almost like she's scared of saying too much for some reason."
    "At first it throws me, but then I remember something that I've observed about her in the past."
    "Sometimes, Camila can be weirdly like a stereotypical guy when it comes to her emotions."
    "What I mean is that she's like one of those guys that always acts tough and hides his true feelings."
    "So I try to read all the signals that she's giving out with that in mind."
    "Figuring how I'd interpret all of this if she were one of those types of guy."
    "And then it hits me - she's being quiet simply because she's got something to say."
    "It's the classic case of a normally out-spoken person clamming up for that very reason!"
    show camila at center, zoomAt(1.5, (640, 1040))
    mike.say "Camila..."
    mike.say "You're being kind of quiet today!"
    show camila blush
    show fx exclamation
    "The moment I say this, Camila comes over all defensive."
    "She shakes her head and crosses her arms over her chest."
    camila.say "What are you talking about, [hero.name]?"
    camila.say "I'm not being quiet...you are!"
    hide fx
    "As soon as the words are out of her mouth, Camila winces."
    "It's like she's finally hearing herself speaking, realising how she actually sounds."
    show camila bored
    camila.say "Ah, fuck..."
    camila.say "Why am I no good at this kind of thing?"
    camila.say "I can play good cop/bad cop all day long!"
    show camila happy
    camila.say "But with you...no chance!"
    "I can't help smiling at Camila's honest outburst."
    "It's just like her, passionate and straight down the line."
    "And it makes me feel that pang in my stomach that I associate with her."
    "I just love that about her, because it makes her so special."
    mike.say "Don't beat yourself up, Camila."
    mike.say "Just say what you have to say to me."
    mike.say "If it's affecting you that much, it must be important, right?"
    show camila normal
    "Camila nods, setting her mouth into a grim smile."
    "And for a moment I wonder if I've done the right thing here."
    "What if I don't like the sound of what she has to say?"
    "Well, then I'll just have to deal with the fallout, I guess!"
    camila.say "The thing is, [hero.name]..."
    camila.say "I was thinking about us - about me being on the force."
    "I frown at this, a little confused."
    mike.say "I thought we discussed this already, Camila?"
    mike.say "Didn't we decide that I'm not intimidated by you being a big tough cop?"
    mike.say "You know that I'm not that kind of meat-headed guy!"
    camila.say "Yeah, yeah - I know all that."
    camila.say "But I took a bullet on duty recently."
    camila.say "And that kind of thing really makes you think."
    show camila annoyed
    camila.say "It makes you weigh things up, you know?"
    "Honestly I don't."
    "I have no idea what being shot would actually be like."
    "All I have to go on is movies, TV and videogames!"
    "But I make a point of nodding anyway."
    mike.say "Yeah, Camila..."
    mike.say "I guess so!"
    show camila normal
    camila.say "And I got to thinking about us, [hero.name]."
    show camila weird
    camila.say "I...I love you, [hero.name] - I mean that!"
    "The admission comes out of the blue."
    "And it catches me a little off-guard."
    mike.say "I love you too, Camila!"
    show camila normal
    camila.say "Yeah, yeah..."
    camila.say "And that's why I want to ask if you can REALLY handle what I do?"
    show camila sad
    camila.say "Can you handle it if I get hurt real bad, or even killed out there?"
    camila.say "Because if the first one happens, then I'm gonna need you real bad!"
    camila.say "And if the second one happens, then...then I won't be around when you need me!"
    "I feel the weight of the question hit me as Camila stares into my eyes."
    "I mean, it's pretty heavy to begin with, and she's asking it with real passion."
    "But there's something in those eyes too, a genuine pleading need."
    "And that means I know that Camila's serious about this."
    "That she's terrified of what might happen down the line."
    mike.say "I know what you do is scary, Camila."
    mike.say "And I know that the dangers are real."
    mike.say "But I won't let them scare me away from you."
    mike.say "Whatever happens out there, I'll be with you - one hundred percent."
    mike.say "And if the worst does happen..."
    mike.say "Well, then I'll have been taught how to be brave by the bravest person I know!"
    show camila flirt
    "Camila doesn't burst into tears and throw her arms around me like any other girl would."
    "And that's because she's not any other girl, she's totally unique - a one-off."
    "She curls her mouth into a knowing smile and gives me a dirty chuckle."
    $ camila.love += 5
    camila.say "You better be as good as your word!"
    camila.say "You hear me?"
    hide camila
    show camila kiss
    with fade
    $ camila.flags.kiss += 1
    "She comes into my arms then, pulling me close with a sudden jerk."
    "But she knows that I like it, those little shows of dominance."
    "And when she we kiss, it's us meeting as equals in love and desire."
    "Because I meant every word I said - she's totally worth the risk that comes with her!"
    return

label camila_sub_event_01:
    if camila.sub.max < 50:
        $ camila.sub.max = 50
    show camila happy
    "Camila's been buzzing ever since we met up today, like she's high on life or something."
    "And don't get me wrong, there's nothing up with that - it's fun when she's fun!"
    "But I'm kind of more used to the Camila that I've grown to know and love."
    "You know, the tough, maybe even cynical cop that's too streetwise to miss a trick."
    "I just keep wondering what it is that's making her so upbeat all of a sudden."
    show camila at center, zoomAt(1.5, (640, 1040))
    mike.say "Camila..."
    show camila wink
    camila.say "Yeah, [hero.name]?"
    mike.say "Did you bust some big bad guy?"
    mike.say "Or get a promotion?"
    mike.say "Maybe win a cop medal or something like that?"
    show camila normal
    "Camila shoots me a sideways look."
    "Which instantly gives away the fact that she's suspicious."
    show fx question
    camila.say "A cop medal?"
    camila.say "What's that supposed to mean?!?"
    hide fx
    "I shrug, starting to feel a little bit silly."
    mike.say "I dunno, Camila!"
    mike.say "You just seem unusually care-free today, that's all!"
    show camila bored
    camila.say "Huh?!?"
    camila.say "I can be care-free!"
    show camila happy
    camila.say "What makes you think I can't be care-free?!?"
    "I'm staring at her with a smile on her face as she says all of this."
    "And with each new word out of her mouth, my eyebrows rise ever higher."
    "In the end, Camila stops talking and lets out a sigh of frustration."
    show camila weird
    camila.say "It's not working, is it?"
    camila.say "Fuck!"
    show camila bored
    camila.say "Why can't I lie to you?"
    camila.say "God knows I try!"
    show camila weird
    camila.say "But when you look at me like that - urgh!"
    "Camila throws her hands up in frustration."
    camila.say "It's like...like you're my Kryptonite or something!"
    mike.say "Wow, Camila!"
    mike.say "That was a geek reference right there!"
    camila.say "You see what I mean?!?"
    camila.say "Being around you, it messes with me!"
    show camila normal
    camila.say "But...in a kind of a good way..."
    camila.say "So I'll just come out and say it."
    camila.say "I can't stop thinking about what we did the other night."
    camila.say "About how you put those hand-cuffs on me!"
    "All it takes is the mere mention of that incident."
    "Just that and I'm right back in the room."
    "Camila's right, that was a hell of a night!"
    mike.say "Yeah, Camila..."
    mike.say "That was a lot of fun!"
    show camila blush
    "I see Camila flush a little."
    "Like she's embarrassed to admit to her feelings."
    mike.say "What's the matter?"
    mike.say "There's nothing to be ashamed of, Camila!"
    mike.say "These days that kind of thing is pretty normal."
    mike.say "You kind of expect most people to have at least a little kink!"
    camila.say "Yeah, yeah...everyone's a pervert - whatever!"
    camila.say "It's different when you're a cop."
    camila.say "Can you imagine what they say down at the precinct if they ever found out?"
    mike.say "So..."
    mike.say "What you're saying is that you DON'T want to do it again?"
    show camila angry at center, zoomAt(1.0, (640, 1040)), vshake
    camila.say "HELL NO!"
    show camila blush
    camila.say "I...I mean I DO want you to use the cuffs on me again - and soon!"
    show camila annoyed
    camila.say "I just need you to keep it a secret, okay?"
    "I nod as firmly as I can manage."
    mike.say "Okay, Camila."
    mike.say "My lips are sealed!"
    mike.say "But you know..."
    mike.say "The idea of a kinky cop keeping secrets from other cops..."
    mike.say "That's kind of kinky too!"
    show camila blush
    camila.say "Urgh..."
    camila.say "Just stick to the agreement, okay?"
    mike.say "Ah, okay, Camila!"
    mike.say "Whatever you say..."
    $ game.active_date.score += 15
    return

label camila_sub_event_02:
    if camila.sub.max < 75:
        $ camila.sub.max = 75
    show camila
    "Camila and I are just talking, you know, about everything and nothing all at once."
    "We've already told each other how our respective days went and all the gossip too."
    "Of course Camila's day at work was a lot more exciting than mine, as usual!"
    "And now we're just keeping it going while we think of other stuff to talk about."
    show camila at center, zoomAt(1.5, (640, 1040))
    "That's when Camila nudges me with her elbow and raises any eyebrow."
    show camila normal
    camila.say "Hey, [hero.name]..."
    camila.say "You remember the time I took you out on patrol with me?"
    mike.say "Yeah, Camila..."
    mike.say "Of course I do."
    camila.say "Hmm..."
    camila.say "You had a good time, right?"
    camila.say "I mean, you enjoyed that whole thing?"
    "I'm not sure where Camila's going with this."
    "So I just decide to play along and see what happens."
    mike.say "It was quite a thrill, Camila!"
    mike.say "I'd never been inside a police car before that."
    "I'm not trying to say what Camila wants to hear."
    "It really was exciting to be able to ride along with her."
    "It was pretty scary too - so I was glad to be close at her side the whole time!"
    camila.say "Do you mean you'd never been in the FRONT of a cruiser?"
    show camila flirt
    camila.say "Because a lot of people have ended up in the back of one!"
    "I know that Camila's screwing around with me."
    "The curl of her lip as she smiles gives it away."
    "But all the same, I can't help feeling a little nervous."
    "She is a cop, after all, and she has that effect on people."
    mike.say "I'm a good boy, Camila."
    mike.say "Especially now I have you to keep me in line!"
    show camila happy
    "Camila barks a laugh at this."
    "Then she playfully punches me in the arm."
    "It actually hurts more than a little."
    "But I do my best to ignore the pain and laugh too."
    show camila flirt
    camila.say "Damn right you do!"
    camila.say "Anyway..."
    show camila bored
    camila.say "The reason I mention it is because I've been thinking..."
    "I nod and make an effort to listen to what Camila has to say."
    "Because it sounds like it's going to be something momentous."
    show camila normal
    camila.say "I get a real buzz from driving around in the cruiser, you know?"
    camila.say "I'd never admit it to anyone else, but it's like a power-trip!"
    camila.say "It's almost like being a hunter, stalking the streets for prey!"
    mike.say "I thought you were out there to protect and serve?"
    show camila bored
    camila.say "Yeah, yeah - of course we are!"
    camila.say "This is all fantasy stuff, you get it?"
    show camila normal
    camila.say "Like stuff I always keep to myself."
    camila.say "Like I could pick up a guy and have him totally at my mercy!"
    camila.say "I could make him do whatever the hell I want!"
    "Camila has a fire in her eyes as she tells me all of this."
    show camila blush
    "But then she seems to realise how it must sound."
    "And her expression changes, becoming more than a little embarrassed and ashamed."
    camila.say "I'd never do anything like that - you know?"
    mike.say "Of course not, Camila!"
    mike.say "You're a good cop!"
    show camila normal
    camila.say "But..."
    camila.say "Maybe we could...pretend some time?"
    camila.say "You and me?"
    mike.say "You mean like roleplay?"
    show camila weird
    camila.say "What - like with dice and stuff?!?"
    mike.say "No, like sexual roleplay!"
    show camila normal
    camila.say "Oh..."
    camila.say "I never heard it called that before!"
    show camila flirt
    camila.say "But yeah, something like that!"
    "I'm amazed that it took Camila this long to get to the point."
    "All she wants to do is ask me to fool around with her in a police car!"
    "And that sounds like a great idea to me, a chance for some serious fun."
    mike.say "Yeah, Camila..."
    mike.say "I'm up for that."
    show camila happy
    "Camila practically beams at this."
    "She nods eagerly, smiling at me happily."
    camila.say "Great!"
    camila.say "I'll work something out with the cruiser."
    show camila wink
    camila.say "Then I'll let you know the time and the place..."
    return

label camila_sub_event_03:
    $ renpy.play("sd/cell_vibrate.ogg", "sound")
    $ result = renpy.call_screen("smartphone_choice", "Camila")
    if not result:
        $ hero.cancel_event()
        return
    if camila.sub.max < 100:
        $ camila.sub.max = 100
    "My phone rings, and when I see that the call is from Camila, I instantly pick up."
    mike.say "H...hey, Camila..."
    mike.say "Are you ready to..."
    camila.say "You shut your mouth and listen to me!"
    camila.say "Be outside in exactly one minute, okay?"
    camila.say "And don't make me come in there to you, understand?!?"
    if 'camila_sub_event_03' in DONE:
        "Oh we're doing this again."
        menu:
            "Pass for this time":
                mike.say "Hum, not this time Camila."
                camila.say "Fine! I'll do this by myself!"
                "She ends the call abruptly."
                "I guess I'll have to deal with this later..."
                $ camila.love -= 2
                return
            "On it Officer":
                pass
    mike.say "Y...yeah, Camila..."
    mike.say "I understand!"
    scene expression f"bg {game.room}"
    "Camila ends the call abruptly a moment later."
    "But I'm already scurrying for the front door."
    scene bg house with fade
    "I make it out onto the porch and to the kerb just in time."
    "Because a cop car is screeching to a halt in front of my house as I do so!"
    show camila work annoyed
    "The drivers side window winds down, and Camila leans her head out."
    camila.say "Get in the damn car!"
    "I nod and make to open the back door."
    show camila angry
    camila.say "What the fuck are you doing?!?"
    camila.say "You're riding shotgun, dummy!"
    "Still nodding, I hurry to obey."
    "But I've hardly got the door open and my ass into the seat when Camila begins to pull out."
    play sound car_door
    with hpunch
    "The force of the accelerating car throws me into the seat, and the door slams shut too."
    "I'm still struggling to fasten my seatbelt as we go careering round the nearest corner."
    scene bg street zorder 1 at center, zoomAt (1.25, (640, 480)), dark
    show carpatrol zorder 2 at center, zoomAt(2.0, (440, 1440))
    show camila work annoyed zorder 3 at center, zoomAt(2.0, (940, 1340))
    with fade
    mike.say "Camila!"
    mike.say "What's gotten into you?"
    mike.say "Are you trying to get us both killed?"
    show camila work happy at center, zoomAt(1.0, (940, 1340)), startle
    "Camila laughs and shakes her head, hair bouncing as she does so."
    "It doesn't seem like my words have done a thing to make her slow down."
    show camila bored
    camila.say "You just leave the driving to me, [hero.name]."
    camila.say "I'm the one that took a course in advanced pursuit!"
    camila.say "When I need you to do something, I'll tell you."
    show camila annoyed
    camila.say "Until then, sit back and shut up!"
    "I do as I'm told, clinging onto my seat as Camila continues to drive like a maniac."
    "But it's more from the need to hold onto something than wanting to obey her."
    scene bg alley with fade
    "Soon enough we screech into what looks like an abandoned lot."
    "There's nobody around and we seem to be totally alone out here."
    mike.say "Whoa..."
    mike.say "Am I glad that's over!"
    mike.say "Okay, Camila - how are we going to handle this?"
    scene bg alley zorder 1 at center, zoomAt (1.25, (640, 680)), dark
    show carpatrol zorder 2 at center, zoomAt(2.0, (440, 1440))
    show camila work flirt zorder 3 at center, zoomAt(2.0, (940, 1340))
    with fade
    "I barely have time to turn and look at Camila."
    "And when I do, I note the way she's looking at me."
    "It's like staring at some kind of big cat."
    "One that's hungry and eyeing up it's prey!"
    with vpunch
    "Camila slams a hand onto my chest, pinning me to the seat."
    camila.say "Let's get one thing straight, buddy."
    camila.say "While you're in my cruiser, I'm the one giving the orders!"
    camila.say "You got that?"
    mike.say "Yeah, yeah..."
    mike.say "I got that, Camila!"
    camila.say "That's 'Officer' to you!"
    mike.say "Yes, officer - I mean, yes, officer!"
    show camila at center, zoomAt(2.0, (940, 1240)) with ease
    "Camila keep her hand on my chest as she rises from her seat."
    show camila at center, zoomAt(2.0, (640, 1240)) with ease
    pause 0.1
    show camila at center, zoomAt(2.0, (640, 1340)) with ease
    "She slides over onto the passenger side until she's straddling me."
    camila.say "As of right now, you're under arrest!"
    camila.say "I'm holding you in custody."
    camila.say "And you won't be released until you've served your sentence!"
    "As she's saying all of this, Camila's tugging at my clothes."
    "She's stripping them off as quickly as she can."
    "And at the same time she's being sure to stoke my cock every chance she gets."
    camila.say "Your first punishment is to get this officer out of her uniform."
    show camila wink
    camila.say "So get to it - NOW!"
    show camila flirt
    "I nod and begin trying as best I can to pull off Camila's clothes."
    "She's wriggling atop me the whole time, panting and gasping."
    "Having me touch her like this seems to be making her hotter by the second."
    show camila happy topless with dissolve
    "And as soon as I expose her breasts, she lets out a cry of delight."
    camila.say "Second helping of punishment..."
    show camila flirt
    camila.say "Tend to the officer's needs!"
    "I don't need to be told what to do next."
    "I lean forwards and bury my head between Camila's breasts."
    "Using my lips, tongue and teeth, I go straight to work."
    "She moans at the sensation, pushing her chest forwards."
    "This thrusts Camila's breasts into my face, almost smothering me."
    "But what a way to go!"
    "I don't stop for a moment, instead redoubling my efforts."
    camila.say "Ah..."
    camila.say "Th...third...help...helping..."
    camila.say "Third helping of punishment!"
    scene camila carsex with fade
    "I feel Camila reach down and grab hold of my cock."
    "She's neither subtle nor gentle about it either."
    "Instead she raises herself up and jams it hard against her pussy."
    camila.say "Satisfy the officer..."
    camila.say "Give her what she wants..."
    camila.say "Make her fucking scream for more!"
    "I can feel the head of my cock slipping and sliding against Camila's lips."
    "She's hot and wet down there, her pussy showing just how turned-on she is right now."
    "So far she's been the one in control, setting the pace and ordering me around."
    "But she just demanded that I fuck her, right?"
    "Not that I let her fuck me."
    "And to do that, I have to take back control."
    "I raise my hands and grab a hold of Camila's waist."
    show camila carsex pleasure
    "She instinctively wriggles and writhes in my grasp."
    camila.say "Hey!"
    camila.say "What the hell?!?"
    show camila carsex normal
    camila.say "I'm the one in charge here!"
    "Camila sounds like she's about to chew me out."
    "But her tone changes a moment later."
    show camila carsex ahegao vaginal at startle(0.05,-10)
    "And that's because I pull her downwards without warning."
    camila.say "Ah..."
    camila.say "Oh fuck..."
    show camila carsex pleasure
    camila.say "Mmm...oh yeah...."
    "Camila's so worked up and wet that she can't resist for a second."
    "As soon as my cock presses against her lips, she opens like flower."
    "And then she's sinking down onto me, my cock inching into her."
    show camila carsex at startle(0.05,-10)
    "Camila pants and nods with desperation as I go as deep as I can."
    show camila carsex at startle(0.05,-10)
    "Her weight ensures that she sinks down and I make sure I'm pushing up."
    show camila carsex at startle(0.05,-10)
    "As I begin to thrust into Camila, her entire demeanour changes."
    "I watch as the tough, dominant cop turns into a helpless ball of pleasure."
    show camila carsex at startle(0.05,-10)
    "Where before she was grunting and demanding, now she's cooing and nodding."
    "Camila even seems to be happy to let me set the pace."
    "And so I make a point of taking things slowly."
    "This means that I can enjoy the sensation of being inside her."
    show camila carsex at startle(0.05,-10)
    "And I can make the most of holding her body as she rides my cock."
    show camila carsex at startle(0.05,-10)
    "Camila leans in close, her breath tickling my ear."
    camila.say "I..."
    camila.say "I'm a good girl...right?"
    show camila carsex at startle(0.05,-10)
    camila.say "A good cop?"
    camila.say "Tell me, [hero.name]...tell me I'm good - please?"
    show camila carsex at startle(0.05,-10)
    mike.say "Oh fuck, Camila..."
    mike.say "You're SO good!"
    show camila carsex at startle(0.05,-10)
    mike.say "You're like...the best cop!"
    mike.say "The hottest, sexiest bitch on the force!"
    show camila carsex normal at startle(0.05,-10)
    "As I say all of this, Camila starts to take control again."
    "With every compliment I bestow, she gets more aggressive and assertive."
    show camila carsex at startle(0.05,-10)
    "Pretty soon she's grinding herself into my lap."
    show camila carsex at startle(0.05,-10)
    "Using all of her weight to push my cock deeper still."
    show camila carsex at startle(0.05,-10)
    mike.say "F...fuck..."
    show camila carsex at startle(0.05,-10)
    mike.say "Camila..."
    show camila carsex at startle(0.05,-10)
    mike.say "I'm going to cum!"
    show camila carsex at startle(0.05,-10)
    camila.say "You'd better do..."
    show camila carsex at startle(0.05,-10)
    camila.say "You'd better fill me up..."
    show camila carsex pleasure
    camila.say "Make me cum too!"
    show camila carsex at startle(0.05,-10)
    "I tighten my grip on Camila as I lose it."
    show camila carsex ahegao creampie with vpunch
    "As deep inside of her as I can possibly get, I shoot my load."
    with vpunch
    "She lets out a deep moan of pleasure, burying her head in my shoulder."
    with vpunch
    "At the same time, I can feel her quaking against me, beginning to cum."
    show camila carsex pleasure
    "Camila stays right there, clinging to me the whole time."
    "Our bodies are intertwined, slick with sweat."
    "And I can hear her gasping in my ear, feel her pussy twitching around my cock."
    scene bg alley zorder 1 at center, zoomAt (1.25, (640, 680)), dark
    show carpatrol zorder 2 at center, zoomAt(2.0, (440, 1440))
    show camila work topless flirt zorder 3 at center, zoomAt(2.0, (940, 1340))
    with fade
    "Afterwards, Camila slumps back into her seat."
    "That was so many different kinds of amazing."
    "But I do kind of feel like I was just beat up in a broom cupboard!"
    camila.say "Shit..."
    camila.say "I SO fucking needed that!"
    show camila wink
    camila.say "Thanks, [hero.name] - you really came up with the goods!"
    mike.say "No worries, Camila."
    mike.say "You can arrest me any time!"
    $ game.room = "alley"
    return

label camila_sub_event_04:
    if 'camila_sub_event_04' in DONE:
        "I seems that Camila enjoyed our time together during her foot patrol."
        "In fact shes ask me to come with her again."
        menu:
            "Pass for this time":
                "But I'm not really in the mood for this right now."
                $ camila.love -= 2
                return
            "On it Officer":
                pass
    else:
        scene bg policestation
        show camila normal work
        with fade
        "It feels like it's taken forever for me to convince Camila to let me do this with her."
        "But she's finally relented, and I'm coming along with her on a routine foot patrol."
        "I've been itching to do this since we first started dating, and I'm buzzing with excitement."
        "Though I am doing the best I can to keep a lid on it and trying to look serious."
    "So much so that I think it's pretty obvious I'm about to burst."
    show camila annoyed
    camila.say "You better not be doing that all the time we're out here, [hero.name]!"
    mike.say "Huh?"
    mike.say "Doing what, Camila?"
    mike.say "I have no idea what you mean."
    show camila normal
    camila.say "Oh yes you do."
    camila.say "You've got that dumb, 'I'm a tough guy' look on your face."
    camila.say "I know it well."
    camila.say "Because I have to deal with it every day on the street."
    mike.say "Oh..."
    mike.say "Okay, Camila - I'll be good, I promise."
    camila.say "Look..."
    camila.say "Just try not to get in the way out there, that's all."
    scene bg street
    show camila normal work
    with fade
    "I nod and hurry after Camila as she strides of down the street."
    "And even when I catch up to her, I still fall in a step behind."
    "I've done the best I can to dress in a streetwise manner."
    "To be able to blend in with the kind of people we're likely to encounter."
    "But I still feel like a little kid tagging along in the wake of a genuine adult."
    "Camila's good to her word, walking me around the neighbourhood she's patrolling."
    scene bg park
    show camila normal work
    with fade
    "Occasionally we stop so that she can talk to someone."
    "Or else she'll tell me an anecdote about policing the area."
    "And some of them are enough to make me gasp in amazement."
    "But by the time we're headed back towards Camila's precinct, something strikes me."
    "We really haven't seen anything exciting go down in all the time we've been out here."
    scene bg street
    show camila normal work
    with fade
    mike.say "Camila..."
    camila.say "Yeah..."
    camila.say "What's up?"
    mike.say "Is your beat usually this..."
    mike.say "Well, this quiet?"
    camila.say "Sometimes it is, sometimes it isn't."
    camila.say "I guess we just got lucky today."
    mike.say "Oh...okay..."
    camila.say "Wait a minute..."
    show camila annoyed
    camila.say "You think I took you someplace that's got no action?"
    mike.say "No, Camila, I didn't say that."
    camila.say "But you wanted more excitement, yeah?"
    show camila wink
    camila.say "So let's do something exciting..."
    "Without warning, Camila grabs hold of my wrist."
    "She has a grip like steel and is way stronger than she looks."
    "So she has no problem hauling me off the street and down the nearest alleyway."
    scene bg alley with fade
    show camila normal work at center, zoomAt(1.5, (640, 1040)) with hpunch
    "Once we're out of sight of the street, she shoves me roughly against a dumpster."
    camila.say "I'm always really tense at the end of a patrol, you know?"
    camila.say "Real wound up and frustrated, like I need to let off steam."
    camila.say "Sometimes I find a place where I can be alone."
    show camila blush
    camila.say "Then I reach into my pants and get myself off on my own."
    "All the time Camila's saying this to me, I'm nodding eagerly."
    "Because I can't get the image of her playing with herself out of my mind."
    "It's so hot that I'm sure it's going to be impossible to forget!"
    mike.say "I can understand that, Camila."
    mike.say "You have a stressful job."
    mike.say "So you need a way to relieve that stress."
    "Camila nods too."
    show camila at center, zoomAt(1.75, (640, 1140)) with hpunch
    "But she pushes me back harder against the dumpster too."
    show camila normal
    camila.say "Difference is, now I got you with me."
    camila.say "So today, you're gonna help me let off that steam."



    "And I begin to do as she says more out of amazement than anything else."

    "But at the same time I can already feel my cock starting to get hard."
    "I have the distinct feeling this is going to make up for the tame patrol."

    mike.say "Okay, Camila..."
    mike.say "I'm ready..."
    "I turn around as I'm saying this, but I don't get to finish."
    "Because Camila literally pounces on me the moment I turn around."
    hide camila
    show camila kiss work
    with vpunch
    $ camila.flags.kiss += 1
    "And I really do mean that - she actually jumps and wraps herself around me!"
    "I struggle to catch her, staggering back a few feet."
    "But luckily I manage to keep my balance, holding her up."
    "All the time I'm doing this, Camila is on me like a wild animal."
    "Kissing, nibbling, biting and even scratching as she clings onto me."
    "I know she said that she gets tense and worked up at the end of her patrols."
    "But this is almost like she's losing her mind!"
    "Suddenly she breaks off kissing me."
    "And I hear her panting out a new demand."
    scene bg alley
    show camila flirt work at center, zoomAt(1.75, (640, 1140))
    with fade
    camila.say "Ah..."
    camila.say "[hero.name]..."
    camila.say "I...want you...in me..."
    camila.say "NOW!"
    "There's not even time to nod as I hurry to do what I'm told."
    "I just jig Camila around in my arms as I try to line everything up down there."
    menu:
        "Fuck her pussy":
            "And luckily for me it doesn't take long to get it just right."
            scene camila stand
            show camila stand alley fuck pose1 work mc_casual
            with fade
            "Camila goes up in my arms and comes down square on the head of my cock."
            "I'm holding onto her, judging everything by what I can feel down there."
            "There's the natural resistance that I was expecting."
            "But I'm already feeling the sensation of that beginning to weaken."
            "Camila must be feeling it too, as she's already moaning in my ear."
            show camila stand alley fuck pose1 pleasure
            camila.say "Yeah...yeah..."
            camila.say "Just like that!"
            "Her words soon fade away into more desperate moans as it happens."
            "Little by little she opens up for me and begins to sink downwards."
            show camila stand alley fuck pose2 normal
            "Still held in my arms, Camila inches her way down and onto my cock."
            "By the time it's filled her completely, she's pretty much helpless."
            show camila stand alley fuck pose3
            "All she can do is cling onto me."
            "Which leaves me free to begin having some real fun."
            "I start to move, thrusting into her."
            show camila stand alley fuck pose2
            "And this new movement seems to bring Camila back to life."
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "I feel her knit her fingers behind my neck."
            show camila stand alley fuck pose2
            "At the same time she wraps her legs around my waist too."
            show camila stand alley fuck pose3
            "Then she leans backwards, maximising the effect of my movements."
            "We're not trying to create a work of art here."
            "And the setting is pretty far from being romantic."
            show camila stand alley fuck pose2
            "So I see no point in holding back or trying to be subtle."
            "Instead I devote all of my energy to fucking Camila as hard as possible."
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "And she seems to appreciate the effort too."
            "Even though her head is bobbing the whole time, I can tell she's nodding too!"
            show camila stand alley fuck pose2
            "Gravity gives me a helping hand along the way."
            "Because once I put in the effort of throwing Camila up, she has to come back down."
            show camila stand alley fuck pose3 pleasure
            "And when she does that, she's obviously sliding right back down my cock again."
            "Pretty soon I can see her eyes start to glaze over and then close."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "But I'm sure to keep mine open the whole time."
            "Because that means I can watch as her pert breasts bounce up and down."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "Their motion is almost hypnotic, and it makes me work harder still."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "That is until the moment I feel Camila starting to tense in my arms."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "For a second I can't make sense of what's happening."
            "But then she answers the question for me."
            show camila stand alley fuck ahegao pose3
            camila.say "Uh..."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            pause 0.2
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            camila.say "G...gonna...cum..."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            pause 0.2
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            camila.say "Gonna...cum!"
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            pause 0.2
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "By now Camila's muscles are squeezing me pretty hard."
            show camila stand pose2
            "And I can feel myself starting to cum too."
            menu:
                "Cum inside":
                    "I hold onto Camila until the very last."
                    show camila stand pose1 creampie with vpunch
                    "And I make sure to shoot my load inside of her."
                    with vpunch
                    "She's clinging onto me again as it happens."
                    $ camila.love += 2
                    with vpunch
                    "I can feel her legs gripping me, her nails digging into my shoulders."
                    "And then we're both spent, leaning against the dumpster for support."
                "Pull out":
                    "I adjust the way I'm holding Camila at the last second."
                    "This means that my next thrust lifts her off my cock completely."
                    show camila stand pleasure pose3
                    "She yelps in surprise as I pop out of her."
                    "And in the next second I shoot my load over her breasts and belly."
                    show camila stand cum with vpunch
                    "Then we're both spent, leaning against the dumpster for support."
                    $ camila.love += 1
        "Fuck her ass":
            "And luckily for me it doesn't take long to get it just right."
            scene camila stand
            show camila stand alley fuck pose1 work
            with fade
            "Camila goes up in my arms and comes down square on the head of my cock."
            "I'm holding onto her, judging everything by what I can feel down there."
            "There's the natural resistance that I was expecting."
            camila.say "My ass..."
            camila.say "Hey...that's my..."
            camila.say "Ooh...oh fuck!"
            "I smile as I hear Camila's surprise melting into pleasure."
            "The resistance is still there in her muscles."
            "But I'm already feeling the sensation of that beginning to weaken."
            "Camila must be feeling it too, as she's already moaning in my ear."
            show camila stand alley fuck pose1 pleasure
            camila.say "Yeah...yeah..."
            camila.say "Just like that!"
            "Her words soon fade away into more desperate moans as it happens."
            "Little by little she opens up for me and begins to sink downwards."
            show camila stand alley fuck pose2 normal
            "Still held in my arms, Camila inches her way down and onto my cock."
            "By the time it's filled her completely, she's pretty much helpless."
            show camila stand alley fuck pose3
            "All she can do is cling onto me."
            "Which leaves me free to begin having some real fun."
            "I start to move, thrusting into her."
            show camila stand alley fuck pose2
            "And this new movement seems to bring Camila back to life."
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "I feel her knit her fingers behind my neck."
            show camila stand alley fuck pose2
            "At the same time she wraps her legs around my waist too."
            show camila stand alley fuck pose3
            "Then she leans backwards, maximising the effect of my movements."
            "We're not trying to create a work of art here."
            "And the setting is pretty far from being romantic."
            show camila stand alley fuck pose2
            "So I see no point in holding back or trying to be subtle."
            "Instead I devote all of my energy to fucking Camila as hard as possible."
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "And she seems to appreciate the effort too."
            "Even though her head is bobbing the whole time, I can tell she's nodding too!"
            show camila stand alley fuck pose2
            "Gravity gives me a helping hand along the way."
            "Because once I put in the effort of throwing Camila up, she has to come back down."
            show camila stand alley fuck pose3 pleasure
            "And when she does that, she's obviously sliding right back down my cock again."
            "Pretty soon I can see her eyes start to glaze over and then close."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "But I'm sure to keep mine open the whole time."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "Because that means I can watch as her pert breasts bounce up and down."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "Their motion is almost hypnotic, and it makes me work harder still."
            "That is until the moment I feel Camila starting to tense in my arms."
            show camila stand alley fuck pose2
            "For a second I can't make sense of what's happening."
            "But then she answers the question for me."
            show camila stand alley fuck ahegao pose3
            camila.say "Uh..."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            pause 0.2
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            camila.say "G...gonna...cum..."
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            pause 0.2
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            camila.say "Gonna...cum!"
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            pause 0.2
            show camila stand alley fuck pose2
            pause 0.2
            show camila stand alley fuck pose1 at startle(0.05,-10)
            "By now Camila's muscles are squeezing me pretty hard."
            show camila stand pose2
            "And I can feel myself starting to cum too."
            menu:
                "Cum inside":
                    "I hold onto Camila until the very last."
                    show camila stand pose1 creampie with vpunch
                    "And I make sure to shoot my load inside of her ass."
                    $ camila.sub += 2
                    with vpunch
                    "She's clinging onto me again as it happens."
                    with vpunch
                    "I can feel her legs gripping me, her nails digging into my shoulders."
                    "And then we're both spent, leaning against the dumpster for support."
                "Pull out":
                    "I adjust the way I'm holding Camila at the last second."
                    "This means that my next thrust lifts her off my cock completely."
                    show camila stand pleasure
                    "She yelps in surprise as I pop out of her ass."
                    show camila stand cum with vpunch
                    $ camila.sub += 1
                    "And in the next second I shoot my load over her breasts and belly."
                    "Then we're both spent, leaning against the dumpster for support."
            $ camila.flags.anal += 1
    $ camila.sexperience += 1
    return

label camila_prison_visit_1:
    scene bg policestation
    "At first I was sure that I never wanted to lay eyes on Kylie again, not after what she put me through."
    "And when the letter arrived telling me I could visit her in prison, I almost tossed it into the trash."
    "But when I showed it to Camila, her response caught me completely off-guard."
    "I'd expected her to have the same reaction as me, and yet she said that I should take up the offer."
    "Even stranger, she told me that she wanted to come along too."
    scene bg jail
    show camila at center, zoomAt (1.5, (640, 1040))
    with fade
    "So that's how we came to be in the prison where they're holding Kylie, waiting to see her."
    "I must have be showing my nerves more than I thought."
    "Because I feel Camila take hold of my hand and give it a squeeze."
    camila.say "Hey, don't worry about it, [hero.name]."
    camila.say "She can't hurt you anymore - we both saw to that."
    "I nod and give her what I hope looks like a confident smile."
    mike.say "Ah...yeah, Camila, I know."
    mike.say "It's just...well, I guess I'm just scared."
    mike.say "I can't help feeling like that!"
    show camila happy
    "Now it's Camila's turn to nod and smile."
    "But somehow hers seems more genuine."
    "And it actually makes me feel a little better."
    "Even a little safer too!"
    camila.say "I'll be with you the whole time."
    show camila normal
    camila.say "And that psycho bitch'll be behind bars."
    camila.say "Trust me - I know how to handle a situation like this."
    "But the moment that we walk into the room, I look around in surprise."
    "I'd been expecting one of those booths you see in the movies."
    "The one's where the convict is on one side of the glass and the visitor on the other."
    play music "music/darren_curtis/come_out_and_play.ogg" loop fadeout 5.0
    scene kylie_bj_bg_jail at center, dark
    show kylie sad jail zorder 1 at center, zoomAt (1.1, (860, 800)), dark
    show kylie_bj_bars as bars1 zorder 2 at center
    show kylie_bj_bars as bars2 zorder 3 at center, zoomAt (1.0, (0, 720))
    with fade
    "But instead we're standing in front of what must be Kylie's cell."
    "There's the standard barred door."
    "The space between the bars is barely wide enough to fit a hand through."
    "All in all, it looks like a scene from that film with the suave cannibal in it!"
    show kylie surprised at center, zoomAt (1.1, (860, 800)), startle
    kylie.say "[hero.name]?!?"
    kylie.say "Is that really you?!?"
    "I can't make out much inside the cell, other than that it's pretty bare."


    pause 0.5
    hide kylie
    show kylie crazyhappy jail at center, zoomAt (1.4, (860, 1000))
    with hpunch
    "And that's because Kylie rushes up and presses herself against the bars."
    "It's like one of those times when an animal rushes at the glass in a zoo."
    "I can't help leaping backwards and crying out in alarm."
    mike.say "Argh!"
    mike.say "Oh shit!"
    "Kylie's dressed in a prison uniform and looks otherwise normal."
    "Well, I mean she looks as crazy as ever."
    "But at least she's not strapped down in a straight-jacket or muzzled like a dog!"
    show kylie happy
    kylie.say "Oh, [hero.name]..."
    kylie.say "I knew that you'd come!"
    kylie.say "I just knew it!"
    kylie.say "Even after that little...misunderstanding we had."
    kylie.say "I knew that you'd come round and come back to me!"
    "I look around, baffled by how sweet and amenable Kylie's being."
    "Surely the sight of Camila should have sent her into a rage?"
    "What's happening here - are they doping her up with drugs, or what?!?"
    "It's then that I realise Camila's nowhere to be seen."
    "She's standing a little way off, hidden in the shadows."
    show camila zorder 4 at center, zoomAt (1.65, (340, 1100)) with easeinleft
    show kylie angry
    "Seeing me notice what she's doing, Camila steps forwards."
    "This allows Kylie to see her for the first time."
    "And the effect is both instant and dramatic."
    show kylie yandere at center, zoomAt (1.0, (860, 1000)), vshake
    kylie.say "WHAT ARE YOU DOING HERE?!?"
    show kylie at center, zoomAt (1.0, (860, 1000)), vshake
    kylie.say "GET AWAY FROM HIM - YOU FUCKING BITCH!"
    show kylie at center, zoomAt (1.0, (860, 1000)), vshake
    kylie.say "I'LL KILL YOU FOR WHAT YOU DID!"
    show kylie at center, zoomAt (1.0, (860, 1000)), vshake
    kylie.say "I'LL KILL YOU FOR TAKING HIM AWAY FROM ME!"
    "I'm left reeling by the sudden transformation in Kylie's demeanour."
    show camila flirt
    "But Camila just seems to be amused by the violence of the outburst."
    camila.say "Hey, Kylie."
    camila.say "How's shitting in a bucket suiting you, huh?"
    "Kylie's staring at Camila now, murder in her eyes."
    "She starts pacing back and forth like a caged animal."
    "And when she speaks again, her voice becomes low and threatening."
    show kylie angry
    kylie.say "What have you been telling him?"
    kylie.say "Have you been poisoning him against me?"
    kylie.say "Whatever you've done, it won't work."
    kylie.say "We're destined to be together - you can't change that!"
    "Maybe I should step in and say something here?"
    "But I have to admit, the scene that's unfolding is quite something."
    "Is it wrong to get off on the fact that they're basically fighting over me?"
    show camila bored
    camila.say "Uh-uh...ain't gonna happen, girl!"
    camila.say "That's all just fantasy inside of your twisted little head."
    camila.say "You lost, bitch - you're gonna rot behind bars."
    show camila flirt
    camila.say "And he's MY man now..."
    "Camila underlines her point a moment later."
    "She drapes her arms around my neck and wraps herself around me."
    show kylie annoyed at center, zoomAt (1.4, (1060, 1000))
    hide camila
    show camila kiss zorder 4 at flip, center, zoomAt (1.0, (540, 740))
    with fade
    $ camila.flags.kiss += 1
    "And then she kisses me, pushing her tongue straight into my mouth."
    "I can't help but respond in kind, returning the gesture eagerly."
    kylie.say "No...what are you..."
    kylie.say "Get your hands off him..."
    "Camila doesn't dignify Kylie's outburst with a response."
    "She just chuckles and shakes her head, as if Kylie's not worth her time."
    hide camila
    show camila flirt zorder 4 at center, zoomAt (1.65, (340, 1100))
    show kylie at center, zoomAt (1.4, (860, 1000))
    with fade
    camila.say "Mmm..."
    camila.say "You have a few moments alone with Little Miss Fruitloop here."
    camila.say "I'll catch you on the way out for some more of that sugar!"
    show kylie angry
    hide camila with easeoutleft
    "With that, Camila turns on her heel and walks out."
    "This leaves me alone with Kylie."
    "I'm frightened that she'll explode with rage."
    show kylie normal
    "But Kylie surprises me by almost instantly changing demeanour."
    "Without Camila present, she becomes as sweet and charming as she was to begin with."
    kylie.say "Oh, I thought she'd never leave us alone!"
    kylie.say "You mustn't think I'm mad at you, [hero.name]."
    kylie.say "It's just that bitch cop I hate - I still love you!"
    "Kylie presses herself against the bars, beckoning me closer."
    scene kylie_bj_bg_jail at center, zoomAt (1.5, (340, 1040)), dark
    show kylie sad jail zorder 1 at center, zoomAt (2.0, (700, 1340))
    show kylie_bj_bars zorder 2 at center, zoomAt (1.5, (340, 1040))
    with fade
    "And like a fool, I do as she asks, approaching the bars."
    kylie.say "I...I was thinking, [hero.name]."
    kylie.say "Maybe you could ask for a special kind of visit?"
    show kylie blush
    kylie.say "You know...the conjugal kind?"
    "Sometimes I don't know how my mind works or what I'm thinking."
    "Because I find myself nodding eagerly at Kylie's request."
    "She's just so hot and needy, and she seems to want me so much!"
    mike.say "I...I guess I could ask..."
    show kylie happy
    kylie.say "Oh, thank you, [hero.name]!"
    show kylie blush
    kylie.say "I'll be thinking about having you inside of me the whole time!"
    kylie.say "There won't be another thing on my mind until it happens, I promise!"
    "Nodding like I'm in a trance, I walk out of the room."
    scene bg jail
    show camila at center, zoomAt (1.5, (640, 1040))
    with fade
    "Camila greets me out in the corridor."
    camila.say "You okay, [hero.name]?"
    mike.say "Yeah...I guess so."
    mike.say "Kylie kind of asked me to arrange a conjugal visit!"
    show camila angry
    camila.say "What?!?"
    camila.say "Tell me you said no!"
    "I hold up my hands, trying to excuse myself."
    mike.say "I...I said I'd ask, that's all."
    mike.say "And I only said that because she sprang it on me, honestly!"
    "Camila scrutinises me for a couple of uncomfortable seconds."
    show camila bored
    "But then she nods and lets out a sigh of resignation."
    camila.say "Well...you have been under a lot of pressure lately."
    camila.say "So it makes sense that you'd say that to pacify her."
    show camila normal
    camila.say "But just for the record, she's not getting her claws back into you!"
    "I nod, relieved that Camila seems to be buying my explanation."
    show camila flirt
    "But then I see a devious smile spread across her face."
    camila.say "Actually, Little Miss Fruitloop might be onto something."
    camila.say "Maybe we give her the conjugal visit she's asking for?"
    camila.say "But we make sure it doesn't go the way she wanted?"
    hide camila with easeoutleft
    "With that, Camila walks off down the corridor."
    "And she leaves me wondering just what that could mean."
    $ camila.flags.camiladelay = TemporaryFlag(True, 3)
    return

label camila_prison_visit_2:
    scene bg jail
    show camila happy
    with fade
    "Camila has a smile on her face as we walk towards Kylie's cell."
    "This was supposed to be the day of my conjugal visit."
    "But Camila still hasn't told me what she has in mind."
    "Even so, I'm more than certain it doesn't involve me fucking Kylie!"
    play music "music/darren_curtis/come_out_and_play.ogg" loop fadeout 5.0
    scene kylie_bj_bg_jail at center, dark
    show kylie sad jail zorder 1 at center, zoomAt (1.1, (860, 800)), dark
    show kylie_bj_bars as bars1 zorder 2 at center
    show kylie_bj_bars as bars2 zorder 3 at center, zoomAt (1.0, (0, 720))
    with fade
    "The moment that she sees me, Kylie's face lights up."


    pause 0.5
    hide kylie
    show kylie crazyhappy jail at center, zoomAt (1.4, (860, 1000))
    with hpunch
    "She rushes over to the bars that stand between us."
    show kylie yandere
    "But then she stops in her tracks and her expression turns ugly."
    show camila zorder 4 at center, zoomAt (1.65, (340, 1100)) with easeinleft
    "And that's because Camila steps out from behind me."
    kylie.say "[hero.name]!"
    kylie.say "What's SHE doing here?!?"
    "Before I can even open my mouth, Camila answers the question herself."
    show camila flirt at center, zoomAt (1.65, (440, 1100)) with ease
    "She wraps her arms around my waist, pressing herself against me."
    "She's all but humping my leg as Kylie fumes on the other side of the bars."
    camila.say "We're here for the conjugal visit, Kylie."
    show camila bored
    camila.say "[hero.name] told me you asked for one, yeah?"
    "Kylie lets out a shriek of frustration and sheer rage."
    "The sound is terrifying, but it doesn't seem to scare Camila at all."
    camila.say "Oh...did you think that..."
    show camila happy
    "Camila lets out a wicked chuckle and shakes her head."
    camila.say "Oh, Kylie - you though it was a conjugal visit for YOU?"
    camila.say "That's such a shame."
    play music "music/roa_music/city_nights.ogg" loop
    show camila flirt
    camila.say "Because I went and arranged one for this side of the bars!"
    "Camila's stroking my cock through my pants the whole time she's saying this."
    "And I can feel myself getting harder with every second that passes."
    camila.say "Mmm..."
    camila.say "I feel really horny right now."
    camila.say "Wanna fuck me, [hero.name]?"
    camila.say "Wanna fuck me real hard?"
    "I'm nodding before I know it, lost in my lust for her."
    "But it's not like Camila waits for me to say yes."
    show camila topless with dissolve
    "She's already tearing at my clothes and urging me to do the same to her too!"
    "I thought that Kylie was supposed to be the crazy one here."
    "But this is a whole different kind of crazy."
    "Camila's actually demanding sex while we're visiting a madwoman in prison."
    "And I guess I must be crazy too, because I'm going along with it!"
    scene camila doggy
    show camila doggy jail
    with fade
    "As soon as we're naked, Camila all but leaps on me."
    "I struggle to hold her up, and we slam into the bars of Kylie's cell."
    "She wraps her legs around me and almost pulls me into her."
    "We tumble onto the floor, Camila landing on all fours."
    show camila doggy inside
    "Before I know what's happening, I'm inside of her, as deep as I can go."
    camila.say "Ah..."
    show camila doggy pleasure
    camila.say "Oh yeah...that's it..."
    camila.say "Fuck...I love your cock inside of me!"
    show camila doggy speed
    "Almost on autopilot, I begin thrusting into Camila."
    "I'm leaning into her, pressing down with all of my weight."
    mike.say "Shit..."
    mike.say "Camila..."
    mike.say "This...is...crazy..."
    mike.say "But I love it too!"
    "All the time I'm looking over Camila's shoulder, staring into the cell."
    "At first, Kylie reacts like a wild animal, hammering in the bars and cursing."
    "But then she makes eye-contact with me, and her protests turn into something else."
    "I see one of her hands disappear into her pants."
    "The other snakes under her shirt and starts to caress one of her breasts."
    "Is...is she..."
    "She is - Kylie's playing with herself!"
    "I watch as she begins to bite her lip and pant heavily."
    "Kylie's bringing herself off while she watches us do it!"
    "Soon the sound of her moaning and wailing is pretty loud."
    "Loud enough to be heard over my thighs slamming into Camila's buttocks."
    "Part of me expects her to be freaked out by Kylie's actions."
    "But all she does is chuckle all over again, gasping into my ear."
    camila.say "Yeah, flick it all you want, bitch."
    camila.say "The real thing's all mine now!"
    "She's so confident in that moment, so strong and powerful."
    "It's not like I feel submissive or anything - of course not!"
    "But she fills me with the desire to do all I can for her."
    show camila doggy -speed ahegao with hpunch
    "And she pushes me over the edge, making me shoot my load."
    with hpunch
    camila.say "Jesus, [hero.name]..."
    with hpunch
    camila.say "You can do that to me forever!"
    "I'm panting and shaking from the effort of holding her weight."
    $ kylie.sub += 25
    $ camila.love += 1
    $ camila.sexperience += 1
    scene kylie_bj_bg_jail at center, dark
    show kylie blush jail zorder 1 at center, zoomAt (1.25, (860, 1100))
    show kylie_bj_bars as bars1 zorder 2 at center
    show kylie_bj_bars as bars2 zorder 3 at center, zoomAt (1.0, (0, 720))
    show camila naked flirt zorder 4 at center, zoomAt (1.65, (440, 1100))
    with fade
    "So it's a relief to plant Camila's feet on the ground."
    show camila casual bottomless nojacket with dissolve
    "I begin to pick up my clothes, and Camila is following my lead."
    "But then she stops and slips a finger between her thighs."
    scene camila handlick kylie with fade
    "The cum is just starting to seep out of her."
    "And I watch as she collects some on the end of her finger."
    camila.say "Aw..."
    camila.say "Did you play with your pussy?"
    camila.say "Here, have a taste of mine!"
    show camila handlick kylie stand cum surprised
    "With that, she pushes her finger through the bars."
    "I fully expect Kylie to explode again - even to bite her finger off."
    show camila handlick kylie close lick
    "But instead she hurries over and laps the cum off of Camila's fingertip."
    show camila handlick kylie up
    "When she's done, Camila pulls her finger back and shakes her head."
    show camila handlick kylie hold pleasure
    "She gets dressed without another word and walks towards the door."
    show camila handlick kylie mike with fade
    "I look back at Kylie, still licking her lips in sheer desperation."
    show camila handlick kylie sad
    "And for a moment I think about saying something to her."
    show camila handlick kylie normal
    "But what is there to say?"
    scene bg jail with fade
    "And so I just shake my head and hurry after Camila."
    "I guess my head's still reeling from what we just did."
    "And a part of me wonders which side of the glass the crazy people were really on!"
    return

label camila_preg_talk:
    "Camila's one of those uncomplicated girls."
    "The kind that says whatever's on her mind at the time."
    "And also the kind that says to hell with the consequences too!"
    "Which means that she doesn't hold back or give me any warning..."
    show camila normal
    camila.say "[hero.name], we've got a problem!"
    mike.say "Huh?"
    mike.say "What do you mean?"
    camila.say "I mean we need to talk about something - right now!"
    mike.say "S...sure thing, Camila!"
    mike.say "I'm all ears."
    "Camila nods, clearly pleased with the way I just jumped to attention."
    camila.say "I've been feeling shitty in the morning the past couple of days."
    camila.say "I tried to ignore it at first, but it just got worse."
    camila.say "So I took a test, and it was positive."
    "Camila lets the words hang in the air."
    "She's clearly expecting a response of some kind from me."
    mike.say "Ah...okay..."
    mike.say "It was positive for what, exactly?"
    "Camila throws her hands up in the air at this."
    show camila annoyed
    "She lets out a grunt of frustration at my answer too."
    camila.say "Urgh..."
    camila.say "What the hell do you think it was for, dummy?!?"
    camila.say "I'm fucking pregnant!"
    "Suddenly I feel like a complete idiot."
    "And not just because Camila's calling me one too."
    "What other kind of test would she be talking about?"
    mike.say "Oh..."
    mike.say "Oh shit!"
    show camila normal
    "Camila nods, relieved to see that I'm finally on the same page as her."
    camila.say "Oh shit is about right."
    camila.say "We need to get serious, [hero.name]."
    camila.say "We need to decide what we're going to do!"
    "Doesn't look like I'm going to get to think about this one."
    "Which is a shame, because how am I supposed to know what's for the best?"
    "Camila's already eyeing me up, waiting for a response..."
    menu:
        "Let's keep the baby":
            "I can't say that I'm honestly ready to have a kid."
            "But then I wasn't ready to fall for a tough cop either!"
            "Chance brought Camila and me together."
            "And she's the best thing in my life right now."
            "So maybe chance is behind this too?"
            mike.say "Camila, I think we should keep the baby."
            "For the first time, Camila looks genuinely surprised."
            camila.say "A...are you serious?!?"
            camila.say "I was sure you'd say no."
            camila.say "That you'd say we should get rid of it!"
            "I shake my head, trying to dismiss the notion outright."
            mike.say "No, Camila."
            mike.say "We should definitely do this."
            "Now it's Camila's turn to shake her head."
            camila.say "I...I don't know if I can be a mom..."
            mike.say "No, Camila."
            mike.say "For the record, I think you'll be a great mom."
            mike.say "Fierce as a fucking lioness with her cubs!"
            "I see her blush a little at this, trying to laugh it off."
            show camila flirt
            camila.say "Shut up, [hero.name]!"
            camila.say "But seriously - who's gonna raise the baby?"
            camila.say "We both have careers, right?"
            mike.say "We can worry about that later, Camila."
            mike.say "And I'm not against staying at home to raise your kids either."
            mike.say "Actually, I kind of like the idea of waiting for a tough cop to come home."
            mike.say "It's hot, and I'd be the envy of the other stay-at-home dad's at the park too!"
            show camila happy
            "Camila laughs, and then gives me a punch on the arm for good measure."
            "Sure, it stings more than a little."
            "But it let's me know that she loves me."
            "So it's more than worth the pain."
            $ camila.love += 10
            $ camila.flags.toldpreg = True
        "Tell her to abort":
            "How can either of us say that we're ready to have a kid?"
            "I'm working every hour that god sends to get ahead in my career."
            "And Camila's a cop that's fighting to keep the streets clean."
            "She's putting her neck on the line daily!"
            "Neither of us is in a position to raise a child."
            mike.say "You don't want to keep it, do you?"
            "For the first time, Camila looks genuinely surprised."
            show camila annoyed
            camila.say "I...I don't know, [hero.name]."
            camila.say "What makes you think that?"
            camila.say "Don't you think I could be a mom?"
            "I shake my head, dismissing the notion out of hand."
            mike.say "No, Camila."
            mike.say "For the record, I think you'd be a great mom."
            mike.say "Fierce as a fucking lioness with her cubs!"
            "I see her blush a little at this, trying to laugh it off."
            mike.say "But you usually know what you want."
            mike.say "If you wanted to keep the kid..."
            mike.say "Well, you'd have just said so."
            "Camila nods, letting me know that I'm right."
            "But all the same, I'm too smart to let it show."
            show camila normal
            camila.say "I guess I wanted to see what you wanted, you know?"
            camila.say "But you got me, [hero.name]."
            camila.say "I don't think I'm ready for this..."
            mike.say "Then we do what we have to do, Camila."
            mike.say "And we wait until both of us ARE ready."
            "Camila lets out an uncharacteristic sob."
            "But she puts her arms around me and we hold each other tight."
            $ camila.love -= 10
            $ camila.unpreg()
    return

label camila_male_ending:







    if renpy.has_label("camila_achievement_3") and not game.flags.cheat:
        call camila_achievement_3 from _call_camila_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I know that most guys are nervous on their wedding day, that's kind of a given thing."
    "But my nerves are threatening to turn into a full-blown case of anxiety right now."
    "My suit feels like a straight-jacket, my tie like a noose around my neck."
    "I know that I'm sweating under my jacket, I just hope that it's not visible."
    "And no, I'm not having a panic-attack at the thought of finally marrying Camila."
    "That's the only thing that's letting me hold it together!"
    "What's worrying me is what I see when I scan the assembled guests behind me."
    "Sure, about half of them are my own friends and family."
    "But the other half are here for Camila, and they all look like cops to me."
    "What's bugging me is just how many of them are packing heat in the pews out there!"
    "Camila's got a nasty habit of 'forgetting' to leave her gun at home when she's off-duty."
    "And cops all seem to suffer from the same kind of habit in my experience."
    "So what are the odds of my wedding turning into a damn shoot-out?!?"
    "I mean, I already asked Camila if she had any enemies that might show up on the day."
    "You know, any old scores that hadn't been settled from when she put someone away?"
    "But I think she got the idea that I was joking."
    "Because she started saying I should get fitted for a bullet-proof vest as well as a wedding suit!"
    "And I know that I'm probably being crazily paranoid."
    "Yet the thought just won't stop coming back to haunt me."
    "I turn back to look at the alter, and the priest catches my eye."
    "He must be used to grooms that are a bag of nerves."
    "Because he gives me a reassuring smile that I hastily return."
    "But as he turns, I think I see a bulge under his robes."
    "Wait a minute..."
    "Is that a holster for a pistol?"
    "Is the priest actually an undercover cop?"
    "If he is, are we even going to be legally married when this is all over?!?"
    "Suddenly I hear the sound of swelling music and everyone gets to their feet."
    "I recognise it as the music Camila chose to come down the aisle to."
    "Looking over my shoulder, my eyes dart this way and that in the hope of seeing her."
    show camila wedding normal at center, zoomAt (1.0, (640, 730)) with dissolve
    "And the moment that they do, I feel like the weight of the world is lifted off my shoulders."
    "I'm used to seeing Camila dressed in street clothes while she's on duty."
    "So used to it that the sight of her in a wedding dress is like a slap in the face."
    "All of the toughness and machismo that she exudes on the beat is nowhere to be seen."
    "Instead she looks elegant, feminine and breath-takingly beautiful."
    if camila.is_visibly_pregnant:
        "It still feels a little odd to see Camila's belly growing on a daily basis."
        "But the cut of her dress is sympathetic to the fact that she's pregnant."
        "And so it only serves to add another level to how stunning she looks."
        "That and it reminds me of the fact we're about to become a family!"
    else:
        "I have to make sure that I heap the compliments on Camila once the ceremony's over."
        "She looks so damn good in that dress that I want to see her wearing stuff like that more often."
        "But I have to be subtle about it, not let on that I'm too keen."
        "Otherwise I'll never get to see her body on show outside of the bedroom again!"
    show camila at center, traveling (1.5, 3.0, (640, 1040))
    "It's like the mere sight of Camila walking down the aisle solves everything."
    "All of my fears and anxiety are gone in the blink of an eye."
    "So long as she's here with me, so long as we're together."
    "Then nothing can possibly go wrong."
    show camila flirt
    "I must be grinning like a fool by the time Camila makes it to the altar."
    "Because she gives me a lop-sided grin and shakes her head."
    show camila talkative
    camila.say "Nice to see you too, [hero.name]!"
    camila.say "Looks like we both scrub up pretty nice, huh?"
    show camila normal
    mike.say "Camila..."
    mike.say "You look..."
    mike.say "I...I don't have the words!"
    "I expect Camila to roll her eyes as I stumble over my words."
    "But somehow my being tongue-tied seems to have the opposite effect."
    show camila happy
    "She actually looks down and blushes, biting her tongue."
    "Camila finally manages to look me in the eye a moment later."
    show camila flirt
    show wedding camila with fade
    "And I get the feeling she's about to say something..."
    "Priest" "Ahem..."
    show wedding camila priest with dissolve
    "At the sound of the priest's voice, we both snap out of it."
    "Whatever Camila was going to say will have to wait until after the ceremony."
    "Priest" "Shall we get started?"
    "Camila and I nod, eager to get things underway."
    "Priest" "Very good!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony..."
    "I hardly hear what comes next, as I'm too busy staring at Camila."
    "She seems to be in pretty much the same place too, gazing back at me."
    "I guess it's just sheer luck that we manage to be aware enough to respond when the time comes."
    "Priest" "Do you, Camila..."
    "Priest" "Take [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    camila.say "I do."
    "Priest" "Very good."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take Camila..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "I do."
    "Priest" "Very well..."
    "Priest" "Now that these two people have exchanged their vows..."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any lawful reason why these two may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "Normally this would be the point where the priest pauses for effect."
    "Then the guests are supposed to have a little nervous laughter before we get on with it."
    "But I swear that I see more than one of the off-duty cops out there getting twitchy."
    "They're glancing around, some of them even reaching towards their guns!"
    "I guess they're all edgy and eager to keep anyone from spoiling Camila's big day!"
    "Priest" "Very good..."
    "As one, the collected guests seem to breath a sigh of relief and relax again."
    "I can't help letting out a deep sigh of genuine relief myself."
    "Thank god nobody pulled a weapon back there!"
    "Priest" "It is therefore my pleasure to declare you husband and wife!"
    "Priest" "You may kiss the bride..."
    show wedding camila -priest with dissolve
    "Camila and I don't need to be told to do something like that."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show camila kiss wedding
    with fade
    $ camila.flags.kiss += 1
    "A moment later she's in my arms and our lips are pressed together."
    "I'm hugging her pretty keenly, but she's squeezing the life out of me!"
    "Not that I'm going to complain, as it feels really good."
    "We did it - we're finally married."
    "My wife's a tough, no-nonsense cop."
    "And I couldn't be happier with that!"
    scene camila ending with fade
    camila.say "This is really weird for me..."
    camila.say "I'm used to being the one telling somebody to sit down and start talking!"
    camila.say "Thinking of that, wait a minute..."
    camila.say "Is this off the record?"
    camila.say "I mean, it's not gonna be used against me in a court of law, right?"
    camila.say "Okay, okay...geez!"
    camila.say "I'm a cop, yeah?"
    camila.say "I have to ask these kind of questions!"
    camila.say "Anyway...what was I supposed to be talking about?"
    camila.say "[hero.name]?"
    camila.say "Oh yeah, now I remember!"
    camila.say "How we met and fell in love and all that stuff..."
    camila.say "Ok, here goes nothing!"
    camila.say "I do kind of feel like I'm being interrogated here!"
    camila.say "Alright, alright...I'm doing it already!"
    camila.say "When you graduate from the academy and become a cop for real, you always make promises to yourself."
    camila.say "You know what I mean - about the kind of officer you're going to be and the way you're gonna get things done."
    camila.say "And one of the promises I made myself was that I'd never get involved with someone I met while I was on the job."
    camila.say "I kept it for a long time too, even when it was almost too tempting to just throw caution to the wind."
    camila.say "So what was it that made [hero.name] different?"
    camila.say "Geez...I wish I knew the answer to that one!"
    camila.say "I guess it's just one of those times when something hits you out of the blue."
    camila.say "I mean, sure I felt sorry for him when he came into the station the first time."
    camila.say "After all the shit that crazy bitch put him through, who wouldn't?"
    camila.say "But at first I wasn't doing anything more than any other officer would have done."
    camila.say "You try to give them support and reassurance, but not to get attached."
    camila.say "You also have to be wary of them getting attached to you in turn."
    camila.say "But there was just something about him that I couldn't get out of my head."
    camila.say "At first I thought it was just me being angry at the psycho that screwed with him."
    camila.say "Though as time went on, I couldn't pretend there wasn't more to it than that."
    camila.say "We just seemed to click on a whole different level, you know?"
    camila.say "Soon enough we were talking like a couple of friends."
    camila.say "And that was when I knew things were getting more serious."
    camila.say "I had to be sure that it was for real though, that our feelings were genuine."
    camila.say "I couldn't let [hero.name] get attached to me because of his trauma at the beginning."
    camila.say "And likewise I needed to know anything between us afterwards wasn't based on it either."
    camila.say "I think that made it hard at first, kind of built a little barrier between us."
    camila.say "He probably thought I was just being a tough bitch cop."
    camila.say "But I was only doing it to protect the both of us."
    camila.say "Soon enough I started to realise that my concerns were unfounded."
    camila.say "[hero.name] was a fun guy that really seemed to love being around me."
    camila.say "Sure, he has his quirks and more than a few little imperfections."
    camila.say "But I've been told that I'm not the easiest of people to get along with at times too."
    camila.say "So we went out on a date, nothing too heavy."
    camila.say "And it went well, so then we went on some more."
    camila.say "It didn't take long for me to start looking forward to the next time I'd get to see him."
    camila.say "I'd keep myself from going mad on boring shifts and long stake-outs by thinking about the guy."
    camila.say "It was like he somehow could respect the fact that I had to be tough as a cop."
    camila.say "But he also seemed to love it when I'd kick back with him and have a laugh too."
    camila.say "Believe me when I say a lot of guys are threatened by a female cop!"
    camila.say "Not, [hero.name] - he even seemed to think it was kind of cool!"
    camila.say "And just like that, we were dating!"
    camila.say "From there it was kind of like when you roll a snowball down a hill."
    camila.say "You know how it just gets bigger and goes faster all the time?"
    camila.say "Well that's kind of what it felt like with [hero.name] too!"
    camila.say "I was having so much fun that we were getting serious before I even realised it."
    camila.say "The next thing I knew, I was staring at a ring and he was asking me to marry him!"

    camila.say "Sure, the matter of me being a cop and it being pretty dangerous came into it."
    camila.say "I was actually the one that brought up the subject when we decided to get hitched."
    camila.say "Because I know from talking to a lot of folks that being married to a cop is tough."
    camila.say "I'm not saying that I'd have quit on the spot if that was what he wanted me to do."
    camila.say "Just that I thought we should have a frank discussion about it, you know?"
    camila.say "But [hero.name] was cool with me staying on the force."
    camila.say "I guess he'd already come to terms with it while we were dating."
    camila.say "I think he knows that I can handle myself out there."
    camila.say "And even better than that, he trusts my judgement too."











    camila.say "I went so long without anyone like [hero.name] in my life."
    camila.say "And I was convinced that I didn't need anyone like that either."
    camila.say "So it's funny now that I can't imagine my life without him!"
    if camila.is_visibly_pregnant or camila.flags.mikeBabies >= 1:
        camila.say "Not that I could imagine it without Nova and Seren either!"
        camila.say "I mean, I kind of always thought I'd have kids at some point in the future."
        camila.say "But when [hero.name] and I found out that I was pregnant, it just felt right."
        camila.say "Now we have two little rascals to keep in line around the house."
        camila.say "I think [hero.name] secretly hopes they'll grow up to be girly girls."
        camila.say "But I have a feeling they might take after me and be tomboys instead!"
    else:
        camila.say "And even though it's just the two of us right now, that may soon change."
        camila.say "I always kind of assumed that I'd have kids at some point in the future."
        camila.say "But now that I'm married, I'm wondering why we should wait any longer?"
        camila.say "[hero.name] seems to be up for starting a family."
        camila.say "And I think he'll make a great dad once the new arrivals are on the scene."
        camila.say "Maybe he'll even enjoy being a house-husband too!"
    camila.say "I still think it's weird that if he'd never come across that psycho, we'd likely never have met."
    camila.say "But part of me feel that it was almost supposed to play out like that, you know?"
    camila.say "Like we found each other because he needed somebody to step in and protect him."
    camila.say "And me, I was kind of rewarded for being a good cop by finding a guy that I could love."
    camila.say "Ah, maybe none of that is true and I'm just talking a load of crap."
    camila.say "But does it really matter?"
    camila.say "[hero.name] and I got together after something really bad happened."
    camila.say "And we managed to make something that was really wonderful once it was over."
    camila.say "I mean, that's got to be a great end to a story, right?"
    camila.say "Not that I think our story's over yet though!"
    camila.say "If you ask me, I think it's only just getting started."
    camila.say "We've both still got a lot of gas in the tank - if you know what I mean!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not camila.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_6
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_6
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label camila_investigation_callback:
    play sound cell_vibrate loop
    "I feel my phone vibrating in my pocket, so I whip it out to see who's calling."
    "And as soon as I see that it's Camila calling, I take it without hesitation."
    stop sound
    mike.say "Hey, Camila..."
    mike.say "What's up?"
    "Camila doesn't beat around the bush, but just gets down to business."
    camila.say "[hero.name]..."
    camila.say "I'm calling about the investigation."
    camila.say "You free to talk?"
    camila.say "Oh, and are you on your own?"
    "I look around, checking that there's nobody within earshot of me right now."
    "And once I'm satisfied, I confirm that it's safe for Camila to continue."
    mike.say "Sure, Camila..."
    mike.say "What's this about?"
    camila.say "I need you to fill me in on a couple of things, okay?"
    camila.say "Nothing serious, just making sure it all squares up."
    mike.say "Okay, Camila..."
    mike.say "Ask away..."
    call investigation_points (10) from _call_investigation_points_10
    return

label camila_birthday_date_male:
    $ DONE["camila_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg street
    "It took me what felt like an age to get the date of Camila's birthday out of her."
    "I know that cops are sensitive about their personal details ending up in the hands of the wrong person."
    "But it's not like I'm a scammer or a criminal trying to pull of some kind of crime against Camila."
    "I'm supposed to be dating her, for god's sake - and all I want is to take her on a date for her birthday!"
    "And even when she finally spills the beans and let's me have the date, the drama's not over."
    "Because it turns out that she doesn't want to go out to a restaurant or to catch a movie."
    "Oh no, Camila wants me to take her down to my local pub instead!"
    scene bg door pub with fade
    "So here we are, about to go on a supposedly romantic date - in The Winchester Arms!"
    show camila casual normal with dissolve
    mike.say "Camila..."
    mike.say "Are you sure about this?"
    mike.say "I mean, you're not pulling my leg, are you?"
    camila.say "Of course not, [hero.name]."
    camila.say "All that romantic crap isn't really me."
    camila.say "Plus, they say you can tell all you need to know about a guy from where he drinks."
    show camila happy
    camila.say "So this is a great way for me to get to know you better too."
    "I nod and smile as I hold the door open for Camila."
    "But I'm still not convinced this is the best idea ever."
    menu:
        "So be it":
            "But I'd better keep that to myself."
            "Especially if I want this date to go well."
            mike.say "If you say so, Camila."
            mike.say "Now let's see about getting a drink, yeah?"
            show camila happy
            "Camila looks happier almost as soon as I say this."
            "And she lets me lead the way over to the bar."
            $ game.active_date.score += 15
        "Meh...":
            "And I feel like I need to tell her that."
            mike.say "Just for the record, Camila..."
            mike.say "I'm going through with this."
            mike.say "But I don't think it's a good idea."
            "Camila fixes me with a suspicious frown."
            show camila annoyed
            "And she narrows her eyes at me for good measure too."
            camila.say "Hmm..."
            camila.say "Is that so?"
            camila.say "You know, if you were a suspect in one of my cases..."
            camila.say "I'd take that as a sign of guilt, that you had something to hide!"
            mike.say "What?!?"
            mike.say "Of course not, Camila!"
            mike.say "Look, let's just get a drink, okay?"
            $ game.active_date.score -= 10
    scene bg pub
    show camila normal
    with fade
    "Inside the pub I see that the taproom is about half full, as usual at this time of night."
    "That's good, because it means we can have the pick of where we want to sit without hassle."
    "And I have my eye on one of the nice, private booths at the back of the place."
    mike.say "How about we sit over there, Camila?"
    mike.say "Grab one of the booths, yeah?"
    mike.say "That way we can talk without anyone getting in our way."
    "Camila shakes her head and then nods towards the bar."
    camila.say "Nah..."
    show camila annoyed
    camila.say "I say we sit on those stools at the bar."
    camila.say "That way we can get the bar-staff's attention easier."
    camila.say "Plus we can size up anyone that walks in the door."
    "I glance in the direction that Camila wants to go."
    "And then I look back longingly at the booth."
    show camila normal
    "Looks like I'm going to have to make a choice."
    menu:
        "Stools are fine":
            "I guess we are supposed to be celebrating Camila's birthday."
            "So what's the problem with letting her have her own way?"
            "After all, it's only where we're sitting, right?"
            mike.say "Okay, Camila..."
            mike.say "Let's go grab those two stools right there."
            "Camila nods and begins to elbow her way through to them."
            "I don't think there's any real need to be so rough about it."
            "But I don't feel like questioning her on it either."
            "So I just follow in her wake."
            "As we reach the stools, another patron looks like he's about to claim them."
            "That is until Camila grabs them first and shoots him a threatening look."
            show camila angry
            camila.say "Beat it, asshole!"
            camila.say "Me and my date already claimed these!"
            "The guy almost leaps away from the stools."
            "And then he beats a hasty retreat."
            show camila normal
            "Camila doesn't seem in the least bit concerned about any of this."
            "And she just gestures for me to sit in one of the seats."
            "Which I do without question!"
            $ game.active_date.score += 15
        "Comfy sits are better":
            "Oh no - no way!"
            "I know how busy this place can get and how crowded the bar can become."
            "There's no way I want to have Camila being jostled by all those elbows!"
            mike.say "Trust me, Camila..."
            mike.say "We'll be better off over there."
            show camila annoyed
            "Camila looks a little pissed at my disagreeing with her."
            "But she soon consoles herself with elbowing through the patrons on her way to the booth."
            "I don't think there's any real need to be so rough about it."
            "But I don't feel like questioning her on it either."
            "So I just follow in her wake."
            "As we reach the booth, another patron looks like he's about to claim it."
            "That is until Camila grabs them first and shoots him a threatening look."
            show camila angry
            camila.say "Beat it, asshole!"
            camila.say "Me and my date already claimed this booth!"
            "The guy almost leaps away from the booth."
            "And then he beats a hasty retreat."
            show camila normal
            "Camila doesn't seem in the least bit concerned about any of this."
            "And she just gestures for me to sit down."
            "Which I do without question!"
            $ game.active_date.score -= 10
    show camila normal
    "Now that we've got somewhere to sit, the next thing we need is drink!"
    "But the question is, what are we going to order?"
    "I'm pondering this when Camila pipes up."
    "And it sounds like we're thinking the exact same thing!"
    camila.say "Geez..."
    camila.say "Are we gonna wait until we die of thirst, [hero.name]?"
    camila.say "We need to get some beer!"
    mike.say "Actually, Camila..."
    mike.say "I was thinking about that."
    mike.say "Seeing as how it's your birthday..."
    mike.say "Would you like me to order something a little special?"
    mike.say "Maybe a bottle of wine?"
    "Camila screws her face up at this."
    camila.say "Urgh..."
    show camila annoyed
    camila.say "I don't normally drink that stuff."
    camila.say "But I don't normally go on many dates either..."
    camila.say "So I'm gonna leave it up to you, okay?"
    "I nod and get on with ordering the drinks."
    "And I just hope that I end up making the right choice."
    menu:
        "Order beers":
            "I think about sticking to the original idea and ordering wine."
            "But then I remember that I'm supposed to be treating Camila tonight."
            "So it'd be a bit of a dick move to force her to drink something she hates."
            "This means I come back with a pitcher of beer and two glasses."
            "The sight of which makes Camila's face light up."
            camila.say "Hey, hey!"
            show camila happy
            camila.say "What happened to the wine?"
            mike.say "Ah, forget about that, Camila."
            mike.say "We're celebrating your birthday."
            mike.say "So I think you should get what you want."
            camila.say "Did I ever tell you how smart you are?"
            "I chuckle and shake my head as I pour out two glasses."
            "Then I hand one to Camila."
            "Which, to my amazement, she proceeds to drain in one go!"
            mike.say "Whoa!"
            mike.say "Slow down there, Camila!"
            show camila annoyed
            camila.say "Urgh..."
            camila.say "Ah, shut up and pour me another!"
            show camila happy
            camila.say "It's my birthday, remember?!?"
            $ game.active_date.score += 15
        "Order wine":
            "I think about just giving up and ordering beer."
            "But then I take a look at Camila and shake my head."
            "Sure, she looks and acts like Dirty Harriet."
            "But I'm sure there's a more sensitive girl inside there."
            "One that's just waiting for the chance to come out."
            "Though when I come back with a bottle of wine and two glasses, she doesn't look pleased."
            camila.say "Oh..."
            show camila annoyed
            camila.say "Wine...yay!"
            "I try to ignore Camila's sarcastic comment."
            "And instead of rising to it, I pour the wine and hand her a glass."
            show camila normal
            "Which, to my amazement, she proceeds to drain in one go!"
            mike.say "Whoa!"
            mike.say "Slow down there, Camila!"
            camila.say "Urgh..."
            show camila annoyed
            camila.say "Ah, shut up and pour me another!"
            camila.say "Maybe if I drink enough of this stuff, I'll get to like it."
            show camila happy
            camila.say "Or maybe I'll get so drunk that I won't care anymore!"
            $ game.active_date.score -= 10
    show camila normal
    "I swallow a good portion of my own drink, trying to keep up with Camila."
    "But it soon becomes apparent that she's going to be hitting it hard tonight."
    "And I'm sure that I can feel the room starting to spin a little already!"
    if game.week_day % 3 == 0:
        "By now, Camila's well into her second glass."
        "And I'm wondering if I should tell her to slow down a little."
        "Or at least order something to eat in the hope it'll soak up the booze!"
        "But then she takes me by surprise, slamming her elbow down in front of me."
        camila.say "Okay, okay..."
        camila.say "We gotta do a little something here, [hero.name]."
        mike.say "Erm..."
        mike.say "What's that, Camila?"
        camila.say "We gotta see if you can beat me..."
        camila.say "Beat me in an arm-wrestling match!"
        camila.say "None of the guys down the precinct can."
        show camila wink
        camila.say "So how about you try me, huh?"
        "I'm about to object."
        "But apparently, Camila wasn't asking - she was telling!"
        "She clasps my hand in her own."
        show camila normal
        "And then she starts pushing it over!"
        if hero.fitness >= 75:
            "As soon as Camila starts wrestling with me, I'm amazed at her strength!"
            "I might not want to be doing this, but she's damn serious!"
            "Luckily for me, all that time spent down the gym wasn't in vain."
            "And I can tell that my own strength is a match for Camila's."
            camila.say "C'mon..."
            show camila annoyed
            camila.say "Don't hold back because I'm a woman!"
            "I take a deep breath, and then I finally do as she asks."
            "And as I start to assert myself, I see Camila's reaction."
            "At first she's genuinely surprised."
            "Then she seems to get a little mad, piling on the effort."
            "But there's nothing she can do as I power my way to victory."
            "Camila's hand slams down, and she leaps back as I release it."
            camila.say "No way!"
            show camila angry
            camila.say "No fucking way!"
            mike.say "What do you mean, no way?"
            mike.say "Are you saying I cheated or something?"
            "Camila shakes her head, eager to dismiss the idea."
            camila.say "No, no..."
            show camila normal
            camila.say "I'm just used to winning, I guess."
            "Camila takes a sip of her drink and looks away."
            "But when she looks back again, I swear I can see a new-found respect in her eyes for me."
            $ game.active_date.score += 15
        else:
            "As soon as Camila starts wrestling with me, I'm amazed at her strength!"
            "I might not want to be doing this, but I don't seem to have a choice."
            "Because if I fail to resist at all, I'm worried she might actually break my arm!"
            camila.say "C'mon..."
            show camila annoyed
            camila.say "Try and stop me!"
            "I honestly do the best I can to put up a fight."
            "But it doesn't take long for Camila to slam my hand down and win the match."
            camila.say "Hah!"
            show camila happy
            camila.say "I win again!"
            mike.say "Ah..."
            mike.say "Yeah, Camila - well done!"
            "I do the best I can to massage feeling back into my arm."
            "And I have to lift my beer with the other one too!"
            $ game.active_date.score -= 10
    elif game.week_day % 3 == 1:
        "Camila keeps glancing over my shoulder as we're talking."
        "At first I think she's eyeing someone up on the other side of the pub."
        "And with that in mind, I get ready for her to do something unexpected."
        "You know, like suddenly leap up and arrest them for some terrible crime?"
        "But when I risk taking a look for myself, I see that's not the case at all."
        "Camila's actually looking at one of the arcade machines in the corner of the taproom."
        "It's one of the ones with a light-gun, and I think it's about cops, or something."
        "The I remember the name."
        mike.say "Virtual Cop!"
        show camila annoyed
        camila.say "Huh?"
        mike.say "The game - it's called Virtual Cop."
        camila.say "It is?"
        camila.say "Well, I should be a natural then!"
        show camila normal
        camila.say "You wanna play?"
        "I look at the machine and then back at Camila."
        "It's only a game, and the guns involved aren't real."
        "So what could possibly go wrong?"
        mike.say "Sure thing, Camila."
        mike.say "Let's go!"
        "I pump some coins into the slot while Camila grabs one of the guns."
        "She does some obligatory posing with it, showing off before we get started."
        "And I'm reminded of how hot it is to be dating a cute but tough female cop."
        mike.say "Okay, here goes..."
        mike.say "And remember - shoot away from the screen to reload!"
        camila.say "Okay, I got it!"
        if hero.has_skill("video_games"):
            "Camila starts out a little shakily."
            "She misses a few shots to begin with."
            show camila annoyed
            "And she curses when some of the enemies shoot her too."
            "But then I see the same coolness descend on her that she possesses on the beat."
            "She's nailing foes left and right, but I have one distinct advantage."
            "Camila's reflexes and aim are incredible, but this isn't real life."
            "It's a game where the enemies appear at a specific time and place."
            "And I've played this game enough to know exactly where and when."
            "This means I can be ready before Camila and beat her to the punch."
            "A fact that soon starts to frustrate her."
            camila.say "Hey!"
            show camila surprised
            camila.say "How did you..."
            camila.say "How are you even doing that?!?"
            "By the time the game is over, I'm way ahead of her."
            camila.say "You cheated!"
            show camila angry
            camila.say "You must have cheated!"
            mike.say "Calm down, Camila."
            mike.say "It's only a game."
            mike.say "I'm sure you'd do far better in real life."
            show camila normal
            "This seems to mollify Camila a little, and she nods in agreement."
            "But I swear I can see a new-found respect in her eyes for me."
            $ game.active_date.score += 15
        else:
            "Camila starts out a little shakily."
            "She misses a few shots to begin with."
            show camila annoyed
            "And she curses when some of the enemies shoot her too."
            "But then I see the same coolness descend on her that she possesses on the beat."
            "And from that point on, there's nothing I can do to keep up with her!"
            "Camila nails each and every foe that comes into her sights."
            show camila bored
            "And most of the time she kills the ones gunning for me too!"
            "By the time the game is over, she's earned a spot in the top ten high scores."
            camila.say "Ha!"
            show camila happy
            camila.say "Told you I was a natural!"
            $ game.active_date.score -= 10
    else:
        "Camila keeps glancing over my shoulder as we're talking."
        "At first I think she's eyeing someone up on the other side of the pub."
        "And with that in mind, I get ready for her to do something unexpected."
        "You know, like suddenly leap up and arrest them for some terrible crime?"
        "But when I risk taking a look for myself, I see that's not the case at all."
        "Camila's actually looking at the well-worn dartboard on the wall."
        mike.say "Do you play, Camila?"
        mike.say "Darts, that is..."
        mike.say "I get a game in myself every so often."
        mike.say "Some say I'm actually pretty good!"
        "Camila looks at me, then at the dartboard."
        camila.say "Sure, [hero.name]."
        camila.say "We can have a game of darts."
        camila.say "But I gotta warn you..."
        show camila wink
        camila.say "I'm one hell of a shot!"
        "We get up and Camila heads over to the dartboard."
        "And at the same time I take a diversion to the bar to get the darts."
        "A few moments later we're all set to go."
        "And I'm pretty sure Camila's sober enough to hit the board."
        show camila normal
        "Rather than me or one of the other drinkers sitting nearby."
        hide camila
        show date pub dart camila
        with fade
        if hero.has_skill("shooting"):
            "I decide to let Camila take the first shot."
            "And as soon as her dart hits the board, I know she means business."
            camila.say "Yeah!"
            camila.say "Right on target!"
            mike.say "Wow!"
            mike.say "Well done, Camila!"
            "I step up to make my own shot, clearing my head as I do so."
            "And I hit the precise spot on the board I was aiming for."
            mike.say "Ah..."
            mike.say "Not bad, even if I do say so myself!"
            "Camila's too busy gawping at the board to say anything at first."
            "But she soon snaps out of it."
            camila.say "What the fuck!"
            camila.say "How did you..."
            camila.say "That must have been a lucky shot!"
            "I just shrug and smile, which only seems to make matters worse."
            "Camila snorts with frustration and goes to take her next shot."
            "It's good, but not good enough, and I go on to trounce her ass."
            mike.say "I guess that means I win!"
            hide date pub dart
            show camila casual annoyed
            with fade
            camila.say "Yeah, yeah..."
            camila.say "Whatever!"
            "Camila seems more than a little pissed at having lost the game."
            $ game.active_date.score += 15
            "But I swear I can see a new-found respect in her eyes for me."
        else:
            "I decide to let Camila take the first shot."
            "And as soon as her dart hits the board, I know it's a mistake."
            camila.say "Yeah!"
            camila.say "Right on target!"
            mike.say "Ah..."
            mike.say "Well done, Camila!"
            "I step up and take my first shot, hoping it goes my way..."
            "And, of course, it doesn't!"
            camila.say "Ha, ha!"
            camila.say "Too bad, loser!"
            mike.say "Hey!"
            mike.say "Can't you at least try to be nice?"
            "Camila snorts and proceeds to make another outstanding shot."
            "And from there she roundly paddles my ass for the rest of the game."
            hide date pub dart
            show camila casual happy
            with fade
            camila.say "I guess that means I win, huh?"
            mike.say "I guess, Camila."
            camila.say "Huh?"
            show camila annoyed
            camila.say "What was that?"
            mike.say "Urgh..."
            mike.say "You won!"
            mike.say "Okay, I said it - are you happy now?"
            show camila happy
            camila.say "You bet I am!"
            $ game.active_date.score += 10
    show camila normal
    "I'm starting to lose track of how many drinks we've had by now."
    "And the conversation is turning into one of those random drunk discussions."
    "The kind where you wander from one topic to another."
    "And where you talk about whatever pops into your head next."
    camila.say "Hey..."
    camila.say "It's my birthday, right?"
    "I nod, as sure as I can be that this is correct."
    mike.say "Yeah, Camila..."
    mike.say "It sure is!"
    "Camila's nodding too."
    "But then she pokes a finger into my chest."
    camila.say "So..."
    show camila weird
    camila.say "Where's my goddamn present, huh?"
    "Wow...that's pretty forward of her!"
    "Most girls would have at least tried to drop hints."
    "But then Camila's not most girls."
    show camila normal
    if not hero.has_gifts:
        "Okay, Okay...so I forgot Camila's present."
        "But maybe I can talk my way out of this one."
        mike.say "What are you talking about, Camila?"
        mike.say "This IS your present, remember?"
        mike.say "Me taking you out on a date!"
        "Camila narrows her eyes as she studies me."
        "And it looks like she's trying to remember the conversation we had about all of this beforehand."
        "But in the end she just shakes her head."
        $ game.active_date.score -= 20
        show camila annoyed
        camila.say "Nah..."
        camila.say "I don't think so, [hero.name]."
        camila.say "I think you're just a cheap bastard!"
        camila.say "And a forgetful one too!"
        "That seems to be the end of it, as Camila lets the matter drop."
        "Sure, I didn't come out of that looking good."
        $ camila.love -= 10
        "But at least I'm not being put on the spot anymore."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_6
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "Of course I got you a present, Camila!"
                mike.say "I have it right here..."
                show camila happy
                "I pull out the gift and hand it over to Camila."
                play sound [paper_ripping_1, paper_ripping_2]
                "And she smiles as she tears off the paper."
                if _return:
                    "The moment she pulls it out of the box, Camila gasps."
                    camila.say "Oh, man..."
                    show camila surprised
                    camila.say "You have got to be kidding!"
                    mike.say "Erm..."
                    mike.say "What's wrong, Camila?"
                    show camila happy
                    camila.say "This is awesome, that's what!"
                    mike.say "You mean...you like it?"
                    "Camila nods."
                    camila.say "I always wanted one of these!"
                    $ game.active_date.score += 20
                    "I smile as Camila beams over her gift."
                    "And I feel a sense of relief for having chosen the right gift too."
                else:
                    "But the moment she pulls it out of the box, Camila groans."
                    camila.say "Oh, man..."
                    show camila surprised
                    camila.say "You have got to be kidding!"
                    mike.say "Erm..."
                    mike.say "What's wrong, Camila?"
                    show camila annoyed
                    $ game.active_date.score -= 10
                    camila.say "It's lame as hell, that's what!"
                    mike.say "Oh..."
                    mike.say "Sorry, I guess?"
                    "Camila shakes her head as she pushes the box aside."
                    "And I'm left wishing that I hadn't bothered to buy her anything at all."
                    "Or that she had better manners."
            else:
                "Okay, Okay...so I forgot Camila's present."
                "But maybe I can talk my way out of this one."
                mike.say "What are you talking about, Camila?"
                mike.say "This IS your present, remember?"
                mike.say "Me taking you out on a date!"
                "Camila narrows her eyes as she studies me."
                "And it looks like she's trying to remember the conversation we had about all of this beforehand."
                "But in the end she just shakes her head."
                $ game.active_date.score -= 20
                show camila annoyed
                camila.say "Nah..."
                camila.say "I don't think so, [hero.name]."
                camila.say "I think you're just a cheap bastard!"
                camila.say "And a forgetful one too!"
                "That seems to be the end of it, as Camila lets the matter drop."
                "Sure, I didn't come out of that looking good."
                $ camila.love -= 10
                "But at least I'm not being put on the spot anymore."
    show camila normal
    "I take a moment to glance at the time, and I see it's later than I thought."
    "Pretty soon they're going to be calling last orders, and then time at the bar."
    "Then I look down at the drinks in front of us, amazed at how much we've gotten through."
    "And I start to wonder if we need to get a last round in before it's too late."
    "Or if I should just let it go, as we're already pretty drunk!"
    "But then Camila seems to realise the same thing."
    "And that forces the issue."
    camila.say "Shit!"
    show camila annoyed
    camila.say "We need to get another one in, before it's too late!"
    menu:
        "I'll buy":
            "I feel like I can handle another drink."
            show camila normal
            "And Camila's a big girl that aught to know her limits."
            mike.say "Okay, Camila..."
            mike.say "Leave it to me!"
            "I stand up and weave my way to the bar."
            "And I swear the only reason I get served at all is that the bar-staff know me."
            "When I come back with our drinks, Camila's in the middle of a conversation with someone else."
            camila.say "So as I was saying..."
            mike.say "Ah, Camila..."
            camila.say "Shhh!"
            show camila annoyed
            camila.say "I'm talking to this guy right here!"
            mike.say "Is that so?"
            camila.say "Yes it is!"
            show camila weird
            camila.say "Do you have a problem with that?"
            mike.say "That's a coat-stand you're talking to!"
            "Camila turns around so fast that she almost falls off her seat."
            show camila normal
            camila.say "Whatever..."
            camila.say "No wonder that guy was such a good listener!"
            $ game.active_date.score += 10
        "I had enough":
            "Camila's obviously too far gone to make a sensible decision."
            "And that means I'm going to have to act as her conscience for the rest of the night."
            "I just hope she sees it that way too!"
            mike.say "Actually, Camila..."
            mike.say "I think I've had enough for one night."
            mike.say "You too!"
            show camila weird
            "Camila frowns at me, like she doesn't understand what I'm saying."
            camila.say "What are you talking about?"
            camila.say "I'm perfectly fine!"
            mike.say "Ah, Camila..."
            mike.say "I'm over here."
            mike.say "That's a coat-stand you're talking to!"
            "Camila turns around so fast that she almost falls off her seat."
            camila.say "Whatever..."
            show camila annoyed
            camila.say "Goddamn killjoy..."
            $ game.active_date.score -= 5
    show camila normal
    "When the bar finally closes, the last of the patrons are shown out of the pub."
    scene bg door pub
    show camila
    with fade
    "That leaves Camila and myself standing in the street, swaying slightly from the alcohol."
    "I shrug and get ready to broach the inevitable subject that's on both our minds."
    mike.say "So..."
    mike.say "What now, Camila?"
    mike.say "Are you headed home?"
    mike.say "Or do you want to go someplace else?"
    if game.active_date.score >= 80 and camila.sexperience >= 1:
        "Camila nods her head."
        camila.say "Oh, I'm not done yet, [hero.name]."
        show camila happy
        camila.say "Not by a longshot!"
        "Camila gets really close to me, smiling the whole time."
        hide camila
        show camila kiss casual
        with fade
        $ camila.flags.kiss += 1
        "I'm smiling too, expecting her to begin kissing me any moment!"
        "But then I hear a clicking sound."
        "And I feel something close around my wrist."
        mike.say "What the..."
        hide camila kiss
        show camila casual normal
        with fade
        "I look down to see that Camila's slapped a handcuff on me!"
        "And then she puts the other cuff on her own wrist too!"
        mike.say "Camila..."
        mike.say "What are you..."
        "Before I can finish speaking, Camila drags me away from the street."
        "And I can see that she's headed for the alley behind the pub!"
        camila.say "You're under arrest, [hero.name]."
        camila.say "For the crime of making an officer of the law horny as hell!"
        show camila flirt
        camila.say "And the sentence is to do something about it!"
        call camila_birthday_sex from _call_camila_birthday_sex
    else:
        "Camila shakes her head."
        camila.say "I'd love to, [hero.name]."
        camila.say "But I'm on duty first thing."
        show camila annoyed
        camila.say "And something tells me I'm going to be hungover as hell as it is!"
        "I nod and smile, knowing that there's no point in arguing."
        "Not when it comes to Camila's line of work."
        mike.say "Okay then, Camila..."
        mike.say "I'll call you, yeah?"
        show camila wink
        camila.say "Not if I call you first!"
        scene bg street with fade
        "With that, we turn and walk away from each other."
        "And I find myself hoping that things went well tonight."
        "At least well enough to earn me that phone-call."
    return

label camila_birthday_sex:
    scene bg alley
    show camila casual flirt
    with fade
    "I think that I can detect a slight stagger in Camila's step as she drags me into the alley."
    "It wouldn't be unusual, as I definitely feel the same in my own footsteps as I follow her."
    "But neither of us seems to be that concerned, instead we're focused on the task at hand."
    "Or at least the tasks, because we're both also doing very different things right now."
    "Camila's looking this way and that, scouting out every nook and cranny of the alley."
    "While the task that's occupying me is just keeping up with her and not falling on my face!"
    camila.say "Here?"
    show camila annoyed
    camila.say "Nah, too close to the street."
    camila.say "Maybe here?"
    camila.say "Urgh, no - this dumpster's overflowing!"
    "As Camila sizes up each spot and then moves on to the next, I seem to be a couple of seconds behind her."
    "Once she's done with a spot and dismissed it, I remain staring at it blankly for a moment."
    "But then she yanks me after her and we move on to the next."
    show camila normal
    "This means that it comes as a surprise to me when she actually settles on one of them."
    "I'm all ready to be dragged to the next one."
    "But instead I find myself shoved roughly up against the wall!"
    mike.say "Wha..."
    mike.say "Ungh..."
    mike.say "What the..."
    camila.say "What the fuck, [hero.name]?"
    show camila annoyed
    camila.say "We came down here to fuck!"
    camila.say "So get your damn cock out already!"
    "Camila uses in that tone of voice I've heard her use while on duty."
    "It's the one that speaks with supreme confidence and authority."
    "And it's also the one that promises bad things will happen if she's not obeyed!"
    "I don't know if it's because I'm drunk right now."
    "Or if Camila's just that good she can make me do as she says with a mere command."
    "But either way I leap to do as she says, fumbling with my flies."
    "Even so, it seems my efforts aren't enough for Camila."
    "As the moment I have them open, she slaps my hands aside."
    mike.say "Ow!"
    mike.say "Hey..."
    mike.say "What the hell, Camila?!?"
    camila.say "Shut the fuck up!"
    camila.say "Or else I'll book you for obstructing a police officer in the execution of her duty!"
    "I'm so drunk and confused by now that I have no idea if Camila's actually being serious."
    "But all the same, I raise my hands and keep out of it as she grabs hold of my cock."
    "I make a grunt of discomfort as she yanks it out of my pants."
    "Though the sound doesn't seem to have any effect on Camila."
    scene camila stand
    show camila stand alley ahegao
    with fade
    "Instead she kneels and starts to lick my shaft."
    mike.say "Uh..."
    mike.say "Camila..."
    show camila stand pleasure
    camila.say "Yeah, I know..."
    camila.say "Feels good, doesn't it?"
    "I swallow audibly as I nod."
    show camila stand normal
    camila.say "You know how many whores I've busted like this?"
    camila.say "How many times I've caught them doing it to their clients?"
    "I shake my head this time."
    show camila stand pleasure
    camila.say "At first you just bust them and have done with it."
    camila.say "But the sight of what they're doing - it just stays with you."
    camila.say "You can't get it out of your head, you know?"
    camila.say "Before you know it, you start watching them first."
    camila.say "You tell yourself it's just so you can be sure they're guilty."
    camila.say "But then you're watching them longer and longer."
    camila.say "And you know that it's because you're turned on!"
    show camila stand ahegao
    "My eyes are wide now as Camila looks up at me."
    "I can see a genuine hunger in her eyes too."
    camila.say "Sometimes I wanna be that girl."
    camila.say "Can you believe that?"
    camila.say "I'm a cop, one of the good guys."
    camila.say "But I'm jealous of a little whore getting dicked in an alleyway!"
    scene bg alley
    show camila flirt nojacket at center, zoomAt (1.5, (640, 1040))
    with fade
    "Camila lets go of my cock so that she can grab my wrists."
    "Then she slaps my hands onto her ass, forcing me to take hold of her."
    camila.say "I want you to fuck me like that, yeah?"
    camila.say "Hard and dirty, you hear me?"
    camila.say "I don't want you to stop until I cum!"
    "By now my head is nodding like it's going to come off my shoulders."
    "Camila's actions and her confession have gotten me as hot as hell."
    "And it's not like I need her to demand that I do that kind of thing to her."
    "Without a conscious thought, may hands begin to move over her body."
    "They stroke, caress and squeeze whatever they touch."
    "And the contact only seems to fan the fire inside of her."
    "Camila grabs hold of my cock again."
    "But this time she pulls it between her thighs."
    "She uses her other hand to pull down her panties."
    "And I swear that I can smell the scent of her already."
    "The odours in the alleyway are strong, but I still catch hers over them."
    "I don't know if pheromones are something we do as a species."
    "But right now I could believe in them."
    scene camila stand
    show camila stand alley fuck pose3 normal
    with fade
    "I turn Camila around so that she's now the one against the wall."
    "And at the same time I lift her off the ground."
    "As she comes down, my cock's in just the right spot to meet her."
    show camila stand fuck pose3 pain
    camila.say "Ah..."
    camila.say "Oh yeah..."
    camila.say "Just like that!"
    show camila stand fuck pose2 normal
    "I'm thrusting upwards as Camila comes down."
    "And I can feel the lips of her pussy already parting for me."
    "We're not going in for delicate foreplay here."
    "Just leaping headlong into animalistic sex."
    "I don't stop pushing until I'm all the way inside."
    show camila stand fuck pose1
    "I'm pinning Camila against the wall, filling her completely."
    "And once I am as deep as I can go, I don't wait a moment longer."
    show camila stand fuck pose2 pain
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "I begin to pound away at her with all of my strength."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "As I go backwards, Camila falls forwards."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "But then I reverse direction, and she's thrust back against the wall."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "Normally I might be worried about hurting her, or at least causing discomfort."
    "But the more I push myself, the more Camila seems to like it."
    show camila stand fuck pose2 pleasure
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "Her arms are wrapped around my neck, her legs around my waist."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "And every time she hits the wall, she gasps with pleasure."
    "In fact, it's almost like she's urging me on."
    show camila stand fuck pose2 pain
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "Like she wants me to go harder and faster."
    "Before Camila was using her mouth to speak words of encouragement."
    show camila stand fuck pose2 pleasure
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "But now she only seems to be capable of making sounds of carnal pleasure."
    "And when that fails, she begins to kiss the side of my neck."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "Not gently or with any delicacy though."
    "So it comes as little surprise when she starts biting a moment later."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose1 at startle(0.05,-10)
    "Rather than putting me off, this has the opposite effect."
    "Every time I feel Camila's teeth against my skin, I go harder."
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    pause 0.25
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    "Each bite earns her more effort on my part."
    show camila stand fuck pose2
    pause 0.15
    show camila stand fuck pose3
    pause 0.25
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    "And I'm sure she only bites harder to make me fuck her harder in turn."
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    pause 0.2
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    "Finally I begin to feel like I'm coming to the end."
    "We're fucking frantically and with desperate abandon."
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    pause 0.2
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    "And that can only mean that we're going to lose it in the same manner."
    show camila stand fuck pose2 ahegao
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    pause 0.2
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 at startle(0.05,-10)
    pause 0.2
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 with hpunch
    pause 0.2
    show camila stand fuck pose2
    pause 0.1
    show camila stand fuck pose3
    pause 0.2
    show camila stand fuck pose2
    pause 0.05
    show camila stand fuck pose1 with hpunch
    "Without any chance to pause or even think, I let go."
    with hpunch
    "There's nowhere for Camila to go, so she takes it as deep as possible."
    with hpunch
    "Now she's biting me so hard that she must be drawing blood."
    with hpunch
    "And I can feel that she's cumming too."
    show camila stand fuck pose2
    "It takes all of my strength not to drop her as this is going on."
    show camila stand fuck pose3 creampie with hpunch
    "I'm leaning into her as much as I dare, using the wall to help."
    "And even when it's over I can't let go of her."
    "Camila's arms stay around my neck, her head on my shoulder."
    scene bg alley
    show camila casual flirt bottomless nojacket at center, zoomAt (1.5, (640, 1040))
    with fade
    "But her legs fall from around my waist, her feet touching the ground."
    "Even so they don't seem able to support her weight."
    "So I hold her up as she recovers."
    hide camila
    show camila casual flirt
    with fade
    "Neither of us speaks as we walk out of the alley together."
    "I don't know whether that's because Camila's exhausted."
    "Or if she's embarrassed at how much she revealed to me back there."
    "Whatever the reason, I keep quiet."
    "Better to let that one well enough alone for now."
    $ camila.sexperience += 1
    return

label camila_redo_undercover:
    mike.say "Detective Foglio!"
    show camila surprised
    camila.say "It's you?!"
    show camila annoyed
    camila.say "I thought you didn't want to pursue all this."
    mike.say "I can't let you down on this. I'm ready now!"
    show camila smile
    camila.say "Nice to hear!"
    $ game.flags.undercover = True
    return

label camila_event_01_alt:
    scene bg alley
    with fade
    "The alley smells like rain and old takeout. Neon from the main street throws a thin, sickly light between dumpsters. I'm cutting through to save time, hands in my pockets, thinking about nothing in particular."
    show camila angry card at dark, center, zoomAt(1.0, (640, 720)) with easeinleft
    "Policewoman" "Stop! Hands where I can see them."
    hide camila
    show camila upset card at center, zoomAt(1.0, (640, 720))
    with dissolve
    "A woman steps out from the shadow of a delivery door, badge half visible, gun levelled with a practised calm. Her voice is low and controlled, the kind that has stopped people before."
    show camila angry
    "Policewoman" "Don't move. You're under arrest."
    show camila upset at center, traveling (1.5, 0.5, (640, 1040))
    "Her badge precises that she is Detective Camila Foglio."
    "Before I can ask a question she has me against the brick. Cuffs click. Her grip is efficient, not rough, but absolute. I don't know why I'm being held. My heart kicks."
    if game.flags.dwaynedead:
        "Damned. How could they now about Dwayne?"
    if game.flags.ryandead:
        "Have they found a link between me and Ryan's little accident?"
    show camila talkative -card
    camila.say "We've been looking for your for while now, knew you'd pass this way."
    show camila annoyed
    if game.flags.dannydead:
        "Shit! Danny's territory was nearby. How stupid was I to come here!"
    with fade
    "She reads me my rights like a script. This all unfolding in a rush."
    "She calls it in on her radio."
    show camila talkative
    camila.say "I have Luca Costella. The Paperboy, in custody and under arrest."
    show camila normal
    if game.flags.dwaynedead or game.flags.dannydead or game.flags.ryandead:
        "Who the fuck is Luca Costella? Looks like I may have a chance to avoid jail!"
    "Her certainty is a physical thing. She believes she has him. I try to explain, but the words feel small in my mouth."
    mike.say "I'm... [hero.name]... not Luca..."
    mike.say "I think you have the wrong person."
    show camila angry
    camila.say "Tell that to the judge. I can see it's you, I studied your numerous mug shots. You've shaven and cut your hair but it's you."
    show camila upset
    "She doesn't waste time. She's back on the radio and calls for a patrol car. The alley feels colder. I watch her, trying to read her face. There's no doubt in it."
    show camila talkative
    camila.say "Patrol to alley three. One in custody. Send transport for pickup and processing for arrest to jail."
    show camila annoyed
    "The sound of the radio is a small, final thing. I realize I'm being taken in. I don't know why, or who this Luca guy is. I don't know what I did. The city hums around us and I feel very small."
    scene bg alley at center, zoomAt (1.5, (540, 1040)) with fade
    pause 0.3
    show luca teaser at dark, center, zoomAt (0.75, (940, 720)) with easeinright
    "Footsteps echo from the far end of the alley. A figure steps into the neon spill - long hair messy hair, a beard. He moves like someone who has spent years in bad weather. He stops when he sees us."
    scene bg alley
    show camila surprised at center, zoomAt(1.5, (540, 1040))
    with fade
    "She turns to the newcomer, a shocked expression lighting up her face."
    camila.say "There. That's him!"
    show camila annoyed
    pause 0.3
    scene bg alley at center, zoomAt (1.5, (540, 1040))
    show luca teaser at dark, center, zoomAt (0.75, (940, 720))
    with fade
    "The man doesn't approach. He just watches, cigarette glowing in the dark. Up close, side by side, the resemblance is uncanny. Same bone structure, same build, same set to the mouth."
    "The differences are his long hair, beard, and his brown eyes where mine are grey."
    scene bg alley
    show camila surprised at center, zoomAt(1.5, (540, 1040))
    with fade
    "For a second I think the world tilts. The woman who cuffed me looks from the man to me and back again. Her jaw tightens. The certainty in her voice cracks."
    show camila angry card at center, traveling (1.0, 0.3, (740, 720))
    pause 0.3
    hide camila with dissolve
    "In an instant she has her gun and badge out!"
    camila.say "Luca Costella, you are under arrest!"
    "She steps forward, in an instant she has him against the wall with cuffs on. The patrol car's lights flash in the distance. The courier, Luca, The Paperboy, has his gaze fixed on me, eyes never leaving me."
    mike.say "So... you arrested me because I look like him?"
    show camila angry at center, zoomAt (1.0, (740, 720)) with dissolve
    show camila at center, traveling (1.5, 0.5, (640, 1040))
    camila.say "I arrested you because you fit the description and you were in the area. I believed I had him. I was wrong."
    show camila annoyed
    show layer master at police_lights
    with dissolve
    "She takes a breath, the kind that sounds like an apology in the making. The patrol car pulls up and two officers get out, cautious, hands near their belts."
    "She removes the hand cuffs from me."
    show camila angry
    camila.say "We'll take you in for processing. We need to clear this up. Come with us."
    show camila upset
    play sound car_door
    scene bg alley night at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (640, 1080))
    show layer master at police_lights
    "They lead me to the patrol car. The courier watches, expression unreadable."
    "In the back of the car I sit watching the city sliding by in wet streaks. I feel ridiculous and exposed."
    $ game.room = "policestation"
    scene bg policestation with fade
    "At the station the paperwork is a slow, bureaucratic thing. An officer takes my statement while Camila watches, fingers steepled in deep thought."
    show camila blush at center, zoomAt(1.25, (640, 880)) with easeinright
    "The woman who cuffed me looks embarrassed in a way that makes her human."
    show camila talkative
    camila.say "I'm Detective Foglio, I'm sorry. I thought you were him. I don't like being wrong."
    show camila normal
    "She slides a paper cup of coffee across the table. It's black and too hot. The gesture is small and oddly intimate after the alley."
    show camila normal
    camila.say "Listen. I shouldn't have arrested you in the alley without more. I own that. But now that we're here, I have to be practical."
    show camila normal
    mike.say "What do you mean?"
    show camila flirt
    camila.say "Luca - The Paperboy - is in custody. That means the hand off is happening. The family only uses a courier on critical matters."
    camila.say "If they called in the Paperboy it means something big is going down. We need to know what's in that package."
    show camila normal at center, traveling (1.75, 0.5, (640, 1140))
    "She leans forward, voice low and careful. The station hums around us. I can see the case files on her desk, the way she keeps everything within reach."
    show camila flirt
    camila.say "So... I could process you as a witness and send you home. Or... I could use the fact that you look exactly like him."
    show camila normal
    "She studies me a long moment before continuing."
    show camila flirt
    camila.say "You'd be a replacement courier. We dress you up to look like him, wig, fake beard, brown contacts, you take the package and bring it to us, you don't open it, you come back."
    camila.say "I watch from a distance. If anything goes wrong, we move in. No risk."
    show camila normal
    "She watches me like she's measuring whether I will break. Sliding a burner phone towards me."
    menu:
        "Agree to help Camila undercover":
            $ game.flags.undercover = True
            show camila happy
            $ camila.love += 4
            camila.say "Good. We'll make you look the part. Wig, fake beard, brown contacts. You're in good hands."
            show camila talkative
            camila.say "Keep your head down. You follow my lead and you don't open the package. If anything goes wrong, just hit dial on the burner and we move in."
            show camila normal
            mike.say "I don't know how to do this, but... okay."
            show camila talkative
            camila.say "You don't need to be an expert. You need to be convincing for a few minutes."
            camila.say "Come back to the station tomorrow, everything will be ready."
            show camila normal
            "She stands and offers a hand to help me up. The apology is still there, but now it's mixed with a plan."
            $ game.flags.undercoverdelay = TemporaryFlag(True, 1)
            show screen message(title="⚠️ WARNING ⚠️",what="Undercover work is not easy and could end badly.\nWe advise you to make a save before progressing further in this story.")
            pause
            hide screen message
        "Refuse and walk away (You might never meet Camila again)":
            "I look down and give the smallest shake of my head."
            $ camila.love -= 1
            $ game.flags.undercover = False
            show camila whining
            camila.say "I understand. You were arrested unfairly. If you walk away now, I'll file you as a witness and the case will proceed without you."
            show camila normal
            mike.say "I can't do it. I can't be dragged into this."
            show camila talkative
            camila.say "Then go home. No one knows you were part of this, you'll be fine. I'll have a patrol car drop you off at your home."
            show camila normal
            "I nod, the coffee cooling between my hands."
            hide camila with easeoutright
            "The trip home in the patrol car is quick and painless."
            $ game.room = "livingroom"
            show bg livingroom with dissolve
            "In a few moments I'm unlocking my front door and find myself back in my livingroom, the whole event seems rather unreal."
    return

label camila_event_02_alt:
    show bg policestation
    show camila normal zorder 2 at center, zoomAt(1.25, (640, 880))
    with fade
    "Camila gives me a quick rundown in a small briefing room. She marks the map of the Maid café where the meet will happen, the back room, the exit routes."
    show camila angry
    camila.say "We'll make you look like Luca. If anyone asks about the package, say it's routine."
    camila.say "Pay attention to who's there, the dynamic of the family, having someone on the inside will be invaluable."
    camila.say "We'll do a full debrief after."
    camila.say "Get the package, get out. We'll be watching."
    camila.say "Any questions?"
    show camila upset
    menu:
        "Who are we expecting to be at the meeting?":
            show camila talkative
            camila.say "Good question [hero.name], it should be a small meet: you, most likely one of the family's Captains who's hand you the package."
            show camila angry
            camila.say "And most likely a goon or two, just muscle."
            camila.say "These things tend to be over in a few minutes, keep it professional and brief."
            show camila normal
            $ camila.love += 1
            $ camila.sub += 2
        "What is inside the package?":
            show camila angry
            camila.say "That is the question, it must be something important to call in The Paperboy. Could be documents that could incriminate them, or some new drug they are about to start pushing."
            show camila upset
            "She shrugs, whatever it is, we want it."
        "Am I being paid for this?":
            show camila annoyed
            "She studies me a moment then nods."
            show camila angry
            camila.say "Sure we can get you an informant fee of $200 for a few minutes work."
            show camila upset
            $ game.flags.undercover_reward = True
            $ camila.love -= 1
            $ camila.sub -= 1
        "Nah! I got this, easy!":
            "She studies me."
            $ camila.sub += 4
            show camila angry
            camila.say "Glad you're feeling confident [hero.name] but take it seriously too please. This could really help us and be a big step to bringing down the crime family in the city."
            show camila upset
    "With that she escorts me to a room to start preparing for the meet."
    show camila talkative
    camila.say "[hero.name] this is Violaine, she is a civilian who helps when needed, she will help you apply the wig and beard properly."
    show violaine zorder 1 at blacker, center, zoomAt(1, (1100, 720))
    mike.say "Hello there Violaine, thanks for the help."
    "She simply looks at me, and offers a half smile."
    show camila talkative
    camila.say "I'll leave you to it then."
    hide camila with easeoutright
    "With that she leaves."
    show violaine zorder 1 at blacker, center, traveling(1.25, 0.5, (640, 880))
    "Violaine isn't the talkative type but she seems to know what she is doing at least."
    "She has me take a seat and then starts to attach the beard."
    "Trimming and making some adjustments so it looks exactly like the photos they just took of The Paperboy who is now in custody."
    "She moves onto the wig next, using tiny hairpins so it sits snug, with no chance of coming off."
    "Finished with those, I stand and look at myself in the mirror."
    "The resemblance is striking... I am the man from the alley..."
    "Violaine hands me the case with the brown contact lenses, the finishing touch."
    "I insert them."
    "Turning my eyes from grey to brown."
    scene bg policestation at blur(16), dark
    show violaine at blur(16), blacker, center, zoomAt(1.25, (640, 880))
    with dissolve
    "But when I put the contacts in everything goes blurry"
    violaine.say "It's all we had on short notice..."
    if hero.knowledge >= 50:
        "No way, I can't see with these, I'll risk the eye colour change."
        "I must keep my senses as sharp as possible if I want to get out of this alive."
        $ game.flags.undercover_contact_lens = False
        "I remove the brown eye contacts"
        scene bg policestation at blur(0)
        show violaine zorder 3 at blacker, center, zoomAt(1.25, (640, 880))
        with dissolve
        "Most people won't notice right?"
    else:
        menu:
            "Keep the contacts in to match Luca's brown eyes":
                "I need to look exactly like him if I want to get away with this."
                $ game.flags.undercover_contact_lens = True
                "So I decide to keep the contacts in"
            "Remove them, it's a risk but being able to see is more important" if hero.has_skill("investigator"):
                "No way, I can't see with these, I'll risk the eye colour change."
                $ game.flags.undercover_contact_lens = False
                "I remove the brown eye contacts"
                scene bg policestation at blur(0)
                show violaine zorder 3 at blacker, center, zoomAt(1.25, (640, 880))
                with dissolve
                "Most people won't notice right?"
    violaine.say "You're all set..."
    "She pauses and touches my arm..."
    violaine.say "Good luck tonight [hero.name]."
    "And with that she leaves."
    hide violaine with easeoutright
    if game.flags.undercover_contact_lens:
        show camila normal at blur(16), center with easeinright
    else:
        show camila normal with easeinright
    "Detective Foglio returns, pausing to look me over."
    show camila talkative
    camila.say "Looking great, no wonder I had the two of you confused."
    show camila normal
    "She pauses, taking a moment before speaking."
    show camila whining
    camila.say "Hey listen [hero.name], you don't have to do this. I'll be there the whole time. But..."
    camila.say "I can't say there isn't risk here, you're just a civy, there is no shame in backing out."
    show camila annoyed
    "(This is your last chance to back out. It is strongly suggested you are in NG+ and have good stats to go undercover)"
    menu:
        "I got this!":
            "I give my cockiest smirk."
            mike.say "Nope I'm all in for you Detective."
            if game.flags.undercover_contact_lens:
                "Maybe its a good thing everything is blurry with these contacts in so I can't see her reaction that might break my confidence"
            else:
                show camila flirt
                "She give me a small smirk that lingers."
            $ camila.love += 1
            $ camila.sub += 2
        "Yeah on second thought... I think I'm not ready for it yet...":
            "This is all a bit much, the arrest, how that criminal looked just like me."
            mike.say "Sorry Detective, I can't do this. It's not me."
            show camila whining
            camila.say "Fair enough, I get it, you can return the disguise and you're free to go [hero.name]."
            hide camila with easeoutright
            "I remove the disguise"
            $ game.flags.undercover = False
            "I walk away from it all, the alley and the woman who offered me a dangerous choice. The city keeps turning."
            $ game.room = "livingroom"
            show bg livingroom at blur(0)
            "I go home, lock the door, and try understand all that just happened."
            return
    show camila talkative
    camila.say "One more thing. Don't try and be a hero here [hero.name]. Get the package, get out, simple."
    show camila flirt
    camila.say "Don't get injured, I don't want to fill out the mountain of paperwork."
    show camila normal
    "I nod. Outside, the city moves on, unaware of the small, dangerous plan being set in motion."
    if game.flags.undercover_contact_lens:
        show bg street at blur(16)
    else:
        show bg street with dissolve
    "The night closes in as we leave the station with a burner in my pocket, a fake beard and wig on me. The case is no longer someone else's story. It's mine."
    return

label camila_event_03_alt:
    $ renpy.dynamic("meeting_chance", "blur_strength", "cash_taken")
    $ meeting_chance = 0
    $ blur_strength = 16 if game.flags.undercover_contact_lens else 0
    show bg street at blur(blur_strength) with fade
    "The wig itches. The fake beard scratches my jaw. I look like Luca Costella's twin from a bad dream, but it's enough to fool someone who doesn't look too closely."
    show camila normal at blur(blur_strength), center, zoomAt(1.5, (640, 1040))
    with fade
    camila.say "Remember: in and out. No small talk. No jokes. No heroics."
    show camila upset
    mike.say "I know. Get the package. Leave."
    show camila angry
    camila.say "And don't die. I'm serious."
    show camila upset
    "She adjusts the collar of my jacket like she's straightening evidence on a table. Her fingers linger for half a second, I'm not sure if it softness, concern or just precision."
    show camila angry
    camila.say "We'll be across the street. If anything feels wrong, just hit dial on the burner, it's silent."
    show camila normal
    "I nod, swallow, and head over to the maid café."
    hide camila with dissolve
    "The maid café is dark except for a single neon sign buzzing in the window. CLOSED. Perfect for a handoff."
    "I knock twice, like Camila told me. My heartbeat is louder than my fist."
    "A bolt slides. The door cracks open."
    show dwayne zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (1100, 740))
    "Thug" "You're late."
    "His breath smells like cheap beer and mint gum. He looks me up and down, eyes lingering on the beard. My stomach tightens."
    if hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "Alright, now it's not the time to look suspicious."
        "Let's just not say anything weird and it should be fine."
        hide black with dissolve
    menu:
        "Make up an excuse":
            mike.say "Traffic was bad"
        "Stay silent":
            "I meet him with a stoic gaze and say nothing."
            $ meeting_chance += 20
        "Blame the long narrative from the game you were playing":
            mike.say "I was gaming and had to finish the chapter."
            $ meeting_chance -= 20
    "Thug" "Boss hates waiting. Get in."
    "He steps aside. I slip inside."
    scene bg maidcafe at blur(blur_strength)
    show dwayne zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (300, 740))
    show dwayne zorder 3 at blacker, blur(blur_strength), center, traveling(1, 5.0, (1140, 740))
    if game.flags.undercover_contact_lens:
        "Everything is still blurry with these contacts and I'm starting to regret the decision."
        "I bump into a chair which causes the thug to stop and look me over."
    else:
        "The café looks wrong without customers, empty tables, chairs stacked, the smell of sugar and disinfectant hanging in the air."
    "Thug" "Move."
    "He nudges me forward with two fingers. Not a shove, a reminder. I'm not in control here."
    if 'fafwm' in DLCS:
        show bg maidcafeback at blur(blur_strength)
        "He leads me through the café and into the back room where the lights aren't as bright."
        $ meeting_chance += 20
    else:
        show bg maidcafe at blur(blur_strength)
    show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(0.9, (600, 740))
    show ryan date zorder 3 at blacker, blur(blur_strength), center, zoomAt(0.9, (900, 720))
    with fade
    "She sits at the center of it all."
    "Classy, composed, and more dangerous than anyone in this room."
    "She wears a fitted black dress, pearls at her throat, and an expression that could cut glass. Her legs are crossed, posture perfect, a glass of red wine untouched beside her."
    show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(1.0, (600, 740)), startle
    "Crime Boss" "Luca. Late."
    "Her voice is smooth, low, and irritated, but not at me. Not entirely. Something else simmers under the surface."
    "She doesn't give me the chance to reply."
    "She lifts one eyebrow. The room goes still. Two men stand behind her, the muscle, silent and watchful."
    "She taps a manicured nail against the table. The sound is soft, but it hits like a warning shot."
    show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (600, 740)), startle
    "Crime Boss" "You know I despise waiting."
    "I swallow. Hard. Luca probably would've smirked or shrugged. I try to channel that."
    mike.say "Won't happen again."
    "Her eyes narrow. She studies me, the beard, the wig, my eyes."
    if game.flags.undercover_contact_lens:
        "I pray the lighting is kind to my disguise."
    else:
        "I pray the lighting is kind and doesn't betray my eye colour is wrong."
        $ meeting_chance -= 5
    show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (600, 740)), startle
    "Crime Boss" "It's been what 2 years now?"
    if hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "That long? Really? Or is that just a figure of speech?"
        "In any case it's best to go with what she says..."
        hide black with dissolve
    "My stomach drops. I force my voice lower."
    menu:
        "Yeah, 2 years. Time flies uh!":
            $ meeting_chance += 10
        "Something like that.":
            pass
        "I haven't been counting.":
            $ meeting_chance += 20
        "3 years and 11 months actually. I'm a courier so time matters to me.":
            $ meeting_chance -=20
            "She frowns, there is the smallest flick of an eye, but then its gone."
    "She leans back, crossing her arms. The pearls catch the light like tiny threats."
    "She lifts a slim hand."
    "One of the muscle steps forward, placing a sleek black courier bag on the table. Heavy. Too heavy for anything innocent."
    show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (600, 740)), startle
    "Crime Boss" "Take it, you okay with those instruction?"
    "I step forward and take the heavy courier bag, turn it to read the label."
    if game.flags.undercover_contact_lens:
        "I try and focus to read the label... the instructions, but with these contacts it just a blur."
        "The moment lingers, heavy."
        "I try deflect not been able to read it."
        mike.say "Yeah easy enough, it will be done."
        "Her eyes linger on me..."
        "She can tell something is off..."
        show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (600, 740)), startle
        "Crime Boss" "What does it say?"
        if hero.charm >= 50 and hero.fitness >= 50:
            "I must get rid of those damned contacts."
            mike.say "ATCHOO!!!" with vpunch
            pause 0.3
            scene bg black
            "I make my most convincing sneeze performance."
            "And while I lean forward with my hands on my face, I quickly wipe out the contacts from my eyes, keeping them in the palm of my hand."
            $ blur_strength = 0
            if 'fafwm' in DLCS:
                scene bg maidcafeback
            else:
                scene bg maidcafe
            show kiara date zorder 3 at blacker, center, zoomAt(0.9, (600, 740))
            show ryan date zorder 3 at blacker, center, zoomAt(0.9, (900, 720))
            show dwayne zorder 3 at blacker, center, zoomAt(1, (1140, 740))
            with dissolve
            "Thug" "Bless you!"
            "The boss gives her reflexively polite minion, a furious look, then turns her gaze towards me."
            mike.say "Sorry about that... Where were we? Oh, right.."
            "I read the label and nod."
            mike.say "Warehouse 7 down on 8th avenue at 10pm tomorrow. I know the drill."
            $ meeting_chance += 20
        else:
            "I swallow hard, silently cursing the contacts."
            "Trying again to get out of this."
            mike.say "Seems clear enough, you can trust me."
            "She rises from her seat, the two men at her side tensing."
            show kiara date zorder 3 at blacker, blur(blur_strength), center, zoomAt(1, (600, 740)), startle
            "Crime Boss" "What does it say Luca?"
            "The tension in the room makes my skin prickle."
            "I look down, deciding to make something up..."
            "While I slip my hand into my pocket to press dial on the burner."
            with screenshot
            play sound gun
            "The gun shot sounds distance, unreal."
            scene black with fade
            "My last action is pressing the little button on the burner before the world fades."
            "As a consolation prize, the crime boss and her goons are arrested for my murder when Camila and her team bash down the door moments later."
            "Being a hero is hard."
            $ renpy.full_restart()
    else:
        "I read the label and nod."
        mike.say "Warehouse 7 down on 8th avenue at 10pm tomorrow. I know the drill."
        $ meeting_chance += 20
    "She slides an envelop of cash towards me."
    show kiara date zorder 3 at blacker, startle
    "Crime Boss" "You get the rest when the package is delivered."
    menu:
        "Take the cash":
            "I reach out and take it, slipping it into my pocket."
            $ hero.money += 5000
            $ meeting_chance += 20
            $ cash_taken = True
        "That is blood money, I'm not taking it.":
            "I shake my head."
            mike.say "I'm a man of honour, pay me in full when I have the job done."
            $ meeting_chance -= 20
            $ cash_taken = False
            "She considers me but nods slowly, the money left on the table."
    "That out the way she pauses, giving me a hard look, her mind turning."
    "When she speaks her voice is soft, warm but I know there is something behind it."
    show kiara date zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Crime Boss" "So tell me Luca... how is that ailment of yours? What was it again?"
    "The room tightens around me. The muscle shift their weight. One of them rests a hand on his jacket, where a gun waits."
    "She watches me with a calm, deadly patience."
    "My mind whirls... this feels like a trick question."
    show kiara date zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Crime Boss" "Well Luca? I don't have all night."
    if hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "A what now!? Why does she care in the first place?!"
        "Damn it... Do I have to make up something?"
        "What ailment could Luca have?"
        "Does it have something to do with him being a smoker?"
        hide black with dissolve
    menu:
        "Make something up about a cough":
            "The only thing I can think of is Luca smoking in alley... would make sense he has smoker cough?"
            mike.say "Do you mean my cough... smokes will do that. Nothing to worry about."
            "I brush it off."
            $ meeting_chance += 20
        "Make something up about a war wound":
            mike.say "Oh that old war wound, yeah still bothers me on cold rainy days like today."
            $ meeting_chance -= 20
        "Make something up about a bullet wound":
            mike.say "My old bullet wound, nah its fully healed, kinda proud of the scar though."
            $ meeting_chance -= 20
        "Be as vague as possible":
            "This feels like a test, but maybe I can bluff my way out."
            mike.say "Yeah still bothers me from time to time, worse on rainy days like today but nothing to worry about Ma'am"
            $ meeting_chance -= 10
    if (hero.knowledge + hero.charm + meeting_chance) >= 200:
        "She considers me a for a hard moment before her shoulders relax."
        show kiara date zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
        "Crime Boss" "I still remember your first job, my husband didn't think you had it in you."
        "She sighs..."
        show kiara date zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
        "Crime Boss" "I'm the one that vouched for you, changed his mind."
        "She looks up and our eyes meet."
        "Don't disappoint me on this one Luca..."
    else:
        "Her sharp eyes focus on me, considering before disappointment flashes in her quite beautiful eyes."
        "She clenches her hand in to a tight fist."
        with screenshot
        play sound gun
        "The gun shot sounds distance, unreal."
        scene black with fade
        "My last action is pressing the little button on the burner before the world fades."
        "As a consolation prize, the crime boss and her goons are arrested for my murder when Camila and her team bash down the door moments later."
        "Being a hero is hard."
        $ renpy.full_restart()
    "With that, she motions for me to leave."
    show kiara date zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Crime Boss" "...and Luca. Don't be late."
    "One of the goon ushers me out."
    hide kiara
    hide ryan
    hide dwayne
    show bg street
    with fade
    "The door clicks shut behind me and the neon buzz of the café feels like a memory."
    "Night air hits my face, cold, sharp, honest. The courier bag is heavy in my hands, its zipper whispering promises I don't want to hear."
    "Now is my chance if I want to take a peek inside the courier bag..."
    menu:
        "Peek inside":
            "Just a small peek won't hurt, no way Camila will know..."
            "The zipper slides easy enough, the silhouette of a small calibre sub-machine gun, lay nestled in the bag."
            with screenshot
            play sound gun
            "The gun shot sounds distance, unreal."
            "They must of been watching, a courier is paid to never..."
            scene black with fade
            "Everything fades..."
            "Being a hero is hard."
            $ renpy.full_restart()
        "Don't open it":
            "I told Camila I wouldn't, I'm a man of my word."
    scene bg taxi
    show camila upset at center, zoomAt(1, (340, 720))
    with fade
    "Across the street, under a sodium lamp, Camila's car idles. The team is there, silhouettes, radios, the quiet hum of people holding their breath."
    "Even from here I can tell she's not entirely composed. Her jaw is tight. Her hands are on the wheel."
    show camila whining
    camila.say "You okay?"
    show camila annoyed
    mike.say "Yeah. Got it."
    "Her eyes flick to the bag and back to me. There's something like eagerness in the way she watches, not triumph, not exactly relief, but a raw need to know what happened in there."
    show camila angry
    camila.say "Tell me everything. Now."
    show camila upset
    mike.say "The boss is a female, Classy as hell with an intelligence to match. She sat like she owned the room."
    mike.say "She asked me a bunch of question, I said what Luca would say. She let me take the bag."
    show camila angry
    camila.say "And the rest?"
    show camila upset
    mike.say "Two muscle large guys. No fuss. She said to meet at Warehouse 7, down on 8th Avenue, ten o'clock tomorrow night."
    show camila talkative
    camila.say "Warehouse 7. 8th. Ten. Good. That gives us a window."
    show camila upset at center, traveling (1.5, 0.3, (640, 1040))
    "Camila reaches for the zipper with the same careful, clinical motion she uses on evidence. The streetlight catches the metal teeth as she parts them."
    show camila sadsmile
    camila.say "Let's see what they were moving."
    show camila upset
    "The bag opens. Inside, is a compact, small-calibre sub-machine gun, slick, cold."
    "She taps her finger to her lips, in thought a moment."
    show camila angry
    camila.say "I'm guessing this has someone's fingerprints and DNA all over... they are trying to take someone out, maybe a rival crime family."
    camila.say "This is bigger than I thought."
    show camila upset
    mike.say "Yeah. That's not just courier stuff."
    show camila normal
    "She turns to the team, speaking in her walkie-talkie."
    show camila angry
    camila.say "Team, we're done here for the night, we will debrief at eight hundred hours at the station tomorrow."
    camila.say "Good work team, a successful op is one where no shots are fired."
    show camila upset
    "The radios crackle as the team responses, standing down."
    "Camila's jaw is tight, even her impatience is precise. For a second she looks at me, annoyed, relieved, and something like trust, and then she's already planning the next move."
    if cash_taken:
        "Her look causes me to slip my hands into my pocket, feeling the pile of cash I walked away with."
        menu:
            "Hand the 5K over to her":
                mike.say "Oh Detective, they gave me this pile of cash as part payment."
                "I hand it over to the Detective."
                $ hero.money -= 5000
                $ camila.love += 2
            "She doesn't need to know about it...":
                "If she asks I'll hand it over, else I'll keep it."
    "The team disperses in controlled motions, radios crackling as they pack up the scene. The sub-machine gun sits on the hood in an evidence tray, small but vicious, looking under the streetlight."
    "Camila steps closer, arms folded, eyes still sharp from the adrenaline. She studies me the way she studies a crime scene, slow, deliberate, making sure nothing is bleeding or broken."
    show camila angry
    camila.say "You handled yourself well in there."
    show camila upset
    "Her voice is steady, but there's a thread of something else underneath it. Relief, maybe. Or the aftershock of almost losing me."
    mike.say "I got lucky."
    show camila angry
    camila.say "No. You didn't. You kept your head. That's rare."
    show camila upset
    "She glances at the courier bag again, then back at me. The streetlight catches the faintest tension in her jaw."
    show camila talkative
    camila.say "Come to the station tomorrow. Four o'clock. We need to go over everything before the next move."
    show camila normal
    mike.say "4pm. Got it."
    show camila annoyed
    "She hesitates. Camila never hesitates. It's strange seeing it, like watching a statue shift."
    show camila angry
    camila.say "And... I want you with us tomorrow night. For the drop."
    show camila annoyed
    "My stomach tightens. I knew it was coming, but hearing it out loud makes it real."
    mike.say "You sure that's a good idea?"
    show camila sadsmile
    camila.say "You're a natural at this. Better than half the undercover guys we've trained."
    show camila normal at center, traveling (1.75, 0.3, (640, 1140))
    "She steps closer, lowering her voice so the team can't hear."
    show camila normal
    camila.say "You got in, you got out, and you didn't get shot. That's more than most manage on their first run."
    mike.say "I almost got caught."
    show camila wink
    camila.say "Almost doesn't count. You improvised. You survived. That's what matters."
    "Her eyes linger on me for a moment, longer than they should. Then she straightens, the detective mask sliding back into place."
    show camila talkative
    camila.say "Warehouse 7, 8th Avenue. Ten p.m. tomorrow. We'll brief at the station first."
    menu:
        "I'll be there Detective.":
            "She smiles touching my arm."
            $ camila.love += 2
            camila.say "That means a lot to me, and call me Camila, we've been into battle together."
        "This was...a lot... I don't thing I can do it again...":
            show camila sad
            "She considers me, disappointment flashing her eyes."
            camila.say "Yeah I was expecting that, I get it. And call me Camila."
            camila.say "Be safe out there [hero.name], see you around."
            hide camila with easeoutright
            "I remove the disguise"
            $ game.flags.undercover = False
            "I walk away from it all, the alley and the woman who offered me a dangerous choice. The city keeps turning."
            $ game.room = "livingroom"
            show bg livingroom at blur(0)
            "I go home, lock the door, and try understand all that just happened."
            return
    if game.flags.undercover_reward:
        camila.say "Oh and you wanted the informant fee, I'll have them transfer you the money."
        $ hero.money += 200
    "She nods once, decisive. The kind of nod that ends a conversation and starts a mission."
    show camila sadsmile
    camila.say "Get some rest. Tomorrow's going to be worse."
    "She turns toward the car, but not before I catch the faintest flicker of something in her expression, worry, maybe. Or trust. Hard to tell with Camila."
    "The night feels colder as she walks away, the sub-machine gun sealed in evidence, the courier bag empty, and tomorrow's danger already waiting on the clock."
    $ game.room = "street"
    show bg street with dissolve
    return

label camila_event_04_alt:
    if camila.love.max < 40:
        $ camila.love.max = 40
    scene bg policestation with fade
    "The precinct feels different at this hour, quieter, heavier. The kind of quiet that comes before a storm."
    "I check in at the front desk, they direct me to head down the hall."
    show camila normal at center, zoomAt(1.0, (1040, 720)) with dissolve
    "Camila is waiting outside the briefing room, arms folded, posture sharp. But her eyes soften, just a fraction, when she sees me."
    show camila talkative at center, traveling(1.5, 1.0, (640, 1040))
    camila.say "Right on time."
    show camila normal
    mike.say "Wouldn't miss it."
    show camila upset
    "She nods, but there's something in the way she looks at me, like she's checking for cracks, or maybe making sure I'm still in one piece."
    show camila angry
    camila.say "Tonight is going to be dangerous. More dangerous than last night. Warehouse 7 isn't just a handoff, it's a gathering. We need you ready."
    show camila upset
    mike.say "I figured."
    "She reaches into a locked drawer and pulls out a small black case. The weight of it hits the air before she even opens it."
    show camila angry
    camila.say "You're getting a gun."
    show camila upset
    "She says it flat, but her eyes flick to mine, gauging my reaction."
    mike.say "I've handled worse."
    show camila angry
    camila.say "This isn't bravado time. If things go bad, you need to be able to defend yourself."
    show camila upset
    "She snaps the case open. Inside: a compact service pistol, clean and cold."
    show camila angry
    camila.say "Range. Now."
    show bg shootingrange with fade
    "The shooting range smells like cordite and old rubber."
    show camila annoyed at center, zoomAt(1.25, (340, 880)) with easeinleft
    "Camila hands me ear protection and steps close, too close, for someone who claims she doesn't do 'personal.'"
    show camila talkative
    camila.say "Alright. Basics first."
    show camila normal
    if hero.has_skill("shooting"):
        "She watches my grip, my stance, the way I check the chamber. Her eyebrow lifts, impressed despite herself."
        show camila surprised
        camila.say "You've done this before."
        mike.say "A bit."
        show camila sadsmile
        camila.say "Good. Saves me time."
    else:
        "She steps behind me, adjusting my hands with slow, precise movements. Her fingers brush my wrist, professional, but warm."
        show camila talkative
        camila.say "Relax your shoulders. You're too tense."
        show camila normal
        mike.say "Hard not to be."
        show camila wink
        camila.say "Get used to it. Undercover work is ninety percent tension."
    show camila normal
    "She steps back as I raise the gun. The target hangs twenty feet away, a blank silhouette waiting to judge me."
    show camila talkative
    camila.say "Whenever you're ready."
    play sound gun
    "I fire. The shot cracks through the room."
    if hero.has_skill("shooting"):
        "The bullet lands center-mass. Clean. Camila's lips twitch, almost a smile."
        show camila sadsmile
        camila.say "Show‑off."
        $ camila.love += 1
    else:
        "The bullet hits low and left. Camila doesn't flinch, but she steps beside me again."
        show camila talkative
        camila.say "You're pulling. Slow down. Breathe."
        "She guides my stance again, closer this time. I can feel her breath near my ear."
    with screenshot
    play sound gun
    "We run through a few more rounds. The rhythm settles, aim, breathe, fire. Camila watches every movement, her expression shifting between instructor and something softer."
    with screenshot
    play sound gun
    show camila normal
    camila.say "You're improving. Fast."
    mike.say "Good teacher."
    show camila blush
    "She looks away at that, just for a second. A crack in the armour."
    camila.say "Don't get sentimental. We still have a job tonight."
    "But the blush lingers. And she doesn't step back."
    show camila normal
    camila.say "Alright. That's enough for now."
    "She unloads the pistol with practised ease, sets it on the bench, and looks at me with that sharp, assessing gaze she uses on suspects and crime scenes. Except this time... it lingers."
    show camila talkative
    camila.say "We should go over the plan for tonight. No point sending you in blind."
    mike.say "I'm listening."
    $ camila.love += 1
    "She gestures for me to follow her out of the range. We walk down the hallway together, the fluorescent lights humming overhead. Her shoulder brushes mine once, accidental, probably, but neither of us steps away."
    show bg policestation with fade
    "The briefing room is empty except for a whiteboard covered in maps and photos. Warehouse 7 sits circled in red like a wound."
    show camila angry
    camila.say "Here's what we know. The family uses Warehouse 7 for mid-level exchanges. Not the big stuff, but not small either. Enough space so things can get ugly."
    show camila upset
    mike.say "And I'm walking in as Luca again."
    show camila talkative
    camila.say "Yes. But this time you're not alone. We'll be close. Last night was a rush on short notice, this time will be a full tactical team supporting you."
    camila.say "We'll also have full comms this time, so I'll be with you all the way."
    show camila normal
    "She steps beside me, pointing at the map. Her hand is inches from mine. Too close. Not close enough."
    show camila talkative
    camila.say "You'll enter through the south gate. They'll expect you. We'll be staged here, northwest corner. If anything feels wrong, you signal."
    show camila normal
    mike.say "Dial on the burner."
    show camila sadsmile
    camila.say "Good. You remember."
    show camila normal
    "There's a softness in her voice she didn't mean to let slip. She clears her throat, straightens a stack of papers that didn't need straightening."
    show camila angry
    camila.say "Look... tonight is dangerous. More than last night. I wouldn't ask you to do this if I didn't think you could handle it."
    show camila upset
    mike.say "You trust me?"
    show camila sad
    "She freezes for half a second. A tiny, human glitch in the detective façade."
    show camila sadsmile
    camila.say "I trust your instincts. And your... adaptability."
    show camila normal
    "Her eyes flick to mine, then away. She's careful, but not careful enough to hide the tension threading between us."
    show camila talkative
    camila.say "We'll prep gear, run comms checks, and go over your cover story again. We've got time."
    show camila normal
    mike.say "So we're staying here until the meet?"
    show camila talkative
    camila.say "Yeah. You and me. We prep together."
    show camila normal
    "Something in her tone makes the room feel smaller. Warmer. Charged."
    show camila talkative
    camila.say "Let's get to work."
    scene bg black
    $ game.pass_time(6)
    pause 0.5
    $ renpy.dynamic("target", "tactical_advantage", "first_enemy_down", "second_enemy_down")
    scene bg warehouse crates at center, zoomAt(1.0, (640, 720)) with fade
    "Warehouse 7 sits at the end of 8th Avenue like a forgotten tooth, dark, cracked, and humming with the kind of silence that makes your skin itch."
    "The wig scratches my scalp. The fake beard tugs at my jaw. I look like Luca, but I don't feel like him."
    "Camila's voice crackles softly in my earpiece."
    camila.say "We've got eyes on you. Stay calm. Stay Luca."
    mike.say "Copy."
    "I cross the cracked pavement toward the side door. A pair of industrial lamps flickers above it, throwing long shadows across the loading bay."
    scene bg warehouse at center, zoomAt(1.5, (940, 900))
    show danny zorder 3 at blacker, center, zoomAt(0.9, (300, 760))
    show shawn date zorder 3 at blacker, center, zoomAt(0.86, (700, 740))
    with fade
    "Two men stand there, broad shoulders, tactical jackets, the kind of posture that says they've been trained to shoot before they talk."
    show danny zorder 3 at blacker, zoomAt(1, (300, 760)), startle
    "Security Team member1" "The Paperboy?."
    "He says it like a statement, not a greeting. The other man watches me with the kind of stare that weighs you, measures you, files you away."
    mike.say "You wanted the package."
    show danny zorder 3 at blacker, zoomAt(1, (300, 760)), startle
    "Security Team member1" "Then hand it over."
    "I lift the courier bag slightly. The zipper glints under the floodlight. My pulse thumps once, hard."
    "Camila whispers in my ear."
    camila.say "You're doing fine. Keep your cool."
    play sound door_sliding
    show bg warehouse open with dissolve
    "The warehouse loading bay opens."
    show danny zorder 3 at blacker, center, zoomAt(0.9, (290, 760))
    show shawn date zorder 3 at blacker, center, zoomAt(0.86, (850, 740))
    show dylan zorder 3 at blacker, center, zoomAt(0.90, (600, 740))
    with easeinleft
    "The guards step aside, revealing a third man approaching from a stack of shipping crates. He's older, sharper, wearing a tailored coat that doesn't belong in a place like this. His posture screams authority."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Lead" "Evening, Luca."
    "I nod, keeping Luca's lazy confidence in my shoulders."
    mike.say "Evening."
    "He gestures to a metal table set up under the floodlights. A makeshift inspection station."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Lead" "Set it down."
    "I place the courier bag on the table. The sound echoes off the warehouse walls. The security lead studies me for a moment, too long, too carefully."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Lead" "You look... different."
    "My throat tightens. I force Luca's trademark smirk."
    mike.say "Long night."
    "He doesn't smile back. He just nods once to his men."
    show danny zorder 3 at blacker, center, zoomAt(1, (290, 760)), startle
    "Security Team member1" "We'll check it."
    "Pulling on surgical rubber gloves with ease."
    "He steps forward, gloved hand hovering near the zipper. The other shifts his stance, subtly blocking my exit path."
    "Camila's breath catches in my ear."
    "Stand by. Don't move unless you have to."
    "The security lead folds his arms, eyes locked on me."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Lead" "Let's see if the Lady kept her end of the deal."
    "His man grips the zipper."
    "The night feels like it's holding its breath."
    "The guard's fingers close around the zipper. He pulls it open in one smooth motion, the sound slicing through the night like a warning."
    "He reaches inside and lifts the sub-machine gun out with both hands, touching only the ends."
    "The gun looks exactly the same. Camila's identical replacement, she is all about the details."
    show danny zorder 3 at blacker, center, zoomAt(1, (290, 760)), startle
    "Security Team member1" "Looks good so far Sir."
    "He turns it over carefully, checking the grip, the barrel, the finish. His expression doesn't change, but something in his posture tightens."
    camila.say "Easy... just breathe."
    "The guard sets the gun on the table and reaches into his jacket. For a second I think he's going for a weapon. Instead, he pulls out a phone."
    "He taps the screen, scrolling. A reference photo. A serial number."
    "My pulse spikes. Camila never told me they had the number. She didn't know."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Lead" "Go on. Check it."
    "The guard picks up the gun again, turning it so the underside catches the light. He wipes a gloved thumb across the serial plate."
    "The night feels like it's shrinking around me."
    "He squints. Looks at the phone. Looks at the gun. Looks again."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Team member1" "Huh."
    "That single sound hits harder than a gunshot."
    mike.say "Something wrong?"
    "I try to sound bored. Luca-bored. But my voice feels too tight in my throat."
    show danny zorder 3 at blacker, center, zoomAt(1, (290, 760)), startle
    "Security Team member1" "Number's... off... by a lot"
    "He says it quietly, but every man in the loading bay hears it. The air changes. The kind of change you feel in your bones."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 740)), startle
    "Security Lead" "Off how?"
    "The guard holds up the phone and the gun side by side."
    "Camila whispers in my ear, barely audible."
    camila.say "Stay calm. Don't run. Don't reach for anything."
    show dylan zorder 3 at blacker, center, traveling(1.5, 0.3, (600, 1060))
    "The security lead steps closer to me. Too close. His eyes narrow, studying my face, my beard, my wig, my pulse hammering in my neck."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 1060)), startle
    "Security Lead" "Luca... you sure she gave you the right package?"
    "My mouth is dry. The gun at my hip feels heavier than it should. The whole world feels like it's leaning forward, waiting."
    mike.say "That's what she handed me."
    "The guard lowers the gun slowly. His other hand drifts toward his jacket. Not fast. Not threatening. Just... ready."
    "The security lead doesn't blink."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 1060)), startle
    "Security Lead" "Funny thing about her. She doesn't make mistakes."
    "He takes one step closer. I can smell his cologne. Sharp. Expensive. Wrong for a place like this."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 1060)), startle
    "Security Lead" "So if this number doesn't match..."
    "He lets the sentence hang. The tension is a wire pulled tight between us."
    "Behind me, one of the guards shifts his weight. Boots on concrete. A subtle sound, but it hits like a warning bell."
    "Camila's voice is a whisper of steel."
    camila.say "[hero.name]... whatever happens, don't let them get behind you."
    "The security lead's hand moves, slow, deliberate, toward the inside of his coat."
    "Not a draw. Not yet. But close enough that my breath catches."
    show dylan zorder 3 at blacker, center, zoomAt(1, (600, 1060)), startle
    "Security Lead" "Why don't you tell me what's really going on here... Luca?"
    "The guards shift their stance. Boots scrape concrete. A safety clicks off. The night tightens around my throat."
    camila.say "[hero.name]... don't reach for your gun. Not yet."
    mike.say "She gave me the bag. That's all I know."
    show dylan zorder 3 at blacker, center, traveling(1.75, 0.5, (640, 1220))
    "The security lead steps closer, eyes narrowing. He's close enough now that I can see the tension in his jaw."
    show dylan zorder 3 at blacker, center, zoomAt(1, (640, 1220)), startle
    "Security Lead" "She doesn't make mistakes, she gave us the serial number, it doesn't add up. Which means you're lying."
    "His hand moves, fast."
    "I don't think. I just move."
    with screenshot
    hide dylan
    hide danny
    hide shawn
    play sound gun volume 1.2
    show bg warehouse crates at center, traveling(3.5, 0.3, (640, 1280))
    "I dive sideways as the first shot cracks through the night. The floodlights explode in a shower of sparks. I hit the ground behind a stack of metal crates, the impact knocking the air from my lungs."
    camila.say "Go! Go! Move in! [hero.name], stay down!"
    play sound multiple_guns
    "Gunfire erupts across the loading bay."
    "The security team fans out, taking positions behind wooden crates, another by metal crates, one by the concrete pillars supporting the warehouse awning by the loading bay."
    "My heart slams against my ribs. The gun at my hip feels impossibly heavy. I draw it with shaking hands."
    "Camila's voice cuts through the chaos."
    camila.say "[hero.name], listen to me. Stay down they are packing serious heat and are obviously ex-military."
    "I peek around the crate. Three shapes in the dark. Three threats."
    play sound multiple_guns
    "Gun fire rains."
    menu:
        "Stay hidden and wait for Camila to rescue me":
            "Gunfire cracks across the loading bay. I press myself tighter against the crate, heart pounding, breath shallow."
            "If I just stay down... if I just wait... Camila's team will handle it."
            "But the security team moves fast. Too fast. One of them sweeps wide, flanking the crates."
            camila.say "[hero.name], move! You can't stay there! They are moving to flank you!"
            "I freeze. Just one second too long."
            with screenshot
            play sound gun
            show bg warehouse at dark, center, traveling(3.5, 0.3, (600, 880))
            "A shadow looms at the edge of the crate. A muzzle flashes. Pain blooms, sharp and sudden, and the world tilts sideways."
            "Camila's voice breaks through the ringing in my ears, raw, panicked, distant."
            camila.say "[hero.name]! [hero.name], stay with me...!"
            "But the night is already slipping away, the sounds of the firefight fading into a dull, empty hush."
            "Being a hero is hard."
            $ renpy.full_restart()
        "Time to use the gun I've got":
            scene bg warehouse open at center, zoomAt(1.5, (640, 1040))
            show danny at blacker, center, zoomAt(0.5, (600, 820))
            show shawn date at blacker, center, zoomAt(0.5, (800, 820))
            show dylan at blacker, center, zoomAt(0.5, (600, 820))
            show bg_warehouse_crates at center, zoomAt(1.75, (640, 1140))
            show danny at blacker, center, traveling(0.5, 0.5, (390, 720))
            show shawn at blacker, center, traveling(0.5, 0.5, (880, 720))
            show dylan at blacker, center, traveling(0.5, 0.5, (290, 720))
            menu:
                "Shoot at the closest guard behind the wooden crate":
                    $ target = "guard crouched behind the wooden crate"
                    $ target_character = "shawn"
                    $ tactical_advantage = 20
                    "I steady my breath and aim at the [target]."
                "Shoot at the furthest guard by the loading door, behind the concrete pillar":
                    $ target = "guard by the loading door"
                    $ target_character = "dylan"
                    $ tactical_advantage = -10
                    "I steady my breath and aim at the [target]."
                "Shoot at the security lead taking cover by the metal crates":
                    $ target = "lead covering by the metal crates"
                    $ target_character = "danny"
                    $ tactical_advantage = 10
    "I steady my breath and aim at the [target]."
    with screenshot
    play sound gun volume 1.2
    pause 0.3
    if hero.has_skill("shooting") and (hero.fitness + hero.knowledge + tactical_advantage) >= 150:
        $ renpy.hide(target_character)
        with easeoutbottom
        "My shot rings out sharp and controlled. The guard jerks back behind the barrel, dropping his weapon. He's out of the fight."
        $ first_enemy_down = True
    elif hero.has_skill("shooting") and (hero.fitness + hero.knowledge + tactical_advantage) >= 100:
        $ renpy.hide(target_character)
        with easeoutbottom
        "The bullet clips the barrel, sending the guard scrambling. He ducks low, pinned and unable to return fire."
        $ first_enemy_down = True
    elif hero.is_lucky or (randint(1, 100) + hero.fitness + hero.knowledge + tactical_advantage) >= 200:
        $ renpy.hide(target_character)
        with easeoutbottom
        "The recoil nearly throws me, but luck is on my side. The guard yelps and drops behind cover, weapon skittering away."
        $ first_enemy_down = True
    else:
        play sound gun volume 0.8
        scene bg warehouse crates at center, zoomAt(3.5, (640, 1280)) with vpunch
        "My shot goes wide, sparking off the concrete. The guard pops up and fires back, forcing me to duck hard."
        $ first_enemy_down = False
        scene bg warehouse open at center, zoomAt(1.5, (640, 1040))
        show danny at blacker, center, zoomAt(0.5, (390, 720))
        show shawn date at blacker, center, zoomAt(0.5, (880, 720))
        show dylan at blacker, center, zoomAt(0.5, (290, 720))
        show bg_warehouse_crates at center, zoomAt(1.75, (640, 1140))
        with fade
    if first_enemy_down:
        "With the [target] out that just leaves 2 more."
    else:
        if hero.is_unlucky:
            "I lean too far out. A burst of fire slams into the crate inches from my head. Splinters rain down as I pull back."
            "I wonder if the crate has a liquid in, because something wet is leaking onto me."
            scene bg warehouse crates at blood, center, zoomAt(3.5, (640, 1280)) with vpunch
            "I touch my chest and my hand return red, blood red..."
            "The night is already slipping away, the sounds of the firefight fading into a dull, empty hush."
            "Being a hero is hard."
            $ renpy.full_restart()
    menu:
        "Shoot at the guard behind the wooden crate" if target != "guard crouched behind the wooden crate":
            $ target = "guard crouched behind the wooden crate"
            $ target_character = "shawn"
            $ tactical_advantage += 20
        "Shoot at the guard by the loading door" if target != "guard by the loading door":
            $ target = "guard by the loading door"
            $ target_character = "dylan"
            $ tactical_advantage -= 10
        "Shoot at the security lead taking cover by the metal crates" if target != "lead taking cover by the metal crates":
            $ target = "lead taking cover by the metal crates"
            $ target_character = "danny"
            $ tactical_advantage += 10
    "I take a breath and aim at the [target], feeling more confident the second time."
    with screenshot
    play sound gun volume 1.2
    pause 0.3
    if hero.has_skill("shooting") and (hero.fitness + hero.knowledge + tactical_advantage) >= 125:
        $ renpy.hide(target_character)
        with easeoutbottom
        "The shot lands exactly where I want it. Clean, controlled, decisive. The guy jerks back behind cover, weapon slipping from his hand. He's out of the fight before he even knows it."
        $ second_enemy_down = True
    elif hero.has_skill("shooting") and (hero.fitness + hero.knowledge + tactical_advantage) >= 75:
        $ renpy.hide(target_character)
        with easeoutbottom
        "My aim isn't perfect, but it's enough. The bullet slams into the crate beside him, forcing him to duck low. He's pinned, swearing, unable to return fire for now."
        $ second_enemy_down = True
    elif hero.is_lucky or (randint(1, 100) + hero.fitness + hero.knowledge + tactical_advantage) >= 175:
        $ renpy.hide(target_character)
        with easeoutbottom
        "The recoil nearly throws me, but luck leans my way. The round clips his shoulder or maybe just his pride, either way, he stumbles back and loses his angle on me."
        $ second_enemy_down = True
    else:
        "The shot goes wide, sparking off metal. He pops up instantly, firing a burst that forces me to flatten myself behind cover, heart hammering."
        $ second_enemy_down = False
        if hero.is_unlucky:
            "I lean out too far. My grip slips. The gun kicks wild, and before I can recover, a burst of return fire slams into the crate inches from my head. "
            "Splinters rain down as I scramble back, exposed and shaken."
            "I wonder if the crate has a liquid in, because something wet is leaking onto me."
            scene bg warehouse crates at blood, center, zoomAt(3.5, (640, 1280)) with vpunch
            "I touch my chest and my hand return red, blood red..."
            "The night is already slipping away, the sounds of the firefight fading into a dull, empty hush."
            "Being a hero is hard."
            $ renpy.full_restart()
    if first_enemy_down and second_enemy_down:
        "Two of them are already down thanks to my shots. The last one realizes he's alone, pinned between Camila's advancing team and the smoking wreck of his plan."
        "He drops his weapon, hands raised high."
        scene bg warehouse open crates with fade
        "Officers rush in, shouting commands. The man goes face down on the concrete, wrists yanked behind him as cuffs snap shut."
        "Another officer reads them their rights over the ringing echo of gunfire fading into silence."
        "The scene shifts from chaos to control in seconds. Camila's people move with precision, clearing the area, securing weapons, and checking the wounded. The fight is over."
    elif first_enemy_down or second_enemy_down:
        "One of the gunmen is down from my shot, but the others keep firing until Camila's team sweeps in from the flank."
        scene bg warehouse open crates with fade
        "The sudden pressure breaks their line. One drops his rifle and surrenders immediately: the other hesitates, then throws his hands up as officers close in."
        "They're forced to the ground, cuffed, and read their rights while the last echoes of the firefight fade into the night."
        "Camila's team moves fast, securing the perimeter and collecting weapons. The warehouse yard shifts from a battlefield back into a crime scene."
    else:
        "My shots miss, forcing me to stay low as bullets chew into the crates around me. Before the gunmen can press the advantage, Camila's team storms the yard in a coordinated sweep."
        "Flashlights flare. Commands bark through the air."
        "Outnumbered and outmaneuvered, the gunmen break. One tosses his weapon aside and drops to his knees."
        scene bg warehouse open crates with fade
        "The other tries to run but is tackled hard onto the concrete."
        "Within moments they're cuffed, disarmed, and being read their rights while officers secure the scene. The fight ends not with a final shot, but with the cold click of handcuffs."
    "I lower my weapon, breath shaking out of me in a long exhale."
    show camila angry at left with easeinleft
    camila.say "[hero.name]!"
    show camila upset
    "Camila strides toward me, boots crunching over spent casings. Her eyes flick over me, checking for wounds, checking that I'm still standing, before narrowing sharply."
    show camila angry
    camila.say "I told you to stay down. You are not trained for this."
    show camila upset
    mike.say "Yeah, well... staying down didn't seem like a great long-term survival strategy."
    show camila sadsmile
    "Her jaw tightens. She wants to stay angry. She really does. But the corner of her mouth betrays her, just a twitch, a crack in the armour."
    show camila flirt
    camila.say "You're impossible."
    show camila normal
    mike.say "And yet... effective."
    "She exhales, half frustration, half relief. The floodlights catch the faintest warmth in her eyes."
    show camila talkative
    camila.say "Come on. Let's get you back to the station before you start thinking you're invincible."
    scene bg policestation
    show camila normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "The precinct hums with late-night energy, phones ringing, officers typing, evidence bags being logged. Camila leads me into an interview room, shuts the door, and leans against the table."
    show camila talkative
    camila.say "Alright. Here's the full picture, some of this just came back."
    show camila normal
    "She pulls up a file on the tablet, photos, reports, ballistic diagrams."
    show camila talkative
    camila.say "The gun you delivered, the real one, just came back from the lab. Fingerprints, DNA, ballistic scoring... all of it matches the son of a sitting politician."
    mike.say "So this was all about him."
    show camila talkative
    camila.say "Looks that way, well him and his Father."
    show camila normal
    mike.say "And those men tonight?"
    show camila talkative
    camila.say "They were hired to blackmail his father."
    show camila normal
    "She taps the screen, showing a chain of encrypted messages, from their just captured phones."
    show camila talkative
    camila.say "They were going to use the murder weapon as leverage. 'Do what we want, or your son goes to prison.'"
    show camila normal
    mike.say "And the crime boss?"
    show camila whining
    camila.say "She never gave us her name. But she stood to gain political favours, zoning, protection, influence. Not money. Power."
    show camila annoyed
    "Camila closes the tablet, the weight of the case settling between us."
    show camila talkative
    camila.say "Tonight exposed the whole operation. The gun, the blackmail, the political angle. We'll be untangling this mess for months."
    show camila normal
    mike.say "But it's over."
    show camila sadsmile
    camila.say "Because of you."
    show camila normal at center, traveling (1.75, 1.0, (640, 1140))
    "She steps closer, her voice softening in a way I haven't heard before."
    show camila angry
    camila.say "I meant what I said earlier. You aren't trained for this. You scared the hell out of me out there."
    show camila upset
    mike.say "But I got the job done."
    show camila normal
    "She looks up at me, really looks, and the air shifts. Warmer. Closer."
    show camila happy
    camila.say "Yeah. You did."
    show camila normal
    "Her hand brushes my arm, light, almost accidental, but not really."
    show camila sadsmile
    camila.say "Keep in touch, okay? I'm serious. This... all of this... was possible because of you."
    show camila normal
    mike.say "You'll hear from me."
    "She smiles, small, genuine, and more dangerous than any gun I faced tonight."
    show camila wink
    camila.say "Good. I'd hate to think this was a one-time thing."
    show camila normal
    "The case is closed. The danger's passed. But something else, something new, hangs in the air between us."
    "And for the first time tonight, I'm not afraid of it."
    hide camila
    $ game.room = "livingroom"
    show bg livingroom
    with fade
    "I return home, pausing a moment and think about what just happened..."
    "I really stepped up and did my part for my city, how many people will be safer because of my actions."
    "Crime will be just a little lower, a little less corruption in our city because of me."
    $ camila.unhide()
    $ camila.love += 6
    $ camila.sub += 4
    if not hero.has_skill("shooting"):
        $ hero.gain_skill("shooting")
        "After all that, I sure feel more comfortable around guns."
    return

label camila_pregnant_request:
    show camila at center, zoomAt (1.25, (640, 880)) with fade
    "Dealing with Camila can be a pretty tricky prospect when you take into account her contradictory nature."
    "What I mean by that is on the one hand she gives off the impression of being a tough, no nonsense cop."
    "You get the impression that she always says what she means and wears her heart on her sleeve."
    "But it doesn't take you long to realise that she's actually one seriously smart cookie."
    "And that's why she's so good at her job, the intelligence underneath the tough exterior."
    "The only problem is that it kind of leaves me guessing a lot of the time when we're together."
    "Like, is she pulling the same act with me, or is she actually being up-front about her feelings?"
    "And sometimes, you just have to poke the bear and then hope you don't get mauled too badly."
    mike.say "Camila..."
    show camila surprised
    camila.say "Huh?"
    show camila normal
    mike.say "Is everything okay?"
    show camila bored
    camila.say "What kind of a question is that?"
    camila.say "Does it look like there's something up?"
    show camila sadsmile
    mike.say "Well, you're snapping at me like someone you just busted for possession..."
    mike.say "So I'm going to go out on a limb and say that there is."
    show camila annoyed
    "Camila's brows furrow and she narrows her eyes, like she's about to launch into a tirade."
    "But then she seems to remember who she's talking to, and the annoyance drains out of her."
    show camila angry
    camila.say "Ah, dammit..."
    show camila talkative
    camila.say "I've been around you so long, you can read me like a frickin book!"
    show camila normal
    mike.say "So what?"
    mike.say "There is something wrong?"
    mike.say "When were you going to tell me?"
    show camila annoyed
    "Camila shakes her head and holds up a hand, trying to stop me going down that lone of reasoning."
    show camila talkative
    camila.say "It's not like that, [hero.name]…"
    camila.say "I don't have something to tell you, like a confession or anything."
    show camila whining
    camila.say "But what I do have is...something to ask you."
    show camila sadsmile
    "Well now I'm more than a little intrigued."
    "What could Camila possibly have to ask me that's got her so wound up?"
    mike.say "Then ask away, Camila..."
    mike.say "I'm all ears!"
    show camila talkative
    camila.say "Okay, okay..."
    camila.say "Just do me a favour and hear me out before you answer."
    camila.say "I always thought that the force was all I'd ever need."
    camila.say "That my fellow officers were like my family, you know?"
    camila.say "But then you came along, and all of that started to change."
    show camila normal
    "I can't help frowning as Camila opens up to me about how she's feeling."
    "Because I'd pretty much come to terms with the fact that she was devoted to her job."
    "Like it or not, I'd accepted that I might come second to her duties as a police officer."
    mike.say "What are you trying to tell me, Camila?"
    mike.say "You're not thinking about jacking it in, are you?"
    "Camila shakes her head again."
    show camila talkative
    camila.say "Not totally, just maybe taking a sabbatical."
    camila.say "No, [hero.name]...I want to start a family."
    show camila normal
    "The statement is made so boldly and out of the blue that it doesn't really sink in fully."
    "So instead of processing this momentous revelation, my brain just flips into stupid mode."
    mike.say "Oh..."
    mike.say "Who with?"
    show camila weird
    "Camila's eyes flare with astonishment, and she instinctively punches me on the arm."
    "Given the circumstances, that's probably a perfectly fair reaction to the question."
    with hpunch
    "And the sudden pain of the well-aimed jab serves to jerk me back to reality as well."
    mike.say "OUCH!"
    show camila angry
    camila.say "With some random junkie I just busted five minutes ago!"
    show camila weird
    camila.say "Geez, [hero.name], who do you frickin think I mean?!?"
    camila.say "You, you dumb bastard!"
    show camila normal
    "By now I'm nodding like crazy, trying to claw back some vague semblance of dignity."
    "And the reality of what Camila is asking me is really beginning to sink in too."
    mike.say "Are you serious?"
    mike.say "I mean...wow!"
    mike.say "I'd kind of gotten used to the idea that you were married to the force."
    mike.say "So it's kind of hard to get my head around the idea of us having a kid."
    show camila whining
    camila.say "Yeah, yeah...I get that."
    show camila talkative
    camila.say "But it's all your fault, you jerk!"
    camila.say "You're the one that came along and made me go all mushy inside."
    camila.say "I can't help that you made me get in touch with my feelings and all that."
    camila.say "And I tried to ignore it, but I couldn't - I want your damn baby!"
    show camila normal
    menu:
        "Agree":
            "Okay, this might be the craziest thing I've ever done."
            "But somehow it just feels one hundred percent right."
            "And I have the urge to go with my gut feeling on this one."
            mike.say "Then I say that we do it."
            "Now it's Camila's turn to look at me like she doesn't understand."
            "Almost like she was ready for me to say no and call her crazy."
            show camila surprised
            camila.say "Wait a minute..."
            camila.say "Did you just say yes?"
            camila.say "Aren't you supposed to say you don't want to be tied down?"
            camila.say "Or jerk me around about not being prepared for this kind of thing?"
            show camila normal
            mike.say "Camila, I'm not going to impregnate you on the spot, right here and now!"
            mike.say "I'm just saying that I think we should go for it."
            mike.say "We can figure out the details later."
            show camila flirt
            "For the first time since we started talking about all of this, Camila cracks a smile."
            "Like the reality's finally dawning on her that I want to make this thing happen too."
            show camila happy
            camila.say "Oh man..."
            camila.say "I was so sure you were going to chicken out on me!"
            show camila flirt
            mike.say "What?!?"
            mike.say "No way - I'm so much tougher now than I was when you first met me."
            show camila talkative
            camila.say "Well you'd better be."
            camila.say "Because being a dad's gonna be harder than anything you've ever done before!"
            show camila normal
            mike.say "Bring it on - I can handle the pressure!"
            show camila talkative
            camila.say "Yeah..."
            camila.say "When the time comes, I'll remind you that you said that!"
            show camila normal
            $ camila.love += 2
            $ camila.flags.pregrequest = True
        "Refuse":
            "Part of me wants to say yes, just for the sake of pleasing Camila."
            "But the more responsible part of me knows that this isn't a frivolous thing."
            "And I owe it to the both of us to be completely honest with her."
            mike.say "There's no way we can have a kid, Camila..."
            mike.say "Not with where the two of us are in terms of our careers."
            mike.say "It'd mess everything up, don't you see?"
            show camila sad
            "Of course that's not going to be what Camila wanted to hear."
            "And the look on her face reflects that, as she scowls at me."
            show camila whining
            camila.say "I'm not asking you to knock me up right here and now!"
            camila.say "I'm talking about us making serious plans together."
            camila.say "About us committing to a vision of our future."
            camila.say "And making sacrifices to have it happen."
            show camila sadsmile
            "All of what Camila's saying makes sense."
            "But I'm not in the mood to let her change my mind."
            mike.say "No, Camila..."
            show camila sad
            mike.say "We can make plans for the long-term, plan for the future."
            mike.say "But the way I see it, kids are a hell of a long way away for us."
            "Camila looks at me in a way that makes me think she might hit me a second time."
            "But then she shakes her head and turns on her heel."
            show camila whining
            camila.say "Maybe we need to be talking about whether or not there is a future for us, [hero.name]."
            camila.say "Because it sounds like we're about a million miles apart right now!"
            show camila sad
            pause 0.5
            hide camila with easeoutright
            "Before I can say another word, Camila strides away from me."
            "And her body-language tells me that following her would not be a good idea."
            "I guess I'll just have to hope that what she said was in the heat of the moment."
            "And that once she's calmed down, we can talk it through."
            $ camila.love -= 2
    return

label camila_collar_request:
    scene bg mall1
    show camila sad at center, zoomAt(1.5, (640, 1040))
    with fade
    "I'm always kind of on edge whenever I go to the mall with Camila."
    "Because she's one of those people that'll tell you she's off duty."
    "She'll swear, hand on heart that she's left her badge at home."
    "And the next thing you know, she's visibly sizing up the other shoppers."
    "Making me worry that she's going to pounce on one of them any moment."
    "So when we're walking arm-in-arm and she slows us down, let's just say it sets off the old alarm-bells."
    mike.say "What the matter, Camila?"
    mike.say "Is the old spider-sense tingling all of a sudden?"

    "Camila tears her eyes away from what she was just staring at."
    "A look of confusion spreading over her face as she does so."
    show camila surprised
    camila.say "Huh?"
    camila.say "What the hell are you talking about?"
    camila.say "What's a frickin spider got to do with it?"
    show camila sadsmile
    "I should have known that a superhero reference would have gone over Camila's head."
    "But the truth is that I don't know enough detective fiction cliches to change it up."
    mike.say "I mean you look distracted, Camila..."
    mike.say "Like your inner cop is speaking to you again, you know?"
    show camila weird
    "Camila responds by screwing up her face into an expression that says 'get a load of this guy!'."
    show camila happy with hpunch
    "And then she gives me a pretty hard, but still pretty playful, shove on the shoulder."
    show camila talkative
    camila.say "Didn't I already tell you I was off-duty?"
    camila.say "So quit busting my balls about it, okay?"
    show camila normal
    mike.say "Okay, Camila..."
    mike.say "On one condition - that you tell me what's on your mind."
    show camila blush
    "I really thought that was a totally innocent thing to ask Camila."
    "That she'd do what she normally does and tell me all about it."
    "But instead she does something that's markedly out of character for her."
    "Which is to look away and have her cheeks begin to flush red."
    mike.say "Camila..."
    mike.say "Are you..."
    mike.say "Are you actually blushing right now?"
    camila.say "Nah..."
    camila.say "Of course not!"
    camila.say "It's just hot in here, that's all."
    "Either Camila's burning up from a fever, or else she's just straight-up lying."
    "Because the whole of the mall is air-conditioned, which means the air is cool and crisp."
    mike.say "Oh, I think you are!"
    mike.say "Come on, Camila - what's eating you?"
    show camila talkative
    camila.say "Okay, okay..."
    camila.say "But you have to promise not to make a big deal out of it."
    show camila sadsmile
    mike.say "Well, I don't see how I can, Camila..."
    mike.say "Not when I don't know what I'm making a promise about."
    show camila with vpunch
    camila.say "JUST PROMISE DAMN YOU!"
    show camila sadsmile
    mike.say "Alright...I promise!"
    "Camila takes a deep breath, visibly trying to regain control of herself."
    "And I choose to keep my mouth firmly shut until she's finished doing so."
    show camila whining
    camila.say "If you really wanna know..."
    camila.say "I was looking at the stuff in the window of that store."
    camila.say "Because...I kinda like the things they sell."
    show camila sadsmile
    "All of a sudden I feel like the pieces are starting to fall into place."
    "That, for all of her protests and acting tough, Camila's really just like any other girl."
    "Because when she comes to the mall she still ends up window-shopping for what she likes."
    "And then getting all embarrassed when her date catches her in the act."
    mike.say "Oh really?"
    mike.say "Well let's see what all the fuss is about..."
    "I turn around, expecting to be presented with a window full of shoes or pretty dresses."
    "But I stop before finishing what I was about to say when I see what's really behind the glass."
    "Because sure, everything that I'm looking at is stuff to wear."
    "And a whole lot of it is made of leather too."
    "But I see halters, corsets and even a couple of whips!"
    mike.say "B...but, Camila..."
    mike.say "This is the fetish store!"
    mike.say "You mean...you're into that kind of thing?!?"
    "Now Camila really is blushing, looking this way and that."
    "As if she's making sure that nobody is eves-dropping on our conversation."
    show camila whining with vpunch
    camila.say "NO!"
    show camila weird
    camila.say "Well..."
    camila.say "At least not all of it!"
    show camila sadsmile
    mike.say "Okay, Camila..."
    mike.say "So what specific parts of it are you interested in?"
    "I watch in a state of utter fascination, as Camila raises her arms."
    "And I follow the line of her finger as she points at one spot in particular."
    show camila blush
    camila.say "The collars, [hero.name]…"
    camila.say "I just...really wanna wear one."
    camila.say "I can't explain it, not really..."
    camila.say "It feels like it'd be fun...and the idea kinda turns me on too."
    camila.say "Like...like I'd belong to you, and everyone would know it."
    show camila sadsmile
    "Okay, so now I'm really looking down the barrel of a dilemma."
    "On the one hand, I should be flattered that Camila feels she can open up to me."
    "And a good boyfriend would be really supportive of her kinks too."
    "But on the other I don't know where this is ultimately going to lead."
    "And the last thing I want is it escalating to the point where she's choking me to get off!"
    menu:
        "Not sure that's a good idea":
            "If this were coming from any other girl, I might feel more inclined to indulge it."
            "But the fact that it's coming from a tough, independent cop makes me worry."
            "Because I feel like it could be a sign that Camila's got deeper issues going on."
            "And if I encourage her in this, it might lead to her losing her confidence altogether."
            mike.say "I'm not sure that's a good idea, Camila."
            mike.say "But I do think that we should talk about this."
            show camila upset
            "Camila frowns at my answer, like it means I'm betraying her."
            show camila at center, traveling(1.25, 0.5, (640, 880))
            "And she takes a step backwards, putting a little distance between us."
            show camila whining
            camila.say "Wait, wait, wait..."
            camila.say "I'm opening up to you here, [hero.name]…"
            camila.say "I'm, like, being really honest and letting you in."
            camila.say "So why are you starting to sound like the shrink they sent me to when I was a kid?"
            show camila upset
            mike.say "I'm not trying to psychoanalyse you."
            mike.say "I'm just saying this all seems pretty extreme to me."
            mike.say "Like it's coming out of nowhere."
            show camila angry
            camila.say "Of course it's coming out of nowhere, genius..."
            camila.say "I never told you about it before!"
            show camila upset
            "I'm about to say more, but Camila hold up a hand to cut me off."
            show camila angry
            camila.say "You know what, forget it..."
            camila.say "If this is what happens when I open up to you..."
            camila.say "Then I don't want to hear whatever you got to say."
            show camila upset
            show bg mall1
            with fade
            "With that Camila gives me the cold-shoulder for the rest of the time we're at the mall."
            "Doing all she can to make things uncomfortable and awkward as a punishment for disagreeing with her."
            $ camila.love -= 10
            $ camila.sub -= 10
            $ game.active_date.score -= 20
        "This could be beneficial for both of us":
            "Though the more I come to think about it, the whole thing does kind of make sense."
            "Camila's a super-tough, no nonsense cop all the time that she's on duty."
            "So when she's not, all of that must flip inside of her head and she wants to be the opposite."
            "And I can definitely see the benefits of the situation for me too!"
            mike.say "You know what, Camila..."
            mike.say "I think that's a great idea."
            show camila surprised
            "Camila looks at me with a mixture of relief and amazement on her face."
            "Almost like she's relieved and yet still can't quite believe what she's hearing."
            show camila happy
            camila.say "You really mean that?"
            camila.say "You're not just yanking my chain?"
            show camila normal
            mike.say "No way, I'm totally serious."
            mike.say "But I will tug on your leash, if that's what you really want?"
            show camila flirt
            "I see a sudden flash of desire in Camila's eyes at the offer."
            "And in that moment I know that I've made the right choice."
            "Soon enough we're chatting away as we stare through the glass."
            "Discussing the collar and leash combos the store has to offer."
            "Deciding which ones offer the best combination of look and practicality."
            "And I'm already imagining the thrill of walking Camila whilst holding her leash!"
            $ camila.love += 4
            $ camila.sub += 2
            $ game.active_date.score += 20
    scene bg black with dissolve
    pause 0.5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
