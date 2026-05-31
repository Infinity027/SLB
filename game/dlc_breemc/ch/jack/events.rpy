init python:
    Event(**{
    "name": "jack_female_event_01",
    "label": "jack_female_event_01",
    "priority": 500,
    "duration": 1,
    "conditions": [
        InInventory("zbox_360"),
        IsNotDone("jack_female_event_01"),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom")
            )
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_02",
    "label": "jack_female_event_02",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("jack_female_event_01"),
        IsNotDone("jack_female_event_02_bis"),
        HeroTarget(
            IsGender("female"),
            IsRoom("electronic")
        ),
        PersonTarget(jack,
            MinStat("love", 20)
            )
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_03",
    "label": "jack_female_event_03",
    "priority": 500,
    "duration": 3,
    "conditions": [
        IsDone("jack_female_event_02"),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom")
            ),
        PersonTarget(jack,
            MinStat("love", 40)
            ),
        IsHour(20, 0),
        IsDayOfWeek("67")
    ],
    "do_once":True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "jack_female_event_04",
    "label": "jack_female_event_04",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(IsGender("female")),
        IsDone("jack_female_event_03"),
        PersonTarget(jack,
            IsActive(),
            MinStat("love", 60)
            ),
        IsDayOfWeek("67")
    ],
    "do_once":True,
    "quit": False,
    })

    Activity(**{
    "name": "prepare_cosplay",
    "display_name": "Prepare cosplay",
    "label": "prepare_cosplay",
    "duration": 2,
    "rooms": "bedroom4",
    "conditions": [
        IsTimeOfDay("morning", "afternoon"),
        HeroTarget(
                   IsGender("female"),
                   MinStat("energy", 4),
                   MinStat("hunger", 4),
                   MaxFlag("cosplay_prepared", 99)
                   ),
        PersonTarget(jack,
                     Not(IsHidden()),
                     IsFlag("convention_delay"),
                     Not(IsFlag("convention_declined")),
                    )
        ],
    "once_day": True,
    "icon": "mirror",
    })

    Event(**{
    "name": "jack_female_event_05",
    "label": "jack_female_event_05",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female")
            ),
        IsDone("jack_female_event_04"),
        IsHour(13, 14),
        PersonTarget(jack,
                     IsFlag("convention_delay", False),
                     Not(IsFlag("convention_declined")),
                     Not(IsHidden())
                     ),
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_06",
    "label": "jack_female_event_06",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female")
            ),
        IsDone("jack_female_event_05"),
        IsNotDone("jack_female_event_06"),
        PersonTarget(jack,
                     OnDate(),
                     MinStat("love", 120)),
        HeroTarget(IsRoom("date_livingroom"))
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_07",
    "label": "jack_female_event_07",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasRoomTag("street")
            ),
        IsDone("jack_female_event_06"),
        IsNotDone("jack_female_event_07"),
        PersonTarget(jack,
                     MinStat("love", 140)
                     ),
        IsTimeOfDay("afternoon"),
        IsDayOfWeek("67")
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_08",
    "label": "jack_female_event_08",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasRoomTag("street")
            ),
        IsDone("jack_female_event_07"),
        IsNotDone("jack_female_event_08"),
        PersonTarget(jack,
                     MinStat("love", 160),
                     Not(IsHidden())
                     ),
        IsTimeOfDay("afternoon"),
        IsDayOfWeek("67")
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_09",
    "label": "jack_female_event_09",
    "priority": 500,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female")
            ),
        IsDone("jack_female_event_08"),
        PersonTarget(jack,
                     OnDate(),
                     MinStat("love", 180)),
        HeroTarget(IsRoom("date_restaurant"))
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_02_bis",
    "label": "jack_female_event_02_bis",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("jack_female_event_01"),
        IsNotDone("jack_female_event_02"),
        HeroTarget(
            IsGender("female"),
            IsRoom("bookstore")
        ),
        PersonTarget(jack,
            MinStat("love", 20)
            )
    ],
    "do_once":True,
    "quit": False,
    })


    Event(**{
    "name": "jack_female_event_03_bis",
    "label": "jack_female_event_03_bis",
    "priority": 500,
    "duration": 3,
    "conditions": [
        IsDone("jack_female_event_02_bis"),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom")
            ),
        PersonTarget(jack,
            MinStat("love", 40)
            ),
        IsHour(13, 17),
        IsDayOfWeek("67")
    ],
    "do_once":True,
    "quit": False,
    })


    Event(**{
    "name": "jack_female_event_04_bis",
    "label": "jack_female_event_04_bis",
    "priority": 500,
    "duration": 3,
    "conditions": [
        IsDone("jack_female_event_03_bis"),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("park")
            ),
        PersonTarget(jack,
            MinStat("love", 60)
            ),
        IsHour(13, 17)
    ],
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_female_event_05_bis",
    "label": "jack_female_event_05_bis",
    "priority": 500,
    "conditions": [
        IsDone("jack_female_event_04_bis"),
        HeroTarget(
            IsGender("female")
            ),
        PersonTarget(jack,
            Not(IsPresent()),
            MinStat("love", 80),
            Not(IsActivity("sleep"))
            ),
        IsHour(20, 0),
    ],
    "do_once":True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "jack_female_event_06_bis",
    "label": "jack_female_event_06_bis",
    "priority": 500,
    "conditions": [
        IsDone("jack_female_event_05_bis"),
        HeroTarget(
            IsGender("female")
            ),
        PersonTarget(jack,
            IsActive(),
            MinStat("love", 120),
            ),
        IsDayOfWeek(5, 6, 7),
        IsHour(18, 21),
    ],
    "duration": 2,
    "do_once":True,
    "quit": False,
    })

    Event(**{
    "name": "jack_preg_talk",
    "label": "jack_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsFlag("pregnancy_father", "jack"),
            Or(
                MinCounter("pregnant", 60),
                IsFlag("foundpreg"),
                ),
            ),
        PersonTarget(jack,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    })


    Event(**{
    "name": "jack_find_out_pregnancy",
    "label": "jack_find_out_pregnancy",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            MinCounter("pregnant", 30),
            CounterChanceChecker("pregnant", 50)
            ),
        PersonTarget(jack,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    })

    Event(**{
    "name": "jack_nightclub_date_female",
    "label": "jack_nightclub_date_female",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsRoom("date_nightclub")
            ),
        PersonTarget(jack,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })


label jack_female_event_01:
    $ jack.unhide()
    scene bg livingroom
    "You know what it's like when you're in the zone, right?"
    "Headphones on, joypad in your hands, head in the game."
    "It's like the real world just doesn't exist anymore."
    "You're so into the game that nothing else matters."
    play sound door_knock
    "And then somebody just has to go and knock at the front door!"
    "Cursing under my breath, I pause the game and pull off my headphones."
    "Whoever just interrupted my gaming session better have a good excuse."
    "Because if they don't..."
    "Well, let's just say that I'll be really mad with them!"
    "So they'd better not expect me to treat them nicely."
    "I make it to the door and undo the latch as quickly as I can."
    "Maybe if I get rid of them fast I can get straight back to my game."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    with wiperight
    "But as soon as I open the door, I get a massive surprise."
    "A balled fist headed straight for my face!"
    with vpunch
    bree.say "Aaargh!"
    jack.say "Aaargh!"
    "As I jump backwards to avoid the blow, the owner of the fist does the same."
    show jack surprised
    "And as soon as I lower my hands, I see that he's as shocked as I am."
    bree.say "What in the hell are you doing?"
    bree.say "I answer the door and you whack me in the face?!?"
    show fx exclamation
    jack.say "What?!?"
    jack.say "Oh...no...no, no, no!"
    jack.say "I was just knocking, that's all!"
    "I see that he's still holding the offending hand in the air."
    "But in the other one he's clutching a mobile phone."
    "I guess he must have been staring at it while he was knocking."
    "That would explain how he nearly hit me in the face just now!"
    bree.say "Um..."
    bree.say "Okay...I'm going to choose to believe you this time."
    bree.say "But you should maybe tell me what you want?"
    show jack normal
    "The guy nods and shoves his phone into his pocket."
    jack.say "[mike.name]..."
    bree.say "You're called [mike.name]?"
    bree.say "That's confusing."
    bree.say "We already have a guy called [mike.name] living here!"
    show fx drop
    jack.say "No, no..."
    jack.say "I'm Jack, and I'm here to SEE [mike.name]!"
    "I suddenly feel like a complete moron."
    "Of course he means that he's here to see [mike.name]."
    "I mean, he even looks like he should be one of [mike.name]'s friends."
    "The hair, the beard and the clothes - all of them scream [mike.name]!"
    menu:
        "Don't care about it":
            bree.say "Whatever, buddy."
            bree.say "I guess he must be in his room or something."
            "Jack looks at me as though he's waiting for something."
            "And then he points over my shoulder and into the house."
            show jack sad
            jack.say "Erm..."
            jack.say "Can I come in?"
            jack.say "And like, see [mike.name]?"
            bree.say "Urgh..."
            bree.say "What do I care?"
            scene bg livingroom with fade
            "I turn my back on him and walk towards the sitting room."
            "Behind me I hear the sound of Jack closing the door."
            show jack at right4 with easeinright
            "But by the time I have the joypad in my hand, he's right there next to me!"
            show jack smile
            jack.say "Aw, man..."
            jack.say "I LOVE this game!"
            jack.say "Did you get to the part where..."
            show jack normal
            show fx exclamation at right4
            "I cut Jack off before he can say another word."
            bree.say "Yeah?"
            bree.say "Well I love it more!"
            bree.say "And no spoilers!"
            show jack sad at right5 with ease
            "Jack flinches and takes a step backwards."
            "And his face looks like a dog snapped at him too."
            "Another time I might have felt bad for him."
            "But it seems to work, as he shuts his mouth and keeps quiet."
            "I go back to my game, forgetting all about Jack."
            show mike at left with easeinleft
            show jack normal
            "That is until [mike.name] wanders into the room."
            mike.say "Oh..."
            show mike happy at left5 with ease
            mike.say "Hey, Jack!"
            show jack smile
            jack.say "Hey, man."
            mike.say "[hero.name], why didn't you tell me Jack was here?"
            "I roll my eyes and pull the headphones off."
            "Why does everyone want to ruin my game time?"
            bree.say "Um...I don't know, [mike.name]."
            bree.say "Maybe because I'm not your fucking social secretary!"
            show jack sad
            show mike normal
            "Now it's [mike.name]'s turn to flinch in surprise."
            hide jack
            hide mike
            with easeoutright
            "He nods to Jack and together they flee the room."
            "Finally alone, I let out a sigh of relief."
            "Now I can get some serious gaming done in peace!"
            $ jack.love -= 2
            $ mike.love -= 2
        "Invite him to enter":
            if hero.morality <= -30:
                "I smile at Jack and slowly lick my lips."
                "He's kind of cute - in a geeky sort of way."
                "The sort of guy that's needy and kind of desperate too!"
                "Like [mike.name], but better because he doesn't live under the same roof as me."
                "So there's no awkward complications to get in my way!"
                bree.say "Sure, sure..."
                bree.say "Of course that's what you meant!"
                bree.say "I was just playing with myself when you knocked."
                "Jack nods, but then he does a double take."
                show jack surprised at startle
                show fx exclamation
                jack.say "Y...you were what?!?"
                bree.say "Playing on the Zbox of course!"
                bree.say "Why - what did you think I meant?"
                show jack blush
                "Jack's cheeks flush with colour."
                "And he tries to change the subject."
                jack.say "Erm..."
                jack.say "Can I come in?"
                jack.say "And like, see [mike.name]?"
                bree.say "Of course you can, Jack."
                bree.say "You can come anywhere you like!"
                show bg livingroom with fade
                "I step aside and usher Jack into the house."
                show jack casual at right with easeinright
                "Then I gesture for him to follow me back to the sitting room."
                "But I make sure that I shake my ass as he follows me."
                bree.say "I'm [hero.name], by the way."
                show jack smile
                jack.say "Oh...right..."
                jack.say "Hi [hero.name]!"
                bree.say "You can wait for [mike.name] in here."
                bree.say "Would you like to play with me until he's ready, Jack?"
                show jack blush
                "Jack's eyes go wide at the question."
                "And he stammers as he tries to answer me."
                show jack perv
                jack.say "P...p...play?"
                jack.say "W...with you?!?"
                show jack blush
                "I smile and nod in the direction of the Zbox."
                bree.say "I'm afraid I only have the one joypad."
                bree.say "So we'll have to share, okay?"
                "Jack nods and he sits down beside me."
                "But I quickly scoot around so I'm sitting between his legs."
                show jack blush at center, zoomAt(1.5, (640, 1040))
                "Then I lean back into him and pull his arms around me."
                bree.say "Hold my joypad, Jack."
                bree.say "And don't be afraid to push my buttons too!"
                "We're soon well into the game."
                "And Jack even seems to warm to the way I'm flirting with him too."
                scene bg livingroom with fade
                pause 0.1
                show mike casual normal at left with easeinleft
                "Until [mike.name] wanders into the room, that is."
                mike.say "Oh..."
                mike.say "Hey, Jack!"
                mike.say "You look like you've made yourself at home!"
                show jack at right4 with dissolve
                "Jack leaps up, looking as guilty as hell."
                show jack happy at left
                show fx drop at right4
                jack.say "H...hey, man."
                jack.say "We were just playing a game together - that's all!"
                show mike normal
                "[mike.name] looks at me and then back at Jack."
                "And I'm sure I see knowing smile on his face."
                mike.say "[hero.name], why didn't you tell me Jack was here?"
                bree.say "Oops!"
                bree.say "We were having such a good time together."
                bree.say "I guess it just slipped my mind!"
                show mike happy at left, startle
                "[mike.name] nods and laughs, as if he's not surprised."
                "And then they leave me alone to play some more."
                show jack smile
                "But not before Jack gives me a smile and a wave over his shoulder."
                "I return the gesture, adding a wink and blowing a kiss for good measure."
                hide jack
                hide mike
                with easeoutright
                "And then I slip on my headphones."
                "Now then..."
                "Where was I?"
                $ jack.sub += 2
            elif hero.morality <= -10:
                "I can't help smiling at Jack."
                "He's kind of cute - in a geeky sort of way."
                "Like [mike.name], but better because he doesn't live under the same roof as me."
                bree.say "Sure, sure..."
                bree.say "Of course that's what you meant!"
                bree.say "I was just on the Zbox when you knocked."
                bree.say "And I guess my head's still in the game!"
                "Jack looks at me as though he's waiting for something."
                "And then he points over my shoulder and into the house."
                jack.say "Erm..."
                jack.say "Can I come in?"
                jack.say "And like, see [mike.name]?"
                bree.say "Of course you can, Jack."
                bree.say "Come right in!"
                scene bg livingroom with fade
                "I step aside and usher Jack into the house."
                show jack casual at right with easeinright
                "Then I gesture for him to follow me back to the sitting room."
                bree.say "You can wait for him in here."
                bree.say "If you don't mind watching me play?"
                show jack smile
                jack.say "Oh no - I'm a bit of a gamer myself!"
                bree.say "I'm [hero.name], by the way."
                jack.say "Oh...right..."
                jack.say "Hi [hero.name]!"
                show jack normal
                "There was no need for him to say that."
                "But it's cute that he thought to do it."
                "I let out a little chuckle and give him a smile."
                bree.say "Hi to you too, Jack!"
                "I walk back into the sitting room."
                show jack at right4 with ease
                "And Jack follows behind me."
                show jack smile
                show fx exclamation at right4
                jack.say "Oh wow - I love this game!"
                bree.say "Well why don't you grab the other joypad?"
                bree.say "We can play together until [mike.name]'s ready."
                show jack normal
                "Jack leaps at the chance, sitting down beside me."
                "We're soon well into the game, chatting and joking as we play."
                "Jack's damn good too, a serious gamer by the looks of it."
                "I make a mental note to ask if he wants to come over and play some time."
                "Because you can never have enough gamer friends."
                "We're having a great time together."
                scene bg livingroom with fade
                pause 0.1
                show mike casual normal at left with easeinleft
                "Until [mike.name] wanders into the room, that is."
                mike.say "Oh..."
                mike.say "Hey, Jack!"
                show jack smile at right with dissolve
                jack.say "Hey, man."
                mike.say "[hero.name], why didn't you tell me Jack was here?"
                bree.say "Ah, sorry, [mike.name]!"
                bree.say "I guess it just slipped my mind."
                show jack normal
                jack.say "It was probably my fault."
                jack.say "We just got playing the game together, that's all!"
                show mike happy at left, startle
                "[mike.name] nods and laughs, as if he's not surprised."
                "And then they leave me alone to play some more."
                "But not before Jack gives me a smile and a wave over his shoulder."
                "I return the gesture, adding a little wink for good measure."
                hide mike
                hide jack
                with easeoutright
                "And then I slip on my headphones."
                "Now then..."
                "Where was I?"
                $ jack.love += 1
                $ jack.sub += 1
            else:
                bree.say "Sure, sure..."
                bree.say "Of course that's what you meant!"
                bree.say "I was just on the Zbox when you knocked."
                bree.say "And I guess my head's still in the game!"
                "Jack looks at me as though he's waiting for something."
                "And then he points over my shoulder and into the house."
                jack.say "Erm..."
                jack.say "Can I come in?"
                jack.say "And like, see [mike.name]?"
                bree.say "Yeah, yeah..."
                scene bg livingroom with fade
                "I step aside and usher Jack into the house."
                show jack casual at right with easeinright
                "Then I gesture for him to follow me back to the sitting room."
                bree.say "You can wait for him in here."
                bree.say "If you don't mind watching me play?"
                "Jack shakes his head at this."
                show jack smile at right5 with ease
                "And then he cracks a smile."
                jack.say "Oh no, that's fine..."
                "He trails off without finishing what he was going to say."
                "And it takes me a moment to figure out why he's done it."
                bree.say "[hero.name]..."
                bree.say "My name's [hero.name]!"
                jack.say "Nice to meet you, [hero.name]!"
                jack.say "And no, it's fine - I'm into that game too."
                show jack normal
                "I start playing the game again."
                "But I chat back and forth with Jack at the same time."
                "He offers me some pretty good advice while he watches over my shoulder."
                "And I make a mental note to ask if he wants to come over and play some time."
                "Because you can never have enough gamer friends."
                scene bg livingroom with fade
                pause 0.1
                show mike casual normal at left with easeinleft
                "Then [mike.name] wanders into the room."
                mike.say "Oh..."
                mike.say "Hey, Jack!"
                show jack casual smile at right with dissolve
                jack.say "Hey, man."
                mike.say "[hero.name], why didn't you tell me Jack was here?"
                bree.say "Ah, sorry, [mike.name]!"
                bree.say "I guess it just slipped my mind."
                jack.say "It was probably my fault."
                jack.say "We just got talking and I kept jabbering, you know?"
                show mike happy at left, startle
                "[mike.name] nods and laughs, as if he's not surprised."
                "And then they leave me alone to play some more."
                "But not before Jack gives me a smile and a wave over his shoulder."
                "I return the gesture and then I slip on my headphones."
                hide mike
                hide jack
                with easeoutright
                "Now then..."
                "Where was I?"
                $ jack.love += 2
    return

label jack_female_event_02:
    $ game.room = "electronic"
    if jack.love.max < 40:
        $ jack.love.max = 40
    scene bg electronic
    "I hadn't actually gone to the mall with the intention of hitting the videogame store."
    "I just kind of ended up wandering into the place on a whim and browsing the shelves."
    "Somehow I find myself lingering around the second-hand games section."
    "And that's where my eyes settle upon an old friend, one I haven't seen in years."
    "Penultimate Fantasy 7!"
    "Wow - how old must that game be by now?"
    "Instantly I'm transported back to being a kid, playing it at home with my Dad!"
    "I remember the hero with the spiky hair and the huge sword."
    "The big guy with a gun for a hand."
    "I even remember the music that used to get my adrenaline pumping too!"
    "My hand reaches out to pick up the game."
    "I don't know what the price is - hell, I don't even know what format it is!"
    "But the pull of fuzzy, rose-tinted nostalgia is just too much for me to resist!"
    with vpunch
    "It's only when my fingers touch somebody else's digits that I snap out of it."
    "My eyes follow the fingers to a hand, and from there to an arm."
    "And the arm leads to me looking into a face."
    "The face of whoever tried to grab the game at the same second as me."
    show jack casual blush at center, zoomAt(1.5, (640, 1040)) with dissolve
    show fx drop
    jack.say "Uh..."
    jack.say "H...hi there, [hero.name]!"
    "I blink in confusion."
    "And then I stammer out a response."
    bree.say "J...Jack?"
    bree.say "What are you doing here?!?"
    "I could kick myself the moment that I say it."
    "What kind of a dumb question is that?"
    "He's here shopping for games, just like everyone else!"
    "But luckily for me, Jack's brain seems to be scrambled too."
    jack.say "Looking for the same game as you, I guess!"
    show jack sad
    jack.say "Ah..."
    jack.say "Is this the only copy they have?"
    bree.say "Yeah, look that way."
    "There's a second of silence as we stare at each other."
    "And neither of us shows any sign of letting go of the game."
    bree.say "I...I used to play this game with my Dad, Jack."
    bree.say "And I REALLY want to own it again!"
    "Jack sighs heavily at this."
    "And I can see that he's torn."
    "At least part of him wants to let me have it."
    "But he obviously loves the game too."
    "Which makes me feel guilty wanting it for myself."
    show jack angry
    jack.say "Look, [hero.name], I'll admit something."
    jack.say "I already have this game."
    jack.say "And all of the remakes too."
    jack.say "But this is the edition that came with the demo for Penultimate Fantasy 8!"
    jack.say "I need that one to complete my collection!"
    show jack sad
    "That should have been more than enough for me to demand he hand it over."
    "He already has more than one copy of the game and I don't have squat!"
    "But instead it only makes me feel for him all the more."
    "I'm a nerd too."
    "And I know how important it is to complete your collection!"
    menu:
        "Fight for it":
            "But still, something in me just won't let go!"
            "I'm every bit the nerd that Jack is - maybe even more so."
            "And I deserve this game, damn it!"
            show jack angry
            jack.say "Erm..."
            jack.say "You're not letting go of it - are you, [hero.name]?"
            show jack sad
            bree.say "No, Jack, I'm not."
            bree.say "I want the game as much as you do."
            show jack smile
            jack.say "Okay, okay..."
            jack.say "I have the perfect solution."
            $ jack.love -= 1
            $ jack.sub += 3
        "Let it go":
            "And I really like this guy."
            "The last thing I want is for him to think I'm a jerk!"
            "So with a heavy heart, I let go of the game."
            bree.say "You take it, Jack."
            show jack surprised
            jack.say "Wh...what just happened, [hero.name]?"
            jack.say "You really wanted it a second ago."
            jack.say "Why are you letting me have it?"
            show jack sad
            bree.say "It's no big deal, Jack."
            bree.say "I want you to have it, that's all."
            "Jack doesn't look convinced."
            "He shakes his head, not ready to let it go."
            show jack smile
            jack.say "I think you're just trying to be nice, [hero.name]."
            jack.say "Which really is...nice."
            jack.say "But I've got a better idea."
            $ jack.love += 3
            $ jack.sub -= 1
        "Challenge him":
            "It's obvious that neither of us is going to back down."
            "We're a pair of nerds, equally matched in almost every sense."
            bree.say "We both want the game, Jack."
            bree.say "We need to find some way to settle this!"
            bree.say "So what do you think - lightsaber duel at dawn?"
            "As ridiculous as the suggestion is, Jack doesn't rubbish it."
            show jack smile
            "Instead I see a flash of amusement and appreciation in his eyes."
            jack.say "Nah, [hero.name]."
            jack.say "I've got a better idea."
            $ jack.love += 1
            $ jack.sub += 1
    if hero.morality <= -25:
        "But then I know what else is important to a guy like Jack too!"
        if hero.morality <= -100:
            "That's why I slide my other hand down the front of his pants."
            show jack blush
            "And I make a point of squeezing his cock while I look into his eyes."
            "Jack begins to get hard the moment I touch him down there too."
            "Letting me know that he's got some serious manhood down there."
        elif hero.morality <= -75:
            "That's why I put my other hand on the front of his pants."
            show jack blush
            "And I make a point of massaging his dick while I look into his eyes."
            "Making a mental note of how surprisingly big it is too."
        elif hero.morality <= -50:
            "That's why I put my other hand firmly on his thigh."
            show jack blush
            "And I make a point of stroking it while I look into his eyes."
        else:
            "That's why I put my other hand over the one he's holding the game in."
            show jack blush
            "And I make a point of stroking it while I look into his eyes."
        bree.say "Mmm..."
        bree.say "Jack..."
        show jack perv
        jack.say "Uh...I...I..."
        bree.say "Mean I REALLY, REALLY want this game!"
        "I choose just the right moment to flutter my eyelids at him."
        "And almost the next moment, I see Jack begin to melt!"
        jack.say "W...well...if you put it like that..."
        show jack sad
        jack.say "Sure, [hero.name] - you should have the game!"
        "I smile happily as Jack hands over the game."
        "And then we walk to the counter where I pay for it."
        bree.say "Anyway, I feel like I need to do something nice for you in return."
        bree.say "You wanna come over to my place sometime soon?"
        bree.say "We can hang out, play some games - maybe even grab a pizza?"
        show jack happy
        "Jack's face lights up at the offer."
        "And he nods his head with genuine enthusiasm."
        jack.say "That'd be great, [hero.name]!"
        jack.say "You mean with [mike.name], right?"
        bree.say "No, silly - just the two of us!"
        show jack perv
        jack.say "Really?!?"
        jack.say "I'd love to, [hero.name]."
        bree.say "Great, Jack - I'll call you, okay?"
        hide jack with dissolve
        "I walk away with the game clutched in my hands."
        "Already excited about the prospect of a nostalgia binge when I get home."
        "And almost as excited about the chance to hang out with Jack too!"
        $ jack.sub += 5
        return
    bree.say "Oh yeah?"
    bree.say "What's that?"
    show jack happy
    jack.say "We have a quiz battle!"
    jack.say "I test your knowledge of Penultimate Fantasy 7!"
    bree.say "And if I win, I get the game?"
    show jack smile
    jack.say "I'll hand it over gladly."
    "It's a pretty silly idea."
    "But I have to admit I can't think of a better one right now."
    "So I shrug and nod my head."
    "Jack nods in return."
    show jack normal
    jack.say "Okay, [hero.name]..."
    jack.say "Here comes question number one."
    jack.say "Which character is the hero's childhood friend?"
    $ quizz_points = 0
    menu:
        "The florist":
            bree.say "Oh..."
            bree.say "Come on, come one..."
            jack.say "You have to know this one, [hero.name]!"
            bree.say "Was it the Florist?"
            jack.say "Of course not - it was the Barmaid!"
            $ quizz_points -= 1
        "The barmaid":
            bree.say "That's easy, Jack!"
            bree.say "It's the Barmaid."
            jack.say "Damn it!"
            jack.say "That was too easy!"
            $ quizz_points += 1
            $ jack.love += 1
            $ jack.sub += 1
        "The ninja":
            bree.say "Oh..."
            bree.say "My mind's gone blank..."
            jack.say "You have to know this one, [hero.name]!"
            bree.say "Was it the Ninja?"
            jack.say "Of course not - it was the Barmaid!"
            $ quizz_points -= 1
    "Jack pauses for a moment as he thinks up the next question."
    show jack smile
    "And then he grins as he prepares to fire it my way."
    jack.say "Question number two, [hero.name]."
    show jack normal
    jack.say "Who's the kick-ass eco-warrior in the game?"
    menu:
        "The cat with the burning tail":
            bree.say "Wasn't that the big cat?"
            bree.say "The one that talked and had it's tail on fire?"
            jack.say "[hero.name], what are you talking about?"
            jack.say "That was like a totally different character!"
            $ quizz_points -= 1
        "The cat with the megaphone":
            bree.say "Wasn't that the cat?"
            bree.say "The one that talked and had a megaphone?"
            jack.say "[hero.name], what are you talking about?"
            jack.say "All that cat did was suck!"
            $ quizz_points -= 1
        "Definitely not the talking cat":
            bree.say "I dunno, Jack."
            bree.say "But it sure as hell wasn't that sucky cat!"
            show jack happy at startle
            "Jack can't keep from laughing at the mere mention of the character in question."
            jack.say "Oh shit, yeah!"
            show jack smile
            jack.say "You get a bonus point for hating that dude!"
            bree.say "It was the guy with the gun for a hand, obviously!"
            show jack normal
            jack.say "Ah...that was the right answer too!"
            $ quizz_points += 1
            $ jack.love += 1
            $ jack.sub += 1
    "I watch Jack as he racks his brain for another question."
    "A nod tells me that he's settled on one and is ready to go."
    jack.say "Third and final question, [hero.name]."
    jack.say "This is make or break!"
    jack.say "Who was the ultimate antagonist in the game?"
    jack.say "You know - the REAL big bad!"
    menu:
        "The mega corporation":
            bree.say "It was the big corporation."
            bree.say "They were the ones behind it all."
            jack.say "Ouch!"
            jack.say "Wrong answer!"
            $ quizz_points -= 1
        "An alien in a tub":
            bree.say "Ooh..."
            bree.say "It was like a plot-twist or something..."
            bree.say "I remember - it was that weird alien in a tub!"
            jack.say "Ouch!"
            jack.say "Wrong answer!"
            $ quizz_points -= 1
        "The strange guy with a long sword":
            bree.say "It was the guy with the long sword, Jack."
            bree.say "He turned out to be behind it all in the end."
            jack.say "Wow..."
            jack.say "I guess you really did play the game back in the day!"
            $ quizz_points += 1
            $ jack.love += 1
            $ jack.sub += 1
    "I wait with baited breath as Jack tots up my score."
    "And I can feel genuine butterflies in my stomach too!"
    if quizz_points > 0:
        show jack sad
        jack.say "Aw..."
        jack.say "I guess it sucks to be me!"
        bree.say "I won?!?"
        "Jack nods and hands over the game."
        show jack smile
        "He shakes his head, but smiles all the same."
        jack.say "I should have made the questions harder!"
        bree.say "I'm sorry, Jack."
        bree.say "But I really do love this game!"
        jack.say "I can see that!"
        show jack normal
        "We walk to the counter, chatting while I buy the game."
        "But as we leave the store, I turn to face Jack."
        bree.say "Thanks again, Jack."
        bree.say "This game means a lot to me."
        bree.say "And it was sweet of you to let me have it."
        jack.say "What do you mean, [hero.name]?"
        show jack smile
        jack.say "You won, fair and square."
        "I narrow my eyes at this."
        "And I study Jack with interest."
        bree.say "I don't know..."
        bree.say "Some of those questions were suspiciously easy!"
        show jack normal
        $ jack.sub += 3
        return
    else:
        jack.say "It sucks ass, [hero.name]."
        jack.say "But you lose - sorry!"
        "I force a smile on my face as I hand the game to Jack."
        bree.say "It's okay, Jack."
        bree.say "You won, fair and square."
        "Jack accepts his prize."
        "But I can see that he's not happy to have won."
        jack.say "This isn't right, [hero.name]."
        jack.say "You should have aced that quiz."
        jack.say "Be honest - did you get the questions wrong on purpose?"
        bree.say "No way, Jack!"
        bree.say "It's been so long since I played it."
        bree.say "I must have just forgotten all that stuff."
        "Jack looks thoughtful for a moment."
        "And then he nods his head."
        show jack smile
        "His face looking like he just made an important decision."
        jack.say "I'm going to buy the game, [hero.name]."
        jack.say "But then I'm lending it to you straight away!"
        bree.say "Really?"
        show jack happy
        jack.say "Yeah, [hero.name]."
        jack.say "You need to brush up on the lore of the game!"
        bree.say "Okay, Jack, if you insist!"
        show jack normal
        "We walk to the counter and Jack buys the game."
    bree.say "Anyway, I feel like I need to do something nice for you in return."
    bree.say "You wanna come over to my place sometime soon?"
    bree.say "We can hang out, play some games - maybe even grab a pizza?"
    show jack smile
    "Jack's face lights up at the offer."
    "And he nods his head with genuine enthusiasm."
    jack.say "That'd be great, [hero.name]!"
    jack.say "You mean with [mike.name], right?"
    bree.say "No, silly - just the two of us!"
    show jack perv
    jack.say "Really?!?"
    jack.say "I'd love to, [hero.name]."
    bree.say "Great, Jack - I'll call you, okay?"
    hide jack with dissolve
    "I walk away with the game clutched in my hands."
    "Already excited about the prospect of a nostalgia binge when I get home."
    "And almost as excited about the chance to hang out with Jack too!"
    $ jack.love += 2
    return

