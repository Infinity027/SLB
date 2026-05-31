init python:
    Event(**{
    "name": "electronic_harem_event_01",
    "label": "electronic_harem_event_01",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(22, 4),
        IsDone("amy_teaser_sex"),
        PersonTarget("amy",
                     MinStat("love", 120),
                     IsFlag("amydelay", False),
                     Not(HasRoomTag("pub"),)),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            HasRoomTag("pub"),),
        ],
    "duration": 1,
    "do_once": True,
    })

    InteractEvent(**{
    "name": "electronic_harem_event_02",
    "label": "electronic_harem_event_02",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("electronic_harem_event_01"),
        PersonTarget("amy",
                     InHarem('electronic'),
                     IsFlag("amydelay", False),
                     IsActive(),
                     ),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "electronic_harem_event_03",
    "label": "electronic_harem_event_03",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("electronic_harem_event_02"),
        IsDayOfWeek("7"),
        PersonTarget("amy",
                     Not(IsRoom("electronic"))),
        HeroTarget(
            IsGender("male"),
            IsRoom("electronic"),
            Not(OnDate())),
        ],
    "duration": 0,
    "do_once": True,
    })

    Event(**{
    "name": "electronic_harem_event_04",
    "label": "electronic_harem_event_04",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("electronic_harem_event_03"),
        PersonTarget("amy",
                     InHarem('electronic'),
                     MinStat("love", 130),
                     MinStat("sub", 20),
                     IsFlag("electronic_harem_delay", False),
                     IsActive(),
                     IsPresent(),
                     ),
        HeroTarget(
            IsGender("male"),
            ),
        ],
    "duration": 0,
    "do_once": True,
    })

    Event(**{
    "name": "electronic_harem_event_05",
    "label": "electronic_harem_event_05",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("electronic_harem_event_04"),
        IsDayOfWeek("123456"),
        IsHour(19, 21),
        PersonTarget("amy",
                     InHarem('electronic'),
                     MinStat("love", 140),
                     MinStat("sub", 50),
                     IsFlag("amydelay", False),
                     IsFlag("agree_electronic_threesome", True),
                     IsFlag("electronic_harem_delay", False),
                     ),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            Not(OnDate()),
            ),
        ],
    "duration": 2,
    "do_once": True,
    })

    Event(**{
    "name": "electronic_harem_event_06",
    "label": "electronic_harem_event_06",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("electronic_harem_event_05", "palla_event_10"),
        IsHour(19, 23),
        PersonTarget("amy",
                     InHarem('electronic'),
                     IsFlag("electronic_harem_delay", False),
                     ),
        PersonTarget(palla),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            Not(OnDate()),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "electronic_harem_event_07",
    "display_name": "Foursome with Shawn",
    "label": "electronic_harem_event_07",
    "duration": 0,
    "icon": "button_shawn",
    "conditions": [
        IsDone("electronic_harem_event_06"),
        HeroTarget(
            IsGender("male"),
            IsFlag("electronic_foursome", True),
            ),
        PersonTarget(palla,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "electronic_harem_event_08",
    "display_name": "Foursome with Shawn",
    "label": "electronic_harem_event_08",
    "duration": 0,
    "icon": "button_shawn",
    "conditions": [
        IsDone("electronic_harem_event_07"),
        HeroTarget(
            IsGender("male"),
            IsFlag("electronic_foursome", True),
            ),
        PersonTarget(amy,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Activity(**{
    "name": "electronic_foursome",
    "display_name": "Foursome (Electronic)",
    "label": "electronic_harem_event_09",
    "conditions": [
        IsDone("electronic_harem_event_08"),
        Not(IsDone("electronic_harem_event_09")),
        IsHour(19, 2),
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            HasStamina(),
            Not(OnDate()),
            IsFlag("electronic_foursome", True),
            ),
        PersonTarget(amy,
            Not(IsHidden()),
            MinStat("love", 170),
            MinStat("sub", 90),
            ),
        PersonTarget(palla,
            Not(IsHidden()),
            MinStat("love", 170),
            MinStat("sub", 90),
            ),
        ],
    "icon": "fuck",
    "duration": 3,
    })

label electronic_harem_event_01:
    scene bg pub
    "Normally when I see someone I know in the Winchester, I make a beeline for them."
    "But this time I end up stopping in my tracks the moment I spot the familiar face."
    show shawn date noglasses sad blush at center, zoomAt(1.0, (220, 880)), dark with dissolve
    "That's because it's Shawn that I see sitting alone at one of the tables."
    "And unlike most of the other drinkers in the pub, he looks miserable as sin!"
    "Yeah, yeah, yeah...I know what you're thinking."
    "One of my friends is drowning his sorrows all alone."
    "And I just happen to be in the same place at the same time."
    "What kind of a friend would I be if I didn't go over there and ask him what's up?"
    "Well the only problem in that I'm pretty sure I already know what the problem is."
    "And what's worse is that I'm a part of it too!"
    "Shawn and I practically haven't spoken since I started dating Amy."
    "I'm sure he blames me for stealing her away from him too."
    "Which isn't strictly true, as she was never really interested in him to begin with."
    "Oh man...I need to make a call here."
    "If I stay put, chances are he's going to see me sooner or later - which would be awkward."
    "Or I could walk out of the place now and keep that from happening."
    "Of course there is a third option."
    "I could grow a pair, go over there and actually talk to Shawn!"
    menu:
        "Grow a pair":
            "Ah, hell...I feel like I have to at least try to be the bigger man."
            "Taking a deep breath, I walk over to the table where Shawn's sitting."
            "He doesn't look up at the sound of me approaching, so I let out the breath."
            hide shawn
            show shawn date noglasses sad blush at center, zoomAt(1.0, (220, 880))
            with dissolve
            mike.say "Ah..."
            mike.say "Hey, Shawn..."
            mike.say "How are you doing?"
            "The moment Shawn looks up, I know the answer to the question."
            "And it can't be anything other than dreadful!"
            "Shawn's eyes look red-rimmed and sunken in."
            "His hair's a mess and he looks like he slept in his clothes."
            show shawn angry
            shawn.say "Urgh..."
            shawn.say "What the actual fuck do you want, [hero.name]?"
            shawn.say "Isn't it enough that you stole away the woman of my dreams?"
            shawn.say "Now you want to come along and rub my face in it?!?"
            scene drink_room_pub
            show shawn date noglasses annoyed blush at center, zoomAt(1.75, (440, 1180))
            show drink_table_pub_victor
            show drink_room_fg_pub
            with fade
            "I pull out the chair on the other side of the table and sit down."
            "Shawn responds by crossing his arms and turning away from me."
            "He's so drunk and melodramatic that the gesture makes him look like a sulking child."
            "But the important thing I note is that he doesn't get up and walk away."
            "Something that I choose to take as meaning that he actually wants to talk."
            mike.say "Come on, man..."
            mike.say "I understand that you were into her, really I do."
            mike.say "But the woman of your dreams?!?"
            mike.say "You fall in love with a new one of those every month, Shawn."
            mike.say "And most of them are whatever actress is in the latest sci-fi movie that's out!"
            "Shawn opens his mouth to argue the point."
            show shawn normal
            "But then he stops with it still hanging open."
            shawn.say "Oh yeah..."
            shawn.say "I guess you're right."
            shawn.say "Which reminds me..."
            show shawn nice
            shawn.say "Have you seen the lead in the new Space Battles series that's streaming?"
            shawn.say "I think she might be the woman of my dreams!"
            "Shawn's so drunk he doesn't even seem to notice what he just did."
            "Right now I bet that I could get him talking about other stuff."
            "That way he might forget about Amy more quickly."
            "But on the other hand, perhaps he needs to face up to what happened?"
            "And I should keep the conversation focused on that subject."
            menu:
                "Keep the conversation":
                    "Talking about other stuff should be easier."
                    "So that's the way I try to steer the conversation."
                    mike.say "No, Shawn, I haven't."
                    mike.say "I still have to finish watching the last one!"
                    show shawn annoyed
                    "Shawn looks at me with an expression of exaggerated disgust."
                    "And he shakes his head to underline his disapproval."
                    show shawn angry
                    shawn.say "Hah!"
                    shawn.say "And you call yourself a fan!"
                    "I watch as Shawn downs the last of his drink."
                    "Then he pushes back his seat and drags himself to his feet."
                    shawn.say "You're as bad of a fan as you are a friend!"
                    show shawn at center, zoomAt(1.75, (440, 940)) with ease
                    "With that said, he turns his back on me."
                    hide shawn with easeoutright
                    "And then he walks straight out of the pub."
                    "Which leaves me sitting alone."
                    "That and wondering how I managed to screw things up so badly!"
                "Keep talking about Amy":
                    "I feel like I need to make Shawn focus on the elephant in the room."
                    "So I do my best to bring the conversation back to Amy."
                    mike.say "I don't think you really want to talk about sci-fi, Shawn."
                    mike.say "I think you're just trying to keep from talking about Amy."
                    "For a moment I think that Shawn's going to throw his drink in my face."
                    "That or collapse into a flood of hopeless tears."
                    "So it comes as some relief when he just lets out a tortured sigh instead."
                    show shawn sad
                    shawn.say "Uuurrrgh!"
                    shawn.say "She hurt me, [hero.name]!"
                    shawn.say "She pierced my normally impervious armour."
                    shawn.say "Then she reached into my chest..."
                    shawn.say "And she pulled out my still-beating heart!"
                    "My first instinct is to laugh at how dramatic Shawn's being."
                    "But somehow I manage to keep a handle on it."
                    "And instead I nod in what I hope is a sympathetic manner."
                    mike.say "I know, man, I know..."
                    mike.say "Look...if it's any comfort..."
                    mike.say "I had no idea you were that into Amy."
                    mike.say "And what happened with us just kind of...happened!"
                    mike.say "We weren't trying to go behind your back or anything."
                    "Shawn rubs his hands over his face, scrubbing his beard."
                    show shawn nice
                    "And then I feel a rush of genuine relief as he nods."
                    shawn.say "I...I know that, dude..."
                    shawn.say "It's just that matters of the heart..."
                    show shawn sad
                    shawn.say "They make me crazy, you know?"
                    "I nod, and not just for the sake of indulging Shawn."
                    "Because any guy that's been in his position understands all too well."
                    shawn.say "I mean...what's wrong with me, dude?"
                    shawn.say "You seem to manage to pull the birds all the time."
                    shawn.say "What is it you have that I don't?"
                    if not 'palla_event_11' in DONE:
                        show shawn angry
                        shawn.say "You did the same thing with Palla too!"
                        shawn.say "And I was crazy into her as well!"
                        mike.say "Erm...yeah..."
                        mike.say "I don't know what to say, man!"
                        mike.say "I guess I just got lucky twice..."
                        show shawn sad
                    "I shake my head as we start to get into the nitty gritty of the subject."
                    "Pretty soon we're ordering more drinks and dissecting it in painful detail."
                    "Shawn seems to be intent on keeping up an almost manic pace when it comes to drinking."
                    "I feel the urge to do the same, as it's helping him vent."
                    "But there's that little voice in the back of my head."
                    "The one that's telling me I should maybe hold back a little."
                    "Just so that one of us is vaguely sober."
                    menu:
                        "Be reasonable":
                            "I deliberately slow down the speed at which I'm drinking."
                            "But Shawn does no such thing, going at the same crazy pace."
                            "And pretty soon the difference is starting to show."
                            "I'm still nodding and offering fairly coherent comments."
                            "Whereas he's beginning to slur his words and making less sense."
                            shawn.say "Yah...yah see..."
                            shawn.say "Yah see what I...I mean?"
                            mike.say "Erm..."
                            mike.say "I guess so!"
                            shawn.say "Nah...nah..."
                            shawn.say "Yah don't...yah don't see!"
                            show shawn happy
                            shawn.say "I'm saying...I LOVE you, dude!"
                            shawn.say "S...sure, yah took her from me..."
                            shawn.say "But I still love yah!"
                            show shawn at startle
                            "Shawn underlines his point by launching himself at me."
                            with hpunch
                            "And the next thing I know, I'm trapped in a drunken hug."
                            "The best I can do is use it as an opportunity."
                            scene bg pub
                            show shawn date noglasses happy blush at center, zoomAt(1.5, (540, 1040))
                            with fade
                            "So I keep a hold of Shawn as I haul him to his feet."
                            mike.say "Come on, Shawn..."
                            show shawn normal
                            shawn.say "Huh?"
                            shawn.say "Are we going somewhere?"
                            mike.say "Yeah..."
                            mike.say "I think it's time I took you home!"
                            "Holding Shawn up with one arm, I use the other to push through the crowd."
                            "All the time hoping that I can get him home before he decides to puke on my shoes."
                        "Keep up the pace":
                            "Keeping up with Shawn seems to be working."
                            "The more we drink, the more he opens up."
                            "And it seems I was wrong to worry about getting drunk."
                            "Because every sip I take, my mind seems to get clearer."
                            "And I feel like I'm making ever more sense too."
                            "Anyone able to hear us must be pretty impressed."
                            "To my ears, we sound like philosophers waxing lyrical on lofty intellectual matters."
                            shawn.say "Yah...yah see..."
                            shawn.say "Yah see what I...I mean?"
                            mike.say "Yeah...yeah..."
                            mike.say "I do...I do..."
                            shawn.say "Nah...nah..."
                            shawn.say "Yah don't...yah don't see!"
                            show shawn happy
                            shawn.say "I'm saying...I LOVE you, dude!"
                            shawn.say "S...sure, yah took her from me..."
                            shawn.say "But I still love yah!"
                            show shawn at startle
                            "Shawn underlines his point by poking me pretty hard in the chest."
                            "I stare down at his finger as he does it, swaying slightly the whole time."
                            "And when I look up again, I feel like a revelation hits me."
                            mike.say "Oh...oh man..."
                            mike.say "That is SO cool of you..."
                            mike.say "But...you shouldn't totally miss out!"
                            show shawn normal
                            shawn.say "Whadda yah mean?"
                            shawn.say "Are you like...gonna share Amy with me?"
                            "I shake my head and wave my hands in the air."
                            mike.say "No, no, no..."
                            mike.say "I'll film us doing it, yeah?"
                            mike.say "Like...with a camera and everything!"
                            mike.say "Then you can watch!"
                            show shawn happy
                            "Shawn's eyes go wide with amazement."
                            shawn.say "You'd do that?"
                            with hpunch
                            "Shawn launches himself at me."
                            "And the next thing I know, I'm trapped in a drunken hug."
                            "I seem to take this as a signal of some kind."
                            scene bg pub
                            show shawn date noglasses happy blush at center, zoomAt(1.5, (540, 1080))
                            with fade
                            "So I keep a hold of Shawn as I haul him to his feet."
                            show shawn normal
                            shawn.say "Huh?"
                            shawn.say "Are we going somewhere?"
                            mike.say "HOME!"
                            mike.say "We're...going home!"
                            "Barely able to hold each other up, we stumble through the crowd."
                            scene bg street with fade
                            "The next thing I know, we're out of the pub and walking home."
                            "But whether that's my home or Shawn's, I have no idea."
                            $ amy.flags.amydelay = TemporaryFlag(True, 1)
                            $ Harem.join_by_name("electronic", "amy")
                            $ game.room = "bedroom1"
                            $ game.pass_time(1)
                            call sleep from _call_sleep_78
                            return
        "Who need balls anyway...":
            "Call me a coward if you like."
            "But I'm not about to stay here and cause a scene."
            "And anyway, it's not like it's my fault Shawn's in such a state."
            "If he'd been even just a little bit more charming and less of an arse..."
            "Then I'm sure that he'd have been in with a chance of winning Amy over."
            hide shawn with dissolve
            "I hastily turn my back on Shawn and down what's left of my drink."
            "As soon as that's done, I head straight for the door and leave the pub."
            "Maybe when he sobers up, Shawn will be in the mood to clear the air."
            "But until then, I think I'm going to keep on avoiding him."
            $ game.room = "map"
    return

label electronic_harem_event_02:
    if DONE['electronic_harem_event_01'] >= game.days_played - 1:
        "I can almost feel the last awful vestiges of my hangover as I rush to meet Amy."
        "And my head is still pounding when I see her waving to me as she approaches."
        "I force a smile onto my face that's really a grimace of discomfort and wave back."
        "But only part of my problem is with the after-effects of the amount I drank last night."
        "Maybe even more of it is on account of the offer that I made to Shawn."
        "I'm still not sure what the fuck I was thinking."
        "What made me offer to actually film myself and Amy having sex and send him the footage!"
        "It'd probably be better to say that I wasn't thinking at all..."
    show amy at center, zoomAt(1.25, (640, 900)) with dissolve
    amy.say "Hey, [hero.name]..."
    show amy worried
    show fx question
    amy.say "Is everything okay?"
    amy.say "You look a little nervous!"
    hide fx
    mike.say "Hey, Amy..."
    mike.say "No...everything's fine..."
    mike.say "But there was something I wanted to talk to you about."
    show amy surprised
    "Amy cocks her head on one side and raises her eyebrows."
    amy.say "Oh yeah?"
    amy.say "And what would that be?"
    show amy normal
    "I take a deep breath and prepare to say what I have to say."
    "But obviously I can't just jump straight in and ask her."
    "I have to set up the scenario in her mind first."
    mike.say "The thing is, Amy..."
    if DONE['electronic_harem_event_01'] >= game.days_played - 1:
        mike.say "I was in the pub last night..."
        show amy flirt
        amy.say "Oh, I see!"
        amy.say "I wondered why you looked a little peaky!"
        show amy normal
        amy.say "Still hung-over, are we?"
        "I smile and hold up a hand to stop Amy."
        mike.say "No!"
        mike.say "Well...maybe a little - but that's not the point I was trying to make."
    else:
        mike.say "I was in the pub a couple days ago..."
    mike.say "I bumped into Shawn while I was there."
    show amy annoyed
    "At the mere mention of her boss's name, Amy groans."
    show amy angry
    amy.say "Eck..."
    amy.say "I bet that was a whole bunch of fun!"
    amy.say "Is he still acting all butt-hurt?"
    amy.say "Like he's the victim in all of this?"
    show amy annoyed
    "I nod, just a little."
    mike.say "He was kinda like that, yeah."
    mike.say "At least he was at first."
    mike.say "We got to talking, and he lightened up quite a bit."
    "Amy's still frowning as she listens to my explanation."
    show amy worried
    "And once I'm finished, she looks more than a little put out."
    "Like she was all set to be one hundred percent against Shawn."
    "But now I've forced her to feel just a tiny bit sorry for him."
    show amy shy
    amy.say "Hmpf..."
    amy.say "Well..."
    show amy annoyed
    amy.say "He was still an asshole to me!"
    show amy shy
    amy.say "None of what you said changes that."
    "I nod, not being dumb enough to argue with Amy."
    "But then I steel myself for what I have to do next."
    "Because apparently I'm totally dumb enough to do that!"
    mike.say "There was one other thing we talked about, Amy."
    mike.say "I kinda made Shawn a promise."
    mike.say "To make up for the fact that he missed out..."
    show amy mad at startle
    "Amy rolls her eyes and shakes her head."
    amy.say "[hero.name]..."
    amy.say "I don't like where this is going!"
    show amy surprised
    amy.say "You didn't..."
    amy.say "You wouldn't..."
    show amy mad
    amy.say "You'd better not have..."
    show amy angry
    amy.say "Because I am not giving Shawn a pity fuck!"
    with vpunch
    mike.say "WHAT?!?"
    mike.say "No way!"
    mike.say "That's not it at all, Amy!"
    show amy normal
    "Amy lets out a gasp of relief."
    amy.say "Phew!"
    amy.say "I was actually worried for a second there!"
    mike.say "No, I'd never ask you to have sex with Shawn."
    show amy surprised at startle
    show fx exclamation
    mike.say "I just promised to film us fucking and let him watch it afterwards!"
    if amy.sub >= 10:
        hide amy
        show amy surprised
        with vpunch
        "I flinch away from Amy, leaping back a good few feet."
        "And I hold up my hands, fully expecting her to hit me."
        "But then I notice that she hasn't moved an inch herself."
        show amy shy
        "And when I sneak a look in her direction, she's actually looking thoughtful."
        mike.say "Amy?"
        mike.say "Are you okay?"
        mike.say "Or are you so angry you're literally paralysed with rage?"
        amy.say "What?"
        amy.say "Oh no..."
        show amy normal
        amy.say "I was just thinking about what you said."
        "Sensing the chance to dig myself out of the hole, I leap to it."
        mike.say "I know, Amy, I know..."
        mike.say "It's a dumb idea and I should never have suggested it."
        mike.say "All I can say is that I was drunk and I'm sorry!"
        "Amy frowns at me and shakes her head."
        amy.say "What the fuck are you talking about, [hero.name]?"
        show amy happy
        $ Harem.join_by_name("electronic", "shawn")
        amy.say "I think it's a great idea!"
        "Okay, now I'm starting to feel like I'm still drunk."
        "And it takes me a couple of seconds to grasp what Amy just said."
        "But as soon as I do, I start back-pedalling like a pro."
        mike.say "Forget everything I just said!"
        mike.say "Of course it's a great idea!"
        mike.say "And you're one hundred percent sure you want to do it?"
        "Amy nods with serious enthusiasm."
        amy.say "Oh yeah!"
        show amy normal
        amy.say "I've always been jealous of pornstars."
        amy.say "And it's not like I actually have to have sex with Shawn."
        $ amy.sub += 2
        show amy flirt
        amy.say "It kind of gives me a thrill - the thought of him watching it."
        amy.say "Knowing that he's seeing what he can't have."
        amy.say "And probably having a self-pitying wank over it too!"
        "I'm nodding too by now, eager to encourage Amy all I can."
        mike.say "That's great!"
        mike.say "I'll get everything set up as soon as I can."
        mike.say "Then we can get the camera rolling!"
    else:
        amy.say "You did?"
        hide fx
        show amy happy
        amy.say "Well that's okay then."
        "I gawp at Amy for a moment, not sure I heard her right."
        mike.say "It...it is?"
        "And that's the moment when the floodgates open."
        "Unleashing the wrath of hell upon my ass."
        $ amy.love -= 10
        $ Harem.leave_by_name("electronic", "amy")
        show amy angry at vshake
        show fx anger
        amy.say "OF COURSE IT'S NOT!"
        amy.say "What kind of a fucking idiot are you?!?"
        hide amy
        show amy upset
        with vpunch
        "I flinch away from Amy, leaping back a good few feet."
        hide fx
        "And I hold up my hands, fully expecting her to hit me."
        "But what she actually does is far worse."
        "She follows right up with her lecture."
        "Blistering me with the evidence of my own stupidity."
        show amy angry
        amy.say "I don't want to sleep with the guy."
        amy.say "So in what insane version of reality would I want to shoot a tape of us fucking for him?"
        amy.say "Basically a porn, staring the two of us, for Shawn to have a self-pitying wank over!"
        mike.say "Well..."
        mike.say "When you put it like that..."
        show amy mad
        "Amy shakes her head one last time."
        show amy at left with ease
        "Then she turns on her heel and storms off."
        mike.say "W...where are you going?"
        amy.say "Anywhere you're not!"
        hide amy with easeoutleft
        "I think about following her for a moment."
        "But then I decide that it's not a good idea."
        "The best thing would be to leave Amy long enough for her to cool off."
        "The only problem is that, based on how mad she is, that could be a very long time indeed!"
    $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return

label electronic_harem_event_03:
    scene bg electronic
    "I walk into the electronics store on a day when I know that Amy isn't working."
    "And I also choose a time that I can be sure the place is going to be quiet too."
    "That way I'm almost certain to catch Shawn on his own in there."
    "I know full well that the level of paranoia I'm feeling is crazy."
    "After all, it's not like I'm coming into the store to sell him hard drugs."
    "All I have to do is hand over the memory-card with the footage on it."
    "Yet somehow this all still feels like one of those handovers in a spy film."
    "Like the second we make the exchange, armed men in suits are going to storm the store!"
    "All of this means that I'm sweating bullets as I walk up to the counter where Shawn's waiting."
    show shawn happy with dissolve
    shawn.say "Ah, Blue Eagle..."
    shawn.say "I hear the blossom is beautiful in Moscow this time of year!"
    "I look around, my heart already beating faster in my chest."
    mike.say "Shawn..."
    mike.say "What are you babbling about?!?"
    mike.say "Have you gone mad?"
    "Shawn seems to realise that I'm on edge all of a sudden."
    "And he changes his whole attitude, holding up his hands to show it too."
    show shawn nice
    shawn.say "Whoa!"
    shawn.say "No need to pop a vein in your brain!"
    shawn.say "It was just a joke - like you see in spy movies, yeah?"
    mike.say "Well stop it, okay?"
    mike.say "You're making me nervous."
    show shawn normal
    "Shawn shrugs and seems to take the hint."
    "Because when he next opens his mouth, he gets straight down to business."
    shawn.say "So..."
    shawn.say "You've got something for me, right?"
    "I reach into my pocket and pull out the memory-card."
    "But even now that we've dispensed with the theatrics, I'm still anxious."
    show shawn at center, zoomAt(1.25, (640, 860))
    "I can't help glancing around as I hand it over to Shawn."
    mike.say "There you go, Shawn."
    mike.say "The raw, unedited footage."
    mike.say "Just like I promised."
    show shawn happy blush
    "Shawn takes the memory card eagerly, a huge grin on his face."
    "As soon as he has it in his hand, he tries to toss it in the air."
    "My guess is that he intends to catch it again and make some witty comment."
    show shawn nice -blush
    "But instead he fumbles it in mid-air, then scrabbles to catch it again."
    show shawn at center, zoomAt(1.0, (640, 860)), vshake
    "In the end he manages it by sprawling across the counter in an undignified mess."
    "Then he straightens up and drops the memory-card into his pocket."
    shawn.say "Ahem..."
    show shawn embarrassed
    shawn.say "Sorry about that!"
    shawn.say "Wouldn't want to damage the merchandise."
    shawn.say "I need to be able to see what I'm watching."
    show shawn nice
    shawn.say "You know, when I'm alone later tonight?"
    "Shawn raises his eyebrows and cracks his knuckles."
    "All of which puts an image in my head I'll never be able to forget."
    mike.say "OKAY!"
    mike.say "Stop right there!"
    "Shawn seems to realise that he's overstepped the mark."
    "And he instantly become apologetic."
    show shawn normal
    shawn.say "Sorry, sorry!"
    shawn.say "I'm just excited, that's all!"
    "I can't help wincing at his choice of words."
    shawn.say "Sorry again!"
    shawn.say "Right...let's change the subject!"
    shawn.say "I need to do something to repay your kindness."
    mike.say "It's no bother, Shawn!"
    mike.say "You don't have to..."
    shawn.say "Like maybe with a Zbox?"

    shawn.say "Or a small permanent discount on every product?"
    mike.say "Actually, now you mention it..."
    mike.say "I do feel like that would be fair compensation!"
    show shawn happy
    "Shawn gives me a wry smile."
    shawn.say "So..."
    shawn.say "Which is it going to be?"
    menu:
        "Finally a real gaming console! Good riddance Zwitch!" if not "zbox_360" in hero.inventory:
            "It's not like I need any time to choose."
            "The mere mention of a Zbox makes my palms go sweaty."
            mike.say "That's great, Shawn!"
            mike.say "I'll take the Zbox, yeah?"
            mike.say "And I can take it home with me now?"
            show shawn at startle
            "Shawn nods as he turns to take one down off the shelf."
            shawn.say "Not a problem."
            shawn.say "There you go."
            shawn.say "And it was a pleasure doing business with you."
            shawn.say "Oh, and be careful with that - it's a special edition!"
            "I grab the box out of his hands, holding it to my chest."
            "And then I glance around the store."
            "Looking as if I think someone's going to try to take it from me."
            "Shawn seems more than a little amused by my reaction."
            shawn.say "So that makes us equal."
            shawn.say "Pleasure doing business with you!"
            hide shawn with dissolve
            "I nod and hurry out of the store, still clutching the box."
        "There's no small profit, it'll take the discount":
            "We already have a perfectly good Zbox in the sitting-room back home."
            "So it's kind of a no-brainer which of the two I'm going to choose."
            mike.say "That's great, Shawn!"
            mike.say "I'll take the permanent discount, yeah?"
            shawn.say "Not a problem."

            "Shawn pulls out a card of the store."
            "And then he inserts it into a slot on the register."
            shawn.say "There you go."

            shawn.say "Just present this card each time you want to make a purchase here."
            "He pulls it out of the slot and hands it over the counter."
            shawn.say "So that makes us equal."
            shawn.say "Pleasure doing business with you!"
            "I take the card with a nod."
            hide shawn with dissolve
            "And as I shove it into my pocket, I'm already looking around the store."
            "There's a bunch of games and accessories I'd like for the Zbox."
            $ Room.find("electronic").flags.discount = 15
    "All I have to do now is figure out an explanation for when I get home."
    "And I'm sure I'll figure out something before I get there."
    $ game.room = "mall2"
    $ amy.flags.electronic_harem_delay = TemporaryFlag(True, 5)
    return

label electronic_harem_event_04:
    scene expression f"bg {game.room}" with fade
    "It's been a while since the time I found Shawn crying into his beer over Amy."
    "You remember, the one where I solved it by filming us having sex for him to watch?"
    "Myself and Amy having sex, that is - not me and Shawn!"
    "And things have been pretty quiet since then, so I'd chosen to assume it all worked out."
    show amy normal with fade
    "So it comes as a surprise to me when Amy brings it up, totally out of the blue."
    show amy happy
    amy.say "You know what..."
    amy.say "I really should thank you, [hero.name]."
    show amy normal
    mike.say "Huh?"
    mike.say "What for, Amy?"
    amy.say "Your idea to film that sex-tape for Shawn."
    amy.say "It really helped to get him off my back."
    show amy shy
    amy.say "And well..."
    show amy happy
    amy.say "I had a lot of fun making it with you too!"
    show amy at startle
    "Amy lets out a giggle that I feel right between my legs!"
    "And she has that smile on her face that really turns me on too."
    mike.say "Happy to be of service, Amy!"
    show amy normal
    mike.say "And if you enjoyed it that much..."
    mike.say "Well, let's just say I have plenty of ideas for a sequel!"
    show amy happy
    amy.say "Oh man - just a sequel?"
    show amy flirt
    amy.say "I wanna make a whole franchise out of it!"
    show amy normal
    "Amy cocks her head on one side, her expression changing a little."
    "And I can see that she wants to be more serious for a moment."
    amy.say "I mean it though, [hero.name]."
    amy.say "It's really defused a lot of the tension at work."
    amy.say "Like, Shawn's being way less of a prick than before."
    "I nod happily, glad that things turned out as well as they did."
    amy.say "Thing is..."
    amy.say "I figured out it's Shawn's birthday coming up soon."
    "I rack my brain as Amy says this."
    "And I seem to remember that she's right."
    mike.say "Oh yeah..."
    mike.say "It is around this time of year."
    show amy shy
    amy.say "So I was thinking..."
    amy.say "I wanted to get him something nice."
    show amy normal
    amy.say "And you're his friend, right?"
    amy.say "So you'd have a better idea of what he'd like than me."
    $ amy.flags.agree_electronic_threesome = False
    menu:
        "Suggest a safe gift":
            "I think about it for a moment."
            "And then the thought of letting Shawn have some more action pops into my head."
            "But I dismiss it almost without hesitation as a bad idea."
            "Amy already dealt with a lot of hassle from him in the workplace."
            mike.say "How about you get him a gift card from somewhere nice?"
            mike.say "That way you don't have to put too much thought into it."
            mike.say "Plus you won't have to haul a gift around either?"
            show amy puzzled
            "Amy screws up her face as she considers my advice."
            "But I can tell that she doesn't seem totally sold."
            show amy surprised
            amy.say "Are you sure that'd work?"
            amy.say "It seems kind of impersonal."
            show amy worried
            amy.say "If you know what I mean?"
            mike.say "Of course it does, Amy!"
            mike.say "Didn't we just deal with Shawn getting TOO personal?"
            mike.say "I think this keeps things going in the right direction."
            "Amy frowns at this, but she nods all the same."
            show amy normal
            amy.say "When you put it that way..."
            amy.say "Yeah, gift card it is!"
            "I nod too, feeling happy that the situation is resolved."
        "Suggest a threesome":
            "I think about it for a moment."
            "And then an idea pops right into my head."
            "I don't take the time to think about it."
            "Because I know that if I do, I'll start to pick it apart in my own head."
            "And plus part of me is expecting Amy to shoot it straight down anyway."
            "So what the hell..."
            mike.say "You know, Amy..."
            mike.say "We could always let Shawn in on the action?"
            show amy puzzled
            "Amy frowns and cocks her head on one side."
            show amy worried
            show fx question
            amy.say "Huh?"
            amy.say "Does that mean what I think it means?"
            mike.say "I think that depends on what you think it means."
            show amy surprised
            amy.say "Don't avoid the question, [hero.name]!"
            amy.say "Are you suggesting we have a threesome with Shawn?!?"
            mike.say "Erm...yeah, pretty much!"
            if amy.sub >= 50 - hero.charm * 0.3:
                show amy normal
                "I hold up my hands in a gesture of peace."
                "And I'm already beginning to backtrack on what I just said."
                mike.say "Of course we don't have to do that!"
                mike.say "Not if you don't want to..."
                mike.say "Unless you actually do want to..."
                mike.say "Do you want to?"
                show amy puzzled
                "When I finally look Amy in the face, I'm stunned."
                "And that's because she doesn't look mad at me."
                "Instead she has a thoughtful expression on her face."
                "Like she's really considering it!"
                show amy normal
                amy.say "You know what..."
                show amy happy
                amy.say "That sounds like it could be a fun idea."
                mike.say "Are you actually serious?"
                mike.say "I mean you're not being sarcastic, are you?"
                mike.say "Like you're going to start yelling at me any second?"
                mike.say "Because that has happened before!"
                "Amy waves away my concerns."
                show amy normal
                amy.say "Don't be stupid."
                amy.say "I wouldn't have said it if I wasn't serious."
                show amy happy
                amy.say "No, I think it's a great idea."
                amy.say "It'll spice things up for us."
                show amy normal
                amy.say "And it should get Shawn off my back once and for all."
                "I blink and stare into space for a moment."
                "As though I'm expecting this all to end up being a dream of some kind."
                "But when that doesn't happen, I snap back to reality."
                mike.say "Okay then..."
                mike.say "I'll just drop Shawn a line and see what he thinks about the idea."
                show amy surprised at startle
                show fx exclamation
                amy.say "NO!"
                amy.say "Let's keep it a secret."
                show amy happy
                amy.say "That way we can get him out on his birthday and surprise him!"
                "I shrug and nod, because that sounds as good as my own idea."
                "And just like that, it seems we're arranging a threesome!"
                $ amy.flags.agree_electronic_threesome = True
                $ amy.flags.electronic_harem_delay = TemporaryFlag(True, 1)
            else:
                show amy surprised
                "As soon as I put the idea out there, Amy's face drops."
                "She stares at me, her jaw hanging open in complete amazement."
                show amy worried
                show fx drop
                amy.say "You can't be serious?"
                amy.say "Can you?"
                show amy surprised
                show fx exclamation
                amy.say "Please tell me you're not fucking serious?!?"
                "I hold up my hands in a gesture of peace."
                "And I'm already beginning to backtrack on what I just said."
                mike.say "Of course we don't have to do that!"
                mike.say "Not if you don't want to..."
                mike.say "Unless you actually do want to..."
                mike.say "Do you want to?"
                "Amy all but explodes in response."
                $ amy.love -= 10
                $ amy.sub -= 5
                show amy angry at vshake
                show fx anger
                amy.say "NO I DO NOT!"
                amy.say "Is that clear enough for you, huh?"
                amy.say "Or do you need it in writing?"
                mike.say "No, no..."
                mike.say "I get it."
                "I do the best I can to keep smiling as Amy looks daggers at me."
                "But I know that I just seriously misjudged the situation."
                "And now I have to be extra careful so that she'll eventually forgive me."
                $ Harem.leave_by_name("electronic", "amy")
    return

label electronic_harem_event_05:
    scene bg pub
    "I'm waiting in the Winchester for Amy and Shawn to turn up as we agreed."
    "On the surface it's just the three of us meeting up after they finish work."
    "Of course with the added bonus that we're supposed to be celebrating Shawn's birthday."
    "But the elephant in the room is that fact that Amy and I have a surprise in store for him."
    "Rather than buying Shawn an actual present, we've decided to offer him a threesome instead!"
    "I mean, it sounded like a good idea at the time."
    "And it sounded better still when Amy actually agreed to it."
    "But now I feel like I'm turning into a bag of nerves as I wait for them to arrive."
    "What if Shawn gets offended and says no?"
    "What if he jumps at the chance and says yes?"
    "I push the thought aside and instead take a long drink from my glass."
    "It's way too late to be getting cold feet now, as the plan's already in motion."
    "And as if on cue, I look up at the sound of the door opening."
    show amy at center with easeinright
    show shawn at right with easeinright
    "Amy walks in, with Shawn close on her heels."
    "He seems to be in the middle of saying something to her."
    "But she's only half listening as she scans the pub for me."
    "I half stand and wave until she spots me and begins to walk over."
    "Okay..."
    "Here we go!"
    show amy at left4 with ease
    mike.say "Hey, Amy!"
    show shawn at right5 with ease
    mike.say "Hey, Shawn!"
    "I do the best I can to keep my greeting for each of them similar."
    show amy happy zorder 2 at center, zoomAt (2.0, (640, 1300))
    with hpunch
    "But Amy kind of blows that by instantly sprinting over the hug me."
    amy.say "Hi, babe!"
    hide amy
    show amy kiss zorder 2
    $ amy.flags.kiss += 1
    "Then she plants a pretty intense kiss on my lips to seal the deal."
    "Normally I'd be more than up for this and try to keep it going as long as possible."
    "But right now I can see the look on Shawn's face as he reacts to the kiss."
    "He's smiling, doing the best he can to look like he's cool with it."
    "But his smile is in danger of turning into a grimace more with each passing second."
    "And sure, I could call him bitter and a sore loser."
    "Yet he did agree to come along for a drink and put the past behind him."
    "So what we're doing is kind of rubbing his nose in it."
    hide amy
    show amy zorder 2 at center, zoomAt (1.5, (340, 1040))
    with fade
    show amy at center, zoomAt (1.5, (340, 1140)) with ease
    "Amy finally ends the kiss and sits down next to me."
    hide shawn
    show shawn at center, zoomAt (1.5, (940, 1040))
    with fade
    show shawn at center, zoomAt (1.5, (940, 1140)) with ease
    "And looking relieved, Shawn does the same."
    mike.say "Erm..."
    mike.say "You guys are a little late getting here."
    mike.say "Is everything okay?"
    show shawn nice
    "Shawn looks relieved to be talking about something familiar."
    "He shakes his head and launches into an explanation for my benefit."
    shawn.say "Oh, man..."
    shawn.say "You wouldn't believe it!"
    shawn.say "People will tell you working in retail is easy."
    shawn.say "But the truth is..."
    show amy annoyed at center, zoomAt (1.5, (540, 1140)) with ease
    amy.say "Oh shut up, Shawn!"
    "Shawn and I both turn to stare at Amy as she cuts him off."
    show amy normal at center, zoomAt (1.5, (340, 1140)) with ease
    show shawn annoyed
    amy.say "I was there with you all day."
    amy.say "I already know how it was!"
    mike.say "Erm..."
    mike.say "I wasn't there, Amy!"
    show shawn angry
    shawn.say "Yeah, Amy..."
    shawn.say "I was trying to tell [hero.name], not you!"
    amy.say "Well I know it's a boring story too."
    amy.say "So I'm saving him the pain of hearing it!"
    amy.say "Anyway, he has something much more exciting to tell you."
    amy.say "Don't you, [hero.name]?"
    show shawn normal
    "I shoot Amy a questioning glance."
    "But she just nods her head towards Shawn, trying to urge me on."
    "Shawn looks at her for a moment."
    "Then he turns his gaze towards me instead."
    shawn.say "What's she talking about?"
    show fx question at right5
    shawn.say "What have you got to tell me?"
    "Damn it!"
    "I was hoping to be able to build up to this naturally."
    "You know, buy Shawn a few rounds of birthday drinks?"
    "Get him comfortable and opening up about stuff."
    "Then work my way round to talking about matters of the heart."
    "Or more likely desires of the flesh!"
    "Now I have no choice but to come right out with it!"
    mike.say "Well..."
    mike.say "You know how you have a thing for Amy here?"
    shawn.say "Yeah."
    mike.say "And you remember how we made a little film for you?"
    shawn.say "Of course I do!"
    show shawn sad
    shawn.say "Wait...you're not trying to blackmail me, are you?"
    shawn.say "Did you get a back-up of my hard-drive or something?!?"
    "I wave my hands in front of me."
    "Trying to stop Shawn before he says something he'll regret."
    show shawn normal
    mike.say "No, no, no!"
    mike.say "We were just thinking, Amy and I..."
    mike.say "What if...what if we let you get involved one time?"
    mike.say "Like, as a birthday present?"
    "Shawn looks at me in sheer amazement."
    "Like he can't quite believe what he's hearing."
    shawn.say "You mean me..."
    shawn.say "And her..."
    shawn.say "And you?!?"
    mike.say "Yeah, Shawn..."
    mike.say "That's pretty much the size of it."
    amy.say "So what do you say, Shawn?"
    "Strangely Shawn seems to have second thoughts."
    menu:
        "Motivate Shawn":
            mike.say "Come on Shawn! I know you want it!"
            shawn.say "Hmmm..."
            show shawn happy
            shawn.say "I get it, guys."
            shawn.say "I can take a joke!"
            "Amy and I exchange a puzzled glance."
            "And then we turn our gazes back to Shawn."
            mike.say "What are you talking about, Shawn?"
            amy.say "Yeah - what joke?"
            "It takes a moment for what we're saying to sink in."
            "And in that time, Shawn keeps on smiling and shaking his head."
            "But slowly I see his expression begin to change."
            "He stops laughing and leans in towards us."
            show shawn normal
            shawn.say "Oh fuck..."
            shawn.say "You aren't joking, are you?"
            shawn.say "This is for real!"
            mike.say "Erm..."
            mike.say "Yeah, Shawn!"
            mike.say "Have you ever heard me joke about this kind of thing before?"
            show amy annoyed
            amy.say "Of course we're not joking, you ass!"
            amy.say "This was the whole reason for us asking you here."
            show amy normal
            shawn.say "Oh..."
            shawn.say "I thought it was just because you were my mates!"
            "Amy and I exchange another glance at this."
            "And instantly we both start reassuring Shawn."
            mike.say "Well..."
            mike.say "That too, obviously!"
            show amy shy
            amy.say "Sure, sure..."
            amy.say "The threesome is kind of your birthday present!"
            "This seems to do a great deal to improve Shawn's mood."
            "So much so that he downs his drink and then claps his hands together."
            show amy normal
            shawn.say "Okay then..."
            shawn.say "Shall we get started?"
            "Amy and I take this as a yes."
            "And we follow Shawn's lead, finishing off our own drinks too."
            amy.say "We should head over to my place."
            amy.say "I live closest."
            amy.say "Plus I don't have any housemates."
            scene bg street at blur(16), dark with dissolve
            "This earns her a round of nods as we head out of the door."
            scene bg black with dissolve
            scene bg amyhome with wipeleft
            "And pretty soon we find ourselves piling into Amy's apartment."
            show amy at left5 with easeinright
            show shawn at right5 with easeinright
            "It's a small place, and I don't take in many of the details."
            "Because we head straight to get things started."
            "But that doesn't mean Shawn and I leap into action."
            "Instead we find ourselves exchanging awkward glances."
            show fx question at left5
            amy.say "What's the matter with you two?"
            amy.say "Oh, I think I see what the problem is here."
            amy.say "You've never had a threesome before, have you?"
            show shawn sad
            shawn.say "Hey!"
            shawn.say "I might have!"
            mike.say "Yeah, Amy - me too!"
            mike.say "Just...not with him..."
            show shawn normal
            "Amy shakes her head at the pair of us."
            "And then, without another word, she begins to take off her clothes."
            "Shawn and I are suddenly hypnotised by the sight."
            "Our eyes are all over Amy, unable to focus on anything else."
            "She takes off one item of clothing after another."
            show amy underwear with dissolve
            "Her movement are slow, suggestive and obviously seductive."
            "As I watch her, I can almost feel my nerves melting away."
            "And taking a quick glance at Shawn, I see the same thing is happening to him too."
            "Now I see why Amy chose to take the lead."
            "She's reminded us of why we're really here."
            "Of the fact that we both want her desperately."
            "Enough to forget about our hang-ups towards getting it on together."
            "I don't know if it's Shawn or me that begins to move first."
            "But either way we're both soon stripping our clothes off."
            show amy naked with dissolve
            "Amy's naked by now, her body on full display."
            "And she shows it off even more by moving in a suggestive manner."
            "All it takes is one glance back over her shoulder."
            "And that's it, I can't stand back and watch any longer."
            hide shawn with moveoutright
            show amy at center with move
            "Almost forgetting about Shawn, I move toward her."


            show electronic 3some mikeamydoggy with fade
            "She squeals in surprise as my hands grab hold of her waist."
            "Already focused on the task at hand, I pull Amy backwards."
            "A move that thrusts my stiffening cock between her thighs."
            "Instantly I feel the heat Amy's giving off."
            "And a moment later the head of my cock slides along the lips of her pussy."
            "And I do mean slides as well, letting me know just how turned-on Amy is right now!"
            amy.say "Ah..."
            amy.say "What are you waiting for?"
            amy.say "I'm ready now!"
            amy.say "Why aren't you fucking me already?"
            "Amy's words are like an irresistible command to me."
            menu:
                "Fuck her pussy":
                    $ hole = "vaginal"
                "Fuck her ass":
                    $ hole = "anal"
            $ renpy.show(f"electronic 3some mikeamydoggy {hole}")
            "And a few seconds later, I begin to act on them."
            show electronic 3some mikeamydoggy mouth_tongueout eyes_wink
            "She's not passive either, reaching down with one hand."
            "I feel her fingers close around the shaft of my cock."
            "Then she pushes it home, making sure I find my way."
            "It doesn't take long for the lips of her pussy to surrender."
            "They part a little at a time, and I begin to inch inside of her."
            show electronic 3some mikeamydoggy shawn eyes_up with fade
            shawn.say "Oh man..."
            shawn.say "Somebody pinch me!"
            shawn.say "Is this really happening to me?"
            "As one, Amy and I look up to see Shawn standing in front of us."
            "In the heat of the moment, we seem to have forgotten he was there."
            "But he's hard to miss, totally naked and his cock standing to attention!"
            show electronic 3some mikeamydoggy blowjob
            "Without missing a beat, Amy reaches for it, just like she did with mine."
            "And Shawn's eyes go wide as she guides it between her lips."
            "As Amy begins to move her head back and forth, I snap back to reality."
            show electronic 3some mikeamydoggy eyes_wink
            "And I start to move too, thrusting with a similar speed and motion."
            "The sensation of being inside her is incredible."
            "But my worry was that I'd find Shawn's presence to be a distraction."
            "That his presence would somehow keep me from being able to perform."
            show electronic 3some mikeamydoggy eyes_open
            "Yet my eyes are drawn away from him and down towards Amy instead."
            "The sight of her working on him with her mouth captures all of my attention."
            "It's almost like being treated to a show as I make love to her."
            "And rather than putting me off, it spurs me on to try harder."
            "Somehow the enthusiasm I'm showing doesn't get in Amy's way."
            show electronic 3some mikeamydoggy eyes_close
            "She bucks and wriggles as I move inside of her."
            "But she still manages to keep her head pretty much level."
            "My urge is to go faster and harder the whole time."
            "To push Amy as far as I possibly can."
            "At first I'm afraid to do that, worried it'll be too much for her."
            "But then I catch a glimpse of what Amy's doing from a different angle."
            show electronic 3some mikeamydoggy eyes_open
            "And instantly I can see that she's taken Shawn seriously deep into her mouth."
            "In fact, I swear that she's pretty much deep-throating him!"
            "If she's doing that while I'm going at a pace like this..."
            "Well, she should be able to handle anything I can throw at her!"
            show electronic 3some mikeamydoggy speedfx eyes_surprised at startle(0.05, -10)
            "And that proves to be the case as I pick up speed."
            "Soon enough I'm gasping from the increased effort."
            "Which blends strangely with the sound of Shawn doing the same."
            show electronic 3some mikeamydoggy eyes_up at startle(0.05, -10)
            "He sounds like he's not going to be able to hold on for much longer."
            "And I know that I'm in the same position."
            "But it also seems like Amy knows as much too."
            show electronic 3some mikeamydoggy mikeout eyes_open -speedfx -blowjob at startle(0.05, -10)
            "Before either of us can lose control, she springs into action."


            "This simultaneously drags my cock out of her and Shawn's out of her mouth."
            "And in the confusion that follows, the two of us are left panting and stunned."
            "But Amy doesn't show any such confusion, instead going straight into action."
            show electronic 3some shawnamyspoon mike mouth_ahegao with vpunch
            "She turns around, putting her back to Shawn."
            show electronic 3some shawnamyspoon blowjob eyes_hurt
            "Then she leans in close and takes my cock into her mouth."
            "In the blink of an eye she's working on me in the same way as she was Shawn."
            "I don't even have time to say a word before my cock is as in her mouth."
            "Shawn, on the other hand, is left standing there for a few moments longer."
            "That is until Amy reaches back and grabs hold of his cock."
            "Once she has hold of it, she gives it what looks like a painful squeeze."
            "That's more than enough to snap Shawn out of it."
            "He lets out a yelp of pain and then leaps forwards."
            "A moment later he puts his hands in the same place I had them."
            $ renpy.show(f"electronic 3some shawnamyspoon {hole} eyes_ahegao")
            "And he makes to push his way into Amy."
            "Where there was resistance for me, Shawn finds it much easier."
            "He all but slips straight inside in one smooth motion."
            "Again Shawn seems to almost jolt into action without a conscious thought."
            show electronic 3some shawnamyspoon eyes_closed
            "Suddenly he starts to make the same motions that I was in his position too."
            "And within moments he's thrusting away like he's been there from the start."
            "Now it's my turn to be the one standing almost totally still."
            "Because there's nothing else for me to do as Amy goes to work down there."
            "It's almost surreal to have swapped places halfway through like this."
            "Like stepping from one side of the looking glass to the other."
            "But one thing that's for certain is that we can't go on forever."
            show electronic 3some shawnamyspoon hairpulled
            "Shawn and I were already on the verge of losing it when Amy made us swap over."
            "Which means that now we're back into it with as much passion, it doesn't take long."
            "I can feel that same pressure building up inside of me."
            show electronic 3some shawnamyspoon eyes_hurt out -blowjob
            "And soon enough the sounds of gasping fill the air for a second time."
            "Just like the first time, Amy seems to hear them clearly."


            "Because she reacts by turning again, pulling both cocks out for a second time."
            show electronic 3some bukkake eyes_open with fade
            "But instead of changing directions, she knees between Shawn and me."
            show electronic 3some bukkake lhandup rhandup
            pause 0.25
            show electronic 3some bukkake lhanddown rhanddown
            pause 0.25
            show electronic 3some bukkake lhandup
            pause 0.25
            show electronic 3some bukkake rhandup lhanddown
            pause 0.25
            show electronic 3some bukkake rhanddown lhandup
            pause 0.25
            show electronic 3some bukkake rhandup lhanddown
            pause 0.25
            show electronic 3some bukkake rhanddown
            "This means that as we cum, she gets a hit from two directions at once."
            show electronic 3some bukkake amyhandpose
            pause 0.35
            show electronic 3some bukkake mikehandmiddle
            pause 0.25
            show electronic 3some bukkake mikehanddown shawnhandmiddle
            pause 0.25
            show electronic 3some bukkake mikehandmiddle shawnhanddown
            pause 0.25
            show electronic 3some bukkake mikehanddown shawnhandmiddle eyes_up
            pause 0.25
            show electronic 3some bukkake mikehandmiddle shawnhanddown
            pause 0.25
            show electronic 3some bukkake mikehanddown shawnhandmiddle
            pause 0.25
            show electronic 3some bukkake shawnhanddown
            pause 0.25
            "She strikes a pose as she prepares to receive both of us cum."
            show electronic 3some bukkake mikehandmiddle
            pause 0.25
            show electronic 3some bukkake mikehandup mikedickcum eyes_close
            pause 0.25
            show electronic 3some bukkake cumfaceleft with vpunch
            pause 0.25
            show electronic 3some bukkake cumtongueout with vpunch
            pause 0.25
            show electronic 3some bukkake cumleftbreath with vpunch
            pause 0.25
            show electronic 3some bukkake eyes_open
            "I cum a few seconds before Shawn, hitting one side of Amy's face."
            show electronic 3some bukkake shawnhandmiddle
            pause 0.25
            show electronic 3some bukkake shawnhandup shawndickcum eyes_close
            pause 0.25
            show electronic 3some bukkake cumfaceright with vpunch
            pause 0.25
            show electronic 3some bukkake cumbody with vpunch
            pause 0.25
            show electronic 3some bukkake cumrightbreath with vpunch
            pause 0.25
            show electronic 3some bukkake eyes_open
            "Then the other gets spattered by his cum a moment later."
            show electronic 3some bukkake -cumtongueout mouth_yumy
            "Amy smiles and laughs as her face is covered, licking up what she can."
            "Shawn and I are staring at her the whole time."
            "Totally amazed at the sight of what she's doing."
            $ amy.sexperience += 1
            $ amy.flags.electronic_harem_delay = TemporaryFlag(True, 5)
            if renpy.has_label("electronic_harem_achievement_1") and not game.flags.cheat:
                call electronic_harem_achievement_1 from _call_electronic_harem_achievement_1
        "Shame Shawn":

            mike.say "Come on Shawn... It's so pitiful to see you alone all the time..."
            mike.say " Take the chance! That might be the only time you can have sex with real people."
            show shawn angry at center, zoomAt (1.0, (940, 1040)), vshake
            "Shawn stands up and pushes his chair backwards."
            "In fact he does it so quickly Amy and I jump."
            "But there's no time to recover before he opens his mouth."
            show shawn annoyed
            shawn.say "Are you guys taking the piss, or what?"
            shawn.say "You invite me here, on my bloody birthday..."
            shawn.say "And then you ask me something like that!"
            show amy annoyed
            "Amy's already frowning across the table at Shawn."
            amy.say "What's the problem, Shawn?"
            amy.say "I thought that was what you wanted?"
            shawn.say "I wanted to have sex with YOU, Amy!"
            show shawn angry
            shawn.say "Not him!"
            "I almost feel the sensation of being poked as Shawn jabs a finger towards me."
            shawn.say "This is like rubbing my face in it."
            shawn.say "Like offering me your sloppy seconds!"
            mike.say "Erm..."
            mike.say "If that's the problem, Shawn..."
            mike.say "Then you can always go first!"
            mike.say "You'll finish quick enough so I can wait my turn."
            show shawn annoyed
            shawn.say "I meant in a metaphorical sense!"
            shawn.say "At least I think that's what I meant..."
            shawn.say "Anyway...I'm leaving!"
            if not game.calendar.season_name == shawn.birthday[0] and not game.day == shawn.birthday[1]:
                shawn.say "That wasn't even my birthday in the first place..."
            hide shawn with easeoutright
            "I make to stand up as Shawn turns to leave the pub."
            show amy at center, zoomAt (1.5, (640, 1140)) with ease
            "But I feel Amy's hand holding onto my arm."
            "And I take the hint to let Shawn go."
            "Once he's stormed out of the place, Amy and I exchange a worried look."
            mike.say "I really don't think that could have gone any worse."
            amy.say "Yeah..."
            amy.say "Work's really going to suck thanks to this!"
            if Room.find("electronic").flags.discount:
                $ Room.find("electronic").flags.discount = 0
            $ Harem.leave_by_name("electronic", "amy")
    return

label electronic_harem_event_06:
    scene bg pub with fade
    "When Shawn asked me to meet him after he got off work today, I was a little hesitant."
    "I haven't really spoken to him since we had the threesome with Amy on his birthday."
    "And while all of that seemed to go down pretty well, it still feels a tad strange."
    "So I've kind of been avoiding Shawn if I could do it in a passive way."
    "You know, like I just need some time to process it all?"
    "But it's not as if I could turn him down either, now is it?"
    "Because that would make it look like I was avoiding him on purpose."
    "Which I am...but I don't want him to know that."
    "Anyway, I agree to meet up with him before I drive myself mad thinking about it."
    "And when he turns up, Shawn seems to be in good spirits."
    scene drink_room_pub
    show shawn date noglasses happy at center, zoomAt(1.75, (440, 1180))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    shawn.say "Hey there!"
    shawn.say "Thanks for meeting me, fella."
    mike.say "Hey, Shawn..."
    mike.say "It's never a bother to meet you."
    mike.say "Did you want to just hang out?"
    mike.say "Or was there something else you wanted?"
    show shawn normal
    "As soon as I ask the question, I see a change come over Shawn."
    "Before he was all smiles and positive vibes."
    "But now he looks awkward and embarrassed, almost pained."
    shawn.say "Ah..."
    shawn.say "There's no fooling you, is there!"
    show shawn nice
    shawn.say "I was just going to shoot the shit with you for a while."
    shawn.say "You know, work my way up to it?"
    shawn.say "But you just sniffed me straight out!"
    "I'm smiling as Shawn says all of this."
    "But I feel like my smile must be pretty awkward too."
    mike.say "Come on, Shawn - out with it!"
    mike.say "What's on your mind?"
    mike.say "And more importantly, what's it got to do with me?"
    show shawn embarrassed
    "Now Shawn look more pained and awkward than ever."
    "Because he can't hide behind conversational niceties anymore."
    "This is the point where he has to get down to it."
    "Or else lose the chance to say it altogether."
    shawn.say "Okay, okay..."
    show shawn normal
    shawn.say "It's a little bit about the three of us hooking up."
    shawn.say "And it's a little bit about something else..."
    "I frown at this, not totally able to make sense of what Shawn's saying."
    "I wanted him to clear things up, not make them more confusing!"
    mike.say "And what's that supposed to mean?"
    mike.say "Just come out and say it, Shawn."
    mike.say "I mean, I just arranged for you to have a threesome with me and Amy."
    mike.say "How much crazier can it be than that?"
    shawn.say "Well..."
    shawn.say "You remember how I had a thing for Palla too?"
    "I nod, my mind already dredging up the memories of that affair."
    shawn.say "It'd kind of be more honest to say that I still do!"
    shawn.say "Because I never really got over her."
    mike.say "Okay, Shawn..."
    mike.say "You still have the hots for your former housemate."
    mike.say "So what does that have to do with me?"
    "Shawn shrugs."
    shawn.say "Well I never thought that I'd have a chance with Amy."
    shawn.say "Not after you swooped in there and took her away from me."
    show shawn nice
    shawn.say "But then you turned round and offered me the chance to shag her!"
    shawn.say "And...well...that started me thinking about Palla too."
    shawn.say "Because you basically did the same thing with her."
    shawn.say "So I was wondering if you could..."
    "Suddenly realisation dawns on me."
    "And I know exactly what Shawn's after."
    "No wonder he couldn't just come right out and say it!"
    mike.say "You want me to arrange a threesome with Palla too?!?"
    shawn.say "Not exactly..."
    show shawn smug
    shawn.say "I was wondering if you could get Amy to jump in on it too?"
    shawn.say "Which would kind of make it a foursome..."
    menu:
        "Let me think about it...":
            "My instinct is to just come right out and say no."
            "Because I know Palla well enough to be wary of asking her for anything."
            "But then I make the mistake of letting my imagination get to work on the idea."
            "And the images that begin to fill my head are simply impossible to ignore."
            show shawn happy
            shawn.say "Aaah!"
            shawn.say "You're already thinking about it!"
            show shawn smug
            shawn.say "All those delightful possibilities, yeah?"
            "The sound of Shawn's voice snaps me out of it."
            "And the knowing tone he's using makes me more than a little embarrassed too."
            mike.say "What?"
            mike.say "No!"
            mike.say "I...well...yeah, you got me!"
            show shawn happy
            "Shawn lets out a cry of triumph."
            "And he literally punches the air."
            shawn.say "HA!"
            shawn.say "I knew you wouldn't be able to resist."
            mike.say "HEY!"
            mike.say "I didn't say I was going to do it yet."
            mike.say "Just that I was thinking about it."
            show shawn nice
            shawn.say "But now the idea's lodged in there..."
            shawn.say "Isn't it?"
            "Shawn taps a finger against his forehead."
            shawn.say "And the only way to get it out is to make it a reality!"
            mike.say "Okay, Shawn..."
            mike.say "You win."
            mike.say "I'll talk to Palla, see what she thinks of the idea."
            mike.say "But that's all I can promise you."
            show shawn happy
            "This seems to be enough to satisfy Shawn."
            "He nods his head eagerly."
            shawn.say "Of course, of course..."
            shawn.say "But I know that you'll be doing your best to convince her."
            show shawn nice
            shawn.say "Just so long as you keep those possibilities in mind!"
            "I nod and then make an effort to change the subject."
            "Already wondering how in the hell I'm going to pull this one off."
            $ game.flags.electronic_foursome = True
        "Absolutely not, you greedy little man!":
            "The moment that I hear what Shawn's actually asking for, I take a step backwards."
            "At the same time I'm shaking my head and refusing to look him in the eye."
            mike.say "Oh no!"
            mike.say "Tell me you did not just ask me to do that."
            mike.say "Tell me you did not just ask for me to get another body involved!"
            "Shawn's reaction is the complete opposite to mine."
            "He does the best he can to move closer to me."
            "And he's holding out his hands, shaking his head in surprise."
            show shawn nice
            shawn.say "Oh come on, man!"
            shawn.say "What's with the sudden change of heart?"
            shawn.say "How is a foursome that much more crazy than a threesome?!?"
            mike.say "Because it's involving another person, that's how!"
            mike.say "Three people is only one step removed from a couple."
            mike.say "Sure, it's more complicated and potentially messier."
            mike.say "But not enough to make it daunting."
            mike.say "Four people is like two entire couples-worth of people being mashed together!"
            mike.say "Just imagine all the permutations of resentment and recrimination!"
            mike.say "And on top of all that, you know Palla as well as I do."
            mike.say "She's kind of high-maintenance!"
            show shawn normal
            "I can see that Shawn wants to argue the toss with me."
            "But the mention of Palla's actual character seems to make a difference."
            "He knows as well as I do that she's a totally different girl to Amy."
            "And that seems to be enough to make him rethink his plans."
            show shawn embarrassed
            shawn.say "Yeah..."
            shawn.say "I guess she can be a bit of a pill!"
            shawn.say "But I still think we could have made it work."
            "Shake my head, making my own position clear."
            mike.say "Maybe in another lifetime, Shawn!"
            "This earns me a grunt from Shawn."
            "And he swings a kick at an imaginary target."
            shawn.say "Okay, okay..."
            shawn.say "I get the message."
            shawn.say "Let's talk about something else instead..."
            "I nod and we move on to different things."
            "And I really do hope that Shawn's telling the truth."
    return

label electronic_harem_event_07:























    "I take a deep breath and prepare myself."
    "Then I let it out and jump right in."
    mike.say "Shawn called me up the other day."
    mike.say "I take it you remember him?"
    show palla surprised
    "Palla raises any eyebrow at the mention of Shawn's name."
    "Which at least tells me that she has some vague interest in him."
    palla.say "Of course I remember Shawn."
    show palla joke
    palla.say "Awkward little nerdy guy."
    palla.say "Is he still slaving away in that ghastly electronics store?"
    mike.say "Yeah..."
    mike.say "That's Shawn all right!"
    mike.say "Well...you also remember that he had a thing for you?"
    show palla flirt
    "Palla raises her eyebrows and her smile lengthens."
    "But I can tell that she's still trying to appear nonchalant."
    palla.say "He did?"
    palla.say "Well, I suppose that's only natural."
    palla.say "I do tend to have that effect on his type!"
    palla.say "But when you're me, it's hard to even notice a guy like him."
    "I sigh and shake my head."
    mike.say "Okay, Palla..."
    mike.say "Let's just take it as read that he does."
    mike.say "And that he got in touch the other day to ask me to ask something."
    mike.say "Specifically if you'd be willing to get involved with something we're planning."
    show palla blank
    show fx question
    "Palla cocks her head on one side, doing the best she can to seem disinterested."
    "But the very fact that she's listening at all tells me she wants to hear me out."
    "Because if not, she'd have simply told me to get lost!"
    hide fx
    mike.say "The thing is, Palla..."
    mike.say "Shawn and I are going to hook up with a girl called Amy."
    mike.say "In fact we already did, and it went so well we're doing it again."
    mike.say "And we were wondering if you wanted to get in on it too?"
    if palla.love >= 150 and palla.lesbian >= 10:
        "I keep a close eye on Palla's expression as I ask the question."
        "And I'm sure I can see a subtle change as she takes it all in."
        show palla flirt
        palla.say "You know what, [hero.name]..."
        palla.say "I'm going to make your day and say yes."
        palla.say "Probably give Shawn the highlight of his sad little life too!"
        "Even though I've been waiting with baited breath, it still comes as a surprise."
        "And I have to ask Palla to be sure."
        mike.say "Are you serious, Palla?"
        mike.say "You're saying that you'll do it?"
        "Palla gives me a quiet chuckle."
        "Then she nods her head."
        show palla normal
        palla.say "Yes, [hero.name]..."
        palla.say "I'm in."
        show palla flirt
        palla.say "Let's just say it amuses me to think of Shawn holding a torch for me all this time."
        show palla normal
        palla.say "And I'm curious to meet this Amy girl too."
        mike.say "That's great news, Palla!"
        mike.say "Leave all the arrangements to me."
        mike.say "And I'll be in touch to get all of the details sorted."
    else:



        show palla angry
        "Palla doesn't need to seem any time to consider it."
        "Instead she snorts with laughter and shakes her head."
        palla.say "Ha!"
        palla.say "Oh my god!"
        palla.say "Please tell me that you're joking?"
        "I do the best I can to keep a serious look on my face."
        "But it's hard with Palla literally laughing in it."
        mike.say "Erm..."
        mike.say "No, Palla..."
        mike.say "I'm totally serious."
        mike.say "We're planning another threesome."
        mike.say "And we'd like you to make it a foursome."
        show palla annoyed
        $ palla.love -= 5
        $ palla.sub -= 5
        "Palla's shaking her head by now."
        "Even wiping a tear from the corner of her eye."
        palla.say "Oh, [hero.name]..."
        show palla angry
        palla.say "I'd rather pull out my own nails with a pair of rusty pliers!"
        palla.say "But thanks for asking me."
        palla.say "You've really cheered me up!"



        $ game.flags.electronic_foursome = False
    return

label electronic_harem_event_08:
    "Part of me's starting to think that I was a moron to take all of this on myself."
    "I mean first I let Shawn talk me into it, then I was the one to reach out to Palla."
    "I had to put up with her quirky ways in order to get her on the same page."
    "And now I'm going to have to be the one to do the same thing with Amy too!"
    "What the hell has Shawn done so far?"
    "Nothing, that's what!"
    "But I keep reminding myself that's because he probably couldn't pull it off."
    "If he could, he'd have been doing all of this himself, right?"
    "So maybe I should be patting myself on the back for being the right man for the job."
    "Now all I have to do is convince Amy that she should jump on this thing too!"
















    mike.say "Amy... I have something to ask you."
    mike.say "And yeah, it's got a lot to do with Shawn too."



    amy.say "What does he want now, huh?"
    amy.say "Another chance to play with the two of us?"
    mike.say "You're getting warm, Amy."
    mike.say "But it's a little different this time."
    show amy puzzled
    show fx question
    "Amy raises her eyebrows."
    "Letting me know that I've piqued her interest."
    amy.say "How is it different?"
    hide fx
    mike.say "Well..."
    mike.say "Shawn wants to get someone else involved this time."
    mike.say "A girl we both know called Palla."
    "Amy looks more intrigued than outraged at the idea."
    "Which has to be a good thing, right?"
    show amy flirt
    amy.say "Palla?"
    amy.say "Is that the same Palla he used to live with?"
    mike.say "Yeah, that's the one."
    amy.say "Wow..."
    amy.say "That guy must be a glutton for punishment!"
    show amy normal
    amy.say "From what he told me, she tore his heart out."
    amy.say "And then she stomped on it for good measure!"
    "I shrug and let out a sigh."
    mike.say "All of that's true."
    mike.say "But I already spoke to her."
    mike.say "And she's agreed to the idea."
    mike.say "So the only person left to ask is you."
    if amy.love >= 150 and amy.lesbian >= 10:
        show amy shy
        "Amy doesn't answer me straight away."
        "Instead she seems to be pondering it."
        "And when she finally speaks, it's not to say what I was expecting either."
        show amy normal
        amy.say "So..."
        amy.say "You think this Palla girl is pretty?"
        mike.say "Erm..."
        mike.say "I guess some people would say she is!"
        amy.say "Is she prettier than me?"
        "A million different answers flash through my mind in the second before I answer."
        "And most of them are sure to land me in hot water with Amy."
        mike.say "No, Amy..."
        mike.say "She's pretty...but in a different way!"
        "I'm expecting Amy to be mad at me."
        "So it comes as some surprise when she bursts out laughing."
        show amy happy
        amy.say "You guys are SO predictable!"
        amy.say "You're all terrified of telling a girl that another girl's pretty!"
        show amy normal
        amy.say "Tell you what, [hero.name]..."
        amy.say "I'm going to say yes to the foursome."
        amy.say "Because I want to see this Palla for myself."
        amy.say "That way I can see what all the fuss is about!"
    else:






        show amy mad
        "Amy shakes her head."
        "And as she does so, I feel my hope dwindling away to nothing."
        show amy upset
        amy.say "Nah..."
        amy.say "It's gonna be a hard pass from me!"
        mike.say "Really, Amy?"
        mike.say "You sounded interested just now."
        mike.say "Back when you thought it was another threesome."
        amy.say "You said it yourself right there."
        amy.say "When I thought it was a threesome!"
        amy.say "A foursome makes it totally different."
        "Now it's my turn to frown."
        mike.say "Oh come on, Amy!"
        mike.say "It's just one more person."
        mike.say "Plus Palla's really hot too!"
        show amy mad
        "When Amy looks me in the eye, I know she won't budge."
        "I can see it in the hard stare she's giving me."
        amy.say "Then the two of you should totally have a threesome with her."
        amy.say "Do that and leave me out of it."
        show amy angry
        amy.say "Because this is getting out of hand!"
        amy.say "First it was the sex-tape."
        amy.say "Then it was a threesome."
        amy.say "Now it's a foursome!"
        amy.say "Where's it going to end?"
        amy.say "And how come you're letting Shawn manipulate you like this?"
        "That question takes me by surprise."
        "Because it really hits a nerve."
        mike.say "What?"
        mike.say "I am not being manipulated!"
        show amy upset
        amy.say "That's not what it looks like to me."
        amy.say "Look, [hero.name]..."
        amy.say "I'm not doing it, and that's my final word."
        amy.say "Maybe call me when you want to do something that's just the two of us for a change?"



        $ game.flags.electronic_foursome = False
    return

label electronic_harem_event_09:
    "As soon as I know that everyone's on board and the time's been arranged, I head out of the door."
    scene bg secondfloor at flip, center, zoomAt(5.5, (150, 3040)), dark with fade
    "And I make my way straight over to Amy's place, not stopping once before I find myself on her doorstep."
    play sound door_bell
    "I ring the door-bell, fully expecting to be greeted by Amy herself."
    scene bg black with dissolve
    scene bg amyhome at dark
    show shawn at center, zoomAt(1.25, (640, 940))
    with wiperight
    "So it comes as quite a shock to find Shawn grinning at me on the other side of the door!"
    show shawn happy
    shawn.say "Hey, man..."
    shawn.say "What took you so long?"
    shawn.say "Hurry up and get your arse in here!"
    scene bg amyhome with fade
    "Still a little surprised, I do as Shawn says, stepping into the hallway of Amy's apartment."
    play sound door_slam
    show shawn at right with easeinright
    "Shawn slams the door closed behind me, still looking almost manically excited."
    "But then he would be, when you consider what we're supposed to be getting together to do."
    mike.say "You certainly didn't waste any time getting here, Shawn!"
    mike.say "I mean, I came as soon as I knew it was on."
    mike.say "But I thought you were coming from further away?"
    show shawn nice at center with ease
    shawn.say "I booked a taxi and hot-footed it over as soon as I heard too."
    shawn.say "But I guess I'm just that little bit more motivated than you!"
    "I shake my head and let out an amused chuckle."
    "But I choose not to challenge Shawn for the sake of keeping the peace."
    "And my tolerance is rewarded a moment later."
    "As well as hearing the voices of the girls, I see a trail of their clothes too!"
    show shawn happy at mostleft4
    show amy flirt naked at right4
    show palla flirt naked at right
    with easeinright
    amy.say "Hi, [hero.name]..."
    amy.say "Am I ever glad to see you!"
    palla.say "Me too, [hero.name]..."
    palla.say "Because now we can finally get started!"
    "I really should say something equally positive in response to that."
    "Or at least throw a couple of compliments their way to keep up the positive vibes."
    "But instead I find myself simply staring at Amy and Palla as they recline on the sofa."
    hide shawn
    hide amy
    hide palla
    show electronic 4some bj
    with fade
    "And I can't keep the smile on my face from becoming even wider as I take it all in."
    "If I saw just one of them lying there naked, I'd be more than impressed."
    "So seeing the pair of them together is something I won't be quick to forget."
    "Part of me would be happy to just stand here and stare at them all night..."
    show shawn nice at center, zoomAt(1.75, (0, 720)) with easeinleft
    shawn.say "Come on, [hero.name]..."
    shawn.say "What are you waiting for?!?"
    "I turn my head to look in Shawn's direction."
    "And I see that he's already starting to undressed himself."
    hide shawn with easeoutleft
    "That's enough to make me shake my head and follow suit."
    "Not because I feel like I have to race against Shawn."
    "More to show willing and make sure things play out as they're supposed to."
    "All the time that Shawn and I are stripping-off, the girls are watching us with interest."
    "More then once I see Amy and Palla lean their heads together."
    "Then they converse with hands over their mouths, keeping what they say secret."
    "I don't know if they're actually discussing what they're seeing."
    "Or else it's all part of an act to make us feel nervous."
    "But either way I make an effort to speed things up on my part."
    "And pretty soon I'm standing before them totally naked."
    scene bg black
    show electronic 4some bj mike
    with fade
    mike.say "Looks like we're all ready to go."
    mike.say "So shall we get started?"
    shawn.say "Whoa..."
    shawn.say "Wait a second..."
    "All three of us turn to see Shawn hopping up and down on the spot."
    "He's halfway out of his shorts and still trying to pull off one of his socks."
    "And that's the very moment he manages to topple over and land in a heap on the floor!" with vpunch
    mike.say "Yeah, we really need to get moving."
    mike.say "Before Shawn hurts himself!"
    amy.say "So..."
    amy.say "How are we going to do this?"
    palla.say "Yeah..."
    palla.say "Who's going to be doing who?"
    "I take one last glance at Shawn."
    "And I see that he's still in a heap on the floor."
    mike.say "Looks like I'm going to have to be the one to take charge here!"
    menu:
        "Fuck Amy":
            "I walk the rest of the short distance to the sofa."
            "And then walk around it, looking down at the girls."
            "They both watch me intently the whole time."
            "Obviously wondering which one of them I'm going to make a play for."
            "Their eyes follow me and they turn their bodies to keep up."
            "So I get a pretty good chance to see them in motion."
            "But once I see Amy turn so that she's almost on all fours..."
            "Well, that pretty much makes up my mind for me!"
            scene bg black
            show electronic 4some fuckamy
            with fade
            mike.say "Here I come, Amy..."
            mike.say "Ready or not!"
            amy.say "Come on, [hero.name]..."
            amy.say "I'm right here waiting for you!"
            "Amy raises her ass in the air and gives it an inviting wiggle."
            "And the sight of her doing that assures me I made the right decision."
            "But at the same time, Palla doesn't seem so pleased with this turn of events."
            palla.say "Huh!"
            palla.say "What am I?"
            palla.say "Chopped liver?"
            "I hardly hear what Palla's saying as I pretty much pounce on Amy."
            "And when I grab hold of her, she lets out a squeal of delight."
            "Which is almost enough to make me forget that Palla's there altogether."
            shawn.say "Don't worry, Palla..."
            shawn.say "Your knight in shining armour is here!"
            "I'm just grabbing hold of Amy's buttocks as Shawn jumps onto the carpet."
            "He lands behind Palla, making her fall forwards and onto her front."
            "This means that her ass is sticking up in the air too."
            "Though it's by accident, rather than design."
            "Not that Shawn seems to notice."
            "On the contrary, he just assumes that she's offering herself up to him."
            "And so he does the same thing as me, clapping his hands onto Palla's buttocks."
            "The sound this makes is loud, but not as loud as the yelp that it elicits from her."
            palla.say "Yargh..."
            palla.say "Ouch!"
            palla.say "What the..."
            "But before Palla can say another word, Shawn springs into action."
            "I see him thrust himself forwards, pushing his cock between her thighs."
            "The effect this has on Palla is instant and visible."
            "And I can only assume that Shawn really does know what he's doing."
            "Because Palla almost goes cross-eyed as he begins to move back and forth."
            "All of her protests fade away, and instead she starts to moan with pleasure."
            "I'm still staring at the pair of them when I feel Amy's ass bump into me."
            "Surprised, I look down to see her gazing back at me over her shoulder."
            amy.say "Are we just going to watch them, or what?"
            amy.say "Because if we are, I wanna be in a more comfortable position!"
            "I shake my head and try as best I can to get myself back into the game."
            "The first thing I do is tighten my hold on Amy's flanks."
            "Then I pull her roughly backwards while I thrust forwards."
            "It's not exactly subtle, but I want to make up for lost time."
            "And luckily for me, that's a sentiment Amy seems to appreciate."
            show electronic 4some fuckamy pose1
            "She nods as she turns her head back to face forwards."
            amy.say "Oh yeah..."
            amy.say "Now we're getting somewhere!"
            amy.say "Oh...oh fuck yeah!"
            "The head of my cock starts to rub against the lips of her pussy."
            "And with each second that passes, I swear I can feel her getting more turned-on."
            "I can definitely feel Amy getting wetter though, as my cock begins to slip and slide."
            "Making an effort to control where it's going, I begin looking for a way inside."
            "Amy seems to be trying to help me with this all that she can."
            "Because I can feel the way she's pushing her ass back against me."
            "And with the two of us working towards the same goal, it doesn't take long."
            "Suddenly I feel something click, some meeting of pressure and resistance."
            "Whatever it is, we're both in the right place at the right time."
            "So as I push forwards, Amy opens up to me."
            show electronic 4some fuckamy pose2
            "With that one thrust, I go almost half the way in."
            "But even so, there's no chance for me to pause and savour the moment."
            "Because Amy pushes straight on, clearly wanting me to go all the way."
            "Not wanting to disappoint her, I do just that."
            "And soon I'm in a state of constant motion, moving back and forth."
            "But when I look up, I almost feel like I'm looking into a mirror."
            "Well, maybe a defective one that shows a less handsome reflection than my own!"
            "Because the motions that Shawn and Palla are making seem to be exactly the same as ours."
            "I don't know if it's deliberate, or just the result of us being in the same positions."
            "But even when I speed up or slow down the pace a little, Shawn still mirrors me."
            "And the way that Palla responds to him fucking her matches Amy's too."
            "I somehow manage to keep this uncanny fact from distracting me."
            "Though I have no idea if the others notice it at all."
            "I'm thinking this is going to go on for as long as we can keep it up."
            "But then something seems to happen to Shawn and Palla."
            "Either she ducks down or he pushes forwards too hard, or both at once."
            "And the result is that they go tumbling over into a heap."
            "I watch in amusement as Shawn's cock pops out of Palla."
            "Then as he scrambles around on top of her, trying to get it back in!"
            "All the time this is happening, I'm still going as hard as I can."
            "So hard in fact that I doubt Amy even knows what's happening in front of her."
            show electronic 4some fuckamy pose1
            "Instead she lowers her head almost to the floor."
            "And she gather's up handfuls of the carpet as she clenches her fists."
            amy.say "I..."
            amy.say "I can't..."
            amy.say "I can't...hold on!"
            "Amy's orgasm seems to rise up from somewhere deep inside of her."
            "And it's like I can feel it affecting my body as much as hers."
            "But once the full force of it hits, I know that she's going to take me with her too!"
            menu:
                "Cum inside":
                    "I don't have the presence of mind to be able to pull out in time."
                    "And it's all I can do to tighten my grip on Amy, then hold on until the end."
                    $ amy.love += 2
                    show electronic 4some fuckamy cum with vpunch
                    "This means that I shoot my load when I'm deep inside of Amy."
                    with vpunch
                    "The effect on her is dramatic, even though she's already in the grips of her own orgasm."
                    with vpunch
                    "She tosses her head and makes sounds like those of an animal in heat."
                    "So much so that everyone else seems to stop and watch until the moment passes."
                "Pull out":
                    call electronic_harem_event_09_bj from _call_electronic_harem_event_09_bj
        "Fuck Palla":










            "I walk the rest of the short distance to the sofa."
            "And then walk around it, looking down at the girls."
            "They both watch me intently the whole time."
            "Obviously wondering which one of them I'm going to make a play for."
            "Their eyes follow me and they turn their bodies to keep up."
            "So I get a pretty good chance to see them in motion."
            "But once I see Palla turn so that she's almost on all fours..."
            "Well, that pretty much makes up my mind for me!"
            scene bg black
            show electronic 4some fuckpalla
            with fade
            mike.say "Here I come, Palla..."
            mike.say "Ready or not!"
            palla.say "What?"
            palla.say "I thought you were going to..."
            show electronic 4some mike
            "Palla turns her head this way and that."
            "And she has a look of confusion written all over her face."
            "But I'm not in the mood to wait for her to get with the program."
            "And so I leap straight onto the floor and onto her in the same motion."
            "Palla let's out a yelp of surprise as my hands take hold of her around the waist."
            "But then the yelp turns into what I can only describe as a purr of amusement and arousal."
            palla.say "Well..."
            palla.say "If you want me that badly..."
            palla.say "I'd be crazy to say no!"
            "As if she needs to show me that she's willing, Palla gets down on all fours."
            "And then she raises her ass in the air, inviting me to take full advantage."
            "Of course I don't hesitate to do just that, because by now my blood is up."
            "And my cock is as hard as it's going to get at the thought of being inside her."
            show electronic 4some fuckpalla mikevaginal
            "As soon as I'm in position, I push it into the space between her thighs."
            "Thrusting forwards, I don't stop until I can feel what I'm aiming for."
            "Palla's pussy, neat, tight and getting wetter by the second!"
            show electronic 4some shawn
            "With a gasp of effort, I begin to move back and forth."
            "Drawing the head of my cock along the lips of her pussy."
            "As I do this, Palla lowers herself even more, spreading her legs wider."
            "All of her efforts make my job easier, and they encourage me to try harder."
            show electronic 4some fuckpalla shawnvaginal
            "Soon enough I can feel them beginning to pay off too, as she starts to open to me."
            "It's then that I choose to look up and suddenly remember we're not alone."
            "Shawn and Amy are right there in front of us, almost mirroring our positions."
            "In fact, as I start to push my way inside Palla, I see that Shawn's doing the same."
            "I don't know if it's deliberate on Shawn's part, as his eyes seem a little glazed over!"
            "But Amy seems to be aware of what's happening, showing her amusement with a wry smile."
            "The feeling is a little uncanny."
            "Like one of those skits where someone pretends to be another person's reflection."
            "So I do the best I can to shake it off and get back to the task at hand."
            "Unlike Amy, Palla doesn't seem to have noticed what's going on."
            "And so I throw myself into the task of fucking her with all the energy I have."
            "Pretty soon this means that she's nodding her head and gasping with approval."
            "And luckily for me, it's not a hard thing to enjoy being inside a girl like Palla!"
            "Though I'm trying hard to keep my mind on Palla and me."
            "I still can't help stealing the occasional glance at Shawn and Amy."
            "And when I do, it feels like I'm the one leading Shawn through a tutorial of some kind."
            "I swear that he's copying every move that I make, even down to the expression on my face!"
            "But if that's the case, then I guess I should be flattered."
            "Because it seems to be making this a memorable experience for Amy."
            "She's nodding her head the whole time, urging him on to greater heights."
            "And I'm getting the same results with Palla too."
            "Though I am trying to pull ahead of him, a little at a time."
            "So I can't help feeling a surge of triumph when I feel Palla starting to wriggle beneath me."
            palla.say "Oh god..."
            palla.say "I think..."
            palla.say "I think I'm going to cum!"
            menu:
                "Cum inside":
                    "Everything happens so fast from that moment on, it's hard to keep track."
                    $ palla.love += 2
                    show electronic 4some fuckpalla mikecum with hpunch
                    "One last thrust sees me losing it too, shooting my load deep into Palla."
                    with hpunch
                    "She instantly reacts, arching her back and letting out a cry of orgasmic pleasure."
                    show electronic 4some fuckpalla shawncum with hpunch
                    "And for once I'm not even tempted to look over and see what Shawn and Amy are doing."
                    "Instead I focus all of my attention on Palla, making sure she enjoys every last moment."
                "Pull out":
                    call electronic_harem_event_09_bj from _call_electronic_harem_event_09_bj_1









    $ amy.sexperience += 1
    $ palla.sexperience += 1
    scene bg amyhome
    show shawn smug at left
    show amy casual at right4
    show palla casual at mostright4
    with fade
    if renpy.has_label("electronic_harem_achievement_2") and not game.flags.cheat:
        call electronic_harem_achievement_2 from _call_electronic_harem_achievement_2
    "Once we're all cleaned up and getting dressed, reality slowly returns."
    "Everyone exchanges pleasantries and then begins to go off on their separate ways."
    "I have to admit, this was a lot of fun - far more than I expected it to be."
    "But part of me is hoping that everyone keeps the details of it to themselves."
    "Because I don't know how much more of this and how many more additional bodies I can take!"
    $ DONE["electronic_harem_event_09"] = game.days_played
    $ game.room = "map"
    return

label electronic_harem_event_09_bj:
    "Before I can surrender to the inevitable orgasm, Amy and Palla make their move."
    "It comes out of nowhere, taking Shawn and I by complete surprise."
    scene bg black
    show electronic 4some bj amy palla shawn mike
    with fade
    "As one they extricate themselves from out grasps and crawl onto the floor."
    "Naturally, Shawn and I make to follow them, standing up too."
    "And that's where they catch us, Amy grabbing me and Palla taking hold of Shawn."
    "Each one of them has a cock in her hand, and she seems to know exactly what to do with it!"
    show electronic 4some bj amyforth pallaforth
    pause 0.3
    show electronic 4some bj amyback pallaback
    pause 0.3
    show electronic 4some bj amyforth pallaforth
    pause 0.3
    show electronic 4some bj amyforth pallaforth
    pause 0.3
    show electronic 4some bj amyback pallaback
    pause 0.3
    show electronic 4some bj amyblowjob pallablowjob playrightboob
    "Amy takes mine into her mouth at the same moment I see Palla leaning towards Shawn's."
    "But that's the last thing that I can remember with any kind of clarity."
    "As after that, my senses are overwhelmed by one of the best blow-jobs I've ever had."
    "I can only think it's the energy in the room from the foursome that does it."
    "Amy uses her tongue, teeth and lips with expert precision."
    "Her head bobs up and down as she swallows me ever deeper."
    "And it comes as no surprise to me that the orgasm I can feel approaching seems to become more intense."
    "When it finally hits, there's simply nothing I can do to resist."
    show electronic 4some bj amyhandjob pallahandjob -playrightboob
    "As one, Amy and Palla stop what they're doing and sit back on their haunches."
    show electronic 4some bj amyforth pallaforth
    pause 0.3
    show electronic 4some bj amyback pallaback
    pause 0.29
    show electronic 4some bj amyforth pallaforth
    pause 0.28
    show electronic 4some bj amyback pallaback
    pause 0.27
    show electronic 4some bj amyforth pallaforth playleftboob
    pause 0.26
    show electronic 4some bj amyback pallaback
    pause 0.25
    show electronic 4some bj amyforth pallaforth
    pause 0.24
    show electronic 4some bj amyback pallaback
    pause 0.23
    show electronic 4some bj amyforth pallaforth
    pause 0.22
    show electronic 4some bj amyback pallaback palla_eyes_closed
    pause 0.21
    show electronic 4some bj amyforth pallaforth
    pause 0.2
    show electronic 4some bj amyback pallaback shawncum mikecum with hpunch
    pause 0.2
    show electronic 4some bj amyforth pallaforth
    pause 0.2
    show electronic 4some bj amyback pallaback with hpunch
    pause 0.2
    show electronic 4some bj amyforth pallaforth
    pause 0.2
    $ amy.love += 2
    $ palla.love += 2
    show electronic 4some bj amyback pallaback amyfacecum pallafacecum with hpunch
    pause 0.2
    show electronic 4some bj amyforth pallaforth
    pause 0.2
    show electronic 4some bj amyback pallaback
    pause 0.2
    $ amy.sub += 1
    $ palla.sub += 1
    show electronic 4some bj amyforth pallaforth amybodycum pallabodycum -shawncum -mikecum
    pause 0.2
    show electronic 4some bj amyback pallaback
    pause 0.2
    show electronic 4some bj amyforth pallaforth
    pause 0.2
    show electronic 4some bj amyback pallaback
    "This means the cocks flop out of their mouths, and then the inevitable happens."
    "I don't know if it's me or Shawn that shoots his load first."
    "Likewise I don't know if it's Amy or Palla that gets hit first."
    "Either way, they both seem to be painted with stripes of white at the same time."
    "Forehead, nose, cheeks and lips, all of them are spattered with cum."
    "And the girls don't move an inch as it runs down their faces, then drips off their chins."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
