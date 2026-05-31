init python:
    Event(**{
    "name": "morgan_kleio_event_01",
    "label": "morgan_kleio_event_01",
    "priority": 750,
    "conditions": [
        IsDone("morgan_event_06", "kleio_event_01"),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(morgan,
            Not(IsHidden()),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        Or(
            HeroTarget(Not(OnDate())),
            PersonTarget(kleio,
                OnDate()
                ),
            PersonTarget(morgan,
                OnDate()
                ),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "morgan_kleio_event_02A",
    "display_name": "About Kleio",
    "label": "morgan_kleio_event_02A",
    "duration": 0,
    "icon": "button_kleio",
    "conditions": [
        IsDone("morgan_kleio_event_01"),
        HeroTarget(
            IsGender("male"),
            MinStat("charm", 50)),
        PersonTarget(morgan,
            IsActive(),
            MinStat("love", 50),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "morgan_kleio_event_02B",
    "display_name": "About Morgan",
    "label": "morgan_kleio_event_02B",
    "duration": 0,
    "icon": "button_morgan",
    "conditions": [
        IsDone("morgan_kleio_event_01"),
        HeroTarget(
            IsGender("male"),
            MinStat("charm", 50)),
        PersonTarget(kleio,
            IsActive(),
            MinStat("love", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "morgan_kleio_event_03",
    "label": "morgan_kleio_event_03",
    "priority": 750,
    "conditions": [
        IsDone("morgan_kleio_event_02A", "morgan_kleio_event_02B"),
        IsNotDone("morgan_kleio_event_03_alternate"),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            MinStat("sexperience", 1),
            MinStat("love", 125),
            MinStat("lesbian", 9),
            ),
        PersonTarget(morgan,
            Not(IsHidden()),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            MinStat("sexperience", 1),
            MinStat("love", 125),
            MinStat("lesbian", 9),
            ),
        Or(
            HeroTarget(Not(OnDate())),
            PersonTarget(kleio,
                OnDate()
                ),
            PersonTarget(morgan,
                OnDate()
                ),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "morgan_kleio_event_03_alternate",
    "label": "morgan_kleio_event_03_alternate",
    "priority": 750,
    "conditions": [
        IsDone("morgan_kleio_event_02A", "morgan_kleio_event_02B"),
        IsNotDone("morgan_kleio_event_03"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            IsActive(),
            MinStat("sexperience", 1),
            MinStat("love", 125),
            MinStat("lesbian", 9),
            ),
        PersonTarget(morgan,
            Not(IsHidden()),
            MinStat("sexperience", 1),
            MinStat("love", 125),
            MinStat("lesbian", 9),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "morgan_kleio_event_04",
    "label": "morgan_kleio_event_04",
    "priority": 750,
    "conditions": [
        TogetherInHarem('pixie', 'kleio','morgan'),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            ),
        Or(
            PersonTarget(kleio,
                IsPresent(),
                ),
            PersonTarget(morgan,
                IsPresent(),
                ),
        ),
        PersonTarget(kleio,
            HasRoomTag("pub"),
            Not(IsHidden()),
            MinFlag("drinks", 2),
            MinStat("love", 100),
            ),
        PersonTarget(morgan,
            HasRoomTag("pub"),
            Not(IsHidden()),
            MinFlag("drinks", 2),
            MinStat("love", 100),
            ),
    ],
    "do_once": True,
    })

    Event(**{
    "name": "morgan_kleio_event_05",
    "label": "morgan_kleio_event_05",
    "priority": 750,
    "conditions": [
        'Harem.together("kleio", "morgan", name="pixie")',
        IsDone("pixie_threesome"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            Not(OnDate())
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            HasRoomTag("pub"),
            ),
        PersonTarget(morgan,
            Not(IsHidden()),
            HasRoomTag("pub"),
            )
        ],
    "do_once": True,
    })

    InteractActivity(**{
    "name": "pixie_threesome",
    "label": "pixie_threesome",
    "display_name": "Fuck Morgan and Kleio",
    "conditions": [
        TogetherInHarem('pixie', 'kleio', 'morgan'),
        IsDone("morgan_kleio_event_04"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            HasStamina(),
            ),
        Or(
            PersonTarget(kleio,
                IsPresent(),
                ),
            PersonTarget(morgan,
                IsPresent(),
                ),
        ),
        PersonTarget(kleio,
            HasRoomTag("pub"),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        PersonTarget(morgan,
            HasRoomTag("pub"),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        Or(
            PersonTarget(kleio,
                IsActive(),
                ),
            PersonTarget(morgan,
                IsActive(),
                ),
            ),
        ],
    "icon": "fuck",
    "do_once": False,
    "once_week": True,
    })

label morgan_kleio_event_01:
    show morgan surprised at center, zoomAt(1.5, (640, 1100)), startle
    show fx exclamation
    "Morgan's face suddenly turns pale with shock and she suddenly ducks down, I can only make the obvious assumption she's seen someone she'd rather not have."
    "Instinctively, my head begins to turn in the direction of the door."
    "But it stops when Morgan fixes me with an urgent stare and shakes her head."
    show morgan annoyed
    morgan.say "No, don't look behind you!"
    "She hisses this, whilst nodding sideways and down, wanting me to stare at the tabletop if need be."
    mike.say "Geez, Morgan - you look like you've seen the devil!"
    morgan.say "Close, but not quite."
    "If I was hoping that she'd say more, I seem destined to disappointment."
    "But with no explanation forthcoming from Morgan, my mind soon begins racing to find a solution of its own."
    "Who could she possibly be that afraid of bumping into that she'd turn as white as a sheet?"
    "When you actually think about it, I suppose there's only one real possibility..."
    mike.say "Your ex just walked in, didn't she?"
    show morgan angry at center, zoomAt(1.5, (640, 1100)), startle
    morgan.say "Shhh - be quiet!"
    show morgan annoyed
    mike.say "Morgan, this place is full of people, all talking and making a racket."
    mike.say "She'd have to be standing right next to us to hear what we're saying to each other!"
    "The truth of what I'm saying seems to take the edge off of Morgan's panic."
    "But while she looks more prepared to talk, she still refuses to stop hiding behind me to keep from being seen."
    mike.say "Look, if her being in here is such a problem, then maybe we should just go somewhere else?"
    "Morgan nods, but then clamps a hand on my wrist as soon as I make to get up do that we can leave."
    mike.say "What's up now?"
    morgan.say "I need you to check the coast is clear, that she can't see me on the way out!"
    "I shake my head in frustration, but then nod and begin to scan the path to the door."
    "And then an obvious thought occurs to me."
    mike.say "Morgan, you do realise that I have absolutely no idea what this girl looks like, don't you?"
    "Morgan rolls her eyes at her own stupidity before leaning in close to remedy the situation."
    morgan.say "Sorry - I was so wound up at seeing her that I clean forgot!"
    morgan.say "She's blonde, skinny, kind of punky - looks like she has a chip on her shoulder all the time."
    hide morgan with dissolve
    "Pretty unusual description, so spotting her shouldn't be too hard."
    "But despite this, when I make a quick scan of the pub, I can't see anyone that jumps out at me."
    show kleio angry at right with dissolve
    "The only person that I note is Kleio, who spots me as quickly as I do her."
    show kleio happy at right5 with ease
    "She looked pissed the moment before recognising me, but brightens up considerably as she starts to make her way over."
    hide kleio
    show morgan surprised at center, zoomAt(1.5, (640, 1100))
    with fade
    "I hold up a hand in greeting, which makes Morgan tug desperately at my arm."
    show morgan angry at startle
    morgan.say "[hero.name] - what in the hell are you doing!"
    mike.say "It's okay, don't worry."
    mike.say "I can't see any sign of your ex."
    mike.say "I was just waving at someone I know, and they're coming over to say hello."
    hide morgan
    show kleio normal
    with fade
    "It's only when I look up again and run the vague description that Morgan gave me through my mind again that I begin to feel a twinge in my guts."
    "How could I not have made the connection before now?!?"
    "A punky-looking blonde with a chip on her shoulder that's into other girls!"
    mike.say "Erm, Morgan...your ex wouldn't happen to be called..."
    show kleio at right
    show morgan angry at left
    with fade
    pause 0.2
    show morgan angry at left, vshake
    morgan.say "KLEIO!"
    "Wow, she took the words right out of my mouth."
    show kleio angry at right, vshake
    kleio.say "MORGAN!"
    "After spending a couple of seconds staring at each other, I feel their eyes turning towards me."
    $ renpy.say("Kleio & Morgan", hero.name.upper() + "!")
    menu:
        "Take Morgan's side" if morgan.love >= kleio.love:
            "As much as I can see that it must have been painful for Kleio to be dumped via text, my instinct is to side with Morgan."
            "She's such an old friend and we've been through so much together that I instantly jump to her defence when Kleio looks at me in askance."
            show fx anger at right
            kleio.say "You mind telling me what the fuck you're doing drinking with this cheating little bitch, Loverboy?"
            mike.say "Hey, calm down, Kleio!"
            mike.say "If you must know, Morgan and I were in school together."
            mike.say "She's one of my oldest friends."
            show kleio annoyed
            "Kleio crosses her arms and gives a derisive snort."
            kleio.say "Kind of a weird coincidence that - wouldn't you say?"
            show morgan annoyed
            morgan.say "Kleio, please - I had no idea we both knew [hero.name]."
            mike.say "She's telling the truth, Kleio."
            mike.say "I didn't know you were seeing her, either."
            "Kleio holds her hands up, looking like she wants to shut us up and push us away at the same time."
            $ kleio.love -= 20
            kleio.say "You know, I'm starting to feel pretty ganged-up on here!"
            "I make to move towards her, realising from the way that she flinches it was the wrong decision."
            show kleio angry at startle
            kleio.say "Don't touch me - don't come even a step closer to me!"
            "She points at Morgan with hatred plain to see in her eyes."
            kleio.say "She's a liar, and if want to take her side over mine, then I guess you're just as bad as she is!"
            hide kleio with moveoutright
            "And with that, Kleio turns her back on Morgan and me, then all but runs out of the pub."
            "In the silence that follows, all either of us can do is shrug and shake our heads, at a loss at what to say."
        "Takes Kleio's side" if kleio.love >= morgan.love:
            "It must be hard for Morgan, wrestling with all of the stuff that she has on her mind at the moment."
            "But I comforted Kleio after she got dumped via text, felt the pain that it had caused here."
            "And now here I am, sitting down, drinking and laughing with the very person who did that to her."
            mike.say "Morgan, this is really awkward - but Kleio's a good friend of mine."
            mike.say "And she told me just how much you hurt her when you dumped her like that!"
            show morgan surprised
            "Morgan shakes her head in confusion, looking like her last support has been kicked out from under her."
            show fx anger at left
            morgan.say "What...what are you saying, [hero.name]?"
            kleio.say "He's saying that he thinks you're a fucking bitch for dumping me, Morgan!"
            "I turn to Kleio, trying to motion for her to back off."
            mike.say "I wouldn't use those words exactly..."
            $ morgan.love -= 20
            show morgan angry
            morgan.say "But you're not denying it either, are you?"
            morgan.say "Jesus, [hero.name] - I thought you were my friend too!"
            morgan.say "And what with how far we go back..."
            "No matter how hard I try to keep it from happening, I can't seem to stop the balance of the conversation turning against Morgan."
            "Especially not when Kleio's already sensed her weakness, like a hyena sensing vulnerable prey."
            show kleio happy
            kleio.say "Funny, Morgan - he never mentioned you before now!"
            kleio.say "And from the looks of him, my guess is that he wishes he was a million miles away from you too!"
            hide morgan with moveoutleft
            "Looking from Kleio to myself and then back again, Morgan suddenly makes a bolt for the door."
            "I make to go after her, but Kleio grabs me by the arm."
            show kleio normal at right5
            with hpunch
            kleio.say "Ah, let her go, [hero.name]."
            kleio.say "She's not worth the energy!"
        "Don't pick a side" if hero.charm >= 50:
            "Now this is pretty awkward, huh?"
            "How often do you find that you've been comforting both people involved in a break-up?"
            "And all without knowing it at the time too!"
            "I know just how hard it's been for Morgan, dealing with all of the issues that she has in her life."
            "And I genuinely felt for Kleio when she told me that she's been dumped by someone that was cheating on her."
            "But I doubt that either of them is going to sympathise with my predicament now it's all out in the open!"
            show morgan surprised at startle
            show fx anger at right
            $ morgan.love -= 5
            morgan.say "[hero.name] - you know HER?!?"
            show kleio surprised
            kleio.say "Wait a minute, that's exactly what I was going to say!"
            morgan.say "You told me I hadn't done anything wrong!"
            show kleio angry
            show fx anger at left
            $ kleio.love -= 5
            kleio.say "Whoa, whoa, whoa - you told me this cheating little bitch didn't deserve me!"
            show morgan annoyed
            show kleio annoyed
            "In turn, they both note what the other has to say about my consoling them, and then look back at me with renewed anger."
            mike.say "Okay, just hold on a second!"
            mike.say "You both must have realised by now that I had no idea you were dating, right?"
            "Slowly, Morgan and Kleio look at each other and then nod their heads grudgingly."
            mike.say "So, you also have to accept that what I said to you both wasn't about the other, yes?"
            "I can see confusion on their faces, but I press on regardless."
            mike.say "I wasn't talking about Morgan or Kleio when I said those things."
            if game.flags.band >= 2:
                mike.say "I was talking about one of my oldest friend's ex, and some girl that had dumped my bandmate."
            else:
                mike.say "I was talking about one of my oldest friend's ex, and some girl that had dumped my [kleio.status]."
            mike.say "Don't you see - I was sympathising with both of you because neither of you is totally in the wrong or the right!"
            "Neither of them looks convinced by my words."
            "But at the very least they've stopped screaming at each other in public."
            mike.say "Couldn't you at least try to see it from each other's perspective?"
            mike.say "Maybe talk about it like civilised adults?"
            show kleio angry
            kleio.say "Not until she apologises for cheating on me!"
            show morgan angry
            morgan.say "Oh yeah - how about not until she apologises to me!"
            show morgan at center, zoomAt(1, (-200, 740))
            show kleio at center, zoomAt(1, (1500, 740))
            with move
            "And with that, they storm off in opposite directions, leaving me alone."
            "Well, that is alone and wondering how they're going to deal with this place having only one exit..."
    return



label morgan_kleio_event_02A:
    show morgan sad
    morgan.say "I'm sorry, [hero.name] - really, I am."
    morgan.say "I'd never have put you in that position if I'd only known..."
    "I shake my head, dismissing Morgan's apology, but appreciating the gesture all the same."
    mike.say "Don't be silly, Morgan."
    mike.say "How could you have had a chance of knowing that I was friends with your ex?"
    mike.say "It's just a weird coincidence, that's all."
    show morgan normal
    "She nods, and I think she's more relieved to know that I forgive her than by the actual words I just used to say so."
    show morgan annoyed
    morgan.say "I guess that you think it's a little pathetic, right?"
    morgan.say "Dumping her with a text and not saying it to her face?"
    mike.say "Let's just say that, in Kleio's case, I can see why you'd make that choice!"
    mike.say "Well, I did get to see - didn't I?"
    show morgan happy
    "Morgan chuckles at this, as though she finally feels able to see the funny side of things."
    show morgan normal
    morgan.say "Yeah, she's kind of fierce when she's angry, huh?"
    mike.say "I'd say Kleio's bark is worse than her bite."
    mike.say "But it really isn't - the one's as bad as the other!"
    show morgan happy
    "While we're sharing a laugh at Kleio's expense, I can't help starting to feel more than a little guilty."
    "I can more than sympathise with her side of the argument, and I suddenly feel the need to defend Kleio in her absence."
    show morgan normal
    mike.say "Joking aside though, Morgan - she's not wrong to be pissed at how things ended between the two of you."
    mike.say "That's not me taking a swipe at you, just looking at the facts of the matter, you know?"
    "For a moment I think that Morgan's going to argue the point, maybe even get mad at me."
    "But then she nods and sighs, letting out what sounds like a hell of a lot of pent up frustration."
    show morgan annoyed
    morgan.say "I guess I'd be pretty pissed if the roles had been reversed."
    morgan.say "And it wouldn't be so bad if I'd actually hated Kleio too!"
    morgan.say "We just seemed to meet and get together at the worst possible time."
    mike.say "Yeah, I remember you saying that you just didn't feel like you were that into her any more."
    mike.say "Like there was someone else..."
    "I feel bad fishing like this, but there's still a part of me that wants to know if it was seeing me that did it."
    "I have to know if she actually dumped Kleio because of the other girl or me."
    show morgan sad
    morgan.say "It's complicated, I know."
    show morgan annoyed
    morgan.say "But then I've always been kind of a complicated girl!"
    "Well, that was suitably vague and served only to keep me guessing!"
    "I suppose that the right thing to do would be to forget about myself for the time being and focus on helping Morgan and Kleio."
    "That's not to say that I stop thinking about the possibility for a moment."
    mike.say "Kleio's kind of prickly when you first meet her, but she's worth persevering with."
    mike.say "Despite the constant insults that she sends my way, I really do think of her as a good friend."
    mike.say "Maybe you should consider thinking of her that way too?"
    show morgan normal
    "Morgan shrugs, but she has an upbeat expression on her face as she does so."
    morgan.say "Maybe - we'll see."
    morgan.say "Thanks for the chat, [hero.name]."
    morgan.say "You've given me a lot to think about."
    return

label morgan_kleio_event_02B:
    "I know that something's up the moment that I see Kleio and note that she's unnaturally quiet, almost shy towards me."
    "If I hadn't been caught up in the middle of her rather explosive confrontation with Morgan the other day, I'd have assumed she was ill!"
    "This definitely isn't the same Kleio that thought nothing of accusing Morgan and I of being involved in some kind of grand conspiracy against her."
    "Or causing an embarrassing scene in front of the entire pub at the same time too..."
    show kleio sad with dissolve
    kleio.say "Hey, [hero.name]..."
    kleio.say "I guess you're still pretty mad at me, huh?"
    "The truth is that I was just that after the argument in the pub, but more at Kleio and Morgan fighting in public than anything else."
    "But it didn't take me long to cool down and realise that the complications of the one of them being the other's ex really didn't change anything."
    "I still sympathised with Morgan's confusion about just who and what she wanted in a relationship."
    "And I also felt sorry for Kleio being dumped by text without knowing all of the facts of the matter too."
    mike.say "No, Kleio."
    mike.say "I'm not mad."
    mike.say "To be honest, I thought that you'd be the one mad at me!"
    show kleio normal
    "Kleio manages to give me a weak smile as she shakes her head at this."
    kleio.say "Nah, not me!"
    kleio.say "I figured that I already lost a girlfriend over this."
    kleio.say "So I should try not to lose a friend as well."
    kleio.say "More so one that knows her better than I ever did too!"
    "Now, as the subject turns to Morgan, it's my turn to give Kleio a similarly weak smile."
    mike.say "Would you believe me if I said that I really didn't?"
    show kleio surprised
    show fx question
    "Kleio's expression becomes puzzled at this admission."
    kleio.say "What's that supposed to mean?"
    mike.say "Well, I've only just found out some things that I never knew about Morgan too."
    mike.say "Stuff I had no idea about back when we were kids."
    show kleio annoyed
    kleio.say "You have to tell me what it is now - you can't leave me in the dark after telling me that!"
    mike.say "Okay, but promise that you won't laugh?"
    show kleio normal
    "Kleio nods hastily, instantly calling into question the worth of her assurance."
    mike.say "I only just found out that she's actually a girl."
    "Kleio stares at me, clearly waiting for the punchline, or for me to tell her that I'm pulling her leg."
    mike.say "It's the truth - when we were at school, I thought she was a guy!"
    show kleio happy
    "Kleio bursts into peals of laughter, which is not exactly the reaction that I'd been aiming for with my confession."
    "I try to wait it out, to let her get it out of her system before I say anything else."
    "But when she doesn't seem to be close to stopping, I begin to lose my temper just a little."
    show kleio normal
    mike.say "Okay, okay - it's the funniest thing ever."
    mike.say "Can you please stop laughing at me now?"
    kleio.say "Oh god, [hero.name] - please tell me that you don't still go round thinking girls are guys!"
    mike.say "No, of course not!"
    mike.say "Look, she was a tomboy when we were kids, okay?"
    mike.say "She hung around with the guys, played rough and even beat up some guys bigger than her back then!"
    "Kleio suddenly adopts a look of exaggerated horror, clutching her hands to her mouth."
    show kleio happy
    show fx exclamation
    kleio.say "Wait a minute, [hero.name] - you don't think I'm a guy too, do you?!?"
    "She erupts into a new burst of laughter at my expense, wiping a tear from the corner of her eye as she does so."
    mike.say "Are you quite finished?"
    mike.say "My point was that you can think you know all there is to know about a person and still be floored by something you didn't."
    mike.say "And I think all three of us have been victims of that here."
    show kleio normal
    "Kleio finally manages to stop laughing, holding her hands up in a gesture of appeasement."
    kleio.say "Okay, okay - I get your point."
    kleio.say "What she did to me was still shitty."
    kleio.say "But from the sound of it, she's got her own fair share of issues too."
    mike.say "If it helps, Kleio - Morgan told me that she never slept with the other girl, just saw a movie with her."
    mike.say "And for what it's worth, I believe her."
    show kleio happy
    "When Kleio laughs this time, it's in a rueful, ironic tone."
    kleio.say "It doesn't help all that much."
    kleio.say "But at least it's something!"
    kleio.say "Thanks for talking it over with me, [hero.name]."
    mike.say "No problem, Kleio - thanks for listening to what I had to say."
    "As the conversation winds down, I find myself hoping that I've been able to help Kleio deal with what happened between herself and Morgan."
    "But part of me is sure that this won't be the last I'll hear about the matter from either of he sides involved."
    return

label morgan_kleio_event_03:
    "It's funny how things turn around sometimes, like my being stuck in the middle of the messy break-up between Morgan and Kleio."
    "When the shit first hit the fan, I was stuck trying to explain myself to both sides and make them see sense all at once."
    "But in the days that followed, I found the pair of them coming to me of their own accord to apologise and find a shoulder to cry on."
    "I tried to be a good friend in both cases, sympathising with their complaints, but then playing Devil's advocate for the other."
    "And for the most part it seemed to work, Morgan and Kleio climbed down a little and tried to see it from the other side."
    "I'm not sure how I fit into all of this, with one of my oldest friends and my bandmate using me as a mediator in their lover's feud."
    "It doesn't help that I find the pair of them undeniably hot into the bargain..."
    "Though that's a fact that I've had to try and ignore throughout all of this affair."
    "But talking to one of them without the other is never going to get this thing sorted."
    show morgan annoyed at left5
    show kleio annoyed at right5
    with dissolve
    "When we're finally all in the same place, it's more than a little tense."
    "Neither Morgan nor Kleio says a word."
    "It's though they've got a lot to say, but each wants to make the other go first."
    "Not wanting to let one take the bait and then have the other pounce on them, I decide to break the silence myself."
    mike.say "It's great that you could both meet like this."
    mike.say "I think it shows that you've accepted what happened as water under the bridge."
    mike.say "That you're ready to move on and let it go, right?"
    "Morgan is the first to respond to this, as I thought she might be."
    show morgan sad
    "She looks pained and awkward, but she speaks up all the same."
    morgan.say "Like you said, [hero.name] - it sucks to be doing this, but I want to get it sorted between us."
    "I nod, and then look towards Kleio, giving her a clear opportunity to follow Morgan's lead."
    "She makes a little snorting sound and, for a moment, curls her lip as though she's about to go on the offensive."
    "But then she sighs, and the fight seems to drain out of her with the exhalation of breath too."
    kleio.say "Sure, whatever - it's dumb to keep on fighting over it now, anyway."
    kleio.say "What's done's done."
    show kleio normal
    "Kleio holds up her hands in a gesture of surrender."
    kleio.say "As far as I'm concerned, Morgan - we're cool."
    show morgan normal
    "Morgan nods in response to this."
    morgan.say "Me too, Kleio."
    "They both manage a weak smile, and then I see Kleio's mouth twist into a wicked smirk."
    show kleio seductive
    kleio.say "For what it's worth, we had some fucking good fun together, didn't we!"
    show morgan blush
    "At this, I see Morgan colour a little, remembering something that's most likely going to remain private between the two of them."
    morgan.say "Yeah, but I think we came out of this knowing what's really important to us in the end..."
    show kleio a zorder 1 at center, zoomAt(2.5, (940, 1640))
    show morgan a zorder 2 at center, zoomAt(2.5, (340, 1640))
    with dissolve
    "While I've been tensely watching this edgy situation lurch towards a pretty positive conclusion, I feel like I've been holding my breath the entire time."
    "That's why it comes as a surprise to feel someone subtly taking hold of my hand out of the line of sight."
    "I wouldn't have made anything obvious out of it, but for the fact that I realise that both my hands are being grasped at the same time."
    "And I'm also pretty sure that neither Morgan nor Kleio would have noticed that they both held my hands if I hadn't yelped and held them up for all to see."
    morgan.say "Well, that's...interesting!"
    kleio.say "Yeah, it sure as hell explains a lot!"
    mike.say "Not to me it doesn't!"
    if not all([person.love >= 125 and person.sub >= 25 and person.lesbian >= 9 for person in [morgan, kleio]]):
        show fx heart at left
        morgan.say "Okay, okay - seeing [hero.name] again stirred up my feelings for him."
        morgan.say "It was the major reason that I broke it off with you, Kleio."
        show kleio annoyed
        show fx anger at right
        "Kleio frowns at this, clearly not happy with the new information."
        kleio.say "That's ancient history, Morgan!"
        kleio.say "[hero.name] really helped me out after you dumped me."
        kleio.say "Helped me pick myself up again - he makes me feel wanted...special, even!"
        "They both fall silent for a moment, brooding on all that's been said."
        morgan.say "It's pretty obvious that there's one more person in this picture than there needs to be."
        kleio.say "Yeah - but since neither of us wants the other to be in it, [hero.name] has to choose who leaves!"
        "As one, they turn to face me, their expressions making it clear that I have to make a difficult choice."
        "And I have to make it right now!"
        menu:
            "Choose Morgan" if morgan.love >= kleio.love.val*0.75:
                "Honestly, I thought this would be tough."
                "But I hardly hesitate for a moment before speaking up for myself."
                mike.say "Morgan...I want to be with you."
                mike.say "If you want that too?"
                show morgan blushhappy
                show fx heart at left
                show kleio a sad
                "Much to my delight, she smiles broadly and nods at this."
                morgan.say "Yeah, I do."
                morgan.say "I feel like we just weren't ready for each other back when we were kids."
                morgan.say "But now...now it could really work between us!"
                show morgan a annoyed
                hide kleio
                show kleio sad zorder 1 at center, zoomAt(1.5, (940, 1040))
                "I feel Kleio let go of my hand and step away from us."
                kleio.say "If that's what you want, [hero.name], swing away."
                kleio.say "At least I know I'm not good enough for either of you now!"
                hide kleio with moveoutright
                "Morgan and I both try to say something to Kleio, but she cuts us off and turns to go."
                "I feel awful as I watch her walk away."
                "And guilty as I enjoy the sensation of Morgan pulling me into a possessive embrace."

                $ band_harem = Harem.find(kleio, name="band")
                if any(band_harem):
                    $ band_harem[0].destroy()
                else:
                    $ kleio.set_gone_forever()
                $ Room.find("studio").hide()
            "Choose Kleio" if kleio.love >= morgan.love.val*0.75:
                "I can almost feel the pull of the past whenever I look at Morgan."
                "But strangely, that's not the emotion and feeling that's having the most effect on me right now."
                "All I can recall is the pain that Kleio came to me with when she'd been dumped."
                "That and just how much I felt for her at the time, how much I wanted to make it right again."
                show fx heart at right
                show kleio a blush
                show morgan a sad
                mike.say "Kleio...I want to be with you."
                mike.say "I think I love you, actually!"
                show kleio a normal blush
                "I was expecting triumph to appear on Kleio's face, but instead she looks to be on the verge of tears."
                kleio.say "Shit...why am I crying like a little bitch?!?"
                kleio.say "Don't say it's because I love you too, [hero.name]!"
                show kleio a annoyed
                hide morgan
                show morgan sad zorder 1 at center, zoomAt(1.5, (340, 1040))
                "I feel Morgan suddenly let go of my hand as she steps away from Kleio and myself."
                morgan.say "But...[hero.name]..."
                morgan.say "I broke it off with her because of how you made me feel!"
                mike.say "I'm sorry, Morgan - but I can't control how I feel, either!"
                mike.say "And all of this has just made me realise how much I care for Kleio..."
                hide morgan with moveoutleft
                "Morgan looks like she's going to say more, but then she turns and dashes away without another word."
                "All I can do is watch her go, reassured by the feel of Kleio's hand squeezing my own."
                $ morgan.set_gone_forever()
    elif not (morgan.love >= 125 and morgan.sub >= 25 and morgan.lesbian >= 9):
        morgan.say "I...I can't deal with all of this shit."
        show morgan sad
        show kleio sad
        morgan.say "Really, I can't!"
        morgan.say "I used to think that I knew who I was, what I wanted."
        morgan.say "But ever since you came back into my life, [hero.name], it's like I don't know myself anymore!"
        show morgan sad zorder 1 at center, zoomAt(1.5, (340, 1040))
        "I make to comfort Morgan, but she immediately lets go of my hand and begins to back away."
        morgan.say "No...please - don't touch me."
        morgan.say "I'm so confused...I don't know what I'll do if you hold me!"
        show kleio normal
        "Kleio looks at me, her eyes wide at Morgan's apparent melt-down."
        "For once in her life, she seems to be utterly lost for words."
        morgan.say "I need to get away from all of this..."
        morgan.say "I need to be somewhere I can be myself, not try to be what I think other people want me to be!"
        hide morgan with moveoutleft
        "Morgan looks like she's going to say more, but then she turns and dashes away without another word."
        "All I can do is watch her go, reassured by the feel of Kleio's hand squeezing my own."
        $ morgan.set_gone_forever()
    elif not (kleio.love >= 125 and kleio.sub >= 25 and kleio.lesbian >= 9):
        show kleio angry
        show morgan sad
        kleio.say "It's pretty clear I'm the proverbial third wheel around here!"
        "When Morgan and I try to argue, she shakes her head, giving us an ironic chuckle."
        kleio.say "Nah, I can see it, even if you two can't."
        kleio.say "You're the ships that passed in the night from way back in the day!"
        kleio.say "I can't compete with that shit."
        hide kleio
        show kleio sad zorder 1 at center, zoomAt(1.5, (940, 1040))
        "A second protest gets the same brush off, as Kleio lets go of my hand."
        kleio.say "Ah...I need to get away from here, clear my head."
        kleio.say "Maybe this was just what I really needed - the chance to make a change, a new start!"
        "Morgan and I both try to at least say something to Kleio, but she cuts us off and turns to go."
        hide kleio with moveoutright
        "I feel awful as I watch her walk away."
        "And guilty as I enjoy the sensation of Morgan pulling me into a possessive embrace."

        $ band_harem = Harem.find(kleio, name="band")
        if any(band_harem):
            $ band_harem[0].destroy()
        else:
            $ kleio.set_gone_forever()
        $ Room.find("studio").hide()
    else:
        show morgan blush
        show fx heart at left
        morgan.say "Well, all I know is that I was feeling like shit about this mess."
        morgan.say "But then I found a good friend that helped to pull me through it."
        show kleio blush
        show fx heart at right
        kleio.say "Funny, because I was thinking the exact same thing just now."
        "Morgan and Kleio look at each other for a moment, and then turn to regard me, sly smiles on their faces."
        kleio.say "There was someone there for both of us."
        kleio.say "Someone that was sure we could make it up and be friends."
        morgan.say "Now, I couldn't be the one to take that person away from you, Kleio."
        kleio.say "And I couldn't bear to take them away from you either, Morgan."
        "My eyes dart from one to the other as I try to figure out just what they're suggesting here."
        morgan.say "I do know that good friends can always share things..."
        show kleio seductive
        kleio.say "Do you think we could do that?"
        show morgan blushhappy
        morgan.say "I think we could try..."
        "At this, Morgan wraps herself around one side of me, and Kleio around the other."
        "Neither of them says another word, simply pressing themselves close to me in the most suggestive manner possible."
        "They can't help but note my resulting state of confused arousal, laughing to each other and stroking my chest to make matters worse."
        "I think I'm starting to see where this is going, but I don't know whether to be excited, terrified, or both!"
        $ Harem.join_by_name("pixie", "kleio", "morgan")
    return

label morgan_kleio_event_03_alternate:
    "After the painful process of untangling the mess that Kleio, Morgan and I were in, I thought that was the last of it."
    "The whole thing was like pulling teeth, and I for one was more than ready to just move on and forget all about what happened."
    "Which is why it takes me by complete surprise when, out of the blue, Kleio's the one to bring it up again."
    kleio.say "Hey, [hero.name]."
    show kleio b sadsmile
    kleio.say "I...I wanted to ask you something..."
    "Two warning signs right there, even before she gets into the finer details."
    "The first is Kleio failing to call me 'Loverboy'."
    "And the second is her asking permission for absolutely anything at all!"
    mike.say "Ah...okay, Kleio."
    mike.say "What's up?"
    show kleio annoyed
    kleio.say "Urrgh..."
    kleio.say "It's about Morgan..."
    "Each and every word sounds like it's being dragged out of Kleio at great cost."
    "And I can tell that even broaching the subject with me is hard for her to manage."
    "I raise my eyebrows in surprise, because like I said, I thought this was all settled."
    mike.say "Morgan?"
    show kleio normal
    kleio.say "Yeah, Morgan!"
    kleio.say "You know - little chick with the blue hair?"
    show kleio upset
    kleio.say "The one I used to date and you thought was a guy?!?"
    "Almost as soon as she begins to get spiky and irritable, Kleio stops in her tracks."
    show kleio normal
    "It's like I can see that she doesn't really have the energy for a fight right now."
    "She seems to deflate before my eyes, sighing and shrugging her shoulders."
    kleio.say "I'm sorry."
    kleio.say "I didn't mean to go off like that..."
    "What's going on here - Kleio actually apologising?"
    "Now I know this must be serious."
    mike.say "What about her, Kleio?"
    mike.say "I thought we already sorted that out?"
    "Kleio gives me a weary smile and shakes her head."
    "She looks so helpless that I can almost feel my heart aching for her."
    kleio.say "Me too."
    show kleio a whining
    kleio.say "But I just can't keep thinking about her!"
    "For the first time since Kleio started talking, it's my turn to feel vulnerable."
    "What does she mean by that?"
    "What does that mean for us?!?"
    "I try as best I can to keep my emotions under wraps as I reply."
    mike.say "What are you trying to say, Kleio?"
    mike.say "Are you choosing Morgan over me?"
    show kleio stuned
    "I see Kleio's eyes go wide at the second question, and she shakes her head."
    "It's almost as though that was the last thing she expected to hear me say."
    "But what else am I supposed to think?"
    "Especially when she tells me she can't get her ex-girlfriend out of her mind!"
    show kleio surprised
    kleio.say "Oh no...fuck no!"
    kleio.say "That's not what I mean at all!"
    show kleio sad
    mike.say "Well, what do you mean?"
    show kleio b sadsmile
    kleio.say "I mean I can't decide between the two of you - that's what I mean."
    show kleio seductive
    kleio.say "I mean that I want to have you both!"
    kleio.say "That'd be cool, wouldn't it?"
    kleio.say "We could share - right?"
    with hpunch
    "Am I hearing this right?"
    "Kleio's actually asking me if I'm okay with a threesome?"
    if (kleio.love >= 125 and kleio.sub >= 25 and kleio.lesbian >= 9) and (morgan.love >= 125 and morgan.sub >= 25 and morgan.lesbian >= 9):
        "I take a little time to turn over what Kleio just said in my mind."
        "Call me paranoid if you like, but I'm looking hard to find the catch."
        "Because there has to be one, right?"
        "I mean, she wouldn't actually be asking me to have the both of them."
        "Would she?"
        "But that's what it sounds like..."
        mike.say "You...and me...and Morgan?"
        "Kleio nods slowly, like she's explaining herself to a complete moron."
        show kleio normal
        kleio.say "Yes - me and you and Morgan."
        "I nod as well, just waiting for something to come along and end the illusion."
        "Like any moment I'm going to wake up and find this was all some crazy dream."
        mike.say "Well..."
        mike.say "I guess that would be okay with me."
        mike.say "I mean, if it's what you two want..."
        show kleio seductive
        "Kleio narrows her eyes at me, shaking her head."
        "Her lips curl into a knowing smile."
        show kleio normal
        kleio.say "So you're in?"
        kleio.say "You know, if you think you could handle it?"
        kleio.say "The thought of all three of us getting it on?"
        kleio.say "You must be curious about what Morgan and I got up to together, right?"
        mike.say "I think I can, Kleio."
        mike.say "So long as you promise to be gentle with me?"
        show kleio at center, traveling (1.5, 3, (640, 1000))
        "At this, Kleio leans closer."
        "Her tone becomes mockingly sincere."
        kleio.say "Oh, we will."
        kleio.say "I promise we'll be gentle."
        show kleio at center, traveling (2, 2, (640, 1280))
        pause 3
        kleio.say "Until we're not..."
        show kleio seductive
        "She winks at me, and I take it as a sign that the deal's been made between us."
        "And I can't help beginning to sweat at he mere thought of what might lie ahead."
        $ Harem.join_by_name("pixie", "kleio", "morgan")
    else:
        "I admit that it sounds like a pretty sweet deal from my point of view."
        "I mean, what guy wouldn't want to swap a relationship with one hot girl for one with two?"
        "But I'm sorry, I just can't bring myself to be that shallow."
        "The whole thing with Kleio and Morgan was a terrible mess."
        "All three of us made mistakes, said things that we never should have done."
        "We're lucky that we came out of it with anything to show apart from bitter memories and broken hearts."
        "And that's why I just can't bring myself to say yes."
        mike.say "No, Kleio."
        mike.say "I don't think that would be a good idea."
        "Kleio looks at me as though she doesn't quite understand my answer."
        show kleio a stuned at hshake
        "And then she shakes her head, the motion seeming to clear her thoughts too."
        show kleio surprised at center, traveling (1.5, 1, (640, 1000))
        kleio.say "Are...are you actually serious?"
        kleio.say "I'm standing here asking you to hook up with me and another girl?"
        show kleio at center, traveling (2, 2, (640, 1280))
        kleio.say "Isn't this the kind of thing that guys dream of?"
        show kleio sadsmile
        mike.say "Don't be like that, Kleio."
        mike.say "I'm not that kind of guy."
        mike.say "And you're not that kind of girl either."
        mike.say "You and Morgan are better than that."
        show kleio sad at stepback(0.05, 5,0)
        pause 0.05
        show kleio sad at stepback(0.05,-5,0)
        "Kleio shakes her head for a second time."
        "I can see that she's more than disappointed by my answer."
        "But it looks like she's not going to argue with me all the same."
        show kleio annoyed
        kleio.say "Ah..."
        kleio.say "If that's what you really want."
        show kleio sad
        mike.say "I think it is, Kleio."
        show kleio at startle(0.05, 5)
        "This time she nods."
        "And that's the last she has to say on the matter."
        "At least for now."
        $ kleio.love -= 10
    return

label morgan_kleio_event_04:
    scene bg house
    show kleio blush at center, zoomAt (1.25, (440, 1000)), swing(1.0, 1.0, 1.0, -3.0, 2.0)
    show morgan blush at center, zoomAt (1.25, (840, 1000)), swing(1.0, 1.0, 1.0, -2.5, 1.8)
    with fade
    "What is it about being drunk that means the more you try to be quiet, the louder you end up being?"
    "Back in the pub, Kleio, Morgan and I didn't seem to be any more noisy than the rest of the people in there."
    "But now that we've made it back to my place, the rest of the world seems to be veiled in complete silence."
    "Whereas we've turned into a trio of clumsy, giggling idiots with the volume turned up to eleven!"
    "As I struggle to make my keys fit into the lock so that I can open the front door, I yell at them both to be quiet."
    mike.say "Shhhh...shh...shhut up!"
    mike.say "We gotta be real quiet..."
    show morgan happy
    show kleio happy
    "All this achieves is another fit of giggles and snorts from Kleio and Morgan as they huddle close behind me."
    mike.say "I'm serious, you guys...and girls!"
    mike.say "My housemates can't hear us..."
    mike.say "They can't know we're gonna have a threesome!"
    show kleio surprised
    kleio.say "Huh...a what?"
    show kleio annoyed
    show morgan annoyed
    morgan.say "Yeah, [hero.name]...I didn't hear you!"
    show morgan sadsmile
    "If I was more sober, I'm sure I'd have just shook my head and ignored them."
    "But I'm not, so I don't."
    mike.say "I said my housemates can't know we're sneaking in for a threesome!"
    show kleio whining
    kleio.say "Nah, didn't hear that!"
    show kleio sadsmile
    show morgan whining
    morgan.say "Me neither!"
    show morgan sadsmile
    mike.say "Urgh...what are you guys - deaf or something?"
    with vpunch
    mike.say "I said...MY HOUSEMATES CAN'T KNOW WE'RE HAVING A THREESOME!"
    "As soon as the words have left my mouth with such volume, I realise what I've done."
    show morgan happy
    show kleio happy
    "Instantly, Kleio and Morgan collapse against each other with laughter."
    morgan.say "Thanks, [hero.name] - I heard you that time alright!"
    show morgan normal
    kleio.say "Yeah, I wouldn't worry about your housemates, Loverboy."
    kleio.say "You should worry about the whole neighbourhood knowing what you're up to!"
    show kleio normal
    "Luckily for me, the lock and key choose to cooperate with me in the next couple of seconds."
    scene bg livingroom with fade
    "The front door opens and we almost fall into the hallway, with me hanging on by the key."
    "From there, I lead the girls through the house, tip-toeing like something from a kid's cartoon."
    "I guess that we must have either made no more noise or picked a night when both [bree.name] and Sasha are out."
    "Or maybe they've just taken pity on me and chosen not to step out of their rooms and demand to know what's going on."
    "No matter the reason, because the end result is still that we make it to my bedroom door."
    "And as there's no lock on this door, it takes me far less time to yank it open."
    scene bg bedroom1 with fade
    "Almost the second that I do so, Kleio and Morgan push past me and hurry into the room."
    "Pushed this way and that by their jostling, I open my mouth to protest."
    show kleio blush at center, zoomAt (1.25, (440, 1000)), swing(1.0, 1.0, 1.0, -3.0, 2.0)
    show morgan blush at center, zoomAt (1.25, (840, 1000)), swing(1.0, 1.0, 1.0, -2.5, 1.8)
    with fade
    "But then I see them begin to pull and tug at each other's clothes, starting to undress before me."
    "And I suddenly remember the reason that we're here, then wonder how I could ever have forgotten..."
    "Kleio and Morgan tumble onto the bed as they finish stripping each other off."
    show kleio naked seductive blush
    show morgan naked
    with dissolve
    "I watch them become a desperate tangle of limbs as they kiss with ever mounting passion."
    "The sight of their naked bodies intertwined is more than enough to keep me totally entranced."
    "It takes them both stopping and looking me straight in the eye to bring me back to reality."
    show kleio talkative
    kleio.say "Check out Loverboy here."
    kleio.say "He'd trip over his tongue if he could move an inch!"
    show kleio normal
    show morgan happy
    "Morgan giggles at Kleio's words, but beckons to me all the same."
    show morgan talkative
    morgan.say "What are you waiting for, [hero.name]?"
    morgan.say "You're not just gonna watch, are you?"
    show morgan normal
    "I have to physically shake myself to snap out of it."
    "But as soon as I feel like I'm in the room again, I start to strip off too."
    mike.say "Yeah...of course I am not."
    mike.say "Just got watching you guys and...well, I kind of zoned out there for a second!"
    "Kleio and Morgan watch me, still giggling as I struggle to get undressed and cross the room all at once."
    "It's all I can do to make it to the bed without tripping over myself and collapsing onto the floor."
    "But as I climb onto the bed, they make room for me, crawling backwards towards the pillows."
    "They begin to kiss and caress each other once more, but now I'm close enough to reach out and touch them."
    "Both Kleio and Morgan have their thighs parted, as if offering me an open invitation."
    "Each one of them looks impossibly inviting, slick and ready for me."
    "And for a moment I have no idea how to choose between the two of them."
    "So in the end, I decide not to."
    hide kleio
    hide morgan
    show kleio morgan threesome out
    with fade
    if renpy.has_label("pixie_harem_achievement_2") and not game.flags.cheat:
        call pixie_harem_achievement_2 from _call_pixie_harem_achievement_2
    "Laying myself down, I put my head between Kleio's thighs and my dick between Morgan's."
    "Needless to say that my cock's already rock-hard by this point."
    "But I still need to glance up to make sure it finds its way home."
    show kleio morgan threesome vaginal morganclose
    "I get all the confirmation I need when I hear Morgan moan through her kissing Kleio."
    "The sound makes me all the more excited in turn, and I push in as far as I can go."
    "Even from this angle, Morgan's tight little pussy feels incredible."
    "But I can't let Morgan have all the fun and Kleio miss out, now can I?"
    "Parting the lips of Kleio's pussy, I begin to tease her with the tip of my tongue."
    "The unique taste of her floods my mouth, like licking the top of a battery."
    "Morgan's getting every inch of dick that I have to give right now."
    show kleio morgan threesome vaginal close
    "But I can be so much more creative with my tongue, as Kleio soon finds out."
    "As I probe ever deeper into the folds of her pussy, she starts to make noises of her own."
    "Unlike Morgan's moans from having my cock inside of her, Kleio yelps and cries out at what I'm doing to her."
    show kleio morgan threesome vaginal morganorgasm
    "And when I can steal a moment to look up, I see her cheeks flushing and her eyes rolling back into her head."
    "This only serves to make me redouble my efforts towards them both."
    show kleio morgan threesome vaginal orgasm
    "I watch as my cock thrusting in and out of Morgan and my tongue exploring Kleio's pussy push them ever closer to the edge."
    "By now it's all that they can do to keep on pressing their lips together."
    "Both Kleio and Morgan are writhing on the bed thanks to my attentions."
    "And it can't be long before one of them cums in the most spectacular manner possible."
    "But a moment later a twinge from down below makes me think I might beat them to it..."
    menu:
        "Cum inside":
            "I make no effort to pull out of Morgan, instead thrusting in and out of her until the very last moment."
            show kleio morgan threesome vaginal cumshot with vpunch
            "As if in response to the sensation of me cumming inside of her, Morgan pulls Kleio in even closer."
            with vpunch
            "I watch as she practically shoves her tongue into the other girl's mouth without mercy."
            "Kleio has no choice but to let Morgan have her way, returning the kiss as best she can."
            "I keep on thrusting into her, using up the last of my energy as I do so."
            "But I can't help thinking that Morgan seems to be using her tongue in the same way as I am my cock."
            "The more I push into her pussy, the more she forced her tongue down Kleio's throat!"
            "In the end, I can't tell if Kleio's gasping from an orgasm or the actual fear of being suffocated!"
            "But as the whole thing settles down into an exhausted afterglow, there are no complaints or recriminations to be heard."
            "Only the sound of three people panting and gasping as they lie in a pile of sweaty limbs."
            "In fact, it's the quietest the three of us have been all night."
        "Share the love" if hero.sexperience >= 15:
            show kleio morgan threesome out
            "I pull my cock out of Morgan and then my tongue out of Kleio without warning."
            "As I'd hoped, the surprise of being denied my attentions makes the pair snap to attention."
            hide kleio
            show kleio naked seductive blush at left5
            show morgan naked blush at right5
            with fade
            kleio.say "Hey...what gives?!?"
            morgan.say "Aww, no fair!"
            "I ignore their protests as I get up from the bed and beckon them to follow."
            "At first they look annoyed and puzzled by my actions, not getting the hint."
            "But then I point at the floor before me with one hand."
            "At the same time, the other is stroking the shaft of my cock, still slick from Morgan's pussy."
            "Kleio seems to catch on first, snaking off of the bed and urging Morgan to follow."
            "I see her eyes go wide and a smile spread across her face as realisation dawns."
            hide kleio
            hide morgan
            show kleio morgan cumshot look
            with fade
            "And a moment later, both of them are kneeling down in front of me."
            "Like a pair of begging bitches, Kleio and Morgan wait in silence, their mouths open."
            show kleio morgan cumshot cum with vpunch
            pause 0.2
            with vpunch
            "The first streamer of cum somehow manages to spread itself across both their faces."
            show kleio morgan cumshot facecum mouthcum -cum
            "They laugh in surprise, ensuring that the second hits their tongues and lips."
            show kleio morgan cumshot kiss
            "Soon enough they're covered in cum, smiling and giggling as they lick themselves clean."
    $ game.room = "bedroom1"
    call sleep from _call_sleep_54
    return

label morgan_kleio_event_05:
    scene bg pub
    "You know those times when you're just sitting there, all innocent and unaware."
    "And then you get the uncanny feeling that you're being watched?"
    "Well that's happening to me right now as I'm sitting in the pub."
    "All I did was come in here to relax with a cold beer and forget my problems."
    "And now I can't help looking up to see what's causing the sensation."
    show kleio at left5 with dissolve
    kleio.say "Hey there, Loverboy!"
    kleio.say "What're ya doing?"
    show morgan happy at right5 with dissolve
    if morgan.male >= 66:
        morgan.say "Yeah, man."
        morgan.say "What are the chances of us bumping into you?"
    elif morgan.male >= 33:
        morgan.say "Hey, [hero.name]..."
        morgan.say "What a coincidence you're here too!"
    else:
        morgan.say "Oh, hi, [hero.name]..."
        morgan.say "Fancy seeing you in here!"
    show morgan normal
    "I look from Kleio to Morgan and then frown."
    "Something smell pretty fishy here."
    mike.say "Yeah, you guys..."
    mike.say "What are the chances you'd just happen to find me in my local pub!"
    mike.say "Like literally the closest place to my house that I'd ever be!"
    mike.say "No chance you tried looking there for me first, huh?"
    show kleio annoyed
    kleio.say "Geez, Loverboy..."
    kleio.say "Do you ever listen to yourself?"
    kleio.say "You sound super paranoid right now!"
    show kleio normal
    "I roll my eyes at Kleio's weak attempt to deflect me."
    "But before I can say another word, Morgan cuts in."
    if morgan.male >= 66:
        morgan.say "Never mind all that."
        morgan.say "We need to ask you something."
    elif morgan.male >= 33:
        morgan.say "Whatever, whatever..."
        morgan.say "We've got something important to ask you!"
    else:
        morgan.say "Oh stop it, Kleio!"
        morgan.say "At this rate we'll never get to ask him!"
    "Now they have my interest piqued."
    mike.say "Ask me what, exactly?"
    show kleio annoyed
    "Kleio frowns in Morgan's general direction."
    "She's clearly annoyed at having her fun curtailed."
    kleio.say "Okay, Morgan!"
    kleio.say "No need to beat about the bush!"
    show kleio blush
    kleio.say "Well...you know what I mean!"
    "I raise my eyebrows and look to Morgan."
    "As Kleio seems to have said something she finds embarrassing."
    "Though I have no idea why."
    show morgan blush
    if morgan.male >= 66:
        morgan.say "I'm gonna cut to the chase, [hero.name]."
        morgan.say "You remember when we all got drunk and fucked?"
    elif morgan.male >= 33:
        morgan.say "The point is this, [hero.name]..."
        morgan.say "You remember the time we all...well, did it together?"
    else:
        morgan.say "There's no easy way to say it, [hero.name]."
        morgan.say "But you remember when we all...did things together?"
    mike.say "Of course I do!"
    mike.say "How could I forget a night like that?!?"
    show morgan happy
    show kleio happy -blush
    "Kleio and Morgan both look instantly pleased at my reaction."
    "But then they realise that they can see each other doing so."
    "And they instantly try to put their poker-faces back on."
    show morgan normal
    show kleio normal
    kleio.say "Yeah, well..."
    kleio.say "We kinda figured you'd be wanting some more."
    show kleio seductive
    kleio.say "Lusting after us like the salivating dog you are!"
    mike.say "Hey!"
    show kleio blush
    if morgan.male >= 66:
        morgan.say "Well?!?"
        morgan.say "Do you want another threesome or not?"
    elif morgan.male >= 33:
        morgan.say "Bit on the strong side there, Kleio!"
        morgan.say "But anyway - what do you say to the idea?"
    else:
        morgan.say "Eww, Kleio!"
        morgan.say "Ignore her, [hero.name]."
        morgan.say "But you want to do it with us again, right?"
    menu:
        "Accept" if hero.sexperience >= 20:
            "Like I even need to think about my answer to that one!"
            "I mean, sure they were pretty rude to me just now."
            "Walking up and assuming that I have nothing better to do."
            "But the truth is that there's nothing better than doing Kleio and Morgan!"
            mike.say "Do you think I'm fucking stupid?!?"
            mike.say "Of course I want to have another threesome with you!"
            mike.say "When can we make it happen?"
            "Kleio and Morgan exchange a knowing glance."
            "And they seem much happier with the way things are going now."
            show kleio happy
            show morgan happy
            kleio.say "Slow down, Loverboy!"
            kleio.say "We're still working on the finer details."
            if morgan.male >= 66:
                morgan.say "You just be ready to supply the cock when we are, okay?"
            elif morgan.male >= 33:
                morgan.say "Don't worry about a thing, [hero.name]."
                morgan.say "It'll be real soon, I promise!"
            else:
                morgan.say "Ooh, I hope it's real soon!"
                morgan.say "I can't wait either!"
            "It doesn't take us long to work things out."
            "And by the time we leave the pub, everyone's getting excited."
            "Now all I have to worry about is living up to their expectations..."
            $ morgan.love += 1
            $ kleio.love += 1
            call pixie_second_threesome from _call_pixie_second_threesome
            $ game.pass_time(2, True)
            $ DONE["pixie_second_threesome"] = game.days_played
        "Refuse":
            "Of course there's a part of me that wants to jump on the offer of a threesome."
            "And I'm sure you can guess which part of me that is, right?"
            "But I'm still pissed at Kleio and Morgan for interrupting my quiet drink."
            "And they're not exactly being subtle about things either."
            "So I feel like I need to put them in their place."
            "You know, remind them that I'm not just here for their amusement and pleasure."
            mike.say "You know what, I think I'll pass."
            mike.say "I'm just not in the right place at the moment."
            show morgan surprised
            show kleio surprised
            "Both Kleio and Morgan look like they've been slapped in the face."
            "Neither of them can believe I'd actually turn them down."
            kleio.say "You do realise we don't just want you to watch?"
            kleio.say "Right, Loverboy?"
            if morgan.male >= 66:
                morgan.say "Yeah, [hero.name]..."
                morgan.say "We bring the pussy and you bring the cock!"
            elif morgan.male >= 33:
                morgan.say "Wow..."
                morgan.say "I don't know how to take that!"
            else:
                morgan.say "What?!?"
                morgan.say "Well I think that's just mean!"
            show morgan sad
            "I shrug off their protests."
            mike.say "Sorry, ladies."
            mike.say "You'll have to find another ride at the theme-park."
            mike.say "This one's closed for maintenance!"
            show kleio sad
            kleio.say "If you ask me it should be condemned as rotten!"
            "With that, Kleio and Morgan turn round and storm out of the pub."
            hide morgan
            hide kleio
            with moveoutright
            "Which leaves me to finally finish my drink in peace."
            $ morgan.sub += 1
            $ kleio.sub += 1
            $ hero.cancel_event()
    return

label pixie_threesome:
    "As the time pass, I can see that Kleio has something in mind."
    show kleio blush at left5
    show morgan blush at right5
    kleio.say "Hey guys, what about... You know."
    morgan.say "Huh yeah! Last time was quite fun."
    kleio.say "What do you say Loverboy?"
    mike.say "Let's go!"
    if "pixie_second_threesome" in DONE:
        call pixie_second_threesome from _call_pixie_second_threesome_1
    else:
        scene bg bedroom1 with fade
        "Within a moment, we're in my bedroom."
        "Kleio and Morgan are already starting to pull and tug at each other's clothes."
        "Kleio and Morgan tumble onto the bed as they finish stripping each other off."
        show kleio naked blush at left5
        show morgan naked blush at right5
        "I watch them become a desperate tangle of limbs as they kiss with ever mounting passion."
        "The sight of their naked bodies intertwined is more than enough to keep me totally entranced."
        "It takes them both stopping and looking me straight in the eye to bring me back to reality."
        show kleio seductive
        kleio.say "Check out Loverboy here."
        kleio.say "He'd trip over his tongue if he could move an inch!"
        "Morgan giggles at Kleio's words, but beckons to me all the same."
        show morgan flirt
        morgan.say "What are you waiting for, [hero.name]?"
        morgan.say "You're not just gonna watch, are you?"
        "I have to physically shake myself to snap out of it."
        "But as soon as I feel like I'm in the room again, I start to strip off too."
        mike.say "Yeah...of course I am not."
        mike.say "Just got watching you guys and...well, I kind of zoned out there for a second!"
        "Kleio and Morgan watch me, still giggling as I struggle to get undressed and cross the room all at once."
        "As I climb onto the bed, they make room for me, crawling backwards towards the pillows."
        "They begin to kiss and caress each other once more, but now I'm close enough to reach out and touch them."
        "Both Kleio and Morgan have their thighs parted, as if offering me an open invitation."
        "Each one of them looks impossibly inviting, slick and ready for me."
        "And for a moment I have no idea how to choose between the two of them."
        "So in the end, I decide not to."
        hide kleio
        hide morgan
        show kleio morgan threesome out
        with fade
        "Laying myself down, I put my head between Kleio's thighs and my dick between Morgan's."
        "Needless to say that my cock's already rock-hard by this point."
        "But I still need to glance up to make sure it finds its way home."
        menu:
            "Fuck her pussy":
                show kleio morgan threesome vaginal morganclose
                "I get all the confirmation I need when I hear Morgan moan through her kissing Kleio."
                "The sound makes me all the more excited in turn, and I push in as far as I can go."
                "Even from this angle, Morgan's tight little pussy feels incredible."
                "But I can't let Morgan have all the fun and Kleio miss out, now can I?"
                "Parting the lips of Kleio's pussy, I begin to tease her with the tip of my tongue."
                "The unique taste of her floods my mouth, like licking the top of a battery."
                "Morgan's getting every inch of dick that I have to give right now."
                show kleio morgan threesome vaginal close
                "But I can be so much more creative with my tongue, as Kleio soon finds out."
                "As I probe ever deeper into the folds of her pussy, she starts to make noises of her own."
                "Unlike Morgan's moans from having my cock inside of her, Kleio yelps and cries out at what I'm doing to her."
                show kleio morgan threesome vaginal morganorgasm
                "And when I can steal a moment to look up, I see her cheeks flushing and her eyes rolling back into her head."
                "This only serves to make me redouble my efforts towards them both."
                show kleio morgan threesome vaginal orgasm
                "I watch as my cock thrusting in and out of Morgan and my tongue exploring Kleio's pussy push them ever closer to the edge."
                "By now it's all that they can do to keep on pressing their lips together."
                "Both Kleio and Morgan are writhing on the bed thanks to my attentions."
                "And it can't be long before one of them cums in the most spectacular manner possible."
                "But a moment later a twinge from down below makes me think I might beat them to it..."
                menu:
                    "Cum inside":
                        "I make no effort to pull out of Morgan, instead thrusting in and out of her until the very last moment."
                        show kleio morgan threesome vaginal cumshot
                        "As if in response to the sensation of me cumming inside of her, Morgan pulls Kleio in even closer."
                        "I watch as she practically shoves her tongue into the other girl's mouth without mercy."
                        "Kleio has no choice but to let Morgan have her way, returning the kiss as best she can."
                        "I keep on thrusting into her, using up the last of my energy as I do so."
                        "But I can't help thinking that Morgan seems to be using her tongue in the same way as I am my cock."
                        "The more I push into her pussy, the more she forced her tongue down Kleio's throat!"
                        "In the end, I can't tell if Kleio's gasping from an orgasm or the actual fear of being suffocated!"
                        "But as the whole thing settles down into an exhausted afterglow, there are no complaints or recriminations to be heard."
                        "Only the sound of three people panting and gasping as they lie in a pile of sweaty limbs."
                        "In fact, it's the quietest the three of us have been all night."
                    "Share the love" if hero.sexperience >= 15:
                        show kleio morgan threesome out
                        "I pull my cock out of Morgan and then my tongue out of Kleio without warning."
                        "As I'd hoped, the surprise of being denied my attentions makes the pair snap to attention."
                        hide kleio
                        show kleio naked blush at left5
                        show morgan naked blush at right5
                        with fade
                        kleio.say "Hey...what gives?!?"
                        morgan.say "Aww, no fair!"
                        "I ignore their protests as I get up from the bed and beckon them to follow."
                        "At first they look annoyed and puzzled by my actions, not getting the hint."
                        "But then I point at the floor before me with one hand."
                        "At the same time, the other is stroking the shaft of my cock, still slick from Morgan's pussy."
                        "Kleio seems to catch on first, snaking off of the bed and urging Morgan to follow."
                        "I see her eyes go wide and a smile spread across her face as realisation dawns."
                        hide kleio
                        hide morgan
                        show kleio morgan cumshot look
                        with fade
                        "And a moment later, both of them are kneeling down in front of me."
                        "Like a pair of begging bitches, Kleio and Morgan wait in silence, their mouths open."
                        show kleio morgan cumshot cum
                        "The first streamer of cum somehow manages to spread itself across both their faces."
                        show kleio morgan cumshot facecum mouthcum
                        "They laugh in surprise, ensuring that the second hits their tongues and lips."
                        show kleio morgan cumshot kiss
                        "Soon enough they're covered in cum, smiling and giggling as they lick themselves clean."
            "Fuck her ass":
                show kleio morgan threesome anal morganclose
                "I get all the confirmation I need when I hear Morgan moan through her kissing Kleio."
                "The sound makes me all the more excited in turn, and I push in as far as I can go."
                "Even from this angle, Morgan's tight little ass feels incredible."
                "But I can't let Morgan have all the fun and Kleio miss out, now can I?"
                "Parting the lips of Kleio's pussy, I begin to tease her with the tip of my tongue."
                "The unique taste of her floods my mouth, like licking the top of a battery."
                "Morgan's getting every inch of dick that I have to give right now."
                show kleio morgan threesome anal close
                "But I can be so much more creative with my tongue, as Kleio soon finds out."
                "As I probe ever deeper into the folds of her pussy, she starts to make noises of her own."
                "Unlike Morgan's moans from having my cock inside of her, Kleio yelps and cries out at what I'm doing to her."
                show kleio morgan threesome anal morganorgasm
                "And when I can steal a moment to look up, I see her cheeks flushing and her eyes rolling back into her head."
                "This only serves to make me redouble my efforts towards them both."
                show kleio morgan threesome anal orgasm
                "I watch as my cock thrusting in and out of Morgan and my tongue exploring Kleio's pussy push them ever closer to the edge."
                "By now it's all that they can do to keep on pressing their lips together."
                "Both Kleio and Morgan are writhing on the bed thanks to my attentions."
                "And it can't be long before one of them cums in the most spectacular manner possible."
                "But a moment later a twinge from down below makes me think I might beat them to it..."
                menu:
                    "Cum inside":
                        "I make no effort to pull out of Morgan, instead thrusting in and out of her until the very last moment."
                        show kleio morgan threesome anal cumshot
                        "As if in response to the sensation of me cumming inside of her, Morgan pulls Kleio in even closer."
                        "I watch as she practically shoves her tongue into the other girl's mouth without mercy."
                        "Kleio has no choice but to let Morgan have her way, returning the kiss as best she can."
                        "I keep on thrusting into her, using up the last of my energy as I do so."
                        "But I can't help thinking that Morgan seems to be using her tongue in the same way as I am my cock."
                        "The more I push into her ass, the more she forced her tongue down Kleio's throat!"
                        "In the end, I can't tell if Kleio's gasping from an orgasm or the actual fear of being suffocated!"
                        "But as the whole thing settles down into an exhausted afterglow, there are no complaints or recriminations to be heard."
                        "Only the sound of three people panting and gasping as they lie in a pile of sweaty limbs."
                        "In fact, it's the quietest the three of us have been all night."
                    "Share the love" if hero.sexperience >= 15:
                        show kleio morgan threesome out
                        "I pull my cock out of Morgan and then my tongue out of Kleio without warning."
                        "As I'd hoped, the surprise of being denied my attentions makes the pair snap to attention."
                        hide kleio
                        show kleio naked blush at left5
                        show morgan naked blush at right5
                        with fade
                        kleio.say "Hey...what gives?!?"
                        morgan.say "Aww, no fair!"
                        "I ignore their protests as I get up from the bed and beckon them to follow."
                        "At first they look annoyed and puzzled by my actions, not getting the hint."
                        "But then I point at the floor before me with one hand."
                        "At the same time, the other is stroking the shaft of my cock, still slick from Morgan's pussy."
                        "Kleio seems to catch on first, snaking off of the bed and urging Morgan to follow."
                        "I see her eyes go wide and a smile spread across her face as realisation dawns."
                        hide kleio
                        hide morgan
                        show kleio morgan cumshot look
                        with fade
                        "And a moment later, both of them are kneeling down in front of me."
                        "Like a pair of begging bitches, Kleio and Morgan wait in silence, their mouths open."
                        show kleio morgan cumshot cum
                        "The first streamer of cum somehow manages to spread itself across both their faces."
                        show kleio morgan cumshot facecum mouthcum
                        "They laugh in surprise, ensuring that the second hits their tongues and lips."
                        show kleio morgan cumshot kiss
                        "Soon enough they're covered in cum, smiling and giggling as they lick themselves clean."
                $ morgan.flags.anal += 1
        $ morgan.sexperience += 1
        $ morgan.love += 2
        $ kleio.love += 2
    $ game.room = "bedroom1"
    call sleep from _pixie_threesome
    return

label pixie_second_threesome:
    $ end_scene = False
    if game.week_day % 2 == 0:
        "Almost the same moment that we've agreed to the threesome, we're up and headed out of the pub."
        "All three of us know that my place is the closest, so there's no question as to where we're going."
        scene bg bedroom1 with fade
        "As soon as we're back at the house, I let us in, the usher Kleio and Morgan into my room."
        "I'm pretty confident that nobody saw us slipping in, so we can get straight down to business."
        "But as I close the door and turn around to face Kleio and Morgan, I'm greeted with a surprise."
        show kleio seductive topless at left5
        show morgan blush topless at right5
        with dissolve
        "The pair of them are already stripped down to their underwear and pulling that off too!"
        kleio.say "Hurry up, Loverboy!"
        if morgan.male >= 66:
            morgan.say "Yeah, you'd better not keep us waiting!"
        elif morgan.male >= 33:
            morgan.say "Come on, [hero.name]!"
            morgan.say "Let's have some fun!"
        else:
            morgan.say "Get a move on, slowcoach!"
        mike.say "Hey, you guys!"
        mike.say "No fair - you should have waited for me!"
        "Kleio and Morgan exchange a wicked smile and shake their heads."
        show kleio naked
        show morgan naked
        with dissolve
        "Almost at the same moment, they drop their bra's on the floor."
        "And then they pull down their panties, kicking them away too."
        "I'm already struggling to pull off my own clothes as fast as I can."
        "Which means that I only get to see glimpses of this as I do so."
        "I'm trying to cross the room at the same time, hopping and stumbling."
        "Which means that I almost fall flat on my face before I catch up to them."
        "Kleio and Morgan are now watching me fumble around, having a good laugh at my expense."
        "But the truth is that I hardly notice or hear a thing."
        "Because the sight of them together is all that's on my mind."
        show pixie handjob with fade
        "And above all because Kleio's now squeezing my cock, stroking the shaft."
        "Morgan's delicately pressing my balls in her sweet hand."
        "And I can see from the look on their faces that Kleio and Morgan are thinking the same thing!"
        kleio.say "So how are we gonna do this thing, guy?"
        kleio.say "I mean, how are we gonna get started?"
        if morgan.male >= 66:
            morgan.say "Yeah, do we fool around a little?"
            morgan.say "Or do we just start fucking?"
        elif morgan.male >= 33:
            morgan.say "I could stand a little foreplay!"
            morgan.say "Unless you guys are desperate for it?"
        else:
            morgan.say "I like to start things off slowly."
            morgan.say "But I'm cool with doing whatever!"
        "Hmm...what a choice to have to make!"
        "Part of me wants to pounce on Kleio and Morgan right now."
        "Then there's the thought of stretching things out a little..."
        "But I need to make a decision soon - they're waiting for me to speak up!"
        menu:
            "Give Morgan some attention":
                "I don't tell Kleio and Morgan what I'm going to do, I just do it."
                "Putting a hand on one of their shoulders, I push down gently."
                scene pixie morgan cunnilingus with fade
                "Kleio and Morgan go with the motion, sitting down on the edge of the bed."
                "But their eyes are on me the whole time, waiting to see what I have in mind."
                "I do the best I can to hold their gazes as I get down on my knees."
                "And they seem to quickly catch on, guessing what's coming next."
                "I say this because Kleio and Morgan both spread their legs."
                show pixie morgan cunnilingus mike
                "A moment later they lift them up, spreading their thighs."
                "This means that I have no problem reaching between them."
                "And it's there that I find their pussies waiting for me."
                "My left hand is on Kleio's lips, my right on Morgan's."
                "I hear them both gasp as I trace the folds with my fingers."
                "And I swear that they begin to get wet at the same moment too!"
                "I don't need to see what I'm doing to either of them."
                "All I have to do is let my hands wander in lazy circles."
                "Kleio and Morgan are leaning back on the bed by now."
                "Their elbows support them as their hands begin to wander too."
                "I watch as they stroke and caress their own bodies above the waist."
                "And inevitably they settle a hand on each of their breasts."
                "I can feel myself getting harder by the second as I watch them."
                "Kleio and Morgan squeeze their breasts, pinching their nipples."
                "It's like they're trying to release the pressure I'm building up inside of them."
                "But it's having the opposite effect on me right now!"
                "I feel like I'm going to burst any moment!"
                "Trying to concentrate on something else, I lower my head."
                "I don't know why I choose Morgan over Kleio."
                "But a second later my head is between her thighs."
                "Morgan moans become even louder as I put my mouth to work."
                "I kiss and lick like my life depends on it, probing deeper all the time."
                "And it doesn't take long for Morgan to begin wailing at my efforts."
                "Her entire body quivering as she cums at the touch of my tongue."
                $ morgan.love += 1
            "Ask for a blowjob":
                "I give Kleio and Morgan what I hope is a wry smile."
                mike.say "You guys seem to know what you want."
                mike.say "So why don't you show me what that is?"
                "Kleio and Morgan exchange a meaningful glance."
                "And then they both nod."
                kleio.say "You take the top and I'll take the bottom."
                kleio.say "Just like we agreed?"
                if morgan.male >= 66:
                    morgan.say "Sure thing, Kleio!"
                    morgan.say "Let's do it!"
                elif morgan.male >= 33:
                    morgan.say "Okay, Kleio - I remember the plan."
                    morgan.say "You start and I'll follow!"
                else:
                    morgan.say "Of course, Kleio!"
                    morgan.say "You can count on me!"
                "Before I have the chance to say a single word, they spring into action."
                "Kleio wraps her arms around my legs, pinning me to the spot."
                "And Morgan pretty much pounces on me, grabbing my shoulders."
                "Between them they make sure that I end up falling backwards."
                "Luckily for me, the bed is there to break my fall!"
                scene pixie blowjob with fade
                "The moment I hit the mattress, Kleio is between my legs."
                "At the same time, Morgan clambers over my chest."
                "Her breasts brush my face, and then I catch the scent of her pussy."
                "I strain my neck to be able to lick at it, my tongue brushing her lips."
                "I hear Morgan gasp and then giggle."
                "But then the pair of them get to work, and I'm left helpless."
                "I don't know who's doing what to me, because I can't see a thing."
                play sexsfx1 bj_sucking loop
                "But I know one of them is sucking on my balls."
                "And the other is already swallowing my cock deep into their mouth!"
                "All I can do is lie back, pinned under Morgan's weight."
                "Not that I have anywhere else I'd rather be right now!"
                "I'm happy to let them work me from both sides."
                "And I make sure to lick at Morgan's pussy every chance I get too!"
                "The only thing is that I can't keep this up forever."
                mike.say "Ah..."
                mike.say "Guys..."
                mike.say "You have to let up!"
                menu:
                    "They keep going!":
                        "I'm just about ready to blow, thinking about where it's going to happen."
                        "But that's the exact moment that Kleio and Morgan leap into action."
                        play sexsfx1 pop_out
                        scene pixie cumshare with fade
                        "Before I know what's happening, I'm out of the hole I was in with an audible pop."
                        "And then Kleio and Morgan are kneeling in front of me on the bed."
                        "They waste no time in going to work on me, making sure I don't lose it."
                        "Hands, tongues and lips are all called into play to tease my cock."
                        "It's like the pair of them are psychic, exchanging thoughts the whole time."
                        "Because they don't seem to need as much as a hint from each other to work so closely."
                        "And it doesn't take long for them to get what they want either."
                        "Kleio and Morgan pass my cock expertly between them until the very last moment."
                        "Then they lean in close as I finally feel myself losing it."
                        show pixie cumshare cum with hpunch
                        "When it comes, my orgasm is every bit as spectacular as I'd hoped."
                        with hpunch
                        "Kleio and Morgan's faces are instantly spattered with stripes of white."
                        with hpunch
                        "They squeal and laugh as it paints their cheeks and runs downwards."
                        "But all I can do is watch the whole thing, panting and spent."
                        $ kleio.sub += 1
                        $ morgan.sub += 1
                        $ end_scene = True
                    "They listen":
                        scene bg bedroom1 with fade
                        kleio.say "Ah..."
                        show kleio seductive naked at left5
                        show morgan blush naked at right5
                        with dissolve
                        kleio.say "I guess he's right, Morgan."
                        kleio.say "We don't want to wear him out - at least not yet!"
                        "Reluctantly they let me go on the promise of there being more to come."
                        $ kleio.sub += 1
                        $ morgan.sub += 1
            "Give Kleio some attention":

































                mike.say "Hey, Morgan..."
                mike.say "Come over here and help me out, yeah?"
                morgan.say "Okay, [hero.name]..."
                if morgan.male >= 66:
                    morgan.say "You just sit tight, Kleio!"
                elif morgan.male >= 33:
                    morgan.say "Wait a minute, Kleio!"
                else:
                    morgan.say "He, he...don't be jealous, Kleio!"
                "Kleio gives me a curious look as I ask Morgan to help me."
                "But then she looks positively paranoid when the other girl rushes to my side."
                kleio.say "Hey..."
                kleio.say "What are you guys trying to pull?"
                "For all of her apparent misgivings, Kleio doesn't resist."
                "Instead she lets Morgan and I guide her down onto the bed."
                scene pixie kleio cunnilingus
                "Once she's laid on her back, I gently spread her legs."
                "Morgan seems to catch on to what I'm doing pretty quickly."
                "She follows my lead as I lean in between Morgan's thighs."
                "And soon enough we're exploring what we find down there together."
                "I catch a glimpse of Kleio's expression as she looks down at us."
                "It's a mixture of trepidation and intense desire."
                "But a moment later I close my eyes and turn my attention to the task at hand."
                "Now all I have to go on is the sounds that Kleio's making."
                "That and the fact that her pussy is getting wetter by the second!"
                "Morgan's the perfect partner for this kind of work."
                "She seems to know her way around down there like nobody else!"
                "And she has no trouble weaving around me either."
                "Together we have Kleio worked into a helpless state."
                "All that she can do is lie there and take all that we give her."
                "And we keep right on delivering until the moment that I hear her squeal."
                "That and the sensation of her thighs pressing together lets me know that she's done."
                "Morgan and I lean back, gasping for breath as Kleio writhes on the bed."
                $ kleio.love += 1
            "Go on for the main course":
                pass
    else:
        scene bg bedroom1 with fade
        "I'm smiling and doing the best I can to keep on joking with them."
        "But part of me's still worried that Kleio and Morgan are going to pick up on it."
        "That they're going to realise just how nervous I am right now."
        "We're behind closed doors and in the privacy of my own bedroom."
        "And all of us are one hundred percent into doing what we're going to do."
        "But I still can't quite believe this is actually happening to me."
        "Which is what's responsible for my nerves."
        "At first it was crazy that I found out the two of them had dated in the past."
        "And then it felt totally insane that the three of us were all hooking up together."
        show kleio seductive topless at left5
        show morgan blush topless at right5
        with dissolve
        "Now I'm actually watching Kleio and Morgan getting undressed in my own room!"
        "They're giggling and exchanging playful pushes as they take off their clothes."
        "And little by little, their bodies are being revealed."
        "I don't honestly think I've ever seen two more beautiful girls."
        "I just can't take my eyes off of them."
        "Part me is sure that if I pinch myself, I'll wake up to find it's all a dream."
        "Just then I see Kleio stop what she's doing and look me in the eye."
        show kleio naked
        show morgan naked
        with dissolve
        show kleio seductive
        kleio.say "Hey, Loverboy..."
        kleio.say "What's the problem over there?"
        "Morgan's attention is instantly drawn to me as well."
        "And she cocks her head on one side as she studies me."
        show morgan blushhappy
        if morgan.male >= 66:
            morgan.say "Huh?"
            morgan.say "Yeah, [hero.name] - what's up?"
        elif morgan.male >= 33:
            morgan.say "Yeah, [hero.name]..."
            morgan.say "Are you feeling okay?"
        else:
            morgan.say "Oh..."
            morgan.say "Is everything okay, [hero.name]?"
        show morgan blush
        "With their attention on me, I realise that I've been standing still this whole time."
        "I'm still fully clothed, while the pair of them are now totally naked."
        mike.say "Oh..."
        mike.say "Sorry, you guys."
        mike.say "I...I think the nerves are getting to me!"
        show kleio normal
        "Kleio and Morgan exchange a puzzled look."
        "But then they both begin to laugh at me."
        show kleio seductive
        show morgan flirt
        kleio.say "You gotta be kidding me!"
        kleio.say "I thought this was every guy's fantasy?"
        show kleio normal
        show morgan happy
        if morgan.male >= 66:
            morgan.say "Getting to fuck two hot chicks!"
            morgan.say "Aren't you into that?"
        elif morgan.male >= 33:
            morgan.say "I thought you were up for this?"
            morgan.say "That you were totally into us?"
        else:
            morgan.say "You're not backing out on us?"
            morgan.say "Are you?"
        "I take a step forwards, waving my hands in the air."
        mike.say "No, no, no!"
        mike.say "It's just that..."
        mike.say "Well...you guys have done it before."
        mike.say "So I'm kind of still the new guy, you know?"
        "Kleio takes full advantage of the fact that I've come closer."
        "Without warning, she pounces on me, pulling me towards the bed."
        "Morgan lets out a mischievous giggle and joins in."
        "And together they pull me down onto the mattress."
        show kleio seductive
        kleio.say "It's not like that, Loverboy."
        show kleio normal
        show morgan talkative
        morgan.say "This is still new for us too."
        show morgan normal
        show kleio talkative
        kleio.say "For one thing..."
        show kleio wink
        kleio.say "We didn't have one of these to play with before!"
        show morgan normal
        "Kleio squeezes my cock through my pants as she says this."
        "I gasp at the sensation, feeling my heart start to beat faster."
        mike.say "B...but what about dildos?"
        mike.say "And...and stuff like that?"
        show kleio talkative
        kleio.say "Oh sure, they're great."
        kleio.say "But I still like the feel of a hard dick inside of me!"
        show morgan normal
        show morgan blushhappy
        morgan.say "Or in my mouth!"
        show morgan blush
        show kleio at center, traveling(1.8, 2, (320, 1120))
        "I nod eagerly as Kleio unzips my flies and reaches inside."
        show morgan zorder 9 at center, traveling(1.8, 2, (960, 1120))
        "At the same time, Morgan begins to strip off my clothes."
        "I don't know if one of them pulls me to my feet."
        "Or if I stand up of my own accord to help them out."
        show kleio c at center, traveling(2, 2, (420, 1220))
        "But either way, I'm up and watching them go to work."
        show morgan b at center, traveling(2.4, 2, (1260, 1420))
        "Morgan has me out of my clothes in record time."
        show kleio a at center, traveling(2, 2, (520, 1320))
        "And Kleio's making sure that I'm ready for them once she's done."
        show kleio at vslide(5, 1)
        "Though I have to say that I think Kleio's got the easier job."
        "Because I've been getting harder by the second for some time now."
        "So her simply touching it is enough to make me stand to attention."
        show kleio at center, traveling(2, 1.2, (520, 1680))
        "Kleio's already kneeling down in front of me by now."
        "But Morgan's still busy tossing aside the last of my clothes."
        "Then she seems to notice that nobody's waiting for her."
        "This makes her hurry to climb over my chest, starting to work on the tip of my cock."
        "Not that this seems to have any effect on Kleio."
        "Who just laughs and leans straight in all the same."
        show morgan at center, traveling(2.4, 1.2, (640, 2020))
        "Normally I'd be used to it being stroked and teased at first."
        show morgan a at center, traveling(2.4, 0.7, (640, 2070))
        pause 0.7
        play sexsfx1 bj_sucking loop
        with hpunch
        "But Morgan just opens her mouth and swallows it whole!"
        show morgan at vslide(45, 1)
        "A moment later, her head's going back and forth."
        "And I'm gasping at the sensations she's making me feel."
        "Kleio seems to be thrown for a moment, staring at Morgan in frustration."
        "But then her expression changes to one of resolve, and she leaps into action."
        show kleio at center, traveling(2.4, 1.2, (640, 2220))
        "Going lower, she instead focuses her attention on my balls."
        "And just like that, I have two parts of my anatomy in different mouths!"
        "Morgan keeps right on working my cock."
        "She licks, sucks and nibbles until I feel like I'm going to explode."
        "All the while Kleio's doing the same and more."
        "I can't help closing my eyes as the pleasure I'm feeling builds."
        scene
        show kleio morgan cumshot look
        with fade
        stop sexsfx1
        kleio.say "Uh-oh!"
        kleio.say "Looks like someone's about to blow!"
        if morgan.male >= 66:
            morgan.say "No worries - I'll handle it!"
        elif morgan.male >= 33:
            morgan.say "You want me to handle this, Kleio?"
        else:
            morgan.say "Ooh!"
            morgan.say "Can I have this one?"
        kleio.say "Nah, Morgan."
        kleio.say "We should let him choose..."
        "I watch as Kleio and Morgan both sit back on their haunches."
        "And then they wait patiently to see what I do next."
        menu:
            "Share the love":
                "It's a tough call to make."
                "But if I make it a facial, maybe I don't have to choose at all." with hpunch
                "While the two of them are kneeling in front of me, I let myself go."
                play sexsfx1 cum_outside
                show kleio morgan cumshot cum with hpunch
                "And as I shoot my load, I make sure to shower them both."
                "Kleio and Morgan close their eyes as it happens."
                show kleio morgan cumshot -cum facecum mouthcum with hpunch
                "But they're sure to keep their mouths open."
                "White stripes of cum paint their faces and begin to run downwards."
                show kleio morgan cumshot kiss
                "But they don't flinch once, instead enjoying the experience."
                "Once I'm done, I sit down on the bed."
                "Because if I don't, I know I'll fall onto the floor."
                "Kleio and Morgan crawl the short distance over to me."
                "And each of them wraps their arms around one of my legs."
                "But from the way they're looking up at me, I know one thing for sure."
                "The pair of them are far from satisfied."
                "In fact, they're probably going to demand a lot more from me before the night is over!"
                $ kleio.sub += 1
                $ morgan.sub += 1
                $ end_scene = True
            "Go on for the main course":
                pass
    if not end_scene:
        menu:
            "Fuck Morgan":
                "It's a pretty hard thing to choose between a pair like Kleio and Morgan."
                "In fact, it's all but impossible!"
                "So instead, I decide to flip the choice in the hope of making things easier."
                "And instead I try to think of who I'd like to fuck."
                "That and which one of them I'd want to have helping me out along the way!"
                mike.say "Hey, Kleio..."
                mike.say "How about you and me show Morgan here a good time?"
                "Kleio's smile is devilish as she nods her head."
                kleio.say "Why not, Loverboy!"
                kleio.say "But you follow my lead, yeah?"
                kleio.say "That way you might actually learn something!"
                "Morgan looks from me to Kleio and back again."
                if morgan.male >= 66:
                    morgan.say "Hey..."
                    morgan.say "Why are you ganging up on me?!?"
                elif morgan.male >= 33:
                    morgan.say "Wha...what gives?"
                    morgan.say "I thought we were all equals here?!?"
                else:
                    morgan.say "Oh no..."
                    morgan.say "What are you going to do to me?!?"
                "Morgan shakes her head as she crawls backwards onto the bed."
                scene pixie threesome morganfuck with fade
                "Kleio stalks her from the left and I take the right."
                "And a moment later we pounce on Morgan!"
                "Kleio catches her around the shoulders, pulling her down."
                "And I grab hold of Morgan's haunches, gripping her tight."
                "She wriggles and squirms, but my cock's already hard."
                "So I take a deep breath, and then I make my move..."
                menu:
                    "Fuck her pussy":
                        "There's no time to get fancy, so I decide to keep things simple."
                        "Or maybe I just catch the scent of Morgan's pussy and I can't help myself."
                        "Either way I feel the sensation of my cock rubbing against her lips."
                        "They're slick and already beginning to yield."
                        "A moment later I give the gentlest of pushes..."
                        show pixie threesome morganfuck -out vaginal
                        play sexsfx1 slide_in
                        "And then I feel Morgan's lips part, letting me inside."
                        if morgan.male >= 66:
                            morgan.say "Oh yeah..."
                            morgan.say "That's it..."
                            morgan.say "That's the shit!"
                        elif morgan.male >= 33:
                            morgan.say "Oh shit..."
                            morgan.say "That feels good..."
                            morgan.say "That feels SO good!"
                        else:
                            morgan.say "Oh my..."
                            morgan.say "That's it..."
                            morgan.say "That feels amazing!"
                        play sexsfx1 slide_in
                        "Morgan lays down on her side as I sink all the way into her."
                        play sexsfx1 slide_out
                        "I can feel the way that she's almost surrendering to me."
                        play sexsfx1 slide_in
                        pause 1
                        play sexsfx1 slide_out
                        "And the sensation makes me pick up the pace."
                        play sexsfx1 fuck_moderate loop
                        "Lifting her leg to get a better angle, I give it all I've got."
                        "At the same time Morgan starts reaching out in front of her."
                        "For a moment I'm confused as to just what she's doing."
                        "But then I look over her shoulder and see Kleio before her."
                        "I don't know what she was planning to do while I fucked Morgan."
                        "But right now she's watching as the other girl reaches between her legs!"
                        "Every time I thrust into Morgan, it pushes her closer to Kleio."
                        "And so within a few moments, she reaches her ultimate goal."
                        "Kleio falls back onto the pillows as Morgan begins to lick her pussy."
                        "And the more I see of her efforts, the more I put into fucking her."
                        "This in turn pushes Morgan's head deeper between Kleio's thighs."
                        show pixie threesome morganfuck vaginal drool
                        play sexsfx1 fuck_speed loop
                        "Hands on her breasts, Kleio surrenders to her fate."
                        "By now all three of us are hard at it, sweating and straining."
                        "I have no idea who's going to be the first to cum."
                        "All I know is that I have to keep going until the very end!"
                        kleio.say "Shit..."
                        kleio.say "Fuck her harder, Loverboy!"
                        kleio.say "I wanna cum - so you'd better make it happen!"
                        play sexsfx1 fuck_sprint loop
                        "Kleio's demands seem to have an instant effect on Morgan."
                        "I can feel the muscles of her pussy quivering around my cock."
                        "She's losing it, cumming with my cock buried inside of her!"
                        "The sensation is amazing, more than enough to push me over the edge."
                        "And I can see from the look on Kleio's face that she's going too!"
                        menu:
                            "Cum inside":
                                mike.say "Oh shit..."
                                mike.say "Here it comes!"
                                "I dig my fingers into Morgan's buttocks, holding her still."
                                with hpunch
                                "And then I push myself as deep into her as I can go."
                                with hpunch
                                play sexsfx1 final_thrust
                                "A moment later I shoot my load, filling her with all that I have."
                                with hpunch
                                "Morgan and Kleio moan as one, both in the throes of their orgasms."
                                show pixie threesome morganfuck out
                                "And then all there is to hear are the sounds of panting and gasping."
                                "As all three of us collapse onto the mattress."
                            "Pull out":
                                mike.say "Head's up..."
                                mike.say "Here it comes!"
                                "I use the last of my strength and the last second before I cum to make my move."
                                play sexsfx1 pull_out
                                show pixie threesome morganfuck out
                                "I pull my cock out of Morgan, making her gasp in surprise."
                                play sexsfx1 cum_outside
                                show pixie threesome morganfuck cum with hpunch
                                "And then I shoot my load over her, spattering her buttocks with cum."
                                with hpunch
                                "Morgan and Kleio moan as one, both in the throes of their orgasms."
                                show pixie threesome morganfuck -cum
                                "And then all there is to hear are the sounds of panting and gasping."
                                "As all three of us collapse onto the mattress."
                    "Fuck her ass":
                        "I have Morgan stretched out before me, helpless to resist."
                        "And that's why I can't help taking full advantage."
                        "I feel my cock slip between her buttocks."
                        "Then the tight grip of her ass takes hold of me."
                        "A moment later I give a firm push..."
                        play sexsfx1 slide_in
                        show pixie threesome morganfuck -out anal
                        "And then I feel my cock beginning to sink into Morgan's ass."
                        if morgan.male >= 66:
                            morgan.say "Oh yeah..."
                            morgan.say "That's it..."
                            morgan.say "That's the shit!"
                        elif morgan.male >= 33:
                            morgan.say "Oh shit..."
                            morgan.say "That feels good..."
                            morgan.say "That feels SO good!"
                        else:
                            morgan.say "Oh my..."
                            morgan.say "That's it..."
                            morgan.say "That feels amazing!"
                        play sexsfx1 slide_in
                        "Morgan lays down on her side as I sink all the way into her."
                        play sexsfx1 slide_out
                        "I can feel the way that she's almost surrendering to me."
                        play sexsfx1 slide_in
                        pause 1
                        play sexsfx1 slide_out
                        "And the sensation makes me pick up the pace."
                        play sexsfx1 fuck_calm loop
                        "Lifting her leg to get a better angle, I give it all I've got."
                        "At the same time Morgan starts reaching out in front of her."
                        "For a moment I'm confused as to just what she's doing."
                        "But then I look over her shoulder and see Kleio before her."
                        "I don't know what she was planning to do while I fucked Morgan."
                        "But right now she's watching as the other girl reaches between her legs!"
                        "Every time I thrust into Morgan, it pushes her closer to Kleio."
                        "And so within a few moments, she reaches her ultimate goal."
                        "Kleio falls back onto the pillows as Morgan begins to lick her pussy."
                        "And the more I see of her efforts, the more I put into fucking her."
                        "This in turn pushes Morgan's head deeper between Kleio's thighs."
                        show pixie threesome morganfuck anal drool
                        play sexsfx1 fuck_moderate loop
                        "Hands on her breasts, Kleio surrenders to her fate."
                        "By now all three of us are hard at it, sweating and straining."
                        "I have no idea who's going to be the first to cum."
                        "All I know is that I have to keep going until the very end!"
                        kleio.say "Shit..."
                        kleio.say "Fuck her harder, Loverboy!"
                        kleio.say "I wanna cum - so you'd better make it happen!"
                        play sexsfx1 fuck_speed loop
                        "Kleio's demands seem to have an instant effect on Morgan."
                        "I can feel the muscles of her ass quivering around my cock."
                        "She's losing it, cumming with my cock buried inside of her!"
                        "The sensation is amazing, more than enough to push me over the edge."
                        "And I can see from the look on Kleio's face that she's going too!"
                        menu:
                            "Cum inside":
                                mike.say "Oh shit..."
                                mike.say "Here it comes!"
                                "I dig my fingers into Morgan's buttocks, holding her still."
                                with hpunch
                                play sexsfx1 final_thrust
                                "And then I push myself as deep into her as I can go."
                                with hpunch
                                "A moment later I shoot my load, filling her with all that I have."
                                "Morgan and Kleio moan as one, both in the throes of their orgasms."
                                show pixie threesome morganfuck out
                                "And then all there is to hear are the sounds of panting and gasping."
                                "As all three of us collapse onto the mattress."
                            "Pull out":
                                mike.say "Head's up..."
                                mike.say "Here it comes!"
                                "I use the last of my strength and the last second before I cum to make my move."
                                play sexsfx1 pop_out
                                show pixie threesome morganfuck out
                                "I pull my cock out of Morgan, making her gasp in surprise."
                                show pixie threesome morganfuck cum with hpunch
                                "And then I shoot my load over her, spattering her buttocks with cum."
                                with hpunch
                                "Morgan and Kleio moan as one, both in the throes of their orgasms."
                                show pixie threesome morganfuck -cum
                                "And then all there is to hear are the sounds of panting and gasping."
                                "As all three of us collapse onto the mattress."
                        $ morgan.flags.anal += 1
            "Fuck Kleio":
                "It's a pretty hard thing to choose between a pair like Kleio and Morgan."
                "In fact, it's all but impossible!"
                "So instead, I decide to flip the choice in the hope of making things easier."
                "And instead I try to think of who I'd like to fuck."
                "That and which one of them I'd want to have helping me out along the way!"
                mike.say "Hey, Morgan..."
                mike.say "How about you and me show Kleio here a good time?"
                "Morgan let's out a genuine laugh and nods her head."
                "I can see that she's eager to play along."
                if morgan.male >= 66:
                    morgan.say "Sure thing, [hero.name]."
                    morgan.say "Let's play real hard too!"
                elif morgan.male >= 33:
                    morgan.say "Like you need to ask!"
                    morgan.say "This is going to be a blast!"
                else:
                    morgan.say "If you say so, [hero.name]."
                    morgan.say "Just point me in the right direction!"
                "Kleio, on the other hand, looks a little worried."
                "I don't think she was ready for us to band together like that!"
                kleio.say "Hey!"
                kleio.say "What the hell is this?"
                kleio.say "We're supposed to be having a threesome here!"
                kleio.say "You two can't tag-team me!"
                "I give Kleio a knowing smile as I start to advance on her."
                "And I nod to Morgan to do the same."
                "Kleio backs away from us, scampering onto the bed."
                "My idea was to pounce on her."
                "But Morgan beats me to it!"
                "Out of nowhere she springs onto Kleio, pinning her down!"
                scene pixie threesome kleiofuck
                show pixie threesome kleiofuck out
                with fade
                if morgan.male >= 66:
                    morgan.say "Gotcha!"
                elif morgan.male >= 33:
                    morgan.say "Too slow, Kleio!"
                else:
                    morgan.say "Quick, [hero.name] - I got her!"
                "Morgan's already straddling Kleio's waist, making the other girl squirm under her weight."
                "I hurry to get myself into the mix, leaping onto Kleio lower down."
                kleio.say "You're a couple of assholes, you know that?!?"
                kleio.say "And you'd better make all of this worth it!"
                "It's not like Kleio's going to have to beg for that to happen."
                "My cock's already good and hard, my heart pounding in my chest."
                "And all I can think about is pounding her!"
                menu:
                    "Fuck her pussy":
                        "Morgan's sitting further up than me, straddling Kleio's waist."
                        "And this means that I'm the one in charge below that point."
                        "I don't waste any time in spreading Kleio's legs nice and wide."
                        "Then I can choose where I go from there."
                        if morgan.male >= 66:
                            morgan.say "What are you waiting for, a written invitation?"
                        elif morgan.male >= 33:
                            morgan.say "Hurry up, [hero.name]!"
                        else:
                            morgan.say "Ooh...where are you going to put it?"
                        "I can already feel the lips of Kleio's pussy against my cock."
                        "They're soft, slick and inviting, as well as totally at my mercy."
                        "And I can't resist the urge to take advantage of that fact!"
                        "All it takes is a little pressure on my part."
                        show pixie threesome kleiofuck -out
                        play sexsfx1 slide_in
                        "Even that proves to be enough to make Kleio moan."
                        "The sound turns me on almost as much as the feel of her."
                        kleio.say "Oh god..."
                        kleio.say "Yeah, Loverboy..."
                        kleio.say "You really are gonna give me what I want!"
                        "Morgan leans down over Kleio a moment later."
                        "And she places her lips over the other girl's mouth."
                        "Now all I can hear is the sound of Kleio sighing as they kiss."
                        "The sight is amazing, and for a moment I almost forget what I'm doing."
                        play sexsfx1 slide_in
                        "Then I jump as I remember that I'm as deep as I can go inside of Kleio!"
                        play sexsfx1 slide_out
                        "I jerk back into action a second later, shaking my head in disbelief."
                        play sexsfx1 slide_in
                        pause 1
                        play sexsfx1 slide_out
                        "I begin to move in and out of Kleio."
                        play sexsfx1 slide_in
                        pause 1
                        play sexsfx1 slide_out
                        "And the effect is clear to see."
                        play sexsfx1 fuck_calm loop
                        "Kleio's head is pressed into the pillows, turning from side to side."
                        "Everything she's feeling is written all over her face too."
                        "Morgan breaks off the kiss, unable to keep up."
                        "And instead she begins to caress Kleio's naked chest."
                        "Of course this only serves to make what she's feeling that much more intense."
                        play sexsfx1 fuck_moderate loop
                        "Soon enough, Kleio is helpless, pinned under Morgan and I."
                        "But it's not the weight of our bodies that's keeping her there."
                        "It's the intensity of what we're doing to her that does it!"
                        "Every second I'm fucking her harder then ever before."
                        "And at the same time, Morgan is playing with her too."
                        play sexsfx1 fuck_speed loop
                        "I can already feel Kleio starting to twitch and buck under me."
                        "Her muscles are squeezing my cock harder all the time."
                        "I don't need to be told that she's about to lose it."
                        "But that doesn't stop Morgan sharing her own insights with me!"
                        if morgan.male >= 66:
                            morgan.say "Hold on, [hero.name]!"
                            morgan.say "This bitch is gonna blow!"
                        elif morgan.male >= 33:
                            morgan.say "Oh shit..."
                            morgan.say "I think she's going to cum!"
                        else:
                            morgan.say "Oh dear..."
                            morgan.say "I think she's going to have an orgasm!"
                        menu:
                            "Cum inside":
                                "There's no time for me to do anything but keep right on going."
                                "So that's exactly what I do, pounding away at Kleio until the last."
                                with hpunch
                                play sexsfx1 final_thrust
                                "I gasp as I shoot my load into her, holding nothing back."
                                with hpunch
                                "And I can feel her take every bit of it, losing her shit too."
                                "Afterwards I fall backwards onto the bed, panting and exhausted."
                                "Morgan looks over her shoulder at me, grinning wickedly."
                                "And then she looks at Kleio too, enjoying the sight of us being totally spent."
                            "Pull out":
                                play sexsfx1 pop_out
                                show pixie threesome kleiofuck out
                                with dissolve
                                "I only just manage to pull out of Kleio before it's too late."
                                "Morgan keeps her pinned to the bed as I fall backwards."
                                with hpunch
                                "A moment later I shoot my load, most of it hitting her in the back."
                                show pixie threesome kleiofuck out cum with hpunch
                                "Morgan looks over her shoulder at me, grinning wickedly."
                                "And then she looks at Kleio too, enjoying the sight of us being totally spent."
                                "But all I can do is lie there, panting and exhausted."
                    "Fuck her ass":
                        "Morgan's sitting further up than me, straddling Kleio's waist."
                        "And this means that I'm the one in charge below that point."
                        "I don't waste any time in spreading Kleio's legs nice and wide."
                        "Then I can choose where I go from there."
                        if morgan.male >= 66:
                            morgan.say "What are you waiting for, a written invitation?"
                        elif morgan.male >= 33:
                            morgan.say "Hurry up, [hero.name]!"
                        else:
                            morgan.say "Ooh...where are you going to put it?"
                        "Kleio's buttocks are already parting before my cock."
                        "And it's just then that I look down to see her tight little ass."
                        "That's it, deal done - I can't resist it!"
                        "I spread her cheeks just that little bit wider."
                        "Then I push the head of my cock straight in there."
                        show pixie threesome kleiofuck -out
                        play sexsfx1 slide_in
                        kleio.say "Oh god..."
                        kleio.say "Yeah, Loverboy..."
                        kleio.say "You really are gonna give me what I want!"
                        "Morgan leans down over Kleio a moment later."
                        "And she places her lips over the other girl's mouth."
                        "Now all I can hear is the sound of Kleio sighing as they kiss."
                        "The sight is amazing, and for a moment I almost forget what I'm doing."
                        play sexsfx1 slide_in
                        "Then I jump as I remember that I'm as deep as I can go inside of Kleio!"
                        play sexsfx1 slide_out
                        "I jerk back into action a second later, shaking my head in disbelief."
                        play sexsfx1 slide_in
                        pause 1
                        play sexsfx1 slide_out
                        "I begin to move in and out of Kleio."
                        play sexsfx1 slide_in
                        pause 1
                        play sexsfx1 slide_out
                        "And the effect is clear to see."
                        play sexsfx1 fuck_calm loop
                        "Kleio's head is pressed into the pillows, turning from side to side."
                        "Everything she's feeling is written all over her face too."
                        "Morgan breaks off the kiss, unable to keep up."
                        "And instead she begins to caress Kleio's naked chest."
                        "Of course this only serves to make what she's feeling that much more intense."
                        play sexsfx1 fuck_moderate loop
                        "Soon enough, Kleio is helpless, pinned under Morgan and I."
                        "But it's not the weight of our bodies that's keeping her there."
                        "It's the intensity of what we're doing to her that does it!"
                        "Every second I'm fucking her harder then ever before."
                        "And at the same time, Morgan is playing with her too."
                        play sexsfx1 fuck_speed loop
                        "I can already feel Kleio starting to twitch and buck under me."
                        "Her muscles are squeezing my cock harder all the time."
                        "I don't need to be told that she's about to lose it."
                        "But that doesn't stop Morgan sharing her own insights with me!"
                        if morgan.male >= 66:
                            morgan.say "Hold on, [hero.name]!"
                            morgan.say "This bitch is gonna blow!"
                        elif morgan.male >= 33:
                            morgan.say "Oh shit..."
                            morgan.say "I think she's going to cum!"
                        else:
                            morgan.say "Oh dear..."
                            morgan.say "I think she's going to have an orgasm!"
                        menu:
                            "Cum inside":
                                "There's no time for me to do anything but keep right on going."
                                "So that's exactly what I do, pounding away at Kleio until the last."
                                with hpunch
                                play sexsfx1 final_thrust
                                "I gasp as I shoot my load into her, holding nothing back."
                                with hpunch
                                "And I can feel her take every bit of it, losing her shit too."
                                "Afterwards I fall backwards onto the bed, panting and exhausted."
                                "Morgan looks over her shoulder at me, grinning wickedly."
                                "And then she looks at Kleio too, enjoying the sight of us being totally spent."
                            "Pull out":
                                play sexsfx1 pop_out
                                show pixie threesome kleiofuck out
                                with dissolve
                                "I only just manage to pull out of Kleio before it's too late."
                                "Morgan keeps her pinned to the bed as I fall backwards."
                                with hpunch
                                "A moment later I shoot my load, most of it hitting her in the back."
                                show pixie threesome kleiofuck out cum with hpunch
                                "Morgan looks over her shoulder at me, grinning wickedly."
                                "And then she looks at Kleio too, enjoying the sight of us being totally spent."
                                "But all I can do is lie there, panting and exhausted."
                        $ kleio.flags.anal += 1
    scene bg bedroom1
    show kleio topless at left5
    show morgan topless at right5
    with dissolve
    "Afterwards we clean ourselves off and begin to get dressed again."
    "Nobody seems to feel the need to speak, but we keep exchanging meaningful glances."
    "It's almost like the three of us gave gotten to a place where we don't need to use words."
    "All we need is the raising of an eyebrow or the curling of a lip in a smile."
    "And yeah, I know that I'm sounding like some kind of tedious hippy right now."
    "And I also know what Kleio and Morgan's reaction would be if they heard me talking like that."
    "But it's the truth - I've never felt a connection like this before now!"
    $ kleio.love += 4
    $ kleio.sexperience += 1
    $ morgan.love += 4
    $ morgan.sexperience += 1
    return

label kleio_morgan_propose_male:
    "I always knew that doing something like this would be a potential minefield, what with the personalities involved."
    "I mean, even if you were to take Kleio and Morgan alone, they're pretty complicated, headstrong girls in their own right."
    "But taken together, they can be almost like a force of nature when they get going, really hard to handle!"
    "And there's a part of me that could easily be put off doing what I have in mind, believe me."
    "Which is why I try not to overthink the whole thing, and take the very first opportunity that presents itself."
    "Kleio and Morgan are walking a little ahead of me when I finally choose my moment."
    "And so they don't see me as I go down on one knee and pull out the pair of rings I bought for the occasion."
    "This means that they walk on a couple of steps before Morgan just happens to glance back over her shoulder."
    show morgan at left5 with dissolve
    morgan.say "[hero.name]...[hero.name], you have to hear this!"
    show morgan surprised
    morgan.say "Oh, what are you..."
    "Kleio seems to notice the surprise in her voice."
    "And she turns to see what's the matter."
    show kleio annoyed at right5 with dissolve
    kleio.say "Don't tell me - Loverboy stepped in a turd again?"
    show morgan blush
    morgan.say "Ah, no...not exactly!"
    show kleio normal
    "Kleio follows Morgan's line of sight until she's looking straight at me too."
    show kleio surprised
    "And then I see her eyes go wide with surprise too, a sly smile twisting her lips."
    kleio.say "Well, well, well - what do we have here?"
    "I honestly never saw it going this way."
    "I knew it was going to be a challenge."
    "But this already feels like I've been thrown to the wolves!"
    mike.say "K...Kleio...Morgan..."
    mike.say "I wanted to ask...if you'd marry me?"
    show kleio seductive
    show morgan normal
    "I look from the snarky expression on Kleio's face to the shocked one on Morgan's and back again."
    "Only now do I realise that I've been unconsciously holding my breath since I asked the question."
    "And every second of silence that follows only serves to make the agony that much worse."
    if morgan.love < 195 or kleio.love < 195:
        kleio.say "Jesus, Loverboy."
        show kleio annoyed
        kleio.say "Why'd you have to go and ruin it, huh?"
        show morgan annoyed
        if morgan.male >= 66:
            morgan.say "Yeah, I'm not into it either, [hero.name]."
            morgan.say "This was fun."
            morgan.say "But you just made it SO serious and heavy!"
        elif morgan.male >= 33:
            morgan.say "That's harsh, Kleio!"
            morgan.say "But yeah, [hero.name] - I'm just not there yet either."
        else:
            morgan.say "Oh, [hero.name], how could you?!?"
            morgan.say "We were having SO much fun too!"

        "I shake my head slowly, already shoving the rings back into my pocket."
        mike.say "I...I'm sorry."
        mike.say "I didn't mean to upset you guys..."
        mike.say "I just thought that it was the right thing to do, that's all."
        "Kleio crosses her arms over her chest and shakes her head at this."
        "She lets out a snort of derision as I get back to my feet."
        kleio.say "Yeah, well, that's not how it turned out, Loverboy."
        show kleio normal
        kleio.say "How about you leave the thinking to us from now on?"
        show morgan normal
        "All I can do is nod, trying the whole time not to let my true emotions show."
        "The smile that I force onto my face seems to be enough to satisfy Morgan that it's all over."
        "But I think I can see concern in Morgan's eyes."
        "Though all the same, she keeps what she's thinking to herself."
        $ morgan.love -= 25
        $ morgan.sub -= 25
        $ kleio.love -= 25
        $ kleio.sub -= 25
    else:
        kleio.say "Jesus, Loverboy."
        kleio.say "We thought you'd never have the balls to ask!"
        show morgan blush
        if morgan.male >= 66:
            morgan.say "Yeah, we were taking odds on it."
            morgan.say "Betting which one of us would have to do it for you!"
        elif morgan.male >= 33:
            morgan.say "Yeah, but we're both glad that you did."
            morgan.say "Even if it did take you a little time to find he courage!"
        else:
            morgan.say "Oh wow - this is SO exciting!"
            morgan.say "We're gonna get married - all three of us together!"
        "I shake my head, not quite able to make sense of what I just heard."
        "Maybe it's the crazy place that my head's at right now."
        "Or maybe the babble of verbiage that just hit me was too much to process."
        mike.say "Ah...yeah..."
        mike.say "Sorry, but was that a yes or a no?"
        "Kleio and Morgan look at each other in astonishment, shaking their heads as they do so."
        "And then I find myself hauled back to my feet as they each grab one of my arms."
        kleio.say "How's about you leave the important decisions to us form now on, Loverboy?"
        show kleio happy
        kleio.say "We wouldn't want you to think too hard and end up hurting yourself!"
        morgan.say "It's a yes, [hero.name]."
        show morgan happy
        morgan.say "Kleio and I would love to marry you!"
        mike.say "Th...that's great!"
        mike.say "Here...let me just..."
        "I begin to fumble with the rings, trying to slip one onto each outstretched finger."
        "But all I end up doing is missing the target in both cases."
        "Without as much as a word, Kleio and Morgan take my hands."
        "And together they guide my efforts until there's a ring on each of their fingers."
        "That done, the girls begin to admire and compare their new pieces of jewellery."
        "Something which they do in complete and utter silence."
        "Letting me know just how much this moment means to them."
        $ morgan.set_fiance()
        $ kleio.set_fiance()
    hide kleio
    hide morgan
    return

label kleio_morgan_male_ending:

    if renpy.has_label("pixie_harem_achievement_3") and not game.flags.cheat:
        call pixie_harem_achievement_3 from _call_pixie_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "Before now, the only real thoughts that I ever had about marriage were around whether it was for me or not."
    "All the business of venues, dresses, guest lists and the potential minefield they can become - forget it!"
    "I was always more concerned with the notion of getting together with suitably hot girls."
    "Actually wanting to marry one of them was the furthest thing from my mind - let alone marrying TWO of them!"
    "And I could never have predicted that the girls I'd be marrying would be a pair like Kleio and Morgan, that's for sure."
    "On the one hand, you have Kleio - spikey, spunky and outspoken."
    "But she's also sexy as hell, and fiercely loyal too."
    "And on the other, there's Morgan and the long, complicated history we have together."
    "Though for all that, I feel as though I've only just started to actually get to know her."
    "Throw me in on top of all that (pardon the mental image), and it sounds like a recipe for disaster."
    "But somehow it just seems to work."
    "It's almost as though we all add something to the whole that the other two are lacking a little of..."
    "And with a situation like that, we were never going to tie the knot in a church."
    "That's why were all standing in a clearing, surrounded by mature trees."
    "It was Morgan's idea, that we get married in the middle of the woods."
    "Most of the small guest list that we invited seem to think that it's a neutral setting."
    "But the three of us know full well this is one of the places Morgan and I used to hang out as kids."
    "Today it looks different though, more impressive and grand."
    "There are chairs, an altar and a priest to perform the ceremony."
    "And most importantly, there's the three of us standing together at the head of the congregation."
    "We chose to stand together, with no one walking down the aisle."
    "Just a small statement to let everyone know that we're all equal in this relationship."
    "And as if that wasn't enough, we aren't dressed conventional either."
    show morgan a wedding at left5
    show kleio a wedding at right5
    with dissolve
    "Sure, I might be wearing a suit, but Kleio and Morgan dispensed with the white dresses entirely."
    "I mean, Kleio is dressed in white."
    "But a cropped top and hotpants over fishnets isn't what you'd expect a bride to wear!"
    if morgan.male >= 66:
        "And the fact that Morgan's dressed in the exact same outfit just reinforces the impression too."
    elif morgan.male >= 33:
        "And Morgan might be wearing a dress."
        "But it's cut short to show off her figure and definitely isn't white either."
    else:
        "And Morgan might be wearing a dress."
        "But it's pink, and a crazy caricature of the dress a cartoon princess might have chosen."
    if morgan.is_visibly_pregnant and kleio.is_visibly_pregnant:
        "I wonder if the guests are more surprised by Kleio and Morgan's clothes or their swollen bellies."
        "After all, there's no way that their outfits could hope to hide it."
        "But whatever they think, the three of us are eager to meet the babies."
    elif kleio.is_visibly_pregnant:
        "I wonder if the guests are more surprised by Kleio's clothes or her swollen belly."
        "After all, there's no way that her outfit could hope to hide it."
        "But whatever they think, the three of us are eager to meet the baby."
    elif morgan.is_visibly_pregnant:
        "I wonder if the guests are more surprised by Morgan's clothes or her swollen belly."
        "After all, there's no way that her outfit could hope to hide it."
        "But whatever they think, the three of us are eager to meet the baby."
    else:
        "In the end, I don't care what the guests that we invited here today think."
        "I love the choices that they made for the statement that it makes about them."
        "They remind me with each and every glance why I love the pair."
    show kleio a seductive
    show fx question at right5
    kleio.say "Like what you see, Loverboy?"
    "Kleio hisses the words at me, but not with any kind of venom or irritation."
    "Morgan hears her too, and looks first to Kleio and then to me."
    morgan.say "Don't worry, [hero.name]."
    morgan.say "You'll get to look as well as touch real soon!"
    "Priest" "Ahem..."
    "At the sound of the priest clearing his throat with authority, all eyes snap forwards as one."
    "Priest" "Please be seated."
    "Without turning around, can hear the sound of asses hitting chairs."
    "Satisfied that his orders are have been followed, the priest nods in approval."
    "Priest" "Dearly beloved."
    "Priest" "We are gathered here today to witness the joining of these three souls in matrimony."
    "The rest of the ceremony is just the usual stuff that everyone knows off by heart."
    "Sounds weird, I know, but not all that much changes when you add a third person in there!"
    "And before long, we arrive at the exchanging of vows..."
    "Priest" "Do you, Kleio, take Morgan and [hero.name] to be your lawful, wedded partners?"
    "Priest" "Will you honour and obey them, comfort and support them?"
    "Priest" "And, forsaking all others, be faithful to them as long as you all shall live?"
    show kleio a wedding annoyed at right5
    kleio.say "Sure, what the hell - in for a penny, in for a pound!"
    with vpunch
    mike.say "KLEIO!"
    show morgan a surprised at left5, vshake
    show fx exclamation at left5
    morgan.say "KLEIO!"
    show kleio a happy
    kleio.say "Okay, okay...I will!"
    show morgan normal
    "Priest" "Do you, Morgan, take Kleio and [hero.name] to be your lawful, wedded partners?"
    "Priest" "Will you honour and obey them, comfort and support them?"
    "Priest" "And, forsaking all others, be faithful to them as long as you all shall live?"
    "Morgan fixes Kleio with an admonishing gaze as she speaks her own vows."
    show morgan a happy
    morgan.say "I will!"
    "Priest" "And do you, [hero.name], take Kleio and Morgan to be your lawful, wedded partners?"
    "Priest" "Will you honour and obey them, comfort and support them?"
    "Priest" "And, forsaking all others, be faithful to them as long as you all shall live?"
    mike.say "I will."
    "Priest" "Very well."
    "Priest" "It is therefore my pleasure to pronounce you married in the eyes of the law."
    "Priest" "You may kiss as a symbol of your union."
    "I know that we're supposed to come together and kiss right now."
    "Not in a hot and heavy way, but so it looks beautiful and chaste in the pictures afterwards."
    "But for a moment, neither one of us seems to be able to actually move a muscle."
    "We just end up standing there, staring at each other as if we're all stunned."
    "I don't think Kleio, Morgan or I can actually believe it's all for real."
    "We're officially married, the three of us!"
    "In the end, Morgan shakes off the funk first."
    "I feel her hand on the small of my back as she does the same to Kleio too."
    show morgan wedding a at center, zoomAt(2, (440, 1380))
    show kleio wedding a at center, zoomAt(2, (840, 1380))
    with hpunch
    "And then we're pulled together into a three-way embrace."
    morgan.say "We did it, guys."
    morgan.say "We're married!"
    kleio.say "Yeah, you two really lucked out landing a babe like me!"
    mike.say "No, Kleio - I'm the one that got lucky!"
    "With that, I pull them even closer to me, kissing their foreheads and then their lips."
    "We can't all kiss each other at once, so we pass them between us."
    "And somehow that seems to work just as well, showing that we're all joined together as one."
    "I think the guests are standing up and cheering for us, but I can't be sure."
    "As all I can see and hear are the two girls standing up here with me."
    "And that's because they're my entire world."
    hide morgan
    hide kleio
    scene pixie ending
    with fade
    kleio.say "Wow - where do I even start!"
    if morgan.male >= 66:
        morgan.say "You mean where do I start, Kleio!"
    elif morgan.male >= 33:
        morgan.say "You mean where do WE start, Kleio!"
    else:
        morgan.say "Ooh, you better tell them all about it, Kleio."
        morgan.say "Because I might forget about something important!"
        morgan.say "Hee, hee!"
    kleio.say "Er, yeah, okay..."
    kleio.say "Whatever, Morgan."
    kleio.say "Geez..."
    morgan.say "Or maybe [hero.name] should be telling the story too?"
    kleio.say "Oh no, there's no way I'm letting that happen!"
    kleio.say "Loverboy's been centre stage for way too long."
    kleio.say "It's time these people got to hear me thrash out a solo!"
    if morgan.male >= 66:
        morgan.say "I'm standing right here, Kleio!"
    elif morgan.male >= 33:
        morgan.say "You've got a real ego problem, you know?"
    else:
        morgan.say "Oh, Kleio - you're SO bad, SUCH a rebel!"
    kleio.say "Yeah, I know, I know..."
    kleio.say "To start with, it was just you and me, Morgan."
    kleio.say "And I was cool with that."
    kleio.say "I was even fine with us calling it quits too."
    kleio.say "I mean, it was my idea..."
    if morgan.male >= 66:
        morgan.say "It was okay, I guess - while it lasted!"
        morgan.say "But that's not how I remember it ending..."
    elif morgan.male >= 33:
        morgan.say "Because that's all that matters, right?!?"
        morgan.say "And for the record - it was a mutual decision to quit seeing each other!"
    else:
        morgan.say "Yeah, we had some fun, didn't we?"
        morgan.say "Shame it had to come to an end."
    kleio.say "None of that's really what's important though."
    kleio.say "Because it'd all have been water under the bridge."
    kleio.say "That is if not for good old Loverboy himself!"
    if morgan.male >= 66:
        morgan.say "Ironic, huh?"
        morgan.say "I was dating a girl, then a guy."
        morgan.say "But the guy got me back in with the girl!"
    elif morgan.male >= 33:
        morgan.say "Maybe I just wasn't ready to be with you then, Kleio."
        morgan.say "But [hero.name] really helped me to find out who I actually was."
        morgan.say "Ironic that finding him brought me right back to you, huh?"
    else:
        morgan.say "Mmm...[hero.name]'s SO manly."
        morgan.say "It's so great that we can both share him, Kleio!"
    kleio.say "Yeah, Morgan, you could say that."
    kleio.say "Ah, what the hell - I'll come right out and admit it."
    kleio.say "He's such a typical, dumb guy sometimes."
    kleio.say "But I wouldn't want to be without him."
    morgan.say "Ahem!"
    kleio.say "Oh, yeah...right."
    kleio.say "And you too, Morgan, you too!"
    morgan.say "[hero.name]'s like the thing that connects us all together."
    morgan.say "The thing that binds us, you know?"
    kleio.say "You mean he's like glue or something?"
    kleio.say "He's sticky and leaves a stain?"
    morgan.say "No, Kleio - you know what I mean!"
    kleio.say "Well, he does smell pretty strong sometimes."
    kleio.say "But I've been sniffing him for a while now and, well..."
    kleio.say "I have to admit, he's kind of addictive too!"
    if (morgan.is_visibly_pregnant or morgan.flags.mikeBabies >= 1) and (kleio.is_visibly_pregnant or kleio.flags.mikeBabies >= 1):
        kleio.say "You're being soft on him now, Morgan."
        kleio.say "But I bet he wasn't when you let him knock you up!"
        morgan.say "Hey, no fair - whatever happened to sisterhood?!?"
        morgan.say "Anyway, you'd look more convincing without that big belly of yours, Kleio!"
        kleio.say "I...I...he can be pretty persuasive, you know!"
    elif kleio.is_visibly_pregnant or kleio.flags.mikeBabies >= 1:
        morgan.say "You'd sound more convincing without that big belly of yours, Kleio!"
        kleio.say "What...hey!"
        kleio.say "You can't make fun of a pregnant woman - what happened to sisterhood?!?"
        morgan.say "Aww, Kleio - you're blushing!"
    elif morgan.is_visibly_pregnant or morgan.flags.mikeBabies >= 1:
        kleio.say "You're being soft on him now, Morgan."
        kleio.say "But I bet he wasn't when you let him knock you up!"
        morgan.say "Hey, no fair - whatever happened to sisterhood?!?"
        kleio.say "Aww, Morgan - you're blushing!"
        kleio.say "Did you go that colour when it happened too?"
    else:
        morgan.say "Let's just say he's moorish, yeah?"
        morgan.say "I think we can both agree on that."
        kleio.say "Mmm...yeah."
        kleio.say "We sure can!"
    kleio.say "I guess I just never thought I'd end up married to the big oaf!"
    morgan.say "Neither did I, Kleio."
    morgan.say "But here we both are!"
    kleio.say "Yeah, here we are."
    kleio.say "And I think it's gonna be a fun ride too!"
    scene bg black
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