label jack_female_event_03:
    if jack.love.max < 60:
        $ jack.love.max = 60
    scene bg livingroom
    "How come I can do something almost every single day for years and not have a problem."
    "But the very moment I ask someone over to do it with me, everything seems to change."
    "Huh, what's up with that?"
    "People always bug me about hogging the games consoles in the house too."
    "They want to play themselves or else they want to watch TV."
    "But now they know Jack's coming over to play some games with me."
    "And so they're all grins and winks, like it's a date or something!"
    "It's not a date, just two people getting together to hang out, that's all."
    "And why, no matter how many times I tell myself that, do I have the butterflies?!?"
    "Yeah, sure, I admit it - I like Jack."
    "And yeah, he's kind of cute in a nerdy way."
    "But this is the twenty-first century for goodness sake."
    "A guy and a girl can be friends without needing to get involved."
    "So that's that."
    "Jack's going to come over and we're just going to play games and eat pizza."
    "Well...unless something else does happen..."
    "Ah...shut up, brain!"
    "Just relax and let whatever happens happen!"
    play sound door_knock
    "All to soon I hear a knock at the door and leap up."
    "Thankfully Sasha and [mike.name] have made themselves scarce."
    "So I scuttle to the front door and open it."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show jack casual smile
    with wiperight
    jack.say "Hey, [hero.name]!"
    jack.say "You ready for a night of hardcore gaming?"
    jack.say "Because I know I am!"
    show bg livingroom with fade
    "I can't help smiling as I let Jack into the house."
    "It's like his geeky enthusiasm is infectious or something."
    "Suddenly I feel myself forgetting all about my previous worries."
    bree.say "You bet I am, Jack!"
    bree.say "The pizza's ready."
    bree.say "I'll go grab it and then we can pick a game."
    show jack normal
    jack.say "Sounds good to me."
    jack.say "I'm starving!"
    scene bg kitchen with fade
    "We exchange another round of grins as I head for the kitchen."
    "Why can't it be like this with other guys too?"
    "Jack seems to treat me just like he does [mike.name]."
    "I mean, it'd be so easy if I were going out with a guy like him..."
    "I almost burn myself on the pizza as I shake off the thought."
    "We're friends, that's all!"
    show bg livingroom
    show jack casual normal
    with fade
    "When I make it back to the sitting room, Jack's already looking through the games."
    "He's sitting on the floor with them spread around him, and looks up as I walk in."
    show jack surprised
    jack.say "Wow, [hero.name]..."
    jack.say "I didn't know you were such a serious gamer!"
    show jack smile
    jack.say "There's stuff here that even I haven't got in my collection!"
    show jack normal
    "I try to keep from blushing at the compliment."
    "Guys usually make comments about the way I look."
    "So it comes as a surprise to be complimented on my videogame collection!"
    bree.say "Ah, I'm just a big old nerd, Jack!"
    bree.say "So..."
    bree.say "You see anything you want to play?"
    jack.say "I think you should choose the first game, [hero.name]."
    jack.say "You are the host, after all!"
    if hero.morality <= -25:
        "The obvious thing would be to suggest that we choose a two-player game."
        "But I can already feel the tension in the air between Jack and myself."
        "And it's something that I want to ramp up as much as I can!"
        bree.say "How about we play Evil Residence?"
        bree.say "It's been a while since I busted that one out!"
        show jack sad
        "Jack frowns, the confusion plain to see on his face."
        jack.say "But..."
        jack.say "That's a single-player game, [hero.name]!"
        jack.say "One of us is going to end up watching."
        jack.say "And where's the fun in that?"
        "I wave away his concerns as I pull out the games."
        bree.say "Leave it to me, Jack."
        bree.say "I know a way we can both join in."
        "Jack doesn't look convinced."
        "But he nods all the same, willing to indulge me."
        jack.say "Okay, [hero.name]."
        jack.say "Which Evil Residence game are we playing?"
        jack.say "Evil Residence one, two or three?"
        bree.say "Erm, duh!"
        bree.say "We're going to play one, then two and then three!"
        "Jack still looks unconvinced."
        "But then I shuffle over to where he's sitting on the floor."
        show jack perv
        "And I place myself right between his legs, leaning back against him."
        jack.say "Wha...what are you doing, [hero.name]?!?"
        "I let out a playful chuckle."
        bree.say "Just getting comfy, Jack."
        bree.say "Will you teach me all your tricks, huh?"
        bree.say "Give me a hands-on lesson?"
        jack.say "Y...yes..."
        show jack happy
        jack.say "I mean...yeah, [hero.name] - sure thing!"
        "Sure, Jack starts out pretty awkward with me snuggled up close to him."
        show jack normal
        "But it doesn't take him long to get used to the idea."
        "And as we play the game together, he soon loosens up."
        "After all, I'm only trying to get cosy!"
        jack.say "Did you know that there's a hidden chamber around here?"
        bree.say "Is there?"
        bree.say "You have to show me, Jack!"
        "Of course I know exactly where it is."
        "I know this game inside out."
        "But Jack seems to love showing off like this."
        "And I make a point of letting him think he's impressing me."
        if hero.morality <= -100:
            "I reach my hand back behind me."
            "And I soon find Jack's cock."
            show jack perv
            "He gasps as I rub it through his pants."
            "And he seems to like it a lot."
            "Because he gets good and hard as I massage his member."
            "So I know that he'll love what I do next."
            "I slip my hand into his pants and take hold of his cock."
            show fx exclamation
            "Jack gasps as I squeeze it."
            "But he doesn't tell me to stop."
            "Indeed, he seems to play much better as I caress it."
            bree.say "Mmm..."
            bree.say "You're so good at this, Jack."
            bree.say "You have to teach me all your secrets!"
            "I hear Jack let out a gasp and a whimper."
            "Then I feel a warm sensation between my fingers."
            "And I can't help smiling as I realise he just came."
            "It makes me feel hot too, turning me on like crazy."
            "And I have to fight to keep from touching myself."
            "Or else begging Jack to touch me too!"
        elif hero.morality <= -75:
            "I reach my hand back behind me."
            "And I soon find Jack's cock."
            show jack perv
            "He gasps as I rub it through his pants."
            "And he seems to like it a lot."
            "Because he gets good and hard as I massage his member."
            "Whenever he does something impressive in the game I squeeze it."
            "And I hear him gasp, struggling to keep on playing."
            "I could so easily slip my hand into his pants right now."
            "Jack's not said a single word to stop me."
            "And the feel of his cock right now..."
            "It's turning me on too!"
            "But I don't want to go too far or too fast."
            "So I just make do with teasing him tonight."
            "Enjoying the way he responds to my attentions."
            "As well as the way it's getting me hot at the same time!"
        elif hero.morality <= -50:
            "I wiggle my butt, rubbing it into his groin."
            show jack perv
            "And Jack seems to like that a lot."
            "Because I feel him getting nice and hard!"
            "I make sure to squeeze his thighs too."
            "Every time he does something impressive in the game."
            "I guess I could probably push him even further."
            "But I don't want to go too far or too fast."
            "So I just make do with teasing him tonight."
            "Enjoying the way he responds to my attentions."
            "As well as the way it turns me on too!"
        else:
            "I even wiggle my butt to show how excited I am."
            show jack perv
            "Which seems to get a positive reaction from him."
            "As he's soon getting nice and hard!"
            "I guess I could probably push him even further."
            "But I don't want to go too far or too fast."
            "So I just make do with teasing him tonight."
    else:
        "As much as I love them, none of my favourite one-player games will do here."
        "We need to be playing something that Jack and I can enjoy together."
        bree.say "How about we play No-man's Lands?"
        bree.say "It's been a while since I busted that one out."
        show jack happy
        "Jack nods with what looks like genuine enthusiasm."
        jack.say "Great idea, [hero.name]."
        jack.say "Are we playing one, two or three?"
        bree.say "Erm, duh!"
        bree.say "I have the game of the year editions of them all!"
        bree.say "DLCs, add-ons and all the other extras too!"
        bree.say "We're going to play one, then two and then three."
        "Jack seems to be finding my enthusiasm infectious."
        "He shuffles closer as I sit down on the floor in front of the TV."
        "And he's beaming when I hand over his joypad."
        show jack normal
        jack.say "I should warn you, [hero.name]."
        jack.say "I'm pretty good at this series!"
        bree.say "Hah!"
        bree.say "I'm so good I should play with one hand tied behind my back!"
        menu:
            "Play for fun":
                show jack happy
                "Jack laughs at this, clearly taking it as a joke."
                "And I laugh too, letting him keep on believing it."
                "It doesn't take me long to realise that I'm better than Jack."
                "I mean, he's good."
                "He's just not on the same level as me."
                "So I decide to hold back and just have fun."
                "I'm not so much letting Jack win the whole time."
                "More like I'm trying to make it fun for the both of us."
                "Between each game, Jack's mood improves."
                "After No-man's Land 1, he begins to let his guard down."
                "After No-man's Land 2, he's telling me all about his RPG exploits."
                "And after No-man's Land 3, he's sharing embarrassing stories about [mike.name]'s childhood!"
                show jack normal
                jack.say "Wow..."
                jack.say "We have to stop soon, [hero.name]."
                jack.say "My eyes are getting tired!"
                bree.say "You're just saying that because I beat you so badly!"
                $ jack.love += 2
            "Play to win":
                show jack happy
                "Jack laughs at this, clearly taking it as a joke."
                "But then he takes a look at the serious expression on my face."
                show jack normal
                "And I see him swallow in trepidation."
                "What follows is a journey through three amazing games."
                "In the course of which I drag hammer Jack without mercy."
                "He wasn't lying when he said that he was good."
                "But the problem is that I'm much better."
                "And now my competitive switch has been thrown!"
                "Between each game Jack's mood changes."
                "After No-man's Land 1, he laughs and jokes."
                "After No-man's Land 2, he asks me to go easy on him."
                "And after No-man's Land 3, he stares at me in stunned silence."
                jack.say "I..."
                jack.say "I guess you win, [hero.name]!"
                bree.say "YES...YES...YES!"
                bree.say "You're damn right I win!"
                bree.say "Suck it up, loser-boy!"
                $ jack.love -= 2
    show jack normal
    "Soon enough we've managed to gorge ourselves on the pizza."
    "And we've played all the games that we can manage."
    "Jack lets out a yawn of genuine fatigue."
    "And I can't help yawning in sympathy."
    jack.say "Oh, man - I'm SO sleepy right now!"
    bree.say "Me too, Jack."
    bree.say "Looks like you've worn me out!"
    "Jack laughs, but looks a little bashful at the same time."
    "He gathers his things and gets up, and I follow his lead."
    show bg house
    "We walk to the front door and I open it, letting him out."
    "But he pauses on the doorstep, trying to look me in the eye."
    jack.say "I...I had a really great time tonight, [hero.name]."
    bree.say "Me too, Jack."
    jack.say "You did?!?"
    bree.say "Of course I did, silly!"
    jack.say "You're pretty fun to hang out with, [hero.name] - just like a guy!"
    show fx drop
    jack.say "N...not that I mean you're LIKE a guy!"
    "I can't help laughing at Jack as he stammers and stutters."
    "It's such a cute way he has of putting his foot in it!"
    bree.say "I know what you mean, Jack."
    bree.say "Even if you don't!"
    bree.say "This was fun - we should do it again soon."
    hide jack
    "With that, I plant a kiss on his cheek and close the door."
    "And I have to try real hard not to look through the peep-hole."
    "Because I bet the look on his face is priceless!"
    return

label jack_female_event_04:
    if jack.love.max < 80:
        $ jack.love.max = 80
    show jack normal
    "The next time I see Jack, I can tell that there's something on his mind."
    "He's doing that thing that guys do when there's something up and it's bugging them."
    "Like he's distracted all the time, but he's trying to act like nothing's the matter."
    "Part of me wants to call him out the moment I realise what he's doing."
    "But Jack's so cute and hopeless when he's like this - it's kind of sweet!"
    jack.say "Ah..."
    jack.say "H...hey, [hero.name]!"
    "I give Jack what I hope is a straight-up smile."
    "After all, I don't want him to know that I'm onto him yet."
    bree.say "Hey, Jack!"
    bree.say "Great to see you."
    jack.say "Y...you wouldn't happen to know if..."
    jack.say "Maybe there'd be a chance that..."
    jack.say "If you're not busy you might want to..."
    "I nod, trying to encourage Jack to get to the point."
    "At this rate, he's going to trip over his own words!"
    jack.say "C...come with me to a convention?"
    jack.say "You know - a comic convention?"
    jack.say "It's two weeks from now."
    jack.say "[mike.name] and I were supposed to be going."
    jack.say "But he's cancelled on me - so I have a spare ticket!"
    menu:
        "Accept":
            "A comic convention?"
            "The kind with superheroes, videogames and geeky stuff?"
            "What's not to like about that?!?"
            bree.say "How did I not know this was happening?"
            bree.say "Of course I want to come, Jack!"
            bree.say "You just try and stop me!"
            show jack happy
            "Jack's face lights up at my answer."
            "And I can see all of the anxiety drain out of him."
            jack.say "Really, [hero.name]?"
            jack.say "That's great!"
            jack.say "I...I mean I'd have loved to go with [mike.name]."
            jack.say "But it's great that you can come along instead!"
            "Jack nods, accepting my decision."
            show jack normal
            show fx exclamation
            "But then his eyes light up."
            "And he looks like he just remembered something important."
            jack.say "Oh yeah, I forgot to say..."
            jack.say "There's a big cosplay contest too."
            jack.say "One that anyone with a ticket can enter!"
            bree.say "Wow!"
            bree.say "That's even better, Jack!"
            bree.say "I'm definitely coming with you now."
            "Then a thought occurs to me."
            bree.say "Jack..."
            bree.say "Are you going to be entering this contest?"
            jack.say "No, [hero.name] - I wasn't going to this year."
            bree.say "Oh...okay..."
            show jack happy
            jack.say "But there's a prize for the winner!"
            bree.say "Ooh..."
            bree.say "I wonder what it could be!"
            "That's not all I'm wondering about either."
            "Maybe I should read up on costume design before I get started?"
            "A little practice wouldn't go amiss either!"
            $ jack.love += 2
            $ game.flags.cosplay_prepared = 10
            $ jack.flags.convention_delay = TemporaryFlag(True, 14)
            return
        "Think it through":
            "Normally I'd jump at the chance to attend a comic convention."
            "I'd be in geek heaven with all the superheroes and videogame stuff."
            "But I don't think I'm ready to spend that much time alone with Jack."
            "Not without a chaperone or something of that kind."
            bree.say "Maybe…"
            bree.say "You said it's two weeks away?"
            "Jack looks hopeful."
            jack.say "Erm..."
            jack.say "Yeah, [hero.name] - in a fortnight."
            bree.say "Hmm..."
            bree.say "I'll have to check my schedule."
            "I see Jack's face fall a little."
            "Because that's obviously not the answer he wanted to hear."
            jack.say "Oh..."
            jack.say "Okay, [hero.name], I understand."
        "Decline":
            "Normally I'd jump at the chance to attend a comic convention."
            "I'd be in geek heaven with all the superheroes and videogame stuff."
            "But I don't think I'm ready to spend that much time alone with Jack."
            "Not without a chaperone or something of that kind."
            bree.say "Oh, darn it!"
            bree.say "You said it's two weeks away?"
            jack.say "Erm..."
            jack.say "Yeah, [hero.name] - in a fortnight."
            bree.say "Sorry, Jack, I can't."
            bree.say "I already made plans for then."
            "Jack looks instantly crestfallen."
            "But he tries to hide his disappointment."
            jack.say "Oh..."
            jack.say "Okay, [hero.name], I understand."
            $ jack.love -= 2
            $ jack.flags.convention_declined = True
            return
    "Jack nods, accepting my decision."
    show fx exclamation
    "But then he seems to remember something else."
    "Something important enough to mention."
    "Even though I already gave him an answer."
    jack.say "Oh yeah, I forgot to say..."
    jack.say "There's a big cosplay contest too."
    jack.say "One that anyone with a ticket can enter!"
    menu:
        "Decline":
            bree.say "That sounds nice, Jack."
            bree.say "But I still can't change my plans."
            bree.say "Not just for the chance to get dressed up!"
            jack.say "Ah well..."
            jack.say "It was worth a try!"
            "And with that, Jack finally lets the matter drop."
            "He doesn't say another word about the convention."
            "Much to my relief!"
            $ jack.love -= 1
            $ jack.flags.convention_declined = True
            return
        "Accept":
            bree.say "A cosplay contest?"
            bree.say "A chance to dress up as my favourite character?!?"
            show jack happy
            jack.say "Yeah, [hero.name] - that's right!"
            if hero.morality <= -100:
                "I change my mind as soon as Jack says the words."
                "All I can think about is how sexy and sultry I can make my costume."
                "And how it'll feel to have every eye at the convention on me too!"
                "Not to mention how hot it'll make Jack once he sees me in it."
                "Maybe we'll be able to sneak off somewhere during the convention?"
                "Somewhere I can let him have his way with me..."
                bree.say "Wow!"
                bree.say "Why didn't you say so before, Jack!"
                bree.say "I'm definitely coming with you now."
            elif hero.morality <= -75:
                "The moment I hear him say those words, I change my mind."
                "An image of what I can wear pops into my mind almost instantly."
                "As extreme and sexy as I can possibly make it."
                "Without getting arrested for indecent exposure, that is!"
                "I can already feel myself getting turned-on by the mental image..."
                bree.say "Wow!"
                bree.say "Why didn't you say so before, Jack!"
                bree.say "I'm definitely coming with you now."
            elif hero.morality <= -50:
                "I can almost see the costume I'm going to wear now."
                "I can picture the look on Jack's face when he sees me too!"
                "In fact, the thought is getting me pretty excited."
                "And that makes it impossible to resist."
                bree.say "Wow!"
                bree.say "Why didn't you say so before, Jack!"
                bree.say "I'm definitely coming with you now."
            elif hero.morality <= -25:
                "Suddenly my mind is filled with the possibilities."
                "So many options for costumes."
                "And so many of them that'll make Jack's eyes pop out too!"
                bree.say "Wow!"
                bree.say "Why didn't you say so before, Jack!"
                bree.say "I'm definitely coming with you now."
            else:
                bree.say "Wow!"
                bree.say "Why didn't you say so before, Jack!"
                bree.say "I'm definitely coming with you now."
            "Jack smiles at my change of heart."
            "But he also looks a little confused."
            show jack normal
            jack.say "But..."
            jack.say "What about your plans, [hero.name]?"
            bree.say "Never mind that, Jack."
            bree.say "I can just reschedule!"
            "Then a thought occurs to me."
            bree.say "Jack..."
            bree.say "Are you going to be entering this contest?"
            jack.say "No, [hero.name] - I wasn't going to this year."
            bree.say "Oh...okay..."
            show jack happy
            jack.say "But there's a prize for the winner!"
            bree.say "Ooh..."
            bree.say "I wonder what it could be!"
            $ jack.love += 1
            $ game.flags.cosplay_prepared = 10
            $ jack.flags.convention_delay = TemporaryFlag(True, 14)
    return

label prepare_cosplay:
    "I pass some time working on my cosplay for the convention..."
    $ game.flags.cosplay_prepared += 10
    if game.flags.cosplay_prepared >= 100:
        "It looks perfect now!"
    elif game.flags.cosplay_prepared >= 70:
        "It's looking good already."
    elif game.flags.cosplay_prepared >= 30:
        "It's progressing well."
    else:
        "There's still plenty of work to do."
    return

