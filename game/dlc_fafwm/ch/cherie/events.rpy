init python:
    
    Event(**{
        "name": "cherie_event_01",
        "label": "cherie_police_interview_male",
        "conditions": [
            IsHour(9, 18),
            IsDone("dwayne_corpse_discovery"),
            HeroTarget(
                IsGender("male"),
                IsRoom("bedroom1"),
                ),
            PersonTarget("cherie",
                ),
            ],
        "priority": 1000,
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Activity(**{
        "name": "cherie_event_02",
        "label": "cherie_event_02",
        "display_name": "Attend Dwayne's funerals",
        "icon": "dwayne",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_01"),
            IsHour(8, 11),
            HeroTarget(
                IsGender("male"),
                ),
            PersonTarget("cherie",
                MinStat("love", 20),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_03",
        "label": "cherie_event_03",
        "duration": 2,
        "conditions": [
            IsDone("cherie_event_02"),
            IsHour(9, 12),
            HeroTarget(
                IsGender("male"),
                IsActivity("run_park"),
                HasRoomTag("park"),
                ),
            PersonTarget("cherie",
                MinStat("love", 40),
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_04",
        "label": "cherie_event_04",
        "duration": 3,
        "conditions": [
            IsDone("cherie_event_03"),
            IsHour(18, 21),
            HeroTarget(
                IsGender("male"),
                InInventory("fancy_clothes"),
                ),
            PersonTarget("cherie",
                MinStat("love", 60),
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_05",
        "label": "cherie_event_05",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_04"),
            HeroTarget(
                IsGender("male"),
                IsRoom("office")),
            PersonTarget("cherie",
                IsFlag("cheriedelay", False)),
            PersonTarget("aletta",
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_06",
        "label": "cherie_event_06",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_05"),
            IsTimeOfDay("evening"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("home"),
                ),
            PersonTarget("cherie",
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_07_1",
        "label": "cherie_event_07_1",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_06"),
            IsHour(22, 1),
            IsDayOfWeek("123456"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("home"),
                ),
            PersonTarget("cherie",
                ),
            Or(
                IsDone("cherie_event_07_2"),
                PersonTarget("cherie",
                    IsFlag("cheriedelay", False),
                    ),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_07_2",
        "label": "cherie_event_07_2",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_06"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("work"),
                IsActivity("None"),
                ),
            PersonTarget("cherie",
                ),
            PersonTarget("aletta",
                HasRoomTag("work"),
                ),
            Or(
                IsDone("cherie_event_07_1"),
                PersonTarget("cherie",
                    IsFlag("cheriedelay", False),
                    ),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_08_1",
        "label": "cherie_event_08_1",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_07_1", "cherie_event_07_2"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("home"),
                IsActivity("None"),
                ),
            PersonTarget("cherie",
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_08_2",
        "label": "cherie_event_08_2",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_07_1", "cherie_event_07_2"),
            HeroTarget(
                IsGender("male"),
                IsActivity("work", "workhard", "work_personal", "workhard_personal"),
                ),
            PersonTarget("cherie",
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_event_09",
        "label": "cherie_event_09",
        "duration": 1,
        "conditions": [
            IsDone("aletta_event_08", "cherie_event_08_1", "cherie_event_08_2"),
            IsTimeOfDay("afternoon"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("work"),
                IsActivity("None"),
                ),
            PersonTarget("cherie",
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "aletta_judiciary",
        "label": "aletta_judiciary",
        "duration": 1,
        "music": "music/johny_grimes/levity.ogg",
        "do_once": True,
        "priority": 500,
        "conditions": [
            IsDone("cherie_event_09"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("mcoffice"),
                IsActivity("work", "workhard", "work_personal", "workhard_personal"),
                IsFlag("JudiciaryDelay", False),
                ),
            ],
        })
    
    BeforeDateEvent(**{
        "name": "cherie_event_10",
        "label": "cherie_event_10",
        "priority": 400,
        "duration": 2,
        "conditions": [
            IsDone("cherie_event_09"),
            IsHour(14, 17),
            IsSeason(0, 1),
            InInventory("swimsuit"),
            HasVehicle(motor=True),
            HeroTarget(
                IsGender("male"),

                ),
            PersonTarget("cherie",
                MinStat("love", 180),
                IsFlag("cheriedelay", False),
                OnDate(),
                ),
            ],
        "clothes": "casual",
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_preg_talk",
        "label": "cherie_preg_talk",
        "do_once": False,
        "conditions": [
            HeroTarget(
                IsActivity("None"),
                IsGender("male"),
                Not(OnDate()),
                ),
            PersonTarget(cherie,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinCounter("pregnant", 6),
                ),
            ],
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_sub_event_01",
        "label": "cherie_sub_event_01",
        "duration": 1,
        "conditions": [
            IsDone("cherie_event_06"),
            HeroTarget(
                IsGender("male"),
                IsActivity("work", "workhard", "work_personal", "workhard_personal"),
                ),
            PersonTarget("cherie",
                MinStat("sub", 25),
                MinStat("sexperience", 1),
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_sub_event_02",
        "label": "cherie_sub_event_02",
        "duration": 1,
        "conditions": [
            IsDone("cherie_sub_event_01"),
            IsHour(14, 20),
            HeroTarget(
                IsGender("male"),
                ),
            PersonTarget("cherie",
                MinStat("sub", 50),
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })
    
    Event(**{
        "name": "cherie_sub_event_03",
        "label": "cherie_sub_event_03",
        "duration": 1,
        "conditions": [
            IsDone("cherie_sub_event_02"),
            InInventory("slave_collar"),
            HeroTarget(
                IsGender("male"),
                IsActivity("work", "workhard", "work_personal", "workhard_personal"),
                ),
            PersonTarget("cherie",
                MinStat("sub", 75),
                IsFlag("cheriedelay", False),
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/focus.ogg",
        })

label cherie_preg_talk:
    $ cherie.flags.toldpreg = True
    show cherie normal at center, zoomAt(1.0, (640, 720))
    "As usual I have a pretty big smile on my face as Cherie shows up."
    "I'm just that happy to see her that I can't help letting it show."
    show cherie annoyed at center, traveling(1.5, 0.5, (640, 1040))
    "But as she comes closer, I can see that the look on her face is very different."
    "She looks stressed, her mouth set in a firm, hard line."
    "And the realisation that she's not in a good place right now changes my mood too."
    mike.say "Cherie..."
    mike.say "What's happened?"
    mike.say "Is everything okay?"
    show cherie sadsmile
    "Cherie shakes her head before she answers my questions."
    "And that's more than enough to let me know things aren't okay."
    show cherie whining
    cherie.say "[hero.name]…"
    show cherie talkative
    cherie.say "I am grateful that you came when I called."
    cherie.say "I have some news, and I am afraid that it is bad."
    cherie.say "Too bad for us to talk about it over the telephone."
    show cherie sadsmile
    "By now I'm really starting to get worried about what Cherie's going to tell me."
    "But at the same time the waiting to hear what she has to say is almost unbearable."
    mike.say "What is it, Cherie?"
    mike.say "You have to tell me!"
    "Cherie's looking me in the eye as I demand to know."
    "But I see one of her hands move to her stomach at the same time."
    show cherie talkative
    cherie.say "Ah, {i}mon ami{/i}…"
    cherie.say "There is no easy way for me to say this..."
    cherie.say "But I have taken a test, and the result is positive."
    show cherie sadsmile
    mike.say "You..."
    mike.say "You mean that..."
    show cherie talkative
    cherie.say "Yes, I am pregnant!"
    show cherie sadsmile
    "The words hit me with all the force of a hard slap to the face."
    "Eyes wide and mouth hanging open, all I can do is shake my head."
    mike.say "Are you serious?"
    mike.say "We're going to have a baby?!"
    "The serious expression on Cherie's face kind of makes the first question sound silly."
    "And the second one seems purely academic, just a symptom of my brain doing backflips."
    show cherie whining
    cherie.say "Of course I am serious!"
    cherie.say "But you misunderstand me, [hero.name]…"
    cherie.say "I am pregnant, yes - but we are not having a baby!"
    show cherie sadsmile
    "I find myself blinking in surprise at what Cherie just said."
    mike.say "Huh?"
    mike.say "What does that mean?"
    if game.flags.dwaynedead:
        show cherie stuned
        "Cherie looks at me like she can't believe what she's hearing."
        show cherie surprised
        cherie.say "Do I look like silly little teenage girl to you?!?"
        cherie.say "I have already been married and a mother, already raised a child."
        cherie.say "I cannot do all of that again, not at my age!"
        show cherie sad
        "The intensity of Cherie's outburst takes me by surprise."
        "I mean sure, I'm fully aware that she's a mature woman."
        "But I never thought that saw herself as being too old for that kind of thing."
    else:
        show cherie annoyed
        "Cherie rolls her eyes and lets out a sigh."
        show cherie angry
        cherie.say "Urgh..."
        cherie.say "Have you forgotten that I am still married to Dwayne?"
        cherie.say "Your employer and the man that is the head of the company?"
        cherie.say "Because I do not think that he would take the news very well!"
        show cherie sad
        "I can't help nodding as Cherie reminds me of the situation we're in."
        "And I don't think we could convince Dwayne the kid was his either."
        "He's probably too smart to fall for a scheme like that."
    "And it's about then that the real implications of what she's saying hit me."
    mike.say "But wait a second, Cherie..."
    mike.say "Are you saying that you..."
    show cherie whining
    cherie.say "Yes, [hero.name]…"
    cherie.say "I want to end the pregnancy."
    cherie.say "And I want to do it as soon as possible."
    show cherie sad
    "The weight of the situation suddenly feels like way too much for me to handle."
    "One minute I'm being told that I'm fifty percent responsible for the pregnancy."
    "And the next, before I can come to terms with that, I learn that Cherie wants to end it."
    "Either of those things alone would be more than enough to make my head spin."
    "But here I am, with Cherie expecting me to just take it all in and..."
    "And what?"
    "Is she just expecting me to go along with the idea of ending it?"
    "Just like that?"
    menu:
        "Alright, if that's what you want...":
            "Part of me feels like I should be arguing to keep the baby."
            "But another part of me, a pretty selfish part, just wants to keep Cherie."
            "And so I make a decision that I sincerely hope I won't come to regret."
            mike.say "Okay, Cherie..."
            mike.say "I'm not crazy about the idea..."
            mike.say "But if that's what you're resolved to do, then you have my support."
            "Cherie looks like she's been holding her breath as she waits for my answer."
            show cherie normal
            "And the relief that spreads across her face now is plain to see."
            show cherie talkative
            cherie.say "Oh, {i}mon ami{/i}…"
            cherie.say "You do not know how happy I am to hear you say that!"
            cherie.say "I was afraid that you would be angry, that you would leave me all alone."
            show cherie sadsmile
            "I shake my head as I wrap my arms around Cherie and pull her into a tight embrace."
            "Feeling my spirits begin to rise a little as she leans into the hug and holds me too."
            "There's no way what lies ahead is going to be easy for either of us."
            "But maybe together we can prove strong enough to make it out the other end."
            $ cherie.love += 10
            $ cherie.unpreg()
        "But why not keep it and raise it, together!":
            "I don't know what it is that makes me shake my head."
            "But suddenly I just have this vision of Cherie and myself as a family."
            "And you know what, it just feels so damn right!"
            mike.say "No, Cherie..."
            mike.say "I don't think that's right."
            mike.say "I think we should keep the baby."
            mike.say "And I think we should raise them together, as a family."
            show cherie stuned
            "Cherie looks at me in pure, unadulterated amazement."
            show cherie surprised
            cherie.say "Have you lost your mind, {i}mon ami{/i}?"
            cherie.say "Did you not hear everything that I just said?"
            show cherie stuned
            mike.say "Of course I did, Cherie..."
            mike.say "But you haven't heard everything I've got to say."
            mike.say "You're not old, you're in your prime."
            mike.say "And things wouldn't be like they were with Dwayne either."
            show cherie surprised
            cherie.say "How so?"
            show cherie stuned
            mike.say "Because I'm a totally different guy, that's how..."
            mike.say "And most importantly, I'm the guy that's madly in love with you!"
            if cherie.love >= 150:
                show cherie surprised
                cherie.say "You..."
                cherie.say "You really mean that, do you not?"
                cherie.say "Oh, {i}mon ami{/i}…"
                cherie.say "Perhaps...perhaps it could be possible?"
                show cherie stuned
                "I sense the chance to change Cherie's mind."
                "And I'm determined not to let it pass me by."
                mike.say "Of course I do, Cherie..."
                mike.say "Of course it could work..."
                mike.say "You and me, together - we can do anything!"
                show cherie sadsmile
                "Cherie pauses for a moment, silently looking me in the eye."
                "I'm afraid that she might pull back at the last second."
                "That her fears might get the better of her, even now."
                "But then she nods."
                show cherie talkative
                cherie.say "Then we will make it work, {i}mon ami{/i}…"
                cherie.say "Together we will make a new life for ourselves."
                cherie.say "And for our child too!"
                show cherie normal
                $ cherie.love += 5
                $ cherie.sub += 5
            else:
                show cherie sad
                "Cherie looks at me with genuine pain in her eyes."
                "And then then reaches out and takes my hands."
                "Squeezing them as she shakes her head."
                show cherie whining
                cherie.say "Oh, {i}mon ami{/i}…"
                cherie.say "Bless you for trying..."
                cherie.say "But my mind is already made up."
                show cherie sad
                "I shake my head as Cherie leans her head on my shoulder."
                "Feeling my spirits begin to rise a little as she wraps her arms around me."
                "There's no way what lies ahead is going to be easy for either of us."
                "But maybe together we can prove strong enough to make it out the other end."
                $ cherie.sub -= 10
                $ cherie.unpreg()
    return

label cherie_police_interview_male:
    $ cherie.unhide()
    scene bg bedroom1 with fade
    pause 0.1
    show mike normal at center, zoomAt(1.25, (640, 880)) with dissolve
    "I'm still feeling more than a little on edge after all of the stuff that's gone down with Cherie and Dwayne."
    "And I've been avoiding answering the phone for that reason, as well as keeping a low profile too."
    "But for some reason, when my phone rings out of the blue, I get the strangest feeling that I should take the call."
    show screen expression "smartphone_calling" pass ("Unknown Number")
    "There's no real explanation for the feeling, and the number that comes up on the screen isn't one that I recognise either."
    "Maybe it's just that I feel like I need to start behaving in a more normal way."
    if game.flags.dwaynedead:
        "You know, before someone notices that I'm acting like someone with a guilty conscience?"
    else:
        "You know, before people start to think that I know something about where the hell Dwayne's gotten to?"
    "Whatever the reason, I decide that I'm going to bite the bullet..."
    show mike annoyed at center, zoomAt(1.5, (640, 1040))
    "Urgh..."
    if game.flags.dwaynedead:
        "That phrase just brings back so many bad memories!"
    else:
        "That's so macabre - like I'm assuming he's dead or something!"
    show bg bedroom1 at dark
    hide screen smartphone_calling
    show mike normal at startle
    mike.say "Erm..."
    mike.say "Hello?"
    show mike normal
    "Unknown caller" "Ahh..."
    "Unknown caller" "Hello there!"
    "The person on the other end of the line speaks in an odd, almost faltering manner."
    "Kind of like he's bumbling along and not too sure of what he's saying to me."
    "Unknown caller" "Would I be speaking to mister [hero.name] [hero.family_name]?"
    show mike surprised
    mike.say "Y...yeah..."
    mike.say "That's me."
    mike.say "And who is this?"
    show mike normal
    "Unknown caller" "Oh..."
    "Unknown caller" "Did I not say already?"
    "Michaels" "My name is Michaels...Detective Michaels."
    "As soon as I hear the word detective, my stomach churns and I feel like I'm going to be sick."
    if "aletta_event_08" in DONE or "alexis_event_07b" in DONE:
        mike.say "Oh..."
        mike.say "Detective Michaels..."
        mike.say "Am I in trouble?"
        "Michaels" "You tell me!"
        "Michaels" "But today, we'd just like to talk to you about Mister Jackson."
    else:
        show mike surprised at center, zoomAt(1.25, (640, 880))
        mike.say "D...detective?"
        mike.say "As in police detective?"
        show mike normal
        "I hear a chuckle on the other end of the line."
        "Michaels" "Yeah, sir..."
        "Michaels" "Something like that!"
        "Michaels" "But don't worry, you're not in any kind of trouble."
        "Michaels" "We'd just like to talk to you about Mister Jackson."
    "This time it feels like I've actually been punched in the gut."
    show mike talkative at center, zoomAt(1.5, (640, 1040)) with vpunch
    mike.say "About Dwayne?"
    mike.say "Listen, I don't know anything about what happened to him!"
    show mike normal
    "I hear chuckling on the other end of the line for a second time."
    "Michaels" "Well then what have you got to worry about?"
    "Michaels" "Just come on down to the station and make a statement to that effect."
    "Michaels" "I understand you worked for Mister Jackson..."
    "Michaels" "So we need to eliminate you from our inquiries, okay?"
    if (hero.charm + hero.knowledge) >= 175 or hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "Do I really have the choice here?"
        "It's not like he will let me off the hook that easily..."
        hide black with dissolve
    menu:
        "Agree to go to the station":
            "I realise that the detective has me bang to rights."
            "If I don't do as he asks, then it's just going to look like I have something to hide."
            show mike talkative at center, zoomAt(1.5, (640, 1040))
            mike.say "Okay, okay..."
            mike.say "I'll be right there."
            show mike normal
            "Michaels" "That's great, Mister [hero.family_name]."
            "Michaels" "So I'll see you soon."
            $ hero.flags.police_trust += 1
        "Refuse to be interviewed":
            "The idea of being sat down and questioned by the police is absolutely terrifying."
            "So the last thing that I'm going to do is say yes and just stroll down to the police station."
            show mike angry at center, zoomAt(1.5, (640, 1040))
            mike.say "Look, I already told you..."
            mike.say "I don't know anything about what's happened to Dwayne."
            show mike talkative
            mike.say "And I know my rights too - you can't make me come down there."
            mike.say "Not unless you arrest me for a real crime, right?"
            show mike upset
            "Part of me is expecting the detective to get nasty with me."
            "To threaten me with something really awful so that I cooperate."
            "But instead all I hear is a kind of resigned grunt on the other end of the line."
            "Like he's more bored and disappointed with my response than actually angry."
            "Michaels" "Ah..."
            "Michaels" "You're right, Mister [hero.family_name]…"
            "Michaels" "We could take that route, and it'd be harder and longer for me."
            "Michaels" "But then there'd be the messy business of us coming round there in a squad car."
            "Michaels" "Several uniformed officers hammering on your door, demanding to be let in."
            "Michaels" "Maybe even leading you to the back seat of the car in handcuffs too."
            "Michaels" "I'd hate to think what the neighbours would make of all that..."
            show mike annoyed
            "Never mind the goddamn neighbours - what would Bree and Sasha make of it?!?"
            show mike talkative at center, traveling(1.25, 0.3, (640, 880))
            mike.say "Erm..."
            mike.say "You know what, detective..."
            mike.say "I'll be right there."
            show mike upset
            "As soon as the words are out of my mouth, it's like everything changes."
            "The detective is all amiable friendliness again, as nice as can be."
            "Michaels" "That's great, Mister [hero.family_name]."
            "Michaels" "So I'll see you soon."
            "Ending the call, I make good on my promise, leaving the house and heading to the police station."
            $ hero.flags.police_trust -= 1
    scene bg street with fade
    "All the way there I'm telling myself that this is only routine, just like the detective said."
    if game.flags.dwaynedead:
        "They don't know that I was involved in what happened to Dwayne."
    else:
        "They don't know about my role in getting Dwayne fired and his sudden departure."
    "So all I have to do is play it cool and not say anything stupid."
    $ game.room = "policestation"
    scene bg policestation with fade
    "With that in mind, I walk right in through the doors of the police station."
    "Because I figure the best thing is to look confident the whole time I'm here."
    with vpunch
    if camila.id not in hero.smartphone_contacts:
        "Officer" "Mister [hero.family_name]?"
        show camila work at center, zoomAt(1.25, (640, 880)) with easeinright
        "I turn to see a tough-looking woman in police uniform."
        show camila at center, traveling(1.5, 0.5, (640, 1040))
        "She's pretty hot, in a scary kind of way, and she's walking towards me."
        mike.say "Y...yeah..."
        mike.say "That's me."
        "She nods once, then motions with her hand."
        show camila talkative
        "Sgt Foglio" "I'm Sergeant Foglio, assigned to the Jackson case."
        "Sgt Foglio" "This way please."
    elif camila.id in hero.smartphone_contacts and camila.status not in ["girlfriend", "fiance"]:
        camila.say "[hero.name]..."
        camila.say "Over here!"
        "I turn to see Camila hurrying towards me."
        show camila work at center, zoomAt(1.25, (640, 880)) with easeinright
        mike.say "Hey, Camila..."
        mike.say "I'm here to see a guy called Michaels?"
        show camila at center, traveling(1.5, 0.5, (640, 1040))
        "Camila nods as she takes hold of my arm."
        show camila talkative
        camila.say "I know - they assigned me to the case as well."
        show camila happy
        camila.say "But don't worry, this is all just routine."
        show camila talkative
        camila.say "Let's get you to the interview room."
    else:
        camila.say "[hero.name]!"
        show camila work at center, zoomAt(1.25, (640, 880)) with easeinright
        "I look around to see Camila almost running over to me."
        "And I feel my spirits lift at the mere sight of her."
        show mike happy at left, zoomAt(1.2, (320, 880))
        mike.say "Camila..."
        mike.say "It's so good to see you!"
        show camila at right, traveling(1.5, 0.5, (640, 1040))
        "Camila almost leans in to kiss me, but then she stops herself."
        mike.say "I...I need to keep this professional, as they assigned me to the Jackson case."
        show camila talkative
        camila.say "I know - they assigned me to the case as well."
        show camila happy
        camila.say "But don't worry, this is all just routine."
    hide camila with easeoutleft
    "I do as I'm told, allowing myself to be guided to the interview room."
    show cherie sad at right, zoomAt(1.25, (460, 880)) with easeinleft
    "But as we get there, the door opens and I see Cherie emerging."
    show cherie surprised at startle
    "There's only enough time for us to exchange a surprised glance."
    hide cherie with easeoutright
    "And then I'm hustled into the room as Cherie walks away."
    "But the sight of her is enough to send me into a minor panic."
    "What did they say to her just now, and what did she tell them?"
    "All I can think is that I'm going to contradict Cherie's account of what happened."
    "Or that I'll unwittingly say something that I think is innocent, but ends up incriminating us both!"
    scene bg policestation at dark, blur(5)
    show inspector at center, zoomAt(1.25, (640, 880))
    with fade
    pause 0.5
    show camila work at center, zoomAt(1.25, (1040, 880)) with easeinright
    "Michaels" "Mister [hero.family_name]..."
    "Michaels" "Would you mind coming in and sitting down?"
    "Michaels" "And you can let yourself out, Detective Foglio..."
    "Michaels" "I'll handle this interview myself."
    hide camila with easeoutright
    "The sound of the detective's voice makes me turn my head around."
    show inspector at center, traveling(1.5, 0.3, (640, 1040))
    "And almost without thinking, I do as he says, sitting in the chair opposite him."
    "Michaels" "Hopefully this won't take too long, Mister [hero.family_name]."
    "Michaels" "And don't worry, I know that this is stressful for you."
    "Michaels" "So just try to relax and think about your answers, okay?"
    "I nod, already aware of how fast my heart is beating right now."
    mike.say "Sure...sure thing."
    "The detective glances down at a file on the desk in front of him."
    "And it looks like he's reading something off the top page."
    "Michaels" "You work for Mister Jackson's company, right?"
    mike.say "Yes, that's right."
    if game.flags.dwaynedead:
        "Michaels" "And how would you describe the deceased?"
    else:
        "Michaels" "And how would you describe your former boss?"
    "He looks up at me as he says this, almost winking."
    "Michaels" "Don't worry about being candid either, okay?"
    if game.flags.dwaynedead:
        "Michaels" "I'm fine with you speaking ill of the dead!"
    else:
        "Michaels" "Since he's been fired, telling me his flaws is more useful than kissing his ass!"
    if (hero.charm + hero.knowledge) >= 175 or hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "If the police conduct their investigation with a minimum of professionalism, they will easily establish that Dwayne was an arrogant and nasty man."
        hide black with dissolve
    menu:
        "Be honest about Dwayne":
            "My first instinct is to spin the detective a line of bullshit."
            "To claim that Dwayne was a prince amongst men and everyone loved him."
            "But then it occurs to me that honestly would be the best policy."
            "Because a detective is trained so sniff out lies."
            "So telling him the truth, at least in part, should reassure the guy."
            mike.say "Ah..."
            mike.say "I feel bad saying this..."
            mike.say "But Dwayne was kind of an asshole!"
            "I was expecting the detective to be shocked."
            "But instead he kind of just nods his head"
            "Michaels" "Heh..."
            "Michaels" "I kinda got that impression from reading the file and talking to your colleagues!"
            "I put what I hope is a relieved smile on my face."
            "But in reality I'm already wondering just who else he's spoken to, and what they've told him."
            mike.say "Yeah, Dwayne was a womaniser and kind of a bully too."
            mike.say "I got the feeling he saw it as his right, because he thought he was an alpha male."
            $ hero.flags.police_trust += 1
        "Lie about Dwayne":
            "I feel like I'm being lured into a trap here."
            "That if I'm honest about Dwayne's flaws, then it'll count against me."
            "So I decide that lying is the best option."
            mike.say "Dwayne was a really great boss."
            mike.say "A total Chad, you know?"
            mike.say "And he was a role-model for me too!"
            "The detective raises his eyebrows at this."
            "Michaels" "You don't say?"
            "Michaels" "Because some people described him as..."
            "He checks the file again."
            "Michaels" "A toxic, sexist, egomaniacal despot."
            "Michaels" "I mean, does that sound like the same man to you?"
            "I can't help feeling like I've been slapped in the face."
            "Because obviously that's a far more honest appraisal of Dwayne's character."
            "But I've gone and trapped myself in my own lie."
            "So all I can do without looking like a complete fool is to double down."
            mike.say "I..."
            mike.say "Well..."
            mike.say "Everyone's entitled to their own opinion, I guess."
            "The detective nods his head at this."
            "But I have to say that he doesn't seem convinced."
            $ hero.flags.police_trust -= 1
    "The detective moves on to ask me about something else next."
    "This time he doesn't bother checking the file on his desk."
    "Instead he looks at me like he's just remembered something."
    "Michaels" "Oh yeah..."
    "Michaels" "I just wondered..."
    "Michaels" "Are you intimate with any of Mister Jackson's female relations?"
    "Michaels" "Like his daughter and his wife?"
    "He asks the question so casually that it catches me totally off-guard."
    mike.say "What are you asking me?"
    mike.say "If I'm having an affair with them?"
    "The detective raises his eyebrows at my response."
    "Michaels" "Well I was thinking of whether or not you know them socially, you know?"
    "Michaels" "But seeing as you brought it up..."
    "Michaels" "Are you?"
    if (hero.charm + hero.knowledge) >= 175 or hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "Looks like another trick question."
        "Michaels might already have information from someone."
        hide black with dissolve
    menu:
        "Answer honestly":
            "Of course the obvious thing would be to deny everything."
            "To claim that I've never looked at Cherie or Cassidy in that way."
            "But the guy's seen the former and probably the latter too."
            "So he's never going to believe that."
            mike.say "Okay, okay..."
            if game.flags.dwaynedead:
                mike.say "I know that they're grieving right now."
            else:
                mike.say "I know that they're dealing with their husband and father being fired and missing right now."
            mike.say "But those are two seriously hot women!"
            "The detective nods at this."
            "And he gives me what I take as a conspiratorial wink."
            mike.say "I mean..."
            mike.say "I wish I'd had the chance for something like that to happen!"
            "The detective nods again, chuckling quietly."
            "Michaels" "Yeah, yeah..."
            "Michaels" "Isn't it always the way?"
            "Michaels" "Guys like you and me..."
            "Michaels" "We never get as much as a look in!"
            "As soon as I realise what he's actually saying, I can't help feeling insulted."
            "But I put a smile on my face and nod along with what he's saying."
            $ hero.flags.police_trust += 1
        "Deny everything":
            "As soon as I hear the question, I can't help myself."
            "It hits a nerve so deep that I leap to answer without thinking."
            with vpunch
            mike.say "NO!"
            mike.say "Of course not!"
            if game.flags.dwaynedead:
                mike.say "Have an affair with a married woman or my boss's daughter..."
            else:
                mike.say "Have an affair with a married woman or my former boss's daughter..."
            mike.say "What kind of a sleaze-bag do you think I am?!?"
            "The detective doesn't seem in the least bit moved by my outburst."
            "Instead he simply keeps on looking me in the eye, like he's weighing me up."
            "Michaels" "I'm not implying anything, Mister [hero.family_name]."
            "Michaels" "Just asking the obvious questions here."
            "Michaels" "Cherie and Cassidy Jackson are very beautiful women."
            "Michaels" "It'd be crazy to deny it."
            "I can feel the stupidity of my denials sinking in as I listen to him."
            "But there's no way I can back down now, as I've already said my piece."
            mike.say "I guess they are..."
            mike.say "But I still wouldn't go there."
            "The detective just shrugs and moves on."
            "Choosing not to say anything more on the subject."
            $ hero.flags.police_trust -= 1
    "I'm prepared for the next question, or at least I think I am."
    "But to my surprise, the detective closes the file on his desk."
    "Then he gestures to the door."
    "Michaels" "Well..."
    "Michaels" "That pretty much wraps it up for now."
    "I look at the door and then back to the detective."
    "Not quite able to believe what I'm hearing."
    mike.say "Are you serious?"
    mike.say "I can really go home?"
    "The detective nods."
    "Michaels" "Sure you can, Mister [hero.family_name]."
    "Michaels" "Just don't go leaving town or moving to another country, okay?"
    "Michaels" "If we need anything more, then you'll hear from us."
    scene bg policestation with fade
    "In get up and hurry to the door, nodding the whole time."
    scene bg street with fade
    "And once I'm out of there, I scuttle out of the police station too."
    "All the way home I'm worrying that I said something incriminating."
    "And I'm thinking that getting to sleep tonight might be a challenge."
    "What with all the stuff that's running through my head right now."
    $ game.room = "street"
    return

label cherie_event_02:
    if cherie.love.max < 40:
        $ cherie.love.max = 40
    "I've been dreading the day of Dwayne's funeral ever since moment the guy bought the farm."
    "Normally it would have been more than enough stress and strain to attend any normal funeral service."
    "But for this one there's all the added drama of knowing that the person in the box was killed."
    "Let alone the fact that I managed to get myself tied up in the whole sordid affair too!"
    "But there's no way I can get out of this one, because missing it would be altogether too suspicious."
    "No, I have to show my face and do the best I can to get through this thing."
    "So on the morning of the funeral, I put on my fanciest and yet most sombre suit."
    "And then I make sure that I arrive at the cemetery in plenty of time."
    show bg cemetery
    show cherie cry funeral zorder 9 at center, zoomAt(0.7, (640, 720))
    show shiori at blacker, center, zoomAt(0.7, (940, 720))
    show vincent teaser at blacker, center, zoomAt(0.7, (440, 720))
    show lavish at blacker, center, zoomAt(0.7, (1040, 720))
    show audrey teaser at blacker, center, zoomAt(0.7, (240, 720))
    show inspector at center, blacker, zoomAt(1, (40, 820))
    show camila a at center, blacker, zoomAt(1, (1240, 820))
    with fade
    "The only problem is that when I get there, it's not the quiet affair I'd been picturing."
    "Firstly, Dwayne's wealth and status means that he's being interred in the most expensive part of the cemetery."
    "Up there some of the tombs are almost the size of houses, and the memorials are like the Arc De Triomphe!"
    "And then, on top of that, there seems to be a veritable media circus here to record it all."
    "There are camera crews and reporters everywhere, as well as people that look like investigators too."
    "But the executives that I recognise from work seem to be keeping their distance from those folks."
    "Not that I'm going to be doing anything different myself!"
    "The last thing that I want is to be cornered and questioned."
    "So I find a spot where I can see everything that's going on, and yet not be seen at the same time."
    "And it doesn't take me long to spot Cherie, standing right at the front of the line of important mourners."
    "She's dressed all in black, and of course, she looks both sombre and stunning at the same time."
    "As does her daughter Cassidy, holding onto her mother's arm as they shed tears by the side of Dwayne's casket."
    "Unfortunately, I'm too far away to be able to hear the ceremony when the priest gets started talking."
    show cherie talkative
    "And so all I can do is watch, even when the time comes for Cherie to deliver the eulogy."
    "Part of me wants to be there to comfort her, as I can see the emotional strain on her face."
    "But obviously that would be the dumbest thing possible right now."
    "The last thing either of us need is wagging tongues asking awkward questions."
    show cherie sad
    if camila.id not in hero.smartphone_contacts:
        "Michaels" "Hmm..."
        "Michaels" "That's a really nice suit!"
        "Michaels" "No wonder you came to pay your respects to the guy who meant you could afford it."
        "At the sound of a voice behind me, I can't help jumping a little."
        show inspector at center, traveling(1.6, 0.5, (340, 1020))
        pause 0.5
        show inspector zorder 11 at brighter, zoomAt(1.6, (340, 1020)) with dissolve
        "And it doesn't help matters when I turn to see Detective Michaels standing there."
        if hero.charm >= 75:
            mike.say "Hello Detective."
            mike.say "You don't look like someone who comes to a funeral to pay their respects."
            $ hero.flags.police_trust += 1
        else:
            mike.say "What the hell?!?" with vpunch
            mike.say "Hey, don't you have any respect?"
            mike.say "This is a damn funeral!"
            $ hero.flags.police_trust -= 1
        "The crumpled detective doesn't seem in the least bit bothered by my words."
        "Because he just gives me a knowing smile and shakes his head."
        "Michaels" "I know, I know - emotional times, right?"
        "Michaels" "But the wheels of justice never stop turning, you know that?"
        "Michaels" "And we're always here, looking and listening for those subtle little clues."
        "I'm about to say something more when I realise that people are starting too look my way."
        "And so I make an effort to clamp my jaw shut and just give Michaels a tense nod."
        "He responds to this with another knowing smile, and then melts into the crowd."
        show inspector at center, traveling(1, 1, (40, 820))
        pause 1
        show inspector at center, blacker, zoomAt(1, (40, 820)) with dissolve
    else:
        camila.say "Wishing you could be up there with her, huh?"
        camila.say "I mean, she does look pretty lonely up there, doesn't she?"
        camila.say "Nothing like a grieving widow to get your juices flowing - especially one as pretty as her!"
        "At the sound of a voice behind me, I can't help jumping a little."
        show camila at center, traveling(1.6, 0.5, (1040, 1020))
        pause 0.5
        show camila work zorder 11 at brighter, zoomAt(1.6, (1040, 1020)) with dissolve
        "And it doesn't help matters when I turn to see Officer Camila standing there."
        if hero.charm >= 75:
            mike.say "Hello Officer."
            mike.say "You don't look like someone who comes to a funeral to pay their respects."
            $ hero.flags.police_trust += 1
        else:
            mike.say "What the hell?!?" with vpunch
            mike.say "Hey, don't you have any respect?"
            mike.say "This is a damn funeral!"
            $ hero.flags.police_trust -= 1
        "The formidable female officer doesn't seem in the least bit bothered by my words."
        "She just raises a single eyebrow and gives me a crooked, knowing smile."
        camila.say "What did you think, [hero.name]?"
        camila.say "That we all stopped being cops while they bury the guy?"
        camila.say "We don't do that - not even for rich bastards like him!"
        "I'm about to say something more when I realise that people are starting to look my way."
        "And so I make an effort to clamp my jaw shut and just give Camila a tense shake of the head."
        "She gives me a triumphant smile in return, and then melts into the crowd."
        show camila at center, traveling(1, 1, (1240, 820))
        pause 1
        show camila at center, blacker, zoomAt(1, (1240, 820)) with dissolve
    "I feel so shaken up by the encounter with the cop that I find it hard to concentrate after that."
    hide inspector with easeoutleft
    pause 0.7
    hide lavish with easeoutleft
    "And before I can clear my head, I realise that the service is actually coming to an end."
    hide camila with easeoutleft
    pause 0.7
    hide vincent with easeoutleft
    "So either it was far more brief than I was expecting, or that little run-in shook me more than I realised."
    hide shiori with easeoutleft
    pause 0.5
    hide audrey with easeoutleft
    "But I soon regain control of my faculties when I see that Cherie is standing alone by the graveside."
    "If I want to talk to her today, then I'm not going to get a better chance than this."
    show bg cemetery at center, traveling(1.2, 2, (640, 770))
    show cherie at center, traveling(1.05, 2, (640, 820))
    pause 2
    show bg cemetery at center, zoomAt(1.2, (640, 770)) with dissolve
    show cherie at center, zoomAt(1.05, (640, 820)) with dissolve
    "So I hurry over there as fast as I can without actually breaking into a run."
    show bg cemetery at center, traveling(1.4, 2, (640, 820))
    show cherie at center, traveling(1.4, 2, (640, 920))
    pause 2
    show bg cemetery at center, zoomAt(1.4, (640, 820)) with dissolve
    show cherie at center, zoomAt(1.4, (640, 920)) with dissolve
    "And when I arrive at Cherie's side, I make a point of coughing discreetly to get her attention."
    mike.say "Ahem..."
    show cherie stuned at startle(0.05, -5)
    "Cherie looks around, noticing me standing beside her."
    show cherie talkative
    cherie.say "Oh, [hero.name]..."
    cherie.say "I am so glad to see that you have come."
    cherie.say "When I could not find you in the crowd, I thought that you had abandoned me!"
    show cherie sadsmile
    mike.say "I'm sorry, Cherie..."
    mike.say "I just didn't think it'd be wise for us to be seen together."
    mike.say "At least not while you were in the act of burying your husband, you know?"
    "Cherie nods as she gazes down at the pile of earth that's been heaped over Dwayne's casket."
    show cherie whining
    cherie.say "You know, I keep thinking that the next thing is going to make it real."
    cherie.say "That seeing his body would make me believe he was gone."
    cherie.say "And then that burying him would finally bring it home."
    cherie.say "But there is still a part of me that cannot truly believe."
    cherie.say "How strange does that sound to you?"
    show cherie sadsmile
    "I realise that Cherie's waiting for me to offer up an answer."
    "And at the same time I get the feeling what I say will be taken very seriously too."
    "So I make a point of thinking deeply before offering up my response."
    menu:
        "Show empathy":
            "There's really only one proper way to react at a time like this."
            "No matter what I thought of Dwayne when he was alive, Cherie's a grieving widow."
            "And what she needs right now is support from those she can call her friends."
            mike.say "You shouldn't put too much stock in what you think and feel right now, Cherie."
            mike.say "Not after all the emotional trauma that you've been put through recently."
            mike.say "I think what you really need is to be kind to yourself."
            mike.say "That and to give yourself permission to grieve in your own way."
            "Cherie nods her head as she listens to what I have to say."
            "And when I'm done, she seems genuinely comforted by it too."
            show cherie talkative
            cherie.say "I should have known that you would be a help, [hero.name]."
            cherie.say "And I feel that I am going to need friends like you very soon."
            cherie.say "So don't be surprised if I call on you in the near future."
            $ cherie.flags.hero_rivalry -= 2
            $ cherie.love += 2
        "React with caution":
            "Normally I'd be committed to nothing more than comforting the grieving widow."
            "But I know Dwayne far too well to let my guard down, even now that he's dead."
            "And I'm not going to let anything he's left in his wake hurt Cherie either."
            mike.say "I hate to say this to you, Cherie..."
            mike.say "But we both know that Dwayne was a scheming bastard."
            mike.say "And just because he's dead, it doesn't mean he didn't plan for that!"
            mike.say "So you should do your best to keep your guard up."
            "At first Cherie looks shocked to hear me lecturing her at a time like this,"
            "But slowly she begins to nod as the truth of my words sinks in."
            show cherie talkative
            cherie.say "Ah, I am afraid that you are right, [hero.name]."
            cherie.say "My husband was never without a plan and a escape route!"
            cherie.say "I sense that I will have further need of your advice in the days to come!"
            $ cherie.love += 4
        "Be cynic":
            "My instinct is to do all that I can to comfort Cherie as a grieving widow."
            "But there's just that little part of me that never wants to fully trust a person."
            "Because in this case I know full well that she's not as helpless as she might look."
            mike.say "If there's one thing I've leaned in life, Cherie..."
            mike.say "It's that people will always find a way to surprise you."
            mike.say "They can be at their most dangerous when they seem the most vulnerable."
            mike.say "And so you should never let your guard down, not totally."
            "At first Cherie looks shocked to hear me lecturing her at a time like this,"
            "But slowly she begins to nod, as if she's taking the measure of me."
            show cherie talkative
            cherie.say "What an interesting and insightful piece of advice, [hero.name]."
            cherie.say "One that I will be sure to ponder in the days to come."
            cherie.say "Until we next meet, I wish you the best."
            $ cherie.flags.hero_rivalry += 2
            $ cherie.love -= 4
    show cherie sad
    "With that, I take it that I'm being subtly dismissed by Cherie."
    "And not wanting to make a scene in front of so many witnesses, I take my leave."
    if not hero.flags.isceo:
        "But as I'm walking towards the gates of the cemetery, I realise that I have to make a choice."
        "Because all of the players in the game are going to be making their move now Dwayne's in the ground."
        menu:
            "Back Cherie for CEO of the company":
                "It's obvious to me now that I have to put all my strength behind Cherie."
                "I have to make sure that she becomes the CEO of Dwayne's company."
                "It's only right, after all of the shit that bastard put her through."
                "And if I'm honest, my feelings for her make me want that too."
                "With her in power and me by her side, we could do whatever we want."
                $ cherie.flags.isceo = True
            "Make a play for the position of CEO":
                "It's obvious to me now that I have to be the one to take over the company."
                "Cherie might want to step into Dwayne's shoes, but I'm not going to let her."
                "Not after she was the one that put him in that damn casket!"
                "Sure, I might have feelings for the woman, want to be with her."
                "But I don't see why I can't have Dwayne's position in the company and his former wife."
                "And I can claim it all without having to share power with her too."
                $ hero.flags.isceo = True
                if aletta.status == "boss":
                    $ aletta.status = "employee"
                if audrey.status == "coworker":
                    $ audrey.status = "employee"
                if lavish.status == "coworker":
                    $ lavish.status = "employee"
                $ hero.flags.workonblissard = TemporaryFlag(True, 7)
                $ game.flags.capped_promotion = False
    scene bg black with dissolve
    $ game.room = "street"
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    return

label cherie_event_03:
    if cherie.love.max < 60:
        $ cherie.love.max = 60
    scene bg park with fade
    "If I thought that having Dwayne's funeral out of the way would relieve the pressure on me, I was definitely mistaken."
    "Because, if anything, the attention that the whole thing's been getting is even more intense now."
    "The police seem to be crawling over the whole thing, interviewing everyone and scrutinising every last detail."
    "I've been doing all that I can to avoid them, keeping my head down and trying to keep a low profile."
    play sound cell_vibrate
    "But it doesn't seem like Aletta's been so lucky, judging by the text message that she just sent me."
    $ phone_show_hero = False
    $ nvl_mode = "phone"
    nvl clear
    aletta_nvl "[hero.name], I need your help - RIGHT NOW!"
    "I find myself staring at my phone, worried at the tone of Aletta's message."
    "But at the same time I'm also concerned at how out of character it is for her."
    "Because I'm used to Aletta being the strong, confident type, never flustered by anything."
    "So I quickly compose a response, hoping to get to the root of the problem."
    mchero_nvl "Okay, Aletta - what's up?"
    mchero_nvl "You sound pretty tense!"
    "Aletta must be waiting on my response, as her next message arrives within mere seconds."
    aletta_nvl "Can't explain in a text-message - it's not safe!"
    aletta_nvl "Meet me as soon as you can, and I'll explain in person."
    "Aletta names the place and time for the meeting, and I hurry to be there."
    $ nvl_mode = None
    $ phone_show_hero = True
    "All the while preparing myself for whatever might be eating at her so badly."
    scene bg forest at center, zoomAt(1.4, (640, 820))
    show aletta a sport upset
    with fade
    "But when I get there, I see that Aletta's beaten me to it."
    "And worse, she's pacing back and forth, arms crossed tightly over her chest."
    "Everything about her seems to be screaming tension and stress."
    mike.say "Ah..."
    mike.say "Aletta?"
    "At the sound of my voice, Aletta almost leaps backwards."
    show aletta at center, traveling(1.4, 0.3, (640, 970))
    pause 0.3
    show aletta at center, zoomAt(1.4, (640, 970))
    "And as soon as she sees that it's me, she hurries straight over."
    show aletta scared at hshake
    aletta.say "Shhh!"
    show aletta dreamy with dissolve
    pause 0.5
    show aletta surprised with dissolve
    aletta.say "Keep your voice down..."
    show aletta scared at center, traveling(1.8, 0.5, (640, 1220))
    pause 0.5
    show aletta at center, zoomAt(1.8, (640, 1220))
    pause 0.1
    show aletta surprised at startle(0.05, 5)
    aletta.say "You never know who might be listening!"
    show aletta scared at center, traveling(1.4, 0.1, (640, 970))
    show bg forest at traveling(1.3, 0.1, (640, 820))
    pause 0.1
    show aletta scared at center, zoomAt(1.4, (640, 970))
    show bg forest at zoomAt(1.3, (640, 820))
    "I find myself taking an automatic step backwards as Aletta comes closer."
    "Because now I can actually see the look in her eyes."
    "And it's one of paranoia, totally at odds with the Aletta that I've come to know."
    mike.say "Whoa..."
    mike.say "Calm down, Aletta..."
    mike.say "It's just me, come to meet you here, like you asked."
    mike.say "There's nobody here but the two of us, see?"
    "I turn around and gesture to our immediate surroundings, trying to show Aletta everything is fine."
    "But Aletta greets this with a shake of the head."
    show aletta surprised
    aletta.say "But...but..."
    show aletta at startle(0.1, 5)
    aletta.say "What if they have one of us bugged?!?"
    show aletta stuned
    "The look on my face must be one of genuine surprise and concern."
    "Because as soon as Aletta looks me in the eye again, her own expression changes."
    "The craziness seems to drain away, and she lets out a groan as she shake her head."
    show aletta whining at startle(0.1, 5)
    aletta.say "Urgh..."
    show aletta at hshake
    aletta.say "What am I saying?"
    show aletta talkative
    aletta.say "Bugging us?"
    show aletta b happy
    aletta.say "If I keep on like this, it'll be spying on us with space-lasers next!"
    "I nod and smile, thankful for the change in Aletta's tone and demeanour."
    "At least now she's starting to sound like we can have a sane conversation."
    show aletta normal
    mike.say "So..."
    mike.say "I'm going to go ahead and guess that this is on account of the investigation?"
    mike.say "That the police poking around is starting to get to you?"
    show aletta at startle(0.1, 5)
    "Aletta nods eagerly."
    show aletta talkative
    aletta.say "That's it exactly, [hero.name]."
    aletta.say "I...I used to think that I was pretty unflappable, you know?"
    aletta.say "But they just keep on asking questions...so many questions."
    aletta.say "I'm sure they've asked me the same one more than once."
    aletta.say "And that I might have given them a different answer."
    show aletta normal
    mike.say "Yeah, they've done that to me too."
    show aletta talkative
    aletta.say "But that's not the worst of it, [hero.name]..."
    show aletta at hshake
    if hero.flags.dwayne_corpse == hero.flags.aletta_gun:
        aletta.say "What if... what if they trace it back to me because of the murder weapon?!?"
    else:
        aletta.say "What if...what if they actually find the murder weapon?!?"
    show aletta surprised
    aletta.say "I'm scared that if they threaten me with prison, I might crack under the pressure!"
    show aletta scared
    "Aletta's moment of clarity and control seems to have passed."
    "And now she's returning to her previous state of anxiety, verging on panic."
    "So it looks like I'm going to have to do something to change that."
    menu:
        "Tell Aletta to pull herself":
            "I could try to tell Aletta that I'll fix everything for her."
            "That it's okay for her to be scared, as that's only natural."
            "But the truth is that I need every ally that I can get right now."
            "And I don't have the time or strength to hold her up as well."
            mike.say "That doesn't sound like the woman that I've worked with for so long, Aletta."
            mike.say "Like the professional valkyrie that used to stride through the office on a Monday morning."
            "Aletta looks up at me, and I can see genuine surprise in her eyes."
            show aletta surprised
            aletta.say "What..."
            aletta.say "What are you talking about, [hero.name]?"
            aletta.say "This isn't about the image I project in the office."
            aletta.say "This is about someone's life!"
            show aletta scared
            "I furrow my brows and harden my stare."
            "Not willing to let Aletta wriggle out of what I'm saying that easily."
            mike.say "So all of your bravado was just an act?"
            mike.say "Is that what you're saying?"
            mike.say "Bullshit, Aletta - you're not that weak!"
            show aletta surprised
            aletta.say "You...you don't mean that."
            aletta.say "You're just saying it to motivate me!"
            aletta.say "I've been to enough coaching seminars to know the technique."
            show aletta stuned
            mike.say "Then you know that it bloody well works!"
            mike.say "Use all of that training to steel yourself, Aletta."
            mike.say "Use it to get through this, and then we're off the hook."
            "For a moment I think that Aletta's going to collapse in on herself all over again."
            show aletta angry with dissolve
            "But then I see a hard expression set on her face, and she nods."
            show aletta at hshake
            aletta.say "Alright, [hero.name]..."
            show aletta at startle(0.1, 5)
            aletta.say "I'll give it my best shot."
            show aletta normal
            pause 0.5
            hide aletta with easeoutright
            "I nod in agreement, and then watch in silence as Aletta turns on her heel and walks away."
            "I can't be one hundred percent sure that she's not putting on an act for my sake."
            "But right now I don't have time to worry about that kind of thing."
            "This is one less problem for me to deal with, and that's got to be a good thing."
            $ aletta.love += 2
            $ aletta.flags.ally = True
        "''We're in this together''":
            "Man, part of me is desperate to tell Aletta that I'm scared too."
            "But I guess someone's going to have to be the strong one here."
            "And from the state she's on right now, it'll have to be me."
            mike.say "You're feeling scared because you've been facing this on your own, Aletta."
            show aletta sad
            mike.say "And that's what the police are going to take advantage of, it's what they want."
            mike.say "They're hoping you'll get so scared that you'll admit everything."
            "Aletta looks at me with her eyes the closest I think I've ever seen them to actual tears."
            show aletta whining
            aletta.say "I'm so close, [hero.name]..."
            aletta.say "So close to cracking!"
            show aletta sad
            mike.say "But they're wrong, Aletta..."
            mike.say "You're not alone in all of this."
            mike.say "What you're doing right now proves that - don't you see?"
            "Aletta's mood seems to lighten almost as soon as I ask the question."
            "And I think that I can see the first glimmers of hope in her eyes."
            show aletta whining
            aletta.say "You..."
            aletta.say "You mean..."
            mike.say "I mean that I'm here for you, Aletta..."
            show aletta sadsmile with dissolve
            mike.say "That whatever happens, we're in this together."
            mike.say "From now on, whenever you start to feel like this, I want you to call me."
            mike.say "No matter what time of day it is, even if it's in the middle of the night."
            mike.say "You call me, and I'll be there for you."
            "I'm smiling and nodding as I say all of this to Aletta."
            "And I'm expecting her to do the same in return."
            "Which is why it takes me completely by surprise when she throws her arms around me instead!"
            "Luckily I manage to shake off my surprise and gently put my arms around her in response a moment later."
            show aletta talkative
            aletta.say "Oh god..."
            aletta.say "Thank you so much, [hero.name]..."
            show aletta happy
            aletta.say "I can't tell you how much I needed to hear you say that!"
            "The hug goes on for a short while longer, with me gently patting Aletta on the back."
            "And when it's finally over, she seems to have recovered a little of her normal reserve."
            show aletta talkative at startle(0.1, 5)
            aletta.say "Erm..."
            aletta.say "Thanks again, [hero.name]..."
            aletta.say "But I don't think there's any need to tell Cherie about all of this."
            show aletta normal
            mike.say "Oh no...of course not."
            mike.say "It'll be our little secret."
            show aletta at startle(0.1, 5)
            pause 0.5
            hide aletta with easeoutright
            "Aletta nods and then turns on her heel, walking away and leaving me alone again."
            "Alone and hoping that I managed to do enough to shore up her defences for what lies ahead."
            $ aletta.love += 5
            $ aletta.flags.liability = True
        "''I'm terrified too''":
            "Part of me feels like I should be reassuring Aletta right now."
            "That I should be the strong one and tell her I'll make everything okay."
            "But what about me?"
            "I'm caught up in this mess too!"
            mike.say "You think I don't know all of that, Aletta?"
            mike.say "Hell, I haven't slept a wink since..."
            mike.say "Well, since IT happened!"
            "Aletta looks at me in genuine surprise."
            "Blinking and shaking her head as I begin to vent in front of her."
            show aletta surprised
            aletta.say "Of...of course, [hero.name]..."
            aletta.say "I wasn't trying to suggest that you didn't."
            show aletta scared
            "But there's no way she can hope to stem the tide."
            "Not now that the damn holding back my emotions has been breached."
            show aletta normal
            mike.say "Fucking hell, Aletta..."
            mike.say "You're worried about what'll happen to you..."
            mike.say "Did you ever think what they'll do to me?!?"
            "Aletta's still shaking her head at all of this."
            "But now she's looking around, like she's worried someone might overhear us."
            show aletta talkative
            aletta.say "Okay, okay..."
            aletta.say "I get it now, [hero.name]..."
            aletta.say "You're worried too."
            aletta.say "But I don't think this is doing either of us any good."
            show aletta happy
            aletta.say "So let's both go and...and try to collect our thoughts, okay?"
            show aletta sadsmile
            "I manage to nod in agreement, expecting Aletta to have more to say."
            show aletta at hshake
            pause 0.5
            hide aletta with easeoutright
            "But instead she nods, gives me a tense smile, and then hurries away."
            "Leaving me to stand there, wrestling with my own fears and paranoia."
            $ aletta.love -= 5
            $ aletta.flags.threat = True
    $ hero.cancel_activity()
    $ game.room = "forest"
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    return

label cherie_event_04:
    if cherie.love.max < 80:
        $ cherie.love.max = 80
    scene bg rpgfeast at blur(5)
    show aletta date at dark, center, zoomAt(0.8, (1240, 720)), blur(5)
    show audrey date at dark, center, zoomAt(0.8, (740, 720)), blur(5)
    show lavish date at dark, center, zoomAt(0.8, (540, 720)), blur(5)
    show shiori sad date at dark, center, zoomAt(0.8, (240, 720)), blur(5)
    show breedad zorder 3 at blacker, center, zoomAt(1, (1040, 720))
    show camila zorder 3 at blacker, center, zoomAt(1, (140, 720))
    show vincent teaser zorder 3 at blacker, center, zoomAt(1, (440, 720))
    show violaine zorder 3 at blacker, center, zoomAt(1, (700, 720))
    with fade
    $ renpy.music.set_audio_filter("sound", af.Lowpass(440), replace=True)
    play sound crowd_theater fadein 1
    queue sound "<from 4 to 32>sd/SFX/ambiences/crowd/crowd_theater.ogg" loop
    "I've never been comfortable in formal attire, even at the best of times."
    "So being coerced into attending a full-blown charity gala in it isn't my idea of a fun time."
    "And then, when you heap on top of that everything to do with Dwayne's untimely demise..."
    "Well, let's just say that I'm feeling the weight of it all pressing down on me."
    "But then it's not like any of this was my idea."
    "I would never have..."
    show cherie sexydate talkative zorder 9 at dark, center, zoomAt(1.6, (640, 1020)), blur(8) with easeinleft
    cherie.say "[hero.name]…"
    stop sound fadeout 2
    cherie.say "Did I not already tell you to turn that frown the other way up?"
    scene bg rpgfeast
    show aletta date at center, zoomAt(0.8, (1240, 720))
    show audrey date at center, zoomAt(0.8, (740, 720))
    show lavish date at center, zoomAt(0.8, (540, 720))
    show shiori sad date at center, zoomAt(0.8, (240, 720))
    show breedad zorder 3 at blacker, center, zoomAt(1, (1040, 720))
    show camila zorder 3 at blacker, center, zoomAt(1, (140, 720))
    show vincent teaser zorder 3 at blacker, center, zoomAt(1, (440, 720))
    show violaine zorder 3 at blacker, center, zoomAt(1, (740, 720))
    show cherie sexydate sadsmile zorder 3 at center, zoomAt(1.6, (640, 1020))
    with Pixellate(1, 10)
    $ renpy.music.set_audio_filter("sound", None)
    play sound "<from 4 to 32>sd/SFX/ambiences/crowd/crowd_theater.ogg" loop
    "The sound of Cherie's voice instantly snaps me back to reality." with hpunch
    "And I almost flinch in surprise as I struggle to focus on the here and now."
    mike.say "Oh..."
    mike.say "Oh yeah..."
    "The problem is that my head's a complete dumpster fire right now."
    "And the best I can hope to pull of is only a vague imitation of normality."
    "None of which is helped by the fact that Cherie, as always, looks stunning."
    mike.say "And it's upside down, by the way."
    show cherie stuned at startle(0.05, -10)
    "Cherie wrinkles her brow and shakes her head at this."
    show cherie surprised
    cherie.say "What is, [hero.name]?"
    show cherie normal
    mike.say "The saying, Cherie..."
    mike.say "It's 'turn that frown upside down', yeah?"
    mike.say "You know, because it rhymes?"
    show cherie annoyed
    "Cherie rolls her eyes and makes a point of grabbing me by the arm."
    show cherie talkative at startle(0.1, 5)
    cherie.say "There is no time for that now, {i}mon ami{/i}."
    cherie.say "We must get out there and mingle."
    cherie.say "We must show all of these people that everything is good."
    show cherie normal
    "I'm nodding all the time that Cherie's giving me her little lecture."
    "Because despite all of my discomfort, I really am on board with the idea."
    "And at the same time I'm doing all I can to match her pace too."
    "But somehow she still manages to end up almost dragging me after her."
    "Luckily for me, I'm able to match her pace by the time we're amongst the crowd."
    "And once we are, it's all smiles and pleasant small-talk as we move amongst the guests."
    "It's also lucky for me that everyone here seems to be on the exact same page too."
    "All the people Cherie and I encounter are dressed up in their most expensive clothes."
    "And there's noting coming out of their mouths but the most bland of pleasantries."
    "Hell, I even manage to spot some of the girls from the office floating around too."
    mike.say "Ah, Cherie..."
    mike.say "You think that you could spare me for a couple of minutes?"
    "Cherie still looks distracted as I ask the question."
    "But she shakes her head and gives me a wave of the hand nonetheless."
    show cherie smile at startle(0.1, 5)
    cherie.say "I suppose so, {i}mon ami{/i}…"
    cherie.say "But do not wander too far."
    cherie.say "I may have need of your help before too long."
    hide cherie with easeoutleft
    "I answer that with a nod of my own and a smile for good measure."
    "And then I weave my way through the crowd of guests."
    "Already heading towards the colleagues that I want to chat with."
    menu:
        "Talk to Aletta":
            show aletta upset zorder 9 at center, zoomAt(1.4, (640, 920)) with fade
            "I find Aletta hovering in a corner, well away from the main throng of the gala."
            "Which I guess makes sense, as she's been a bag of nerves ever since what happened to Dwayne."
            mike.say "Hey, Aletta..."
            mike.say "How are you doing?"
            show aletta surprised at startle(0.05, -10)
            "As soon as she hears my voice, Aletta does the same thing that I did with Cherie earlier."
            "By which I mean that she visibly jumps on the spot, almost spilling the drink in her hand."
            show aletta normal
            "But being Aletta, she somehow manages to recover more quickly and pull herself together more completely."
            show aletta talkative
            if aletta.sub >= 25:
                aletta.say "Oh, [hero.name]…"
                aletta.say "Am I glad to see you!"
                aletta.say "All these people asking all these questions - how am I supposed to answer them?"
            elif aletta.sub <= -25:
                aletta.say "There you are, [hero.name]…"
                aletta.say "I feel like I should have you on a leash sometimes!"
                aletta.say "That way I could make sure you don't say the wrong thing to the wrong people."
            else:
                aletta.say "Oh, hello, [hero.name]."
                aletta.say "I'm coping as well as can be expected."
                aletta.say "But we should all be watching what we say to the people here."
            show aletta normal
            "Part of me wishes that Aletta could be a little warmer sometimes."
            "Maybe offer some support when the going gets tough like it is right now."
            "But then I guess she is right when she says that we need to be on guard."
            mike.say "You've got a point, Aletta."
            mike.say "Maybe we should limit who we talk to while we're here?"
            mike.say "You know, try to keep a lid on it?"
            "I feel a genuine sense of relief as Aletta nods and manages a little smile."
            "But maybe more for my own sake than for hers."
            $ aletta.love += 5
            show aletta date zorder 2 at center, zoomAt(0.8, (1240, 720)) with dissolve
        "Talk to Audrey":
            "Audrey's helping herself to the free drinks that have been provided."
            "And that means she's easy to find hanging around the bar, harassing the staff."
            "But as soon as she sees me approaching, I seem to become the centre of her attention."
            "Audrey walks towards me, a swagger visible in her step as she does so too."
            show audrey zorder 9 at center, zoomAt(1.4, (640, 920)) with fade
            if audrey.sub >= 25:
                show audrey happy at startle(0.1, 5)
                audrey.say "[hero.name]!"
                audrey.say "Over here!"
                audrey.say "Won't you come and pay me some attention?"
            else:
                show audrey talkative at startle(0.1, 5)
                audrey.say "There you are, [hero.name]!"
                audrey.say "I was starting to think that you'd forgotten all about little old me."
                audrey.say "And I was about to make a scene to get your attention!"
            show audrey flirt
            "Audrey's making a point of saying all of this in a pretty loud voice."
            "And I can already see people turning to look in our general direction."
            "But the last thing that I need is her making a spectacle of herself."
            mike.say "Ah..."
            mike.say "Yeah, Audrey - here I am..."
            mike.say "Paying you all of the attention I possibly can!"
            show audrey mock with dissolve
            "It doesn't take an expert to realise that Audrey can sense the tension in me right now."
            "From the way a knowing smile spreads across her face, I know that she intends to use that knowledge as well."
            "And by that I mean use it in the only way that she knows how - to her own advantage!"
            if audrey.sub >= 25:
                show audrey embarrassed at startle(0.1, 5)
                audrey.say "Oh, that's SO good to hear, [hero.name]…"
                audrey.say "Because I'm feeling exceptionally needy today!"
            else:
                show audrey joke at startle(0.1, 5)
                audrey.say "Is that so?"
                audrey.say "Then maybe you'd better prove it, huh?"
            show audrey mock
            mike.say "Okay, Audrey, here's the deal..."
            mike.say "Behave yourself until this thing is over."
            mike.say "Do that and I'll give you whatever you want afterwards."
            show audrey happy at startle(0.1, 5)
            if audrey.sub >= 25:
                audrey.say "Anything I want?!?"
                audrey.say "Oh, [hero.name] - you've got a deal!"
            else:
                audrey.say "You'd better be for real, [hero.name]."
                audrey.say "Because if not, I really will make you pay!"
            show audrey flirt
            "With that, Audrey turns her back on me and walks away."
            "Making me wonder what kind of deal with the devil I just struck."
            $ audrey.love += 5
            show audrey date zorder 2 at center, zoomAt(0.8, (740, 720)) with dissolve
        "Talk to Lavish":
            show lavish b zorder 9 at center, zoomAt(1.4, (640, 920)) with fade
            "Lavish is clutching a drink close to her chest when I finally spot her."
            show lavish pleased with dissolve
            "And it doesn't take long for her to see me too, waving me over as she does so."
            "In fact she looks pretty pleased to see me, which is a pleasant surprise."
            show lavish happy at startle(0.1, 5)
            if lavish.sub >= 25:
                lavish.say "[hero.name]…"
                lavish.say "Am I ever glad to see you!"
            else:
                lavish.say "Oh, hi, [hero.name]…"
                lavish.say "It's so good to finally see a friendly face!"
            show lavish normal
            mike.say "Hey, Lavish..."
            mike.say "The feeling's definitely mutual!"
            mike.say "These things can be a real challenge, huh?"
            show lavish pleased at startle(0.2, 10)
            pause 0.5
            show lavish normal with dissolve
            "Lavish nods eagerly as she takes another sip from her drink."
            show lavish talkative at startle(0.1, 5)
            lavish.say "And what makes it even worse is that I recognise lots of these people too."
            lavish.say "They are some really influential types here, very important individuals."
            lavish.say "I kind of want to talk to some of them, maybe network a little..."
            lavish.say "But I'm worried that would make me seem like some kind of mercenary!"
            show lavish normal
            "I'm looking around as Lavish confesses all of this to me."
            "Trying to work out what would be the better thing to tell her here."
            "Because on the one hand, I don't want anyone asking too many questions."
            "But on the other, we need to make it look like it's business as usual."
            mike.say "I'm sure you can introduce yourself to a couple of them, Lavish."
            mike.say "Just be careful to make it seem like you're not angling for a new job, that's all."
            show lavish pleased with dissolve
            "Lavish seems to be pleased with the idea of doing what she wanted, but in a discreet manner."
            "And she nods happily, before heading off to begin her round of schmoozing."
            $ lavish.love += 5
            show lavish date zorder 2 at center, zoomAt(0.8, (540, 720)) with dissolve
        "Talk to Shiori":
            play sfx1 woman_crying
            show shiori a at startle(0.1, -5)
            pause 0.2
            show shiori at startle(0.1, -5)
            "I can almost hear Shiori before I see her."
            play sfx1 woman_crying
            show shiori at startle(0.1, -5)
            pause 0.2
            show shiori at startle(0.1, -5)
            "Because the sound of sniffling reaches my ears over the background hum of conversation."
            show shiori sad zorder 9 at center, zoomAt(1.4, (640, 920)) with fade
            "And when I finally make it over to Shiori, I see that she's really made an effort to dress up."
            play sfx1 woman_crying
            show shiori at startle(0.1, -5)
            pause 0.2
            show shiori at startle(0.1, -5)
            "But the effect is kind of ruined by the fact that she's been crying, so her eyes are all pink and puffy."
            play sfx1 woman_crying
            show shiori at startle(0.1, -5)
            pause 0.2
            show shiori at startle(0.1, -5)
            mike.say "Shiori..."
            mike.say "Are you okay?"
            mike.say "Did somebody upset you?"
            show shiori happy with dissolve
            "Shiori seems to cheer up almost as soon as she sees me, a smile spreading across her face."
            show shiori at center, traveling(2.4, 0.7, (740, 1420))
            "And when I reach her side, she surprises me by throwing her arms around my waist."
            "I'm kind of thrown, not used to her making such gestures in public."
            "So all I can do in response is to gently pat her on the back."
            show shiori whining
            if shiori.sub >= 25:
                shiori.say "Oh, Mister [hero.family_name]..."
                shiori.say "I still can't believe what happened to poor Mister Johnson!"
                shiori.say "I start crying whenever I think about it."
            else:
                shiori.say "Oh, [hero.name]..."
                shiori.say "I can't stop thinking about what happened to Mister Johnson."
                shiori.say "And worrying that the same thing might happen to you too!"
            show shiori sad
            "Oh man, this is going to be tough."
            "Part of me actually likes having Shiori throw herself at me like this."
            "And another part of me would like to ask if I could use her chest as a pillow too!"
            "But right now I need to make sure that she's able to make it through this thing."
            "Because having her collapse into a blubbering mess in front of everyone isn't a good look."
            mike.say "It's okay, Shiori..."
            mike.say "I'm sure everyone is as cut up about Dwayne as you are."
            mike.say "They're just a little better at hiding it, you know?"
            mike.say "So maybe we can put a brave face on it for the rest of today?"
            mike.say "Then you can come and see me in the office tomorrow morning."
            show shiori sadsmile
            mike.say "And we can talk all about it, if you'd like?"
            show shiori talkative
            if shiori.sub >= 25:
                shiori.say "You'd...you'd do that for me?"
                shiori.say "I think I can be strong, now that I know that."
            else:
                shiori.say "You know that I'd do anything for you, [hero.name]."
                shiori.say "So I'll be strong - and I'll see you tomorrow!"
            "Shiori gives me a smile and a wave as she walks away."
            "And I make sure to return both, hoping that she can be as strong as she promised."
            $ shiori.love += 5
            show shiori date zorder 2 at center, zoomAt(0.8, (240, 720)) with dissolve
    "I'm just about to allow myself to relax a little."
    "To think that all of this might actually work out."
    show cassidy date zorder 1 at center, zoomAt(0.8, (840, 720))
    play sfx1 crowd_yeah
    "And, of course, that's when I hear a commotion on the other side of the room."
    show breedad zorder 3 at blacker, center, traveling(1, 0.7, (1180, 720))
    pause 0.3
    show vincent teaser zorder 3 at blacker, center, traveling(1, 0.7, (240, 720))
    pause 0.5
    show violaine zorder 3 at blacker, center, traveling(1, 0.7, (340, 720))
    pause 0.5
    "I do the best I can to elbow my way through the crowd without actually hurting any of the guests."
    show audrey date at center, traveling(0.8, 0.7, (340, 720))
    pause 0.2
    show lavish date at center, traveling(0.8, 0.7, (340, 720))
    pause 0.2
    show shiori date at center, traveling(0.8, 0.7, (240, 720))
    "And when I make it over to the source of the problem, I'm not surprised by what I see before me."
    "Cassidy is right there, looking like she just swept into the place as though she owned it."
    show cherie sexydate annoyed zorder 1 at center, zoomAt(0.8, (600, 720)) with easeinleft
    "And on the other hand, there's Cherie, glaring at her daughter with genuine enmity in her eyes."
    "Luckily for everyone involved, they're far enough away from the other guests not to be overheard."
    "But I'm soon closing the gap between us, and so I can hear every word they exchange."
    scene bg rpgfeast at center, zoomAt(1.4, (640, 820))
    show cherie sexydate at center, zoomAt(1, (340, 720))
    show cassidy date at center, zoomAt(1, (840, 720))
    with fade
    pause 1
    show cherie angry at startle(0.075, 10)
    cherie.say "Cassidy..."
    cherie.say "What in the hell are you doing?!?"
    show cherie annoyed
    show cassidy surprised
    cassidy.say "Really, Mother..."
    cassidy.say "I would have thought that was obvious, even to you."
    cassidy.say "What else would I be doing but attending this dreary little affair of yours?!?"
    show cassidy upset
    show cherie angry at startle(0.075, 10)
    cherie.say "I told you to be here before the doors opened."
    cherie.say "So that we could greet the guests and present a united front."
    cherie.say "Walking in as late as this, you...you would have been better staying away!"
    show cherie annoyed
    "I can see that Cherie's getting angrier and less composed by the second."
    "And at the same time, Cassidy's feeding on her mother's discomfort."
    "It feels like this would be the right time for me to step in and try to calm things down."
    show cassidy at center, traveling(1.2, 1, (840, 820))
    "But as soon as Cassidy realises I'm there, she seems to kick things up a notch."
    show cassidy surprised
    cassidy.say "What do you say, [hero.name]?"
    cassidy.say "You worked for Daddy, didn't you?"
    cassidy.say "What would he have said about Mother trying to take over like this?"
    cassidy.say "Would he have wanted her to strut around, telling me what do do?"
    show cassidy upset
    "Suddenly I'm aware of the fact that both of them are staring at me."
    "Mother and daughter, looking me in the eye and waiting to see what I have to say."
    "And no doubt both of them expecting me to take their side in the matter."
    menu:
        "Side with Cherie":
            if cassidy.is_girlfriend:
                "I know that Cassidy and I are technically an item right now."
                "But I also have to think about the whole situation with the company."
            else:
                "Another time I might have sided with a girl as incredibly hot as Cassidy."
                "But right now I have to think about the whole situation with the company."
            "And that means that I'm going to have to come to Cherie's aid on this occasion."
            mike.say "I don't know what Dwayne would have said or done, Cassidy..."
            mike.say "But I do know for sure that he would have said this isn't the time or place to be discussing it."
            mike.say "And I know for sure that he'd have told you to settle down and behave in front of all these people."
            show cherie smile at startle(0.1, -5)
            show cassidy surprised at center, traveling(1.2, 0.1, (840, 830))
            "Cassidy's jaw literally drops open as I make a point of putting her in her place."
            "But before she can mount a counter-offensive, Cherie steps into the fray as well."
            show cherie talkative at startle(0.1, 5)
            cherie.say "[hero.name] is right."
            cherie.say "We will discuss this another time."
            cherie.say "And when we do, it will be in private."
            show cherie normal
            show cassidy angry at hshake
            "Cassidy looks like she's about to fire back at her mother."
            "But then she seems to think better of it."
            show cassidy at startle(0.1, -5)
            pause 0.1
            hide cassidy with easeoutleft
            pause 0.5
            show cherie closed with dissolve
            "Because she stamps her foot and then storms off towards the bar instead."
            show cherie whining at startle(0.1, 5)
            cherie.say "Oh my goodness!"
            cherie.say "What ever am I going to do with that girl?"
            show cherie smile
            cherie.say "And thank you for your help too, {i}mon ami{/i}."
            show cherie amused
            hide cherie with easeoutleft
            $ cherie.flags.hero_rivalry -= 2
            $ cherie.love += 5
            $ cassidy.love -= 5
        "Side with Cassidy":
            if cassidy.is_girlfriend:
                "Urgh...I know this is going to be like adding fuel to the fire."
                "But I'm in a relationship with Cassidy, so I feel like I need to have her back."
            else:
                "It'd be far easier and less messy just to side with Cherie on this one."
                "But I feel like she's getting too comfortable with being the one in charge around here."
            "And that means I'm going to have to side with the daughter over the mother on this one."
            mike.say "I don't think this is the time or place to thrash it out."
            mike.say "But I do think that Cassidy's got a point, Cherie."
            show cherie stuned
            mike.say "You can't just go an acting like you're taking Dwayne's place in everything."
            show cassidy happy at startle(0.1, -5)
            show cherie surprised at center, traveling(1, 0.1, (340, 730))
            "Cherie's jaw literally drops open as I make my put her in her place."
            show cassidy normal
            "But before she can mount a comeback, Cassidy seems to see her chance."
            show cassidy at startle(0.1, 5)
            cassidy.say "[hero.name]'s right, Mother..."
            cassidy.say "You're acting like you're in control of everything and everyone!"
            cassidy.say "Maybe it's time I went and hired a lawyer of my own."
            show cherie annoyed at hshake
            "Cherie looks like she's about to fire back at her daughter."
            "But then it's almost like the weight of it all suddenly pushes down on her shoulders."
            hide cherie with easeoutleft
            "And she turns away, walking off towards the bar in search of a drink."
            "As soon as she's out of earshot, Cassidy looks me straight in the eye."
            show cassidy surprised at startle(0.1, 5)
            if cassidy.sub >= 25:
                cassidy.say "Oh, thank you so much!"
                show cassidy happy
                cassidy.say "I could never have stood up to mother like that without you being here!"
            elif cassidy.sub <= -25:
                cassidy.say "Well done for backing me up when I needed it, [hero.name]."
                cassidy.say "That really helped me out, and it deserves a reward."
            else:
                cassidy.say "Thanks for taking my side, [hero.name]."
                show cassidy wink
                pause 0.3
                show cassidy normal with dissolve
                cassidy.say "I mean, I can handle her myself - but having you weigh in too really helped!"
            hide cassidy with easeoutright
            $ cherie.flags.hero_rivalry += 2
            $ cassidy.love += 5
            $ cherie.love -= 5
    show bg rpgfeast at sepia, blur(5)
    with Pixellate(1, 10)
    $ renpy.music.set_audio_filter("sound", af.Lowpass(440), replace=True)
    play sound crowd_theater fadein 1
    queue sound "<from 4 to 32>sd/SFX/ambiences/crowd/crowd_theater.ogg" loop
    "With the confrontation between Cherie and Cassidy defused, I take a moment to collect myself."
    "Only realising when I walk away from them both just how stressful being around two such feasty women can be."
    "But I hardly feel like my heart has slowed down and stopped pounding in my chest when I hear footsteps approaching."
    "I spin around, expecting another confrontation, maybe even that the damn police have crashed the event too."
    scene bg rpgfeast at center, zoomAt(1.4, (640, 820))
    show cherie sexydate smile at center, zoomAt(1.6, (640, 1020))
    with Pixellate(1, 10)
    $ renpy.music.set_audio_filter("sound", None)
    play sound "<from 4 to 32>sd/SFX/ambiences/crowd/crowd_theater.ogg" loop
    "So it comes as a genuine surprise to find Cherie standing before me."
    "From the look on her face, she seems to have used the intervening time to calm herself down again."
    "And she's holding two glasses of champagne, one of which she offers to me."
    show cherie talkative at startle(0.1, 5)
    cherie.say "I must apologise for earlier, mon ami."
    cherie.say "Cassidy and I have always clashed at times like this."
    cherie.say "And so it is only natural that she would behave in such a way."
    show cherie normal
    play sfx1 drinking
    "I make a point of shrugging as I accept the glass from Cherie and take a sip."
    mike.say "Ahh..."
    mike.say "There's no need to apologise, Cherie."
    mike.say "What with everything that's happened recently..."
    mike.say "You've both been through the roughest of times."
    show cherie at startle(0.2, 10)
    "Cherie nods at this, but I notice that she has a thoughtful look on her face."
    show cherie talkative at startle(0.1, 5)
    cherie.say "That may be so, {i}mon ami{/i}..."
    cherie.say "But it is also important that we make new alliances for the sake of the future."
    cherie.say "And I for one know who I can rely upon to be my ally."
    cherie.say "I do not think that I could have made it this far without..."
    cherie.say "Without your composure."
    show cherie normal
    "Cherie holds up her glass, gesturing for me to do the same."
    "And once I've done as she asks, she taps her own against mine."
    show cherie talkative
    cherie.say "I propose a toast..."
    show cherie happy at startle(0.1, 5)
    cherie.say "To new beginnings."
    show cherie smile
    mike.say "To new beginnings."
    play sfx1 drinking
    "I nod and take a sip of my drink as Cherie does the same."
    "And all the time she's looking me straight in the eye."
    "Though not with the kind of intensity one reserves for a business partner!"
    "Soon enough some important person or another needs to talk to Cherie."
    hide cherie with easeoutleft
    "And so she's dragged away from me to attend to other business."
    "But by now the crowd seem to have thinned out as people drift away."
    "Which makes me think this would be a good time to slip away unnoticed myself."
    "I put down my empty glass and start making for the door."
    "All the time hoping that I might bump into Aletta, Audrey, Lavish or Shiori agian."
    "As I could use the company and someone to split the taxi-fare home with right now."
    "But as fate would have it, another girl entirely is the one that cuts off my exit."
    show bg rpgfeast at center, traveling(2, 3, (440, 1120))
    pause 2.7
    show cassidy date talkative at center, zoomAt(1.8, (640, 1120)) with easeinright
    show bg rpgfeast at center, zoomAt(2, (440, 1120)) with hpunch
    cassidy.say "And just where do you think you're going?"
    show cassidy normal
    "I turn around just in time to see Cassidy striding towards me."
    "And in that moment, I know that there's no chance of escape."
    show cassidy whining at startle(0.1, 5)
    if cassidy.is_girlfriend:
        if cassidy.sub >= 25:
            cassidy.say "I just wanted to say how sorry I am about that run in with my mother, [hero.name]."
            show cassidy talkative
            cassidy.say "And to say that if there's anything I can do to make it up to you - just ask."
        elif cassidy.sub <= -25:
            cassidy.say "You're not leaving without saying goodbye to me, are you, [hero.name]?"
            show cassidy talkative
            cassidy.say "Shouldn't you be asking my permission to be dismissed?"
        else:
            cassidy.say "Sorry again for you getting dragged into that little family squabble, [hero.name]."
            show cassidy talkative
            cassidy.say "But I'm sure we can find a way to make it up to each other, right?"
        show cassidy normal
        "As tired and mentally drained as I'm feeling, I stop as soon as I see Cassidy."
        "Because I have to admit that being this close to her is actually making me feel better."
        "And it's reminding me of the bond that already exists between us too."
        mike.say "I'm sorry, Cassidy..."
        mike.say "I should have come and found you before I tried to leave."
        mike.say "All of this business with your mom's kind of fried my brain!"
        "Cassidy nods, leaning in closer than before."
        show cassidy b whining at startle(0.1, 5)
        cassidy.say "I know how that feels, trust me!"
        show cassidy b talkative
        cassidy.say "But I also know the perfect thing to fix it too!"
        cassidy.say "Call me later tonight and we'll get together, okay?"
        show cassidy b normal
        pause 0.3
        hide cassidy with easeoutright
        "I nod as Cassidy slips away from me and back into the crowd."
        "My head already filling with ideas of just what she might have in store for me later."
    else:
        mike.say "Ah..."
        mike.say "Hey, Cassidy..."
        mike.say "Look, I'm sorry for getting into the discussion you were having with your mom earlier."
        mike.say "I know things can't be easy for either of you right now."
        "To my surprise, Cassidy shakes her head and waves away my words."
        "Dismissing my attempt to make peace with her as if she's simply not interested."
        show cassidy talkative at startle(0.1, 5)
        cassidy.say "Yeah, yeah, yeah..."
        cassidy.say "I know what you're trying to do, [hero.name]..."
        cassidy.say "But I don't work for my Dad and I'm not my mother either."
        cassidy.say "What I want isn't bland platitudes and bullshit - it's you!"
        show cassidy normal
        "I feel my eyes go wide as Cassidy makes herself plain to me."
        mike.say "You..."
        mike.say "You want...ME?!?"
        show cassidy happy at center, traveling(2.2, 2, (640, 1320))
        "Cassidy chuckles as she moves in closer still."
        show cassidy normal at center, zoomAt(2.2, (640, 1320))
        "Not stopping until she's more than close enough to touch me."
        show cassidy talkative at startle(0.1, 5)
        cassidy.say "What I mean is that I want you on my side, [hero.name]."
        cassidy.say "I want you fighting for me the way you did for my father!"
        show cassidy normal
        "I do the best I can to hide my all to obvious disappointment as Cassidy clarifies her meaning."
        "Nodding my head and trying to make the tone of my voice more formal, more business-like."
        mike.say "Oh..."
        mike.say "Oh yeah...of course."
        mike.say "That's what I thought you meant."
        show cassidy happy at startle(0.1, 5)
        "Cassidy chuckles again, and this time it's an irresistibly seductive sound."
        show cassidy talkative b at startle(0.1, 5)
        cassidy.say "Oh no, [hero.name]..."
        cassidy.say "I want to fuck you too!" with hpunch
        cassidy.say "You see, I'm used to having my cake and eating it."
        cassidy.say "Used to getting what I want when I want it."
        cassidy.say "So I'll give you what you want as an incentive, okay?"
        cassidy.say "Call me later tonight and we'll get together."
        show cassidy b normal
        pause 0.3
        hide cassidy with easeoutright
        "I nod as Cassidy slips away from me and back into the crowd."
        "But then it hits me that I'm going to have to make a decision here."
        "To choose between staying loyal to Cherie or betraying her and backing Cassidy in this fight."
        "Unless there's some way I can manage to have my cake and eat it too?"
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    return

label cherie_event_05:
    if cherie.love.max < 100:
        $ cherie.love.max = 100
    scene bg ceo with fade
    "It still feels kind of weird, having Cherie summon me to her office in the same way Dwayne used to."
    "And when I walk in there, a part of me is still expecting to see him sitting behind the desk, like a king on his throne."
    show cherie upset at center, zoomAt(1.0, (1040, 720))
    "But I have to admit that it's a lot more aesthetically pleasing to see Cherie looking up from the papers in front of her."
    mike.say "Hey, Cherie..."
    mike.say "You call and I come running!"
    "Cherie's face was twisted into what looked almost like a grimace when I first walked into her office."
    "But almost as soon as she realises that it's me standing in front of her, it visibly lightens."
    show cherie normal at center, traveling(1.25, 0.5, (940, 880))
    "And I'd swear that she's doing all she can to remain serious, rather than breaking into a smile."
    show cherie talkative
    cherie.say "Oh, I hate it when you do that to me, {i}mon ami{/i}!"
    cherie.say "Here I am, trying to be professional and get things done..."
    cherie.say "But then I see that smile on your face and..."
    play sound door_open
    pause 0.7
    play sound door_slam volume 2
    pause 0.5
    show cherie stuned at hshake
    with vpunch
    "Before Cherie can finish what she's trying to say, the doors behind me burst open."
    "In fact they're flung open with such force that they slam into the walls with tremendous crash."
    mike.say "What the..."
    show cherie surprised
    cherie.say "Who is..."
    show cherie stuned at hshake
    aletta.say "CHERIE..."
    aletta.say "Cherie, I need to see you...NOW!"
    show aletta at center, zoomAt(1.25, (440, 880)) with easeinleft
    "I find myself instinctively stepping out of the way as Aletta comes thundering into Cherie's office."
    "I'm not even sure that she's seen me, as her gaze is focussed on the other woman entirely."
    "And Aletta doesn't stop until she's literally leaning on the desk, looming over Cherie."
    show cherie angry
    cherie.say "Aletta..."
    cherie.say "What is the meaning of this...this intrusion?!?"
    cherie.say "Can't you see that I'm in the middle of..."
    show cherie annoyed
    show aletta angry
    aletta.say "I don't care what you're in the middle of."
    aletta.say "You're going to listen to what I have to say!"
    show aletta upset
    "I watch as Cherie remains amazingly calm, even with Aletta almost bearing down on her."
    "And I can't help being impressed when all she does is raise a single eyebrow in response."
    show cherie talkative
    cherie.say "And just what would that be, Aletta?"
    cherie.say "What exactly is it that you have to say to me?"
    show cherie normal
    show aletta angry
    aletta.say "That I won't be made the scapegoat for your husband vanishing off face of the Earth!"
    aletta.say "Because I know that's what you're doing your best to make happen, Cherie..."
    aletta.say "Letting the damn police get just close enough to suspect that it was me who did it."
    aletta.say "And you'd better listen to me too, because if I go down - then I'm taking you with me, Cherie!"
    show aletta upset
    show cherie closed
    "Cherie leans back in her chair and takes a deep breath."
    "She holds it in for a few seconds, and then lets it out as a sigh."
    show cherie normal with dissolve
    cherie.say "Hmm..."
    show cherie talkative
    cherie.say "That's a very serious accusation, Aletta..."
    cherie.say "Wouldn't you agree, [hero.name]?"
    show cherie annoyed
    "It seems that I was right, and Aletta really didn't see me when she came storming in."
    show aletta stuned
    "Because as soon as Cherie says my name and looks in my direction, Aletta almost leaps backwards."
    "And then she turns on her heel, seeing me for the first time, a look of surprise on her face."
    "But the truth is that it's not much different from the look on my own face in that moment."
    show aletta surprised
    aletta.say "[hero.name]…"
    aletta.say "What...what are you doing there?!?"
    show aletta stuned
    mike.say "I was just here to see Cherie, that's all."
    mike.say "I had no idea you were going to come in here, Aletta."
    if aletta.is_girlfriend:
        "It only takes a couple of seconds for Aletta's surprise to fade."
        "And then she seems to realise that she has a potential ally in the room."
        show aletta talkative
        if aletta.sub >= 25:
            aletta.say "You know more about this than either of us, [hero.name]…"
            aletta.say "So you could make her see sense, couldn't you?"
        elif aletta.sub <= -25:
            aletta.say "What are you waiting for, [hero.name]?"
            aletta.say "You already know that I'm right - so make her see sense!"
        else:
            aletta.say "You know me better than anyone, [hero.name]…"
            aletta.say "So you know that I'm right about all of this, don't you?"
    else:
        "It doesn't take Aletta long to get over her initial surprise at seeing me."
        "And as she regains her mental equilibrium, her attitude to me seems to change."
        "Where before she seemed to see me as a threat, now she sees a potential ally."
        show aletta talkative
        aletta.say "You're as deep into this thing as either of us, [hero.name]…"
        aletta.say "So you have to make her see sense, right?"
        aletta.say "You have to make her admit what she's trying to do!"
    show aletta normal
    "I start to hold up my hands, appealing to Aletta for her to calm down."
    "Because all of this is happening too quickly for me to be able to make sense of it."
    "And I'm afraid of being talked into a corner before I know what's really going on."
    "But before I can say a word myself, Cherie's talking again."
    show cherie angry at startle(0.1, 5)
    cherie.say "How dare you, Aletta?"
    cherie.say "How dare you come in here, throwing around such allegations?!?"
    show cherie at startle(0.1, 5)
    cherie.say "And as for you, [hero.name]..."
    cherie.say "Are you just going to stand there and let her do it?"
    cherie.say "Why, are you defending her?"
    show cherie upset
    "Cherie's last question hits me like a slap across the face."
    "Is she really accusing me of defending Aletta?"
    "And why - because I haven't managed to get a word in edgeways yet?"
    "All I did was walk in her at her request and get caught in the cross-fire!"
    "Now Cherie and Aletta are both staring at me."
    "Each expecting me to come to their defence and tear into the other."
    menu:
        "Defend Aletta":
            "Cherie might have accused me of siding with Aletta out of sheer anger and desperation."
            "But the notion somehow sets the wheels turning inside of my head."
            "And the more I think about it, the more logical Aletta's side of the argument seems to me."
            mike.say "Well maybe I am defending her, Cherie..."
            mike.say "But that's only because it's the sane thing to do."
            show cherie stuned
            "Cherie's eyes go wide as she listens to what I have to say."
            "And then she blinks, shaking her head in disbelief."
            show cherie surprised with dissolve
            cherie.say "What..."
            cherie.say "What are you saying?"
            show cherie stuned
            "I can tell that I'm skating on thin ice with Cherie right now."
            "But it's not like I can go back on what I just said."
            "So instead I push on, consequences be damned."
            mike.say "I'm saying that you could be doing more to protect Aletta."
            mike.say "After all, she's not the one that was behind Dwayne's mur…"
            mike.say "I...I mean Dwayne's disappearance."
            mike.say "The way you treat her, no wonder she thinks that you're going to sell her to the cops!"
            mike.say "And I for one won't stand back and let that happen either."
            "Cherie doesn't say anything at first, just sits back in her chair, looking stunned."
            "But a quick glance in Aletta's direction is enough to let me know that she's reacting in a totally different manner."
            "Where before she seemed to be almost frantic with worry, now Aletta's regained some of her former confidence."
            show aletta talkative
            aletta.say "Thank you, [hero.name]…"
            aletta.say "At least one person is on my side!"
            show aletta normal
            show cherie whining
            cherie.say "Oh, so we're all taking sides now, are we?!?"
            cherie.say "Because neither of you seem to be on mine!"
            show cherie sad
            $ aletta.love += 5
            $ cherie.love -= 5
            $ cherie.flags.hero_rivalry += 5
        "Side with Cherie":
            "I can totally understand where Aletta's coming from on this one."
            "But I also know that there's just no way to clue her in on everything."
            "And the fact that she's almost losing it makes matters even worse."
            "Because if she cracks and goes running to the police, we're all fucked!"
            mike.say "I'm not defending her, Cherie..."
            mike.say "In fact I think she's losing her mind!"
            show aletta stuned with dissolve
            show cherie normal
            "Aletta's eyes go wide as I pretty much throw her under the metaphorical bus."
            "And she takes an unconscious step away from me towards the door."
            show aletta surprised
            aletta.say "[hero.name]…"
            aletta.say "You can't mean that, surely?"
            show aletta stuned
            "But the effect on Cherie is quite the opposite of that on Aletta."
            "She's looking more empowered and sure of herself by the second."
            show cherie talkative
            cherie.say "Oh, but I think he does mean it, Aletta."
            cherie.say "And I see that your list of allies grows thin!"
            show cherie normal
            "I feel like I'm stabbing Aletta in the back right now."
            "But I'm already committed to backing Cherie in this fight."
            "So I can't start back-pedalling now."
            mike.say "You're letting your paranoia dictate to you, Aletta."
            mike.say "And it's making you see enemies everywhere you look."
            mike.say "I'd be the first one to help you, if I could."
            mike.say "But the truth is that you have to stop accusing everyone else first."
            "Cherie nods slowly as I keep on delivering more verbal blows to Aletta."
            "And every one of them seems to stagger her just a little more than before."
            show cherie talkative
            cherie.say "So you see, Aletta..."
            cherie.say "This isn't a fight you're going to win!"
            show cherie normal
            show aletta angry
            aletta.say "Oh, so you admit that this is a fight then?"
            aletta.say "Well that's fine with me!"
            show aletta upset
            $ aletta.love -= 5
            $ cherie.love += 5
            $ cherie.flags.hero_rivalry -= 5
        "Try to remain neutral":
            "Urgh...this is the kind of situation that I hate more than anything."
            "Being able to look from Aletta to Cherie and realise that they both have a point."
            "But at the same time they're both pushing their own agendas too."
            "Which means that I have to do all I can to build bridges between them."
            mike.say "I'm not trying to defend her, Cherie..."
            show aletta stuned
            show cherie normal
            "As soon as the words are out of my mouth, Cherie seems to rally."
            "And at the same time, Aletta reels like she's been slapped in the face."
            mike.say "But I'm not taking your side over hers either."
            show aletta normal
            show cherie stuned
            "And once I've blurted out the second line, those positions are reversed."
            "But now the pair of them are beginning to look more than a little confused too."
            show cherie whining
            cherie.say "Then just what are you doing, {i}mon ami{/i}?"
            cherie.say "Because your intentions are not at all clear."
            show cherie sadsmile
            show aletta talkative
            aletta.say "Just who's side are you on, [hero.name]?"
            aletta.say "Hers or mine?"
            show aletta sadsmile
            "I make a point of groaning and shaking my head at their questions."
            mike.say "Argh..."
            mike.say "Will the two of you stop thinking of yourselves for one second?"
            mike.say "Will you face up to the fact that we're all in this together?"
            mike.say "It's us against the police, okay?"
            mike.say "And they want to turn us against each other!"
            "I don't need to be told that my little rant hasn't gone down too well."
            "Cherie is leaning back in her chair, arms crossed over her chest."
            "And Aletta seems to be making sure there's nothing between her and the door."
            show cherie talkative
            cherie.say "It is all well and good saying that we should be allies, {i}mon ami{/i}…"
            cherie.say "But for that to work, there must also be trust between us."
            show cherie normal
            show aletta angry
            aletta.say "Why would I trust either of you two?"
            aletta.say "All you've done is use me and then toss me to the sharks!"
            $ aletta.love -= 2
            $ cherie.love -= 1
    show aletta angry
    aletta.say "Whatever happens, I won't go down alone!"
    show aletta upset
    "I open my mouth to try and offer a counter-argument."
    "But before I can get a word out, Aletta turns on her heel."
    hide aletta with easeoutleft
    pause 0.3
    play sound door_slam volume 2
    "And then she storms out, slamming the doors behind her."
    "As soon as we're alone again, the fight seems to drain out of Cherie."
    "In fact she sags in her chair with such drama that I think there could be something seriously wrong."
    mike.say "Cherie..."
    mike.say "Are you feeling okay?"
    show cherie talkative
    cherie.say "Ah..."
    cherie.say "I cannot recall ever feeling this tired before, {i}mon ami{/i}."
    cherie.say "I thought that Dwayne's passing would be the answer to all of my problems."
    cherie.say "I told myself that it would free me - but I fear that it has damned me instead!"
    show cherie sadsmile
    mike.say "Don't give in to that kind of thinking, Cherie."
    mike.say "I'm sure that we're almost there, almost through this thing."
    mike.say "All we need to do is hold on a little longer, to keep each other strong."
    show cherie talkative
    cherie.say "Oh, [hero.name]…"
    cherie.say "I wish that I had your strength, your optimism."
    show cherie normal
    "I feel like I should be saying more, that I should find the words to lift Cherie up."
    "But the truth is that she's not the only one that's tired."
    "And Aletta's not the only one feeling anxiety."
    "I just don't know which one of us will be the first to break."
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    return

label cherie_event_06:
    if cherie.love.max < 120:
        $ cherie.love.max = 120
    scene expression f"bg {game.room}" with fade
    "I still feel like the whole affair with Dwayne's demise is dominating my life."
    "As though every quiet moment that I get is suddenly invaded by thoughts about it."
    "And I find myself lying awake at night, going over the details again and again."
    "So any distraction that comes my way, I tend to pounce on without hesitation."
    "Doing anything for even a few moments of relief from the magnitude of the problem."
    "And even when a potential distraction is related to it, I still leap at the chance."
    "Especially if it just so happens to involve someone else that's wrapped up in it too."
    play sound cell_vibrate
    "Which is why, when my phone rings and the call is from Cherie, I instantly pick it up."
    scene expression f"bg {game.room}" at blur(5), dark
    $ renpy.show_screen("smartphone_choice", "Cherie", show_mc=False, accept_only=True)
    with dissolve
    mike.say "Hey, Cherie..."
    mike.say "Is everything okay?"
    mike.say "Do you need me to do anything for you?"
    "There's a brief pause on the other end of the line, as if Cherie's momentarily overwhelmed."
    "But it doesn't take her long to recover and reply."
    cherie.say "Oh, [hero.name]..."
    cherie.say "You sound so keen tonight, so eager to please me!"
    "There's just something about the way Cherie says what she has to say."
    "The combination of her accent and the unusual choice of words."
    "Somehow it always conspires to make me almost blush."
    mike.say "Oh, I don't know about that, Cherie..."
    mike.say "I was just trying to be helpful, you know?"
    mike.say "We need to stick together in times like these."
    cherie.say "But of course..."
    cherie.say "And so you will no doubt be eager to come over to see me tonight, yes?"
    cherie.say "Because I would like you to sit with me and..."
    cherie.say "Discuss company strategy...yes, to discuss that and other purely business matters."
    "It doesn't take a genius to get the vibe there's something else going on here."
    "That Cherie's feeding me a cover story to cover the true nature of the meeting."
    "But then even if she is actually wanting to talk shop with me, so what?"
    "We're already deeply embroiled in the messy business of Dwayne's disappearance."
    "And on top of that, it's a chance to spend some quality alone time with Cherie."
    mike.say "Okay, Cherie..."
    mike.say "I'll pop over this evening."
    cherie.say "Very good, {i}mon ami{/i}..."
    cherie.say "I'll be sure to make you very welcome."
    $ renpy.hide_screen("smartphone_choice")
    scene expression f"bg {game.room}"
    with dissolve
    "Almost as soon as I end the call, Cherie becomes the only thing I can think about."
    "And that means that the hours between then and the proposed meeting just fly past."
    scene bg mansionentrance with fade
    "It feels like the very next moment that I find myself walking up the driveway."
    "Gazing up at the always impressive sight of Dwayne's...I mean Cherie's house."
    "Though I guess calling it a mansion would be more accurate."
    "But the weird thing is that when Dwayne was alive, this place seemed to be an extension of his personality."
    "I mean it was huge, imposing and totally trying to impress anyone that laid eyes upon it."
    "And yet now it seems to be a totally different place without his presence to lend it those qualities."
    "Not much of the place is lit up, making its bulk appear to lurk in the darkness."
    "Almost as if the house is now doing the best it can to hide itself away from prying eyes."
    "By the time I make it to the grand front-door, I'm beginning to feel a little spooked."
    "Like I'm walking up to the haunted house at the amusement park, rather than someone's home."
    scene bg door mansionentrance at center, zoomAt(1.0, (640, 720)) with fade
    pause 0.3
    show bg door mansionentrance at center, traveling(1.5, 1.0, (640, 1040))
    "So much so that I'm almost afraid to ring the bell when I finally get there."
    "But then I stop and take a moment to have a word with myself."
    "To remind myself of why I'm here and who I've come to see."
    play sound door_bell
    "And that done, I ring the bell, listening to the sound of it chiming loudly beyond the door."
    play sound door_lock
    "Luckily for me, the next sound I hear is that of the locks opening and the bolts being slid."
    scene bg mansion at dark, center, zoomAt (1.5, (640, 1040)), blur(5)
    show cherie sad casual at center, zoomAt(1.5, (640, 1040))
    with fade
    "Then one of the doors swings open, just enough to allow Cherie to poke her head around it."
    "I see that there's a nervous expression on her face as she looks out."
    "Like Cherie's worried about just who could be standing on her doorstep."
    show cherie smile
    "But as soon as she lays eyes on me, she smiles and pushes the door all the way open."
    show cherie happy
    cherie.say "[hero.name]..."
    cherie.say "It is so good to see you!"
    show cherie sad at center, zoomAt(1.5, (140, 1040)) with ease
    "Cherie steps aside to make room for me to enter, waving me inside at the same time."
    scene bg mansion with fade
    "And I don't hesitate to accept the invitation, returning the smile as I hurry through the doorway."
    mike.say "The feeling's mutual, Cherie!"
    mike.say "Although it does feel a little weird, you know?"
    play sound door_close
    "Cherie frowns a little as she closes the door behind me."
    "And I notice that she's careful to secure all of the locks too."
    show cherie casual talkative at center, zoomAt(1.25, (640, 880)) with easeinright
    cherie.say "Why do you say that, {i}mon ami{/i}?"
    cherie.say "Have we not spent a great deal of time together already?"
    cherie.say "Do we not know each other very well by now?"
    show cherie normal
    "Okay, now I'm regretting coming out with a line like that."
    "Because it was supposed to be one of those dumb, throwaway things to say."
    "The kind of conversational gambit most people would just hear and ignore."
    "But not being used to making small-talk in English, Cherie's naturally puzzled."
    mike.say "I..."
    mike.say "I just mean it's weird being here...without Dwayne, you know?"
    mike.say "And sure, we've spent a lot of time together - but that's been at work!"
    "Cherie cocks her head on one side as she begins to lead me deeper into the house."
    "And she doesn't even have to beckon for me to follow her as she goes either."
    "I just find myself instinctively trailing after her."
    "As if I'm hanging on her every word, desperate to hear what she has to say."
    show cherie talkative
    cherie.say "Oh come on, [hero.name]..."
    cherie.say "You don't have to play the innocent with me."
    cherie.say "I think that we are way past that now, don't you?"
    show cherie normal
    "Cherie says this as she leads me into a room dominated by a huge fireplace."
    "Logs are heaped in the grate, already blazing and filling the space with light and heat."
    "Two chairs are drawn up close to it, and Cherie motions for me to take one of them."
    "Again I find myself doing as she tells me without a single word being spoken."
    "And then I watch as she goes to a side-table that holds a bottle of wine and two glasses."
    "Without asking if I want to partake, she pours two generous measures."
    "Then she takes the seat across from me, placing one of the glasses into my hand as she does so."
    mike.say "Oh..."
    mike.say "Thank you, Cherie..."
    "Wanting to show that I appreciate her hospitality, I take a sip of the wine."
    "And the second I do so, my eyes almost pop out of their sockets."
    mike.say "WHOA!"
    mike.say "This is amazing..."
    mike.say "I never tasted wine like this before!"
    show cherie smile
    "Cherie's eyes seem to come alive as soon as I say this."
    "Seriously, it's like they're blazing as bright as the fire."
    show cherie happy
    cherie.say "You like it that much?"
    cherie.say "I am so glad to hear you say so."
    show cherie smile
    "By now I'm well into taking my second sip of the wine."
    "So I end up frowning over the lip of the glass as Cherie gushes."
    mike.say "You are?"
    mike.say "I mean, it's that important to you that I like the wine?"
    show cherie closed
    pause 0.3
    show cherie amused
    "Cherie blinks and looks away from me for a moment, clearly amused."
    "Then she does this weird thing where she half smiles and shakes her head."
    "And in that moment I feel like she's casting some kind of spell over me."
    "Because I can never recall finding her so much at ease in my company."
    "Or thinking that she ever looked as beautiful as she does right now."
    show cherie talkative
    cherie.say "Well...no...and yet, also yes."
    cherie.say "You see, this is a wine from the region where I was born."
    cherie.say "I grew up with it and I know it so well that it almost feels a part of me."
    show cherie whining
    cherie.say "Now Dwayne, he could never appreciate it, never come to love it."
    show cherie talkative
    cherie.say "But you..."
    show cherie sadsmile
    "By now Cherie's looking me straight in the eye."
    "And as her words trail off, I feel her gazing deeper still."
    "Almost like she's looking straight into my soul!"
    mike.say "It's...it's very nice wine, Cherie!"
    "I hear myself blurting out the words, like a total clod."
    "And I could almost kick myself as it seems to break the spell."
    "Suddenly Cherie looks away, and everything returns to normal."
    show cherie happy
    cherie.say "Let us just say that I am happy you like the wine, {i}mon ami{/i}."
    cherie.say "Because I want to make it clear to you how much I appreciate all that you have done for me."
    cherie.say "All the times that you have stood at my side and helped me to weather the storms of misfortune."
    show cherie normal
    "Oh man, this wine must be way stronger than I thought."
    "Because I swear that I can feel my head starting to spin."
    "Or maybe that's more to do with the way Cherie's talking to me right now."
    mike.say "It was the least that I could do, Cherie..."
    mike.say "After Dwayne passed, I couldn't leave you to face it all on your own."
    show cherie sad
    "At the mention of her husband's name, Cherie seems to come over a little melancholic."
    "She casts her gaze around the room, as if oppressed by it's sheer size and scale."
    show cherie whining
    cherie.say "Oh, {i}mon ami{/i}..."
    cherie.say "This house was made for him like his tailor made his clothes."
    cherie.say "It is gigantic, and in some ways, even vulgar in it's decor."
    cherie.say "And it makes no sense without him thundering around inside of it."
    show cherie sadsmile
    "I'm nodding as Cherie says all of this, doing the best I can to sympathise."
    "But then I watch her free hand slide downwards, travelling below her waist."
    "It follows the curve of her thigh and then the angle of her knee."
    "Until finally it rounds her calf and arrives just below the ankle."
    "Cherie's fingers deftly pull off her elegant heels, revealing her bare feet."
    "And then I watch as she massages them, seeming to work out the weariness of her tired muscles."
    mike.say "Ah..."
    mike.say "You mean..."
    mike.say "You mean that you're lonely?"
    mike.say "That you miss having Dwayne around the place?"
    "Cherie gives me a shrug and a slight shake of the head."
    show cherie whining
    cherie.say "The former, maybe..."
    show cherie talkative
    cherie.say "The latter, definitely not!"
    cherie.say "It is strange, {i}mon ami{/i}..."
    cherie.say "I always thought that the guilt would be worse than the loneliness."
    cherie.say "But it seems that the opposite is true!"
    show cherie sadsmile
    "I want to say something that will make Cherie feel better."
    "But the problem is that she's just so darn sophisticated."
    "Just being in her presence is making me feel like a total clod!"
    mike.say "But you're not alone, Cherie..."
    mike.say "You have your daughter, and..."
    show cherie normal
    "As soon as I hint at someone else Cherie can call upon, she looks me straight in the eye."
    show cherie talkative
    cherie.say "Go on, {i}mon ami{/i}..."
    cherie.say "I have my daughter and you were about to name another whom I can call upon?"
    show cherie normal
    mike.say "Well..."
    mike.say "I guess, for what it's worth..."
    mike.say "You have me?"
    "I'm fully expecting Cherie to laugh and brush what I just said aside."
    show cherie a at center, traveling(1.75, 0.5, (640, 1200))
    "So it comes as a genuine surprise when she reaches out and takes my hand instead."
    "And now she's doing that thing again, where she seems to be looking into my soul!"
    show cherie a happy blush
    cherie.say "Oh, [hero.name]..."
    cherie.say "If you could only know how I have longed to hear you say that..."
    cherie.say "To admit the bond that has grown between us through all of this!"
    show cherie a normal
    "Okay, okay...even I can tell that this is one of those intense moments."
    "When one person is opening up to another completely."
    "So I have to be totally sure about what I choose to do next!"
    menu:
        "Offer warmth and comfort to Cherie":
            "I feel like my body is switching over to autopilot."
            "Because I can't stop myself putting down my wine-glass."
            "And then I lean forwards, reaching out with my free hand."
            "But it's not like I'm alone in doing so, not at all."
            show cherie a flirt -blush
            "At the same moment, Cherie's other hand is reaching out too."
            "And soon enough, our hands are entwined together."
            mike.say "Cherie..."
            mike.say "I feel like all of that is true..."
            mike.say "But I always wanted to offer you more than that, you know?"
            mike.say "To be able to be more than just a colleague."
            mike.say "And...more than a friend too!"
            "I know I already said there's been a light in Cherie's eyes tonight."
            "But now I swear that it's burning far brighter than the fire itself."
            "She's nodding her head too, eagerly and without a care for being discreet."
            show cherie a happy blush
            cherie.say "Do you think I have not felt the same way about you, {i}mon ami{/i}?"
            cherie.say "I have seen the weight that your shoulders have borne through all of this."
            cherie.say "I have watched as you struggled against the slings and arrows of outrageous fortune."
            cherie.say "How many times I have longed to comfort you, to hold you close to me!"
            show cherie a flirt -blush
            "We seem to have been getting closer together the whole time we've been talking."
            "Closing the short distance as we admit the depth of our feeling for each other."
            "And I'm not entirely sure which one of us it is that makes the first move."
            hide cherie
            show cherie kiss casual
            with fade
            "But mere seconds later, I feel Cherie's lips pressed against mine."
            "And just like that, we're doing it, kissing like impassioned teenagers."
            "At first it's intense and like an unstoppable release of pressure."
            "Part of me feeling like we're going to end up doing it in mere moments."
            "Like I'm gonna do Cherie in front of the fireplace."
            "But then the pace slows, and the crazy sensation seems to pass."
            "Instead the kiss turns into a long, lingering affair."
            "And it's all the more poignant and powerful for it too."
            hide cherie
            show cherie flirt a at center, zoomAt(1.75, (640, 1200))
            with fade
            "When it finally ends, Cherie doesn't pull away from me either."
            "Instead she remains holding my hands and looking into my eyes."
            cherie.say "Mmm..."
            show cherie a happy blush
            cherie.say "Now we are finally being honest with each other, {i}mon ami{/i}."
            cherie.say "Supporting each other in the best way that we possibly can."
            show cherie a normal
            "And I'd say something of the same sort in return, if I were capable."
            "But my heart is still pounding in my chest and my brains are scrambled."
            "So the best I can manage is to nod my head as I gasp and for breath."
            $ cherie.love += 5
        "Gently flirt with Cherie":
            "I can't help smiling as I twine my fingers with Cherie's own."
            "By now we've both had more than a little wine."
            "And I can almost feel the edges of my vision getting blurry."
            mike.say "I'm glad you finally came out and said it, Cherie..."
            mike.say "Because I've been trying to hide my feelings for you all this time."
            mike.say "And I don't know how much longer I could have kept it up."
            show cherie amused
            "I watch as Cherie's eyebrows rise and she looks genuinely amused."
            show cherie happy
            cherie.say "Oh, {i}mon ami{/i}..."
            cherie.say "When you put it like that, you make me wish I had held back a little longer."
            cherie.say "Just enough time for you to finally reach your limit and explode with desire for me."
            cherie.say "Then who knows what heights of passion you would have been driven to!"
            show cherie amused
            "I'm chucking and smiling right back at Cherie as she says all of this."
            "But at the same time I'm beginning to feel genuinely turned-on."
            "Because from the way she's talking, I could believe that's what she wanted to happen."
            "And the feeling is so intense that it takes me a while to notice what her foot is doing."
            mike.say "What the..."
            "Looking down, I see that Cherie's using it to stroke the inside of my leg."
            "And there's no way I can misread the signal that's supposed to be sending!"
            mike.say "Keep that up and things might still go that way!"
            "Cherie and I seem to have crossed a line now."
            "We're definitely never going to be able to go back to the way things were before."
            "Part of me feeling like we'll end up doing it in mere moments."
            "Like I'm gonna do Cherie in front of the fireplace."
            "But then the mood subtly changes, and the crazy sensation seems to pass."
            "As if she's underlining the point, Cherie leans back in her chair."
            "Yet she keeps her eyes on me as she does so."
            "And I can see the barely restrained hunger in her gaze."
            "All of which makes me think it won't be long before we give in to our mutual desires."
            $ cherie.love += 2
            $ cherie.sub -= 2
        "Offer Cherie support, but maintains boundaries":
            "I make a point of gentle squeezing Cherie's hand."
            "But then I place it back on her knee and pull back a little."
            mike.say "I feel the same way too, Cherie."
            mike.say "We've worked so closely with each other through all of this."
            mike.say "How could we have helped becoming allies and friends."
            "Cherie's nodding as I say all of this."
            show cherie stuned
            "But then she seems surprised when I don't say any more."
            show cherie whining blush
            cherie.say "Have you nothing more to say to me, {i}mon ami{/i}?"
            cherie.say "Are we no more than mere colleagues and casual friends?"
            show cherie sadsmile
            "I put on what I hope is an indulgent and sympathetic face."
            "And I hope that my answer will be good enough to satisfy Cherie."
            mike.say "I'm going to be honest with you, Cherie..."
            mike.say "I feel like there's a spark between us."
            mike.say "Like there's the potential for us to be a lot more."
            "Just as I was expecting, I see the light of hope in Cherie's eyes."
            "But I make a point of cutting her off before she can say respond."
            mike.say "But you're a woman that's just been widowed."
            mike.say "We're also in the middle of dealing with the mess of what happened to Dwayne."
            mike.say "All of which means you're vulnerable on so many different levels right now."
            "I pause to let all of that sink in before saying more."
            mike.say "If something is going to happen between us, Cherie..."
            mike.say "If we're going to become more than friends..."
            mike.say "Then I want it to happen when you're not under that kind of pressure."
            mike.say "Because I couldn't forgive myself if it didn't happen for the right reasons."
            show cherie normal
            "Cherie's still looking at me by the time I finish my little speech."
            "And I think that she still has that same desire for me in her eyes too."
            "Yet now there's something else in there too."
            "And this might sound like an ego-trip on my part."
            "But I think it's a newfound level of respect!"
            show cherie happy
            cherie.say "You know that there are few men who would have done that, {i}mon ami{/i}?"
            cherie.say "That would have restrained their desires for the sake of a woman's dignity?"
            cherie.say "And that makes me all the more certain I am right to trust you."
            $ cherie.love += 2
            $ cherie.sub += 2
    scene bg mansionentrance with fade
    "By the time Cherie lets me out of the front door and I start to walk home, the wine is really starting to kick in."
    "And the stuff is so strong that I could honestly believe everything that went before was a dream."
    "But the one thing that makes me sure it was real is the genuine way I can feel my heart swelling in my chest."
    "Swelling from the affection that I'm already feeling for Cherie."
    $ cherie.flags.nokiss = False
    $ cherie.flags.nodate = False
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    return


label cherie_event_07_1:
    if cherie.love.max < 140:
        $ cherie.love.max = 140
    scene bg black
    show expression f"bg {game.room}" at dark, center, zoomAt(1, (640, 720))
    "It's at times like this that my life feels like spinning plates, you know?"
    "There are so many things in motion at the same time, all of them demanding my attention."
    "And if I spend too much time on one of them, the others are all going to come crashing down."
    "So the only thing that I can possibly do is keep trying to stay ahead of events."
    scene bg ceo at dark, center, zoomAt(1, (640, 720)) with fade
    "To try and see potential issues and deal with them before they become actual problems."
    "Which is why I've just sent a text message to Cherie, asking her to step into my office."
    play sound door_knock_light
    "And when there's a discreet knock at the door, I get up and hurry over to open it."
    cherie.say "[hero.name]…"
    play sound door_knock_light
    cherie.say "I came as soon as I could."
    play sound door_open
    pause 0.5
    show cherie a work at center, zoomAt(1, (340, 750)) with easeinleft
    "I nod as I open the door to allow Cherie to step into my office."
    "And then I close it behind her, making sure it's secure."
    "Only then do I gesture for her to join me at my desk and begin to answer."
    show cherie at center, traveling(1.4, 1, (640, 950))
    pause 1
    show cherie at center, zoomAt(1.4, (640, 950))
    mike.say "Thanks, Cherie..."
    mike.say "Obviously I couldn't say what this is about in a text message."
    mike.say "We can't be sure that someone isn't snooping around in there."
    show cherie at startle(0.5, 10)
    "Cherie nods, letting me know that we're both on the same page."
    show cherie talkative
    cherie.say "Of course, {i}mon ami{/i}…"
    cherie.say "But then this is something serious?"
    cherie.say "Something that we must discuss with all haste?"
    show cherie normal
    "I'm sitting down at my desk as Cherie answers the question."
    "And I pause before answering to gesture to the pot of steaming coffee that's within reach."
    "The view out of the windows is already pitch black, as we're meeting late into the night."
    "And it comes as no surprise to me that Cherie nods again, even before I've said another word."
    "It's no secret that the both of us are exhausted by the whole affair of covering up Dwayne's death."
    "So I go ahead and pour two cups of coffee, hoping that the injection of caffeine will perk us up."
    mike.say "I'm afraid that I've heard something pretty worrying about Aletta."
    mike.say "Something that could be serious enough to change everything ."
    "Cherie scoops up her coffee cup as I begin to explain myself in earnest."
    show cherie closed with dissolve
    "I watch as she listens to, closing her eyes while taking a long sip of her coffee."
    "Even when she's done that, Cherie still keeps her eyes closed for a few seconds."
    "And I can almost sense her doing all she can to gather the reserves of her strength."
    show cherie c talkative
    cherie.say "Hmm..."
    cherie.say "I would like to say that I am surprised, {i}mon ami{/i}…"
    show cherie upset
    cherie.say "But the truth is that I always suspected Aletta might prove to be the weak link."
    cherie.say "So, tell me more - what have you heard?"
    show cherie closed with dissolve
    "I nod, taking a long sip of my own coffee."
    "And then I launch into my explanation."
    mike.say "Long story short..."
    mike.say "I've heard that the police are leaning on Aletta."
    mike.say "That they're trying to pressure her into testifying at the inquest into Dwayne's death."
    show cherie b stuned at startle(0.1, -5)
    "Cherie shakes her head and rubs her temples with the index-fingers of both hands."
    show cherie upset
    cherie.say "This is not good, {i}mon ami{/i}…"
    cherie.say "She is too close to the truth of the matter."
    cherie.say "And I fear that if she is put in the witness stand, then she will crack under the pressure!"
    show cherie c annoyed
    mike.say "My thoughts exactly."
    mike.say "And the worst thing is that I don't think there's any way we can stop it happening."
    mike.say "Well...unless I were to bump Aletta off!"
    show cherie stuned with dissolve
    "Cherie's eyes go wide as she hears me suggest killing Aletta."
    "And the mouthful of coffee she just took spurts out from between her pursed lips."
    show cherie b surprised at startle
    cherie.say "Bleurgh!"
    cherie.say "You...you cannot be serious, {i}mon ami{/i}!"
    cherie.say "How would you even go about doing such a thing?!?"
    show cherie stuned
    "I don't know what's more surprising out of the two things I just saw."
    "Either the normally dignified Cherie, spitting out coffee."
    "Or her actually asking me if I'd seriously consider killing Aletta!"
    mike.say "Cherie..."
    mike.say "I was just kidding!"
    mike.say "You know, trying to lighten the mood?"
    show cherie a annoyed
    "Cherie looks equal parts shocked and relieved as I put her right on the matter."
    "But as soon as she seems to recover some of her poise, she looks down at her blouse."
    "Needless to say, the one she has on right now looks both elegant and expensive in nature."
    "But the fact coffee's dribbled down the front of it does kind of spoil the effect."
    show cherie talkative
    cherie.say "That is a relief to hear, {i}mon ami{/i}."
    show cherie whining
    cherie.say "But look at the state of me now!"
    show cherie sad
    menu:
        "Offer tissues to clean herself up":
            "I reach down and open one of the drawers in my desk."
            "And then I pull out a box of paper tissues that I offer to Cherie."
            mike.say "Sorry about that, Cherie..."
            mike.say "Use these to clean yourself up."
            "Cherie nods and takes the box from me."
            "But as she plucks out a couple of tissues and begins to dab her blouse, I see she's grinning."
            show cherie happy
            cherie.say "So, {i}mon ami{/i}…"
            cherie.say "You always have tissues to hand?"
            show cherie amused
            mike.say "Erm..."
            mike.say "Yeah, Cherie..."
            mike.say "You never know when you might need one."
            show cherie smile
            "The smile on Cherie's face is positively wicked by now."
            show cherie wink
            "And she gives me a knowing wink."
            show cherie happy
            cherie.say "For those private moments in the office, no?"
            cherie.say "When a hard-working man needs some relief?"
            show cherie amused
            "I feel my cheeks beginning to flush as I realise what she's implying."
            mike.say "What?!?"
            mike.say "No, no, no..."
            mike.say "That's not what I use them for at all!"
            $ cherie.sub -=1
            $ cherie.love -=2
        "Offer Cherie my jacket to cover her blouse":
            "Acting on instinct, I stand up and take off my jacket."
            show bg ceo at dark, center, zoomAt(1, (640, 720))
            show cherie at center, zoomAt(1.4, (640, 950))
            pause 0.3
            show bg ceo at dark, center, traveling(1.2, 1, (640, 820))
            show cherie at center, traveling(2.2, 1, (640, 1400))
            "And then I offer it to Cherie, who nods happily."
            show cherie happy
            cherie.say "Oh, {i}mon ami{/i}…"
            cherie.say "You would really give me your jacket?"
            cherie.say "What a perfect gentleman you are!"
            show cherie smile
            "I shrug and wave a hand dismissively in the air as Cherie slips the jacket on."
            "But at the same time I make sure not to totally dismiss the praise she's heaping onto me."
            "Because the truth is that it feels pretty good to be able to impress such a sophisticated woman."
            mike.say "Anything for you, Cherie..."
            mike.say "Anything at all."
            $ cherie.sub += 1
            $ cherie.love +=2
    show cherie closed at startle(0.2, 5)
    "Just as I was feeling like the mood had lightened a little, Cherie lets out a weary sigh."
    "And that's all it takes to bring us right back to where we were when we started the conversation."
    show cherie whining
    cherie.say "Ah..."
    cherie.say "So the question is, what are we going to do about Aletta?"
    show cherie sad
    mike.say "The only thing we can do is make sure that we're on the same page."
    mike.say "We need to be sure that, whatever Aletta says in court, we're telling the same story."
    show cherie b closed at startle(0.1, -5)
    "Cherie nods, but I can see that she's rubbing her temples again."
    "As if the weariness is really starting to get to her."
    show cherie whining
    cherie.say "And just what would that be?"
    cherie.say "It's been so long since we last went over it."
    cherie.say "I feel the need for you to remind me."
    show cherie sad
    mike.say "Okay, Cherie..."
    mike.say "This is how it goes..."
    if hero.knowledge >= 85 or hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "First, we should stick to the same version."
        "I hope the rivalry between Aletta and Cherie won't be a problem."
        "Secondly, confessing to a crime, even in cases of self-defense, is a good way to attract the attention of the police."
        hide black with dissolve
    menu:
        "'Stick to the truth'":
























































            mike.say "We stick to the absolute truth of what happened."
            mike.say "Dwayne walked in on us and started to attack me."
            mike.say "He was dead set on killing me, until Aletta shot him."
            mike.say "And the only reason she did that was to defend me."
            "Cherie listens to what I have to say."
            "But I can see that she doesn't look convinced."
            show cherie b surprised
            cherie.say "But what if Aletta says something different?"
            cherie.say "What if she says we always planned to kill Dwayne?"
            show cherie a stuned
            mike.say "She can say whatever she likes, and it won't matter."
            mike.say "Because this way we'll have the physical evidence backing us up."
            $ cherie.flags.dwaynedeath_truth = True
        "'Claim Aletta killed Dwayne because of their affair'":
            mike.say "If Aletta's going to betray us, then we do the same to her."
            mike.say "We make everyone aware that the two of them were having an affair."
            mike.say "And we hammer home that he was being an abusive prick too."
            mike.say "Then we say that Aletta killed Dwayne to escape his clutches."
            "Cherie listens to what I have to say."
            "But I can see that she doesn't look convinced."
            show cherie b surprised
            cherie.say "But that's not the truth."
            show cherie a stuned
            mike.say "It's true that they were having an affair."
            mike.say "And her prints are all over the murder weapon."
            $ cherie.flags.dwaynedeath_partialtruth = True
        "'Claim Dwayne was supposed to go to New York and we don't know what happens'":













            mike.say "We stick to the story that Dwayne went off to New York and we don't know what happens then."
            mike.say "Maybe throw in a little background detail about him wanting to start a new life."
            "Cherie listens to what I have to say."
            "But I can see that she doesn't look convinced."
            show cherie b surprised
            cherie.say "But Aletta will tell them that I killed him!"
            cherie.say "Won't they be more likely to believe that?"
            show cherie a stuned
            mike.say "Aletta wouln't take that risk since she is the actual murderer."
            $ cherie.flags.dwaynedeath_dwaynegone = True
        "'Claim you killed Dwayne in the kitchen with a knife'":
            mike.say "We tell them that you killed Dwayne with a knife."
            mike.say "And we say that you did it in the kitchen."
            mike.say "Oh, and it was self-defence."
            "Cherie listens to what I have to say."
            "But I can see that she doesn't look convinced."
            show cherie b surprised
            cherie.say "But that's not the truth."
            cherie.say "Aletta shot Dwayne with the gun, remember?"
            show cherie a stuned
            mike.say "They can't prove that, Cherie, because they don't have the body."
            mike.say "And self-defence is more believable with a knife than a gun."
            $ cherie.flags.dwaynedeath_cherieknife = True
        "'I will claim to have shot Dwayne in self-defence'":
            mike.say "We tell them that it was me, Cherie..."
            mike.say "We say that Dwayne attacked me and I shot him in self-defence."
            mike.say "That way you're off the hook, no matter which way things go."
            "Cherie listens to what I have to say."
            "But I can see that she doesn't look convinced."
            show cherie b surprised
            cherie.say "But that's not the truth."
            cherie.say "And I can't let you take the blame for Aletta!"
            show cherie a stuned
            mike.say "You're not letting me do it..."
            mike.say "I'm choosing to do it myself."
            $ cherie.flags.dwaynedeath_mikeselfdefense = True
    show cherie c closed
    "Once I'm done explaining the plan, Cherie goes quiet."
    "And I can see that she's pondering every aspect of it."
    "But then she nods her head, a look of finality settling upon her face."
    show cherie a talkative
    cherie.say "Very well, {i}mon ami{/i}…"
    cherie.say "We will do as you say."
    cherie.say "I just hope that your plan is the right one."
    show cherie sadsmile
    mike.say "Me too, Cherie, me too!"
    $ cherie.love += 6
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    return

label cherie_event_07_2:
    if cherie.love.max < 140:
        $ cherie.love.max = 140
    "I've been preparing myself for the chance to meet with Aletta for what feels like forever by now."
    show aletta normal at center, zoomAt(1, (340, 720)) with easeinleft
    "And so when she walks in and looks me straight in the eye, I'm more than ready to launch into it."
    show aletta normal at center, traveling(1.5, 1.0, (640, 1040))
    "Which is why I'm caught off-guard when she's the one that immediately starts talking."
    show aletta talkative
    aletta.say "I'm glad that we got the chance to talk, [hero.name]…"
    aletta.say "Because I think it's vital that we get our stories straight."
    aletta.say "The police are going to want to interview us, of course..."
    aletta.say "And so we need to be on the same page when that happens."
    show aletta normal
    "It's been a while since I was in a position where Aletta was the one taking the lead."
    "And so I'd kind of forgotten just how forceful she's capable of being."
    "But recent events have forced me to be strong, and I'm more than capable of meeting her head-on."
    mike.say "My thoughts exactly, Aletta..."
    mike.say "And you'll be relieved to know that I've given it a great deal of thought."
    mike.say "So much thought, in fact, that I know exactly what we're going to tell them."
    "As soon as I announce that I've got a plan, hope seems to flare in Aletta's eyes."
    "But then her usual, business-like demeanour asserts itself, and she just nods."
    "Like she's relieved that I'm going to tell her my plan, but afraid of showing weakness."
    show aletta talkative
    aletta.say "Come on then..."
    aletta.say "Let's hear it."
    show aletta normal
    "Trying my best not to get annoyed with Aletta's pushiness, I nod my head."
    "And then I launch into the explanation I've practiced in earnest."
    "Hoping that it's enough to convince her to toe the line on this one."
    if hero.knowledge >= 85 or hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "First, we should stick to the same version."
        "I hope the rivalry between Aletta and Cherie won't be a problem."
        "Secondly, confessing to a crime, even in cases of self-defense, is a good way to attract the attention of the police."
        hide black with dissolve
    menu:
        "'Stick to the truth'":
            mike.say "No matter what happens, you have to stick to the truth, okay?"
            mike.say "And I really mean that, Aletta..."
            mike.say "The absolute truth of what went down that night."
            mike.say "Dwayne attacked Cherie and me, tried his darndest to kill us both."
            mike.say "Then you shot him in self-defence, after all the shit he put you through."
            show aletta embarrassed
            "I can already see that Aletta's frowning as she listens to what I have to say."
            "Like she's taking it all in, but the information isn't sitting well with her."
            "And so I'm not surprised when she begins questioning me as soon as I'm done."
            show aletta whining
            aletta.say "But that still means me admitting that I killed him!"
            aletta.say "[hero.name], even if they accept that it was self-defence..."
            aletta.say "They'll still send me to jail for it!"
            show aletta sad
            "I shake my head, doing the best I can to calm Aletta down."
            mike.say "I don't think they will, not after they see pictures of Dwayne."
            mike.say "For god's sake, Aletta, the guy looked like that bloody wrestler!"
            mike.say "You know, the one that became an actor?"
            mike.say "Most of the jury will think they'd need a fucking bazooka to take him out!"
            show aletta whining
            aletta.say "You think they'll let me off?"
            show aletta annoyed
            "I nod my head, trying to convince Aletta that I'm right."
            mike.say "I'd stake my life on it."
            mike.say "So just stick to the truth, okay?"
            $ aletta.flags.dwaynedeath_truth = True
        "'Claim you killed Dwayne because of your affair'":
            mike.say "Okay, Aletta..."
            mike.say "We tell them that you shot Dwayne in self-defence, yeah?"
            mike.say "That he'd been manipulating you for bloody ages..."
            mike.say "Blackmailing you into sleeping with him, and stuff like that."
            show aletta embarrassed
            "I can already see that Aletta's frowning as she listens to what I have to say."
            "Like she's taking it all in, but the information isn't sitting well with her."
            "And so I'm not surprised when she begins questioning me as soon as I'm done."
            show aletta whining
            aletta.say "But what about the fight that he had with you, [hero.name]?"
            aletta.say "And the argument he was having with Cherie over that ledger from the safe?"
            aletta.say "What if they start asking me about all of that?"
            show aletta sad
            "I shake my head, doing all I can to silence Aletta's fears."
            "Trying to steer her back down the path that I want her to take."
            mike.say "They don't know anything about any of that."
            mike.say "All they have to go on is the physical evidence at the scene."
            mike.say "So we need to stick to that and nothing else."
            show aletta whining
            aletta.say "But that still means me admitting that I killed him!"
            aletta.say "[hero.name], even if they accept that it was self-defence..."
            aletta.say "They'll still send me to jail for it!"
            show aletta sad
            "I shake my head, doing the best I can to calm Aletta down."
            mike.say "I don't think they will, not after they see pictures of Dwayne."
            mike.say "For god's sake, Aletta, the guy looked like that bloody wrestler!"
            mike.say "You know, the one that became an actor?"
            mike.say "Most of the jury will think they'd need a fucking bazooka to take him out!"
            show aletta whining
            aletta.say "You think they'll let me off?"
            show aletta annoyed
            "I nod my head, trying to convince Aletta that I'm right."
            mike.say "I'd stake my life on it."
            $ aletta.flags.dwaynedeath_partialtruth = True
        "'Deny everything, your were never there'":
            mike.say "As far as they're concerned, you were never even there."
            mike.say "So whatever they ask you, deny it all and stick to that."
            mike.say "The only people there were Cherie, Dwayne and me."
            show aletta embarrassed
            "I can already see that Aletta's frowning as she listens to what I have to say."
            "Like she's taking it all in, but the information isn't sitting well with her."
            "And so I'm not surprised when she begins questioning me as soon as I'm done."
            show aletta talkative
            aletta.say "But what about the affair I had with him?"
            show aletta whining
            aletta.say "Dwayne forced me to do so many...awful things."
            show aletta angry
            aletta.say "They're certain to bring that up and press me on it."
            show aletta upset
            "I shake my head, doing all I can to silence Aletta's fears."
            "Trying to steer her back down the path that I want her to take."
            mike.say "They probably will do all of that, and more."
            mike.say "But there's no way they can link any of it to Dwayne's death."
            mike.say "Hell, Aletta, there's not even any evidence you were there that night."
            mike.say "So just answer all of their other questions honestly."
            mike.say "That way they'll have to drop it eventually."
            show aletta talkative
            aletta.say "You think that'll work?"
            show aletta normal
            "I nod my head, trying to convince Aletta that I'm right."
            mike.say "I'd stake my life on it."
            $ aletta.flags.dwaynedeath_dwaynegone = True
        "'Claim Cherie killed Dwayne in the kitchen with a knife'":
            mike.say "Okay, Aletta..."
            mike.say "The story is that Cherie was the one that killed Dwayne."
            mike.say "She stabbed him in the kitchen, and you had nothing to do with it."
            mike.say "You were just an innocent bystander."
            show aletta embarrassed
            "I can already see that Aletta's frowning as she listens to what I have to say."
            "Like she's taking it all in, but the information isn't sitting well with her."
            "And so I'm not surprised when she begins questioning me as soon as I'm done."
            show aletta surprised
            aletta.say "Cherie?"
            aletta.say "In the kitchen?"
            aletta.say "With the knife?"
            show aletta whining
            aletta.say "Oh god, it sounds like that boardgame where you have to guess who the killer is!"
            show aletta sad
            "I shake my head, doing all I can to silence Aletta's fears."
            "Trying to steer her back down the path that I want her to take."
            mike.say "Just try to focus, okay?"
            mike.say "We've gotten rid of the body and the gun."
            mike.say "There's nothing to link you to Dwayne's death."
            show aletta whining
            aletta.say "But what about the affair I had with him?"
            aletta.say "Dwayne forced me to do so many...awful things."
            show aletta angry
            aletta.say "They're certain to bring that up and press me on it."
            show aletta upset
            "I shake my head, doing all I can to silence Aletta's fears."
            "Trying to steer her back down the path that I want her to take."
            mike.say "They probably will do all of that, and more."
            mike.say "But there's no way they can link any of it to Dwayne's death."
            mike.say "Hell, Aletta, there's not even any evidence you touched a damn thing that night."
            mike.say "So just answer all of their other questions in line with the story we've agreed."
            mike.say "That way they'll have to drop it eventually."
            show aletta talkative
            aletta.say "You think that'll work?"
            show aletta normal
            "I nod my head, trying to convince Aletta that I'm right."
            mike.say "I'd stake my life on it."
            $ aletta.flags.dwaynedeath_cherieknife = True
        "'I will claim to have shot Dwayne in self-defence'":
            mike.say "Okay, Aletta..."
            mike.say "The story is that I was the one that killed Dwayne."
            mike.say "I shot him in the kitchen, and you had nothing to do with it."
            mike.say "You were just an innocent bystander."
            show aletta embarrassed
            "I can already see that Aletta's frowning as she listens to what I have to say."
            "Like she's taking it all in, but the information isn't sitting well with her."
            "And so I'm not surprised when she begins questioning me as soon as I'm done."
            show aletta surprised
            aletta.say "[hero.name]?"
            aletta.say "In the kitchen?"
            aletta.say "With the pistol?"
            show aletta whining
            aletta.say "Oh god, it sounds like that boardgame where you have to guess who the killer is!"
            show aletta sad
            "I shake my head, doing all I can to silence Aletta's fears."
            "Trying to steer her back down the path that I want her to take."
            mike.say "Just try to focus, okay?"
            mike.say "We've gotten rid of the body and the gun."
            mike.say "There's nothing to link you to Dwayne's death."
            show aletta whining
            aletta.say "But what about the affair I had with him?"
            aletta.say "Dwayne forced me to do so many...awful things."
            show aletta angry
            aletta.say "They're certain to bring that up and press me on it."
            show aletta upset
            "I shake my head, doing all I can to silence Aletta's fears."
            "Trying to steer her back down the path that I want her to take."
            mike.say "They probably will do all of that, and more."
            mike.say "But there's no way they can link any of it to Dwayne's death."
            mike.say "Hell, Aletta, there's not even any evidence you touched a damn thing that night."
            mike.say "So just answer all of their other questions in line with the story we've agreed."
            mike.say "That way they'll have to drop it eventually."
            show aletta talkative
            aletta.say "You think that'll work?"
            show aletta normal
            "I nod my head, trying to convince Aletta that I'm right."
            mike.say "I'd stake my life on it."
            $ aletta.flags.dwaynedeath_mikeselfdefense = True
    show aletta annoyed
    "I can see that Aletta's still not totally convinced that all of this is going to work."
    "But she must realise that it's the best hope she's got of keeping her arse out of jail."
    "Because she puts on a brave face and nods."
    show aletta talkative
    aletta.say "Got it, [hero.name]…"
    aletta.say "I'll do my best, I promise."
    show aletta normal
    mike.say "I know you will, Aletta..."
    mike.say "And don't worry about a thing."
    mike.say "We'll get through this, because we deserve to."
    mike.say "The only one that got his just desserts in all of this was Dwayne himself!"
    $ aletta.love += 4
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 2)
    scene bg black with dissolve
    return


label cherie_event_08_1:
    if cherie.love.max < 160:
        $ cherie.love.max = 160
    scene expression "bg [game.room]"
    with fade
    play sound door_knock
    "There's a knock at the door, and I look up from what I'm doing with a frown on my face."
    "Because I'm not expecting anyone to be calling around today, or anything being delivered."
    "But then I think that maybe it's one or the other of those things for one of my housemates."
    "So I decide to just ignore it and go back to what I was doing, to pretend I didn't hear."
    "The only problem with that is the person on the other side of the door doesn't take the hint."
    play sound door_banging
    "And within a short space of time they're at it again, hammering harder now."
    "Which means that the noise is stopping me from being able to concentrate."
    "So I have no choice but to get up and walk to the door, grumbling every step of the way."
    "And I keep on grumbling until the very moment that I open the door."
    scene bg house
    show inspector
    with fade
    "Because that's when I'm greeted with a very shiny and very official-looking badge being waved in my face."
    if "cherie_event_08_2" in DONE:
        "Michaels" "Hello again Mister [hero.family_name]."
        "The unkempt hair, the grubby raincoat and the general dishevelled appearance."
        "How could I fail to recognise the inimitable Detective Michaels?"
        mike.say "Oh..."
        mike.say "Detective Michaels..."
    else:
        "Michaels" "Erm..."
        "Michaels" "Would you...erm...happen to be..."
        "Michaels" "Mister [hero.family_name]?"
        "Michaels" "Mister [hero.name] [hero.family_name]?"
        "The unkempt hair, the grubby raincoat and the general dishevelled appearance."
        "How could I fail to recognise the inimitable Detective Michaels?"
        mike.say "Oh..."
        mike.say "Detective Michaels..."
        mike.say "Yeah, that's me."
        "The detective squints at me as he realises that I just called him by name."
        "Michaels" "Excuse me..."
        "Michaels" "But have we met before?"
        "Michaels" "Because I pride myself on never forgetting a face."
        "Michaels" "But yours...well, let's just say it's not ringing any bells!"
        mike.say "Well, yeah..."
        mike.say "We met that one time, you remember?"
        mike.say "At the police station?"
        "Michaels" "Oh, so you're a career criminal then!"
        "I wave my hands in the air, trying to dismiss the accusation."
        mike.say "No, no, no..."
        mike.say "We just met once before, that's all!"
        "Michaels" "Anyway..."
    "Michaels" "I just had a few questions to ask you, if you don't mind?"
    "Michaels" "You know, about the untimely and very suspicious death of one Mister Dwayne Jackson?"
    "The moment that the detective mentions Dwayne's name, everything falls into place."
    "Of course, he's here to question me about what happened to Dwayne!"
    mike.say "Oh fuck..."
    mike.say "I...I mean of course!"
    mike.say "Do you want to come in?"
    "Michaels shrugs and shakes his head."
    "Michaels" "Well, most people seem to like doing it that way."
    "Michaels" "Me, I don't mind asking my questions out here on your doorstep."
    "Michaels" "But some folks would rather their neighbours didn't overhear, you know?"
    "I start nodding as I open the door and usher the dishevelled detective inside."
    "And as soon as he's shuffled his way into the hallway, I close the door and lock it behind him."
    "When I turn around, I see that he's already started to walk further into the house."
    scene bg kitchen
    show inspector at center, zoomAt(1.15, (640, 780))
    with fade
    "It looks like he's headed for the kitchen, so I hurry after him."
    "And when I catch up, I make a point of scooting around to stand in his path."
    mike.say "So..."
    mike.say "You said that you had some questions about Dwayne's disappearance?"
    show inspector at startle(0.1, -5)
    "Michaels" "Oh yeah, that's right."
    "Michaels" "Now humour me here, okay?"
    "Michaels" "Because I already read all the statements you guys made."
    "Michaels" "But sometimes things get all jumbled up inside of my head."
    "The detective makes a vague circular gesture around his temples."
    "Which I guess is supposed to symbolise his apparent mental confusion."
    show inspector at startle(0.1, -5)
    "Michaels" "What I'd like you to do is..."
    "Michaels" "In your own words and at your own pace..."
    "Michaels" "Explain to me exactly what happened that night at Mister Jackson's residence, okay?"
    "Oh man, here we go."
    "Time for me to spin my tale, and hope the detective buys it."
    if hero.knowledge >= 85 or hero.has_skill("investigator"):
        show black at opacity(0.25) with dissolve
        "First, we should stick to the same version."
        "I hope the rivalry between Aletta and Cherie won't be a problem."
        "Secondly, confessing to a crime, even in cases of self-defense, is a good way to attract the attention of the police."
        hide black with dissolve
    menu:
        "Tell the truth":
            mike.say "Well, the thing is that Cherie and I thought that Dwayne was out of the country."
            show inspector at startle(0.1, -5)
            "Michaels" "That would be Cherie Jackson, the wife of the missing man?"
            mike.say "Uh-uh..."
            mike.say "Like I was saying, we thought he was away on business."
            mike.say "So we took it as a chance to break into his safe."
            "I watch as one of the detective's eyebrows rises at this."
            show inspector at startle(0.1, -5)
            "Michaels" "Erm..."
            "Michaels" "Would you mind explaining exactly why you were doing that?"
            mike.say "Cherie was sure that Dwayne had been cooking the books, you know?"
            mike.say "That there was a ledger of accounts in the safe that would prove it."
            show inspector at startle(0.1, -5)
            "Michaels" "Hmm..."
            "Michaels" "That's a serious offence, right there."
            mike.say "But just as we got our hands on it, Dwayne walked in on us."
            show inspector at startle(0.1, -5)
            "Michaels" "And let me guess - he wasn't pleased?"
            "I can't help frowning as I recount the events that followed."
            "The memories causing me genuine discomfort as I do so."
            mike.say "He attacked Cherie, and I think he would have killed her."
            mike.say "But I intervened and we ended up having one hell of a fight."
            show inspector at startle(0.1, -5)
            "Michaels" "The result of which was...what, exactly?"
            "The question catches me off-guard."
            mike.say "I didn't kill him!"
            mike.say "That was Aletta - she was the one that shot Dwayne."
            show inspector at startle(0.1, -5)
            "Michaels" "Is that so?"
            "I can feel the weight of what I just did pressing down on me."
            "The fact that I just admitted that Aletta's technically guilty of Dwayne's murder."
            mike.say "She didn't do it in cold blood though..."
            mike.say "Dwayne had been manipulating her for a long time."
            mike.say "Exploiting her and making her do the most disgusting things for him."
            mike.say "I...I think she just saw a chance to be free of him and took it."
            show inspector at startle(0.1, -5)
            "Michaels" "And then what?"
            "Michaels" "Mister Jackson's body just turned to dust and blew away?"
            "Michaels" "And the gun your friend Aletta used - where's that?"
            "It's too late for me to turn back now, I'm in too deep."
            "So I grit my teeth and keep on confessing to the detective."
            mike.say "We got rid of them, Cherie and me."
            mike.say "I can tell you where to look for them, if you like?"
            show inspector at startle(0.1, -5)
            "Michaels" "Nah, there's going to be plenty of time for that later."
            "Michaels" "Right now, I need to take you down to the station."
            mike.say "Am I..."
            show inspector at startle(0.1, -5)
            "Michaels" "Under arrest?"
            "Michaels" "Oh most definitely!"
            "Michaels" "You're at the very least under suspicion of conspiring to cover up a murder."
            "Michaels" "As for the rest of your story, we'll have to see what comes out in the wash."
            show inspector at center, traveling(1.5, 1.0, (640, 1000))
            "I nod as the detective puts a hand on my shoulder, leading me towards the door."
            "There's no point in arguing or making a scene, as this is what I expected would happen."
            "Now all I can hope is that things turn out for the best."
            "That none of us, even Aletta, are charged with murder in the first degree."
            $ hero.flags.dwaynedeath_truth = True
        "Aletta killed Dwayne":
            mike.say "The truth is that it was my colleague that did it."
            mike.say "Aletta shot Dwayne and killed him."
            "Up till now the Detective's expression has been pretty calm."
            "And at times I could have believed he was actually falling asleep."
            "But now his eyes pop wide open, and he stares at me in genuine surprise."
            show inspector at startle(0.1, -5)
            "Michaels" "Pardon me..."
            "Michaels" "But did you just say that she murdered the guy?"
            "Michaels" "Because that, right there, is a very serious allegation!"
            "I can't help swallowing audibly from the way my mouth is going dry."
            "I always thought this would be a tough thing to pull off."
            "But it seems like I had no idea just how tough it would be in reality."
            mike.say "Detective, you have to understand..."
            mike.say "She didn't do it in cold blood though..."
            mike.say "Dwayne had been manipulating her for a long time."
            mike.say "Exploiting her and making her do the most disgusting things for him."
            mike.say "I...I think she just saw a chance to be free of him and took it."
            show inspector at startle(0.1, -5)
            "Michaels" "And, erm..."
            "Michaels" "Might I ask where all of this took place?"
            mike.say "Oh, it was at Dwayne's mansion..."
            mike.say "After he'd tried to kill me and his wife."
            "This time the detective raises both of his eyebrows."
            show inspector at startle(0.1, -5)
            "Michaels" "Oh boy..."
            "Michaels" "I think we'd better continue this back at the station."
            mike.say "You mean the police station?!?"
            mike.say "Am I under arrest?"
            "The detective puts a hand on my shoulder, leading me towards the door."
            show inspector at startle(0.1, -5)
            "Michaels" "At the current time you're just helping with our enquiries."
            "Michaels" "But if you want it to stay that way, then I'd suggest you try to be as helpful as possible!"
            $ hero.flags.dwaynedeath_partialtruth = True
        "I was not at Dwayne's house that night":
            mike.say "The truth is that I really can't really help you, Detective."
            show inspector at startle(0.1, -5)
            "Michaels raises one eyebrow as he regards me."
            "Michaels" "Oh really?"
            "Michaels" "And, erm...would you mind explaining to me why that is?"
            "I do the best I can to shrug and look totally nonchalant."
            "While knowing all the time that I'm lying through my teeth to a police detective."
            "And hoping that he's not one of those guys that can spot guilt in a potential suspect."
            mike.say "Well, because I wasn't at Dwayne's place the night he was killed."
            "This time the detective raises both of his eyebrows."
            show inspector at startle(0.1, -5)
            "Michaels" "Exactly when did I say Mister Jackson was murdered in his mansion?"



            "For a moment I feel like I'm actually going to lose control of my bowels."
            "Like I might have an accident of a very personal nature right in front of the detective."
            "But somehow my brain manages to kick in and start to pull me out of the hole I've dug for myself."
            mike.say "Oh, come on, Detective..."
            mike.say "You've got Dwayne's mansion swarming with cops right now."

            mike.say "And I work for his company, which means I've heard all the rumours going."
            mike.say "Dwayne had more than a couple of skeletons in his closet, believe me!"
            "The detective nods at this, though he's still studying me with interest."
            show inspector at startle(0.1, -5)
            "Michaels" "Now that there is some impressive deduction."
            "Michaels" "You should consider a career in law enforcement."
            "I can't tell if he's joking or serious, so I just smile in response."
            show inspector at center, zoomAt(1.15, (940, 780)) with ease
            "And it comes as a genuine relief when the detective turns and starts to walk back towards the door."
            show inspector at startle(0.1, -5)
            "Michaels" "Well, that's all the questions I have for now."
            "Michaels" "Don't go leaving town or anything, yeah?"
            "Michaels" "As we might need to talk to you again."
            hide inspector with easeoutright
            "I nod eagerly as I show him to the door and then close it behind him."
            "And once the detective is gone, I fasten every lock and lean against it."
            "Relieved that my ordeal is over, at least for a short while."
            $ hero.flags.dwaynedeath_dwaynegone = True
        "Cherie killed Dwayne with a knife":
            mike.say "Well, the thing is that Cherie and I thought that Dwayne was out of the country."
            show inspector at startle(0.1, -5)
            "Michaels" "That would be Cherie Jackson, the wife of the missing man?"
            mike.say "Uh-uh..."
            mike.say "Like I was saying, we thought he was away on business."
            mike.say "So we took it as a chance to break into his safe."
            "I watch as one of the detective's eyebrows rises at this."
            show inspector at startle(0.1, -5)
            "Michaels" "Erm..."
            "Michaels" "Would you mind explaining exactly why you were doing that?"
            mike.say "Cherie was sure that Dwayne had been cooking the books, you know?"
            mike.say "That there was a ledger of accounts in the safe that would prove it."
            show inspector at startle(0.1, -5)
            "Michaels" "Hmm..."
            "Michaels" "That's a serious offence, right there."
            mike.say "But just as we got our hands on it, Dwayne walked in on us."
            show inspector at startle(0.1, -5)
            "Michaels" "And let me guess - he wasn't pleased?"
            "I can't help frowning as I recount the events that followed."
            "The memories causing me genuine discomfort as I do so."
            mike.say "He attacked Cherie, and I think he would have killed her."
            mike.say "But I intervened and we ended up having one hell of a fight."
            show inspector at startle(0.1, -5)
            "Michaels" "The result of which was...what, exactly?"
            "The question catches me off-guard."
            mike.say "I didn't kill him!"
            mike.say "That was Cherie - she got hold of a knife and stabbed Dwayne."
            show inspector at startle(0.1, -5)
            "Michaels" "Is that so?"
            "I can feel the weight of what I just did pressing down on me."
            "The fact that I just admitted that Cherie's technically guilty of Dwayne's murder."
            "But then I remind myself that this was the plan we came up with together."
            "To hide the fact that Aletta shot him and to emphasize that it was self-defence."
            mike.say "You have to understand, Detective..."
            mike.say "He was going to kill us both..."
            mike.say "And he nearly did it!"
            show inspector at startle(0.1, -5)
            "Michaels" "And then what?"
            "Michaels" "Mister Jackson's body just turned to dust and blew away?"
            "Michaels" "And the knife his wife used - where's that?"
            "It's too late for me to turn back now, I'm in too deep."
            "So I grit my teeth and keep on confessing to the detective."
            mike.say "We got rid of them, Cherie and me."
            mike.say "I can tell you where to look for them, if you like?"
            show inspector at startle(0.1, -5)
            "Michaels" "Nah, there's going to be plenty of time for that later."
            "Michaels" "Right now, I need to take you down to the station."
            mike.say "Am I..."
            show inspector at startle(0.1, -5)
            "Michaels" "Under arrest?"
            "Michaels" "Oh most definitely!"
            "Michaels" "You're at the very least under suspicion of conspiring to cover up a murder."
            "Michaels" "As for the rest of your story, we'll have to see what comes out in the wash."
            show inspector at center, traveling(1.5, 1.0, (640, 1000))
            "I nod as the detective puts a hand on my shoulder, leading me towards the door."
            "There's no point in arguing or making a scene, as this is what I expected would happen."
            "Now all I can hope is that things turn out for the best."
            "That none of us, even Cherie, are charged with murder in the first degree."
            $ hero.flags.dwaynedeath_cherieknife = True
        "I shot Dwayne":
            mike.say "Well, the thing is that Cherie and I thought that Dwayne was out of the country."
            show inspector at startle(0.1, -5)
            "Michaels" "That would be Cherie Jackson, the wife of the missing man?"
            mike.say "Uh-uh..."
            mike.say "Like I was saying, we thought he was away on business."
            mike.say "So we took it as a chance to break into his safe."
            "I watch as one of the detective's eyebrows rises at this."
            show inspector at startle(0.1, -5)
            "Michaels" "Erm..."
            "Michaels" "Would you mind explaining exactly why you were doing that?"
            mike.say "Cherie was sure that Dwayne had been cooking the books, you know?"
            mike.say "That there was a ledger of accounts in the safe that would prove it."
            show inspector at startle(0.1, -5)
            "Michaels" "Hmm..."
            "Michaels" "That's a serious offence, right there."
            mike.say "But just as we got our hands on it, Dwayne walked in on us."
            show inspector at startle(0.1, -5)
            "Michaels" "And let me guess - he wasn't pleased?"
            "I can't help frowning as I recount the events that followed."
            "The memories causing me genuine discomfort as I do so."
            mike.say "He attacked Cherie, and I think he would have killed her."
            mike.say "But I intervened and we ended up having one hell of a fight."
            show inspector at startle(0.1, -5)
            "Michaels" "The result of which was...what, exactly?"
            "I realise that this is the moment, that I've reached the point of no return."
            mike.say "I killed him."
            mike.say "There was a gun in the room..."
            mike.say "I don't remember if Cherie brought it or Dwayne did."
            mike.say "But somehow I got hold of it, and I shot him."
            "The detective's eyes are almost popping out of their sockets by now."
            "And he slowly shakes his head, like he can't quite believe what he's hearing."
            show inspector at startle(0.1, -5)
            "Michaels" "And then what?"
            "Michaels" "Mister Jackson's body just turned to dust and blew away?"
            "Michaels" "And the gun you used - where's that?"
            "It's too late for me to turn back now, I'm in too deep."
            "So I grit my teeth and keep on confessing to the detective."
            mike.say "We got rid of them, Cherie and me."
            mike.say "I can tell you where to look for them, if you like?"
            show inspector at startle(0.1, -5)
            "Michaels" "Nah, there's going to be plenty of time for that later."
            "Michaels" "Right now, I need to take you down to the station."
            mike.say "I suppose that I'm under arrest?"
            show inspector at startle(0.1, -5)
            "Michaels" "Buddy, you just confessed to murder."
            "Michaels" "So take a wild guess!"
            show inspector at center, traveling(1.5, 1.0, (640, 1000))
            "I nod as the detective puts a hand on my shoulder, leading me towards the door."
            "There's no point in arguing or making a scene, as this is what I expected would happen."
            "Now all I can hope is that things turn out for the best."
            "That my version of events holds up to scrutiny."
            "And that Cherie and Aletta manage to get off scott-free."
            $ renpy.full_restart()
            return
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 1)
    return

label cherie_event_08_2:
    if cherie.love.max < 160:
        $ cherie.love.max = 160
    "I'm sitting at my desk, working hard as usual, when I hear the sound of an unfamiliar voice."
    "Michaels" "Erm..."
    "Michaels" "Yeah..."
    "Michaels" "Could you maybe tell me whereabouts I can find Mrs Jackson?"
    "My head pops up as soon as I recognise the mumbling voice of the detective on Dwayne's case."
    scene bg office at center, zoomAt(1.0, (640, 720))
    show inspector at center, zoomAt(0.9, (920, 720))
    if not shiori.hidden:
        show shiori _a sad at center, zoomAt(0.9, (380, 720))
        with fade
        "And it doesn't take me long to spot him either, in his shabby raincoat and creased shirt."
        "Because the guy looks totally out of place standing in the middle of our stylish, modern offices."
        "Right now he's talking to Shiori, fingering his badge."
    else:
        with fade
        "And it doesn't take me long to spot him either, in his shabby raincoat and creased shirt."
        "Because the guy looks totally out of place standing in the middle of our stylish, modern offices."
        "Right now he's talking to one of the girls that works on the same floor as me, fingering his badge."
    "But I'm already leaping up out of my chair, almost sending it crashing into the wall behind me."
    show bg office at center, traveling(1.25, 0.5, (540, 880))
    show inspector at center, traveling(1.25, 0.5, (740, 900))
    if not shiori.hidden:
        show shiori _a sadsmile at center, traveling(1.25, 0.5, (140, 880))
        "And then I dash across the space between us, waving a hand in the air as I get closer to him."
        mike.say "Hey, there..."
        mike.say "Hello...yes..."
        mike.say "Detective Michaels, what can I do for you?"
        hide shiori with easeoutleft
        "Shiori seems to sense the manic energy I'm giving out."
    else:
        "And then I dash across the space between us, waving a hand in the air as I get closer to him."
        mike.say "Hey, there..."
        mike.say "Hello...yes..."
        mike.say "Detective Michaels, what can I do for you?"
        "The girl that Michaels was talking to seems to sense the manic energy I'm giving out."
    "And she takes the opportunity to retreat without saying a word to either of us."
    show inspector at center, traveling(1.5, 1.0, (640, 1000))
    "But that's no problem, as the detective seems to recognise me in an instant."
    show inspector at startle(0.1, -5)
    "Michaels" "Oh..."
    "Michaels" "Mister [hero.family_name]…"
    "Michaels" "Of course, you're one of Mister Jackson's employees, aren't you?"
    mike.say "Well, I'm actually one of the bigger cogs in the corporate machine!"
    mike.say "But that's not important right now..."
    if hero.knowledge >= 50 or hero.has_skill("investigator"):
        mike.say "Did I just hear you asking after Mrs Cherie Jackson?"
        $ hero.flags.police_trust += 2
    else:
        mike.say "Did I just hear you asking after Cherie?"
        "The moment that I use Cherie's first name in his presence, I know that I've made a mistake."
        "Because as soon as he hears it, Michaels raises his eyebrows in a look of surprise and interest."
        $ hero.flags.police_trust -= 2
    "His weather-beaten features suddenly coming to life as his curiosity is piqued."
    show inspector at startle(0.1, -5)
    "Michaels" "Ooh la la!"
    "Michaels" "Now that's one hell of a fancy name."
    "Michaels" "I'm guessing the lady in question is French?"
    "Michaels" "And we all know what they say about the French, right?"
    "Before I can say anything in response, Michaels chuckles and elbows me in the ribs."
    "I think it's supposed to be one of those old-fashioned, manly gestures of solidarity."
    "But the problem is it catches me totally off-guard, and almost doubles me over."
    mike.say "Ouch!" with vpunch
    "And it's while I'm clutching my side that I hear another voice speaking nearby."
    cherie.say "Non, mon ami…"
    cherie.say "I do not know what they say about us!"
    cherie.say "So perhaps you would be so kind as to enlighten me?"
    show inspector at startle(0.1, -5)
    "Michaels" "Pardon me, madame..."
    "Michaels" "I wasn't aware that there was a lady present."
    "Michaels" "I will endeavour to improve the quality of my language from now on."
    show inspector at center, traveling(1.25, 0.3, (340, 880))
    show cherie at center, zoomAt(1.15, (940, 820)) with easeinright
    "I've just about managed to start breathing again by the time the two are talking."
    "And I'm watching the most extraordinary change taking place in front of me."
    "Cherie's standing there, looking at Michaels as though she's waiting to be impressed."
    "But he's acting totally weird, trying to stand up straight and even fussing with his hair."
    "I mean, none of it seems to be improving the way he looks, but that's not the point."
    "What matters is that he's obviously trying to put on a good show for Cherie!"
    mike.say "Erm..."
    mike.say "This is Detective Michaels..."
    mike.say "He's working on Mister Jackson's case."
    show inspector at startle(0.1, -5)
    "Michaels" "Pleased to meet you, Missus Jackson."
    "Michaels" "You have already given statements to my colleagues, but it is time to speak to you directly."
    show inspector at center, zoomAt(1.25, (380, 880)) with ease
    "Michaels shuffles forwards, holding out his hand for Cherie to shake."
    show cherie amused at center, zoomAt(1.15, (900, 820)) with ease
    "And when she holds out her own, he's obviously supposed to kiss it."
    "But instead the bumbling detective grabs it and starts to waggle it up and down instead."
    show cherie happy
    cherie.say "Enchanted, I'm sure..."
    cherie.say "Now, what can I do for you?"
    show cherie normal
    "Michaels opens his mouth to answer the question."
    "But I'm already feeling more than a little paranoid at his turning up unannounced."
    "And on top of that, his obvious attraction to Cherie is making my jealously flare up too."
    "So I feel the need to step in and do what I can to take control of the situation."
    menu:
        "Stay cool" if hero.charm >= 75:
            mike.say "I'm sorry, Mrs Jackson..."
            mike.say "I'd have brought the detective straight to you."
            mike.say "But I'm afraid that I initially mistook him for one of the janitors."
            "Michaels wrinkles his face into an expression of annoyance."
            show inspector at startle(0.1, -5)
            "Michaels" "Hey..."
            "Michaels" "I'll have you know this outfit was the height of fashion when I bought it!"
            mike.say "Oh, no doubt at all..."
            mike.say "You must have traded, what...a dozen mammoth tusks for it?"
            "Michaels's eyes almost pop out of their sockets as I continue to needle him."
            "And I can see that he's doing the best he can to come up with a response."
            "But, luckily for him, Cherie steps in to save him from further humiliation."
            show cherie angry
            cherie.say "Now, now, [hero.name]…"
            cherie.say "Leave the good detective alone."
            show cherie talkative
            cherie.say "He is here to execute his duty, after all."
            show cherie normal
            "Michaels ruffles himself up as Cherie says all of this."
            "Like a scruffy pigeon shaking off a failed attack from a vicious cat."
            show inspector at startle(0.1, -5)
            "Michaels" "Erm..."
            "Michaels" "Thank you, Cherie..."
            "Michaels" "Ah...may I call you that?"
            show cherie happy
            cherie.say "Well, it seems like you already have!"
            show cherie normal
            "I watch as the two of them begin to converse, obviously jealous of Michaels."
            "But I feel a sense of pride that I managed to skewer him in front of Cherie all the same."
            "And secure in the knowledge that she was forced to come to his rescue as well."
            $ hero.flags.police_trust += 2
        "Step in":
            mike.say "You know that you can't just walk in here and start asking questions, don't you?"
            mike.say "This is private property, so you at least need a warrant to come waltzing in off the street!"
            show cherie stuned
            "Michaels and Cherie turn to look at me as one."
            "And I can see the surprise on their faces."
            "But I'm already in a peevish mood, and so that's not going to stop me."
            mike.say "Well?"
            mike.say "What have you got to say to that?"
            mike.say "I bet you don't like it when people actually know their rights!"
            show inspector at startle(0.1, -5)
            "Michaels wrinkles his face up as he shakes his head at me."
            "Michaels" "Geez..."
            "Michaels" "I didn't know you could be a lawyer and a clown at the same time!"
            "Michaels" "What's the salary for that kind of thing like?"
            "Michaels" "Or do you just get to eat the rotten vegetables they throw at you?"
            "I can feel my sense of irritation growing as Michaels makes fun of me."
            "But what's worse is the sound of Cherie giggling at my expense."
            mike.say "What did you just say to me?"
            mike.say "I have never been so insulted in all my..."
            show cherie angry
            cherie.say "That's enough, [hero.name]."
            show cherie annoyed
            mike.say "But...I..."
            show cherie upset
            cherie.say "I said that is enough."
            cherie.say "Now please be silent while I answer the detective's questions."
            show cherie annoyed
            "I open my mouth to say more, but as I do so, Cherie widens her eyes."
            "The gesture is more than enough to kill the words in my throat."
            "And I can't help feeling totally humiliated as I'm forced to back off."
            $ hero.flags.police_trust -= 2
    show cherie talkative
    cherie.say "So, Detective..."
    cherie.say "If you don't mind, a quieter room should be more appropirate to persue our conversation."
    show cherie normal
    show inspector at startle(0.1, -5)
    "Michaels" "Of course."
    mike.say "My office is right there."
    if hero.flags.isceo:
        show bg ceo
    else:
        show bg personal
    with fade
    "Once the three of us are in my office, Cherie goes directly to the point."
    show cherie talkative
    cherie.say "I am thinking that you have questions for me?"
    show cherie normal
    show inspector at startle(0.1, -5)
    "Michaels" "That's right, Cherie..."
    "I note that Michaels grins as he says her name."
    show inspector at startle(0.1, -5)
    "Michaels" "Just the usual stuff I need to ask in this kind of a situation."
    "Michaels" "Obviously your husband was missing for few days before the discovery of his remains..."
    "Michaels" "So I need to ask you what you know about all that."
    "Michaels" "You know, what you think might have happened, anything that could be relevant to our enquiries?"
    "I can't help holding my breath as I wait to hear what Cherie's going to say."
    "Because I know full well how important her answer is to both of our futures."




    $ cherie.flags.cherie_response = "default"


    if cherie.flags.dwaynedeath_truth:
        $ cherie.flags.cherie_response = "truth"


    elif (cherie.flags.dwaynedeath_partialtruth or
          cherie.flags.hero_rivalry >= 0 or
          aletta.flags.threat):
        $ cherie.flags.cherie_response = "betrayal"


    elif (cherie.flags.dwaynedeath_dwaynegone or
          aletta.flags.liability or
          aletta.flags.ally):
        $ cherie.flags.cherie_response = "denial"


    elif cherie.flags.dwaynedeath_cherieknife or cherie.sub >= 90:
        $ cherie.flags.cherie_response = "cherie_confess"


    elif cherie.flags.dwaynedeath_mikeselfdefense or cherie.love <= 100:
        $ cherie.flags.cherie_response = "hero_confess"

    if debug:
        $ renpy.log(f"cherie_event_08_2 cherie.flags.cherie_response: {cherie.flags.cherie_response}")

    if cherie.flags.cherie_response == "truth":
        "Cherie takes a deep breath and nods her head."
        show cherie whining
        cherie.say "The truth, Detective, is that my husband is dead."
        show cherie sad
        if not cherie.flags.dwaynedeath_truth:
            "The words hit me like a punch to the jaw."
            "And I can't keep myself from crying out."
            mike.say "Cherie..."
            mike.say "No!"
            "Cherie holds up a hand to silence me."
            show cherie whining
            cherie.say "[hero.name]…"
            cherie.say "We must tell the whole truth."
            cherie.say "It is the only way things will ever be settled."
            show cherie sad
        "I have to bite my lip as Cherie continues to explain herself to Michaels."
        show cherie talkative
        cherie.say "It happened at my home, while my husband was supposed to be away on business."
        cherie.say "[hero.name] and I were taking a ledger from his safe that would prove fraud within the company."
        show cherie normal
        "By now Michaels's eyes are almost bulging as Cherie unburdens herself."
        "He's produced a notepad and pen so that he can take notes."
        "And he keeps on nodding as he frantically scribbles down what she's saying."
        show inspector at startle(0.1, -5)
        "Michaels" "So you suspected financial jiggery-pokery?"
        "Michaels" "That would explain a lot!"
        show cherie talkative
        cherie.say "Yes, but then Dwayne walked in on us."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "He came back from his trip early?"
        show cherie whining
        cherie.say "Perhaps - or maybe he always meant to catch us in the act."
        cherie.say "I do not know, and now I obviously cannot ask him."
        cherie.say "Whatever the truth is, he went mad, attacking [hero.name] and I."
        cherie.say "And I honestly believe he would have killed us."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "If one of you hadn't killed him first?"
        "Cherie shakes her head at this."
        "And that's when I know she's going to drag someone else into it too."
        show cherie talkative
        cherie.say "No, Detective..."
        cherie.say "It was Aletta, another of his employees, who did that."
        cherie.say "She shot him, and the wound proved to be fatal."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "So this Aletta, she was there too..."
        "Michaels" "And she shot Mister Jackson in order to protect the two of you?"
        "Cherie shakes her head again, then shrugs."
        show cherie talkative
        cherie.say "Perhaps..."
        cherie.say "Perhaps not..."
        cherie.say "My husband had many affairs, Detective."
        cherie.say "Aletta was one of his conquests."
        cherie.say "And he was known to be...exploitative towards her."
        show cherie sad
        "Michaels stops writing and rubs the back of his head."
        show inspector at startle(0.1, -5)
        "Michaels" "So let me guess..."
        "Michaels" "Then the three of you disposed of the body and the murder weapon?"
        "Cherie opens her mouth to say more."
        "But this time it's Michaels's turn to hold up a hand and stop her."
        show inspector at startle(0.1, -5)
        "Michaels" "No, don't tell me."
        "Michaels" "We can thrash out the finer details at the station."
        "Michaels" "Because the two of you are under arrest."
        "Michaels" "Let's go!"
        "I keep my head down as Michaels leads Cherie and me out of the offices."
        "My guess is that he'll send someone else along to get Aletta later."
        "There's no point in arguing or trying to get away."
        "Cherie just laid it all out in front of the detective."
        "So all I can do now is cooperate in the hope of getting off as lightly as possible."
        $ renpy.full_restart()
    elif cherie.flags.cherie_response == "betrayal":
        "Cherie takes a deep breath and nods her head."
        show cherie whining
        cherie.say "The truth, Detective, is that my husband is dead."
        show cherie sad
        if not cherie.flags.dwaynedeath_partialtruth:
            "The words hit me like a punch to the jaw."
            "And I can't keep myself from crying out."
            mike.say "Cherie..."
            mike.say "No!"
            "Cherie holds up a hand to silence me."
            show cherie whining
            cherie.say "[hero.name]…"
            cherie.say "We must tell the whole truth."
            cherie.say "It is the only way things will ever be settled."
            show cherie sad
        "I have to bite my lip as Cherie continues to explain herself to Michaels."
        show cherie talkative
        cherie.say "It happened at my home, while my husband was supposed to be away on business."
        show cherie normal
        "By now Michaels's eyes are almost bulging as Cherie unburdens herself."
        "He's produced a notepad and pen so that he can take notes."
        "And he keeps on nodding as he frantically scribbles down what she's saying."
        show inspector at startle(0.1, -5)
        "Michaels" "He came back from his trip early?"
        show cherie whining
        cherie.say "I do not know, and now I obviously cannot ask him."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "If one of you hadn't first?"
        "Cherie shakes her head at this."
        "And that's when I know she's going to drag someone else into it too."
        show cherie whining
        cherie.say "But he was not alone, Detective..."
        cherie.say "It was Aletta, another of his employees, who killed him."
        cherie.say "She shot him, and the wound proved to be fatal."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "So this Aletta, she was there too..."
        "Michaels" "And she shot Mister Jackson in order to...?"
        "Cherie shakes her head again, then shrugs."
        show cherie angry
        cherie.say "My husband had many affairs, Detective."
        cherie.say "Aletta was one of his conquests."
        cherie.say "And he was known to be...exploitative towards her."
        show cherie sad
        "Michaels stops writing and rubs the back of his head."
        show inspector at startle(0.1, -5)
        "Michaels" "So let me guess..."
        "Michaels" "She threatened you to help her dispose of the body and the murder weapon?"
        "Cherie opens her mouth to say more."
        "But this time it's Michaels's turn to hold up a hand and stop her."
        show inspector at startle(0.1, -5)
        "Michaels" "No, don't tell me."
        "Michaels" "We can thrash out the finer details at the station."
        "Michaels" "Because you are going to make a deposition."
        "Michaels" "Let's go!"
        "I keep my head down as Michaels leads Cherie out of the offices."
        "My guess is that he'll send someone else along to get Aletta later."
        $ aletta.set_gone_forever()
    elif cherie.flags.cherie_response == "denial":
        show cherie whining
        cherie.say "I'm willing to tell you all that I know, Detective..."
        cherie.say "But I think that you have made a wasted journey."
        cherie.say "Because I know no more than I have already told your colleagues."
        cherie.say "My husband left on a business trip, and he has not returned."
        cherie.say "And few days later the police announced that he had been found dead."
        show cherie sad
        "Michaels listens patiently to what Michaels has to say."
        "But once she's finished, he gives her a knowing smile."
        "In fact I almost expect him to add a nod and a wink too."
        show inspector at startle(0.1, -5)
        "Michaels" "Ah..."
        "Michaels" "Come on, Missus Jackson..."
        "Michaels" "Don't try to kid a kidder!"
        show cherie surprised
        cherie.say "Whatever can that mean?"
        show cherie stuned
        show inspector at startle(0.1, -5)
        "Michaels" "You're a worldly woman, right?"
        "Michaels" "You know what a guy like your husband was getting up to, don't you?"
        show cherie annoyed
        "Cherie raises her eyebrows at the question."
        show cherie angry
        cherie.say "I am afraid I do not, Detective..."
        cherie.say "What exactly are you trying to suggest my husband was doing?"
        show cherie annoyed
        "I can see a look of pain beginning to creep into Michaels's smile."
        "Like he's having to fight hard to keep up his affable demeanour."
        "And for a moment I think that he might actually crack."
        "But then he throws his hands into the air and shakes his head."
        show inspector at startle(0.1, -5)
        "Michaels" "Okay, okay..."
        "Michaels" "If you say that's all you know, then that's all you know."
        "Michaels" "I'll leave my card at reception, so you can call me if you remember anything else."
        hide inspector with easeoutleft
        "With that, Michaels turns on his heel and walks out, leaving Cherie and me alone."
        show cherie at center, zoomAt(1.5, (640, 1040)) with fade
        "Once he's gone, Cherie picks up the phone on the desk and speaks to the secretary on the other end."
        "I'm not sure what she's doing until someone comes bustling through the door a moment later."
        "And I see that they're carrying a tray of sandwiches and a pot of fresh coffee."
        show cherie talkative
        cherie.say "After that little interrogation, I thought we could use some refreshments."
        show cherie normal
        "I can feel myself relaxing as I pick up one of the sandwiches and Cherie pours the coffee."
        mike.say "You think it helped that the detective they sent had a crush on you?"
        show cherie smile
        "Cherie smiles at me over her cup of coffee."
        show cherie happy
        cherie.say "I don't think that it hurt my case!"
        cherie.say "And anyway, it was good to see you a little jealous, mon ami."
        cherie.say "You are so cute when that happens!"
        show cherie normal
        "I feel a strange sense of embarrassment and relief as Cherie grins at me."
        "Glad that Michaels is gone, but also thrilled that Cherie prefers me over him."
        mike.say "I'm sorry if I was being a little childish back there."
        "Cherie shakes her head."
        show cherie happy
        cherie.say "Of course not, mon ami…"
        cherie.say "I am often not as warm to you as I should be when we are in public together."
        cherie.say "Because I am worried people will think that I have not grieved for Dwayne long enough."
        show cherie normal
        "I reach out and put my hand atop Cherie's, a small gesture of closeness and support."
        show cherie smile
        "But from the smile that spreads across her face, I know that she appreciates it."
        "That she knows it's a show of our unity against all the forces conspiring against us right now."
    elif cherie.flags.cherie_response == "cherie_confess":
        "Cherie takes a deep breath and nods her head."
        show cherie whining
        cherie.say "The truth, Detective, is that my husband is dead."
        cherie.say "And I am the one that killed him."
        show cherie sad
        if not cherie.flags.dwaynedeath_cherieknife:
            "The words hit me like a punch to the jaw."
            "And I can't keep myself from crying out."
            mike.say "Cherie..."
            mike.say "No!"
            "Cherie holds up a hand to silence me."
            show cherie whining
            cherie.say "[hero.name]…"
            cherie.say "We must tell the whole truth."
            cherie.say "It is the only way things will ever be settled."
            show cherie sad
        "I have to bite my lip as Cherie continues to explain herself to Michaels."
        show cherie talkative
        cherie.say "It happened at my home, while my husband was supposed to be away on business."
        cherie.say "[hero.name] and I were taking a ledger from his safe that would prove fraud within the company."
        show cherie normal
        "By now Michaels's eyes are almost bulging as Cherie unburdens herself."
        "He's produced a notepad and pen so that he can take notes."
        "And he keeps on nodding as he frantically scribbles down what she's saying."
        show inspector at startle(0.1, -5)
        "Michaels" "So you suspected financial jiggery-pokery?"
        "Michaels" "That would explain a lot!"
        show cherie talkative
        cherie.say "Yes, but then Dwayne walked in on us."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "He came back from his trip early?"
        show cherie whining
        cherie.say "Perhaps - or maybe he always meant to catch us in the act."
        cherie.say "I do not know, and now I obviously cannot ask him."
        cherie.say "Whatever the truth is, he went mad, attacking [hero.name] and I."
        cherie.say "And I honestly believe he would have killed us."
        show cherie sad
        "Michaels" "If you hadn't killed him first?"
        "Cherie nods at this."
        show cherie whining
        cherie.say "I reached for the first thing that came to hand."
        cherie.say "And fate decreed that was a knife."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels holds up a hand before Cherie can say anything more."
        "Michaels" "No, don't tell me."
        "Michaels" "We can thrash out the finer details at the station."
        "Michaels" "Because the two of you are under arrest."
        "Michaels" "Let's go!"
        "I keep my head down as Michaels leads Cherie and me out of the offices."
        "There's no point in arguing or trying to get away."
        "Cherie just laid it all out in front of the detective."
        "So all I can do now is cooperate in the hope of getting off as lightly as possible."
        $ cherie.set_gone_forever()
    elif cherie.flags.cherie_response == "hero_confess":
        "Cherie takes a deep breath and nods her head."
        show cherie whining
        cherie.say "The truth, Detective, is that my husband is dead."
        show cherie sad
        if not cherie.flags.dwaynedeath_mikeselfdefense:
            "The words hit me like a punch to the jaw."
            "And I can't keep myself from crying out."
            mike.say "Cherie..."
            mike.say "No!"
            "Cherie holds up a hand to silence me."
            show cherie whining
            cherie.say "[hero.name]…"
            cherie.say "We must tell the whole truth."
            cherie.say "It is the only way things will ever be settled."
            show cherie sad
        "I have to bite my lip as Cherie continues to explain herself to Michaels."
        show cherie talkative
        cherie.say "It happened at my home, while my husband was supposed to be away on business."
        cherie.say "[hero.name] and I were taking a ledger from his safe that would prove fraud within the company."
        show cherie normal
        "By now Michaels's eyes are almost bulging as Cherie unburdens herself."
        "He's produced a notepad and pen so that he can take notes."
        "And he keeps on nodding as he frantically scribbles down what she's saying."
        show inspector at startle(0.1, -5)
        "Michaels" "So you suspected financial jiggery-pokery?"
        "Michaels" "That would explain a lot!"
        show cherie whining
        cherie.say "Yes, but then Dwayne walked in on us."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "He came back from his trip early?"
        show cherie whining
        cherie.say "Perhaps - or maybe he always meant to catch us in the act."
        cherie.say "I do not know, and now I obviously cannot ask him."
        cherie.say "Whatever the truth is, he went mad, attacking [hero.name] and I."
        cherie.say "And I honestly believe he would have killed us."
        show cherie sad
        show inspector at startle(0.1, -5)
        "Michaels" "If one of you hadn't killed him first?"
        "Cherie nods at this."
        show cherie whining
        cherie.say "If [hero.name] had not brought his gun, I honestly believe we would both be dead."
        show cherie sad
        "I'm nodding along with all that Cherie's said, right up to that last point."
        if not cherie.flags.dwaynedeath_mikeselfdefense:
            "Because that's when I realise the implications of what she just told Michaels."
            mike.say "Cherie..."
            mike.say "What the hell?!?"
        "All of a sudden Michaels is looking at me in a whole different way."
        show cherie talkative
        cherie.say "I am sorry, [hero.name]…"
        cherie.say "But I have to tell them the truth!"
        show cherie sad
        if not cherie.flags.dwaynedeath_mikeselfdefense:
            "I'm shaking my head as I feel like the ground is giving way under me."
            mike.say "But that's not how it happened..."
            mike.say "You have to tell them the truth!"
            show cherie talkative
            cherie.say "No, mon ami…"
            cherie.say "I cannot tell them any more lies!"
        show cherie sadsmile
        "I don't hear what the Michaels is saying as he puts his hand on my shoulder."
        "And I keep my head down as he leads me out of the offices."
        "There's no point in arguing or trying to get away."
        "Cherie just laid it all out in front of the detective."
        "So all I can do now is cooperate in the hope of getting off as lightly as possible."
        $ renpy.full_restart()
    $ hero.replace_activity()
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 1)
    return


label cherie_event_09:
    $ arrest_reason = ""
    $ hero_arrest_reason = ""

    $ suspects = set()



    if hero.flags.dwaynedeath_truth or hero.flags.dwaynedeath_partialtruth:
        $ suspects.add("hero")

        if hero.flags.dwaynedeath_truth:
            $ suspects.add("aletta")
            $ suspects.add("cherie")


    if aletta.flags.dwaynedeath_truth or aletta.flags.dwaynedeath_partialtruth:
        $ suspects.add("aletta")


    if cherie.flags.cherie_response == "truth":
        $ suspects.add("hero")
        $ suspects.add("aletta")
        $ suspects.add("cherie")
    elif cherie.flags.cherie_response == "betrayal":
        $ suspects.add("aletta")
    elif cherie.flags.cherie_response == "cherie_confess":
        $ suspects.add("cherie")
    elif cherie.flags.cherie_response == "hero_confess":
        $ suspects.add("hero")



    if hero.flags.dwayne_corpse == "mansion" or game.flags.handle_gun_body is False:
        $ suspects.add("hero")
        $ suspects.add("cherie")

    if hero.flags.aletta_gun == "mansion" or game.flags.handle_gun_body is False:
        $ suspects.add("hero")
        $ suspects.add("aletta")


    if hero.flags.dwayne_corpse and hero.flags.dwayne_corpse == hero.flags.aletta_gun:
        $ suspects.add("hero")
        $ suspects.add("aletta")
        $ suspects.add("cherie")
        $ hero.flags.police_trust -= 10


    if hero.has_item("dwayne_corpse"):
        $ hero.flags.police_trust -= 10


    if hero.has_item("aletta_gun"):
        $ hero.flags.police_trust -= 5



    if hero.flags.police_trust >= 5:

        if "hero" in suspects and not (hero.flags.dwaynedeath_truth or hero.flags.dwaynedeath_partialtruth):
            $ suspects.discard("hero")


    elif hero.flags.police_trust <= -5:

        if not suspects:
            $ suspects.add("hero")

    $ renpy.log(f"cherie_event_09 suspects: {suspects}")

    if cherie.love.max < 180:
        $ cherie.love.max = 180

    if "hero" in suspects and "aletta" in suspects and "cherie" in suspects:

        $ arrest_reason = "being an accessory to the murder of Dwayne Jackson"
        $ hero_arrest_reason = arrest_reason
        "I can hear the sound of subdued voices spreading throughout the office."
        "And I know what the reason must be even before I raise my head from my work."
        "Because the truth is that I've been waiting for this moment to come."
        show inspector at center, zoomAt(1.0, (840, 720))
        show camila at center, zoomAt(1.0, (440, 720))
        with dissolve
        show inspector at center, traveling(1.25, 0.5, (840, 900))
        show camila at center, traveling(1.25, 0.5, (440, 880))
        "So when I see Detective Michaels and Camila walking towards me, it comes as no surprise."
        "And the fact that they have grim determination written all over their faces just proves it."
        "The game is finally up, as they're here to arrest me."
        "I make a point of standing and holding out my hands as they reach my desk."
        "Hoping that they'll understand it means that I'm going to come quietly."
        show inspector at startle(0.1, -5)
        "Michaels" "[hero.name] [hero.family_name]…"
        if hero.flags.police_trust >= 5:
            "Michaels" "I'm sorry to have to do this, given how helpful you've been..."
            "Michaels" "But I'm afraid that you're under arrest on suspicion of [hero_arrest_reason]."
        elif hero.flags.police_trust <= -5:
            "Michaels" "I knew there was something fishy about you from the start."
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        else:
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        "Michaels" "You do not have to say anything..."
        "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
        "Michaels" "Anything you do say may be given in evidence."
        "I keep my lips firmly closed all the time Michaels is reading me my rights."
        "And when he's done, the detective gives Camila a nod."
        "Then she steps forwards, pulling out her handcuffs and using them to bind my wrists."
        "But as she's doing so, we're close enough that nobody else can overhear us."
        show camila sadsmile
        camila.say "Don't worry, [hero.name], I know you were framed."
        camila.say "I'm going to do everything I can to prove it too."
        camila.say "As well as nailing the bastard that did this to you!"
        show camila sad
        mike.say "Thanks, Camila..."
        mike.say "With you on my side, I know I have a chance."
        "Camila and I exchange a subtle nod."
        "By now Michaels is standing in front of the doors to what used to be Dwayne's office."
        "His hand is balled into a fist and raised, ready to rap on the wood."
        "But before he can do so, the doors swing open and he's forced to take a step backwards."
        show inspector at center, traveling(1.25, 0.3, (640, 900))
        show camila at center, traveling(1.25, 0.3, (340, 880))
        show cherie normal at center, zoomAt(1.25, (940, 900)) with easeinright
        "Because Cherie comes sweeping out, looking every bit like a queen holding court."
        show cherie talkative
        cherie.say "What is all this?"
        cherie.say "Do you two have an appointment?"
        show camila annoyed
        "Camila seems to be more than little flustered by this show of defiance."
        show camila upset
        "Her cheeks flushing as she all but squares up to Cherie."
        "I guess she already used up the last of her calm and compassion dealing with me."
        show camila angry
        camila.say "An appointment?!?"
        camila.say "We're the police - we don't need no damn appointment!"
        show camila upset
        "Luckily for everyone involved, Michaels seems to be able to keep a cooler head than his colleague."
        "Because he simply pulls out his badge and waves it vaguely in front of Cherie's face."
        show inspector at startle(0.1, -5)
        "Michaels" "Missus Jackson…"
        "Michaels" "You too are under arrest on suspicion of the murder of your husband, Dwayne Jackson."
        "Michaels" "You do not have to say anything..."
        "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
        "Michaels" "Anything you do say may be given in evidence."
        show cherie normal
        "I've got to admit that I'm not sure how I was expecting Cherie to react."
        "Whether she would finally collapse once she was finally arrested."
        show cherie amused
        "Or if she'd tough it out and keep on playing the dignified widow."
        "But it's not long before I get my answer, as she simply raises an eyebrow."
        show cherie talkative
        cherie.say "Is that so, Detective?"
        cherie.say "Then I will consent to come with you to the police station."
        show camila angry
        cherie.say "But I must inform you that I will not be answering any questions..."
        show camila upset
        "The statement is so emphatic and matter-of-fact that it seems to trigger Camila."
        "Right now she seems to be like a tensed spring, a vein actually standing out on her forehead."
        show camila angry
        camila.say "Oh, you won't, huh?"
        camila.say "Lady, I don't think you know how this works!"
        show camila upset
        show cherie normal
        "Cherie turns her gaze on Camila, staring the younger woman down."
        show cherie talkative
        cherie.say "And you do not seem to understand basic manners, Detective."
        cherie.say "If you would have let me finish, I would have added - until my lawyer is present."
        show inspector at startle(0.1, -5)
        "Michaels" "Erm..."
        "Michaels" "Mrs Jackson does have that right."
        show cherie angry
        cherie.say "Oh, believe me, Detective Michaels..."
        cherie.say "I know my rights, and I know just who has betrayed me!"
        show cherie normal
        "Cherie holds out her hands as she says this, letting Camila cuff her."
        hide cherie with dissolve
        show aletta normal at center, zoomAt(1.25, (940, 880)) with easeinright
        "By now Aletta's emerged from her office too, no doubt drawn by the commotion out here."
        show aletta surprised
        "She hurried over, hands outstretched, as if reaching for Cherie and me."
        "Which makes it a simple matter for Camila to cuff her too."
        show aletta stuned
        "Aletta looks down at her wrists, a puzzled look on her face."
        show aletta surprised
        aletta.say "Wha…"
        aletta.say "What the..."
        show aletta stuned
        show camila talkative
        camila.say "Miss Applebaum..."
        camila.say "You are also under arrest on suspicion of being an accessory to the murder of Dwayne Jackson."
        camila.say "And all the good stuff my colleague already said to your colleagues applies to you too!"
        show camila upset
        hide aletta
        hide camila
        hide inspector
        with dissolve
        "Literally everyone in the office is gathered around, watching us by now."
        "Part of me wants to see the looks on their faces so that I can judge their response."
        "But three of us are already being led away, and I can't look back."
        "So I guess that's the end of my story, at least as a free man."
        "Dwayne's dead, Aletta, Cherie and I are going down for it."
        "And as for the company, I guess Cassidy will most likely inherit the lot."
        "While I'll get a private cell in which to sit and dwell on where it all went wrong."
        $ renpy.full_restart()
    elif "hero" in suspects and "aletta" in suspects:

        $ arrest_reason = "the murder of Dwayne Jackson"
        $ hero_arrest_reason = arrest_reason
        "I can hear the sound of subdued voices spreading throughout the office."
        "And I know what the reason must be even before I raise my head from my work."
        "Because the truth is that I've been waiting for this moment to come."
        show inspector at center, zoomAt(1.0, (840, 720))
        show camila at center, zoomAt(1.0, (440, 720))
        with dissolve
        show inspector at center, traveling(1.25, 0.5, (840, 900))
        show camila at center, traveling(1.25, 0.5, (440, 880))
        "So when I see Detective Michaels and Camila walking towards me, it comes as no surprise."
        "And the fact that they have grim determination written all over their faces just proves it."
        "The game is finally up, as they're here to arrest me."
        "I make a point of standing and holding out my hands as they reach my desk."
        "Hoping that they'll understand it means that I'm going to come quietly."
        show inspector at startle(0.1, -5)
        "Michaels" "[hero.name] [hero.family_name]…"
        if hero.flags.police_trust >= 5:
            "Michaels" "I'm sorry, [hero.name], but rules are rules."
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        elif hero.flags.police_trust <= -5:
            "Michaels" "I think it's time we had a proper chat down at the station."
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        else:
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        "Michaels" "You do not have to say anything..."
        "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
        "Michaels" "Anything you do say may be given in evidence."
        "I keep my lips firmly closed all the time Michaels is reading me my rights."
        "And when he's done, the detective gives Camila a nod."
        "Then she steps forwards, pulling out her handcuffs and using them to bind my wrists."
        "But as she's doing so, we're close enough that nobody else can overhear us."
        show camila sadsmile
        camila.say "Don't worry, [hero.name], I know you were framed."
        camila.say "I'm going to do everything I can to prove it too."
        camila.say "As well as nailing the bastard that did this to you!"
        show camila sad
        mike.say "Thanks, Camila..."
        mike.say "With you on my side, I know I have a chance."
        "Camila and I exchange a subtle nod."
        "And then we go back to pretending to be on opposite sides."
        "By now Michaels is standing in front of the door of Aletta's office."
        "His hand is balled into a fist and raised, ready to rap on the wood."
        "But before he can do so, the doors swing open and he's forced to take a step backwards."
        show inspector at center, traveling(1.25, 0.3, (640, 900))
        show camila at center, traveling(1.25, 0.3, (340, 880))
        show aletta normal at center, zoomAt(1.25, (940, 880)) with easeinright
        "Because Aletta comes sweeping out, oozing confidence as she glares down at him."
        show aletta talkative
        aletta.say "Can I help you two?"
        aletta.say "I thought that I already answered all of your questions?"
        show camila annoyed
        "Camila seems to be more than little flustered by this show of defiance."
        show camila blush
        "Her cheeks flushing as she all but squares up to Aletta."
        show camila angry
        camila.say "Hey, we're the ones that are gonna be asking the questions around here."
        camila.say "We're the police - and we don't take orders from the likes of you!"
        show camila upset
        "Luckily for everyone involved, Michaels seems to be able to keep a cooler head than his colleague."
        "Because he simply pulls out his badge and waves it vaguely in front of Aletta's face."
        show inspector at startle(0.1, -5)
        "Michaels" "Miss Applebaum…"
        "Michaels" "You too are under arrest on suspicion of the murder of your boss, Dwayne Jackson."
        "Michaels" "You do not have to say anything..."
        "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
        "Michaels" "Anything you do say may be given in evidence."
        show aletta normal
        "I've got to admit that I'm not sure how I was expecting Aletta to react."
        "Whether she would finally collapse once she was finally arrested."
        "Or if she'd tough it out and keep on playing the defiant accused."
        "But it's not long before I get my answer, as she simply raises an eyebrow."
        show aletta angry
        aletta.say "So that's how it's going to be, Detective?"
        aletta.say "Then I suppose I'm going to have to come along with you."
        aletta.say "But I'm not going to be answering any questions..."
        show aletta upset
        show camila upset
        "The statement is so emphatic and matter-of-fact that it seems to trigger Camila."
        "Right now she seems to be like a tensed spring, a vein actually standing out on her forehead."
        show camila angry
        camila.say "Oh, you won't, huh?"
        camila.say "Lady, I don't think you know how this works!"
        show camila upset
        show aletta normal
        "Aletta turns her gaze on Camila, staring the tough cop down."
        show aletta talkative
        aletta.say "You really do need to learn to keep a lid on that temper of yours, Detective."
        aletta.say "I was about to add - until I am provided with legal representation."
        show inspector at startle(0.1, -5)
        "Michaels" "Erm..."
        "Michaels" "Miss Applebaum does have that right."
        show aletta angry
        aletta.say "Oh, believe me, Detective Michaels..."
        aletta.say "I know my rights, and I'm through being pushed around by people in positions of power!"
        show aletta upset
        "Aletta holds out her hands as she says this, letting Camila cuff her."
        "She gives me a grudging nod as she seems to realise that we're in this together."
        "But a stern glance from the detectives makes me think trying to talk now would be a bed idea."
        hide aletta with dissolve
        show cherie normal at center, zoomAt(1.25, (940, 880)) with easeinright
        "By now Cherie has come hurrying out of her office to see what's going on."
        show cherie stuned
        "Part of me wants to see the looks on her so that I can judge her response."
        hide cherie
        hide camila
        hide inspector
        with dissolve
        "But Aletta and I already being led away as she makes it to my desk, and I can't look back."
        "So I guess that's the end of my story, at least as a free man."
        "Dwayne's dead and Cherie gets the company."
        "And as for Aletta and me, I suppose we get to take the blame for it all."
        "As well as a private cell in which to sit and dwell on where it all went wrong."
        $ renpy.full_restart()
    elif "hero" in suspects:

        $ arrest_reason = "the murder of Dwayne Jackson"
        $ hero_arrest_reason = arrest_reason
        "I can hear the sound of subdued voices spreading throughout the office."
        "And I know what the reason must be even before I raise my head from my work."
        "Because the truth is that I've been waiting for this moment to come."
        show inspector at center, zoomAt(1.0, (840, 720))
        show camila at center, zoomAt(1.0, (440, 720))
        with dissolve
        show inspector at center, traveling(1.25, 0.5, (840, 900))
        show camila at center, traveling(1.25, 0.5, (440, 880))
        "So when I see Detective Michaels and Camila walking towards me, it comes as no surprise."
        "And the fact that they have grim determination written all over their faces just proves it."
        "The game is finally up, as they're here to arrest me."
        "I make a point of standing and holding out my hands as they reach my desk."
        "Hoping that they'll understand it means that I'm going to come quietly."
        show inspector at startle(0.1, -5)
        "Michaels" "[hero.name] [hero.family_name]…"
        if hero.flags.police_trust >= 5:
            "Michaels" "I'd like to believe your story, I really would..."
            "Michaels" "But there are still too many unanswered questions."
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        elif hero.flags.police_trust <= -5:
            "Michaels" "Did you really think you could lie your way out of this?"
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        else:
            "Michaels" "You are under arrest on suspicion of [hero_arrest_reason]."
        "Michaels" "You do not have to say anything..."
        "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
        "Michaels" "Anything you do say may be given in evidence."
        "I keep my lips firmly closed all the time Michaels is reading me my rights."
        "And when he's done, the detective gives Camila a nod."
        "Then she steps forwards, pulling out her handcuffs and using them to bind my wrists."
        "But as she's doing so, we're close enough that nobody else can overhear us."
        show camila sadsmile
        camila.say "Don't worry, [hero.name], I know you were framed."
        camila.say "I'm going to do everything I can to prove it too."
        camila.say "As well as nailing the bastard that did this to you!"
        show camila sad
        mike.say "Thanks, Camila..."
        mike.say "With you on my side, I know I have a chance."
        if cherie.flags.dwaynedeath_truth:
            "Camila and I exchange a subtle nod."
            "And then we go back to pretending to be on opposite sides."
        elif cherie.flags.dwaynedeath_mikeselfdefense:
            show camila talkative
            camila.say "There's still time to change your story, [hero.name]."
            camila.say "I don't know why you're doing this, I really don't..."
            camila.say "You could be in jail for the rest of your life!"
            "All I can do is smile and shake my head at Camila's whispered pleas."
            "Knowing that she'd never understand the sacrifice that I'm making."
            "For her, life is about rules, everything is black and white."
            "But for me, it's become almost endless shades of grey."
        else:
            show camila angry
            camila.say "The evidence we've got on you is air-tight."
            camila.say "I can't believe I ever trusted a shit like you."
            camila.say "I hope they lock you up and throw away the key!"
            show camila upset
            "I could say something in response to that."
            "But what good would it do me?"
            "If Camila's telling the truth, of course she's going to hate me."
            "No, better to hold my tongue and try to hold onto a shred of my dignity."
        "By now Aletta and Cherie have hurried out of their offices to see what's going on."
        "Part of me wants to see the looks on their faces so that I can judge their response."
        if cherie.love > 100:
            show inspector at center, traveling(1.25, 0.3, (640, 900))
            show camila at center, traveling(1.25, 0.3, (340, 880))
            show cherie sad at center, zoomAt(1.25, (940, 880)) with easeinright
            "Cherie's face is a mask of grief and shock as she watches them lead me away."
            "And for a fleeting moment, her eyes meet mine, and I see a flash of something more."
            "A promise, perhaps? Or just the shared secret of what we've done?"
            show cherie cry
            cherie.say "[hero.name]! No!"
            show inspector
            "She starts to move toward me, but Detective Michaels blocks her path."
            "Her concern feels genuine, and it's the only thing that keeps me from breaking as they lead me out."
        else:
            show inspector at center, traveling(1.25, 0.3, (640, 900))
            show camila at center, traveling(1.25, 0.3, (340, 880))
            show cherie normal zorder 3 at center, zoomAt(1.25, (940, 880)) with easeinright
            "Cherie just stands there, watching with a cold, detached expression on her face."
            "Like she's already calculating how to move on without me."
            show aletta stuned zorder 2 at center, zoomAt(1.25, (1140, 880))
            "And Aletta looks just as stunned, her mouth hanging open as she watches the scene unfold."
        hide cherie
        hide aletta
        hide camila
        hide inspector
        with dissolve
        "But I'm already being led away as they make it to my desk, and I can't look back."
        "So I guess that's the end of my story, at least as a free man."
        "Dwayne's dead, Aletta's free of his tentacles and Cherie gets the company."
        "And as for me, I suppose I get to take the blame for it all."
        "As well as a private cell in which to sit and dwell on where it all went wrong."
        $ renpy.full_restart()
    elif "cherie" in suspects:

        "Everyone in the office seems to be doing the very best they can to pretend that everything's normal."
        "But there's a weird tension in the air, threatening to explode any moment and prove it's not business as usual."
        "Though my guess is that only Cherie, Aletta and me really know the true cause of it all."
        "So when I hear the sound of subdued voices spreading throughout the office."
        "And I know what the reason must be even before I raise my head from my work."
        "Because the truth is that I've been waiting for this moment to come."
        show inspector at center, zoomAt(1.0, (840, 720))
        show camila at center, zoomAt(1.0, (440, 720))
        with dissolve
        show inspector at center, traveling(1.25, 0.5, (840, 900))
        show camila at center, traveling(1.25, 0.5, (440, 880))
        "So when I see Detective Michaels and Camila walking towards the acting CEO's office, it comes as no surprise."
        "And the fact that they have grim determination written all over their faces just proves it."
        "The game is finally up, as they're here to arrest Cherie."
        "I just hope that all the work Aletta and I did to finger her for Dwayne's murder was enough."
        show inspector zorder 3 at center, traveling(1.25, 0.3, (640, 900))
        show camila at center, traveling(1.25, 0.3, (340, 880))
        show aletta normal at center, zoomAt(1.5, (940, 1040)) with easeinright
        "My fellow conspirator is already following on their heels, trying her best to look innocent as she does so."
        "And I fall in beside her, making sure to catch her eye before the detectives reach their destination."
        mike.say "Okay, Aletta..."
        mike.say "Just stick to the plan, okay?"
        show aletta talkative
        aletta.say "Yeah, yeah..."
        aletta.say "I'm not going to do anything to blow it, [hero.name]."
        hide aletta
        show bg door office private
        with dissolve
        "By now Michaels is standing in front of the doors to what used to be Dwayne's office."
        "His hand is balled into a fist and raised, ready to rap on the wood."
        "But before he can do so, the doors swing open and he's forced to take a step backwards."
        show cherie normal zorder 1 at center, zoomAt(1.0, (640, 720)) with dissolve
        show cherie at center, traveling(1.25, 0.5, (940, 900))
        show inspector zorder 3 at center, traveling(1.25, 0.5, (640, 900))
        show camila at center, traveling(1.25, 0.5, (340, 880))
        "Because Cherie comes sweeping out, looking every bit like a queen holding court."
        show cherie talkative
        cherie.say "What is all this?"
        cherie.say "Do you two have an appointment?"
        show camila annoyed
        "Camila seems to be more than little flustered by this show of defiance."
        show camila upset
        "Her cheeks flushing as she all but squares up to Cherie."
        show camila angry
        camila.say "An appointment?!?"
        camila.say "We're the police - we don't need no damn appointment!"
        show camila upset
        "Luckily for everyone involved, Michaels seems to be able to keep a cooler head than his colleague."
        "Because he simply pulls out his badge and waves it vaguely in front of Cherie's face."
        show inspector at startle(0.1, -5)
        "Michaels" "Missus Jackson…"
        "Michaels" "You are under arrest on suspicion of the murder of your husband, Dwayne Jackson."
        "Michaels" "You do not have to say anything..."
        "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
        "Michaels" "Anything you do say may be given in evidence."
        show cherie normal
        "I've got to admit that I'm not sure how I was expecting Cherie to react."
        "Whether she would finally collapse once she was finally arrested."
        "Or if she'd tough it out and keep on playing the dignified widow."
        "But it's not long before I get my answer, as she simply raises an eyebrow."
        show cherie talkative
        cherie.say "Is that so, Detective?"
        cherie.say "Then I will consent to come with you to the police station."
        cherie.say "But I must inform you that I will not be answering any questions..."
        show cherie amused
        show camila angry
        "The statement is so emphatic and matter-of-fact that it seems to trigger Camila."
        "Right now she seems to be like a tensed spring, a vein actually standing out on her forehead."
        show camila angry
        camila.say "Oh, you won't, huh?"
        camila.say "Lady, I don't think you know how this works!"
        show camila upset
        show cherie normal
        "Cherie turns her gaze on Camila, staring the younger woman down."
        show cherie talkative
        cherie.say "And you do not seem to understand basic manners, Detective."
        cherie.say "If you would have let me finish, I would have added - until my lawyer is present."
        show inspector at startle(0.1, -5)
        "Michaels" "Erm..."
        "Michaels" "Mrs Jackson does have that right."
        show cherie angry
        cherie.say "Oh, believe me, Detective Michaels..."
        cherie.say "I know my rights, and I know just who has betrayed me!"
        show cherie upset
        "Cherie holds out her hands as she says this, letting Camila cuff her."
        "But all the while she's looking straight at Aletta and me."
        "And as she's led away, I can already feel an uneasy sensation churning my stomach."
        hide cherie
        hide camila
        hide inspector
        with dissolve
        show aletta talkative at center, zoomAt(1.25, (940, 880)) with easeinright
        aletta.say "[hero.name]…"
        aletta.say "What did she mean by that?"
        show aletta surprised
        aletta.say "Does she know what we did?!?"
        show aletta sad
        "I shake my head, trying my best to reassure Aletta."
        mike.say "Don't worry about it, Aletta..."
        mike.say "She was just trying to intimidate us, that's all."
        mike.say "If there was any evidence against us, we'd have been in cuffs too."
        show aletta sadsmile
        "Aletta nods, but I can see that she's not totally convinced."
        "I'm going to need to keep a close eye on her in the days to come."
        "Which is a pain, because I'd rather focus my attention on consolidating my position around here."
        "Specifically getting myself into the role of CEO and making sure that I get control of the company."
        "At least that way something good will come out of the whole mess."
        hide aletta
        with dissolve
        $ cherie.set_gone_forever()
    elif "aletta" in suspects:

        "If I thought that having Dwayne's funeral out of the way would relieve the pressure on me, I was definitely mistaken."
        "Because, if anything, the attention that the whole thing's been getting is even more intense now."
        "The police seem to be crawling over the whole thing, interviewing everyone and scrutinising every last detail."
        "I've been doing all that I can to avoid them, keeping my head down and trying to keep a low profile."
        "But it doesn't seem like Aletta's been so lucky, judging by the text message that she just sent me."
        $ nvl_mode = "phone"
        nvl clear
        aletta_nvl "[hero.name], I need your help - RIGHT NOW!"
        "I find myself staring at my phone, worried at the tone of Aletta's message."
        "But at the same time I'm also concerned at how out of character it is for her."
        "Because I'm used to Aletta being the strong, confident type, never flustered by anything."
        "So I quickly compose a response, hoping to get to the root of the problem."
        mchero_nvl "Okay, Aletta - what's up?"
        mchero_nvl "You sound pretty tense!"
        "Aletta must be waiting on my response, as her next message arrives within mere seconds."
        aletta_nvl "Can't explain in a text-message - it's not safe!"
        aletta_nvl "Meet me as soon as you can, and I'll explain in person."
        $ nvl_mode = None
        scene bg street with dissolve
        "Aletta names the place and time for the meeting, and I hurry to be there."
        "All the while preparing myself for whatever might be eating at her so badly."
        "But when I get there, I see that Aletta's beaten me to it."
        show aletta annoyed at center, zoomAt(1.0, (940, 720)) with dissolve
        "And worse, she's pacing back and forth, arms crossed tightly over her chest."
        "Everything about her seems to be screaming tension and stress."
        mike.say "Ah..."
        mike.say "Aletta?"
        show aletta stuned
        "At the sound of my voice, Aletta almost leaps backwards."
        show aletta upset at center, traveling(1.5, 0.5, (640, 1040))
        "And as soon as she sees that it's me, she hurries straight over."
        show aletta angry
        aletta.say "Shhh!"
        show aletta whining
        aletta.say "Keep your voice down..."
        aletta.say "You never know who might be listening!"
        show aletta annoyed with vpunch
        "I find myself taking an automatic step backwards as Aletta comes closer."
        "Because now I can actually see the look in her eyes."
        show aletta upset
        "And it's one of paranoia, totally at odds with the Aletta that I've come to know."
        mike.say "Whoa..."
        mike.say "Calm down, Aletta..."
        mike.say "It's just me, come to meet you here, like you asked."
        mike.say "There's nobody here but the two of us, see?"
        "I turn around and gesture to our immediate surroundings, trying to show Aletta everything is fine."
        show aletta sad
        "But Aletta greets this with a shake of the head."
        show aletta whining
        aletta.say "But...but..."
        aletta.say "what if they have one of us bugged?!?"
        show aletta sad
        "The look on my face must be one of genuine surprise and concern."
        show aletta stuned
        "Because as soon as Aletta looks me in the eye again, her own expression changes."
        "The craziness seems to drain away, and she lets out a groan as she shake her head."
        show aletta angry
        aletta.say "Urgh..."
        show aletta talkative
        aletta.say "What am I saying?"
        aletta.say "Bugging us?"
        aletta.say "If I keep on like this, it'll be spying on us with space-lasers next!"
        show aletta normal
        "I nod and smile, thankful for the change in Aletta's tone and demeanour."
        "At least now she's starting to sound like we can have a sane conversation."
        mike.say "So..."
        mike.say "I'm going to go ahead and guess that this is on account of the investigation?"
        mike.say "That the police poking around is starting to get to you?"
        show aletta sadsmile
        "Aletta nods eagerly."
        show aletta whining
        aletta.say "That's it exactly, [hero.name]."
        aletta.say "I...I used to think that I was pretty unflappable, you know?"
        aletta.say "But they just keep on asking questions...so many questions."
        aletta.say "I'm sure they've asked me the same one more than once."
        aletta.say "And that I might have given them a different answer."
        show aletta sad
        mike.say "Yeah, they've done that to me too."
        show aletta whining
        aletta.say "But that's not the worst of it, [hero.name]..."
        aletta.say "What if...what if they actually find the murder weapon?!?"
        aletta.say "I'm scared that if they threaten me with prison, I might crack under the pressure!"
        show aletta sad
        "Aletta's moment of clarity and control seems to have passed."
        "And now she's returning to her previous state of anxiety, verging on panic."
        "So it looks like I'm going to have to do something to change that."
        menu:
            "Pull yourself together!":
                "I could try to tell Aletta that I'll fix everything for her."
                "That it's okay for her to be scared, as that's only natural."
                "But the truth is that need every ally that I can get right now."
                "And I don't have the time or strength to hold her up as well."
                mike.say "That doesn't sound like the woman that I've worked with for so long, Aletta."
                mike.say "Like the professional valkyrie that used to stride through the office on a Monday morning."
                show aletta stuned
                "Aletta looks up at me, and I can see genuine surprise in her eyes."
                show aletta surprised
                aletta.say "What..."
                aletta.say "What are you talking about, [hero.name]?"
                aletta.say "This isn't about the image I project in the office."
                aletta.say "This is about someone's life!"
                show aletta stuned
                "I furrow my brows and harden my stare."
                "Not willing to let Aletta wriggle out of what I'm saying that easily."
                mike.say "So all of your bravado was just an act?"
                mike.say "Is that what you're saying?"
                mike.say "Bullshit, Aletta - you're not that weak!"
                show aletta whining
                aletta.say "You...you don't mean that."
                aletta.say "You're just saying it to motivate me!"
                aletta.say "I've been to enough coaching seminars to know the technique."
                show aletta sad
                mike.say "Then you know that it bloody well works!"
                mike.say "Use all of that training to steel yourself, Aletta."
                mike.say "Use it to get through this, and then we're off the hook."
                "For a moment I think that Aletta's going to collapse in on herself all over again."
                show aletta upset
                "But then I see a hard expression set on her face, and she nods."
                show aletta angry
                aletta.say "Alright, [hero.name]..."
                aletta.say "I'll give it my best shot."
                show aletta upset
                "I nod in agreement, and then watch in silence as Aletta turns on her heel and walks away."
                hide aletta with easeoutright
                "I can't be one hundred percent sure that she's not putting on an act for my sake."
                "But right now I don't have time to worry about that kind of thing."
                "This is one less problem for me to deal with, and that's got to be a good thing."
                $ aletta.set_gone_forever()
            "Aletta... We're in this together":
                "Man, part of me is desperate to tell Aletta that I'm scared too."
                "But I guess someone's going to have to be the strong one here."
                "And from the state she's on right now, it'll have to be me."
                mike.say "You're feeling scared because you've been facing this on your own, Aletta."
                mike.say "And that's what the police are going to take advantage, it's what that want."
                mike.say "They're hoping you'll get so scared that you'll admit everything."
                show aletta sad
                "Aletta looks at me with her eyes the closest I think I've ever seen them to actual tears."
                show aletta whining
                aletta.say "I'm so close, [hero.name]..."
                aletta.say "So close to cracking!"
                show aletta sad
                mike.say "But they're wrong, Aletta..."
                mike.say "You're not alone in all of this."
                mike.say "What you're doing right now proves that - don't you see?"
                "Aletta's mood seems to lighten almost as soon as I ask the question."
                show aletta sadsmile
                "And I think that I can see the first glimmers of hope in her eyes."
                show aletta talkative
                aletta.say "You..."
                aletta.say "You mean..."
                show aletta normal
                mike.say "I mean that I'm here for you, Aletta..."
                mike.say "That whatever happens, we're in this together."
                mike.say "From now on, whenever you start to feel like this, I want you to call me."
                mike.say "No matter what time of day it is, even if it's in the middle of the night."
                mike.say "You call me, and I'll be there for you."
                "I'm smiling and nodding as I say all of this to Aletta."
                "And I'm expecting her to do the same in return."
                show aletta happy at center, traveling(1.75, 0.2, (640, 1200))
                "Which is why it takes me completely by surprise when she throws her arms around me instead!"
                "Luckily I manage to shake off my surprise and gently put my arms around her in response a moment later."
                show aletta talkative
                aletta.say "Oh god..."
                aletta.say "Thank you so much, [hero.name]..."
                aletta.say "I can't tell you how much I needed to hear you say that!"
                show aletta happy
                "The hug goes on for a short while longer, with me gently patttig Aletta on the back."
                show aletta normal at center, traveling(1.5, 0.5, (640, 1040))
                "And when it's finally over, she seems to have recovered a little of her normal reserve."
                show aletta talkative
                aletta.say "Erm..."
                aletta.say "Thanks again, [hero.name]..."
                aletta.say "But I don't think there's any need to tell Cherie about all of this."
                show aletta sadsmile
                mike.say "Oh no...of course not."
                mike.say "It'll be our little secret."
                show aletta normal at center, traveling(1.25, 0.5, (940, 880))
                "Aletta nods and then turns on her heel, walking away and leaving me alone again."
                hide aletta with easeoutright
                "Alone and hoping that I managed to do enough to shore up her defences for what lies ahead."
                if hero.money >= 5000:
                    "Moral support is important, but I fear it's not enough to help Aletta."
                    "The best I can do for her right now is to hire a competent lawyer."
                    $ hero.money -= 5000
                    $ game.flags.JudiciaryDelay = TemporaryFlag(1, 7)
                    $ aletta.hide()
                else:
                    $ aletta.set_gone_forever()
            "I'm terrified too":
                "Part of me feels like I should be reassuring Aletta right now."
                "That I should be the strong one and tell her I'll make everything okay."
                "But what about me?"
                "I'm caught up in this mess too!"
                mike.say "You think I don't know all of that, Aletta?"
                mike.say "Hell, I haven't slept a wink since..."
                mike.say "Well, since IT happened!"
                show aletta stuned
                "Aletta looks at me in genuine surprise."
                "Blinking and shaking her head as I begin to vent in front of her."
                show aletta whining
                aletta.say "Of...of course, [hero.name]..."
                aletta.say "I wasn't trying to suggest that you didn't."
                show aletta sad
                "But there's no way she can hope to stem the tide."
                "Not now that the damn holding back my emotions has been breached."
                mike.say "Fucking hell, Aletta..."
                mike.say "You're worried about what'll happen to you..."
                mike.say "Did you ever think what they'll do to me?!?"
                show aletta surprised
                "Aletta's still shaking her head at all of this."
                show aletta annoyed
                "But now she's looking around, like she's worried someone might overhear us."
                show aletta whining
                aletta.say "Okay, okay..."
                aletta.say "I get it now, [hero.name]..."
                aletta.say "You're worried too."
                aletta.say "But I don't think this is doing either of us any good."
                aletta.say "So let's both go and...and try to collect our thoughts, okay?"
                show aletta sad
                "I manage to nod in agreement, expecting Aletta to have more to say."
                show aletta sadsmile
                "But instead she nods, gives me a tense smile, and then hurries away."
                hide aletta with easeoutright
                "Leaving me to stand there, wrestling with my own fears and paranoia."
                $ aletta.set_gone_forever()
    else:

        "Everyone in the office seems to be doing the very best they can to pretend that everything's normal."
        "But there's a weird tension in the air, threatening to explode any moment and prove it's not business as usual."
        "Though my guess is that only Cherie, Aletta and me really know the true cause of it all."
        "So when I hear the sound of subdued voices spreading throughout the office."
        "And I know what the reason must be even before I raise my head from my work."
        "Because the truth is that I've been waiting for this moment to come."
        show inspector at center
        show camila normal at left
        with dissolve
        "So when I see Detective Michaels and Camila walking towards the acting CEO's office, it comes as no surprise."
        "And the fact that they have grim determination written all over their faces just proves it."
        "The game is finally up, as they're here to arrest Cherie."
        "Or maybe Aletta..."
        "Or me..."
        "Or all three of us!"
        "I almost leap up from my desk, trying to follow the detectives without making it too obvious."
        show aletta normal at right with easeinright
        "And I see that Aletta already out of her office, following on their heels."
        "Also trying her best to look innocent as she does so."
        "So I fall in beside her, making sure to catch her eye before the detectives reach their destination."
        mike.say "Okay, Aletta..."
        mike.say "Just stick to the plan, okay?"
        show aletta talkative
        aletta.say "Yeah, yeah..."
        aletta.say "I'm not going to do anything to blow it, [hero.name]."
        hide aletta
        with dissolve
        "By now Michaels is standing in front of the doors to what used to be Dwayne's office."
        "His hand is balled into a fist and raised, ready to rap on the wood."
        "But before he can do so, the doors swing open and he's forced to take a step backwards."
        show cherie normal at right with easeinright
        "Because Cherie comes sweeping out, looking every bit like a queen holding court."
        show cherie talkative
        cherie.say "What is all this?"
        cherie.say "Do you two have an appointment?"
        "I can't help wincing, like I'm bracing myself for the ugly scene that's about to unfold."
        "But then I find myself staring in amazement as Michaels's face breaks into a smile."
        "Michaels" "Oh..."
        "Michaels" "Hello there, Missus Johnson..."
        if hero.flags.police_trust >= 5:
            "Michaels" "I hope we're not disturbing you? We just had a few things to clear up."
        elif hero.flags.police_trust <= -5:
            "Michaels" "I'm sorry to disturb you, but your friend here hasn't been making things easy for us."
        else:
            "Michaels" "I hope we're not disturbing you?"
        show cherie surprised
        "Cherie looks from Michaels to Camila and back again, as if she can't quite process what he just said."
        show cherie talkative
        cherie.say "No, no..."
        cherie.say "Of course not, Detective."
        cherie.say "But I must ask - what are you doing here?"
        "Michaels is still grinning like a fool as Cherie asks the question."
        "And I can't help remembering that he's got some kind of old-man crush on her."
        "Though I'd have thought even he could put that aside in a serious situation like this."
        show camila annoyed
        "Luckily for everyone involved, Camila isn't as easily distracted by a pretty face."
        show camila talkative
        camila.say "This is just a brief visit, Madame..."
        camila.say "A courtesy call to inform you of a development in your husband's case."
        "At once I feel a surge of mixed emotions as Camila starts to explain their visit."
        "Anxiety at the mere mention of Dwayne, and hope at the tone of their voices."
        show cherie talkative
        cherie.say "Is that so?"
        cherie.say "Then you must tell me - what has developed?"
        "By now Michaels seems to have recovered some of his faculties."
        "Or else he's seen an opportunity to impress Cherie."
        "As he eagerly speaks up before Camila can say another word."
        "Michaels" "Oh yeah, that's it..."
        "Michaels" "We've looked into it from every angle possible."
        "Michaels" "Left no stone unturned, if you know what I mean?"
        show camila talkative
        camila.say "And we've had to conclude that there's no evidence that Mister Jackson is dead."
        camila.say "But there's no evidence to suggest that he's alive either."
        camila.say "So the official line is that he's...missing."
        "Michaels" "Unless he shows up again, you can have him declared dead too!"
        "I know that I should be standing back and letting the conversation play out."
        "But what Camila and Michaels are saying still sounds way too vague for my liking."
        "And I feel as though I need to hear something a lot more concrete to sooth my nerves."
        mike.say "Ah..."
        mike.say "Excuse me..."
        "As one, Cherie, Camila and Michaels all turn to look at me."
        "And in that instant, I feel myself become the centre of everyone's attention."
        mike.say "Okay..."
        mike.say "Hi, Detective Michaels..."
        mike.say "Hi, Detective Camila..."
        mike.say "[hero.name] here, just wanting to ask - does that mean it's, like, over?"
        mike.say "You know, is Dwayne's case closed?"
        mike.say "And if so, are we all cool?"
        "Michaels looks at me as if I have steaming turds hanging out of my mouth."
        show camila annoyed
        "And for her part, Camila gives me a glance that tells me she's not impressed."
        "As well as that the next time we meet in private, it's going to be...interesting."
        "Michaels" "Well, I wouldn't necessarily put it like that myself..."
        "Michaels" "But unless new evidence turns up, we're not pursuing this any further."
        show camila talkative
        camila.say "So yeah, [hero.name]…"
        camila.say "You, Miss Applebaum and Missus Jackson are off the hook - for now."
        "The detectives hang around the office a little longer after that."
        "I get the impression more because Michaels is looking for an excuse to chat to Cherie than anything else."
        "And so Camila is forced to stand there, reminding him that they have better things to do than just chat."
        hide cherie
        hide camila
        hide inspector
        with dissolve
        "For my part I feel like all I can manage to do is stagger back to my office and collapse into the chair behind my desk."
        "I feel like a massive weight has been lifted off my shoulders."
        "But oddly I don't feel elated at the news, at least not yet."
        "In fact I kind of feel like I'm going to need some time to process it all."
        "And for now, the best I can do is try to relax and let it all sink in."
    return

label aletta_judiciary:
    scene expression f"bg {game.room}"
    show aletta work normal at center, zoomAt(1.25, (340, 880)) with easeinleft
    "Aletta walks toward me."
    show aletta at center, traveling(1.5, 0.5, (640, 1040))
    "Last time I saw her was when the investigation about Dwayne's murder seems to target her."
    show aletta talkative
    aletta.say "[hero.name], I've excellent news. All charges against me were dropped. Thanks to my amazing lawyer."
    show aletta happy
    aletta.say "Or should I say thanks to you. I am really free now."
    hide aletta
    show aletta kiss
    with fade
    $ aletta.flags.kiss += 1
    "She plants her lips against mine and kisses me with a passion."
    "Taken completely by surprise, I'm helpless to resist."
    hide aletta
    show aletta work at center, zoomAt(1.25, (640, 880))
    with fade
    "Gasping and panting, Aletta breaks off the kiss."
    hide aletta with easeoutleft
    "And then she leaves, without a word."
    $ aletta.unhide()
    $ aletta.love += 10
    $ aletta.sub += 10
    return

label cherie_event_10:
    if cherie.love.max < 200:
        $ cherie.love.max = 200
    scene bg beach
    show cherie casual closed at center, zoomAt(1.0, (640, 740))
    with dissolve
    cherie.say "Are we there yet, mon ami?"
    mike.say "No...not quite yet, Cherie..."
    mike.say "Just a little further to go."
    cherie.say "And you are sure that I cannot open my eyes?"
    cherie.say "Because I am worried that I may trip and fall!"
    mike.say "Not far now, I promise..."
    mike.say "We're almost there."
    "I totally get what Cherie's saying, because I'm struggling along at her side."
    "But where she's impeded by my insisting she close her eyes, I'm hauling an awkward load."
    "Balancing it all on my back as I lead the way towards our ultimate destination."
    show cherie surprised
    cherie.say "Oh..."
    cherie.say "What is that?"
    cherie.say "Do I hear the sound of water?"
    cherie.say "Are those waves, [hero.name]?"
    "By now we're so close to where we need to be that, a mere few metres away."
    "So there doesn't seem to be any point in keeping it up any longer."
    mike.say "Okay, Cherie..."
    mike.say "You can open your eyes now."
    show cherie normal
    "I watch with more than a little trepidation as Cherie does just that."
    show cherie stuned
    "Noting the way that her eyes light up as she surveys the view from where we're standing."
    show cherie surprised
    cherie.say "The beach?"
    cherie.say "This is where we're going to be having our date?"
    show cherie normal
    "I spent a long time thinking about where to take Cherie today."
    "The choice was a big one, as this is our first date since everything worked out."
    "Since the whole business with Dwayne and the police got wrapped up so neatly."
    "So you could say that this is the beginning of a new era for us, a fresh start."
    "I considered a meal at a fancy restaurant, even going mad with an actual cruise."
    "But in the end I thought that a trip to the beach was more me, you know?"
    "Something that would help Cherie to tune into the kind of guy that I am."
    "And now I get to see if my choice was the right one."
    mike.say "Ta da!"
    mike.say "Surprise, Cherie - a day full of surf and sand."
    "I'm almost holding my breath as Cherie looks out over the beach."
    show cherie smile
    "And so it comes as a genuine relief when she smiles and nods her head."
    show cherie happy
    cherie.say "It has been so long since I came to a place like this."
    show cherie talkative
    cherie.say "When I was younger, we were always at the beach, you know?"
    show cherie whining
    cherie.say "But Dwayne...well, he did not have time for this kind of thing."
    cherie.say "All he wanted to do was work - that and chase other women!"
    show cherie sad
    "I can sense that Cherie's starting to dwell too much on the shitiness of her dead husband."
    "And so I make a point of stepping in and ushering her towards the golden sand before us."
    mike.say "Well he's one less jerk that we have to worry about now, right?"
    mike.say "Come on, Cherie - let's go grab one of the good spots on the sand."
    show cherie normal
    "I hand one of the lightest bags I'm carrying to Cherie, and then walk onto the sand."
    show cherie smile
    "She follows eagerly, the smile on her face only getting wider as we go."
    "Once we find a spot that meets with my approval, I throw down a rug."
    "And I make a point of fastidiously arranging everything according to my plan."
    show cherie amused
    "But as I fuss and fiddle, I hear the sound of Cherie chuckling to herself."
    "When I look up, I can see amusement in her eyes, but a genuine affection too."
    mike.say "Hey!"
    mike.say "What's so funny?"
    "Cherie shakes her head."
    show cherie happy
    cherie.say "Oh, mon ami…"
    cherie.say "Forgive me for laughing, I did not mean to offend you."
    show cherie talkative
    cherie.say "But you are so different to Dwayne, I cannot help it."
    show cherie normal
    "And I can't help frowning a little at the mention of Dwayne's name."
    "Because I was hoping that we could avoid talking about him today."
    mike.say "I'm sorry, Cherie..."
    mike.say "I know that I'm not as big, and buff and rich as he was..."
    mike.say "But I'd like to think that I make up for it in other ways."
    "Cherie nods as I try to explain myself."
    show cherie happy
    cherie.say "I mean precisely that, mon ami…"
    show cherie talkative
    cherie.say "Dwayne would never have brought me here and done all of this himself."
    cherie.say "He would have thrown his money around, buying everything and swaggering."
    cherie.say "He was not thoughtful and caring like you are."
    show cherie smile
    "Okay, so I'll admit it - that does kind of make me feel better."
    "And I begin to feel my resentment melting away."
    mike.say "Well you'd better strap yourself in, Cherie..."
    mike.say "Because you ain't seen nothing yet!"
    "I know that I just made it sound like I have a totally crazy day planned out."
    "But the truth is that we're going to be all the usual things you do at the beach."
    "Walking hand in hand over the sand, paddling in the sea, that kind of thing."
    "And the truth is that it seems to have been the right call on my part."
    "Because Cherie smiles and laughs through everything that we do together."
    "So much so in fact, that the time seems to just fly by."
    hide cherie with dissolve
    "And in what feels like the blink of an eye, the sun is starting to set."
    $ game.hour = 20
    scene bg beach night with dissolve
    "Leading Cherie back to where I spread our blanket, I gesture for her to sit down."
    "And then I set about arranging the picnic meal I brought along for the occasion."
    "Cherie watches me with genuine interest, making me feel the need to impress her."
    show cherie normal casual at center with dissolve
    mike.say "So..."
    mike.say "I guess Dwayne never put on a spread like this?"
    show cherie talkative
    cherie.say "Oh no, mon ami…"
    cherie.say "He would have burnt down the house trying to pour a bowl of cereal!"
    show cherie happy
    "We share a laugh at the idea of Dwayne's domestic ineptitude."
    show cherie normal
    "And then I hand Cherie a plate, signalling that we're ready to eat."
    "Again I feel a pang of concern as Cherie takes her first mouthful."
    "I mean, she does come from a country famous for the quality of its cuisine."
    "And the life that he lives as a wealthy woman means she's used to the finer things."
    "So it comes as a relief when she nods her head and goes back for a second helping."
    show cherie amused
    cherie.say "Mmm…"
    show cherie talkative
    cherie.say "Sometimes what one really needs are the simpler things in life."
    cherie.say "Wouldn't you agree?"
    show cherie normal
    "I frown and wrinkle my nose."
    mike.say "Wait a minute..."
    mike.say "Are you talking about the food, or me?"
    show cherie amused
    cherie.say "Hmm..."
    show cherie happy
    cherie.say "Maybe a little of both?"
    show cherie normal
    "Cherie reaches out and puts her hand atop mine as she says this."
    "The action showing the affection behind the comment she just made."
    "And I find myself taking her hand without a conscious thought."
    mike.say "Actually, Cherie..."
    mike.say "I don't care if you're talking about me or the food."
    mike.say "All that matters to me is that you're here, with me."
    show cherie closed at center, traveling(1.5, 0.3, (640, 1040))
    "Cherie leans in close and plants a kiss on my cheek."
    "And once she's done that, she doesn't pull away as much as a fraction of an inch."
    show cherie talkative
    cherie.say "You know that I never knew how I truly felt about Dwayne?"
    show cherie whining
    cherie.say "I always assumed that what I felt for him was love."
    show cherie talkative
    cherie.say "But as soon as I met you, became unsure."
    show cherie normal
    "I can feel my heart starting to beat faster as Cherie broaches the subject of love."
    "Part of me wants to urge her on, to see what else she has to say about it."
    "But another part of me wants to play it cool and let her get to the point naturally."
    mike.say "Why..."
    mike.say "Why is that?"
    show cherie talkative
    cherie.say "Because the first time chose to protect me, [hero.name]…"
    cherie.say "The first time you did that and proved that you would never simply use me..."
    show cherie happy
    cherie.say "When that happened, my heart almost burst with an emotion for you."
    show cherie talkative
    cherie.say "And I soon realised it was love, that it was very different to what I felt for Dwayne."
    show cherie normal
    mike.say "Oh wow..."
    mike.say "You just said that you loved me!"
    mike.say "I mean...I kind of assumed that you did..."
    mike.say "But it's pretty wild to hear you say it out loud like that!"
    show cherie happy
    cherie.say "Well, here is more proof of it..."
    hide cherie
    show cherie kiss casual
    with fade
    "Cherie plants her lips against mine, kissing me gently and yet with definite passion."
    "And for a moment I'm totally stunned, almost unable to believe all of this is happening to me."
    "But it doesn't take long for my instincts to takeover and for me to be swept along too."
    "So we kiss as the sun sets on the horizon, painting the sky with bands of pink."
    "The waves crash on the shore beside us, providing a natural soundtrack."
    "And in the back of my mind, I wish that this moment would never end."
    "Or at least that the memory of it will stay with me for a long time to come."
    scene bg black with dissolve
    $ hero.cancel_activity()
    $ game.active_date.abort = True
    $ game.room = "beach"
    return

label cherie_male_ending:

    if renpy.has_label("cherie_achievement_3") and not game.flags.cheat:
        call cherie_achievement_3 from _call_cherie_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church with dissolve
    "I've been so wired and worried for the past couple of days that I swear it's starting to affect my brain."
    "Like the whole of reality is beginning to feel like some kind of crazy hallucination that's freaking me out."
    "I've tried reasoning with myself, listening to self-help videos on the internet, even breathing exercises."
    "And the fact that I'm currently dressed up in what feels like the most uncomfortable suit ever made doesn't help."
    "Glancing around, I should be reassured by all of the familiar faces I can see sitting in the pews behind me."
    "Or that the chapel looks so nice now that it's been decorated and filled with all the guests that we invited."
    "But somehow all of it still seems unreal, like any moment it's going to turn into a lurid nightmare."
    "And just before the worst of it happens, I'll sit up in bed, bathed in sweat and gasping for breath."
    "I'm just about to try to pinch myself, just to make sure that I really am here and not asleep in my bedroom."
    "But that's the very moment that familiar music starts to play, filling the chapel and raising the mood."
    "Along with everyone else in the place, my eyes are drawn to the doors at the back of the building."
    "And when they swing open, I finally seem to snap out of it, realising that this all one hundred percent real."
    "Because that's when I set eyes on Cherie in her wedding dress for the very first time."
    show cherie wedding normal at center, zoomAt(1.0, (640, 720)) with dissolve
    "She insisted on keeping up the old tradition of the groom not seeing the bride in the dress before the ceremony."
    "And so when she sweeps into the chapel and comes down the aisle, the sight hits me like a slap in the face."
    "I should stress I mean that in a good way."
    "Because Cherie looks like a princess in that goddamn dress."
    "No, forget that - she looks like a total queen, surveying her kingdom!"
    "Or queendom?"
    "Okay, I don't know how that works..."
    "But the important thing is that my prospective wife-to-be is the hottest thing in the room right now."
    if cherie.is_visibly_pregnant:
        show cherie wedding normal
        "Hell, the dress is even cut to accommodate the size of Cherie's belly."
        "Which to me seems to be getting bigger with each passing day."
        "Reminding everyone that sees it of the future that we're planning together."
    else:
        show cherie wedding smile
        "I know that she's one of those elegant older women that always amazes."
        "Yet somehow the sight of her in that dress still manages to almost floor me."
        "Maybe because of what it represents and the commitment we're about to make."
    show cherie at center, traveling(1.5, 10.0, (640, 1040))
    "As Cherie gets closer, I see the heads of our colleagues turning to follow her progress too."
    "There's Aletta, finally starting to look like her old self again now that Dwayne's gone for good."
    "Lavish, taking the chance to dress to impress, and yet still not holding a candle to Cherie."
    "Audrey leaning back in her seat, no doubt looking around for someone to wrap around her little finger."
    "And, of course, there's Shiori, already blubbing into a handful of tissues as emotion gets the better of her."
    show wedding cherie with fade
    "Once Cherie finally reaches the altar, she gives me a look that seems to sum it all up."
    "There's eagerness and nerves in equal measure, as well as genuine excitement."
    "Priest" "Ahem..."
    "Priest" "Shall we begin?"
    show wedding cherie priest with dissolve
    "As one, Cherie and I turn to face the priest, just like we did in the rehearsal."
    "Only this time it's for real - we're actually getting married!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join together these two people..."
    "Priest" "In the bonds of holy matrimony."
    "The first part of the ceremony seems to just fly by, none of it really registering with me."
    "But as soon as we make it to the vows, all of that changes and the reality of it all hits me again."
    "Priest" "Do you, Cherie..."
    "Priest" "Take [hero.name]…"
    "Priest" "To be your lawful, wedded husband?"
    "Much to my relief, Cherie doesn't hesitate."
    cherie.say "Oui…"
    cherie.say "I do."
    "The priest nods, and then turns to face me."
    "Priest" "And do you, [hero.name]…"
    "Priest" "Take Cherie..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "YOU BET I DO!"
    mike.say "I...I mean...yes, I do."
    "I can see that the priest is smiling at my enthusiasm."
    "Even as he tries to keep things serious and formal."
    "Priest" "Yes, yes..."
    "Priest" "Very good."
    "Priest" "Now Cherie and [hero.name] have exchanged their vows before you..."
    "Priest" "It falls to me to ask that, if anyone here present..."
    "Priest" "Knows of any lawful reason that these two may not be married..."
    "Priest" "That you speak now, or forever hold your peace!"
    "As usual this formality gets a round of nervous laughter from the assembled guests."
    "But the truth is that I'm starting to sweat as the priest pauses for the usual couple of seconds."
    "The guests are most likely chuckling at the idea that Dwayne might come bursting into the chapel any moment."
    "Yet Cherie and I know for a fact that's not going to happen, as he's have to come back from the dead first."
    "No, we're more worried that Camila and Detective Michaels might kick those doors open and arrest the both of us."
    "Because some new piece of evidence might have come to light that ruins our story of Dwayne having simply disappeared."
    "Priest" "Good, good..."
    "Priest" "Now, where was I..."
    "Cherie and I exchange a relieved glance, both thankful the moment is passed."
    "Priest" "By the power vested in me..."
    "Priest" "It is my great pleasure to pronounce you man and wife."
    "Priest" "You may kiss the bride."
    show wedding cherie -priest with dissolve
    "It's not like we need to be told to do that."
    "Because the moment the priest is done talking, Cherie is in my arms."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show cherie kiss wedding at flip
    with fade
    $ cherie.flags.kiss += 1
    "And the very next second, her lips are pressed against mine!"
    "This mature, sophisticated woman is kissing me like a love-sick teenager."
    "And I'm not holding back either, returning the gesture with all my might."
    "We did it, we made it to the altar and tied the knot."
    "Cherie's my wife and I'm her husband."
    "And now the real adventure begins!"
    hide cherie with dissolve

    scene bg black
    show cherie ending
    with fade
    cherie.say "Ah, mon ami…"
    cherie.say "Where am I to begin with the story that you want me to tell?"
    cherie.say "I will not got all the way back to the beginning, because I do not think that will interest you."
    cherie.say "So instead I will begin where I honestly thought that my story had already come to an end."
    cherie.say "Or at least where I thought that there was nothing more to look forward to in my life."
    cherie.say "You see I was one of those girls raised to believe that a woman was not complete until she was married."
    cherie.say "And that those women who had truly won in life were the ones that married not for love, but for money!"
    cherie.say "Ah, when I met Dwayne, he seemed so different to all of the other men I had known before."
    cherie.say "He was a foreigner, brimming with confidence and firm in the belief there was nothing he could not do."
    cherie.say "How, I ask you, could I not have fallen for him?"
    cherie.say "I was seduced in the blink of an eye, and married before my head stopped spinning."
    cherie.say "And, for a while at least, I was sure that I was in love and perfectly happy."
    cherie.say "But with time I began to see that what my new husband truly loved was the things that he could possess."
    cherie.say "Things that were expensive, beautiful to look at and would inspire desire in those who laid eyes on them."
    cherie.say "Truly, Dwayne only valued them for the way that they reflected his own importance."
    cherie.say "The true value of things was lost on him, as he did not appreciate the subtle or the deep."
    cherie.say "Art was only worth the price he paid for it, property the way it made his contemporaries jealous."
    cherie.say "And his wife, only for the way that she inspired desire of a physical kind in other men."
    cherie.say "Yes, I had realised that I was merely one amongst Dwayne's glittering collection of possessions."
    cherie.say "But I told myself that I had every reason to be happy and grateful for the life he provided me."
    cherie.say "And when we had a daughter, raising her was a welcome distraction from my loveless marriage."
    cherie.say "By then I had become a cold person when it came to my relationship with my husband."
    cherie.say "Even when I discovered that he was seeing other women, I did not let it affect me."
    cherie.say "Instead I told myself that it was inevitable, that he would always seek out something new."
    cherie.say "Be it his tailored suits, his fast cars or the women with whom he chose to share his bed."
    cherie.say "Maybe you think that I should have done likewise?"
    cherie.say "That I should have indulged myself with lovers as he did?"
    cherie.say "Let me tell you that there was no shortage of offers over the years."
    cherie.say "But most of the men who moved in our social circle were just the same as Dwayne."
    cherie.say "To them I would only have been a conquest, another trophy to add to their collection."
    cherie.say "No, I had been used by one such man."
    cherie.say "I would not allow myself to be passed between a whole network of them."
    cherie.say "And that did not change until I happened to meet a man that seemed to be different."
    cherie.say "At first I was sure that [hero.name] would be just another in the vein of my husband."
    cherie.say "A shallow corporate climber who modelled himself on Dwayne and wanted to follow in his wake."
    cherie.say "But then something happened, something that made me sit up and pay attention."
    cherie.say "[hero.name] stood up for me and took my side against Dwayne."
    cherie.say "Of course I kept my distance still, as it could simply have been a ploy to win me over."
    cherie.say "Yet as I kept on watching him, it happened again and again."
    cherie.say "And each time I came a little closer to believing that [hero.name] was genuine."
    cherie.say "Eventually I could simply watch him no longer, and so I made overtures to him."
    cherie.say "The rest, as they say, is history."
    cherie.say "We became acquaintances, then friends and finally lovers."
    cherie.say "And oh, how ecstatic I was to find that my suspicions had been correct."
    cherie.say "Here was a man that looked at me and saw not a trophy, but a companion."
    cherie.say "I had always harboured suspicions that Dwayne's business dealings were not without corruption."
    cherie.say "And now that I had a confidant, decided that he might also become my conspirator too."
    cherie.say "Together [hero.name] and I laid our plans and put them into motion."
    cherie.say "But when Dwayne surprised us, I was sure that one or both of us would die."
    cherie.say "I watched helplessly as Dwayne beat [hero.name], and felt like I was dying along with him."
    cherie.say "Honestly, I believe that, if Aletta had not stepped in when she did, I would have been the one to finish Dwayne."
    cherie.say "But fate decreed that the responsibility was not to be mine."
    cherie.say "And for a while I thought that the crime would damn all three of us."
    cherie.say "That we would be made to pay for ridding the world of such a vile man."
    cherie.say "So the relief that came when the police concluded he had simply vanished..."
    cherie.say "Mon dieu...I cannot describe it!"
    cherie.say "Not only was I free of the man who had kept me in a gilded cage..."
    cherie.say "But also I was free to love the man who had thrown open its door!"
    cherie.say "Now the company that Dwayne built belongs to us, and we run it together."
    cherie.say "[hero.name] and I, we are...how do you say...a power-couple?"
    cherie.say "But we make sure that our company is ethical and a power for good."
    if cherie.is_visibly_pregnant or cherie.flags.mikeBabies >= 1:
        cherie.say "But soon I think that we will take a step back from running things."
        cherie.say "Put Aletta and Cassidy in place as vice-presidents of the company."
        cherie.say "Then [hero.name] and I will devote ourselves to being parents."
        cherie.say "So we can make sure that little Francois grows up be just like his father."
        cherie.say "And not at all like that of his older half-sister!"
    else:
        cherie.say "But soon I think that we will take a step back from running things."
        cherie.say "Put Aletta and Cassidy in place as vice-presidents of the company."
        cherie.say "Then [hero.name] and I will devote ourselves to creating something more important."
        cherie.say "A legacy that will endure far longer than that of the company."
        cherie.say "One that only the two of us can create when we come together."
    cherie.say "So you could say that once I thought that I had it all."
    cherie.say "But I was shown in a harsh way that I was totally wrong."
    cherie.say "Yet now, after almost losing everything, I feel like I really do have it all."
    cherie.say "Because, in the end, it is not money or status that makes a person truly rich."
    cherie.say "That is something that only true love can bestow."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not cherie.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_24
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_24
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label cherie_sub_event_01:
    if cherie.sub.max < 50:
        $ cherie.sub.max = 50
    "It's been one of those days at the office when all I really remember is sitting down and starting to work."
    "After that the passage of time just seems to escape me, as I keep looking up and realising that long hours have passed."
    "But I swear that I just glanced down at my work five minutes after I got here, it's that much of a blur."
    "In fact there are times when I have to try really hard to remember what day it is and whether I made it home last night."
    "Or if I just kept on working right through the night, fuelled by coffee and sheer desperation."
    "The only other people that I seem to see are the girls that work alongside me in the office."
    "Hearing the sound of the door opening and glancing up to see Aletta, Audrey, Lavish or Shiori walk in."
    "Then the inevitable groan as I see that their arms are full of yet another pile of files for me to work through."
    "I mean seriously, who'd have thought that bumping your boss off could have generated so much paperwork?!?"
    "So when I hear the sound of the door open again, I don't even bother to look up."
    "I just point to part of my desk that's got the fewest teetering piles of files on it."
    mike.say "Just drop them right there, okay?"
    mike.say "And if there's not enough space..."
    mike.say "I dunno, maybe drop them on the floor?"
    cherie.say "Just what do you mean by that, mon ami?"
    show cherie work talkative at center, zoomAt(1.0, (340, 730)) with vpunch
    cherie.say "What exactly are you expecting me to drop?"
    cherie.say "My very expensive, French designer panties, perhaps?"
    show cherie normal
    "As soon as I recognise who the voice belongs to, my head snaps up from my desk."
    "And all whatever I was engrossed in the moment before becomes suddenly meaningless to me."
    "Because that's just the kind of effect that Cherie's presence has on me."
    "Not just on account of the fact that we're co-conspirators when it comes to Dwayne's fate either."
    "Since we started to become closer, she's begun to have that kind of a hold on me, to command all of my attention."
    "But even though she just walked in here gently joking with me, I can see that there's more going on with her."
    show cherie sadsmile
    "Cherie looks more strained and stressed than usual, like things are really getting to her."
    "And I get the feeling that she's been putting on a brave face in front of everyone else at the office."
    "But now that we're alone, it's finally starting to slip."
    mike.say "Sorry, Cherie..."
    mike.say "I haven't stopped to catch my breath all day."
    mike.say "But I don't need to tell you how much work we all have on, do I?"
    mike.say "And I know that you're probably shouldering more of the burden than me..."
    show cherie amused
    "Cherie waves a hand vaguely in my direction, cutting me off."
    show cherie talkative
    cherie.say "There is no need to talk to me like that, [hero.name]…"
    cherie.say "To flatter me and tell me how well I am doing."
    cherie.say "You and me, we are far beyond that."
    cherie.say "No, I came here because we can talk to each other as equals."
    show cherie normal
    mike.say "Okay, Cherie..."
    mike.say "Sounds like you want to get something off your chest?"
    play sound door_close
    show cherie at center, traveling(1.25, 1.0, (440, 880))
    "Cherie nods and closes the door behind her."
    "Which pretty much confirms that what she's about to say is for my ears only."
    show cherie talkative
    cherie.say "Oh, mon ami…"
    cherie.say "I was so sure that I knew what taking the reins would require of me."
    cherie.say "That I had learned enough from watching Dwayne to be able to take his place."
    show cherie whining
    cherie.say "But now, I am not so sure..."
    cherie.say "And all the time I feel like he is still watching me, mocking me from beyond the grave!"
    show cherie sad
    "I'm watching Cherie all the time that she's talking."
    "Noting with interest the look on her face and the way she's holding herself."
    "And I can see just how close she actually is to losing her nerve."
    "That her normally unassailable control is in danger of being lost."
    mike.say "That's understandable, Cherie..."
    mike.say "You wanted to escape Dwayne's control, and you achieved that goal."
    mike.say "But I think the problem is you really wanted to escape the man, not the control."
    show cherie annoyed
    "I see Cherie's brows furrow as she listens to what I have to say."
    "As if the idea isn't one that she's considered before now."
    show cherie talkative
    cherie.say "What are you trying to say, mon ami?"
    cherie.say "That I really want to be controlled by another?"
    show cherie normal
    "Okay, I can hear the subtle challenge in Cherie's voice as she asks the question."
    "Which means that it's time for me to put my money where my mouth is."
    mike.say "Let me show you what I mean, Cherie."
    mike.say "Now, lock the door so we're not disturbed."
    mike.say "Then come over here and kneel down in front of me."
    "I make sure to keep my tone even and the instructions simple."
    "Uttering them in a manner that makes it clear they're commands, and not requests."
    "Then I wait, as a tense moment passes, in which Cherie remains perfectly still."
    "At the same time I stay silent, looking her straight in the eye."
    "And I feel that it could go either way in that instant."
    show cherie at center, traveling(1.0, 0.5, (240, 730))
    "But then Cherie breaks eye-contact, and she turns around."
    play sound door_lock
    "Then I hear the sound of my office door locking, and I know that I've won."
    show cherie at center, traveling(1.5, 1.0, (640, 1040))
    "Cherie turns back to face me, then walks slowly to the spot I indicated."
    show cherie at center, traveling(1.5, 1.0, (640, 1220))
    "And I watch as she gets down and kneels in front of me, looking up."
    show cherie talkative
    cherie.say "Okay, mon ami…"
    cherie.say "What would you have me do next?"
    show cherie normal
    mike.say "Nothing hard, Cherie..."
    mike.say "Just to admit that you need this release..."
    mike.say "That you need to surrender yourself to me."
    "I reach out with one hand, cupping Cherie's chin in my palm."
    "Almost as soon as I do so, a shiver runs through her body."
    "Going from head to foot, it's like my touch wakes something inside her."
    "And Cherie lets out a moan that has an almost sexual quality to it."
    show cherie flirt
    cherie.say "Mmmh…"
    show cherie whining blush
    cherie.say "I...I cannot resist any longer, mon ami..."
    cherie.say "I must confess to you!"
    show cherie flirt
    "I make sure to nod my head, encouraging Cherie to say more."
    "But at the same time I make sure to keep quiet myself."
    "Not wanting to influence what she's about to tell me."
    show cherie talkative
    cherie.say "That is why I married dwayne - not for love, or even for his money..."
    cherie.say "Because I thought that he could protect me and give me purpose."
    show cherie whining
    cherie.say "But I soon found that, for all his intelligence, he was just a brute!"
    show cherie happy
    cherie.say "Not like you, mon ami..."
    cherie.say "In you, I believe I have found all that I have ever desired!"
    show cherie flirt
    "I gently tilt Cherie's chin upwards, making her gasp."
    mike.say "You can have exactly that, Cherie..."
    mike.say "I will give you protection, purpose...and love."
    mike.say "But only if you willingly surrender yourself to me."
    mike.say "Yield to me in everything, that is what I want in return."
    "Cherie looks at me with an innocence and helplessness I've never seen in her before."
    "As if all the layers of her commanding persona have been stripped away."
    "And what I'm seeing is the vulnerable core of her being beneath."
    show cherie talkative
    cherie.say "Please, [hero.name]..."
    cherie.say "That is what I want!"
    cherie.say "Please, show me how to let go?"
    show cherie flirt
    "I nod my head, acknowledging the pledge that Cherie is making."
    hide cherie
    show cherie kiss
    with fade
    "And then I lean in closer, placing my lips gently against hers."
    "The kiss that follows serving as a gesture to seal the deal."
    "Cherie quivering and quaking as long as it continues."
    "And the end only coming when I decide that it's gone on long enough."
    $ cherie.flags.cheriedelay = TemporaryFlag(True, 1)
    scene bg black with dissolve
    pause 0.3
    return

label cherie_sub_event_02:
    if cherie.sub.max < 75:
        $ cherie.sub.max = 75
    scene bg mansionentrance with fade
    "I feel like I'm getting more used to visiting the huge pile that used to belong to Dwayne now that he's gone."
    "When he was here, his larger-than-life personality kind of managed to fill the huge place up pretty well."
    scene bg mansion with fade
    "But now the house feels bigger than it did before, and I'm more aware of the echoes and dark corners in the place."
    "That and the fact the only real source of light and warmth in the whole place is Cherie herself."
    "Seriously, I could swear that the rooms are chilly and cold, until she walks in and I feel things heat up."
    "Today Cherie greets me with her usual elegant smile and sophisticated manner, every inch the perfect host."
    show cherie happy at center, zoomAt(1.25, (640, 880)) with easeinleft
    cherie.say "Bonjour, mon ami…"
    cherie.say "It is so good to see you out of the office."
    cherie.say "I am beginning to feel like we are both spending our entire lives there!"
    show cherie normal
    mike.say "Boy, Cherie..."
    mike.say "I know what you mean."
    mike.say "I feel asleep at my desk yesterday..."
    mike.say "And when I woke up, it was today!"
    show cherie smile
    "Cherie chuckles and shakes her head, gesturing for me to follow her."
    show cherie talkative
    cherie.say "Oh dear!"
    cherie.say "This simply will not do."
    cherie.say "Come, let me find something to reinvigorate you."
    show cherie normal
    "I nod eagerly and then fall in beside Cherie as she leads me deeper into the house."
    "She's all smiles and pleasantries until we make it to one of the inner rooms."
    show cherie sadsmile at center, traveling (1.25, 1.0, (240, 880))
    "But as soon as she closes the doors behind us, the mask she's been wearing slips."
    "I can't help being worried as Cherie's shoulders seem to sag, like she's carrying the weight of the world."
    "And the amiable expression on her face is replaced with one that tells of deep and enduring exhaustion."
    "In fact the transformation is so sudden and complete that I'm worried she's having an attack of some kind."
    mike.say "Cherie..."
    mike.say "Are you okay?"
    mike.say "Do you need me to get you some help?"
    show cherie normal at center, traveling (1.25, 0.5, (440, 880))
    "Cherie waves away my concerns, shaking her head as she collects herself."
    show cherie talkative
    cherie.say "No, no, no..."
    cherie.say "I am grateful for your attention, mon ami…"
    cherie.say "But it is just the strain of everything, you know?"
    cherie.say "We have had to become the leadership of the company almost overnight."
    cherie.say "And at the same time we are still reeling from my husbands...disappearance."
    show cherie sadsmile at center, traveling (1.5, 1.0, (600, 1040))
    "Cherie places an understandable emphasis on he word 'disappearance'."
    "Making a point that's not lost on me and helps me to understand her predicament."
    "I nod my head as Cherie fixes us both a drink, my mind quietly racing."
    show cherie at center, traveling (1.5, 1.0, (640, 1200))
    "Then she hands one of the glasses to me and flops down into the nearest chair."
    mike.say "Cherie..."
    mike.say "You remember when you came to me in my office the other day?"
    mike.say "Remember how you...unburdened yourself to me?"
    show cherie normal
    "Cherie's taking a sip of her drink as I ask the question."
    "And I see her eyebrows rise as it stirs her memory of the event."
    show cherie talkative
    cherie.say "Oh, mon ami…"
    cherie.say "How could I ever forget?"
    show cherie normal
    mike.say "Well..."
    mike.say "Do you think doing it again would help?"
    show cherie sadsmile
    "Cherie gives me a helpless smile."
    show cherie whining
    cherie.say "Alas, mon ami…"
    cherie.say "This time I have been embroiled in boardroom battles."
    cherie.say "Fighting a veritable war behind closed doors."
    cherie.say "And if the conflict has escalated, then I fear your response must too!"
    show cherie sad
    "I nod as I take a long, thoughtful sip of my drink."
    "Thinking that Cherie's basically telling me that her stress has upped the stakes."
    "So I'm going to have to do the same thing if I want to be able to make a difference."
    "And that's when my eyes settle on the silk scarf that Cherie's wearing around her neck."
    "Without asking her permission, I reach out and take hold of the soft material."
    "Unwinding it as I do so and slipping it through my fingers."
    mike.say "That's the only bit of help that you're going to get from me."
    mike.say "So you'd better get moving and take off the rest yourself."
    mike.say "Because I can't inspect you properly with your clothes on."
    show cherie stuned
    "Cherie's eyes go wide with surprise as I issue the command, and she doesn't move a muscle."
    "I don't know if it's simply because I gave her an order out of the blue with no preamble."
    "Or on account of the fact that I'm deliberately stepping things up this time around."
    "But either way, the hesitation isn't something that I want to encourage from her."
    mike.say "You're not in the boardroom anymore, Cherie..."
    mike.say "Or did you just go and forget that I'm the one in charge here?"
    mike.say "The one that ordered you to strip and present yourself for inspection?"
    "I must have managed to pitch the tone of my voice just right when I spoke."
    "Because the effect that my demands have on Cherie is visible and instant."
    show cherie normal at center, traveling (1.25, 1.0, (600, 880))
    "She puts down her drink and stands up, already unbuttoning her blouse."
    "And it's not like she hurries to obey me either, making a show out of it."
    "Which means that I have to do the best I can to keep on looking stern and in control."
    "All the while wanting to openly applaud the sight of Cherie's body being revealed before me."
    "Soon she's shouldering her way out of that blouse and shrugging it off."
    "Meaning that I'm treated to the sight of her naked to the waist save for her bra."
    "Next Cherie unfastens her skirt, peeling it away to reveal her legs."
    show cherie underwear with dissolve
    "And yes, there's panties and stockings under there too!"
    "Putting one leg up onto the chair, she slides the nylons off one leg."
    "Then she repeats the exact same series of motions with the other."
    "Yet somehow it seems even more thrilling to watch the second time around."
    "Putting her hands behind her back, Cherie deftly unhooks her bra."
    "This frees her breasts to move naturally and in sympathy to the motions of her body."
    "And it's hard to tear my eyes away from them when she then pulls down her panties."
    "Cherie stands before me, naked and motionless, just looking me in the eye."
    "And the sight is so overwhelming that it takes me a moment to remember what's going on here."
    "To be reminded that she's waiting patiently for me to tell her what to do next."
    mike.say "Sit down, Cherie."
    show cherie at center, traveling (1.5, 1.0, (640, 1200))
    "Cherie moves to obey the simple command as soon as it's spoken."
    "She places her arms on those of the chair and her feet flat on the floor."
    "Almost as if she has a suspicion as to what I'm going to do next."
    mike.say "Is there another of these?"
    "I hold up the silk scarf for Cherie to see as I ask the question."
    "And by way of an answer, she nods towards a nearby bureau."
    "Pulling open the first drawer I find, I pull out a second scarf."
    "Then I use both to bind Cherie's wrists to the arms of the chair."
    "Okay, I'll admit that I'm no boy-scout when it comes to tying knots."
    "But the point of the exercise isn't really to keep Cherie from escaping."
    "The bindings are more symbolic, her not breaking them being the point."
    "Once the task is complete, I stand back and inspect my handiwork."
    "Enjoying the way that Cherie keeps on looking up at me from the chair."
    "Then almost turning her gaze away whenever I meet her eye."
    "As if she wants to have my eyes all over her now that she restrained and exposed."
    "But the realisation that it means total submission is still embarrassing her."
    "Which of course means that I keep on looking her over."
    show cherie a naked with dissolve
    pause 0.3
    show cherie a at top_to_bottom
    "My gaze travelling up and down her naked body as she struggles and twitches."
    "Sure, I could put my hands anywhere I wanted right now, totally go to town on it."
    "But I can feel the tension building from Cherie's anticipation of that."
    show cherie at bottom_to_top
    "And to do so would instantly defuse the pressure that's growing between us."
    "So instead I decide to interrogate her verbally."
    mike.say "Tell me how it feels, Cherie..."
    mike.say "Tell me what being stripped and bound does to you."
    mike.say "Before you came home, you were battling it out in the boardroom."
    mike.say "Now you're naked and tied down, totally powerless."
    "My eyes are on Cherie's chest as I say all of this."
    "Focussed on her nipples and watching as they get ever harder."
    "She has her thighs pressed tightly together at the same time."
    "And I can only imagine what must be happening to her pussy right now."
    show cherie talkative
    cherie.say "I..."
    cherie.say "I feel free..."
    cherie.say "Freed from all of my burdens!"
    show cherie flirt
    "Cherie's words are breathy, almost coming in desperate gasps."
    "And I can see her struggling weakly against the scarves around her wrists."
    mike.say "You like this, don't you?"
    mike.say "You'd never admit as much to anyone else."
    mike.say "But you crave being dominated and commanded."
    "I say the last as a statement and not a question."
    "And by now Cherie seems to be quivering in her seat."
    "Her entire body shaking like she's being overcome."
    "Then she throws her head back, gasping in a pretty dramatic fashion."
    "If I didn't know better, I'd have sworn that she was having an orgasm."
    "But then maybe this is the mental and emotional equivalent of that?"
    "Whatever the cause, Cherie lets out a deep moan and her head sags forwards."
    "Which I take as an appropriate cue to untie the knots at her wrists."
    "Before I can do anything about it, Cherie slumps out of the chair."
    "And then she slides onto the floor, ending up on all fours."
    show cherie talkative
    cherie.say "Thank you, mon ami…"
    cherie.say "Your commanding me..."
    cherie.say "It...it unburdens my soul!"
    show cherie normal
    "I can sense the emotion in Cherie's words, feel how deeply this has affected her."
    "And I do the best I can to process what it means, the power it grants me."
    "Not only that, but how I should make use of it."
    $ cherie.sub += 5
    $ cherie.love += 2
    scene bg black with dissolve
    return

label cherie_sub_event_03:
    if cherie.sub.max < 100:
        $ cherie.sub.max = 100
    scene expression f"bg {game.room}" with dissolve
    "I'm usually in my office and chained to my desk at work."
    "Or else I'm hurrying from one place to another in the building."
    scene bg office with dissolve
    "And today it seems to be the latter, as I stride down the corridor."
    "Doing that thing where you try to walk as fast as possible without breaking into an actual run."
    "As if the change in pace would be an admission that you were losing control and freaking out."
    scene bg door office private2 with dissolve
    "But if I had actually been running, then I doubt I'd have heard the sounds coming from the boardroom."
    "What seems to be someone crying out in anger and frustration, and something crashing to the floor."
    "Stopping in my tracks, I slide over to the doors, which luckily are ajar right now."
    "So I can risk a look inside without having to commit to opening them and alerting whoever's in there."
    "But as soon as my eye peers through the crack, all need for stealth and secrecy disappears in an instant."
    scene bg black
    show shiori_stretch_bg
    show cherie c work closed at center, zoomAt(1.25, (440, 900))
    show black as doorleft at center, zoomAt(1, (-200, 720))
    show black as doorright at center, zoomAt(1, (1440, 720))
    with fade
    "Because now I can see that the person inside the boardroom is Cherie, and she's looking pretty distressed."
    show cherie c at center, traveling(1.25, 1.0, (640, 900))
    "She's propping herself up on the edge of the table with both hands, head down so that her hair covers her face."
    "And now I can see that there's a pile of papers on the floor at her feet too."
    "So I guess she just swiped a bunch of files off the table in a moment of emotional outburst."
    "I'm still hovering on the edge of pushing open the door or walking quietly away."
    "Trying to judge if Cherie's in the mood where she needs support or would be best left alone."
    "That's why I'm still standing there when she suddenly raises her head."
    show cherie b stuned
    "And, of course, she then looks me straight in the eye."
    show cherie b surprised
    cherie.say "Who is there?"
    cherie.say "Who is spying on me?!?"
    show cherie b annoyed
    "There doesn't seem to be any sense in even thinking of running away."
    show black as doorleft at center, zoomAt(1, (-700, 720))
    show black as doorright at center, zoomAt(1, (2000, 720))
    with ease
    "And so I push the doors open, hoping the sight of me will calm Cherie down."
    mike.say "It's only me, Cherie..."
    mike.say "And for the record, I wasn't spying on you."
    mike.say "I heard a sound and I was worried, that's all."
    show cherie a normal
    "Luckily for me, my prediction about Cherie's reaction seems to be correct."
    "Her expression softens almost as soon as she sees that it's me behind the doors."
    "And I notice that she makes an effort to straighten herself up too."
    show cherie happy
    cherie.say "Ah..."
    cherie.say "I am sorry, mon ami…"
    cherie.say "These days, it seems that I am always in a tumult of emotion!"
    cherie.say "On the one side I have the jackals of business, snapping at my heels."
    cherie.say "And on the other, the dogs of the police, sniffing for clues."
    show cherie normal
    "I nod without saying a word, totally aware of the position Cherie's in."
    "Because the truth is that I'm in a similar one myself, and bound to her."
    "But this isn't the first time that I've seen her in a state recently."
    "And there's been a certain way of handling the fallout developing between us."
    "One that I think has grown to the point where I can apply it when the situation demands."
    mike.say "I think the time has come for a takeover, Cherie."
    mike.say "An aggressive corporate takeover at the very top of this company."
    show cherie surprised
    cherie.say "A takeover?"
    cherie.say "Mon ami…"
    cherie.say "Whatever can you mean?!?"
    show cherie stuned
    pause 0.5
    play sound door_close
    "By way of an answer, I turn my back on Cherie long enough to close the doors behind me."
    play sound door_lock
    "And I make a point of locking them in a manner that means she can hear it too."
    "Then I turn around and pull something out of my pocket."
    show cherie whining
    cherie.say "You?"
    cherie.say "You are telling me that you are the one taking over the company?"
    show cherie sadsmile
    "I shake my head as I start to walk towards Cherie."
    "And she's standing at the head of the table, the length of the room away."
    "So that means I can get at least a little bit of drama out of my approach."
    mike.say "You misunderstand me, Cherie..."
    mike.say "I'm not talking about a takeover of the company."
    mike.say "I'm talking about a takeover of the acting CEO."
    show cherie blush
    "Cherie's eyes go wide as she realises the implications of what I'm saying."
    "And she takes a step behind the chair at the head of the table."
    "As of it's going to keep me from being able to reach her."
    show cherie surprised
    cherie.say "A takeover of...of me?"
    cherie.say "But how...how would such a thing even be possible?"
    show cherie stuned
    "I take that as my cue to hold up the box in my hand and open the lid."
    show cherie blush
    "And the moment that Cherie sees what's inside, she nods her head."
    "Letting me know that she's now on exactly the same page as me."
    "Because inside the box is a stylish, discreet necklace."
    "Exactly the kind of thing that a sophisticated female executive might wear."
    "Only this one has been subtly made to resemble a collar or choker."
    "Meaning that it secretly signifies the submission of the wearer."
    mike.say "You wear this as a symbol, Cherie..."
    mike.say "An outward declaration that you belong to me."
    mike.say "That you're my...my corporate sub."
    mike.say "You might be the one in the spotlight, heading up the meetings and signing the contracts."
    mike.say "But as soon as you put this on, I'll be the one pulling your strings from the shadows."
    "I leave it there, silently waiting to see what Cherie's response will be."
    "Because sure, she's seemed to love all of the ways I've subtly dominated her in the past."
    "But this is different, an open declaration of her being submissive to my will."
    "And once she commits to something like that, things will never be the same again."
    show cherie happy
    cherie.say "Yes, mon ami…"
    cherie.say "You must put this around my neck, and quickly!"
    cherie.say "I do not desire to be alone anymore - I want to be yours."
    cherie.say "To be steered by your strong and masterful hand."
    show cherie blush
    "I can feel my heart starting to race as Cherie gives in to my demands."
    "And it's a battle for me to keep my face straight as I take the necklace out of the box."
    "Cherie obligingly lifts her hair and waits patiently as I hook it around her neck."
    show cherie collar
    "And once it's in place, she lets it drop again, shaking her head and shoulders."
    "I know that all she's really doing is straightening herself up out of habit."
    "But to me it looks as though she's experimenting with the weight of the necklace."
    "Coming to terms with the limits and restraints of the new role that she's accepted."
    mike.say "So, Cherie..."
    mike.say "How does it feel?"
    show cherie happy
    cherie.say "It does not feel like I have been chained or collared."
    cherie.say "Instead it feels as though I have been liberated, mon ami…"
    show cherie sadsmile
    "Cherie pauses, as though she realises that she's said something wrong."
    show cherie happy
    cherie.say "Oh..."
    cherie.say "I mean to say Master!"
    cherie.say "You are my CEO now, Master - you own every single part of me."
    show cherie normal
    "I nod, still doing all that I can to contain my growing feeling of excitement."
    "Wanting to punch the air and cheer out loud, because Cherie's giving herself to me."
    mike.say "Not quite yet, Cherie."
    mike.say "The wearing of the necklace, that's like the drafting of the contract."
    mike.say "We still need to carry out the act that takes the place of signing it."
    "I'm about to start dropping what I hope are subtle hints."
    "Guiding Cherie towards what I want her to do for me next."
    "But it seems like she's more tuned in to what I want than expected."
    "Because with just one brief nod, Cherie shoulders out of her jacket."
    "Then she kicks off her shoes and begins to un button her blouse too."
    "Glad that I already locked the doors, I watch with growing fascination."
    "And yeah, obviously with a fast growing cock as well!"
    "Cherie takes off her blouse and then unfastens her skirt."
    show cherie underwear with dissolve
    "Which leaves her standing before me in nothing more than her underwear."
    "And do I really need to explain that Cherie wear the most exquisite, French underwear?"
    "Of course everything is perfectly matched and accentuates her body impossibly well."
    show cherie naked with dissolve
    "So much so that it's almost a shame to see her unhook her bra and pull down her panties."
    "But then there's nothing more stirring than the sight of Cherie completely naked!"
    show cherie happy
    cherie.say "I am ready, Master..."
    cherie.say "Where would you like me?"
    show cherie normal
    "Trying to keep up the feel of a corporate takeover, I gesture to the head of the table."
    "Cherie nods and then positions herself right where I want her."
    "But she makes a point of resting her hands on the edge of the table."
    "Then using the support to bend over, sticking out her ass and spreading her legs."
    "That done, she looks back at me over her shoulder."
    cherie.say "I am ready, Master..."
    cherie.say "Would you like to seal the deal?"
    play sound pants_unzip
    "Keeping a firm hand on my emotions, I nod and begin to unzip my flies."
    scene bg black
    show cherie doggy naked ceo
    with fade
    "Cherie turns her head back to face forwards, putting herself in my hands."
    "One of which is currently pointing my painfully hard cock between her thighs."
    "And the other grabbing onto one of her haunches, holding her tightly."
    cherie.say "Ah..."
    cherie.say "Mmm…"
    cherie.say "Yes, Master - merge your assets with mine!"
    "Normally I'd be a lot more subtle about this kind of thing."
    "I'd be taking my time and making sure Cherie was one hundred percent ready."
    "But the circumstances demand that we get down to it right here and now."
    "Which is why I don't hesitate to thrust myself straight forwards."
    "I was fully intending to just slide along the lips of Cherie's pussy."
    "To make an initial pass so that I can see how ready for me she really is."
    "But almost as soon as I do, Cherie moans and lowers herself down."
    "This subtly changes the angle of everything down there."
    "And in the very next instant, I discover just how ready Cherie really is."
    cherie.say "Oh..."
    cherie.say "Mon dieu!"
    mike.say "Fuck!"
    "Already wet and warm, Cherie's lips part almost at the first touch of my cock."
    "This means that all of the motion I had planned is still behind me."
    play sexsfx1 slide_in
    show cherie doggy vaginal at startle(0.07, -15)
    "And so, rather than passing her pussy, I sink all of the way into her."
    "My thighs slap into the back of Cherie's, pushing her hard against the table."
    "And she shudders as my cock fills her up completely."
    "Part of me wants to stay right there and savour the sensation while it lasts."
    "But by now the animal part of my brain has fully take over."
    show cherie doggy at startle(0.07, -15)
    pause 0.25
    show cherie doggy at startle(0.07, -15)
    "And so I instantly pull back and then thrust into her a second time."
    "The result is just as explosive and pleasurable, driving me even more crazy."
    "So, of course, I keep on repeating the action, wanting to feel it again."
    play sexsfx1 fuck_moderate loop
    show cherie doggy at startle(0.07, -15)
    pause 0.25
    show cherie doggy at startle(0.07, -15)
    "And before there's the time to have a coherent thought, I'm in a state of constant motion."
    "Cherie's holding onto the edge of the table as if her life depended on it."
    "Her entire body shaking and her muscles desperately squeezing me."
    show cherie doggy at startle(0.07, -15)
    pause 0.25
    show cherie doggy at startle(0.07, -15)
    "Each thrust seems to make her resistance fade just a little more."
    "Seeing her arms lower her torso ever closer to the tabletop."
    "Soon enough, Cherie's belly makes contact with the polished wood."
    "And then her breasts are pressed against it too, nipples rubbing the whole time."
    show cherie doggy at startle(0.07, -15)
    pause 0.2
    play sexsfx1 fuck_speed loop
    show cherie doggy at startle(0.05, -10)
    "Like I already said, there's no way that I can rein myself in right now."
    "I'm totally consumed by my need for Cherie, my desire to fuck her brains out."
    "And so the moment she looks back over her shoulder at me, it's too much."
    "Her cheeks are flushed, her mouth hanging open in a silent moan."
    "And her eyes are somehow at once glazed over and yet expressive."
    show cherie doggy at startle(0.07, -15)
    pause 0.2
    show cherie doggy at startle(0.05, -10)
    "Showing me the total submission that Cherie is offering as I fuck her."
    "Suddenly I know that it's too much, that I can't keep on going any longer."
    show cherie doggy at startle(0.05, -10)
    pause 0.15
    play sexsfx1 cum_inside
    show cherie doggy cum pleasure with vpunch
    "That's when I feel my body jerk and myself exploding inside of her."
    with vpunch
    "Cherie raised her head from the table for long enough to moan."
    with vpunch
    "But then it falls back down again as her whole body goes limp."
    "And the only thing keeping her up is the table she's slumped over."
    play sexsfx1 slide_out
    show cherie doggy -cum outside with vpunch
    "I do the best I can to pull out of her gently, eliciting another moan."
    "And as I make an effort to clean myself up, I can still hear Cherie saying something softly."
    "So I lean in, wanting to know what it could possibly be."
    "Which is when I hear her repeating the same word, over and over again."
    cherie.say "Master...Master...Master..."
    $ cherie.sub += 5
    $ cherie.love += 3
    $ cherie.set_sex_slave()
    $ cherie.flags["giftslave_collar"] = True
    call stop_all_sfx from _call_stop_all_sfx_67
    scene bg black with dissolve
    pause 0.5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
