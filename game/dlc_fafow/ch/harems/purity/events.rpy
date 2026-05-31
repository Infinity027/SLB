init python:
    Event(**{
    "name": "purity_harem_event_01",
    "label": "purity_harem_event_01",
    "priority": 500,
    "duration": 1,
    "music": "music/roa_music/one_day.ogg",
    "conditions": [
        IsDone("reona_event_07"),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_park"),
                HasRoomTag("park"),
                ),
            ),
        PersonTarget("reona",
            Not(IsHidden()),
            MinStat("love", 170),
            MinStat("purity", 100),
            MaxStat("sexperience", 0),
            ),
        PersonTarget("harmony",
            MinStat("love", 170),
            HasTrait("religious"),
            MinStat("purity", 100),
            ),
        Or(
            PersonTarget("harmony",
                MaxStat("sexperience", 0),
                ),
            And(
                PersonTarget("harmony",
                    MaxStat("sexperience", 1),
                    ),
                IsDone("harmony_event_07_religious"),
                ),
            ),
        Or(
            PersonTarget("harmony",
                IsFlag("nodate", True),
                HasRoomTag("park"),
                IsActive(),
                ),
            PersonTarget("harmony",
                OnDate(),
                ),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "purity_harem_event_02a",
    "label": "purity_harem_event_02a",
    "display_name": "About Reona",
    "icon": "button_reona",
    "duration": 0,
    "conditions": [
        IsDone("purity_harem_event_01"),
        HeroTarget(IsGender("male"),
            Not(IsFlag("puritydelay")),
            ),
        PersonTarget("harmony",
            IsActive(),
            HasTrait("religious"),
            MinStat("purity", 100),
            ),
        Or(
            PersonTarget("harmony",
                MaxStat("sexperience", 0),
                ),
            And(
                PersonTarget("harmony",
                    MaxStat("sexperience", 1),
                    ),
                IsDone("harmony_event_07_religious"),
                ),
            ),
        ],
    "do_once": True,
    })

    Activity(**{
    "name": "purity_harem_event_02b",
    "label": "purity_harem_event_02b",
    "display_name": "Text Reona About Harmony",
    "icon": "reona",
    "duration": 1,
    "music": "music/roa_music/one_day.ogg",
    "conditions": [
        IsDone("purity_harem_event_01"),
        IsHour(14, 21),
        HeroTarget(
            IsGender("male"),
            Not(IsFlag("puritydelay")),
            ),
        PersonTarget("reona",
            Not(IsHidden()),
            MinStat("purity", 100),
            MaxStat("sexperience", 0),
            Not(IsPresent()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "purity_harem_event_03",
    "label": "purity_harem_event_03",
    "priority": 500,
    "duration": 1,
    "music": "music/roa_music/one_day.ogg",
    "conditions": [
        IsDone("purity_harem_event_02a", "purity_harem_event_02b"),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("church"),
                HasRoomTag("street"),
                HasRoomTag("park"),
                HasRoomTag("pub"),
                ),
            Not(OnDate()),
            Not(IsActivity()),
            ),
        PersonTarget("reona",
            Not(IsHidden()),
            MinStat("love", 200),
            MinStat("purity", 100),
            MaxStat("sexperience", 0),
            ),
        PersonTarget("harmony",
            Not(IsHidden()),
            MinStat("love", 200),
            HasTrait("religious"),
            MinStat("purity", 100),
            MaxStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

label purity_harem_event_01:
    "Have you ever been guilty of complaining that your life is too quiet, that nothing exciting ever happens to you?"
    "I think at one time or another we've all been there, wishing that things were more like an emotional rollercoaster."
    "But the problem is that it's one of those things you don't really appreciate the stress of until you're in the middle of it."
    "And after the mess that's just been made of my personal life by exciting shit, I want the exact opposite."
    "That's why I'm wandering around the park with Harmony, strolling here and there as the afternoon edges towards evening."
    "Sure, it's a slow and sedate as could be, but that's the point - I'm relaxed, chilled-out and feeling totally at ease."
    "Part of me was worried that Harmony would want to go over all of the recent drama with Reona, to dissect it in minute detail."
    "But luckily for me, all she seems to want to do is walk and exchange the occasional word about this and that."
    "We can't have spoken more than a couple of dozen words to each other since we got here."
    "And the odd thing is that it's working, just being here with Harmony feels like it's a healing experience."
    "Eventually we settle down on a bench that commands a pretty sweet view of the park."
    "From it we can see everyone walking on the paths below us and offer casual comments on them too."
    $ renpy.scene()
    $ renpy.show(f"bg {game.room}", at_list=[center, zoomAt(2, (1240, 1320))])
    show harmony normal at center, zoomAt(2, (640, 1340))
    with fade
    pause 1
    show harmony surprised
    harmony.say "Oh, [hero.name]…"
    harmony.say "Look at that sweet little dog!"
    show harmony stuned
    "I strain to see where Harmony is pointing."
    mike.say "Which one are you meaning, Harmony?"
    mike.say "I can see a girl down there, walking up the hill..."
    mike.say "But I don't think she has a dog with her."
    show harmony whining
    harmony.say "Oh no, she doesn't need a dog..."
    show harmony angry
    harmony.say "Because she's already the biggest bitch in the world!"
    show harmony annoyed
    "I'm totally surprised by the sudden change in the tone of Harmony's voice."
    "It's gone from quiet contemplation to complete hatred in a mere matter of seconds."
    "For a moment I think that she's totally lost her mind."
    "But then I strain to see the person that she's talking about."
    "And when I do, everything suddenly falls into place."
    mike.say "Fuck me..."
    mike.say "Is that..."
    show harmony angry
    harmony.say "Reona?"
    harmony.say "Oh yes, it's her alright!"
    show harmony annoyed
    "I watch as Reona draws ever closer to our bench, feeling my confusion begin to turn into dread."
    "There's no question that it really is her, and she's coming straight towards us."
    "So there's also no confusion as to what she's intending to do - which is to confront Harmony and me."
    "As she gets closer I can see that there's an intense expression on her face."
    "One that looks like several strong emotions are battling it out inside of her."
    "Yet it's still impossible to guess just what Reona's intentions are right now."
    "Once she's close enough to be heard, Harmony jumps up from the bench."
    $ renpy.show(f"bg {game.room}", at_list=[center, traveling(1 , 0.3, (640, 720))])
    show harmony at center, traveling(1, 0.3, (340, 720))
    pause 0.3
    "And I do the same a moment later, more out of instinct than anything else."
    show reona pensive at right with moveinright
    show harmony angry
    harmony.say "You've got some nerve, Reona..."
    harmony.say "To even be in the same place as [hero.name] and I after what you did..."
    harmony.say "But to come walking right up to us - that's something else!"
    show harmony b annoyed
    "I'm kind of staggered by the way Harmony's tearing into Reona from the word go."
    "It's so out of character for her, so much more aggressive than the girl I've come to know."
    "And to be honest, it was more the way that I expected Reona to start things out."
    show reona guilty
    "But she just looks downcast, like she's not capable of firing back in the same way."
    "Though when she finally opens her mouth, she still doesn't get to speak."
    "And that's because Harmony takes the opportunity to slap the other girl in the face!"
    show harmony angry a zorder 1 at center, blacker, traveling(1, 0.1, (840, 720))
    play sound spank
    pause 0.1
    show reona shock at hshake
    hide harmony
    show harmony a angry at center, zoomAt(1, (640, 720))
    "The noise it makes is like a Hollywood whipcrack sound-effect."
    "Reona's head twists to the side and then back again in mere seconds."
    "All I can do is step between them, trying on sheer instinct to break it up."
    "But there really doesn't seem to be any chance of Reona fighting back."
    show harmony b mean
    mike.say "HARMONY!" with hpunch
    mike.say "What in the hell are you doing?!?"
    "I can see that Harmony has a look of horror on her face right now."
    "And she's shaking her head, like she can't believe what she just did."
    show harmony surprised
    harmony.say "I..."
    harmony.say "I don't know..."
    harmony.say "I don't know what came over me!"
    harmony.say "I just looked at her, and I saw red."
    show harmony annoyed
    "I glance back over at Reona, who's oddly nodding at this."
    show reona sadsmile at startle(0.2, 5)
    pause 0.2
    show reona sadshock
    pause 0.3
    show reona sad
    reona.say "It's okay, [hero.name]…"
    reona.say "I guess that I deserved it, under the circumstances."
    reona.say "And it's way less than a guy would have gotten in my place."
    show reona normal
    "I'm still looking from one of them to the other and back again."
    "Trying to start talking so that I can get a handle on just what's going on here."
    "But at the same time worried that the two might come to blows again at any moment."
    mike.say "Reona..."
    mike.say "You mind telling me what you're doing here?"
    mike.say "I mean, apart from asking to get slapped in the face!"
    $ renpy.show(f"bg {game.room}", at_list=[center, traveling(1.5 , 0.3, (640, 1020))])
    show harmony at center, traveling(1.5, 0.3, (320, 1020))
    show reona talkative at center, traveling(1.5, 0.3, (960, 1020))
    pause 0.3
    reona.say "Look, guys - I know this looks totally fucking dumb on my part."
    show reona guilty
    show harmony angry
    harmony.say "You're darn right it does!"
    harmony.say "It looks like you're here to try and get your claws into [hero.name] again."
    harmony.say "Like you're swooping in for a second crack at stealing him away from me!"
    show harmony a annoyed with dissolve
    show reona shock at center, traveling(1.5, 0.05, (1060, 1020))
    pause 0.05
    "Reona takes an instinctive step back from Harmony."
    "Raising her hands to defend herself at the same time."
    show reona guilty at center, traveling(1.5, 0.8, (960, 1020))
    pause 0.8
    reona.say "Please, Harmony..."
    reona.say "Just listen to what I have to say, okay?"
    show reona sadangry
    reona.say "I'm not doing any of this because I want to steal your man."
    show reona guilty
    reona.say "I'm doing it because I want to be honest with the both of you."
    show reona pensive
    "Part of me wants to tell Reona to beat it, to get out of my sight."
    "But I can hear the sincerity in her voice as she's pleading with us."
    mike.say "Okay, Reona..."
    mike.say "You already tracked us down here."
    show reona sadshock
    mike.say "And got a slap in the face for your trouble."
    mike.say "We'll hear you out, but after that, no promises."
    "I look to Harmony as I say this, wanting to make sure she's on the same page."
    show harmony angry
    "And for a brief moment she opens her mouth, looking like she's going to object."
    show harmony b mean at startle(0.2, 5)
    pause 0.2
    show harmony annoyed
    "But then she lets out a sigh and shakes her head."
    show harmony angry
    harmony.say "Alright, whatever..."
    harmony.say "But you'd better make this good!"
    show harmony annoyed
    "Reona nods eagerly, and then launches into her explanation."
    show reona talkative
    reona.say "First thing you need to know is that I didn't want to do this."
    reona.say "I tried so hard to keep it bottled up inside for so long."
    reona.say "But that's all part of this mess - [hero.name] taught me to be honest with myself and others!"
    reona.say "Hell, I even took a page out of your book, Harmony."
    reona.say "I even tried praying for the strength to keep it to myself."
    reona.say "But I couldn't..."
    show reona sadsmile
    reona.say "I couldn't keep from saying that I love you, [hero.name]."
    reona.say "You see what I mean?"
    show reona normal
    "Harmony lets out a derisive snort and shakes her head for a second time."
    show harmony angry
    harmony.say "You lust for him, more like!"
    harmony.say "I know your type, Reona - I've seen it all before."
    harmony.say "You see a guy that's got a girlfriend, and that's it."
    harmony.say "You won't be happy until you steal him away from her!"
    show harmony annoyed
    "Now it's Reona's turn to shake her head."
    show reona talkative
    reona.say "I'm not going to stand here and argue with you, Harmony."
    reona.say "I'm not going to claim that I've become some kind of saint either."
    reona.say "Maybe I can't convince you that I mean what I'm saying."
    reona.say "But that's not why I'm doing this."
    show reona normal
    show harmony whining
    harmony.say "Then why are you doing it, Reona?"
    harmony.say "What possible point is there in putting us through this?!?"
    show harmony annoyed
    show reona pensive
    reona.say "I'm doing it because I want you both to know the truth."
    show reona guilty
    pause 0.3
    show reona pensive
    reona.say "I'd rather do that and have you not believe me than keep on lying to your faces."
    show reona normal
    "Reona turns to face me, and as soon as she does, Harmony follows her example."
    "So all of a sudden the attention is on me." with hpunch
    "And it's like staring down the barrel of a gun!"
    $ renpy.show(f"bg {game.room}", at_list=[center, traveling(1 , 0.3, (640, 720))])
    show harmony a at center, traveling(1, 0.3, (320, 720))
    show reona talkative at center, traveling(1, 0.3, (960, 720))
    pause 0.3
    reona.say "I do love you, [hero.name]..."
    reona.say "It started from the way you believed in me when nobody else did."
    reona.say "And I guess it just grew from there, you know?"
    show reona normal
    "I'm still feeling totally confused and disoriented by all of this."
    "So the best I can do is kind of nod in a non-committal manner."
    "On the one hand wanting to seem sympathetic to Reona as she opens her heart to me."
    "But on the other feeling the need to make it plain that I'm not betraying Harmony by doing so."
    mike.say "I..."
    mike.say "I was just trying to be a good friend, Reona."
    mike.say "I'm sorry if it seemed like more than that to you."
    show reona sad at startle(0.2, 5)
    pause 0.2
    show reona sadsmile
    "Reona nods at this."
    show reona talkative
    reona.say "I know, [hero.name], I know..."
    reona.say "And it's okay if you don't feel the same way about me."
    reona.say "Like I said, I'm not trying to steal anyone from anyone!"
    show reona sad
    "Reona's in tears by now, the emotion of the whole thing getting the better of her."
    "I'm about to say something in response."
    "But then Harmony jumps in before I have the chance."
    show harmony annoyed
    harmony.say "Urgh!"
    show harmony b whining
    harmony.say "I hate it when this kind of thing happens to me."
    harmony.say "I hate it because I'm not enough of a bitch to just tell you to get lost!"
    harmony.say "You had to go and be all 'I'm in love, but it doesn't matter if you love me back'!"
    show harmony annoyed
    "Reona and I are both staring at Harmony in amazement right now."
    "Mostly because she seems to be in the middle of some strange process of acceptance."
    "When mere moments before it sounded like she was willing to fight it to the death."
    mike.say "Erm..."
    mike.say "What are you saying...exactly?"
    show harmony whining
    harmony.say "I guess I'm saying that she has to prove it, [hero.name]."
    harmony.say "That if Reona really does love you the way I do..."
    harmony.say "Then she has to find a way to make it work - without turning it into something ugly!"
    show harmony annoyed
    "I open my mouth to say something, but then I just find myself going silent."
    "Because I really don't know where that leaves the three of us."
    "Harmony still looks like she's fuming, and Reona's in tears."
    "And me...well, let's just say that the whole thing leaves me with a lot to think about."
    $ game.flags.puritydelay = TemporaryFlag(True, 2)
    return

label purity_harem_event_02a:
    "I really don't like being in the position that I am right now, feeling like I'm trapped between a rock and a hard place."
    "Only in this case the rock is Harmony, the girl that I truly love and who's been a solid foundation for me since we got together."
    "And of course the hard place is the fact that I've just found out how a totally different girl feels about me too."
    "Normally I'd just chalk Reona's confession of love down to bad timing on her part and focus all my attention on Harmony."
    "But the problem is that Reona's been on a journey of her own recently, one of self-discovery that's changed who she is."
    "And again, were it anyone else, I'd be patting them on the back for waking up to the problems in their life and making a change."
    "The only problem is that all of the changes Reona's going through started when I made her question the life she was living."
    "So in a very real way, I'm bound up in the whole affair, responsible, at least in part, for all of it."
    "It'd be easier if I didn't have a conscience and could just shrug it all off as not my problem."
    "But then if that were the case, I don't think I'd be in a relationship with Harmony in the first place."
    "So I guess that means I have to take the bull by the horns and do what I can to sort things out."
    show harmony at center, zoomAt(1.0, (640, 720))
    "The only problem is that it's pretty apparent Harmony's not interested in discussing the matter."
    mike.say "Harmony..."
    mike.say "Would you come and sit with me?"
    mike.say "I feel like there's some things we should talk about."
    "I'm patting the seat beside me as I say all of this."
    "And at the same time doing the best I can to look at ease."
    "Harmony turns to regard me, and I can already see that she's in denial."
    show harmony talkative at center, traveling(1.5, 0.3, (640, 1050))
    harmony.say "Sure thing, [hero.name]…"
    harmony.say "But I don't know why you need to make it sound so ominous!"
    harmony.say "We can sit and chat about anything you want anytime we like."
    show harmony normal at center, traveling(1.5, 0.3, (640, 1150))
    "Harmony says this as she hurries over and sits down beside me."
    show harmony talkative
    harmony.say "So..."
    harmony.say "What would you like to talk about, huh?"
    harmony.say "The weather's been very pleasant the past few days."
    harmony.say "And I've been meaning to tell you about the sermon my pastor gave last Sunday."
    show harmony normal
    "All the time Harmony's suggesting light-hearted topics of conversation I'm looking her in the eye."
    show harmony sad
    "And it's not long before she seems to realise that her efforts to ignore the elephant in the room aren't working."
    show harmony whining
    harmony.say "Oh bother..."
    harmony.say "When you said things, you didn't really mean that, did you?"
    harmony.say "You meant one thing in particular!"
    show harmony sad
    "I nod as I prepare myself for what lies ahead."
    mike.say "That's right, Harmony..."
    mike.say "What I really need to talk to you about is Reona."
    mike.say "We need to talk about what happened in the park the other day."
    show harmony annoyed
    "As soon as the truth is out in the open, Harmony's whole demeanour changes."
    "Don't get me wrong, it's not like she suddenly becomes mean or nasty - she's not that kind of girl."
    "But she does become defensive, and it's obvious that she's far from fond of even discussing Reona."
    show harmony angry
    harmony.say "What is there to discuss, [hero.name]?"
    harmony.say "She's just some silly little girl that's infatuated with you."
    harmony.say "We both know that she doesn't love you - not the way I do!"
    show harmony annoyed
    "I shake my head, already aware of the fact I'm probably upsetting Harmony by doing so."
    "But all the same, I feel like we have to be totally honest about Reona's feelings."
    mike.say "I wish it were that simple, Harmony."
    mike.say "But I think we both know Reona's totally serious."
    mike.say "You saw the way she was in the park - it's like she can't deny her feelings."
    show harmony b mean
    "Harmony lets out a snort of derision, and she crosses her arms over her chest."
    show harmony angry
    harmony.say "Well of course she's going to think her feelings are real, [hero.name]."
    harmony.say "Especially if you insist on encouraging her!"
    harmony.say "Just tell Reona to get lost, and she'll soon forget all about it."
    show harmony upset
    "Oh man, this is harder than I ever thought it would be."
    "I can see how paranoid Reona's confession is making Harmony feel."
    "And it's tearing me apart inside watching her try to fight back."
    "But even so I can't just abandon Reona, not after I started her down this road."
    show harmony normal
    mike.say "Harmony, you know that I love you."
    mike.say "And I'd never do anything to hurt you."
    mike.say "But I also know that you're in pain right now, that you're feeling vulnerable."
    mike.say "And it's making you forget about the lessons of faith that you taught me."
    show harmony stuned
    "Harmony looks at me with genuine surprise in her eyes."
    show harmony surprised
    harmony.say "What do you mean?"
    show harmony stuned
    mike.say "Mercy and forgiveness, Harmony..."
    mike.say "Those are things that you taught me to believe in."
    mike.say "Not judgement and condemnation, remember?"
    "I'm watching Harmony closely as I bring all of this up."
    "Mainly because I'm afraid trying to use her faith against her like this is a dumb idea."
    "Part of me is expecting her to blow her top and slap me across the face any moment."
    show harmony embarrassed
    "And from the way her face is filling with emotion, that could be about to happen!"
    show harmony sad
    "But then the dam breaks, and Harmony bursts into tears, rather than exploding into violence."
    show harmony whining
    harmony.say "Aargh!"
    harmony.say "Why is this happening to me?!?"
    harmony.say "I've done the best I can to be a good person."
    harmony.say "I go to church and I volunteer to do stuff all the time."
    harmony.say "I even buy that horrid chocolate with the white-stuff on it!"
    harmony.say "And I was really happy when I got myself a lovely boyfriend..."
    harmony.say "A nice guy that digs my natural curves - that's all I ever wanted."
    show harmony sad
    "I'm staring at Harmony in amazement as all of this comes flooding out of her."
    "There are genuine tears streaming down her cheeks right now."
    show harmony whining
    harmony.say "Then this Reona girl has to show up."
    harmony.say "With her whole redemption arc thing going on..."
    harmony.say "Urgh...I feel like I'm being tested, you know?"
    harmony.say "Like my morals are being stretched to their limits?"
    show harmony sad
    "I'm nodding all the time Harmony is off-loading her feelings."
    "And I dig in my pockets, finding a handkerchief to offer her as well."
    "Harmony takes it and does the best she can to dry her eyes."
    "Then she makes a point of blowing her nose too."
    "And the sound of that is enough to make my eyes bulge."
    "As well as reluctant to accept the handkerchief when she's done with it too."
    mike.say "For what it's worth, Harmony..."
    mike.say "I don't think you're being tested."
    show harmony stuned
    "Harmony looks at me with confusion on her face."
    show harmony surprised
    harmony.say "You..."
    harmony.say "You don't?"
    show harmony stuned
    mike.say "No, Harmony, I don't."
    mike.say "I think what you're going through right now is just proof that you're a good person."
    mike.say "You'd like to ignore Reona's plight and just get on with your life like it was before."
    mike.say "And that's totally natural, what anyone else would do - but not someone as good as you."
    mike.say "Because you know that I'm right when I say that Reona's changed, that she's on a journey."
    mike.say "One of those spiritual journeys that are kind of a religious thing?"
    "Harmony sniffles and snuffles as she listens to me."
    "And it's pretty obvious that she's far from happy about all of this."
    "But I can see from the look in her eye that she's listening closely, taking it all in."
    show harmony sadsmile
    "And when she gives me a small nod, I know that I've truly reached her."
    show harmony talkative
    harmony.say "Okay, [hero.name]…"
    harmony.say "I'll do the best I can to help."
    harmony.say "But I just hope that you're right about her."
    harmony.say "Because if you're not...then I don't know what will become of me!"
    show harmony normal
    "I return Harmony's nod, taking hold of her hand and squeezing it as I do so."
    "And I'm not doing all of that just for the sake of talking her round either."
    "I believe that she's struggling against her own base instincts right now."
    "That there's a battle going on inside of her that's very real indeed."
    "I just have to trust that I know what I'm doing when it comes to Reona."
    "That my instincts are telling me the right things and not leading me astray."
    $ game.flags.puritydelay = TemporaryFlag(True, 2)
    return

label purity_harem_event_02b:
    "Now that I've managed to sit Harmony down and have a serious discussion, I feel like it's time to tackle the other half of the equation."
    "Which, of course, means that I have to do the same thing with Reona in the hope that I can make a similar breakthrough with her too."
    "But the problem is that Reona seems less than eager to face me after the meeting between the three of us in the park."
    "It takes a hell of a lot of pleading on my part even to get her to agree to meet up with me, with texts flying back and forth."
    $ nvl_mode = "phone"
    nvl clear
    mike_nvl "Hey, Reona - how are you doing?"
    reona_nvl "Oh...hey, [hero.name]…"
    reona_nvl "Pretty bad, really!"
    mike_nvl "Oh man, sorry to hear that."
    mike_nvl "I was hoping we could meet up?"
    mike_nvl "Maybe it'd help to talk about things?"
    reona_nvl "You really want to?"
    reona_nvl "Thought I'd be the last person you wanted to see!"
    mike_nvl "Of course not, Reona!"
    mike_nvl "I'm serious - can we meet up soon?"
    reona_nvl "Okay, okay..."
    reona_nvl "So long as it's just the two of us, right?"
    mike_nvl "Sure thing, Reona - just tell me where and when."
    "A few more messages fire off between us, agreeing a time and place to meet."
    $ nvl_mode = None
    $ game.room = "pub"
    scene bg pub with fade
    "And with that I'm off to the appointed place, already beginning to feel myself getting nervous."
    "Of course, in my eagerness, I manage to make it there first, which leaves me standing around waiting."
    show reona leftback at center, zoomAt(1.25, (640, 880)) with easeinright
    "And even though it doesn't take Reona all that long to turn up too, I have enough time to start doubting myself."
    "All of which means that I look every bit as edgy as she does once we're exchanging awkward waves."
    show reona talkative rightopen at center, traveling(1.5, 0.5, (640, 1050))
    reona.say "Ah..."
    reona.say "Hey, [hero.name]…"
    show reona normal rightnormal
    mike.say "Hey, Reona - thanks for agreeing to meet me."
    "Reona nods at this, but she takes a deep breath before saying anything more."
    "And it's clear that this isn't going to be a light-hearted little chat."
    show reona talkative
    reona.say "I...I don't really know how to do this!"
    reona.say "Hell, I wasn't even sure that you'd want to see me again after..."
    show reona normal
    mike.say "After what happened in the park?"
    show reona talkative
    reona.say "Yeah, obviously that..."
    reona.say "I mean...are you sure that you don't want to chew me out over that?"
    reona.say "Because I'd totally understand it if you did."
    show reona normal
    "I don't hesitate to shake my head."
    show reona interested
    mike.say "No, Reona - I don't want to do anything like that."
    mike.say "I got the feeling that what you did took a lot of guts."
    mike.say "And I don't think you felt like you had a choice either."
    "Reona's listening to every word I say with rapt attention."
    "And I can see hope beginning to shine in her eyes as I empathise with her."
    show reona pensive
    "For a moment she seems to want to ask me to say more in the same vein."
    show reona sad
    "But then I notice that she changes her expression."
    "Almost like she's forcing herself down a different path."
    show reona sadfrustrated
    reona.say "Don't bite my head off, okay?"
    reona.say "But I just wanted to ask..."
    reona.say "Is Harmony doing okay?"
    reona.say "I mean...I get it if you don't want me to talk about her."
    show reona normal
    "I can see how much Reona's trying right now."
    "Doing the best she can to think of others rather than herself."
    "And it just adds to the conviction I have that she's totally genuine."
    "The old Reona would never have done that, as she was just too self-obsessed."
    show reona interested
    mike.say "You're being honest with me, Reona - I can sense that."
    mike.say "So I'm going to be honest with you in return."
    mike.say "Harmony's conflicted about what's happened."
    mike.say "She's afraid that you're going to come between us."
    mike.say "But she's doing the best she can to listen and be rational about it."
    mike.say "And I've told her that I believe your intentions come from a good place."
    "Reona listens intently as I explain the situation."
    "And she nods when I describe my take on her actions too."
    show reona shout
    reona.say "You have to believe me when I say I never meant to break that girl's heart!"
    reona.say "And I'm not trying to throw myself at you out of desperation either."
    show reona embarrassed
    reona.say "It's just that I've never felt an attraction like this before, [hero.name]."
    reona.say "Back in the day, I only ever knew what it felt like to desire someone's body."
    reona.say "But with you...I feel like you're interested in my soul!"
    reona.say "It's totally new, and it's scary too."
    show reona happy at startle
    "Reona chuckles and shakes her head."
    show reona shy blush
    reona.say "This is going to sound totally cheesy..."
    reona.say "But I feel like I stopped chasing men when I realised what kind of man I should have been chasing!"
    show reona normal
    "Reona's looking me straight in the eye as she says this."
    "And I can feel the intensity of her emotions as she does so."
    "Man, there's no way I can doubt her sincerity right now."
    "And I know that if I wasn't so in love with Harmony, there's no way I could resist her!"
    mike.say "I'm not going to lie to you, Reona..."
    mike.say "I know that there's a genuine affection for you in my heart."
    mike.say "All I have to do is think of you, and I feel it, like a sudden warmth in my chest."
    mike.say "But the problem that I have is this - I don't know what form it should take yet."
    mike.say "And I'm starting to think maybe that's a part of what's happening here, you know?"
    show reona surprised
    "Reona looks more than a little puzzled with what I'm saying."
    "And she shakes her head, confirming my suspicions a moment later."
    show reona shock
    reona.say "No, [hero.name], I really don't!"
    reona.say "I'm new to all of this stuff, remember?"
    show reona normal
    mike.say "What I mean is that I feel like this was all meant to happen, Reona."
    mike.say "Like you needed to be saved, and I was supposed to help with that."
    mike.say "Harmony would just say that this was God moving in mysterious ways."
    mike.say "And I don't know about that myself, but it does feel like something higher has a hand in it."
    mike.say "It feels like all this is about forgiveness, and maybe more - maybe it is a little divine?"
    show reona at center, traveling(1.75, 1.0, (640, 1150))
    "Reona's nodding again, and getting closer to me the whole time I'm talking."
    "For a moment I'm worried that she's getting carried away by the emotion of the moment."
    "That she's going to lean in close and try to kiss me or something."
    "But then I see that she's raising her hands, bringing them together."
    "And I know that she's been struck by the urge to pray on all I've said."
    "So without the need to say another word, I raise my hands too."
    "And bringing them together with Reona's, I close my eyes and begin to pray."
    "It's not the loud, speaking out loud kind of prayer you hear in church."
    "Instead this is silent and contemplative, a chance to look inwards and reflect."
    "Because god knows the two of us have a lot to meditate on right now!"
    "So any chance to take time out is more than welcome."
    $ game.flags.puritydelay = TemporaryFlag(True, 2)
    return

label purity_harem_event_03:
    "Now that I've had a frank discussion with both Harmony and Reona, I feel like I should be closer to having this whole thing figured out."
    "I mean, I felt that way when I walked away from my talk with each of them, like I'd taken a big step towards understanding everyone's feelings."
    "But as soon as I found myself alone again, the confusion just seems to come creeping back in, making me question everything all over again."
    show reona leftback at center, zoomAt(1.25, (840, 880))
    show harmony b at center, zoomAt(1.25, (440, 880))
    with dissolve
    pause 0.3
    show reona at center, traveling(1.5, 1.0, (840, 1040))
    show harmony b at center, traveling(1.5, 1.0, (440, 1040))
    "And you can imagine the way that all of this is magnified when I look up to see Harmony and Reona walking towards me, totally unannounced."
    "What's more, they're clearly together - even holding hands!"
    "It's not like I can hide my surprise at seeing them like that either."
    "And it's obvious to Harmony and Reona too, as they begin to gesture to me as soon as they're close enough to do so."
    show harmony happy
    harmony.say "Don't panic, [hero.name] - it's okay!"
    show harmony normal
    show reona talkative rightopen
    reona.say "Yeah, [hero.name]…"
    reona.say "We're not trying to gang up on you, I promise!"
    show reona normal rightnormal
    "Okay, I admit that I might have taken an involuntary step backwards just now."
    "But once the two of them are close enough to have an actual conversation, I manage to get a hold of myself."
    "So much so that I can take a step forwards and force a smile onto my face."
    mike.say "Ah..."
    mike.say "Hey, guys!"
    mike.say "This is a real surprise."
    mike.say "I certainly wasn't expecting to see the two of you - together, at least."
    show harmony happy
    show reona embarrassed
    "Harmony and Reona exchange a quick glance, and I can see that something passes between them."
    "There's a couple of nods thrown in there too, making me think that they've rehearsed for this moment."
    "But when it comes to the actual talking, Reona seems to take a conscious step backwards."
    "Clearing the way for Harmony to take the lead, which she does a moment later."
    show harmony talkative
    harmony.say "First things first, [hero.name]…"
    harmony.say "Obviously Reona and I have been talking to one another."
    harmony.say "And while we might not have told you about it, we weren't trying to be underhanded."
    show harmony normal
    "Reona nods, backing up Harmony's sentiment."
    show reona talkative
    reona.say "We just felt like it was time the two of us talked in an open and honest manner."
    reona.say "That we began to share our feelings and see where that lead us."
    show reona normal
    "All of this sounds encouraging, so I make sure to listen without interrupting."
    show harmony talkative
    harmony.say "It didn't take us long to realise that fighting was a dumb thing to do."
    harmony.say "Especially when the dominant emotion we're all feeling is love."
    harmony.say "And after all, isn't love a sacred thing?"
    harmony.say "Something that's spiritual, that we should be thankful for?"
    show harmony normal
    show reona talkative
    reona.say "That's something you showed us, [hero.name]…"
    reona.say "That love shouldn't be a selfish thing."
    reona.say "It shouldn't make us want to possess another person and keep them to ourselves."
    reona.say "We should be sharing our love, allowing it to raise up those around us."
    show reona normal
    "The more I hear, the more amazed I find myself feeling."
    "I can't believe that I'm talking to the same two girls right now."
    "Because they're so different from the ones I remember back when this all got started."
    mike.say "Wow..."
    mike.say "That's a lot to take in, guys!"
    mike.say "And I have to say that it's beautiful you see things that way."
    "Everyone's nodding and smiling right now."
    "But I still feel like there's an elephant in the room with us."
    "And I'm going to need to address it for the matter to be fully closed."
    mike.say "So..."
    mike.say "Where does that leave the three of us?"
    mike.say "You know, in terms of our relationship to each other?"
    mike.say "I know that I'm still one hundred percent devoted to you, Harmony."
    mike.say "But what about you, Reona - are you going to be okay?"
    "It's not like I expected there to be an instant and easy answer to the question."
    "After all, it's a pretty serious thing to ask someone under any circumstances."
    show reona embarrassed
    "But what I wasn't expecting was another of those meaningful glances between Harmony and Reona."
    "And this time I'm sure that there's even more weight behind it than the first."
    "All of which makes me suspect that I'm about to get another rehearsed answer."
    "One that Harmony's going to take the lead in delivering."
    show harmony talkative
    harmony.say "That's another thing we've been discussing."
    harmony.say "In fact, it's something we've talked about more than anything else."
    harmony.say "We think that there's nothing wrong with all of the love between us."
    show harmony normal
    show reona talkative
    reona.say "In fact, we think that it's a special kind of love."
    reona.say "A sacred love, even!"
    show reona normal
    show harmony talkative
    harmony.say "And that's why we want to do something to celebrate it."
    show harmony normal
    "I'm nodding along through all of this, though I don't really know where it's going."
    "Are they going to suggest that we perform some kind of sacred orgy to celebrate?"
    "Or are they thinking more along the lines of us all going off to become nuns and monks?"
    "Oh god, I seriously hope that they're not wanting to start some kind of cult!"
    mike.say "Is that so?"
    mike.say "And just what did you have in mind, exactly?"
    show harmony talkative
    harmony.say "We're suggesting that we stop denying what's so obvious, [hero.name]…"
    harmony.say "That we accept the three of us are supposed to be able to express our love for each other."
    show harmony normal
    show reona talkative
    reona.say "We want to marry you, [hero.name]!"
    show reona normal
    show harmony talkative
    harmony.say "Well, that's the legally binding form the union would take, certainly."
    harmony.say "But I tend to see it primarily as a spiritual union."
    harmony.say "An unconventional one, but a genuine one nonetheless."
    show harmony normal
    show reona talkative
    reona.say "So what do you say?"
    reona.say "Will you marry us?"
    show reona interested
    "I'm doing the best I can to formulate an answer to Reona's question."
    "But the problem is that it's so simple and straight-forward of a thing to ask."
    "Especially when the larger proposition behind it is so mind-blowing in nature."
    "I don't know what I was expecting the solution to this whole thing to look like."
    "But I can definitely say that it wasn't a union between Harmony, Reona and myself."
    mike.say "Are you guys for real?!?"
    mike.say "The three of us getting married?"
    mike.say "I...I suppose you mean we'd do it for the formal acknowledgement, right?"
    mike.say "I mean...I wouldn't expect the three of us to..."
    mike.say "Well, you know...do stuff...in the bedroom?"
    show harmony happy
    show reona happy
    "Harmony and Reona surprise me by responding to my stumbling question with smiles and laughter."
    show harmony talkative
    harmony.say "Oh, [hero.name]…"
    harmony.say "You're so humble and sweet!"
    show harmony normal
    show reona talkative
    reona.say "We already worked all of that out between us."
    reona.say "And we decided that if our love is sacred, then expressing it is too!"
    show reona normal
    "I feel a flood of relief wash over me, and not a little excitement too."
    mike.say "Oh, well..."
    mike.say "I suppose that's okay then."
    $ Harem.join_by_name("purity", "harmony", "reona")


    mike.say "And yes, I will marry you both - but not just because of what you just told me!"
    "I can feel that my mouth is curved into a pretty wide smile right now."
    show reona stuned
    show harmony stuned
    "But I notice that Harmony and Reona are looking at me with concern in their eyes."
    show harmony surprised
    harmony.say "[hero.name], you're crying!"
    show harmony stuned
    show reona surprised
    reona.say "Are you feeling okay?"
    show reona stuned
    "Putting a hand to my cheek, I realise that they're right."
    "Tears are streaming down my face right now, and yet I feel like laughing."
    mike.say "This is crazy - I feel so happy right now..."
    mike.say "So why am I crying?"
    show harmony talkative
    show reona happy
    harmony.say "I think you're just overwhelmed, that's all."
    show harmony happy
    show reona talkative
    reona.say "Yeah - it's a lot to take in."
    show reona happy
    show harmony talkative
    harmony.say "But enjoy the chance to be a mess while you still can."
    harmony.say "Because there's going to be a lot of stuff to plan!"
    show harmony normal
    show reona talkative
    reona.say "We're going to have to work out all the details of the wedding."
    reona.say "Where it's going to happen and who we're going to invite - all that stuff."
    show reona normal
    mike.say "Well, I only know one thing for sure..."
    mike.say "It's going to be a small affair."
    mike.say "This isn't a wedding for the world - it's one for the soul!"
    return

label harmony_reona_male_ending:


    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    with fade
    "The chapel is a small affair, no more than a couple of rows on each side of the aisle."
    "And those seats are filled with only the closest relatives and friends that that we could fit in."
    "But looking back over my shoulder at all of them, I realise that I still don't know many of those faces."
    "Which is a reminder that there's a lot things about my prospective brides that I don't know as well."
    "Though I suppose that the same is true of them when it comes to my own family and friends."
    "Whatever life has in store for the three of us, it's going to be a voyage of discovery."
    "There is one thing that strikes me though, and that's how few of the guests are from Harmony's own church."
    "My guess would be that's on account of the fact that she's going to be marrying Reona, as well as me."
    "And I suppose it's a pretty good indication of how tolerant some of that congregation are."
    "Because even though polygamy is now legal in this country, that doesn't mean everyone's cool with it."
    "My thoughts are just about to wander down that rather gloomy path, when something makes my ears prick up."
    "It's the sound of music beginning to swell and fill the chapel, stirring everyone in attendance as it does so."
    show reona wedding happy at left4
    show harmony wedding happy at right4
    "Of course I instantly recognise the tune that Harmony and Reona chose for their entrance."
    "It's subtle and yet memorable, totally fitting for two girls that I'm about to marry."
    "A moment later the door of the chapel open and the brides stride through them."
    "All eyes are instantly on Harmony and Reona as they make their way down the aisle."
    "They walk side by side, keeping almost perfect pace with each other as they come ever closer."
    "And I must have imagined what they'd look like in those dresses a hundred times already."
    "But there's no way what I conjured up inside of my head could hope to compare with what I'm seeing now."
    "Nobody could ever compare Harmony and Reona in terms of their individual looks."
    "The two of them are a striking contrast to each other, even when both in wedding dresses."
    "And yet to my eye they seem almost like they were meant to be seen together."
    "As if each is the perfect contrast and compliment to the other."
    "All three of us are beaming at each other by now, eager to get the ceremony started."
    "And so there's no small-talk once Harmony and Reona reach my side at the altar."
    show harmony normal
    harmony.say "Ahem!"
    show reona normal
    "At the sound of Harmony's cough, the priest almost leaps to attention."
    "Priest" "Wha..."
    "Priest" "I..."
    "Priest" "Oh...oh yes!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To witness the union of these three people..."
    "Priest" "In the bonds of holy matrimony."
    "Even though there are three of us tying the knot here today, almost everything else is familiar."
    "The priest says all of the same things, only on occasion mentioning three people, rather than two."
    "Things only really start to get interesting once we make it to the vows."
    "Priest" "Do you, Harmony..."
    "Priest" "Take Reona and [hero.name]…"
    "Priest" "To be your sister-wife and husband?"
    show harmony happy
    harmony.say "I do."
    "Priest" "And do you, Reona..."
    "Priest" "Take Harmony and [hero.name]…"
    "Priest" "To be your sister-wife and husband?"
    show reona happy
    reona.say "I do."
    "Priest" "And do you, [hero.name]…"
    "Priest" "Take Harmony and Reona..."
    "Priest" "To be your brides?"
    mike.say "I totally do!"
    "Priest" "Very well."
    "The priest turns to face the assembles guests, a serious expression on his face."
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these three may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary ripple of nervous laughter."
    "Not to mention tense glances between Harmony, Reona and myself."
    "But thankfully the moment passes without anyone speaking up."
    "Which means that we're in the clear."
    "Priest" "In that case, it is my pleasure to announce that you are man and wives."
    "Priest" "You may celebrate in a dignified manner."
    "Harmony, Reona and I already agreed that we'd embrace at this point in the ceremony."
    "And that's exactly what we do, coming together in a show of dignified unity."
    "Maybe later there'll be time for doing something more traditional, like sharing a kiss."
    "But we've already vowed that our union will be between ourselves and god."
    "Nothing that we do of an intimate nature will be on public display."
    "And I wouldn't have it any other way."


    scene bg bedroom1
    show harmony wedding at left4
    show reona wedding at right4
    with fade
    "I have to admit that my head is still spinning by the time Reona, Harmony and I make it to the bedroom."
    "Everything seems to have happened so fast today, as if it's all gone past in the mere blink of an eye."
    "One minute I was waking up and remembering that today was the big day."
    "And then it feels like the next I was a married man with a bride on each arm."
    "For the most part, I feel like Reona and Harmony are in the same place too."
    "But as I close the door to the bedroom behind me, all of that seems to change."
    "Because when I turn around to face them, they both have very serious looks on their faces."
    mike.say "Erm..."
    mike.say "Why so serious, guys?"
    mike.say "Isn't this part of the wedding festivities supposed to be fun?"
    "Reona and Harmony nod as soon as I ask the question, but they don't look any less intent."
    show harmony talkative
    harmony.say "Of course this is going to be fun, [hero.name]."
    harmony.say "We've all been perfectly chaste and faithful to one another."
    harmony.say "And this is where that sacrifice is rewarded."
    show harmony normal
    "I see Reona flush a little as Harmony describes the chaste nature of our relationship."
    "Because not all of us have been on that particular band-wagon from the very start."
    show reona talkative
    reona.say "You..."
    reona.say "You mean the relationship between all three of us, right?"
    reona.say "That's the one that really matters, yeah?"
    show reona normal
    show harmony talkative
    harmony.say "Of course I do, Reona!"
    show harmony normal
    show reona shy
    reona.say "Okay, okay - just checking."
    show reona normal
    "Harmony does the best she can to sound serious again."
    show harmony talkative
    harmony.say "Now it's your duty to demonstrate your manliness, [hero.name]."
    harmony.say "It's time to make your wives heavy with child!"
    show harmony normal
    "I can already feel myself starting to sweat a little as Harmony lays out my duties."
    "But then I did sign up for this knowing what was going to be expected of me."
    mike.say "Rest assured, my brides - I will fulfil my duties!"
    "This seems to be the correct thing to say."
    show reona interested
    show harmony embarrassed
    "As it sets the pair of them off giggling and blushing too."
    "Something that only seems to become more intense as I start to take off my clothes."
    "Reona and Harmony are sitting on the bed, watching me strip off."
    "And they soon start to follow my example, peeling things off a little at a time."
    show reona underwear
    show harmony underwear
    with dissolve
    "Of course the sight of them getting naked only serves to increase my own excitement."
    "Which means that I do all I can to speed up the process."
    show reona underwear topless
    show harmony underwear topless
    with dissolve
    "But this in turn seems to make them more excited again, increasing their speed too."
    "And so we undress in a weird kind of race, each pushing the other to go faster."
    show reona naked
    show harmony naked
    with dissolve
    "Once I'm finally naked, I walk slowly towards the bed where my brides await me."
    "I'm already getting myself into the idea of playing the role of the dutiful husband."
    "Thinking that they're going to want me to be the one taking the lead in all of this."
    mike.say "Okay, ladies..."
    mike.say "Just lie back and leave this to..."
    mike.say "WHOA!"
    "As one, Reona and Harmony reach out and grab hold of my arms."
    "And then they yank me forwards so that I stumble forwards onto the bed."
    "Before I can even make sense of what's happening, they're turning me over."
    "This means I'm suddenly on my back, staring up at the ceiling."
    scene purity foreplay with fade
    harmony.say "Just lie back and leave it to us, [hero.name]."
    harmony.say "Because we've had plenty of time to figure all of this out."
    reona.say "Yeah, [hero.name]…"
    reona.say "We've worked it all out in minute detail!"
    "Don't get the impression that Reona and Harmony are just saying all of this to me."
    "Oh no, they're already on the move, getting into position and pinning me to the bed."
    "Raising my head, I see Harmony straddling my thighs while facing me."
    "And I just manage to see her reaching form my cock before my view is obscured."
    "Specifically it's obscured by Reona swinging her leg over my chest."
    "Then I find her butt landing a mere few inches from my face!"
    "Before I can say a word, I feel Harmony tighten her grip on my cock."
    show purity foreplay forth
    "She's handling it with a skill that I find pretty surprising."
    show purity foreplay back
    "Almost like she might never have done the practical before now, but she's studied the theoretical until it's second nature."
    show purity foreplay forth
    "And she's doing it so well that there's no way I want her to stop."
    show purity foreplay back
    "So instead of protesting, I decide to get in on the action too."
    show purity foreplay forth
    "Slapping a hand on either side of Reona's waist, I take a firm hold of her."
    show purity foreplay back
    "And when she yelps and jumps in surprise, I push my head forwards."
    show purity foreplay forth cunni
    "This means that I can just about reach between Reona's thighs."
    "And my tongue can make it all the way to her pussy too."
    show purity foreplay forth cunni up
    "So I don't hesitate to make the most of that fact, licking and lapping at those lower lips."
    show purity foreplay back cunni mid
    "Of course this means that Reona's soon helplessly moaning from the pleasure she's feeling."
    show purity foreplay forth cunni down lookmike
    "And as good as the sensation of Harmony playing with my cock is, I don't think it's going to last."
    show purity foreplay back cunni mid
    "Because I know all too well how long she's been waiting for this time to arrive."
    show purity foreplay forth cunni up
    "How she's kept herself chaste and pure, all until the right guy came along."
    show purity foreplay back cunni mid
    "So how can anyone expect her to just sit back now and watch another girl getting all the action?"
    show purity foreplay forth cunni down lookreona
    harmony.say "Ah..."
    harmony.say "Maybe we should be a little more careful, Reona?"
    show purity foreplay back cunni mid
    reona.say "Huh?"
    reona.say "Wha..."
    show purity foreplay back cunni up
    harmony.say "I mean, we don't want to wear him out, do we?"
    harmony.say "It'd be a terrible waste if neither of us got what we wanted to tonight!"
    show purity foreplay back cunni mid
    "In the end I feel Harmony let go of my cock, and then lean forwards."
    "A second later she must shove Reona backwards, because the other girl tumbles off me."
    "Reona rolls a little way away on the bed, looking more than a little puzzled."
    scene bg bedroom1
    show reona annoyed naked at left4
    show harmony naked at right4
    with dissolve
    reona.say "Hey..."
    reona.say "I was enjoying that!"
    show reona sadfrustrated
    show harmony embarrassed
    harmony.say "I know, I know - but we need to focus, Reona."
    harmony.say "[hero.name] has a duty to perform tonight."
    harmony.say "And he can't do that with you sitting on his face!"
    show harmony stuned
    "I'm about to speak up and say that I probably could."
    "But from the look on their faces right now, I don't think that would be a good idea."
    "So instead I focus my attention on solving the next issue that's fast approaching."
    "Specifically which one of them is going to get it first?"
    default purityset = set()
    scene bg bedroom1
    show reona naked at left4
    show harmony naked at right4
    with fade
    menu purity_choices:
        set purityset
        "Choose Harmony":
            mike.say "What are you waiting for, Harmony?"
            mike.say "You had it in your hand just now."
            mike.say "So why not just take things to the next step?"
            "Harmony looks more than a little surprised at this, shaking her head."
            show harmony surprised
            harmony.say "I..."
            harmony.say "I don't like to presume."
            show harmony stuned
            "Sensing that she needs to be given some sign of my permission, I put my hands on her waist."
            "And then I gently guide her downwards, relying on her own instincts to know what to do next."
            "I'm betting on the fact that Harmony's been wanting this for so long to make things work."
            "That now she's finally in this position, everything is going to click for her."
            "But as she gets ever closer, I can see that it's not playing out in the way I'd hoped."
            "And the pressure seems to be proving too much for Harmony to handle."
            show reona talkative
            reona.say "Oops..."
            reona.say "We just need to change angles here a little bit."
            reona.say "Like this..."
            scene bg black
            show purity threesome harmony with fade
            "Without needing to be asked, Reona steps in and lends Harmony a helping hand."
            "And she does so in a way that doesn't undermine the other girl too."
            "I can't help smiling as I watch the two of them working together so well."
            "Because it's a reminder of how far we've all come together."
            "And how close our relationship is now that we're all joined together in marriage."
            "Harmony nods as Reona makes sure the two of us come together in just such a way."
            "But the moment the tip of my cock touches Harmony's lips, everything changes for me."
            show purity threesome harmony full
            "I can't keep on watching the two of them in the same way as I was just now."
            "Because from this point on I'm right there in the middle of the action."
            "I feel my breathing become more laboured and my heart begin to pound in my chest."
            "At the same time, Harmony is starting to rub herself up and down against me."
            "Every move she makes sending incredible sensations through my entire body."
            "I can feel the change in her pussy as it gets ever softer and slicker too."
            "So it really shouldn't come as any surprise when she reaches the point of no return."
            show purity threesome harmony vaginal half
            play sexsfx1 slide_in
            "But even so, when those lips begin to part and I inch my way inside, it's almost mind-blowing."
            "Suddenly I'm not just holding Harmony in place above me."
            show purity threesome harmony closed
            "Instead it feels like I'm pulling her down and onto me, almost in desperation."
            play sexsfx1 slide_in
            "And at the same time I'm trusting myself upwards and into her too."
            play sexsfx1 slide_out
            pause 1
            play sexsfx1 slide_in
            "The very moment that I feel my cock filling Harmony, I pull back and thrust again."
            play sexsfx1 slide_out
            pause 1
            play sexsfx1 slide_in
            "That simple motion feels so good that it compels me to do it over and over again."
            play sexsfx1 fuck_calm loop
            "But it's not like I'm some mindless animal that's determined to copulate with her."
            show purity threesome harmony full back
            "Because Harmony's hardly passive while all of this is going on."
            "She's pushing down with the same force as I'm thrusting upwards."
            "And I get the distinct impression that she wouldn't let me stop if I wanted too."
            "Looking up I can see that truth of the matter written all over Harmony's face."
            "She doesn't just look like she's enjoying the experience of being fucked."
            show purity threesome harmony speed
            play sexsfx1 fuck_moderate loop
            "What I can see there is the realisation of her whole system of philosophy and belief."
            "Here's the girl that's spent her entire life keeping herself pure and chaste."
            "She's waited until the right man came along, until her wedding night."
            "And now that it's all paying off, she really looks as though it was worth the effort."
            "I'd be happy to keep on gazing up at Harmony right now, watching her until the very end."
            "But it seems as though Reona has other plans."
            "Because a moment later, her butt is right back where it was before - mere inches from my face!"
            show purity threesome harmony oo
            play sexsfx1 fuck_speed loop
            reona.say "Head's up, [hero.name]..."
            reona.say "You've got two wives, remember?"
            reona.say "And that means you got to take care of them both!"
            "It's not like I'm in any kind of position to object or argue with Reona right now."
            "And as it looks like she wants more of the treatment I was giving her before, I get right to it."
            "Feeling a sense of the familiar, I put my tongue and lips to work pleasing her."
            show purity threesome harmony mm hip
            play sexsfx1 fuck_moderate loop
            "And soon enough my ears are filled with the sound of them both moaning with pleasure."
            "Thankfully I can soon keep up my efforts by repeating the same actions over and over."
            "All the same I still kind of feel like I'm spinning plates here."
            "So it comes as a relief when I feel Harmony beginning to press down harder still."
            "At the same time there's the sensation of her squeezing my cock too."
            "And all of that leads me to believe that she's about to climax."
            play sexsfx1 fuck_speed loop
            "I have no idea how close I was to being there myself, but I feel my body begin to do the same."
            "Maybe I was almost there and didn't realise it, or maybe Harmony's own readiness pushed me to it."
            "Either way there's only one way that this is going to end."
            "Holding onto Harmony more tightly than ever, I make one final thrust into her."
            show purity threesome harmony creampie -speed
            play sexsfx1 final_thrust
            "And then I lose it, shooting my load once I'm as deep inside of her as possible."
            "Harmony throws her head back, letting out a cry that's as much triumph as it is the sound of her orgasm."
            show purity threesome harmony ahegao full tongue
            harmony.say "Aaargh!"
            harmony.say "Yeah...fuck yeah!"
            show purity threesome harmony oo squirt
            "A moment later Reona cums too, but I can't hear a single thing."
            "Because as she does so, she squirms down, pushing her butt into my face!"
            $ harmony.sexperience += 1
            scene bg bedroom1
            show reona naked at left4
            show harmony naked at right4
            with fade
            jump purity_choices
        "Choose Reona":
            mike.say "I've got to say, Reona..."
            mike.say "You tasted really good just now."
            mike.say "And I think there's another part of me that wants to sample that flavour!"
            "Reona can't help smiling as I make it plain that I want some more of her."
            "But even as I make the admission, I'm worried that Harmony might be jealous."
            "Even after all of the talk between us about being faithful and devoted to each other..."
            "Reona's the one of them that came to this a lot later."
            "Whereas Harmony's lived most of her life being chaste and pure."
            "But it seems that the result of that is her being made of stronger moral stuff."
            "As Harmony simply nods and does all that she can to help make it happen."
            harmony.say "Here, Reona..."
            harmony.say "Let me help you get into position."
            scene bg black
            show purity threesome reona with dissolve
            "Reona nods and holds out her hands, which Harmony takes gentle hold of."
            "And together they move here and there, until the former is straddling my thighs."
            "That done, the former reaches down and takes an equally gentle hold of my cock."
            "Without needing to be asked, Harmony guides us closer together."
            "And she makes sure that the head of my cock presses against the lips of Reona's pussy."
            "In another times and place, this all could have seemed awkward."
            "It could have felt like Harmony was a third wheel, getting in the way."
            "But somehow it doesn't feel like that at all, in fact it feels totally natural."
            "Harmony is as much a part of this as either Reona or myself."
            "And she's acting as a conduit between the two of us right now."
            "So much so that I can already feel how Reona's starting to loosen up down there."
            "The tip of my cock is sliding this way and that against the lips of her pussy."
            "And that means it's only going to be a matter of time before..."
            show purity threesome reona vaginal closed
            play sexsfx1 slide_in
            reona.say "Oh..."
            reona.say "Oh fuck!"
            mike.say "Whoa..."
            mike.say "Fucking hell!"
            play sexsfx1 slide_in
            "Without warning, it happens - Reona's lips part and she begins to sink down and onto me."
            "And just like that, everything seems to change, to shift and to become so much more urgent."
            "Reona's hands grip me, as if she's afraid of being pulled away before it can happen."
            "At the same time I reach up for her from below, trying to hold onto her for the same reason."
            "And somewhere in the middle of all this, we're also coming together an inch at a time."
            show purity threesome reona opened
            "Reona and I gasp with the passion it's causing us to feel, right until I can go no deeper."
            show purity threesome reona lookmike
            "All the time Harmony is watching with genuine interest, silently urging us on."
            "But when we end up staring into each other's eyes, that seems to be too much for her."
            show purity threesome reona lookreona
            harmony.say "Come on, you two..."
            harmony.say "What are you waiting for?"
            show purity threesome reona lookreona down
            "Putting hand near my dick, she encourages me to begin moving again."
            play sexsfx1 slide_out
            "And almost as soon as I start to rise up, she puts the other one on Reona's butt."
            play sexsfx1 slide_in
            "Which she then pushes down at the same time, encouraging us to get on with it."
            play sexsfx1 slide_out
            pause 1
            play sexsfx1 slide_in
            "And I have to say that Harmony's efforts seem to have the desired effect."
            show purity threesome reona up closed bulge
            play sexsfx1 fuck_calm loop
            "Pretty soon I'm thrusting up and down from below, gaining speed all the time."
            "All while Reona is riding me hard, pushing down from above with all of her weight."
            show purity threesome reona -bulge
            "By now we don't need any encouragement from Harmony to keep things going."
            play sexsfx1 fuck_moderate loop
            "Reona and I are holding onto each other with no intention of letting go."
            show purity threesome reona bulge lookmike
            "And we're riding this thing out until the very end, bouncing up and down on the bed."
            show purity threesome reona -bulge down
            play sexsfx1 fuck_calm loop
            "In fact I can vaguely hear the sound of the frame creaking beneath us."
            "A sound that makes me worry about us breaking it if this goes on much longer!"
            show purity threesome reona bulge opened lookreona
            play sexsfx1 fuck_moderate loop
            reona.say "Aaah..."
            reona.say "I...I can't..."
            reona.say "I can't hold on any longer!"
            show purity threesome reona -bulge closed
            "There's no need for me to say anything in response to that."
            "Because I know exactly what's happening to Reona right now."
            show purity threesome reona bulge
            "I can feel the muscles of her body tensing and her limbs twitching."
            "I know that she's going to cum any moment now."
            show purity threesome reona -bulge
            "And that when she does, she's going to take me with her too!"
            "In the end, it all begins to happen before I can do anything to prepare myself."
            show purity threesome reona bulge ahegao creampie
            play sexsfx1 final_thrust
            "I feel myself kind of stiffen and then push upwards, shooting my load a moment later."
            "And it seems that Reona's unprepared too, as she's soon wriggling and writhing atop me."
            "Luckily for us, Harmony's there to make sure that Reona doesn't fall off."
            "As well as to make sure that she takes everything that I have to give."
            "Ensuring the best chance of there being something to celebrate in a few days time."
            $ reona.sexperience += 1
            scene bg bedroom1
            show reona naked at left4
            show harmony naked at right4
            with fade
            jump purity_choices


    scene bg bedroom1
    show reona naked happy at left4
    show harmony naked happy at right4
    with fade
    "Now that my duty has been done, I feel like I can finally relax."
    "And this means that I hardly hear or feel Reona and Harmony settling down to either side of me."
    "I take their silence as a good sign, as proof of their satisfaction at a job well done on my part."
    "Reaching out with one arm for each of them, the last thing I manage to do is pull them closer to me."
    "Making sure that the three of us are nestled together as we fall into a deep slumber."
    "And as I begin to fall asleep, I'm already wondering what tomorrow is going to bring."
    "The first day of a new part of my life, as one part of a three-way marriage."
    "But even though I don't know what the future has in store for us, I don't feel worried."
    "Because I'm sure there's no challenge out there the three of us can't face, as long as we're together."
    "This is something that I'd been afraid of, that I wouldn't have the stamina for them both."
    "But somehow the opposite proves to be the case, and I know it the moment I'm done the first time."
    "Instead of daunting me, the sight of there being a second girl that needs satisfying energises me."
    "I feel a renewed surge of energy in my limbs, and there's no thought of stopping to rest even for a moment."
    "Something that seems to be obvious to Reona and Harmony as they watch me, surprise written all over their faces as they do so."


    scene purity ending
    harmony.say "I think you should go first, Reona."
    reona.say "Oh no, Harmony..."
    reona.say "You should so be the one to get things started!"
    harmony.say "No, no, no...I insist!"
    reona.say "Erm..."
    reona.say "Harmony, I think we already started it!"
    harmony.say "Oopsie!"
    harmony.say "Isn't that just like us, though?"
    harmony.say "Always trying to be kind and somehow muddling through?"
    reona.say "Yeah, I guess it is."
    reona.say "But I never thought that my life would turn out like this."
    reona.say "I was so sure that I had everything figured out."
    reona.say "That I was the smart one and everyone else was fooling themselves."
    harmony.say "We all have lessons to learn in life, Reona."
    harmony.say "And one of them is to always be humble, as well as honest."
    reona.say "Yeah, Harmony..."
    reona.say "And if it wasn't for [hero.name], it'd never have happened."
    reona.say "I thought he was going to be just another guy."
    reona.say "Like all of the others I used up and spat out before him."
    harmony.say "Oh yes..."
    harmony.say "He does have a way of surprising you, doesn't he?"
    harmony.say "Of confounding your expectations of him as a guy."
    reona.say "You can say that again!"
    reona.say "Man, I went through all the stages of it with that guy."
    reona.say "At first I just thought he was saying that he was too good for me."
    reona.say "But when the anger faded, I realised that I still had feelings for him."
    reona.say "And I had to try and make sense of them somehow."
    harmony.say "Oh my goodness..."
    harmony.say "I remember that time so well, Reona."
    harmony.say "And I feel so bad about the way I treated you at first."
    reona.say "It's so brave of you to own your actions like that, Harmony."
    reona.say "And, of course, I totally forgive you and understand where you were back then."
    reona.say "I had to prove myself to you and [hero.name], to prove I was for real."
    harmony.say "Oh, Reona..."
    harmony.say "We were both being tested, and by a higher power too."
    harmony.say "But we endured all of the trials, overcame the obstacles in our way."
    harmony.say "And look at us now."
    reona.say "You are so right, Harmony."
    reona.say "And how we have been rewarded for our perseverance too!"
    reona.say "We have a beautiful home and a perfect little family."
    if harmony.pregnant and reona.pregnant:
        harmony.say "Damien and Lilith are so much like their father!"
        harmony.say "I just wish that he could be around to spend more time with them."
    elif harmony.pregnant:
        harmony.say "Lilith is so much like her father!"
        harmony.say "I just wish that he could be around to spend more time with her."
    elif reona.pregnant:
        harmony.say "Damien is so much like his father!"
        harmony.say "I just wish that he could be around to spend more time with him."
    else:
        harmony.say "I just wish that he could be around to spend more time with us."
    reona.say "Now, now, Harmony..."
    reona.say "We both know that [hero.name] works very hard to keep us all."
    reona.say "And that our lot is to keep a well-ordered house in return."
    reona.say "It's not our place to question or criticise him."
    harmony.say "Ah..."
    harmony.say "You're right, of course."
    harmony.say "It's just that I do love him so, Reona."
    harmony.say "And my heart years for more time with him!"
    reona.say "Mine does too, Harmony."
    reona.say "But we have to be strong, and to do all we can to support him."
    reona.say "Because his strength comes from the love we provide, remember?"
    harmony.say "I do, I do..."
    harmony.say "And we have so much time ahead of us to do all of that it."
    reona.say "We have the rest of our lives together!"
    reona.say "And won't that be an adventure?"
    harmony.say "Only the greatest adventure in this lifetime!"

    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