label jack_female_event_05:
    if jack.love.max < 120:
        $ jack.love.max = 120
    $ jack.flags.nodate = False
    $ jack.flags.forceLocation = (game.days_played, game.hour, "street")
    scene bg arena
    show jack normal casual
    "Being at the comic convention is like being a kid at Christmas."
    "There's no other way I can explain how excited I am right now!"
    "Everywhere I look there's something shiny and new."
    "I want to see and do everything the moment I lay eyes on it!"
    "So I end up flitting this way and that."
    "And I drag Jack along with me as I go."
    "But it's not like he's complaining."
    if hero.has_skill("cosplayer") or game.flags.cosplay_prepared >= 50:
        "Everything I rush to see, he's crazy about too!"
        "Well, that and the fact that I'm in my costume for the cosplay contest later on."
        "I'm dressed as a certain character called Sindee from a certain popular videogame."
        "And let's just say that he's impressed with the effort I made for my entry!"
        jack.say "I said it already, [hero.name]."
        show jack happy
        jack.say "But you look amazing!"
        bree.say "Aw..."
        bree.say "Thank you for noticing!"
        "I smile at Jack's compliment."
        "But the very next moment my attention is elsewhere."
    bree.say "Oh god, Jack!"
    bree.say "Is that the guy who draws Tank Babe?!?"
    show jack normal
    jack.say "I...I think so..."
    bree.say "And there - right over there!"
    bree.say "I think I see Nate Filliman."
    bree.say "The captain from Glowbug!"
    jack.say "Wh...where, [hero.name]?!?"
    "But then I stop dead in my tracks."
    "And Jack almost walks straight into my back." with hpunch
    jack.say "Oof..."
    jack.say "Hey, what the..."
    bree.say "Oh...my...god..."
    bree.say "Jack, that's...that's Metallikea!"
    bree.say "They're right there!"
    bree.say "All of them!"
    "Jack squints in the direction I'm pointing."
    "And then he nods his head."
    show fx exclamation
    jack.say "Wow..."
    jack.say "You're right, [hero.name]!"
    jack.say "They must be promoting the new Sitar Heroes game."
    jack.say "I didn't know you were a fan too!"
    "I wave away the comment with a flapping hand."
    "And I make snort to show how silly Jack's comment is."
    bree.say "Of course I'm a fan, Jack!"
    bree.say "Metallikea are like the best band ever!"
    bree.say "Come on - let's go join the queue to get something signed!"
    "Without waiting for an answer, I rush over to the queue."
    "Jack joins me a moment later, panting from the dash across the floor."
    jack.say "Phew..."
    jack.say "Made it!"
    jack.say "Aww..."
    jack.say "Look at the length of the queue!"
    if hero.morality <= -25:
        bree.say "Urgh...I know."
        bree.say "But let me see what I can do about it..."
        "I lean out of the queue and wave to one of the band's security guys."
        "He looks at me, rolls his eyes and then begins to saunter over."
        jack.say "Erm, [hero.name]..."
        jack.say "What are you doing?"
        "Ignore Jack's question."
        "And I whisper into the security guy's ear."
        "He grins the moment he hears what I have to say."
        "Then he motions for us to step out of the queue and follow him."
        show fx exclamation
        "Jack's mouth literally drops open."
        "But he hurries after me all the same."
        "Less than a minute later, we're standing in front of the band."
        if hero.morality <= -100:
            "Metallikea Guy" "Hey, babe!"
            "Metallikea Guy" "Are you the chick with something special to show us?"
            "I smile and step forward before Jack can say a word."
            show jack perv
            "And at the same time, I pull down my top."
            "Exposing my breasts for the entire band to see."
            "They pull off their shades and stare, wide-eyed."
            "I can feel their gazes upon me the whole time."
            "And my efforts get a cheer from the queuing fans."
            "Metallikea Guy" "Whoa..."
            "Metallikea Guy" "This really is a rock n' roll town!"
        elif hero.morality <= -75:
            "Metallikea Guy" "Hey, babe!"
            "Metallikea Guy" "Are you the chick with something special for us to sign?"
            "I smile and step forward before Jack can say a word."
            show jack perv
            "And at the same time, I pull down my top."
            "Each member of the band signs my chest with their marker pens."
            "I can feel each and every stroke as they write."
            "And my efforts get a cheer from the queuing fans."
            "Metallikea Guy" "Whoa..."
            "Metallikea Guy" "I wish we got asked to sign more stuff like that!"
        elif hero.morality <= -50:
            "Metallikea Guy" "Hey, babe!"
            "Metallikea Guy" "Are you the chick that's got a kiss for all of us?"
            "I smile and step forward before Jack can say a word."
            show jack perv
            "And I plant a kiss on each band member's lips."
            "I make sure to give each one of them some tongue action."
            "Lingering a little longer than I should every time."
            "And my efforts get a cheer from the queuing fans."
            "Metallikea Guy" "Whoa..."
            "Metallikea Guy" "We'll sign anything you want for that!"
        else:
            "Metallikea Guy" "Hey, babe!"
            "Metallikea Guy" "Are you the chick that's got a kiss for all of us?"
            "I smile and step forward before Jack can say a word."
            show jack perv
            "And I plant a kiss on each band member's lips."
            "There's no tongues involved and it's over in mere seconds."
            "But it still gets a cheer from the queuing fans."
            "Metallikea Guy" "Whoa..."
            "Metallikea Guy" "We'll sign anything you want for that!"
        "After my little performance, the band are eating out of the palm of my hand."
        "They eagerly sign photos with whatever Jack and I ask of them."
        "But as we walk away, he seems to be in a strange kind of daze."
        bree.say "Are you okay, Jack?"
        show jack normal
        jack.say "Ah...yeah, I guess."
        jack.say "I just can't believe that actually happened!"
        bree.say "Do you mean the autographs?"
        bree.say "Or how I got them?"
        jack.say "B..both!"
    else:
        bree.say "Urgh...I know."
        bree.say "But what can we do about it, right?"
        "Jack shrugs."
        "But then he nods."
        "And we settle in to wait our turn."
        scene bg black with dissolve
        pause 1.0
        scene bg arena
        show jack
        with dissolve
        "After what seems like an age, we make it to the front."
        "I step forwards at the signal from one of the band's security."
        "But as Jack makes to follow me, the security guy holds up his hand."
        "Security" "Uh-uh..."
        "Security" "That's it, buddy!"
        "Security" "This little lady's the last for the day."
        bree.say "What?!?"
        bree.say "That's not fair!"
        "Security" "Not my problem."
        "Security" "Either you're the last or the guy that went before you is."
        "Security" "Make up your mind, lady!"
        show jack happy
        jack.say "It's okay, [hero.name]."
        jack.say "I'll just wait for you here."
        "Before I can protest, the security guy shoves me forwards."
        hide jack
        "Metallikea Guy" "Hey, babe!"
        "Metallikea Guy" "Who'd you want this making out to?"
        "I think for a moment."
        "And then I lean in, whispering in his ear."
        "Metallikea Guy" "Here you go!"
        "I'm handed a photograph of the band."
        "And then hustled away before the ink is even dry on the autographs."
        show jack
        jack.say "Hey, [hero.name]!"
        jack.say "Let me see what they wrote!"
        menu:
            "Autograph for myself":
                "I hold up the photo for Jack to see."
                "And he strains to read the words in black marker pen."
                jack.say "'To [hero.name]...Metal Forever - Metallikea!'"
                show jack perv
                jack.say "Wow..."
                jack.say "That's so cool, [hero.name]!"
                jack.say "I wish I'd gotten one too."
                "I can't help feeling a little sorry for Jack."
                "But it was just dumb luck that I got the last one."
            "Autograph for Jack":
                "I hold up the photo for Jack to see."
                "And he strains to read the words in black marker pen."
                jack.say "'To Jack...Metal Forever - Metallikea!'"
                show jack perv
                "I see Jack's eyes go wide."
                "And then he looks at me in disbelief."
                jack.say "NO WAY!"
                bree.say "Yes way, Jack!"
                bree.say "I asked them to sign it to you."
                bree.say "It's my way of saying thanks for bringing me along!"
                "Jack still looks dumbstruck."
                "But now there's something else in his eyes too."
                bree.say "Jack..."
                bree.say "Why are you looking at me like that?"
                jack.say "Huh...like what?"
                bree.say "Like I just gave you one of my kidneys!"
                show jack happy
                jack.say "Oh, sorry..."
                jack.say "You just really blew me away, that's all!"
                bree.say "Aw...thank you, Jack!"
                $ jack.love += 10
    show jack
    "It takes a while for Jack to come down from the experience of meeting Metallikea."
    "And we spend that time wandering around the convention floor in a state of sheer awe."
    "There's just so much cool stuff to see and do, neither of us knows where to start."
    "But I soon begin to notice that Jack's not starstruck anymore."
    "Yet he still seems to be in a little bit of a daze."
    bree.say "What's the matter, Jack?"
    bree.say "Are you overloaded on geeky goodness?"
    jack.say "N...no, [hero.name] - it's not that."
    jack.say "It's just..."
    jack.say "Well, I never met a girl as into this kind of stuff as you."
    jack.say "I thought I was a geek, but you're giving me a run for my money!"
    "For a moment I feel a pang of worry in my gut."
    "I know how defensive guys can be when it comes to their interests."
    "And some of them just hate it when a girl knows as much as they do!"
    bree.say "That's not a problem...is it, Jack?"
    show jack happy
    jack.say "Aw, hell no, [hero.name]!"
    jack.say "It's great, just great!"
    jack.say "Most girls would be bored stiff right now."
    jack.say "But you're still going strong!"
    "I break out into a smile of genuine relief."
    "But I don't have more than a few seconds to enjoy it."
    show jack normal
    jack.say "Oops..."
    jack.say "Look at the time, [hero.name]!"
    bree.say "Oh yeah!"
    bree.say "They're about to start judging the cosplay contest."
    if not (hero.has_skill("cosplayer") or game.flags.cosplay_prepared >= 50):
        "I can't help my face falling at the sight of all the contestants."
        "There's a stage full of them, looking all cute and colourful."
        "Jack looks disappointed too, like he wishes I was up there with them."
        bree.say "I kinda wish I'd entered the competition now!"
        jack.say "Yeah, me too!"
        jack.say "But there's always next year, right?"
        bree.say "Is that an invitation to do this all over again?"
        jack.say "Erm...I guess it is, [hero.name]!"
        jack.say "If you want to, that is..."
        bree.say "Of course I do, silly!"
        bree.say "Now, we have more geeky stuff to do and see!"
        jack.say "Okay - let's go!"
        "And with that, we dive back into the crowds amongst the stalls."
        $ jack.love -= 3
        return
    bree.say "I have to get over there!"
    "Without asking permission, I grab hold of Jack's hand."
    "And then I run through the crowds of convention-goers." with hpunch
    "This means that he's dragged in my wake, bouncing off of one person after another." with hpunch
    "Soon enough we arrive at the stage where the contest is going to be judged."
    "I hastily make myself known to the organisers and get ushered onto the stage."
    hide jack
    "The next thing I know, I'm waiting in line for my turn to step forwards."
    "Organiser" "And now, we have [hero.name]."
    "Organiser" "Cosplaying Sindee, from Penultimate Fantasy 15!"
    "I take a deep breath and step forwards."
    "My mind racing as I think how I should handle this..."
    menu:
        "Play the character":
            "Time to put the 'play' in 'cosplay', I guess!"
            "I know the character inside out."
            "So it shouldn't be too hard to pull off the role."
            bree.say "Hey, Prompto - what are you looking at?"
            bree.say "Grandpa Cid taught me everything I know!"
            if hero.has_skill("video_games"):
                "The crowd pops for the lines."
                "They obviously remember Sindee from the game."
                "I just hope that it's good enough to impress the judges too!"
                $ game.flags.cosplay_prepared += 15
            else:
                $ game.flags.cosplay_prepared -= 10
        "Strike poses":
            "I know Sindee's character inside out."
            "And I could reel off some improvised lines."
            "But this is cosplay, not an actual play."
            "So maybe it's the visuals that count?"
            "I stride out onto the stage and strike a dynamic pose."
            "And then I transition into something a bit for coy and fun."
            "Best to give them the full range that I can pull off."
            if hero.charm >= 25:
                "The crowd seems to like it well enough."
                "They obviously remember Sindee from the game."
                "I just hope that it's good enough to impress the judges too!"
                $ game.flags.cosplay_prepared += 10
            else:
                $ game.flags.cosplay_prepared -= 5
        "Make sexy moves":
            "Let's face it - everyone pretends that cosplay is about dressing-up."
            "We all claim to be impressed by the outfits and the make-up."
            "But in reality, it's all about the chance to dress sexy."
            "And then have people drool over you like salivating dogs!"
            "That's why I don't bother reciting any lines."
            "And I certainly don't pull off the poses from the game."
            "Instead I stride out there and flash everything that I have."
            "Ass, tits and even lips are pouted and pushed into their faces."
            "I give them all that I can."
            "Well, everything short of resorting to a strip-tease!"
            if -50 > hero.morality <= -10:
                "The crowd seems to like it well enough."
                "They obviously still have a hard-on for Sindee from the game."
                "I just hope that it's good enough to impress the judges too!"
                $ game.flags.cosplay_prepared += 15
            else:
                $ game.flags.cosplay_prepared -= 10
    "Once my turn on the stage is over, I step back into line."
    "All I can do now is hope that I made the right impression."
    show jack happy
    "As I wait, I glance down and see that Jack is watching me."
    "He smiles and gives me a thumps up, showing his approval."
    "So I know that I have at least one real fan in the crowd!"
    hide jack
    if game.flags.cosplay_prepared >= 90:
        "The judges reel off the names of the winners."
        "Organiser" "And the overall winner is...[hero.name]!"
        "Organiser" "Cosplaying Sindee, from Penultimate Fantasy 15!"
        "For a moment I can't actually believe it."
        "But then I'm ushered forwards to claim my prize."
        "There's some kind of impressive certificate."
        "And there's also an envelope crammed with one thousand dollars!"
        "I try to say something, but I'm lost for words."
        "Though I wouldn't have been heard over the sound of the crowd anyway!"
        $ jack.love += 5
        $ jack.sub += 3
    else:
        "The judges reel off the names of the winners."
        "And I'm disappointed not to hear my name amongst them."
        "But I force a smile onto my face all the same."
        "And I dutifully clap for the big winner as they claim their prize."
        $ jack.love += 2
        $ jack.sub += 1
    show jack happy casual
    "As soon as I'm off the stage, Jack comes hurrying over."
    "He has a huge smile on his face, making me smile in turn."
    jack.say "Well done, [hero.name]."
    jack.say "You were great up there!"
    "I look at Jack for a moment, studying his face."
    "And it becomes clear to me that my winning or losing doesn't matter to him."
    "He seems more proud of being able to call himself my friend than anything else."
    "I guess that's something that makes him pretty special in his own right."
    bree.say "Thanks, Jack."
    bree.say "I saw you cheering me on during the contest."
    bree.say "And I don't think I could have done it without you!"
    show jack perv
    "Jack instantly blushes at this, embarrassed and bashful."
    jack.say "Y...you really mean that, [hero.name]?"
    bree.say "Of course I do, silly!"
    bree.say "Now, we have more geeky stuff to do and see!"
    show jack happy
    jack.say "Okay - let's go!"
    "And with that, we dive back into the crowds amongst the stalls."
    return

label jack_female_event_06:
    if jack.love.max < 140:
        $ jack.love.max = 140
    $ jack.flags.nokiss = False
    scene bg bedroom4
    show jack casual
    "I know that we girls are supposed to be able to read a guy like a book."
    "But that's one of those supposedly female things I've always struggled with."
    "I dunno - maybe it's because I'm less of a girly girl than most, you know?"
    "Like being into things that guys like too has made me more like them."
    "Whatever the reason, it means I don't tune into Jack at first."
    "And it takes me a while to realise there must be something on his mind."
    "We're just hanging out in my bedroom."
    "But he looks like he's a million miles away right now."
    bree.say "Erm..."
    bree.say "What's up, Jack?"
    show fx exclamation
    "At the sound of the question, Jack looks up."
    "The surprise on his face is plain to see."
    "I guess most of the girls he knows aren't this up-front with him!"
    "But then, how many other girls does Jack even know?"
    jack.say "Huh?"
    jack.say "Oh...it's...it's nothing, [hero.name]."
    bree.say "Well, it must be something, Jack."
    bree.say "Otherwise there wouldn't be anything to call nothing - would there?"
    "Jack frowns as he tries to follow my reasoning."
    "But he nods all the same."
    show fx drop
    jack.say "I guess so, [hero.name]."
    bree.say "Come on, Jack."
    bree.say "Whatever it is - you can tell me!"
    "Jack looks me in the eye in complete silence for a few seconds."
    "Then he takes a deep breath, preparing to spill his guts."
    jack.say "Well..."
    jack.say "It's like this, [hero.name]..."
    jack.say "Do you...do you like how I look?"
    jack.say "I mean, would you like me better if I maybe looked...different?"
    "Now it's my turn to be caught by surprise."
    "I'm just not used to Jack asking me stuff like that!"
    "And I can't help looking him up and down in response."
    "He looks...well, he just looks like Jack!"
    "Brown hair, little goatee, band t-shirt."
    "Usually grinning and with a goofy expression on his face."
    "But would I change anything about him?"
    menu:
        "You're perfect as you are":
            "I don't even have to think about my answer."
            "I'm already shaking my head at Jack."
            bree.say "No, Jack!"
            bree.say "No, no, no!"
            "Jack looks surprised by my answer."
            "That and the passion with which it's delivered."
            jack.say "Huh?!?"
            jack.say "What do you mean, [hero.name]?"
            jack.say "Even my Mom says I could stand to lose a couple of pounds!"
            "I shake my head at this."
            bree.say "I'm not your mom, Jack!"
            bree.say "And I like you just the way you are."
            "I throw my arms around Jack, pulling him close to me."
            "He returns the gesture, and we enjoy an intense session of cuddling."
            bree.say "Ah..."
            bree.say "Look, Jack - you can lose all the weight you want if it makes you happier."
            bree.say "What I mean is that you don't have to change for me."
            bree.say "And don't change who you are in here!"
            "I tap the centre of his chest, just where his heart is."
            show jack happy
            $ jack.love += 3
            $ game.active_date.score += 50
            jack.say "Okay, [hero.name]."
            jack.say "I promise!"
        "You could use a little refinement":
            "I sit back and stare at Jack for a moment."
            "And he waits in tentative silence as I look him up and down."
            bree.say "Just for the record, Jack."
            bree.say "I think you look pretty good right now."
            bree.say "But there's always room for a little improvement."
            "Jack looks more than a little confused."
            "Like he's not sure how to take that statement."
            jack.say "Erm..."
            jack.say "Is that a yes or a no, [hero.name]?"
            bree.say "Don't think of it as either, Jack."
            bree.say "Think of it as an opportunity instead!"
            show fx drop
            "Jack still looks confused."
            "Staring at me like a dog that's been shown a card-trick."
            bree.say "What I mean is we could do small things, make easy changes."
            if hero.morality <= -100:
                bree.say "Like we could get you some bondage gear!"
                bree.say "Black rubber, chains and clamps!"
                bree.say "Mmm...I can see it now, Jack!"
            elif hero.morality <= -75:
                bree.say "Like we could get you some ink!"
                bree.say "Tattoos, you know?"
                bree.say "Make you look like the bad boy you really are!"
            elif hero.morality <= -50:
                bree.say "Like we could freshen up your wardrobe."
                bree.say "Get you some clothes that show off your guns!"
            elif hero.morality <= -25:
                bree.say "Like we could get you a piercing."
                bree.say "In your ear - or maybe somewhere else!"
            else:
                bree.say "Like we could be gym buddies, you know?"
                bree.say "And eat healthy together?"
        "You need a lot of work":
            "I hate to admit as much."
            "But there's a lot of room for improvement!"
            "And they do say that honesty is the best policy."
            bree.say "Well, now that you mention it, Jack..."
            bree.say "You could stand to lose a couple of pounds here and there."
            $ jack.love -= 5
            $ game.active_date.score -= 50
            "Jack looks instantly hurt."
            "But he nods all the same."
            jack.say "Cut down on the cheeseburgers - okay."
            bree.say "And you do dress a little slobby too!"
            "Jack almost winces at this."
            "And I feel his pain too!"
            show fx question
            jack.say "M...my clothes?"
            jack.say "I suppose I never thought of that..."
            "I try as best I can to make it sound positive."
            "Like this is friendly advice, not character assassination."
            bree.say "Sure, Jack - that's all."
            bree.say "Apart from your hair, head, facial and bodily."
            bree.say "The fact that you only talk about geek stuff."
            bree.say "Oh, and your general levels of personal hygiene too!"
            "Jack nods slowly, looked utterly stunned."
            "I try to make it all better by smiling at him."
            "But he goes quiet for the rest of the time he's over."
            return
    show jack normal
    "Jack seems to cheer up after hearing what I have to say."
    "He's still quiet and looks like he has a lot on his mind."
    "But there's no longer the sense of tension hanging in the air."
    "Though I can't help feeling like he needs more reassurance."
    "Maybe words alone aren't enough?"
    if hero.morality <= -100:
        "I lean over towards Jack."
        hide jack
        show jack kiss
        $ jack.flags.kiss += 1
        "And without saying a word, I kiss him."
        "I don't hesitate to slip my tongue between his lips."
        "It's in his mouth before he even knows what's happening!"
        "But it doesn't take him more than a moment to respond."
        "Jack rises to the occasion, returning the passion of the kiss."
        "I can feel his hands on my body the whole time."
        "Just like mine are running up and down him too!"
        "He gasps as I almost tear open his pants."
        "And a second later his cock is in my hand."
        scene jack handjob
        bree.say "Mmm..."
        bree.say "Jack, it's SO big!"
        bree.say "You must like me a lot, huh?"
        "Jack nods as I begin to work the shaft of his cock."
        "He can't hope to actually speak at that moment in time."
        "Instead he just pants and gasps at the sensations he's feeling."
        "Using my other hand to squeeze his balls, I pick up speed."
        "Jack gets bigger and bigger as I handle him."
        "And by the time he can't get any larger, he's utterly helpless."
        jack.say "Oh shit..."
        jack.say "Oh shit, [hero.name]!"
        scene jack blowjob
        "It's only now that I truly pounce on him."
        "I have the head of his cock in my mouth a moment later."
        "Jack's already pretty excited, and this pushes him further still."
        "I hardly have to swallow more than a few inches of his cock."
        "And I can already feel him bucking and twitching beneath me."
        "Jack collapses backwards as he shoots his load."
        show jack blowjob out
        "I let his cock slip out of my mouth as he does so."
        "Which means that I take it all in the face."
        show jack blowjob onface
        "Jack's cum spatters over my nose and cheeks."
        "And then it runs down, over my lips and onto my chin."
        "I gaze down at him the whole time, smiling happily."
        "Making a point of licking my lips and tasting the droplets."
        $ jack.sub += 5
        $ game.active_date.score += 100
    elif hero.morality <= -75:
        "I lean over towards Jack."
        hide jack
        show jack kiss
        $ jack.flags.kiss += 1
        "And without saying a word, I kiss him."
        "I don't hesitate to slip my tongue between his lips."
        "It's in his mouth before he even knows what's happening!"
        "But it doesn't take him more than a moment to respond."
        "Jack rises to the occasion, returning the passion of the kiss."
        "I can feel his hands on my body the whole time."
        "Just like mine are running up and down him too!"
        "He gasps as I almost tear open his pants."
        "And a second later his cock is in my hand."
        scene jack handjob
        bree.say "Mmm..."
        bree.say "Jack, it's SO big!"
        bree.say "You must like me a lot, huh?"
        "Jack nods as I begin to work the shaft of his cock."
        "He can't hope to actually speak at that moment in time."
        "Instead he just pants and gasps at the sensations he's feeling."
        "Using my other hand to squeeze his balls, I pick up speed."
        "Jack gets bigger and bigger as I handle him."
        "And by the time he can't get any larger, he's utterly helpless."
        jack.say "Oh shit..."
        jack.say "Oh shit, [hero.name]!"
        scene jack blowjob
        "It's only now that I truly pounce on him."
        "I have the head of his cock in my mouth a moment later."
        "Jack's already pretty excited, and this pushes him further still."
        "I hardly have to swallow more than a few inches of his cock."
        "And I can already feel him bucking and twitching beneath me."
        "Jack collapses backwards as he shoots his load."
        show jack blowjob inmouth
        "It hits the back of my throat, warm and sticky."
        "And I only just manage to swallow it down without choking!"
        "Once I'm sure Jack's done, I slide his cock out of my mouth."
        "And I smile as I lick my lips."
        $ jack.love += 1
        $ jack.sub += 3
        $ game.active_date.score += 80
    elif hero.morality <= -50:
        "I lean over towards Jack."
        hide jack
        show jack kiss
        $ jack.flags.kiss += 1
        "And without saying a word, I kiss him."
        "I don't hesitate to slip my tongue between his lips."
        "It's in his mouth before he even knows what's happening!"
        "But it doesn't take him more than a moment to respond."
        "Jack rises to the occasion, returning the passion of the kiss."
        "I can feel his hands on my body the whole time."
        "Just like mine are running up and down him too!"
        "He gasps as I almost tear open his pants."
        "And a second later his cock is in my hand."
        scene jack handjob
        bree.say "Mmm..."
        bree.say "Jack, it's SO big!"
        bree.say "You must like me a lot, huh?"
        "Jack nods as I begin to work the shaft of his cock."
        "He can't hope to actually speak at that moment in time."
        "Instead he just pants and gasps at the sensations he's feeling."
        "Using my other hand to squeeze his balls, I pick up speed."
        "Jack gets bigger and bigger as I handle him."
        "And by the time he can't get any larger, he's utterly helpless."
        jack.say "Oh shit..."
        jack.say "Oh shit, [hero.name]!"
        show jack handjob cumshot
        "Jack collapses backwards as he shoots his load."
        "It spurts out of his cock and over my hand."
        "Warm and sticky, it runs down my arm too."
        "And I can't help smiling now that it's over."
        $ jack.love += 2
        $ jack.sub += 2
        $ game.active_date.score += 70
    elif hero.morality <= -25:
        "I lean over towards Jack."
        hide jack
        show jack kiss
        $ jack.flags.kiss += 1
        "And without saying a word, I kiss him."
        "I don't hesitate to slip my tongue between his lips."
        "It's in his mouth before he even knows what's happening!"
        "But it doesn't take him more than a moment to respond."
        "Jack rises to the occasion, returning the passion of the kiss."
        "I can feel his hands on my body the whole time."
        "Just like mine are running up and down him too!"
        "The sensation of it lingers in my memory."
        "And I can't help smiling, even when it's over."
        $ jack.love += 2
        $ jack.sub += 1
        $ game.active_date.score += 60
    else:
        "I lean over towards Jack."
        hide jack
        show jack kiss
        $ jack.flags.kiss += 1
        "And without saying a word, I kiss him."
        "It's great to feel how he rises to it."
        "And the sensation sends tingles down my spine."
        "Though it doesn't last long, it lingers in my memory."
        "And I can't help smiling, even when it's over."
        $ jack.love += 2
        $ game.active_date.score += 50
    return

label jack_female_event_07:
    if jack.love.max < 160:
        $ jack.love.max = 160
    $ jack.flags.nodate = False
    scene expression f"bg {game.room}"
    show jack sad at center, zoomAt(1.5, (640, 1080))
    with fade
    "Most of the time it's pretty easy to read Jack, as he can't really hide his emotions."
    "And it's especially easy to read him when he's trying hard to hide his emotions anyway."
    "At times like that, he might as well have what he's feeling tattooed on his forehead."
    "Because it's all there, plain as day and so easy to read it almost makes me want to weep!"
    "Like right now, Jack's shooting me meaningful looks all the time."
    show jack annoyed at backforth(1.0, -10, 0)
    "But when I look up to meet his eyes, he instantly looks away again."
    "It's almost like Jack's not got the courage to just come out and ask me about whatever's on his mind."
    "And instead he's trying to coax me into being curious and asking him what's the matter myself."
    "Urgh...he can be so annoyingly passive some times."
    "Like he wouldn't even piss himself if he was on fire!"
    "I do the best I can to ignore Jack's efforts."
    "But before too long I can feel myself almost going insane from what he's doing."
    "And I just have to call his buff before I lose my mind."
    show jack sad
    bree.say "Jack..."
    bree.say "For the love of god..."
    bree.say "What's the matter with you?"
    show jack surprised at startle
    show fx shock at stepback, center, zoomAt(1.5, (640, 990))
    "Jack instantly jumps backwards, flinching in surprise."
    show jack sad
    "And he gets that look on his face, that's so hard to be angry at."
    "The one that makes him look like a puppy that you just accidentally kicked."
    jack.say "Aargh..."
    jack.say "Why are you shouting at me, [hero.name]?"
    jack.say "I wasn't doing anything wrong, was I?"
    "And just like that he's managed to do it again."
    "Turn the whole thing around on me so that I feel like a complete and utter bitch."
    "So I let out a long, tired sigh of surrender, and prepare to go through the motions."
    bree.say "Urgh..."
    bree.say "Okay, Jack, okay..."
    bree.say "I can tell that you have something on your mind."
    bree.say "And I can also tell that you're not going to come out and tell me what it is yourself."
    bree.say "So I'm going to save you the trouble of sitting there, worrying yourself to death."
    bree.say "What is it, Jack?"
    bree.say "What's up?"
    show jack smile
    bree.say "Think you're too geeky to be one of those new-fangled 'alpha geeks'?"
    bree.say "Worried your character's going to get nerfed in the new edition of Demons and Demi-Gods?"
    bree.say "Think you might be just a little too tubby for the character you want to cosplay as next?"
    show jack at backforth(1.0, 5, 0)
    "I add a gentle poke in the belly as I say the last one."
    show jack sad
    "But then I instantly regret it as Jack gives me the puppy-dog eyes again."
    jack.say "Hey..."
    show fx drop
    show jack angry
    jack.say "That's fat-shaming..."
    jack.say "And that is totally not cool!"
    show jack sad
    bree.say "Quit the guilt-tripping, Jack..."
    bree.say "Just tell me what's on your mind."
    bree.say "Or else I'll slap you until it falls out of your ears!"
    show jack guilty
    "I can see that Jack's more than a little afraid I'll actually do it."
    "And that seems to be what finally makes him do as he's told."
    show jack embarrassed at backforth(0.5, -5, 0)
    jack.say "Okay, okay..."
    jack.say "It's [mike.name], [hero.name]..."
    jack.say "I'm worried about him muscling in on our relationship!"
    "For a moment I can't quite believe what I'm hearing."
    "I shake my head at Jack."
    bree.say "You're afraid that [mike.name]'s going to steal me away from you?"
    bree.say "Jack, the guys sweet, but he's a total nerd!"
    show jack angry
    jack.say "But don't you see, [hero.name]?"
    jack.say "So am I, but he's like more of an alpha-nerd than me!"
    jack.say "[mike.name] does things like going to rock gigs and getting tattoos!"
    show jack sad
    "I'm still staring at Jack in sheer amazement."
    "He's talking about [mike.name] like he's some kind of Giga-Chad!"
    "When in reality the only thing the guy's got over him is a better gym-routine."
    "But I can see that I'm going to have to nip this one in the bud."
    "Because if I don't, Jack's going to get obsessed."
    menu:
        "Confess that I'm seeing [mike.name] behind this back" if game.days_played - mike.sexperience.last <= 7:
            $ jack.flags.know_seeing_mike = True
            "I take a deep breath, preparing myself for what lies ahead."
            "Something that I hoped I'd never have to do."
            bree.say "Okay, Jack..."
            bree.say "I'm going to tell you something now."
            bree.say "But you have to promise me that you won't freak out when I do."
            show jack normal
            "Jack nods with a confidence I can't help thinking is misplaced."
            show jack smile
            jack.say "Sure thing, [hero.name]..."
            jack.say "Hit me with it."
            jack.say "I can take the hard truth."
            show jack normal
            bree.say "I was lying to you just now, about [mike.name]..."
            bree.say "We've been seeing each other for a while now."
            bree.say "And yes, I do mean seeing each other in the way that involves sex."
            show jack sad at backforth(1.0, 0, 20)
            "Rather than taking it all in his stride, Jack crumbles instantly."
            "Which really doesn't take me by surprise."
            "Because I was expecting it anyway."
            show jack surprised
            jack.say "Oh no!"
            jack.say "Oh god no!"
            jack.say "[hero.name], how could you do this to me?!?"
            jack.say "I love you more than my own life!"
            jack.say "But now you're going to leave me for another man!"
            show jack sad
            "I shake my head as I hear the last part."
            bree.say "Erm..."
            bree.say "I'm not going to leave you, Jack!"
            show jack surprised
            jack.say "Huh..."
            jack.say "Wha..."
            jack.say "What do you mean, [hero.name]?"
            show jack at backforth(0.3, 5, 0)
            jack.say "If you're seeing another guy behind my back, you must want him more than me!"
            show jack sad
            "All I can do is shrug and shake my head."
            bree.say "Well, I wasn't planning on leaving you, Jack."
            bree.say "Admittedly, I also wasn't planning on telling you about [mike.name] and me."
            bree.say "And this is going to sound really selfish of me..."
            bree.say "But I was kind of hoping that I could keep on seeing you both at once."

            if jack.sub < 40:
                show jack angry
                show fx anger
                jack.say "What is this, [hero.name]?"
                jack.say "Some kind of sick game you like to play?!?"
                show jack angry at startle
                show fx exclamation at startle
                jack.say "Well I won't be a part of it!"
                show jack sad
                "I'm trying to make sense of what Jack's saying."
                "As well as the implications for me in particular."
                "And then the reality dawns on me."
                bree.say "Wait a minute..."
                bree.say "Are you..."
                bree.say "Are you actually dumping ME?!?"
                "Jack seems as surprised as me by that explanation."
                "But he does the best he can to make it look like he knew it all along."
                show jack angry at backforth(1.0, 0, 20)
                jack.say "I guess so, [hero.name]..."
                jack.say "So consider your ass well and truly dumped!"
                hide jack with easeoutleft
                "With that, he turns on his heel and walks away."
                "And I'm not sure which is confusing me more."
                "The fact that Jack actually managed to dump me."
                "Or that he temporarily grew a spine while he did so."
                "But I comfort myself with the fact that I still have [mike.name]."
                "So I'm not going to be short of fawning attention from desperate nerds anytime soon."
                $ jack.set_gone_forever()
            else:
                show fx drop
                jack.say "Erm..."
                jack.say "Are you allowed to do that, [hero.name]?"
                jack.say "I mean, it sounds a bit dishonest!"
                show jack sad
                "I roll my eyes in amazement at Jack."
                "Because I can't believe even he could be so naïve."
                bree.say "Don't be silly, Jack."
                bree.say "There isn't a 'Relationship Police' out there!"
                bree.say "You can do whatever you want, fuck whoever you want too!"
                show jack perv
                show fx question
                jack.say "We can?"
                show jack sad
                bree.say "Of course we can, Jack!"
                bree.say "And I promise you, just because I'm fucking [mike.name]..."
                bree.say "I won't stop fucking you too."
                "That actually seems to do the trick."
                show jack normal
                "Because I see a smile spreading across Jack's face."
                "And his entire mood picks up too."
                show jack smile
                jack.say "I..."
                jack.say "I think I'm okay with that!"
                show jack normal
                bree.say "Great news, Jack."
                bree.say "So we can all go back to normal, right?"
                show jack smile
                jack.say "I guess so, [hero.name]."
                jack.say "But you'd better watch out being so liberal and into free-love."
                jack.say "Because I might go and get myself another girl too!"
                show jack normal
                bree.say "Yeah..."
                bree.say "I won't hold my breath, Jack!"
                show jack surprised
                jack.say "Huh?"
                jack.say "What did you say?"
                show jack normal
                bree.say "Oh..."
                bree.say "I said 'maybe', Jack, 'maybe'..."
        "Reassure him, he's the only guy I'm seeing":
            bree.say "Jack..."
            bree.say "I am not seeing [mike.name] behind your back."
            bree.say "And I'm not interested in him like that either."
            bree.say "As far as I'm concerned, we're just friends."
            "Jack listens intently to all that I have to say."
            "Nodding at what he thinks are important points along the way."
            show jack normal
            "And when I'm done, he does seem a little calmer than before."
            show jack smile
            show fx sigh at center, zoomAt(1.5, (640, 940))
            jack.say "Okay, [hero.name]..."
            jack.say "I believe you, of course I do."
            jack.say "It's just being around a hot, blonde goddess like you..."
            jack.say "I think it kind of makes me a little crazy!"
            show jack normal
            "I can't help curling my lip and chuckling at this."
            bree.say "You don't say, Jack?"
            bree.say "But you hide it so well..."
    return

