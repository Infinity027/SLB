init python:
    Event(**{
    "name": "bree_sasha_convenient_store",
    "priority": 500,
    "label": "bree_sasha_convenient_store",
    "conditions": [
        IsHour(9, 15),
        HeroTarget(Not(OnDate())),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 25),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 25),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_sasha_showdown",
    "priority": 500,
    "label": "bree_sasha_showdown",
    "conditions": [
        IsNotDone("bree_sasha_alternative_creation"),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        "Person.showdown(sasha, bree)",
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_sasha_showdown_2",
    "priority": 500,
    "label": "bree_sasha_showdown_2",
    "conditions": [
        "not Harem.find_by_name('home')",
        IsNotDone("bree_sasha_showdown", "bree_sasha_alternative_creation"),
        HeroTarget(
            Not(OnDate()),
            IsRoom("livingroom"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinCounter("pregnant", 9),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinCounter("pregnant", 9),
            ),
        ],
    "do_once": True,
    }
    )

    Event(**{
    "name": "3bj_birthday",
    "label": "bj_birthday",
    "priority": 250,
    "conditions": [
        IsActiveHarem('home'),
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            IsBirthday(),
            IsRoom("livingroom"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            MinStat("love", 150),
            MinStat("lesbian", 5),
            MinStat("sexperience", 1),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 150),
            MinStat("lesbian", 5),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    "once_year": True,
    }
    )

    Event(**{
    "name": "bree_sasha_bitches_1",
    "label": "bree_sasha_bitches_1",
    "conditions": [
        IsActiveHarem('home'),
        HeroTarget(
            IsGender("male"),
            IsActivity("watch_tv_with_everyone_male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            MinStat("sub", 90),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            Not(HasCheated()),
            MinStat("sub", 90),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/feels.ogg",
    })

    Event(**{
    "name": "bree_sasha_bitches_2",
    "label": "bree_sasha_bitches_2",
    "conditions": [
        IsActiveHarem('home'),
        IsDone("bree_sasha_bitches_1"),
        HeroTarget(
            IsGender("male"),
            IsActivity("watch_tv_with_everyone_male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            MinStat("sub", 100),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            Not(HasCheated()),
            MinStat("sub", 100),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/feels.ogg",
    }
    )

    Event(**{
    "name": "repeat_bree_sasha_bitches",
    "label": "repeat_bree_sasha_bitches",
    "conditions": [
        IsActiveHarem('home'),
        IsDone("bree_sasha_bitches_2"),
        HeroTarget(
            IsGender("male"),
            IsActivity("watch_tv_with_everyone_male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            MinStat("sub", 100),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            MinStat("sub", 100),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    "once_month": True,
    "music": "music/roa_music/feels.ogg",
    }
    )

    Event(**{
    "name": "bree_sasha_alternative_creation",
    "priority": 500,
    "label": "bree_sasha_alternative_creation",
    "conditions": [
        IsNotDone("bree_sasha_showdown", "bree_sasha_showdown_2"),
        IsHour(12, 19),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            HasSkill("cooking"),
            HasSkill("guitar"),
            HasSkill("video_games"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            MinStat("sub", 50),
            MinStat("lesbian", 9),
            MaxStat("sexperience", 0),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            MinStat("sub", 50),
            MinStat("lesbian", 9),
            MaxStat("sexperience", 0),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "home_harem_pegging_bree_sasha",
    "label": "home_harem_pegging_bree_sasha",
    "priority": 500,
    "conditions": [
        IsActiveHarem('home'),
        IsHour(19, 23),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            IsFlag("bree_sasha_threesome", True),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 150),
            IsFlag("strapon_known", True),
            MinStat("sexperience", 2),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "home_harem_bree_sasha_sunscreen",
    "priority": 500,
    "label": "home_harem_bree_sasha_sunscreen",
    "conditions": [
        IsActiveHarem('home'),
        IsSeason(0, 1),
        HeroTarget(
            Not(OnDate()),
            IsRoom("livingroom"),
            IsActivity("None"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("pool"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("pool"),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_month": True,
    })

label bree_sasha_convenient_store:
    show bree at center, zoomAt(1.25, (340, 880))
    show sasha at center, zoomAt(1.25, (940, 880))
    with fade
    "I snap my fingers as I remember the thing that's been bugging me most of the day."
    "Something that I needed to do and was trying to recall, but only now comes back to me."
    mike.say "Hey, you guys."
    mike.say "Don't let me forget to pick up some groceries today, yeah?"
    show bree happy at center, zoomAt(1.25, (640, 880)) with ease
    "At the mention of groceries, [bree.name] leans over to Sasha, a smile on her face."
    show sasha annoyed
    "Sasha rolls her eyes even before the other girl opens her mouth."
    "It's as if she already knows what [bree.name]'s about to say."
    show sasha whining
    sasha.say "Don't do it, [bree.name]!"
    show bree smile
    bree.say "Aw, come on, Sasha!"
    show bree normal
    show sasha vangry
    sasha.say "I mean it - don't you dare!"
    show sasha upset
    show bree smile
    bree.say "I'm doing it..."
    show sasha vangry
    sasha.say "Don't do it!"
    show sasha upset
    "I watch in fascination at this weird display."
    show bree happy at swing(1.25, 0.8, 1.25, -0.8, 0.4), center, zoomAt(1.0, (340, 1030)) with ease
    "And then [bree.name] amazes me by starting to sing!"
    bree.say "It's so convenient, it's a Convenient Store!"
    show sasha happy at swing(1.0, 0.8, 1.0, -0.8, 0.4), center, zoomAt(1.25, (940, 1030))
    sasha.say "You can't ask for more, at the Convenient Store!"
    show sasha normal
    show bree normal
    "I shake my head in disbelief at Sasha actually joining in too."
    hide bree
    hide sasha
    show bree happy at center, zoomAt(1.25, (340, 880))
    show sasha at center, zoomAt(1.25, (940, 880))
    mike.say "Wow..."
    mike.say "I never realised they actually had a jingle!"
    show bree smile
    bree.say "It's pretty old."
    bree.say "Sasha looked it up on the internet."
    show bree normal
    show sasha whining
    sasha.say "And now I wish I hadn't."
    sasha.say "It's such an annoying earworm!"
    show sasha annoyed
    mike.say "It's great having one of those things around the corner from here."
    mike.say "But you know, I've never seen one anywhere else but in this town."
    show bree smile
    bree.say "Yeah, we never had them back home."
    show bree normal
    show sasha shout
    sasha.say "Same here."
    show sasha normal
    mike.say "And at first, I kinda thought someone messed up the sign!"
    show sasha shout
    sasha.say "I know, right?"
    sasha.say "But everyone from around here, they just accept it."
    sasha.say "You point it out to them and they don't know what you're talking about!"
    show sasha normal
    show bree smile
    bree.say "Like they're brainwashed or something!"
    show sasha joke
    sasha.say "Like a cult!"
    show bree happy at center, zoomAt(1.0, (340, 880)), startle
    show sasha happy at center, zoomAt(1.0, (940, 880)), startle
    "The girls laugh at the idea, and I can't help joining in."
    mike.say "Joking aside, though - I love the place."
    mike.say "I don't know what I'd do without it."
    bree.say "We ALL love it!"
    sasha.say "All hail the Convenient Store!"
    scene bg black with dissolve
    return

label home_harem_preg_talk:
    if bree.is_collared and sasha.is_collared:
        "I know that you kind of grow up in the modern day and age with the morals of safe sex and taking sensible precautions practically drummed into you."
        "But once you start breaking the rules of mainstream society and venturing into areas that are pretty much uncharted for most people, things are different."
        "Throwing a whole load of accepted rules and regulations out of the window makes you kind of lax in other areas too."
        "And if you've, oh I don't know, been living under the same roof as your two devoted sex-slaves, for example."
        "Then you could obviously be forgiven for letting the use of an occasional condom slip your mind, right?"
        show bree happy underwear at center, zoomAt (1.25, (420, 880))
        show sasha happy underwear at center, zoomAt (1.25, (860, 880))
        with dissolve
        "I mean, when you have a pair of girls like [bree.name] and Sasha, literally on the end of a couple of leads..."
        "Perhaps I should have spotted the warning signs when they first appeared."
        "Like one of them starting to feel like crap in the mornings or craving weird stuff at mealtimes."
        "But to miss the same tell-tale signs in both [bree.name] and Sasha..."
        "Well, maybe I was seeing them, but ignoring what they actually meant out of unconscious fear?"
        "Either way, I have the unenviable experience of walking in on [bree.name] and Sasha as they're comparing their stomachs."
        "Believing themselves to be totally alone, they experimentally prod and squeeze at each other."
        "Although it looks a little weird, I'm actually more than a little turned on by the sight!"
        "Before they realise I'm there, the conversation between them is quiet, almost conspiratorial in nature."
        "But as soon as they see me, I'm treated to a round of smiles and fluttering eyelids."
        "Specifically the kind that remind me of just how good it is to be their master."
        show bree smile
        bree.say "Hi there, [hero.name]."
        show bree normal
        show sasha shout
        sasha.say "Sorry, we didn't hear you come in."
        show sasha normal
        "Both of the girls have their tops hiked up, exposing their bellies."
        "And as I return their smiles, I note that neither of them makes a move to pull them back down again."
        mike.say "No worries about that."
        mike.say "So long as you tell me what you were talking about just now?"
        "[bree.name] and Sasha look at each other, seeming to take a literal deep breath before answering my question."
        show sasha shout
        sasha.say "We were just comparing bellies, that's all."
        show sasha normal
        show bree smile
        bree.say "Sasha thinks mine's a little bigger."
        bree.say "But I don't think there's that much in it."
        show bree normal
        "I frown a little at this, not really knowing what to make of their sudden obsession with their stomachs."
        "Neither of them is particularly large in that area to begin with."
        "And if putting on a little weight around the middle bothered me, then I'd have said so already."
        "After all, that's one of the advantages of having a couple of sex-slaves - they don't get pissy when you tell them to lose weight!"
        "But as [bree.name] points to their respective midriffs, I do seem to notice that they're both looking just a tad more prosperous at the moment."
        "Not that I find that a turn-off in the slightest."
        "It actually kind of suits them, makes them look cute and like I want to use those bellies as a cushion..."
        mike.say "You shouldn't argue about things like that, you know."
        mike.say "Neither of you is fat - not in the slightest."
        mike.say "In fact, I think it makes you both look pretty hot!"
        show sasha upset
        show bree happy
        "At this, Sasha gives me an oddly irritated look and [bree.name] turns to her, trying to suppress a fit of giggles."
        "Confused by this reaction, I look form one of them to the other and then back again."
        "I really don't know what was so odd about that statement."
        "But so much for me thinking that I was being all modern and relaxed about their apparent pot-bellies!"
        mike.say "What did I say?"
        mike.say "What's so funny?"
        show bree smile
        bree.say "Oh, [hero.name] - you really don't know, do you?"
        show bree happy at startle
        "[bree.name] giggles again."
        mike.say "Know what?"
        show bree normal at center, zoomAt (1.25, (420, 880))
        show sasha shout at center, zoomAt (1.25, (860, 880))
        sasha.say "It's [bree.name] and I, [hero.name] - we're both pregnant."
        show sasha normal
        "I don't know if Sasha's being so blunt out of obedience or frustration at my being so slow on the uptake."
        "But she still manages to cut through the confusion and get to the heart of the matter with those few words."
        mike.say "You're pregnant...BOTH of you?!?"
        show sasha shout
        sasha.say "That is what I just said, [hero.name]."
        show sasha normal
        mike.say "I...I know..."
        mike.say "It's just...a lot to take in, that's all!"
        "I should be acting the part of the confident and unshakable Master here, I know."
        "But the news really has taken me completely by surprise."
        "And this is not the scene I'd always imagined would confront me if I happened to get two different girls pregnant at the same time, either."
        mike.say "Wait a minute - you're both okay with this?"
        mike.say "You're not mad at all?"
        "[bree.name] and Sasha look at each other again, before they return their respective gazes to me."
        "They exchange one of those loaded glances that speaks of serious discussions having happened before this moment."
        "Sasha nods first, and then [bree.name] a few seconds later."
        show bree smile
        bree.say "It's not our place to be mad or to judge your actions, [hero.name]."
        show bree normal
        show sasha shout
        sasha.say "You've made us both pregnant with your children, whether that was your plan or not."
        show sasha normal
        show bree smile
        bree.say "We're your slaves, so we obey your will in all such matters."
        show bree normal
        "I nod, thinking at first that this pretty much gets me off of the hook on both counts."
        show bree happy at center, traveling(1.4, 0.3, (420, 1050))
        show sasha happy at center, traveling(1.4, 0.3, (860, 1050))
        "But then it occurs to me that, while I'm not getting my ass kicked, the actual opposite is true when it comes to responsibility."
        "As my sex-slaves, [bree.name] and Sasha are effectively happy to sit back and let me make all of the decisions for all three of us."
        "No, wait - all FIVE of us!"
        "It seems that being the undisputed Master isn't all fun and games..."
    else:
        "Have you ever watched one of those wildlife documentaries on the TV?"
        "The kind where you see lionesses sizing up a bewildered wildebeest?"
        "Well that's how I feel right about now."
        show bree happy at center, zoomAt (1.25, (420, 880))
        show sasha happy at center, zoomAt (1.25, (860, 880))
        with dissolve
        "I just walked in on [bree.name] and Sasha, and everything just stopped dead."
        "They were chatting away intently the very second before they realised I was there."
        show bree normal
        show sasha normal
        "But then the conversation ended abruptly, and both of them are now staring straight at me."
        "And here I am, that poor, dumb animal that doesn't know whether to freeze or turn tail and run!"
        "The only difference is that I don't think the lionesses often wear knowing smiles on the TV shows..."
        show bree happy at startle
        bree.say "Hey, [hero.name]!"
        show bree normal
        show sasha shout
        sasha.say "What a coincidence!"
        show sasha normal
        show bree smile
        bree.say "Yeah - we were just talking about you..."
        show bree normal
        "I hope my smile doesn't look too nervous and forced."
        "But I'm already sure they know just how much I'm freaked."
        mike.say "Erm...really?"
        "The girls nod and their smiles become even more smug than before."
        show sasha joke
        sasha.say "Yeah, we were just discussing what kind of a guy you are."
        show bree normal
        mike.say "What kind of a...a guy I am?"
        show sasha shout
        sasha.say "That's right."
        sasha.say "You see [bree.name] here."
        show sasha embarrassed
        "Sasha gestures to [bree.name], who flutters her eyelids and regards me sweetly."
        show sasha shout
        sasha.say "Now she thinks that you're the kind of guy that likes to be treated with kid gloves."
        show sasha normal
        show bree happy
        "[bree.name] nods happily at this statement."
        show sasha shout
        sasha.say "That you need to have things sugar-coated so that you can swallow them."
        show sasha normal
        show bree smile
        bree.say "But Sasha, on the other hand."
        show bree normal
        "[bree.name] leans forward, taking over the conversation."
        bree.say "She subscribes to the school of thought that you appreciate being direct."
        show bree normal
        "Now it's [bree.name]'s turn to regard Sasha, who shrugs and nods."
        show bree smile
        bree.say "Sasha thinks you'd want to be told the plain and unadorned truth."
        show bree normal
        "I look from Sasha to [bree.name] and back again, still not exactly sure what's going on here."
        show sasha shout
        sasha.say "So, [hero.name] - which is it?"
        show sasha normal
        show bree smile
        bree.say "Yeah - which one of us has you figured?"
        show bree normal
        mike.say "Wait...let me get this straight."
        mike.say "The two of you have been sitting around, debating how I prefer to hear news?"
        mike.say "And now you want me to settle the argument?"
        "[bree.name] and Sasha look at each other briefly, and then nod as one."
        mike.say "Mind if I ask a question of my own?"
        mike.say "I mean, what's so important about that?"
        "[bree.name] smiles at me again, looking as innocent and harmless as she ever has."
        show bree smile
        bree.say "Oh, [hero.name] - don't be silly!"
        bree.say "There's nothing really important about that."
        show bree normal
        mike.say "Then why did you..."
        mike.say "Why all the questions?!?"
        show bree happy at startle
        show sasha happy at startle
        "I hear Sasha laugh at the frustration in my voice, and my head snaps round in her direction."
        show bree normal
        show sasha shout
        sasha.say "Ah, [hero.name], chill out!"
        sasha.say "We just thought it'd be best to distract you a little bit."
        sasha.say "Rather than just coming out and telling you that we're both pregnant!"
        show sasha normal
        "What with all the confusion that the girls have been careful to create, I don't understand straight away."
        "Instead I keep on staring at Sasha and [bree.name], as if I expect them to say more."
        show bree talkative
        bree.say "[hero.name]..."
        bree.say "Didn't you hear what Sasha said?"
        show bree normal
        show sasha shout
        sasha.say "Yeah, earth to [hero.name] - both your girlfriends are knocked up!"
        show sasha normal
        "Bless her heart - you can see why Sasha's the song-writer of the pair..."
        with vpunch
        mike.say "What..."
        mike.say "You mean that..."
        show sasha shout
        sasha.say "Yes and yes."
        show sasha normal
        show bree smile
        bree.say "We mean it, [hero.name]."
        bree.say "You're going to be a daddy - twice over!"
        show bree normal
        "I don't know what to say, and so, for a change, I don't say anything."
        "My mind is racing at the implications of what I've just been told, what it means for the three of us."
        "And more than ever I feel like that wildebeest, cornered and helpless in the face of his inevitable fate!"
        show bree talkative
        bree.say "[hero.name], are you feeling okay?"
        show bree sadsmile
        show sasha whining
        sasha.say "Yeah, you don't look too good!"
        show sasha sadsmile
        mike.say "I...I'll be okay."
        mike.say "It's just a lot to take in - you know?"
        show bree happy at center, traveling(1.4, 0.3, (420, 1050))
        show sasha happy at center, traveling(1.4, 0.3, (860, 1050))
        "[bree.name] and Sasha both nod, coming closer to put their arms around me and offer their support."
        "And do you know what?"
        "As soon as they do, I'm almost certain that it will - be okay, that is."
        "Three of us."
        "Two of them."
        "And more than enough love to go around."
        "Sorry if that sounds a bit sappy and emotional, but I just found out that I'm going to be a dad."
        "And that's the kind of thing that can make a guy get hit right in the feels!"
    $ sasha.flags.toldpreg = True
    $ bree.flags.pregtest = 2
    return

label bree_sasha_showdown:
    scene bg livingroom with fade
    "Yet another lazy day finds me, lounging around the living room, spread across the couch and staring at the television screen blankly."
    "The girls are off doing something or another, the last I saw them in fact, [bree.name] was heading into Sasha's room as the two whispered about something."
    "I'm glad the two are getting along, they're very different but seem to like each other well enough at least."
    "It's only when my attention begins to drift idly back towards the television that I hear a door open and two sets of footsteps approaching."
    show bree gloomy at center, zoomAt (1.0, (420, 720))
    show sasha upset at center, zoomAt (1.0, (860, 720))
    with easeinright
    "Glad for the company, I turn to watch both Sasha and [bree.name] enter the room, although I quickly realise something here is very, very wrong."
    "Sasha looks furious, something or someone has clearly upset her greatly, while [bree.name] is a wreck, her eyes a crimson red, the telltale sign that she's just stopped crying."
    "I immediately snap to attention, standing up and quickly glancing between the two of them, wondering what they could have been talking about that devastated them so much."
    mike.say "What? What's wrong?"
    show sasha at center, traveling(1.25, 0.3, (860, 880))
    "Sasha's glare is terrifying, and before she even opens her mouth, I clue into exactly why the two of them seem to be confronting me."
    show sasha vangry
    sasha.say "How the hell did you think you'd get away with this?"
    show sasha angry
    mike.say "What? Get away with what?"
    "I feign ignorance in the desperate hope that I'm wrong."
    show bree sad at center, traveling(1.25, 0.3, (420, 880))
    bree.say "Please don't lie. No more lying."
    show bree gloomy
    "She's audibly on the verge of tears once more, practically biting herself to bide them away."
    show sasha vangry
    sasha.say "You're sleeping with BOTH of us?"
    sasha.say "We live together, genius! Or did you forget?"
    sasha.say "Of course we're going to figure it out."
    show sasha angry
    mike.say "Oh. That."
    show sasha vangry at center, zoomAt (1.0, (860, 880)), startle
    sasha.say "Yes, 'THAT'! What the fuck were you thinking?"
    show sasha angry
    mike.say "I..."
    if "bree_preg_talk" in DONE and "sasha_preg_talk" in DONE:
        show sasha vangry
        sasha.say "You even got us pregnant moron!"
        show sasha angry
        show bree cry
        "[bree.name]'s eyes are welling up with tears."
    elif "sasha_preg_talk" in DONE:
        show sasha vangry
        sasha.say "You even got me pregnant moron!"
        show sasha angry
        show bree cry
        "[bree.name]'s eyes are welling up with tears."
    elif "bree_preg_talk" in DONE:
        show sasha vangry
        sasha.say "You even got [bree.name] pregnant moron!"
        show sasha angry
        show bree cry
        "[bree.name]'s eyes are welling up with tears."
    if all([person.love >= 150 and person.lesbian >= 9 and person.flags.collared for person in [sasha, bree]]):
        show sasha normal
        "I see Sasha fingering the collar around her neck, a thoughtful look beginning to appear on her face."
        show sasha whining
        sasha.say "You know what, [bree.name] - when you think about it, this whole argument is pretty dumb!"
        show sasha sadsmile
        show bree stuned
        "[bree.name] wrinkles her nose, as if puzzled by the statement."
        show bree surprised
        bree.say "Huh...what do you mean?"
        show bree stuned
        show sasha whining
        sasha.say "Well, why are we even discussing who [hero.name] chooses to have sex with?"
        sasha.say "Didn't we both agree to wear these collars as a sign that he's our Master?"
        show sasha sadsmile
        show bree blank
        "Now it's [bree.name]'s turn to look down at her own collar in a thoughtful manner."
        show bree talkative
        bree.say "I...guess so..."
        show bree sadsmile
        show sasha shout
        sasha.say "So we can't go round picking and choosing when he's the Master and when he's not, can we?"
        sasha.say "He either is or he isn't."
        show sasha normal
        show bree normal
        "[bree.name] nods slowly as the logic of Sasha's argument begins to dawn on her."
        show bree talkative
        bree.say "You're right, Sasha."
        bree.say "We shouldn't be getting mad at [hero.name]."
        show bree smile
        bree.say "We should be happy that he's still keeping us as his slaves at all!"
        show bree normal
        "A part of me can't actually believe what I've just heard."
        "Without my needing to utter a single word, [bree.name] and Sasha have thrashed it all out right in front of me."
        "And not only that, they've managed to come to just the conclusion that I would have hope for too!"
        "Before I can say a single word, they both turn to me with huge smiles on their faces."
        show sasha happy
        show bree happy
        sasha.say "We're sorry you had to hear that, [hero.name]."
        bree.say "We REALLY are!"
        sasha.say "But of course, you can have as many girls as you want to."
        bree.say "Yeah, as many as you like."
        bree.say "But please - don't forget about us while you're out having fun!"
        $ Harem.join_by_name("home", "bree", "sasha")
    elif any(Harem.find(sasha, name='band')) and not sasha.is_collared:
        show sasha whining
        sasha.say "I know just how weird I'm gonna sound saying this, what with us being involved with the entire band already."
        sasha.say "But I can't have any more people getting involved in my love life!"
        show sasha sad
        "Sasha shakes her head at the strange direction the conversation has now taken."
        show sasha whining
        sasha.say "You already know how hard it was for me to get my head around sharing you with two other girls."
        sasha.say "I can't keep this up if it becomes three."
        show sasha sad
        "I nod, not liking what I'm hearing, but still able to empathise with what Sasha's saying."
        show bree surprised
        bree.say "Wait a minute - you're saying you're not okay to share [hero.name] with me."
        bree.say "But it's cool for scuzzy bandmates to run a train on him?!?"
        show bree gloomy
        mike.say "[bree.name], I'm sure that's not what she means at all."
        mike.say "Is it, Sasha?"
        show sasha annoyed
        "Bristling more than a little at the way in which she just heard Anna and Kleio described, Sasha looks daggers at [bree.name]."
        show sasha vangry
        sasha.say "She knows what I meant, [hero.name]."
        sasha.say "The girls in the band are like sisters to me."
        sasha.say "So when we accepted you into the group you became like...well, I guess you became like a brother too."
        show sasha annoyed
        show bree angry
        "[bree.name] crosses her arms at this and fixes Sasha with an exceptionally bitchy stare."
        show bree vangry
        bree.say "So you're saying that this little thing you've got going on is like incest?"
        show bree angry
        show sasha angry
        "For a moment, Sasha looks like she's about to fire back in the same manner."
        "But then she makes a dismissive gesture and offers [bree.name] a sarcastic grin instead."
        show sasha joke
        sasha.say "You know what, I don't have to do this."
        sasha.say "Who in the hell are you anyway, [bree.name]?"
        sasha.say "You're just some blonde bitch that happens to live under the same roof as me."
        show sasha annoyed
        show bree annoyed
        "[bree.name] looks seriously pissed off at the insult, but Sasha cuts her off before she can respond in kind."
        show sasha vangry
        sasha.say "I'll make this really simple, [hero.name]."
        sasha.say "It's either me and the girls in the band, or her."
        show sasha annoyed
        "She cocks her head at [bree.name]."
        show sasha vangry
        sasha.say "So you make your choice - but either way, one of us has to go!"
        show sasha upset
        menu:
            "Choose [bree.name]":
                mike.say "I'm Sorry, Sasha."
                mike.say "I probably sound crazy saying this, but if I have to choose - I choose [bree.name]."
                show sasha surprised
                show bree happy
                "Sasha's jaw almost literally drops open at this, as if she can't believe what she's hearing."
                "In rather predictable contrast, [bree.name] looks openly triumphant."
                "I guess this has already gotten way too personal for anyone to be civil about it."
                show sasha stuned
                show bree smile
                bree.say "Well, Sasha - there's your answer!"
                bree.say "I guess [hero.name] must love me three times as much as he does you!"
                show bree normal
                show sasha whining
                sasha.say "But...what about all we've been through with the band?"
                sasha.say "What about how close we are with Anna and Kleio?"
                show sasha sad
                "She pauses for a moment, looking genuinely heart-broken as she adds one last thing to her list."
                show sasha whining
                sasha.say "What about...what about all the stuff we went through that was just you and me?"
                show sasha sad
                "I open my mouth, wanting to find something to say that might make things just a little better."
                "But [bree.name] cuts me off before I can say a single word."
                show bree vangry
                bree.say "Oh, please, Sasha!"
                bree.say "[hero.name] already told you who he wants to be with."
                bree.say "Stop trying to turn on the waterworks and play the victim!"
                show bree angry
                show sasha annoyed
                "Sasha looks as though she's about to spit as much venom back in [bree.name]'s direction in return."
                show sasha cry
                "But then something inside of her seems to break, and her cheeks colour with emotion."
                hide sasha with easeoutright
                "She puts a hand to her mouth, perhaps to stifle a genuine cry of emotion, and rushes away."
                show bree normal at center, zoomAt (1.25, (640, 880)) with ease
                "[bree.name] wraps herself around my arm, smiling as the other girl disappears."
                "All I can do is watch her go, wondering if I've made the right decision after all."
                $ sasha.set_gone_forever()
                $ kleio.set_gone_forever()
                $ anna.set_gone_forever()
                $ Room.find("bedroom3").hide()
                $ Room.find("studio").hide()
            "Choose the band":
                mike.say "I'm sorry, [bree.name]."
                mike.say "But if I have to choose - I choose the band."
                show bree annoyed
                "[bree.name] lets out a sound of pure disgust and shakes her head."
                show bree vangry
                bree.say "Jesus, [hero.name] - I wish I'd know that you were such a pervert BEFORE we got involved!"
                bree.say "I mean, you should have a T-shirt printed with it on."
                bree.say "Or maybe hang a sign around you neck - you too, Sasha!"
                show sasha at center, zoomAt (1.25, (740, 880))
                show bree angry at center, zoomAt (1.25, (340, 880))
                with ease
                "I feel Sasha take a hold of my arm, leaning against me."
                "As much as I know she's doing so to face [bree.name] down, it feels good to have her supporting me all the same."
                mike.say "This isn't just about the sex, [bree.name]."
                mike.say "But I guess you need to be an artist to see that."
                "[bree.name] snorts give this a derisive snort, a look of annoyed amusement on her face."
                show sasha shout zorder 2
                sasha.say "He's right, [bree.name]."
                sasha.say "But believe me - the sex is still pretty mind-blowing too!"
                sasha.say "I guess you just have to be big enough to be able to share..."
                show sasha normal
                show bree vangry zorder 1
                bree.say "Urgh - you can dress it up however you like, Sasha."
                bree.say "But the truth is that you're just a bunch of filthy degenerates, that's all."
                bree.say "And I won't breath the same air as either of you!"
                hide bree with easeoutright
                "That said, she turns her back on us and storm away."
                show sasha at center, zoomAt (1.25, (640, 880)) with ease
                "I feel Sasha's grip on my arm tighten as we watch [bree.name] walk off."
                show sasha shout
                sasha.say "Don't worry about her, [hero.name]."
                sasha.say "And don't listen to a word she's said."
                sasha.say "We've got something that the likes of her will never be able to understand."
                sasha.say "If anything, we should feel sorry for her!"
                show sasha normal
                "I nod as I watch [bree.name] go, hoping that I've made the right decision this time."
                $ bree.set_gone_forever()
                $ Room.find("bedroom2").hide()
    elif all([person.love >= 150 and person.lesbian >= 9 and person.sub >= 25 for person in [sasha, bree]]):
        mike.say "I'm sorry. I should have said something."
        mike.say "It's just I like you both."
        mike.say "I thought I'd be able to decide eventually, but the more time I spent with both of you, the harder it got to cut it off with one and."
        show bree cry
        bree.say "You should have just said something."
        bree.say "Are we the only ones?"
        show bree gloomy
        menu:
            "Yes":
                mike.say "Yes! Of course you are."
                mike.say "I don't go around fucking everything I see."
                if Harem.find_by_name("band"):
                    show sasha surprised
                    sasha.say "What about the band?"
                    $ sasha.love -= 15
                    $ bree.love -= 15
                    if Harem.find(sasha, name='band'):

                        sasha.say "Come on..."
                    else:
                        sasha.say "Oh yeah, they had a lot to tell me about you."
                    show sasha upset
                    mike.say "I, Right, and the band."
                    show bree cry
                    bree.say "You can't keep lying about this stuff."
                    show bree gloomy
                    mike.say "I know, I'm just..."
                elif sasha.flags.cheated:
                    $ g = sasha.flags.cheated
                    show sasha surprised
                    sasha.say "What about [g]?"
                    $ sasha.love -= 15
                    $ bree.love -= 15
                    mike.say "I, Right, [g]."
                    show bree cry
                    bree.say "You can't keep lying about this stuff."
                    show bree gloomy
                    mike.say "I know, I'm just..."
                elif bree.flags.cheated:
                    $ g = bree.flags.cheated
                    show bree surprised
                    bree.say "What about [g]?"
                    $ sasha.love -= 15
                    $ bree.love -= 15
                    show bree sad
                    mike.say "I, Right, [g]."
                    show sasha wtf
                    sasha.say "Fucking manwhore..."
                    mike.say "I know, I'm just..."
                else:
                    show sasha vangry
                    sasha.say "You could have fooled me, jackass!"
                    sasha.say "How the hell are we supposed to trust anything you say?"
                    show sasha upset
                    mike.say "I don't know. I really don't."
            "No":
                mike.say "You, No, you aren't the only ones."
                $ sasha.love -= 5
                $ bree.love -= 5
                show sasha vangry
                sasha.say "Just how many people are you fucking?"
                show sasha annoyed
                mike.say "I-"
                show sasha vangry
                sasha.say "Save it, I don't want to know actually."
                sasha.say "If you tell me, I feel like I'm going to throw up on you."
                show sasha upset
        mike.say "I fucked up, I know, but I'll do anything to make it up to the both of you."
        show bree sad
        bree.say "It isn't easy to build up shattered trust."
        show bree gloomy
        mike.say "I know, but I'm going to try."
        mike.say "I don't expect you to forgive me, I don't know if I can forgive myself, but just know that the last thing I wanted was to hurt either of you."
        show sasha vangry
        sasha.say "And you did a *great* job with that, well done."
        sasha.say "Really, just look at how happy the both of us are."
        show sasha annoyed
        "She's still clearly furious, but unless it was simply my wishful thinking talking, some of the edge seems to have slipped out of her words."
        "An awkward silence falls on the room. I've said my piece, tried my best, but now it's up to the girls to decide my metaphorical fate."
        show sasha upset
        "The two stare at me for a while, Sasha's glare terrifying while [bree.name]'s almost pathetic puppy dog eyes almost outright painful."
        "Eventually, the silence is unbearable, and I'm forced to break it."
        mike.say "So what now?"
        show sasha vangry
        sasha.say "I don't know."
        show sasha angry
        show bree sad
        bree.say "Neither do I."
        show bree gloomy
        show sasha vangry
        sasha.say "I should kick your ass for what you did."
        show sasha upset
        show bree sad
        bree.say "I should just leave."
        show bree gloomy
        mike.say "Yeah both of those would be fair."
        show sasha whining
        sasha.say "But."
        sasha.say "I don't *want* to go anywhere."
        show sasha sadsmile
        show bree sad
        bree.say "You really hurt me, [hero.name]."
        bree.say "You betrayed my trust and it's going to take a long time to repair that."
        "I nod solemnly along to their words."
        bree.say "But I don't want to leave you either."
        show bree sadsmile
        mike.say "So...?"
        show sasha shout
        sasha.say "Sounds like you're in luck, [hero.name]."
        sasha.say "Neither of us are going anywhere. You'll have plenty of time to make it up to us."
        show bree surprised
        bree.say "So, are we just gonna share him?"
        show bree stuned
        show sasha shout
        sasha.say "Why not? Apparently we've already been doing so, and we've been happy enough."
        show sasha normal
        show bree talkative
        bree.say "Well, like, sure, but it's a little weird?"
        show bree sadsmile
        show sasha shout
        sasha.say "The only thing that's changed is we're being more honest with each other."
        show sasha normal
        show bree smile
        bree.say "Yeah Yeah! You're right."
        show bree normal
        "I feel like I don't have any say in the situation anymore, with Sasha easily convincing [bree.name] to her side."
        "It isn't as though the outcome is a bad one for me though, so I just keep my mouth shut."
        show sasha shout
        sasha.say "Of course I'm right."
        sasha.say "So, [hero.name]. It looks like you're getting a second chance."
        show sasha normal
        show bree smile
        bree.say "From like, both of us."
        show bree normal
        show sasha vangry
        sasha.say "If you dare cheat on either of us again, it's over for good. You're lucky you're so charming."
        show sasha normal
        mike.say "Heh, I guess I am."
        mike.say "Never again, I swear."
        show bree smile
        bree.say "Good! But like, you've still got a long way to go before things will be the same again."
        show bree normal
        show sasha shout
        sasha.say "Damn right. I can't stress how much you need to make this up to us."
        show sasha normal
        mike.say "Anything I can do, I will."
        show sasha shout
        sasha.say "We'll think of something."
        sasha.say "In fact, we'll do that right now. [bree.name], come on."
        hide sasha with easeoutright
        show bree talkative
        bree.say "Now? Well like, sure I guess!"
        show bree at center, zoomAt (1.25, (640, 840)) with ease
        bree.say "Um, I'm glad we're going to work this out, [hero.name]."
        bree.say "It might be hard, but I do really like you, just please not again?"
        show bree normal
        mike.say "Of course not."
        show bree smile
        bree.say "I'll just have to try and trust you then! See you later!"
        hide bree with easeoutright
        "With a wave, [bree.name] turns and rushes off down the corridor that Sasha escaped down, the two headed into one of their bedrooms and quickly filling the hallway with hushed voices."
        "Try as I might, I can't figure out what they're saying to one another, and eventually decide it's probably better that way."
        "My heart pounding, I'm frozen in place for a little while, wondering just how I'd managed to pull off not only cheating on two girls with one another, but having them find out and both agree to stay with me anyway."
        "Both relieved, and curious about what might be just around the corner in my relationship with the two, I get back to my day, trying to ignore the incessant whispering from behind their closed doors."
        $ Harem.join_by_name("home", "bree", "sasha")
    elif sasha.love > bree.love and sasha.love >= 125:
        mike.say "I don't know what I was thinking."
        mike.say "I don't have any excuse. I fucked up. I deserve anything you can throw at me."
        show sasha vangry
        sasha.say "Damn right you do!"
        sasha.say "Are we the only ones?"
        show sasha annoyed
        mike.say "Yeah, of course you are."
        show sasha sad
        show bree sad
        bree.say "Well we don't know, [hero.name]."
        bree.say "How are we supposed to believe you?"
        show bree gloomy
        mike.say "I don't know."
        show bree sad
        bree.say "Was I really asking so much of you, [hero.name]?"
        bree.say "I just I just wanted to be with you."
        bree.say "If I wasn't enough, you should have just told me I could have just."
        show bree gloomy
        "She's crying again, tears streaming freely down her face as her voice barely breaks through to barely form her words."
        mike.say "It isn't that you aren't enough [bree.name]."
        show bree cry
        bree.say "Then why? Why would you do this? *How* could you do this?"
        show bree gloomy
        "I stammer over my words a few times before falling silent. I don't have an explanation for her, and I can't bring myself to lie to [bree.name]'s face. Not now."
        show bree cry
        bree.say "I think I need to go."
        show bree gloomy
        sasha.say "Yeah, go calm down [bree.name]."
        show bree cry
        bree.say "I don't mean calm down."
        show bree gloomy
        mike.say "Wait, you can't-"
        show bree cry
        bree.say "I'm going to move back home I'll um, be gone by tomorrow morning."
        show bree gloomy
        show sasha shocked
        sasha.say "You're moving?"
        show sasha stuned
        "Sasha looked as shocked as I was. [bree.name] couldn't make eye contact with either of us, instead preferring the spot on the carpet that her steady stream of tears stained."
        show bree cry
        bree.say "Yeah I can't stay here anymore."
        show bree gloomy
        show sasha whining
        sasha.say "Look, [hero.name] fucked up, I agree, but you don't have to move away."
        show bree vangry
        bree.say "Yes I do, Sasha!"
        show bree angry
        "The outburst was sudden, almost violent."
        show bree vangry
        bree.say "You don't get it! This was supposed to be a fresh start, a new beginning."
        bree.say "[hero.name] ruined that."
        bree.say "I can't just pretend like it never happened and move on, my brain doesn't work like yours does, Sasha!"
        bree.say "Not while I still live in this city."
        bree.say "I can't move on until I've moved."
        show bree angry
        mike.say "Aren't you being a bit drastic? Just, sleep on it, alright?"
        show bree vangry
        bree.say "I'm not being drastic!"
        bree.say "I just."
        show bree cry
        bree.say "I'll go call a cab."
        hide bree with easeoutright
        "I try again to stop her, plead for her to stay, but she ignores me and marches away to her room. I don't need to try the handle to know it's locked."
        "Not everything she said made sense to me, but it's clear that she's confused right now."
        "I am too. I can't tell if she's making a mistake, or the right decision."
        show sasha whining
        sasha.say "I didn't think she'd actually go."
        show sasha sad
        mike.say "Neither did I."
        mike.say "You aren't going too, right?"
        show sasha whining
        sasha.say "Maybe. I haven't decided yet."
        show sasha sad
        mike.say "...Please don't."
        show sasha whining
        sasha.say "Why shouldn't I, [hero.name]? What can you possibly do to convince me?"
        show sasha sad
        mike.say "I have no idea, but I'll try anything."
        mike.say "I can't lose both of you."
        "There's a short silence. I can tell that Sasha is thinking, hard, but her expression is so muddled, a cocktail of so many different emotions, I've no idea which way she's leaning."
        show sasha at center, zoomAt (1.25, (640, 880)) with ease
        "Eventually, with a sigh, she throws herself onto the couch, and motions for me to sit next to her."
        show sasha whining
        sasha.say "You're pathetic."
        show sasha sad
        "Her words might have hit me hard, were it not for the overwhelming sense of relief washing over me as I readily sat besides her."
        show sasha vangry
        sasha.say "If you ever, and I mean *ever*, pull anything like this again, you'll regret it."
        show sasha annoyed
        mike.say "Never again. I promise."
        show sasha vangry
        sasha.say "You've got a long way to go before the word 'promise' means anything to me again."
        sasha.say "Just shut up for a while now. I'm still mad at you."
        show sasha annoyed
        "I open my mouth to confirm I'll be quiet, before realising how stupid that'd be, and just fall silent."
        "The two of us sit there for a while, the tension in the air eventually beginning to dissipate."
        hide sasha with easeoutright
        "Sasha eventually leaves me to go help [bree.name] pack her things, before returning to escort me out of the room while she helps [bree.name] get to the cab."
        "I don't know where [bree.name] got the money for a flight so soon, but it doesn't even give me chance to say goodbye."
        "The closest I get is staring after her as her cab disappears into the distance."
        "I doubt I'll ever see [bree.name] again."
        "At the very least, there's still hope for Sasha and I, I just need to prove to her I can be loyal."
        "It won't be easy, but she's worth it."
        $ bree.set_gone_forever()
        $ Room.find("bedroom2").hide()
    elif bree.love >= sasha.love and bree.love >= 125:
        mike.say "I don't know."
        mike.say "I don't want to make excuses and lie, claim it's because of something it wasn't."
        mike.say "I just can't explain why I did it."
        show sasha vangry
        sasha.say "You're so full of shit."
        show sasha angry
        mike.say "I-"
        show sasha vangry
        sasha.say "Save it. I'm done."
        show sasha angry
        mike.say "Sasha, wa-"
        show sasha vangry
        sasha.say "I told you to save it, [hero.name]."
        sasha.say "What the hell do you expect? That we'll continue like nothing happened?"
        sasha.say "That in a few weeks the three of us will be looking back at this and having a good old chuckle at the whole thing?"
        sasha.say "You're a piece of shit. The sooner I get away from you, the better."
        show sasha angry
        mike.say "Get away?"
        show sasha vangry
        sasha.say "I'll get my things tomorrow."
        show sasha annoyed
        show bree surprised
        bree.say "W-wait, are you moving out?"
        show bree stuned
        show sasha whining
        sasha.say "Yeah, I am."
        sasha.say "What, I'm supposed to live with {b}him{/b}?"
        sasha.say "I can't stand the thought of standing next to him for any longer, let alone sleeping under the same roof."
        show sasha sad
        show bree sad
        bree.say "But where are you going to go?"
        show bree gloomy
        show sasha whining
        sasha.say "I'll crash on someone's couch for now. Shouldn't take too long to find a place of my own."
        show sasha sad
        mike.say "But-"
        show sasha vangry
        sasha.say "Shut up, you. You should consider yourself lucky that I'm leaving it at moving out."
        sasha.say "I'll hail a cab. Later."
        hide sasha with easeoutright
        "The goodbye is so abrupt I almost don't have time to object, try as I might."
        play sound door_slam
        "Sasha is gone before I have a chance to stop her, having been unable to really get a word in for a little while now."
        "Slowly, I slump back down onto the couch, cursing myself for hurting her so much."
        show bree at center, zoomAt (1.25, (640, 880)) with ease
        "I almost don't notice [bree.name] sitting besides me until I feel her hand on my back, slowly rubbing it in an attempt to console me."
        show bree sad
        bree.say "Um, you really liked her, didn't you?"
        show bree sadsmile
        mike.say "...Yeah, I think I did."
        "I don't see any point in lying at this point, even taking into account who I'm talking to."
        "A silence follows, one that I can tell that [bree.name] is using to consider what her reaction should be."
        "I can't bring myself to break it, letting the hand on my back calm me down surprisingly effectively, before [bree.name] practically whispers to me."
        show bree sad
        bree.say "I was going to leave too."
        show bree gloomy
        mike.say "You were?"
        show bree sad
        bree.say "Yeah I um."
        show bree talkative
        bree.say "You remember when I told you that trust was important to me, right?"
        show bree gloomy
        mike.say "Of course I remember."
        show bree talkative
        bree.say "I was so upset when I figured it out, it was like my worst fears had come true, but."
        bree.say "I think I'll stay."
        show bree sadsmile
        "She hardly seemed convinced in her own words, but they were enough to send relief coursing through my veins."
        mike.say "Really?"
        show bree talkative
        bree.say "Um, yeah But like, you can't do this ever again."
        show bree sad
        bree.say "Please, please don't do this again."
        bree.say "I want to trust you, that you'll be better, but that's really hard right now."
        bree.say "I don't think I could handle it if you ever cheated on me again."
        show bree gloomy
        mike.say "[bree.name], I promise, I'll never do it again."
        mike.say "Consider the lesson learned, I swear."
        mike.say "If there's anything I can do to try and get things back to normal, I will."
        show bree sad
        bree.say "I don't know if things can ever really go back to normal anymore, [hero.name]."
        show bree talkative
        bree.say "But um, we can try at least."
        show bree sadsmile
        "I nod, thankful that [bree.name]'s at least trying to be so understanding. My arms wrap around her on their own, holding her close."
        show bree cry at startle
        "Apparently, that was enough to open the floodgates, as the tears that she'd been holding back for so long begin pouring into my shoulder."
        "We stay like that for a while, before eventually [bree.name] calms down."
        "After a little longer of sitting in silence, she announces that the evening has worn her out, and she's going to head to bed, leaving me alone to think about the two girls."
        $ sasha.set_gone_forever()
        $ Room.find("bedroom3").hide()
    else:
        "I fall silent."
        show bree dazed
        "I don't know what I can say to make this better. I can't tell if trying and failing might even be worse, so I just hang my head in shame."
        show sasha vangry
        sasha.say "You're pathetic."
        show sasha sad
        show bree sad
        bree.say "Aren't you even going to try and explain yourself?"
        show bree gloomy
        mike.say "What can I say to make this better?"
        show sasha vangry
        sasha.say "It's too late for words, jackass."
        show sasha upset
        mike.say "Then what do you want from me?"
        mike.say "I'm sorry, I really am."
        show sasha vangry
        sasha.say "I don't believe a word of that. You're only sorry because we caught you."
        show sasha upset
        show bree sad
        bree.say "How could you do this, [hero.name]?"
        show bree gloomy
        mike.say "I don't know, alright?"
        mike.say "I don't know why I cheated on you both."
        show sasha vangry
        sasha.say "Well that just makes everything better then, doesn't it?"
        show sasha angry
        mike.say "Of course it doesn't."
        show sasha vangry
        sasha.say "Then try. Put in some sort of effort to prove that you're actually sorry."
        show sasha upset
        mike.say "I just."
        mike.say "I don't know what to tell you."
        show bree cry at startle
        "[bree.name] is crying again, her tears streaming to the floor as I struggle to talk my way out of the situation."
        show sasha vangry
        sasha.say "Well I know what to tell you."
        sasha.say "We're moving out."
        show sasha angry
        mike.say "Wait, you're what?"
        show bree sad
        bree.say "We're moving out, [hero.name]."
        show bree gloomy
        show sasha vangry
        sasha.say "We just finished the details. We leave tonight."
        show sasha angry
        mike.say "Where are you going?"
        show sasha vangry
        sasha.say "I'm crashing on a friend's couch and [bree.name]'s taking their guest room."
        show bree sad
        bree.say "I'll um probably go home tomorrow."
        show bree gloomy
        mike.say "Home? You mean out of the city?"
        show sasha vangry
        sasha.say "We can't live with you anymore, [hero.name]."
        sasha.say "I can barely stand just talking to you right now."
        show sasha angry
        show bree sad
        bree.say "You betrayed my trust, even after I told you how important it was to me."
        bree.say "I can't stay here any more. You've tainted this place."
        show bree gloomy
        mike.say "You don't have to move out though!"
        show sasha vangry
        sasha.say "Yeah, we do. Just be glad we gave you warning."
        sasha.say "We were just going to leave a note."
        show sasha angry
        mike.say "I Thanks?"
        "The sound of a car pulling up outside, then beeping it's horn, interrupts the conversation."
        show bree sad
        bree.say "I think that's for us."
        show bree dazed
        show sasha whining
        sasha.say "He's a little early, but alright."
        sasha.say "Let's go get our bags [bree.name]. Leave [hero.name] here."
        show sasha sad
        show bree sad
        bree.say "Yeah hum, let's go."
        hide sasha
        show bree gloomy at center, zoomAt (1.25, (640, 880))
        with easeoutright
        "I wasn't expecting it to be so sudden, and for a moment I'm shocked."
        mike.say "Wait!"
        show bree sad
        bree.say "Why?"
        bree.say "What's the point, [hero.name]?"
        bree.say "You're just going to lie to me again."
        show bree gloomy
        mike.say "[bree.name], no, I-"
        bree.say "[hero.name], please just stop."
        show bree cry
        bree.say "I'm sick of the lying If you aren't sorry, just say so."
        bree.say "I know you never liked me, that you just wanted sex."
        show bree gloomy
        mike.say "[bree.name], that isn't true."
        show bree cry
        bree.say "...That's what it feels like."
        show bree gloomy
        sasha.say "[bree.name]! He isn't going to wait forever!"
        show bree cry
        bree.say "I um I should go."
        show bree gloomy
        mike.say "You don't even have your things. Just stay, one night, let's talk about this, [bree.name]."
        show bree at center, zoomAt (1.25, (940, 880)) with ease
        "My words give her pause, and for a brief second I'm hopeful as she turns away from the door to her room, but instead of walking towards me, she walks straight past me towards the door."
        show bree cry
        bree.say "I'll hum send someone for my things tomorrow."
        hide bree dazed with moveoutright
        "And with that, I was left alone."
        play sound door_slam
        "The door slammed shut behind Sasha, and seconds later the vehicle outside drove away, vanished past a corner before I could get to the door to even see it leave."
        "I got the nasty feeling that I would never see either of them again."
        $ bree.set_gone_forever()
        $ Room.find("bedroom2").hide()
        $ sasha.set_gone_forever()
        $ Room.find("bedroom3").hide()
    return

label bree_sasha_showdown_2:
    scene bg livingroom with dissolve
    "There's been a palpable tension in the air for a couple of days now, making it awkward to spend time around the house."
    "I guess it's pretty much one hundred percent my own fault, as I was the one that had to try to have his cake and eat it."
    "Or more specifically have his [bree.name] and eat Sasha..."
    "It honestly seemed like a good idea at the time, and I was sure that I could deal with it - so long as no one got pregnant."
    "Of course, the moment that I allowed that thought to enter into my head, I should have known at least one of them would."
    "But never in my worst nightmare did I imagine a scenario where they'd both be pregnant!"
    "Before this, it was hard enough to keep on sleeping with both of my housemates under the same roof and keep it a secret."
    "Adding the two pregnancies into the mix made the complexity of the lies and deception I've had to pull off just that much worse!"
    "There was just no way they could fail to notice each other were pregnant at the same time."
    "Especially not when their bellies started to swell and all the other signs showed up."
    "If I'm getting it right, both [bree.name] and Sasha should think that I'm only screwing them and the other was knocked up by some dumb asshole."
    "(Which is probably not too far from the actual truth in both cases...)"
    "The one ace that I still hold is the fact that I insisted to each of them that we keep our relationship a secret from the other."
    "At the time I claimed it was to keep the other housemates from either getting jealous or making living under the same roof uncomfortable."
    "But right now, it's probably the only thing keeping me from being skinned alive by the pair of them."
    "I'd have hidden away in my room for the sake of not getting caught in between them."
    "But I figure that just gives them so many more chances to get talking."
    "And if they do, how long before something incriminating slips out?"
    show bree zorder 2 at center, zoomAt(1.0, (340, 720)) with easeinleft
    "That's why, when [bree.name] waddles into the living room, I'm sitting on the sofa and watching TV."
    show bree gloomy at center, traveling(1.25, 0.3, (440, 1000))
    "She virtually collapses beside me, moaning and rubbing her knuckles into the small of her back."
    show bree sad
    bree.say "[hero.name], my back's aching!"
    show bree smile
    bree.say "Would you give me a massage?"
    show bree normal
    "How can I honestly refuse without it looking massively suspicious?"
    "So I nod and oblige her, all the time praying that I can get it over and done with before..."
    show sasha shout zorder 1 at center, zoomAt(1.0, (940, 720)) with easeinright
    sasha.say "Hey, [hero.name], hey [bree.name]!"
    sasha.say "I SWEAR that our bodies are synchronising because of our babies or something."
    sasha.say "That's just what I could do with right now!"
    show sasha normal
    "I nod, trying to keep both of them sweet."
    show sasha stuned
    "But I can already see the slightly puzzled look on Sasha's face at finding her baby's father massaging another woman."
    show bree stuned
    "And just the same, I can feel [bree.name]'s eyes on me."
    "She's frowning as she tries to figure out why Sasha would think she can ask for me to treat her in the same way as I would my pregnant girlfriend."
    mike.say "Erm...maybe a little later?"
    mike.say "When I...get the feeling back in my hands?"
    show sasha annoyed at center, traveling(1.25, 0.3, (880, 1000))
    show bree at center, zoomAt(1.25, (400, 1000)) with ease
    "Sasha makes a harrumphing sound and sits down on the opposite side of me to [bree.name]."
    show bree talkative
    bree.say "What's the matter, Sasha - wouldn't your own man give you a massage?"
    show bree normal
    show sasha upset
    "Suddenly I can see anger flare in Sasha's eyes."
    "To [bree.name], the comment must have sounded pretty innocent, based on the circumstances."
    "But to Sasha, it has to sound like she's being taunted for me paying attention to [bree.name] when I should be giving it to her."
    show sasha vangry
    sasha.say "No, [bree.name] - he's too busy rubbing his hands all over little blonde sluts that got knocked up by some douchebag!"
    show bree surprised at center, zoomAt(1.0, (400, 1000)), startle
    bree.say "Ooh, that sounds harsh!"
    bree.say "Hey...wait a minute!"
    show bree annoyed
    "I instinctively curl myself up into a ball as the argument intensifies around me."
    "I could try to step in, or maybe make a run for the door."
    "The noble thing, I suppose, would be to come out and tell them both the truth, consequences be damned."
    "But it just seems a little late to start being honest."
    show bree vangry
    bree.say "Did you just call me a SLUT?!?"
    show bree angry
    show sasha vangry
    sasha.say "What else should I call you, huh?"
    sasha.say "I walk in on you getting a rub down from the father of my baby."
    sasha.say "And you have the audacity to rub it in my face!"
    show sasha angry
    "And there it is, the statement that's going to seal my fate..."
    show bree surprised
    bree.say "What...wait..."
    bree.say "What do you mean the father of YOUR baby?"
    show bree stuned
    show sasha vangry
    sasha.say "I mean what I said - [hero.name]'s the father of my baby."
    sasha.say "I thought you knew that?!?"
    show sasha upset
    show bree vangry
    bree.say "No, he's the father of MY baby!"
    bree.say "I thought you knew that?!?"
    show bree angry
    show sasha vangry
    sasha.say "But, he told me you were knocked up by some deadbeat asshole!"
    bree.say "He told me the same thing - about you!"
    show bree at startle
    show sasha upset at startle
    "As one, they look down at me."
    show sasha at center, zoomAt(1.25, (940, 880))
    show bree at center, zoomAt(1.25, (340, 880))
    with ease
    "And I think I finally get what people mean when they say 'if looks could kill'."
    "I honestly can't hear all of the things that [bree.name] and Sasha are saying as they rain down slaps and punches on me."
    "But I'm going to go out on a limb and guess that none of it is particularly pleasant in nature."
    hide bree
    hide sasha
    with easeoutright
    "What I do hear though, is the sound of them both stomping upstairs to their rooms."
    "Then drawers and wardrobes being thrown open so that hastily grabbed bags can be stuffed with clothes."
    "I don't need to have someone sit me down with a slideshow to know what's happening right now."
    show sasha upset zorder 1 at center, zoomAt(1.25, (940, 880))
    show bree angry zorder 2 at center, zoomAt(1.25, (340, 880))
    with easeinright
    "When they both reappear, clutching their bags and with tears in their eyes, I choose to keep my mouth shut."
    "I just stand in the hallway, staring at my feet like a scolded child."
    show bree sad
    bree.say "Don't you go into my room, you hear me?"
    bree.say "I'll send someone over for the rest of my stuff!"
    play sound punch_hard
    pause 0.2
    show bree angry at center, zoomAt (1.4, (610, 980))
    with hpunch
    "She punctuates this with a fist to the jaw that I did not see coming."
    hide bree with easeoutright
    pause 0.1
    show sasha at center, zoomAt(1.25, (540, 880)) with ease
    "Clutching my face, I only hear Sasha approaching at the last moment."
    show sasha vangry
    sasha.say "Same goes for me too."
    sasha.say "But if I ever see you again, I'll slice off your goddamn balls!"


    pause 0.2
    show sasha at center, zoomAt (1.4, (640, 980))
    with vpunch
    "Her parting gift is a swift knee to the same part of my anatomy she just threatened."
    scene bg livingroom at blur(16), dark with dissolve
    play sound body_fall
    "I collapse to the floor, rolling around in pain."
    play sound door_slam
    "I only half hear the sound of the door slamming shut."
    "And then there's silence, which is something that I suppose I'll have to try and get used to from now on."
    $ bree.set_gone_forever()
    $ sasha.set_gone_forever()
    $ Room.find("bedroom2").hide()
    $ Room.find("bedroom3").hide()
    return

label bj_birthday:
    show bg livingroom
    if renpy.has_label("home_harem_achievement_2") and not game.flags.cheat:
        call home_harem_achievement_2 from _call_home_harem_achievement_2_1
    "I enter the living room."
    "Nothing crazy could happen here, right?"
    bree_sasha "Hey, [hero.name]"
    show sasha underwear zorder 4 at center, zoomAt (1.0, (840, 740))
    show bree underwear zorder 5 at center, zoomAt (1.0, (440, 740))
    "Suddenly, I'm bombarded with the sight of both of my roommates standing right before me, down to their lingerie."
    mike.say "Whoa! [bree.name]!? Sasha!? The hell is all this about?"
    show sasha shout
    sasha.say "Hey, [hero.name]."
    sasha.say "You know what day it is."
    show sasha normal
    show bree smile
    bree.say "I, like, don't think he could have forgotten, right...?"
    show bree normal
    mike.say "Today?"
    "I think about it a moment."
    mike.say "Wait... did you two... did you remember my birthday?"
    show sasha shout
    sasha.say "Remember it?"
    show sasha a normal
    "Sasha asks, scoffing, her hands on her hips."
    show sasha shout
    sasha.say "I think we did a lot more than that!"
    show sasha normal
    show bree smile
    bree.say "Or... I mean technically..."
    show bree normal
    show sasha shout
    sasha.say "We're GOING to do a lot more than that."
    show sasha a happy
    sasha.say "Go ahead, [hero.name] strip."
    show bree smile blush
    bree.say "Um, take your time if you want... I mean, it's your day, do whatever you want...?"
    show bree normal
    "The two are like Yin and Yang, Sasha seems happy to stand there, confident, while [bree.name] seems more embarrassed about the situation."
    "I don't bother with questions though, and simply do as I'm told, and soon, I'm naked before them, intrigued and excited."
    show sasha a shout
    sasha.say "Now, sit on the couch."
    show sasha b normal topless with dissolve
    "Sasha's fingers hooks over the straps of her bra then she slides the straps over her shoulders."
    show bree smile
    bree.say "Yeah, just um... Relax."
    show bree normal
    "[bree.name] stammers her line, almost as though it was rehearsed, while shimmying out of her panties."
    show bree naked
    show sasha naked
    with dissolve
    "When I glance at them again, [bree.name] and Sasha stand on either side of the couch."
    "Both of my roommates have removed their clothes and smile down at me with lust and intent."
    show bree smile
    bree.say "I hope you enjoy this, [hero.name]..."
    show bree normal
    show sasha shout
    sasha.say "Now then!"
    show sasha normal
    show bree smile
    bree.say "Let's get down to business shall we?"
    show bree normal
    "The two nod at each other."
    "They must have rehearsed this, or at least planned it out."
    "For a moment, I imagine the two of them alone, nude, and if my cock wasn't already standing as straight as a candle, I'd immediately get hard from that."
    show sasha at center, traveling (1.2, 1.0, (840, 800))
    show bree at center, traveling (1.2, 1.0, (440, 800))
    "The two of them lean in over the couch, each of them giving me their fluttering bedroom eyes."
    show sasha happy at center, traveling (1.4, 1.0, (860, 1050))
    show bree happy at center, traveling (1.4, 1.0, (420, 1050))
    "As they climb up onto the couch, [bree.name] on my left and Sasha on my right, the soft words whisper gently to my ears."
    show bree smile
    bree_sasha "Happy Birthday to you..."
    show bree normal
    "The song continues as they synchronize themselves, sliding their fingers down my body."
    "Soon, the two lay there, their warm bodies up against my own, pressed against my spread legs."
    "I reach up and hold onto both of them, sliding my own fingers over their smooth skin."
    hide bree
    hide sasha
    show bj breesasha bree sasha sashaopen
    with fade
    "Together, they wrap their fingers around my shaft, and also together, they roll their tongues out, licking up along my length."
    mike.say "O... oh wow..."
    show bj breesasha bree sasha breesuck
    mike.say "You two... you work great together."
    sasha.say "Only the best for the birthday boy..."
    show bj breesasha bree sasha sashaopen sashasuck
    bree.say "I just wanted to repay you, for how good roommates you both have been."
    show bj breesasha bree sasha both sashaclosed breeclosed
    "Again, they lick up my shaft, up over the glans and over the tip."
    "Their tongues touch, and they both stare up at me, a chuckle shared between the two of them before they wrap their lips around the head."
    "The two best roommates in the world make out with my cock in the middle of it all, their tongues dancing over my skin as their hands move in sync to jerk me off."
    "What did I do to deserve the greatest roommates in the world?"
    "I wonder this as the excitement of their actions tingles up through my body."
    show bj breesasha bree sasha sashaopen -sashasuck cumshot with vpunch
    "I can't hold back and, with a groan, I release, shooting up onto them."
    with vpunch
    "Cum sprays up onto their faces, getting them nice and covered by my birthday jizz."
    show bj breesasha bree sasha sashaopen breefacial sashafacial nodick -cumshot
    "The girls smile up at me, batting their half-lidded eyes up in my direction."
    sasha.say "Enjoy this view, birthday boy."
    if randint(1, 2) == 1:
        hide bj breesasha
        show breesasha kiss naked cum at flip
        with fade
        "I watch as [bree.name] and Sasha embrace one another and lean in for a kiss."
        "Their lips part and they touch, tongues darting into each other's open mouths."
        "And the whole time they're doing this, my cum is still running down their faces!"
        "It drips and pools from one of them to the other, and they don't even seem to notice."
        "Some falls onto their lips and tongues, which they lick up and swallow too!"
    else:
        "Sasha takes a finger and slips a drop of my cum off of her face."
        show bj breesasha bree sasha sashaopen breesuck breefacial sashafacial -nodick
        "She hands it to [bree.name], who wraps her lips around my cock, moaning quietly in delight at the taste."
        hide bj breesasha
    scene bg livingroom
    show bree naked smile cum at left5
    show sasha naked cumface at right5
    with fade
    bree.say "Alright [hero.name], um, I've got another surprise for you now."
    show bree normal
    mike.say "Something else?"
    show bree happy
    bree.say "Yeah..."
    bree.say "The Cake!"
    hide bree
    hide sasha
    $ game.pass_time(1)
    return

label bree_sasha_threesome:
    if renpy.has_label("home_harem_achievement_2") and not game.flags.cheat:
        call home_harem_achievement_2 from _call_home_harem_achievement_2_3
    scene bg bedroom1 with fade
    $ game.flags.bree_sasha_threesome = True
    $ game.flags.threesomelastnight = TemporaryFlag(True, 2)
    $ sasha.sexperience += 1
    $ bree.sexperience += 1
    "It still feels bizarre to me to have come to the point where I'm living with two very different, but equally desirable women."
    "Even more so that my luck has turned around to the degree that not one, but both of them are also involved in a sexual relationship with me."
    show bree naked blush at left5
    show sasha naked at right5
    with dissolve
    "A part of me can't keep from glancing from [bree.name] to Sasha and back as they recline, naked on the bed waiting for me to join them."
    "Seeing me hesitate, they chuckle wickedly and shoot each other a conspiratorial look."
    show bree happy at startle
    bree.say "What are you waiting for?"
    show sasha joke
    sasha.say "Yeah - I promise we will bite!"
    show sasha normal at center, zoomAt (1.2, (840, 800))
    show bree blush at center, zoomAt (1.2, (440, 800))
    with fade
    "I climb onto the bed between them, still not sure where to look thanks to the appealing nature of each girl waiting for me."
    "Before I can decide where to start, [bree.name] and Sasha rise to their knees."
    show sasha happy at center, traveling (1.4, 1.0, (860, 1050))
    show bree happy at center, traveling (1.4, 1.0, (420, 1050))
    "[bree.name] comes at me from the left and Sasha from the right, leaning in to kiss me at the corners of my mouth."
    "Neither of them kisses me full on the lips, but instead they tease me with their tongues and then begin to move downwards."
    "At the same time, I can feel their breasts brushing against my chest, and I reach out to take one from each girl in my hands."
    "Pinching and squeezing at their nipples, I enjoy the subtle differences in feel between the two breasts as I massage them."
    show sasha flirt
    show bree mindless
    "[bree.name] moans in appreciation as I twist her nipple between my fingers, and Sasha gives a delighted growl."
    show bree happy
    "For a moment, the three of us are held there, just enjoying the sensations of each other."
    "But I can feel myself getting stiff and the heat from the girls is almost palpable in the air."
    "There's no way that this is going to be just a matter of kisses and the fondling of breasts, and everyone knows as much."
    "Suddenly there are hands, lips and bodies everywhere."
    "No one seems to be taking control, so I decide to push for what I want right there and then."
    show bree normal
    menu:
        "Sasha eat [bree.name] out":
            "As if Sasha and I are communicating on a psychic level, I press [bree.name]'s shoulders down while she does the same with her legs."
            "[bree.name] doesn't resist, her eyes instead focused on my dick as it now hovers over her face."
            hide sasha
            hide bree
            show bree rough oral bedroom naked
            with fade
            "I take hold of her head and gently guide her mouth as she takes the tip inside."
            show bree rough oral bedroom open sasha naked with dissolve
            "Just as I start to feel the unbelievable sensation of her tongue snaking around the head, Sasha leans herself towards [bree.name]'s lower lips."
            "I watch as the other girl begins to tease and tickle [bree.name] with her tongue, expertly probing and licking, more with each passing second."
            show bree rough oral bedroom open sasha squirt naked
            "Unable to see what is being done to her, I feel [bree.name]'s body shudder from the pleasure, making her attentions to me all the more intense and unpredictable."
            "I feel guilty to admit it, but part of me feels as though it's Sasha using her mouth on me, like we've turned [bree.name] into nothing more than a human toy for our own pleasure."
            show bree rough oral bedroom open sasha cum naked with hpunch
            "Shamefully turned on by the mere thought, I can't keep myself from cumming sooner than I wanted."
        "Sasha use a strap-on on [bree.name]" if bree.sub >= 25:
            $ sasha.flags.strapon_known = True
            hide bree
            hide sasha
            show bree doggy sasha front
            with fade
            "I guide [bree.name] down onto all fours and she doesn't resist me, her eyes instead fixated on my cock as it hangs before her face."
            "Before she can reach out for it with either her hands or lips, Sasha comes up behind her, taking hold of her arms."
            "[bree.name]'s cheeks redden at the sudden realisation she's being forced into a submissive role, but we press on regardless of her reaction."
            show bree doggy suck
            "As Sasha forces her forwards and she accepts my dick into her open mouth, it's only then that I see the other girl has hastily strapped something around her own waist and groin."
            show bree doggy suck sasha scream
            "Sasha grins wickedly at me over [bree.name]'s back as she lowers the impressively-sized strap-on she's wearing and pushes from the opposite direction."
            "[bree.name]'s shocked whimperings of surprise translate into an unpredictable and yet exciting sensation for me, as she moans around my dick."
            "Sasha enthusiastically makes use of the strap-on, thrusting away inside of [bree.name] until she's covered in a sheen of sweat from the effort."
            show bree doggy suck sasha ahegao
            "We lock eyes, both majorly aroused by the way in which we're using [bree.name] as a vessel for our own pleasure."
            show bree doggy deep pull sasha ahegao with hpunch
            "I use the last of my energy to thrust myself still further into [bree.name]'s throat, so that she had no choice but to accept it."
            show bree doggy deep pull cuminmouth sasha ahegao with hpunch
            "Moments later, I feel myself losing it and releasing all that I have in one go."
    hide bree
    show multisleep homeharem bree sasha
    with fade
    "Nobody speaks as we lie in a slick pile of bodies and limbs, cooling rapidly but still feeling the aftershocks."
    "They say that people only complain if they're unhappy with the service."
    "So I'm happy to read the silence in the bedroom as quiet satisfaction on the part of [bree.name] and Sasha."
    "I know for sure that I have no reason whatsoever to complain."
    call sleep (["bree", "sasha"]) from _call_sleep_27
    return

label bree_sasha_threesome_2:
    if renpy.has_label("home_harem_achievement_2") and not game.flags.cheat:
        call home_harem_achievement_2 from _call_home_harem_achievement_2_2
    scene bg bedroom1
    $ game.flags.bree_sasha_threesome = True
    $ game.flags.threesomelastnight = TemporaryFlag(True, 2)
    $ sasha.sexperience += 1
    $ bree.sexperience += 1
    show sasha zorder 4 at center, zoomAt (1.0, (840, 740))
    show bree zorder 5 at center, zoomAt (1.0, (440, 740))
    with fade
    "As much as there's the excitement and thrill of living out a threesome, there's also always a faint feeling of unspoken tension hanging over it all too."
    "How could there not be, especially when the genders of the people involved means that you have two of one thing and one of the other to go around?"
    "No one ever talks about it beforehand, probably wouldn't even if they had the chance for fear of looking like they were trying to steal the lion's share for themselves."
    "But I can always feel the slight sense of competition between [bree.name] and Sasha before we get up to something as a trio."
    show sasha happy at center, traveling (1.4, 5.0, (860, 1050))
    show bree blush at center, traveling (1.4, 5.0, (420, 1050))
    "Neither of them would admit it, but they're both wondering just who's going to be the one to get to ride my dick."
    "For my part, I know that I should probably make sure that harmony is achieved and that nobody ends up feeling left out."
    "But I'm only human - how can I pretend that knowing two such hot girls are basically trying to outdo each other for that same reason?"
    show sasha normal underwear
    show bree underwear
    with dissolve
    "I feel like that right now, with the door to my room firmly closed behind us and the girls stripping off in front of me."
    "As I take off my own clothes, I can't help feeling like some kind of prize stallion that's having broodmares paraded in front of him."
    "Each one of them is enough to make me desperate on their own, but together it's going to be almost impossible to choose between them."
    show sasha naked
    show bree naked
    with dissolve
    "In the end, I'm, just going to have to come down and make a choice, for better or worse."
    show sasha joke
    "It's just then that I catch the twinkle in Sasha's eye."
    show sasha normal
    "Maybe it's nothing more than my imagination, desperately looking for an excuse to pick one over the other."
    "But there seems to be something darker and more sultry in Sasha's gaze - spice as opposed to [bree.name]'s own delightful sweetness."
    "Whether I'm right or wrong, I'll go with that."
    "If I wait and ponder it any longer, I'm afraid that the moment will pass and the mood die completely."
    if sasha.is_visibly_pregnant:
        "Sure, Sasha didn't have much trouble turning me on before she fell pregnant - after all, one kind of followed on from the other!"
        "But there's just something about the sight of her with that big, round belly that makes me want to do it all over again."
        "As I take her by the hand and make it plain that I want her in front of me, back to belly, she sways like a beautifully ripe fruit."
        "Once she's standing in front of me, I feel as though I'm about to have sex with a primeval fertility icon brought magically to life."
    elif sasha.flags.boobjob:
        "Don't get me wrong, I love the natural size and shape of [bree.name]'s breasts."
        "But there's just something so wonderfully fake and dirty about the implants that pump Sasha's up to a comparable size."
        "As I take her by the hand and make it plain that I want her in front of me, back to belly, they bounce and sway like rubber balls."
        "Even when she's got her back to me, I can still see them sticking out in front of her!"
    elif sasha.flags.haircut:
        "I reach out and take hold of Sasha's hand, leading her to stand before me and then turn her back."
        "Her ass is mere inches away from my already rising cock, and I can see the black roots of her blonde hair up close."
        "I don't know exactly why, but the sight of where the black meets the blonde always gets me worked up."
        "Maybe it's because it makes her look so delightfully trashy and cheap..."
    elif bree.is_collared and sasha.is_collared:
        "[bree.name] and Sasha are obediently standing before me in their collars, a fact that should make the whole thing that much easier."
        "But still it feels a hard decision to make as I take hold of Sasha's lead and make it plain that she's the one I'm set on actually fucking tonight."
        "While she looks instantly delighted to have been chosen, I can see [bree.name] trying to hide her disappointment so as not to be guilty of spoiling the moment."
        "Maybe that's what inspires me to be a little more forceful than I might otherwise have been as I tug Sasha's lead to have her trot around in front of me."
    hide bree
    hide sasha
    show threesome breesasha
    with fade
    "Eager to begin, Sasha clambers hastily onto the bed before me, looking back over her shoulder to be sure that I'm following."
    "She need not have worried in the slightest, as her thighs moving in this way means that I'm treated to an intimate view of what lies between them."
    "Even though we've hardly begun, I can see that her lips are becoming ever more slick in anticipation."
    "In fact, I swear that I can almost hear them make a liquid sound as she moves."
    "And right now, there's nowhere that I want to be more than right spot right there."
    "In all, Sasha can't be more than a couple of feet onto the bed before I'm up and after her."
    show threesome breesasha squeezesasha sashapleasure
    "I catch her none to gently around the waist, taking her in a firm grip that makes it clear I don't intend for her to go any further."
    "She yelps in genuine surprise at the feel of me grasping her and taking full control of the proceedings."
    show threesome breesasha sashanormal
    "But I also note with the faint beginnings of a smile that she offers no protests and makes no effort to break my hold upon her."
    "Keeping my hands in the same position as they were when I grabbed her a moment before, I now pull Sasha back towards me."
    show threesome breesasha vaginaltip
    "At the same time I thrust myself forwards to meet her, trusting to the design of nature to ensure that my aim is true."
    menu:
        "Fuck Sasha's pussy":
            $ hole = "p"
            "For a second to two I think that my cock is going to go straight up her ass."
            "But then I feel the slick sensation of her pussy, and it spurs me to push on even more hastily than before."
            show threesome breesasha vaginal sashapleasure
            "I don't enter Sasha in the most gentle or smooth of motions, but this isn't an occasion for subtle entrances."
            "Even though she's already more than a little wet in anticipation, I still need to keep up the pressure and push hard to make it in one go."
            "Sasha moans, deep and long as I keep on going, making sure that my cock's as deep into her as it will go."
        "Fuck Sasha's ass":
            $ hole = "a"
            "I was kind of aiming for Sasha's pussy, already anticipating the wet sensation of her lips around my cock."
            show threesome breesasha anal sashapleasure
            "But somehow my aim seems to be off, and it ends up jammed between her buttocks instead."
            "As soon as she feels the head in her ass, Sasha yelps with surprise."
            sasha.say "Oh my..."
            sasha.say "My ass..."
            sasha.say "That's my ass!"
            "I don't pause for a second, not giving Sasha the chance to object to what I'm doing."
            "Instead I give it one massive push, thrusting myself into her ass in one move."
            "Soon enough I feel her muscles begin to yield, and her yelps turn into moans of pleasure."
    "As I show no signs of mercy to Sasha, I comfort myself with the clear evidence that she's liking this kind of treatment."
    "All the while she's gasping and moaning in what can only be a rough and breath-taking kind of pleasure."
    "And there's going to be plenty more of that kind of treatment to come, as the rough push to get inside of her has made me hungry for more of the same."
    "With every single thrust that I make into her, I feel like I'm trying to fill Sasha and get as deep in as possible."
    "Each movement of mine seems to shake her to the core, sending quivers and spasms through her muscles."
    "By now her moans have begun to turn into cries, and she's making them completely in time with my thrusts in and out of her."
    show threesome breesasha dripbree
    "[bree.name] begins to caress me in the hope of getting some attention for herself."
    "I instantly feel bad for having almost forgotten that she was even in the room with us, let alone supposed to be a partner in our love-making."
    "Unable and more than a little unwilling to be distracted from what I'm doing with Sasha, I let go of her waist with one hand and reach out towards [bree.name]."
    menu:
        "Finger [bree.name]'s pussy":
            show threesome breesasha fingers breepleasure
            "Guided more by instinct than anything else, I feel for the space between her thighs."
            "Luckily for me, I find my hand gripped firmly and pulled straight towards what had been my ultimate goal."
            "All I can say is that she must have been getting pretty excited from simply watching Sasha and I go at it."
            "[bree.name]'s crotch is wet and warm to the touch, and she wastes no time in pressing my fingers against her lips with almost desperate force."
            show threesome breesasha vaginalfing
            $ bree.love += 1
            "Before it feels like any amount of time has passed, my fingers are finding their way ever deeper into her pussy."
            "Unable to fully divide my attention between the two tasks, I find myself pushing into Sasha and rubbing away at [bree.name] with one single rhythm."
            "I can't honestly tell if Sasha senses a change in that same rhythm as I'm forced to accommodate [bree.name]'s needs, or else hears the other girls own sounds of pleasure."
            show threesome breesasha -anal -vaginal
            "Either way, she shifts beneath me and I can't keep my cock from slipping out of her as she does so."
            "At first I can only think that she must be annoyed at losing the largest share of my attention."
            "But then she nods almost desperately, urging me to keep going as I pleasure the both of them at once!"
        "Finger [bree.name]'s ass":
            show threesome breesasha fingers breepleasure
            "Guided more by instinct than anything else, I feel for the space between her buttocks."
            "Luckily for me, I find my hand gripped firmly and pulled straight towards what had been my ultimate goal."
            "All I can say is that she must have been getting pretty excited from simply watching Sasha and I go at it."
            "[bree.name]'s ass is slick with sweat and warm to the touch, and she wastes no time in pressing my fingers against her hole with almost desperate force."
            show threesome breesasha analfing
            $ bree.sub += 1
            "Before it feels like any amount of time has passed, my fingers are finding their way ever deeper into her ass."
            "Unable to fully divide my attention between the two tasks, I find myself pushing into Sasha and rubbing away at [bree.name] with one single rhythm."
            "I can't honestly tell if Sasha senses a change in that same rhythm as I'm forced to accommodate [bree.name]'s needs, or else hears the other girls own sounds of pleasure."
            show threesome breesasha -anal -vaginal
            "Either way, she shifts beneath me and I can't keep my cock from slipping out of her as she does so."
            "At first I can only think that she must be annoyed at losing the largest share of my attention."
            "But then she nods almost desperately, urging me to keep going as I pleasure the both of them at once!"
        "Use dildo on [bree.name]'s pussy":
            "Guided more by instinct than anything else, I feel for the dildo that I always keep at my beside."
            show threesome breesasha dildo breepleasure
            $ bree.love += 2
            "And then I push it between [bree.name]'s thighs before anyone has the chance to object."
            "Luckily for me, I find my hand gripped firmly and pulled straight towards what had been my ultimate goal."
            "All I can say is that she must have been getting pretty excited from simply watching Sasha and I go at it."
            "[bree.name]'s crotch is wet and warm to the touch, and she wastes no time in pressing the dildo against her lips with almost desperate force."
            "Before it feels like any amount of time has passed, the toy finds its way ever deeper into her pussy."
            "Unable to fully divide my attention between the two tasks, I find myself pushing into Sasha and rubbing away at [bree.name] with one single rhythm."
            "I can't honestly tell if Sasha senses a change in that same rhythm as I'm forced to accommodate [bree.name]'s needs, or else hears the other girls own sounds of pleasure."
            show threesome breesasha -anal -vaginal
            "Either way, she shifts beneath me and I can't keep my cock from slipping out of her as she does so."
            "At first I can only think that she must be annoyed at losing the largest share of my attention."
            "But then she nods almost desperately, urging me to keep going as I pleasure the both of them at once!"
        "Use dildo on [bree.name]'s ass":
            "Guided more by instinct than anything else, I feel for the dildo that I always keep at my beside."
            show threesome breesasha dildo analdild breepleasure
            $ bree.sub += 2
            "And then, before anyone can object, I feel for the space between her buttocks."
            "Luckily for me, I find my hand gripped firmly and pulled straight towards what had been my ultimate goal."
            "All I can say is that she must have been getting pretty excited from simply watching Sasha and I go at it."
            "[bree.name]'s ass is slick with sweat and warm to the touch, and she wastes no time in pressing the dildo against her hole with almost desperate force."
            "Before it feels like any amount of time has passed, the toy finds its way ever way ever deeper into her ass."
            "Unable to fully divide my attention between the two tasks, I find myself pushing into Sasha and rubbing away at [bree.name] with one single rhythm."
            "I can't honestly tell if Sasha senses a change in that same rhythm as I'm forced to accommodate [bree.name]'s needs, or else hears the other girls own sounds of pleasure."
            show threesome breesasha -anal -vaginal
            "Either way, she shifts beneath me and I can't keep my cock from slipping out of her as she does so."
            "At first I can only think that she must be annoyed at losing the largest share of my attention."
            "But then she nods almost desperately, urging me to keep going as I pleasure the both of them at once!"
        "Spank Sasha":
            show threesome breesasha -squeezesasha sashanormal
            "Almost as soon as I do so, I feel an irresistible pull back towards Sasha."
            show threesome breesasha slapsasha sashapleasure
            play sound spank
            with hpunch
            "And the hand that I had intended to use to spank [bree.name] slaps Sasha's exposed buttocks instead."
            show threesome breesasha -slapsasha
            "Sasha yelps in surprise at the sudden blow, but she makes no effort to escape as I give her another."
            show threesome breesasha slapsasha slapedsasha
            play sound spank
            with hpunch
            "Already I can see her ass turning red from the blows, and she's beginning to pant desperately."
            "Far from putting her off, a little bit of corporal punishment seems to be getting Sasha even more excited!"
            show threesome breesasha -slapsasha
            "Part of me feels bad for ignoring [bree.name] in that moment, but it's pushed to one side as I indulge myself."
            show threesome breesasha slapsasha
            play sound spank
            with hpunch
            $ sasha.sub += 2
            "And all that I can see is the way that Sasha's buttocks wobble as I slap them over and over again."
            show threesome breesasha -slapsasha
        "Spank [bree.name]":
            show threesome breesasha slapbree breepleasure
            play sound spank
            with hpunch
            "My hand lands flat and hard on [bree.name]'s exposed buttocks, the clapping sound unexpectedly loud."
            show threesome breesasha -slapbree
            "[bree.name] yelps in surprise at the sudden blow, but she makes no effort to escape as I give her another."
            show threesome breesasha slapbree slapedbree
            play sound spank
            with hpunch
            "Already I can see her ass turning red from the blows, and she's beginning to pant desperately."
            show threesome breesasha -slapbree
            "Far from putting her off, a little bit of corporal punishment seems to be getting [bree.name] even more excited!"
            "And the same thrill sees me thrusting into Sasha with a renewed vigour too."
            "Soon enough, [bree.name] is gasping and moaning from the repeated slaps to her ass."
            show threesome breesasha slapbree
            play sound spank
            with hpunch
            "Her buttocks wobble and glow red as I slap them over and over again."
            show threesome breesasha slapbree
            $ bree.sub += 2
            "And at the same time, Sasha is panting as every slap makes me fuck her harder still."
            show threesome breesasha -slapbree
        "Spank [bree.name] and Sasha":
            show threesome breesasha -squeezesasha sashapleasure slapsasha breepleasure slapbree
            play sound spank
            with hpunch
            "My hand lands flat and hard on [bree.name]'s exposed buttocks, the clapping sound unexpectedly loud."
            show threesome breesasha -slapsasha -slapbree
            "And she barely has time to yelp in surprise before I land a second slap on Sasha's ass a second later."
            "Neither of them makes an effort to escape another slap to the buttocks."
            show threesome breesasha slapsasha slapbree slapedbree slapedsasha
            play sound spank
            with hpunch
            "Instead they quiver and quake in anticipation as I begin to get into a rhythm."
            show threesome breesasha -slapsasha -slapbree
            "Far from putting [bree.name] and Sasha off, a little corporal punishment seems to be getting them even more excited!"
            "Soon enough the pair of them are nodding their heads and moaning with pleasure as I spank them."
            show threesome breesasha slapsasha slapbree
            play sound spank
            with hpunch
            $ bree.sub += 2
            $ sasha.sub += 2
            "Their buttocks wobble and begin to glow read as I slap them over and over again."
            "And at the same time, Sasha is panting as every slap makes me fuck her harder still."
            show threesome breesasha -slapsasha -slapbree
    if hole == "p":
        show threesome breesasha vaginal
    else:
        show threesome breesasha anal
    show threesome breesasha squeezesasha squeezebree breepleasure sashapleasure
    "I've been working out at the gym like crazy the past couple of weeks."
    "And I've never felt better than I do right now, filled with life and energy."
    "But even so, I've been giving [bree.name] and Sasha all that I have to give."
    "And I can feel that my reserves are running low."
    "I know that I won't be able to go on like this for much longer."
    "Which is why it comes as a relief to feel that I'm about to cum."
    "The only problem is that I have to decide where I'm going to do it!"
    if randint(1, 2) == 1:
        menu:
            "Cum inside" if hole == "p":
                "The easiest thing to do would be to just keep right on going, thrusting into Sasha's pussy."
                show threesome breesasha creampie sashaahegao with vpunch
                $ sasha.love += 2
                "And so that's exactly what I do, devoting the very last of my strength to pounding her hard."
                with vpunch
                "Sasha seems to appreciate the effort, groaning as she feels me letting go inside of her."
                with vpunch
                "I can tell from the way her muscles are squeezing my cock that she's cumming too."
                "And the feeling makes the whole thing almost indescribable."
                "I keep right on until cum starts to seep out of Sasha and run down the inside of her thighs."
                "And then she collapses onto the bed, sliding off my cock as she does so."
            "Cum inside" if hole == "a":
                "The easiest thing to do would be to just keep right on going, thrusting into Sasha's ass."
                show threesome breesasha creampie sashaahegao
                with vpunch
                $ sasha.sub += 2
                "And so that's exactly what I do, devoting the very last of my strength to pounding her hard."
                with vpunch
                "Sasha seems to appreciate the effort, groaning as she feels me letting go inside of her."
                with vpunch
                "I can tell from the way her muscles are squeezing my cock that she's cumming too."
                "And the feeling makes the whole thing almost indescribable."
                "I keep right on until cum starts to seep out of Sasha and run down the inside of her thighs."
                "And then she collapses onto the bed, sliding off my cock as she does so."
            "Cum on Sasha's ass":
                show threesome breesasha -anal -vaginal -squeezesasha fap sashafap
                "I pull my cock out of Sasha at the last possible moment, just before I lose it."
                show threesome breesasha fx
                "She shudders and moans at the sensation, beginning to cum herself a second later."
                show threesome cumshot breesasha with vpunch
                "And then I shoot my load straight onto her ass, making her yelp with surprise."
                show threesome breesasha -fx -cumshot cum onsashabody with vpunch
                $ sasha.love += 1
                $ sasha.sub += 1
                "Streamers of hot, sticky white cum stripe Sasha's buttocks."
                with vpunch
                "And the stuff begins to succumb to gravity, running down the back of her thighs."
                "Sasha manages to remain upright until I'm spent, and then she collapses onto the bed."
            "Cum on [bree.name]'s ass":
                show threesome breesasha -anal -vaginal -squeezesasha fap sashafap
                "She shudders and moans at the sensation, beginning to cum herself a second later."
                show threesome breesasha fx onbree -sashafap breefap cumshot with vpunch
                "But then I turn to the side and shoot my load over [bree.name]'s unsuspecting ass."
                with vpunch
                "The sudden and unexpected sensation makes her yelp with surprise."
                show threesome breesasha -fx -cumshot cum onbreebody with vpunch
                $ sasha.love += 1
                $ sasha.sub += 1
                "Streamers of hot, sticky white cum stripe [bree.name]'s buttocks."
                "And the stuff begins to succumb to gravity, running down the back of her thighs."
                "Meanwhile, Sasha manages to remain upright until I'm spent, and then she collapses onto the bed."
        hide breesasha
        "One by one we end up laid in a pile of limbs, wrapped up in the sweaty bedclothes."
        "Nobody seems to have the energy left to be able too speak, just to pant and gasp with exhaustion."
        "But I can see that both [bree.name] and Sasha are smiling, with a satisfied look in their eyes."
        "And once I know that they're sated, I begin to feel the same way too."
        "At last I can relax, basking in the warmth of the afterglow that I created."
        if hole == "a":
            $ sasha.flags.anal += 1
        call sleep (["bree", "sasha"]) from _call_sleep_38
    else:
        hide threesome breesasha
        show cumshot breesasha blow blowjob closed handjob breesurprised
        with fade
        "But then she surprises me, and probably [bree.name] too, by pushing her down onto the bed and leaning over her to snatch my cock into her own mouth."
        "The sudden change from being the one making the effort to please two other people to having one of them pleasuring me alone is sharp and sudden."
        "It's all that I can do to keep from losing it the moment that Sasha's lips close around the head of my dick."
        show cumshot breesasha normal
        "She must sense that this means I'm about to cum, as she quickly releases me and waits poised for the climax."
        "But even so, there's no way to tell just what she intends to do when it finally arrives."
        if sasha.sub > bree.sub:
            show cumshot breesasha cumshoot with vpunch
            "Much to my surprise, and again to [bree.name]'s too, Sasha backs off just enough to let me cum all over the other girl's chest."
            show cumshot breesasha -cumshoot dickcum cum onbreebody onsashaface onbreeface spitedout breepleasure with vpunch
            "[bree.name] yelps and laughs in genuine surprise as the warm cum spurts and sprays onto her naked breasts."
            show cumshot breesasha lick tongueout limp
            "But even before I've finished losing myself over the prostrate female form before me, Sasha leans back in again."
            "This time she has her tongue out and ready, wasting no time in licking away at the lines of sticky, white fluid running down [bree.name]'s breasts."
            "Each and every mouthful that she laps up is a sensual experience for the both of them, as Sasha is sure to pay close attention to not missing a single drop."
            show cumshot breesasha swallow -spitedout
            "She chases the cum around [bree.name]'s nipples, between both breasts and finally down her stomach, swallowing each mouthful with relish."
        else:
            show cumshot breesasha blow creampie with vpunch
            "Sasha surprises us both with her skill, if not as to her intentions, when she somehow manages to catch most of the cum in her mouth."
            show cumshot breesasha dickcum cum onbreebody -creampie with vpunch
            "Only the smallest amount either misses her lips to spatter onto [bree.name]'s chest below, or else dribbles down Sasha's chin."
            show cumshot breesasha opened -blowjob limp
            "But then she looks down at the other girl with a mischievous smile on her face, lowering her head until they're mere inches apart."
            show cumshot breesasha lick
            "[bree.name] opens her mouth, meaning to ask what Sasha's up to, and that's all the opportunity that she needs for what comes next."
            show cumshot breesasha tongueout spitedout breepleasure
            "Quick as a flash, Sasha spits the mouthful of cum between [bree.name]'s breasts."
        hide breesasha with fade
        "Though I'm exhausted and drenched in sweat by the time the whole thing is over, I still feel that I can't be nearly as spent as either [bree.name] or Sasha."
        show multisleep homeharem bree sasha with fade
        "Both are sprawled on the bed before me, bathed not only in their own perspiration, but a good amount of my own cum as well."
        "I don't bother to offer any invitations or suggest that they stay to sleep in my room if they like, as I'm frankly too tired to care."
        "All I want to do is find a portion of the bedclothes that we haven't completely soaked between the three of us and collapse."
        "Finding both or either of them by my side when I finally wake up would be a plus, but I'm not about to let the thought of it's likelihood keep me awake even a second longer."
        if hole == "a":
            $ sasha.flags.anal += 1
        call sleep (["bree", "sasha"]) from _call_sleep_42
    return

label bree_sasha_male_ending:

    if renpy.has_label("home_harem_achievement_3") and not game.flags.cheat:
        call home_harem_achievement_3 from _call_home_harem_achievement_3
    scene bg beach with fade
    "While it's a pretty romantic choice of location, none of us would have settled on getting married on the beach had it not been for the rather unique nature of the wedding that we were planning."
    "For a start, there are three of us involved in this relationship, which means three rings, three wedding outfits and three lots of guests to be accommodated on the big day."
    "Sure, we might have been able to find a church or a civil venue that could have handled all those people without looking too hard."
    "But when there's two brides and one groom, what side of the aisle are people even supposed to sit on?"
    "On top of all that, we also had the issue of being one of the first trios (well, we're not a couple now, are we?) to get married under the new polygamy laws."
    "The fuss hasn't died down over them yet, and the press have been hungry for weddings involving three individuals that they can turn into a sensational story."
    "None of us wanted that to happen either, and so a remote stretch of the beach that was well of the beaten track seemed to be a sensible choice."
    "We had to spend a lot of time figuring out just who would go where for the ceremony as well."
    "Should we all be at the front of the congregation to begin with?"
    "Should we all come down the aisle together?"
    "Or should we come down one at a time, and if so, in what specific order?"
    "In the end, for the sake of simplicity, that I would stand at the head of the congregation, like a traditional groom, while [bree.name] and Sasha walked up the aisle together."
    "They justified this to me by saying that neither of them wanted to upstage the other on their big day."
    "But a large part of me thinks that it had more to do with them wanting to make a show of numbers and remind me that I'm the minority gender in this relationship!"
    "So here I am, standing with the eager crowd of guests behind me and nothing in front of me, save for the priest and the view out to sea."
    "Just as I think that I can feel the nerves starting to set in, the band starts to play."
    "Instantly I recognise the tune that [bree.name] and Sasha settled on coming down the aisle to."
    "And I damn well should, as it took almost a month of arguing and negotiation to eventually come to a compromise!"
    show sasha wedding zorder 4 at center, zoomAt (1.0, (880, 740))
    show bree wedding zorder 5 at center, zoomAt (1.0, (400, 740))
    with fade
    "Turning to watch their approach, I see the crowd part roughly down the middle to allow my two brides to walk to where the priest and I are awaiting them."
    show sasha at center, traveling (1.25, 5.0, (860, 900))
    show bree at center, traveling (1.25, 5.0, (420, 900))
    if not bree.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, [bree.name]'s chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red above flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebony hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    elif bree.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, [bree.name]'s chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The dress has been tastefully cut to accommodate the curve of [bree.name]'s belly, and so this only adds to her radiance."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red, cut to be sympathetic to the curve of her swelling belly."
        "Below are flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebony hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    elif bree.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, [bree.name]'s chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "The dress has been tastefully cut to accommodate the curve of [bree.name]'s belly, and so this only adds to her radiance."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red above flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebony hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    elif not bree.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "They walk slowly, arm in arm through the sand."
        "I'm surprised to see that, despite being fond of tradition, [bree.name]'s chosen to wear pink."
        "A light, floating affair that's short in the front and long in the back."
        "Pink roses woven into a headband and the locks of her hair compliment the delicate tones of her skin."
        "And she clutches a bouquet of the same flowers, though their beauty is put to shame by the smile on her face as she walks towards me."
        "Sasha walks at her side, a vision in red and black against her strikingly pale skin."
        "The dress is a bodice of red, cut to be sympathetic to the curve of her swelling belly."
        "Below are flowing skirts of that same colour and folds of black."
        "Delicate sleeves of lace cover her arms, and three crimson roses have been woven into her tumbling, ebony hair."
        "In her hands, Sasha clutches a bouquet of black roses."
        "And her face is obscured by a veil of fine, black lace."
        "Oh, did I forget to mention - she kind of has a thing for black!"
    show sasha at center, traveling (1.4, 5.0, (820, 1050))
    show bree blush at center, traveling (1.4, 5.0, (460, 1050))
    "Seeing them walking towards me, their arms intertwined, I'm reminded of the fact that [bree.name] and Sasha are as much marrying each other as they are me."
    "So it's heart-warming to see how close they are and how natural they look together, a beautiful sight to see."
    "And I don't just mean that in carnal sense either - we've grown so close as a trio that we have a true bond now."
    "When I say that we love each other, I mean it in every possible sense of the word."
    "Of course, the ceremony takes a little longer than it would for a couple getting wed."
    "There's an extra set of vows and questions to be asked, but they're longer than they would otherwise be."
    "After all, we're making a declaration of faithfulness and commitment to two other people, rather than one."
    "I can almost hear the guests straining to listen for every unique word and phrase used in the ceremony and then whispering to each other with curiosity."
    "In truth, I can't blame any of them for being so intrigued."
    "I'm intrigued myself, only more as to what happens after the ceremony than during it!"
    "We exchange rings by each putting one onto the finger of one of the others and pushing them on at the same time."
    "I don't know if the guests pick up on the symbolism of this gesture."
    "But we wanted it to show us binding ourselves together, each binding themselves to the others."
    "Priest" "I now declare you husband and wives - you may kiss...well...each other!"
    show sasha happy zorder 4 at center, zoomAt (1.4, (780, 1050))
    show bree happy zorder 5 at center, zoomAt (1.4, (500, 1050))
    with hpunch
    "[bree.name], Sasha and I wrap our arms tightly around each other, pulling our bodies close and placing our lips together in a three-way kiss."
    "As the girls...no, I mean my wives - wow, that's going to take some getting used to!"
    "As my wives toss their bouquets to the clapping and cheering guests, it strikes me how far we've come and how much has changed."
    "When we met, this wouldn't have been legal, let alone believable."
    "[bree.name], Sasha and I have gone from housemates, to friends and then to lovers, finally committing our lives to one another."
    "I honestly have no idea as to just what the future might hold for us."
    "But if it's even half as exciting as the journey that got us here, it'll be well worth looking forward to."
    scene bg park
    show breesasha ending
    with fade
    bree.say "So, hey...yeah...it's me, [hero.name]."
    bree.say "You know, the hero of this whole story?"
    sasha.say "That's so funny, [bree.name] - you sound just like him!"
    bree.say "Uh...yeah - I'm gonna wrap up this whole thing, and tell you how it is!"
    bree.say "And then, I'm gonna fart, and blame it on Sasha and [bree.name] - like I always do!"
    sasha.say "Okay...okay...it's us - it's Sasha."
    bree.say "And [bree.name]!"
    sasha.say "We thought that [hero.name] had been telling his side of the story for too long already."
    bree.say "Yeah, too right!"
    bree.say "And seeing how it's now our story too, we think that we at least deserve to have the last word on it."
    sasha.say "This is the point where, I guess, we're supposed to say something deep and philosophical about married life."
    bree.say "Or get all teary-eyed over the journey that we took to get where we are right now."
    sasha.say "But that sounds pretty boring to us, so we won't."
    bree.say "We think you're far more interested in hearing all about what it's like to live in a threesome."
    bree.say "Am I right?"
    sasha.say "Well, no one ever sat down and wrote a book about it."
    sasha.say "So after the wedding was over, we were pretty much left to figure it out for ourselves."
    bree.say "We kept doing most of the same fun stuff that we'd been doing before we were married."
    bree.say "But with the added bonus that we didn't have to hide it any more!"
    sasha.say "In a lot of ways, we're just like an ordinary married couple."
    sasha.say "We eat out and go to the movies, argue about who's turn it is to put out the rubbish."
    bree.say "And then we have make-up sex, which is almost worth starting an argument for in the first place!"
    bree.say "But it's different too..."
    bree.say "Like if two of us fall out over something, there's always another head to see both sides and mediate."
    sasha.say "And you're not often lonely either."
    sasha.say "Chances are that if one of us is working late or cramming into the night for an exam, the other two are curled up on the sofa together."
    bree.say "Hey, Sasha - I bet that last one had everyone imagining us two being the lonely ones, and [hero.name] tied up somewhere else!"
    sasha.say "You mean people are wondering if we have fun together while [hero.name]'s away?"
    bree.say "Uh-huh!"
    sasha.say "Well, there are some things that should remain a secret - part of the sanctity of marriage!"
    sasha.say "So they can just go on wondering!"
    if not bree.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "We still live in the same house together."
        sasha.say "But we have been talking about saving up to put a deposit down on something we can one day own."
    elif bree.is_visibly_pregnant and sasha.is_visibly_pregnant:
        bree.say "We still live in the same house together."
        sasha.say "But that's mainly because I was expecting Dahlia so soon after the wedding."
        bree.say "And don't forget I was almost as far on with Poppy at the same time too!"
        sasha.say "So with two baby girls on the way so close together, moving was out of the question!"
    elif bree.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "We still live in the same house together."
        sasha.say "Mainly because we thought you were going to pop any second after the wedding!"
        bree.say "With Poppy on the way, moving was out of the question!"
    elif not bree.is_visibly_pregnant and sasha.is_visibly_pregnant:
        sasha.say "We still live in the same house together."
        bree.say "Mainly because we thought you were going to pop any second after the wedding!"
        sasha.say "With Dahlia on the way, moving was out of the question!"
    bree.say "We all still talk about just how weird it is - that things turned out like this."
    bree.say "It was total chance that Sasha and I both moved into the same house that [hero.name] was already living in."
    sasha.say "More than that, what are the chances that two of us out of the three would have hit it off so well as to start a relationship - let alone all three of us becoming involved?"
    sasha.say "And even then, it working for anything more than a quick fling before blowing up in our faces!"
    bree.say "I guess that it was just written in the stars, that it was meant to be!"
    sasha.say "Urgh...let's just say that it was a freakishly rare thing, and we're lucky to have something so special!"
    bree.say "If you say so, Miss Misery-Guts!"
    sasha.say "Right back at you, Sugar-Coated Snot!"
    bree.say "Love you!"
    sasha.say "Yeah, I love you too!"
    scene bg black with dissolve
    pause 2.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label bree_sasha_bitches_1:
    $ hero.cancel_activity()
    show tv bree sasha naked with fade
    "It's weird how things can change so much and how stuff that was crazy at first can come to be pretty much the norm with time."
    "Take my domestic arrangements, for example."
    "Just a couple of months ago, I was adjusting to having two brand new and very different female room-mates move in with me."
    "And before I could get my head all the way around that, things changed all over again."
    "Now I'm living with them both in a three-way relationship that involves them both being basically my obedient slaves."
    "So kids at home, the lesson is that, while things always change, some changes are better than others."
    "Tonight's a good example of how normal things can be, and yet how weird at the same time."
    "[bree.name], Sasha and myself are just sitting on the sofa together, binging on a box-set and eating popcorn."
    "Sounds pretty innocent, right?"
    "Well, not if you could actually see us doing it."
    if bree.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around [bree.name]'s neck to my left."
        "Save for the collars, both of them are naked, their heavily pregnant bellies plain to see."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, [bree.name] simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif sasha.is_visibly_pregnant:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around [bree.name]'s neck to my left."
        "Save for the collars, both of them are naked, but Sasha's pregnant belly is plain to see."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, [bree.name] simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif bree.is_visibly_pregnant:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around [bree.name]'s neck to my left."
        "Save for the collars, both of them are naked but [bree.name]'s pregnant belly is plain to see."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, [bree.name] simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif not sasha.flags.boobjob and not sasha.flags.haircut:
        "While I'm sitting there looking fairly normal, with my popcorn in my lap, I am holding onto two leads at the same time."
        "The black one is attached to the collar that Sasha's wearing as she sits to my right."
        "The pink one to the collar around [bree.name]'s neck to my left."
        "Save for the collars, both of them are naked."
        "While Sasha is sitting with her legs drawn up and her arms crossed over her knees, [bree.name] simply has her legs crossed."
        "She keeps popping pieces of popcorn into her mouth, utterly unfazed by the fact that her ample breasts are bare and fully on show."
        "Sasha stares intently at the TV screen, lost in the show that we're watching to the exclusion of all else."
    elif sasha.flags.boobjob and not sasha.flags.haircut:
        "I guess I could pass for normal, with my popcorn - but not while holding two leather leads in my other hand."
        "[bree.name] is on the end of the pink one, naked save for a pink collar."
        "And Sasha is on my right, tethered by a black collar, also naked, with nothing to conceal her surgically enlarged breasts."
        "Written on both collars in capital letters is the word 'SLAVE'."
        "But apart from that, both are sitting with their attention focused totally on the TV."
        "Sasha leaning forward intently and [bree.name] sitting cross-legged as she eats her own bowl of popcorn."
        "Together, I think we make quite the picture of domestic harmony and bliss."
    elif not sasha.flags.boobjob and sasha.flags.haircut:
        "I guess I could pass for normal, with my popcorn - but not while holding two leather leads in my other hand."
        "[bree.name] is on the end of the pink one, naked save for a pink collar."
        "And Sasha is on my right, tethered by a black collar, also naked, contrasting vividly with her bleached blonde hair."
        "Written on both collars in capital letters is the word 'SLAVE'."
        "But apart from that, both are sitting with their attention focused totally on the TV."
        "Sasha leaning forward intently and [bree.name] sitting cross-legged as she eats her own bowl of popcorn."
        "Together, I think we make quite the picture of domestic harmony and bliss."
    else:
        "I guess I could pass for normal, with my popcorn - but not while holding two leather leads in my other hand."
        "[bree.name] is on the end of the pink one, naked save for a pink collar."
        "And Sasha is on my right, tethered by a black collar, also naked, with nothing to conceal her surgically enlarged breasts, not even her bleached blonde hair."
        "Written on both collars in capital letters is the word 'SLAVE'."
        "But apart from that, both are sitting with their attention focused totally on the TV."
        "Sasha leaning forward intently and [bree.name] sitting cross-legged as she eats her own bowl of popcorn."
        "Together, I think we make quite the picture of domestic harmony and bliss."
    $ game.pass_time(1)
    "It's been one of those lazy, quiet nights, the kind where no one really needs to speak to be aware that everyone else is happy and at ease."
    "Even though both of the girls are quite comfortable with the arrangement of needing to ask permission if they want to speak, it's been almost an hour since anyone actually has."
    "I've totally lost track of the time when Sasha finally sits up and raises her hand, wanting to speak."
    mike.say "Yes, Sasha - what is it?"
    sasha.say "Mmm...[hero.name], I need to use the bathroom - may I be excused?"
    "Sasha's yawn and the sound of her tired voice seems to have roused [bree.name] into wakefulness too."
    "She now raises her hand in the same manner."
    "I nod, giving her permission to speak as well."
    if bree.flags.mikeNickname:
        bree.say "I'd like to use the bathroom too, [hero.name]..."
    menu:
        "Remove their leashes":
            mike.say "Okay, but you two are to come straight back here when you're done, you hear?"
            "Sasha and [bree.name], both sitting up on their haunches now, are quick to nod in agreement."
            "I unclip their leashes and watch as they hurry off upstairs together eagerly."
            "After a short while, they come back down the stairs at a much more leisurely pace."
            "They walk around the sofa and kneel in front of me, waiting to be put back on their leads."
            "That done, they clamber back on the sofa, snuggling down against me, one on either side."
            "And we get back to watching the TV once more."
        "Take them out for a walk":
            hide tv
            call bree_sasha_bitches_garden from _call_bree_sasha_bitches_garden
    $ game.pass_time(1)
    return

label bree_sasha_bitches_garden:
    scene bg livingroom with fade
    mike.say "Okay, let's get you two a little fresh air."
    "[bree.name] and Sasha look at each other in confusion as I stand up."
    "But a gentle yet firm tug on their leads convinces them to follow suit."
    show bree naked leash at left5
    show sasha naked leash at right5
    show hand bree sasha
    with fade
    "I walk them to the front door and open it wide, then gesture for them to step outside."
    mike.say "There you go - what are you waiting for?"
    "[bree.name] raises a tentative hand."
    mike.say "Speak."
    if bree.flags.mikeNickname:
        bree.say "Please, [hero.name]...we don't understand..."
    mike.say "What's not to understand?"
    mike.say "You're my bitches, you're wearing collars, and you need the bathroom."
    "[bree.name] still looks confused, but I see recognition appear in Sasha's eyes."
    "Without needing to be told, she drops onto all fours and pulls eagerly on her leash, whining to be allowed outside."
    "[bree.name] doesn't seem to get what she's doing at first, but then she truly thinks about it, and a bashful grin spreads across her face."
    "She copies Sasha, and is soon straining by her side, making whining sounds of her own that are quite something to hear."
    "Shit - they're actually going to do this!"
    hide bree
    hide sasha
    hide hand
    show bitches
    with fade
    "Not willing to be outdone by them, I walk the girls out of the front door and down the street to the local park."
    "Luckily for us, there aren't many street lights and the place is totally deserted when we arrive."
    show bitches stand
    "That means that only I get to see the spectacle of first Sasha and then [bree.name] hunting on their hands and knees for an agreeable spot amongst the borders and flowerbeds."
    show bitches stand sashapee sashacloseeyes sashaswallow
    play sound peeing
    "Sasha pees for longer, seeming to enjoy having my eyes on her."
    show bitches breepee -sashapee breecloseeyes sashaopeneyes sashatongueout
    play sound peeing
    "But [bree.name] quickly relieve herself too."
    show bitches -breepee breeopeneyes
    stop sound fadeout 0.5
    mike.say "Both finished?"
    "Sasha and [bree.name] nod happily, not fazed in the least by the experience."
    "Shaking my head, and more than a little turned-on, I lead them back along the street to the house, usher them inside and lock the door."
    scene bg black with dissolve
    return


label bree_sasha_bitches_2:
    $ hero.cancel_activity()
    show tv bree sasha naked with fade
    "It's just an average night of the week for [bree.name], Sasha and myself."
    "Sitting in front of the TV and watching any old thing we can find to kill time before turning in for the evening."
    "But then of course, the two girls being stark naked and wearing collars and leashes that I clutch in one hand might look odd to an outsider."
    "Though it's become the accepted norm for myself and my two eager and very willing slaves."
    "I'd say that nothing out of the ordinary happened throughout most of the evening."
    "But there's already the image of [bree.name] and Sasha in their cute little collars and nothing else to make that sound strange in and of itself!"
    "It's normal for us, okay?"
    "We're not watching anything in particular, no one's enjoying a drink at the end of the day, and there are no illicit drugs going around."
    "For a master and slaves, I guess we're pretty domesticated."
    "Though there is one thing that's been bugging me for the past hour or so."
    "Both [bree.name] and Sasha have been drinking a lot more fluids than they normally seem to on a typical evening."
    "In fact, come to think of it, I haven't seen either of them without their noses in their water bowls every fifteen minutes or so for hours."
    "Yet both of them have only crawled off of the sofa and across the room to where their bowls (inscribed with their names and in colours matching their respective collars too) are kept."
    "On top of that, they seem to have developed individual nervous ticks that weren't there before."
    "Sasha keeps twitching her leg, almost like a dog moving in it's sleep."
    "And [bree.name] is constantly chewing on her lip, as if she's trying to relieve some unseen urge."
    "I have no idea what's going on, and it's beneath the dignity of a master to ask such a thing of his slaves anyway."
    "So I just sit back and watch as the ticks seem to become ever more pronounced as time slowly passes."
    "But eventually, I can only think of one way to call their bluff without losing face."
    "I yawn in what I hope is a convincing manner and begin to rise from the sofa."
    $ game.pass_time(1)
    scene bg livingroom with fade
    mike.say "Okay, time for bed!"
    mike.say "The pair of you, upstairs and into my bed!"
    show bree naked sad at right5
    show sasha naked sad at left5
    "Both the girls begin to whine and pout, and at first I think they're actually protesting about being sent to bed."
    show bree evil at right5, onknees
    show sasha joke at left5, onknees
    pause 0.5
    show bree evil at right, onknees
    show sasha joke at center, onknees
    with ease
    "But then they crawl on all fours towards the hallway, in the direction of the front door."
    hide bree
    hide sasha
    with easeoutright
    "I could order them back, and they'd doubtless obey."
    "But something's going on here, and I want to get to the bottom of it."
    "So I follow them into the hallway, giving them enough slack on their leads to reach their intended destination."
    "They stop by the closed front door, sitting up on their haunches to scratch it with their fingernails."
    "Ah, now it all begins to make some kind of sense!"
    "The other night, when they both wanted to pee at the same time, I called their bluff and walked them to the park to do it, just like a pair of bitches."
    "Well, it seems like they really got off on the exhibitionism and danger that the little late night stroll involved and want to repeat it."
    "They even went to the trouble of making sure they were desperate to pee for added effect!"
    "I shrug and then nod."
    "Why the hell not?"
    "It's not too far from the time we went out the last time, and there was no one around on that occasion."
    "Chances are we won't bump into anyone tonight either."
    "The day has been fairly warm, but there's usually a chill breeze at night right now, so I make sure to grab myself a jacket."
    call bree_sasha_bitches_park from _call_bree_sasha_bitches_park
    $ game.pass_time(1)
    return

label bree_sasha_bitches_park:
    "[bree.name] and Sasha don't get any such consideration though, as after all, they're just a pair of bitches."
    "And whoever heard of bitches complaining about the cold or asking for a coat?"
    "I open the door to a chorus of appreciative panting and other sounds of happiness from [bree.name] and Sasha."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    with wiperight
    pause 0.5
    show sasha naked leash at right5, onknees
    show bree naked leash at left5, onknees
    with moveinleft
    "They eagerly walk out onto the sidewalk on all fours, and I almost forget to scan the street for signs of anyone watching."
    scene bg street
    show sasha naked leash at right5, onknees
    show bree naked leash at left5, onknees
    with fade
    "So hypnotic is the sight of their naked backsides in motion and the occasional hint of breasts, swaying from side to side."
    hide bree
    hide sasha
    show bitches
    with fade
    "Several times before we reach the gates of the park, I'm almost half sure that I can see hints of light as people jerk curtains."
    "It's the way I can't be sure if we're being watched or not that makes the thought so thrilling for me."
    "But if anyone is peeping through their drapes at me walking my most unusual pets tonight, they're not making a point of coming out to confront me about it."
    "It's too late for mundane dog-walkers as we finally walk off of the street and into the park."
    "Though I can hear the occasional noise that I'm sure can't be an animal every now and then."
    "There are no street lights in the park, and we seem to be insulated in our own little world of darkness as we find our way to a stand of trees."
    "Just then I hear the unmistakable sound of footsteps approaching quickly."
    "I glance over my shoulder in time to see a jogger pounding her way up the path towards where I'm standing."
    "I step neatly out of the way as she passes, giving her a polite smile."
    "But all the time I'm silently panicking, trying to resist the urge to glance over at [bree.name] and Sasha for fear of drawing the eye of the jogger as well."
    "She gives me a brief glance and a smile, before she passes me and jogs off until she's out of sight."
    "Finally I can breathe out and look over towards where I last saw my bitches."
    "Shaken by the experience, but not wanting to show it to [bree.name] and Sasha, I walk into the stand of trees and call for them to come to me."
    "They obey eagerly, making me think that either they missed the passing of the jogger entirely, or else did not and enjoyed the thrill of coming so close to being seen."
    show bitches stand
    "It's then that I look up to see that they both have a hand raised, asking permission to speak."
    menu:
        "Allow [bree.name] to speak":
            mike.say "Alright, [bree.name] - what do you have to say?"
            bree.say "Now that we've had our exercise and fun..."
            if bree.flags.mikeNickname:
                bree.say "Would [hero.name] allow me to do something nice and fun for him?"
            show bitches sashaswallow
            "Sasha looks disappointed that [bree.name] got to speak first, but she obediently stares at the ground all the same."
            "I look at [bree.name]'s smile and her wide, innocent-seeming eyes."
            "Why shouldn't I indulge her?"
            "We've only seen one other person the entire time we've been out here, and now we're well and truly standing in amongst the trees."
            "Also, my nerves are getting pretty frayed around the edges."
            "I could do with something enjoyable to calm me down before we head back home."
            "I smile indulgently at [bree.name] and nod my assent."
            "In response, she claps her hands together and happily shuffles forwards until she's kneeling before me."
            show bitches breebj
            "[bree.name] sets about unzipping my flies and pulling out my cock, making small, excited noise as she does so."
            "It's cold in the spot where we're standing, and that breeze returns now with a vengeance."
            show bitches inside hold
            "But as if she can sense the way in which the cold is making me a little uncomfortable, [bree.name] wastes no time in wrapping her lips around my dick."
            "I'm not yet fully aroused, but the wet, warm sensation of her tongue soon fixes that problem."
            "Watching [bree.name]'s face as she literally coaxes my cock to being fully erect is an experience in and of itself."
            show bitches breecloseeyes
            "As it grows, she's forced to manoeuvre around it and struggle to keep the entire thing inside of her mouth as much as possible."
            "Her almost stubborn determination to keep it from escaping her is almost as arousing as the feeling of the blowjob she's giving me at the same time."
            "Indeed, [bree.name] whines and pines whenever it looks like my dick is going to slip from between her lips."






            show bitches cumshot with hpunch




            with hpunch
            "I lose myself in [bree.name]'s mouth, a trickle of my cum begins to seep from the corner of her mouth."
        "Allow Sasha to speak":
            mike.say "Yes, Sasha - you may speak."
            sasha.say "[hero.name]...are you quite okay?"
            sasha.say "You seem a little pale...what can we do to make you feel better?"
            "[bree.name] looks down, obviously somewhat ashamed not to have noticed the same change in her Master as Sasha has."
            mike.say "I don't know, Sasha - what did you have in mind?"
            "Sasha shuffles forward, looking meek and demure as she does so."
            "But then she begins to paw at my crotch, her tongue hanging out as she does so."
            "Sasha adds to the effect by whining a little pathetically and looking up at me with huge, appealing eyes."
            "I nod in approval, and her expression immediately transforms into one of open anticipation."
            show bitches sashabj
            "Sasha slowly opens my flies and reaches inside with her fingers to take hold of my cock."
            "She doesn't pull it out immediately, and instead spends some time stroking and rubbing it in very pleasant manner."
            "This means that not only am I almost erect by the time she actually does pull out my dick."
            "But it's also had the last traces of the cold massaged out of it and I hardly feel the chill of the breeze at all."
            show bitches inside hold
            "Only now does Sasha begin to inch my dick into her mouth, taking a little more in with each lick and caress of her lips and tongue."
            "She works quickly, rather than dragging it out as she might have had we been in a more private setting."
            "But the effect only serves to intensify the feelings of pleasure that her ministrations are giving me."
            show bitches sashacloseeyes
            "Soon Sasha is taking my dick so deeply into her mouth and with such determined speed that I begin to worry about her over-facing herself."
            "But she never gags or chokes once, and the deeper that she takes me the more enjoyable the experience becomes as a result."





            "Soon I'm on the brink of cumming, and there's nothing more that either of the bitches can do to prolong the experience."
            show bitches cumshot with hpunch
            "I cum in Sasha's mouth, and the depth that she's taken me in means that she has to swallow without thinking about it."
            with hpunch
            "She does so as I pull out, gasping for air in the hope of making it easier for herself."
            show bitches outside sashaswallow dickcum -cumshot cum onsashaface nohold with hpunch
            "But in doing so triggers a few aftershots of my cum, splattering on her face."


    show bitches stand -breebj -sashabj breeopeneyes sashaopeneyes breetongueout sashatongueout nohold outside
    "I stand still and allow the bitches to push my cock back into my pants and zip them up between them."
    show bitches walk breehappy sashahappy -cum
    "With their leads firmly back in my hand, I give them a firm but gentle tug, making them trot along almost perfectly at heel."
    "It doesn't take us long to walk the short distance back home, and there are even fewer signs of life along the way than there were earlier in the evening."
    scene bg livingroom
    show bree naked at right5
    show sasha naked at left5
    with fade
    "Once we're back in the house, I lock the front door and turn to face my pair of bitches."
    mike.say "Right...NOW it's downstairs and into my bed!"
    hide bree
    hide sasha
    with moveoutright
    "Without a hint of protest, both [bree.name] and Sasha turn and dash eagerly up the stairs."
    "I follow silently, astonished that they still have so much energy left."
    $ sasha.flags.walk_outside = True
    $ bree.flags.walk_outside = True
    return


label repeat_bree_sasha_bitches:
    scene bg livingroom with fade
    "It's just an average night of the week for [bree.name], Sasha and myself."
    "Sitting in front of the TV and watching any old thing we can find to kill time before turning in for the evening."
    show tv bree sasha naked with fade
    "I yawn in what I hope is a convincing manner and begin to rise from the sofa."
    $ game.pass_time(1)
    scene bg livingroom with fade
    mike.say "Okay, time for bed!"
    mike.say "The pair of you, upstairs and into my bed!"
    show bree naked sad at right5
    show sasha naked sad at left5
    "Both the girls begin to whine and pout, and at first I think they're actually protesting about being sent to bed."
    show bree evil at right5, onknees
    show sasha joke at left5, onknees
    pause 0.5
    show bree evil at right, onknees
    show sasha joke at center, onknees
    with ease
    "But then they crawl on all fours towards the hallway, in the direction of the front door."
    hide bree
    hide sasha
    with easeoutright
    menu:
        "Take them out in the garden.":
            call bree_sasha_bitches_garden from _call_bree_sasha_bitches_garden_1
        "Take them to the park.":
            call bree_sasha_bitches_park from _call_bree_sasha_bitches_park_1
    $ game.pass_time(1)
    return

label home_harem_bree_sasha_shower:
label shower_ffm:
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    if renpy.has_label("home_harem_achievement_2") and not game.flags.cheat:
        call home_harem_achievement_2 from _call_home_harem_achievement_2_4
    $ game.flags.shower_ffm = True
    $ game.flags.bree_sasha_shower = True
    $ sasha.flags.showerbj = True
    scene bg bathroom






























    show shower bj breesasha bree sasha
    with fade
    play sound shower loop
    "Once we're all standing in the shower together, [bree.name] and Sasha sink to their knees before me without needing any encouragement."
    "They work so well as a team that I can't help but wonder if they've taken the time to plan all of this out beforehand."
    "[bree.name] takes the lead, beginning to stroke the shaft of my cock with one hand and teasing the tip with her tongue."
    "While Sasha cups my balls and starts to lick them slowly, sucking one into her mouth at a time."
    show shower bj breesasha breemouth
    "[bree.name] looks up at me as she finally takes my cock into her mouth, holding my eye the whole while."
    "It's like she wants me to see the effect that it's having on her at the same moment that I feel the sensations myself."
    "Just as I think [bree.name] can't swallow me any further and that she must be about to choke, she slides my cock out of her mouth again."
    "Only her lips linger on the very tip, and I'm clueless as to what she's doing until Sasha's lips appear on the other side."
    "As smoothly as it's possible to imagine, [bree.name] surrenders my cock to Sasha's intentions, while she takes over caressing my balls."
    show shower bj breesasha sashamouth
    "But where [bree.name] was attentive and fairly meek, Sasha instantly sets a different tone."
    "She smiles impishly as she uses her teeth almost as much as her lips and tongue."
    "When she takes me into her own mouth, it's like being pleasured by a predatory animal."
    "And where [bree.name] stroked my shaft, I can already feel Sasha's nails, sharp and sensual against my tautly stretched skin."
    "If asked to choose, I couldn't honestly say that I could pick [bree.name]'s warm gentleness over Sasha's exquisite pain."
    "But what I do know is that if this keeps up for much longer, I'm going to cum!"
    if bree.is_collared and sasha.is_collared and bree.sub >= 50:
        "As nice as the attention that I'm getting from the mouths of my bitches might be, I want to shoot my load into a more intimate hole."
        "A short tug on each of their leads lets Sasha and [bree.name] know that I've had enough of what they're doing and that it's time for a change."
        show shower bj breesasha -sashamouth
        "But as we're building up towards a peak and not about to slacken off any time soon, they don't need to be told what it is that I want next."
        "Both of them kneel before me, looking up with smiles on their faces and appeals to be picked in their eyes."
        "On a whim, I give Sasha's lead a second tug, and watch as she happily gets to her feet in anticipation of what's to come next."
        "[bree.name] looks disappointed, but she's well-trained enough to know that she shouldn't complain."
        "As soon as I have Sasha's buttocks within easy reach, it's time to begin."
    else:
        mike.say "Ah...ah...I'm gonna..."
        "[bree.name] and Sasha don't even need me to finish the sentence to know what's up."
        show shower bj breesasha -sashamouth
        "They exchange knowing glances, even as Sasha lets my cock slip out of her mouth."
        "Still kneeling in the bottom of the shower cubicle, they begin to play what looks like a game of Rock, Paper, Scissors."
        "[bree.name] goes first, revealing scissors, but a split second later, Sasha has rock."
        "Showing good grace even when losing, [bree.name] shrugs and backs off a little, letting Sasha claim her prize."
        "I have no idea of just what that could be, until she rises to her feet and turns her back on me."
        "Sasha glances over her shoulder, giving me an inviting smile and shaking her buttocks just enough so that the message can't be misinterpreted."
    show shower threesome breesasha with fade
    "The combination of the warm water showering down on all three of us and the games that we've already been playing mean that Sasha is enticingly soft and compliant."
    "I take a firm hold of her buttocks, enjoying the sensation of just how slippery they feel as the water cascades over them."
    "Sasha makes no protest whatsoever as I part them and then pull her smoothly back and onto me in one movement."
    "But if her skin is soft and yielding, then the inside of her pussy is suddenly tight and willing to put up more of a fight."
    "I begin to thrust into Sasha with ever more enthusiasm, feeling her quiver and shake in response to my efforts."
    "Looking up, I see that [bree.name] is leant against the tiled wall of the shower, her arms crossed as she watches us."
    "She's trying to look resigned to the way things have played out, but it still feels wrong for her to be just watching."





    "Soon, though I'm vigorously pounding away on Sasha, I'm getting off as much on watching her and [bree.name] as anything else."
    "Her hands are playing all over her body in response to Sasha's attentions."
    "Stroking her thighs and squeezing her breasts to exorcise some of the feelings overtaking her senses."
    with hpunch
    "When [bree.name]'s own hands reach down for her pussy too, probing the folds and creases that Sasha neglects as she probes deeper, I feel like I can't go on much longer."
    with hpunch
    "Even as [bree.name] begins to stroke herself towards an orgasm, I'm losing myself inside of Sasha."

    with hpunch
    "Afterwards, all three of us stand beneath the still falling water, letting it wash away the sweat and other things that have accumulated."
    "All that can be heard over the pounding of the droplets is the sound of our own breath as it comes in ragged gasps."
    stop sound fadeout 0.5
    scene bg black with dissolve
    return

label bree_sasha_alternative_creation:
    "You know it's weird, back when I found out Sam and Ryan were moving out, I thought it was all over."
    "Okay, that sounds way more dramatic than it was supposed to, so let me put it another way..."
    "I thought this place would never fell the same again, never feel like the home it once was."
    "Well...maybe that was more on account of Sam leaving then Ryan, but you get the general point, yeah?"
    "But something's been creeping up on me slowly, ever since [bree.name] and Sasha moved in."
    "Creeping up so quietly that I didn't even realise it until recently - that feeling's gone."
    "Somehow this place totally feels like home again."
    "Different to how it felt before, but definitely like home."
    show bree at center, zoomAt(1.25, (420, 900))
    show sasha at center, zoomAt(1.25, (860, 900))
    with fade
    "Like right now, [bree.name], Sasha and I are just hanging out around the house."
    "Nobody's really doing anything in particular, apart from sitting and talking about whatever."
    "But suddenly I feel like I've been hit my a bolt of inspiration, right out of the blue."
    show bree stuned
    show sasha stuned
    with vpunch
    "And that's when I leap to my feet, much to the surprise of [bree.name] and Sasha."
    show bree surprised
    bree.say "Whoa..."
    bree.say "Are you okay, [hero.name]?"
    bree.say "Did you remember there's somewhere else you need to be?"
    show bree sadsmile
    show sasha joke
    sasha.say "More like he's regretting that Mexican food from last night."
    show sasha shout
    sasha.say "I told you not to reheat those enchiladas, [hero.name]!"
    show sasha normal
    "I can't help shooting the pair of them a disapproving look."
    mike.say "For the record, you're both wrong."
    mike.say "I decided that it's been too long since we all sat down and had a meal together."
    show bree stuned
    show sasha stuned
    "I watch as [bree.name] and Sasha exchange a puzzled glance."
    show sasha whining
    sasha.say "What are you talking about?"
    sasha.say "Didn't I just say we had Mexican food last night?"
    show sasha annoyed
    show bree talkative
    bree.say "Yeah, and we eat together all the time, don't we?"
    show bree blank
    "I wave a hand in the air, dismissing their questions."
    mike.say "Takeout food doesn't count."
    mike.say "And snacking on junk food in the same room doesn't either."
    mike.say "I mean one of us actually cooking something from scratch."
    mike.say "Then all three of us sitting down at the table to eat it."
    show bree gloomy
    "[bree.name] looks like my words are causing her a little bit of concern."
    show sasha normal
    "But Sasha seems to be more unimpressed than concerned."
    show bree talkative
    bree.say "Yeah, [hero.name]..."
    bree.say "But I'm just not that good when it comes to cooking."
    show bree sadsmile
    show sasha whining
    sasha.say "Plus it takes so much time to prepare all that stuff."
    sasha.say "Who can be bothered doing something so boring?"
    show sasha sadsmile
    "In way of an answer, I turn around and stride out of the room."
    "And luckily for me, it seems [bree.name] and Sasha are intrigued enough to follow."
    scene bg kitchen with fade
    pause 0.3
    show bree at center, zoomAt(1.25, (420, 880))
    show sasha at center, zoomAt(1.25, (860, 880))
    with easeinleft
    "Because by the time I reach the kitchen, they're hot on my heels."
    mike.say "You won't have to lift a finger, Sasha..."
    mike.say "Because I'm the one that's going to be to doing the cooking."
    mike.say "And before you ask, [bree.name]..."
    mike.say "Yes, I'm a total wizard in the kitchen!"
    "[bree.name] and Sasha settle into comfortable spots as I prepare to get to work."
    "It looks like the reality of me cooking for them is starting to set in."
    "Or at least the promise of a free lunch!"
    "I'm rooting around in cupboards and the refrigerator for what I'll need."
    "And I'm also feeling like I'm on show, needing to put in a good performance."
    show sasha shout
    sasha.say "So what are you gonna make for us, [hero.name]?"
    show sasha joke
    sasha.say "Better not be warmed-up leftovers!"
    show sasha normal
    show bree talkative
    bree.say "Sasha, be nice!"
    show bree smile
    bree.say "It's really kind of [hero.name] to cook for us."
    bree.say "I'm sure whatever he makes will be very nice."
    show bree hesitating
    "I happen to look up as [bree.name] says the last part."
    "I can see that there's almost a pleading look on her face."
    "Add to that the ironic smile Sasha's wearing too."
    "And what you have is a whole lot of pressure!"
    "But that doesn't mean I have to let it show."
    mike.say "Ha!"
    mike.say "You guys never had me cook for you before."
    mike.say "So prepare to be dazzled!"
    "I make a point of starting to chop the vegetables as I say this."
    "And then I launch into cooking the meal, making sure it looks flashy."
    show bree stuned
    show sasha sadsmile
    with fade
    "[bree.name] and Sasha seem to be watching me with serious interest the whole time."
    "But it's only when things are well underway that I see a change in them."
    "Once things are cooking away, the smells of what I'm making start to fill the air."
    "And it's almost like I'm casting a spell over the pair of them."
    show bree flirt
    show sasha normal
    "Before now, [bree.name] looked nervous, Sasha like she was waiting for drama."
    "Now the pair of them are exchanging excited glances."
    "And they're breathing in the aromas so much I'm worried they might pass out!"
    mike.say "Okay, guys..."
    mike.say "Grab a seat at the table..."
    mike.say "Because dinner is served!"
    show bree happy
    bree.say "Ooh..."
    bree.say "I'm so excited!"
    show bree normal
    show sasha shout
    sasha.say "This better taste as good as it smells, [hero.name]!"
    show kitchen meal multi bree sasha with fade
    "I plate up three portions of the meal I've cooked in from of the girls."
    "Then I place one in front of them both, and sit down with my own."
    bree.say "Shouldn't we say grace, or something?"
    mike.say "Are you serious, [bree.name]?"
    bree.say "I don't know!"
    bree.say "We usually eat on the sofa, so this feels really formal."
    sasha.say "Rub-a-dub dub, thanks for the grub!"
    sasha.say "There, you happy now?"
    sasha.say "Let's eat, before it gets cold!"
    "Sasha takes the lead by grabbing her knife and fork."
    "Then she's away, shovelling it into her mouth."
    "[bree.name] and I exchange a glance and a shrug."
    "And then we follow her example."
    "As we eat, a second little bit of magic seems to happen."
    "Because I notice nobody's talking, not even a single word."
    "But that's not to say everyone's being quiet."
    "[bree.name] and Sasha are making noises the whole time."
    "Appreciative noises that follow every mouthful they eat."
    "In fact, it's pretty embarrassing to admit this..."
    "But they're kind of making the sounds I always imagined they would during sex!"
    "And the thought makes me chuckle to myself."
    mike.say "Ha!"
    sasha.say "Hey!"
    sasha.say "What's so funny?"
    bree.say "Yeah, [hero.name]..."
    bree.say "Are you laughing at us?"
    "I shake my head as I put down my cutlery and hold up my hands."
    mike.say "No way, guys!"
    mike.say "I'm just happy to see you enjoying your food, that's all."
    "I watch as [bree.name] and Sasha exchange a meaningful look at this."
    "And of course that instantly sets me off panicking."
    mike.say "Wait..."
    mike.say "You are enjoying my cooking, aren't you?!?"
    bree.say "Oh man..."
    bree.say "I can't hold it in any longer, [hero.name]..."
    bree.say "I wanted to be all cool and collected about it..."
    bree.say "But your food's not just good - it's...ORGASMIC!"
    "I can't help staring at [bree.name] in amazement, stunned by her sudden outburst."
    mike.say "Erm..."
    mike.say "Okay, [bree.name], that's...very complimentary."
    mike.say "What about you, Sasha?"
    sasha.say "I dunno if I'd use that exact word..."
    sasha.say "But yeah, she's not kidding - this really is great!"
    "I was expecting to follow up [bree.name] and Sasha's compliments with a joke."
    "Some way of playing down my culinary skills and laughing it off."
    "But the strangest thing happens as I listen to the girls praise me."
    "I get a warm feeling, deep down in my gut."
    "Oh man, I really feel like we're all connecting here!"
    mike.say "I..."
    mike.say "I'm..."
    mike.say "I'm really glad!"
    sasha.say "You okay, [hero.name]?"
    sasha.say "You look like you're gonna burst into tears or something!"
    bree.say "Don't be mean, Sasha!"
    bree.say "He's just touched, that's all - isn't it, [hero.name]?"
    "I nod quickly, trying to deflect attention from my emotional state."
    mike.say "I'm fine, I'm fine..."
    mike.say "But we should do this kind of thing more often, yeah?"
    mike.say "And maybe keep it going right now?"
    "This suggestion seems to make [bree.name] and Sasha thoughtful."
    bree.say "That's a good idea."
    bree.say "But what else can we do next?"
    sasha.say "I know, [bree.name]..."
    sasha.say "Since [hero.name] used one of his talents, let's return the favour."
    "[bree.name] claps her hands together in delight."
    bree.say "That's an even better idea, Sasha!"
    bree.say "Come on, let's get started."
    scene bg kitchen
    show bree at center, zoomAt(1.25, (420, 880))
    show sasha at center, zoomAt(1.25, (860, 880))
    with fade
    "The meal that I just made for us hasn't had the time to even settle before [bree.name] leaps up."
    show bree at center, zoomAt(1.25, (220, 880)) with ease
    "And she almost seems to forget to tell us what she has in mind as she hurries to the door."
    show bree stuned
    mike.say "[bree.name]..."
    mike.say "Aren't you forgetting something?"
    show sasha shout
    sasha.say "We're not fucking psychic, you know?"
    show sasha normal
    "[bree.name] stops in her tracks as she reaches the doorway to the hall."
    show bree blush
    "And I can see that she's pretty embarrassed, but still eager."
    show bree hesitating
    bree.say "Oops!"
    bree.say "Sorry, guys - I guess I got a little carried away."
    bree.say "I meant to say that we should all go and play on the Z-Box, right now!"
    show bree normal
    "Sasha and I exchange a glance and a shrug."
    mike.say "I'm up for it..."
    mike.say "What about you, Sasha?"
    show sasha shout
    sasha.say "Sure, [hero.name]…"
    show sasha joke
    sasha.say "You two are always hogging the thing anyway!"
    show sasha normal with hpunch
    "Sasha gives me a playful jab in the ribs as she gets up."
    "And it's enough to catch me off-guard, making me stumble."
    show sasha at center, zoomAt(1.25, (460, 880)) with ease
    "Then she dashes over to where [bree.name]'s waiting for us."
    hide bree
    hide sasha
    with easeoutleft
    "The two of them giggle as they hurry off to the sitting room."
    "Obviously amused at the way they've managed to leave me behind."
    mike.say "Hey..."
    mike.say "I just cooked a succulent meal for you two..."
    mike.say "And this is how you show your gratitude?"
    scene bg livingroom
    show bree at center, zoomAt(1.25, (420, 900))
    show sasha at center, zoomAt(1.25, (860, 900))
    with fade
    "By the time I catch up to the girls, they're already turning on the Z-Box."
    "Sasha tosses me a joypad as I flop onto the sofa."
    "And I see that [bree.name]'s rummaging through our collection of games."
    sasha.say "Ah, get over yourself, [hero.name]!"
    sasha.say "Sure, it was a great meal today."
    sasha.say "But it's just tomorrow's poop!"
    bree.say "Eww!"
    bree.say "Can we please stop talking about poop?"
    bree.say "Especially when we should be gaming!"
    "Eager to change the subject, I decide to weigh in on [bree.name]'s side."
    mike.say "So, [bree.name]..."
    mike.say "What are we playing?"
    mike.say "This was your idea, so you've got to have something in mind, right?"
    bree.say "I thought we could play 'Superior Slam Sisters'?"
    bree.say "Super fun game and really easy to pick up too."
    bree.say "So it should be great for our resident newbie here!"
    "All eyes suddenly fall on Sasha."
    "And she looks less than comfortable about it too."
    sasha.say "What's that supposed to mean?"
    sasha.say "It's not like I never played a videogame before!"
    "[bree.name] gives Sasha a smile that looks a little condescending to me."
    bree.say "It's not supposed to be an insult, Sasha."
    bree.say "You're what we call a 'casual gamer'..."
    bree.say "While [hero.name] and I are more hardcore."
    "I can see that Sasha's not best pleased with [bree.name]'s attempt at an explanation."
    "So I make a point of firing up the Z-Box and putting myself between the two of them."
    mike.say "Best way to see who's casual and who's hardcore is to actually play the game."
    mike.say "Come on, [bree.name]..."
    mike.say "Let's see what Sasha can do!"
    show play console sasha
    show play_console_bree_third at center, zoomAt(1.2, (1360, 720))
    with fade
    "As soon as the game begins, [bree.name] forgets about everything else."
    "Because she really is pretty hardcore, and her head is totally occupied with playing."
    "But my gamble soon pays off, as it means that she's not pissing Sasha off anymore."
    "And that in turn allows the less serious gamer to get into the swing of things."
    "Sasha seems to be a fast learner too, surprising [bree.name] and I more than once."
    "Even so, I can feel the energy change after a while."
    "Like we're getting ready to move on to something a little different."
    mike.say "Hmm..."
    mike.say "I fancy a change of pace."
    mike.say "How about you guys?"
    sasha.say "What?!?"
    sasha.say "You're just saying that because I'm beating you!"
    bree.say "Okay, [hero.name]..."
    bree.say "Should we play another game?"
    bree.say "Oh, I know - we could play 'Guitar God'!"
    "Sasha wrinkles her nose at the suggestion."
    sasha.say "Huh?"
    sasha.say "What's that?"
    bree.say "It's a great game, Sasha..."
    bree.say "Where you get to play a guitar!"
    scene bg livingroom
    show sasha stuned at center, zoomAt(1.25, (420, 900))
    show bree at center, zoomAt(1.25, (880, 900))
    with fade
    "Sasha turns to look at me."
    "As if she can't believe what she's hearing."
    mike.say "Well, it's not a real guitar..."
    mike.say "And you don't really play it either."
    mike.say "You just kinda press buttons at a certain time."
    show sasha whining
    sasha.say "Ah, fuck that!"
    sasha.say "Why play a shitty game when we have the real thing right here?"
    show sasha annoyed
    show bree vangry
    bree.say "It's not shitty!"
    bree.say "And what do you mean 'the real thing'?"
    show bree angry
    "I can feel a smile creeping across my face as I look Sasha in the eye."
    show sasha normal
    "She raises an eyebrow too, pretty much telling me we're on the same wavelength."
    mike.say "Sasha's saying I should grab my guitar."
    show sasha shout
    sasha.say "And I'll go grab my base too."
    sasha.say "Then we'll jam for fucking real!"
    show sasha normal
    show bree stuned
    "[bree.name] looks from Sasha to me and back again."
    show bree surprised
    bree.say "Really?"
    bree.say "You mean I'm going to get a private performance?"
    bree.say "Right here in the sitting room?"
    hide sasha with easeoutright
    "Sasha nods as she hurries off to get her base."
    scene bg bedroom1 with fade
    "I do the same thing too, running to pick up my guitar."
    scene bg livingroom
    show bree at center, zoomAt(1.25, (420, 900))
    with fade
    show bree at center, traveling(1.1, 0.3, (400, 810))
    show concert solo sasha nobg at center, zoomAt(1.0, (840, 790)) with easeinright
    "Mere minutes later we're both back in the room, strapping on our instruments."
    "All the while [bree.name] watches us with am eager expression on her face."
    mike.say "So..."
    mike.say "What's the plan here?"
    play music "<from 7 to 193>music/deathless_harpies/Deathless_Harpies_Bass.ogg"
    queue music "music/deathless_harpies/Deathless_Harpies_Bass.ogg" loop
    "By way of an answer, Sasha strums her base."
    "The sound is low and loud, enough for me to feel it in my guts."
    sasha.say "Don't overthink it, [hero.name]..."
    sasha.say "Just jam with me, yeah?"
    sasha.say "Let your creative genius guide you."
    "I nod, hoping that I'm going to be able to do as she says."
    play music1 ["<sync music>music/deathless_harpies/Deathless_Harpies_GuitarLead.ogg","music/deathless_harpies/Deathless_Harpies_GuitarLead.ogg"] loop
    "And then we launch into it, the sound of guitars filling the room."
    "It doesn't take long for my nerves to begin easing as we play."
    "Sasha's every bit as good as I thought she'd be."
    show concert solo sasha nobg at center, traveling(1.4, 1.0, (640, 980))
    "But I'm relieved to find that she's also not an asshole."
    "She seems to be genuinely listening to what I'm playing."
    "And she expertly weaves her bass-line around it."
    "This in turn means that I can hear where she's coming from too."
    "So I make a point of playing in sympathy as well."
    hide bree with dissolve
    "It works too, as I find myself forgetting about everything else."
    "I'm not even looking down at my guitar as I play."
    hide concert
    show sasha b at center, zoomAt(1.4, (640, 1120))
    with fade
    "Instead I find myself staring into Sasha's eyes."
    "Our gazes are locked as we improvise, totally fixated on each other."
    "I know it sounds crazy, but I can't help feeling like we're connecting."
    "Like the music that we're making on the spur of the moment is binding us together."
    "Eventually we get to the point where our playing reaches a natural crescendo."
    "And I can feel the passion bubbling up inside of me."
    "Sasha's standing so close that we're almost touching."
    "Letting my guitar fall away, I reach out to her."
    "At the same time she lets go of her bass and does likewise."
    "Without a second thought, I pull her close and lean into the embrace."
    stop music
    stop music1
    hide sasha
    play music "music/roa_music/city_nights.ogg" loop
    show bree witness at flip, center, zoomAt(1.1, (740, 720))
    show sasha kiss
    with fade
    "Sasha returns the gesture, pressing her lips against mine."
    "And just like that, we're making out with a desperate passion."
    "I can't explain how it happened, just that it feels totally natural."
    "Like we connected so deeply while we were playing together."
    "And this is the next logical step in the process."
    "I also have no idea where this is ultimately going."
    "All I know is that I can feel my desire for Sasha growing."
    "At the same time as something more physical is growing too!"
    hide bree
    hide sasha
    show sasha blush at center, zoomAt(1.4, (640, 1050))
    with fade
    "Suddenly the kiss breaks, with Sasha and I both gasping for breath."
    "Then it's like we remember something important at the same moment."
    scene bg livingroom at center, zoomAt(1.25, (500, 890))
    show bree spying fingering casual down at center, zoomAt(1.25, (740, 980))
    "And as one we glance around to the sofa, staring at [bree.name]."
    "She seems as surprised as we are, eyes wide as she looks up at us."
    bree.say "Erm..."
    bree.say "Yay, that was great!"
    bree.say "I'd give you a round of applause."
    bree.say "If I could..."
    "[bree.name] has one hand held up in the air, waving at us."
    show bg livingroom at center, traveling (1.0, 0.5, (640, 720))
    show bree spying fingering casual down at center, traveling (0.9, 0.5, (780, 720))
    "But then my eyes travel downwards, and I see where the other one is."
    "[bree.name]'s pants are half open, and her hand is stuffed inside of them."
    "Which can only mean that she's been playing with herself while watching us!"
    scene bg livingroom
    show sasha stuned blush at center, zoomAt(1.4, (640, 1050))
    with fade
    "Sasha and I exchange a look of amazement at the sight of [bree.name] playing with herself on the sofa."
    "And for an instant I'm worried that it's going to be enough to kill the moment, to change the mood."
    show sasha shy -blush
    "But much to my surprise, I see the intensity in Sasha's eyes burn even brighter than before."
    "It's almost like the realisation that we're turning [bree.name] on makes her want this even more."
    "And a moment later I get unmistakable proof that I'm right, as I feel Sasha's hand on my groin."
    show sasha shout blush
    sasha.say "What are we waiting for, [hero.name]?"
    sasha.say "[bree.name]'s just sitting there watching us."
    sasha.say "And she's already wetter than a mermaid's pussy!"
    sasha.say "Are we really gonna let her have more fun than we are?"
    show sasha normal
    "I find myself standing there for a moment, almost paralysed."
    "The sensation of Sasha's hand, squeezing my cock, is overwhelming."
    "I feel like I want her so badly, and all I have to do is make a move."
    mike.say "Fuck it, Sasha..."
    mike.say "You're so right!"
    "Tossing my guitar aside, I use both hands to fiddle with Sasha's pants."
    hide sasha
    show sasha kiss casual
    with fade
    "My efforts are clumsy, thanks to her planting more kisses on me the whole time."
    "But soon enough I have them undone and I can see the first glimpse of her underwear."
    "I wish I could say that I was stripping her off smoothly and with some kind of style."
    "But the truth is that I'm just shoving my hands down there, desperate to feel her."
    "And when my fingers finally manage to feel out her pussy, there's no way to hold back."
    "Even the slightest sensation of the hot, wet state that Sasha's in down there makes me crazy."
    "Now there's no way that I can stop myself from yanking down her pants and panties."
    "At the same time she's following my lead, shrugging off her bass."
    show sasha kiss naked with dissolve
    "Then I feel her hands pulling at my clothes as she tries to undress me."
    "There's no plan or conscious cooperation going on between us right now."
    "All we want is to tear off each other's clothes and then get into it."
    hide sasha
    show sasha foreplay nobg up
    with fade
    "This means that as soon as there's enough flesh exposed, we start to do it."
    "Neither of us even think about trying to get to one of the sofas."
    "Hell, we don't even sink to the floor to start fucking down there."
    "Sasha just rubs herself against me like a cat in heat."
    "And we start to do it standing up, just like a couple of felines in an alley."
    "Much as I hate to do it, I have to cut off the kisses from Sasha."
    "As I do so, she makes a sound of pure and plain disappointment."
    "But now that we're pretty much naked, I can make my intentions plain."
    "So I waste no time in stepping closer, almost pressing my hips to her own."
    "At the same time I make sure to thrust myself forwards too."
    "This means that my cock slides right between Sasha's thighs."
    "And the look on her face as it does so is just priceless."
    show sasha foreplay nobg orgasm
    sasha.say "Oh..."
    sasha.say "Hello!"
    sasha.say "Does someone want to come inside?"
    show sasha foreplay nobg pleasure
    mike.say "What do you think?"
    mike.say "Question is, are you going to open up?"
    "I make a point of moving back and forth as I ask the question."
    "And as I do so I can feel the sensation of my cock against Sasha's pussy."
    "The trouble is that it feels so good I'm struggling to keep this up."
    "Sure, I have a knowing smile on my face right now."
    "But all I want is to let go and fuck Sasha senseless!"
    "Luckily for me, it seems like she's on the same page too."
    "Because I can already see her flushing with the effort of holding back."
    show sasha foreplay nobg orgasm
    sasha.say "I..."
    sasha.say "I think..."
    sasha.say "Ah...fuck it!"
    sasha.say "Just do me already, okay?!?"
    scene bg livingroom at center, zoomAt(1.25, (480, 800)), blur(5)
    show sasha stand nobg zorder 2 at center, zoomAt (1.0, (630, 720))
    with fade
    "The moment that Sasha breaks, everything changes."
    "For some reason I'm not beating around the bush anymore."
    "Instead I feel my animal instincts taking over."
    "And a few seconds later I've taken a firm hold of her."
    "Then my thighs are moving, like they have a mind of their own."
    "Sasha offers no resistance whatsoever, not even for a second."
    "If anything, she does all that she can to make my task easier."
    "Pressing herself against me and pushing down, she speeds things up too."
    show sasha stand nobg at stepback(speed=0.1, h=10, v=0)
    "I make one thrust and then another, each one making me gasp."
    show sasha stand nobg vaginal at stepback(speed=0.1, h=10, v=0)
    "But on the third, the unexpected happens."
    "All at once the resistance is just gone."
    show sasha stand nobg vaginal at stepback(speed=0.05, h=10, v=0)
    "Sasha opens up to me, and I slide straight into her."
    "She's still gripping me tightly the whole time, for sure."
    "But the force that I'm using means I sink all the way in."
    show sasha stand vaginal nobg insert zorder 2 at center, zoomAt (1.0, (640, 720))
    sasha.say "Mmm..."
    sasha.say "Oh...oh fuck..."
    sasha.say "That's it...that's what I want!"
    sasha.say "Give me more of that, [hero.name]!"
    show sasha stand vaginal nobg -insert zorder 2 at center, zoomAt (1.0, (630, 720))
    pause 0.1
    show sasha stand nobg vaginal at stepback(speed=0.1, h=10, v=0)
    "I don't hesitate to take advantage of the invitation."
    "Which means that I'm moving before she's finished making the demand."
    show sasha stand nobg vaginal at stepback(speed=0.1, h=10, v=0)
    "Sasha's left to cling onto me as I start to move inside her."
    show sasha stand nobg speed vaginal at stepback(speed=0.05, h=10, v=0)
    "And I can feel her grip tightening as I start to pick up speed."
    "Each thrust seems to have an effect on her too."
    "So that soon enough it's not just her fingers tightening."
    show sasha stand nobg speed vaginal at stepback(speed=0.05, h=10, v=0)
    "Now I can also feel the sensation of Sasha's nails coming into play."
    "She's bunching her fingers and pushing them into my skin!"
    "But the pain I'm feeling isn't making me want to stop."
    "If anything, it seems to energise me, to push me harder still."
    show sasha stand nobg speed vaginal at stepback(speed=0.05, h=10, v=0)
    "So grabbing a firmer hold of Sasha, I start to pound her harder too."
    "The intensity of the sensations seems to sharpen my senses."
    "And for the first time I actually remember where we are right now."
    show bree spying fingering casual down zorder 1 at center, zoomAt (0.9, (780, 720))
    "I'm looking over Sasha's shoulder, right at where [bree.name]'s slumped on the sofa."
    "Before she had her hand inside of her shorts as she played with herself."
    "But now they're splayed open and pulled down her thighs."
    "Which means that I can clearly see her pleasuring herself."
    bree.say "Oh, [hero.name]…"
    bree.say "I know I shouldn't be here."
    bree.say "I know that watching you is...wrong."
    bree.say "But it's so hot!"
    "I don't know if Sasha can hear what [bree.name]'s saying too."
    "But the mere sight of her sends a jolt through me."
    "One that's enough to make me begin to lose it."
    show sasha stand nobg speed vaginal at stepback(speed=0.05, h=10, v=0)
    "And the change of pace seems to have the same effect on Sasha too."
    show sasha stand nobg speed vaginal at stepback(speed=0.05, h=10, v=0)
    "She cums a few seconds before me, digging her nails into my flesh."
    menu:
        "Cum in pussy":
            "And I can't hold back a moment longer."
            show sasha stand nobg vaginal insert ahegao with hpunch
            "So I just let go, allowing myself to be swept along."
            with hpunch
            "One last thrust is all it takes."
            show sasha stand nobg vaginal cum creampie insert ahegao with hpunch
            "Then I feel myself lose it deep inside of Sasha."
        "Pull out of pussy":
            "At the very last moment I pull back."
            show sasha stand nobg -vaginal insert ahegao with hpunch
            "Which means that I slide straight out of Sasha."
            with hpunch
            "My cock bobs in the air between us for a brief second."
            show sasha stand nobg cumshot insert ahegao with hpunch
            "And then I shoot my load all over her."
    $ sasha.sexperience += 1
    scene bg livingroom with fade
    "Sasha collapses onto the floor in a slow, languid motion."
    "But I'm left standing in the middle of the sitting room."
    "I'm panting and almost ready to collapse myself."
    show bree spying fingering casual down at center, zoomAt (0.9, (780, 720)) with dissolve
    "And then my eyes fall on [bree.name], still playing with herself on the sofa."
    "I know this is going to make me sound like a massive asshole."
    "But the moment that I know Sasha's okay, I totally forget about her for a moment."
    "And all of my attention is instead focussed on [bree.name] as she lounges on the sofa."
    "I'm still buzzing from fucking Sasha, and normally I'd be totally exhausted too."
    "But it's like there's something special in the air tonight."
    "Like the three of us are creating some kind of weird energy."
    "And instead of feeling like all my reserves are spent, I'm ready to go again!"
    hide bree
    show bree stuned blush at center, zoomAt(1.4, (640, 1050))
    with fade
    "As I walk the short distance to where [bree.name]'s laid, she gazes up at me."
    "Her eyes are wide, full of excitement and what looks like expectation."
    "And I don't even have to ask her if she's thinking along the same lines as me."
    show bree bottomless
    "Because without a word, she starts to pull down her pants!"
    "[bree.name] lets them fall around her ankles, then kicks them aside."
    show bree naked
    "And by the time I reach her, she's hastily pulling off her top too."
    mike.say "Ah..."
    mike.say "You look a little flustered there, [bree.name]..."
    mike.say "Want me to help you with that?"
    show bree smile
    "The smile that spreads across [bree.name]'s face would have been answer enough alone."
    show bree evil
    bree.say "Mmm..."
    show bree hesitating
    bree.say "Would you, [hero.name]?"
    bree.say "It kinda feels like I have an itch, you know?"
    bree.say "One I just can't seem to scratch on my own!"
    show bree flirt
    "[bree.name]'s totally naked by the time I start lowering myself down and onto her."
    "And her legs are spread wide enough for me to slide right between them."
    "By rights I should be totally spent by now, ready to fall asleep or something."
    "Instead I can feel my cock getting hard again, starting to stand to attention."
    "I feel every bit as energised as I did when I was fucking Sasha."
    "I just hope that this feeling lasts long enough for me to do [bree.name] too!"
    "Because I soon find out that she's got plenty of energy of her own."
    "And she shows me as much by suddenly wrapping her legs around my waist."
    hide bree
    show bree kiss naked
    with fade
    "Before I know what's happening, [bree.name]'s arms are around my neck too."
    "Then she pulls me down, closing the last few inches between us."
    "I don't have time to react, I'm just carried along for the ride."
    "[bree.name]'s tongue is in my mouth, writhing like a snake."
    "And I can feel her hands all over my body too."
    "They're not caressing gently, more like they're grasping in desperation."
    "Man, [bree.name] must really have gotten horny watching me and Sasha go at it!"
    "And now it seems like she wants the same treatment."
    "I'm just starting to be able to think about how I'm going to do this."
    "But that's when I feel something clamp onto the shaft of my cock."
    mike.say "Urgh..."
    mike.say "What the..."
    "A quick glance down shows me that [bree.name]'s hand is gripping it tightly."
    "And in the next moment she shoves it hard between her thighs."
    "Which I guess is her way of telling me that I need to get on with it!"
    scene bg black
    show bree missionary livingroom normal
    with fade
    "Spurred into action by [bree.name]'s grip on my cock, I decide to make my move."
    "Which really doesn't involve anything fancy or complicated on my part."
    "I simply lean in closer and push myself forwards at the same time."
    "Essentially I'm just giving her what she wants."
    "Adding more weight and motion to where she's directing traffic."
    "Even so, [bree.name] lets out a gasp of genuine surprise as I do so."
    show bree missionary pleasure
    bree.say "Oh..."
    bree.say "Oh fuck!"
    show bree missionary normal
    "At first I think that's just because she's been waiting for this."
    "That the desire in her has built up to the point where she can't hold back."
    "But then I feel myself literally sinking straight into her."
    "Where I'd expect to meet resistance, there's nothing at all."
    show bree missionary vaginal at stepback(speed=0.1, h=10, v=0)
    "The head of my cock just slides into [bree.name] as though she's melted."
    mike.say "Ah..."
    mike.say "Fuck!"
    "I can't help repeating [bree.name]'s own exclamation as I fill her."
    "The sensation is just that intense and overwhelming."
    "And now I feel like I'm being enveloped in [bree.name]'s all-consuming desire."
    "Like the same heat that's infused her as she watched I is affecting me."
    "Before I was kind of watching her with a growing interest."
    "But now I'm feeling it flowing through me too."
    "And there's only one way that I can do anything about it."
    show bree missionary pleasure at stepback(speed=0.1, h=10, v=0)
    "So without another word, I start to move inside of [bree.name]."
    "Normally I'd be trying to start slow and then build up momentum."
    "But as soon as I get going, I feel myself picking up speed."
    show bree missionary at stepback(speed=0.05, h=10, v=0)
    "It feels like I'm running down a steep hill, getting faster by the moment."
    "And no matter what I do, there's no way I can hope to stop it."
    "Soon enough I'm not moving back and forth atop [bree.name]."
    show bree missionary at stepback(speed=0.05, h=10, v=0)
    "Instead I'm desperately thrusting in and out of her."
    "Pounding away for all that I'm worth, without a hope of stopping."
    "But it's not like [bree.name]'s a passive observer either."
    show bree missionary at stepback(speed=0.05, h=10, v=0)
    "She's still clinging onto me as tightly as ever."
    "And it feels like the harder I fuck her, the more she clings to me."
    show bree missionary normal at stepback(speed=0.05, h=10, v=0)
    "Like she's the hottest, neediest limpet imaginable!"
    show bree missionary pleasure
    bree.say "[hero.name]…"
    bree.say "Don't stop..."
    bree.say "I...need this...so bad!"
    show bree missionary normal arm at stepback(speed=0.05, h=10, v=0)
    "It's not like [bree.name] really needs to encourage me."
    "I can't imagine anything that could tear me off her right now."
    show bree missionary pleasure at stepback(speed=0.05, h=10, v=0)
    "But the need in her voice does serve to make me try harder still."
    "Putting everything I have left into it, I make one final push."
    sasha.say "Oh man..."
    sasha.say "You get that cock, girl!"
    sasha.say "Shit, you're making me feel hot all over again."
    "The sound of Sasha's voice takes me totally by surprise."
    "As if I'd just assumed that she passed out once we were done."
    hide bree
    show sasha foot naked footjob at center, zoomAt(1.4, (340, 980))
    with vpunch
    "But a quick glance shows me that she's made it to the sofa."
    "And now she's reclining a short distance from us, just watching the show."
    "I don't know if that's the sole reason that things begin to speed up for me."
    hide sasha
    show bree missionary vaginal arm pleasure livingroom at stepback(speed=0.05, h=10, v=0)
    "But whatever the cause, I can feel that I won't be lasting much longer."
    "So I'm going to have to decide what happens next!"
    menu:
        "Cum in pussy":
            "By now I feel like there's no chance I can go any way but forwards."
            show bree missionary vaginal arm ahegao creampie with hpunch
            "So I just keep right on going, shooting my load without hesitation."
            with hpunch
            "The moment that I do, [bree.name] seems to explode around me."
            with hpunch
            "She hugs, squeezes and pinches me in every way humanly possible."
            "All of which serves to make the sensation all the more intense."
        "Pull out of pussy":
            "Somehow I manage to fight the urge to just plough straight on."
            show bree missionary -vaginal arm
            "It takes every ounce of my will, but I manage to pull out just in time."
            show bree missionary arm cumshot with hpunch
            pause 0.25
            show bree missionary arm -cumshot cum onbelly with hpunch
            "A moment later I explode, shooting my load over [bree.name]'s belly."
            with hpunch
            "She hugs, squeezes and pinches me in every way humanly possible."
            "All of which serves to make the sensation all the more intense."
    $ bree.sexperience += 1
    scene bg livingroom with fade
    "The last thing I manage to do is collapse to the side of [bree.name]."
    "Which I guess is better than just landing on top of her."
    "I'm able to do no more than lie there in a heap, gasping for breath."
    "But as soon as I open my eyes, I see Sasha and [bree.name] gazing down at me."
    mike.say "Phew..."
    mike.say "I am so spent after all of that!"
    mike.say "I bet you guys are exhausted too?"
    mike.say "Right?!?"















































































































































































































































































































































































































































































    $ Harem.join_by_name("home", "bree", "sasha")
    "The sitting room is silent once we're all done, save for our panting gasps."
    "I have no idea what to say or where to go from here, as my mind's totally blown."
    "I'm sure once we've all recovered it'll begin to make sense."
    "But right now I don't know if we'll even make it back to our own bedrooms tonight!"
    "For all I know we could just stay right here, laid in a tangled heap on the sofa."
    "After all, there's nobody to walk in and find us like this."
    "When everyone in the house is in on the action, you don't have to hide it."
    "And that's a thought already bubbling around inside of my head."
    "Because it raises a lot of interesting possibilities."
    scene bg black with dissolve
    return

label home_harem_pegging_bree_sasha:
    scene bg bedroom1 with fade
    show bree normal at center, zoomAt(1.0, (440, 720))
    show sasha normal at center, zoomAt(1.0, (840, 720))
    with dissolve
    "There was a time when I would have struggled to believe that I'd ever end up with a couple of majorly hot girls living with me as my housemates."
    "Back then it'd have been amazing just to imagine sharing my home with two women that turned me on, being able to see them each and every day."
    "The very idea of one of them falling for me and us becoming an item would have seemed far-fetched as well, like it was too much to ask."
    "And if you'd even suggested to me that I might actually wind up engaged in the three-way relationship with both of them..."
    "Well, let's just say that I would have probably said you had a vivid imagination and maybe you should take up writing fiction for a living!"
    show bree at center, traveling(1.25, 0.3, (440, 850))
    show sasha at center, traveling(1.25, 0.3, (840, 850))
    show bree smile
    show sasha happy
    "But here I am, well and truly through the looking glass when it comes to the state of my relationship and sex-life."
    "I am living with two hot girls, they're both into me and we're all three of us pretty happy with the arrangement of sleeping together as a trio."
    "What more could I possibly want?"
    show bree hesitating
    show sasha normal
    "Well, maybe a little bit more courage for what I've been told we're going to be trying out for the first time tonight?"
    show sasha joke
    "Both [bree.name] and I know full well that Sasha's the most outrageous member of our threesome, by some considerable way."
    "We're fine with it, and it adds some real spice to the mixture when you're thinking up new ways to get frisky together."
    "But tonight she's suggested that she pulls out one of her favourite sex-toys and tosses it into the mix."
    show bree at center, traveling(1.25, 0.3, (340, 850))
    show sasha at center, traveling(1.4, 0.3, (740, 920))
    show sasha wink
    sasha.say "You know what I'm talking about, don't you [hero.name]?"
    show sasha flirt
    "I've seen the toy in question before, a pretty impressive strap-on dildo that Sasha likes to jokingly call her 'battering ram'."
    "Now you might well ask at this point, what exactly my problem is with all of this."
    "You might be surprised or even shocked to discover that a guy who's part of a threesome is quailing at something as relatively mundane as a strap-on."
    "How I have a problem with seeing someone fucked with a dildo might confuse you."
    "But maybe not so much once I tell you that the person supposed to be getting fucked by it is me!"
    "Sasha, of course, was dead keen on the idea, as she was the one that suggested it in the first place."
    "And there was no hope of [bree.name] being the voice of reason and shooting her down, as her eyes practically lit up at the thought of it."
    "That left me outnumbered, two to one."
    mike.say "I... I don't know about this..."
    show sasha at center, traveling(1.25, 0.3, (840, 850))
    show bree at center, traveling(1.4, 0.3, (440, 925))
    show bree talkative
    bree.say "Don't worry, it only hurts a little when it first goes in."
    bree.say "After that, well...it still hurts, but then it's kind of pleasurable pain!"
    hide sasha
    hide bree
    show sasha strapon at center, zoomAt(1.0, (640, 720))
    with fade
    "Before I can really digest that rather ominous statement, Sasha makes a show of turning around and posing with the strap-on, well...strapped-on."
    "The sound of me swallowing is actually audible in the otherwise silent room."
    show sasha at center, traveling(1.4, 0.3, (640, 920))
    show sasha joke
    sasha.say "Aw, don't look so frightened, [hero.name]."
    show sasha wink at startle
    sasha.say "I promise I'll be gentle!"
    show sasha normal
    "She has a palm full of lube as she says this, and begins to rub it up and down the length of the dildo as she walks slowly towards the bed."
    "For all that [bree.name]'s trying to be sweet and reassuring, I get the distinct impression that Sasha is actually enjoying my discomfort."
    show sasha at center, traveling(1.4, 0.3, (840, 920))
    show bree talkative naked at center, zoomAt(1.4, (440, 930)) with easeinleft
    bree.say "Don't worry, [hero.name] - I won't let her hurt you, I promise."
    bree.say "And I'll do something really nice to take your mind off of it too!"
    show bree flirt at center, traveling(1.4, 0.3, (340, 930))
    menu:
        "No really, no":
            mike.say "Sorry girls but no, really."
            mike.say "But you two, have fun."
            return
        "So be it":
            pass
    "Well, here we go."
    "I could have said no, and I could still say no."
    "But it looks as though I'm just going to have to grin and bear it!"
    sasha.say "Just lie down and relax, [hero.name]."
    sasha.say "And don't worry - I've done this a thousand times before..."

    scene sasha strap at center, zoomAt(1.0, (640, 720))
    with fade
    play sound "<from 0 to 0.5>sd/SFX/house/bed_jump.ogg"
    "With that, she pushes me back onto the bed until I'm laid on my back."
    "Sasha's not rough with me, but she does make the push forceful, so that I know she means business."
    "At the same time, [bree.name]'s leaning in close to me, stroking my chest and cooing gently into my ear."
    show sasha strap bree with fade
    "Not for the first time, I'm reminded of the contrast between the pair of them."
    "[bree.name] - blonde and almost angelic in appearance."
    "Sasha - raven-haired and with the charm of the devil."
    "And they certainly seem to be playing those very same roles with me tonight!"
    sasha.say "Do you like big ones, [hero.name], huh?"
    sasha.say "Do you like the look of mine?"
    "She's looming over me now, stroking the dildo with one hand, a wicked smile on her face."
    sasha.say "Spread those cheeks for me, [hero.name] - because I'm coming for you!"
    "I've never been spoken to like this before, and certainly not by a girl."
    "There's something threatening about it, but then also a quality that sends a strange thrill coursing through my entire body."
    "I wonder if this is how it feels for a woman when a dominant man takes matter in hand."
    "Modern women almost always dismiss that old-fashioned kind of wish to be dominated, but some must actually enjoy it nevertheless."
    "It's weirdly liberating to feel as though all the decisions are being made by someone else for a change."
    "It takes a lot of the responsibility and fear of failure away from me too."
    "Have I been looking at this entire thing the wrong way?"
    "Surely now the need to make this a memorable encounter rests solely with Sasha?"
    "She's the one that's swinging her (metaphorical) dick about tonight."
    "Whereas all that I need to do is lie back and let her get on with it."
    "Instinctively, I part my thighs and allow Sasha to lean in close enough to bring the battering ram with her."
    sasha.say "That's right...you know this is what you want, [hero.name]!"
    "She uses one hand to guide the dildo between the cheeks of my ass and the other to begin stroking my dick at the same time."
    "My breath is coming in shallow gasps by this time, and even though I think I've managed to rationalise it all in my mind, my body is still showing signs of tension."
    "It's now that [bree.name] leans in and whispers softly into my ear."
    bree.say "Play with me..."
    "She leans over me, putting her breasts within easy reach of my hands and lips."
    "At this, my cock stiffens more quickly as I reach out to caress [bree.name]'s dangling breasts."
    "It's in this moment of pleasant distraction that Sasha finally picks her moment to pluck my anal cherry."
    play sexsfx1 slide_in
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.5
    play sexsfx1 slide_out
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=-10, v=0)
    "[bree.name]'s efforts must have relaxed me enough to at least make this a dance between the insistence of the dildo and the muscles of my ass."
    "I'd been expecting the painful sense of something hard and unforgiving being shoved up my ass."
    "But this is far more a matter of give and take, as pushing from Sasha's side sees an equal and opposite reaction pulling the dildo yet further in."
    with hpunch
    "The combination of this and Sasha's massaging of my cock is more than enough to defeat the last of my lingering paranoia."
    play sound "sd/moans/sasha/sasha_panting.ogg" loop
    play sexsfx1 slide_in
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.5
    play sexsfx1 slide_out
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=-10, v=0)
    "She begins to move back and forth, causing the dildo to do the same inside of me and matching her stroking of my dick to the same rhythm."
    play sexsfx1 slide_in
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.5
    play sexsfx1 slide_out
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=-10, v=0)
    "By now the sensations of being taken up the ass and being given what amounts to a hand-job at the same time is making me pant and bite my lip."
    "I can hear that [bree.name]'s breath is coming faster now too, as she watches the gleeful look on Sasha's face and my reactions to what she's doing."
    bree.say "Mmm...[hero.name], you're getting so big down there!"
    "[bree.name] begins to crawl down the bed, clambering over me, I guess in order to get closer to where the action is taking place."
    bree.say "Hey, Sasha - don't be selfish with it!"
    bree.say "Throw something my way?"
    play sexsfx1 slide_in
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.5
    play sexsfx1 slide_out
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=-10, v=0)
    pause 0.5
    play sexsfx1 slide_in
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.5
    play sexsfx1 slide_out
    pause 0.5
    show sasha strap at stepback(speed=0.1, h=-10, v=0)
    pause 0.5
    play sexsfx1 fuck_calm loop
    with hpunch
    "Sasha meets the request with a grin, pushing my now almost painfully erect cock in [bree.name]'s direction."
    "She returns the smile, pausing only to push the hair back behind her ear before she descends upon the proffered organ."
    play sexsfx2 bj_sucking loop
    show sasha strap breesuck
    "Hungry to be involved in the proceedings, [bree.name] wastes no time in taking the head of my cock into her mouth and caressing it with her tongue and lips."
    "She uses the angle of her mouth to pull me in deeper than I expected her to, taking me by surprise."
    "Taken alone, I could have described what either of the girls are doing to me right now as something guaranteed to blow my mind and body alike."
    "But together, I can scarcely tell the feeling of one thing from the other."
    "[bree.name]'s blow-job merges with the entirely new sensation of what Sasha's doing to me with the aid of the dildo."
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.25
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    "One pleasure doesn't seem to end where the other begins, instead each feels like it flows into the other without a definite limit or boundary."
    "And the thought that keeps occurring to me, over and again, is that I'm the only one that's going to cum."
    show sasha strap orgasm at stepback(speed=0.1, h=10, v=0)
    pause 0.25
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    "Sasha's already slick with sweat and flushed red from her efforts to use the dildo on me."
    "[bree.name] is almost desperate as she works away at my cock."
    "But neither of them is about to peak in the way they're both trying to cause in me."
    "I really can't believe that I was ever nervous about doing this!"
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    pause 0.25
    show sasha strap at stepback(speed=0.1, h=10, v=0)
    "Both Sasha and [bree.name] are pushing themselves to the limit here - and it's all for my benefit."
    "They both seem to be enjoying the whole thing though, delighted at the prospect of giving me so much pleasure."
    "I'm getting close to cumming even as this thought occurs to me, and I think that it also helps to push me over the edge."
    play sexsfx1 fuck_moderate loop
    with hpunch
    pause 0.2
    show sasha strap orgasm
    with hpunch
    "My body begins to buck, even though it's been held down thus far pretty well by the combined efforts of both Sasha and [bree.name]."
    "There's no time for [bree.name] to realise what's coming and have a choice in how she brings the blow-job to an end."
    play sexsfx1 cum_inside
    play sexsfx2 sasha_blowjob_swallow loop
    show sasha strap cumbree
    with hpunch
    "Instead she's forced to take the entirety of my ejected load in her mouth, which is already hard pressed to accommodate my cock as it is."
    with hpunch
    "Though she doesn't visibly choke on it, [bree.name] does splutter a little, and I can see the strings of cum running from the corner of her mouth."
    "Sasha can't help but let out an almost evil laugh at this, still thrusting in and out of me as she does so."
    "There's still no way in which her actions are causing me serious amounts of discomfort."
    "But all the same, without [bree.name]'s attentions alongside them and now that I've cum, the time seems to have come to call it quits all round."
    "I reach down to put a hand on the dildo, but feel Sasha give my hand a playful slap for my trouble."
    show sasha strap normal
    play sound spank
    with hpunch
    sasha.say "Hey, [hero.name] - hand's off the merchandise!"
    "She obligingly pulls the thing smoothly out of my ass, chuckling to herself the entire time."
    play sexsfx1 slide_out
    queue sexsfx1 pop_out
    scene bg black
    with fade
    scene multisleep homeharem
    show multisleep homeharem bree sasha
    with fade
    sasha.say "You've got one of your own, and while you might be jealous of it, this one's all mine!"
    stop sound fadeout 1.0
    stop sexsfx1 fadeout 1.0
    stop sexsfx2 fadeout 1.0
    with fade
    "Nobody speaks as we lie in a slick pile of bodies and limbs, cooling rapidly but still feeling the aftershocks."
    "They say that people only complain if they're unhappy with the service."
    "So I'm happy to read the silence in the bedroom as quiet satisfaction on the part of [bree.name] and Sasha."
    "I know for sure that I have no reason whatsoever to complain."

    $ sasha.love += 2
    $ bree.love += 2
    $ sasha.sub -= 2
    $ game.flags.threesomelastnight = TemporaryFlag(True, 2)
    $ sasha.sexperience += 1
    $ bree.sexperience += 1
    return

label home_harem_bree_sasha_sunscreen:
    scene bg black
    show bg livingroom
    "I walk into the living-room, fully expecting to find [bree.name] well into a marathon gaming session on the Z-Box."
    "Or else to discover Sasha slumped across one of the sofas and binging her way through a true-crime series."
    "But when I find that I'm actually alone in there, it comes as kind of a shock."
    "I was all ready to get into a heated debate about the importance of having some space around the house."
    "And now that I don't need to, I can't help feeling a little lost and a tad deflated."
    "Trying to shake off the feeling, I begin hunting for the remote and thinking of something I want to watch."
    "But that's when I hear the sound of someone calling from outside in the garden."
    bree.say "Sasha?"
    bree.say "SASHA?!?"
    bree.say "Are you there?"
    $ game.room = "pool"
    scene bg black
    show sunscreen bree sasha nosasha at center, zoomAt(1.25, (800, 720))
    with fade
    "My curiosity piqued, I sidle over to the window and take a look out."
    "And I'm instantly rewarded with the sight of [bree.name], lying on one of the sun-loungers."
    "Even better, she's in her swimsuit!"
    sasha.say "Yeah, yeah, [bree.name]..."
    sasha.say "I'm coming already!"
    sasha.say "What's up?"
    "I take a little step backwards as Sasha strolls up to where [bree.name]'s laid out."
    "I mean, I'm not really spying on them in any real sense - but I don't want to be seen all the same."
    "Sasha comes to a stop beside the lounger, and [bree.name] looks up at her with a smile."
    bree.say "Ssh!"
    bree.say "I want you to rub some sunscreen on my back before I burn up."
    bree.say "But I don't want [hero.name] to know you're doing it."
    "I can't help frowning at the idea of [bree.name] wanting to keep that a secret from me."
    "Even more so when Sasha just nods in agreement."
    sasha.say "Oh yeah, I get you!"
    sasha.say "He'd just make it weird."
    show sunscreen bree sasha -nosasha at center, traveling(1.0, 1.0, (640, 720))
    with fade
    "I feel like banging on the glass or storming straight out there to give them a piece of my mind."
    "But then I see that Sasha's already picked up the sunscreen and is squeezing a generous amount onto the palm of her hand."
    "I watch as she proceeds to spread it over both of her hands and [bree.name] obligingly pulls down the straps of her swimming-costume."
    bree.say "Thanks for doing this, Sasha..."
    bree.say "And let's keep it between us, okay?"
    sasha.say "Sure thing, [bree.name]..."
    sasha.say "It'll be our little secret."
    "And my little secret will be that I was watching the whole time and saw everything!"
    "So that'll teach them to accuse me of being sleazy and making things weird."
    "I watch with baited breath as Sasha begins to work the sunscreen into [bree.name]'s shoulders."
    "Her hands working efficiently, but still sensuously enough for it to be a thrill."
    "And as she works her way downwards, [bree.name] stretches out on the sun-lounger."
    "Letting out the occasional satisfied sigh, showing that Sasha's doing a good job."
    sasha.say "Ooh..."
    sasha.say "Feels like you've got some kinks in your back, [bree.name]."
    sasha.say "You could do with something to loosen you up."
    bree.say "Mmm…"
    bree.say "I'm so stiff and hard, Sasha..."
    bree.say "But you're doing wonders back there, you know?"
    bree.say "I feel like I should get you to give me an all-over massage."
    mike.say "OH HELL YES!"
    "I clap a hand over my mouth, realising I said that without even thinking."
    scene bg livingroom at center, zoomAt(3.0, (-300, 1300)) with hpunch
    "And I do the best I can to hide myself behind the corner next to the window, hoping that neither of them spotted me."
    sasha.say "Huh?"
    sasha.say "What was that?"
    bree.say "I dunno…"
    bree.say "But it kind of sounded like [hero.name]."
    "For a moment I think the pair of them are going to get up and come looking for me."
    "But then I breathe a sigh of relief as [bree.name] shrugs and motions for Sasha to resume her rubbing."
    bree.say "Ah, he's probably just playing on the Z-Box, that's all."
    sasha.say "Playing with himself, more like!"
    "I can feel my cheeks starting to flush as [bree.name] and Sasha burst into peals of laughter."
    show sunscreen bree sasha with fade
    "But I do the best I can to keep a lid on it and stay right where I am all the same."
    "Because by now Sasha's worked her way down to the base of [bree.name]'s back."
    "And she's getting dangerously close to the curve of her buttocks!"
    "In fact her hands are just about to..."
    bree.say "Oh, it's okay, Sasha..."
    bree.say "I can reach my own butt - so I already did it."
    sasha.say "Oh...okay, [bree.name], that's cool."
    scene bg livingroom
    with fade
    "Stifling a curse I retreat deeper into the house now that the show's over."
    "Already hoping that I can keep the image of what I just watched fresh in my mind."
    "At least until I have a chance to make the most of it."
    $ game.room = "livingroom"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
