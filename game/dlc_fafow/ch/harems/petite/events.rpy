init python:
    Event(**{
    "name": "petite_harem_event_01",
    "label": "petite_harem_event_01",
    "priority": 500,
    "music": "music/roa_music/innocence.ogg",
    "conditions": [
        PersonTarget("kat",
                     MinStat("love", 100),
                     MinFlag("kiss", 1),
                     MinStat("sexperience", 1),
                     HasRoomTag("pub"),
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        PersonTarget(anna,
                     MinStat("love", 100),
                     MinFlag("kiss", 1),
                     MinStat("sexperience", 1),
                     HasRoomTag("pub"),
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        Or(
            PersonTarget("kat",
                IsPresent(),
                ),
            PersonTarget(anna,
                IsPresent(),
                ),
        ),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            IsFlag("petite_delay", False),
            Not(OnDate()),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "petite_harem_event_02",
    "label": "petite_harem_event_02",
    "priority": 500,
    "music": "music/roa_music/tiny_love.ogg",
    "conditions": [
        PersonTarget("kat",
                     MinStat("love", 100),
                     MinFlag("kiss", 1),
                     MinStat("sexperience", 1),
                     HasRoomTag("park"),
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        PersonTarget(emma,
                     MinStat("love", 100),
                     MinFlag("kiss", 1),
                     MinStat("sexperience", 1),
                     HasRoomTag("park"),
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        Or(
            PersonTarget("kat",
                IsPresent(),
                ),
            PersonTarget(emma,
                IsPresent(),
                ),
        ),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("park"),
            IsFlag("petite_delay", False),
            Not(OnDate()),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "petite_harem_event_03",
    "label": "petite_harem_event_03",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "conditions": [
        IsDone("petite_harem_event_01", "petite_harem_event_02"),
        "Person.are_in_same_room_now([anna, emma, kat], filter_by_room_tag=True)",
        PersonTarget("kat",
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        PersonTarget(anna,
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        PersonTarget(emma,
                     Not(OnDate()),
                     Not(IsHidden()),
                     ),
        Or(
            PersonTarget("kat",
                IsPresent(),
                ),
            PersonTarget(anna,
                IsPresent(),
                ),
            PersonTarget(emma,
                IsPresent(),
                ),
        ),
        HeroTarget(
            IsGender("male"),
            IsFlag("petite_delay", False),
            Not(OnDate()),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "petite_harem_event_04_trigger",
    "label": "petite_harem_event_04_trigger",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "conditions": [
        IsNotDone("petite_harem_event_04"),
        TogetherInHarem('petite', 'anna', 'emma', 'kat'),
        ValidRooms("beach"),
        PersonTarget(anna,
                     Not(OnDate()),
                     Not(IsHidden()),
                     MinStat("love", 150),
                     MinStat("sub", 75),
                     ),
        PersonTarget(emma,
                     Not(OnDate()),
                     Not(IsHidden()),
                     MinStat("love", 150),
                     MinStat("sub", 75),
                     ),
        PersonTarget(kat,
                     Not(OnDate()),
                     Not(IsHidden()),
                     MinStat("love", 150),
                     MinStat("sub", 75),
                     ),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        ],
    "duration": 0,
    "do_once": False,
    "once_day": True,
    })

label petite_harem_event_01:
    scene bg pub with fade
    "I've literally just walked into The Winchester and ordered a pint at the bar."
    "And then I happen to look around at the sound of someone walking in through the door."
    show kat at right with easeinright
    "As soon as I see who it is, I can't help smiling, as it looks like my luck is good."
    "It's Kat, the cute gamer girl that I've been seeing recently."
    "Kat sees me glancing in her direction too, and she instantly mirrors my own smile."
    "Then she hurries over to where I'm standing with an eagerness that's impossible to hide."
    show kat happy at center with ease
    kat.say "[hero.name]!"
    kat.say "I thought you might be in here."
    kat.say "And I was right!"
    show kat normal
    "Kat stands on her tiptoes to plant a kiss on my cheek."
    "But she's still a little to short to reach."
    "Which means that I have to crouch down to make it happen."
    mike.say "Hey, Kat..."
    mike.say "Did you actually come in here on the off chance?"
    mike.say "Just because I might have been in here too?"
    show kat normal blush
    "Kat blushes a little."
    "And for a moment I think she's going to deny it."
    "But then she nods her head and lets out a cute chuckle."
    show kat talkative
    kat.say "Okay, okay..."
    kat.say "That's exactly what I did!"
    show kat surprised
    kat.say "Oh...that makes me look like a stalker, doesn't it?"
    show kat shy -blush
    "I shake my head, keen to dismiss the idea."
    mike.say "Not to me it doesn't, Kat."
    mike.say "I mean to some people, yeah..."
    mike.say "They'd probably think you were a proper psycho."
    mike.say "But I know you better than that!"
    show kat happy at startle
    "Kat laughs again."
    "And this time she adds a gentle punch on the arm."
    show kat smile
    kat.say "Shut up, asshole!"
    kat.say "I'm going to get a drink."
    kat.say "Then we can sit down and chat, okay?"
    show kat normal
    mike.say "Sounds good to me!"
    if kat.is_visibly_pregnant:
        mike.say "But remember to make it non-alcoholic, yeah?"
        "Kat nods, and I notice that she can't help unconsciously cradling her belly."
    mike.say "I'll go grab us a table."
    hide kat with easeoutleft
    "Kat heads to the bar and I go in search of the table I promised her."
    "It doesn't take me long to spot a good one, and so I make straight for it."
    "But just as I put my drink down and go to sit in one of the chairs, I hear a familiar voice."
    anna.say "Hey, [hero.name]!"
    show anna happy with dissolve
    "Normally the sound of Anna's voice is pretty sweet to my ears."
    "Reminding me of how cute and sexy she is."
    "As well as the fact that she can be endearingly ditzy too."
    "But on this occasion, it has the opposite effect."
    "Right now it's filling me with a terrible sense of dread."
    "And that's because of her close proximity to Kat."
    "Something I've been trying to avoid happening, at least when I'm around too."
    "Because I've been juggling the two like a couple of hot little balls recently."
    "Seeing them behind each other's backs and trying to keep it a secret the whole time!"
    mike.say "A...Anna..."
    mike.say "What are you doing here?"
    "I turn to see Anna grinning from ear to ear."
    show anna annoyed
    "But my question seems to upset her."
    "As the smile soon fades from her face."
    show anna worried
    anna.say "Well that's a funny thing to ask a girl."
    anna.say "And here I was thinking that you'd be pleased to see me!"
    anna.say "Now I'm starting to think you'd rather I wasn't here..."
    show anna sad
    mike.say "Erm..."
    mike.say "No, Anna..."
    mike.say "Of course not!"
    mike.say "You just caught me by surprise, that's all."
    "It's an admittedly weak explanation."
    show anna normal
    "But it seems to have the desired effect."
    show anna happy
    "Within mere seconds, Anna's smiling again."
    show anna talkative
    anna.say "Okay, [hero.name]..."
    anna.say "You're forgiven!"
    show anna normal
    "With that she walks straight up to me and puts her arms around my neck."
    "If anything, Anna's actually a little shorter than Kat."
    "But rather than straining to reach up, she pulls me down."
    if anna.is_visibly_pregnant:
        "Something that the weight of her pregnant belly makes easier than normal."
    show anna kiss with fade
    $ anna.flags.kiss += 1
    "And then she plants her lips against mine, kissing me deep and hard."
    "I'm terrified that Kat's going to see us any second."
    "But I can't pull away from Anna, as that'll look seriously suspicious."
    "So I have no choice but to let her have her fill of tongue action."
    "All the time fearing that I'm going to hear Kat freaking out."
    hide anna kiss
    show anna happy
    with fade
    "But luckily for me, Anna's done before that can happen."
    "And we're both sitting down, looking innocent when Kat walks over with her drink."
    show anna stuned
    show kat surprised at left5 with easeinleft
    kat.say "Oh..."
    kat.say "We have company?"
    show kat stuned
    "Anna looks up in surprise as she hears Kat's voice."
    show anna surprised at right4 with ease
    anna.say "Hey there!"
    anna.say "Are you joining us too?"
    show anna stuned
    "Oh dear - it looks like both of them are assuming that they were here first!"
    "I mean, I know that Kat technically was here before Anna."
    "But as neither of them knows the other, I can hardly blame them."
    mike.say "Okay, okay..."
    mike.say "Let me explain..."
    show kat normal
    show anna normal
    mike.say "Anna, this is Kat, a really cool live-streamer I know."
    mike.say "Kat, this is Anna, the super-talented drummer in a rock band."
    mike.say "Anna, I already bumped into Kat at the bar just now."
    mike.say "Kat, Anna spotted me while you were over there and said hi."
    mike.say "There...are we all caught up now?"
    show anna annoyed
    show kat annoyed
    "I look from Anna to Kat a couple of times."
    "And I can see that neither of them is totally happy with what I just said."
    "Which is perfectly understandable, as they're both waiting for me to say more."
    "Specifically to add that I'm in a relationship with them."
    "Thus confirming that the other is just a friend."
    "But as awkward seconds pass it becomes ever more clear that's not going to happen."
    "And so they have no choice but to let the matter drop."
    "But that doesn't mean the danger is passed."
    "Not by a long measure."
    show anna talkative
    show kat normal
    anna.say "So, Kat..."
    anna.say "You just met, [hero.name], yeah?"
    anna.say "Because he never mentioned you before."
    show anna normal
    show kat shocked
    "Kat opens her mouth to reply."
    "But Anna's not letting her get a word in just yet."
    show anna evil
    anna.say "Because the two of us go way back!"
    show kat offended
    "Kat's frowning now, fully aware of what Anna's trying to do."
    "And she seems determined to give as good as she's getting."
    show kat angry
    kat.say "Really, Anna?"
    kat.say "We might have only met recently."
    kat.say "But I already feel like I've known him all my life!"
    show kat defiant
    show anna unpleased
    kat.say "We just clicked that much, you know?"
    if anna.is_visibly_pregnant and kat.is_visibly_pregnant:
        "Both of the girls are still looking to score points."
        "And soon their eyes settle on each other's bellies."
        show kat talkative
        kat.say "Oops!"
        kat.say "Did somebody have a little accident?"
        kat.say "Forget to take the proper precautions?"
        kat.say "Or are you just casual about that kind of thing?"
        show kat defiant
        show anna talkative
        anna.say "Look who's talking!"
        anna.say "Someone got careless, didn't they?"
        anna.say "Did you just forget?"
        anna.say "Or can you not remember who the father is?"
        show anna unpleased
        "Both Anna and Kat look to me to come to their aid."
        "But when I look the other way, they fall back to poking at each other."
        show anna evil
        anna.say "Oh no!"
        anna.say "The father of my child and I are very much together and in love!"
        show kat talkative
        kat.say "Hurmph..."
        kat.say "Well, it's the same for me too!"
    elif anna.is_visibly_pregnant:
        "Still looking to score points, Kat's eyes settle on Anna's belly."
        show kat talkative
        kat.say "Oops!"
        kat.say "Did somebody have a little accident?"
        kat.say "Forget to take the proper precautions?"
        kat.say "Or are you just casual about that kind of thing?"
        show kat defiant
        show anna annoyed
        "Anna's face shows her irritation and annoyance at the question."
        "She looks at me to come to her aid."
        "But when I look the other way, she decides to stand up for herself."
        show anna evil
        anna.say "Oh no!"
        anna.say "The father of my child and I are very much together and in love!"
    elif kat.is_visibly_pregnant:
        "Still looking to score points, Anna's eyes settle on Kat's belly."
        show anna talkative
        anna.say "Oh my god!"
        anna.say "Someone got careless, didn't they?"
        anna.say "Did you just forget?"
        anna.say "Or can you not remember who the father is?"
        show anna normal
        show kat angry
        "Kat's face shows her irritation and annoyance at the question."
        "She looks at me to come to her aid."
        "But when I look the other way, she decides to stand up for herself."
        show kat defiant
        kat.say "Oh no!"
        kat.say "The father of my child and I are very much together and in love!"
        show kat normal
    "The atmosphere is getting more tense and awkward by the second."
    "But much to my relief, the solution presents itself a moment later."
    "Almost as one, Anna and Kat both get up from the table."
    show anna annoyed
    show kat annoyed
    "Anna and Kat" "Well..."
    "Anna and Kat" "I'd better be heading off..."
    show anna angry
    show kat angry
    anna.say "Wait, I said that first!"
    kat.say "No, I think you'll find I did!"
    hide kat with easeoutleft
    hide anna with easeoutright
    "Either way, both of them make their apologies and leave."
    "Which I note entails them leaving from separate doors."
    "That leaves me to sit back and enjoy my drink in peace."
    "Though my head is full of worries about what all of this means."
    "And what's going to happen if one or both of them discovers the truth."
    $ game.flags.petite_delay = TemporaryFlag(True, 1)
    return

label petite_harem_event_02:
    scene bg park with fade
    "Today was just one of those days when I knew that I needed to get away for a while."
    "Not like I needed to book a holiday or check into a hotel, nothing as extreme as that."
    "Just that I had to do something a little different to break things up."
    "Something to give me a chance to relax and unwind."
    "So I chose to come along to the park and spend some time strolling around on my own."
    "It's peaceful, serene, and best of all, nobody's charging me for the privilege."
    "Sure, there are other people here, walking dogs, jogging and the like."
    "But all of them are totally absorbed in what they're doing."
    "So all I have to do is give the occasional nod and smile to anyone that's particularly friendly."
    "I'm getting happily lost in a little world all of my own."
    "Or at least I was, until I hear the sound of someone calling my name!"
    emma.say "[hero.name]..."
    emma.say "Hey, [hero.name]!"
    "I look around, searching for the owner of the voice."
    show emma happy with dissolve
    "And it doesn't take me long to spot Emma hurrying towards me."
    "She waves her hand in the air as she gets closer."
    if emma.is_visibly_pregnant:
        "And even the fact that she's visibly pregnant doesn't seem to slow her down."
    "So I have no choice but to stop and wait for her to catch me up."
    "Don't get me wrong, I don't have any real reason to want to avoid Emma right now."
    "Save for the fact that I was supposed to be grabbing some me time and spending it all alone."
    "But then I guess that we did get it on not too long ago."
    "Which doubtless means that Emma's convinced I would want to spend time with her."
    show emma fear
    emma.say "Phew!"
    emma.say "I...whoa..."
    emma.say "Just...let me...catch my breath here!"
    mike.say "Erm..."
    mike.say "Hey, Emma..."
    mike.say "I was just out for a stroll."
    mike.say "What are you doing here in the park?"
    show emma happy
    "Emma seems to have caught her breath by now."
    "She smiles and shakes her head."
    emma.say "Me too, [hero.name]..."
    emma.say "What a weird coincidence, right?"
    emma.say "It's almost like we were meant to bump into each other."
    show emma normal
    emma.say "So...you want to keep strolling - but with me, yeah?"
    "I have no more than a few moments to turn the thought over in my mind."
    "I mean, I would have liked to keep on walking alone."
    "But if I say that to Emma, then she's bound to take it personally."
    "Which is why I put the idea out of my head and nod."
    mike.say "Of course I do, Emma!"
    mike.say "Strolling with you would be so much better than doing it alone."
    show emma happy
    "Emma seems delighted with my answer."
    "And she doesn't hesitate to take hold of my arm."
    "With that decided, we start to walk in the same direction I was before."
    "Emma does most of the talking, mentioning this and that random thing that occurs to her."
    "But that's fine with me, as I'm not really in the mood for a deep conversation anyway."
    "So I just pay enough attention to know when I should be saying yes and no."
    "That seems to be more than enough to make Emma happy, and we stroll on for a while."
    show emma normal
    "This status of peaceful equilibrium is only challenged when we have to step aside for a moment."
    "Because a group of people on those weird hover-board things comes the other way."
    "There's so many of them that they take up most of the path."
    "So Emma and I step onto the grass for a moment to let them pass."
    "But just as we're about to step back on and resume our walk, I hear another voice calling me."
    kat.say "Hi, [hero.name]..."
    show kat happy at left5 with dissolve
    kat.say "Sorry if we nearly ran you over back there!"
    "Kat looks really pleased to see me as she hurries over."
    if kat.is_visibly_pregnant:
        "Though she does look more than a little precarious on her hover-board."
        "What with also having to cradle her pregnant belly."
    show kat surprised
    kat.say "Oh..."
    kat.say "Who's this?"
    show emma annoyed
    emma.say "Funny you should say that..."
    emma.say "Because I was about to ask the same thing!"
    show emma normal
    show kat normal
    "As one, Emma and Kat stare at me, waiting for an answer."
    "Ah shit...I'm going to have to make this sound good!"
    mike.say "Okay, okay..."
    mike.say "Let me explain..."
    mike.say "Emma, this is Kat, a really cool live-streamer I know."
    mike.say "Kat, this is Emma, an amazing girl I met in a dream."
    show kat shocked
    kat.say "You met her in a DREAM?!?"
    mike.say "Yes, but that's not important right now."
    mike.say "Kat, I already bumped into Emma as I was walking in the park."
    mike.say "Emma, Kat nearly ran us over back there, and now she's here to say sorry."
    mike.say "There...are we all caught up now?"
    show emma annoyed
    show kat annoyed
    "I look from Emma to Kat a couple of times."
    "And I can see that neither of them is totally happy with what I just said."
    "Which is perfectly understandable, as they're both waiting for me to say more."
    "Specifically to add that I'm in a relationship with them."
    "Thus confirming that the other is just a friend."
    "But as awkward seconds pass it becomes ever more clear that's not going to happen."
    "And so they have no choice but to let the matter drop."
    "But that doesn't mean the danger is passed."
    "Not by a long measure."
    show emma normal
    show kat normal
    emma.say "So, Kat..."
    emma.say "You just met, [hero.name], yeah?"
    emma.say "Because he never mentioned you before."
    show kat shocked
    "Kat opens her mouth to reply."
    "But Emma's not letting her get a word in just yet."
    show emma blush
    emma.say "Because the two of us go way back!"
    show kat offended
    "Kat's frowning now, fully aware of what Emma's trying to do."
    "And she seems determined to give as good as she's getting."
    show kat angry
    kat.say "Really, Emma?"
    kat.say "We might have only met recently."
    kat.say "But I already feel like I've known him all my life!"
    show kat defiant
    kat.say "We just clicked that much, you know?"
    if emma.is_visibly_pregnant and kat.is_visibly_pregnant:
        "Both of the girls are still looking to score points."
        "And soon their eyes settle on each other's bellies."
        kat.say "Oops!"
        kat.say "Did somebody have a little accident?"
        kat.say "Forget to take the proper precautions?"
        kat.say "Or are you just casual about that kind of thing?"
        emma.say "Look who's talking!"
        emma.say "You must have been a little careless."
        emma.say "You know, to end up in that state?"
        emma.say "I hope you know who the father is!"
        "Both Emma and Kat look to me to come to their aid."
        "But when I look the other way, they fall back to poking at each other."
        emma.say "Oh no!"
        emma.say "The father of my child and I are very much together and in love!"
        kat.say "Hurmph..."
        kat.say "Well, it's the same for me too!"
    elif emma.is_visibly_pregnant:
        "Still looking to score points, Kat's eyes settle on Emma's belly."
        kat.say "Oops!"
        kat.say "Did somebody have a little accident?"
        kat.say "Forget to take the proper precautions?"
        kat.say "Or are you just casual about that kind of thing?"
        show emma annoyed
        "Emma's face shows her irritation and annoyance at the question."
        "She looks at me to come to her aid."
        "But when I look the other way, she decides to stand up for herself."
        show emma blush
        emma.say "Oh no!"
        emma.say "The father of my child and I are very much together and in love!"
    elif kat.is_visibly_pregnant:
        "Still looking to score points, Emma's eyes settle on Kat's belly."
        emma.say "Oh my!"
        emma.say "You must have been a little careless."
        emma.say "You know, to end up in that state?"
        emma.say "I hope you know who the father is!"
        show kat angry
        "Kat's face shows her irritation and annoyance at the question."
        "She looks at me to come to her aid."
        "But when I look the other way, she decides to stand up for herself."
        show kat defiant
        kat.say "Oh no!"
        kat.say "The father of my child and I are very much together and in love!"
    "The atmosphere is getting more tense and awkward by the second."
    "But much to my relief, the solution presents itself a moment later."
    "Almost as one, Emma and Kat turn to walk in opposite directions."
    show emma annoyed
    show kat annoyed
    "Emma and Kat" "Well..."
    "Emma and Kat" "I'd better be heading off..."
    show emma angry
    show kat angry
    emma.say "Wait, I said that first!"
    kat.say "No, I think you'll find I did!"
    "Neither of them seems to think of asking me to leave with them."
    hide emma with easeoutright
    hide kat with easeoutleft
    "They just stalk off in opposite directions."
    "Which leaves me to stroll off and enjoy my walk in peace."
    "Though my head is full of worries about what all of this means."
    "And what's going to happen if one or both of them discovers the truth."
    $ game.flags.petite_delay = TemporaryFlag(True, 1)
    return

label petite_harem_event_03:
    "I'm walking along, just minding my own business when it happens."
    "Someone literally steps out in front of me and holds up their hand."
    "Maybe if it had been someone taller, I would have seen them in time to stop."
    "But the flash of pink hair I see before it happens tells me that it's probably Anna."
    "And she's one of the shortest people I've ever met!"
    "So when I walk straight into her, she's sent tottering back a good distance."
    show anna close angry
    anna.say "Stop right there you..."
    show anna surprised
    anna.say "Whoa..."
    show anna embarrassed -close
    with vpunch
    mike.say "Urgh..."
    mike.say "Anna, what are you doing?"
    "I see Anna falling backwards in slow-motion."
    "And I just manage to make a grab for her before it's too late."
    if anna.is_visibly_pregnant:
        "All the better on account of her being so heavily pregnant!"
    show anna surprised
    "My hand grasps her wrist, just in time to keep Anna on her feet."
    show anna annoyed
    "But rather than thanking me, Anna slaps my hand away."
    mike.say "Ouch!"
    mike.say "What was that even for?!?"
    show anna angry
    anna.say "Don't give me that silver-tongued treatment!"
    anna.say "Not this time, Mister!"
    "Anna surprised me with her tone, and by advancing on me."
    "She's jabbing a finger in my face the whole time too."
    "Making me back off from her out of the sheer instinct to defend myself."
    show emma angry at mostleft5 with hpunch
    "But then I feel someone else shove me from the side."
    show emma at left
    show anna at right4
    with ease
    "And a moment later, Emma's standing right by Anna!"
    emma.say "And why are you backing off, huh?"
    emma.say "Think you're going to get away this time?"
    emma.say "Well you're wrong!"
    mike.say "Emma?"
    mike.say "Where did you come from?"
    "I'm already staggering to the side from Emma's shove."
    if emma.is_visibly_pregnant:
        "Which was pretty impressive, to say that she's pregnant!"
    show kat angry at mostright5 with hpunch
    "Then I find myself being pushed again from the other side."
    show emma at left5
    show anna at center
    show kat at right5
    with ease
    "This time I have to jump backwards, as Kat closes in on me too!"
    if kat.is_visibly_pregnant:
        "One hand holding her pregnant belly as the other makes a fist that's waved in my face."
    kat.say "That's it, girls..."
    kat.say "Keep him cornered."
    kat.say "Don't let him get away!"
    mike.say "Kat?"
    mike.say "What's all this about?"
    mike.say "Why are the three of you ganging up on me like this?"
    show anna annoyed
    anna.say "Because we know what's been going on, [hero.name]."
    emma.say "We all figured out there was something going on."
    emma.say "So the three of us all confronted each other."
    show kat offended
    kat.say "But when we did, we realised something important."
    kat.say "That none of us actually knew you were seeing the others."
    kat.say "So you were playing all of us off against each other!"
    "I can actually feel the muscles of my ass clenching as they say all of this."
    "Sure, I thought that I was being really clever, screwing three girls at once."
    "But I never really thought about what would happen if they all found out."
    "Maybe I thought that I could handle it if one of them did."
    "Perhaps even two, so long as they didn't get to compare notes."
    "But now the worst case scenario has come to pass."
    "And I'm going to have to pay the price!"
    if Harem.find('anna', name='band'):
        show anna angry
        if Harem.find('sasha', name='band') and Harem.find('kleio', name='band'):
            anna.say "What am I supposed to tell Sasha and Kleio, huh?"
            anna.say "I thought what the four of us had was special?!?"
        if Harem.find('kleio', name='band'):
            anna.say "What am I supposed to tell Kleio, huh?"
            anna.say "I thought what the three of us had was special?!?"
        show emma surprised
        show kat shocked
        "Suddenly Emma and Kat are staring at Anna."
        "And as soon as she realises, Anna clams up."
        if Harem.find('sasha', name='band') and Harem.find('kleio', name='band'):
            emma.say "Who in the hell are Sasha and Kleio?!?"
            kat.say "And what are you three doing sleeping with all of them?!?"
        if Harem.find('kleio', name='band'):
            emma.say "Who in the hell is this Kleio?!?"
            kat.say "And what are you two doing sleeping with all of them?!?"
        show anna embarrassed
        anna.say "Erm..."
        anna.say "Ouch!"
        anna.say "This is kinda awkward!"
        anna.say "Can we like...deal with that one later?"
    elif Harem.find('emma', name='friendly') and Harem.find('samantha', name='friendly'):
        emma.say "What am I supposed to tell Sam, huh?"
        emma.say "I thought what the three of us had was special?!?"
        show anna surprised
        show kat shocked
        "Suddenly Anna and Kat are staring at Emma."
        "And as soon as she realises, Emma clams up."
        anna.say "Who in the hell is this Sam?!?"
        kat.say "And what are you two doing sleeping with her too?!?"
        show emma fear
        emma.say "Erm..."
        emma.say "I really shouldn't have brought that up!"
        emma.say "It kind of complicates things..."
        emma.say "Maybe we could discuss it later?"
    "All I can think to do is clasp my hands together and sink to my knees."
    "Sure, getting down in front of them and begging isn't exactly dignified."
    "But in the heat of the moment, it's he best plan I can come up with!"
    show anna unpleased
    show emma normal
    show kat angry
    mike.say "Anna, Emma, Kat..."
    mike.say "Look, I know what I did was really shitty."
    show anna surprised
    show emma surprised
    show kat surprised
    mike.say "But in the end, can you actually blame me?"
    "I think the three of them had been expecting more grovelling."
    "Not for me to ask them to understand my motivations and empathise."
    show anna angry
    show emma angry
    show kat angry
    anna.say "Why shouldn't we blame you?"
    emma.say "You cheated on all three of us!"
    kat.say "Yeah, you went behind our backs!"
    mike.say "I know that's what it looks like, really I do!"
    show anna surprised
    show emma surprised
    show kat surprised
    mike.say "But the reality is that I'm in love with you."
    mike.say "With all three of you!"
    mike.say "And how could I possibly choose?"
    mike.say "When all three of you are so beautiful and amazing!"
    "Yeah, I know that it sounds ludicrous."
    "But I'm doing the best I can to be honest."
    "Well, and not to make myself look like a total douche!"
    show anna embarrassed
    anna.say "Y...you can't love more than one girl!"
    show emma annoyed
    emma.say "It's not possible!"
    show kat shy blush
    kat.say "You've got to choose just one!"
    "As Kat says this, I see surprise on Anna and Emma's faces."
    show anna angry
    show emma angry
    show kat surprised -blush
    anna.say "Wait...what?!?"
    emma.say "I thought we were here to confront him?"
    anna.say "That's right - then dump him!"
    "Kat looks more than a little worried as she tries to explain herself."
    show kat shy
    kat.say "W...well..."
    kat.say "Why can't one of us keep him?"
    kat.say "If he loves us all so much?"
    "I sense a chance to tip the scales in my favour."
    "So I nod and do the best I can to sound humble."
    show anna unpleased
    show emma normal
    mike.say "That's right..."
    mike.say "I've got enough love for all of you!"
    mike.say "That is...if you want it?"
    if all([person.love >= 120 and person.lesbian >= 10 for person in [anna, emma, kat]]):
        show anna normal
        anna.say "Well...I kinda want it!"
        show emma happy
        emma.say "Choose me, [hero.name]!"
        show kat smile
        kat.say "I want as much of his love as I can get!"
        "All three of them stop dead."
        "As if they're only now hearing what they said."
        show anna blush
        show emma annoyed
        show kat shy blush
        "And they all look embarrassed by it as well."
        mike.say "Wait a minute..."
        mike.say "Two seconds ago you were all tearing into me for sleeping with other women."
        mike.say "Now you're telling me that not one of you can stand to actually dump me?"
        "The girls are still exchanging embarrassed looks."
        "But eventually they manage to start explaining themselves."
        anna.say "I was too mad, [hero.name]!"
        anna.say "But not mad enough to leave you."
        show emma normal
        emma.say "I guess I saw red, you know?"
        emma.say "I really didn't think it through."
        show kat afraid
        kat.say "This is all pretty complicated."
        kat.say "Normally my relationships are far more simple!"
        show anna normal
        anna.say "So..."
        anna.say "Are you going to let us stay?"
        mike.say "Are you kidding?!?"
        mike.say "Of course I am!"
        show anna happy
        show emma happy
        show kat happy
        "As one, Anna, Emma and Kat throw their arms around me."
        "They seem genuinely pleased that I said yes."
        "And that's enough to silence all of their questions."
        "But as for me, I'm already miles ahead of them."
        "Thinking of the possibilities that this turn of events could offer."
        $ Harem.join_by_name("petite", "anna", "emma", "kat")
    elif all([person.love >= 120 and person.lesbian >= 10 for person in [anna, emma]]):
        show kat shocked
        show anna normal
        anna.say "Well...I kinda want it!"
        show emma happy
        emma.say "Choose me, [hero.name]!"
        "Kat turns to stare at Anna and Emma."
        show anna surprised
        show emma surprised
        show kat offended
        kat.say "Are you even for real?!?"
        "Anna and Emma look intimidated at first."
        "But then they both meet my eye."
        show anna blush
        show emma normal
        "And I see their moods change."
        anna.say "I meant what I said."
        emma.say "And so did I."
        "Then they over to where I'm standing and take hold of my hands."
        show kat angry
        "Kat shakes her head in obvious disbelief."
        kat.say "You're out of my life for good!"
        hide kat with dissolve
        $ kat.set_gone_forever()
        "With that, she turns and walks away."
        "But I feel Anna and Emma squeeze my hands as she does so."
        "And I've never been more grateful for them than I am right now."
        $ Harem.join_by_name("petite", "anna", "emma")
    elif all([person.love >= 120 and person.lesbian >= 10 for person in [anna, kat]]):
        show emma surprised
        show anna normal
        anna.say "Well...I kinda want it!"
        show kat smile
        kat.say "I want as much if his love as I can get!"
        "Emma turns to stare at Anna and Kat."
        show anna surprised
        show kat surprised
        show emma angry
        emma.say "I can't believe what I'm hearing!"
        "Anna and Kat look intimidated at first."
        show anna blush
        show kat sadsmile blush
        "But then they both meet my eye."
        "And I see their moods change."
        anna.say "I meant what I said."
        kat.say "And so did I."
        "Then they over to where I'm standing and take hold of my hands."
        "Emma shakes her head in obvious disbelief."
        emma.say "Well you won't be seeing me again."
        hide emma with dissolve
        $ emma.set_gone_forever()
        "With that, she turns and walks away."
        "But I feel Anna and Kat squeeze my hands as she does so."
        "And I've never been more grateful for them than I am right now."
        $ Harem.join_by_name("petite", "anna", "kat")
    elif all([person.love >= 120 and person.lesbian >= 10 for person in [emma, kat]]):
        show anna surprised
        show emma happy
        emma.say "Choose me, [hero.name]!"
        show kat smile
        kat.say "I want as much if his love as I can get!"
        "Anna turns to stare at Emma and Kat."
        show emma surprised
        show kat surprised
        show anna angry
        anna.say "What in the hell?"
        "Emma and Kat look intimidated at first."
        "But then they both meet my eye."
        show emma normal
        show kat sadsmile blush
        "And I see their moods change."
        emma.say "I meant what I said."
        kat.say "And so did I."
        "Then they over to where I'm standing and take hold of my hands."
        "Anna shakes her head in obvious disbelief."
        anna.say "You've really blown it this time, [hero.name]."
        hide anna with dissolve
        $ anna.set_gone_forever()
        "With that, she turns and walks away."
        "But I feel Emma and Kat squeeze my hands as she does so."
        "And I've never been more grateful for them than I am right now."
        $ Harem.join_by_name("petite", "emma", "kat")
    elif anna.love >= 120 and anna.lesbian >= 10:
        show emma surprised
        show kat shocked
        show anna normal
        anna.say "Well...I kinda want it!"
        "As one, Emma and Kat turn to stare at Anna."
        show emma angry
        show kat offended
        show anna surprised
        emma.say "I can't believe what I'm hearing!"
        kat.say "Are you even for real?!?"
        "Anna looks intimidated at first."
        "But then she meets my eye."
        show anna blush
        "And I see her mood change."
        anna.say "I meant what I said."
        "Then she walks over to where I'm standing and takes hold of my hand."
        show kat angry
        "Emma and Kat shake their heads in obvious disbelief."
        emma.say "Well you won't be seeing me again."
        kat.say "You're out of my life for good!"
        hide emma
        hide kat
        with dissolve
        $ emma.set_gone_forever()
        $ kat.set_gone_forever()
        "With that, they both turn and walk away."
        "But I feel Anna squeeze my hand as they do so."
        "And I've never been more grateful for her than I am right now."
        $ Harem.join_by_name("petite", "anna")
    elif emma.love >= 120 and emma.lesbian >= 10:
        show anna surprised
        show kat shocked
        show emma happy
        emma.say "Choose me, [hero.name]!"
        "As one, Anna and Kat turn to stare at Emma."
        show anna angry
        show kat offended
        show emma surprised
        anna.say "What in the hell?"
        kat.say "Are you even for real?!?"
        "Emma looks intimidated at first."
        "But then she meets my eye."
        show emma normal
        "And I see her mood change."
        emma.say "I meant what I said."
        "Then she walks over to where I'm standing and takes hold of my hand."
        show kat angry
        "Anna and Kat shake their heads in obvious disbelief."
        anna.say "You've really blown it this time, [hero.name]."
        kat.say "You're out of my life for good!"
        hide anna
        hide kat
        with dissolve
        $ anna.set_gone_forever()
        $ kat.set_gone_forever()
        "With that, they both turn and walk away."
        "But I feel Emma squeeze my hand as they do so."
        "And I've never been more grateful for her than I am right now."
        $ Harem.join_by_name("petite", "emma")
    elif kat.love >= 120 and kat.lesbian >= 10:
        show anna surprised
        show emma surprised
        show kat smile
        kat.say "I want as much if his love as I can get!"
        "As one, Anna and Emma turn to stare at Kat."
        show anna angry
        show emma angry
        anna.say "What in the hell?"
        emma.say "I can't believe what I'm hearing!"
        "Kat looks intimidated at first."
        "But then she meets my eye."
        show kat sadsmile blush
        "And I see her mood change."
        kat.say "I meant what I said."
        "Then she walks over to where I'm standing and takes hold of my hand."
        "Anna and Emma shake their heads in obvious disbelief."
        anna.say "You've really blown it this time, [hero.name]."
        emma.say "Well you won't be seeing me again."
        hide anna
        hide emma
        with dissolve
        $ anna.set_gone_forever()
        $ emma.set_gone_forever()
        "With that, they both turn and walk away."
        "But I feel Kat squeeze my hand as they do so."
        "And I've never been more grateful for her than I am right now."
        $ Harem.join_by_name("petite", "kat")
    else:
        show anna angry
        show emma angry
        show kat angry
        anna.say "What in the hell?"
        emma.say "I can't believe what I'm hearing!"
        kat.say "Are you even for real?!?"
        "I do the best I can to get a word in."
        "But the girls cut me off before I can even speak."
        anna.say "You've really blown it this time, [hero.name]."
        emma.say "Well you won't be seeing me again."
        kat.say "You're out of my life for good!"
        hide anna
        hide emma
        hide kat
        with dissolve
        $ anna.set_gone_forever()
        $ emma.set_gone_forever()
        $ kat.set_gone_forever()
        "With that, they all turn and walk away."
        "Leaving me well and truly on my own."
    return

label petite_harem_event_04_trigger:
    $ hero.calendar.add(game.days_played + 1, HaremAppointment((12, 17), "petite", ["anna", "emma", "kat"], "petite_harem_event_04", name="Meet Anna, Emma and Kat at the beach", fail_label="petite_harem_event_04_missed"))
    return

label petite_harem_event_04_missed:
    "Shit I missed my date with Anna, Emma and Kat."
    $ anna.love -= 5
    $ emma.love -= 5
    $ kat.love -= 5
    $ DONE.pop("petite_harem_event_04_trigger")
    return

label petite_harem_event_04(appointment=None):
    $ DONE['petite_harem_event_04'] = game.days_played
    $ renpy.dynamic(anna_score=0, emma_score=0, kat_score=0)
    scene bg map with fade
    "I've been looking forward to today ever since I convinced the girls it'd be a great idea."
    "So with the sun shining in the sky, we've filled the car with towels, shades and a cooler full of snacks."
    play sound car_door
    pause 0.4
    play sound car_door
    pause 0.2
    play sound car_door
    pause 0.3
    play sound car_door
    queue sound car_ignition
    "The Anna, Emma and Kat all jump into the car with me, and I drive the short distance to the beach."
    "Everyone's chatting and laughing the entire journey there, suggesting stuff we should do on the sand."
    "So much so that I almost miss the entrance to the carpark as we arrive."
    mike.say "Oops..."
    mike.say "Looks like we're here, guys!"
    kat.say "There's a spot right there, [hero.name]!"
    emma.say "I'll get the parking fee - I have the app they use in this parking lot."
    anna.say "Ooh...looks pretty quiet in there..."
    anna.say "We must have got here nice and early!"
    scene bg beach at center, zoomAt(2.25, (0, 1175)) with fade
    show anna a swimsuit at center, zoomAt(1.0, (940, 720))
    show emma swimsuit at center, zoomAt(1.0, (640, 720))
    show kat swimsuit at center, zoomAt(1.0, (340, 720))
    with easeinright
    "Everyone hurries around, doing their part to get us in a spot and the parking fee paid."
    "Then we pile out of the car and I open the trunk, letting the girls start grabbing stuff."
    "Quick as a flash, Emma and Kat have things in their hands."
    show emma swimsuit at center, zoomAt(1.0, (540, 720))
    show kat swimsuit at center, zoomAt(1.0, (240, 720))
    with ease
    "And the next thing I know, they're turning to walk down to the beach itself."
    show anna a swimsuit at flip, center, zoomAt(1.25, (1280, 880)) with fade
    "But a quick glance shows me that Anna's still rummaging in the back of the car."
    "In fact, she's almost half buried in there."
    show anna a at center, zoomAt(1.0, (1280, 880)), startle
    "Her ass wiggling in the air as she tries to pull something out."
    show kat talkative
    kat.say "Come on, [hero.name]…"
    kat.say "What's with the hold-up?"
    show kat normal
    show emma talkative
    emma.say "Yeah..."
    emma.say "Are you coming or what?"
    hide kat
    hide emma
    with easeoutleft
    "I look towards them and then back at Anna."
    mike.say "I think that..."
    mike.say "Anna's kind of stuck, maybe..."
    "I see Kat and Emma holding a hand to their ears and shaking their heads."
    "Like they can't really hear what I'm saying to them."
    "But they're also motioning for me to join them at the same time."
    "Though I can see that Anna's feet are now well and truly off the ground."
    "Like she's actually starting to burrow into the contents of the trunk!"
    anna.say "Hey..."
    anna.say "Hey, guys..."
    anna.say "I could use a hand here?!?"
    menu:
        "Help Anna":
            "Part of me really wants to run after Emma and Kat."
            "I've waited so long to see the girls in their swimming costumes."
            "It's almost painful to think of one more obstacle being put in my path."
            "But then I take a look at Anna's legs, flailing in the air."
            "And I know what I have to do."
            "So I give Emma and Kat a wave."
            mike.say "Urgh..."
            mike.say "I'll catch you up in a minute, okay?"
            mike.say "Anna needs a hand."
            "With that, I turn my attention to helping Anna."
            "Which literally involves me grabbing her at the waist with both hands."
            show anna at center, zoomAt(1.0, (1280, 880)), hshake
            "Then I do the best I can to literally pull her out of the trunk."
            anna.say "Whoa..."
            anna.say "Wha..."
            anna.say "Whoo..."
            show anna a swimsuit surprised at flip, center, traveling(1.5, 0.2, (740, 1040))
            with hpunch
            "All of a sudden, Anna pops out of the trunk."
            "The momentum sends me staggering backwards and her slamming into me."
            "Which means that we end up in an awkward tangle of limbs."
            "Anna looks dazed at first, clinging onto me to keep herself upright."
            "But when she regains her senses, she seems more than a little embarrassed."
            anna.say "Oh..."
            anna.say "Oopsie!"
            show anna a normal at flip, center, traveling(1.25, 0.2, (740, 880))
            "Anna takes a step backwards, letting go of me and straightening herself up."
            show anna happy
            anna.say "Thanks for helping me out there, [hero.name]..."
            anna.say "I was kinda stuck!"
            show anna normal
            mike.say "No problem, Anna..."
            mike.say "Let's grab the stuff we need and catch up to the others, okay?"
            "Anna seems to snap out of if as soon as I say this."
            show anna a normal at flip, center, traveling(1.25, 0.3, (1140, 880))
            "She nods and starts to grab things from the trunk."
            "And I do the same, only stopping to close it and lock the car."
            hide anna with easeoutleft
            "Then we hurry down the path to the beach."
            scene bg beach
            show emma swimsuit at center
            show kat swimsuit at left
            with fade
            pause 0.3
            show anna b swimsuit at right with easeinright
            "By the time we catch up to them, Emma and Kat have picked out a spot."
            "And they're already spreading out towels on the warm sand."
            show emma talkative
            emma.say "You guys took your time!"
            show emma normal
            show kat talkative
            kat.say "We were starting to wonder what you were up to!"
            show kat normal
            "Anna ignores the implications of the last comment."
            "Instead planting her balled fists on her thighs."
            show anna evil
            anna.say "[hero.name] was helping me out in my moment of need, like a proper gentleman."
            show anna angry
            anna.say "Not like you jerks!"
            show anna unpleased
            "I can't help smiling as Emma and Kat look a little ashamed of themselves."
            show anna normal
            "But Anna seems to want to let the matter drop after that."
            "So it's soon forgotten."
            $ anna_score += 1
        "Quickly follow Emma and Kat":
            "Part of me knows that I really should stay and help Anna out."
            "But I've been waiting to see the girls in their swimming costumes for so long."
            "And it's just takes me a matter of seconds to pull out my keys and toss them into the trunk."
            "Then I pick up just enough stuff to fill my hands yet let me move at a sprint."
            mike.say "Hey, Anna..."
            mike.say "You okay to lock up the car when you're done?"
            anna.say "Huh..."
            anna.say "Wha..."
            anna.say "Who said that?!?"
            scene bg beach
            show emma swimsuit at right4
            show kat swimsuit at left4
            with fade
            "I turn my back on the car and hurry off down the path."
            "My haste means that I catch up to Emma and Kat pretty quickly."
            "Then we stroll down to the beach together."
            "It's only when we make it down to the sand that anyone seems to notice Anna's absence."
            show emma surprised
            show kat stuned
            "Emma looks around as we're picking out a spot, her expression becoming a little confused."
            emma.say "Where's Anna?"
            emma.say "I thought she was with you?"
            show emma annoyed
            mike.say "Erm..."
            mike.say "No..."
            mike.say "She was still getting stuff out of the car."
            mike.say "But she should be along any minute now."
            "As if on cue, I hear the sound of huffing and puffing approaching us."
            "And a moment later, Anna appears on the path."
            "She's almost hidden under the pile of stuff that she's carrying."
            show anna a swimsuit sad at right
            show emma swimsuit at center
            show kat swimsuit at left
            with hpunch
            "All three of us rush over to take some of her burden."
            "And once she's been relieved of it, Anna slumps down onto the sand."
            show anna worried
            anna.say "Oh man..."
            anna.say "I can see spots in front of my eyes..."
            anna.say "Why didn't you help me, [hero.name]?!?"
            show anna sad
            "I can feel everyone staring at me."
            "And so I do the best I can to explain myself."
            "Which unfortunately means shrugging and letting out a nervous laugh."
            mike.say "Ah...ha, ha..."
            mike.say "I thought you could handle it, Anna..."
            mike.say "Like, it'd be sexist if I tried to help you out too much?"
            "Anna narrows her eyes, glowering at me as she catches her breath."
            "Then she turns her head and looks away, leaving me to sink into a pit of guilt."
            $ anna_score -= 1
    scene bg beach
    show anna a swimsuit at right
    show emma swimsuit at center
    show kat swimsuit at left
    with fade
    "Now that everyone's down on the beach, we're really settling into our spot."
    "Emma and Kat really picked a good one too, not too exposed and not too shady."
    "So long as the weather stays good, we should be set for the rest of the day."
    mike.say "So..."
    mike.say "What's the plan?"
    mike.say "Are we just going to be soaking up the rays, or what?"
    show anna stuned
    show emma surprised
    "I'm looking at Anna and Emma as I say all of this."
    "But I'm kind of puzzled by the looks on their faces."
    "Because they seem to be looking behind me."
    "And they're smiling too, which is very suspicious."
    scene bg black
    show beach_volleyball_bg_04
    "I can't resist the urge to turn my head around."
    show beach_volleyball_ball_front_03 at center, zoomAt(1.0, (720, 650))
    show beach_volleyball_ball_front_03 at center, traveling(3.5, 0.15, (1420, 2250))
    play sound punch_hard
    pause 0.1
    with hpunch
    pause 0.2
    scene bg black
    "But as soon as I do so, something hits me square in the face."
    mike.say "Aaargh!"
    scene bg beach with vpunch
    "I collapse onto my back, clutching my nose."
    "But then I realise that there's really no pain, just surprise."
    "And I also see Kat standing over me, a hand placed over her mouth."
    show kat swimsuit whining with dissolve
    kat.say "Oops!"
    kat.say "Sorry, [hero.name]..."
    kat.say "I was trying to bounce the volleyball off the back of your head."
    kat.say "You weren't supposed to turn around like that!"
    show kat sad
    "I can't help frowning at Kat as she explains herself."
    mike.say "Yeah..."
    mike.say "My bad, I guess!"
    mike.say "So I take it you guys want a game of volleyball?"
    show kat sadsmile
    anna.say "I could play a couple!"
    show emma swimsuit happy at left with easeinleft
    emma.say "Yeah..."
    emma.say "That sounds like fun."
    show emma normal
    show anna swimsuit normal at right with easeinright
    "Everyone gets to their feet, and we start setting up the net."
    show kat talkative
    kat.say "Anna and Emma against me and [hero.name], okay?"
    show kat normal
    show anna happy
    anna.say "Sure."
    show anna normal
    show emma happy
    emma.say "Okay."
    show emma normal
    mike.say "Fine by me."
    scene bg black
    show beach_volleyball_bg_04
    show beach_volleyball_back_mc_04_mikemc at center, flip
    show beach_volleyball_back_mc_04_normal_mikemc at center, flip
    show beach_volleyball_back_kat
    show beach_volleyball_swimsuit_kat
    show beach_volleyball_net_04 at center, flip
    show beach_volleyball_ball_front_03 at center, zoomAt(1.0, (720, 650))
    show beach_volleyball_front_anna at flip, center, zoomAt(1.0, (340, 720))
    show beach_volleyball_swimsuit_anna at flip, center, zoomAt(1.0, (340, 720))
    show beach_volleyball_front_emma at flip, center, zoomAt(1.0, (540, 820))
    show beach_volleyball_swimsuit_emma at flip, center, zoomAt(1.0, (540, 820))
    with fade
    "Soon enough, Kat and I are stood on one side of the net, Anna and Emma on the other."
    "Anna throws the ball in the air and starts the game."
    "And then we're into it!"
    menu:
        "Play for fun":
            "I'm not going to lie, I can be as competitive as any guy."
            "And I know full well that Anna and Emma aren't exactly professional athletes too."
            "Almost instantly I can see the opportunity to obliterate them."
            "But then I remember that I'm here on a date with three girls."
            "The whole point of the day is to relax and have some fun together."
            "So I deliberately ignore my urge to win, in favour of playing for laughs."
            "Sure, it's hard and it can get frustrating at times."
            "But I just tell myself that it's worth the effort."
            "Plus the smiles and laughter coming from the girls starts to distract me."
            "And soon enough I'm enjoying the chance to watch them moving as we play."
            "So instead of being an asshole and pushing to win, I get to enjoy myself instead."
            "All the same, we're neck and neck until the very end of the game."
            kat.say "[hero.name]..."
            kat.say "Get the ball!"
            "I leap forwards, launching the ball back over the net."
            emma.say "Oh no..."
            emma.say "I can't..."
            anna.say "No worries, Emma..."
            anna.say "Leave it to me!"
            "At the very last moment possible, Anna leaps into the air."
            "I swear she moves in slow-motion as she strikes the ball."
            "Then time speeds up as it flies over the net again."
            "Kat and I have no chance of returning it, and that's game over."
            emma.say "Anna, you did it!"
            anna.say "Yeah, we won!"
            "While they celebrate, Kat walks over and pats me on the shoulder."
            kat.say "Don't worry, we'll beat them next time!"
            $ anna_score += 1
            $ emma_score += 1
            $ kat_score += 1
        "Show them of much of a winner you are!":
            "I know that we're just playing a casual game on the beach."
            "But that doesn't change the fact that I'm going to play to win."
            "This is just another chance to assert my dominance, to show I'm the alpha male around here."
            "So from the moment the ball comes in my direction, I'm totally in the zone."
            "I don't hesitate to pummel it back towards Anna and Emma."
            "Often making them squeal and dart aside to avoid being hit."
            "And I'm sure to make Kat aware of just what she needs to be doing as well."
            mike.say "Kat..."
            mike.say "Wake up..."
            mike.say "You should have got to that one!"
            mike.say "Try harder next time, yeah?"
            "As soon as I sense victory is within reach, I go for it."
            "I leap forwards, launching the ball back over the net."
            emma.say "Oh no..."
            emma.say "I can't..."
            anna.say "No worries, Emma..."
            anna.say "Leave it to me!"
            "At the very last moment possible, Anna leaps into the air."
            "I swear she moves in slow-motion as she reaches for the ball."
            "But there's no way she can reach it, and Anna misses badly."
            "Time seems to speed up again as she lands face-first in the sand."
            mike.say "YES!"
            mike.say "WE WON!"
            "I turn around, expecting Kat to congratulate me."
            "But instead I see her walking away, shaking her head at the same time."
            kat.say "Well done, [hero.name]..."
            kat.say "Way to ruin a fun game!"
            $ anna_score -= 1
            $ emma_score -= 1
            $ kat_score -= 1
    scene bg beach
    show anna a swimsuit
    with fade
    "I look up to see Anna staring longingly at the shore."
    "And it's no mystery why she's so enraptured by the sight."
    "The waves are breaking out there, creating beautiful white surf."
    mike.say "You want to go have some fun in the sea, Anna?"
    "The question seems to be exactly what Anna wanted to hear."
    show anna a talkative
    anna.say "You want to do that, [hero.name]?"
    anna.say "Because I'd love to!"
    show anna b normal
    "Anna turns to Kat and Emma, waving for their attention."
    show anna b talkative
    anna.say "You guys want to come play around in the water too?"
    hide anna
    show kat swimsuit at left
    show emma swimsuit at right
    with fade
    "Kat begins to nod almost instantly, eager to get in on the act."
    show kat talkative
    kat.say "You know I do!"
    show kat normal
    "But Emma looks a little flustered by the notion."
    show emma whining
    emma.say "Can't you wait a couple of minutes?"
    emma.say "I need to put on a higher factor sun screen first."
    emma.say "Otherwise I'll burn to a crisp out there!"
    hide kat with easeoutleft
    pause 0.3
    hide emma
    show anna a swimsuit at left
    with fade
    pause 0.3
    show kat swimsuit at right with easeinright
    "Anna and Kat don't seem to have much sympathy for Emma's predicament."
    "Because they both leap up and begin heading for the water."
    show anna talkative
    anna.say "Whatever, Emma..."
    anna.say "You can catch us up."
    show anna normal
    show kat talkative
    kat.say "See you in there, Emma..."
    kat.say "You coming, [hero.name]?"
    show kat normal
    "I look towards Anna and Kat as they call for me to join them."
    hide anna
    hide kat
    with easeoutleft
    pause 0.3
    show emma swimsuit blank with fade
    "Then I look back at Emma, desperately squeezing sun screen onto her hands."
    menu:
        "Help Emma":
            "I can feel the pull of the water even as I'm standing there."
            "And a quick look in that direction makes things harder still."
            "Anna and Kat are already in there, leaping around and laughing."
            "Two of the hottest girls imaginable, splashing each other in their swimming costumes!"
            "But then I look back at Emma, watching as she begins rubbing the sun screen into her skin."
            mike.say "Hey, Emma..."
            mike.say "Let me help you with that, yeah?"
            scene bg black
            show beach cream emma
            with fade
            "Emma smiles at me as I kneel down beside her."
            emma.say "Would you?"
            emma.say "It'd really help speed things up."
            "I nod, letting her know that it's no big deal."
            "And Emma obligingly squeezes a generous amount into the palm of my hand."
            "Then I start working it into her shoulders and back."
            "All the time I'm doing the best I can to make it look professional."
            "But the truth is that I'm loving every moment that it takes me!"
            "Sure, I could be playing around in the water with Anna and Kat right now."
            "But this pretty much counts as a massage session with Emma!"
            "I'm getting to rub my hands over every inch of her body."
            "And she's thanking me for the effort!"
            "The only problem is that with two of us at it, the job's soon done."
            emma.say "Thanks so much, [hero.name]..."
            emma.say "Now let's go catch them up, okay?"
            scene bg beach with fade
            pause 0.3
            show emma swimsuit at center, zoomAt(1.5, (640, 1040)) with easeinbottom
            "Emma stands up and takes hold of my hand."
            "But as she does so, the other one reaches out."
            "And for just a few brief seconds, she strokes the front of my shorts."
            "Which obviously lets her know that I'm totally hard from what we just did."
            show emma blush
            "Emma doesn't say a word, but she gives me a knowing smile."
            "Letting me know that she's onto me, and that she's not disapproving either!"
            scene bg black
            show playing_water_bg_01_beach
            show playing_water_npc_anna at center, zoomAt(1.0, (840, 720))
            show playing_water_outfits_anna_swimsuit at center, zoomAt(1.0, (840, 720))
            show playing_water_arms_03_anna at center, zoomAt(1.0, (840, 720))
            show playing_water_splash_02
            show playing_water_npc_kat
            show playing_water_outfits_kat_swimsuit
            show playing_water_npc_emma at flip, center, zoomAt(1.0, (-230, 720))
            show playing_water_outfits_emma_swimsuit at flip, center, zoomAt(1.0, (-230, 720))
            with fade
            "All of which means I'm still hard all the time we're playing in the water too."
            $ emma_score += 1
        "Quickly join Anna and Kat":
            "I kind of want to stop and watch Emma rub the stuff into her skin."
            "Because the sight of that would be quite something to behold."
            "But then I take another glance in the opposite direction."
            "And I'm almost struck dumb by the sight that I see in the water."
            scene bg black
            show playing_water_bg_01_beach
            show playing_water_npc_anna at center, zoomAt(1.0, (840, 720))
            show playing_water_outfits_anna_swimsuit at center, zoomAt(1.0, (840, 720))
            show playing_water_arms_03_anna at center, zoomAt(1.0, (840, 720))
            show playing_water_splash_02
            show playing_water_npc_kat
            show playing_water_outfits_kat_swimsuit
            with fade
            "Anna and Kat are already in there, leaping around and laughing."
            "Two of the hottest girls imaginable, splashing each other in their swimming costumes!"
            "I don't even bother to look back at Emma."
            "Instead I make my excuses even as I start to move."
            mike.say "Erm..."
            mike.say "Yeah..."
            mike.say "So I'll..."
            mike.say "I'll see you out there, okay?"
            "I think I hear Emma say something as I begin to run towards the water."
            "But whatever it is, the words are drowned out by Anna and Kat's cries of delight."
            "Which only get louder as I wade out to them and get involved in the action too."
            "All three of us are splashing and shouting, having the time out our lives."
            "So we almost fail to notice when Emma actually makes it out to us."
            emma.say "Phew..."
            emma.say "Finally made it!"
            show playing_water_npc_emma at flip, center, zoomAt(1.0, (-230, 720))
            show playing_water_outfits_emma_swimsuit at flip, center, zoomAt(1.0, (-230, 720))
            with fade
            "Emma reaches down and makes an effort to splash us all."
            "But by then the moment has kind of passed."
            "And the attempt to keep it going falls flat."
            mike.say "Erm..."
            mike.say "Great, Emma..."
            mike.say "But we were just thinking of getting out of the water, yeah?"
            anna.say "But you can stay if you like."
            kat.say "Yeah..."
            kat.say "The waves are still fun, I guess!"
            "Emma keeps quiet, obviously embarrassed at having arrived too late."
            "And the rest of us do the best we can to ignore the awkwardness of the situation."
            "Everyone shuffling back onto the sand, trying not to make eye-contact."
            $ emma_score -= 1
    "The water is amazing, even more so because I'm in it with Anna, Emma and Kat."
    "But it doesn't take long for the sun to get involved in our trying to have some fun."
    anna.say "Ouch!"
    anna.say "Where'd I put my sunglasses?!?"
    scene bg black
    show playing_water_bg_01_beach
    show anna swimsuit sad at center, zoomAt (1.0, (840, 720))
    with fade
    "We all turn around to see what's wrong with Anna."
    show emma upset swimsuit at center, zoomAt (1.25, (240, 880))
    "But Emma's the closest, and she soon reacts in the same way."
    show emma whining
    emma.say "Whoa..."
    emma.say "The sunlight..."
    show emma upset
    show kat whining swimsuit at center, zoomAt (1.15, (540, 780))
    kat.say "Right..."
    kat.say "It's bouncing off the water!"
    show kat sad
    "I can't help frowning as the three of them are wincing and shielding their eyes."
    mike.say "Huh?"
    mike.say "I don't know what you guys are even talking about!"
    show anna unpleased at center, traveling(1.5, 0.3, (980, 1040))
    show emma upset at center, traveling(1.5, 0.3, (300, 1040))
    show kat upset at center, traveling(1.5, 0.3, (640, 1040))
    "Mere seconds after I've said the words, I find myself surrounded."
    "Anna, Emma and Kat are all glaring up at me from below."
    show anna angry
    anna.say "Are you calling me a liar?"
    show anna unpleased
    show emma angry
    emma.say "You can't see it because you're so tall!"
    show emma upset
    show kat angry
    kat.say "You see?"
    kat.say "He's prejudiced against short people!"
    show kat upset
    "I hold my hands up and take a couple of steps back."
    mike.say "Calm down, guys!"
    mike.say "It's no big deal!"
    show anna angry
    anna.say "'Big deal'!"
    anna.say "That is SO typical of a tall person!"
    show anna unpleased
    show emma angry
    emma.say "Come on, girls..."
    emma.say "Let's get out of the sun."
    show emma upset
    show kat angry
    kat.say "Yeah, we can go get ice-cream to cool down."
    kat.say "And I suppose you can come too, [hero.name]."
    kat.say "But no more anti-short language from you!"
    show kat upset
    menu:
        "Go with them":
            "The idea of an ice-cream suddenly sounds like the best thing ever."
            "Especially when Anna, Emma and Kat are all getting one too."
            mike.say "You know what..."
            mike.say "That sounds great."
            hide anna
            hide emma
            hide kat
            with easeoutright
            "Kat leads the way back to the beach, with Anna and Emma in front of her."
            "I have to confess that I hang back a little, admiring the view."
            "But I don't get away with that for long."
            scene bg beach
            show anna a swimsuit at flip, center, zoomAt(1.0, (980, 720))
            with fade
            "Anna happens to glance back and catch me checking her out."
            show anna happy
            anna.say "Hey!"
            anna.say "He's ogling our asses!"
            hide anna with easeoutright
            "With a giggle, Anna starts running the last few metres to the sand."
            "Emma and Kat take it in the same spirit, beginning to sprint too."
            "Which leaves me chasing after them, making sure that I don't catch up too soon."
            "The girls lead me straight to the ice-cream stand."
            show beach icecream emma
            show beach_icecream_girl_kat at center, zoomAt(1.0, (420, 720))
            show beach_icecream_swimsuit_kat at center, zoomAt(1.0, (420, 720))
            show beach_icecream_ice_kat at center, zoomAt(1.0, (420, 720))
            show beach_icecream_girl_anna at center, zoomAt(1.0, (140, 720))
            show beach_icecream_swimsuit_anna at center, zoomAt(1.0, (140, 720))
            with fade
            "And we're soon each holding one of our own choosing."
            "Then we take a leisurely stroll back to our spot on the beach."
            "Where I have the immense pleasure of watching them eat their ice-creams."
            "Which is something that I don't think I'll ever forget."
            "In fact I kind of feel like I could use a second dip in the cold sea after wards."
            "Because it leaves me feeling kind of hot and bothered."
            $ anna.love += 1
            $ emma.love += 1
            $ kat.love += 1
            scene bg beach with fade
            "By the time we've finished eating our ice-creams, it's getting later in the day."
        "Stay in the sea a little longer":
            "I shake my head, shading my eyes from the sun as I do so."
            mike.say "Nah..."
            mike.say "I'm good."
            mike.say "I'll catch up to you guys later, back at our spot."
            "I wave with my other hand, making it clear I'm not changing my mind."
            "So Kat has no choice by to turn back to the others, shrugging her shoulders."
            hide anna
            hide emma
            hide kat
            with easeoutright
            "And the three of them walk away, chatting to each other."
            "I keep on telling myself that I just made the right decision."
            "That staying in the water was the better of the two choices."
            "But as soon as I see them looking back at me, I start to question my decision."
            "And when I realise that all three of them are laughing and giggling..."
            "Well my first instinct is to hurry after them."
            "Because I want to know what they're talking about."
            "Thankfully I manage to hold on in there."
            "And I turn away until they're on the beach."
            "But even then I can't help watching them walk over to the ice-cream stand."
            show beach icecream emma nomc
            show beach_icecream_girl_kat at center, zoomAt(1.0, (420, 720))
            show beach_icecream_swimsuit_kat at center, zoomAt(1.0, (420, 720))
            show beach_icecream_ice_kat at center, zoomAt(1.0, (420, 720))
            show beach_icecream_girl_anna at center, zoomAt(1.0, (140, 720))
            show beach_icecream_swimsuit_anna at center, zoomAt(1.0, (140, 720))
            with fade
            "Anna, Emma and Kat all order themselves something."
            "Then they walk back to our spot, casually licking away."
            "And now I really am regretting my decision to stay here."
            "Because I don't know what looks better right now."
            "Those ice-creams, or the sight of the girls licking them!"
            "It's only sheer stubbornness that makes me tough it out in the water."
            "And once I see they're done eating, I start to slink back."
            "Hoping they won't bring up the subject once I get there."
            scene bg beach with fade
            "By the time they've finished eating their ice-creams, it's getting later in the day."
    "The sun is sinking lower in the sky, and the heat is becoming more intense."
    "Anna and Emma are laid out on their towels, covered from head to toe in sun screen."
    "Their ultimate aim seeming to be soaking up as many rays as possible."
    "I'm feeling the heat myself, and it's making me feel pretty lethargic."
    "Part of me's thinking that I could lay down and take a rest too, maybe even nap."
    "But then I remember that there are four of us here, not just three."
    "And I find myself getting curious as to what Kat's doing."
    show kat swimsuit annoyed at center, zoomAt(1.25, (940, 900)) with dissolve
    "Glancing around, I see that she's hunched over something."
    mike.say "Hey, Kat..."
    mike.say "What are you doing?"
    "Kat doesn't seem to hear me, which is weird."
    "I'm easily close enough, and I'm sure she wouldn't just ignore me."
    show kat swimsuit annoyed at center, traveling(1.5, 0.5, (940, 1140))
    "I lean in a little closer, meaning to try again."
    "But then I see that Kat's got ear-buds in, and she's holding her phone."
    emma.say "Don't even bother, [hero.name]..."
    emma.say "She's gaming, and she's in a world of her own!"
    anna.say "Totally spaced-out and on a higher plane!"
    anna.say "Come and soak up some sun with us instead."
    show kat stuned at startle
    "Kat seems to have noticed that we're talking about her."
    "Because she looks up and pulls out one of her ear-buds."
    show kat surprised
    kat.say "Huh?"
    kat.say "Did you say something?"
    show kat stuned
    menu:
        "Sunbathe with Anna and Emma":
            "I feel a little sorry for Kat as she looks really confused."
            "But the sound of Anna and Emma's giggling makes me look back in their direction."
            "And when I see that there's just enough space for me to lie between them..."
            mike.say "Ah..."
            mike.say "Nothing, Kat..."
            mike.say "I was just talking to Anna and Emma."
            "Kat blinks in surprise."
            show kat annoyed
            "But then she shrugs and turns her attention back to her phone."
            hide kat
            show anna swimsuit at center, zoomAt(1.5, (300, 1140))
            show emma swimsuit at center, zoomAt(1.5, (980, 1140))
            with fade
            "I take this as permission to turn my own attention to Anna and Emma."
            "So I scuttle over and lie down between them."
            show anna happy
            anna.say "Oh wow..."
            anna.say "This is perfect!"
            show anna normal
            show emma happy
            emma.say "You fit in just right, [hero.name]."
            emma.say "But you don't have nearly enough sun screen on!"
            show emma normal
            "Anna and Emma proceed to squeeze more sun screen onto their hands."
            "Then they make a point of rubbing it into my chest, arms and legs."
            "Lying back on the sand, I feel like a king being attended by his servants."
            "But I still can't help sneaking a look in Kat's direction before I close my eyes."
            hide anna
            hide emma
            show kat swimsuit upset at center, zoomAt(1.25, (940, 900))
            with fade
            "And when I do, I'm surprised to find her looking straight at me."
            "There's irritation in her eyes too, as if she's pissed at being left out."
            "But who's fault is that?"
            "She's the one that decided to play around on her phone."
            "So I just close my eyes and do the best I can to forget about it."
            "Something that's helped immensely by the sensation of Anna and Emma's hands on my body."
            $ kat_score -= 1
        "Ask Kat about that 59F's game she's playing {i}(we see you){/i}":
            "I feel kind of sorry for Kat, as she looks confused."
            "Plus Anna and Emma are giggling away at her expense."
            show kat swimsuit sad at center, zoomAt(1.5, (640, 1140)) with fade
            "So I make an effort to shuffle over and see what she's doing."
            mike.say "What game are you playing, Kat?"
            mike.say "Is it any good?"
            mike.say "I've been looking for something new to play myself."
            show kat normal
            "Kat's mood seems to improve the moment I show interest in what she's doing."
            show kat at center, traveling(2.0, 0.5, (640, 1380))
            "And she scuttles over on her butt until she's as close as she can get to me."
            show kat enthusiastic
            kat.say "Oh yeah?"
            show kat happy
            kat.say "Well this one's pretty good."
            kat.say "Come have a look..."
            show kat smile
            "I take one last look over at Anna and Emma."
            "Which earns me rolling eyes and disapproving shakes of the head."
            "But by then, Kat's totally leaning into me and demanding my attention."
            show kat talkative
            kat.say "It's a dating game, see?"
            show kat normal
            mike.say "A dating game?!?"
            show kat talkative
            kat.say "Yeah, but it's a really good one."
            kat.say "Look, I'm dating this guy, Micky."
            kat.say "The one with the crazy, spiky hair."
            show kat normal
            mike.say "Huh..."
            mike.say "He kind of looks like a geek."
            show kat talkative
            kat.say "Well, yeah..."
            show kat happy
            kat.say "But he's cute and romantic, in a clumsy kind of way!"
            show kat normal with fade
            "I spend the next hour or so watching Kat as she plays the game."
            "And I soon find myself getting into it, offering her advice when I think she needs it."
            "Pretty soon time feels like it's flying by as I become more emotionally invested in the game."
            show kat surprised
            kat.say "Oops..."
            show kat sadsmile
            kat.say "I'd better stop playing soon..."
            kat.say "Or else I'll have no battery left!"
            show kat normal
            mike.say "Not yet!"
            mike.say "I need to know if you're going to go steady with Micky..."
            mike.say "Or if you'll betray him with his friend Jake!"
            show kat happy at startle
            "Kat chuckles and shakes her head at me."
            "But I note that she puts her phone away all the same."
            show kat smile
            kat.say "Download it and play it yourself if you like it that much!"
            $ kat_score += 1
    scene bg beach with fade
    "It feels like the very next time I look up, hours have sped past."
    "Because while it's by no means dark, it's clear we're burning daylight."
    mike.say "Huh..."
    mike.say "Where did all the time go?"
    mike.say "I guess it flies when you're having fun!"
    show anna swimsuit at right
    show emma swimsuit at center
    show kat swimsuit at left
    with dissolve
    "I look for confirmation from the girls."
    "Scanning each of their faces for agreement."
    if all(score >= 2 for score in (anna_score, emma_score, kat_score)):
        show anna talkative
        anna.say "Wait..."
        anna.say "It's not time to go home yet, is it?"
        show anna normal
        show emma talkative
        emma.say "I feel like I could stay here a lot longer."
        show emma normal
        show kat talkative
        kat.say "I'm not ready to call it a day yet."
        kat.say "Unless everyone else is?"
        show kat normal
        "I can feel a smile spreading across my face."
        "Because that's exactly what I was hoping to hear."
        mike.say "That's great news!"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        "As one the girls nod their heads."
        "All of them seeing eager to stay."
        show anna happy
        anna.say "Ooh..."
        anna.say "That sounds totally romantic!"
        show anna normal
        show emma happy
        emma.say "You know, I never did that before!"
        show emma normal
        show kat happy
        kat.say "Oh yeah..."
        kat.say "Maybe we could start a fire with drift-wood or something?"
        show kat normal
        "I'm nodding too, doing all I can to encourage them."
        "Because things seem to be going exactly as I hope they would."
        "Now I just need to see that they play out that way too."
        $ anna.love += 1
        $ emma.love += 1
        $ kat.love += 1
        call petite_harem_event_04_sex_intro from _call_petite_harem_event_04_sex_intro
    elif all(score >= 2 for score in (anna_score, emma_score)):
        show anna talkative
        anna.say "Wait..."
        anna.say "It's not time to go home yet, is it?"
        show anna normal
        show emma talkative
        emma.say "I feel like I could stay here a lot longer."
        show emma normal
        show kat whining
        kat.say "It's a couple of hours I'm never going to get back!"
        show kat sad
        show anna stuned
        show emma surprised
        "Anna, Emma and I look at Kat with genuine surprise."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        show anna normal
        show emma normal
        "Anna and Emma nod their heads."
        "But Kat doesn't look impressed at all."
        show anna happy
        anna.say "Ooh..."
        anna.say "That sounds totally romantic!"
        show anna normal
        show emma happy
        emma.say "You know, I never did that before!"
        show emma normal
        show kat annoyed
        kat.say "I have to go home and play online."
        kat.say "I said I'd be someone's back-up."
        "Anna, Emma and I sit down to plan what we're going to do next."
        "But Kat's already gathering up her stuff and preparing to leave."
        "And there doesn't seem to be anything I can do to change her mind."
        $ anna.love += 1
        $ emma.love += 1
        $ kat.love -= 1
    elif all(score >= 2 for score in (emma_score, kat_score)):
        show emma talkative
        emma.say "I feel like I could stay here a lot longer."
        show emma normal
        show kat talkative
        kat.say "I'm not ready to call it a day yet."
        kat.say "Unless everyone else is?"
        show kat normal
        show anna worried
        anna.say "Then that must be why I feel like I've been here forever!"
        show anna sad
        show emma surprised
        show kat stuned
        "Emma, Kat and I look at Anna with genuine surprise."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        show emma normal
        show kat normal
        "Emma and Kat nod their heads."
        "But Anna doesn't look impressed at all."
        show emma happy
        emma.say "You know, I never did that before!"
        show emma normal
        show kat happy
        kat.say "Oh yeah..."
        kat.say "Maybe we could start a fire with drift-wood or something?"
        show kat normal
        show anna worried
        anna.say "Nah, I want to go home."
        show anna sadsmile
        "Emma, Kat and I sit down to plan what we're going to do next."
        "But Anna's already gathering up her stuff and preparing to leave."
        "And there doesn't seem to be anything I can do to change her mind."
        $ anna.love -= 1
        $ emma.love += 1
        $ kat.love += 1
    elif all(score >= 2 for score in (anna_score, kat_score)):
        show anna talkative
        anna.say "Wait..."
        anna.say "It's not time to go home yet, is it?"
        show anna normal
        show kat talkative
        kat.say "I'm not ready to call it a day yet."
        kat.say "Unless everyone else is?"
        show kat normal
        show emma whining
        emma.say "Huh..."
        emma.say "It's just been a massive drag for me."
        show emma sad
        show anna stuned
        show kat stuned
        "Anna, Kat and I look at Emma with genuine surprise."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        show anna normal
        show kat normal
        "Anna and Kat nod their heads."
        "But Emma doesn't look impressed at all."
        show anna happy
        anna.say "Ooh..."
        anna.say "That sounds totally romantic!"
        show anna normal
        show kat happy
        kat.say "Oh yeah..."
        kat.say "Maybe we could start a fire with drift-wood or something?"
        show kat normal
        show emma whining
        emma.say "I need a bath to get rid of all this sand!"
        show emma sad
        "Anna, Kat and I sit down to plan what we're going to do next."
        "But Emma's already gathering up her stuff and preparing to leave."
        "And there doesn't seem to be anything I can do to change her mind."
        $ anna.love += 1
        $ emma.love -= 1
        $ kat.love += 1
    elif anna_score >= 2:
        show anna talkative
        anna.say "Wait..."
        anna.say "It's not time to go home yet, is it?"
        show anna normal
        show emma whining
        emma.say "Huh..."
        emma.say "It's just been a massive drag for me."
        show emma sad
        show kat whining
        kat.say "It's a couple of hours I'm never going to get back!"
        show kat sad
        "I can't help staring at the Emma and Kat in amazement."
        "Because I thought today went pretty well."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        show anna happy
        anna.say "Ooh..."
        anna.say "That sounds totally romantic!"
        show anna normal
        show emma whining
        emma.say "I need a bath to get rid of all this sand!"
        show emma sad
        show kat whining
        kat.say "I have to go home and play online."
        kat.say "I said I'd be someone's back-up."
        show kat sad
        "Anna and I sit down to plan what we're going to do next."
        "But Emma and Kat are already gathering up their stuff and preparing to leave."
        "And there doesn't seem to be anything I can do to change their minds."
        $ anna.love += 1
        $ emma.love -= 1
        $ kat.love -= 1
    elif emma_score >= 2:
        show emma talkative
        emma.say "I feel like I could stay here a lot longer."
        show emma normal
        show anna worried
        anna.say "Then that must be why I feel like I've been here forever!"
        show anna sad
        show kat whining
        kat.say "It's a couple of hours I'm never going to get back!"
        show kat sad
        "I can't help staring at the Anna and Kat in amazement."
        "Because I thought today went pretty well."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        show anna worried
        anna.say "Nah, I want to go home."
        show anna sad
        show kat annoyed
        kat.say "I have to go home and play online."
        kat.say "I said I'd be someone's back-up."
        "Emma and I sit down to plan what we're going to do next."
        "But Anna and Kat are already gathering up their stuff and preparing to leave."
        "And there doesn't seem to be anything I can do to change their minds."
        $ anna.love -= 1
        $ emma.love += 1
        $ kat.love -= 1
    elif kat_score >= 2:
        show kat talkative
        kat.say "I'm not ready to call it a day yet."
        kat.say "Unless everyone else is?"
        show kat normal
        show anna worried
        anna.say "Then that must be why I feel like I've been here forever!"
        show anna sad
        show emma whining
        emma.say "Huh..."
        emma.say "It's just been a massive drag for me."
        show emma normal
        "I can't help staring at the Anna and Emma in amazement."
        "Because I thought today went pretty well."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        show kat happy
        kat.say "Oh yeah..."
        kat.say "Maybe we could start a fire with drift-wood or something?"
        show kat normal
        anna.say "Nah, I want to go home."
        show emma whining
        emma.say "I need a bath to get rid of all this sand!"
        show emma sad
        "Kat and I sit down to plan what we're going to do next."
        "But Anna and Emma are already gathering up their stuff and preparing to leave."
        "And there doesn't seem to be anything I can do to change their minds."
        $ anna.love += 1
        $ emma.love -= 1
        $ kat.love += 1
    else:
        show anna worried
        anna.say "Then that must be why I feel like I've been here forever!"
        show anna sad
        show emma whining
        emma.say "Huh..."
        emma.say "It's just been a massive drag for me."
        show emma sad
        show kat whining
        kat.say "It's a couple of hours I'm never going to get back!"
        show kat sad
        "I can't help staring at the girls in amazement."
        "Because I thought today went pretty well."
        mike.say "Erm..."
        mike.say "Are you sure?"
        mike.say "Because I was going to ask if you wanted to stay longer?"
        mike.say "Maybe even watch night fall on the beach?"
        "As one the girls shake their heads and start to get up."
        "And before I know it, they're packing up their things too!"
        show anna worried
        anna.say "Nah, I want to go home."
        show emma whining
        emma.say "I need a bath to get rid of all this sand!"
        show emma whining
        kat.say "I have to go home and play online."
        kat.say "I said I'd be someone's back-up."
        show emma
        "All I can do is shrug and start packing up too."
        "That and hope that the next time we're on a date, things go better."
        $ anna.love -= 1
        $ emma.love -= 1
        $ kat.love -= 1
    return

label petite_harem_foursome_intro(appointment=None):
    scene bg beach
    show kat swimsuit happy at right
    show emma swimsuit happy
    show anna swimsuit happy at left
    with fade
    "We're enjoying our time at the beach, you know, \"Sea, Sex and Sun\"."
    "Well, minus the sex part."
    show kat naked happy with dissolve
    "But as Kat starts to remove her swimsuit, I suspect the missing part of the song won't be missing for that long."
    show emma naked happy
    show anna naked happy
    with dissolve
    "Soon, we're all naked on the beach, and the only thing to worry is: where to start."
    menu:
        "Play a bit":
            call petite_harem_event_04_sex_foreplay from _call_petite_harem_event_04_sex_foreplay_1
        "Straight to the main course":
            call petite_harem_event_04_sex_fuck from _call_petite_harem_event_04_sex_fuck_2
    scene beach_night
    show kat swimsuit happy at right, dark
    show emma swimsuit happy at center, dark
    show anna swimsuit happy at left, dark
    with fade
    "Once it's all over, we quickly scoop up our clothes and make ourselves decent."
    hide kat
    hide emma
    hide anna
    with easeoutright
    "Then we throw everything back into the bags we brought it in and scuttle off the beach."
    "It's a short, quiet walk back to the car, with little of any importance being said."
    "But in the comfortable silence I can feel a closeness growing between the four of us."
    "It's unspoken and I'd struggle to define it in words if I were to try."
    "Yet I'm totally sure that it's real, and that it's getting stronger by the day."
    $ anna.sexperience += 1
    $ emma.sexperience += 1
    $ kat.sexperience += 1
    $ game.pass_time(20 - game.hour)
    return

label petite_harem_event_04_sex_intro:
    $ DONE['petite_harem_event_04_sex'] = game.days_played
    scene bg beach with fade
    "By the time that we've all agreed to stay longer at the beach, most people have begun to leave."
    "Now that the sun is starting to sink in the sky, it's not as crazily hot as before."
    "There's the threat of a chill creeping into the air, and the need to think about lighting a fire."
    "So Anna, Emma, Kat and I set about scouring the beach for driftwood, then piling it in a circle of stones."
    "Luckily someone thought to bring along a lighter, and so getting the fire going is pretty easy."
    show anna b swimsuit at center, zoomAt(1.5, (980, 1040))
    show emma swimsuit at center, zoomAt(1.5, (300, 1040))
    show kat swimsuit at center, zoomAt(1.5, (640, 1040))
    with fade
    "And soon enough we're sitting on the sand, warmed by the flames licking at the wood."
    "The girls seem to be pretty much entranced by the flickering motion of the fire."
    "They're staring into it, and in turn I can see the flames reflected in their eyes."
    mike.say "So..."
    mike.say "I'm going to guess that you guys don't do this kind of thing very often?"
    "The girls exchange glances, shaking their head at the question."
    show anna b talkative
    anna.say "I've always been a city girl, you know?"
    anna.say "Never got to hang out at the beach much."
    show anna b normal
    show emma talkative
    emma.say "It's the same with me really..."
    emma.say "My folks didn't live anywhere near the coast when I was growing up."
    show emma normal
    show kat talkative
    kat.say "Not me, I lived right by the beach."
    show kat normal
    "My eyebrows rise as Kat seems to buck the trend."
    "And I'm all the more intrigued to hear her story."
    mike.say "So you must have been on the sand all the time, right?"
    show kat happy at startle
    "Kat shakes her head and chuckles."
    show kat talkative
    kat.say "Nope - allergies!"
    kat.say "Why'd you think I ended up inside playing videogames all the time?"
    kat.say "It was only when I was in my teens I got medication to handle it."
    show kat normal
    "I shake my head, unable to believe what I'm hearing."
    mike.say "Huh..."
    mike.say "My friends and I used to hang out at the beach all the time."
    mike.say "In fact, it was kind of a rite of passage when you..."
    mike.say "Well, when, you know..."
    "I'm doing the best I can to drop what I feel are heavy hints."
    "But they don't seem to be working on some of my companions."
    show kat surprised
    kat.say "When you what?"
    show emma surprised
    emma.say "Yeah, [hero.name]..."
    emma.say "We already said we never hung out at the beach!"
    kat.say "So how are we gonna know what you mean?!?"
    show emma surprised
    show kat stuned
    "Surprisingly, it's Anna that comes to their rescue."
    show anna b surprised
    anna.say "Oh..."
    anna.say "I think I know what he means!"
    anna.say "You're talking about getting frisky on the sand..."
    anna.say "Aren't you, [hero.name]?"
    show anna b normal
    "I can't help nodding and smiling at the way Anna puts it."
    "And I can see that the idea's already getting into Emma and Kat's heads."
    show emma surprised
    emma.say "Oh my..."
    emma.say "That sounds dangerous..."
    show emma happy
    emma.say "But exciting too!"
    show emma
    show kat talkative
    kat.say "You know what..."
    kat.say "I can't see anyone else around here right now."
    show kat naked with dissolve
    "Kat underlines her statement by beginning to peel off her swimming costume."
    "And just like that, an unspoken message seems to pass between all of us."
    show emma naked
    show anna naked
    with dissolve
    "Because a moment later, Anna and Emma start to do the exact same thing."
    "So there's nothing else for me to do, other than pull down my trunks too!"
    "I guess we're doing this thing."
    "Anna, Emma, Kat and I are going to have sex on the sand!"
    "Now one thing you have to understand about foursomes is that it's not a simple affair."
    "With a couple there's only two people to please, and even a threesome isn't much more complicated."
    "But once you get up to four, things start to get more complicated."
    "Especially when the pussys outnumber the cocks two to one!"
    "As usually happens, all of the girls make a rush for mine too."
    "All of a sudden there are three pairs of hands grabbing for it!"
    "Sure, we're only supposed to be engaging in some foreplay."
    "Just trying to get everyone in the mood, both mental and physical."
    "But I know these girls, so I also know how possessive they can get."
    "Which means I'm going to have to be the one to impose some kind of order here."
    "And that means making a decision as to who's going to be getting what and when."
    menu:
        "Foreplay":
            call petite_harem_event_04_sex_foreplay from _call_petite_harem_event_04_sex_foreplay
        "Fuck":
            call petite_harem_event_04_sex_fuck from _call_petite_harem_event_04_sex_fuck
    scene beach_night with fade
    "Once it's all over, we quickly scoop up our clothes and make ourselves decent."
    "Then we throw everything back into the bags we brought it in and scuttle off the beach."
    "It's a short, quiet walk back to the car, with little of any importance being said."
    "But in the comfortable silence I can feel a closeness growing between the four of us."
    "It's unspoken and I'd struggle to define it in words if I were to try."
    "Yet I'm totally sure that it's real, and that it's getting stronger by the day."
    $ anna.sexperience += 1
    $ emma.sexperience += 1
    $ kat.sexperience += 1
    $ game.pass_time(20 - game.hour)
    if renpy.has_label("petite_harem_achievement_2") and not game.flags.cheat:
        call petite_harem_achievement_2 from _call_petite_harem_achievement_2
    return

label petite_harem_event_04_sex_foreplay:
    scene bg black
    show petite 4some foreplay beach
    with fade
    "I'm all caught up in the task of choosing which of the girls I want to fuck."
    "So distracted in fact, that I don't even notice them beginning to take charge."
    show petite 4some foreplay kat with fade
    "As one, Anna and Kat tackle me around the waist."
    "And this wouldn't normally be much of a challenge to me staying on my feet."
    show petite 4some foreplay emma with fade
    "But a moment later I feel Emma grab me from behind, adding her weight to the effort."
    mike.say "Whoa..."
    mike.say "What the..."
    mike.say "Oof!"
    anna.say "Just relax, [hero.name]..."
    emma.say "Yeah, leave everything to us!"
    kat.say "Don't worry..."
    kat.say "We've got everything covered!"
    "I find myself staring up at their three faces, all looking down on me."
    "And it takes me a few moments to realise that I'm laid on my back."
    "Instinctively I make an effort to move, but then stop the very next second."
    "Because I feel a tight squeezing sensation below my waist."
    "Specifically around the shaft of my cock!"
    emma.say "Oh..."
    emma.say "Sorry, [hero.name]..."
    emma.say "Was that a little too hard?"
    anna.say "I don't know about that, Emma..."
    anna.say "It seems to be getting bigger already!"
    "I'm blinking and straining to see what's going on down there."
    "But I still don't dare to move in case they squeeze me harder still."
    anna.say "Don't worry, [hero.name]..."
    anna.say "I'll kiss it better!"
    "With a giggle, Anna's head disappears from view."
    "And a moment later, Emma's follows."
    emma.say "Hey!"
    emma.say "Wait for me - I want to kiss it too!"
    "Only once the two of them have disappeared can I actually lift my head."
    "Because now their weight is pinning down my middle, rather than my chest."
    "Plus Kat doesn't seem as interested in keeping me down as the others did."
    "In fact, she props me up a little, helping me to see what's happening."
    kat.say "Oh, wow..."
    kat.say "They're really serious about this, [hero.name]."
    kat.say "Looks like you're in for a real treat!"
    "Now I can actually see what's going on down there."
    "And as soon as I do, my entire mood changes."
    "Anna and Emma are both leaning in low over my erect cock."
    "Their eyes are fixated on it, like they're worshipping it or something."
    "All of a sudden they see me watching them, and their faces become impish."
    "Still holding my eye, they part their lips and start to lick at the shaft."
    "It's only when they really start to get into a rhythm that they close their eyes."
    "And that's when I feel the sense of being rooted to the spot again."
    "Only this time it's on account of the sensations they're creating."
    "Anna and Emma work together like a double-act, each supporting the other."
    "One goes up top while the other slides down below."
    "Then they swap places without even stopping along the way."
    "I honestly don't know which of them is the first to swallow me whole."
    "But that's not because of how well they're working together."
    "Instead I feel movement behind my head, as Kat reminds me of her presence."
    "Without a word of warning or the slightest hint of asking, she slides one leg over me."
    "And then she lowers herself almost directly onto my face!"
    mike.say "What the..."
    mike.say "Mmmph..."
    kat.say "Remember your manners, [hero.name]..."
    kat.say "It's not polite to talk with your mouth full!"
    "I can hear Kat chuckling at her own joke."
    "And that's what makes me all the more determined to pay her back a little."
    "So if she wants me to chow down on her pussy, then that's what she's going to get!"
    "Like Anna and Emma a few moments before, I part my lips and stick out my tongue."
    "But unlike them, I don't like with it."
    "Instead I push it as far into Kat's pussy as I possibly can."
    "And I'm instantly rewarded with the sound of her beginning to wail with pleasure."
    kat.say "Oh..."
    kat.say "Ah..."
    kat.say "Mmm..."
    kat.say "Oh, you beast!"
    "I know that the name she just called me isn't supposed to shame me."
    "In fact I suspect that it's more intended to make me give her more of the same."
    "So I don't hesitate to slide my tongue around the folds of her pussy."
    "Every circle I make seems to loosen the muscles in there a little more."
    "As well as making Kat wetter too, filling my mouth with the taste of her."
    "She's sitting down lower all the time, while I'm struggling to push upwards."
    "I can feel the lips of her pussy opening to me ever wider."
    "That and my tongue probing ever deeper too."
    "I'd almost forgotten that Anna and Emma were pleasuring me at the same time."
    "The pleasure I'm feeling becoming the background sensation to pleasing Kat."
    "That is until I can feel something building up inside of me."
    "An intense wave of pleasure that's going to break at any moment."
    "And it doesn't take a genius to figure out what that is!"
    menu:
        "Hold it and fuck them":
            call petite_harem_event_04_sex_fuck from _call_petite_harem_event_04_sex_fuck_1
        "Let them finish you off":
            call petite_harem_event_04_sex_cumshare from _call_petite_harem_event_04_sex_cumshare
    return

label petite_harem_event_04_sex_fuck:
    menu:
        "Fuck them all":
            show petite 4some fuckall anna beach with fade
            "Putting my hands on Anna's shoulders, I act before she knows what's happening."
            "In that time I manage to spin her around, then push her down onto all fours."
            anna.say "Wha..."
            anna.say "What's happening?!?"
            mike.say "Be a good girl, and stay right there."
            "Emma and Kat watch all of this with interest."
            show petite 4some fuckall emma with fade
            "That is until I do the same thing to Emma, pushing her down to Anna's left."
            emma.say "Whoa..."
            anna.say "Oh..."
            anna.say "Hi, Emma!"
            show petite 4some fuckall kat with fade
            "I turn around to give Kat the same treatment a moment later."
            "But I see that she's already seen what's coming and taken action."
            "Because she's kneeling down to Anna's right, just where I wanted her."
            anna.say "Hey, Kat..."
            anna.say "Fancy seeing you here!"
            kat.say "Well, Anna..."
            kat.say "It's a small world!"
            "Now that I have all three of them down in front of me, I'm starting to get excited."
            "Six buttocks are hovering right there, drawing my eye and stiffening my cock."
            "Plus each pair has something so inviting hidden between them too."
            "How on earth am I supposed to choose which one to explore?"
            "Especially when they all look so damn good?"
            "All I can do is shrug and admit defeat."
            "I'll just have to fuck each one in turn!"
            show petite 4some fuckall mike with fade
            "Clapping my hands together for effect, I drop down onto my knees in the sand."
            mike.say "Okay then..."
            mike.say "Who am I going to fuck first?"
            "The question seems to jolt all three of them to life."
            "Suddenly their asses are shaking in front of my eyes."
            "I can see their breasts swaying from side to side too."
            "And each of them looks back over their shoulder at me."
            "Doing the best they can to promise me the earth in return for my cock."
            anna.say "Do me first..."
            anna.say "I have the peachiest ass!"
            emma.say "No, me first..."
            emma.say "I'm already aching for you!"
            kat.say "Don't listen to them, [hero.name]..."
            kat.say "Mine's the sweetest, the tightest too!"
            "That's it - that's the one that does it."
            "Until a moment ago, I was going to choose one of them at random to get things started."
            "But Kat's comments about the tightness of her pussy seem to pique my interest just enough."
            show petite 4some fuckall behind_kat with fade
            "So I turn in her direction and then grab hold of her around the waist."
            kat.say "Whoo..."
            kat.say "Oh..."
            kat.say "Oh wow!"
            show petite 4some fuckall fuck_kat with fade
            "I'm not holding back here either, I'm pushing straight ahead."
            "As if Kat's claims were a direct challenge to me getting inside of her."
            anna.say "Aww..."
            anna.say "No fair!"
            emma.say "Yeah..."
            emma.say "I wanted to go first!"
            "I can hear Anna and Emma's complaints, so I guess Kat can too."
            "But I don't pay them a moment's notice, as I'm totally focussed on the task at hand."
            "Kat wasn't exaggerating all that much when she said it was tight and sweet."
            "Because I can feel the resistance that her pussy is putting up right now."
            "And the sweetness soon follows as the tightness begins to ease off."
            show petite 4some fuckall kat_eyes_closed
            "Not totally, just enough for me to start sinking into her."
            "I don't stop to enjoy the intensity of the sensation, instead I push all the way in."
            "Even when I can't go any further I don't pause, I just start to thrust back and forth."
            "Believe mem I'd love to be able to take my time, but I have two other girls to please!"
            "That's why I'm doing all I can to rattle Kat, to stimulate her quickly and powerfully."
            "Stirring her up into a state of excitement that won't stop just because I have to move on."
            show petite 4some fuckall kat_eyes_ahegao
            "Not that Kat's aware of my plans at all, even as she gets worked up into just such a state."
            "Her head is bowed, her limbs stiff and her breasts swaying wildly."
            "But when she looks like she's right on the point of exploding, I suddenly pull out."
            show petite 4some fuckall behind_kat with hpunch
            kat.say "Ah..."
            kat.say "Urgh..."
            show petite 4some fuckall behind_anna with fade
            "And then I make a grab for Anna in the middle."
            "My hopes prove correct as soon as I push my cock between Anna's thighs."
            anna.say "Is..."
            anna.say "Is it my turn?"
            anna.say "Oh yeah!"
            "She's been watching everything I've done to Kat, and she's been getting excited the whole time."
            show petite 4some fuckall fuck_anna with hpunch
            "That means I can pretty much slide straight into Anna's waiting pussy."
            "Her muscles barely try to squeeze me as I fill her to the brim."
            "Just as with Kat before her, I keep up the same pace with Anna."
            "And to me it feels like there was a seamless switch-over."
            "Sure, the pussy feels subtly different and the sounds she's making are her own."
            "But the motions of my own body remain the same as I dish it out for a second time."
            "The feeling of pleasure returns almost instantly too, washing over me in waves."
            "Though with Kat it was fresh and new, far easier to ignore the urge to let go."
            "Now that I'm fucking Anna instead, the feelings are waxing fuller than before."
            "I'm experiencing more pleasure, but it's even harder to keep myself going for longer."
            "Doing the best I can to push that fear aside, I concentrate on fucking Anna."
            "Hoping that by going as hard and fast as I can, it'll numb the sensations."
            "But the more I seem to try, the more intense they become."
            "More than once I almost lose it."
            "Only managing to pull myself back from the brink at the very last second."
            "And I know that I'm going to have to change things up right now."
            "Otherwise Emma's going to get left out!"
            "Gathering all of my remaining strength and power of will, I pull myself backwards."
            show petite 4some fuckall behind_anna with hpunch
            "This means that my cock pops out of Anna with an audible sound."
            "And she's not quiet about the matter either."
            anna.say "Wha..."
            anna.say "What happened?"
            anna.say "Where'd the dick go?!?"
            "But even as Anna's turning her head this way and that in confusion, I've moved on."
            show petite 4some fuckall behind_emma with fade
            "And my hands are already making a grab for Emma's waiting ass."
            "Not that I have to make much of one, as she practically thrusts it at me."
            "I guess she's been waiting for this moment right from the start."
            "Seeing me begin with Kat and knowing that she was on the other end of the line."
            "Now it's finally her turn, and she doesn't mean to miss out on a second of it."
            "And the moment that she opens her mouth, Emma pretty much confirms my suspicions."
            show petite 4some fuckall emma_mouth_happy
            emma.say "Okay..."
            emma.say "My turn!"
            show petite 4some fuckall emma_eyes_closed emma_mouth_pleasure fuck_emma with hpunch
            emma.say "Oh..."
            emma.say "Oooh..."
            "I can hear the delight in her voice, the feeling that she's now the one in control."
            "But the problem is that it doesn't last for very long, not after I get my hands on her."
            "There's no sense of my trying to prove Emma wrong or assert myself over her."
            "More that I'm hitting the ground running, trying to keep up the same pace as before."
            "This means that I pretty much push aside the token resistance that Emma's pussys offers."
            show petite 4some fuckall emma_eyes_ahegao
            "And before she knows what's happening, I'm deep inside of her, thrusting away like crazy."
            "The words that Emma was able to get out soon fade away into meaningless moans."
            "In fact every time I push into her, she seems to become more animal in nature."
            "Soon enough, she's making long, drawn-out sounds that remind me more of a cow than a human being."
            "Again I have the strange sensation of changing pussys, yet doing the exact same thing."
            "It almost feels like I haven't moved an inch and the girls have somehow swapped places."
            "But if I felt the pace quicken with Anna, then it's accelerating far more with Emma."
            "The only option that I have is to give in to the urge and quicken my pace."
            "Yet that doesn't mean I'm just going to sign off with a whimper."
            "Instead I summon the very last of my strength and start to hammer away at Emma."
            "Sure, she might not get as long with me as Kat and Anna did."
            "But she's probably getting more than twice the intensity while it lasts."
            "Those moans become gasps, then the gasps become cries of intense passion."
            "The sound of them is too much for me to be able to handle."
            "I can't hold on any longer."
            "I just have to let go!"
            menu:
                "Let them finish you off":
                    call petite_harem_event_04_sex_cumshare from _call_petite_harem_event_04_sex_cumshare_1
                "CUUUUUUUUUM":
                    show petite 4some fuckall behind_emma hand with hpunch
                    "Almost lurching backwards, I pull myself out of Emma."
                    show petite 4some fuckall cum bodycum_emma with hpunch
                    "Then I shoot my load, making sure it's spread over all three of them."
                    show petite 4some fuckall bodycum_anna bodycum_kat with hpunch
                    "Hot, white cum spatters over six buttocks, drawing a random pattern."
                    show petite 4some fuckall -cum -mike with vpunch
                    "Which I stare at as I collapse onto my own ass in complete exhaustion."
        "Fuck Anna":
            "It was always going to be hard to decide which one of the girls was going to get it."
            show petite 4some fuckanna beach with fade
            "Which is why I feel like thanking Anna as she lowers herself onto all fours in front of me."
            "Because that means my attention is immediately drawn to the curve of her buttocks."
            "As soon as that happens, it's like my entire body goes into autopilot."
            show petite 4some fuckanna mike anna_lookback out with fade
            "I feel myself reaching out as I get down onto my knees behind Anna."
            "Then my hands take hold of her around the waist, pulling her sharply backwards."
            "Anna lets out a gasp, as if she's surprised at my actions."
            "But I seriously doubt that there's anything genuine about the sound."
            anna.say "Oh..."
            anna.say "Goodness me!"
            anna.say "What are you trying to do back there?"
            "Anna looks back over her shoulder as she says all of this."
            "And she all but winks at me as she does so."
            "Which makes me all the more determined to press on with what I'm doing."
            "With a knowing smile on my face, I aim my cock squarely between Anna's thighs."
            "And then I thrust myself forwards, not even trying to take things slowly."
            show petite 4some fuckanna vaginal
            "The moment that my cock makes contact with Anna's pussy, her entire demeanour changes."
            "Before she was smiling as she teased me, holding my eye."
            "But now her eyes close and the lowers her head, turning it to face forwards."
            "And I can hardly blame her for doing so, based on what I'm feeling right now."
            "Anna's pussy is putting up an admirable fight, doing it's best to keep me out."
            "But the combination of her horniness and my own is too much to resist."
            "Already I can feel the muscles down there beginning to loosen up."
            "All the time I'm pushing harder, stroking up and down her lips."
            "I can feel them getting wetter and softer with each passing second."
            "Then it happens, Anna's lips part and I suddenly sink into her."
            "I could brace myself and take charge of what's happening."
            "But instead I choose to hold back, letting nature take it's course."
            "This means that I keep on sinking into Anna, using gravity to do the work for me."
            "And I don't make my move until I'm as far into her as I can possibly go."
            "When I reach that point, I leap into action."
            show petite 4some fuckanna anna_lookfront with hpunch
            "My grip on Anna's waist tightens, and I begin thrusting in and out of her."
            "Suddenly her head pops up and I can hear her start to moan with pleasure."
            "That only serves to urge me on even more, and soon I'm going as fast as I can."
            show petite 4some fuckanna at stepback(speed=0.1, h=-10, v=-20)
            "Anna's entire body shakes and jiggles as she rides my cock."
            show petite 4some fuckanna at stepback(speed=0.1, h=-10, v=-20)
            "And the sound of my thighs slapping against hers fills the air."
            show petite 4some fuckanna at stepback(speed=0.1, h=-10, v=-20)
            "Until now I've been looking down at Anna's buttocks or the back of her head."
            "But then I see Emma, spreading herself out on the sand in front of us."
            "She has a knowing smile on her face, and I can soon see why."
            "Because Kat appears next, lowering herself over Emma."
            "As she does so, Emma reaches up, pulling the other girl's groin over her face."
            "Just like that, I find myself watching as Emma licks at Kat's pussy."
            "The two of them do it brazenly, right in front of Anna and I."
            show petite 4some fuckanna at stepback(speed=0.1, h=-10, v=-20)
            "And I can tell that they're getting off on having me watch them too."
            "I have no way of knowing if Anna's eyes are even open right now."
            show petite 4some fuckanna at stepback(speed=0.1, h=-10, v=-20)
            "Just that what I'm seeing makes me redouble my efforts."
            "I find a reserve of strength that I didn't know I had left in me."
            with hpunch
            "And I use it to fuck Anna harder than ever before."
            with hpunch
            "The effect on her is instant and impressive in the extreme."
            with hpunch
            "Mere seconds pass before I feel Anna's pussy begin to squeeze my cock."
            menu:
                "Let them finish you off":
                    call petite_harem_event_04_sex_cumshare from _call_petite_harem_event_04_sex_cumshare_2
                "CUUUUUUUUUM":
                    show petite 4some fuckanna cum with hpunch
                    "And one last thrust seals the deal, making me shoot my load into her."
        "Fuck Emma":
            "It was always going to be hard to decide which one of the girls was going to get it."
            show petite 4some fuckemma beach with fade
            "Which is why I feel like thanking Emma as she lowers herself onto the sand in front of me."
            "Because that means my attention is immediately drawn to the curve of her thighs."
            "As soon as that happens, it's like my entire body goes into autopilot."
            show petite 4some fuckemma mike out with fade
            "I feel myself Kneeling down and reaching out for her without a conscious thought."
            "Emma smiles up at me as I come to her, spreading her legs wide in anticipation."
            "I take hold of her right leg, lifting it so that I have a better angle to work from."
            "And then I make sure to aim myself straight at what lies between them."
            "Emma holds herself up with one hand, but reaches up with the other."
            "I'm looking her in the eyes as I feel her begin to stroke my cock."
            "And she keeps on holding my gaze as I come closer still, guiding it home."
            emma.say "Just relax, [hero.name]..."
            emma.say "Leave it to me!"
            "Emma's true to her word too, as I feel her push it hard against her pussy."
            "I gulp and swallow hard as the sensation floods through me."
            "It's like she's making me quiver from head to toe."
            "And I want to be inside of her more with every passing moment."
            mike.say "Oh wow..."
            mike.say "Emma, please..."
            "Emma lets out a giggle, as if my desperation amuses her."
            "But she doesn't seem to want to torture me unduly."
            "As she begins to push harder, working my cock against her harder then before."
            "I'm doing all I can to add to the pressure as well, gently pressing down from above."
            "Together our efforts are too much for her body to resist."
            "I feel a slight give down below, and that's all the prompting I need."
            "Redoubling my efforts, I lean all of my weight into it."
            show petite 4some fuckemma vaginal emma_pleasure
            "And then I feel myself beginning to sink into Emma."
            "She's nodding as this happens, pulling me towards her."
            "Everything comes together to build the momentum, letting me fill her all the way."
            "But as soon as I can go no further, the urge overtakes me to begin seizing more control."
            "Where before I was almost passive, now my muscles start to tense and twitch."
            "I'm braced in the perfect position to take advantage of the opportunity."
            show petite 4some fuckemma at startle(0.05,-10)
            "And so I don't hesitate to start moving in and out of Emma."
            "As soon as this change takes place, the whole mood between us changes."
            show petite 4some fuckemma emma_normal at startle(0.05,-10)
            "We go from slow and tentative to energetic and almost desperate in mere seconds."
            "And now it's not Emma guiding me home."
            show petite 4some fuckemma emma_pleasure at startle(0.05,-10)
            "It's me doing all I can to fuck her senseless!"
            "My motions don't take long to start pushing Emma back."
            "And she's so overwhelmed that she can't seem to support herself anymore."
            show petite 4some fuckemma emma_normal at startle(0.05,-10)
            "But before she falls flat on her back, Anna and Kat come to the rescue."
            "Together they hold her up, one on either side, letting me take full advantage."
            "With their help, I manage to move even faster and thrust even harder than before."
            show petite 4some fuckemma emma_pleasure with vpunch
            "All of which means that Emma and I are pushed further than before too."
            with vpunch
            "It's not long until I feel myself starting to lose it."
            "But Emma seems to be in the exact same place too."
            menu:
                "Let them finish you off":
                    call petite_harem_event_04_sex_cumshare from _call_petite_harem_event_04_sex_cumshare_3
                "CUUUUUUUUUM":
                    show petite 4some fuckemma emma_ahegao cum with vpunch
                    "She cums just as I shoot my load into her, body going limp."
                    "So the only thing holding her up is now the grip Anna and Kat have on her."
        "Fuck Kat":
            "It was always going to be hard to decide which one of the girls was going to get it."
            "Which is why I feel like thanking Kat as she lowers herself onto the sand in front of me."
            "Because that means my attention is immediately drawn to the curve of her ass."
            "She looks back over her shoulder, giving me a wink of encouragement."
            "As soon as that happens, it's like my entire body goes into autopilot."
            "I want to reach out and grab Kat, to push her onto her hands and knees."
            "But just as I make my move, Anna and Emma take me by complete surprise."
            "Anna pops up and gives me a hard shove, sending me staggering backwards."
            "And Emma's already crouching down behind me, so that I stumble over her!"
            mike.say "Whoa..."
            mike.say "What the..."
            mike.say "Oof!"
            anna.say "Just relax, [hero.name]..."
            emma.say "Yeah, leave everything to us!"
            "I land in a heap on the sand, still not sure what's going on."
            "Which means I'm defenceless as the girls put their plan into action."
            "Anna and Emma pin me down and hold me there as I flail about helplessly."
            show petite 4some fuckkat beach with fade
            "And Kat turns her back to me, lowering herself down to straddle my thighs."
            "But now all of her attention is focussed on what's between my legs."
            "I gasp as Kat sits down on me and grabs hold of my cock with both hands."
            kat.say "There it is..."
            kat.say "Now let's have some fun with this thing!"
            "Kat underlines exactly what she means a moment later."
            "As I feel her press the head of my cock hard against the lips of her pussy."
            "She's moving up and down at the same time, working it as much as she can."
            show petite 4some fuckkat anna emma with fade
            "Anna and Emma don't need to hold me down any longer."
            "Because there's no way I'd ever want to escape what's happening to me."
            "I just lie as still as I possibly can, staring at what Kat's doing."
            "As aroused as I'm feeling right now, she can't be far behind me."
            "Because I can already tell that her pussy is getting warmer and wetter by the moment."
            "Kat starts to move faster too, increasing the pressure she's putting on it."
            "Things can't go on like this for too much longer, something has to give."
            "And when it does, Kat's the one that throws back her head, letting out a helpless moan."
            show petite 4some fuckkat vaginal kat_pleasure kat_blush at startle(0.05,-10)
            "She sinks down and onto me as she does so, not stopping until I'm all the way inside."
            "I have maybe a couple of seconds to reach out and take hold of Kat."
            "But then she starts to move in earnest, bouncing up and down atop me."
            show petite 4some fuckkat kat_normal at startle(0.05,-10)
            "Though she starts out slowly, Kat soon picks up speed."
            show petite 4some fuckkat at startle(0.05,-10)
            "And before long, she's going as fast as she possibly can."
            "I'm holding onto her more to keep her in place than to guide her."
            "Because I don't want her to fall off, and I also don't want it to stop!"
            show petite 4some fuckkat kat_pleasure at startle(0.05,-10)
            "Anna and Emma look on in stunned silence as Kat works herself into a frenzy."
            "Her hands caress her own body, travelling up and down at their leisure."
            "But they always seem to linger longest upon her pert little breasts."
            "Or else slide down the sides of her pussy."
            with vpunch
            "All of a sudden, Kat pushes down with all of her weight at once."
            with vpunch
            "And the effect on me is instant, as if she's hit the self-destruct switch."
            "Now my hands really are holding onto her, keeping her in place."
            menu:
                "Let them finish you off":
                    call petite_harem_event_04_sex_cumshare from _call_petite_harem_event_04_sex_cumshare_4
                "CUUUUUUUUUM":
                    show petite 4some fuckkat kat_ahegao cum with vpunch
                    "Because a moment later I lost it, shooting my load into her."
                    "I'm deep inside Kat when it happens, meaning that she takes it all."
                    "Nothing gets held back, and she's swept along with me, cumming too."
    return

label petite_harem_event_04_sex_cumshare:
    scene bg black
    show petite 4some cumshare emma_mouth_closed kat_mouth_closed anna_mouth_closed beach
    "Before I can let nature take it's course, the girls are hauling me onto my feet."
    "I barely have the time to glance around before I'm standing up on the stand."
    "And a moment later, they're kneeling in front of me."
    "Emma's in the middle, with Kat to her right and Anna to her left."
    "Though that's all I have the time to get straight in my head."
    "Because a mere second later, they leap into action."
    "As one, the girls reach out to take hold of my cock and balls."
    "Three pairs of hands, all working to play with a different part of me."
    "I've seen magicians do slight of hand tricks before."
    "But Anna, Emma and Kat come close to having them beat."
    "And what they do is certainly a kind of magic too!"
    "Once their hands have gotten me good and stiff, it's the turn of their mouths."
    show petite 4some cumshare emma_mouth_open kat_mouth_open anna_mouth_open
    "Lips, tongues and teeth coming into play to complete the task."
    "At first it's just kissing and licking, upping the ante from the hands."
    "But suddenly my cock disappears into Anna's mouth."
    "And as soon as it does, the whole mood changes."
    "The girls start to go ever faster, swapping it between them."
    "Their heads bob up and down, too fast for me to follow."
    "Something made worse by the effects their attentions are having on me."
    "By now my head is almost spinning with pleasure."
    "And I'm getting worried that I might become dizzy too."
    "So as crazy as it sounds, the feeling I'm about to cum is a relief!"
    "The girls seem to sense that it's time too, as they cease their efforts."
    "All three of them lean back, sitting on their haunches."
    "Then they wait patiently for the inevitable to happen."
    show petite 4some cumshare cum throb with hpunch
    "When it does, I make sure to move as I shoot my load."
    show petite 4some cumshare with hpunch
    "Doing the best I can to spread it over all three of their faces."
    show petite 4some cumshare facecum_emma emma_eyes_closed with hpunch
    "Being in the middle, Emma gets most of it lining her cheeks."
    show petite 4some cumshare facecum_emma facecum_anna facecum_kat emma_eyes_open anna_eyes_closed kat_eyes_closed with hpunch
    "Though Anna and Kat hardly seem to notice, revelling in all they get too."
    show petite 4some cumshare -cum -throb annahand kathand heart anna_eyes_lookmc kat_eyes_open
    "I watch as they hungrily lick it from their lips and then off each other's cheeks."
    "And suddenly I don't feel quite so faint as I did a moment before."
    return

label anna_emma_kat_propose_male:
    scene bg park with fade
    "Normally I'm on top of the world when I'm with Anna, Emma and Kat."
    "And why in the hell wouldn't I be?"
    "There can't be a guy that's into girls who wouldn't want to be in that position."
    "Three of the cutest girls in the world draped all over me, laughing at all of my jokes."
    "Well...most of them at least, you know?"
    "Okay, okay...maybe I have a fifty percent success rate at best."
    "But the important thing is that they like my company and I love theirs too."
    "Which is why I've decided that this is the day I make a play to keep it."
    "That I'm going to do something that will make sure Anna, Emma and Kat are all mine."
    show emma normal at center, zoomAt(1.0, (340, 720))
    show kat normal at center, zoomAt(1.0, (940, 720))
    show anna normal a at center, zoomAt(1.0, (640, 720))
    with easeinright
    "So when I spot the three of them walking together, I start walking along, slightly behind the three of them."
    "Doing the best I can to listen in as they talk amongst themselves."
    "All I'm waiting for is the perfect moment to leap into action."
    "The precise second when all the odds are in favour of success."
    show emma whining
    emma.say "It's just such a turn-off for me, you know?"
    show emma upset
    show anna talkative
    anna.say "What is?"
    show anna normal
    show emma angry
    emma.say "People not listening to me!"
    show emma upset
    show anna embarrassed
    anna.say "Oh, sorry, Emma..."
    anna.say "I wasn't paying attention just now."
    show emma surprised
    emma.say "What the..."
    emma.say "Are you being serious right now?"
    show emma annoyed
    show kat whining
    kat.say "I get what you're saying, I do..."
    show kat whinge
    kat.say "But you know what's even worse?"
    show emma whining
    emma.say "What's that?"
    show emma normal
    show anna talkative
    anna.say "I dunno, Kat..."
    anna.say "What is it?"
    show anna annoyed
    show kat defiant
    kat.say "People listening in on your private conversations!"
    show bg park at center, traveling(1.15, 0.2, (640, 800))
    show emma at center, traveling(1.25, 0.2, (340, 880))
    show kat normal at center, traveling(1.25, 0.2, (940, 880))
    show anna a at center, traveling(1.25, 0.2, (640, 880))
    "Kat stops and turns around as she says this."
    "Which means that I almost walk straight into her."
    with hpunch
    "But luckily for me, I somehow manage to stop myself before that happens."
    mike.say "Whoa..."
    mike.say "Watch out there, Kat..."
    mike.say "I nearly walked straight into you!"
    "Kat doesn't seem the least bit impressed with my warning."
    "Instead she stands there, arms crossed and staring at me."
    show kat angry
    kat.say "Nice try, [hero.name]..."
    kat.say "But we caught you in the act just now."
    kat.say "You were snooping on our conversation."
    show kat upset
    show emma annoyed
    show anna annoyed
    "I'm kind of thrown for a second time by the accusation."
    "Not least because it's actually not the truth of the matter."
    "I wasn't trying to overhear the conversation at all."
    "Just waiting for a convenient time to leap into action."
    "As my mind is kind of doing donuts in a wheatfield, I go onto autopilot."
    "Reaching into my pockets for what I have hidden in there."
    "Because my most basic instinct is it might explain the situation."
    "Which means that I end up thrusting my hands forwards."
    "A trio of matching rings spread across my palms for all to see."
    "As soon as that happens, I can feel the mood change."
    "Almost like it's something in the air that can be felt."
    show emma blank
    show anna normal
    show kat normal
    "Anna, Emma and Kat are all staring down at the rings."
    "Like they're hypnotised by the mere sight of them."
    show kat surprised
    kat.say "Are those..."
    show kat stuned
    show emma surprised
    emma.say "They certainly look like..."
    show emma blank
    show anna surprised
    anna.say "WEDDING RINGS!!!"
    anna.say "Oh my god...oh my fucking god!"
    anna.say "Who are those for?"
    show anna talkative
    anna.say "Who's getting married?!?"
    show anna normal
    show kat shocked
    kat.say "Who do you think, dumb-ass?"
    show kat stuned
    show anna sadsmile
    show emma surprised
    emma.say "[hero.name]'s proposing to all three of us!"
    show emma blank
    show anna normal
    "The moment of division that Anna's causing gives me the chance I need."
    "So I hastily get down on one knee, still holding out the rings."
    mike.say "Yes..."
    mike.say "Yes I am!"
    mike.say "So what do you say, girls?"
    mike.say "Will you marry me?"
    if anna.love >= 195 and emma.love >= 195 and kat.love >= 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Anna seems to come suddenly to life, shoving first Kat and then Emma on the shoulder."
        show anna talkative
        anna.say "What in the hell are you two waiting for?"
        anna.say "You want him to start begging or something?!?"
        show anna normal
        "Anna shakes her head as she turns to face me."
        show anna happy
        anna.say "I'll marry you, [hero.name]!"
        anna.say "Even if these guys are too dumb to say yes!"
        show anna normal
        "Anna snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Emma and Kat into action."
        "Because a moment later, they both make a move to do the same."
        "Which results in an undignified scramble for the last two rings."
        "Once all three of them have one on their finger, I get back up again."
        mike.say "So..."
        mike.say "I might be jumping to conclusions here."
        mike.say "But I'm going to take that as a yes then?"
        show anna happy
        "Anna looks triumphant, nodding her head at this."
        "But Emma and Kat look kind of sheepish."
        "Staring at their feet and refusing to meet my eye."
        show kat sadsmile
        kat.say "Yeah..."
        show kat happy
        kat.say "Sorry about that!"
        show kat smile
        show emma whining
        emma.say "Me too, [hero.name]..."
        show emma happy
        emma.say "I don't know what came over me!"
        show emma sad
        show anna talkative
        anna.say "Aah..."
        anna.say "Don't be such moping bitches!"
        show anna happy
        anna.say "We're all getting married - so we should be celebrating."
        show anna normal
        "I nod my head, keen to encourage Anna's positive vibe."
        show emma happy
        show kat happy
        "And it soon begins to spread to everyone else too."
        "As if finally dawns on us all they we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ anna.set_fiance()
        $ emma.set_fiance()
        $ kat.set_fiance()
    elif anna.love >= 195 and emma.love >= 195 and kat.love < 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Anna seems to come suddenly to life, shoving first Kat and then Emma on the shoulder."
        show anna talkative
        anna.say "What in the hell are you two waiting for?"
        anna.say "You want him to start begging or something?!?"
        show anna normal
        "Anna shakes her head as she turns to face me."
        show anna happy
        anna.say "I'll marry you, [hero.name]!"
        anna.say "Even if these guys are too dumb to say yes!"
        show anna normal
        "Anna snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Emma and Kat into action."
        show emma happy
        "Because a moment later, Emma reaches out and takes another one of the rings."
        show kat annoyed
        "But Kat shakes her head and takes a step backwards."
        mike.say "So..."
        mike.say "I might be jumping to conclusions here."
        mike.say "But I'm going to take that as a yes?"
        mike.say "At least from two of you..."
        show anna happy
        "Anna looks triumphant, nodding her head at this."
        "But Kat refuses to meet my eye, showing her embarrassment."
        show kat sadsmile
        kat.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        kat.say "Then it would be that much more simple to say yes."
        show kat sad
        show anna talkative
        anna.say "Ah, forget about her, [hero.name]..."
        show anna happy
        anna.say "We're getting married!"
        show anna normal
        show emma happy
        emma.say "She's right, let's start planning already!"
        show emma happy
        "I nod my head, keen to encourage Anna's positive vibe."
        "But all the same, I can't help worrying about Kat."
        "Though that feels hard to do as it begins to dawn on me that we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ anna.set_fiance()
        $ emma.set_fiance()
        $ kat.love -= 25
        $ kat.sub -= 25
    elif anna.love >= 195 and emma.love < 195 and kat.love >= 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Anna seems to come suddenly to life, shoving first Kat and then Emma on the shoulder."
        show anna talkative
        anna.say "What in the hell are you two waiting for?"
        anna.say "You want him to start begging or something?!?"
        show anna normal
        "Anna shakes her head as she turns to face me."
        show anna happy
        anna.say "I'll marry you, [hero.name]!"
        anna.say "Even if these guys are too dumb to say yes!"
        show anna normal
        "Anna snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Emma and Kat into action."
        show kat happy
        "Because a moment later, Kat reaches out and takes another one of the rings."
        show emma annoyed
        "But Emma shakes her head and takes a step backwards."
        mike.say "So..."
        mike.say "I might be jumping to conclusions here."
        mike.say "But I'm going to take that as a yes?"
        mike.say "At least from two of you..."
        "Anna looks triumphant, nodding her head at this."
        "But Emma refuses to meet my eye, showing her embarrasment."
        emma.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        emma.say "Then it would be that much more simple to say yes."
        show emma whining
        show anna normal
        anna.say "Ah, forget about her, [hero.name]..."
        show anna happy
        anna.say "We're getting married!"
        kat.say "She's right, let's start planning already!"
        "I nod my head, keen to encourage Anna's positive vibe."
        "But all the same, I can't help worrying about Emma."
        "Though that feels hard to do as it begins to dawn on me that we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ anna.set_fiance()
        $ kat.set_fiance()
        $ emma.love -= 25
        $ emma.sub -= 25
    elif anna.love >= 195 and emma.love < 195 and kat.love < 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Anna seems to come suddenly to life, shoving first Kat and then Emma on the shoulder."
        show anna talkative
        anna.say "What in the hell are you two waiting for?"
        anna.say "You want him to start begging or something?!?"
        "Anna shakes her head as she turns to face me."
        show anna talkative
        show anna happy
        anna.say "I'll marry you, [hero.name]!"
        anna.say "Even if these guys are too dumb to say yes!"
        "Anna snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Emma and Kat into action."
        "As one they take a step backwards, shaking their heads."
        show emma annoyed
        show kat annoyed
        emma.say "Oh, [hero.name]..."
        emma.say "That's very romantic of you."
        emma.say "But..."
        show emma blank
        show kat whining
        kat.say "But there's no way we can say yes."
        kat.say "No way that we can all marry you!"
        kat.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        kat.say "Then it would be that much more simple to say yes."
        show kat sad
        show emma whining
        emma.say "But with four different people in the mix..."
        emma.say "It's so much more complicated than that!"
        show emma sad
        show kat whining
        kat.say "Everything has to be one hundred percent perfect."
        show kat sad
        "I nod my head."
        "Beginning to tune into their way of thinking."
        "But before I can say a single word, Anna cuts into the conversation."
        show anna talkative
        anna.say "Ah, forget about them, [hero.name]..."
        anna.say "We're getting married!"
        show anna normal
        show kat sadsmile
        kat.say "She's right, let's start planning already!"
        show kat smile
        "I nod my head, keen to encourage Anna's positive vibe."
        "But all the same, I can't help worrying about Emma and Kat."
        "Though that feels hard to do as it begins to dawn on me that we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ anna.set_fiance()
        $ emma.love -= 25
        $ emma.sub -= 25
        $ kat.love -= 25
        $ kat.sub -= 25
    elif anna.love < 195 and emma.love >= 195 and kat.love >= 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Kat seems to come suddenly to life, shoving first Kat and then Anna on the shoulder."
        show kat annoyed
        kat.say "What in the hell are you two waiting for?"
        kat.say "You want him to start begging or something?!?"
        "Kat shakes her head as she turns to face me."
        show kat happy
        kat.say "I'll marry you, [hero.name]!"
        kat.say "Even if these guys are too dumb to say yes!"
        show kat smile
        "Kat snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Emma and Anna into action."
        show emma happy
        "Because a moment later, Emma reaches out and takes another one of the rings."
        show anna annoyed
        "But Anna shakes her head and takes a step backwards."
        mike.say "So..."
        mike.say "I might be jumping to conclusions here."
        mike.say "But I'm going to take that as a yes?"
        mike.say "At least from two of you..."
        "Emma looks triumphant, nodding her head at this."
        "But Anna refuses to meet my eye, showing her embarrasment."
        show anna worried
        anna.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        anna.say "Then it would be that much more simple to say yes."
        show anna sadsmile
        show kat smile
        kat.say "Ah, forget about her, [hero.name]..."
        show kat happy
        kat.say "We're getting married!"
        show anna normal
        show emma happy
        emma.say "She's right, let's start planning already!"
        show emma normal
        "I nod my head, keen to encourage Kat's positive vibe."
        "But all the same, I can't help worrying about Anna."
        "Though that feels hard to do as it begins to dawn on me that we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ emma.set_fiance()
        $ kat.set_fiance()
        $ anna.love -= 25
        $ anna.sub -= 25
    elif anna.love < 195 and emma.love >= 195 and kat.love < 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Emma seems to come suddenly to life, shoving first Kat and then Anna on the shoulder."
        show emma talkative
        emma.say "What in the hell are you two waiting for?"
        emma.say "You want him to start begging or something?!?"
        show emma annoyed
        "Emma shakes her head as she turns to face me."
        show emma happy
        emma.say "I'll marry you, [hero.name]!"
        emma.say "Even if these guys are too dumb to say yes!"
        show emma normal
        "Emma snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Anna and Kat into action."
        "As one they take a step backwards, shaking their heads."
        show anna talkative
        show kat annoyed
        anna.say "Oh, [hero.name]..."
        anna.say "That's very romantic of you."
        show anna worried
        anna.say "But..."
        show anna annoyed
        show kat whining
        kat.say "But there's no way we can say yes."
        kat.say "No way that we can all marry you!"
        kat.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        kat.say "Then it would be that much more simple to say yes."
        show kat sad
        show anna worried
        anna.say "But with four different people in the mix..."
        anna.say "It's so much more complicated than that!"
        show anna sad
        show kat whining
        kat.say "Everything has to be one hundred percent perfect."
        show kat sad
        "I nod my head."
        "Beginning to tune into their way of thinking."
        "But before I can say a single word, Emma cuts into the conversation."
        show emma normal
        emma.say "Ah, forget about them, [hero.name]..."
        show emma happy
        emma.say "We're getting married!"
        show emma normal
        "I nod my head, keen to encourage Emma's positive vibe."
        "But all the same, I can't help worrying about Anna and Kat."
        "Though that feels hard to do as it begins to dawn on me that we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ emma.set_fiance()
        $ anna.love -= 25
        $ anna.sub -= 25
        $ kat.love -= 25
        $ kat.sub -= 25
    elif anna.love < 195 and emma.love < 195 and kat.love >= 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But it's just when I feel my hope beginning to fade that something happens."
        "Kat seems to come suddenly to life, shoving first Anna and then Emma on the shoulder."
        show kat talkative
        kat.say "What in the hell are you two waiting for?"
        kat.say "You want him to start begging or something?!?"
        show kat annoyed
        "Kat shakes her head as she turns to face me."
        show kat happy
        kat.say "I'll marry you, [hero.name]!"
        kat.say "Even if these guys are too dumb to say yes!"
        show kat smile
        "Kat snatches one of the rings from my outstretched hand."
        "And then she shoves it onto her finger."
        "This seems to be enough to shake Emma and Anna into action."
        "As one they take a step backwards, shaking their heads."
        show anna annoyed
        show emma talkative
        emma.say "Oh, [hero.name]..."
        emma.say "That's very romantic of you."
        show emma whining
        emma.say "But..."
        show emma annoyed
        show anna worried
        anna.say "But there's no way we can say yes."
        anna.say "No way that we can all marry you!"
        anna.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        anna.say "Then it would be that much more simple to say yes."
        show anna annoyed
        show emma whining
        emma.say "But with four different people in the mix..."
        emma.say "It's so much more complicated than that!"
        show emma annoyed
        show anna worried
        anna.say "Everything has to be one hundred percent perfect."
        show anna annoyed
        "I nod my head."
        "Beginning to tune into their way of thinking."
        "But before I can say a single word, Kat cuts into the conversation."
        show kat smile
        kat.say "Ah, forget about them, [hero.name]..."
        show kat happy
        kat.say "We're getting married!"
        show kat smile
        "I nod my head, keen to encourage Kat's positive vibe."
        "But all the same, I can't help worrying about Emma and Anna."
        "Though that feels hard to do as it begins to dawn on me that we're going to be getting married."
        "At least as soon as I can convince myself this is really happening to me!"
        $ kat.set_fiance()
        $ anna.love -= 25
        $ anna.sub -= 25
        $ emma.love -= 25
        $ emma.sub -= 25
    elif anna.love < 195 and emma.love < 195 and kat.love < 195:

        "I watch, my eyes wide with hope, as the three of the exchange glances."
        "But I can feel that same hope beginning to fade as I read their expressions."
        "Well, at least the ones on Emma and Kat's faces."
        "Anna still seems to be as shell-shocked as before."
        show emma talkative
        emma.say "Oh, [hero.name]..."
        emma.say "That's very romantic of you."
        show emma whining
        emma.say "But..."
        show emma sad
        show kat whining
        kat.say "But there's no way we can say yes."
        kat.say "No way that we can all marry you!"
        show kat sad
        show anna surprised
        anna.say "Huh?"
        anna.say "There isn't?!?"
        "As one, Emma and Kat shoot Anna a hard look."
        show anna annoyed
        "And she responds my staring at the ground."
        "Letting me known that there'll be no more division in their ranks."
        mike.say "I don't understand, guys..."
        mike.say "Aren't we having a really great time together?"
        mike.say "You know, getting on like a house on fire?"
        mike.say "I thought marriage was the next logical step!"
        "I can see from the looks I'm getting that they don't agree."
        "But I still have to hold on to find out what their actual objection is."
        show kat sadsmile
        kat.say "Maybe if there was just two or three of us in this relationship, [hero.name]."
        kat.say "Then it would be that much more simple to say yes."
        show kat sad
        show emma whining
        emma.say "But with four different people in the mix..."
        emma.say "It's so much more complicated than that!"
        show emma sad
        show kat whining
        kat.say "Everything has to be one hundred percent perfect."
        show kat sad
        "I nod my head."
        "Beginning to tune into their way of thinking."
        mike.say "And you don't think we're there yet?"
        mike.say "We're not one hundred percent perfect?"
        show kat whining
        kat.say "No..."
        kat.say "But we're almost there!"
        show kat sad
        show emma whining
        emma.say "It wouldn't take much to make it, for sure."
        show emma sad
        show anna talkative
        anna.say "For the record, I thought we were nailing it!"
        anna.say "But I gotta go with the majority here."
        show anna sadsmile
        "I raise myself to a standing position as I take all of this in."
        "And I nod my head as I put the rings back into my pocket."
        mike.say "Okay, guys..."
        mike.say "If that's the way you want it."
        mike.say "I won't give you any excuse to say no next time I ask!"
        $ anna.love -= 25
        $ anna.sub -= 25
        $ emma.love -= 25
        $ emma.sub -= 25
        $ kat.love -= 25
        $ kat.sub -= 25
    return


label anna_emma_propose_male:
    scene bg park with fade
    "Normally I'm on top of the world when I'm out with Anna and Emma."
    "And why in the hell wouldn't I be?"
    "There can't be a guy that's into girls who wouldn't want to be in that position."
    "Two of the cutest girls in the world draped all over me, laughing at all of my jokes."
    "Well...most of them at least, you know?"
    "Okay, okay...maybe I have a fifty percent success rate at best."
    "But the important thing is that they like my company and I love theirs too."
    "Which is why I've decided that this is the day I make a play to keep it."
    "That I'm going to do something that will make sure Anna and Emma are all mine."
    "All I'm waiting for is the perfect moment to leap into action."
    "The precise second when all the odds are in favour of success."
    "So I'm walking along, slightly behind the three of them."
    "Doing the best I can to listen in as they talk amongst themselves."
    show emma whining at center, zoomAt(1.0, (440, 720))
    show anna normal a at center, zoomAt(1.0, (840, 720))
    with easeinright
    emma.say "It's just such a turn-off for me, you know?"
    show emma upset
    show anna talkative
    anna.say "What is?"
    show emma upset
    show anna embarrassed
    emma.say "People not listening to me!"
    show anna embarrassed
    anna.say "Oh, sorry, Emma..."
    anna.say "I wasn't paying attention just now."
    show emma surprised
    emma.say "What the..."
    emma.say "Are you being serious right now?"
    show emma annoyed
    show anna worried
    anna.say "Wait..."
    show anna worried
    anna.say "You know what's even worse?"
    show anna unpleased
    show emma whining
    emma.say "What's that?"
    show emma normal
    show anna angry
    anna.say "People listening in on your private conversations!"
    show bg park at center, traveling(1.15, 0.2, (640, 800))
    show emma at center, traveling(1.25, 0.2, (440, 880))
    show anna a unpleased at center, traveling(1.25, 0.2, (840, 880))
    "Anna stops and turns around as she says this."
    "Which means that I almost walk straight into her."
    with hpunch
    "But luckily for me, I somehow manage to stop myself before that happens."
    mike.say "Whoa..."
    mike.say "Watch out there, Anna..."
    mike.say "I nearly walked straight into you!"
    with hpunch
    "Anna doesn't seem the least bit impressed with my warning."
    "Instead she stands there, arms crossed and staring at me."
    show anna a talkative
    anna.say "Nice try, [hero.name]..."
    anna.say "But we caught you in the act just now."
    anna.say "You were snooping on our conversation."
    show anna a unpleased
    show emma annoyed
    "I'm kind of thrown for a second time by the accusation."
    "Not least because it's actually not the truth of the matter."
    "I wasn't trying to overhear the conversation at all."
    "Just waiting for a convenient time to leap into action."
    "As my mind is kind of doing donuts in a wheatfield, I go onto autopilot."
    "Reaching into my pockets for what I have hidden in there."
    "Because my most basic instinct is it might explain the situation."
    "Which means that I end up thrusting my hands forwards."
    "A pair of matching rings spread across my palms for all to see."
    "As soon as that happens, I can feel the mood change."
    "Almost like it's something in the air that can be felt."
    show emma blank
    show anna normal
    "Anna and Emma are staring down at the rings."
    "Like they're hypnotised by the mere sight of them."
    show emma surprised
    emma.say "They certainly look like..."
    show emma blank
    show anna surprised
    anna.say "WEDDING RINGS!!!"
    anna.say "Oh my god...oh my fucking god!"
    anna.say "Who are those for?"
    show anna talkative
    anna.say "Who's getting married?!?"
    show emma annoyed
    emma.say "Who do you think, dumb-ass?"
    show emma surprised
    emma.say "[hero.name]'s proposing to us!"
    show emma blank
    show anna normal
    "The moment of division that Anna's causing gives me the chance I need."
    "So I hastily get down on one knee, still holding out the rings."
    mike.say "Yes..."
    mike.say "Yes I am!"
    mike.say "So what do you say, Anna...Emma?"
    mike.say "Will you marry me?"
    if anna.love >= 195 and emma.love >= 195:
        "Anna's the first to react, leaping into the air and waving her arms."
        "And the next thing I know, she's snatched one of the rings out of my hand."
        show anna talkative
        anna.say "Oh yeah..."
        show anna happy
        anna.say "You'd better believe that I will!"
        show anna normal
        "At first Emma seems more than a little overwhelmed."
        "But eventually she shakes it off as Anna does a victory-lap around us both."
        show emma surprised
        emma.say "Oh..."
        show emma happy
        emma.say "I...I will too, [hero.name]!"
        show emma normal
        "I watch as Emma takes the second ring and slips it onto her finger."
        "And part of me can't actually believe that we're really getting married!"
        $ anna.set_fiance()
        $ emma.set_fiance()
    elif anna.love >= 195:
        "Anna's the first to react, leaping into the air and waving her arms."
        "And the next thing I know, she's snatched one of the rings out of my hand."
        show anna talkative
        anna.say "Oh yeah..."
        show anna happy
        anna.say "You'd better believe that I will!"
        show anna normal
        "At first Emma seems more than a little overwhelmed."
        "But eventually she shakes it off as Anna does a victory-lap around us both."
        show emma surprised
        emma.say "Oh, [hero.name]..."
        show emma whining
        emma.say "That's very romantic of you."
        emma.say "But..."
        emma.say "But there's no way we can say yes."
        show emma annoyed
        emma.say "No way that I marry you!"
        show emma sad
        "I feel like I've been slapped in the face."
        "And all I can do is try to find out the reason for the refusal."
        "But before I can say another word, Anna cuts me off."
        show anna talkative
        anna.say "Ah, forget about her, [hero.name]..."
        show anna happy
        anna.say "We're going to get married!"
        show anna normal
        "Much as I want to keep on talking things over with Emma, she's right."
        "And I feel myself getting swept up in the positive vibes of the whole thing."
        $ anna.set_fiance()
        $ emma.love -= 25
        $ emma.sub -= 25
    elif emma.love >= 195:
        "Anna's the first to react, shaking her head and backing off."
        show anna worried
        anna.say "There's no way we can say yes."
        anna.say "No way that we can both marry you!"
        show anna annoyed
        "Her words are so sudden and so final, it's like a slap across the face."
        "And they seem to have an instant effect on Emma too."
        "As she steps forwards and picks up one of the rings."
        "Then I watch as she slips it onto her finger."
        show emma annoyed
        emma.say "I can speak for myself, Anna."
        show emma happy
        emma.say "I...I will, [hero.name]!"
        show emma normal
        "I give Anna another look, hoping for an explanation."
        "And she shrugs, a helpless look on her face."
        show anna talkative
        anna.say "Maybe if there was just two of us in this relationship, [hero.name]."
        show anna embarrassed
        anna.say "Then it would be that much more simple to say yes."
        show anna normal
        "But before I can say another word, Emma cuts me off."
        show emma talkative
        emma.say "Does it really matter why she said no, [hero.name]?"
        show emma happy
        emma.say "We're going to get married!"
        show emma normal
        "Much as I want to keep on talking things over with Anna, she's right."
        "And I feel myself getting swept up in the positive vibes of the whole thing."
        $ emma.set_fiance()
        $ anna.love -= 25
        $ anna.sub -= 25
    elif anna.love < 195 and emma.love < 195:
        show emma talkative
        emma.say "Oh, [hero.name]..."
        emma.say "That's very romantic of you."
        show emma whining
        emma.say "But..."
        show emma sad
        show anna embarrassed
        anna.say "But there's no way we can say yes."
        anna.say "No way that we can both marry you!"
        show anna sad
        "I feel like I've been slapped in the face."
        "And all I can do is try to find out the reason for the refusal."
        mike.say "I don't understand, guys..."
        mike.say "Aren't we having a really great time together?"
        show anna normal
        show emma normal
        mike.say "You know, getting on like a house on fire?"
        mike.say "I thought marriage was the next logical step!"
        show anna worried
        anna.say "Maybe if there was just two of us in this relationship, [hero.name]."
        anna.say "Then it would be that much more simple to say yes."
        show anna embarrassed
        show emma whining
        emma.say "But with three different people in the mix..."
        emma.say "It's so much more complicated than that!"
        show emma annoyed
        "I nod my head."
        "Beginning to tune into their way of thinking."
        mike.say "And you don't think we're there yet?"
        mike.say "We're not one hundred percent perfect?"
        anna.say "No..."
        show anna talkative
        anna.say "But we're almost there!"
        anna.say "It wouldn't take much to make it, for sure."
        show anna normal
        show emma talkative
        emma.say "For the record, I thought we were nailing it!"
        show emma normal
        "I raise myself to a standing position as I take all of this in."
        "And I nod my head as I put the rings back into my pocket."
        mike.say "Okay, guys..."
        mike.say "If that's the way you want it."
        mike.say "I won't give you any excuse to say no next time I ask!"
        $ anna.love -= 25
        $ anna.sub -= 25
        $ emma.love -= 25
        $ emma.sub -= 25
    return

label anna_kat_propose_male:
    scene bg park with fade
    "Normally I'm on top of the world when I'm out with Anna and Kat."
    "And why in the hell wouldn't I be?"
    "There can't be a guy that's into girls who wouldn't want to be in that position."
    "Two of the cutest girls in the world draped all over me, laughing at all of my jokes."
    "Well...most of them at least, you know?"
    "Okay, okay...maybe I have a fifty percent success rate at best."
    "But the important thing is that they like my company and I love theirs too."
    "Which is why I've decided that this is the day I make a play to keep it."
    "That I'm going to do something that will make sure Anna and Kat are all mine."
    "All I'm waiting for is the perfect moment to leap into action."
    show kat normal at center, zoomAt(1.0, (840, 720))
    show anna normal a at center, zoomAt(1.0, (440, 720))
    with easeinright
    "The precise second when all the odds are in favour of success."
    "So I'm walking along, slightly behind the three of them."
    "Doing the best I can to listen in as they talk amongst themselves."
    show kat whining
    kat.say "It's just such a turn-off for me, you know?"
    show kat sad
    show anna talkative
    anna.say "What is?"
    show anna normal
    show kat angry
    kat.say "People not listening to me!"
    show anna embarrassed
    anna.say "Oh, sorry, Kat..."
    anna.say "I wasn't paying attention just now."
    show kat annoyed
    kat.say "What the..."
    kat.say "Are you being serious right now?"
    kat.say "Hum..."
    show kat whinge
    kat.say "You know what's even worse?"
    show anna normal
    anna.say "I dunno, Kat..."
    anna.say "What is it?"
    show anna embarrassed
    show kat defiant
    kat.say "People listening in on your private conversations!"
    show bg park at center, traveling(1.15, 0.2, (640, 800))
    show kat sad sad at center, traveling(1.25, 0.2, (840, 880))
    show anna a at center, traveling(1.25, 0.2, (440, 880))
    "Kat stops and turns around as she says this."
    "Which means that I almost walk straight into her."
    with hpunch
    "But luckily for me, I somehow manage to stop myself before that happens."
    mike.say "Whoa..."
    mike.say "Watch out there, Kat..."
    mike.say "I nearly walked straight into you!"
    "Kat doesn't seem the least bit impressed with my warning."
    "Instead she stands there, arms crossed and staring at me."
    show kat whining
    kat.say "Nice try, [hero.name]..."
    kat.say "But we caught you in the act just now."
    kat.say "You were snooping on our conversation."
    show kat annoyed
    show anna annoyed
    "I'm kind of thrown for a second time by the accusation."
    "Not least because it's actually not the truth of the matter."
    "I wasn't trying to overhear the conversation at all."
    "Just waiting for a convenient time to leap into action."
    "As my mind is kind of doing donuts in a wheatfield, I go onto autopilot."
    "Reaching into my pockets for what I have hidden in there."
    "Because my most basic instinct is it might explain the situation."
    "Which means that I end up thrusting my hands forwards."
    "A pair of matching rings spread across my palms for all to see."
    "As soon as that happens, I can feel the mood change."
    "Almost like it's something in the air that can be felt."
    show anna normal
    show kat normal
    "Anna and Kat are staring down at the rings."
    "Like they're hypnotised by the mere sight of them."
    show kat surprised
    kat.say "Are those..."
    kat.say "They certainly look like..."
    show kat stuned
    show anna surprised
    anna.say "WEDDING RINGS!!!"
    anna.say "Oh my god...oh my fucking god!"
    show anna talkative
    anna.say "Who are those for?"
    anna.say "Who's getting married?!?"
    show anna normal
    show kat angry
    kat.say "Who do you think, dumb-ass?"
    kat.say "[hero.name]'s proposing!"
    show kat annoyed
    "The moment of division that Anna's causing gives me the chance I need."
    "So I hastily get down on one knee, still holding out the rings."
    mike.say "Yes..."
    mike.say "Yes I am!"
    mike.say "So what do you say, Anna...Kat?"
    mike.say "Will you marry me?"
    if anna.love >= 195 and kat.love >= 195:
        "Anna's the first to react, leaping into the air and waving her arms."
        "And the next thing I know, she's snatched one of the rings out of my hand."
        show anna talkative
        anna.say "Oh yeah..."
        show anna happy
        anna.say "You'd better believe that I will!"
        show anna normal
        "At first Kat seems more than a little overwhelmed."
        "But eventually she shakes it off as Anna does a victory-lap around us both."
        show kat talkative
        kat.say "Oh..."
        show kat happy
        kat.say "I...I will too, [hero.name]!"
        show kat smile
        "I watch as Kat takes the second ring and slips it onto her finger."
        "And part of me can't actually believe that we're really getting married!"
        $ anna.set_fiance()
        $ kat.set_fiance()
    elif anna.love >= 195:
        "Anna's the first to react, leaping into the air and waving her arms."
        "And the next thing I know, she's snatched one of the rings out of my hand."
        show anna talkative
        anna.say "Oh yeah..."
        show anna happy
        anna.say "You'd better believe that I will!"
        show anna normal
        "At first Kat seems more than a little overwhelmed."
        "But eventually she shakes it off as Anna does a victory-lap around us both."
        show kat shocked
        kat.say "Oh, [hero.name]..."
        show kat talkative
        kat.say "That's very romantic of you."
        kat.say "But..."
        show kat sadsmile
        kat.say "But there's no way we can say yes."
        kat.say "No way that I marry you!"
        show kat annoyed
        "I feel like I've been slapped in the face."
        "And all I can do is try to find out the reason for the refusal."
        "But before I can say another word, Anna cuts me off."
        show anna talkative
        anna.say "Ah, forget about her, [hero.name]..."
        show anna happy
        anna.say "We're going to get married!"
        show anna normal
        "Much as I want to keep on talking things over with Kat, she's right."
        "And I feel myself getting swept up in the positive vibes of the whole thing."
        $ anna.set_fiance()
        $ kat.love -= 25
        $ kat.sub -= 25
    elif kat.love >= 195:
        "Anna's the first to react, shaking her head and backing off."
        show anna worried
        anna.say "There's no way we can say yes."
        anna.say "No way that we can both marry you!"
        show anna unpleased
        "Her words are so sudden and so final, it's like a slap across the face."
        "And they seem to have an instant effect on Kat too."
        "As she steps forwards and picks up one of the rings."
        "Then I watch as she slips it onto her finger."
        show kat annoyed
        kat.say "I can speak for myself, Anna."
        show kat happy
        kat.say "I...I will, [hero.name]!"
        show kat smile
        "I give Anna another look, hoping for an explanation."
        "And she shrugs, a helpless look on her face."
        show anna worried
        anna.say "Maybe if there was just two of us in this relationship, [hero.name]."
        anna.say "Then it would be that much more simple to say yes."
        show anna embarrassed
        "But before I can say another word, Kat cuts me off."
        show kat talkative
        kat.say "Does it really matter why she said no, [hero.name]?"
        show kat happy
        kat.say "We're going to get married!"
        show kat smile
        "Much as I want to keep on talking things over with Kat, she's right."
        "And I feel myself getting swept up in the positive vibes of the whole thing."
        $ kat.set_fiance()
        $ anna.love -= 25
        $ anna.sub -= 25
    elif anna.love < 195 and kat.love < 195:
        show kat talkative
        kat.say "Oh, [hero.name]..."
        kat.say "That's very romantic of you."
        show kat sadsmile
        kat.say "But..."
        show kat sad
        show anna worried
        anna.say "But there's no way we can say yes."
        anna.say "No way that we can both marry you!"
        show anna embarrassed
        "I feel like I've been slapped in the face."
        "And all I can do is try to find out the reason for the refusal."
        mike.say "I don't understand, guys..."
        mike.say "Aren't we having a really great time together?"
        show anna normal
        show kat normal
        mike.say "You know, getting on like a house on fire?"
        mike.say "I thought marriage was the next logical step!"
        show anna worried
        anna.say "Maybe if there was just two of us in this relationship, [hero.name]."
        anna.say "Then it would be that much more simple to say yes."
        show anna embarrassed
        show kat whining
        kat.say "But with three different people in the mix..."
        kat.say "It's so much more complicated than that!"
        show kat annoyed
        "I nod my head."
        "Beginning to tune into their way of thinking."
        mike.say "And you don't think we're there yet?"
        mike.say "We're not one hundred percent perfect?"
        show anna worried
        anna.say "No..."
        show anna talkative
        anna.say "But we're almost there!"
        anna.say "It wouldn't take much to make it, for sure."
        show anna normal
        show kat talkative
        kat.say "For the record, I thought we were nailing it!"
        show kat normal
        "I raise myself to a standing position as I take all of this in."
        "And I nod my head as I put the rings back into my pocket."
        mike.say "Okay, guys..."
        mike.say "If that's the way you want it."
        mike.say "I won't give you any excuse to say no next time I ask!"
        $ anna.love -= 25
        $ anna.sub -= 25
        $ kat.love -= 25
        $ kat.sub -= 25
    return


label emma_kat_propose_male:
    scene bg park with fade
    "Normally I'm on top of the world when I'm out with Emma and Kat."
    "And why in the hell wouldn't I be?"
    "There can't be a guy that's into girls who wouldn't want to be in that position."
    "Two of the cutest girls in the world draped all over me, laughing at all of my jokes."
    "Well...most of them at least, you know?"
    "Okay, okay...maybe I have a fifty percent success rate at best."
    "But the important thing is that they like my company and I love theirs too."
    "Which is why I've decided that this is the day I make a play to keep it."
    "That I'm going to do something that will make sure Emma and Kat are all mine."
    "All I'm waiting for is the perfect moment to leap into action."
    show emma normal at center, zoomAt(1.0, (440, 720))
    show kat normal at center, zoomAt(1.0, (840, 720))
    with easeinright
    "The precise second when all the odds are in favour of success."
    "So I'm walking along, slightly behind the three of them."
    "Doing the best I can to listen in as they talk amongst themselves."
    show emma whining
    emma.say "It's just such a turn-off for me, you know?"
    show emma upset
    show kat talkative
    kat.say "What is?"
    show kat normal
    show emma whining
    emma.say "People not listening to me!"
    show emma sad
    show kat confused
    kat.say "Oh, sorry, Emma..."
    kat.say "I wasn't paying attention just now."
    show emma annoyed
    emma.say "What the..."
    emma.say "Are you being serious right now?"
    kat.say "I get what you're saying, I do..."
    show kat whinge
    kat.say "But you know what's even worse?"
    show emma normal
    emma.say "What's that?"
    show kat defiant
    kat.say "People listening in on your private conversations!"
    show bg park at center, traveling(1.15, 0.2, (640, 800))
    show emma at center, traveling(1.25, 0.2, (440, 880))
    show kat normal at center, traveling(1.25, 0.2, (840, 880))
    "Kat stops and turns around as she says this."
    "Which means that I almost walk straight into her."
    with hpunch
    "But luckily for me, I somehow manage to stop myself before that happens."
    mike.say "Whoa..."
    mike.say "Watch out there, Kat..."
    mike.say "I nearly walked straight into you!"
    "Kat doesn't seem the least bit impressed with my warning."
    "Instead she stands there, arms crossed and staring at me."
    show kat whining
    kat.say "Nice try, [hero.name]..."
    kat.say "But we caught you in the act just now."
    kat.say "You were snooping on our conversation."
    show kat annoyed
    show emma annoyed
    "I'm kind of thrown for a second time by the accusation."
    "Not least because it's actually not the truth of the matter."
    "I wasn't trying to overhear the conversation at all."
    "Just waiting for a convenient time to leap into action."
    "As my mind is kind of doing donuts in a wheatfield, I go onto autopilot."
    "Reaching into my pockets for what I have hidden in there."
    "Because my most basic instinct is it might explain the situation."
    "Which means that I end up thrusting my hands forwards."
    "A pair of matching rings spread across my palms for all to see."
    "As soon as that happens, I can feel the mood change."
    "Almost like it's something in the air that can be felt."
    show emma normal
    show kat normal
    "Emma and Kat are staring down at the rings."
    "Like they're hypnotised by the mere sight of them."
    show kat surprised
    kat.say "Are those..."
    show kat stuned
    show emma surprised
    emma.say "They certainly look like..."
    show emma blank
    show kat shocked
    kat.say "Wedding rings!"
    show emma surprised
    emma.say "Oh my god...oh my fucking god!"
    emma.say "Who are those for?"
    emma.say "Who's getting married?!?"
    show emma blank
    show kat annoyed
    kat.say "Who do you think, dumb-ass?"
    kat.say "[hero.name]'s proposing!"
    show kat normal
    "The moment of division that Emma's causing gives me the chance I need."
    "So I hastily get down on one knee, still holding out the rings."
    mike.say "Yes..."
    mike.say "Yes I am!"
    mike.say "So what do you say, Emma...Kat?"
    mike.say "Will you marry me?"
    if emma.love >= 195 and kat.love >= 195:
        "Kat's the first to react, leaping into the air and waving her arms."
        "And the next thing I know, she's snatched one of the rings out of my hand."
        show kat smile
        kat.say "Oh yeah..."
        show kat happy
        kat.say "You'd better believe that I will!"
        show kat smile
        "At first Emma seems more than a little overwhelmed."
        "But eventually she shakes it off as Kat does a victory-lap around us both."
        show emma talkative
        emma.say "Oh..."
        show emma happy
        emma.say "I...I will too, [hero.name]!"
        show emma normal
        "I watch as Emma takes the second ring and slips it onto her finger."
        "And part of me can't actually believe that we're really getting married!"
        $ emma.set_fiance()
        $ kat.set_fiance()
    elif emma.love >= 195:
        "Kat's the first to react, shaking her head and backing off."
        show kat whining
        kat.say "There's no way we can say yes."
        show kat sadsmile
        kat.say "No way that we can both marry you!"
        show kat sad
        "Her words are so sudden and so final, it's like a slap across the face."
        "And they seem to have an instant effect on Emma too."
        "As she steps forwards and picks up one of the rings."
        "Then I watch as she slips it onto her finger."
        show emma talkative
        emma.say "I can speak for myself, Kat."
        show emma happy
        emma.say "I...I will, [hero.name]!"
        show emma normal
        "I give Kat another look, hoping for an explanation."
        "And she shrugs, a helpless look on her face."
        show kat sadsmile
        kat.say "Maybe if there was just two of us in this relationship, [hero.name]."
        kat.say "Then it would be that much more simple to say yes."
        show kat sad
        "But before I can say another word, Emma cuts me off."
        show emma talkative
        emma.say "Does it really matter why she said no, [hero.name]?"
        show emma happy
        emma.say "We're going to get married!"
        show emma normal
        "Much as I want to keep on talking things over with Kat, she's right."
        "And I feel myself getting swept up in the positive vibes of the whole thing."
        $ emma.set_fiance()
        $ kat.love -= 25
        $ kat.sub -= 25
    elif kat.love >= 195:
        "Kat's the first to react, leaping into the air and waving her arms."
        "And the next thing I know, she's snatched one of the rings out of my hand."
        show kat talkative
        kat.say "Oh yeah..."
        show kat happy
        kat.say "You'd better believe that I will!"
        show kat smile
        "At first Emma seems more than a little overwhelmed."
        "But eventually she shakes it off as Kat does a victory-lap around us both."
        show emma talkative
        emma.say "Oh, [hero.name]..."
        emma.say "That's very romantic of you."
        show emma whining
        emma.say "But..."
        emma.say "But there's no way we can say yes."
        emma.say "No way thatI marry you!"
        show emma annoyed
        "I feel like I've been slapped in the face."
        "And all I can do is try to find out the reason for the refusal."
        "But before I can say another word, Kat cuts me off."
        show kat talkative
        kat.say "Ah, forget about her, [hero.name]..."
        show kat happy
        kat.say "We're going to get married!"
        show kat smile
        "Much as I want to keep on talking things over with Emma, she's right."
        "And I feel myself getting swept up in the positive vibes of the whole thing."
        $ kat.set_fiance()
        $ emma.love -= 25
        $ emma.sub -= 25
    elif emma.love < 195 and kat.love < 195:
        show kat talkative
        kat.say "Oh, [hero.name]..."
        kat.say "That's very romantic of you."
        show kat sadsmile
        kat.say "But..."
        show emma whining
        emma.say "But there's no way we can say yes."
        emma.say "No way that we can both marry you!"
        show emma annoyed
        "I feel like I've been slapped in the face."
        "And all I can do is try to find out the reason for the refusal."
        mike.say "I don't understand, guys..."
        mike.say "Aren't we having a really great time together?"
        show emma normal
        show kat normal
        mike.say "You know, getting on like a house on fire?"
        mike.say "I thought marriage was the next logical step!"
        show kat whining
        kat.say "Maybe if there was just two of us in this relationship, [hero.name]."
        kat.say "Then it would be that much more simple to say yes."
        show kat sadsmile
        show emma talkative
        emma.say "But with three different people in the mix..."
        show emma whining
        emma.say "It's so much more complicated than that!"
        show emma annoyed
        "I nod my head."
        "Beginning to tune into their way of thinking."
        mike.say "And you don't think we're there yet?"
        mike.say "We're not one hundred percent perfect?"
        show kat whining
        kat.say "No..."
        show kat sadsmile
        kat.say "But we're almost there!"
        kat.say "It wouldn't take much to make it, for sure."
        show kat smile
        show emma talkative
        emma.say "For the record, I thought we were nailing it!"
        show emma normal
        "I raise myself to a standing position as I take all of this in."
        "And I nod my head as I put the rings back into my pocket."
        mike.say "Okay, guys..."
        mike.say "If that's the way you want it."
        mike.say "I won't give you any excuse to say no next time I ask!"
        $ emma.love -= 25
        $ emma.sub -= 25
        $ kat.love -= 25
        $ kat.sub -= 25
    return


label anna_emma_kat_male_ending:

    if renpy.has_label("petite_harem_achievement_3") and not game.flags.cheat:
        call petite_harem_achievement_3 from _call_petite_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I'm standing at the altar, looking back over my shoulder."
    "And it's pretty obvious that I'm waiting for my brides to turn up."
    "As I gaze down the aisle, I can see the pews in the chapel are full."
    "Anna, Emma, Kat and I have all made sure to invite our friends and family."
    "So the upshot of that is everyone else in there waiting impatiently too."
    "When I hear the music begin to play, a flood of relief washes over me."
    "Because that's the exact tune that I remember them picking."
    "The one that all three of them wanted to come down the aisle to."
    "But even when the chapel doors open, I still don't see any sign of them."
    "For a moment I'm total thrown, wondering if they all decided to stand me up."
    "It's then that I notice a change in the rows at the very of the chapel."
    "Heads are turning back there, following something passing by them."
    "Of course - the guests in the pews are pretty much all around average height."
    "Whereas Anna, Emma and Kat are all way shorter than that."
    "It's not that my trio of brides aren't there."
    "It's just that they're too short to be seen yet!"
    "So instead of puzzling over what's happening, I wait a moment longer."
    "And then, when the angle from which I'm looking changes, I see the walk into view."
    show anna b wedding zorder 1 at center, zoomAt (1.0, (340, 740))
    show emma wedding zorder 3 at center, zoomAt (1.0, (640, 740))
    show kat wedding smile zorder 2 at center, zoomAt (1.0, (940, 740))
    show anna zorder 1 at center, traveling(1.5, 5.0, (340, 1040))
    show emma zorder 3 at center, traveling(1.5, 5.0, (640, 1040))
    show kat zorder 2 at center, traveling(1.5, 5.0, (940, 1040))
    "Anna, Emma and Kat are walking in an almost perfect line, three abreast."
    "They never bothered to tell me they were going to be doing that."
    "The most I knew was that they'd be coming down the aisle together."
    "So I guess that they wanted to make a statement in this way."
    "To show that they're all equal and united in what we're doing here today."
    "But still, I can't help noticing the unique and individual charms each one possesses."
    "Of course, Anna's the most forward and upbeat of the three."
    "Practically beaming as she walks towards me."
    if anna.is_visibly_pregnant:
        "I'm relieved to see that Anna's holding onto her belly."
        "Because she's really starting to show now."
        "And I'm always worried about keeping her and the baby as safe as possible."
    else:
        "In fact Anna's moving so quickly that I'm worried she's going to trip and fall."
        "She seems to be rushing in an effort to get here as fast as she possibly can!"
    "Emma's walking with far more care and awareness of her surroundings."
    "In fact I'm amazed that she can keep up with Anna at all."
    if emma.is_visibly_pregnant:
        "I steal a second to glance at the curve of Emma's belly."
        "Proud of the fact that we're going to be parents."
        "Proud of the fact that all of us are going to be a family."
    else:
        "I honestly never thought this moment would come."
        "And in just a few moments time, we're going to be married!"
    "Last, but by no means least is Kat, walking with more confidence than Emma."
    "But maybe not as much of a genuine swagger as Anna."
    if kat.is_visibly_pregnant:
        "Even the delicate curve of Kat's belly looks damn good to me."
        "Making a subtle statement of the fact that she's pregnant."
        "Rather than shoving the fact into the face of anyone that sees her."
    else:
        "But she's one of the three most beautiful girl in the world to my eyes."
        "And just looking at her tells me I'm one hell of a lucky guy!"
    "Like I said before, Anna's hurrying a little ahead of the others."
    "But then Emma and Kat seem to realise they're being left behind."
    "And they put on a last minute burst of speed, catching up to her."
    "Which means that all three of them arrive at the alter together."
    show anna b happy
    anna.say "Hey, [hero.name]!"
    show anna b normal
    show emma happy
    emma.say "Oh my god..."
    emma.say "We're actually doing this!"
    show emma blush
    show kat talkative
    kat.say "Yeah..."
    kat.say "Shit suddenly got real!"
    show kat smile
    mike.say "Tell me about it!"
    "The four of us are already beginning to strike up a conversation at the altar."
    "The natural chemistry that brought us together smoothing over our nerves."
    "But in our need to chatter away, we've obviously forgotten where we are right now."
    "Priest" "Ahem..."
    "At the sound of the priest's voice, everyone snaps out of it."
    "In fact we almost jump to attention in perfect time with each other."
    "Priest" "Well..."
    "Priest" "Now that I have your undivided attention..."
    "Priest" "Perhaps we can get things underway?"
    "This earns the priest a round of nods from the four of us."
    "But he hardly seems to notice them."
    "Which makes me think the question was academic in nature."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these four people..."
    "Priest" "In the bonds of holy matrimony."
    "Look, I know there are four of us standing up here right now."
    "One devastatingly handsome guy and three really got girls."
    "But the majority of the stuff that's being said is the same as usual."
    "It's just that there's more of it thanks to the additional bodies involved."
    "Things only really starts to pick up once we get into the vows."
    "You know, the good stuff?"
    "Priest" "Do you, Anna..."
    "Priest" "Take Emma, Kat and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show anna b happy at startle
    anna.say "You bet I do!"
    show anna b normal
    "Priest" "Do you, Emma..."
    "Priest" "Take Anna, Kat and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show emma happy at startle
    emma.say "I totally do!"
    show emma blush
    "Priest" "Do you, Kat..."
    "Priest" "Take Anna, Emma and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show kat happy at startle
    kat.say "Of course I do!"
    show kat smile
    "The priest nods as all of the girls recite their vows."
    "But when he turns to me, the guy seems to be a little out of breath."
    "He holds up a hand and lets out a horse chuckle, shaking his head."
    "Priest" "A moment, please?"
    "Priest" "I'm not as young as I used to be."
    "Priest" "And these multiple weddings do rather take it out of me!"
    "There's a quiet ripple of laughter from the guests."
    "And I nod to let the priest know that I appreciate his predicament."
    "Priest" "Alright..."
    "Priest" "Do you, [hero.name]..."
    "Priest" "Take Anna, Emma and Kat..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "The priest nods with satisfaction."
    "Priest" "Then it is my duty to call on all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these people may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "Of course the guests enjoy a moment of subtle laughter."
    "But for Anna, Emma, Kat and I it's just a little more tense."
    "None of us is really expecting anything dramatic to happen."
    "Yet there's always that fear you might have forgotten something."
    "Or else one of us might have a skeleton in the closet they've kept to themselves."
    "After all, there are four of us involved in this marriage."
    "And that's a hell of a lot of history crammed into one small space!"
    "But thankfully the moment passes without incident."
    "I feel myself letting out a breath I didn't know I'd been holding in."
    "Priest" "Very good..."
    "Priest" "I now have the pleasure of pronouncing you all married."
    "Priest" "You may celebrate in a manner of your choosing."
    "Priest" "So long as it doesn't outrage anyone present!"
    "The priest adds a knowing wink as he says this."
    "But I'm swamped by my brides before I can say a word."
    show anna b happy zorder 1 at center, traveling(2.0, 0.3, (340, 1340))
    show emma happy zorder 3 at center, traveling(2.0, 0.3, (640, 1340))
    show kat happy blush zorder 2 at center, traveling(2.0, 0.3, (940, 1340))
    "Anna, Emma and Kat wrap me in a four-way embrace."
    "And once that happens, I forget about everyone else in the chapel."
    "There might be words spoken in those moments, but I can't hear them."
    "Because my senses are filled with the way I'm being touched."
    "And my head is swimming with the realisation that we actually did it."
    "I'm married to my trio of petite goddesses!"
    "Which makes me feel like I've already won in the game of life."
    "So anything that comes along after this is more like a bonus."
    scene petite ending with fade
    kat.say "It's pretty simple, guys..."
    kat.say "We just talk about out lives with [hero.name]."
    kat.say "Like, before we met him and how we started dating him."
    emma.say "Then where all of it lead to?"
    emma.say "Like a kind of epilogue to the story?"
    kat.say "That's exactly it, Emma."
    anna.say "But what's the point in that?"
    anna.say "We already know all of that stuff."
    kat.say "It's not supposed to be for us, Anna..."
    kat.say "We're telling the story to other people."
    emma.say "But Anna's got a point, doesn't she?"
    emma.say "There's only us around here."
    emma.say "And it's not like we can send an email or a text, now is it?"
    anna.say "Ooh..."
    anna.say "Emails and texts - I remember those!"
    kat.say "No worries, guys..."
    kat.say "I have a pencil and some paper right here."
    kat.say "Once we're done, we seal it up in this here bottle."
    emma.say "You're serious?"
    emma.say "You're going to toss that thing into the sea?"
    anna.say "Like a message in a bottle?!?"
    kat.say "Literally a message in a bottle!"
    kat.say "I mean, we can't be sure anyone will ever read it."
    kat.say "But that's not really the point, is it?"
    emma.say "I guess not!"
    anna.say "Okay, okay..."
    anna.say "Me first!"
    anna.say "I met [hero.name] when he started hanging around my band, The Deathless Harpies."
    anna.say "And at first I thought he was into the other girls in the band."
    anna.say "You know, the taller ones?"
    kat.say "Nah, he definitely has a thing for us shorties!"
    kat.say "I hated him at first, you know that?"
    kat.say "He was competing against me and my former gaming partner."
    kat.say "Along with that blonde housemate of his, yeah?"
    emma.say "You mean the tall one?"
    anna.say "Wasn't she called Gouda or something else cheesy?"
    kat.say "Like that matters now!"
    kat.say "But even after he beat me, I couldn't let it go."
    kat.say "At first I thought I just hated his ass."
    kat.say "But then I realised that I was actually attracted to him!"
    emma.say "Yeah, he'll do that to ya!"
    emma.say "Did I ever tell you that he said he saw me in his dreams?"
    emma.say "Which is either totally amazing, or a total come-on line!"
    emma.say "Luckily for him, we got on pretty well in the real, non-dream world too!"
    kat.say "So..."
    kat.say "Let's talk about the elephant in the room, shall we?"
    kat.say "Or more like the elephant on the island, in our case!"
    anna.say "WHAT?!?"
    anna.say "Since when was there an elephant around here?"
    emma.say "Figure of speech, Anna!"
    emma.say "She means a big issue we don't always talk about."
    anna.say "Oh..."
    anna.say "You mean [hero.name] seeing all of us at once, don't you!"
    anna.say "Well, I was kind of used to that sort of thing."
    anna.say "We were always swapping guys and girls in the band!"
    kat.say "You guys know that I used to be a streamer on the side."
    kat.say "So I wasn't too far behind you in those stakes, Anna."
    kat.say "I mean, I needed [hero.name] to understand that part of my life."
    kat.say "So I couldn't just demand that he behave like a saint, could I?"
    emma.say "Yeah..."
    emma.say "It sounds easy for you guys to say that."
    emma.say "But I was never into any of those scenes before I met [hero.name]."
    emma.say "So I found the idea of sharing him with other girls really tough."
    emma.say "Though I think it being you two made things a little easier!"
    kat.say "We were all gettin along so well, weren't we?"
    kat.say "We got married and had all those plans worked out."
    kat.say "But then we got on that damn plane to fly off for a honeymoon that never happened."
    anna.say "Oh, Kat..."
    anna.say "Do we have to talk about the plane?"
    anna.say "I still have flashbacks to that day!"
    emma.say "It's okay, Anna..."
    emma.say "We're only talking about what happened in passing."
    emma.say "I promise we won't go into the details of it again."
    anna.say "Okay..."
    anna.say "But I still don't know how we made it out of an actual plane crash!"
    kat.say "I guess we were just lucky, Anna..."
    kat.say "We all made it out alive and managed to swim to this island."
    emma.say "Yeah, marooned on an actual desert island!"
    emma.say "You couldn't make that up."
    anna.say "But life here's not so bad, is it?"
    anna.say "We all built the shack we live in."
    anna.say "And we have enough coconuts to last us for years to come."
    if all([girl.flags.mikeBabies < 1 and not girl.is_visibly_pregnant for girl in [anna, emma, kat]]):
        anna.say "Plus I think [hero.name] wants to add to the population too!"
        anna.say "He certainly spends a lot of his time trying to get us involved..."
        emma.say "Yeah..."
        emma.say "And I don't like it when he jokes about starting his own tribe of little people either!"
        kat.say "Urgh..."
        kat.say "He thinks that's SO funny too!"
    else:
        if anna.flags.mikeBabies >= 1 or anna.is_visibly_pregnant:
            anna.say "Plus this is a safe place for Tommy to grow up."
            anna.say "Not like the shitty neighbourhood I was brought up in!"
        if emma.flags.mikeBabies >= 1 or emma.is_visibly_pregnant:
            emma.say "I was always worrying about what schools I'd be able to get my kids into."
            emma.say "But since Emily was born here, none of that stuff matters."
            emma.say "Which I think means I'm worrying about more important things instead."
        if kat.flags.mikeBabies >= 1 or kat.is_visibly_pregnant:
            kat.say "I know that Mario's growing up strong and healthy on this island."
            kat.say "And I'm actually glad he won't have videogames to play on."
            kat.say "As much of a hypocrite as that makes me!"
    kat.say "But aside from the bad jokes, I can't say life here is all that bad."
    kat.say "The island is beautiful in the day, and the sunsets are to die for."
    emma.say "I think the company helps too, you know?"
    emma.say "It just being the three of us girls and [hero.name]."
    anna.say "Oh, I totally agree with that one."
    anna.say "I don't have to put up with assholes that I hate around here!"
    emma.say "But [hero.name] is always talking about that boat he wants to make."
    emma.say "The one he's sure will get us all back to civilisation."
    kat.say "Oh, I wouldn't get too worried about that, Emma."
    kat.say "[hero.name] couldn't have made the shack without all of us helping him."
    anna.say "And even I know enough about boats to be to make one sink!"
    kat.say "So we're not going to be going anywhere soon."
    kat.say "Not unless we want to!"
    scene bg black with dissolve
    pause 0.3
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