label jack_female_event_08:
    if jack.love.max < 180:
        $ jack.love.max = 180
    scene expression f"bg {game.room}" with fade
    jack.say "Erm..."
    jack.say "[hero.name]..."
    show jack casual at center, zoomAt(1.5, (640, 1080)) with dissolve
    "At the sound of Jack's voice, I glance up to see him looking straight at me."
    "And instantly I know that he's got something he wants to tell me, I'm sure of it."
    "I can usually read Jack like a book, because he's utterly hopeless at hiding his emotions."
    "And the same goes for his motivations too."
    bree.say "What is it, Jack?"
    bree.say "Is there something that you wanted to tell me?"
    show jack surprised
    "Jack's expression becomes one of sheer amazement as soon as I ask the question."
    "Because as easy as he is to read, he's also totally unaware of the fact."
    jack.say "Whoa..."
    jack.say "That's so weird, [hero.name]!"
    jack.say "You're right, there is something that I wanted to tell you."
    "Jack shakes his head."
    show jack smile
    jack.say "You know, sometimes I think you might be psychic, [hero.name]."
    jack.say "You should take a test or something to see if you really are!"
    show jack normal
    "There are definitely advantages to having Jack think I'm psychic."
    "But I put on a smile and try to steer him back to the matter at hand."
    "Because Jack can so easily get carried away with something like that."
    "And if he does, then he'll totally forget what he wanted to tell me."
    bree.say "That's a great idea, Jack..."
    bree.say "But what was it that tell me?"
    bree.say "It sounded as though it might be important."
    "Jack nods, suddenly remembering what was so important to him a few seconds ago."
    "And not for the first time, he reminds me of a dog, chasing its own tail."
    "Sweet and adorable, but maybe not too focussed in the brain stakes."
    show jack smile
    jack.say "Oh yeah, [hero.name]..."
    jack.say "It was about the other day, when we talked about [mike.name]."
    show jack embarrassed
    jack.say "You remember?"
    bree.say "Of course I do, Jack."
    if jack.flags.know_seeing_mike:
        bree.say "I told you I was seeing the both of you."
        bree.say "And you told me that you were okay with it."
        show jack blush
        "Jack instantly begins to turn red as he's reminded of what happened."
        jack.say "Erm..."
        show jack annoyed
        show fx drop
        jack.say "Yeah, [hero.name]..."
    else:
        bree.say "You had the silly idea I was seeing [mike.name] too!"
        show jack blush
        "Jack instantly begins to turn red as he's reminded of what happened."
        jack.say "Erm..."
        show jack annoyed
        show fx drop
        jack.say "Yeah, [hero.name]..."
        jack.say "I remember that part, even though I wish I could forget about it!"
    jack.say "It's not that part that I wanted to talk about!"
    "I'm doing the best I can to indulge Jack."
    "But it still kind of feels like I'm the one doing all the work here."
    bree.say "So what exactly do you want to talk about, Jack?"
    bree.say "You haven't even told me that yet!"
    "Even as I'm saying this, I can see Jack squirming on the spot."
    "Which means that whatever it is, he's having trouble getting it out."
    show jack normal
    jack.say "It's..."
    jack.say "It's kind of more about why I was asking in the first place, [hero.name]..."
    jack.say "The reason why I can get so paranoid when it comes to relationships with girls."
    "Now I have to admit, this is not something I was expecting to hear."
    "It sounds like Jacks really trying to bare his soul to me on the subject."
    "So I should probably do all I can to encourage him."
    "Though I do kind of feel like producing a doll."
    "Then asking him to point out where the mean girls hurt him!"
    bree.say "That's pretty brave of you, Jack."
    bree.say "I know that guys find it hard to talk about stuff like that."
    "Jack nods at this."
    show jack happy
    jack.say "That's right, [hero.name]..."
    show jack smile
    jack.say "Oh, and thanks for putting me in same box as guys in general."
    jack.say "When you're a nerd, that doesn't happen very often!"
    show jack normal at backforth(0.2, 0, 6)
    show fx cough zorder 2 at center, zoomAt(1.0, (640, 650))
    pause 0.2
    show jack at backforth(0.2, 0, 4)
    show fx cough as fx2 zorder 2 at center, zoomAt(1.0, (650, 700))
    "Jack makes an attempt to clear his throat."
    "And I get the impression he sees this as a very serious matter."
    "So I do the best I can to seem interested in what he has to say."
    "While also trying not to overdo it and make him think I'm taking the piss."
    show jack smile
    jack.say "Okay, [hero.name]..."
    show jack guilty
    jack.say "You see it all happened back when I started college."
    jack.say "There was this girl, and she was called Reona..."
    "I'm doing the best I can to keep an open mind."
    "But the moment Jack mentions a girl, I begin to have my suspicions."
    "And I'm already pretty use I know where this is going."
    show jack smile
    jack.say "We were both starting out there, with no friends."
    jack.say "So we kind of banded together, became friends out of necessity."
    jack.say "And the weird thing was, that at first, we really clicked."
    jack.say "Reona and I were getting on like a house on fire."
    show jack embarrassed
    "I'm still nodding along with all that Jack's saying."
    "But then he pauses, like he's remembering something unpleasant."
    bree.say "Let me guess, Jack..."
    bree.say "Something changed after that?"
    "Again Jack nods, looking astounded at my insight."
    show jack angry
    jack.say "Right again, [hero.name]!"
    jack.say "Once we were well into our first semester, Reona seemed to change."
    jack.say "She started hanging out with more manly guys all the time."
    show jack embarrassed
    jack.say "And she hardly ever spoke to me, even when I was standing right in front of her!"
    jack.say "What's worse, I'm sure she was sleeping with all those guys too!"
    jack.say "Lots and lots of them!"
    "I take a deep breath, preparing to make an interjection."
    "Sure, it's a risky thing to do at a point like this."
    "But I'm more than confident I know where Jack's going with this."
    bree.say "Jack..."
    bree.say "I'm going to ask you a question now."
    bree.say "You don't have to answer it, not if you don't want to."
    bree.say "But I think it'd help me to understand all of this better if you did."
    "Jack blinks, a little surprised by my statement."
    "But he nods all the same."
    show jack smile
    jack.say "Okay, [hero.name]..."
    jack.say "You can ask me."
    show jack normal
    "I nod and then ask the question."
    bree.say "This Reona..."
    bree.say "You were in love with her, weren't you, Jack?"
    show jack surprised
    "Jack reacts like he's been slapped hard on the cheek."
    "He shakes his head, gobsmacked at my apparent insight."
    jack.say "Oh my god!"
    jack.say "I was totally in love with her, [hero.name]!"
    jack.say "She was so amazingly beautiful, and so sexy too..."
    "Suddenly, Jack seems to realise what he's saying and who he's saying it to."
    show jack embarrassed
    jack.say "B...b...but not as beautiful as you, [hero.name], obviously!"
    if hero.morality >= 25:
        "I can't help getting upset the moment that Jack admits he used to love this Reona girl."
        "Part of me knows that it's silly of me to be reacting like this, but I just can't help it."
        bree.say "Oh, Jack..."
        bree.say "How could you even look at a slutty girl like that?!?"
        bree.say "And to think, I was sure that you were a nice boy!"
        "Jack's already waving his hands in the air."
        "Doing all that he can to distance himself from his own past."
        show jack angry
        jack.say "No, no, no..."
        jack.say "That's not what I was trying to say, [hero.name]!"
        jack.say "I feel for a girl like that once, just once."
        jack.say "And she totally tore my heart out of my chest!"
        jack.say "I could never even look at a girl like Reona again, I swear!"
        show jack sad
        "I feel a small amount of reassurance in what Jack's saying."
        "Mainly because of the way he's almost prostrating himself as he says it!"
        "But I still feel like he's shown a side of himself that I can't believe ever existed."
        bree.say "Alright, Jack..."
        bree.say "I'll believe what you're telling me."
        bree.say "But from now on, I want you to keep away from sluts like this Reona girl."
        bree.say "I don't even want to see you looking in the direction of one, okay?"
        show jack guilty
        "Jack swallows audibly, but he nods all the same."
        "I don't think this was how he saw things playing out."
        "But I feel like I managed to get my message across all the same."
        $ jack.love += 2
        $ jack.sub += 1
    elif hero.morality <= -25:
        "Part of me knows that I should be showing Jack some serious sympathy right now."
        "But the more he tells me about this Reona girl, the more he piques my interest."
        "And for all of the reasons he wouldn't want it to as well."
        bree.say "Aww..."
        bree.say "You flatterer, Jack!"
        bree.say "But I'm sure what you're describing was just a big misunderstanding."
        show jack surprised
        "Jack stares at me, his eyes wide with amazement."
        "Then he blinks, as if breaking the spell my reaction's cast over him."
        show jack angry
        jack.say "[hero.name]..."
        jack.say "I don't think you heard what I said just now..."
        jack.say "Reona totally broke my heart."
        jack.say "And she didn't give a damn about it either!"
        show jack sad
        "I wave a hand in the air, trying to calm Jack down."
        bree.say "Okay, Jack, okay..."
        bree.say "I believe she hurt you."
        bree.say "But there's always two sided to a story, right?"
        bree.say "I mean, is this Reona girl still going to college?"
        bree.say "Could we find her and ask her what she thinks happened between you?"
        "Jack's shaking his head by now, amazed at what he's hearing."
        show jack embarrassed
        jack.say "I...I can't face Reona again, [hero.name]..."
        jack.say "It'd totally break me!"
        "I roll my eyes at Jack's reaction."
        "Not buying the drama that he's putting into it at all."
        bree.say "Alright, Jack..."
        bree.say "Forget the idea of actually talking to the girl."
        bree.say "Maybe we could go to the campus, and then you could point her out to me?"
        bree.say "That way I can warn you if she ever shows up out of the blue, yeah?"
        show jack surprised
        "Jack looks pretty confused by all of this."
        "But as it doesn't involve him coming into contact with Reona, he nods his head."
        jack.say "Erm..."
        show jack smile
        jack.say "Okay, [hero.name]..."
        jack.say "I guess that kind of makes sense."
        show jack embarrassed
        "I nod as I'm forced to settle for nothing more than a vague promise."
        "Which leaves me feeling totally frustrated and unfulfilled."
        "Because I so desperately want to check out this Reona for myself."
        "As she sounds very interesting, even if she's only half the slut Jack claims she is!"
        $ jack.sub += 2
    else:
        "The way that I've been able to predict all of Jack's confessions really helps me get what he's saying."
        "Plus there's the fact that I can totally relate to all of the stuff he's telling me too."
        "Sure, I might be seeing it from a female perspective, but I've gone through similar things myself."
        bree.say "Oh, Jack..."
        bree.say "Don't be so silly!"
        bree.say "There's no need to apologise for other girls being pretty or sexy."
        bree.say "Just keep telling me that I'm both of those things too!"
        show jack embarrassed
        "Jack looks more than a little embarrassed."
        "And that's totally natural, as he's baring his soul right now."
        show jack smile
        jack.say "I..."
        jack.say "I just felt so dumb, [hero.name] - for thinking a girl like Reona might like me!"
        show jack embarrassed
        bree.say "Trust me, Jack - she's the dumb one!"
        bree.say "If this Reona girl couldn't see how great you are..."
        bree.say "Well, then screw her!"
        show jack surprised
        "Jack seems amazed at my dismissing Reona like that."
        "And I can see that there's more to this than just a former crush of his."
        show jack smile
        jack.say "That's why I'm so paranoid about you, [hero.name]!"
        jack.say "You're every bit as pretty as Reona was."
        jack.say "Plus you're way funnier and smarter too..."
        jack.say "So I'm terrified that you're just too good for me!"
        show jack normal
        "I cup Jack's cheeks in my hands, gently making him meet my eye."
        bree.say "Jack, you're smart, sweet and funny."
        bree.say "Plus, and you might not believe it, you're a hot nerd too!"
        bree.say "And I'm not dating you out of desperation or pity."
        bree.say "I'm doing it because I really like you!"
        hide jack
        show jack kiss
        $ jack.flags.kiss += 1
        "I end my little speech by planting my lips against Jack's."
        "And I kiss him in a way that I hope expresses my feelings for him too."
        hide jack kiss
        show jack casual embarrassed blush at center, zoomAt(1.5, (640, 1080))
        "Afterwards he's blushing again, but he seems to be mollified."
        show jack smile
        jack.say "Wow, [hero.name]..."
        jack.say "Nobody ever called me hot before!"
        show jack embarrassed
        show fx heart zorder 2
        bree.say "You're nerd-hot, Jack..."
        bree.say "And it takes a fellow nerd to see that!"
        $ jack.love += 4
    return

label jack_female_event_09:
    if jack.love.max < 200:
        $ jack.love.max = 200
    scene bg door restaurant with fade
    "Jack's been bugging me about taking me to eat at a restaurant for our next date."
    "And when I say bugging me, I mean going on about it pretty much non-stop until I agreed to it."
    "Which is when the first of my alarm bells kind of starts to ring, you know?"
    "Because Jack's not exactly the kind of guy that usually wants to eat in a fancy restaurant."
    "He's definitely more of the kind that wants to grab a burger on the way to see a movie."
    "Or order a pizza so that he can spend the night playing wargames with his fellow nerds!"
    "So it'd be fair to say that I'm on a slightly higher level of alert when we meet up tonight."
    show jack date at center, zoomAt(1.5, (640, 1080)) with dissolve
    "And as soon as I lay eyes on Jack, I feel like my reaction's justified."
    "Because he's made a real effort in the wardrobe department as well."
    "I mean, he's not in a tuxedo or anything."
    "But he's obviously put a lot of thought into his outfit."
    bree.say "Hi, Jack..."
    if hero.morality >= 25:
        bree.say "Don't you look extra nice tonight!"
    elif hero.morality <= -25:
        bree.say "Mmm..."
        bree.say "My man looks hot tonight!"
    else:
        bree.say "Looking good, I see?"
    show jack blush embarrassed
    "The moment I give him the compliment, Jack flushes with colour."
    "And he stumbles to get his words out too."
    show jack smile
    jack.say "Oh..."
    jack.say "H...hi, [hero.name]..."
    jack.say "You look sexy too!"
    jack.say "Oh...not that I think I look sexy..."
    jack.say "You know what I mean?"
    show jack embarrassed
    "I can't help chuckling and shaking my head as Jack gets all flustered."
    "Because it's one of those little quirks that makes him so endearing."
    "So in an effort to help settle his nerves, I lean in and plant a kiss on his cheek."
    if hero.morality >= 25:
        "Then I make sure to leave it at that, not wanting to overwhelm him."
    elif hero.morality <= -25:
        hide jack
        show jack date kiss
        $ jack.flags.kiss += 1
        "Then I follow up with one on his lips, making sure to use plenty of tongue."
        "Because I want to start getting him horny nice and early."
    else:
        hide jack
        show jack date kiss
        $ jack.flags.kiss += 1
        "Then I follow it up with another on his lips, just for good measure."
    hide jack kiss
    show jack date embarrassed at center, zoomAt(1.5, (640, 1080))
    bree.say "I know what you mean, Jack."
    bree.say "And I'm looking forward to our meal."
    bree.say "I don't think we've ever been to a place like this together!"
    hide jack with easeoutleft
    pause 0.3
    scene bg restaurant with fade
    pause 0.3
    show jack date at center, zoomAt(1.5, (840, 1080)) with easeinright
    "Jack reaches out and takes hold of my hand, leading me inside the restaurant."
    "He's nodding eagerly, obviously pleased with my enthusiasm."
    show jack smile
    jack.say "Oh, you know how it is, [hero.name]..."
    jack.say "A guy can't live on potato chips and beer his whole life!"
    show jack normal
    bree.say "I don't know, Jack..."
    bree.say "You seemed to be making a pretty good effort!"
    show jack smile
    jack.say "Well not tonight."
    jack.say "Tonight, we dine in style!"
    show jack normal at backforth(0.5, 10, 0)
    "Jack makes a sweeping gesture as he says this."
    show ryan as man zorder 1 at center, zoomAt(1.5, (340, 1080)), blacker with easeinleft
    "Which doesn't seem to impress the waiter much."
    "Waiter" "Ahem..."
    show jack embarrassed
    "Waiter" "I assume that sir has a reservation?"
    "I watch in amusement as Jack almost shrinks into himself at the question."
    "Because the embarrassment he's feeling is almost like something I can feel on the air."
    show jack normal
    jack.say "Erm..."
    show jack smile
    jack.say "Yes..."
    jack.say "Sir does have one of those."
    show jack normal
    "In the blink of an eye, the waiter's whole demeanour changes."
    "Where before he was cold and critical, now he's warm and friendly."
    "Which I guess has a lot to do with him realising Jack's not wasting his precious time."
    "Waiter" "Ah, I see your name right here."
    "Waiter" "This way, sir..."
    scene restaurant_meal_bg_pose01 with fade
    "The waiter leads us straight over to what looks like a pretty nice table."
    show restaurant meal jack date nomeals jackhappy with dissolve
    show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeinright
    "And a moment later we're sat down with menus in our hands."
    jack.say "Oh wow..."
    show restaurant meal jack date nomeals jackbored -jackhappy
    jack.say "Most of this is in some kind of code or something!"
    if hero.morality >= 25:
        "I can't help giggling and shaking my head."
        bree.say "Oh, Jack..."
        bree.say "You are silly!"
        bree.say "That's French!"
    elif hero.morality <= -25:
        "I nod in agreement as I study the menu."
        bree.say "Yeah, what's up with that?"
        "Waiter" "Ahem..."
        "Waiter" "I think you will find that's actually French!"
    else:
        "I do the best I can to keep from laughing."
        bree.say "I think that's French, Jack!"
    show restaurant meal jack date nomeals -jackbored
    "Jack shakes off the confusion and finds something in English."
    jack.say "I'll just have the steak, right here."
    jack.say "And could you make it well-done?"
    "The waiter nods."
    "Waiter" "And for madam?"
    if hero.morality >= 25:
        bree.say "Oh..."
        bree.say "I'll just have what he's having!"
    elif hero.morality <= -25:
        bree.say "I want a plate of the oysters, yeah?"
        bree.say "I heard that they're an aphrodisiac!"
    else:
        bree.say "I like the look of the fish."
        bree.say "So I'll go with that, thank you."
    "The waiter nods as he writes down our orders."
    hide waiter with easeoutright
    "Then he walks away, leaving us alone at the table."
    "I watch him until he disappears, then turn back to face Jack."
    "And much to my surprise, he's pouring me a glass of wine!"
    bree.say "Where did that come from?"
    bree.say "Did you have that hidden up your sleeve?"
    show restaurant meal jack date nomeals jackhappy
    "Jack gives me a nervous smile."
    jack.say "Ah..."
    jack.say "Don't get on my back about it, [hero.name]."
    jack.say "I'm just trying to make things nice for you!"
    show restaurant meal jack date nomeals -jackhappy
    "Jack's handing me a glass of wine as he says this, which I'm happy to accept."
    "But I can see that he's also trying to deflect my questions as well."
    "Which only makes me all the more intrigued to keep on him for an answer."
    bree.say "So..."
    bree.say "Is this the beginning of a totally new Jack?"
    bree.say "A more sophisticated version of the guy I thought I knew?"
    "I can see that I've hit on something."
    "Because Jack's starting to blush again."
    jack.say "Of come on, [hero.name]..."
    jack.say "Does there have to be a reason?"
    jack.say "Can't I just be doing something nice?"
    bree.say "Oh, Jack!"
    bree.say "Your idea of something nice is binging an entire sci-fi series on download!"
    bree.say "So when you bring me to a fancy restaurant, I'm always going to be suspicious."
    show restaurant meal jack date nomeals jackblush
    "Finally the strain of keeping up the pretence seems to get to Jack."
    "And his shoulders sag as he surrenders to the inevitable."
    jack.say "Okay, [hero.name]..."
    jack.say "You got me!"
    jack.say "I brought you here so that I'd have a nice setting."
    jack.say "Somewhere to make a pretty important confession."
    "Jack looks around before he goes on."
    "Almost like he's afraid that someone will overhear what he has to say."
    "Which of course makes me all the more interested in just what it is."
    show restaurant meal jack date nomeals jackhappy -jackblush
    jack.say "This isn't an easy thing for me to say, [hero.name]..."
    jack.say "In fact I'm kind of terrified to admit it..."
    show restaurant meal jack date nomeals -jackhappy
    jack.say "But I feel like I have to get it out, or else I'll go mad!"
    jack.say "I...I love you, [hero.name]!"
    jack.say "And I don't mean like a friend, either - I'm totally, utterly and insanely in love with you!"
    "For a moment it's like I can't quite make sense of what Jack's saying."
    "I understand the words, but they don't seem to work as a coherent sentence."
    "But then it hits me like a slap in the face."
    bree.say "Jack..."
    bree.say "Are you serious?"
    bree.say "Because I...I think I love you too!"
    "It's only now that I realise Jack's got something in his hand."
    "That and the fact he's getting down on his knees in front of me."
    "Plus he has a ring in his hand!"
    jack.say "Erm..."
    jack.say "So with that in mind, [hero.name]..."
    jack.say "What do you think about making it official?"
    menu:
        "Accept Jack's proposal":

            "I don't even have to think about it."
            "I just nod my head and thrust out my hand."
            bree.say "Yeah, Jack..."
            show restaurant meal jack date nomeals -jackhappy
            bree.say "I'll marry you!"
            "Jack beams at my answer."
            "And he slides the ring straight onto my finger."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeinright
            show restaurant meal jack date -nomeals -jackhappy with dissolve
            hide waiter zorder 1 at flip with easeoutright
            "But then the waiter arrives with our food."
            "Which kind of spoils the moment a little."
            "Jack leaps back into his seat and we start to eat."
            "But we spend the rest of the night exchanging knowing glances."
            "Like we can't wait to be able to see what life is like now we're officially engaged!"
            $ jack.set_fiance()
        "Refuse Jack's proposal":
            "I don't even have to think about it."
            "I just nod my head and wave for him to put it away."
            bree.say "No way, Jack!"
            show restaurant meal jack date nomeals jackbored
            bree.say "We're not ready for that level of commitment."
            bree.say "Stop it before you embarrass me!"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeinright
            show restaurant meal jack date -nomeals jackbored with dissolve
            hide waiter zorder 1 at flip with easeoutright
            "Just then the waiter arrives with our food."
            "Which makes Jack look even more foolish."
            "He puts the ring away and scurries back into his chair."
            "Then we spend the rest of the meal in an awkward silence."
            "Neither of us able to look the other in the eye for the rest of the night."
            $ jack.love -= 25
    return

