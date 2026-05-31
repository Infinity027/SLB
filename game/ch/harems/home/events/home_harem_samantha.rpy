init python:
    SpecificTalkSubject(**{
    "name": "ask_bree_about_sam",
    "display_name": "About Sam",
    "label": "ask_bree_about_sam",
    "duration": 0,
    "icon": "button_samantha",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Or(
                IsFlag("ongoinghomeharem", "samantha"),
                IsFlag("ongoinghomeharem", False),
                ),
            ),
        PersonTarget(bree,
            IsActive(),
            InHarem('home'),
            IsFlag("sam_home_harem", False),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsFlag("nonexclusive", True, 'harem'),
            Not(InHarem("home")),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "ask_sasha_about_sam",
    "display_name": "About Sam",
    "label": "ask_sasha_about_sam",
    "duration": 0,
    "icon": "button_samantha",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Or(
                IsFlag("ongoinghomeharem", "samantha"),
                IsFlag("ongoinghomeharem", False),
                ),
            ),
        PersonTarget(sasha,
            IsActive(),
            InHarem('home'),
            IsFlag("sam_home_harem", False),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsFlag("nonexclusive", True, 'harem'),
            Not(InHarem("home")),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "ask_minami_about_sam",
    "display_name": "About Sam",
    "label": "ask_minami_about_sam",
    "duration": 0,
    "icon": "button_samantha",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Or(
                IsFlag("ongoinghomeharem", "samantha"),
                IsFlag("ongoinghomeharem", False),
                ),
            ),
        PersonTarget(minami,
            IsActive(),
            InHarem('home'),
            IsFlag("sam_home_harem", False),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsFlag("nonexclusive", True, 'harem'),
            Not(InHarem("home")),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    CallEvent(**{
    "name": "introduce_sam_to_girls",
    "label": "introduce_sam_to_girls",
    "priority": 250,
    "conditions": [
        IsHour(0, 18),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("ongoinghomeharem", "samantha"),
            ),
        PersonTarget(samantha,
            IsActive(),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("sam_home_harem"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("sam_home_harem"),
            ),
        Or(
            PersonTarget(minami,
                Not(InHarem('home')),
                ),
            PersonTarget(minami,
                IsGone(),
                ),
            PersonTarget(minami,
                Not(IsActivity("sleep")),
                IsFlag("sam_home_harem"),
                ),
            ),
        ],
    })

    Event(**{
    "name": "sexual_tension_bree_sam",
    "label": "sexual_tension_bree_sam",
    "priority": 500,
    "conditions": [
        "samantha.room == bree.room",
        GameTarget(IsFlag("sexual_tension", False)),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    }
    )

    Event(**{
    "name": "lesbian_sex_bree_sam",
    "label": "lesbian_sex_bree_sam",
    "priority": 500,
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(1, 5),
        IsDone("sexual_tension_bree_sam"),
        HeroTarget(
            IsGender("male"),
            IsActivity("knock_bedroom2")),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            MinStat("lesbian", 10),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            MinStat("lesbian", 10),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_month": True,
    }
    )

    Event(**{
    "name": "sexual_tension_sam_lexi",
    "label": "sexual_tension_sam_lexi",
    "priority": 500,
    "conditions": [
        "Person.find('lexi') and samantha.room == lexi.room",
        GameTarget(IsFlag("sexual_tension", False)),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        PersonTarget("lexi",
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    }
    )

    Event(**{
    "name": "lesbian_sex_sam_lexi",
    "label": "lesbian_sex_sam_lexi",
    "priority": 500,
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(1, 5),
        IsDone("sexual_tension_sam_lexi"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(samantha,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        PersonTarget("lexi",
            Not(IsHidden()),
            IsRoom("livingroom"),
            MinStat("lesbian", 10),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_month": True,
    }
    )

    Event(**{
    "name": "sexual_tension_sam_sasha",
    "label": "sexual_tension_sam_sasha",
    "priority": 500,
    "conditions": [
        "samantha.room == sasha.room",
        GameTarget(IsFlag("sexual_tension", False)),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    }
    )

    Event(**{
    "name": "lesbian_sex_sam_sasha",
    "priority": 500,
    "label": "lesbian_sex_sam_sasha",
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(1, 5),
        IsDone("sexual_tension_sam_sasha"),
        HeroTarget(
            IsGender("male"),
            IsActivity("knock_bedroom3")),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            MinStat("lesbian", 10),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            MinStat("lesbian", 10),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_month": True,
    }
    )

    Event(**{
    "name": "sexual_tension_sam_minami",
    "label": "sexual_tension_sam_minami",
    "priority": 500,
    "conditions": [
        "samantha.room == minami.room",
        GameTarget(IsFlag("sexual_tension", False)),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    }
    )

    Event(**{
    "name": "lesbian_sex_sam_minami",
    "label": "lesbian_sex_sam_minami",
    "priority": 500,
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(1, 5),
        IsDone("sexual_tension_sam_minami"),
        HeroTarget(
            IsGender("male"),
            IsActivity("knock_bedroom5")),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsRoom("bedroom5"),
            MinStat("lesbian", 10),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            IsRoom("bedroom5"),
            MinStat("lesbian", 10),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_month": True,
    }
    )

    InteractEvent(**{
    "name": "home_harem_confession_to_sam",
    "label": "home_harem_confession_to_sam",
    "priority": 250,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsTimeOfDay("evening"),
            IsFlag("ongoinghomeharem", "samantha"),
            ),
        PersonTarget(samantha,
            IsActive(),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsFlag("sam_home_harem"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsFlag("sam_home_harem"),
            ),
        Or(
            PersonTarget(minami,
                Not(InHarem('home')),
                ),
            PersonTarget(minami,
                IsGone(),
                ),
            PersonTarget(minami,
                InHarem('home'),
                IsFlag("sam_home_harem"),
                ),
            ),
        ],
    })

    Event(**{
    "name": "samantha_sharing_bed",
    "label": "samantha_sharing_bed",
    "duration": 0,
    "conditions": [
        IsTimeOfDay("night"),
        Or(
            And(
                IsDone("introduce_sam_to_girls"),
                'DONE["introduce_sam_to_girls"] + 7 <= game.days_played'
                ),
            And(
                IsDone("home_harem_confession_to_sam"),
                'DONE["home_harem_confession_to_sam"] + 7 <= game.days_played'
                ),
            ),
        HeroTarget(
            IsGender("male"),
            IsActivity("sleep"),
            ),
        PersonTarget(samantha,
            InHarem('home'),
            Not(IsHidden()),
            HasRoomTag("home"),
            ),
        ],
    "chances": 33,
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "tv_bj_bree_samantha_sasha",
    "label": "tv_bj_bree_samantha_sasha",
    "priority": 500,
    "conditions": [
        IsTimeOfDay("evening", "night"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            InHarem('home'),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            InHarem('home'),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            HasRoomTag("home"),
            InHarem('home'),
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "samantha_sasha_pregnant_showdown",
    "label": "samantha_sasha_pregnant_showdown",
    "duration": 1,
    "conditions": [
        Not(TogetherInHarem('home', 'samantha', 'sasha')),
        PersonTarget(samantha,
                IsPresent(),
                IsVisiblyPregnant(),
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                ),
        PersonTarget(sasha,
                IsPresent(),
                IsVisiblyPregnant(),
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                ),
        HeroTarget(
            IsGender("male"),
            ),
        ],
    "do_once": True,
    })


label ask_bree_about_sam:
    "I guess I should count myself lucky right now - well, if I'm honest, REALLY lucky!"
    "I mean, in Sam I have the girl that I always wanted, the one that I thought got away."
    "But at the same time, I'm living something that most guys only dream of too."
    "I'm in a relationship with all of the girls that moved in after she moved out!"
    "Not only that, but when Sam found out about it, she was totally cool."
    "All she asked was for full disclosure - that I tell her who I'm fucking and when."
    "Most guys would want to leave things just as they are right now, would think it was perfect."
    "Well, you can accuse me of being dumb if you like."
    "But I can see a way in which things could be just that little bit better."
    "What if Sam were in on what I have going with the girls living in the house with me?"
    "All I have to do is convince them that it's a great idea."
    "And how hard could that be?"
    show bree with dissolve
    "Pretty soon, the chance arises to broach the subject with [bree.name]..."
    mike.say "Ah, hey, [bree.name]!"
    show bree happy
    bree.say "Oh, hi, [hero.name]."
    show bree normal
    show fx question
    bree.say "Is there something the matter?"
    mike.say "Huh...what?"
    mike.say "No...why...should there be?"
    show bree happy at startle
    "[bree.name] can't help bursting into a peal of giggles at this."
    "My being so easily flustered seems to amuse her greatly."
    bree.say "Honestly, [hero.name] - you're so easy to see through."
    bree.say "You might as well hang a sign round your neck!"
    mike.say "Ah...okay, [bree.name], you got me."
    mike.say "I admit it - there is kind of something the matter."
    "Upon hearing this, a distinct change comes over [bree.name]."
    show bree normal
    "She becomes more serious, almost concerned."
    "And she devotes all of her attention to me, waiting to hear what I have to say."
    "Wow, what a girl."
    "I'm lucky to be living with her, let alone in a relationship!"
    bree.say "I'm listening, [hero.name]."
    bree.say "What's the matter, huh?"
    mike.say "Well, you remember Sam?"
    mike.say "She lived here before you moved in."
    show bree annoyed
    "[bree.name] looks thoughtful for a moment."
    show bree normal
    "But then she nods."
    bree.say "I remember you telling me all about her and Ryan."
    bree.say "And I think you introduced me to her once."
    bree.say "But now that I think about it, that might have been one of the girl's you work with!"
    mike.say "Yeah, [bree.name], whatever."
    mike.say "The thing is that I always held a bit of a torch for her."
    mike.say "And she split up with Ryan recently too."
    show bree sad
    bree.say "Aw, that's a shame."
    mike.say "Yeah, I guess you could call it that..."
    mike.say "She needed a friend, and well..."
    mike.say "I kind of wound up being a bit more than that to her!"
    if "samantha_event_D05" in DONE or "samantha_event_D05B" in DONE:
        show bree surprised
        "[bree.name] looks at me with a shocked expression on her face."
        bree.say "Oh my god!"
        show fx question
        bree.say "Were you her revenge fuck?!?"
        mike.say "You could say that, yeah!"
    else:
        show bree annoyed
        show fx question
        bree.say "You've been sleeping with her?"
    mike.say "I'm sorry to tell you like this..."
    show bree normal
    bree.say "Oh, that's okay."
    mike.say "Y...you mean that?!?"
    "[bree.name] rolls her eyes at me, as though I just said something really stupid."
    bree.say "I might have been pissed before now."
    bree.say "But let's just say that what we've been doing together kind of broadened my mind!"
    "I'm about to express my immense feeling of relief."
    show bree evil
    "But I see a sudden change in [bree.name]'s expression."
    show bree at center, zoomAt (1.25, (640, 900))
    "She leans towards me in a conspiratorial manner, as if afraid of being overheard."
    bree.say "Wait, isn't she the one you're always calling 'cupcake'?"
    mike.say "Erm, yeah - that's my nickname for her."
    mike.say "Because she's so sweet and delicious..."
    "Am I imagining it, or is [bree.name] starting to look almost...furtive?"
    show bree flirt blush
    "She keeps looking this way and that, like she's embarrassed."
    "And I could swear that her hands are straying towards what's between her thighs too!"
    bree.say "[hero.name]..."
    bree.say "What's...what's she like?"
    show bree mouthful
    bree.say "You know - what's she like in bed?"
    "I can't believe what I'm hearing."
    "[bree.name]'s actually fishing for details of my conquests."
    "And ones that have been going on behind her back at that!"
    "Almost without a conscious thought, my brain seizes on the opportunity."
    mike.say "How about I go one better than telling you?"
    mike.say "How about I actually show you?"
    show bree surprised
    bree.say "Show me?"
    show fx question
    bree.say "But how?"
    mike.say "How about we let Sam in on what we have going on in the house?"
    mike.say "That way everyone gets to have some serious fun, right?"
    show fx question
    bree.say "Do...do you think we could?"
    "That's it, she's taken the bait."
    "All I need to do now is reel her in!"
    mike.say "Well, I'd be up for it and I'm sure Sam could be persuaded."
    mike.say "We just need to talk to everyone first, get them all on board."
    mike.say "But don't worry - I can take care of that."
    "[bree.name] nods happily, even kisses me on the cheek."
    "It feels better to know that she's committed to the idea."
    "And that I really only had to prod her in the right direction to make it so..."
    $ bree.flags.sam_home_harem = True
    return

label ask_sasha_about_sam:
    "You might think that a guy in my rather unique position might be ready to call it quits."
    "After all, I am currently in a relationship with my rather hot female housemates."
    "As if that wasn't enough, I've also managed to win Sam's heart too."
    "And she's special, the one that I thought had got away."
    "Even when I thought I'd blown it, when she found out I was seeing other girls, it didn't end."
    "I mean, can you actually believe that?"
    "I confessed that I was sleeping with other women, and she said she was okay with it!"
    "But maybe I'm just a perfectionist, or else some kind of masochist."
    "Because I thought of a way things could be even better."
    "What if Sam joined in the fun that we've been having at home?"
    "What if she became a part of the relationship I have with my housemates?"
    "Trust me, I know that this isn't going to be easy."
    "There are a lot of unique personalities involved in my scheme."
    "Perhaps the most unique of all being Sasha."
    show sasha with dissolve
    "Which is why I'm pretty nervous when I manage to corner her and broach the matter."
    "I know that Sasha's the most forthright and feminist of my housemates."
    "And so she might object on the grounds of my exploiting her gender."
    "Never mind be enraged by the knowledge that I've been screwing other women!"
    mike.say "Hey Sasha."
    mike.say "How are you doing?"
    "Sasha gives me one of her familiar smiles."
    "The kind that are half genuine warmth and half implied mischief."
    sasha.say "Hey there, stud!"
    sasha.say "I can't complain."
    sasha.say "And you?"
    show sasha joke
    sasha.say "How are you holding up as the only dick in the mix?"
    "I make a point of laughing at Sasha's little joke."
    "But all the same, I'm worried that it sounds more than a little forced."
    mike.say "Ha...yeah..."
    mike.say "What can I say - it's tough, but rewarding!"
    mike.say "Actually, Sasha...I kind of wanted to talk to you about that."
    show sasha annoyed
    "Sasha frowns a little at this, cocking her head on one side."
    sasha.say "You serious, [hero.name]?"
    sasha.say "In that case, shouldn't we all be in on this?"
    mike.say "No, I don't think so, Sasha."
    mike.say "This is the kind of thing I want to tackle one-on-one, yeah?"
    sasha.say "Okay, [hero.name]."
    sasha.say "But I've got to say - you're starting to make me nervous!"
    "I can see that she's telling the truth."
    "And I know that this is the point where I could blow it all."
    "But I'm committed now, and there's no backing out."
    mike.say "The thing is, Sasha..."
    mike.say "You remember Sam?"
    sasha.say "Yeah, I remember - she lived here before [bree.name] and I moved in."
    mike.say "That's right."
    mike.say "Well, we kept in touch after that, just as friends."
    show sasha normal
    sasha.say "But let me guess - you wanted more than that?"
    mike.say "Wha..."
    mike.say "How did you know?"
    show fx drop
    sasha.say "It's a bit of a cliche, [hero.name]."
    sasha.say "Almost every girl can spot that in a guy."
    sasha.say "The irony is that the only one who can't is usually the girl he's in love with!"
    mike.say "Whatever..."
    mike.say "What happened was that she broke up with her husband."
    mike.say "He was screwing around behind her back and she needed a friend to lean on."
    "At this, Sasha leans back a little, narrowing her eyes."
    "She studies me for a few moments."
    "And it's as she's if weighing up what I've said, as well as what I haven't."
    sasha.say "Yeah, but that's not the whole of it, right?"
    if "samantha_event_D05" in DONE or "samantha_event_D05B" in DONE:
        sasha.say "Let me guess - she wanted to get back at this guy?"
        show sasha flirt
        sasha.say "And you just happened to be there, still nursing your little crush on her?"
        "I can feel my cheeks flushing red as Sasha puts me on the spot."
        "How can she see through me so easily?"
        "Am I really that transparent?"
    mike.say "I...I've been sleeping with her, Sasha."
    mike.say "I'm sorry."
    show sasha surprised
    "Sasha surprises me then, her grin turning positively wolfish."
    sasha.say "Whoa!"
    show fx exclamation
    sasha.say "You dog, you!"
    mike.say "Y...you don't sound very upset, Sasha."
    mike.say "Aren't you pissed at me sleeping around?"
    show sasha normal
    sasha.say "I might have been once."
    sasha.say "You know, before we started getting other people involved in our love life?"
    sasha.say "But now I really don't see fucking like I used to."
    sasha.say "I guess it taught me to separate the emotion of love from the act of sex."
    show sasha happy
    sasha.say "Just because you screw someone else, it doesn't mean you love me any less."
    sasha.say "And anyway, you didn't force yourself on this Sam, did you?"
    mike.say "No...of course not!"
    show sasha flirt
    if "samantha_event_D05" in DONE or "samantha_event_D05B" in DONE:
        sasha.say "And you were helping her to stick it to her lousy husband too."
        sasha.say "Actually, she sounds like a pretty sound kind of girl!"
        "Shocked as I am by Sasha's reaction, I still know an opportunity when I hear one."
    else:
        sasha.say "In fact, she looks like my kind of girl."
    mike.say "You think so?"
    mike.say "Sam sounds like your kind of girl?"
    "Sasha nods, beginning to see that I'm going somewhere with this."
    mike.say "In that case, what do you say we extend an invitation to her?"
    mike.say "Because I was thinking that she could fit into what we have going on here in the house."
    "Sasha looks as though she's about to say yes."
    "But then she comes over all thoughtful."
    show sasha annoyed
    sasha.say "We can't decide that between the two of us."
    sasha.say "Everyone needs to have their say."
    "I nod, already noting Sasha's answer down as a conditional yes."
    mike.say "Sure thing, Sasha."
    mike.say "But I think we're both on the same page, yeah?"
    show sasha normal
    "Sasha nods at this, and I feel a weight lift off of my shoulders."
    "That's one step closer to getting Sam through the door!"
    $ sasha.flags.sam_home_harem = True
    return

label ask_minami_about_sam:
    "While Sam might be okay with me seeing other girls on the side, that only solves half of the problem."
    "I still need to convince [bree.name], Sasha and Minami that it's cool for me to be seeing Sam too!"
    "That's why I need to get her in on the relationship that we have going under our roof right now."
    "I mean, there's got to be room for one more, surely?"
    "Divide and conquer seems to be the best option, rather than tackling them all at once."
    "That way I can focus on each of them individually, not have them gang up on me."
    "And Minami strikes me as being one of the easiest to deal with."
    "After all, she's the youngest and most rebellious of the three."
    "Didn't she already mark her card as being into wild shit since she moved in here?"
    "Point one, she's in a relationship with me, her own adopted brother."
    "And point two, she wanted to hop in bed with me and my two housemates!"
    "So what's another body in the mix?"
    show minami with dissolve
    "But as I find Minami and broach the subject, I'm hoping to god that I'm right!"
    mike.say "Hey, Minami."
    show minami happy
    minami.say "Hey, big bro."
    show minami normal
    minami.say "What's up with you?"
    mike.say "Uh...n...nothing, Minami..."
    mike.say "Nothing at all - I just wanted to talk to you!"
    show minami annoyed
    minami.say "Yeah, yeah, whatever!"
    minami.say "I know when you want something, big bro."
    minami.say "You get all sneaky."
    minami.say "And you try to cover it up by acting innocent too!"
    "Knowing that I've been found out, I hold up my hands in a gesture of surrender."
    mike.say "Okay, Minami, okay."
    mike.say "You got me."
    mike.say "I do want something."
    show minami hunt
    "Minami gives me a smile worthy of a satisfied cat."
    "A smile that reminds me of just how sexy she is when she's gloating."
    minami.say "Yes - I KNEW it!"
    minami.say "So what is it this time, huh?"
    show minami tehe
    minami.say "It better be something really naughty!"
    "I nod, taking a deep breath as I prepare to spill my guts."
    mike.say "Did I ever mention Sam?"
    mike.say "One of the people that lived here before [bree.name] and Sasha?"
    show minami normal
    "Minami wrinkles her nose, trying to put a face to the name."
    "But then she shakes her head and shrugs her shoulders."
    minami.say "I think you dropped her name a couple of times."
    minami.say "But I probably wasn't listening at the time."
    mike.say "Well, the thing is that I've kinda been dating her for a while."
    "It takes a couple of seconds for the implications of what I just said to sink in."
    "But then Minami's eyes go wide, and she gasps in shock at the revelation."
    minami.say "Oh, big bro..."
    "I wince unconsciously, expecting her to burst into tears and pound me with her fists."
    show minami tehe
    show fx exclamation
    minami.say "You're SUCH a stud!"
    minami.say "Like...is a there any girl that you can't get?!?"
    "I feel like gasping in relief as I see the look that's growing in Minami's eyes."
    "Just like I hoped, she seems excited by the idea of me sleeping around."
    "And I can tell from her body language that it's actually starting to turn her on too!"
    if samantha.flags.divorced:
        mike.say "Aw...well..."
        mike.say "It's not like that really..."
        mike.say "She was married to this jerk called Ryan - and I was there for her!"
        show minami normal
        show fx question
        minami.say "You got it on with a married woman?!?"
        minami.say "Ooh...that makes it even more amazing!"
    else:
        show minami normal
    mike.say "The thing is, Minami..."
    mike.say "I want to let Sam in on what we have, you know?"
    mike.say "What we have with [bree.name] and Sasha?"
    show minami happy
    minami.say "That'd be great, big bro!"
    minami.say "Like you've caught her and brought her home to us."
    minami.say "Like she's kind of a trophy or something!"
    "I nod, relieved to hear Minami so happy at the prospect of Sam joining our foursome."
    mike.say "Okay, I just need to talk to the others."
    mike.say "Hopefully they'll feel the same way too."
    "Now it's Minami's turn to nod, as if them saying yes is just a formality."
    "But I wish I had her confidence that it's going to go that way..."
    $ minami.flags.sam_home_harem = True
    return

label introduce_sam_to_girls:
    "So, all of my housemates are up to speed on the situation with Sam and want her on board."
    "Which means that we're ready to move on to the next stage of the operation."
    "But just how do I go about telling Sam that I'm sleeping with all of them?"
    "And worse, how do I pitch the idea that she should get involved as well?"
    "Call me unimaginative, but the best I can come up with is just to tell her all about it."
    play sound phone_calling
    "So I call her up and act innocent, hoping for the best..."
    stop sound
    samantha.say "Hey, [hero.name]!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake."
    else:
        mike.say "Hey, Sam."
    mike.say "Are you free this afternoon?"
    samantha.say "Erm, yeah, I think so."
    samantha.say "Nothing that I can't cancel for you!"
    samantha.say "What's up?"
    samantha.say "Are you springing a surprise date on me, or what?"
    mike.say "Ah...not unless you coming over here to hang out counts!"
    samantha.say "Oh, sure thing, [hero.name]."
    samantha.say "I'll see you soon, okay?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Okay, Cupcake - see you later."
    else:
        mike.say "Okay, Sam - see you later."
    "It's only when I end the call that I look up and see that I have an audience."
    "The girls are watching me intently, their heads peeking around the nearest doorway."
    show bree annoyed with dissolve
    bree.say "Hey, why didn't you tell her about us?"
    if Harem.find(minami, name='home'):
        show minami annoyed at left with dissolve
        minami.say "Yeah, big bro - what gives?"
    show sasha annoyed at right with dissolve
    sasha.say "Way to chicken out!"
    mike.say "What...wait..."
    mike.say "How long have you guys been eavesdropping?!?"
    show bree evil
    bree.say "Long enough to know that you need our help."
    if Harem.find(minami, name='home'):
        show minami tehe at left
        minami.say "Trust me, you REALLY do!"
    show sasha joke at right
    sasha.say "Don't worry about a thing, [hero.name]."
    sasha.say "We got this!"
    hide sasha
    hide bree
    hide minami
    with dissolve
    "And with that, they disappear from sight."
    "Which leaves me standing there, still clutching my phone."
    mike.say "Wait a minute..."
    mike.say "What in the hell does that even mean?!?"
    "I don't get any kind of answer from the girls, as they remain tight-lipped."
    "But one thing I do know is that it means I now have another reason to be nervous."
    scene bg black with timelaps
    $ game.pass_time(1)
    scene bg livingroom with timelaps
    "So when the time comes for me to answer the door to Sam, I'm feeling rather jumpy."
    "Not only do I have to worry about telling her I'm in a polygamous relationship."
    "I also have no idea how the others are planning to let her know the exact same thing!"
    "All the same, I force a smile onto my face as I open the front door."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show samantha
    with wiperight
    samantha.say "Hey, [hero.name]."
    samantha.say "I'd have gotten here sooner, but..."
    samantha.say "Well, short notice and all that!"
    if samantha.flags.nickname == "cupcake":
        mike.say "No problem, Cupcake."
    else:
        mike.say "No problem, Sam."
    mike.say "Come on in."
    "I'm trying my best not to look paranoid as I let Sam in."
    "There's no sign of the others yet, but I'm not letting my guard down."
    "They could be lurking anywhere, plotting anything!"
    scene bg livingroom
    show samantha
    with fade
    "Which is why it kind of comes as a surprise to walk into the sitting room and find them there."
    "But the strangest thing of all is that they're just acting like there's nothing up."
    "[bree.name]'s playing on the Zbox, seemingly oblivious to the world at large."
    "Sasha's sat on the sofa, engrossed in a book that's resting in her lap."
    if Harem.find(minami, name='home'):
        "And Minami's scrolling through social media on her phone, as quiet as a mouse."
    samantha.say "Oh..."
    show fx exclamation
    samantha.say "I didn't know your housemates were going to be in too!"
    samantha.say "I kind of thought we'd have the place to ourselves."
    "At the sound of Sam's voice, the others all stop what they're doing."
    "They look up, pleasant smiles and expressions of vague interest on their faces."
    "All of which makes me narrow my eyes in expectation."
    "Because I know full well that it's nothing more than an act on their part."
    if samantha.flags.nickname == "cupcake":
        mike.say "It's okay, Cupcake."
    else:
        mike.say "It's okay, Sam."
    show samantha at right with move
    mike.say "We can head to my room instead."
    mike.say "At least that way we can get some privacy!"
    "I make a point of glaring at the others as I say this."
    "But all it earns me is a round of infuriatingly innocent smiles."
    show sasha joke a behind bree at left:
        xoffset -150
    sasha.say "Hah - good luck with that!"
    if Harem.find(minami, name='home'):
        show minami happy a behind bree at left:
            xoffset 150
        minami.say "Yeah, the walls here are like paper thin."
    show bree wink a at left
    bree.say "We can hear EVERYTHING that [hero.name] does in that room, trust me!"
    "Sam looks more than a little surprised at what she's hearing."
    "So I do my best to step in and make the save."
    mike.say "Ah...haha..."
    if samantha.flags.nickname == "cupcake":
        mike.say "They're joking, Cupcake!"
    else:
        mike.say "They're joking, Sam!"
    mike.say "You know [bree.name] and Sasha, right?"
    mike.say "I mentioned them before, I think..."
    if Harem.find(minami, name='home'):
        "Minami makes a huffing sound at being left out of the introduction."
        mike.say "Oh, and Minami, of course!"
    show sasha normal
    sasha.say "Don't worry, Sam."
    sasha.say "Even if this rude jerk never told you about us, he definitely told us about you!"
    show bree normal
    bree.say "Yeah, you're the one that got away, right?"
    if Harem.find(minami, name='home'):
        show minami normal
        minami.say "Big bro was always kinda hooked on you!"
    "Sam's eyes go wide at all of this, and she casts a questioning glance at me."
    "And I just know she's wondering what else I've been saying about her to these guys."
    show samantha blush
    samantha.say "I...I feel like I'm at a disadvantage here."
    samantha.say "Like you all know far more about me than I do about you!"
    sasha.say "Well, it's like that when you live under the one roof."
    bree.say "Yeah, we spend so much time in each other's pockets."
    if Harem.find(minami, name='home'):
        minami.say "You just can't keep a secret, no matter how hard you try!"
    if samantha.flags.nickname == "cupcake":
        mike.say "You know what, Cupcake - maybe we should go outside?"
    else:
        mike.say "You know what, Sam - maybe we should go outside?"
    mike.say "We could sit by the pool and chat."
    "Sam nods at this."
    "But before she can speak a word, [bree.name] cuts in."
    bree.say "Oh, I was going to take a dip when I finished this game."
    bree.say "But I promise that I won't cramp your style."
    samantha.say "I...well..."
    sasha.say "She has to ask, because some people are so prudish."
    show sasha joke
    sasha.say "You know - when it comes to skinny-dipping in broad daylight!"
    if Harem.find(minami, name='home'):
        show minami tehe
        minami.say "We do it all the time around here."
        minami.say "So it's like no big deal for us!"
    "Sam's openly gaping at me by now, wondering what she's let herself in for."
    "This was supposed to be a casual afternoon of hanging out and chilling."
    "And it's quickly turning into the prelude to an orgy!"
    if samantha.flags.nickname == "cupcake":
        mike.say "It's not like they make it sound, Cupcake - really it's not!"
    else:
        mike.say "It's not like they make it sound, Sam - really it's not!"
    mike.say "I mean, the back yard's pretty secluded."
    mike.say "So nobody would see that you were naked."
    mike.say "Not that I'm saying anyone will be!"
    show sasha happy
    show bree happy at startle
    if Harem.find(minami, name='home'):
        show minami happy
    "The others are laughing openly now, amused by how flustered I'm getting."
    "Sam seems to be more confused than anything else."
    "But the important thing is that she's neither mad nor freaked out."
    "At least not yet..."
    show sasha normal
    sasha.say "Don't worry, Sam."
    sasha.say "We're just screwing with you."
    show bree evil
    bree.say "Yeah, we always bust his chops like this."
    if Harem.find(minami, name='home'):
        show minami tehe
        minami.say "We do it to all the girls he brings home!"
    show samantha normal
    samantha.say "Ah, okay..."
    samantha.say "If you guys say so!"
    sasha.say "We're not that bad, Sam."
    sasha.say "We're really like best friends."
    bree.say "We share everything with each other too."
    if Harem.find(minami, name='home'):
        minami.say "Clothes, make-up and stuff..."
    sasha.say "And [hero.name]'s cock!"
    "It takes a moment for what Sasha just said to fully sink in, it sounds so casual."
    "But then awareness dawns in Sam's eyes, and she takes a sharp breath of surprise."
    "Everyone in the room seems to fall silent, holding their breath in anticipation."
    "This is it, the moment when we all learn what Sam has to say about our unusual relationship..."
    show samantha annoyed
    samantha.say "It's...it's you guys."
    show fx question at right
    samantha.say "It is, isn't it?"
    samantha.say "You're the girls that [hero.name]'s been seeing on the side?"
    show sasha normal
    sasha.say "Well, that's your take on it, yeah?"
    show bree normal
    bree.say "From our point of view, it's kinda the other way round!"
    if Harem.find(minami, name='home'):
        show minami normal
        minami.say "Yeah, he's been seeing you on the side, girlfriend!"
    if samantha.flags.nickname == "cupcake":
        mike.say "I'm sorry, Cupcake."
    else:
        mike.say "I'm sorry, Sam."
    mike.say "I was trying to pick my moment to tell you."
    mike.say "Honestly I was!"
    sasha.say "Yeah, but he'd have taken forever."
    bree.say "So we decided to do it for him."
    if Harem.find(minami, name='home'):
        minami.say "Yeah, he needed a kick in the pants!"
    show samantha normal
    "Sam nods at this, beginning to look thoughtful."
    samantha.say "Well, I guess I was the one that said I was cool with it."
    samantha.say "And now that you clued me in, I stand by what I said."
    samantha.say "I've got no problem with you guys hooking up."
    show fx question at right
    samantha.say "What about you though?"
    samantha.say "Are you okay with me getting a share of him?"
    "Sam nods in my direction almost as an afterthought."
    "And I can't help beginning to feel like a piece of meat here!"
    mike.say "Well..."
    if samantha.flags.nickname == "cupcake":
        mike.say "It's about more than just being cool with it, Cupcake."
    else:
        mike.say "It's about more than just being cool with it, Sam."
    mike.say "You see, we've talked it through."
    mike.say "And we want to ask if you'll join us."
    show sasha flirt
    sasha.say "The more the merrier, Sam."
    show bree wink
    bree.say "We want to see how the cupcake tastes too!"
    if Harem.find(minami, name='home'):
        show minami hunt
        minami.say "We can make room for big bro's other girl!"
    "For a moment, I honestly don't know what Sam's answer will be."
    "At one time I would have thought she'd say no without hesitation."
    "But the way her relationship with Ryan ended in such an acrimonious mess."
    "Well, it seems to have changed her in more ways than one."
    "She's somehow more adventurous and willing to take risks."
    "And I think I can see that same quality in her eyes right now."
    samantha.say "You know, it wasn't Ryan wanting to fuck other girls that ended our marriage."
    samantha.say "It was his not being honest enough to tell me he wanted to fuck other girls."
    samantha.say "If he's just come right out and asked me, I might actually have said yes!"
    mike.say "D...does that mean you're saying yes now?"
    "Sam looks me in the eye, smiling as if the answer were obvious."
    samantha.say "Well, do you see me getting mad or throwing things, storming out of here?"
    show samantha happy
    samantha.say "The fact that I'm still standing here answers that question, doesn't it?"
    "Almost as one, the other girls are up and on their feet."
    "They rush over to Sam, wrapping her in their arms and hugging her as close as possible."
    show sasha happy
    sasha.say "Welcome, Sam!"
    show bree happy
    bree.say "We have SO much to talk about!"
    if Harem.find(minami, name='home'):
        show minami happy
        minami.say "Wow - three big sisters!"
    "All I can do is stand back and watch in stunned silence."
    "There they are, the most beautiful girls I could ever hope to meet."
    "And they're all willing to share themselves with each other - and me!"
    "I hardly notice the huge, dumb smile that's spread across my face."
    "But really, with the thought of what lies ahead, can you blame me?"
    $ Harem.join_by_name("home", "samantha")

    $ minami.flags.sam_home_harem = True
    $ game.flags.ongoinghomeharem = False
    $ samantha.flags.schedule = "harem"
    $ game.pass_time(1)
    if Harem.find(minami, name='home'):
        call fivesome_breeminamisamsasha from _call_fivesome_breeminamisamsasha_4
        call sleep (["bree", "minami", "samantha", "sasha"]) from _call_sleep_fivesome_breeminamisamsasha
    else:
        call foursome_breesamsasha from _call_foursome_breesamsasha_3
        call sleep (["bree", "samantha", "sasha"]) from _call_sleep_foursome_breesamsasha
    return

label sexual_tension_bree_sam:
    "I confess that I've been a little more alert and aware of what's going on in the house recently."
    "Listening in on conversations and analysing what people are saying more deeply than normal."
    "But that's only because I'm worried about how well Sam is settling in now that she's back living here."
    "I mean, it's got to be weird, coming back here after breaking up with Ryan and all that stress."
    "Having all those memories on top of the stress she's going through right now..."
    "Well, let's just say it's got to be hard for her, you know?"
    "That's why I'm surprised to hear the sound of laughter as I walk past a doorway."
    "I recognise the familiar sound of the laughter and can't help looking into the room."
    scene expression "bg " + samantha.room
    show bree happy at left5
    show samantha happy at right5
    with fade
    "And that's when I see Sam and [bree.name], chatting and giggling away like old friends."
    "Pleased to see that they're getting on, I pause to listen in on the conversation."
    samantha.say "Oh no, [bree.name]..."
    samantha.say "This place HAS changed since I was last here."
    show samantha normal
    samantha.say "For one thing, I like what you guys have done with the decor."
    show bree normal
    bree.say "Really, Sam?"
    bree.say "That's the one thing you're stuck on?"
    bree.say "Like, all we did was paint a couple of walls and buy some cheap furniture!"
    show samantha happy at startle
    "Sam lets out a peal of laughter."
    "Then she puts a hand on top of [bree.name]'s."
    samantha.say "Oh, [bree.name]..."
    samantha.say "That's so cute"
    show samantha flirt at right4 with move
    samantha.say "You think I was just talking about the decoration!"
    show bree flirt
    "I see [bree.name]'s eyes go wide and she stares down at Sam's hand on her own."
    "At the same time I can see her cheeks flushing red too!"
    "But I can also see that [bree.name]'s not pulling her hand away either."
    "In fact, as I watch from the doorway, I see her start to smile!"
    "Are...are they flirting with each other?"
    "I'm almost leaning into the room by now, eager to see what's happening."
    "And what pushes me over the edge is the gesture that [bree.name] makes next."
    show bree at left4 with move
    "She slowly pulls her hand out from under Sam's."
    "Then she uses the same hand to smooth her hair behind her ear."
    "At the same time she's still smiling at Sam too!"
    "I know that look and those moves - that's one hundred percent a flirting thing!"
    "Almost without thinking, I walk into the room."
    mike.say "Hey, you guys!"
    mike.say "Great to see you chatting and getting on."
    mike.say "What were you talking about?"
    show samantha surprised
    show bree surprised
    "Sam and [bree.name] both look a little surprised to see me."
    show samantha normal
    show bree normal
    "But neither of them seems to be embarrassed either."
    "They don't leap apart like I was expecting them to."
    "Instead it's all calm and casual, like they're not in the least bit concerned."
    bree.say "Oh yeah, [hero.name]..."
    bree.say "Sam and I have been having a good get to know you session."
    show bree wink
    bree.say "Just swapping all the stuff about each other that's essential knowledge."
    show samantha flirt
    samantha.say "And don't forget all the things you need to know about other people too!"
    "I notice that Sam's looking at me when she says this."
    show bree happy
    show samantha happy
    "And the unease of the situation only gets worse when they both begin laughing."
    mike.say "Wh...what does that mean?"
    mike.say "Have you two been gossiping about me?"
    show samantha normal
    show bree normal
    "[bree.name] rolls her eyes and shakes her head."
    bree.say "You see, Sam..."
    bree.say "Typical guy reaction."
    bree.say "Assumes everything is about him!"
    samantha.say "Aw..."
    samantha.say "Go easy on him, [bree.name]."
    show samantha flirt
    samantha.say "It can't be easy for [hero.name], having me back here."
    samantha.say "New friends and old friends, all mixed up together."
    mike.say "Hey!"
    if samantha.flags.nickname == "cupcake":
        mike.say "I'm the one that's supposed to be worrying about you, Cupcake!"
    else:
        mike.say "I'm the one that's supposed to be worrying about you, Sam!"
    mike.say "And trust me, I'm handling the situation just fine."
    show samantha normal
    "Sam shrugs and raises her eyebrows."
    samantha.say "If you say so."
    samantha.say "Anyway..."
    samantha.say "I have some stuff I need to handle."
    samantha.say "So I'll see you guys later."
    hide samantha with moveoutright
    "With that, Sam turns and walks away."
    "Which leaves [bree.name] and I standing there in an awkward silence."
    bree.say "So..."
    bree.say "I gotta say, [hero.name]..."
    bree.say "I really like Sam."
    bree.say "And I think we're going to get on really well."
    "I nod and smile, trying not to say what I'm thinking."
    "Which is that I hope they don't get on TOO well!"
    mike.say "That's...great, [bree.name]...just great!"
    if samantha.flags.nickname == "cupcake":
        mike.say "And thanks for doing so much to get Cupcake settled in."
    else:
        mike.say "And thanks for doing so much to get Sam settled in."
    bree.say "Oh no, it's my pleasure!"
    show bree flirt
    bree.say "I can't wait to get to know her better..."
    "[bree.name] smiles as she turns and walks away too."
    hide bree with moveoutleft
    "And I'm pretty sure she doesn't understand how her words sound to me right now."
    "Because when I invited Sam to stay here, I was kind of hoping to reconnect with her."
    "Maybe even to take out relationship to a whole new level too."
    "But I never figured that I might have competition for her affections!"
    "I can see I'm going to have to keep an eye on [bree.name] and her from now on."
    $ game.flags.sexual_tension = TemporaryFlag(True, 1)
    scene expression f"bg {game.room}"
    return

label lesbian_sex_bree_sam:
    "I'm feeling like a lot of pressure's been lifted off me now that Sam's been able to move in."
    "And I'm also really grateful to the other girls for letting her stay here at such short notice."
    "The only problem is that Sam's room isn't going to be ready for a while."
    "She was happy to sleep on the sofa until then, but the girls were having none of it."
    "They said that she could share their rooms until hers was ready, however long it takes."
    "I guess I'm lucky to have such great housemates!"
    "Tonight Sam's going to be sleeping in [bree.name]'s room, and I want to make sure she's okay."
    "Which is why I find myself outside the door to [bree.name]'s bedroom when everyone's turning in."
    "I'm only going to knock on the door and see how the pair of them are settling in."
    "But then a thought occurs to me - what If I'm disturbing them?"
    "I could just leave it and walk away, but something keeps me from doing that."
    "It's like I really need to know that Sam's okay."
    "Otherwise I'm worried that the thought will keep me awake all night."
    "So in the end, I decide to make a compromise and just peek through the keyhole."
    "Okay, okay...I know it sounds a little suspect."
    "But I'm only going to look for a second or two."
    "Just long enough to check that Sam's doing okay in there."
    "I close one eye as I bend over and stick the other against the hole."
    "It takes a moment for my vision to adjust."
    "But then I can see the familiar sights of [bree.name]'s bedroom."
    show lesbian sex breesam with fade
    "Oh...oh my!"
    "Scrub that - I can actually see some very unfamiliar sights in there right now!"
    "Sam's in there alright."
    "In fact, she's the first person I see."
    "It's just the actual amount of her that I can see that throws me off."
    "You see, she's totally naked!"
    "Nothing odd about that, I tell myself."
    "Maybe she's just about to get her pyjamas on?"
    "But then I something move on the bed, and my eyes are drawn in that direction."
    "It's [bree.name]...and she's naked too!"
    "[bree.name]'s just laid there on the bed, watching Sam as she walks towards her."
    "I swallow and begin to sweat as I realise what I'm watching here."
    "Those two are about to get it on!"
    "That has to be what's happening!"
    menu:
        "Don't watch":
            "I pull myself back from the keyhole almost as soon as I see what's happening in there."
            scene bg secondfloor with fade
            "And the moment that I do, I start to feel guilty for even having peeked in the first place."
            "I guess that's fitting punishment for thinking it's okay to spy on my housemates!"
            "Don't get me wrong, it's not that I disapprove of what Sam and [bree.name] are doing in there."
            "It's more that I wasn't prepared for finding out like that."
            "And, well...I guess I'm more than a little bit jealous too!"
            "I've always held a torch for Sam, from back when she was married to Ryan."
            "Now that she's back on the market, I kinda thought I might be in with a chance."
            "But it seems like [bree.name]'s beaten me to it!"
            "I hurry away from her bedroom door as quickly and quietly as I can."
            "Though I doubt I'll be able to get that image out of my head for a long time."
            $ game.room = "secondfloor"
            return
        "Watch":
            "I know that I shouldn't be doing this."
            "I know that I should take my eye away from the keyhole."
            "And I know that I should just walk away and forget about what I've already seen."
            "But in what reality is that ever going to happen?"
            "Instead I press my eye close to the keyhole, hoping to be able to see more!"
            "Now that I'm devoting all of my attention to the scene, I start to notice a little more."
            "And one of those things is the look on Sam and [bree.name]'s faces right now."
            "[bree.name]'s laid there looking more than a little worried and vulnerable."
            "She's looking up at Sam like she's afraid and excited in equal measures."
            "Sam's a different story entirely as she walks slowly towards the bed."
            "She's looking down at [bree.name] with a confident smile on her face."
            "And it looks very much like she's the one that's in control here."
            samantha.say "So, [bree.name]..."
            samantha.say "Are you ready for me now?"
            bree.say "Y...yeah, Sam..."
            bree.say "Ready as I'll ever be, I guess!"
            bree.say "You...you're sure that this is okay?"
            samantha.say "Don't be silly, [bree.name]."
            samantha.say "Of course this is okay."
            samantha.say "You're being so nice to me, letting me share your room for the night."
            samantha.say "So I have to find a way to repay your kind hospitality, don't I?"
            "[bree.name] nods as Sam begins to lower herself onto the bed."
            "And her eyes are as wide as I've ever seen them."
            "But at the same time, this is a side of Sam I'm not used to seeing."
            "I can't remember her ever being this in control before, so domineering!"
            "That's one of the reasons I can't look away."
            "Or at least it's one of the things that I tell myself is a reason."
            "I'm fascinated to see Sam taking charge and [bree.name] just falling in line."
            samantha.say "Aww..."
            samantha.say "Don't worry, [bree.name]..."
            samantha.say "I promise I'll be gentle."
            bree.say "Y...you will?"
            bree.say "You promise?"
            samantha.say "Well...not too gentle!"
            "With that, Sam springs into action before [bree.name] can say another word."
            "She takes hold of [bree.name]'s ankles, using them to lift her legs off the bed."
            "At the same time she parts them too, leaning forwards."
            samantha.say "Mmm..."
            samantha.say "[bree.name]!"
            samantha.say "You're so warm and wet down there!"
            samantha.say "Did I do that to you?"
            "[bree.name]'s eyes are closed as she gasps at the sensations she's feeling."
            "Samantha must be rubbing her pussy against the other girl's right now."
            "And it looks like [bree.name]'s getting a serious thrill from it too!"
            bree.say "Ah..."
            bree.say "Oh...oh yeah..."
            bree.say "You're making...making me wet, Sam!"
            "Samantha lets out a wicked laugh at [bree.name]'s admission."
            "It's deep and totally filthy, a sound I never heard her make before!"
            samantha.say "That's good, [bree.name]..."
            samantha.say "Because you're doing the same to me!"
            "Sam keeps on doing what she's doing."
            "All the time she's grinding herself into [bree.name]."
            "Oh god...this is SO hot!"
            "It just seems to go on and on, Sam moving and [bree.name] writhing beneath her."
            "And I'm starting to lose track of how long I've been watching them."
            menu:
                "Masturbate":
                    "Without thinking, I find myself unzipping my flies and reaching into my pants."
                    "My cock's been hard as a rock since almost the moment I started watching them go at it."
                    "But now I'm feeling like I need to be doing something to release my own tension."
                    "And every time Sam rubs herself against [bree.name], I rub my own cock in sympathy."
                    "Pretty soon I'm panting and gasping along with her too, feeling every move Sam makes!"
                    "So when it looks like [bree.name]'s about to cum, I feel myself shooting my load too."
                "Just watch":
                    "I think about putting my hand into my pants and stroking myself along with them."
                    "But then the fear of getting caught doing that outside [bree.name]'s door puts me off."
                    "Instead I tell myself that there's time for that later, when I'm alone."
                    "Because there's no chance of me forgetting what I've seen going on in there!"
                    "And soon enough, it looks like [bree.name]'s about to cum anyway."
            bree.say "Oooh..."
            bree.say "Oh god, Sam..."
            bree.say "I can't..."
            "[bree.name]'s head rolls back onto the bed as her orgasm takes hold."
            "She grasps at her breasts, squeezing her nipples looking for release."
            "I have no idea if her efforts help at all, I'm too engrossed to even notice."
            "All the time it's happening, Sam keeps right on doing what she's doing."
            "Okay...perhaps this is where I should flee the scene."
            "The last thing I see through the keyhole is a tangle of sweaty limbs."
            scene bg bedroom1 with fade
            "Then I make it back to my own room and close the door behind me."
            "I don't honestly know whether to feel pleased at how well Sam's fitting in."
            "That and how much [bree.name] seems to be doing to get her settled."
            "Or jealous that I'm not getting in on any of the same action!"
            $ game.room = "bedroom1"
    return

label sexual_tension_sam_lexi:
    "I've been watching Sam pretty closely since she moved back into the house."
    "Part of that is because I want to be sure that she's settling in okay."
    "I mean, after the whole business with Ryan, she's going to need time to recover."
    "But on top of that I can't help being thrilled by the idea of Sam here."
    "Back when we were last living under the same roof she was already spoken for."
    "All of that's different now, and maybe there's a chance of us being more then friends."
    "Though I need to keep in mind that she's not in a good place right now."
    "So I try as best I can to keep things strictly platonic at first."
    scene expression "bg " + samantha.room
    show lexi sad nophone at right5
    show samantha at left5
    with fade
    "Which is kind of hard when I walk into a room and find Sam and Lexi chatting."
    "Especially when they're talking about the kind of clothes Lexi likes to wear!"
    lexi.say "Like..."
    lexi.say "I don't see what the big deal is, Sam."
    lexi.say "It's not like you need permission to wear this kind of stuff!"
    show samantha flirt blush
    "Sam shakes her head at this."
    "But she also giggles and her cheeks flush a little too."
    "All things that make her look hotter than ever."
    samantha.say "I know, I know..."
    samantha.say "I guess it's just a matter of confidence, Lexi."
    samantha.say "I'd be worried what people would think of me."
    show lexi happy at startle
    "This time it's Lexi that laughs."
    "But where Sam was demure and delicate, she's the opposite."
    "Lexi bursts into a guffawing laugh that ends in a loud snort."
    lexi.say "What people would think?!?"
    lexi.say "Fuck's sake, Sam!"
    show lexi normal
    lexi.say "All they'd be able to think is how crazy sexy you'd look!"
    show samantha happy -blush
    samantha.say "Oh, Lexi!"
    samantha.say "Stop teasing me!"
    "Lexi shakes her head at Sam's humble reaction."
    lexi.say "I'm not kidding, Sam!"
    show lexi wink
    lexi.say "You're hot fucking stuff!"
    show samantha normal
    samantha.say "You really think so, Lexi?"
    show samantha flirt
    samantha.say "Well..."
    samantha.say "I wasn't going to say this..."
    samantha.say "But you're pretty hot yourself!"
    show samantha at left4
    show lexi normal blush at right4
    with move
    "Lexi and Sam begin to lean in a little closer."
    "And it's right about now that I realise I'm eavesdropping on their conversation."
    "I've been lingering in the doorway this whole time, listening to them talking."
    "If they see me now, they're going to assume that I did that on purpose!"
    mike.say "AHEM..."
    mike.say "I'm not interrupting, am I?"
    show samantha normal
    show lexi normal -blush
    "As one, Lexi and Sam glance around and finally notice me."
    "But neither of them seems to be in the least bit surprised."
    "I was kind of expecting them to leap apart and act all guilty."
    "But I guess these girls are just wired up differently to most guys."
    lexi.say "Nah, [hero.name]..."
    lexi.say "We were just yacking about nothing."
    samantha.say "Mmm..."
    samantha.say "I was just spending some time with Lexi, you know?"
    samantha.say "Like, getting to know her a little."
    samantha.say "She's super interesting - I've never met anyone else quite like her!"
    show lexi happy
    "Lexi smiles broadly as Sam heaps praise onto her."
    lexi.say "How's about that, [hero.name]?"
    show lexi wink
    lexi.say "I'm super interesting!"
    "I can't help rolling my eyes and shaking my head at this."
    mike.say "Yeah, Lexi..."
    mike.say "That's one way of putting it!"
    show samantha at left5 with move
    "While I'm talking to Lexi, Sam takes the opportunity to withdraw."
    "She gives us a quick wave as she heads out of the room."
    show samantha happy
    samantha.say "Talk later, guys."
    samantha.say "I have to go handle something, okay?"
    show lexi normal
    hide samantha with moveoutleft
    "Lexi and I both nod and smile as Sam leaves the room."
    "But once she's gone, Lexi lets out a whistle and shakes her head."
    show lexi surprised at center with move
    lexi.say "Phew!"
    lexi.say "She could make SO much money on the streets!"
    mike.say "WHAT?!?"
    mike.say "You're joking, Lexi!"
    if samantha.flags.nickname == "cupcake":
        mike.say "You have to be - because Cupcake would never do something like that!"
    else:
        mike.say "You have to be - because Sam would never do something like that!"
    show lexi sad
    "Lexi shakes her head again and sucks her teeth at the same time."
    lexi.say "Shame..."
    lexi.say "I know punters that'd go wild for a sweet, well-spoken girl like her."
    lexi.say "I mean, I don't know how you ever managed to live under the same roof as Sam."
    "I frown at this, not sure what Lexi's implying."
    mike.say "What?"
    mike.say "You mean you'd be all over her if you were a guy?"
    show lexi happy
    "Lexi snorts with laughter again."
    lexi.say "Aww..."
    lexi.say "That's so cute, [hero.name]!"
    show lexi wink
    lexi.say "But nah - I mean I'd do that first chance I got."
    lexi.say "Guy or girl, I'd nail her!"
    "I do the best I can to keep my reaction under wraps."
    "Trying to look like the concerned friend rather than a jealous rival."
    mike.say "Whatever, Lexi..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Just try to remember what Cupcake's been through recently, okay?"
    else:
        mike.say "Just try to remember what Sam's been through recently, okay?"
    mike.say "What she needs right now is the support of friends."
    mike.say "Not to be objectivised and turned into an object of sexual conquest!"
    show lexi normal
    "Lexi laughs yet again, but this time she's nodding too."
    lexi.say "Okay, [hero.name], okay..."
    lexi.say "You know I can't understand big words like that!"
    show lexi wink
    lexi.say "So I'll just promise to be a good girl!"
    hide lexi with moveoutleft
    "With that, Lexi gets up and walks out too."
    "Which leaves me alone and worrying about the situation."
    "I'd been concerned about the girls getting on with Sam before."
    "But now I'm also worried I might have a rival for her affections among them!"
    $ game.flags.sexual_tension = TemporaryFlag(True, 1)
    scene expression f"bg {game.room}"
    return

label lesbian_sex_sam_lexi:
    "I'm on my way to my room, fully intending to turn in for the night."
    "But then I find myself changing course and heading for the sitting room."
    "Because that's where Sam's supposed to be sleeping tonight."
    "She's taking one of the two sofas, the one that Lexi's not using."
    "I know it's not ideal to have two people sleeping on the sofas."
    "But the deal was that Sam would share a room with a different person each night."
    "And that means that Lexi's on the list too and has to share her sleeping quarters."
    "I mean, I could have offered to let Sam sleep in my room with me."
    "But I kind of get the impression that wouldn't have gone down too well!"
    "Keeping as quiet as I possibly can, I sneak over to the sitting room doorway."
    "Dumb as it sounds, I flatten myself against the wall and listen carefully."
    "And in that moment I feel like I'm pretending to be some kind of fucking spy!"
    "So I shake my head and prepare to just glace around the doorframe."
    "And that's when I hear some of the sounds coming out of there."
    "I was prepared to maybe hear Sam and Lexi chatting."
    "Then I could have just said hi and told them I was checking on Sam."
    "I was even prepared to hear them both snoring and just take a quick glance."
    "But that's not the sound of chatting or snoring."
    "More like the sound of panting and gasping!"
    "Curiosity gets the better of me, and I'm soon gazing into the sitting room."
    "And what I see is almost enough to make my eyes pop out of their sockets."
    "Because Sam and Lexi aren't on different sofas."
    show lesbian sex samlexi with fade
    "They're on the same one, and neither of them is sleeping either."
    "All I can see is two naked bodies in a tangle of limbs."
    "But I know that they're getting up to something intimate in there!"
    "The question is, what am I going to do about it?"
    menu:
        "Don't watch":
            hide lesbian sex samlexi
            "Like that's even a question!"
            "The one thing I'm not going to do is stand here and watch them."
            "Because that'd make one serious creep!"
            "So still taking care to be silent, I turn away from the door."
            "And then I hurry back to my room as quickly as I can."
            "Sure, I can't get the image of what I've just seen out of my head."
            "But at least I know that I don't have anything to feel guilty about."
            "Even if I have no idea what all of this means."
            return
        "Watch":
            "Hah!"
            "Like that's even a question!"
            "I don't hesitate to lean in closer still."
            "Still trying my best to keep quiet, I strain for a better view."
            "And as I do so, what's happening in there finally becomes clear."
            "The tangle of limbs resolves itself, and I can tell Sam and Lexi apart."
            "They're both sprawled on the sofa, facing towards each other."
            "Their legs are hitched up and they're leaning back on their elbows too."
            "I can see Lexi's a little lower down, with Sam hovering over her."
            "But it's the motion of their bodies that gives it away."
            "Even before I catch a glimpse of what's happening between their thighs."
            "I can tell from the way they're moving that their lips are rubbing together!"
            "Sam and Lexi are in the prefect position too."
            "Every move they make brings their pussys into contact."
            "And I don't need to be close enough to inspect them to know how wet they must be either."
            "I swear I can see their lips glistening, even from this far away."
            "Plus the sounds that they're making are crazily hot too!"
            "It looks like Lexi's the one taking the lead, panting with effort."
            "And Sam's moving less, though she seems to be gasping more."
            "Not that she's the only one getting pleasure from all of this."
            "Both of their heads keep falling backwards."
            "And when they do, their faces stare at the ceiling."
            "I see Lexi and Sam's features in an expression of pure bliss."
            "So I know that they're taking and giving at the same time."
            "Maybe I shouldn't be watching this."
            "But there's no way I can tear my eyes away from the sight."
            "It's impossible to say if either of them has a more beautiful body."
            "And at times I even lose track of who I'm actually staring at."
            "Heads, breasts, bellies and buttocks."
            "All of them are moving in an almost hypnotic fashion."
            "But the only part of my own body I can feel is my cock."
            "Which is getting harder by the second!"
            menu:
                "Masturbate":
                    "Almost without thinking, I reach down and unzip my pants."
                    "And then before I know it, I have it out and I'm away."
                    "Sure, doing this makes watching that much more dangerous."
                    "If I get caught, then I'm going to be in more trouble than I can imagine."
                    "But that's only if I get caught."
                    "Soon enough, I'm gasping and panting too."
                    "The sight of Sam and Lexi making my cock twitch."
                    "And when they both begin to wail, I know they're going to cum."
                    "Because at the same time, I can feel something warm and sticky running over my fingers."
                "Just watch":
                    "I think about getting it out and pleasuring myself while I watch."
                    "But doing that would make watching that much more dangerous."
                    "If I got caught, then I'd be in more trouble than I can imagine."
                    "So instead I force myself to leave it alone and just watch."
                    "Soon enough, I'm gasping and panting too."
                    "The sight of Sam and Lexi making my cock twitch."
                    "And when they both begin to wail, I know they're going to cum."
                    "Seriously, it's all I can do to keep from losing it in my shorts!"
            "I watch as Sam and Lexi collapse onto the sofa, still locked together."
            "The only sounds they're making now are pants and gasps of exhaustion."
            "But even though they seem out of it, I'm not taking any chances."
            "Still taking care to be silent, I turn away from the door."
            scene bg bedroom1 with fade
            "And then I hurry back to my room as quickly as I can."
            "I can't get the image of what I've just seen out of my head."
            "And I don't know if I ever will be able to forget what I saw tonight."
            "As for what it means in terms of us all living under the same roof..."
            "Well, I have absolutely no idea!"
            $ game.room = "bedroom1"
    return

label sexual_tension_sam_sasha:
    "I've been waiting for Sam to have the chance to really get to know the girls in the house."
    "Because in all the drama and fuss of her divorcing Ryan and moving in here it's been chaos."
    "Sure, everyone was on-board with her moving back in here when she needed helping out."
    "But that doesn't mean that everyone's going to actually get on once the dust has settled."
    "And if I'm honest, Sasha's the one that I'm the most worried about getting along with Sam."
    "Don't get me wrong, I'm not dumping on either one of them."
    "It's just that Sam and Sasha are such different people on paper."
    "I'm worried that they're going to clash, and sooner rather than later."
    "So when I pass by and hear them actually talking to each other, I slow down and stop."
    "I know that I shouldn't be listening in on other people's conversations."
    "But I tell myself that it's just out of concern for Sam's well-being."
    scene expression "bg " + samantha.room
    show samantha happy at left5
    show sasha surprised at right5
    with fade
    sasha.say "You're fucking kidding?"
    sasha.say "You have to be, kidding?"
    sasha.say "Are you kidding, Sam?"
    show samantha happy at startle
    "Sam laughs at the surprise in Sasha's voice."
    show samantha normal
    samantha.say "Do I, Sasha?"
    samantha.say "Is it really that hard to believe?"
    show sasha annoyed
    sasha.say "You just look so..."
    samantha.say "So what?"
    samantha.say "So normal?"
    samantha.say "So boring?"
    show sasha normal
    "Sasha shakes her head at this."
    sasha.say "No..."
    sasha.say "No way!"
    sasha.say "I just never had you pegged as being into rock, that's all!"
    show samantha happy at startle
    "Sam laughs again, clearly enjoying Sasha's confusion."
    samantha.say "Oh yeah, Sasha..."
    show samantha flirt
    samantha.say "I was totally into it back in the day."
    samantha.say "I had the dyed hair, the leather jacket, the works!"
    show fx exclamation at right5
    sasha.say "Wait a minute..."
    sasha.say "Do you..."
    sasha.say "You don't have any tattoos, do you?"
    hide fx
    "All that Sasha gets in response to her question is an enigmatic smile."
    show sasha at center with move
    "But that doesn't seem to satisfy her curiosity, as she reaches out with one hand."
    "And for a moment, it looks like she's actually going to pull up Sam's top!"
    "So I choose that very moment to make my presence felt."
    mike.say "What's going on here, then?"
    mike.say "Impromptu game of strip-poker?"
    show sasha shocked at right5
    show samantha surprised
    "Sasha almost leaps backwards and Sam pulls down her top just as quickly."
    "They exchange a glance and they both let out a nervous little laugh."
    "But despite their best efforts, they look as guilty as hell."
    sasha.say "WHAT?!?"
    sasha.say "No way!"
    show sasha normal
    sasha.say "We were just chatting, that's all."
    show samantha normal
    samantha.say "Yeah, [hero.name]..."
    samantha.say "I was just filling Sasha in on my past, you know?"
    "I feel like my presence has defused the situation somewhat."
    "So I decide to play along with the excuses they're giving me."
    mike.say "I heard something about dyed hair and leather jackets?"
    if samantha.flags.nickname == "cupcake":
        mike.say "And you being into rock back in the day, Cupcake?"
    else:
        mike.say "And you being into rock back in the day, Sam?"
    mike.say "Is that for real?"
    mike.say "Because you never told me anything about that!"
    "Sam doesn't offer me an answer."
    show samantha at mostleft5 with move
    "Instead she just turns towards the door and walks away."
    "But just as she gets to there, she stops and looks back."
    show samantha flirt at mostleft4
    samantha.say "There's a lot of stuff about me I never told you, [hero.name]."
    samantha.say "A girl's got to keep a little bit of mystery about herself!"
    hide samantha with moveoutleft
    "With that, she's gone, leaving Sasha and me to stare at each other."
    show sasha angry
    sasha.say "Ah, [hero.name]!"
    sasha.say "Why'd you have to come barging in like that?"
    sasha.say "Sam was just about to show me her tattoos!"
    "It takes me a couple of seconds to react to what Sasha just said."
    "I guess I was expecting her to keep on denying it, even with Sam gone."
    mike.say "Really, Sasha?"
    mike.say "I thought you were just chatting?"
    show sasha annoyed
    "Sasha shoots me a knowing glance."
    "And the laugh that comes along with it is pure filth."
    show sasha flirt
    sasha.say "Come on, [hero.name]!"
    sasha.say "You're not that naive, are you?"
    sasha.say "I think I'm gonna enjoy having Sam staying here with us!"
    hide sasha with moveoutleft
    "Before I can say another word, Sasha turns and walks out too."
    "Which leaves me without any option but to stand there and watch her."
    "I can't chase her down and question her any further."
    "Because that would be as good as me admitting it."
    "Admitting that I think there's something going on between them."
    "And then I'd have to explain just why I'd have a problem with that."
    "Which in turn would mean admitting that I'm not just a concerned friend."
    "Well-played, Sasha, well-played!"
    $ game.flags.sexual_tension = TemporaryFlag(True, 1)
    scene expression f"bg {game.room}"
    return

label lesbian_sex_sam_sasha:
    $ hero.cancel_activity()
    "I'm feeling like a lot of pressure's been lifted off me now that Sam's been able to move in."
    "And I'm also really grateful to the other girls for letting her stay here at such short notice."
    "The only problem is that Sam's room isn't going to be ready for a while."
    "She was happy to sleep on the sofa until then, but the girls were having none of it."
    "They said that she could share their rooms until hers was ready, however long it takes."
    "I guess I'm lucky to have such great housemates!"
    "Tonight Sam's going to be sleeping in Sasha's room, and I want to make sure she's okay."
    "That's why I'm about to knock on the door of Sasha's bedroom, just to check up on Sam."
    "But as I raise my hand to knock, I hear a strange noise coming from inside."
    "It's a deep moaning, almost like someone's in pain."
    "Okay, okay...I'm not going to try to play it like I'm that naive!"
    "I know what that kind of moaning means when it's coming from a bedroom."
    "Even more so when it's also coming from behind a closed door!"
    "Either Sasha or Sam's in there having a little bit of fun before bedtime!"
    "I take a moment to glance around, making sure there's nobody around."
    "Then I lean in to peek through the keyhole."
    "Yeah, I know - it's a little bit pervy of me."
    "But all I want is a quick eye-full of what's going on in there."
    "The sight of one of the girls masturbating should be enough to help me do the same later!"
    show lesbian sex samsasha with fade
    "Peeking through the keyhole, I can see that Sam's laid out on the bed."
    "She's naked, leg wide apart and she has a look of very real pleasure on her face!"
    "But then I see that she's not alone."
    "Sasha's there too, also totally naked - and she's climbing on top of Sam!"
    "It's then that I see what's swaying and bobbing between Sasha's legs."
    "A strap-on!"
    "And it looks like she's going to use it on Sam too!"
    menu:
        "Don't watch":
            hide lesbian sex samsasha
            "I pull myself back from the keyhole almost as soon as I see what's happening in there."
            "And the moment that I do, I start to feel guilty for even having peeked in the first place."
            "I guess that's fitting punishment for thinking it's okay to spy on my housemates!"
            "Don't get me wrong, it's not that I disapprove of what Sam and Sasha are doing in there."
            "It's more that I wasn't prepared for finding out like that."
            "And, well...I guess I'm more than a little bit jealous too!"
            "I've always held a torch for Sam, from back when she was married to Ryan."
            "Now that she's back on the market, I kinda thought I might be in with a chance."
            "But it seems like Sasha's beaten me to it!"
            "I hurry away from her bedroom door as quickly and quietly as I can."
            "Though I doubt I'll be able to get that image out of my head for a long time."
            return
        "Watch":
            "I push my eye closer to the keyhole, struggling to get a better view."
            "All thoughts of this being inappropriate vanish in an instant as I watch."
            "How can I possibly pass up on an opportunity like this?"
            "Two hot girls living under the same roof as me are hooking up in there!"
            "I'd be kicking myself if I didn't do the best I can to be able to watch!"
            "It's pretty obvious that Sasha's the one taking the lead here."
            "Apart from the strap-on she's wearing, she also seems to be calling the shots."
            "Sam, on the other hand, appears happy to lie back and take it."
            sasha.say "Are you ready for me, Sam?"
            sasha.say "Are you ready to pay the price for sleeping in my room?"
            "As she says all of this, Sasha thrusts the dildo forwards."
            "It hangs over Sam, swaying in a vaguely menacing manner."
            "She nods, eyes wide with what looks like excitement mingled with a little fear."
            "Sam reaches up and begins to stroke the thing with both hands."
            samantha.say "Y...yes, Sasha..."
            samantha.say "I'm ready to pay!"
            samantha.say "But...please be gentle?"
            "Sasha chuckles and shakes her head."
            "It's clear that she's enjoying Sam's submissive role in what they're doing."
            show lesbian sex samsasha strapon
            "And the smile on her face only gets wider as she lowers the dildo towards its target."
            "Sam keeps her hands on it too, steering the thing between her thighs."
            "Well, she has at least one hand on it most of the time."
            "The other keeps flitting to her pussy, rubbing and caressing it's folds."
            "This means that by the time Sasha is in position, Sam's more than ready for her."
            samantha.say "Mmm..."
            samantha.say "Oh, Sasha..."
            samantha.say "Don't stop..."
            "Sasha's smile turns into a grin as she slides the dildo into Sam."
            "She keeps the motion smooth and slow, letting the other girl feel every moment."
            show lesbian sex samsasha pleasure
            "And once she's all the way in there, she holds her position and begins to grind away."
            "At first, Sasha doesn't move back and forth, instead rotating her groin."
            "Sam reacts instantly, her head falling back onto the bed."
            "From where I'm kneeling, I can see her eyes roll back into her head."
            "And there's no chance of her speaking another word after that point."
            "The only sounds she seems capable of making are delirious moans."
            "I look up to see just what Sasha's doing to her."
            show lesbian sex samsasha normal
            "And as soon as I do, the reason for Sam's state of delirium becomes clear."
            "Sasha's holding her legs wide apart, almost squatting over her."
            "And she's using the height and angle this gives her to maximum effect!"
            "By now Sasha's pretty much ploughing into Sam with everything she's got."
            "All that she can do is lie there and take it!"
            menu:
                "Masturbate":
                    "Without thinking, I find myself unzipping my flies and reaching into my pants."
                    "My cock's been hard as a rock since almost the moment I started watching them go at it."
                    "But now I'm feeling like I need to be doing something to release my own tension."
                    "And every time the dildo is thrust into Sam, I rub my own cock in sympathy."
                    "Pretty soon I'm panting and gasping along with her too, feeling every move Sasha makes!"
                    "So when it looks like Sam's about to cum, I feel myself shooting my load too."
                "Just keep watching":
                    "I think about putting my hand into my pants and stroking myself along with them."
                    "But then the fear of getting caught doing that outside Sasha's door puts me off."
                    "Instead I tell myself that there's time for that later, when I'm alone."
                    "Because there's no chance of me forgetting what I've seen going on in there!"
                    "And soon enough, it looks like Sam's about to cum anyway."
            sasha.say "You like that, huh?"
            sasha.say "You like what I can give you?"
            "All that Sam can do is nod as Sasha pushes her over the edge."
            "I see her hands grabbing onto the bedclothes, holding on for dear life."
            show lesbian sex samsasha pleasure cum
            "At the same time, Sam's gasping as her orgasm takes hold."
            "And I take that as my cue to flee the scene."
            "The last thing I see through the keyhole is a tangle of sweaty limbs."
            "Then I make it back to my own room and close the door behind me."
            scene bg bedroom1 with fade
            $ game.room = "bedroom1"
            "I don't honestly know whether to feel pleased at how well Sam's fitting in."
            "That and how much Sasha seems to be doing to get her settled."
            "Or jealous that I'm not getting in on any of the same action!"
    return

label sexual_tension_sam_minami:
    "I've been worrying about how weird it'll be for Sam to move back into the house."
    "She's coming back here with all the memories that it must hold for her from the past."
    "And on top of that she's also dealing with the fallout from divorcing Ryan too."
    "I want to do the best I can to help, to be a good friend."
    "Even if that means putting aside my own feeling for as long as it takes."
    scene expression "bg " + samantha.room
    show minami at left5
    show samantha at right5
    with fade
    "But I feel a sense of welcome surprise as I walk in on Minami and Sam."
    "They're chatting away like a couple of old friends."
    "And that fills me with hope that they're going to get on."
    minami.say "Oh yeah, Sam..."
    minami.say "I make ALL of the costumes myself."
    show minami tehe
    minami.say "That's what makes cosplay such a rewarding hobby."
    "Sam's listening to Minami with genuine interest."
    "And my little sister is clearly loving the attention too!"
    samantha.say "Ah..."
    samantha.say "I was never any good at that kind of thing, Minami!"
    show samantha happy
    show minami normal
    samantha.say "All I ever managed with a needle and thread was turning my thumb into a pin-cushion!"
    "Minami giggles and shakes her head."
    "The smile on her face is warm and one hundred percent genuine."
    minami.say "Don't be silly, Sam!"
    minami.say "You'd pick up the basics in no time at all."
    show minami happy
    minami.say "Because I'm a pretty good teacher."
    show minami at left4 with ease
    "I watch as Minami leans back a little, squinting at Sam."
    show samantha surprised
    "Sam seems to notice this and her expression becomes curious."
    "But that doesn't stop Minami from sizing up the other girl."
    samantha.say "Wh..."
    samantha.say "What are you looking at, Minami?"
    show minami surprised at left5, startle
    "The question seems to make Minami snap out of it."
    show samantha blush
    "She looks up at Sam with a smile, her cheeks blushing just a little."
    show minami hunt
    minami.say "Oh..."
    minami.say "I'm sorry, Sam."
    minami.say "I was just trying to guess what size you are, that's all."
    samantha.say "But...why?"
    show minami normal
    minami.say "Well..."
    minami.say "I'm always having great ideas for new cosplay costumes, right?"
    show samantha normal
    "Sam nods, clearly interested in where this is going."
    minami.say "But I'm kinda petit, yeah?"
    minami.say "So some of them just don't look right on me."
    minami.say "But you, Sam..."
    minami.say "You're so tall and...well...so feminine!"
    show minami happy
    show samantha surprised
    minami.say "I'd LOVE to make a costume for someone with a figure like yours!"
    "Now it's Sam's turn to blush, as she looks away from Minami."
    show samantha sad blush
    samantha.say "Oh, I..."
    samantha.say "I don't know about that, Minami..."
    samantha.say "Those things look like they're so complicated..."
    samantha.say "Like they take so much time to make!"
    "Minami shakes her head, brushing aside Sam's objections."
    minami.say "No way, Sam!"
    minami.say "I'd love to do it!"
    show minami normal
    minami.say "In fact, I can see it now..."
    minami.say "You could pull of a fairy-tale princess with ease."
    show minami hunt
    minami.say "Maybe even a female barbarian warrior in a chainmail bikini!"
    "I can hear Minami starting to get carried away."
    "And at the same time, Sam's leaning in ever closer."
    "I think she's beginning to catch the bug too!"
    "So I choose that same moment to make my presence felt."
    mike.say "Ah..."
    mike.say "Hey, guys!"
    mike.say "Hope I'm not interrupting anything?"
    show samantha surprised
    show minami surprised blush at left5
    "Minami and Sam turn to face me as one."
    "But luckily for me, neither of them seems to be annoyed at the sight of me."
    show samantha sad
    samantha.say "Oh no, [hero.name]..."
    samantha.say "Minami and I were just chatting."
    show samantha normal -blush
    samantha.say "It's the first chance I've had to really talk to her since I moved in."
    show minami normal -blush
    minami.say "Yeah, big bro..."
    minami.say "I've been telling Sam all about you!"
    "I frown at this, starting to worry a little."
    mike.say "Erm..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake and I have been friends for a long time, Minami."
    else:
        mike.say "Sam and I have been friends for a long time, Minami."
    mike.say "She already knows all about me."
    minami.say "Oh no, big bro..."
    show minami tehe
    minami.say "I've been telling her all the stuff you'd never admit to!"
    minami.say "All the really embarrassing things I can remember about you!"
    show minami sad
    "I shoot Minami a disapproving look."
    "But Sam intervenes, waving away my concerns."
    show samantha at center
    show minami normal at left5
    with ease
    samantha.say "Don't worry, [hero.name]."
    samantha.say "She didn't tell me anything worse than what I already knew."
    show samantha happy
    samantha.say "At least not yet!"
    hide samantha with moveoutright
    "With that, Sam laughs and slips out of the room."
    "Which leaves me to confront Minami."
    show minami at center with move
    mike.say "Okay, Minami..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Just what have you been telling Cupcake?"
    else:
        mike.say "Just what have you been telling Sam?"
    show minami annoyed
    minami.say "Oh, don't shit yourself, big bro!"
    minami.say "I really didn't spill the good stuff."
    show minami tehe
    minami.say "I'm keeping that for later!"
    mike.say "Seriously, Minami..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake's going through a hard time right now."
    else:
        mike.say "Sam's going through a hard time right now."
    mike.say "She could use as many good friends as she can get."
    show minami annoyed
    "Minami lets out a weary sigh."
    "But I note that she nods her head all the same."
    minami.say "I know, I know..."
    show minami normal
    minami.say "And I think it's going to be great having her here, big bro."
    mike.say "Really?"
    show minami happy
    minami.say "Oh yeah - she's like the big sister I never had!"
    mike.say "That's great to hear, Minami!"
    mike.say "You mean that she could be like a mentor to you?"
    mike.say "Or a role-model or something?"
    "Minami laughs and shakes her head at this."
    minami.say "Oh yeah, big bro!"
    minami.say "Because that's what you are to me too, right?"
    mike.say "Wh...what do you mean?"
    show minami normal
    "Minami rolls her eyes at me."
    minami.say "Oh, come on, big bro!"
    minami.say "If I can have an adopted big brother I think is hot..."
    show minami hunt
    minami.say "Then I can have a big sister that's equally hot, right?"
    "I open my mouth to object."
    hide minami with moveoutright
    "But Minami uses the chance to skip out of the room."
    "The last thing I hear is the sound of her laughter as she makes her escape."
    "She was joking, right?"
    "Minami was just trying to wind me up, wasn't she?"
    "Hmm...I'm going to have to keep an eye on those two."
    $ game.flags.sexual_tension = TemporaryFlag(True, 1)
    scene expression f"bg {game.room}"
    return

label lesbian_sex_sam_minami:
    "I'm feeling like a lot of pressure's been lifted off me now that Sam's been able to move in."
    "And I'm also really grateful to the other girls for letting her stay here at such short notice."
    "The only problem is that Sam's room isn't going to be ready for a while."
    "She was happy to sleep on the sofa until then, but the girls were having none of it."
    "They said that she could share their rooms until hers was ready, however long it takes."
    "I guess I'm lucky to have such great housemates!"
    "Tonight Sam's going to be sleeping in Minami's room, and I want to make sure she's okay."
    "Yeah, I know - it sounds like I'm being a little bit overbearing."
    "But Minami's my little sister, and I'm not used to relying on her for things like this."
    "I just know that I'll feel better knowing for certain that Sam is okay."
    "So I raise my hand to knock at the door of Minami's bedroom."
    "But then I hear the sound of people tumbling around inside."
    "And I swear that I can hear laughter too."
    "Without thinking, I kneel down and put one eye to the keyhole."
    "Not my proudest moment, believe me."
    "And not something that I'd be doing under normal circumstances."
    "But I feel protective towards the pair of them, so I guess it brings out the adult in me."
    "As my eye adjusts to the view through the keyhole, I struggle to make anything out."
    "At first I see someone lying on the bed, and my gaze is naturally drawn towards them."
    "And as things come into focus, I realise that it's Sam."
    "She's reclining on her elbow, looking pretty chilled out."
    "But then I notice that she's totally naked!"
    "How did I not see that before?!?"
    "She's smiling, using her free hand to beckon to someone on the other side of the room."
    samantha.say "What are you doing over there?"
    samantha.say "Come on and join me, yeah?"
    samantha.say "I promise I won't bite."
    samantha.say "Well, not unless you want me to..."
    "My eye turns as I look to the other side of the room."
    "And even though I know she must be in there with Sam, I'm still surprised to see Minami."
    "But then maybe that's more on account of the fact she's also naked right now!"
    "That and the fact Sam's talking dirty to her."
    minami.say "Oh..."
    minami.say "Okay, Sam..."
    "Minami does as she's told, walking slowly over to the bed."
    "She lowers herself down, sitting as close to Sam as she dares."
    minami.say "Are you SURE this is okay?"
    minami.say "I...I don't want big bro to be mad with me, Sam!"
    "Sam shakes her head, already reaching up to pull Minami closer."
    samantha.say "Why would it be wrong, Minami?"
    samantha.say "We're not doing anything we don't want to do, are we?"
    "At this, Minami shakes her head."
    "And she seems to hurry towards Sam too."
    minami.say "NO!"
    minami.say "No, Sam..."
    minami.say "I want to do this as much as you do!"
    samantha.say "Then let's do it!"
    samantha.say "It's only a little bit of fun, Minami!"
    show lesbian sex minsam with fade
    "I watch as Sam parts her legs and guides Minami forwards."
    "Soon she's straddling Sam's thigh, their legs intertwined."
    samantha.say "Come a little closer, Minami..."
    samantha.say "Oh yeah..."
    samantha.say "That's it!"
    menu:
        "Don't watch":
            hide lesbian sex minsam with fade
            "I pull myself back from the keyhole almost as soon as I see what's happening in there."
            "And the moment that I do, I start to feel guilty for even having peeked in the first place."
            "I guess that's fitting punishment for thinking it's okay to spy on my housemates!"
            "Don't get me wrong, it's not that I disapprove of what Sam and Minami are doing in there."
            "It's more that I wasn't prepared for finding out like that."
            "And, well...I guess I'm more than a little bit jealous too!"
            "I've always held a torch for Sam, from back when she was married to Ryan."
            "Now that she's back on the market, I kinda thought I might be in with a chance."
            "But it seems like Minami's beaten me to it!"
            "I hurry away from her bedroom door as quickly and quietly as I can."
            "Though I doubt I'll be able to get that image out of my head for a long time."
        "Watch":
            "I know that I shouldn't be watching what's happening on the other side of the door."
            "But somehow I can't tear my eye away from the keyhole not what I've seen it."
            "Maybe it's the protective instinct that I have towards Sam and Minami alike."
            "Or more likely it's my inner pervert getting the upper hand!"
            "Whatever the reason, I stay right where I am, not moving an inch."
            minami.say "L...like this, Sam?"
            minami.say "Am I doing it right?"
            "Minami's pressing her pussy against Sam's own lips."
            "She keeps gazing down at what she's doing and then up at Sam."
            "All the time she seems desperate for validation from the older girl."
            samantha.say "Mmmm..."
            samantha.say "You bet you're doing it right, Minami!"
            samantha.say "That feels SO good!"
            "Minami smiles, clearly delighted to hear Sam praising her efforts."
            "But then a look of determined concentration appears on her face."
            "It's a look I've seen many times before, and it means she's determined to succeed."
            "Suddenly Minami pushes down with all her weight, grinding herself into Sam."
            samantha.say "Oh god!"
            samantha.say "Minami..."
            minami.say "Oh, oh..."
            minami.say "I'm sorry, Sam!"
            minami.say "What did I do wrong?"
            "Sam smiles and shakes her head, cupping Minami's chin in her hand."
            samantha.say "You didn't do anything wrong, Minami, I promise."
            samantha.say "It was just a little too much too quickly, that's all."
            samantha.say "Look...let me show you how, okay?"
            "Minami nods eagerly, surrendering herself to Sam as she does so."
            "I watch as Sam begins to slowly rub herself against Minami."
            "At the same time she reaches out with one hand."
            "Her fingers trace lines on Minami's naked chest."
            "And when they reach her breasts, they begin to caress her."
            "As she pleasures her down below, Sam also strokes Minami's nipples."
            "When they get hard and stand erect from this, she steps it up and squeezes them too."
            minami.say "Oh fuck..."
            minami.say "Oh, Sam..."
            minami.say "That's SO good!"
            minami.say "Please don't stop!"
            "Sam chuckles and shakes her head, clearly loving having Minami in the palm of her hand."
            "But she does as asked all the same, stepping up her efforts as she does so."
            "Soon enough Minami's utterly helpless, moaning and whimpering as she's teased towards losing it."
            menu:
                "Masturbate":
                    "Without thinking, I find myself unzipping my flies and reaching into my pants."
                    "My cock's been hard as a rock since almost the moment I started watching them go at it."
                    "But now I'm feeling like I need to be doing something to release my own tension."
                    "And every time Sam rubs herself against Minami, I rub my own cock in sympathy."
                    "Pretty soon I'm panting and gasping along with her too, feeling every move Sam makes!"
                    "So when it looks like Minami's about to cum, I feel myself shooting my load too."
                "Just keep watching":
                    "I think about putting my hand into my pants and stroking myself along with them."
                    "But then the fear of getting caught doing that outside Minami's door puts me off."
                    "Instead I tell myself that there's time for that later, when I'm alone."
                    "Because there's no chance of me forgetting what I've seen going on in there!"
                    "And soon enough, it looks like Minami's about to cum anyway."
            minami.say "Sam..."
            minami.say "I'm gonna..."
            minami.say "I'm gonna cum!"
            "True to her word, Minami loses it a moment later."
            "She collapses backwards onto the bed, panting and gasping for breath."
            "Sam's still sitting up, but she looks like she's cumming too."
            "Her cheeks are flushed and she's already fingering her pussy."
            "I think this would be a good time for me to get the hell out of here."
            "The last thing I see through the keyhole is a tangle of sweaty limbs."
            "Then I make it back to my own room and close the door behind me."
            scene bg bedroom1 with fade
            $ game.room = "bedroom1"
            "I don't honestly know whether to feel pleased at how well Sam's fitting in here."
            "That and how much Minami seems to be doing to get her settled."
            "Or jealous that I'm not getting in on any of the same action!"
    return

label home_harem_confession_to_sam:
    $ renpy.dynamic("hh_active_girls")
    $ hh_active_girls = Harem.find_by_name("home").active_members
    "I was pretty much convinced that I was the luckiest guy in the world until it happened."
    "To begin with, I'm the only guy living in a house full of the hottest girls imaginable."
    "On top of that, I've managed to start a relationship with them too."
    "If that weren't enough, I've also convinced them that we can all be in one together."
    "So I'm not just living with hot girls, they're kind of like a harem as well!"
    "But then was all before it happened, before she moved back into the house."
    "Sam's always been special to me, the one that I thought had got away."
    "All the time I was living here with her and Ryan, I held a torch for her."
    "And when things went south with their relationship, I did have hope."
    "Not that I'm a scavenger waiting to pick over the bones of what they had."
    "I've just still got those suppressed feelings for Sam."
    "She just seems to have a weird kind of hold over me somehow."
    "So when she moved back in here, I was faced with a dilemma."
    "We're getting on better than ever, like the old friends we are."
    "And I feel like we're getting closer all the time too."
    "But on the other hand, I'm still seeing the other girls."
    "Sooner or later, something is going to give."
    "Maybe Sam and I will take things to the next level."
    "Or maybe she'll find out about the arrangement I have with the others."
    "Either way I feel the need to handle this before any of that can happen."
    "And the only logical answer I can think of is to come clean with Sam."
    "To tell her what's going on in the house."
    "And then offer her the chance to get in on it too."
    "I might be crazy for doing this, but I don't see any other way."
    show samantha normal with dissolve
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, Cupcake..."
    else:
        mike.say "Ah, Sam..."
    mike.say "You got a spare minute?"
    mike.say "I think we need to talk..."
    samantha.say "Oh-oh!"
    show samantha annoyed
    samantha.say "You said the dreaded words!"
    samantha.say "And you've got that shifty look on your face too."
    mike.say "Wh...what shifty look?"
    mike.say "I don't know what you mean!"
    show samantha normal
    samantha.say "Oh come on, [hero.name]."
    samantha.say "You always look like that when you want something."
    samantha.say "Like a kid that's trying to ask for a puppy!"
    "I can already feel myself blushing as Sam sees straight through me."
    "How is it that she can always do that, make me feel this way?"
    "Is it because of how deep my feelings are for her, how real?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Okay, Cupcake, you win."
    else:
        mike.say "Okay, Sam, you win."
    mike.say "I do have something to tell you."
    mike.say "I guess you could even say it was a kind of confession."
    "Now Sam begins to look more interested than amused."
    show samantha at center, zoomAt(1.5, (940, 1040))
    "She raises her eyebrows as she leans in closer."
    samantha.say "Ooh!"
    show samantha happy
    samantha.say "A confession!"
    samantha.say "I like the sound of that!"
    show samantha normal
    mike.say "Well..."
    mike.say "It's about me and the other girls in the house..."
    show samantha flirt
    samantha.say "I did mean to ask, [hero.name]..."
    samantha.say "Exactly how many of them are you sleeping with right now?"
    "I stare at Sam, my mouth hanging open in surprise."
    "How in the hell did she know?!?"
    mike.say "Y...you know about that?!?"
    show samantha happy
    "Sam smiles broadly and nods."
    "She's clearly enjoying all of this."
    show samantha normal
    samantha.say "You're a guy and they're all girls, [hero.name]."
    samantha.say "And they're all pretty cute too, whereas you're only human."
    samantha.say "Then there's the fact I see you sneaking around the house all the time!"
    samantha.say "I guess you thought you were getting away with it, huh?"
    show samantha happy
    "I guess there's no sense in hiding it any longer."
    "If Sam's already figured it out, then I should just come clean."
    "So I give her an awkward smile as I rub the back of my head."
    if samantha.flags.nickname == "cupcake":
        mike.say "Okay, Cupcake - you got me!"
    else:
        mike.say "Okay, Sam - you got me!"
    show samantha normal
    samantha.say "I knew it!"
    samantha.say "So are you seeing [bree.name]?"
    show samantha flirt
    samantha.say "She's your classic blonde babe."
    samantha.say "Or is it Sasha?"
    samantha.say "The dark and mysterious one!"
    if "minami" in hh_active_girls:
        samantha.say "Don't tell me it's Minami?"
        samantha.say "Your own adopted sister - you dog, you!"
    if "lexi" in hh_active_girls:
        samantha.say "Maybe it's Lexi?"
        samantha.say "In my experience, most guys can't resist a bad girl!"
    "I swallow hard and then take a deep breath."
    "Okay, here goes nothing..."
    mike.say "Ah, well..."
    mike.say "It's kind of...all of them!"
    show samantha surprised
    "Now it's Sam's turn to look genuinely surprised."
    "She shakes her head in disbelief."
    "And it's only now that I remember how Ryan cheated on her."
    "Oh shit, is that going to colour her reaction to my confession?"
    samantha.say "You mean..."
    samantha.say "You're seeing them behind each other's backs?"
    show samantha angry
    samantha.say "You're cheating on ALL of your housemates?"
    "I shake my head, trying to explain myself."
    "But that's what I was already trying to do."
    "And I feel like I'm making a mess of that."
    if samantha.flags.nickname == "cupcake":
        mike.say "No, Cupcake, no - it's not like that!"
    else:
        mike.say "No, Sam, no - it's not like that!"
    mike.say "Nobody's cheating or being cheated on, I promise!"
    show samantha annoyed
    samantha.say "Then how..."
    mike.say "We're all in a relationship together, you see?"
    if len(hh_active_girls) == 2:
        mike.say "Kind of like a threesome."
    elif len(hh_active_girls) == 3:
        mike.say "Kind of like a foursome."
    elif len(hh_active_girls) == 4:
        mike.say "Kind of like a fivesome."
    else:
        mike.say "Kind of like a threesome, foursome, fivesome, or whatever."
    mike.say "Maybe even like a harem, you know?"
    show samantha surprised
    "I can see that Sam isn't grasping what I'm saying to her."
    "Maybe I'm not doing a good enough job of explaining it."
    "Or maybe she's just not going to be sold on the idea no matter what I say."
    "Then I see her expression change and she seems to become intrigued than puzzled."
    samantha.say "My god..."
    samantha.say "You're all in on it?"
    show samantha flirt
    samantha.say "You've been having orgies with all these girls?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Look, Cupcake..."
    else:
        mike.say "Look, Sam..."
    mike.say "I understand if you're mad..."
    show samantha normal
    samantha.say "More like shocked, [hero.name]."
    samantha.say "I never thought you had it in you!"
    "I honestly don't know whether to be proud or insulted by that."
    "So instead I choose to ignore it and push on."
    mike.say "I just thought it'd be better if you found out from me."
    mike.say "Rather than stumbling across it by accident, you know?"
    "Sam nods, but then her expression becomes serious."
    samantha.say "So what happens now that I know?"
    mike.say "Well, here's the thing..."
    mike.say "I was wondering if you wanted in?"
    mike.say "If you wanted to join us?"
    if samantha.flags.nonexclusive:
        show samantha surprised
        "Sam looks at me for a moment, surprise again on her face."
        "But then I see something more clear come over her expression."
        "She looks intrigued at the suggestion."
        show samantha blush
        "In fact, it looks like she's getting more eager with each second that passes!"
        samantha.say "You..."
        samantha.say "You'd do that?"
        samantha.say "You and the other girls would let me in on it?"
        "I nod, trying to look one hundred percent genuine."
        "Because I want Sam in on this thing more than ever now."
        if samantha.flags.nickname == "cupcake":
            mike.say "Of course, Cupcake!"
        else:
            mike.say "Of course, Sam!"
        mike.say "The girls are all up for you getting involved."
        mike.say "And for me..."
        mike.say "Well...it'd be like a dream come true!"
        "Sam looks at me strangely."
        show samantha normal
        "Almost like what I said last surprised her more than the offer itself."
        samantha.say "I've got to admit, it sounds like fun!"
        samantha.say "Like being in on a really great secret."
        samantha.say "I...I've always been kind of curious, you know?"
        show samantha flirt
        samantha.say "About this kind of kinky stuff, yeah?"
        "I'm still nodding away at all of this."
        "But then I realise that Sam's not actually given me an answer yet."
        if samantha.flags.nickname == "cupcake":
            mike.say "So what are you saying, Cupcake?"
        else:
            mike.say "So what are you saying, Sam?"
        mike.say "Are you in?"
        samantha.say "I...well..."
        show samantha happy
        samantha.say "Yes...yes I am!"
        "I can't help grinning like a fool as Sam says the words."
        "And I can't wait to tell the other girls too."
        "Our little harem just got another member!"
        mike.say "How about we go tell the girls?"
        $ Harem.join_by_name("home", "samantha")
        $ game.flags.ongoinghomeharem = False
        $ samantha.flags.schedule = "harem"
        $ game.pass_time(1)
        if Harem.find(minami, name='home'):
            call fivesome_breeminamisamsasha from _call_fivesome_breeminamisamsasha_5
            call sleep (["bree", "minami", "samantha", "sasha"]) from _call_sleep_43
        else:
            call foursome_breesamsasha from _call_foursome_breesamsasha_4
            call sleep (["bree", "samantha", "sasha"]) from _call_sleep_47
    else:
        show samantha surprised
        "Sam looks at me for a moment, surprise again on her face."
        "But then I see something more clear come over her expression."
        show samantha annoyed
        "She takes a deep breath and lets it out as a heavy sigh."
        "Then she shakes her head."
        samantha.say "No, [hero.name]."
        show samantha angry
        samantha.say "I don't think that I do."
        if samantha.flags.nickname == "cupcake":
            mike.say "Are you sure, Cupcake?"
        else:
            mike.say "Are you sure, Sam?"
        mike.say "This is a big decision."
        mike.say "Wouldn't you like some time to think it over?"
        "Sam shakes her head again."
        "But this time the gesture is more forceful."
        samantha.say "No, I don't."
        samantha.say "I'm grateful that you told me about this."
        show samantha angry
        samantha.say "But I'm not comfortable with what you're doing."
        samantha.say "In fact, I don't think I want to be under the same roof as it."
        mike.say "Y...you're moving out?"
        samantha.say "For now."
        samantha.say "At least while this is still going on."
        "I open my mouth to protest."
        "But the look in Sam's eyes stops me dead."
        "It's telling me that this is a point on which she won't be moved."
        "So I just nod, letting her know that I understand her decision."
        "And then I let the matter drop."
        "Looks like it was a choice between Sam and the other girls."
        "I just hope that I made the right decision."
        hide samantha
        $ samantha.set_gone_forever()
    return

label foursome_breesamsasha:
    scene bg bedroom1 with fade
    "I guess things like this just have a momentum all of their own, right?"
    "Like when you shift something that seems massive and never going to move."
    "The next thing you know, it's rolling downhill, getting faster and faster."
    "And then you couldn't stop it, even if you really wanted to!"
    "I mean, Sam only came round an hour ago."
    "At that time it seemed like the only important thing was cluing her in."
    "You know - on [bree.name], Sasha and me?"
    "Specifically on the fact that we've been sleeping together behind her back."
    "But the moment that she turned out to be okay with it, things changed."
    "Well, not only was Sam okay with it, she also jumped at the chance to get involved too!"
    "And from there, one thing led to another, you know?"
    show bree naked at left
    show sasha naked at right
    show samantha naked
    with dissolve
    "Which is how we come to be here, in my bedroom."
    "All four of us stripping off and casting glances at each other."
    "I guess that now she's accepted the deal, Sam wants to sample the merchandise..."
    "She's certainly sizing up what's on offer right now!"
    "And I can't help feeling a little jealous as she casts an eye over the other girls."
    "Sure, she's seen me naked already, and they are downright gorgeous."
    "But what am I - the last turkey in the shop?!?"
    "Unfortunately for me, it seems my feelings are pretty easily read."
    show bree naked annoyed
    bree.say "Aw..."
    bree.say "What's up, [hero.name]?"
    show sasha joke
    sasha.say "Ah, don't worry about him."
    sasha.say "He's just jealous we're getting all the attention!"
    show bree normal
    show sasha normal
    show samantha at startle
    "Sam's head almost snaps around at Sasha's pronouncement."
    "My guess is that she wasn't aware of how hard she was staring just now."
    "And for a moment, I think that she's going to let the embarrassment get to her."
    mike.say "Ah...no...I..."
    if samantha.flags.nickname == "cupcake":
        mike.say "It's a real eyeful - right, Cupcake?"
    else:
        mike.say "It's a real eyeful - right, Sam?"
    mike.say "I mean in a good way!"
    "The sound of my voice seems to have a positive effect on Sam."
    "It's almost as if she's drawing confidence from my familiar presence."
    show samantha blush
    samantha.say "You're telling me, [hero.name]!"
    samantha.say "But you're the only unique one here."
    samantha.say "You bring something to the party none of us have!"
    show samantha b at center, zoomAt(1.5, (640, 1040))
    "And with that, she closes the distance between us."
    "Sam presses herself against me, her hand rubbing my cock."
    show bree b at center, zoomAt(1.5, (340, 1040))
    show sasha b at center, zoomAt(1.5, (940, 1040))
    "The others walk over to join us, both nodding in agreement."
    sasha.say "Yeah, there's never enough of that to go around!"
    bree.say "So we have to be careful to share, like good girls should!"
    sasha.say "But as you're new, Sam, you get to ride it tonight!"
    bree.say "Mmm-hmm..."
    bree.say "You get to ride the cock rocket all the way to the moon!"
    mike.say "Hah..."
    mike.say "You make me sound like a theme-park ride, [bree.name]!"
    bree.say "Well, why not?"
    bree.say "There's a queue to ride you!"
    sasha.say "And you're at the front of it tonight, Sam!"
    "Sam looks at me sideways and then nods her head towards the bed."
    "I don't need to be told twice, and I clamber straight onto the mattress."
    "Sam follows close behind me, crawling atop me and pinning me down."
    scene foursome breesamsasha
    show foursome breesamsasha tease
    with fade
    "She already has her hands on my cock, rubbing it against her pussy."
    "The sensation is amazing, letting me know that she's slick and ready for me."
    "And then she guides the head between her lips, lowering herself onto it."
    show foursome breesamsasha vaginal
    samantha.say "Oh..."
    samantha.say "Oh, that feels good..."
    "It feels pretty good from where I'm sitting too!"
    "I can feel every inch of my cock as it slides ever deeper into Sam."
    "The weight of her body and the pressing of her muscles makes me gasp."
    "And when I can't get any deeper, she begins to ride me in earnest."
    "I find myself staring up at Sam as she moves like something out of a dream."
    "Her hair falls over her shoulders and her breasts sway slowly."
    "I'm about to reach out in the hope of grabbing them."
    "And that's when I hear voices whispering in my ears."
    bree.say "Ah, hello?"
    bree.say "[hero.name]?"
    sasha.say "Did you forget about us?"
    "I look to my left and then my right, seeing [bree.name] and Sasha flanking me."
    "They're down on all-fours, almost presenting their asses to me!"
    bree.say "Would you mind?"
    sasha.say "Two free hands and two girls at a loose end!"
    "As if to underline the point, they part their buttocks a second later."
    "My eyes dart this way and that, staring at their exposed pussies."
    "There's no way I can look two ways at once."
    "And so instead I settle for feeling my way forwards and keeping my eyes on Sam instead."
    show foursome breesamsasha breevaginal sashavaginal
    "My thumb and fingers find [bree.name]'s lips a second before Sasha's."
    "I hear her giggle at the feeling, the sound full of delight."
    "And then I find the same spot on Sasha too."
    "But her laugh is almost wicked in contrast, filled with dark promises."
    "They're both more than ready for what follows."
    "Their pussies are almost dripping in anticipation."
    "So it's no great challenge to slip one finger after another inside of them."
    "As I do this, the laughter and giggles are replaced with long, low moans of pleasure."
    "And for the short space of time that follows, I have all three of them in the palm of my hand."
    show foursome breesamsasha samanthapleasure
    "Sam keeps right on riding my cock, for all she's worth."
    "Her own hands are squeezing her breasts and pinching her nipples."
    "But all it seems to do is build her desires, rather than release them."
    show foursome breesamsasha breepleasure sashapleasure
    "At the same time, [bree.name] and Sasha are panting like bitches on heat."
    "Their bodies writhe as I work their pussies without mercy."
    "I feel like I'm on another plane, like I've achieved sexual nirvana!"
    "Which is why I hear my own voice before I realise I'm the one speaking..."
    mike.say "Uh...uh..."
    mike.say "Gonna cum..."
    "Quick as a flash, [bree.name] and Sasha are up and pulling Sam off of my cock."
    "She protests for a moment, but then sees the other girls pointing to their mouths."
    "I swear I see her lick her lips as she nods, understanding what they mean."
    scene bj breesamsasha
    show bj breesamsasha samanthasuck
    with fade
    "Before I can do the same thing myself, Sam has my cock in her mouth."
    "She's working on me like a jackhammer, no chance of building up slowly."
    show bj breesamsasha breeballsuck sashaballsuck
    "Her head bobs up and down, while [bree.name] and Sasha busy themselves to either side."
    "They kiss and caress every part of me that Sam's not already claimed for herself."
    "And they smile up at me like a particularly wicked pair of sirens the whole time too!"






    "It doesn't take long before I realize I can't hold on any longer."
    mike.say "I...I can't hold on!"
    show bj breesamsasha -samanthasuck -breeballsuck -sashaballsuck breeopen sashaopen samanthaopen
    "Sam releases me from her mouth, inviting [bree.name] and Sasha around my pulsing dick."
    show bj breesamsasha cumshot with vpunch
    "Within a second, the rising pressure in my cock disappears in a huge cum spray."
    show bj breesamsasha onface with vpunch
    "I watch, panting and exhausted, the three beautiful faces splattered with my jizz."
    with vpunch
    "Afterwards, Sam can't help shaking her head at what we just did."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake?"
    else:
        mike.say "Sam?"
    mike.say "Are you okay?"
    samantha.say "What?!?"
    samantha.say "Oh, yeah - I'm better than okay."
    bree.say "So you like it this way?"
    sasha.say "It's a real eye-opener, huh?"
    samantha.say "I...I always thought I'd feel jealous, you know?"
    samantha.say "But it's not like that at all."
    samantha.say "In fact, it's like there's so much more of everything to go around!"
    "There's no need to say anything more to that."
    "And so all Sam gets in the way of an answer is a round of nods."
    "Because sometimes silence can say so much more than words."
    $ samantha.sexperience += 1
    return

label fivesome_breeminamisamsasha:
    scene bg bedroom1 with fade
    "I've never been the kind to go in for mind-altering substances or drugs of the hallucinogenic kind."
    "But all the same, the place I find myself in right now is pretty much how I imagine they'd feel."
    "The whole thing took on a distinctly trippy, dream-like quality after the girls sprang their surprise on Sam."
    "And it only got that much stranger when she reacted by jumping on board and getting in on the action too!"
    "Well, one thing leads to another, as they say."
    show bree at top_mostleft
    show minami at left4
    show samantha at right4
    show sasha at top_mostright
    with dissolve
    "So here we are, in my bedroom - all five of us!"
    "Once it was decided that Sam was to become a part of our..."
    "Ah, what would you call this kind of thing anyway?"
    "A polygamous relationship?"
    "A harem?"
    "An orgy?"
    "Well, whatever it is - once Sam was in, it felt like there was only one way to properly mark the occasion."
    "Everyone's still buzzing from the thrill of it all, and so there's no time to waste waiting for the comedown."
    "Even so, there are so many bodies involved in this thing, no one seems to know who's in charge!"
    show bree blush underwear
    show minami blush naked
    show samantha blush underwear
    show sasha underwear
    with dissolve
    "We all start stripping off, but then stop and stare at each other."
    "No one can figure out who goes where and who does what."
    "And when we finally manage to speak, everyone ends up talking at once."
    mike.say "Erm, I guess I could..."
    show bree evil
    bree.say "I wouldn't mind getting some..."
    show minami tehe at left4, startle
    minami.say "I should probably go on top..."
    show samantha sad at right4, startle
    samantha.say "I don't want to step on anybody's toes..."
    show sasha annoyed at center, zoomAt(1.25, (1040, 840))
    sasha.say "SHUT UP!" with vpunch
    show bree normal at top_mostleft
    show minami normal at left5
    show samantha normal at center
    with ease
    "Everyone falls silent at the commanding tone of Sasha's voice."
    sasha.say "I'm directing traffic tonight, okay?"
    "The statement is greeted by a series of hastily exchanged glances."
    "And then everyone, myself included, nods in agreement."
    sasha.say "Right, let's get things moving!"
    sasha.say "Sam's the noob, so she gets to ride cock."
    "Sasha looks around the assembled faces, waiting for any objections."
    "But all she gets is another round of nods."
    "Well, that and maybe the smallest of blushes from Sam and me!"
    show sasha joke at center, zoomAt(1.0, (1040, 840)), startle
    sasha.say "Well, what are you waiting for?"
    show fx exclamation at center, zoomAt(1.25, (1040, 840))
    sasha.say "Let's get this show on the road!"
    show sasha normal naked with dissolve
    "Sasha takes the lead, beginning to strip off in front of everyone else."
    show bree naked
    show samantha naked
    with dissolve
    "And soon enough, the rest of the girls are following her example."
    "It feels a little odd at first, almost like getting undressed in the locker-room at the gym."
    "But as the sly little glances and giggles begin, reminding us of what's actually happening here."
    "And when I begin to see flashes of breasts and buttocks, I feel my mind instinctively shift gear."
    "This is nothing like the changing rooms at the gym!"
    "Showing off your body here isn't something you do surreptitiously."
    "And getting hands on is the entire point!"
    "Once we're all naked, Sasha holds out a hand to Sam."
    sasha.say "Come here, Sam."
    sasha.say "That's right, just follow me..."
    "Sam looks understandably nervous, but she takes Sasha's hand all the same."
    "She allows the other girl to guide her to the bed and lay her down."
    "Sasha positions herself behind Sam, cradling her head in her lap."
    "From there, she motions to the others."
    "[bree.name] she points to her left, Minami to her right."
    scene fivesome breeminamisamsasha
    show fivesome breeminamisamsasha breelookdown sashalookdown minamilookdown
    with fade
    "And finally, she beckons me to the obvious position required."
    "I feel like holding back for a moment, just to commit the scene to memory."
    "There's Sam, one of the most beautiful girls that I've ever come across."
    "But her head is laying between Sasha's amazing breasts."
    if not bree.is_visibly_pregnant:
        "To one side of her, [bree.name] is crouched, stroking her flat stomach."
    else:
        "To one side of her, [bree.name] is crouched, stroking her round stomach."
    "And on the other, Minami is squeezing her breasts too!"
    "As for Sam herself, she looks almost overwhelmed."
    "She's already beginning to pant from the attention of the other girls."
    "But she's holding my eye as I lower myself onto her, biting her lip in anticipation."
    "I'm close enough to feel my cock rubbing between her legs now."
    "And I can see that she's already getting wet down there."
    "Yet there's still something making me hold back."
    "I can't tell what it is, until the moment that Sam nods eagerly."
    "That's it, right there - I was waiting for her to give me permission."
    "And now that I have it, there's nothing in this world that could hold me back!"
    "I part Sam's thighs and push into her almost in the same motion."
    "My cock doesn't need to be shown where to go, and it finds her lips with ease."
    "I hear Sam whimper in anticipation as the head rubs against the slick folds."
    show fivesome breeminamisamsasha vaginal
    "And then I'm inside of her, pushing aside any lingering resistance like it's not even there at all."
    "I don't stop until my cock is as deep into Sam as I can get."
    "Then I hold it there for a moment, just enjoying the sensation."
    show fivesome breeminamisamsasha samanthablush
    "Sam gasps at being filled so completely."
    "And then she moans, releasing all that she's feeling along with it."
    "While all of this is going on, [bree.name] and Minami don't sit back and watch."
    "Instead they redouble their efforts, hands travelling all over Sam's helpless body."
    "They kiss her nipples as they play with her breasts."
    if samantha.is_visibly_pregnant:
        "And their free hands slide over her rounded stomach."
    else:
        "And their free hands slide over her flat stomach."
    "All the time teasing that they might soon go lower..."
    "Not wanting to leave all of the work to [bree.name] and Minami, I begin to move inside of Sam."
    "I try to keep the thrusts that I'm making in and out of slow at first."
    "But all too soon I can feel my speed beginning to increase as I surrender to the moment."
    samantha.say "Oh..."
    samantha.say "Oh fuck..."
    show fivesome breeminamisamsasha breelookup
    bree.say "Hmm..."
    bree.say "Sounds like someone's having fun!"
    show fivesome breeminamisamsasha minamilookup
    minami.say "No kidding - looks like she's gonna cum too!"
    sasha.say "She can cum all she likes."
    show fivesome breeminamisamsasha sashalookup
    sasha.say "He doesn't get to shoot his load until we're done with him!"
    "Sasha underlines her point by nodding in my direction."
    "She gestures to [bree.name] and Minami, and they hastily pull me off of Sam."
    mike.say "Hey!"
    mike.say "What the hell?!?"
    show fivesome breeminamisamsasha samanthalookdown
    samantha.say "Oh god!"
    samantha.say "I'm cumming...right now!"
    "I watch as Sam curls into a ball on the bed, her orgasm taking hold."
    "She moans and twitches, and I can't help feeling a little left out in the cold."
    "As if she understands my feelings, Sasha grabs my hand and pulls me to my feet."
    sasha.say "No need for the long face, [hero.name]."
    sasha.say "This next part is a treat just for you!"
    scene bj breeminamisamsasha
    show bj breeminamisamsasha sashasuck
    with fade
    "Sasha gets down on her knees before me and kisses the tip of my cock."
    "[bree.name] and Minami hurry to follow her example."
    "They huddle in close so that they can get in on the action too."
    "Even Sam seems keen to join in, sliding off of the bed as soon as she's able."
    "Pretty soon I've all but forgotten about being pulled off Sam."
    "And I have to admit, a blowjob from all four of them is more than ample compensation!"
    show bj breeminamisamsasha breesuck -sashasuck
    "Sasha, [bree.name], Minami and Sam pass my cock from one mouth to the next."
    show bj breeminamisamsasha minamisuck -breesuck
    "The feeling of going from one to another almost as good as when it's actually inside."
    show bj breeminamisamsasha samanthasuck -minamisuck
    "And while whoever has it between their lips is busy sucking and caressing, the others keep themselves busy too."
    show bj breeminamisamsasha sashasuck -samanthasuck
    "It's almost impossible for me to tell who's sucking my balls or stroking the shaft from one moment to the next."
    show bj breeminamisamsasha breesuck -sashasuck
    "Somehow they all seem to know just what to do and when, working in what feels like perfect harmony."
    show bj breeminamisamsasha minamisuck -breesuck
    "Their smiles and giggles are like music to my ears, as they eagerly await their turn to suck on my cock."
    show bj breeminamisamsasha sashasuck -minamisuck
    "I really don't want this to end, but I can feel myself getting ready to cum!"
    show bj breeminamisamsasha samanthasuck -sashasuck
    mike.say "I...I can't hold on!"
    mike.say "I'm gonna..."
    show bj breeminamisamsasha -samanthasuck breeopen minamiopen samanthaopen sashaopen big
    "As if on cue, I feel my cock released so that it sways and bobs in front of them."
    show bj breeminamisamsasha cumshot with vpunch
    "I lose it a second later, the motion of my dick sending it this way and that."
    show bj breeminamisamsasha breeonface minamionface samanthaonface sashaonface with vpunch
    "Sasha, [bree.name], Minami and Sam all get their cheeks painted with the sticky, white cum."
    show bj breeminamisamsasha breeonface minamionface samanthaonface sashaonface with vpunch
    "They shriek, yelp and giggle as they're showered, loving every moment."
    "All I can do is stand there panting, trying to catch my breath."
    "Sam is the first one to speak, after licking her lips to chase a drop of cum."
    scene bg bedroom1
    show samantha naked cum at right4
    with fade
    samantha.say "So is it official now?"
    samantha.say "Am I like bonded to you guys?"
    show bree naked cum at top_mostleft with dissolve
    bree.say "All I know is that I'm going to be bonded to this carpet if I don't get cleaned up!"
    show minami naked at left4 with dissolve
    minami.say "Yeah, I'm bringing an umbrella next time!"
    show sasha naked cumface at top_mostright with dissolve
    sasha.say "Ignore them, Sam - they think they're funny."
    show sasha happy
    sasha.say "But yeah, you're officially one of us now."
    "Sam smiles at this, but makes a point of looking at me as she does so."
    show fx question at right4
    samantha.say "Is that right, [hero.name]?"
    show bree naked evil
    bree.say "Oh, don't ask him, Sam."
    show minami hunt
    minami.say "Yeah, he's just the meat!"
    mike.say "Sasha's right - you guys really aren't funny!"
    if samantha.flags.nickname == "cupcake":
        mike.say "You're in, Cupcake - of course you are!"
    else:
        mike.say "You're in, Sam - of course you are!"
    $ samantha.sexperience += 1
    return

label samantha_sharing_bed:
    scene bg bedroom1 with fade
    "It's been a long, hard day, at least by my standards."
    "And all I'm thinking about is turning in and getting some much needed sleep."
    "I'm sure there was something that I wanted to find out before I slept."
    "But it's too late for that now, and whatever it was has totally slipped my mind."
    play sound door_knock
    "So you can imagine my irritation when I hear the sound of a knock at the door."
    mike.say "Urgh..."
    mike.say "What now?!?"
    "I keep on muttering to myself as I stalk across the room."
    scene bg black with dissolve
    pause 0.1
    scene bg livingroom
    show samantha underwear normal
    with wiperight
    "But as soon as I open the door and look into the corridor, my mood changes."
    show samantha happy
    samantha.say "Hi, [hero.name]..."
    show samantha talkative
    samantha.say "Hope I didn't get you out of bed!"
    show samantha normal
    "I blink as I stare at Sam, standing there with a smile on her face."
    "Mainly confused because she's dressed like she's about to go to bed too."
    mike.say "Erm..."
    if samantha.flags.nickname == "cupcake":
        mike.say "No, Cupcake..."
    else:
        mike.say "No, Sam..."
    mike.say "I hadn't made it that far yet!"
    show samantha happy
    samantha.say "Oh, that's good."
    samantha.say "I thought I might have to wake you up!"
    show samantha talkative
    samantha.say "Well, are you going to let me in or what?"
    show samantha normal at center, zoomAt(1.5, (640, 1040))
    "Sam makes to push her way past me."
    "And I only stay where I am because the action totally throws me."
    "I mean, I always had fantasies about Sam sneaking into my room at night."
    "But in them she was a little more subtle and a lot more seductive than this!"
    mike.say "Whoa..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Wait a minute, Cupcake!"
    else:
        mike.say "Wait a minute, Sam!"
    mike.say "What's going on here?"
    mike.say "Why are you wanting to come into my bedroom right now?"
    show samantha surprised at center, zoomAt(0.8, (640, 840)), vshake
    "Sam takes a step back, looking more than a little confused."
    show samantha annoyed
    samantha.say "I..."
    samantha.say "I thought this was part of the arrangement?"
    show samantha sadsmile
    mike.say "When did we arrange that you'd sleep with me?!?"
    show samantha sad
    samantha.say "Didn't we agree that you'd each share with me on a different night?"
    show samantha sadsmile
    play sound spank
    with vpunch
    "The moment Sam explains herself, I slap myself on the forehead."
    "That was it, the thing I was meaning to ask the others."
    "Sam's shared a room with all of the girls by now."
    "So where does she sleep after that?"
    "I was expecting that they'd just go round again."
    "But it seems like Sam has a very different idea."
    mike.say "I...I thought it was just the girls you were sharing with?"
    mike.say "I mean...I assumed you wouldn't want to share with me!"
    mike.say "You know - with a guy?"
    show samantha surprised
    "Sam shakes her head at this, looking a little confused."
    samantha.say "Why not, [hero.name]?"
    show samantha talkative
    samantha.say "We're friends, aren't we?"
    samantha.say "And I've known you longer than anyone else living here, haven't I?"
    show samantha happy
    samantha.say "I trust you to look after me."
    show samantha normal
    "The smile Sam gives me as she says all of this just isn't fair."
    "It makes her whole face light up, and it instantly melts me inside."
    "But I have to make a decision quickly."
    "I can't leave her standing out in the corridor all night."
    menu:
        "Turn her away":
            mike.say "Ah..."
            mike.say "I just don't think it's a good idea, Sam - that's all."
            "Sam frowns at this, cocking her head on one side."
            show samantha surprised
            samantha.say "What do you mean, [hero.name]?"
            samantha.say "Why's it a bad idea?"
            "I let out a sigh and shake my head."
            if samantha.flags.nickname == "cupcake":
                mike.say "Look, Cupcake..."
            else:
                mike.say "Look, Sam..."
            mike.say "You've been through a lot lately."
            mike.say "You've had your whole world turned upside down."
            mike.say "And that can make people do things they'd normally never do."
            mike.say "It can make them interpret things in a way they wouldn't at another time."
            "Sam's frown loosens a little as she ponders my words."
            "But then she nods, as if she's starting to see what I mean."
            show samantha sad
            samantha.say "I...I think I get it, [hero.name]."
            samantha.say "I guess we're all a little messed up, huh?"
            samantha.say "It's kind of like being drunk and doing something you regret later, right?"
            show samantha sadsmile
            if samantha.flags.nickname == "cupcake":
                mike.say "Yeah, Cupcake..."
            else:
                mike.say "Yeah, Sam..."
            mike.say "It's kinda like that."
            show samantha sad at center, zoomAt(0.8, (740, 840)) with ease
            "She nods again and takes a step back from the door."
            show samantha talkative
            samantha.say "Maybe I'll go knock on some other doors."
            samantha.say "Find somewhere quiet to think about what you just said."
            show samantha sadsmile
            pause 0.1
            hide samantha with easeoutright
            $ samantha.love -= 5
            "With that, she turns on her heel and walks away."
            "Which leaves me to close my door and get into bed."
            scene bg bedroom1 with fade
            "All the time hoping that I just made the right decision."
            "Because it feels like it sucks in the right now."
            "So I hope it pays off in the long run!"
        "Take the bed, I'll sleep on the floor":
            $ samantha.set_room("bedroom1")
            if samantha.flags.nickname == "cupcake":
                mike.say "Okay, Cupcake..."
            else:
                mike.say "Okay, Sam..."
            mike.say "You win - you can sleep in my bed tonight."
            show samantha happy
            mike.say "But!"
            "I hold up a hand to stop Sam as she smiles and tries to push past me."
            mike.say "But only on the understanding that I sleep on the floor, okay?"
            show samantha surprised
            "I study the look on Sam's face as she reacts to my ultimatum."
            "She looks surprised and maybe even a little disappointed."
            "But she nods all the same, agreeing to my terms."
            show samantha talkative
            samantha.say "Sure, [hero.name]..."
            samantha.say "If that's what you want."
            show samantha sadsmile
            "I nod and then stand aside, finally letting Sam into my room."
            scene bg bedroom1
            show samantha underwear normal
            with fade
            "She hurries inside and over to the bed as I close the door behind her."
            "And when I turn round, she's already under the covers."
            "I do the best I can to look casual, like seeing her there means nothing."
            "But the truth is it's one of the hardest things I've ever had to do."
            "I can't count the number of times I've imagined having Sam in my own bed."
            "And now it's happening, I have to bed down on the floor a few feet from her!"
            show samantha surprised
            samantha.say "Why are you looking at me like that, [hero.name]?"
            show samantha annoyed
            samantha.say "Is there something wrong?"
            show samantha sadsmile
            mike.say "Ah..."
            if samantha.flags.nickname == "cupcake":
                mike.say "No, Cupcake..."
            else:
                mike.say "No, Sam..."
            mike.say "There's nothing wrong."
            mike.say "I'm just tired, that's all!"
            show samantha talkative
            samantha.say "Okay."
            samantha.say "Good night then!"
            hide samantha
            show multisleep homeharem samantha underwear nomc fall
            with fade
            "With that, Sam lies down and puts her head on the pillow."
            "I spend a few minutes hunting out a spare pillow and sheets for myself."
            "Then I do the best I can to make myself comfortable on the floor by the bed."
            "Pretty soon I hear the sound of Sam beginning to snore gently."
            "But I can't seem to drop off myself."
            "It could be the fact I'm sleeping on the hard floor."
            "Or more likely that I can't stop thinking of how close she is to me right now."
            "And I know that I'm going to wake up sore and grumpy tomorrow morning."
            $ samantha.love += 4
            $ hero.energy -= 5
        "I'll make some space":
            $ samantha.set_room("bedroom1")
            if samantha.flags.nickname == "cupcake":
                mike.say "You're right, Cupcake."
            else:
                mike.say "You're right, Sam."
            mike.say "What was I even thinking!"
            mike.say "Of course you can sleep in here tonight."
            "I step aside and wave Sam into the room."
            "And she wastes no time stepping inside."
            scene bg bedroom1
            show samantha underwear happy
            with fade
            samantha.say "Wow!"
            samantha.say "Your bed's bigger than I remember it being, [hero.name]."
            samantha.say "There's plenty of room for us both in there."
            show samantha normal
            "I rub the back of my neck as I walk over to the opposite side of the bed."
            scene multisleep homeharem fall with fade
            "Sure, I'm full of talk about how this is just a couple of friends in the same bed."
            "But now I'm recalling all the times I imagined Sam being under those sheets with me!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Yeah, Cupcake - there's plenty of space."
            else:
                mike.say "Yeah, Sam - there's plenty of space."
            mike.say "But it can get pretty cold in here at night."
            show multisleep homeharem samantha underwear with fade
            "Sam chuckles as she pulls back the covers and hops in on her side."
            samantha.say "Is that so?"
            samantha.say "Hmm...then I guess I should warn you..."
            samantha.say "I have a habit of cuddling in my sleep, okay?"
            samantha.say "So just elbow me in the ribs if I do that."
            samantha.say "Ryan used to complain about me putting my cold feet on him all the time!"
            "I nod and smile, trying not to show how much that idea's affecting me."
            "And I'm very grateful for the fact the bedclothes are covering me up right now."
            "Because the idea of Sam snuggling up to me in her sleep is making me hard!"
            mike.say "I...I'm going to turn the light off now..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Okay, Cupcake?"
            else:
                mike.say "Okay, Sam?"
            samantha.say "Okay, [hero.name]."
            samantha.say "Good night, sleep tight!"
            "I switch the light off and bury my head in the pillow."
            show multisleep homeharem samantha underwear at dark, dark
            "Once the light is off, I honestly do the best I can to fall asleep."
            "But it's hard to turn off my brain with Sam laying mere inches away."
            "All I can hear is the sound of her breathing softly."
            "And I'm afraid to move for fear of disturbing her."
            "Or even worse, accidentally touching her under the covers!"
            "Pretty soon I'm lost in that weird time-warp you get in bed."
            "It feels like I've been laid there forever."
            "But for all I know, it could have just been a couple of minutes."
            "The spell is only broken when I hear Sam make a groaning sound."
            "Then she turns over beside me, closing the short distance between us."
            scene bg black
            show cuddle samantha at dark, dark
            with fade
            "I feel her nestle herself against my back, spooning with me."
            "Then her arm reaches over and wraps around me."
            menu:
                "Jab her in the ribs":
                    "Almost without thinking, I do exactly what Sam told me to do."
                    "As gently as I can, I jab an elbow into her."
                    samantha.say "Wha..." with hpunch
                    samantha.say "Ouch!"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry, Cupcake..."
                    else:
                        mike.say "Sorry, Sam..."
                    mike.say "But you were sleep spooning!"
                    samantha.say "I...I was?"
                    samantha.say "Oh, sorry!"
                    scene bg black
                    show multisleep homeharem samantha underwear fall at dark, dark
                    with fade
                    "With that, she turns over and inches away from me."
                    "I feel bad at jabbing Sam in the ribs."
                    "But that was what she told me to do."
                    "And it seems to have done the trick."
                    "From that point on, she keeps to her side of the bed."
                    "Soon enough I find myself drifting off to sleep."
                    "Secure in the knowledge that we avoided anything inappropriate happening between us."
                    $ samantha.love += 2
                "Enjoy the moment":
                    "I know that Sam told me to give her a jab in the ribs if this happened."
                    "But the sensation of her wrapping herself around me is just too much."
                    "It's like a dream coming true, and I can't bring myself to do it."
                    "I keep telling myself that it's okay because she's asleep."
                    "She won't remember any of this in the morning."
                    "And I won't tell her it happened to save her the embarrassment."
                    "So I just lie there in silence, enjoying the feeling of her body against mine."
                    "That is until the moment I feel Sam's hand sliding into my shorts!"
                    "I gasp as her fingers close around my cock."
                    "And then they squeeze it hard, giving away her intent!"
                    menu:
                        "Jab her in the ribs":
                            "Almost without thinking, I do exactly what Sam told me to do."
                            "As gently as I can, I jab an elbow into her."
                            samantha.say "Wha..." with hpunch
                            samantha.say "Ouch!"
                            "I breathe a sigh of relief as her hand lets go of my cock."
                            "Then it's pulled out of my shorts too."
                            if samantha.flags.nickname == "cupcake":
                                mike.say "Sorry, Cupcake..."
                            else:
                                mike.say "Sorry, Sam..."
                            mike.say "But you were sleep spooning!"
                            samantha.say "I...I was?"
                            samantha.say "Oh, sorry!"
                            scene bg black
                            show multisleep homeharem samantha underwear fall at dark, dark
                            "With that, she turns over and inches away from me."
                            "I feel bad at jabbing Sam in the ribs."
                            "But that was what she told me to do."
                            "And it seems to have done the trick."
                            "From that point on, she keeps to her side of the bed."
                            "Soon enough I find myself drifting off to sleep."
                            "Secure in the knowledge that we avoided anything inappropriate happening between us."
                            "Sure it's pretty suspicious, but I'm just going to chalk Sam's actions up to her being asleep."
                            "No need to tell her all about it and cause her any more embarrassment."
                            $ samantha.love += 2
                        "Let her sleep" if hero.stamina:
                            "I'm almost holding my breath as I wait to see what Sam will do next."
                            "And sure enough, she starts to slowly stroke her hand up and down."
                            "The sensation is amazing, filling me with excitement."
                            "I know Sam told me that she cuddled in her sleep."
                            "But could she really be doing this without knowing it?"
                            "Well, there's one sure way to find out."
                            if samantha.flags.nickname == "cupcake":
                                mike.say "C...Cupcake..."
                            else:
                                mike.say "S...Sam..."
                            mike.say "Are you..."
                            samantha.say "Mmm..."
                            samantha.say "What do you think?"
                            "The sound that Sam makes is half a laugh and half a sigh of pleasure."
                            "I can feel her warm breath against my ear, her breasts against my back."
                            samantha.say "I'll stop if you tell me to."
                            samantha.say "Just say the word..."
                            "My heart is beating faster with each second that passes."
                            "But I already know that I'm not going to tell Sam to stop."
                            "She giggles, knowing that she's literally got me in the palm of her hand."
                            samantha.say "No..."
                            samantha.say "I didn't think so!"
                            samantha.say "So just lie still, [hero.name]."
                            samantha.say "And let me say thank you for being such a good friend to me!"
                            samantha.say "Or maybe..."
                            "Sam pauses as she presses herself more closely against me."
                            samantha.say "Maybe you'd like to give me something instead?"
                            menu:
                                "Let Samantha play with you":
                                    mike.say "N...no..."
                                    mike.say "This is...just fine!"
                                    "Sam giggles again."
                                    show samantha handjob naked onmike open at dark with fade
                                    samantha.say "Whatever you say, [hero.name]."
                                    samantha.say "I am in your debt, after all."
                                    samantha.say "You've been the best friend I could have asked for."
                                    samantha.say "And well...I've kind of grown to see you as more than that!"
                                    show samantha handjob naked tease
                                    "All the time she's telling me exactly what I want to hear, Sam's also stroking my cock."
                                    "I could never have imagined it happening like this."
                                    "The girl I always held a torch for is confessing that she wants to be more than friends."
                                    "And she's doing while giving me a hand-job!"
                                    show samantha handjob naked mc_pleasure at dark
                                    mike.say "Oh, Sam..."
                                    mike.say "You're so good..."
                                    mike.say "Too good to be true!"
                                    show samantha handjob naked ondick speed
                                    "Sam sighs as she begins to pick up speed."
                                    "It's like my words are getting her hotter by the second."
                                    show samantha handjob naked onmike open
                                    samantha.say "Oh no, [hero.name]..."
                                    samantha.say "This isn't a dream."
                                    samantha.say "But I'll make it feel like one, just for you!"
                                    show samantha handjob naked ondick concentrate
                                    "I have no idea if Sam's giving me the best hand-job I've ever had."
                                    "Or if it just feels that way because I want it so much."
                                    "But either way, I'm panting from the way she's touching me."
                                    with vpunch
                                    "And it doesn't take long for her efforts to pay off."
                                    show samantha handjob naked mc_ahegao cumshot at dark with vpunch
                                    "I gasp as I shoot my load, unable to hold back."
                                    show samantha handjob naked mc_ahegao dickcum -cumshot -speed at dark with vpunch
                                    "Sam giggles one last time, still squeezing as it covers her hand."
                                    show samantha handjob naked tease onmike
                                    samantha.say "Mmm..."
                                    show samantha handjob naked open
                                    samantha.say "I think you'll sleep better now!"
                                    show samantha handjob naked tease
                                    if samantha.flags.nickname == "cupcake":
                                        mike.say "Y...yeah, Cupcake..."
                                    else:
                                        mike.say "Y...yeah, Sam..."
                                    mike.say "Like a log!"
                                    "And she's right."
                                    "I fall asleep soon afterwards."
                                    "My head filled with visions and memories of Sam."
                                "Fuck Samantha" if samantha.sexperience >= 5:
                                    mike.say "R...really?"
                                    mike.say "You mean you want to..."
                                    "Sam giggles again."
                                    samantha.say "Oh, [hero.name]..."
                                    samantha.say "I could never tell you this before."
                                    samantha.say "But I used to think about doing this all the time!"
                                    "Sam's words are enough to blow my mind."
                                    "I can't actually believe what she's saying."
                                    mike.say "You did?!?"
                                    show multisleep homeharem samantha underwear at dark with fade
                                    samantha.say "Oh yeah!"
                                    samantha.say "I used to have this little fantasy..."
                                    samantha.say "In it, I'd sneak out of bed with Ryan."
                                    samantha.say "Then I'd come down here and jump in bed with you!"
                                    "I have no idea if Sam's telling the truth right now."
                                    "For all I know, she could have cooked that story up a few minutes ago."
                                    "But in the end, what does that matter?"
                                    "The girl I've dreamed about is right here in my bed."
                                    "And she's telling me all about how she wants me to fuck her!"
                                    samantha.say "Then you'd take off my pyjamas..."
                                    show multisleep homeharem samantha -underwear at dark
                                    "I'm doing as she says before she can even get the words out."
                                    "Pulling down her pants and popping the buttons off her top."
                                    samantha.say "Oh, [hero.name]..."
                                    samantha.say "Just like that!"
                                    samantha.say "I'd turn over..."
                                    samantha.say "Like this..."
                                    scene bg black
                                    show samantha flat doggy bedroom at dark
                                    with fade
                                    "Sam slowly rolls over so that her back is turned to me."
                                    "Without thinking, I follow her example."
                                    "Now my belly is facing her back."
                                    samantha.say "And then I'd snuggle up to you..."
                                    samantha.say "Like this..."
                                    "Sam pushes her butt into me, making sure to grind at the same time."
                                    "And the moment I feel her do that, I know there's no going back."
                                    samantha.say "Then you'd..."
                                    samantha.say "You'd..."
                                    samantha.say "Put it in me..."
                                    show samantha flat doggy bedroom anal at dark
                                    samantha.say "Oh fuck..."
                                    samantha.say "Just like that!"
                                    "I don't know what's turning me on more right now."
                                    "The sensation of my cock sinking into Sam."
                                    "Or hearing her describe what I'm doing to her at the same time."
                                    "It feels like I'm making her fantasy come true."
                                    "And I know for certain that I'm making mine a reality."
                                    samantha.say "Don't stop..."
                                    show samantha flat doggy bedroom pleasure at dark
                                    samantha.say "Please, [hero.name]..."
                                    "I do as Sam asks, beginning to move inside her."
                                    "Part of me wants to go as hard and fast as I can."
                                    "I've wanted this for so long that it's hard to resist the urge."
                                    "But I can feel the way Sam's putting herself in my hands."
                                    "The way that she's trusting me to take care of her."
                                    "And so I make sure that I take it slow and steady."
                                    "But that doesn't mean I go lightly or hold anything back."
                                    "I make sure to get as deep into Sam as I can with each thrust."
                                    "And I can feel the satisfaction that gives her every time."
                                    "She pushes herself backwards into me."
                                    "At the same time my hands are roaming all over her body."
                                    "Sam moans as I find her breasts and begin to massage them."
                                    "But the moans turn into cries when I pinch at her nipples too."
                                    "For a moment I hesitate, worried about how thick the walls are."
                                    "What if someone else hears us?"
                                    "But so what if they do?"
                                    "With that thought, I redouble my efforts."
                                    "I'd be a complete fool to let something like that ruin this moment."
                                    "Who cares if one of my housemates hears me and Sam?"
                                    "It's not like I'm going to apologise for what we're doing."
                                    "So I keep right on going, sinking deep into Sam with every thrust."
                                    "She's on the same page as me too, nodding the whole time."
                                    "Which means that I know she wants it every bit as much as I do."
                                    "But soon enough I can feel her beginning to twitch in my arms."
                                    "Sam moans as she starts to cum, and her body reacts as well."
                                    show samantha flat doggy bedroom ahegao at dark
                                    "The muscles inside her contract, squeezing me harder than ever."
                                    "And a moment later, I'm losing it too."
                                    "Sam holds onto me for all she's worth."
                                    show samantha flat doggy bedroom cum at dark with hpunch
                                    "Then she rides me until the very end."
                                    with hpunch
                                    "I lose it inside her, filling her with everything that I have."
                                    with hpunch
                                    samantha.say "Mmm..."
                                    show samantha flat doggy bedroom cum normal at dark
                                    samantha.say "I wish you could do that to me every night."
                                    samantha.say "I think you'll sleep better now!"
                                    if samantha.flags.nickname == "cupcake":
                                        mike.say "Y...yeah, Cupcake..."
                                    else:
                                        mike.say "Y...yeah, Sam..."
                                    mike.say "Like a log!"
                                    "And she's right."
                                    show samantha flat doggy bedroom cum ahegao at dark, dark with dissolve
                                    "I fall asleep soon afterwards."
                                    show samantha flat doggy bedroom cum ahegao at blacker with dissolve
                                    "My head filled with visions and memories of Sam."
                            $ samantha.love += 2
                            $ samantha.sexperience += 1
                            scene bg black with dissolve
    return

label samantha_sasha_pregnant_showdown:
    show sasha zorder 2
    hide samantha
    with fade
    "Sasha leans over to whisper something to me, but I'm a little distracted as she does so."
    show samantha zorder 1 at right with easeinright
    "Mainly because Sam just so happens to be walking by, and I'm enjoying checking out her ass!"
    show sasha joke
    sasha.say "[hero.name]..."
    sasha.say "Have you noticed something different about Sam?"
    show sasha normal
    mike.say "Huh?"
    mike.say "What do you mean, Sasha?"
    show samantha at left4 with ease
    "I try not to sound guilty as I answer the question."
    show samantha at left5 with ease
    "And that's because I'm seeing both Sasha and Sam behind the other's back right now!"
    show samantha at left with ease
    "So one of them sticking her nose into what the other is doing can't be a good thing."
    show samantha at top_mostleft with ease
    show sasha joke
    sasha.say "Oh come on!"
    sasha.say "Her belly's getting bigger every time I see her."
    sasha.say "It doesn't take a genius to figure it out!"
    show sasha normal
    "I open my mouth to say something in response."
    show sasha surprised at right5
    show samantha at left5
    with hpunch
    "But someone else beats me to it."
    samantha.say "I couldn't help overhearing what you two were saying just now."
    samantha.say "And it's no secret, Sasha - I am pregnant!"
    show sasha annoyed
    "Sasha looks more than a little embarrassed to have been overheard."
    "But there's nothing I can do to keep myself from going pale."
    "These two can't be having a conversation about that!"
    show samantha surprised
    samantha.say "What's the matter, [hero.name]?"
    samantha.say "You look like you've seen a ghost!"
    show sasha surprised
    sasha.say "Yeah, man..."
    sasha.say "You're white as a sheet!"
    show samantha annoyed
    show sasha annoyed
    "Sam frowns and cocks her head on one side."
    show samantha surprised
    samantha.say "Wait a minute, [hero.name]..."
    samantha.say "Why didn't you tell Sasha I was pregnant already?"
    show samantha sad
    "I can feel the panic rising inside of me as everything starts to unravel."
    show sasha joke
    "Sasha frowns and shoots me a withering glance."
    sasha.say "Huh?"
    sasha.say "Why would he know about that, Sam?"
    sasha.say "Because you only told your really old friends?"
    show samantha surprised
    "Sam chuckles and shakes her head."
    samantha.say "What?"
    samantha.say "No, because..."
    mike.say "Oh man - is that the time?!?"
    mike.say "I just remembered, we all have to be somewhere else right now!"
    show samantha angry
    show sasha angry
    "Sam and Sasha are both looking at my with suspicion now."
    "And I can feel my fate closing in on me."
    show samantha annoyed
    samantha.say "Because he's the father, Sasha!"
    samantha.say "So of course he knows about it!"
    show sasha wtf
    sasha.say "WHAT THE HELL?"
    show sasha angry
    sasha.say "You two have been fucking behind my back?!?"
    show samantha surprised
    samantha.say "Wait..."
    show samantha annoyed
    samantha.say "What do you mean behind YOUR back?"
    "I'm almost done turning around and preparing to run."
    show sasha angry
    show samantha angry
    "But then then the two of them turn on me as one."
    sasha.say "[hero.name]!"
    samantha.say "Stop right there!"
    mike.say "I..."
    mike.say "I don't know what to say, guys!"
    mike.say "I love the both of you, and I just couldn't choose!"
    if samantha.love >= 125 and sasha.love >= 125:
        "Sam and Sasha are still looking at me like they want to kill me."
        "But I can see their expressions softening by the second."
        show samantha normal
        samantha.say "You know, I should dump your ass."
        samantha.say "You cheated on me, just like Ryan did!"
        samantha.say "But I know you better than that, [hero.name]."
        samantha.say "I know that if you say you love two girls, then you mean it!"
        show sasha normal
        sasha.say "You know what, I'm supposed to be in a fucking metal band."
        sasha.say "So maybe it's time I started to behave like it."
        sasha.say "And not like some prissy old woman!"
        sasha.say "I mean, who really cares you're fucking two girls at once?"
        samantha.say "Who cares?"
        "I can hardly believe what I'm hearing."
        "Are they really agreeing to share me?"
        mike.say "You mean..."
        mike.say "You're okay with it?"
        mike.say "With me being with you both?!?"
        show sasha blush
        show samantha blush
        "Sam and Sasha exchange a certain kind of look."
        "And I note that they both flush with colour at the same time."
        samantha.say "More than okay, [hero.name]!"
        sasha.say "Maybe we can all get something out of this?"
        "Are they..."
        "They are!"
        "They're saying we should all hook-up together!"
        "Wow - this just keeps on getting better!"
    elif sasha.love > samantha.love and sasha.love >= 100:
        "Sam's still looking at me like she wants to kill me."
        "But I can see a change in Sasha's expression."
        show sasha normal
        show samantha annoyed
        sasha.say "You know what, I'm supposed to be in a fucking metal band."
        sasha.say "So maybe it's time I started to behave like it."
        sasha.say "And not like some prissy old woman!"
        sasha.say "I mean, who really cares you're fucking two girls at once?"
        show samantha angry
        samantha.say "Who cares?"
        samantha.say "I care, that's who!"
        show samantha at left with ease
        "Sam shakes her head and backs away from Sasha and me."
        show samantha sad
        samantha.say "You really cheated on me?"
        samantha.say "After all that shit that happened with Ryan?"
        samantha.say "After all that talk, you're just the same as him!"
        hide samantha with easeoutleft
        "I watch as Sam turns and walks away."
        "Part of me feels bad that it ended this way."
        "But another part of me is relieved that it's her leaving and not Sasha."
        "I guess I just found out which one of them I really love the most."
        $ samantha.set_gone_forever()
    elif samantha.love > sasha.love and samantha.love >= 100:
        "Sasha's still looking at me like she wants to kill me."
        "But I can see Sam's expression softening by the second."
        show samantha normal
        show sasha annoyed
        samantha.say "You know, I should dump your ass."
        samantha.say "You cheated on me, just like Ryan did!"
        samantha.say "But I know you better than that, [hero.name]."
        samantha.say "I know that if you say you love two girls, then you mean it!"
        show sasha angry
        sasha.say "Excuse me?"
        sasha.say "Do you have any self-respect whatsoever?!?"
        "Sasha shakes her head and backs away from Sam and me."
        sasha.say "I'm not sharing a man with anyone!"
        sasha.say "You two can stay the hell away from me."
        sasha.say "In fact, you won't be seeing me again!"
        hide sasha with easeoutright
        "I watch as Sasha turns and walks away."
        "Part of me feels bad that it ended this way."
        "But another part of me is relieved that it's her leaving and not Sam."
        "I guess I just found out which one of them I really love the most."
        $ sasha.set_gone_forever()
        $ Room.find("bedroom3").hide()
    else:
        "Sam and Sasha are still looking at me like they want to kill me."
        "But it's Sasha that speaks up first."
        show sasha angry
        sasha.say "I'm not sharing a man with anyone!"
        sasha.say "You two can stay the hell away from me."
        sasha.say "In fact, you won't be seeing me again!"
        hide sasha with easeoutright
        "I watch as Sasha turns and walks away."
        "Then I look at Sam, hoping she's going to say the opposite."
        show samantha sad
        samantha.say "You really cheated on me?"
        samantha.say "After all that shit that happened with Ryan?"
        samantha.say "After all that talk, you're just the same as him!"
        hide samantha with easeoutleft
        "I watch as Sam turns and walks away too."
        "Which leaves me standing alone."
        "I guess I'll never know which one of them I loved the most."
        "Because I've gone and blown it."
        "Big time and with both of them."
        $ samantha.set_gone_forever()
        $ sasha.set_gone_forever()
        $ Room.find("bedroom3").hide()
    return


label bree_minami_samantha_sasha_male_ending:
    $ game.room = "church"
    scene bg church wedding
    with fade
    "I feel like I should be able to reel off a long and exciting story about how I came to be standing here."
    "After all, who could possibly forget the sequence of events that lead to them marrying four girls at once?"
    "No, sorry, let me be more specific - marrying the four hottest girls that I've ever met in my entire life!"
    "But it's all a blur right now, what with this being the big day and all..."
    "I'm sure I'll be able to recall everything once it's over and the dust has settled."
    "I just have to accept that right now, my head's spinning with excitement and anticipation."
    "It's a cliche that women have always planned this day in their lives out with painful amounts of detail."
    "Whereas the average gut probably hasn't spared as much as a thought about how it'll play out."
    "But I think that in my case, I can rightfully say that speculation would have been a waste of time."
    "I mean, how could I have predicted that my wedding day would involve four people?"
    "Well, five, when you include me!"
    "I would have been happy to have landed either of the cute housemates that moved in with me."
    "But when I started a relationship with both [bree.name] and Sasha, I could hardly believe it."
    "Minami moving in too could have spelled disaster for all of that."
    "Especially when I found out she had designs on me too!"
    "And yet it wasn't long before she became a part of that same relationship as well."
    "I guess I was still reeling from that when Sam was added to the equation."
    "The one that I thought had got away for good."
    "The girl that I was resigned to waving goodbye to."
    "Suddenly she was back in the picture."
    "And even the fact that I was already seeing three other girls didn't seem to matter!"
    "Before I knew it, all four of them were in on it."
    "What's more, it wasn't just some crazy fling either."
    "Four proposals of marriage met with four answers of yes."
    "And that lead to this moment, right here and now."
    "I'm lost so deep in my own thoughts that I hardly notice the music begin to fill the chapel."
    show bree wedding normal zorder 2 at center, zoomAt (1.0, (280, 740))
    show sasha wedding normal zorder 1 at center, zoomAt (1.0, (520, 740))
    show minami wedding normal zorder 4 at center, zoomAt (1.0, (760, 740))
    show samantha wedding normal zorder 3 at center, zoomAt (1.0, (1000, 740))
    with dissolve
    "It's only when I see the four of them appear at the other end of the aisle that I snap out of it."
    "The aisle isn't wide enough for them to come down it side by side."
    "But it looks like nobody wanted to be the one to walk at the back."
    "Either that or all of them were too self-conscious to put themselves at the front."
    show bree at center, traveling (1.25, 4.0, (240, 900))
    show sasha at center, traveling (1.25, 4.0, (500, 900))
    show minami at center, traveling (1.25, 4.0, (780, 900))
    show samantha at center, traveling (1.25, 4.0, (1040, 900))
    "This means that they come down the aisle in a kind of knot, walking together."
    "Which I guess is pretty appropriate, as we're all marrying each other."
    "Once we exchange our vows, we're all going to be equals in this relationship."
    "All of them looks stunning in their dresses, the most beautiful brides imaginable."
    "But none of them look alike, and their personalities shine through."
    show bree happy
    "[bree.name] is all in pink, blonde hair bouncing as she walks towards me."
    "Her smile is even more beautiful than her dress."
    show sasha happy
    "Sasha, as always, is in black that contrasts with her pale skin."
    "She looks dark and brooding, yet also sensual and beguiling too."
    show minami happy
    "Then there's Minami, petite and practically bursting with life."
    "She wears a dress of silk that's covered in intricate patterns."
    "But it has a modern cut, one that suits her down to the ground."
    show samantha happy
    "And then there's Sam, the only one that I've ever seen in a wedding dress before now."
    "Yet she somehow looks so much better in this one than the last!"
    if bree.is_visibly_pregnant and minami.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of four large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not minami.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha, Minami and Sam as they stand beside me at the altar."
        "My four brides - soon to be my four wives!"
    else:
        if bree.is_visibly_pregnant:
            "Whoever made [bree.name]'s dress managed to pull off a miracle."
            "With the bouquet in her hands, her already massive bump is almost invisible!"
            "Not that I want to forget about the fact that she's carrying my child."
        if sasha.is_visibly_pregnant:
            "As she gets closer, I can see that it's not just the make-up that's making Sasha look white."
            "She's already pretty far on with her pregnancy, and it's taking its tole on her."
            "But she smiles and nods, letting me know that she's doing okay."
        if minami.is_visibly_pregnant:
            "Minami's dress makes no effort to hide the fact that she's heavily pregnant."
            "But then she's a thoroughly modern girl, and sees no shame in the fact."
            "Instead she wears it with pride, and I feel the same feeling swell inside of me too."
        if samantha.is_visibly_pregnant:
            "Though I've seen Sam in a wedding dress before, there's one big difference this time around."
            "Last time she didn't have a belly that was already swelling with my kid inside of it!"
            "I guess that just goes to show how different things are this time!"
    "There's barely enough time for the five of us to exchange glances and nervous smiles."
    "And that's because the priest leaps into the ceremony almost as soon as the music come to an end."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these FIVE people in the bonds of holy matrimony!"
    show bree wedding normal
    show sasha wedding normal
    show minami wedding normal
    show samantha wedding normal
    "The priest's tone is a little exasperated, but more amused than anything."
    "And there's an appreciative ripple of laughter from the assembled guests too."
    "Even the five of us share a round of giggles and laughter, some cheeks flushing too."
    "Sure, this is all legal now, but it's still pretty new for all concerned."
    "I guess this is just part of the journey to it becoming part of the new normal."
    "The priest dives into the task ahead, doing the best he can to keep up."
    "Before too long, we're already at the point where we're making our vows!"
    "Priest" "Do you, [bree.name], take Sasha, Sam, Minami and [hero.name], to be your lawful, wedded partners?"
    show bree happy at startle
    bree.say "Oh, I do!"
    "Priest" "Do you, Sasha, take [bree.name], Sam, Minami and [hero.name], to be your lawful, wedded partners?"
    show sasha happy at startle
    sasha.say "Yeah, I do."
    "Priest" "Do you, Sam, take [bree.name], Sasha, Minami and [hero.name], to be your lawful, wedded partners?"
    show samantha happy at startle
    samantha.say "I do."
    "Priest" "Do you, Minami, take [bree.name], Sasha, Sam and [hero.name], to be your lawful, wedded partners?"
    show minami happy at startle
    minami.say "I sure do!"
    "The priest makes a dramatic pause, filling his lungs for the final push."
    "Priest" "And do you, [hero.name], take [bree.name], Sasha, Sam and Minami, to be your lawful, wedded partners?"
    "Now it's my turn to take an equally deep breath before answering."
    mike.say "I do."
    "The priest nods, clearly happy to be reaching the end of the ceremony."
    "Priest" "If anyone present knows of any lawful reason these five may not be joined in holy matrimony..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "There's the usual pause and nervous laughter as he surveys the crowd."
    "But nobody leaps to their feet to call a halt to the proceedings."
    "Priest" "The I hereby pronounce you husband and wives."
    "Priest" "You may kiss the brides."
    "Priest" "Or each other..."
    "Priest" "I'm not sure how this bit is supposed to work!"
    show bree at center, traveling (1.5, 1.0, (240, 1040))
    show sasha at center, traveling (1.5, 1.0, (500, 1040))
    show minami at center, traveling (1.5, 1.0, (780, 1040))
    show samantha at center, traveling (1.5, 1.0, (1040, 1040))
    "Neither are we, and so we come together in a kind of group hug."
    "We exchange kisses with each other, each one as passionate as the last."
    "And we did it - the five of us actually managed to tie the knot!"
    "We're not doing this behind closed doors anymore - we're a fivesome in the eyes of the law!"

    scene home ending
    show home ending sasha
    with fade
    sasha.say "Well, I guess I should be the one to kick things off here."
    show home ending bree with dissolve
    bree.say "Wait, wait, wait!"
    bree.say "Why's that?!?"
    sasha.say "Erm, I think I was the first one to move into the house."
    sasha.say "That means I was the first one to meet [hero.name]!"
    bree.say "What?"
    bree.say "You maybe moved in a couple of days before me - that's all!"
    show home ending samantha with dissolve
    samantha.say "Hello - am I hearing this right?"
    samantha.say "I was living with [hero.name] before either of you two."
    samantha.say "It was only me moving out that meant you could move in!"
    show home ending minami with dissolve
    minami.say "Okay guys, I'm gonna play my little sis card."
    minami.say "Which means I've known big bro WAY longer than any of you!"
    samantha.say "Alright, alright."
    samantha.say "This is just getting stupid."
    samantha.say "We're supposed to be married, for god's sake."
    samantha.say "We shouldn't be squabbling like schoolgirls over their latest crush!"
    bree.say "You're right, Sam."
    minami.say "Yeah...sorry."
    sasha.say "We shouldn't be arguing, should we?"
    samantha.say "No, we shouldn't."
    samantha.say "This is our chance to speak for ourselves."
    samantha.say "A chance to tell everyone what life's like from our perspective."
    minami.say "Well, we do kinda fight a lot!"
    bree.say "Speak for yourself, shorty!"
    minami.say "Who are you calling short, blondie?!?"
    sasha.say "Ah, yeah..."
    sasha.say "Thanks for the demonstration, guys!"
    samantha.say "Of course we fight sometimes."
    samantha.say "That's just part of being in a relationship."
    samantha.say "But it's the making up that's the fun part."
    sasha.say "Yeah, you got me there, Sam."
    sasha.say "It is a lot more fun with four other people to make it up to!"
    bree.say "Oh yeah!"
    minami.say "Totally!"
    samantha.say "Only four people?"
    if bree.is_visibly_pregnant and minami.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        bree.say "Are we still technically a fivesome?"
        sasha.say "Yeah, we might have accidentally become a tribe somewhere along the way!"
        sasha.say "[hero.name] could be the founder of a whole new nation."
        minami.say "Aww - that's sweet."
        minami.say "But please don't tell big bro that."
        samantha.say "I agree - his head's big enough as it is!"
    elif not bree.is_visibly_pregnant and not minami.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "Yeah, always room for more!"
        minami.say "Huh...is someone else moving in?"
        sasha.say "She means the patter of tiny feet, Minami!"
        samantha.say "You know - babies?"
        minami.say "Oh..."
    else:
        if bree.is_visibly_pregnant:
            bree.say "Yeah, yeah...I know."
            bree.say "Poppy's got so much energy, it's hard to keep up!"
        if minami.is_visibly_pregnant:
            minami.say "I don't think I could handle Mei without you guys."
            minami.say "And she loves her four mommies!"
        if sasha.is_visibly_pregnant:
            sasha.say "I think [hero.name] likes not being the only guy around here."
            sasha.say "That's why he spoils Dahlia every chance he gets!"
        if samantha.is_visibly_pregnant:
            samantha.say "Don't forget about little Jemima!"
            samantha.say "She might be small, but she feels like she makes up for it!"
    samantha.say "But mainly, it's all sunshine and rainbows - right guys?"
    bree.say "Oh yeah, I'm really having fun with married life."
    sasha.say "It's a rollercoaster at times."
    sasha.say "But then I like rollercoasters - so what's not to like?"
    minami.say "It's great."
    minami.say "I have big bro, just like I always wanted."
    minami.say "And I have all of you guys too!"
    minami.say "But I could do without one thing..."
    bree.say "Huh?"
    sasha.say "What's that?"
    samantha.say "It's okay, Minami - you can tell us."
    minami.say "I could do without big bro's smelly socks!"
    bree.say "Oh, yeah - they do stink."
    sasha.say "He can be such a slob sometimes!"
    samantha.say "Don't worry guys, we have the rest of his life to straighten him out."
    samantha.say "And the best thing is, we outnumber him four to one!"
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label bree_samantha_sasha_male_ending:
    $ game.room = "church"
    scene bg church wedding
    with fade
    "I feel like I should be able to reel off a long and exciting story about how I came to be standing here."
    "After all, who could possibly forget the sequence of events that lead to them marrying three girls at once?"
    "No, sorry, let me be more specific - marrying the three hottest girls that I've ever met in my entire life!"
    "But it's all a blur right now, what with this being the big day and all..."
    "I'm sure I'll be able to recall everything once it's over and the dust has settled."
    "I just have to accept that right now, my head's spinning with excitement and anticipation."
    "It's a cliche that women have always planned this day in their lives out with painful amounts of detail."
    "Whereas the average gut probably hasn't spared as much as a thought about how it'll play out."
    "But I think that in my case, I can rightfully say that speculation would have been a waste of time."
    "I mean, how could I have predicted that my wedding day would involve three people?"
    "Well, four, when you include me!"
    "I would have been happy to have landed either of the cute housemates that moved in with me."
    "But when I started a relationship with both [bree.name] and Sasha, I could hardly believe it."
    "I guess I was still reeling from that when Sam was added to the equation."
    "The one that I thought had got away for good."
    "The girl that I was resigned to waving goodbye to."
    "Suddenly she was back in the picture."
    "Before I knew it, all three of them were in on it."
    "What's more, it wasn't just some crazy fling either."
    "Three proposals of marriage met with three answers of yes."
    "And that lead to this moment, right here and now."
    "I glance back over my shoulder at the chapel filled with all of our guests."
    "They're an interesting bunch of people to be sure, from all walks of life."
    "But it reassures me to see that the place is pretty much full."
    "That and the fact that all I see are smiling faces too."
    "It's at that moment the music starts to play, filling the chapel."
    "And on cue, all of the guests get to their feet as one."
    "I'm still looking back as the bridal procession appears in the aisle..."
    show bree wedding happy zorder 2 at center, zoomAt (1.0, (640, 730)) with dissolve
    "[bree.name] is all in pink, blonde hair bouncing as she walks towards me."
    "Her smile is even more beautiful than her dress."
    show bree wedding at center, zoomAt (1.0, (340, 730)) with ease
    show sasha wedding happy zorder 3 at center, zoomAt (1.0, (640, 730)) with dissolve
    "Sasha, as always, is in black that contrasts with her pale skin."
    "She looks dark and brooding, yet also sensual and beguiling too."
    show sasha wedding normal at center, zoomAt (1.0, (940, 730)) with ease
    show samantha wedding happy zorder 1 at center, zoomAt (1.0, (640, 730)) with dissolve
    "And then there's Sam, the only one that I've ever seen in a wedding dress before now."
    "Yet she somehow looks so much better in this one than the last!"
    show samantha normal
    if bree.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of three large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha, and Sam as they stand beside me at the altar."
        "My three brides - soon to be my three wives!"
    else:
        if bree.is_visibly_pregnant:
            "Whoever made [bree.name]'s dress managed to pull off a miracle."
            "With the bouquet in her hands, her already massive bump is almost invisible!"
            "Not that I want to forget about the fact that she's carrying my child."
        if sasha.is_visibly_pregnant:
            "As she gets closer, I can see that it's not just the make-up that's making Sasha look white."
            "She's already pretty far on with her pregnancy, and it's taking its tole on her."
            "But she smiles and nods, letting me know that she's doing okay."
        if samantha.is_visibly_pregnant:
            "Though I've seen Sam in a wedding dress before, there's one big difference this time around."
            "Last time she didn't have a belly that was already swelling with my kid inside of it!"
            "I guess that just goes to show how different things are this time!"
    "There's barely enough time for the four of us to exchange glances and nervous smiles."
    "And that's because the priest leaps into the ceremony almost as soon as the music come to an end."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these FOUR people in the bonds of holy matrimony!"
    "The priest's tone is a little exasperated, but more amused than anything."
    "And there's an appreciative ripple of laughter from the assembled guests too."
    "Even the four of us share a round of giggles and laughter, some cheeks flushing too."
    "Sure, this is all legal now, but it's still pretty new for all concerned."
    "I guess this is just part of the journey to it becoming part of the new normal."
    "The priest dives into the task ahead, doing the best he can to keep up."
    "Before too long, we're already at the point where we're making our vows!"
    "Priest" "Do you, [bree.name], take Sasha, Sam and [hero.name], to be your lawful, wedded partners?"
    show bree happy at startle
    bree.say "Oh, I do!"
    "Priest" "Do you, Sasha, take [bree.name], Sam and [hero.name], to be your lawful, wedded partners?"
    show sasha happy at startle
    sasha.say "Yeah, I do."
    "Priest" "Do you, Sam, take [bree.name], Sasha and [hero.name], to be your lawful, wedded partners?"
    show samantha happy at startle
    samantha.say "I do."
    "The priest makes a dramatic pause, filling his lungs for the final push."
    "Priest" "And do you, [hero.name], take [bree.name], Sasha and Sam, to be your lawful, wedded partners?"
    "Now it's my turn to take an equally deep breath before answering."
    mike.say "I do."
    "The priest nods, clearly happy to be reaching the end of the ceremony."
    "Priest" "If anyone present knows of any lawful reason these four may not be joined in holy matrimony..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "There's the usual pause and nervous laughter as he surveys the crowd."
    "But nobody leaps to their feet to call a halt to the proceedings."
    "Priest" "The I hereby pronounce you husband and wives."
    "Priest" "You may kiss the brides."
    "Priest" "Or each other..."
    "Priest" "I'm not sure how this bit is supposed to work!"
    show sasha at center, traveling (1.5, 1.0, (920, 1040))
    show bree at center, traveling (1.5, 1.0, (360, 1040))
    show samantha at center, traveling (1.5, 1.0, (640, 1040))
    "Neither are we, and so we come together in a kind of group hug."
    "We exchange kisses with each other, each one as passionate as the last."
    "And we did it - the four of us actually managed to tie the knot!"
    "We're not doing this behind closed doors anymore - we're a foursome in the eyes of the law!"

    scene home ending
    show home ending sasha
    with fade
    sasha.say "Well, I guess I should be the one to kick things off here."
    show home ending bree with dissolve
    bree.say "Wait, wait, wait!"
    bree.say "Why's that?!?"
    sasha.say "Erm, I think I was the first one to move into the house."
    sasha.say "That means I was the first one to meet [hero.name]!"
    bree.say "What?"
    bree.say "You maybe moved in a couple of days before me - that's all!"
    show home ending samantha with dissolve
    samantha.say "Hello - am I hearing this right?"
    samantha.say "I was living with [hero.name] before either of you two."
    samantha.say "It was only me moving out that meant you could move in!"
    samantha.say "However."
    samantha.say "This is just getting stupid."
    samantha.say "We're supposed to be married, for god's sake."
    samantha.say "We shouldn't be squabbling like schoolgirls over their latest crush!"
    bree.say "You're right, Sam."
    sasha.say "We shouldn't be arguing, should we?"
    samantha.say "No, we shouldn't."
    samantha.say "This is our chance to speak for ourselves."
    samantha.say "A chance to tell everyone what life's like from our perspective."
    samantha.say "Of course we fight sometimes."
    samantha.say "That's just part of being in a relationship."
    samantha.say "But it's the making up that's the fun part."
    sasha.say "Yeah, you got me there, Sam."
    sasha.say "It is a lot more fun with two other people to make it up to!"
    bree.say "Oh yeah!"
    samantha.say "Only two people?"
    if bree.is_visibly_pregnant:
        bree.say "Yeah, yeah...I know."
        bree.say "Poppy's got so much energy, it's hard to keep up!"
    if sasha.is_visibly_pregnant:
        sasha.say "I think [hero.name] likes not being the only guy around here."
        sasha.say "That's why he spoils Dahlia every chance he gets!"
    if samantha.is_visibly_pregnant:
        samantha.say "Don't forget about little Jemima!"
        samantha.say "She might be small, but she feels like she makes up for it!"
    samantha.say "But mainly, it's all sunshine and rainbows - right guys?"
    bree.say "Oh yeah, I'm really having fun with married life."
    sasha.say "It's a rollercoaster at times."
    sasha.say "Especially when it comes to [hero.name]'s stinky shoes."
    bree.say "...those REALLY do stink!"
    samantha.say "Don't worry guys, we have the rest of his life to straighten him out."
    samantha.say "And the best thing is, we outnumber him three to one!"
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label tv_bj_bree_samantha_sasha:
    scene bg house with fade
    "It's the end of what's been a pretty long and trying day."
    "But now it's over and nobody has a claim on my time until tomorrow."
    "So I can finally kick back and do whatever I want to unwind."
    scene bg livingroom with fade
    "Which right now is just sitting in front of the TV and turning off my brain!"
    "Seriously, I'm not even that bothered about what I actually end up watching."
    "I just flick through this and that until I find something that looks good."
    "And then I press play, intending to binge on it until I fall asleep."
    samantha.say "There you are, [hero.name]!"
    "I look up to see Sam standing in the doorway."
    show samantha normal with fade
    mike.say "Oh..."
    mike.say "Hi, Sam..."
    mike.say "I was just..."
    scene bg black
    show watch tv samantha
    with fade
    "Before I can finish, Sam walks into the sitting-room."
    "And then she proceeds to sit herself down on the sofa beside me."
    "I open my mouth to protest, meaning to tell her that I want to be left alone."
    "But then she leans herself against me, laying her head on my shoulder!"
    samantha.say "So..."
    samantha.say "What are we watching?"
    mike.say "Erm..."
    mike.say "I don't know, Sam."
    mike.say "I was just chilling out, you know?"
    "Sam nods, nestling herself even closer to me than before."
    samantha.say "Mmm..."
    samantha.say "That sounds nice."
    samantha.say "Just you and me, chilling together on the sofa."
    samantha.say "Doesn't it?"
    mike.say "Y...yeah, Sam..."
    mike.say "That sounds great!"
    "Something so simple might sound crazy to anyone else."
    "But to me it's like a dream come true."
    "I can't count the number of times I walked past that same door."
    "And glanced in here to see Sam curled up like this with Ryan."
    "It always made me feel so jealous of what they had."
    "I'd have given anything for the chance to sit with Sam like that."
    "And now here I am, getting exactly what I always wanted!"
    "So I don't hesitate to put an arm around Sam, pulling her closer still."
    scene bg livingroom
    show bree normal
    with fade
    bree.say "Hey, [hero.name]!"
    bree.say "Mind if I join you?"
    "What the hell?"
    "I was just settling down with Sam."
    "And now [bree.name]'s at the door too!"
    "But like Sam before her, she doesn't wait even for a second."
    scene bg black
    show watch tv bree samantha
    with fade
    "[bree.name] just breezes into the room and sits down on the sofa beside me."
    "Of course she chooses to sit on the opposite side to Sam."
    "Which is why she didn't see the other girl when she came in just now."
    "And she only discovers that we're not alone when she leans in close to me."
    bree.say "Aargh!"
    bree.say "Oh...it's only you, Sam!"
    bree.say "But wait a minute - what are you doing there?"
    samantha.say "Funny thing, [bree.name]..."
    samantha.say "I was about to ask you the same thing!"
    "I choose this moment to cut into the conversation."
    "Because I think I can sense where this is going."
    "And it's flattering to think that two hot girls want to curl up on the sofa with me."
    "But the idea of them fighting each other for the spot is less than appealing."
    mike.say "I was just watching TV, [bree.name]."
    mike.say "Then Sam came along and joined me."
    mike.say "But there's plenty of room for you too."
    mike.say "Isn't there, Sam?"
    "Sam looks less than pleased with the idea of [bree.name] joining us."
    "But then it seems to dawn on her that she can't just kick a fellow housemate out of the sitting-room."
    "Because how would she go about explaining her reasons for doing something like that?"
    "Other than admitting that she wanted to get up close and personal with me!"
    samantha.say "I suppose so."
    samantha.say "So long as you stay on your side of the sofa."
    "[bree.name] and Sam both retreat to their own ends of the sofa."
    "But I'm quietly thrilled when they come creeping back a moment later."
    "I honestly think each of them is sure the other won't be doing the exact same thing."
    "So as long as I keep still, I can enjoy being snuggled up to the pair of them!"
    scene bg livingroom
    show sasha normal
    with fade
    sasha.say "I hear you in there, [hero.name]!"
    sasha.say "You think you're getting away with it, huh?"
    sasha.say "Watching crap on the TV without me?"
    "Unlike [bree.name] and Sam, Sasha doesn't even bother to stand in the doorway."
    "She just comes rushing straight into the sitting-room."
    "And it looks like she was planning to jump straight onto me too!"
    "So it's a shame when she sees the other two girls, one to either side of me."
    scene bg black
    show watch tv bree samantha sasha
    with fade
    sasha.say "What the fuck?"
    bree.say "What the fuck do you mean 'what the fuck'?"
    samantha.say "What the fuck do the both of you mean 'what the fuck'?"
    mike.say "Erm..."
    mike.say "I don't see what the problem is here, guys."
    mike.say "Can't we all just sit down and watch TV together?"
    mike.say "I mean, we are housemates, aren't we?"
    "All three of the girls shoot dirty looks at each other."
    "But there's no real way they can object to the presence of the others."
    "Not without admitting that they want me all to themselves."
    bree.say "Okay, Sasha, okay..."
    bree.say "But this sofa's already full!"
    samantha.say "[bree.name]'s right, Sasha..."
    samantha.say "You have to sit on the other sofa, over there!"
    "Sasha bristles for a moment, and it looks like she's going to object."
    "But then she puts on a smile."
    "The sly kind of smile that I know means she's just figured something out."
    sasha.say "Nah..."
    sasha.say "No need for that..."
    sasha.say "I'll just sit right here, on the floor!"
    "With that, Sasha plants her ass on the floor, right in front of me."
    "She gets between my knees, and leans back against the sofa and me."
    "I can sense [bree.name] and Sam staring daggers at her."
    "But she just stares straight ahead in silence."
    "Though I can be pretty sure that she's smiling right now."
    "For a couple of minutes I think that's the end of it for the evening."
    "With one of the girls in the room, I'd have been happy to fool around a little."
    "Even with two of them present, I could have stood an occasional touch or stroke."
    "But now three of them are here."
    "So doing anything would be tantamount to asking to be rumbled in the act."
    "Which is why I'm so surprised a moment later to feel myself being touched."
    "And not by one hand, but by three!"
    "It seems the girls aren't as cautious as I am."
    "Sam's hand feels like it's slipped under one of my arms."
    "And it's now making slow progress towards my waist."
    "[bree.name]'s is going in the opposite direction."
    "I can feel it on my thigh, climbing upwards."
    "Not to be left out, Sasha's is creeping up the other leg."
    "Making good progress towards my knee."
    "All of which leaves me in an even more awkward situation than before."
    "Sure, I'm enjoying the sensation of being felt up three different ways at once."
    "But what happens when they all meet in the middle?"
    "Especially when the middle just so happens to be my groin!"
    "If I call them out, it's probably going to mean everything kicking off."
    "A three-way argument, with me stuck in the centre of the action!"
    "Suddenly I hear a whisper in my ear."
    samantha.say "Oh, [hero.name]..."
    samantha.say "Since when did you have such soft, feminine hands?"
    bree.say "That's really weird..."
    bree.say "I was just about to ask the same thing!"
    sasha.say "What are you guys talking about?"
    sasha.say "I was gonna ask him first!"
    "I glance down with a growing sense of dread."
    "And I see [bree.name], Sam and Sasha's hands on my groin."
    "All of them caressing the others on top of it."
    "That is until the three of them realise what's going on."
    "And when they do, they all retreat, slapping at each other at the same time."
    scene bg livingroom
    show bree angry
    with fade
    bree.say "What are you two, sex-crazed or something?"
    show samantha angry at left with dissolve
    samantha.say "You're a fine one to talk, you hormonal harlot!"
    show sasha angry at right with dissolve
    sasha.say "At least I'm not drooling over the guy like a bitch in heat!"
    mike.say "Erm..."
    mike.say "Please don't take this the wrong way, guys..."
    mike.say "But I was really trying to just watch some TV and relax here!"
    mike.say "I'm flattered and all that - but can't we all just get along?"
    show bree annoyed
    show samantha annoyed
    show sasha annoyed
    "One by one the girls expressions change from anger to embarrassment."
    "And they exchange guilty glances as the reality of the situation sinks in."
    bree.say "He's right."
    show bree normal
    bree.say "We should be able to get along."
    samantha.say "Of course we should."
    show samantha normal
    samantha.say "We're all adults, aren't we?"
    sasha.say "More than that - we should be able to work together."
    show sasha normal
    sasha.say "To make our home a more harmonious place!"
    "I watch as they begin exchanging nods and knowing glances."
    "And I wonder if I'm ever going to be able to figure that out."
    "You know, the weird way women seem to be able to read each other's minds?"
    "Because a few seconds later, the three of them leap into action."
    "[bree.name] and Sam get up off the sofa, and Sasha kneels on the floor."
    "And without saying a word, they begin to take off their clothes!"
    show bree naked
    show samantha naked
    show sasha naked
    with dissolve
    "I can only sit and watch them doing this, helpless to say or do a thing."
    "Part of that is because I'm stunned to be seeing it happening."
    "And part of it is that I wasn't lying when I said that I was dog-tired."
    "The combination of the two is enough to render me helpless."
    "It still keeps me from moving as the now naked girls turn their attention to me."
    scene bj breesamsasha with fade
    "And it doesn't disappear as they take off my clothes either."
    "I just lie back and watch as the three of them strip me naked on the sofa."
    "Then they kneel down in front of me, [bree.name] to my left, Sasha to my right and Sam in the middle."
    "I'm not going to lie, they don't need to do anything to encourage me."
    "My cock is already rising into the air at the mere sight of them!"
    "My heart is beating hard too, blood pumping ever faster around my body."
    "They hold back from touching me, like they're aware it's not needed."
    "And only when I know that it can't get any bigger do they begin to move."
    "As one they lean in as close as possible."
    "Their mouths open, lips parting and tongues poking out."
    "But the moment the tips of those tongues touch me..."
    "I feel a shudder of excitement run the entire length of my body."
    "Yet it doesn't make me want to move."
    "Instead it keeps me rooted to the spot, immobile and helpless."
    "All I can do is watch as lips, tongues and teeth go to work on me."
    "At first I can keep track of who's doing what and when."
    "Sam kisses the head, while [bree.name] works the shaft and Sasha plays with my balls."
    "But all too soon the pleasure I'm feeling seems to blur my senses."
    "It's like I blink and the girls have all changed places."
    show bj breesamsasha breesuck
    "Now [bree.name]'s got the head of my cock buried deep in her mouth."
    "Sasha's using her tongue to caress the shaft."
    "And I can feel what must be Sam's lips on my balls."
    show bj breesamsasha samanthasuck
    "My head's almost reeling from what they're doing."
    "Because none of them seem to be getting in the way of the others."
    show bj breesamsasha sashasuck
    "Even when they change places, the pleasure isn't interrupted for a moment."
    "Instead they pick up where the last one left off."
    show bj breesamsasha breesuck
    "So I'm constantly being worked in three ways at once."
    "And the glances they shoot me are making it more intense too."
    show bj breesamsasha sashasuck
    "Every time one of their knowing eyes meets mine, I think that's going to do it."
    "The knowledge of what's happening and what they're doing to me is right there."
    show bj breesamsasha samanthasuck
    "And I can tell instantly that the three of them are as into it as I am."
    "The only sounds that can be heard aside from their efforts reinforce that."
    show bj breesamsasha sashasuck
    "Because the room is filled with my own panting."
    "And alongside that can be heard sighs and moans too."
    show bj breesamsasha samanthasuck
    "Whenever their mouths aren't on my cock, they're almost overcome."
    "With any one of these girls I'd be sure to lose it sooner or later."
    show bj breesamsasha breesuck
    "With two of them it'd be a sure thing I couldn't go too long."
    "But with all three of them, I'm amazed I've lasted even this long."
    show bj breesamsasha sashasuck
    "My hands are grasping handfuls of the sofa cushions."
    "My teeth are gritted, jaw clenched shut."
    "All because I'm trying to hang on just a little longer."
    show bj breesamsasha -sashasuck
    "Luckily for me, it seems that [bree.name], Sam and Sasha notice this."
    "And they change what they're doing in order to be prepared."
    "So when the inevitable begins to happen, they kneel before me."
    "All three of them waiting patiently to see what I do next."
    menu:
        "Cum in [bree.name]'s mouth":
            "I don't know what makes up my mind in the end."
            "I just feel an irresistible pull towards [bree.name]."
            "So in the last few seconds, I pull her head forwards."
            "She looks surprised, her mouth opening to form a question."
            show bj breesamsasha breesuck
            "But all that means is that my cock slides straight in there."
            "[bree.name] closes her eyes as I begin to lose it."
            "And she seems to be back in control as I shoot my load."
            show bj breesamsasha inmouth with vpunch
            "Because she handles what follows like a pro, swallowing without a hitch."
            "Sam and Sasha watch on as all of this happens."
            "And I'm sure I can see disappointment and jealousy in their eyes."
            "That wasn't my intention, but I'm grateful that they choose to hide it."
        "Cum in Samantha's mouth":
            "I don't know what makes up my mind in the end."
            "I just feel an irresistible pull towards Sam."
            "So in the last few seconds, I pull her head forwards."
            "She looks surprised, her mouth opening to form a question."
            show bj breesamsasha samanthasuck
            "But all that means is that my cock slides straight in there."
            "Sam closes her eyes as I begin to lose it."
            "And she seems to be back in control as I shoot my load."
            show bj breesamsasha inmouth with vpunch
            "Because she handles what follows like a pro, swallowing without a hitch."
            "[bree.name] and Sasha watch on as all of this happens."
            "And I'm sure I can see disappointment and jealousy in their eyes."
            "That wasn't my intention, but I'm grateful that they choose to hide it."
        "Cum in Sasha's mouth":
            "I don't know what makes up my mind in the end."
            "I just feel an irresistible pull towards Sasha."
            "So in the last few seconds, I pull her head forwards."
            "She looks surprised, her mouth opening to form a question."
            show bj breesamsasha sashasuck
            "But all that means is that my cock slides straight in there."
            "Sasha closes her eyes as I begin to lose it."
            "And she seems to be back in control as I shoot my load."
            show bj breesamsasha inmouth with vpunch
            "Because she handles what follows like a pro, swallowing without a hitch."
            "[bree.name] and Sam watch on as all of this happens."
            "And I'm sure I can see disappointment and jealousy in their eyes."
            "That wasn't my intention, but I'm grateful that they choose to hide it."
        "Just cum":
            "How in the hell am I supposed to choose between the three of them?"
            "They managed to get me this far by working together as a team."
            "So it only seems right that I include them all in what happens at the end too."
            scene cumshot breesamsasha
            "With that in mind, I stay right where I am, keeping my cock still."
            show cumshot breesamsasha cumshot with vpunch
            "Only when I feel myself starting to shoot my load do I make a move."
            with vpunch
            "And that's to angle it so that each of them is hit by the spurts that follow."
            show cumshot breesamsasha -cumshot onface with vpunch
            "[bree.name], Sam and Sasha squeal and squeeze their eyes shut as it happens."
            "But as my cock goes from left to right and back again, they're all hit."
            "Lines of warm, sticky white cum paint their faces."
            "And streamers even linger for a while, linking one to the next."
            "None of them can resist opening their mouths and licking their lips either."
            "But for me, the best thing is seeing them all smiling as it happens."
            "Because it lets me know that I've given them pleasure in return for pleasuring me."
    $ bree.sexperience += 1
    $ samantha.sexperience += 1
    $ sasha.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