label jack_female_ending:
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I always wondered what my wedding day would be like when I was younger."
    "You know, like every girl does at once time or another?"
    "Wondering about the dress I'd be wearing or the place it'd happen."
    "Not to mention the guy that I'd be getting married to!"
    "But I have to say that I never imagined it would be like this."
    "I mean we're standing at the altar in a pretty typical wedding chapel."
    "And the place is all done out, looking really pretty."
    "Plus both sides of the chapel are full to bursting with family and friends."
    "So on paper at least, everything is going to plan."
    "It's just that I'm standing here on my own, without the groom!"
    "And yeah, I know that it's normal for the bride to be the one that walks down the aisle."
    "But Jack and I decided that we were going to break with that tradition and stand together."
    "The problem is that when I walked in here, there was no sign of him whatsoever!"
    "Now I'm standing here alone, clutching at my bouquet and wondering what happened."
    if hero.pregnant:
        "I can also feel the eyes of the guests on the curve of my belly."
        "And I wonder how many of them are dwelling on the fact I'm pregnant right now."
        "Thinking that it could be the reason that Jack's failed to show up today."
        "Even though I know that he's as thrilled as I am to be expecting a child."
    else:
        "It's at times like this that I'm really glad I didn't get pregnant."
        "Because I know exactly what people would be thinking if I were."
        "So at least that's one thing I can be sure of right now."
        "That no one thinks Jack knocked me up and then ran away from his responsibilities!"
    "I'm just beginning to get worried, glancing at the priest standing in front of me."
    "All he can do is offer a weak smile and a helpless shrug by way of a response."
    "But that's when the doors of the chapel swing open, slamming against the walls."
    "As one, everybody in the room turns to look over their shoulder."
    "And there he is, standing in the doorway."
    show jack wedding sad at center, zoomAt (1.0, (640, 740)) with dissolve
    "Even from this distance I can see that Jack's panting like he's having a heart attack."
    "He looks more than a little bit dishevelled too, staggering down the aisle like a zombie."
    show jack wedding sad at center, traveling (1.5, 5.0, (640, 1080))
    "As he gets closer, he raises a hand in the air."
    show jack whining
    jack.say "Sorry..."
    jack.say "So sorry, folks..."
    show jack worried
    jack.say "The car broke down, so I had to get a taxi."
    jack.say "Then the taxi broke down, so I had to thumb a lift."
    jack.say "A farmer in a tractor came to my rescue..."
    show jack lying
    jack.say "And he just dropped me off outside!"
    show jack sadsmile
    "By now Jack's staggered all the way to the altar."
    "And I rush to his side, worried sick about the state he's in."
    bree.say "Oh, my poor Jack!"
    bree.say "Are you okay?"
    "I fuss about him, doing the best I can to straighten up his clothes."
    "And then I grab his hands, squeezing them out of sheer concern for him."
    show jack lying
    jack.say "I...I guess so, [hero.name]..."
    show jack whining
    jack.say "I'm so sorry I'm late."
    show jack sadsmile
    "I shake my head, just relieved that he's okay."
    bree.say "That's not important, Jack."
    bree.say "You made it here..."
    bree.say "And that's all that matters!"
    "The priest has been listening to all of this with interest."
    "And when we both look his way, he raises his hands to us."
    "Priest" "Are you sure that you're want to proceed right now?"
    "Priest" "We could let this poor fellow rest a little, if he needs to?"
    show jack normal
    "Jack straightens himself up at this, shaking his head."
    show jack smile
    jack.say "No way..."
    jack.say "I'm marrying this girl, no matter what!"
    show wedding jack with fade
    "I feel myself swelling up with emotion as Jack says this."
    "And I cling onto his arm like a limpet, not wanting to let go."
    show wedding jack priest with dissolve
    "Priest" "Very well..."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony."
    "Now that the ceremony is officially underway, things seem to be getting back to normal."
    "I can hear murmurs of relief amongst the guests, and my own panic has subsided."
    "And nothing really noteworthy happens until we make it to the exchanging of vows."
    "Priest" "Do you, Jack..."
    "Priest" "Take [hero.name], to be your lawful, wedded wife?"
    jack.say "You bet I do!"
    "Priest" "Very good."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take Jack, to be your lawful, wedded husband?"
    bree.say "I do."
    "The priest nods."
    "Priest" "I call on those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these two may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "Jack bursting in on the chapel earlier seems to have soaked up all the drama in the air."
    "So I don't even hear the customary ripple of laughter as the question is asked."
    "Priest" "Very well..."
    "Priest" "By the power vested in me..."
    "Priest" "I hereby declare you husband and wife."
    "Priest" "You may kiss your spouse."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show jack kiss wedding
    with fade
    $ jack.flags.kiss += 1
    "Jack and I do as he says, enjoying a long and rather passionate kiss."
    "I'm intrigued to hear all about his adventures in getting here today."
    "But I temper that with the knowledge that this is the start of our new life together."
    "And there's going to be plenty of time for him to fill me in on the details later."
    "Right now, all I want to do is focus on the fact that we actually pulled it off."
    hide jack kiss
    show jack wedding happy at center, zoomAt(1.5, (640, 1080))
    "We're married, and I keep pinching myself as a reminder that it's all for real."

    scene jack ending
    with fade
    jack.say "Sure I'll tell you about my life with [hero.name]."
    jack.say "Why wouldn't I want to talk all about the fact I'm married to the hottest girl in the world?!?"
    jack.say "I tell everyone that I meet how great my wife is and how she's the coolest woman on the planet!"
    jack.say "Huh?"
    jack.say "You want me to go into actual details?"
    jack.say "Oh...okay, I can do that too!"
    jack.say "I guess I was always one of those guys that thought he never had any luck with girls."
    jack.say "You might not have noticed, but I'm not the most athletic of guys."
    jack.say "In fact, some people have actually accused me of being a little bit of a nerd."
    jack.say "If you can believe that?!?"
    jack.say "But yeah, I was kind of stuck in a cycle of seeing a girl and falling in love with her."
    jack.say "Then I'd go through a roller-coaster of emotions with her, up and down the whole time."
    jack.say "What?"
    jack.say "I had some rough relationships?"
    jack.say "Oh no, I was never really in a relationship with those girls I mentioned just now!"
    jack.say "That was just in the time from me seeing them to thinking about maybe considering asking them out."
    jack.say "By the time I managed to pluck up the courage, they'd always be seeing other guys."
    jack.say "I guess that's how [hero.name] managed to become a part of my life in a different way."
    jack.say "Because she was introduced to me more as a friend than a potential conquest."
    jack.say "She just showed up one day, [mike.name] telling me she was his housemate and she was cool."
    jack.say "In a lot of ways, she was more like a guy to me than a girl!"
    jack.say "I mean, she was into so much cool stuff, you know?"
    jack.say "She played videogames until her hands went numb."
    jack.say "She was always wanting to get into Demons and Demigods."
    jack.say "Hell, she even thought cosplay was really cool!"
    jack.say "None of that was stuff the girls I knew were into - they always hated it."
    jack.say "Soon enough, [hero.name] was hanging out with [mike.name] and me all the time."
    jack.say "Of course I was sure that it was [mike.name] she'd be into."
    jack.say "He's far more of an alpha nerd than me..."
    jack.say "But then I kept finding that [hero.name] was always talking to me."
    jack.say "Like, she'd ask me questions and laugh at my jokes."
    jack.say "At first I thought she was just humouring me."
    jack.say "But then she actually started to ask if she could do stuff with just me!"
    jack.say "I kept on telling myself that we were just friends."
    jack.say "But luckily for me, [hero.name] wasn't thinking the same way."
    jack.say "And when she kissed me that first time..."
    jack.say "Oh man, I can still remember just how it felt!"
    jack.say "I was totally blown away - I had an actual girlfriend!"
    jack.say "And she looked like that!"
    jack.say "Sure, we had some bumps along the way."
    jack.say "I was still totally clueless around women."
    jack.say "And I don't think [hero.name] was ready for the full intensity of geek culture."
    jack.say "But we met those problems and we dealt with them, getting stronger as a result."
    if hero.pregnant:
        jack.say "Even when we found out that [hero.name] was pregnant, we made it work."
        jack.say "Daenaris came along nine months later, officially making us a family."
        jack.say "And I wouldn't change any of it if I had a wish spell memorised."
        jack.say "Because she's my little princess, and her mommy's my queen!"
    else:
        jack.say "In fact, I think the only challenge that we still have left is starting a family."
        jack.say "We've both kind of skirted around the subject a little."
        jack.say "But I think the time's fast approaching when we'll want to take the leap."
        jack.say "And I have the perfect name in mind, one that I know [hero.name] will love!"
    jack.say "We're living our passions on a daily basis right now."
    jack.say "Because [hero.name] and I pooled our resources and opened a games store together!"
    jack.say "We have comics, minis, wargames and all the books you could ever want."
    jack.say "So every day we get up and go there, immersing ourselves in glorious geekdom from dawn to dusk!"
    jack.say "I just can't believe I have people coming up to me and telling me how cool my life is."
    jack.say "I really feel like I have it all these days."
    jack.say "And the future just seems to keep getting brighter too."
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label jack_female_event_02_bis:
    $ game.room = "bookstore"
    scene bg bookstore
    "I love the feeling of being in the biggest bookstore in town."
    "Don't get me wrong, I love those little bookstores too - they're great."
    "But there's just something amazing about being around so many new books!"
    "And this place has shelf after shelf of books."
    "All pristine and begging for somebody to read them!"
    "Sometimes I come in here even when I'm not looking for something in particular."
    "And I'll just spend my time browsing the shelves, looking at whatever catches my eye."
    "I'm in a world of my own, able to forget about boring reality."
    "Which is why I don't notice somebody creeping up on me."
    show jack close
    jack.say "Hey, [hero.name]!"
    jack.say "What are you doing here?"
    bree.say "Aargh!"
    show jack -close
    show fx exclamation
    jack.say "Aargh!"
    "I leap backwards in one direction."
    "And Jack leaps backwards the opposite way."
    hide fx
    bree.say "Jack..."
    bree.say "What the hell..."
    bree.say "Don't sneak up on me like that!"
    "Jack looks instantly crest-fallen and sheepish."
    "Which makes me regret snapping at him like that."
    show fx drop
    jack.say "Sorry, [hero.name]..."
    jack.say "I didn't think!"
    hide fx
    bree.say "It's okay, Jack."
    bree.say "You just startled me, that's all."
    bree.say "I kind of come here to zone out, you know?"
    bree.say "To lose myself in all of the books?"
    "Jack nods eagerly, and not just because I'm changing the subject."
    "I can see that he's getting that look in his eyes."
    "The one that's from sheer, child-like enthusiasm."
    show jack happy
    jack.say "I know exactly what you mean, [hero.name]!"
    jack.say "This place is so great!"
    show jack normal
    jack.say "The only thing that sucks is there are too many books."
    show jack happy
    jack.say "So many that I could never read all of them!"
    "It's only now that I notice Jack has a book in his hand."
    "It's a large, shiny hard-back with a colourful cover."
    "It's not the right shape to be a novel."
    "And the style of the illustration doesn't make me think of a graphic novel either."
    "Intrigued by the mystery of what Jack's buying, I point to the book."
    bree.say "What's that, Jack?"
    bree.say "I don't think I've seen it before."
    show jack normal
    "Jack holds up the book with a real measure of pride."
    jack.say "How can you be a nerd and not know what this is, [hero.name]?"
    show jack happy
    jack.say "It's the long-awaited, much-anticipated new edition of 'Demons and Demigods'!"
    "Now I can see that the cover of the book is covered with dragons and glittering treasure."
    "Well, that along with men and women wearing next to nothing, while swinging massive weapons!"
    bree.say "Demons and Demigods?"
    bree.say "That sounds exciting!"
    bree.say "Is it a manga?"
    bree.say "Or a graphic novel?"
    show jack normal
    "Jack shakes his head, looking a little disappointed in my questions."
    jack.say "No, [hero.name]!"
    jack.say "It's an RPG!"
    jack.say "You know - a roleplaying game?"
    if hero.morality <= -25:
        if jack.love.max < 40:
            $ jack.love.max = 40
        bree.say "Roleplaying?"
        bree.say "I like the sound of that, Jack!"
        bree.say "The kind of roleplaying you do in the bedroom!"
        show fx drop
        "Jack's eyes go wide at the mere mention of such a thing."
        "And he leans in closer, as if he's afraid someone will overhear."
        jack.say "No, [hero.name]!"
        hide fx
        jack.say "You know the kind of roleplaying I mean!"
        jack.say "Rolling dice and slaying dragons!"
        "I take advantage of how close Jack's come."
        show jack close
        "And putting my hands on him, I pull him closer still"
        bree.say "Of course I know what it is, silly!"
        bree.say "But that's not the kind of game I want us to play!"
        show jack perv
        "Jack swallows audibly, at this."
        jack.say "It...it's not?"
        bree.say "No, Jack, it's not."
        bree.say "But I can be the princess you rescue."
        bree.say "Or the evil sorceress that you subdue."
        bree.say "I can even be the elf slave-girl that has to obey your every word!"
        jack.say "Wh...when can we play a game like that, [hero.name]?"
        bree.say "Soon, Jack, soon."
        $ jack.sub += 2
        bree.say "I'm going to make your fantasies into reality!"
    else:
        menu:
            "Be interested":
                if jack.love.max < 40:
                    $ jack.love.max = 40
                bree.say "Oh yeah..."
                bree.say "That's like a pen and paper roleplaying game, right?"
                bree.say "The kind where you roll dice and slay dragons?"
                show jack happy
                "Jack nods, his mood picking up at instantly."
                jack.say "Yeah, [hero.name]!"
                jack.say "That's it exactly."
                jack.say "This is like THE best roleplaying game ever!"
                show jack normal
                jack.say "You must have played it?"
                jack.say "I thought everyone had!"
                "I shake my head, looking more than a little disappointed."
                bree.say "No, Jack..."
                bree.say "I never got the chance to play it."
                bree.say "Some guys used to play it when I was in high-school."
                bree.say "And I really wanted to get involved back then."
                bree.say "But they were kind of a bunch of dicks."
                bree.say "They always told me to get lost, that it wasn't for girls!"
                "Jack looks seriously offended on my behalf."
                "In fact, he looks like my story made him mad!"
                jack.say "What a bunch of jerks!"
                jack.say "They were wrong, [hero.name] - one hundred percent wrong!"
                jack.say "Demons and Demigods is for everyone!"
                bree.say "You mean I could play with you?"
                bree.say "I...I mean if you'd let me, that is!"
                bree.say "You sound like you're a veteran player, Jack."
                bree.say "And I'd just be a newbie!"
                show jack happy
                "Jack waves away my concerns."
                "His eyes are filled with enthusiasm, like I just had the best idea ever."
                $ jack.love += 2
                jack.say "Of course you can play with me, [hero.name]!"
                jack.say "You can play with me anytime!"
                show jack normal
                jack.say "I...I mean we can play a game of Demons and Demigods!"
                jack.say "I can run things and you can roll up a player character."
                jack.say "I'm sure we can get [mike.name] to play - he loves Demons and Demigods."
                jack.say "Maybe even that other housemate of yours too?"
                "I clap my hands together with glee."
                bree.say "That sounds perfect, Jack."
                bree.say "I can't wait!"
            "Wrap up the subject":
                bree.say "Oh, right..."
                bree.say "You mean where you roll dice and slay dragons, yeah?"
                show jack happy
                "Jack nods, his mood picking up at instantly."
                jack.say "Yeah, [hero.name]!"
                jack.say "That's it exactly."
                jack.say "This is like THE best roleplaying game ever!"
                show jack normal
                jack.say "You must have played it?"
                jack.say "I thought everyone had!"
                "I frown a little, racking my brain to think."
                "If I had played it, I think I'd remember."
                bree.say "I don't know, Jack."
                bree.say "I might have played a videogame based on it once."
                bree.say "But I never played the real thing."
                "At this, Jack seems to see an opening."
                jack.say "Then we should organise a game!"
                jack.say "I can run things and you can roll up a player character."
                jack.say "I'm sure we can get [mike.name] to play - he loves Demons and Demigods."
                jack.say "Maybe even that other housemate of yours too?"
                "This is starting to get out of hand."
                "All I was trying to do was be nice to Jack."
                "Just showing some interest in his choice of literature."
                "Now I feel like I'm being signed up for some kind of amateur dramatics bullshit!"
                bree.say "Thanks for the offer, Jack."
                bree.say "But I like my RPGs to be on the Zbox."
                bree.say "That way I can turn them off and walk away whenever I like."
                jack.say "Aw, come on, [hero.name]!"
                jack.say "It'll be fun - I promise!"
                bree.say "No, Jack, I'm gonna pass."
                bree.say "You and [mike.name] will just have to play with each other instead..."
                $ jack.set_gone_forever()
    return

label jack_female_event_03_bis:
    if jack.love.max < 60:
        $ jack.love.max = 60
    scene bg livingroom
    "I've been waiting for the big day to come around for what feels like forever."
    "But now it's finally here - the day I get to play Demons and Demigods with Jack!"
    "Well, we'll be playing it with [mike.name] and Sasha too..."
    "But Jack did agree to organise the game after I asked him to at the bookstore."
    "So I still feel like he's kind of doing this for me."
    "And the others are just tagging along for the ride."
    "When I hear the sound of somebody at the door, I hurry into the hallway."
    scene bg house
    show jack
    show mike at left5
    with fade
    "There I find [mike.name] already opening the door to let Jack into the house."
    mike.say "Hey, Jack!"
    jack.say "Hey, [mike.name]!"
    "It looks like [mike.name]'s about to say something more to his friend."
    "But at that same moment, Jack spots me coming down the stairs."
    hide jack
    show jack close happy
    show mike angry at mostleft4
    with hpunch
    "Instantly his face lights up and he elbows his way past [mike.name]."
    jack.say "H...hello, [hero.name]!"
    jack.say "You're looking really great today!"
    show jack normal
    jack.say "Are you ready for your first game of Demons and Demigods?"
    mike.say "Whoa..."
    mike.say "What are you trying to do, Jack?"
    mike.say "Trample me to death?!?"
    if hero.morality <= -50:
        "I smile slowly as I sidle down the last few stairs and into the hallway."
        "I can almost feel Jack's eyes on me the whole time, almost hear his heart beating faster."
        bree.say "More than ready, Jack!"
        bree.say "I've been waiting for my Master to arrive since you agreed to do this for me!"
        bree.say "Oops...did I say Master?"
        bree.say "I meant Gamesmaster!"
        $ jack.sub += 2
        show jack perv
        "By now Jack's nodding and grinning at me."
        $ mike.love -= 2
        "But [mike.name]'s still rubbing his shoulder and looking annoyed."
        mike.say "Did somebody cast an invisibility spell on me or something?"
        mike.say "I'm standing right here, guys!"
        show jack normal -close
        show fx drop
        jack.say "Oh..."
        jack.say "Sorry, buddy!"
        jack.say "I'm just so stoked to be introducing somebody new to the game!"
        jack.say "I guess I just got carried away, you know?"
        hide fx
        show mike normal
        "[mike.name] makes a huffing sound and rolls his eyes."
        "But he seems to want to let the matter drop."
        mike.say "Sure, Jack, sure."
        mike.say "Let's just get on with it, okay?"
    elif hero.morality <= -25:
        "I give Jack a suitably enthusiastic grin as I reach the bottom of the stairs."
        bree.say "I sure am, Jack!"
        bree.say "I've been looking forward to it since you agreed to do this for me."
        bree.say "And I can't wait to see just what you're going to teach me!"
        show jack happy
        "By now Jack's nodding and grinning at me."
        $ mike.love -= 2
        "But [mike.name]'s still rubbing his shoulder and looking annoyed."
        mike.say "Did somebody cast an invisibility spell on me or something?"
        mike.say "I'm standing right here, guys!"
        show jack normal -close
        show fx drop
        jack.say "Oh..."
        jack.say "Sorry, buddy!"
        jack.say "I'm just so stoked to be introducing somebody new to the game!"
        jack.say "I guess I just got carried away, you know?"
        hide fx
        show mike normal
        "[mike.name] makes a huffing sound and rolls his eyes."
        "But he seems to want to let the matter drop."
        mike.say "Sure, Jack, sure."
        mike.say "Let's just get on with it, okay?"
    elif hero.morality >= 25:
        "I almost fail to hear Jack's question as I hurry over to [mike.name]."
        hide mike
        show jack -close at right4
        show mike
        bree.say "[mike.name]!"
        bree.say "Are you okay?"
        show mike down
        $ mike.love += 2
        mike.say "Erm..."
        mike.say "I don't know, [hero.name]..."
        show mike normal
        mike.say "I kind of feel like I might have been bruised pretty badly!"
        "Jack looks on as I tend to [mike.name]."
        "And I can almost see the guilt growing in his eyes."
        show fx drop at right4
        jack.say "Oh..."
        jack.say "Sorry, buddy!"
        jack.say "I guess I don't know my own strength!"
        hide fx
    else:
        "I shake my head as I reach the bottom of the stairs."
        bree.say "Jack!"
        hide mike
        show jack -close at right5
        show mike at left4
        bree.say "What's with you pushing [mike.name] aside like that?"
        bree.say "Aren't we all supposed to be playing this game together?"
        "Jack's cheeks flush a little as my words sink in."
        "He glances from me to [mike.name] and then back again."
        show fx drop at right5
        jack.say "Oh..."
        jack.say "Sorry, buddy!"
        jack.say "I'm just so stoked to be introducing somebody new to the game!"
        jack.say "I guess I just got carried away, you know?"
        hide fx
        "[mike.name] makes a huffing sound and rolls his eyes."
        "But he seems to want to let the matter drop."
        mike.say "Sure, Jack, sure."
        mike.say "Let's just get on with it, okay?"
    "It's only now that I see Jack's wearing a backpack stuffed to the brim with books."
    "I know that [mike.name] was setting up some of his own stuff on the dining room table just now."
    "I'm wondering just how much stuff we actually need to play a game of Demons and Demigods!"
    scene bg livingroom
    show mike at mostright4
    show jack
    with fade
    "As [mike.name] ushers him towards the table, Jack casts his gaze around the house."
    "At first I think he's just checking out the decor."
    "But then I remember that he's a straight guy, so that can't be it."
    jack.say "Hey..."
    jack.say "Where's Sasha?"
    jack.say "She's still playing with us, right?"
    "Before I know what's happening, I feel a tinge of jealousy in my gut."
    "Why is Jack so concerned about Sasha turning up on time?"
    "I was the one that asked him to set this whole thing up!"
    "Does it really matter if she's here or not?!?"
    "Whoa...settle down there, tiger!"
    "Where did all of that come from?"
    "Am I getting jealous of Jack even thinking about other girls?"
    "No, no...that can't be right."
    "It must be that I'm worried for him, that's all."
    "I know how much work he must have put into this, how passionate he is about it."
    "I just don't want to see all of his efforts go to waste and him get upset."
    show sasha annoyed at mostleft5 with moveinleft
    sasha.say "What's the big deal?"
    sasha.say "I'm here already!"
    show sasha normal
    sasha.say "We all ready for the big nerd orgy?"
    "Sasha doesn't really wait for an answer to her question."
    show sasha at mostleft5, zoomAt (1, (200, 850))
    "Instead she breezes over to the table and starts picking up random objects."
    "As she flicks through books and stares at papers, I see Jack and [mike.name] turning white."
    jack.say "[mike.name]..."
    jack.say "My barely adequate psychic defences are crumbling!"
    show mike angry
    mike.say "Sasha!"
    mike.say "Stop that, right now!"
    "Sasha wrinkles her face in confusion."
    "But she does as she's told all the same."
    show sasha surprised
    sasha.say "Huh?"
    sasha.say "What did I do now?"
    show sasha normal
    sasha.say "I was just looking at some of this cool artwork."
    sasha.say "I never knew Demons and Demigods was this dark!"
    if hero.morality <= -50:
        "The moment that I catch sight of what Sasha's looking at, I rush over to her side."
        "At first she looks like she's going to object, but then she sees the look on my face."
        "Sasha holds up the book so I can see the glossy, full-page illustrations."
        bree.say "Wow!"
        bree.say "Let me see that, Sasha!"
        bree.say "I want to see some rippling demon flesh too!"
        show sasha happy
        sasha.say "Yeah, [hero.name]!"
        sasha.say "I hope we come across this guy."
        show sasha flirt
        sasha.say "He can demonically possess my soul anytime!"
        show sasha surprised
        "And we both jump back in alarm as [mike.name] snaps it shut."
        show sasha angry
        sasha.say "Hey!"
        sasha.say "I was looking at that!"
        show mike angry
        mike.say "That's the Gamesmaster's Guide, Sasha!"
        mike.say "Only Jack gets to look at that!"
        mike.say "And the papers are his notes for the game."
        mike.say "If you read those you'll spoil it for everyone!"
        show sasha annoyed
        sasha.say "Okay, okay..."
        sasha.say "I didn't know, Jack!"
        sasha.say "Maybe keep the secret stuff secret in future, huh?"
        show jack at center, zoomAt (1, (640, 850))
        "Jack rushes over to rearrange his books and papers."
        $ jack.love -= 4
        "But as he does so, Sasha and I can't help laughing at him."
        "I just hope the actual game is this much fun!"
    elif hero.morality <= -25:
        "I know that I should come to Jack and [mike.name]'s defence."
        "But then I catch sight of the artwork Sasha's talking about."
        "And I can't help leaning in to get a look for myself."
        bree.say "Wow!"
        bree.say "Let me see that, Sasha!"
        bree.say "I want to see some rippling demon flesh too!"
        show sasha shocked
        "A moment later the book is snatched away."
        "And we both jump back in alarm as [mike.name] snaps it shut."
        show sasha vangry
        sasha.say "Hey!"
        sasha.say "I was looking at that!"
        show mike angry
        mike.say "That's the Gamesmaster's Guide, Sasha!"
        mike.say "Only Jack gets to look at that!"
        mike.say "And the papers are his notes for the game."
        mike.say "If you read those you'll spoil it for everyone!"
        show sasha annoyed
        sasha.say "Okay, okay..."
        sasha.say "I didn't know, Jack!"
        sasha.say "Maybe keep the secret stuff secret in future, huh?"
        show jack at center, zoomAt (1, (640, 850))
        "Jack rushes over to rearrange his books and papers."
        $ jack.love -= 2
        "But I note that he shoots me a pleading look as he does so."
    elif hero.morality >= 25:
        "I shake my head at Sasha and let out a sigh."
        "Obviously she doesn't know anything about this kind of thing."
        show mike normal
        bree.say "That's the Gamesmaster's Guide, Sasha."
        bree.say "Only Jack's supposed to be able to read that."
        bree.say "And those are obviously his notes for the game."
        bree.say "You shouldn't be reading those either!"
        show sasha annoyed
        "Sasha rolls her eyes and holds up her hands."
        hide sasha
        show sasha annoyed at mostleft5
        "She also makes a point of stepping back from the table."
        "But she does so in a deliberately dramatic fashion to make her point."
        sasha.say "Okay, okay..."
        sasha.say "I didn't know you were the queen of the nerds, [hero.name]!"
        show jack at center, zoomAt (1, (640, 850))
        "Jack rushes over to rearrange his books and papers."
        $ jack.love += 4
        "But I note that he shoots me a look of thanks as he does so."
    else:
        "I can't help giggling at what's going on right now."
        "Sure, it's pretty rude of Sasha to just flick through all of Jack's stuff."
        "But he and [mike.name] never bothered to tell her that it was off limits."
        "And the look of horror on their faces is hilarious."
        bree.say "That's all of Jack's Gamesmastering stuff, Sasha."
        bree.say "He's supposed to keep us from seeing it."
        bree.say "If we read it, then it's like spoilers for the game, right?"
        show sasha annoyed
        "Sasha rolls her eyes and holds up her hands."
        hide sasha
        show sasha annoyed at mostleft5
        "She also makes a point of stepping back from the table."
        "But she does so in a deliberately dramatic fashion to make her point."
        sasha.say "Okay, okay..."
        sasha.say "I didn't know, Jack!"
        sasha.say "Maybe keep the secret stuff secret in future, huh?"
        show jack at center, zoomAt (1, (640, 850))
        "Jack rushes over to rearrange his books and papers."
        $ jack.love += 2
        "But I note that he shoots me a look of thanks as he does so."
    hide jack
    show jack
    "After a few minutes of fussing with his books and papers, Jack seems satisfied."
    "He sits down at the head of the table and [mike.name] motions for us to take a seat too."
    show rpg
    bree.say "So, Jack..."
    bree.say "How does this all work?"
    sasha.say "Yeah, Jack..."
    sasha.say "Is it like improv theatre or something?"
    "Rather than answering us, Jack sets up a piece of folded card on the table."
    "It's folded so that it screens his papers off from us."
    "Plus it has a pretty sick picture of a dragon on the front too."
    "Jack regards us from behind it, one eyebrow raised in a curious manner."
    jack.say "'Jack'?!?"
    jack.say "Who is this 'Jack' of whom ye speaks?!?"
    "Sasha giggles at the dramatic voice Jack's putting on."
    "And I look at [mike.name], hoping he can explain what's gotten into Jack."
    mike.say "Ah..."
    mike.say "Jack likes to be called 'Gamesmaster' when he's running the game."
    mike.say "So it's best to just go along with it, okay?"
    "I nod slowly and force a smile onto my face."
    "This isn't too crazy for me."
    "I'm sure I can handle it."
    bree.say "What happens now...Gamesmaster?"
    jack.say "Now I bestow upon you the characters that you'll be playing."
    jack.say "[mike.name]..."
    jack.say "Thou shalt be 'Sir Percival the Pure'!"
    jack.say "A holy Paladin!"
    mike.say "A knight in shining armour!"
    mike.say "I can make that work!"
    jack.say "Who draws his power from an inviolable vow of total chastity!"
    mike.say "WHAT?!?"
    mike.say "Gamesmaster, that sucks!"
    "Jack holds up his hand, cutting off [mike.name]'s protests."
    jack.say "No arguing, Sir Percival."
    jack.say "Your sacred vow is essential to the plot!"
    "[mike.name] shakes his head and begins to mutter something under his breath."
    jack.say "Sasha..."
    jack.say "Thou art translated into 'Lilith'!"
    jack.say "A half-demon, half-human sorceress!"
    jack.say "Seduction made infernal flesh!"
    sasha.say "Alright!"
    sasha.say "Now you're talking!"
    mike.say "No fair, Gamesmaster!"
    mike.say "You're making me play what's basically a eunuch!"
    jack.say "Silence, Sir Percival!"
    "I'm waiting eagerly for my turn, wondering what's in store for me."
    "Despite [mike.name]'s complaints, both his and Sasha's characters sound great from where I'm sitting."
    jack.say "And finally, [hero.name]..."
    jack.say "Thou art Galadria!"
    jack.say "Elven priestess of the Goddess of Love!"
    jack.say "Beauty and grace personified - and a hot chick to boot!"
    show rpg sashabored
    sasha.say "Passeth ye olde bucket, because I think I'm gonna be sick!"
    if hero.morality <= -50:
        "Ooh...I'm already starting to get a tingle when I think about the possibilities!"
        "Jack's a dirty little perv, dreaming up characters for me and Sasha to play."
        "I be he's already been fantasising about 'Lilith and Galadria'!"
        "And he's nerfed [mike.name] into a goody-goody wimp as well."
        "This is going to be a lot of fun!"
        bree.say "Mmm..."
        bree.say "I accept the mantle of Galadria, Gamesmaster!"
        bree.say "And I think that I should spread love to honour my patron deity."
        bree.say "Not in the platonic sense either."
        show rpg sashanormal
        bree.say "I mean worship her through hot, wanton and erotic action!"
    elif hero.morality <= -25:
        "Jack's such an obvious little perv!"
        "He's been dreaming of Sasha and me dressed up as sexy fantasy babes this whole time."
        "And now he's trying to make us act out his little fantasy for him!"
        "Plus he's taken [mike.name] out of contention by making the poor guy a chaste, holy knight!"
        "If I were a bigger nerd, I'd probably call him out on it."
        "But all of this sounds like too much fun!"
        bree.say "I accept the mantle of Galadria, Gamesmaster!"
        show rpg sashanormal
        bree.say "I will be a beacon of passion, a torch of sensuality!"
        bree.say "I'll light up this dark world with my boundless love!"
    elif hero.morality >= 25:
        "I like the idea of being a powerful priestess."
        "And I just love the idea of being an elf even more!"
        bree.say "I accept the mantle of Galadria, Gamesmaster!"
        bree.say "I will be a shining beacon of goodness in a dark world!"
        show rpg sashabored
        sasha.say "Urgh..."
        sasha.say "At this rate, I'm gonna need another bucket!"
    else:
        "I can't help rolling my eyes as Jack hands out the sheets with our characters on them."
        "It's impossible not to see what he's up to, making Sasha and I play stereotypical fantasy babes."
        "Plus he's taken [mike.name] out of contention by making the poor guy a chaste, holy knight!"
        "I could call him out right here and how, but I decide to give him another chance."
        bree.say "Okay, Gamesmaster..."
        bree.say "I'll do my best to play Galadria."
    jack.say "Ahem..."
    jack.say "Great to see you all getting into character..."
    show rpg sashanormal
    "Jack ducks down behind his card screen for a moment."
    "[mike.name], Sasha and I exchange puzzled glances and shrugs."
    "But then Jack pops up again, making us jump."
    scene bg white
    pause 0.15
    scene bg rpgforest at blur(16), dark
    jack.say "NIGHTFALL!"
    jack.say "Nightfall..."
    scene bg rpgforest at dark
    show sasha rpg at right
    show mike rpg at mostleft4
    show bree rpg
    with dissolve
    jack.say "And you find yourselves in the outskirts of a small village."
    jack.say "The day has been long and hard..."
    show sasha joke
    sasha.say "Ha, ha!"
    jack.say "Filled with tiresome travelling, which leaves you exhausted."
    jack.say "You make straight for the sound of raised voices and music."
    jack.say "Seeking instinctively for the one tavern at the centre of town."
    show sasha normal
    show rpg
    sasha.say "Wait..."
    sasha.say "A tavern's like a pub, right?"
    mike.say "Yeah, but with more smoke and straw on the floor."
    sasha.say "Ooh...I know a couple of places like that!"
    jack.say "AHEM!"
    hide rpg with dissolve
    jack.say "Opening the door, you are greeted with dozens of staring eyes."
    sasha.say "Loads of eyes?"
    show sasha flirt
    sasha.say "It's a monster!"
    sasha.say "Let's kill it and nick it's stuff!"
    jack.say "The eyes all belong to the VILLAGERS, Lilith!"
    show mike happy
    show sasha happy
    "At this, [mike.name], Sasha and I can't help bursting into laughter."
    "But Jack shakes his head and does his best to soldier on."
    show mike normal
    show sasha normal
    jack.say "The villagers..."
    jack.say "Who are looking at the door..."
    jack.say "All of them wondering what brings strangers to their remote, isolated village?"
    "With that, Jack falls silent."
    "He gives us a certain look."
    "It's like he's expecting us to do something."
    "But what could it be?"
    show rpg
    mike.say "Erm, guys..."
    mike.say "This is the bit where we actually do the roleplaying, right?"
    "Sasha and I exchange a glance and a shrug of the shoulders."
    "Here goes nothing!"
    bree.say "I..."
    bree.say "I walk up to the bar?"
    "Jack looks at me over the top of his screen."
    "His eyes are wide and he's nodding eagerly."
    bree.say "And I...order some drinks?"
    mike.say "Try getting into character, [hero.name]!"
    "I nod, putting on my best attempt at how I think Galadria would sound."
    bree.say "B...barkeep?"
    bree.say "Three flagons of your finest ale!"
    sasha.say "Yeah, and be quick about it too!"
    "I see smiles on both Jack and [mike.name]'s faces."
    "So I guess that means we did pretty well."
    jack.say "Oh, right away, my dears!"
    "Jack puts on a high-pitched voice as he plays out the barmaid's response."
    "It's not exactly the most feminine thing I've ever heard."
    "And I can't help chuckling as he does it."
    show rpg tavern with dissolve
    jack.say "The barkeep hands you each a foaming flagon of ale."
    jack.say "And then you find an empty table in one corner of the taproom."
    jack.say "But no sooner have you sat down than one of the villagers walks over."
    jack.say "He's an old man that seems to be better dressed than most of the others."
    jack.say "He smiles and introduces himself..."
    jack.say "'Greetings, adventurers,' he says, 'welcome to our humble village.'"
    jack.say "'My name is Elder Perkins, and I wonder if you come looking for work?'"
    jack.say "'We have been plagued by goblins in the hills around here.'"
    jack.say "'And I would like to hire you to take care of them.'"
    "Sasha seems to be getting into the swing of things by now."
    "Because she instantly leans across the table, pointing a finger at Jack."
    sasha.say "Now see here, old man - we don't work for free!"
    sasha.say "Adventuring gear ain't cheap."
    sasha.say "And we need to pay for all this shit!"
    mike.say "Ah..."
    mike.say "What my companion means to say is that we have obvious expenses."
    mike.say "But I'm sure that whatever form of material compensation you offer will be sufficient!"
    if hero.morality <= -50:
        "Things have been a little vanilla thus far."
        "So maybe it's time somebody spiced it up a little?"
        bree.say "Material compensation is all well and good, Elder Perkins."
        bree.say "But there are other ways to pay us for our efforts."
        bree.say "For example, you could extend us credit in your local businesses."
        bree.say "Particularly those that are concerned with the pleasures of the flesh."
        bree.say "If you know what I mean?"
    elif hero.morality <= -25:
        "Things have been a little vanilla thus far."
        "So maybe it's time somebody spiced it up a little?"
        bree.say "Material compensation is all well and good, Elder Perkins."
        bree.say "But there are other ways to pay us for our efforts."
        bree.say "For example, you could extend us credit in your local business establishments."
        bree.say "I'm sure we'd be very grateful if your tradespeople made themselves available to us?"
        bree.say "If they let us take advantage of them when we felt the need?"
    elif hero.morality >= 25:
        "I figure that, as a priestess of love, I should set a good example."
        "So I step in to back [mike.name] up as he tries to downplay Sasha's rudeness."
        bree.say "My noble friend is right, Elder Perkins."
        bree.say "We will be amply compensated by whatever you can spare."
        show rpg sashabored
        sasha.say "Hey - you're selling my skills way too cheap!"
    else:
        "I can see what [mike.name]'s trying to do as he downplays Sasha's rudeness."
        "But she does have a point, and I don't want to see us exploited either."
        "So maybe I can be the voice of reason here?"
        bree.say "Both of my companions are right, Elder Perkins."
        bree.say "We must be compensated for our efforts."
        bree.say "But we also understand that you are a community of humble means."
        bree.say "Therefore our fee will be fair and not excessive."
    jack.say "Elder Perkins looks more than a little flustered."
    show rpg sashanormal
    jack.say "But he nods all the same, agreeing to your terms."
    jack.say "And I think that's a pretty good place to leave things."
    show rpg livingroom with dissolve
    jack.say "So how did you girls find your first roleplaying session?"
    "Sasha leans back in her chair and nods her head."
    sasha.say "Not gonna lie..."
    sasha.say "I had more fun than I thought I would!"
    bree.say "Me too, Jack!"
    bree.say "I want to see what happens when we go after the goblins."
    "Jack looks pleased with the reactions that he's getting from us."
    "He nods as he begins to pack away his things."
    $ jack.love += 2
    jack.say "That's great!"
    jack.say "We can organise another gaming session as soon as we're all free."
    "As [mike.name] shows Jack to the door, Sasha and I start to tidy things up a little."
    "[mike.name] comes back to help a moment later, and we're soon done."
    "Everyone's chatting idly as we tidy, but my mind is elsewhere."
    "And I'm already day-dreaming about our next roleplaying session."
    return

label jack_female_event_04_bis:
    if jack.love.max < 80:
        $ jack.love.max = 80
    scene bg park
    "Jack mentioned that he was going to be hanging out at the park today."
    "And he told me that I was more than welcome to come along and join him."
    "To be honest, I decided to take him up on the offer out of curiosity."
    "Jack's not the kind of guy that does much outdoors stuff of any kind."
    "So part of me is dying to know why he's at the park in the first place."
    "And yeah, I do kind of want to hang out with Jack too."
    "I can't help it, I like the big old nerd!"
    "It's only when I get there that I realise something important."
    "Jack didn't just fail to tell me what he was doing."
    "He also neglected to tell me where he was doing it too!"
    "So as soon as I reach the park, I have to start searching for him."
    "I walk along the paths that wind through the place."
    "And all the time I'm looking for any sign of Jack."
    jack.say "Get back, foul wench!"
    jack.say "Else you'll feel the bite of my blade!"
    "Wait a minute - that sounds like Jack."
    "And his voice is raised, like he's in trouble!"
    "I follow the sound of Jack's voice, running as fast as I can."
    "It doesn't take me long to track him down either."
    show jack halloween at mostright5 with moveinright
    "As I round the corner, I'm relieved to see him there."
    "But a moment later I find myself blinking and shaking my head."
    "And that's because I can't actually believe what I'm seeing!"
    "Jack's standing there, dressed in a furry pair of pants."
    "He has some kind of horned helmet on his head."
    "And there's an actual sword in his hands too!"
    "Weirder still, it looks like he's having a fight with a guy."
    "He's dressed as strangely as Jack too, with pointed ears!"
    "I hurry over, calling out to him as I get closer."
    bree.say "Jack!"
    bree.say "Jack, what's going on!"
    "Elf" "Erm..."
    "Elf" "Well, that kind of killed the illusion for me!"
    "Elf" "You know this maiden, Jackdar?"
    "Elf" "Because she seems to think she knows you!"
    show fx drop at mostright5
    "Jack looks instantly embarrassed, going red in the face."
    "But I can't tell if it's on account of me or the person with the pointy ears."
    jack.say "Yeah, yeah..."
    hide fx
    jack.say "It's okay, Thandariel."
    jack.say "She's with me - I invited her along."
    "The person with the pointed ears roll their eyes and walks away."
    "And it's only now that I notice two other things I missed before."
    "One is that the axe in Jack's hand is made of rubber."
    "And the other is that there are more than a few other people walking around in funny costumes too."
    "I glance around, seeing that they're dressed as what look like characters from a fantasy novel."
    show jack at center with move
    jack.say "Sorry about that, [hero.name]."
    jack.say "Thandariel and I were just getting some practice in before the game starts for real."
    jack.say "He's a great guy, for an elf - but he hates to break character!"
    bree.say "What is all of this, Jack?"
    bree.say "Did you join an amateur dramatic group?"
    bree.say "Are you all going to be extras in a film?"
    jack.say "Oh no, [hero.name] - it's better than that."
    jack.say "We're larping!"
    bree.say "Wh...what's larping?"
    jack.say "Oh, sorry...Live action roleplaying - larping for short!"
    bree.say "You mean like Demons and Demigods roleplaying?"
    show jack happy
    jack.say "Yeah, kind of - but we act it all out for real!"
    jack.say "I didn't tell you about it because I wanted it to be a surprise."
    show jack normal
    jack.say "So what do you think?"
    jack.say "Pretty cool, huh?"
    if hero.morality <= -50:
        bree.say "Are all of the outfits that revealing, Jack?"
        bree.say "Because I don't think I've seen you wear as little as that before!"
        "I walk slowly around Jack, looking him up and down."
        "He turns his head to follow me, his cheeks now burning."
        show fx drop
        jack.say "Ah...no, [hero.name]..."
        jack.say "That's not really the point here!"
        hide fx
        bree.say "You look SO hot in that thing, Jack!"
        bree.say "All I can think about is you carrying me off like a helpless damsel."
        bree.say "That and what I'd want you to do to me once I was back at your castle!"
        bree.say "Can you imagine that too, Jack?"
        show jack perv
        "I can see that Jack's fiddling with his faux-fur shorts."
        "It's almost as if they're suddenly feeling a little too small."
        jack.say "Y...you really mean that, [hero.name]?"
        jack.say "You think it's cool?"
        jack.say "I mean...it IS cool..."
        jack.say "But it's cooler that you think it's cool too!"
        bree.say "Sure it is, Jack!"
        bree.say "I can already see the possibilities!"
        bree.say "You think I can get involved too?"
        $ jack.love += 5
        show jack happy
        "Now Jack looks like a kid on Christmas morning."
        "My guess is that he was hoping I'd be interested."
        "But he does his best to make it look like he's not elated."
        jack.say "Of course, [hero.name]..."
        show jack normal
        jack.say "I...I mean, sure, if you like..."
        "Jack spends the rest of the afternoon showing me the ropes."
        "He introduces me to all of the other 'larpers', as he calls them."
        "And by the time we're done, I'm already thinking up ideas for my own character."
    elif hero.morality <= -25:
        bree.say "Are all of the outfits that revealing, Jack?"
        bree.say "Because I don't think I've seen you wear as little as that before!"
        "I walk slowly around Jack, looking him up and down."
        "He turns his head to follow me, his cheeks now burning."
        show fx drop
        jack.say "Ah...no, [hero.name]..."
        jack.say "That's not really the point here!"
        hide fx
        bree.say "It would be if I were involved!"
        bree.say "Just imagine what else you could get away with."
        bree.say "I've seen those chain-mail bikinis in fantasy art!"
        bree.say "I bet I could pull one of those off, right?"
        show jack perv
        "I can see that Jack's fiddling with his faux-fur shorts."
        "It's almost as if they're suddenly feeling a little too small."
        jack.say "Y...you really mean that, [hero.name]?"
        jack.say "You think it's cool?"
        jack.say "I mean...it IS cool..."
        jack.say "But it's cooler that you think it's cool too!"
        bree.say "Sure it is, Jack!"
        bree.say "I can already see the possibilities!"
        bree.say "You think I can get involved too?"
        $ jack.love += 5
        show jack happy
        "Now Jack looks like a kid on Christmas morning."
        "My guess is that he was hoping I'd be interested."
        "But he does his best to make it look like he's not elated."
        jack.say "Of course, [hero.name]..."
        show jack normal
        jack.say "I...I mean, sure, if you like..."
        "Jack spends the rest of the afternoon showing me the ropes."
        "He introduces me to all of the other 'larpers', as he calls them."
        "And by the time we're done, I'm already thinking up ideas for my own character."
    elif hero.morality >= 50:
        "I can't help still feeling more than a little shaken."
        "The sound of Jack shouting and thinking that he was in danger..."
        "Plus the idea of running around in all of these crazy costumes."
        "It's all too much for me!"
        bree.say "No, Jack, it's not!"
        bree.say "In fact, it's really scary!"
        "Jack looks genuinely shocked and concerned with my answer."
        show fx drop
        jack.say "I...I'm sorry, [hero.name]."
        jack.say "I had no idea all of this would scare you!"
        jack.say "Is there anything I can do to make it up to you?"
        hide fx
        "I glance around again, looking at all of the strangeness around me."
        bree.say "Right now all I want to do is go home, where it's safe!"
        bree.say "That and never come here again!"
        $ jack.love -= 5
        jack.say "Okay, [hero.name]..."
        jack.say "If that's what you want..."
        hide jack
        "I hurry away, not bothering to look over my shoulder."
        "I know that I should have said goodbye to jack."
        "But I feel the need to get to a place where I feel safe."
        "I just hope that he can understand that."
    elif hero.morality >= 25:
        "I can't help bursting into laughter once Jack's explained himself to me."
        "He looks at me with an expression of confusion on his face."
        jack.say "What is it, [hero.name]?"
        jack.say "What's so funny?"
        bree.say "Oh, Jack..."
        bree.say "You're standing there in a faux-fur posing pouch."
        bree.say "And you have a rubber axe in your hand too."
        bree.say "You look like you're about to go trick or treating on Halloween!"
        "The colour in Jack's cheeks becomes instantly more intense."
        "And in that moment he seems to realise how little he actually has on."
        show fx anger
        jack.say "Hey!"
        jack.say "This costume took me an age to make!"
        jack.say "And we've all worked hard to organise this game!"
        jack.say "We take all of this very seriously!"
        bree.say "Jack, you're running around the park dressed as elves and barbarians!"
        bree.say "It's about as far from serious as you can get!"
        $ jack.love -= 10
        "Jack looks down at his feet, fingering his rubber axe."
        jack.say "I...I thought you'd be into this kind of thing, [hero.name]."
        jack.say "I mean, you like RPG's and fantasy, right?"
        bree.say "Yeah, but I don't want to dress up and play pretend games, Jack!"
        bree.say "I kind of stopped doing that when I grew up!"
        jack.say "Oh..."
        jack.say "Okay, I guess..."
        bree.say "Look, Jack..."
        bree.say "I'm going to get out of here, leave you to play with your friends."
        bree.say "Call me if you ever want to do something a little more adult, okay?"
        hide jack
        "Jack nods and watches me as I turn and walk away."
        "Part of me hopes that I haven't wounded his pride too deeply."
        "But I'm not going to pretend to like something that lame just to please him."
        "That's no way to be a good friend to him, let alone anything more than that."
    else:
        "I keep on looking at the people spread around us."
        "Their costumes are so cool, so well made too."
        "All of them seem to be having a great time as well."
        bree.say "Jack..."
        bree.say "Why didn't you tell me you were into something like this?"
        bree.say "It's like Demons and Demigods, but for real!"
        "Jack looks a little stunned at my enthusiasm."
        "But I guess that's understandable."
        "We geeks are pretty protective of the things we love."
        "And he was taking a big risk opening up to me about this."
        jack.say "Y...you really mean that, [hero.name]?"
        jack.say "You think it's cool?"
        jack.say "I mean...it IS cool..."
        jack.say "But it's cooler that you think it's cool too!"
        bree.say "Sure it is, Jack!"
        bree.say "Did you make all of this stuff yourself?"
        bree.say "Like your costume?"
        "Jack visibly swells with pride as I gush over his costume."
        "Suddenly he looks every bit the fantasy barbarian to me."
        jack.say "Yeah, [hero.name], I did."
        jack.say "Most of us make our own stuff - so it's totally unique!"
        bree.say "Do you think..."
        bree.say "Maybe I could get in on the act too?"
        $ jack.love += 5
        show jack happy
        "Now Jack looks like a kid on Christmas morning."
        "My guess is that he was hoping I'd be interested."
        "But he does his best to make it look like he's not elated."
        jack.say "Of course, [hero.name]..."
        show jack normal
        jack.say "I...I mean, sure, if you like..."
        "Jack spends the rest of the afternoon showing me the ropes."
        "He introduces me to all of the other 'larpers', as he calls them."
        "And by the time we're done, I'm already thinking up ideas for my own character."
    return

label jack_female_event_05_bis:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Jack")
    if not result:
        $ hero.cancel_event()
        $ jack.love -= 5
        return
    if jack.love.max < 120:
        $ jack.love.max = 120
    $ jack.flags.nodate = False
    "When my phone rings, I always make sure to check out who's calling before I answer."
    "Because nobody wants to look like they're totally desperate and pick up straight away, right?"
    "But when I see the caller ID, I change my mind pretty quickly."
    "The call's from Jack, and I can't help smiling as I answer it."
    bree.say "Hey, Jack!"
    bree.say "How are you doing?"
    jack.say "Hey, [hero.name]!"
    jack.say "Pretty good."
    jack.say "But better after hearing your voice!"
    "It's a cheesy line, but I can't help chuckling at it all the same."
    "Any other guy and I'd have been put off by a line the likes of that."
    "But somehow, when it's coming from Jack, it's just so cute!"
    bree.say "Me too, Jack, me too!"
    bree.say "So, did you call to hear my voice?"
    bree.say "Or was there something else?"
    jack.say "Oh yeah, [hero.name], of course."
    jack.say "You like music, right?"
    bree.say "Erm, yeah, Jack."
    bree.say "Doesn't everyone?"
    jack.say "That's great, [hero.name]!"
    jack.say "So you'll want to come to the gig with me?"
    "I find myself smiling and shaking my head."
    "It sounds like Jack's getting ahead of himself."
    "But that's probably because he was so eager to ask me out."
    bree.say "What gig would that be, Jack?"
    bree.say "You never mentioned it before now!"
    jack.say "Oh, yeah!"
    jack.say "Sorry, [hero.name]!"
    jack.say "Let me start over..."
    jack.say "[mike.name]'s band are playing a gig in town, right?"
    jack.say "And he's managed to get me on the guest list."
    jack.say "Me and a plus one too!"
    bree.say "And you wanted to ask..."
    jack.say "Yeah, [hero.name] - I wanted to ask if you'd come?"
    jack.say "You want to be my plus one for the night?"
    if hero.morality <= -25:
        "It's a total no-brainer for me - of course I want to go to the gig!"
        "All those people pressed together in a sweaty little venue."
        "That means Jack and I are going to be pressed together the whole time."
        "So there's a whole world of possibilities to explore!"
        bree.say "Of course I do, Jack!"
        bree.say "I've never seen their band actually play before."
        bree.say "But it's not like that's the important thing, is it?"
        bree.say "What matters is that we'll be in that crowd together."
        bree.say "Right in the middle of the crowd!"
        jack.say "Ah, yeah, [hero.name]...I guess so!"
        jack.say "I mean, it can get pretty intense in there..."
        "I let out a peal of laughter."
        "And that cuts Jack off before he can finish what he was trying to say."
        bree.say "Oh, I'm not worried about that, Jack!"
        bree.say "Because I know that you'll be there to protect me, right?"
        bree.say "And I'll be sure to keep right by your side the whole time."
        bree.say "Trust me, I'll be pressed against you so close."
        bree.say "You'll be able to feel every inch of my body..."
        $ jack.sub += 2
        "For a moment it sounds like Jack's tuned out from reality."
        "And I can just picture him thinking about all I just said."
        bree.say "Ah, Jack..."
        bree.say "Are you still there?"
        jack.say "Oh..."
        jack.say "Oh yeah, [hero.name]!"
        jack.say "I'm just stoked that you're coming along, that's all."
        bree.say "Me too, Jack."
        bree.say "It's going to be fun."
        scene expression f"bg {game.room}"
        "I'm still smiling when we end the call."
        "This gig is going to be a whole lot of fun."
        "And also a chance to get closer to Jack."
        "In every possible sense of the word!"
        $ jack.flags.go_to_gig = True
    elif hero.morality >= 25:
        "Part of me wants to say yes on the spot."
        "And that's because I'd love to have the chance to hang out with Jack."
        "But what stops me is the thought of being in a venue full to the rafters."
        "There's sure to be far too much noise as well, at least too much for me."
        "And then there's that fact that I've heard [mike.name] and Sasha practicing."
        "They sound like they're torturing cats!"
        bree.say "I'm flattered, Jack, really I am."
        bree.say "But I'm not really into the kind of music they play."
        $ jack.love -= 2
        "Jack sounds instantly disappointed with my answer."
        "But bless his heart, he does the best he can to hide it."
        jack.say "Oh..."
        jack.say "Okay, [hero.name]."
        jack.say "If it's not your kind of thing..."
        bree.say "Maybe we could do something else instead?"
        bree.say "You know, just you and me?"
        jack.say "Maybe, [hero.name]."
        jack.say "I'll check my calendar and get back to you, okay?"
        bree.say "Okay, Jack."
        scene expression f"bg {game.room}"
        "As soon as Jack hangs up, I start worrying."
        "Did I just do the wrong thing?"
        "Should I have lied and gone to the gig anyway?"
        "I guess all I can do is wait and see."
    else:
        menu:
            "Accept":
                "I barely need to think before I blurt out my answer."
                "No sooner has Jack asked the question than I'm nodding eagerly."
                bree.say "Of course I do, Jack!"
                bree.say "I've never seen their band actually play before."
                bree.say "I mean, I've heard [mike.name] and Sasha practicing around the house."
                bree.say "But I've never been to one of their gigs."
                jack.say "That's perfect, [hero.name]!"
                jack.say "We can have a great night at the gig."
                jack.say "And we can tick something off your bucket list at the same time!"
                "I can't help chucking at the suggestion and the way Jack makes it."
                bree.say "I'm not sure seeing [mike.name] and Sasha on stage is on my bucket list, Jack!"
                bree.say "At least not ahead of travelling the world or winning the lottery!"
                jack.say "Ah..."
                jack.say "Okay, [hero.name]!"
                jack.say "I'm just stoked that you're coming along, that's all."
                bree.say "Me too, Jack."
                bree.say "It's going to be fun."
                scene expression f"bg {game.room}"
                "I'm still smiling when we end the call."
                "And I'm not humouring Jack either."
                "The gig sounds like a lot of fun, and I can't wait for it."
                "All I have to do now is wait for the big night to come around."
                $ jack.flags.go_to_gig = True
            "Refuse":
                "Ah, damn it!"
                "Why did he have to ask me to go see [mike.name] and Sasha's band?"
                "Anything else and I'd have been there in an instant."
                "But I've heard the pair of them practicing around the house."
                "'Deathless Harpies' they call themselves."
                "More like 'Tone Deaf Harpies'!"
                "They sound like they're torturing cats!"
                bree.say "I'm flattered, Jack, really I am."
                bree.say "But I'm not really into the kind of music they play."
                "Jack sounds instantly disappointed with my answer."
                "But bless his heart, he does the best he can to hide it."
                jack.say "Oh..."
                jack.say "Okay, [hero.name]."
                jack.say "If it's not your kind of thing..."
                bree.say "Don't get down-hearted, Jack."
                bree.say "We can do something else together instead."
                bree.say "Something that's much more fun, yeah?"
                jack.say "Okay, [hero.name]..."
                jack.say "That could work."
                "I can hear Jack trying to cheer himself up and warm to the idea."
                "It's like he still wants to spend the time with me."
                "But he's also still smarting from me rejecting his own idea."
                jack.say "I'll check my calendar and get back to you, okay?"
                bree.say "Okay, Jack."
                scene expression f"bg {game.room}"
                "As soon as Jack hangs up, I regret turning him down like that."
                "Maybe I should have just swallowed my pride and agreed to go."
                "But part of me feels like it'd be wrong to lie to him like that."
                "I want Jack to get to know the real me, not someone I'm pretending to be."
                "I guess that all I can do is wait and see how things turn out."
    return

label jack_female_event_06_bis:
    "Let's go see the Deathless Harpies"
    menu:
        "Go":
            pass
        "Report":
            $ hero.cancel_event()
            $ jack.love -= 2
            return
    if jack.love.max < 140:
        $ jack.love.max = 140
    $ jack.flags.nokiss = False
    show bg street
    "When the night of the gig comes around, I can't believe how nervous I'm actually feeling."
    "It's not like I've never been to something like this before."
    "In fact, I've been to much bigger and more impressive gigs in the past."
    "But somehow this one is more exciting than anything else I can remember."
    "Maybe it's because I'm finally going to get to see [mike.name] and Sasha on stage?"
    "Which is going to be super-weird!"
    "Or maybe it's got more to do with the fact that I'm going to the gig with Jack?"
    "Sure, we've been on dates already and we spend a lot of time hanging out together."
    "But this is different - more like the kind of thing that couples do, you know?"
    "It's almost like we're going to this thing as boyfriend and girlfriend!"
    "Even if we're not - because we're not boyfriend and girlfriend...are we?"
    "Anyway...where was I?"
    "Oh yeah, the gig!"
    "The place the Deathless Harpies are playing is pretty small."
    show bg pub
    show jack casual
    "But once Jack and I get inside, we find that it's packed to the rafters."
    "This means that it somehow feels much larger, like a much bigger deal."
    jack.say "Geez..."
    jack.say "I've never seen this place so full!"
    jack.say "This is crazy, [hero.name]!"
    "Jack and I are holding hands as he says this."
    "It's more on account of keeping together than anything else."
    "But I still find myself squeezing his hand from time to time."
    "And I find the sensation reassuring when he does the same in return."
    bree.say "I know, Jack!"
    bree.say "Just don't let go of me, okay?"
    bree.say "Whoa...is that..."
    bree.say "Yeah, it is - there are people with Deathless Harpies T-shirts here!"
    jack.say "Hah!"
    jack.say "[mike.name] told me they were getting some printed up!"
    bree.say "Oh wow..."
    bree.say "I HAVE to get one of those, Jack!"
    bree.say "They're so cool!"
    "Jack and I fight our way over to the merch tables."
    "And I see the piles of Deathless Harpies T-shirts for sale."
    "I'm about to pick one up and pay for it."
    "But then I feel Jack put his hand over mine."
    jack.say "Hey, [hero.name]..."
    jack.say "Let me buy you one, okay?"
    menu:
        "Accept":
            bree.say "You don't need to do that, Jack."
            bree.say "You were the one that got me in here for free to begin with!"
            jack.say "Yeah, [hero.name]..."
            jack.say "But we were on the guest-list, so it was a freebie."
            jack.say "And I know it sounds dumb, but that makes me feel kind of cheap!"
            "I frown at Jack and let out a little chuckle."
            "Guys can be so strangely old-fashioned sometimes."
            "But I guess if it makes him feel better..."
            bree.say "Okay, Jack."
            bree.say "If it makes you feel more like a gentleman!"
            "Jack beams as I indulge him, buying the T-shirt I wanted."
            "He hands it to me with a smile, and we dive back into the crowd."
        "Decline":
            "I can't help scoffing at the idea of Jack buying me a T-shirt."
            "And that's exactly how I phrase it a moment later."
            bree.say "Ah, you're okay, Jack."
            bree.say "I can afford to buy myself a T-shirt!"
            jack.say "Oh..."
            jack.say "Okay, [hero.name]..."
            "I shake my head as he backs off."
            "What is it with some guys?"
            "It's like they need to be in control of everything a girl does!"
            "Shaking my head, I buy the T-shirt and forget about it."
    "Almost the same moment that we're back in the crush of the crowd, something seems to change."
    "It's like everyone in the place is suddenly aware of it to, as they all surge forwards."
    "In the rush, I almost lose my grip on Jack's hand and get swept away."
    "But he seems to sense the danger of this happening and wraps his arms around me."
    "As the crowd surges around us, Jack holds me tight, protecting me the whole time."
    "And it's weird, but the sensation of being wrapped in his arms keeps me totally calm."
    "Everyone else in the crowd feels like they're too close, pressing in on me."
    "But not Jack, even though he's the closest to me of all."
    "Instead his closeness feels right, almost like it's natural."
    "The lights go up on the stage a moment later, explaining the rush forwards."
    "And then I see figures moving up there too, silhouetted by the glare."
    "There's the sound of instruments being tuned up."
    "Then the silhouette's resolve themselves into recognisable people."
    scene bg black
    show concert anna kleio sasha mike with fade
    kleio.say "Hello, you sexy bastards!"
    kleio.say "We are the Deathless Harpies."
    kleio.say "And we're here to FUCKING ROCK!"
    "At this, the crowd goes wild."
    "Limbs are flying everywhere."
    "People are screaming in delight."
    "I see [mike.name] and Sasha up there with the other band members."
    "I think their names are Chloe and Annie?"
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "And it feels like I'm at one of those gigs you see in the movies."
    "The music is mega-loud and I can't make out most of the lyrics."
    "But the atmosphere is out of this world and I absolutely love it!"
    "As the crowd begins to move, it loosens up as well."
    "And Jack instinctively loosens his grip on me too."
    if hero.morality <= -50:
        "The moment I realise what he's doing, I grab hold of Jack's wrists."
        "And at the same time I grind my ass into his groin, just to emphasize the point."
        "He resists for a moment, but then goes with it."
        "And a then I feel him pull me closer still."
        "Looks like he's getting the message!"
        "It feels amazing to have Jack pressed so close to me."
        "And I decide that this is how we're going to spend the rest of the gig."
        "The fact that we're in the middle of the crowd means that we can be this close."
        "Pressed up against people all around us, close enough to hear then breathe."
        "But at the same time too close for them to be able to see what we're doing."
        "We couldn't exchange a word even if we wanted to."
        "The band is way too loud for that to be possible."
        "But Jack and I seem to be able to communicate on a physical level."
        "There's none of the usual geeky awkwardness from him when it's like this."
        "And I don't have to worry about saying the wrong thing either."
        "It's like we've finally found a way to connect without any barriers."
        "I love the feel of him getting hard against me."
        "I love knowing that I'm getting him hot and bothered too."
        "There's only one thing that I can think of to make it better."
        "I reach around and search until I find Jack's flies."
        "And then I unzip them, sliding my hand in before he can object."
        "He shudders as I begin to stroke the length of his shaft."
        "I hear the gasps of breath that he's taking too."
        "And I know that my fingers are doing a good job."
        "Normally I'd take my time and tease him towards losing it."
        "But Jack's already worked up and seriously aroused."
        "Plus there's the fact that I'm doing all of this in the middle of the crowd."
        "And Jack couldn't escape my attentions without making a scene and giving away what's happening."
        "Instead he's forced to stand there while I use my hand to push him over the edge."
        "Pretty soon I hear him gasping even more loudly."
        "Then I feel something warm, wet and sticky oozing between my fingers!"
        "And a wicked smile spreads across my face."
    elif hero.morality <= -25:
        "The moment I realise what he's doing, I grab hold of Jack's wrists."
        "And at the same time I grind my ass into his groin, just to emphasize the point."
        "He resists for a moment, but then goes with it."
        "And a then I feel him pull me closer still."
        "Looks like he's getting the message!"
        "It feels amazing to have Jack pressed so close to me."
        "And I decide that this is how we're going to spend the rest of the gig."
        "The fact that we're in the middle of the crowd means that we can be this close."
        "Pressed up against people all around us, close enough to hear then breathe."
        "But at the same time too close for them to be able to see what we're doing."
        "We couldn't exchange a word even if we wanted to."
        "The band is way too loud for that to be possible."
        "But Jack and I seem to be able to communicate on a physical level."
        "There's none of the usual geeky awkwardness from him when it's like this."
        "And I don't have to worry about saying the wrong thing either."
        "It's like we've finally found a way to connect without any barriers."
        "I love the feel of him getting hard against me."
        "I love knowing that I'm getting him hot and bothered too."
        "I have no idea if he's able to keep from making a mess in his shorts."
        "But the thought of it is enough to put a wicked smile on my face."
    else:
        "Instinctively I take hold of Jack's wrists."
        "And then I wrap his arms around my waist."
        "He resists for a moment, but then goes with it."
        "And a then I feel him pull me closer still."
        "The fact that all of this happens on instinct is amazing."
        "It sends a genuine thrill running through me too!"
        "Somehow it just feels right, Jack and I being so close."
        "That's how we spend the rest of the gig."
        "Jack holding me while I lean back into him."
        "Sure, I can feel every part of his body."
        "And I'm liking the fact that I can."
        "But it's not like we're getting hot and heavy in a public place!"
        "It's more that we're comfortable together, like a hand in a glove."
        "We couldn't exchange a word even if we wanted to."
        "The band is way too loud for that to be possible."
        "But Jack and I seem to be able to communicate on a physical level."
        "There's none of the usual geeky awkwardness from him when it's like this."
        "And I don't have to worry about saying the wrong thing either."
        "It's like we've finally found a way to connect without any barriers."
    "Once the Deathless Harpies have played their last song, Jack and I squeeze out of the crowd."
    scene bg pub
    show jack casual smile
    with fade
    "We must look like a complete mess, because I'm soaked with sweat and absolutely exhausted."
    "But Jack has a huge smile on his face, and I can't help following his example."
    bree.say "Wow..."
    bree.say "That was amazing, Jack!"
    bree.say "But I think I went deaf halfway through!"
    show jack normal
    jack.say "Huh, [hero.name]?"
    jack.say "What was that?"
    "I roll my eyes and give him a gentle poke in the ribs."
    bree.say "Very funny, Jack!"
    show jack happy
    jack.say "You want to hang around here a while?"
    jack.say "Maybe get that T-shirt signed?"
    bree.say "Nah, let's get out of here."
    bree.say "I can get fifty percent of that done at home!"
    $ jack.love += 2
    return

label jack_birthday_date_female:
    $ DONE["jack_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg street with fade
    "I keep pulling out my phone to check the time, then shoving it back in my pocket."
    "I'm one hundred percent sure that I told Jack to meet me here and the right time."
    "It was kind of [mike.name]'s idea to take Jack on a date to a games-store."
    "And I'm stepping outside of my comfort zone doing this."
    "But where in the hell is Jack?"
    "He's usually pretty good at making it on time, mainly because he's eager to please."
    "But I've been standing outside the local games-store for almost half an hour."
    "And there's still no sign of him, no answers to my texts and no answer when I call him either."
    "At this rate we're going to lose the table I've booked for us inside the place."
    "That thought makes me paranoid, and I turn to take a glance through the window."
    "I'm trying to check that the table's still free."
    "But then I do a double-take, as I recognise one of the guys in there."
    "Sure, they all kind of look alike - long hair, beards, and some with questionable hygiene."
    "But I can still pick Jack out of the crowd."
    "And there he is, browsing the shelves without a care in the world!"
    "Without pausing to collect myself, I storm straight into the store."
    scene bg gamestore with fade
    "This seems to cause a strange amount of disturbance in the place."
    "So much so that I have to stop halfway across the store."
    "Because I realise that everyone in the place is staring at me."
    show jack at left with easeinleft
    "Luckily for me, Jack turns and sees me a few seconds later."
    "And he makes his way over, pretty much coming to my rescue."
    show jack smile at center with ease
    jack.say "Oh, there you are, [hero.name]!"
    jack.say "I was starting to think that you'd stood me up!"
    bree.say "I thought you'd done the same to me, Jack!"
    bree.say "We were supposed to be meeting outside."
    show jack normal
    show fx drop
    "An awkward smile spreads across Jack's face."
    "And he offers me a shrug in way of explanation."
    jack.say "Sorry, [hero.name]..."
    jack.say "This place is like a second home to me."
    hide fx
    jack.say "I turned up early and tried to wait outside, just like you said."
    jack.say "But I couldn't resist coming inside and checking out the new arrivals!"
    "I'm about to say something in response when I realise something."
    "A quick glance around the store confirms my suspicions."
    bree.say "Erm..."
    bree.say "Jack..."
    bree.say "Why is everyone staring at me?"
    bree.say "Is it like, because I'm a girl?"
    "Jack looks at me for a moment."
    show jack happy at startle
    "And then he bursts out laughing."
    "Which makes me cross my arms over my chest and frown."
    bree.say "What's so funny about that, Jack?"
    bree.say "Aren't these places supposed to be full of nerdy, awkward guys?"
    show jack normal
    jack.say "Oh, [hero.name]!"
    jack.say "This is the twenty-first century."
    show jack smile
    jack.say "There are nerdy, awkward girls in here too!"
    "I look around in amazement, not believing what I'm hearing."
    bree.say "There are?"
    bree.say "Because they don't look like girls to me!"
    "Jack doesn't hear my comment."
    "Or else he chooses to ignore it."
    show jack normal
    jack.say "No, [hero.name]..."
    jack.say "The reason they're staring is because you're a cute girl."
    bree.say "Really?"
    jack.say "Yeah, afraid so!"
    jack.say "But cut them some slack, maybe?"
    jack.say "They already dealt with the trauma of girls coming in here."
    jack.say "You can't expect them to become sexually liberated straight after that."
    bree.say "Wait a minute..."
    bree.say "Weren't we talking about you not being here on time?"
    jack.say "Well..."
    jack.say "Technically I was here on time."
    show jack happy
    jack.say "I was just on the wrong side of the door!"
    menu:
        "Tell him he's technically correct":
            "I don't feel like having an argument with Jack over something so petty."
            "Plus we're only just at the start of our date and there's an audience too."
            "So I decide to make a joke out of it instead, using humour as a defence."
            show jack normal
            bree.say "Jack, you are TECHNICALLY correct."
            bree.say "The best kind of correct there is!"
            show jack smile at startle
            "Jack stares at me in surprise for a moment."
            show jack happy
            $ game.active_date.score += 15
            "And then a huge smile spreads across his face."
            jack.say "Oh man..."
            jack.say "I love that show!"
            jack.say "[mike.name] and I used to quote it at each other for hours!"
            bree.say "Yeah..."
            bree.say "Now why doesn't that surprise me?"
            show jack normal
            jack.say "Huh?"
            bree.say "I said that we should get down to it."
            bree.say "Get some serious gaming in, yeah?"
            show jack happy
            "Jack nods happily and gestures towards the table."
        "Let it slide, for now...":
            "I don't feel like having an argument with Jack over something so petty."
            "Plus we're only just at the start of our date and there's an audience too."
            "So I just shrug my shoulders and decide to let it go."
            show jack normal
            bree.say "Okay, Jack..."
            bree.say "I guess it's no big deal."
            bree.say "One of us would have noticed the other soon enough."
            bree.say "Now...shall we get on with it?"
            "Jack nods in agreement."
            $ game.active_date.score -= 10
            "But I can see that he seems a little crest-fallen."
            "I'm not sure what that should be, as I let him off this time."
            "But then it occurs to me that maybe that's the problem."
            "Letting him off means that he's not having to defend himself."
            "And instead he's got the room to think about what happened."
            "I can't do anything about it now."
            "But I make a mental note to be more careful in the future."
            "Sometimes trying to smooth over things can actually make it worse!"
    scene bg gamestore at center, zoomAt (1.5, (960, 720))
    show jack blush at center, zoomAt (1.25, (640, 840))
    with fade
    "As we get to the table, I can see that Jack's watching me closely."
    "Almost like he still can't believe that I'm actually doing this."
    bree.say "You can stop looking at me like that, Jack."
    bree.say "You're not dreaming, yeah?"
    show jack normal
    show fx exclamation
    "Jack shakes his head."
    jack.say "I'm sorry, [hero.name]."
    jack.say "It's just still a little weird to be doing this with you."
    jack.say "I mean, I know you're a gamer and all that."
    jack.say "But I never thought you'd try Battlemallet!"
    menu:
        "Tell you're intrigued by the game":
            bree.say "Why the hell not, Jack?"
            bree.say "I mean, I just love fantasy movies."
            bree.say "And I've played a ton of RPGs on the Zbox."
            bree.say "Plus I always hear you and [mike.name] talking about it."
            bree.say "So I wanted to see what all the fuss was about for myself."
            show jack smile
            $ game.active_date.score += 15
            "I can see Jack getting more enthusiastic all the time I'm talking."
            "And as I explain myself and my interest, his eyes almost start to glow."
            "It's like he can't actually believe his luck."
            "He's on a date with a girl that's asking him to explain his favourite wargame."
            "I don't think he could have imagined the scenario in a million years!"
            jack.say "Oh man..."
            jack.say "You're going to love it, [hero.name]!"
            jack.say "It's like all of those things you mentioned."
            show jack happy
            jack.say "But better!"
        "Tell you try it to get closer to him":
            bree.say "Well, I might not have tried it normally."
            bree.say "But you and [mike.name] are always talking about it."
            bree.say "So I figured it was a good way for us to get closer."
            show jack sad
            "Jack nods."
            "But I can see that he looks a little concerned."
            $ game.active_date.score -= 10
            show fx drop
            jack.say "Oh..."
            jack.say "That's cool, [hero.name]."
            bree.say "What's the matter, Jack?"
            bree.say "I thought you'd be happy I was interested in your game?"
            hide fx
            show jack smile
            jack.say "I am, [hero.name], I am."
            show jack normal
            jack.say "It's just most people play Battlemallet because it's so cool."
            jack.say "But what you said is a good reason too."
            "I get the feeling Jack's worried that I'm just humouring him."
            "That I'm not really interested in the game at all."
            "So I'm just going to have to try harder to convince him, that's all!"
    show jack normal
    "I take a moment to look over the table we're going to be playing on."
    "And I have to say that I'm more than a little impressed by what I see."
    "It's filled with miniature buildings and trees, all crazily detailed."
    "And if reminds me of those model villages people build as tourist attractions."
    jack.say "Okay..."
    jack.say "Let's get our armies on the table!"
    "Jack reaches down and picks up a case from the side of the table."
    "He pops open the clasps on it and reveals foam padding inside."
    "Then he starts plucking brightly-painted little men out of it."
    "I watch as he arranges them carefully on the table."
    bree.say "Wow, Jack..."
    bree.say "Those look amazing!"
    menu:
        "Ask who painted the army for him":
            bree.say "Who painted all of those for you?"
            "As soon as I utter the words, I regret it."
            show jack angry
            show fx anger
            "Jack looks up at me, a frown on his face."
            jack.say "What do you mean, who painted them FOR me?"
            hide fx
            bree.say "Ah..."
            bree.say "I just wanted to know, Jack?"
            bree.say "There's so many of them and the painting is so good."
            bree.say "Whoever did it must be really good!"
            show jack sad
            jack.say "What, you don't think that I could have painted them myself?"
            "Suddenly I can see what the problem is."
            "And I hurry to do all I can to rectify my mistake."
            bree.say "You painted them yourself?"
            bree.say "That's great, Jack!"
            $ game.active_date.score -= 10
            show fx anger
            jack.say "Yeah, but you made it sound like you didn't think it could be me!"
            bree.say "I didn't mean it like that, Jack!"
            hide fx
            jack.say "Okay, [hero.name], okay..."
            jack.say "Let's just forget about it and play the game..."
        "Ask if he painted the army himself":
            bree.say "Did you paint all of these yourself?"
            "I look up to see Jack visibly inflating with pride."
            "He does the best he can to seem nonchalant."
            "But it's plain to see that he's happy to be praised."
            $ game.active_date.score += 15
            show jack perv
            jack.say "Oh these?"
            jack.say "These are my orcs."
            jack.say "And yeah, [hero.name]..."
            jack.say "I painted all of them myself."
            "It's hard not to laugh as Jack basks in my praise."
            "He's like a little kid getting patted on the head."
            "But I'm not pretending to be impressed."
            "The job he's done on them really is good."
            "And I can see other people in the store checking them out too."
            show jack smile
            jack.say "I can give you some pointers if you like?"
            jack.say "Maybe even a few painting lessons?"
            bree.say "You know what, Jack..."
            bree.say "I might just take you up on that offer."
    show jack normal
    "Now that Jack's got his guys on the table, he glances over to me."
    jack.say "Where's your army, [hero.name]?"
    jack.say "You're going to need one for the game!"
    if randint(0, 1) == 0:
        "I take that as my cue to explain myself."
        "And so I take a deep breath and go for it."
        if hero.has_skill("work"):
            bree.say "You're going to have to help me out with the rules, Jack."
            bree.say "Because I was up all night getting these ready..."
            "I choose that moment to produce my own case and pop it open."
            show jack surprised at startle
            "But as I take the models out of it, Jack's eyes pop open too!"
            show fx exclamation
            jack.say "[hero.name]..."
            jack.say "Those are..."
            hide fx
            bree.say "Elves?"
            "Jack shakes his head in disbelief."
            show jack smile
            jack.say "Those are frickin beautiful!"
            jack.say "Did you do all of this yourself?!?"
            "I nod and smile, rolling my eyes in embarrassment."
            bree.say "Well..."
            bree.say "I am kind of obsessive about stuff like this."
            bree.say "So I wanted to have a nice army to play with."
            bree.say "But like I said, I didn't read up on the rules!"
            show jack normal
            "Jack's still shaking his head."
            "But now it's to dismiss my concerns."
            jack.say "Don't worry about that, [hero.name]."
            jack.say "I'll walk you through it."
            jack.say "Damn..."
            $ game.active_date.score += 15
            show jack happy
            jack.say "I'd do the whole thing for you, just to play against these guys!"
        else:
            bree.say "Thing is, Jack..."
            bree.say "I kinda don't have an army!"
            "All I can do is shrug and smile."
            "Hoping that Jack will see the funny side."
            show fx question
            jack.say "You don't?"
            jack.say "Why's that, [hero.name]?"
            hide fx
            bree.say "Well..."
            bree.say "[mike.name] lent me his copy of the rules."
            bree.say "So that I could prepare for the game."
            bree.say "And back in school, I was always the kid that crammed the night before the test!"
            "Jack nods, like he understands me completely."
            bree.say "So I spent all my time learning the rules."
            bree.say "And I totally forgot to get an army!"
            "Jack still looks a little flustered by this."
            "But he nods his head all the same."
            jack.say "Don't worry, [hero.name]."
            jack.say "You can borrow one of the store's armies."
            jack.say "Just let me go and ask for one..."
            hide jack with easeoutright
            "Jack disappears for a moment, leaving me alone."
            show jack at center, zoomAt (1.25, (640, 840)) with easeinright
            "Then he returns with what looks like a case full of elves."
            jack.say "There you go, [hero.name]."
            jack.say "If you memorised the rules, you should know how to use these."
    else:
        "It's pretty obvious that I don't have an army of my own."
        "But I remember there was a way for me to get round needing one."
        "I either read something or heard something about it."
        "But what was it..."
        if hero.knowledge >= 50:
            "Oh yeah..."
            "Now I remember!"
            bree.say "I checked up on the store's website last night."
            bree.say "Don't they have armies that you can borrow?"
            bree.say "For people wanting to play without armies of their own?"
            show fx exclamation
            "Jack stares at me for a moment."
            "But then he nods his head."
            "And I can see that he's impressed."
            hide fx
            show jack happy
            $ game.active_date.score += 15
            jack.say "Wow, [hero.name]..."
            jack.say "You've really done your homework."
            show jack smile
            jack.say "That means you'll probably be a great Battlemallet player too."
            bree.say "It does?"
            jack.say "Oh yeah!"
            jack.say "Battlemallet's a game that demands commitment and dedication."
            jack.say "You can't just muddle through it."
            show jack normal
            jack.say "You need to be organised!"
            "Sure, I know that all I just did was impress Jack over a game."
            "But I can still feel a real measure of pride welling up inside of me."
        else:
            bree.say "Erm..."
            bree.say "No, Jack..."
            bree.say "I don't have an army!"
            "All the time I'm saying this, I'm racking my brain."
            "But no matter how hard I try, I can't think of the answer."
            "So I just end up shrugging helplessly at Jack."
            $ game.active_date.score -= 10
            "He looks a little put out by my clueless reaction."
            "But he nods his head all the same."
            jack.say "Don't worry, [hero.name]."
            jack.say "You can borrow one of the store's armies."
            jack.say "Just let me go and ask for one..."
            hide jack with easeoutright
            "Jack disappears for a moment, leaving me alone."
            show jack at center, zoomAt (1.25, (640, 840)) with easeinright
            "Then he returns with what looks like a case full of elves."
            jack.say "There you go, [hero.name]."
            jack.say "But maybe put a little more effort in next time?"
            jack.say "Battlemallet's not a game you can just muddle your way through."
            jack.say "You need to be organised!"
            "I can feel my cheeks burning as I take the models from Jack."
            "But I do the best I can to forget about it and concentrate on the game instead."
    "Now it's my turn to arrange my models on the table."
    "Jack gives me some pointers as I choose where to put them."
    "And once that's done, we're almost ready to play the game."
    show jack smile
    jack.say "Okay, [hero.name]..."
    jack.say "Seeing as you're the noob, you can go first."
    show jack normal
    "I nod and reach for the dice, already thinking up my first move."
    bree.say "Okay, Jack..."
    bree.say "Prepare to be put to the sword!"
    "And just like that, we're into it - I'm playing my first game of Battlemallet!"
    "I don't know if it's Jack's enthusiasm or my own genuine enjoyment."


    "But it doesn't take long for me to be totally engrossed in the game."
    "Jack and I are going back and forth, battling it out across the table."
    "And I'm as invested in this thing as I've ever been in a video-game."


    "I'm killing his orcs off one moment, the next he's slaughtering my elves."
    if randint(0, 1) == 0:
        "I'm really doing it!"
        "I'm playing Battlemallet with Jack!"
        if randint(1, 10) == 10:
            "I'm sure that I've got the rules memorised."
            "And I've studied the table pretty well too."
            "So I'm feeling confident as we go into the game."
            "Soon enough, Jack and I are locked in mortal conflict!"
            "I'm trying to make sure that my tactics are working."
            "And at the same time keep an eye on Jack's too."
            "And for a while the game seems to be a pretty even match."
            "But little by little, I seem to be inching ahead."
            "I can feel the thrill of victory being within my grasp."
            "And it all comes down to one last roll of the dice."


            "And once he sees the numbers that come up, I can't contain myself any longer."
            bree.say "YES!"
            bree.say "I did it!"
            bree.say "I won!"
            bree.say "Kiss my..."
            bree.say "Oops..."
            bree.say "Sorry, Jack!"
            show jack smile
            "Jack shakes his head with a smile."
            jack.say "It's okay, [hero.name]."
            show jack happy
            jack.say "You won the game fair and square."
            $ game.active_date.score += 5
            show jack normal
            jack.say "Well done."
        else:
            "I'm doing the best I can to remember all of the rules."
            "At the same time I'm also trying to keep an eye on my tactics too."
            "Oh, and add to that making predictions as to what Jack's up to."
            "And for a while the game seems to be a pretty even match."
            "But little by little, Jack seem to be inching ahead."
            "Sure, he's doing the best he can to be humble about it."
            "But I can see that there's a smile on his face as he rolls the dice."


            "And once he sees the numbers that come up, he can't contain himself any longer."
            show jack happy
            jack.say "YES!"
            jack.say "That's it!"
            jack.say "I win!"
            jack.say "Stick it up your..."
            show jack blush
            jack.say "Oops..."
            jack.say "Sorry, [hero.name]!"
            show jack normal
            "I can't help smiling."
            "And I make sure to shake my head as well."
            bree.say "It's okay, Jack."
            bree.say "You won the game fair and square."
            $ game.active_date.score += 15
            bree.say "Well done."
    else:
        "I'm sure that I've read up on the rules and remembered them."
        "And I know that I checked out all of the terrain on the table."
        "But somehow I just can't seem to get into the game."
        "Everything I try, Jack has an answer for it."
        "Or else I just keep getting it wrong myself."
        "Pretty soon it's looking like Jack's going to walk away with the victory."
        "And the only chance I have is to throw all of my forces into one last attack."
        "It all comes down to this one last roll."
        "Either I get the number I want, or else Jack wipes me out!"
        if hero.luck >= 1:
            "I hold my breath and throw the dice."


            "And everything seems to pause as it bounces onto the table."
            "I stare at the dice, trying to see what I rolled..."
            bree.say "Oh my god!"
            bree.say "I did it!"
            bree.say "I actually did it!"
            show jack surprised
            "Jack leans over and looks at the dice."
            $ game.active_date.score -= 5
            "Then he sucks his teeth and shakes his head."
            show fx drop
            jack.say "Wow!"
            jack.say "I can't believe it!"
            jack.say "You actually made the roll."
            hide fx
            "I do the best I can to stay humble."
            "But I can't keep the smile off my face."
            bree.say "I just got lucky, Jack."
            bree.say "That's all."
        else:
            "I hold my breath and throw the dice."


            "And everything seems to pause as it bounces onto the table."
            "I stare at the dice, trying to see what I rolled..."
            bree.say "Oh no!"
            bree.say "Dammit!"
            bree.say "I was so close too..."
            "Jack leans over and looks at the dice."
            "Then he sucks his teeth and shakes his head."
            show fx drop
            jack.say "Ouch!"
            jack.say "Sorry, [hero.name]."
            "I can't help smiling."
            "And I make sure to shake my head as well."
            hide fx
            bree.say "It's okay, Jack."
            bree.say "You won the game fair and square."
            $ game.active_date.score += 5
            bree.say "Well done."
    show jack normal with fade
    "Once the game is over, we pack away the models in their cases."
    "Then Jack and I leave the table for the next couple of players."
    jack.say "So, [hero.name]..."
    jack.say "You know it's my birthday and all that..."
    bree.say "Yeah, Jack."
    jack.say "Well..."
    show jack blush
    jack.say "Did you happen to have something for me?"
    if not hero.has_gifts:
        "Oh no!"
        "I spent so much time trying to get ready for the game."
        "I totally forgot about getting something for Jack!"
        bree.say "Erm..."
        bree.say "No, Jack..."
        bree.say "Me learning to play the game was the gift!"
        show jack normal
        jack.say "Oh..."
        jack.say "Okay, [hero.name]."
        $ game.active_date.score -= 20
        jack.say "No problem."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_20
        if _return != "done":
            if _return not in ["None", "exit"]:
                bree.say "Oh yeah!"
                bree.say "I almost forgot!"
                bree.say "Here you go, Jack."
                show jack smile
                "I pull out the gift and hand it over to Jack."
                play sound [paper_ripping_1, paper_ripping_2]
                "He grins like a kid and begins to tear it open."
                if _return:
                    show jack at startle
                    "But when he sees what's inside, Jack gasps in amazement."
                    bree.say "What's up, Jack?"
                    bree.say "Is something wrong?"
                    jack.say "How did you know, [hero.name]?"
                    show jack happy
                    $ game.active_date.score += 15
                    jack.say "How did you know this was what I wanted?!?"
                    bree.say "Oh, I don't know, Jack."
                    bree.say "I just listened out for clues, I guess!"
                else:
                    show jack normal
                    show fx drop
                    "But when he sees what's inside, his face falls."
                    bree.say "What's up, Jack?"
                    bree.say "Is something wrong?"
                    jack.say "Ah..."
                    jack.say "No, [hero.name]."
                    hide fx
                    $ game.active_date.score -= 10
                    jack.say "It's great...I guess."
            else:
                "Oh no!"
                "I spent so much time trying to get ready for the game."
                "I totally forgot about getting something for Jack!"
                bree.say "Erm..."
                bree.say "No, Jack..."
                bree.say "Me learning to play the game was the gift!"
                show jack surprised
                jack.say "Oh..."
                show jack normal
                jack.say "Okay, [hero.name]."
                $ game.active_date.score -= 20
                jack.say "No problem."
    "With the game over, there's really nothing to keep us in the games-store."
    "So Jack and I walk over to the door and head outside."
    scene bg street
    show jack
    with fade
    "Which leaves us standing on the sidewalk."
    bree.say "I had a great time today, Jack."
    bree.say "I loved trying something new with you."
    bree.say "I hope you had a good time too?"
    if game.active_date.score >= 80 and jack.sexperience >= 1:
        "Jack starts nodding his head like crazy."
        "So much so that I'm worried it'll drop off!"
        show jack smile
        jack.say "Yeah, [hero.name]..."
        jack.say "I had the best time ever!"
        show jack normal
        jack.say "You wanna do something else?"
        jack.say "Maybe go somewhere else?"
        "I'm left with my mouth hanging open as Jack asks this."
        "Because I was just about to ask him the same thing."
        "I shake my head, trying to recover from the surprise."
        bree.say "Sure, Jack..."
        bree.say "That sounds like a great idea!"
        bree.say "I'm sure we can think of something fun to do."
        show jack close blush
        "I wrap my arm in Jack's."
        "And together we walk off down the street."
        "Swapping war stories from our game as we go."
        call jack_birthday_sex_female from _call_jack_birthday_sex_female
    else:
        "Jack smiles, but it looks a little forced to me."
        jack.say "I'm glad you enjoyed yourself, [hero.name]."
        jack.say "But I get worn out teaching the game to newbies."
        "He stretches and lets out a yawn."
        "As if he needs to prove what he's saying."
        jack.say "So I could do with chilling out, you know?"
        "I nod and take an instinctive step away from Jack."
        bree.say "Oh..."
        bree.say "Okay, Jack..."
        bree.say "I mean, I was going to ask..."
        bree.say "Maybe if you wanted to do something else?"
        bree.say "You know?"
        "Jack shakes his head, shutting me down."
        jack.say "Maybe another time, [hero.name]."
        show jack wink
        jack.say "Call me, yeah?"
        hide jack with easeoutright
        "I nod as I watch Jack turn and walk away."
        "Which leaves me wondering if I did something wrong."
    return

label jack_birthday_sex_female:
    "I thought about suggesting that Jack take me back to his place after the games-store."
    "But then it occurred to me that I have no idea if he lives alone or with housemates."
    "Hell, he's a nerdy guy that plays wargames in his spare time."
    "So he could even still be living in his parent's basement for all I know!"
    "And just suggesting him taking me home could send him into a state of blind panic."
    "So I decide that the best thing is to just take him back to my place."
    scene bg black with dissolve
    scene bg house
    show jack sad
    with wiperight
    bree.say "Okay, Jack..."
    bree.say "Here we are."
    "I'm just unlocking the door."
    "And I take a moment to look back over my shoulder."
    "I'm expecting to see Jack ready to follow me inside."
    "But instead he's standing a little way off."
    "And he's looking pretty nervous too."
    bree.say "What's the matter, Jack?"
    bree.say "Do I smell bad or something?"
    show jack normal at center, zoomAt (1.25, (640, 840))
    "Jack shakes his head as he comes a little closer."
    jack.say "Erm..."
    jack.say "You don't know if [mike.name]'s in, do you?"
    jack.say "I'm kind of worried about bumping into him!"
    "I push the door open and frown at Jack."
    bree.say "Why would you be afraid of that?"
    bree.say "I thought you two were friends?"
    "Jack scuttles over and then in through the door."
    "All the time he's still glancing around."
    scene bg livingroom
    show jack at center, zoomAt (1.25, (940, 840))
    with fade
    jack.say "We are, [hero.name]."
    show jack sad
    jack.say "I just don't like the idea of him seeing me with you!"
    jack.say "Like he might be mad with me or something!"
    show jack at center, zoomAt (1.25, (640, 840)) with ease
    "I'm shaking my head as I close the door behind us."
    "Because I can't make sense of what Jack's saying."
    bree.say "What's it got to do with him?"
    bree.say "I can see whoever I want."
    bree.say "And so can you."
    show jack normal
    "Now that we're inside, Jack seems to be calming down a little."
    "He's looking at me instead of all around him."
    "And he actually manages to give me a decent answer."
    jack.say "I know that, [hero.name]."
    jack.say "It's just that I'm not used to being the one with a girlfriend."
    jack.say "I usually bump into [mike.name] when he's on a date with a hot girl."
    "I can't help letting out a giggle at this."
    show jack at center, zoomAt (1.5, (640, 1040))
    "And then I plant a kiss on Jack's lips."
    show jack surprised at startle
    jack.say "Wow, [hero.name]..."
    jack.say "Why did you kiss me?"
    show jack smile
    jack.say "I was just admitting to being a loser!"
    bree.say "Really?"
    bree.say "All I heard was you calling me a hot girl!"
    "With that, I take hold of Jack's hand."
    "And I lead him up the stairs to my bedroom."
    scene bg secondfloor with fade
    "I'm still having to lead Jack as we walk into my room."
    "Not that I'm dragging him along, as he's coming willingly."
    "He seems to be over the spell of nerves he had when we got here."
    "Now it's more like he's in a kind of daze at what's happening to him."
    scene bg bedroom2
    show jack at center, zoomAt (1.5, (640, 1040))
    with fade
    jack.say "This is really happening to me!"
    jack.say "I'm really in your room!"
    "Jack's looking this way and that as I walk him over to my bed."
    scene bg bedroom2 at center, zoomAt (1.75, (1080, 820))
    show jack at vshake, center, zoomAt (1.25, (440, 940))
    "Which means he's not ready for it when I shove him down onto it."
    jack.say "Whoa..."
    jack.say "Oh...okay, [hero.name]..."
    jack.say "I think I like where this is going!"
    "I nod and treat Jack to a slow, sensuous smile."
    bree.say "Take off your clothes, Jack."
    jack.say "W...why, [hero.name]?"
    bree.say "Because I'm going to take mine off right now."
    bree.say "And what I'm going to do to you next..."
    bree.say "Well, it'll be a lot easier if you're naked!"
    show jack blush
    "Jack's eyes go wide at this, and he nods eagerly."
    "Then he scrambles to pull off his clothes."
    "But it's not like he does it with ease."
    "In fact he's so flustered that he seems to forget how to do it!"
    show jack angry at hshake, center, zoomAt (1.25, (440, 940))
    "He ends up rolling around on the bed, like he's wrestling himself."
    "At the same time I start to strip off my own clothes."
    "But I manage to make it a more dignified affair."
    show jack smile
    "In fact Jack slows right down as he watches me."
    "Finally coming to a complete stop halfway out of his clothes."
    "I know it sounds bad to admit this."
    "And you could argue that I'm kind of exploiting Jack here."
    "But I can't help getting off on the way that he's looking at me right now."
    "Most guys are pretty open about checking a girl like me out."
    "Some even act all entitled when you show interest in them."
    "You know, like they're sure you were going to be into them?"
    "And they're almost doing you a favour by returning the attention."
    "But with Jack, I can see that he's sitting there entranced."
    "Nothing that I do is being taken for granted."
    "I know that he thinks he's the luckiest guy in the world right now."
    "And you can't tell me that's not a turn-on for a girl."
    "Sure, you can pop for a hot body or the face of a movie-star."
    "But I'll take knowing that a guy likes me for me over those things any time."
    "As I get closer to the bed and closer to being naked, I realise something."
    "Before now I thought that Jack was totally frozen to the spot."
    "But as I get nearer, I notice that he's moving in sympathy with me."
    "As I lower myself onto the bed, he leans backwards to make room."
    "And as I climb onto the mattress, his hands reach up to meet me."
    "It's like neither of us has to say a word, we just move together."
    show jack naked with dissolve
    "In this way we pull off the last of his clothes."
    "And I climb atop Jack as he lays down on the bed."
    show jack at center, zoomAt (1.5, (640, 1040))
    "But as much as we seem to be synchronized, some things still come as a surprise."
    "Such as the moment I reach down and take a firm hold of his cock."
    show jack blush
    "Jack gasps, his eyes going wide at the sensation."
    "Yet he does nothing to pull away."
    "Which lets me know that I'm getting it right."
    "I can tell that Jack was already pretty hard before."
    "And so it doesn't take much effort to take him all the way."
    hide jack
    show jack cowgirl pleasure
    with fade
    "I do this by lowering myself until we're touching down there."
    "Sure, his eyes are still wide and he looks almost overwhelmed."
    "But I can't keep up the act of being all superior and in control."
    "When I feel the head of Jack's cock against my lips..."
    bree.say "Mmm..."
    bree.say "Jack..."
    bree.say "I want this inside me..."
    bree.say "I want it so badly!"
    "Jack nods his head, as if he needs to tell let me know it's okay."
    "But from the look on his face, there's no way he could speak the words."
    show jack cowgirl hurt
    "And a second later, as the inevitable happens, his eyes roll back into his head."
    "The truth is that I know how he's feeling."
    "My body surrenders slowly, meaning that he slides into me slowly."
    show jack cowgirl pleasure
    "And it feels like forever before he's as deep as he can go."
    "Until then, I'm happy to let the experience remain passive."
    "But after a short pause, I feel the urge to take control."
    "Jack stays laid back on the bed, pinned beneath me."
    show jack cowgirl normal bounce
    "And I take advantage of this, beginning to ride him in earnest."
    "It doesn't take me long to pick up speed either."
    "Now that I have Jack exactly where I want him, I don't hold back."
    "I know that I could slow down and make this into a sensual experience."
    "But part of me knows that's not going to happen this time."
    "Now that I have him inside of me, I'm the one in control."
    "And on this occasion, what I want is to be fucked."
    show jack cowgirl pleasure enjoying
    "And to be fucked hard."
    "At first, Jack seems happy to remain the passive partner."
    "My thighs are pushing down on him, making him sink into the mattress."
    "But soon the temptation becomes too much for him."
    show jack cowgirl cuddle normal
    "That's when I feel his hands begin to move over my body."
    "He doesn't try to take hold of me or control what we're doing."
    "Instead he simply explores me the whole time."
    "One moment his hands are gentle, touching me softly."
    "The next he comes across my belly, then wanders up to my breasts."
    "I gasp at the sensation of his hands on them."
    "And hearing this, Jack pauses, probably afraid of overstepping the mark."
    show jack cowgirl resting -cuddle
    "Almost desperate to assure him he hasn't, I put my hands over his."
    "Pressing them harder against my breasts, I nod."
    show jack cowgirl suck dazed
    "Jack seems to get the message, as I feel him squeeze them."
    "And this time it's harder than before."
    show jack cowgirl enjoying
    "The sensation floods my body, making me ride him harder still."
    jack.say "Ugh..."
    show jack cowgirl cuddle pleasure
    jack.say "[hero.name]!"
    "That's all Jack manages to say before I feel it happen."
    show jack cowgirl ahegao with vpunch
    $ jack.sexperience += 1
    "He lets go when he's all the way inside of me."
    with vpunch
    "And I feel my senses struggle to cope with the feeling."
    with vpunch
    "My orgasm comes on the heels of his, impossible to stop."
    show jack cowgirl resting pleasure
    "I lie down atop Jack, clinging onto him as it happens."
    "And once it's over, neither of us moves a muscle."
    "All we can do is lie there, exhausted and overwhelmed."
    return

label jack_preg_talk:
    $ jack.flags.toldpreg = True
    $ jack.flags.know_is_father = True
    show jack
    "Jack can be like a big kid at the best of times, not able to deal with adult issues."
    "So you can imagine how hard it's been to make myself stand in front of him and say it."
    "But I really can't think of any other way to tell him the news, as it's that big."
    bree.say "Jack..."
    bree.say "I have something I need to tell you..."
    "Jack's head snaps around at the sound of my voice."
    show jack sad
    "But then his face falls when he gets a handle on the tone of it too."
    jack.say "Ah, [hero.name]..."
    jack.say "I don't know what you have to say."
    jack.say "But it sounds pretty heavy!"
    "I can't help letting out a weary sigh."
    "As I know that this isn't going to be easy for either of us."
    bree.say "Yeah, Jack..."
    bree.say "This is going to suck..."
    bree.say "I'm kind of pregnant!"
    jack.say "Y...you're kinda pregnant?"
    bree.say "Well, no...I'm more like very definitely pregnant, Jack!"
    bree.say "I took a test and everything."
    bree.say "So the chances are that I really am."
    "Jack looks off into the distance, his eyes kind of glazed over."
    "He puffs his cheeks up and then lets out the breath in one long exhale."
    "All the time I'm watching him, getting more nervous each passing second."
    "I kind of expected Jack to freak out when I told him."
    "I thought I was prepared for fear and panic."
    "But silence wasn't something I could have predicted on his part."
    bree.say "Erm..."
    bree.say "Jack..."
    bree.say "Are you okay?"
    "Jack turns to look at me suddenly."
    "In fact it's so quick I kind of flinch."
    "His eyes are wide, maybe even a little crazy."
    "But he also looks like he's come to some kind of decision."
    if jack.love >= 150:
        show jack smile
        jack.say "This is like one of those movies, [hero.name]!"
        bree.say "Huh?"
        bree.say "Jack, what are you talking about?"
        bree.say "I just told you I'm pregnant - and you're the father!"
        jack.say "Well...actually you didn't, [hero.name]."
        jack.say "I just kind of assumed that part."
        jack.say "Otherwise you choosing to tell me would have been pretty weird!"
        "I shake my head as Jack starts to confuse me even more."
        bree.say "I...I thought you were talking about movies?"
        jack.say "Oh yeah!"
        jack.say "It's like those movies where the guy's a screw-up, don't you see?"
        jack.say "And he has to muddle through with the kid and responsibility."
        jack.say "But he makes out good in the end, and it all turns out great!"
        "I stare blankly at Jack, still not getting what he means."
        bree.say "Okay...okay..."
        bree.say "Me [hero.name]...you Jack."
        bree.say "[hero.name] and Jack do it many times."
        bree.say "[hero.name] and Jack make baby - understand?"
        show jack normal
        "Jack nods eagerly."
        jack.say "Shit..."
        jack.say "Sorry, [hero.name] - I got carried away there!"
        jack.say "I just think this is so great!"
        bree.say "Y...you do?!?"
        show jack happy
        "Jack beams at me."
        jack.say "Of course I do, [hero.name]!"
        jack.say "We're going to be parents!"
        jack.say "And I can't wait!"
        "All I can do is smile weakly and nod."
        "I think that was the answer I wanted."
        "But Jack's kind of got me in a state where I can't be sure!"
    else:
        jack.say "I'm sorry, [hero.name]..."
        jack.say "I'm so frikin sorry!"
        bree.say "Ah...okay, Jack."
        bree.say "But we kind of did this together, you know?"
        bree.say "So there's no need to apologise to me!"
        "Jack shakes his head at this."
        "And I start to realise that I've misunderstood."
        jack.say "No, [hero.name], no!"
        jack.say "I mean I'm sorry because I can't do this."
        jack.say "I can't be a father."
        jack.say "I'm just not parent-material!"
        "I force a weak smile onto my face."
        "As I'm still trying to salvage something from this mess."
        bree.say "You know what, Jack..."
        bree.say "I don't think anyone sees themselves as parent-material."
        bree.say "At least not in the beginning."
        bree.say "But people kind of grow into the role, yeah?"
        bree.say "And they end up surprising themselves!"
        "Jack starts to back away from me."
        "He's shaking his head as he does so."
        "And he holds out his hands to ward me off."
        jack.say "Oh no..."
        jack.say "I'm not listening, [hero.name]."
        jack.say "You're trying to use psychology on me - but it won't work!"
        "With that, her turns on his heel and runs away."
        "And by that, I mean he literally runs away!"
        "Pretty much letting me know that I'm on my own this time."
        $ jack.breakup()
    return

label jack_find_out_pregnancy:
    $ jack.flags.toldpreg = True
    show jack normal
    "Jack keeps shooting sideways glances in my direction."
    "And every time I look up, he turns away like's been caught out."
    "This goes on for quite a while, and it's starting to get annoying."
    show jack at center, zoomAt(1.5, (640, 1040))
    "But then he surprises me by actually plucking up the courage to ask a question."
    jack.say "Erm..."
    jack.say "[hero.name]..."
    bree.say "Yes, Jack?"
    jack.say "This is kind of a personal question..."
    jack.say "And you don't have to answer it..."
    jack.say "But...are you pregnant?"
    "The question actually comes as a relief."
    "As I'd been waiting for the right time to tell him."
    "And this seems as the perfect opportunity."
    bree.say "You got me, Jack..."
    bree.say "I'm pregnant."
    show jack surprised
    "Jack's eyes go so wide I think they're going to pop out of his head!"
    bree.say "But wait..."
    bree.say "There's more!"
    menu:
        "It's yours":
            $ jack.flags.know_is_father = True
            bree.say "You're the father, Jack!"
            bree.say "I'm having your baby!"
            "If Jack looked surprised before, now I think he's going to faint!"
            if jack.love >= 160:
                jack.say "P...P...Pregnant?"
                jack.say "F...F...Father?"
                "Now I'm really starting to get worried about Jack."
                "He's stammering and starting."
                "And I'm almost ready to try to catch him when he finally goes."
                "But then something seems to click inside of his head."
                show jack happy
                "And a huge smile spreads over his face."
                jack.say "That's great, [hero.name]!"
                jack.say "That's like the best news ever!"
                bree.say "It is?"
                bree.say "You really mean that?"
                "Jack nods eagerly."
                show jack smile
                jack.say "[hero.name], I never thought this would happen to me."
                jack.say "Not only am I dating the hottest chick in the world..."
                jack.say "But we're gonna have a baby together too!"
                "Whoa..."
                "Hottest chick in the world?"
                "Is he serious?"
                "No...wait...I need to focus here!"
                bree.say "So you're...happy?"
                jack.say "I've never been happier, [hero.name]!"
                jack.say "Let's start planning for when they get here..."
                jack.say "Right now!"
            else:
                jack.say "P...P...Pregnant?"
                jack.say "F...F...Father?"
                "Now I'm really starting to get worried about Jack."
                "He's stammering and starting."
                "And I'm almost ready to try to catch him when he finally goes."
                "But then something seems to click inside of his head."
                "And a look of horror spreads over his face."
                if jack.love >= 150:
                    bree.say "Jack..."
                    bree.say "Are you okay?"
                    jack.say "Y...yeah, [hero.name]..."
                    jack.say "Or at least I will be."
                    jack.say "I need some time to get my head around this!"
                    bree.say "Wait..."
                    bree.say "We need to talk about this!"
                    jack.say "We will, we will..."
                    jack.say "Just not right now!"
                    "I nod as Jack turns his back on me and walks away."
                    "I guess he just needs some space right now."
                    "And at least he didn't run away screaming!"
                else:
                    jack.say "No..."
                    jack.say "Oh no...no way!"
                    jack.say "I can't be a father..."
                    jack.say "I'm too young!"
                    jack.say "And there are so many action figures I don't own yet!"
                    bree.say "Wait..."
                    bree.say "We need to talk about this!"
                    "But it looks like I'm too late."
                    hide jack
                    show jack sad
                    "Jack lurches backwards, almost falling on his face."
                    hide jack with easeoutright
                    "Then he turns his back and runs away."
                    "He literally runs away from me!"
                    "So maybe he was right when he said he couldn't be a father?"
                    $ jack.set_gone_forever()
        "It's not yours":
            bree.say "You're not the father, Jack!"
            bree.say "I'm having another man's baby!"
            "If Jack looked surprised before, now I think he's going to faint!"
            if jack.love >= 140:
                show jack sad
                "But then his expression changes, becoming sad and hurt."
                "And suddenly I feel like the biggest bitch in history."
                "Like I just kicked a giant, friendly puppy in the ass!"
                jack.say "But, [hero.name]..."
                jack.say "That means that you..."
                jack.say "That you must have..."
                bree.say "Urgh..."
                bree.say "Yeah, Jack - I slept with another guy!"
                bree.say "Look, I'm sorry."
                bree.say "It was a mistake, okay?"
                "Jack nods, but still can't look me in the eye."
                jack.say "Okay, [hero.name]..."
                jack.say "I love you, so I guess I can forgive you."
                bree.say "Thank you, Jack!"
                bree.say "But what about the baby?"
                menu:
                    "Ask Jack to help with the baby":
                        if jack.love >= 160:
                            "Jack sighs and shakes his head."
                            jack.say "I'll do whatever I can to help, [hero.name]."
                            jack.say "What kind of a boyfriend would I be if I didn't?"
                            "I nod and smile, grateful for Jack's help."
                            "But at the same time, his words cut me like a knife."
                            "What kind of a girlfriend does his answer make me?"
                            "Especially after I went behind his back and got pregnant?"
                            "Oh god..."
                            "I really don't deserve this guy!"
                        else:
                            show jack angry
                            jack.say "No..."
                            jack.say "Oh no...no way!"
                            jack.say "I can't be a father..."
                            jack.say "I'm too young!"
                            jack.say "And there are so many action figures I don't own yet!"
                            "Well, that wasn't the reaction I was expecting!"
                            "But I don't feel like pushing my luck right now."
                            "So I just nod and let the matter alone."
                            $ jack.breakup()
                    "I won't bother you about it":
                        pass
            else:
                show jack sad
                "But then his expression changes, becoming sad and hurt."
                "And suddenly I feel like the biggest bitch in history."
                "Like I just kicked a giant, friendly puppy in the ass!"
                jack.say "But, [hero.name]..."
                jack.say "That means that you..."
                jack.say "That you must have..."
                bree.say "Urgh..."
                bree.say "Yeah, Jack - I slept with another guy!"
                bree.say "Look, I'm sorry."
                bree.say "It was a mistake, okay?"
                "Jack looks at me like he doesn't know me anymore."
                "And he begins to shake his head as his expression hardens."
                show jack angry
                jack.say "No, [hero.name], it's not okay."
                jack.say "Because this means I can't trust you anymore."
                jack.say "I don't know if anything you tell me is true."
                bree.say "Jack, please..."
                bree.say "We can talk about this..."
                "But it looks like I'm too late."
                hide jack
                show jack sad
                "Jack lurches backwards, almost falling on his face."
                hide jack with easeoutright
                "Then he turns his back and runs away."
                "He literally runs away from me!"
                "Geez..."
                "Looks like I really blew it this time."
                $ jack.set_gone_forever()
    return


label jack_nightclub_date_female:
    scene bg street with fade
    "Going out to a nightclub for my date with Jack seemed like a good idea at the time."
    "It's not something I'd think twice about doing if I were on a date with any other guy."
    "And I thought that it'd be something new for Jack, something to help bring him out of his shell."
    "Because he hardly looks like the kind of guy that regularly hangs out at popular clubs."
    "In fact, he looks more suited to wargaming clubs or ones for people that play with model trains!"
    "But I thought that I could get him used to the noise and energy of clubs."
    "Maybe bring out the more adventurous side of his personality at the same time."
    "Though I'm starting to wonder if I might have misjudged things just a little."
    show jack date sad with dissolve
    "Because Jack seems to be kind of intimidated by the whole experience of even getting into the club."
    jack.say "Oh man..."
    jack.say "Those bouncers are huge!"
    jack.say "I'll try to look innocent, okay, [hero.name]?"
    bree.say "No way, Jack..."
    bree.say "You'll just end up looking shifty."
    bree.say "And that'll make them think you're hiding something!"
    jack.say "Then what should I do?"
    bree.say "I don't know - just act natural and be yourself."
    jack.say "Okay..."
    show jack surprised
    jack.say "How do I do that?!?"
    show jack blush
    "Luckily we arrive at the door the moment Jack asks the question."
    "And the bouncers mistake his waiting for an answer for plain old silence."
    "Which means they usher us past and into the club without incident."
    play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
    scene bg nightclub with fade
    show jack date smile at left with easeinleft
    "Jack looks back over his shoulder, relief written all over his face."
    jack.say "Wow..."
    show jack happy at center with ease
    jack.say "That was a close one!"
    show jack smile
    bree.say "Whatever you say, Jack..."
    bree.say "Come on, I need a drink."
    bree.say "Preferably a strong one!"
    "I make straight for the bar without saying another word."
    show jack at left4 with ease
    "And Jack follows on my heels like a loyal terrier."
    "Once we're there, I get the barman's attention and order."
    "But as we get our drinks, he leans over to speak to me."
    "Barman" "You want to get into the VIP lounge?"
    show jack surprised
    jack.say "Wha...what did you just say?"
    show jack normal
    "Barman" "You heard me, buddy!"
    "Barman" "It's pretty empty tonight."
    "Barman" "So the management are cool with us letting some patrons in."
    "Barman" "You know, good looking patrons?"
    bree.say "Sure we'd like that."
    bree.say "Thanks, man."
    "The barman turns away to wave to the bouncer on the door of the VIP lounge."
    "Which I guess is his way of letting them know we're to be let in there."
    show jack at right with ease
    "As we walk over, Jack seems to be getting more excited by the moment."
    jack.say "You think he's serious, [hero.name]?"
    jack.say "That he really thinks I'm good-looking?"
    jack.say "I mean, I'm not really into other guys..."
    show jack happy
    jack.say "But a compliment is a compliment, after all!"
    bree.say "Erm..."
    bree.say "Yeah, Jack..."
    bree.say "I think there's a chance he might have been talking about me!"
    show jack blush
    jack.say "Oh..."
    jack.say "Oh yeah..."
    "Jack's cheeks flush red and he falls silent."
    "Which is fine by me."
    hide jack with easeoutright
    "As it means he stays quiet as we're let into the VIP lounge."
    scene bg vip with fade
    show jack date smile at left with easeinleft
    "Once in there, we find a booth that is pretty much totally private."
    "I lie back on the sofa, trying to enjoy the surroundings."
    scene drink
    show drink club jack
    with fade
    "But I can see that Jack's finding it hard to even sit still."
    jack.say "Does this kind of thing happen to you all the time, [hero.name]?"
    jack.say "Like is it something I'm going to have to get used to on our dates?"
    jack.say "Because this kind of thing never happens to me!"
    bree.say "Really?"
    bree.say "I can't imagine why..."
    "I can't help being amused by all the energy that Jack's putting into it."
    "How animated and excited he seems to be simply doing something familiar to me."
    "It kind of reminds me of just how infectious that side of him can be."
    "And how much fun it can be to be carried along on his positive energy."
    "Or maybe how I could channel it into something else..."
    bree.say "You know what else goes on in places like this, Jack?"
    "I make sure to lean in close as I ask the question."
    "And as I suspected, Jack can't resist doing the same."
    jack.say "N...no, [hero.name]..."
    jack.say "What's that?"
    "I gently place my hand on Jack's groin."
    "And I begin to stroke his cock through his pants."
    bree.say "Whatever the hell you want, Jack..."
    bree.say "That's what!"
    bree.say "Because this booth is totally private."
    bree.say "And we can do whatever we want!"
    call jack_fuck_date_vip_doggy_female (1) from _call_jack_fuck_date_vip_doggy_female
    scene drink
    show drink club jack
    with fade
    "It doesn't take me long to put my clothes back on."
    "And once I'm done, Jack's mood seems to improve a great deal."
    "Now it's like he's proud and even a little cocky."
    "Like he's just gotten away with something he never expected he could."
    "I can't help smiling, hoping that this will give him a confidence boost."
    "But not too much of one, not enough to chance him significantly."
    "Because I wouldn't want to lose the cute, endearing elements of his character."
    "No matter how much fun a more confident version of Jack might be."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
