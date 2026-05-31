
init python:
    Event(**{
    "name": "minami_request",
    "priority": 500,
    "label": "minami_request",
    "conditions": [
        IsDone("minami_snooping"),
        IsHour(8, 22),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("tempminamiharem", False),
            ),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            MaxFlag("haremdenied", 2),
            MinStat("love", 150),
            MinStat("lesbian", 5),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "bree_sasha_request",
    "display_name": "Ask [bree.name] & Sasha about Minami",
    "label": "bree_sasha_request",
    "icon": "button_minami",
    "duration": 0,
    "conditions": [
        IsDone("minami_request"),
        IsNotDone("bree_request", "sasha_request"),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("minamirefusedinhomeharem", False),
            IsFlag("breerefusedminami", False),
            IsFlag("breeacceptminami", False),
            IsFlag("shasharefusedminami", False),
            IsFlag("sashaacceptminami", False),
            ),
        PersonTarget(minami,
            Not(IsHidden())
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        Or(
            PersonTarget(bree,
                IsActive(),
                ),
            PersonTarget(sasha,
                IsActive(),
                ),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "bree_request",
    "display_name": "About Minami",
    "label": "bree_request",
    "icon": "button_minami",
    "duration": 0,
    "conditions": [
        IsDone("minami_request"),
        IsNotDone("bree_sasha_request"),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("minamirefusedinhomeharem", False),
            IsFlag("breeacceptminami", False),
            ),
        PersonTarget(minami,
            Not(IsHidden())
            ),
        PersonTarget(bree,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_convince_sasha",
    "priority": 500,
    "label": "bree_convince_sasha",
    "conditions": [
        IsDone("bree_request", "sasha_request"),
        IsNotDone("bree_sasha_request"),
        IsHour(8, 22),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("sasharefusedminami"),
            IsFlag("breerefusedminami", False),
            IsFlag("minamirefusedinhomeharem", False),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "sasha_request",
    "display_name": "About Minami",
    "label": "sasha_request",
    "icon": "button_minami",
    "duration": 0,
    "conditions": [
        IsDone("minami_request"),
        IsNotDone("bree_sasha_request"),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("minamirefusedinhomeharem", False),
            IsFlag("sashaacceptminami", False),
            ),
        PersonTarget(minami,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sasha_convince_bree",
    "priority": 500,
    "label": "sasha_convince_bree",
    "conditions": [
        IsDone("bree_request", "sasha_request"),
        IsNotDone("bree_sasha_request"),
        IsHour(8, 22),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("breerefusedminami"),
            IsFlag("sasharefusedminami", False),
            IsFlag("minamirefusedinhomeharem", False),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "samantha_request",
    "display_name": "About Minami",
    "label": "samantha_request",
    "icon": "button_minami",
    "duration": 0,
    "conditions": [
        IsDone("minami_request"),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            IsFlag("ongoinghomeharem", "minami"),
            IsFlag("minamirefusedinhomeharem", False),
            ),
        PersonTarget(minami,
            Not(IsHidden())
            ),
        PersonTarget(samantha,
            IsActive(),
            InHarem('home'),
            ),
        ],
    "do_once": True,
    })

    WakeUpEvent(**{
    "name": "bj_bree_sasha_minami",
    "label": "bj_bree_sasha_minami_intro",
    "priority": 500,
    "conditions": [
        TogetherInHarem('home', 'bree', 'sasha', 'minami'),
        IsHour(7),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom1")),
        PersonTarget(minami,
            MinStat("love", 150),
            MinStat("lesbian", 5),
            MinStat("sexperience", 1),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            MinStat("love", 150)
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 150)
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "threesome_bree_minami",
    "label": "bree_minami_threesome_intro",
    "priority": 500,
    "conditions": [
        TogetherInHarem('home', 'bree', 'minami'),
        IsHour(20, 23),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 150),
            ),
        PersonTarget(minami,
            IsActive(),
            HasRoomTag("home"),
            MinStat("love", 150),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "threesome_sasha_minami",
    "label": "minami_sasha_threesome_intro",
    "priority": 500,
    "conditions": [
        TogetherInHarem('home', 'sasha', 'minami'),
        IsHour(20, 23),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 150),
            ),
        PersonTarget(minami,
            IsActive(),
            HasRoomTag("home"),
            MinStat("love", 150),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "foursome_bree_minami_sasha",
    "label": "foursome_bree_minami_sasha_intro",
    "priority": 500,
    "conditions": [
        TogetherInHarem('home', 'bree', 'sasha', 'minami'),
        IsHour(20, 23),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 150),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            MinStat("love", 150),
            ),
        PersonTarget(minami,
            IsActive(),
            HasRoomTag("home"),
            MinStat("love", 150),
            MinStat("lesbian", 5),
            MinStat("sexperience", 1),
            ),
        Or(
            HeroTarget(IsFlag("sashastrapon")),
            PersonTarget(sasha,
                IsFlag("strapon_known")
                ),
            ),
        ],
    "do_once": True,
    })

label minami_request:
    "It's only been a short while since I admitted the truth to Minami, telling her that [bree.name], Sasha and I are a threesome."
    "But I can already sense that she's building up to something, just based on the way she's behaving right now."
    "For one thing, Minami's going to great lengths to avoid me around the house."
    "And when she does happen to see me, she keeps her mouth shut and just hurries away without any excuse."
    "Believe me, that's out of character - my kid sister normally bugs me constantly."
    "That and she can't keep her mouth shut for more than a couple of seconds at a time either!"
    "Normally I'd just assume that she has something on her mind, or that she's sulking."
    "But it's a pretty complicated situation, even without the revelation of the threesome."
    "I mean, we finally bit the bullet and slept together not that long ago."
    "So we're still kind of working out how our relationship works, now that we're much more than adopted siblings."
    "More than once I think about confronting her about it, opening my mouth to speak when I see her."
    "But I always let the words die in my mouth or she slips away before I can ask her to stop and listen to me."
    "In the end, I resolve myself to waiting for Minami to talk to me."
    "And even so, when she finally does, it still catches me a little off-guard."
    show minami normal with dissolve
    minami.say "Erm...hey, big bro."
    mike.say "Hey, Minami..."
    mike.say "This...is...kinda awkward!"
    show minami annoyed
    "Minami nods and lets out a weary sigh."
    minami.say "Ah, yeah - isn't it just?"
    minami.say "I wanted to talk to you, but I..."
    mike.say "It's okay, Minami - I understand."
    mike.say "Maybe I should have told you about [bree.name], Sasha and me before we..."
    mike.say "Well, before we got so close, if you know what I mean?"
    show minami normal
    "Minami gives me a demure little smile at this, batting her eyelids as she looks up at me."
    "She has that combination of innocence and the promise of something far more dirty underneath it in her eyes."
    "You know, the look that makes her almost impossible for me to resist?"
    minami.say "Uh, uh, big bro."
    minami.say "You're not the one that should be saying sorry."
    minami.say "I was just jealous when you told me, that's all."
    mike.say "Y...you were?"
    mike.say "And now you're...not?"
    mike.say "Jealous, that is?"
    show minami tehe at center, zoomAt(1.5, (640, 1000))
    "Minami moves closer, her smile becoming less innocent with every step she takes towards me."
    minami.say "Oh no, big bro."
    minami.say "Now I've thought about it, the whole thing's really HOT!"
    mike.say "It...it is?!?"
    show minami happy at startle
    "Minami lets out a trill of laughter, as if she's amused at my cluelessness."
    show minami normal
    minami.say "Of course it is!"
    minami.say "Think about it - I come to the big city to be with my gorgeous big bro."
    minami.say "And not only do I get him, and he's EVERYTHING I wanted him to be."
    minami.say "But he's got a harem of girls already eating out of the palm of his hand too!"
    minami.say "It's like they can't resist you, big bro."
    show minami blush
    minami.say "Just like I can't..."
    "I know that I should be taking what she's saying with a massive pinch of salt."
    "Minami's nothing if not manipulative when it comes to getting what she wants."
    "But all the same, how much can a guy take when he's being described like that?"
    "God knows that Minami used to wrap me around her little finger when we were kids."
    "And now it seems like she's ten times better at it since she talked her way into my pants!"
    mike.say "That's great to hear, Minami - really, it is!"
    mike.say "So...so you're cool with me seeing [bree.name] and Sasha, right?"
    "Minami cocks her head on one side, the smile still fixed upon her face."
    minami.say "Sure, big bro, sure."
    show minami tehe
    minami.say "So long as you let me in on all of the fun too..."
    menu:
        "I can't do that":
            mike.say "Yeah, that's not gonna happen, Minami."
            mike.say "I should have just come out and said no when you started trying to butter me up!"
            show minami surprised -blush
            "Minami's smile turns instantly into a frown and she crosses her arms over her chest."
            minami.say "What?"
            show fx question
            minami.say "Why the hell not?!?"
            show minami annoyed
            mike.say "Minami, please!"
            mike.say "This thing I have going on with [bree.name] and Sasha, it's...complicated."
            mike.say "I can't just stroll up to them and ask to let someone else in on it."
            show minami normal
            minami.say "You could try, big bro - they might say yes!"
            mike.say "You really think so, Minami?"
            mike.say "And just how would that go, huh?"
            mike.say "'Hey, [bree.name], Sasha - you wanna let my little sister in on it when we all fuck?'"
            mike.say "'Oh, and by the way, I've been screwing her on the side.'"
            mike.say "'You know, keeping it in the family!'"
            show minami sad
            "From the look on Minami's face, I know that I probably shouldn't have gone there."
            "When this was about [bree.name] and Sasha, I was on pretty solid ground."
            "But I just made it about us being adopted siblings, which puts it all on her."
            minami.say "So what, big bro?"
            minami.say "Are you embarrassed about what we did?"
            mike.say "No, Minami - that's not what I meant!"
            show minami angry
            show fx anger
            minami.say "Well that's how it sounded, you jerk!"
            hide minami with moveoutright
            "And with that, she turns her back on me and storms off."
            "Leaving me alone and worried about what she might say or do next."
            $ game.flags.minamirefusedinhomeharem = True
        "I have to ask the girls.":
            "I think about saying no, but then it occurs to me that it's more of an instinct than anything else."
            if Harem.find(samantha, name='home'):
                "I mean sure, it was a serious leap to get involved with three girls at once."
            else:
                "I mean sure, it was a serious leap to get involved with two girls at once."
            "But once you're over that first hurdle, why turn into a prude about it?"
            "I'm not ashamed of Minami or what we've done together, not in the slightest."
            if Harem.find(samantha, name='home'):
                "Likewise I don't feel like [bree.name], Sasha, Samantha and me are doing anything wrong either."
            else:
                "Likewise I don't feel like [bree.name], Sasha and me are doing anything wrong either."
            "So why should I hide one from the other or let either be ruined in the same way?"
            if Harem.find(samantha, name='home'):
                "I'm seriously into [bree.name], Sam and Sasha, but Minami's been a part of my life for much longer."
            else:
                "I'm seriously into [bree.name] and Sasha, but Minami's been a part of my life for much longer."
            "I don't want to lose her for the sake of hooking up with my hot housemates."
            mike.say "Sure, Minami."
            mike.say "I'll talk to them as soon as I get the chance."
            show minami happy
            minami.say "Really, you will?!?"
            show fx exclamation
            minami.say "Oh, big bro, you're the best!"
            "She throws her arms around my neck, almost having to jump up thanks to her short stature."
            "This means that she's practically hanging off of me, and I have to cradle her buttocks to hold her up."
            hide minami
            show minami kiss
            with fade
            $ minami.flags.kiss += 1
            "The feeling is something else, and when she begins to kiss me full on the lips..."
            "Well, you get the idea."
            "I know that I'm taking a risk doing this."
            "But I truly believe that it's the right thing to do."
            if Harem.find(samantha, name='home'):
                "I just hope that [bree.name], Sam Sasha will see it that way too."
            else:
                "I just hope that [bree.name] and Sasha will see it that way too."
            "Because otherwise, I might have just agreed to light the fuse on a powder-keg."
            "One that could potentially blow the domestic harmony of the house to kingdom come!"
    return

label bree_sasha_request:
    "Let's just say that it takes me a while to be able to pluck up the courage to ask [bree.name] and Sasha about what Minami wants."
    "I mean, who could just walk up to two girls that he's already in a relationship and casually ask them to let his little sister join in?"
    "While I don't know who could do that, I definitely know who couldn't, because I look at him in the mirror every morning!"
    "And so I take my time, trying to pick a moment when I think that they'll be most open to what I have to say."
    "But even when that moment finally seems to have arrived, I'm pretty much a bag of nerves as I open my mouth to speak."
    mike.say "Ah, [bree.name]...Sasha..."
    show bree at right
    show sasha at left
    "As one, they look around at me, warm and open expressions on their faces."
    bree.say "Yeah, [hero.name]?"
    if sasha.flags.mikeNickname:
        sasha.say "Yes, [hero.name]?"
    else:
        sasha.say "What's up, man?"
    "I give them a shaky smile in return."
    "All the time trying not to look like a man on the way to the electric chair."
    mike.say "Well..."
    mike.say "You know that we've all been...getting along together?"
    show fx question at right
    "[bree.name] creases her brows into a frown, clearly wondering what I'm talking about."
    bree.say "Uh, we've always gotten on well, [hero.name]."
    show bree happy
    bree.say "That's one of the reasons that living here is so great!"
    "Sasha chuckles and shakes her head at the innocent response."
    show bree dazed
    show fx exclamation at left
    sasha.say "Don't be such a bimbo, [bree.name]!"
    sasha.say "He means how we've all been fucking as a threesome!"
    sasha.say "But somethings making him be a pussy about it - isn't it, [hero.name]?"
    show bree surprised
    "[bree.name] turns her puzzled frown on me again."
    bree.say "Is that right, [hero.name]?"
    bree.say "Is there something bugging you, huh?"
    "I shrug and shake my head, trying and probably failing to play it down."
    mike.say "It's...it's just about Minami."
    mike.say "Her living here with us all, while we're..."
    mike.say "While we're all an item, you know?"
    "I expect this to go down like a lead balloon."
    "But instead, I get a round of smiles and chuckles from [bree.name] and Sasha."
    show bree wink at right
    bree.say "Ooh, I know what you mean, [hero.name]."
    bree.say "I've felt SO naughty sneaking around behind her back!"
    bree.say "Maybe even a little guilty too."
    show sasha flirt at left5 with ease
    sasha.say "Don't worry about it, [hero.name]."
    sasha.say "We know how to be discreet."
    sasha.say "There's no reason for Minami to find us out."
    "Sasha meets my eye as she says this, and I can feel myself beginning to sweat."
    "She holds me there, her expression slowly changing from bright and breezy to serious in mere moments."
    show sasha normal
    "It seems that by staying silent and looking as white as a sheet, I've given her reason to doubt me."
    sasha.say "Unless..."
    sasha.say "Unless she knows about it already."
    show bree surprised at right5
    show fx question at right5
    with ease
    bree.say "Wha...what's that mean, Sasha?"
    bree.say "How could Minami have found out?"
    show sasha annoyed
    sasha.say "Well, neither of US would have said anything."
    sasha.say "So that just leaves..."
    show sasha normal
    "Sasha's mouth curls into a wry grin as she points straight at me."
    "[bree.name] stares at me in silence for a second in shock and surprise."
    "But soon enough, she finds her voice."
    show fx question at right5
    bree.say "[hero.name], how could you?!?"
    "I hold up my hands in a gesture of defence."
    "And I'm already backing off out range of a physical blow."
    mike.say "For god's sake, I didn't just come out and tell her!"
    mike.say "She's been sniffing around for a while now, suspecting we were up to something."
    mike.say "I figured that if I told her, maybe she'd just accept it and back off!"
    sasha.say "Which I suppose means that you did and she didn't."
    sasha.say "Am I right?"
    bree.say "Ooh, this is SO unfair!"
    bree.say "Why's there always someone wanting to spoil my fun?"
    "Okay, here it comes."
    "I just hope there's enough of me left afterwards for them to identify my body..."
    mike.say "Ah, that's the thing."
    mike.say "Minami's not interested in stopping us."
    mike.say "She's interested in turning our threesome into...well, a foursome!"
    show sasha surprised
    show bree surprised
    "The revelation is enough to stop both [bree.name] and Sasha dead."
    "Their mouths are hanging open in shock and surprise."
    "And I can only imagine what's going through their heads right now."
    "I think about saying something, trying to break the heavy silence that's fallen over us all."
    "But Sasha beats me to it, shaking off the funk to voice a question."
    show sasha annoyed
    sasha.say "Wait a minute, [hero.name]."
    sasha.say "You don't just want to let someone else into what we have going on."
    show sasha surprised
    show fx exclamation at left5
    sasha.say "You want it to be your SISTER!"
    "The sound of Sasha's voice seems to have the effect of snapping [bree.name] out it too."
    show bree dazed
    "She literally shakes her head, as if clearing out the mental cobwebs."
    show bree normal
    bree.say "Yeah, [hero.name] - how come you want to get it on with your own sister?"
    bree.say "Unless...unless..."
    show sasha angry
    show fx exclamation at left5
    sasha.say "Unless you already are!"
    "I guess that my cheeks must flush just as Sasha voices the thought."
    "Either that or else I look so shifty in that moment it's impossible to think anything else."
    "Both of the girls gasp in amazement, and I don't know if they're disgusted or impressed."
    mike.say "She's my adopted sister, remember?!?"
    with hpunch
    mike.say "ADOPTED!"
    show sasha sad
    "Sasha crosses her arms over her chest, studying me intently."
    show sasha annoyed
    "But then she looks at [bree.name] with a far more charitable expression on her face."
    sasha.say "He is right, [bree.name]."
    sasha.say "They're not actually related in any real sense."
    show bree annoyed
    bree.say "I hear you, Sasha."
    bree.say "And if we can deal with there being three of us in this relationship..."
    bree.say "Maybe this isn't that much stranger?"
    mike.say "Erm...so...what do you say?"
    mike.say "Is Minami in or not?"
    show sasha sad
    show bree angry
    "Suddenly I feel both of them turning their gazes on me again."
    "And I can't help feeling like an animal staring down the barrel of a hunter's gun..."
    if bree.sub <= 50 or sasha.sub <= 50:
        show sasha annoyed
        sasha.say "I don't know about you, [bree.name]."
        sasha.say "But I don't want to get it on with some snot-nosed little brat!"
        "I instinctively open my mouth to defend Minami."
        "But a quick glare from Sasha stops me before I can put my foot in it."
        show bree sad
        bree.say "Ooh, this is so unfair!"
        bree.say "I think Minami's a sweet kid."
        show bree annoyed
        bree.say "Or...I did until I found out she was spying on us all!"
        show sasha normal
        "Sasha nods at this, turning to face me as she does so."
        sasha.say "Here's where I am on this one, [hero.name]."
        sasha.say "You can keep doing whatever you're doing with Minami."
        sasha.say "And all three of us can keep doing what we're doing with each other too."
        sasha.say "But they stay exclusive for anyone but you."
        "I nod slowly, aware that I could come out of this one pretty well."
        "So long as [bree.name] agrees, Minami can be mollified and I don't find a way to screw it up for myself."
        show bree normal
        bree.say "Ah...I guess I'm cool with all of that, Sasha."
        show bree evil
        bree.say "I don't want to stop what we're doing - it's WAY too much fun for that!"
        "The wicked grin on [bree.name]'s face as she says this goes a long way to reassuring me."
        "Making me think that it's all going to be okay."
        mike.say "Thanks so much - you guys are the best!"
        show bree happy
        bree.say "Yeah, I suppose we are!"
        show sasha happy
        show fx exclamation at left5
        if sasha.flags.mikeNickname:
            sasha.say "You better remember that, [hero.name]."
        sasha.say "And good luck letting Minami down too!"
        "All I can do is nod and smile with a nervous laugh."
        "But I'm already dreading the fallout that's sure to come from Minami not getting what she wants..."
        $ game.flags.minamirefusedinhomeharem = True
    else:
        sasha.say "I don't know about you, [bree.name]."
        show sasha joke
        sasha.say "But I kind of like the idea of breaking in a new prospect!"
        "I instinctively open my mouth to object to Minami being described in such terms."
        show bree normal blush
        "But a quick glance at the look on [bree.name] and Sasha's faces stops me dead."
        "I don't think I've ever seen them both look so turned on and wicked before."
        "At least not outside of the bedroom!"
        bree.say "Yeah, I know what you mean, Sasha."
        show bree evil
        bree.say "She's cute, and the whole little sister thing is like forbidden fruit!"
        show bree flirt
        "[bree.name] bites her lip a little as she looks at me."
        bree.say "And the fact that [hero.name]'s already fucking her..."
        sasha.say "I know, what you mean - it makes the idea that much hotter!"
        sasha.say "It's like he went out and seduced her, just for us..."
        "I swallow nervously, more than a tad worried about the way they're discussing Minami."
        "I feel like it should really be triggering me, hearing them talk about her like she's a piece of meat."
        "But then maybe I'd be more inclined to speak up and say something if they weren't turning me on so much!"
        mike.say "S...so you're into it, right?"
        mike.say "You want me to tell Minami she's in?"
        show sasha dazed
        "Sasha regards me with a look that puts me instantly in mind of a hungry lioness."
        "And the way [bree.name] nods is only slightly less predatory in nature too."
        sasha.say "Looks that way."
        bree.say "Yeah, you go tell her she's in, [hero.name]."
        sasha.say "And let's hope she's been careful what she wishes for too."
        sasha.say "Because she's sure as hell going to get it!"
        "All I can do is nod and smile with a nervous laugh."
        "But my imagination is already running away with all of the possibilities that lie ahead..."
        $ game.flags.breeacceptminami = True
        $ game.flags.sashaacceptminami = True
        $ bree.love += 2
        $ sasha.love += 2
        if Harem.find(samantha, name='home'):
            if game.flags.samanthaacceptminami:
                $ Harem.join_by_name("home", "minami")
                $ game.flags.ongoinghomeharem = False
            else:
                "I still have to ask Samantha."
        else:
            $ Harem.join_by_name("home", "minami")
            $ game.flags.ongoinghomeharem = False
    hide sasha
    hide bree
    return

label bree_request:
    "I could keep putting it off forever, just telling myself that the time isn't quite right to ask something like this."
    "But then the chances are that if I did that, the precise right moment might never actually turn up at all."
    "And so that's why I steel myself and choose the first chance that I get to ask [bree.name] about what Minami wants."
    "As soon as we're alone together, I just come straight out and broach the subject."
    "I figure that if I catch [bree.name] a little off guard she's more likely to actually think about it before saying no."
    "That and there's no Sasha there to elbow in on the conversation, swaying [bree.name] towards her own way of thinking."
    "So, here goes nothing..."
    show bree with dissolve
    mike.say "[bree.name]..."
    bree.say "Uh, yeah, [hero.name]?"
    mike.say "I...I wanted to ask you something."
    "[bree.name] smiles at me, a puzzled look in her eyes."
    bree.say "Okay, [hero.name], you're making it sound pretty weird."
    bree.say "But whatever - ask away!"
    mike.say "Well...it's kind of Minami that wants me to ask you this."
    mike.say "And it involves me too."
    mike.say "And you...and Sasha..."
    show bree surprised blush
    "Understanding dawns on [bree.name]'s face, and she instantly turns a bright shade of red."
    bree.say "Oh no, oh no, oh no!"
    show fx question
    bree.say "She saw us, didn't she?!?"
    show bree dazed
    bree.say "Oh, [hero.name], I'm so sorry that your poor kid sister had to find out like that!"
    show bree sad
    bree.say "Poor Minami - she must be devastated, the precious little thing."
    "The smile on my own face is pained as [bree.name] gushes with misplaced sympathy."
    "Not least because it would have been so easy to get away with it if that were really the situation at hand."
    "But now I have to put her straight and tell her the real reason that I'm here on Minami's behalf."
    mike.say "Yeah, well..."
    mike.say "You see, that's not quite it, [bree.name]."
    show bree surprised
    show fx question
    bree.say "Huh?"
    mike.say "She knows about you, me and Sasha."
    mike.say "But she's not exactly traumatised by it."
    show fx question
    bree.say "She isn't?"
    "Okay, here goes nothing."
    mike.say "No, [bree.name]."
    mike.say "It's the opposite - she wants in on the action."
    show bree dazed
    "[bree.name] looks at me in silence, the implications of what I just said not fully sinking in."
    "It takes a few long, drawn-out moments for the light of realisation to appear in her eyes."
    show bree surprised blush
    "And then she turns an even deeper shade of red than before."
    bree.say "Oh...my...god!"
    show fx exclamation
    bree.say "No way, [hero.name]!"
    bree.say "That'd mean she'd have to have sex...with you!"
    mike.say "Ah, yeah, bree."
    mike.say "I think she kind of gets that."
    show bree at startle
    show fx exclamation
    bree.say "But, but...she's your SISTER!"
    mike.say "Adopted sister, [bree.name] - I think it's REALLY important we remember that fact!"
    "[bree.name] shakes her head, as much in bafflement at my relatively calm reaction as at the actual issue at hand."
    "But even as she does so, I can almost see the wheels turning inside of her head."
    show bree lose
    "And then her eye go wide with horror."
    bree.say "You say that like...like the two of you had already..."
    "I keep on looking her straight in the eye."
    "Not saying anything, but not denying anything either."
    "And pretty quickly she comes to the only logical conclusion possible."
    show bree surprised
    show fx question
    bree.say "You...you and...Minami?!?"
    mike.say "Yeah, [bree.name], pretty much."
    mike.say "Look, I understand if you're mad."
    mike.say "Or grossed out."
    mike.say "Or both."
    "I didn't think it was possible, but [bree.name]'s eyes seem to go wider still."
    if bree.sub <= 50:
        show bree annoyed
        bree.say "It's just not what I expected to hear from you, [hero.name]."
        show bree sad
        "She lets out a deep sigh, as if she's more than a little disappointed in me."
        bree.say "It took a lot for me to be okay with the three of us hooking up."
        bree.say "I know that you and Sasha are WAY more adventurous than me."
        bree.say "But I really tried my hardest to go along with it."
        bree.say "And...well, I think it's something that's very special."
        "I can only nod, knowing how hard this must be for [bree.name]."
        "Sure, she's no prude and knows exactly how to have fun."
        "But maybe this is a step too far for her after all."
        mike.say "Okay, [bree.name], I hear what you're saying."
        mike.say "Thanks for hearing me out."
        show bree normal
        "[bree.name] smiles at me, more broadly than I'd been expecting."
        bree.say "It's okay, [hero.name]."
        bree.say "Don't get me wrong, I like Minami - she's a sweet kid."
        bree.say "But I guess I just like you and Sasha more!"
        $ game.flags.breerefusedminami = True
        if game.flags.sasharefusedminami:
            $ game.flags.minamirefusedinhomeharem = True
    else:
        bree.say "Oh, no..."
        bree.say "That's not it..."
        show bree evil
        bree.say "I'm...kind of...feeling a little turned-on by the idea!"
        "It takes me a moment to actually get what [bree.name]'s saying."
        mike.say "You...you ARE?!?"
        show bree flirt blush
        "None of this is helping to stop [bree.name] from blushing."
        "And by now she's redder than ever."
        bree.say "Well, yeah, [hero.name]."
        bree.say "The hot guy that I move in with manages to seduce me."
        bree.say "Then he gets the cute goth girl we live with into it too."
        bree.say "And now his spunky little sister wants in on the action."
        bree.say "It's like the plot of a crazy movie or something."
        bree.say "One that I get to star in!"
        "All I can do is shake my head in amazement."
        mike.say "So...so you're saying yes?"
        "[bree.name] nods at this, with an enthusiasm that I can't quite believe."
        $ game.flags.breeacceptminami = True
        if Harem.find(samantha, name='home'):
            if game.flags.samanthaacceptminami and game.flags.sashaacceptminami:
                $ Harem.join_by_name("home", "minami")
                $ game.flags.ongoinghomeharem = False
        elif game.flags.sashaacceptminami:
            $ Harem.join_by_name("home", "minami")
            $ game.flags.ongoinghomeharem = False
    hide bree
    return

label bree_convince_sasha:
    "Now I have [bree.name] on board with the idea of letting Minami join in and turn the threesome into a foursome."
    "Which means that two thirds of the votes are going the way that I want them to."
    "And although Sasha might have said no, I figure that the matter's not settled until she's discussed it with [bree.name] too."
    "Luckily for me, it doesn't take much to convince [bree.name] to put the matter to Sasha either."
    "As now that she's behind the idea, all of her previous misgivings seem to have melted away."
    show bree at left
    show sasha sad at right5
    with dissolve
    "And it's actually [bree.name] that takes the initiative as soon as she spots Sasha alone."
    show bree happy
    bree.say "Sasha, hey!"
    show bree normal
    show sasha normal
    "Sasha looks up at the sound of [bree.name]'s voice, an open, interested expression on her face."
    show sasha annoyed
    "But when she sees me trailing behind, her eyes roll and she lets out a groan of frustration."
    sasha.say "Urgh!"
    sasha.say "Please tell me this isn't about the Minami thing!"
    show bree dazed at left5 with ease
    "[bree.name] stops a couple of paces from Sasha, planting her hands on her hips."
    "She seems taken aback by the other girl's getting straight down to business."
    bree.say "Well...yeah, it is."
    show bree normal
    bree.say "I guess there's no sense in hiding it if you're gonna use your psychic powers on me!"
    bree.say "[hero.name] tells me that you said no way, right?"
    "Sasha crossed her arms over her chest, adopting a defensive pose."
    "It seems like she can't decide which one of us she wants to direct her ire towards."
    "Clearly she's mad at me for not letting the whole thing with Minami lie after she already said no."
    "But she's also getting pretty pissed off with [bree.name], probably for not siding with her straight away."
    sasha.say "And from the tone of your voice, I'm going to guess that you didn't."
    sasha.say "Am I right?"
    "[bree.name] nods at this, not letting Sasha shame her into regretting her decision."
    bree.say "This isn't about what I said, Sasha."
    bree.say "But it's not really about what you said either."
    "Sasha frowns at this, clearly not expecting such a cryptic answer from [bree.name]."
    "And I have to admit that it's not her usual, breezy kind of chat too."
    show fx question at right5
    sasha.say "What...what's that supposed to mean?"
    show bree annoyed
    bree.say "When I heard that you'd said no to letting Minami join in, I was..."
    bree.say "I was worried about you, Sasha."
    show sasha surprised
    show fx question at right5
    sasha.say "Huh?"
    sasha.say "Why would you be worried about me?!?"
    show bree sad
    bree.say "Well, it's so not like you, is it?"
    bree.say "You've always been the one that was so exciting, even a little dangerous, Sasha."
    bree.say "You play guitar in a rock band, you wear black all the time and you're SO kinky in the bedroom!"
    bree.say "And...and I couldn't have plucked up the courage to get involved with [hero.name] AND you."
    bree.say "Not if you hadn't showed me that it was okay to be outrageous."
    "[bree.name] sighs ruefully to herself."
    "And it sounds like she's disappointed in Sasha, but can't bring herself to actually say as much."
    show bree normal
    bree.say "But I guess we all have our limits, don't we?"
    bree.say "I just never thought you'd hit yours before I hit mine, that's all."
    show sasha annoyed
    "Sasha stares at [bree.name] in complete silence for what feels like forever."
    "And I can see in her eyes that she's got nothing to fire back with."
    "She's clearly being forced to digest and process all that's just been thrown at her."
    sasha.say "It...it's not about that, [bree.name]."
    sasha.say "It's the principle of the thing, you know?"
    bree.say "Huh...it's what now?"
    sasha.say "The principle, yeah?"
    sasha.say "We had something special, and [hero.name] ruined it!"
    "Sasha pauses to jab an accusatory finger in my general direction."
    bree.say "Oh, Sasha, you're being such a prude!"
    show sasha surprised
    show fx question at right5
    sasha.say "WHAT?"
    sasha.say "I am not - how can you even say that?!?"
    bree.say "Seriously, you need to lighten up."
    bree.say "You coped with three of us, so why not four?"
    show bree evil
    bree.say "Because you know, Sasha, we can always start up another threesome without you..."
    "Is...is [bree.name] actually threatening her right now?"
    "Hinting that she'll just replace Sasha with Minami if she doesn't say yes?"
    show sasha angry
    sasha.say "That's...that's blackmail, [bree.name]!"
    bree.say "Oh, is it?"
    bree.say "Maybe it looks that way to you, Sasha."
    bree.say "But me, I've just gotten a taste for this polygamy stuff."
    bree.say "And I'm not going to let you or anyone else take it away from me."
    show sasha surprised
    "Sasha looks shocked at [bree.name]'s stark admission."
    "That and the fact that she's been told in no uncertain terms that she can be replaced with Minami."
    sasha.say "N...no...no...don't do that!"
    show sasha sad
    sasha.say "Look...maybe I was too hasty, yeah?"
    show bree normal
    bree.say "So, what are you saying, Sasha?"
    bree.say "You'll give it a try?"
    show sasha normal
    sasha.say "Okay, [bree.name], okay."
    "The very moment that Sasha gives in and agrees to let Minami in on the threesome, [bree.name]'s entire demeanour changes."
    "She instantly becomes the same bright and bouncy girl that I know so well, all smiles and positive energy."
    show bree happy
    bree.say "Great, Sasha!"
    bree.say "Now, that wasn't so hard was it?"
    "Sasha nods slowly, still looking more than a little confused at what just happened."
    "But before she can properly think it over, I join in on the congratulations."
    "And together, [bree.name] and I sweep her up with what we wanted all along."
    hide bree
    hide sasha
    $ game.flags.sashaacceptminami = True
    if Harem.find(samantha, name='home'):
        if game.flags.samanthaacceptminami:
            $ Harem.join_by_name("home", "minami")
            $ game.flags.ongoinghomeharem = False
        else:
            "I still have to ask Sam about all this."
    else:
        $ Harem.join_by_name("home", "minami")
        $ game.flags.ongoinghomeharem = False
    return

label sasha_request:
    if Harem.together('home', 'bree', 'sasha', 'samantha', 'lexi'):
        "I keep thinking about the best way to go about asking [bree.name], Sasha, Samantha and Lexi about the possibility of Minami joining our fivesome."
        "Which would obviously make it into a sixsome, I guess - I'm not sure of the exact terminology involved here."
    elif Harem.together('home', 'bree', 'sasha', 'samantha'):
        "I keep thinking about the best way to go about asking [bree.name], Sasha and Samantha about the possibility of Minami joining our foursome."
        "Which would obviously make it into a fivesome, I guess - I'm not sure of the exact terminology involved here."
    elif Harem.together('home', 'bree', 'sasha', 'lexi'):
        "I keep thinking about the best way to go about asking [bree.name], Sasha and Lexi about the possibility of Minami joining our foursome."
        "Which would obviously make it into a fivesome, I guess - I'm not sure of the exact terminology involved here."
    else:
        "I keep thinking about the best way to go about asking [bree.name] and Sasha about the possibility of Minami joining our threesome."
        "Which would obviously make it into a foursome, I guess - I'm not sure of the exact terminology involved here."
    "But unlike the sex, I have a hunch this would be something better done one-on-one than with all parties concerned."
    "I wouldn't exactly call it divide and conquer, as I feel like I'm the one that's going to be under attack pretty soon!"
    "All the same, I steel myself to get it done as soon as the first chance arises for me to do so."
    "And so, as soon as I get a moment alone with Sasha, I take the plunge..."
    show sasha with dissolve
    mike.say "Ah, Sasha..."
    mike.say "You got a minute?"
    sasha.say "Huh...oh, yeah."
    show fx question
    sasha.say "Sure thing, [hero.name] - what's up?"
    "Well, here goes nothing..."
    mike.say "I...I just wanted to talk to you about something, that's all."
    sasha.say "Ooh, this should be good!"
    sasha.say "You never want to talk about something."
    show sasha joke
    sasha.say "Not unless it's serious!"
    "Sure, she's joking around with me right now."
    "But Sasha's also telling the truth."
    "I am the kind of guy that only gets serious like this when there's something serious on my mind."
    mike.say "Yeah, Sasha - you know me too well!"
    mike.say "There is something I need to talk about."
    mike.say "It's about Minami..."
    show sasha normal
    "Sasha raises an eyebrow, clearly intrigued to hear what I have to say next."
    "She's been friendly towards my little sister since she moved in."
    "But I have no idea if she's actually accepted her presence like [bree.name] seems to have done."
    sasha.say "You don't say!"
    mike.say "Yeah, well..."
    mike.say "Let's just say that she might have figured something out about us."
    if Harem.together('home', 'bree', 'sasha', 'samantha', 'lexi'):
        sasha.say "By that, I'm gonna guess that you mean you, me, [bree.name], Sam and Lexi?"
    elif Harem.together('home', 'bree', 'sasha', 'samantha'):
        sasha.say "By that, I'm gonna guess that you mean you, me, [bree.name] and Sam?"
    elif Harem.together('home', 'bree', 'sasha', 'lexi'):
        sasha.say "By that, I'm gonna guess that you mean you, me, [bree.name] and Lexi?"
    else:
        sasha.say "By that, I'm gonna guess that you mean you, me and [bree.name]?"
    "I nod quickly, still trying to rush on with what I have to say."
    mike.say "That and she might have asked someone about it."
    show sasha annoyed
    sasha.say "Urgh..."
    sasha.say "And that someone would be you?"
    "I nod again."
    sasha.say "And that someone didn't deny it, did he?"
    mike.say "No, he didn't."
    mike.say "Because maybe he was already feeling guilty because..."
    mike.say "Because he'd slept with her..."
    show sasha shocked
    "Sasha looks at me in shock, her mouth open and her eyes wide."
    "She hardly needs to shake her head for me to know just how baffled she is right now."
    sasha.say "So let me get this straight, [hero.name]."
    sasha.say "You told your little sister, who you're also sleeping with, that we're all fucking each other?"
    sasha.say "Why are you telling me all of this now?"
    show sasha joke
    sasha.say "Are you actually hoping that I'll kill you?"
    sasha.say "Kill you so you don't have to deal with all of this shit?!?"
    "I manage a weak smile, trying to play off what Sasha's saying as a joke."
    "At least I hope that it's a joke and she's not actually thinking of murdering me!"
    mike.say "If you think that's funny, then you'll love what I've got to say next."
    mike.say "Minami wants to get in on the thing we have going too!"
    if sasha.sub <= 50:
        show sasha annoyed
        show fx exclamation
        sasha.say "Oh no, no way!"
        if Harem.together('home', 'bree', 'sasha', 'samantha', 'lexi'):
            sasha.say "I can cope with her knowing that we're a fivesome."
        elif Harem.together('home', 'bree', 'sasha', 'samantha') or Harem.together('home', 'bree', 'sasha', 'lexi'):
            sasha.say "I can cope with her knowing that we're a foursome."
        else:
            sasha.say "I can cope with her knowing that we're a threesome."
        sasha.say "I can even get my head around you fucking her on the side."
        sasha.say "But what we have is special, [hero.name]."
        sasha.say "We can't just let someone in on a whim."
        "I open my mouth to protest, but then I let the words go unspoken."
        "I've already asked so much of Sasha, merely by telling all of this stuff."
        if Harem.together('home', 'bree', 'sasha', 'samantha', 'lexi'):
            "She could have dumped my ass for either telling Minami about the fivesome."
        elif Harem.together('home', 'bree', 'sasha', 'samantha') or Harem.together('home', 'bree', 'sasha', 'lexi'):
            "She could have dumped my ass for either telling Minami about the foursome."
        else:
            "She could have dumped my ass for either telling Minami about the threesome."
        "Or ended it when she found out that I was sleeping with my sister too."
        "And she'd have been well within her rights to do so too."
        "What right do I have to go on pushing her after that?"
        "So instead of trying to argue, I just nod my head."
        mike.say "Okay, Sasha, okay."
        mike.say "I hear you."
        mike.say "Thanks for hearing me out."
        show sasha normal
        "Sasha smiles at me, weakly and yet I sense with genuine sincerity."
        if Harem.together('home', 'bree', 'sasha', 'samantha', 'lexi'):
            sasha.say "Look, I know we're a messed-up quintet, me, you, [bree.name], Sam and Lexi."
        elif Harem.together('home', 'bree', 'sasha', 'samantha'):
            sasha.say "Look, I know we're a messed-up quartet, me, you, [bree.name] and Sam."
        elif Harem.together('home', 'bree', 'sasha', 'lexi'):
            sasha.say "Look, I know we're a messed-up trio, me, you, [bree.name] and Lexi."
        else:
            sasha.say "Look, I know we're a messed-up trio, me, you and [bree.name]."
        sasha.say "But we've got something that's pretty special, don't we?"
        "I return her smile, nodding as I turn to go."
        $ game.flags.sasharefusedminami = True
        if game.flags.breerefusedminami:
            $ game.flags.minamirefusedinhomeharem = True
    else:
        show sasha normal
        "Sasha opens her mouth to speak."
        "And I can almost hear her saying no before she utters a single word."
        "But then Sasha pauses, as if she's thought of something she'd not considered before."
        "I see a strange smile spread across her face, one that makes me feel strangely nervous."
        sasha.say "So, [hero.name]..."
        show fx question
        sasha.say "You seduced your kid sister, yeah?"
        "I can already feel myself blushing from the way she's looking at me."
        "I mean, she's right - I did sleep with my adopted little sister."
        "But somehow she's managing to make it all sound so sleazy!"
        mike.say "I...I guess you could put it like that, Sasha."
        mike.say "I'm not really sure who seduced who."
        mike.say "It kind of went both ways, you know?"
        "Sasha shakes her head at this, still smiling at me in that same odd way."
        sasha.say "No, [hero.name], I don't."
        sasha.say "You see, I never fucked my brother, adopted or otherwise."
        show sasha flirt
        sasha.say "But now that I think about it, that's pretty hot..."
        mike.say "It...it is?"
        mike.say "I mean, yeah...of course it is!"
        sasha.say "But not as hot as watching you fuck her in front of me."
        sasha.say "So as far as I'm concerned, she's in."
        sasha.say "You go and tell that nosey little bitch I said so."
        "I return her smile, nodding with enthusiasm as I turn to go."
        $ game.flags.sashaacceptminami = True
        if Harem.find(samantha, name='home'):
            if game.flags.samanthaacceptminami and game.flags.breeacceptminami:
                $ Harem.join_by_name("home", "minami")
                $ game.flags.ongoinghomeharem = False
        elif game.flags.breeacceptminami:
            $ Harem.join_by_name("home", "minami")
            $ game.flags.ongoinghomeharem = False
    hide sasha
    return

label sasha_convince_bree:
    "As soon as I have Sasha on board with the idea of Minami join in on what we've got going on, I can feel the momentum shifting."
    "It's like having her on my side is like rolling a snowball down a hill, watching it get larger as it goes."
    "In fact, I hardly have to hint at the notion of her trying to talk [bree.name] around to our way of thinking."
    "And as soon as I do, Sasha practically marches off to confront the only dissenting member of the threesome."
    "I follow behind her as she does so, feeling like I'm being drawn along in her wake."
    show sasha at right
    show bree at left
    sasha.say "[bree.name], we need to talk."
    show bree surprised
    "[bree.name] looks up from what she's doing, clearly surprised at Sasha's tone of voice."
    "She blinks a couple of times before managing to speak, shaking off her momentary confusion."
    show bree normal
    bree.say "Oh, hey, Sasha."
    bree.say "Hey, [hero.name] - I didn't see you there, behind Sasha!"
    "It's only after she's said all of this and received no response in kind that her mood takes a visible nose-dive."
    show fx question at left
    bree.say "Erm...what's the matter, Sasha?"
    bree.say "Why are the two of you looking at me like that?"
    show sasha normal at right5 with ease
    sasha.say "Don't play innocent with me, [bree.name]."
    sasha.say "You know exactly what this is about."
    show fx question at left
    bree.say "I...I do?"
    show sasha annoyed
    "Sasha rolls her eyes in frustration."
    show sasha normal
    "But then she makes [bree.name] yelp and leap back as she pokes a finger in her face."
    show fx exclamation at right5
    sasha.say "Don't play the dumb blonde with me, - because it won't work!"
    sasha.say "We could have had an innocent, Japanese little sister jump into bed with us, [bree.name]."
    sasha.say "An innocent...Japanese...little sister!"
    sasha.say "Just let that sink in for a moment."
    show bree dazed
    "[bree.name] shakes her head, still visibly reeling from the verbal assault she's just sustained."
    "I can't help but feel sorry for her being ambushed like this."
    "But I'm not about to jump in and come to her aid either."
    "Not when I want basically the same thing as Sasha does anyway."
    "And even if I did, I'd only be gaining the gratitude of a single girl."
    "By keeping quiet, I'm getting in with two thirds of the women that live under the same roof as me."
    show bree annoyed
    bree.say "But, Sasha, it's Minami we're talking about!"
    bree.say "I thought we were supposed to be like big sisters to her."
    bree.say "Not lure her into our web of sin!"
    show sasha joke
    sasha.say "Ha, is that what you think?!?"
    sasha.say "From what I hear, she pretty much twisted [hero.name]'s arm for this!"
    show bree normal
    show sasha normal
    "Suddenly, both [bree.name] and Sasha are staring right at me."
    "One looking for an explanation and the other for me to back her up."
    "I nod with a helpless smile on my face, rubbing the back of my head with one hand."
    mike.say "Ah, well..."
    mike.say "Now that you ask, that is kind of how it happened."
    show sasha happy
    "Sasha nods, satisfied that I've done as I was told."
    sasha.say "You see, [bree.name]?"
    show sasha normal
    sasha.say "Minami's plenty old enough to know what she's getting into."
    sasha.say "The only reason that you'd say no is if you're afraid of her making you look bad."
    sasha.say "Or that you're not as adventurous as you claim to be."
    sasha.say "So, which is it?"
    sasha.say "Because both are pretty good reasons for us to kick you out in favour of Minami."
    sasha.say "Right, [hero.name]?"
    "My jaw literally drops open at this, and I realise that Sasha's pretty much dropped me right in it."
    "In order to get what I want, it looks like I'm going to have to back her all the way."
    mike.say "Er...well..."
    mike.say "It's going to be hard to go back to how things were after this."
    mike.say "Awkward doesn't even begin to cover it..."
    mike.say "And it just wouldn't be the same without you, [bree.name]!"
    "Nothing that I said seems to be having much of an effect."
    "Not until I add that last line in there for good measure."
    show bree normal blush
    "As soon as I do, [bree.name]'s face lights up and she looks me straight in the eye."
    bree.say "Do you really mean that, [hero.name]?"
    show fx question at left
    bree.say "You won't trade me in for a younger model, will you?"
    "I open my mouth to say something about her not being that much older than Minami."
    "But I feel Sasha jab me in the ribs, as if predicting what I was about to say."
    mike.say "No...no way, [bree.name]."
    mike.say "It doesn't matter how many of us there are."
    mike.say "You're still one of the originals, just like me and Sasha."
    show bree happy
    "[bree.name] nods, her smile slowly returning as she does so."
    bree.say "O...okay, [hero.name]."
    bree.say "I'll try my best to make this work for us all."
    bree.say "Tell Minami I'm fine with her joining in."
    "Sasha glances sideways, a smirk on her face that's intended for me alone."
    "But I'm just grateful that we were able to talk [bree.name] around to our way of thinking."
    hide bree
    hide sasha
    $ game.flags.breeacceptminami = True
    if Harem.find(samantha, name='home'):
        if game.flags.samanthaacceptminami:
            $ Harem.join_by_name("home", "minami")
            $ game.flags.ongoinghomeharem = False
        else:
            "I still have to ask Sam about all this."
    else:
        $ Harem.join_by_name("home", "minami")
        $ game.flags.ongoinghomeharem = False
    return

label samantha_request:
    "I'm plucking up the courage to ask Sam the question that's been on my mind for days now."
    "But even as I finally find it in me to walk up to her and do it, I'm still wondering if I'm actually crazy."
    "I mean, I'm already living under the same roof as three super hot girls."
    "And the four of us are also involved in what counts as the hottest thing ever to happen to me!"
    "Surely I must be insane to even think of doing something that could ruin it all?"
    "Is it really worth it, just to get Minami involved in on the action too?"
    "But even knowing all that, here I am, still going through with the idea."
    "So maybe I am crazy after all."
    "Or maybe I'm just willing to dream!"
    show samantha with dissolve
    mike.say "Ah..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey there, Cupcake..."
    else:
        mike.say "Hey there, Sam..."
    show samantha happy
    "At the sound of my voice, Sam turns and gives me a smile."
    "It's one of the kind that make me feel funny inside."
    "Like she's melting me with how sexy and perfect she is!"
    samantha.say "Hey, [hero.name]."
    show fx question
    samantha.say "What's on your mind?"
    "I feel my cheeks begin to flush as I suddenly get all hot and bothered."
    "All I did was walk up to her and say hello."
    "How could she have known that I have something on my mind?"
    "Is she some kind of psychic?!?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Wha...what do you mean, Cupcake?"
    else:
        mike.say "Wha...what do you mean, Sam?"
    mike.say "I don't have a mind."
    mike.say "I...I mean...I don't have anything on my mind!"
    "Sam giggles at my state of confusion and shakes her head."
    samantha.say "Oh, [hero.name]!"
    samantha.say "I can always tell from the tone of your voice."
    samantha.say "You'd be better sending me a text."
    samantha.say "That way I can't hear what you're saying without meaning to say it!"
    "Rubbing the back of my neck with one hand, I try to laugh it off."
    if samantha.flags.nickname == "cupcake":
        mike.say "Wow, Cupcake."
    else:
        mike.say "Wow, Sam."
    mike.say "I guess you know me that well, huh?"
    "She nods at this, but then cocks her head on one side."
    "And I can tell from the look on her face that this isn't over yet."
    show samantha normal
    samantha.say "And I know you well enough to get what you're doing now too."
    samantha.say "Don't try to throw me off, [hero.name]."
    samantha.say "Just hurry up and get to the point, okay?"
    "I nod, finally accepting that I'm just going to have to do as she says."
    "Sam obviously knows me better than I know myself."
    "And trying to sneak up on the subject just isn't going to work."
    mike.say "Ah, okay, okay."
    mike.say "It's about Minami."
    samantha.say "Your little sister?"
    show samantha surprised
    show fx question
    samantha.say "What about her?"
    "I'm about to open my mouth and just come out with it."
    "But then I see a change in Sam's expression."
    "Rather than being amused, she suddenly seems to become worried."
    show samantha annoyed
    samantha.say "Oh no..."
    samantha.say "Did she find out about the thing we have with [bree.name] and Sasha?"
    samantha.say "Is she freaking out about it?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...no, Cupcake."
    else:
        mike.say "Ah...no, Sam."
    mike.say "She found out about it - you got that bit right."
    mike.say "But she's not losing her mind over it."
    mike.say "She...well, she kind of wants in on it!"
    "Sam's mouth drops open at the news, her eyes going wide with surprise."
    "But it doesn't take long for her to recover, and I see her expression change again."
    "Now she's studying me, as if a thought just occurred to her."
    show samantha normal
    samantha.say "Kind of a strange thing for a sister to ask her brother."
    samantha.say "Don't you think, [hero.name]?"
    "Instantly I'm back to blushing and trying to shake off the implications of her words."
    if samantha.flags.nickname == "cupcake":
        mike.say "Adopted sister, Cupcake - Minami's my adopted sister!"
    else:
        mike.say "Adopted sister, Sam - Minami's my adopted sister!"
    mike.say "It's only incest if you're blood relatives!"
    "I didn't think it was possible, but Sam's eyes become wider still."
    samantha.say "Erm, who even mentioned incest, [hero.name]?"
    show samantha surprised at startle
    show fx exclamation
    samantha.say "Oh my god - you're fucking her, aren't you?!?"
    "I think about flat out denying it for a moment."
    "But then I remember what the ultimate point of this conversation was meant to be."
    "And if Minami gets in on the foursome, I'll be fucking her anyway."
    if samantha.flags.nickname == "cupcake":
        mike.say "Yeah, Cupcake, you got me."
    else:
        mike.say "Yeah, Sam, you got me."
    mike.say "Minami and I have been sleeping together for a while now."
    show samantha normal
    "Sam fixes me with a smile and shakes her head."
    samantha.say "I don't mind you sleeping with other girls, [hero.name]."
    samantha.say "Not so long as you're honest about it with me."
    show samantha happy
    samantha.say "It's actually quite hot, you know?"
    mike.say "It...it is?!?"
    show samantha normal blush
    samantha.say "Sure it is!"
    samantha.say "Minami's super-cute."
    samantha.say "And then there's the fact she's your sister too!"
    mike.say "Adopted sister!"
    samantha.say "Whatever..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Well, I wanted to ask, Cupcake..."
    else:
        mike.say "Well, I wanted to ask, Sam..."
    mike.say "Would you be cool with Minami getting in on our thing with [bree.name] and Sasha?"
    if game.flags.breeacceptminami and game.flags.sashaacceptminami:
        mike.say "I already spoke to [bree.name] and Sasha about it."
        mike.say "And they both agreed."
    elif game.flags.breeacceptminami:
        mike.say "I already spoke to [bree.name] about it."
        mike.say "And she's agreed."
    elif game.flags.sashaacceptminami:
        mike.say "I already spoke to Sasha about it."
        mike.say "And she's agreed."
    else:
        mike.say "I haven't spoken to [bree.name] or Sasha yet."
        mike.say "But if you're up for it, I know we can convince them too."
    samantha.say "Hmm..."
    samantha.say "Do I want your sweet little, adopted, Asian sister to hop into bed with us?"
    samantha.say "That's a tough one, [hero.name]."
    samantha.say "I'm going to need some time to think about it."
    mike.say "Erm..."
    if samantha.flags.nickname == "cupcake":
        mike.say "How much time, Cupcake?"
    else:
        mike.say "How much time, Sam?"
    show samantha happy
    samantha.say "I'm joking, [hero.name]!"
    samantha.say "Of course I'm fine with it!"
    show samantha normal
    "I can't help but nod and smile as Sam makes her feelings plain to me."
    "And I think I just took a massive step towards being the luckiest guy in the world!"
    $ game.flags.samanthaacceptminami = True
    if game.flags.breeacceptminami and game.flags.sashaacceptminami:
        $ Harem.join_by_name("home", "minami")
        $ game.flags.ongoinghomeharem = False
    return

label minami_crash_threesome:
    $ minami.flags.crash_threesome = True
    scene bg bedroom1 with fade
    "I feel pretty bad that the answer to my asking for Minami to be let into what we're doing as a threesome was a no."
    "But you really can't do something like that without a unanimous decision from everyone involved, can you?"
    "All the same, I guess that [bree.name] and Sasha must have picked up on how bummed out I was by how it turned out."
    "And they seem to know just the thing to take my mind off of it and pick up my mood..."
    "As soon as they get the chance, I find myself being pulled towards my bedroom door."
    show bree at left5
    show sasha at right5
    with dissolve
    "[bree.name] has me by one hand, Sasha by the other, and both of them are grinning at each other the whole time."
    "I have no idea what they've got planned for me, but that's a big part of the thrill."
    "And before too long, I've all but forgotten about what was bothering me just now!"
    "Once we're inside of my room, [bree.name] holds her finger to her lips, letting me know to keep quiet."
    "The they start to strip off my clothes, working quickly so that I'm undressed mere moments later."
    "I walk over to the bed and lie down."
    "Reclining with my head on my hand so that I can watch as they do the same to each other."
    show bree underwear at left4
    show sasha underwear at right4
    with ease
    "Pretty soon they're stripped down to their underwear, teasing me with every move they make."
    show bree naked at center, zoomAt (1.2, (440, 840)) with dissolve
    "[bree.name] slips out of her bra and panties, and joins be on the bed."
    "She wraps her arms around my neck and pulls herself close to me, pressing her chest against mine."
    show sasha at right with ease
    "But when I look over to Sasha, I see that she's headed in the opposite direction."
    mike.say "You okay, Sasha?"
    bree.say "Yeah, where are you going?"
    show sasha at top_mostright with ease
    "By now, Sasha's reached the door, still dressed only in her panties and bra."
    "She opens it halfway and begins to slip out, explaining herself as she goes."
    sasha.say "Bathroom stop, gotta go now!"
    sasha.say "But I call dibs on [hero.name]'s cock!"
    show bree annoyed
    bree.say "Hey, no fair!"
    hide sasha with moveoutright
    play sound door_slam
    "As the door slams shut behind Sasha, I can't help chuckling at [bree.name]'s annoyance."
    show bree normal at center, zoomAt(1.5, (640, 1040))
    "I shake my head and pull her closer to me again."
    mike.say "Hey there, [bree.name], just let it go."
    mike.say "I'm sure we can find something just as good for you too!"
    show bree happy
    "[bree.name] smiles at this, biting her lip in anticipation."
    hide bree
    show bree kiss naked
    with fade
    $ bree.flags.kiss += 1
    "But rather than making straight for something more intense and involved, I lean in and kiss her on the lips."
    "It's such a simple thing, one that's so common and yet so hot when you do it right."
    "And the way that [bree.name] melts into it is more than enough to make me hard as a rock in no time at all."
    hide bree
    show bree evil naked at center, zoomAt(1.5, (640, 1040))
    with fade
    "She breaks off for a moment to giggle suddenly, surprising me by doing so."
    "But then I realise that she's feeling the sensation of my cock stiffening against her thighs."
    bree.say "Mmm..."
    bree.say "I know it's naughty of me to say this, [hero.name]."
    bree.say "But I like that Sasha's going to be sucking your cock after I got you hard!"
    "[bree.name] can seem so pure and innocent at times, at least in comparison to Sasha."
    "And so it's a massive turn-on to hear her talking dirty."
    hide bree
    show bree kiss naked
    with fade
    "She kisses me again, and this time that same feeling of arousal permeates the whole thing."
    "It feels like [bree.name] gets hotter and more aroused with each movement of my tongue inside of her mouth."
    scene black with dissolve
    "So much so, that when we hear the sound of the door opening again, she laughs through the kiss."
    "I do the same, as we both imagine Sasha lining herself up to suck my painfully erect dick."
    "And it's not long before I can feel a pair of slender, delicate female hands taking hold of it."
    "Their touch is so soft, the skin so smooth that it's almost like being stroked with silk."
    "The first sensations of tongue and lips brushing the head come next."
    if hero.has_skill("guitar"):
        "And I think that I have to ask Sasha how she managed to get rid of the callouses on her fingers and palms."
        "Trust me, as a fellow guitarist, I know how hard it is to avoid that kind of thing!"
    "It's then that I think I hear the sound of the bedroom door opening again."
    "Normally I'd be more aware of such a noise, but I'm more than a little distracted right now."
    "So it's only when I hear the sound of a familiar voice from that direction that I react at all."
    with hpunch
    sasha.say "WHAT THE FUCK?!?"
    "I'm fully aware that Sasha shouldn't be able to talk around a mouthful of cock."
    scene bg bedroom1 with wipeup
    "And so I open my eyes and sit bolt upright, almost pushing [bree.name] off of the bed in the act."
    show bree naked surprised at center, zoomAt(1.5, (540, 1040)) with hpunch
    bree.say "Huh...whoa...hey, what gives?!?"
    show sasha angry underwear topless a at right
    "The scene that I find myself looking at is pretty fucking crazy."
    "One that I don't think I could have cooked up in the weirdest of dreams."
    "There, standing in the doorway, is Sasha."
    "Which makes me wonder who was the one with my cock in her mouth?"
    scene minami bj
    show minami bj suck
    with vpunch
    "And so I look down to see Minami staring back up at me, her eyes wide with panic."
    "But the image is made all the more insane by the fact that she still has my dick between her lips."
    bree.say "Wait a minute - you're not Sasha!"
    "I refrain from pointing out that [bree.name] just stated what was absolutely obvious."
    "Instead choosing to concentrate on the fact my little sister just snuck in here uninvited."
    "Well, that and the fact that she has my cock in her mouth too!"
    mike.say "Minami...what the actual fuck?!?"
    show minami bj out -suck
    "Minami looks sheepishly at me as she slides her lips off of my cock."
    "She retreats to the end of the bed, perching there with a look of shame on her face."
    scene bg bedroom1
    show bree naked a at left
    show minami sad naked c zorder 2
    show sasha angry underwear topless a zorder 1 at right
    with fade
    "And it's only now that I realise she's also naked."
    "The nipples on her petite breasts are standing firm and erect."
    "A sure sign that she's every bit as aroused and horny as I was no more than a minute ago."
    sasha.say "Jesus Christ, [hero.name]."
    sasha.say "I was only gone, like what, five minutes!"
    mike.say "What?!?"
    mike.say "You...you think I knew it wasn't you, Sasha?"
    "Sasha cocks her head on one side, as if I just said the dumbest thing in the entire history of the human race."
    show fx anger at right
    sasha.say "Erm, hello - she was sucking your cock!"
    sasha.say "If someone was licking me down there, I think I'd know who it was!"
    show bree angry at left
    bree.say "That's not fair, Sasha."
    show bree flirt blush at left
    bree.say "[hero.name] and me...well, we were making out the whole time."
    bree.say "We had our eyes closed and it was getting really intense."
    mike.say "Yeah, Sasha - you were the one that called dibs on my dick, remember?"
    show sasha normal at right
    "I can see that Sasha's about to fire back at me, when I hear someone giggling."
    "As one, everyone looks round to see Minami, covering her mouth with her hands."
    "No longer looking shameful, and trying to stifle the laughter that's gripping her."
    mike.say "Wha...what's up, Minami?"
    show fx question at right
    sasha.say "Yeah, what's so funny, you little perv?"
    show minami normal
    "Minami shakes her head, finally regaining control of herself enough to talk."
    minami.say "It's...it's you guys."
    minami.say "You're supposed to be like some edgy, sexy bunch of rebels."
    minami.say "But you argue like an old, married couple!"
    bree.say "Ooh, you cheeky little..."
    bree.say "Someone aught to spank some manners into you!"
    show minami hunt
    minami.say "Well, I was kind hoping one of you might do that..."
    menu:
        "Just get out!":
            mike.say "Minami, I think you'd better get out of here - NOW!"
            mike.say "You just stepped over the line, big time."
            show minami angry zorder 2 at startle
            show sasha annoyed zorder 1
            show bree annoyed -blush
            "Minami looks at me, a defiant light flaring in her eyes."
            "I have to admit that I'm impressed."
            "She's clearly in the wrong and outnumbered three-to-one."
            "And for a moment I think that she's actually going to make a fight of it."
            show minami at right5 with move
            "But then something seems to snap inside of her, and she bolts for the door."
            show sasha zorder 1 at right5
            show minami zorder 2 at top_mostright
            with ease
            "Sasha watches her go, but steps neatly aside, not barring Minami's way."
            hide minami with moveoutright
            "As soon as we're alone again, I let out a sigh of frustration."
            mike.say "Well, that was not how I saw this going!"
            show bree surprised at left
            if game.flags.breerefusedminami or game.flags.sasharefusedminami:
                bree.say "[hero.name], I thought you told her we said no already?"
                sasha.say "Get real, [bree.name], of course he did."
                show sasha annoyed at right
                sasha.say "You really think that little bitch listened to him, huh?"
                "I feel myself prickle at the way Sasha is talking about Minami."
                "But under the circumstances, I think better of defending her."
                bree.say "Oh...yeah, I see."
            show bree sad
            bree.say "Guys, I don't think I want to do anything else tonight."
            bree.say "Sorry!"
            "Now it's Sasha's turn to sigh as she picks up her clothes."
            show sasha sad
            sasha.say "Me neither, [bree.name]."
            sasha.say "But at least you two got to do something before she killed the mood!"
            "For my part, I choose to keep quiet."
            "Simply nodding in agreement so that I can be alone with my thoughts."
            "Sure, I'm frustrated at not getting off and mad at Minami for what she just did."
            "But I'm also worried."
            "For her and the future of this relationship while she's living with us."
            $ bree.love -= 2
            $ sasha.love -= 2
            $ minami.love -= 10
            $ Harem.find(sasha, name="home")[0].leave("minami")
            $ game.flags.ongoinghomeharem = False
            $ minami.flags.haremdenied = 3
            scene bg black with dissolve
        "You will get what you deserve.":
            mike.say "Maybe we should let you stay, Minami."
            mike.say "That way we can make sure you get exactly what you deserve..."
            "I see hope flare in Minami's eyes as she thinks that she's getting her own way."
            "But in her eagerness, she misses the truth of what I just said."
            "Sasha and [bree.name], on the other hand, seem to grasp my meaning almost instantly."
            "Both of them knowing the difference right now between what Minami wants and what she deserves..."
            show sasha joke at right
            sasha.say "That sounds pretty good to me."
            sasha.say "How about you, [bree.name]?"
            show bree evil -blush at left
            bree.say "Oh, I think that'd be lots of fun!"
            "Minami looks around at the three of us."
            "And I can see that she's suddenly nervous about the way things are going."
            show minami normal
            minami.say "Ah...sure, guys...that's really cool of you!"
            minami.say "So...what do I need to do?"
            sasha.say "You just worry about finishing what you started, yeah?"
            bree.say "We can handle the rest!"
            "Minami stares at them for a moment, and then back at me."
            hide minami
            hide bree
            hide sasha
            show bj breeminamisasha2 minami bree sasha
            with fade
            "I just shrug my shoulders and look down at my still erect cock."
            "She seems to get the message, crawling tentatively back towards me."
            show bj breeminamisasha2 blowjob breewink
            "Minami holds my eye until the very moment that she has it in her mouth once more."
            show bj breeminamisasha2 eyesclose
            "And then she closes her eyes as she resumes the interrupted blowjob."
            "Sasha waits for a little while, lulling Minami into an illusion of safety."
            show bj breeminamisasha2 sashaevil
            "But once she's sure the other girl is totally distracted, she makes her move."
            show bj breeminamisasha2 -sasha with dissolve
            "Silently directing [bree.name] towards Minami's exposed breasts, Sasha reaches for her pussy at the same time."
            "Almost in the same instant, they begin to stroke and caress her."
            "[bree.name] pinches and twists Minami's already erect nipples."
            "Sasha traces the shape of the lips between her thighs, teasing as she goes."
            "I hear Minami whimper at the sensation, but she doesn't stop what she's doing to me."
            "If anything, the fact that the girls are playing with her makes it all the more intense."
            "As Minami's pleasure becomes that much greater, she swallows my cock with a renewed appetite."
            "It feels to me as if she can only find satisfaction from taking me as deep and desperately as possible."
            "But all I can really know is that she's mere moments away from making me cum..."
            menu:
                "Cum in her mouth":
                    "As I feel myself about to lose it, Sasha and [bree.name] are quick to act."
                    show bj breeminamisasha2 breewink sasha sashaevil with dissolve
                    "They leave off what they were doing to Minami and hold her in place instead."
                    show bj breeminamisasha2 cumshot eyesopen breesurprised sashasurprised sashablush breeblush with hpunch
                    "This means that when I finally let go, she has no choice but to swallow the entire thing."
                    with hpunch
                    "Minami gulps and gags, but all the same she chokes down all that I have to give."
                    show bj breeminamisasha2 eyesclose with hpunch
                    "And only then do Sasha and [bree.name] release her, letting her collapse onto the bed."
                    show bj breeminamisasha2 -cumshot -blowjob dickcum mouthcum swallow sashanormal breenormal
                    "My cock slides out of Minami's mouth as she does so, strings of cum still trailing from the head."
                    show bj breeminamisasha2 mouthcum open eyesopen
                    "She lies there unable to speak, gasping for breath and drooling a mixture of semen and saliva onto the sheets."
                "Cum on her face":
                    "As I feel myself about to lose it, Sasha and [bree.name] are quick to act."
                    show bj breeminamisasha2 -blowjob eyesopen breewink sasha sashaevil with dissolve
                    "They manoeuvre Minami in just such a way that my cock pops straight out of her mouth."
                    "But she's still held in the exact same spot as it bobs in front of her face."
                    "There's just enough time for her to focus on it, a surprised look in her eyes."
                    show bj breeminamisasha2 cumshot eyesclose breesurprised sashasurprised sashablush breeblush with hpunch
                    "And then I lose it, straight into her face."
                    show bj breeminamisasha2 -cumshot facecum dickcum sashanormal breenormal with hpunch
                    "Cum spatters over Minami's nose, cheeks and mouth before she can even turn away."
                    "It runs down to her chin, dripping off in heavy globs."
                    show bj breeminamisasha2 -bree -sasha eyesopen with dissolve
                    "Only then do Sasha and [bree.name] release her, letting her collapse onto the bed."
                    "She lies there unable to speak, gasping for breath and drooling a mixture of semen and saliva onto the sheets."
            "No one speaks in the moments that follow, simply gazing down at Minami as she pants and coughs."
            "I know for sure that this must mean a sea change in her relationship to us all."
            "But for the life of me, I can't be sure if it means that she's now officially a part of this thing."
            "Or else she's just nominated herself to be the occasional butt of a sexual prank the likes of this one."
            $ bree.love += 2
            $ sasha.love += 2
            $ minami.love += 2
            if Harem.find(samantha, name='home'):
                if game.flags.samanthaacceptminami:
                    $ Harem.join_by_name("home", "minami")
                    $ game.flags.ongoinghomeharem = False
                else:
                    $ game.flags.minamirefusedinhomeharem = False
                    $ game.flags.breeacceptminami = True
                    $ game.flags.sashaacceptminami = True
                    "I still have to ask Sam about all this."
            else:
                $ Harem.join_by_name("home", "minami")
                $ game.flags.ongoinghomeharem = False
            call sleep (["bree", "minami", "sasha"]) from _call_sleep_minami_crash_threesome
    return

label bj_bree_sasha_minami_intro:
    $ game.flags.bj_bree_sasha_minami = True
    scene bg bedroom1 with fade
    "I don't know what's the matter with me today, there's just something making me feel..."
    "Making me feel...well, just kind of...meh!"
    "Maybe I got out the wrong side of the bed this morning."
    "Or perhaps I'm just not firing on all cylinders for some reason."
    "But whatever the case, I feel like I'm stuck in a funk that I can't explain or shake off."
    "Which means that I'm not fantastic company either, as [bree.name] and Sasha soon discover."
    "I'm laying - well, more like slumping on my bed, when [bree.name] appears in the doorway."
    show bree at top_mostright with moveinright
    bree.say "Hey, [hero.name]!"
    show bree at right5 with ease
    bree.say "How are you feeling today?"
    mike.say "Harumph..."
    show bree surprised
    show fx question at right5
    bree.say "Wha..."
    bree.say "Did you actually just say 'harumph'?"
    mike.say "I might have - what of it?"
    show sasha at top_mostright with moveinright
    "It's at that moment Sasha chooses to walk into the room."
    show bree at left5
    show sasha sad at right5
    with ease
    "And from the expression on her face, it's clear she caught the end of that little exchange."
    sasha.say "Wow, [hero.name]."
    sasha.say "Who took a shit on your cornflakes, huh?"
    mike.say "Grumble...."
    show bree surprised
    bree.say "Wait, did you just say..."
    show sasha annoyed
    show fx exclamation at right5
    sasha.say "Yeah, [bree.name] - he did!"
    sasha.say "Jesus, what a grouch!"
    show bree dazed
    "I'm about to summon all of my strength to reply."
    "Maybe I can actually manage to string together a much as a basic sentence."
    "But before I can speak, the last member of the household not present makes an appearance too."
    show minami at top_mostright with moveinright
    minami.say "Hey, [bree.name]!"
    minami.say "Hey, Sasha!"
    show bree at left
    show sasha at center
    show minami at right
    with ease
    minami.say "What's going on in here?"
    sasha.say "It's your brother, Minami."
    sasha.say "He's what!"
    bree.say "Yeah, he's being a total downer today!"
    "The last thing I need right now is a dose of Minami's saccharine charms."
    "And I open my mouth, hoping to get a word in this time."
    "But she beats me to the punch again!"
    minami.say "Aw, don't mind him."
    minami.say "He used to get like this all the time back home."
    minami.say "Mom and I used to call him 'The Incredible Sulk'!"
    show sasha normal
    sasha.say "Really?"
    show bree happy at startle
    bree.say "Ooh...that's really kinda funny!"
    with hpunch
    mike.say "HEY!"
    mike.say "You never told me that?!?"
    mike.say "And just for the record, I'm not sulking, okay?"
    "Minami rolls her eyes at me and then shakes her head, amused at my denials."
    show bree normal
    show minami annoyed
    minami.say "Oh please, big bro!"
    minami.say "You always sulk - especially when you're horny!"
    bree.say "Does he really do that, Minami?"
    sasha.say "Huh..."
    sasha.say "Sure would explain a lot!"
    show minami normal
    minami.say "Oh, hell yeah."
    minami.say "And in the past, I could never do a thing about it."
    minami.say "Not like now - right, girls?"
    call bj_bree_sasha_minami from _call_bj_bree_sasha_minami_3
    $ game.pass_time(2)
    return

label bj_bree_sasha_minami:
    "Minami glances meaningfully at [bree.name] and Sasha, all three exchanging nods."
    "It's one of those moments where a guy can't hope to read a girl's face."
    "They're communicating in that secret language that they have, faster than you can follow."
    show bree zorder 2 at center, zoomAt(1.25, (340, 940))
    show sasha zorder 3 at center, zoomAt(1.25, (940, 940))
    show minami zorder 1 at center
    with ease
    "And before I can flinch, let alone move, they're on me like a pack of wolves!"
    "It's only now that I remember I'm naked under the bedclothes."
    show bree at center, zoomAt(1.5, (340, 1040))
    show sasha at center, zoomAt(1.5, (940, 1040))
    with vpunch
    "[bree.name] grabs my left arm, Sasha my right, holding me down on the bed."
    show minami at center, zoomAt(1.25, (640, 840))
    with vpunch
    "At the same time, Minami makes a dive for my blanket."
    "She tears it away with a speed that leaves me astonished."
    show bree at center, zoomAt(1.5, (300, 1040))
    show sasha at center, zoomAt(1.5, (980, 1040))
    show minami at center, zoomAt(1.5, (640, 1040))
    with vpunch
    "And a moment later, she's grabbed my cock too!"
    scene bg black
    show bj breeminamisasha minami
    with fade
    minami.say "Aww, don't worry, big bro."
    minami.say "I know what you want, even if you don't!"
    minami.say "Trust me - I know what you need..."
    "And with that, she begins to stroke the shaft of my cock."
    "As bad as my mood is, it doesn't take long for her attentions to have an effect."
    "Minami smiles wickedly as it stiffens in her grasp, looking at [bree.name] and Sasha as she does so."
    "As if sensing that there's no need to keep a hold of me, they release my arms."
    show bj breeminamisasha bree sasha with dissolve
    "And then the pair of them kneel down to either side of Minami, huddling in close."
    "They stare down at my cock, which is now hard as a rock."
    "Minami gives it a sharp tug, forcing me up and onto my feet."
    "And then she begins to kiss and lick at the base as the others watch her with interest."
    show bj breeminamisasha minamiside tome
    bree.say "Hmm..."
    show bj breeminamisasha breehappy
    bree.say "I guess she was right, Sasha."
    bree.say "This is the perkiest I've seen him all day!"
    sasha.say "Little sis knows best!"
    show bj breeminamisasha sashahappy
    sasha.say "But that doesn't mean we can't join in..."
    "As one they lean in and begin to give my balls the same treatment as Minami's giving my cock."
    "I was already starting to gasp at the sensation of the former."
    "But the addition of the latter makes pant out loud."
    "Seriously, the feeling is just that good - intense and deeply sensual all at once."
    show bj breeminamisasha minamionmouth
    "Minami swallows the head, and then begins to work up and down the shaft."
    "She takes it deep, but never enough to choke on, her eyes closed the whole time."
    "But then, without warning, she lets it pop out of her mouth."
    "My own mouth opens, and I'm ready to ask why on earth she stopped."
    show bj breeminamisasha sashahand nohandsminami
    "Which is precisely when Sasha ducks in there to take her place."
    "The change-over is so smooth that it feels that they've practiced it before."
    "Though I'm not in any kind of position to ask."
    show bj breeminamisasha sashaonmouth
    "And that's because Sasha sets a much quicker pace than Minami before her."
    "It's like she's trying to keep the momentum going as best she can."
    "And thankfully, Sasha's best is generally something quite special!"
    "Pretty soon she's taking me deeper and sucking harder than ever before."
    "There's no time for me to catch my breath before I'm pushed ever further."
    "Minami and [bree.name] must be doing something right now."
    "But all I can feel is Sasha's lips and tongue wrapping around my cock!"
    mike.say "Oh shit, Sasha!"
    mike.say "What are you doing to me?!?"
    "All I get in return for my sudden outburst is a round of mischievous giggles."
    "And I assume they're coming from Minami and [bree.name]."
    "As there's no pause in Sasha's efforts."
    "In fact, I think I'm about to cum!"
    show bj breeminamisasha breenormal
    bree.say "Oh no you don't!"
    bree.say "I know what that face means."
    bree.say "Move over, Sasha - my turn!"
    "I feel Sasha break off from what she's doing and then gasping for breath."
    "And before I can protest, [bree.name] grabs a hold of my cock."
    show bj breeminamisasha breehand nohandssasha
    "I mean that too - she squeezes it like her life depends on me not shooting my load just yet!"
    "I guess the shock and the sudden pain must have the desired effect too."
    "As I feel the urge to cum lessening until it's enough to resist."
    show bj breeminamisasha breeonmouth
    "Well, that is until [bree.name] gets it in her own mouth..."
    "I thought that Sasha was pushing the limits, but I'm not prepared for what happens next."
    "My guess is that [bree.name] knows it won't take much to make me cum right now."
    "And so she's decided that this isn't the time to beat about the bush."
    "That's why she gets straight down to business, taking me deeper than ever before."
    "Neither Minami nor Sasha dared to swallow my cock like [bree.name]'s doing right now."
    "I have no idea if it actually counts as deep-throat or not."
    "But it certainly feel like that's what she's doing to me!"
    "A part of me wants to tell her to stop, at least to plead with her to slow down."
    "And that's as much out of concern for her choking as it is for anything else."
    "The only problem is that I'm sure she'd just ignore me."
    "That and the fact she's rendered me totally unable to speak!"
    "I fully expect to shoot everything that I have straight down [bree.name]'s throat."
    "Then I expect to be the one giving her the Heimlich manoeuvre moments later."
    show bj breeminamisasha -breeonmouth -minamiside
    "But at the last second, [bree.name] rears her head up, releasing me from her mouth."
    "She keeps a tight hold on my cock as I erupt from the sensation."
    show bj breeminamisasha breeopen sashaopen minamiopen
    "And all three of them are leaning in close enough to ensure a shower."
    show bj breeminamisasha breeshot minamifacial breefacial sashafacial with vpunch
    pause 1.0
    with vpunch
    "The cum paints their faces with sticky, white stripes as I gasp for breath."
    show bj breeminamisasha breesmile sashasmile minaminormal with vpunch
    "Which is a stark contrast to their laughter, as they lick their lips."
    minami.say "See, girls - told you I knew what he needed!"
    minami.say "He's just a guy, after all, so he's not that complicated."
    bree.say "Kinda like a dog that needs to be walked, yeah?"
    sasha.say "More like a hamster that need to run on it's wheel!"
    "I open my mouth to protest, but then I just shake my head and close it again."
    "Who cares if they want to compare me to some kind of domestic pet?"
    "After the treatment that they just gave me..."
    "Well, maybe I could come to like it!"
    return

label bree_minami_sasha_transition_bj_foursome:
    scene expression f"bg {game.room}"
    "Getting a blowjob from all three of the girls certainly snapped me out of my funk."
    "But even more than that, it's given me an appetite for more."
    "I can't concentrate on anything else, no matter how hard I try."
    "I need another hit, and I need to get it now!"
    "And that's when it strikes me that we haven't properly initiated Minami."
    "Sure, she was in on the action earlier, which was great."
    "But she hasn't been on the receiving end yet."
    mike.say "Hey, [bree.name]?"
    show bree naked at right with dissolve
    mike.say "You too, Sasha?"
    show sasha naked at left with dissolve
    bree.say "Huh?"
    sasha.say "What's up, [hero.name]?"
    mike.say "I was thinking, we haven't shown Minami the ropes yet!"
    show minami naked scared with dissolve
    "Minami looks up in obvious surprise."
    "Her eyes are wide and her mouth hangs open."
    minami.say "Wha..."
    minami.say "What's all this about ropes?!?"
    show bree happy at startle
    show sasha happy at startle
    "[bree.name] and Sasha burst out laughing."
    "And I shake my head with a chuckle."
    mike.say "Figure of speech, Minami."
    mike.say "I mean action of the bedroom variety!"
    show bree happy at startle
    "[bree.name] leaps up and claps her hands together."
    bree.say "That sounds like a great idea!"
    "Sasha gets up more slowly."
    "But she looks just as enthusiastic."
    sasha.say "Yeah - we can use my room."
    sasha.say "Let's go get things ready, [bree.name]."
    "The two of them hurry off together."
    "Which leaves me alone with Minami."
    "I give her what I hope is my most reassuring smile and hold out my hand."
    mike.say "Come on, Minami."
    mike.say "This is going to be great, I promise!"
    show minami normal
    "Minami nods as she stands up and takes my hand."
    scene secondfloor
    show minami naked
    with fade
    "Reaching Sasha's door, I pause with my hand hovering above the handle."
    mike.say "Whatever happens, Minami, don't worry."
    mike.say "I'll be right there, looking out for you."
    show minami blush
    "Minami looks up at this, a smile on her face."
    "But I can see that she's still a little scared."
    minami.say "Thanks, big bro."
    minami.say "But I'll be fine - I promise!"
    "I offer her a nod in way of an answer."
    scene bg bedroom3 with fade
    "And then I open the door and walk into Sasha's bedroom."
    show minami naked with moveinleft
    sasha.say "Hey guys, what took you so long?"
    "Neither Minami nor I can actually manage to utter a response to the question."
    "The reason might have seemed to be that we just walked in on Sasha while she's totally naked."
    "But seriously, we're here for something that pretty much needs her to be in a state of total undress."
    "No, what stops the pair of us in our tracks is when Sasha turns around."
    show sasha strapon at right with dissolve
    show minami surprised at startle
    "Revealing for the first time that she is wearing something after all..."
    sasha.say "What's the matter?"
    sasha.say "You never seen a girl wearing a strap-on before?"
    show minami scared
    minami.say "Is...is she...going to use...that?"
    minami.say "On me?!?"
    show sasha joke
    sasha.say "Aww, don't be scared, Minami."
    sasha.say "It won't hurt all that much, I promise!"
    sasha.say "And if you don't believe me, ask [hero.name] here..."
    "Minami's eyes go wide at this."
    "She looks at me as though she's about to ask the dreaded question."
    show bree naked at left with moveinleft
    "But then the door bursts open, and [bree.name] strolls straight in."
    "And stops dead as she sees the scene playing out before her."
    show bree evil
    bree.say "Ooh, Sasha - what a big cock you have!"
    show sasha happy
    sasha.say "All the better to bang you with, my dear!"
    show bree happy at startle
    show sasha at startle
    "They both laugh, until Minami lets out a yelp of fear."
    show bree normal
    "[bree.name] turns to regard her, genuine concern in her expression as she does so."
    bree.say "Oh, Minami, I'm sorry."
    bree.say "I'm just so used to that thing by now, it doesn't bother me."
    bree.say "But it scared the hell out of me at first too."
    bree.say "Trust me though, there's nothing to be scared about."
    bree.say "[hero.name] and I will keep you safe from the Big Bad Sasha."
    "[bree.name]'s assurances are met with a peal of laughter from Sasha and another yelp from Minami."
    "Not wanting this thing to go south before it even gets started, I take this as my cue to step in."
    mike.say "[bree.name]'s right Minami - she's just screwing with you."
    mike.say "Aren't you, Sasha?"
    "For a moment, I actually think that she's going to go the other way."
    show sasha normal
    "But then Sasha shakes her head in amusement."
    sasha.say "Sure, of course I am."
    show bree at left5 with ease
    "[bree.name] leans in close to Minami, a bright and breezy smile on her face."
    bree.say "See, Minami - nothing to be afraid of!"
    show minami at startle
    "Minami nods, but then jumps a little as she finds [bree.name]'s hands upon her."
    show minami normal
    "I see Minami taking a deep breath, seemingly steeling herself for what lies ahead."
    sasha.say "We were talking before, [bree.name] and myself."
    sasha.say "And we think you need something familiar to start with."
    bree.say "Yeah, Minami."
    bree.say "That's why we're gonna let you have dibs on [hero.name]'s cock this time."
    bree.say "I'd tell you it's a sweet ride."
    bree.say "But you already know that, right!"
    show minami blush
    "Minami blushes at this, and I can feel my cheeks flushing a little too."
    "Suddenly I feel the need to step up and be heard, not treated like an object here!"
    mike.say "I'm fine with that, as long as you are, Minami."
    mike.say "So, what do you say?"
    "Minami nods as she takes hold of my hand."
    minami.say "Sure thing, big bro."
    minami.say "I know I'm safe with you!"
    return

label bree_minami_threesome_intro:
    $ CONDOM = False
    scene bg bedroom1
    show bree normal at left5
    show minami normal at right5
    with fade
    "I think that all three of us are more than a little nervous as we sneak into my room and close the door behind us."
    "I mean, I could understand Minami being nervous, as she's the youngest and probably the most innocent."
    "[bree.name]'s a little older and more experienced than Minami, but there are still things that are new to her."
    "And I'd like to think that I'm the worldly type, the kind of guy that could take this kind of thing in his stride."
    "But as much as I want it, I'm kind of nervous about the three of us getting together too."
    "Everyone's quiet, like we're afraid of being caught."
    "Yet we're all consenting adults, - we're not doing anything wrong!"
    show minami blush
    minami.say "Erm..."
    minami.say "What happens now, big bro?"
    minami.say "I mean...how do we get started?"
    mike.say "I don't know, Minami."
    mike.say "It's not like there are any rules for this sort of thing!"
    mike.say "Are there, [bree.name]?"
    show bree blush
    bree.say "N...no, not really!"
    show bree flirt -blush
    bree.say "Normally I'd just jump on you, wouldn't I?"
    bree.say "Or you'd pounce on me!"
    bree.say "I like it when that happens!"
    show minami surprised
    minami.say "Oh..."
    minami.say "So do I pounce on one of you?"
    minami.say "Or do you guys both pounce on me?"
    mike.say "Ah..."
    mike.say "Maybe we should just start out slow, yeah?"
    mike.say "Sit down on the bed and see where things go?"
    "[bree.name] and Minami seem relieved to have someone finally make a decision."
    show bree underwear normal
    show minami underwear normal norobe
    with dissolve
    "They hurry over to the bed and start stripping off their clothes."
    show bree naked normal
    show minami naked normal
    with dissolve
    "I follow on their heels, surprised to see them already getting naked."
    mike.say "Hey, you guys!"
    mike.say "Wait for me!"
    "[bree.name] and Minami look up as one."
    "And then they begin to giggle at my haste to get undressed."
    show bree happy at startle
    bree.say "Hurry up, [hero.name]!"
    show minami happy at startle
    minami.say "Yeah, big bro - or we'll have to start without you!"
    "I shake my head and redouble my efforts."
    "And it looks comical as I hop towards the bed, still trying to pull my pants off."
    "But secretly I'm relieved to hear the sound of their laughter."
    "Because it means that they're relaxing and the nerves are fading away."
    show bree at center, zoomAt(1.25, (400, 900))
    show minami at center, zoomAt(1.25, (880, 900))
    with vpunch
    "In the end I half collapse onto the bed landing between [bree.name] and Minami."
    "They both scoot aside, but then [bree.name] throws herself atop me."
    bree.say "I've got him, Minami!"
    show bree evil
    show fx exclamation at left5
    bree.say "Now you grab the goods!"
    "Minami doesn't need to be told what that means."
    "With [bree.name] pinning me down, she pounces on my midriff."
    "And I gasp as she grabs hold of my cock!"
    minami.say "I got it, [bree.name]!"
    show minami tehe
    show fx question at left5
    minami.say "Now what are we gonna do with it?"
    menu:
        "Fuck [bree.name]":
            call bree_minami_threesome from _call_bree_minami_threesome
        "Stack them":
            call bree_minami_sandwich from _call_bree_minami_sandwich
    $ bree.sexperience += 1
    $ minami.sexperience += 1
    $ game.pass_time(2)
    return

label bree_minami_threesome:
    "I choose that exact moment to wrap my arms around [bree.name]."
    show bree surprised with hpunch
    "She squeals in surprise as I pull her ass towards my lap."
    mike.say "We're going to stick it inside of [bree.name]."
    mike.say "That's what were going to do!"
    "[bree.name] wriggles and squirms in my grasp, still squealing."
    show bree happy blush with hpunch
    "But I can hear the fact she's fighting off the giggles too."
    bree.say "Help me, Minami!"
    bree.say "You have to save me!"
    "Now it's Minami's turn to let out a cry of mock alarm."
    "She tries to scurry away across the bed."
    show bree evil
    "But [bree.name]'s too quick for her."
    "She catches Minami just as I caught her."
    scene threesome breeminami with fade
    bree.say "Oh my..."
    bree.say "What do we have here?"
    bree.say "Forget saving me, Minami."
    bree.say "I'll just help myself to this instead!"
    "I watch as [bree.name] parts Minami's buttocks."
    "Then she leans forwards and begins to lick between them."
    show threesome breeminami breetonguemid
    "Minami's pussy is already glistening in the light."
    "It's slick and beginning to open itself like a flower."
    show threesome breeminami breetongueup
    "And [bree.name]'s tongue only serves to hurry things along."
    minami.say "Oooh..."
    show threesome breeminami breetonguemid
    minami.say "Oooh, big bro..."
    minami.say "What's she doing to me?!?"
    mike.say "The same thing I'm about to do to her!"
    show threesome breeminami breetonguedown mike with dissolve
    "I hear [bree.name] let out a muffled moan as I rub my cock between her thighs."
    "Then I take a deep breath, and thrust myself forwards..."
    menu:
        "Fuck her pussy":
            show threesome breeminami breetonguemid
            "Seeing [bree.name] licking at Minami's pussy is what makes up my mind."
            "All I can think about is the same part of her body and how much I want it."
            show threesome breeminami breetongueup
            "So I stroke the head of my cock along the lips between her legs."
            call check_condom_usage (bree) from _call_check_condom_usage_49
            if _return == False:
                return
            if CONDOM:
                show threesome breeminami condom
            "She lets out another muffled moan, quivering with anticipation."
            "And I don't need any more of an invitation than that."
            show threesome breeminami breetonguemid mike vaginal
            "Slowly and firmly I push myself into her."
            "There's almost no resistance from [bree.name], just smooth surrender."
            "This means that I can sink into her in one motion."
            "I don't stop until I can go no further, filling her as much as I can."
            show threesome breeminami breetonguedown breepleasure
            "[bree.name]'s surprise only seems to last for a few seconds."
            "And soon enough her head is back between Minami's thighs."
            "I take this as my cue to spring into action."
            show threesome breeminami breetonguemid
            "Which means that I begin thrusting into [bree.name] with all my strength."
            "The whole time that I'm doing it I have a perfect view of both her and Minami."
            "And I get to watch every twitch and yelp that comes out of them too."
            show threesome breeminami breetongueup
            "It's like we're forming some kind of human chain right now."
            "With me moving in and out of [bree.name] being the start of it."
            show threesome breeminami breetonguemid minamipleasure
            "From there, she takes that energy and passes it on to Minami."
            "Who's the very last link in the chain and helpless to resist!"
            "Sure, I'm panting and sweating, loving every moment of this."
            show threesome breeminami breetonguedown
            "And [bree.name]'s riding my cock like her life depended on it too."
            "But Minami's the one that's just having to take it."
            "She writhes and wriggles on the bed, clawing at the sheets beneath her."
            "The fact that her mouth is free means that she can vocalise all of it too."
            show threesome breeminami breetonguemid minamibreathing
            minami.say "Ah...ah..."
            minami.say "I...I'm gonna..."
            minami.say "[bree.name]...you're gonna make me cum!"
            "Hearing Minami make such a helpless admission is like an adrenaline shot."
            "It makes me grab [bree.name] so tightly that my hands leave marks where I grasp her."
            "And before I know it, I'm pounding her to within an inch of her life!"
            show threesome breeminami breetongueup
            "For some reason I want to shoot my load at the same time Minami cums."
            "Like I'm using [bree.name] as a means to reach her."
            mike.say "Oh shit..."
            mike.say "Here it comes!"
            menu:
                "Cum inside":
                    with hpunch
                    "I make one final thrust forwards, clutching [bree.name] tightly as I do so."
                    "This means that I'm as deep as I can go when it happens."
                    "[bree.name]'s head rears up, tearing her lips away from Minami's pussy."
                    show threesome breeminami breeahegao minamiahegao minamipanting creampie with hpunch
                    "But it hardly matters, as Minami chooses that moment to cum too."
                    with hpunch
                    "[bree.name] joins us a few seconds later as I feel her muscles squeezing my cock."
                    "After that we collapse into a heap of sweaty, tangled limbs."
                    if not CONDOM:
                        $ bree.impregnate()
                    $ bree.love += 2
                    $ minami.love += 1
                "Cum outside":
                    show threesome breeminami -vaginal -anal
                    "I pull back, wrenching my cock out of [bree.name] as I do so."
                    "[bree.name]'s head rears up, tearing her lips away from Minami's pussy."
                    show threesome breeminami breeahegao minamiahegao minamipanting cumshot with hpunch
                    "But it hardly matters, as Minami chooses that moment to cum too."
                    with hpunch
                    "[bree.name] quivers and shakes, clearly cumming too."
                    with hpunch
                    "And all the while I spatter streamers of sticky, white cum over her ass."
                    show threesome breeminami breeahegao minamiahegao minamipanting dickcum -cumshot
                    "After that we collapse into a heap of sweaty, tangled limbs."
                    $ bree.sub += 1
                    $ minami.love += 1
        "Fuck her ass":
            show threesome breeminami breetonguemid
            "Seeing as how [bree.name] is licking Minami's pussy, I decide to take a different route."
            "And so I explore between her buttocks with the head of my cock."
            show threesome breeminami breetongueup
            "[bree.name] pulls her mouth away from Minami's lips for a moment."
            "She lets out a gasp of surprise too, making me move with more haste."
            bree.say "Are you..."
            bree.say "Are you going to fuck my ass?"
            $ bree.sub += 1
            show threesome breeminami breetonguemid mike anal
            "It's at that very moment I push my cock home."
            "[bree.name]'s words turn into a deep moan as I sink into her."
            "And I don't stop until I'm as deep into her ass as I can go."
            show threesome breeminami breetonguedown breepleasure
            "[bree.name]'s surprise only seems to last for a few seconds."
            "And soon enough her head is back between Minami's thighs."
            "I take this as my cue to spring into action."
            show threesome breeminami breetonguemid
            "Which means that I begin thrusting into [bree.name] with all my strength."
            "The whole time that I'm doing it I have a perfect view of both her and Minami."
            "And I get to watch every twitch and yelp that comes out of them too."
            show threesome breeminami breetongueup
            "It's like we're forming some kind of human chain right now."
            "With me moving in and out of [bree.name] being the start of it."
            show threesome breeminami breetonguemid minamipleasure
            "From there, she takes that energy and passes it on to Minami."
            "Who's the very last link in the chain and helpless to resist!"
            "Sure, I'm panting and sweating, loving every moment of this."
            show threesome breeminami breetonguedown
            "And [bree.name]'s riding my cock like her life depended on it too."
            "But Minami's the one that's just having to take it."
            "She writhes and wriggles on the bed, clawing at the sheets beneath her."
            "The fact that her mouth is free means that she can vocalise all of it too."
            show threesome breeminami breetonguemid minamibreathing
            minami.say "Ah...ah..."
            minami.say "I...I'm gonna..."
            minami.say "[bree.name]...you're gonna make me cum!"
            "Hearing Minami make such a helpless admission is like an adrenaline shot."
            "It makes me grab [bree.name] so tightly that my hands leave marks where I grasp her."
            "And before I know it, I'm pounding her to within an inch of her life!"
            show threesome breeminami breetongueup
            "For some reason I want to shoot my load at the same time Minami cums."
            "Like I'm using [bree.name] as a means to reach her."
            mike.say "Oh shit..."
            mike.say "Here it comes!"
            menu:
                "Cum inside":
                    with hpunch
                    "I make one final thrust forwards, clutching [bree.name] tightly as I do so."
                    "This means that I'm as deep as I can go when it happens."
                    "[bree.name]'s head rears up, tearing her lips away from Minami's pussy."
                    show threesome breeminami breeahegao minamiahegao minamipanting creampie with hpunch
                    "But it hardly matters, as Minami chooses that moment to cum too."
                    with hpunch
                    "[bree.name] joins us a few seconds later as I feel her muscles squeezing my cock."
                    "After that we collapse into a heap of sweaty, tangled limbs."
                    $ bree.sub += 1
                    $ minami.love += 1
                "Cum outside":
                    show threesome breeminami -vaginal -anal
                    "I pull back, wrenching my cock out of [bree.name] as I do so."
                    "[bree.name]'s head rears up, tearing her lips away from Minami's pussy."
                    show threesome breeminami breeahegao minamiahegao minamipanting cumshot with hpunch
                    "But it hardly matters, as Minami chooses that moment to cum too."
                    with hpunch
                    "[bree.name] quivers and shakes, clearly cumming too."
                    with hpunch
                    "And all the while I spatter streamers of sticky, white cum over her ass."
                    show threesome breeminami breeahegao minamiahegao minamipanting dickcum -cumshot
                    "After that we collapse into a heap of sweaty, tangled limbs."
                    $ bree.sub += 1
                    $ minami.love += 1
            $ bree.flags.anal += 1
    return

label bree_minami_sandwich:
    "I flip [bree.name] onto her back, and she lands with a muffled thump on the bed."
    hide bree with moveoutbottom
    "She has an endearing look of shock and surprise on her face."
    "And I intend to make use of that confusion before she comes to her senses."
    "I gently pin [bree.name] down on the mattress and call to Minami."
    mike.say "Hey, Minami..."
    mike.say "Get over here!"
    show minami normal blush
    minami.say "O...okay, big bro!"
    "Minami appears at my shoulder and I nod down at [bree.name]."
    mike.say "I don't know if this is your first time with another girl, Minami."
    mike.say "But I think that you should have the honour of going on top!"
    show minami surprised
    "Minami looks at me with genuine surprise written all over her face."
    "But by now, [bree.name]'s shaken off the confusion she was feeling."
    "And she reaches up to take hold of Minami's hands."
    bree.say "Come on, Minami."
    bree.say "Climb aboard already!"
    bree.say "I promise that I'll be gentle..."
    "Minami gives me one last look."
    "And I nod, gently pushing her towards [bree.name]."
    scene sandwich breeminami with fade
    "Minami allows us to guide her until she's straddling [bree.name]'s waist."
    "She looks nervous as hell, until the moment [bree.name] kisses her."
    "It's full on the lips, subtly at first."
    "But the kiss becomes more intense with each second that passes."
    "And it's not just [bree.name] that's getting into it either."
    "Soon enough, Minami is returning the kiss with an equal amount of passion!"
    "All I can do is sit back and watch as they go at it."
    "Not that I mind having a front row seat for something like this!"
    "Part of me could just enjoy the show that they're putting on."
    "See where it takes [bree.name] and Minami and not touch either of them."
    "But this is supposed to be a threesome."
    "If I don't get involved, I might as well just be watching a movie!"
    "That said, I'm not sure just where I should start."
    "Or what I should be sticking in which hole!"
    $ go_on = False
    $ dildo_used = False
    $ bree_ass_filled = False
    $ bree_ass_licked = False
    $ bree_pussy_filled = False
    $ bree_pussy_licked = False
    $ minami_ass_filled = False
    $ minami_ass_licked = False
    $ minami_pussy_filled = False
    $ minami_pussy_licked = False
    while not go_on:
        menu:
            "Lick [bree.name]'s ass" if not bree_ass_licked:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "But I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can lean right on in there with my tongue..."
                "And I can lick all the way around [bree.name]'s butt!"
                show sandwich breeminami lick lickbreeass mike
                "As soon as my tongue touches the sensitive skin, I hear her yelp."
                "Then she starts to giggle as I get down to licking her out."
                "I explore with my tongue, probing as deep into her as I can go."
                "All of which makes her writhe under Minami, unable to escape."
                "Their kiss becomes all the more intense as I double her pleasure."
                "By now I have almost all of my face between her buttocks."
                "And I'm trying to burrow deeper the whole time too!"
                "I can't see a thing, but I can hear the effect my efforts are having."
                show sandwich breeminami -lick -mike
                $ bree.sub += 1
                $ bree_ass_licked = True
            "Lick [bree.name]'s pussy" if not bree_pussy_licked:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "But I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can lean right on in there with my tongue..."
                "And I can lick all the way around [bree.name]'s pussy!"
                show sandwich breeminami lick lickbreepussy mike
                "As soon as my tongue touches the lips and their folds, I hear her yelp."
                "Then she starts to giggle as I get down to licking her out."
                "I explore with my tongue, probing as deep into her as I can go."
                "All of which makes her writhe under Minami, unable to escape."
                "Their kiss becomes all the more intense as I double her pleasure."
                "By now I have almost all of my face between her thighs."
                "And I'm trying to burrow deeper the whole time too!"
                "I can't see a thing, but I can hear the effect my efforts are having."
                show sandwich breeminami -lick -mike
                $ bree.love += 1
                $ bree_pussy_licked = True
            "Lick Minami's ass" if not minami_ass_licked:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "But I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can lean right on in there with my tongue..."
                "And I can lick all the way around Minami's butt!"
                show sandwich breeminami lick lickminamiass mike
                "As soon as my tongue touches the sensitive skin, I hear her yelp."
                "Then she starts to giggle as I get down to licking her out."
                "I explore with my tongue, probing as deep into her as I can go."
                "All of which makes her writhe atop [bree.name], unable to escape."
                "Their kiss becomes all the more intense as I double her pleasure."
                "By now I have almost all of my face between her buttocks."
                "And I'm trying to burrow deeper the whole time too!"
                "I can't see a thing, but I can hear the effect my efforts are having."
                show sandwich breeminami -lick -mike
                $ minami.sub += 1
                $ minami_ass_licked = True
            "Lick Minami's pussy" if not minami_pussy_licked:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "But I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can lean right on in there with my tongue..."
                "And I can lick all the way around Minami's pussy!"
                show sandwich breeminami lick lickminamipussy mike
                "As soon as my tongue touches the lips and their folds, I hear her yelp."
                "Then she starts to giggle as I get down to licking her out."
                "I explore with my tongue, probing as deep into her as I can go."
                "All of which makes her writhe atop [bree.name], unable to escape."
                "Their kiss becomes all the more intense as I double her pleasure."
                "By now I have almost all of my face between her thighs."
                "And I'm trying to burrow deeper the whole time too!"
                "I can't see a thing, but I can hear the effect my efforts are having."
                show sandwich breeminami -lick -mike
                $ minami.love += 1
                $ minami_pussy_licked = True
            "Use anal beads on [bree.name]" if hero.has_item("anal_beads") and not bree_ass_filled:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "In fact, I think I can see both of their buttholes too!"
                "And that reminds me of the anal beads I have under the bed."
                "Quick as a flash, I lean down and pluck them off the floor."
                "I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                show sandwich breeminami beadsbree
                "I can push the first bead into [bree.name]'s ass!"
                "She lets out a muffled yelp of surprise as I shove it in there."
                "But one bead follows another, and she has no choice but to let it happen."
                "Soon enough she's moaning as each one disappears up her ass."
                "And by the time most of them are up there, she's totally surrendered."
                "The end of the string bounces and sways as they go at it."
                "And when I tear it out without warning, it's like pulling a ripcord!"
                $ bree.sub += 2
                $ bree_ass_filled = True
            "Use anal beads on Minami" if hero.has_item("anal_beads") and not minami_ass_filled:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "In fact, I think I can see both of their buttholes too!"
                "And that reminds me of the anal beads I have under the bed."
                "Quick as a flash, I lean down and pluck them off the floor."
                "I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                show sandwich breeminami beadsminami
                "I can push the first bead into Minami's ass!"
                "She lets out a muffled yelp of surprise as I shove it in there."
                "But one bead follows another, and she has no choice but to let it happen."
                "Soon enough she's moaning as each one disappears up her ass."
                "And by the time most of them are up there, she's totally surrendered."
                "The end of the string bounces and sways as they go at it."
                "And when I tear it out without warning, it's like pulling a ripcord!"
                $ minami.sub += 2
                $ minami_ass_filled = True
            "Use double dildo on [bree.name]" if hero.has_item("double_dildo") and not (bree_ass_filled or bree_pussy_filled) and not dildo_used:
                "I take a moment to look at [bree.name]'s butt."
                "It's going up and down like crazy right now!"
                "In fact, I think I can see both of her holes too!"
                "And that reminds me of the double dildo I have under the bed."
                "Quick as a flash, I lean down and pluck it off the floor."
                "I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can push the thing first into [bree.name]'s pussy."
                "And then into her ass too!"
                show sandwich breeminami dildobree
                "She wails and yelps, taken totally by surprise."
                "But there's nothing she can do to resist."
                "Inch by inch, the dildo works its way into her holes."
                "Her and and pussy eagerly swallow it ever deeper."
                "And the effect it's having on her is plain to see."
                "[bree.name]'s pussy and asshole writhe and wriggle."
                "Riding the dildo like it was a living cock."
                $ bree_pussy_filled = True
                $ bree_ass_filled = True
                $ dildo_used = True
                $ bree.sub += 1
                $ bree.love += 1
            "Use double dildo on Minami" if hero.has_item("double_dildo") and not (minami_ass_filled or minami_pussy_filled) and not dildo_used:
                "I take a moment to look at Minami's butt."
                "It's going up and down like crazy right now!"
                "In fact, I think I can see both of her holes too!"
                "And that reminds me of the double dildo I have under the bed."
                "Quick as a flash, I lean down and pluck it off the floor."
                "I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can push the thing first into Minami's pussy."
                "And then into her ass too!"
                show sandwich breeminami dildominami
                "She wails and yelps, taken totally by surprise."
                "But there's nothing she can do to resist."
                "Inch by inch, the dildo works its way into her holes."
                "Her and and pussy eagerly swallow it ever deeper."
                "And the effect it's having on her is plain to see."
                "Minami's pussy and asshole writhe and wriggle."
                "Riding the dildo like it was a living cock."
                $ dildo_used = True
                $ minami_pussy_filled = True
                $ minami_ass_filled = True
                $ minami.sub += 1
                $ minami.love += 1
            "Use double dildo on both girls" if hero.has_item("double_dildo") and not (bree_pussy_filled and minami_pussy_filled) and not dildo_used:
                "I take a moment to look at [bree.name] and Minami's butts."
                "They're going up and down like crazy right now!"
                "In fact, I think I can see both of their pussies too!"
                "And that reminds me of the double dildo I have under the bed."
                "Quick as a flash, I lean down and pluck it off the floor."
                "I think that I can..."
                "If I just get myself into position..."
                "Oh yeah - I knew it!"
                "I can push the thing first into [bree.name]'s pussy."
                "And then into Minami's too!"
                show sandwich breeminami dildodouble
                "They wail and yelp as one, taken totally by surprise."
                "But there's nothing they can do to resist."
                "Inch by inch, the dildo works its way into them."
                "Their pussys eagerly swallow it ever deeper."
                "And the effect it's having on them is plain to see."
                "[bree.name] and Minami's pussys writhe and wriggle."
                "Riding the dildo like it was a living cock."
                $ dildo_used = True
                $ bree_pussy_filled = True
                $ minami_pussy_filled = True
                $ bree.love += 1
                $ minami.love += 1
            "Fuck them":
                $ go_on = True
    menu:
        "Fuck [bree.name]'s pussy" if not bree_pussy_filled:
            "I take a moment to look at [bree.name] and Minami's butts."
            "They're going up and down like crazy right now!"
            "But I think that I can..."
            show sandwich breeminami mike
            "If I just get myself into position..."
            "Oh yeah - I knew it!"
            "Aiming the head of my cock at [bree.name]'s pussy, I go for it."
            call check_condom_usage (bree) from _call_check_condom_usage_50
            if _return == False:
                return
            if CONDOM:
                show sandwich breeminami condom
            "I feel it slide along the slick lips to either side."
            "Then all it takes is for me to give one last push."
            show sandwich breeminami breefuck vaginal
            "And I'm sinking into her."
            "I don't stop until I'm balls deep."
            "Every inch feels amazing."
            show sandwich breeminami breefuck vaginal breepleasure
            "And I can hear [bree.name] moaning in pleasure too!"
            "Without hesitation, I start to thrust in and out of her."
            "My efforts only serve to push [bree.name] harder."
            "And she redoubles her efforts, kissing Minami the whole time."
            $ fuck_choice = "bree_pussy"
        "Fuck [bree.name]'s ass" if not bree_ass_filled:
            "I take a moment to look at [bree.name] and Minami's butts."
            "They're going up and down like crazy right now!"
            "But I think that I can..."
            show sandwich breeminami mike
            "If I just get myself into position..."
            "Oh yeah - I knew it!"
            "Aiming the head of my cock between [bree.name]'s buttocks, I go for it."
            "I feel it slide down the soft crack of her ass."
            "Then all it takes is for me to give one last push."
            show sandwich breeminami breefuck anal
            "And I'm sinking into her."
            "I don't stop until I'm balls deep."
            "Every inch feels amazing."
            show sandwich breeminami breefuck anal breepleasure
            "And I can hear [bree.name] moaning in pleasure too!"
            "Without hesitation, I start to thrust in and out of her."
            "My efforts only serve to push [bree.name] harder."
            "And she redoubles her efforts, kissing Minami the whole time."
            $ fuck_choice = "bree_ass"
        "Fuck Minami's pussy" if not minami_pussy_filled:
            "I take a moment to look at [bree.name] and Minami's butts."
            "They're going up and down like crazy right now!"
            "But I think that I can..."
            show sandwich breeminami mike
            "If I just get myself into position..."
            "Oh yeah - I knew it!"
            "Aiming the head of my cock at Minami's pussy, I go for it."
            call check_condom_usage (minami) from _call_check_condom_usage_51
            if _return == False:
                return
            if CONDOM:
                show sandwich breeminami condom
            "I feel it slide along the slick lips to either side."
            "Then all it takes is for me to give one last push."
            show sandwich breeminami minamifuck vaginal
            "And I'm sinking into her."
            "I don't stop until I'm balls deep."
            "Every inch feels amazing."
            show sandwich breeminami minamifuck vaginal minamipleasure
            "And I can hear Minami moaning in pleasure too!"
            "Without hesitation, I start to thrust in and out of her."
            "My efforts only serve to push Minami harder."
            "And she redoubles her efforts, kissing [bree.name] the whole time."
            $ fuck_choice = "minami_pussy"
        "Fuck Minami's ass" if not minami_ass_filled:
            "I take a moment to look at [bree.name] and Minami's butts."
            "They're going up and down like crazy right now!"
            "But I think that I can..."
            show sandwich breeminami mike
            "If I just get myself into position..."
            "Oh yeah - I knew it!"
            "Aiming the head of my cock between Minami's buttocks, I go for it."
            "I feel it slide down the soft crack of her ass."
            "Then all it takes is for me to give one last push."
            show sandwich breeminami minamifuck anal
            "And I'm sinking into her."
            "I don't stop until I'm balls deep."
            "Every inch feels amazing."
            show sandwich breeminami minamifuck anal minamipleasure
            "And I can hear Minami moaning in pleasure too!"
            "Without hesitation, I start to thrust in and out of her."
            "My efforts only serve to push Minami harder."
            "And she redoubles her efforts, kissing [bree.name] the whole time."
            $ fuck_choice = "minami_ass"
        "Just look":
            $ fuck_choice = "watch"
            pass
    show sandwich breeminami breepleasure minamipleasure
    "There are so many limbs flailing around, it's getting confusing."
    "I'm not sure who's doing what to who right now!"
    "But a moment later, something cuts through the chaos."
    "It's the knowledge that I'm about to cum!"
    "And I need to decide what I'm going to do about it now..."
    menu:
        "Cum in [bree.name]'s ass" if fuck_choice == "bree_ass":
            show sandwich breeminami breefuck anal deep with hpunch
            "I make one final thrust forwards, clutching [bree.name] tightly as I do so."
            with hpunch
            "This means that I'm as deep inside of [bree.name]'s ass as I can go when it happens."
            with hpunch
            "[bree.name]'s head rears up, tearing her lips away from Minami's."
            show sandwich breeminami breefuck anal -deep breeahegao creampie with hpunch
            "But it hardly matters, as Minami chooses that moment to cum too."
            "[bree.name] joins us a few seconds later as I feel her muscles squeezing my cock."
            "After that we collapse into a heap of sweaty, tangled limbs."
            $ bree.sub += 1
            $ minami.love += 1
        "Cum in [bree.name]'s pussy" if fuck_choice == "bree_pussy":
            show sandwich breeminami breefuck vaginal deep with hpunch
            "I make one final thrust forwards, clutching [bree.name] tightly as I do so."
            with hpunch
            "This means that I'm as deep inside of [bree.name]'s pussy as I can go when it happens."
            "[bree.name]'s head rears up, tearing her lips away from Minami's."
            show sandwich breeminami breefuck vaginal -deep breeahegao creampie with hpunch
            "But it hardly matters, as Minami chooses that moment to cum too."
            with hpunch
            "[bree.name] joins us a few seconds later as I feel her muscles squeezing my cock."
            "After that we collapse into a heap of sweaty, tangled limbs."
            if not CONDOM:
                $ bree.impregnate()
            $ bree.love += 2
            $ minami.love += 1
        "Cum in Minami's ass" if fuck_choice == "minami_ass":
            show sandwich breeminami minamifuck anal deep with hpunch
            "I make one final thrust forwards, clutching Minami tightly as I do so."
            with hpunch
            "This means that I'm as deep inside of Minami's ass as I can go when it happens."
            "Minami's head rears up, tearing her lips away from [bree.name]'s."
            show sandwich breeminami minamifuck anal minamiahegao creampie with hpunch
            "But it hardly matters, as [bree.name] chooses that moment to cum too."
            with hpunch
            "Minami joins us a few seconds later as I feel her muscles squeezing my cock."
            show sandwich breeminami dripcum
            "After that we collapse into a heap of sweaty, tangled limbs."
            $ bree.love += 1
            $ minami.sub += 1
        "Cum in Minami's pussy" if fuck_choice == "minami_pussy":
            show sandwich breeminami minamifuck vaginal deep with hpunch
            "I make one final thrust forwards, clutching Minami tightly as I do so."
            with hpunch
            "This means that I'm as deep inside of Minami's pussy as I can go when it happens."
            "Minami's head rears up, tearing her lips away from [bree.name]'s."
            show sandwich breeminami minamifuck anal minamiahegao creampie with hpunch
            "But it hardly matters, as [bree.name] chooses that moment to cum too."
            with hpunch
            "Minami joins us a few seconds later as I feel her muscles squeezing my cock."
            show sandwich breeminami dripcum
            "After that we collapse into a heap of sweaty, tangled limbs."
            if not CONDOM:
                $ minami.impregnate()
            $ bree.love += 1
            $ minami.love += 2
        "Cum outside":
            "I pull back, my cock swaying in the air as I do so."
            show sandwich breeminami outside
            "[bree.name]'s head rears up, tearing her lips away from Minami's."
            "But it hardly matters, as Minami chooses that moment to cum."
            with hpunch
            "[bree.name] quivers and shakes, clearly cumming too."
            show sandwich breeminami cumshot with hpunch
            "And all the while I spatter streamers of sticky, white cum over her ass."
            show sandwich breeminami dickcum cumbody with hpunch
            "After that we collapse into a heap of sweaty, tangled limbs."
            $ bree.love += 1
            $ minami.love += 1
        "Cum on their face":
            "I pull back, my cock swaying in the air as I do so."
            show sandwich breeminami outside
            "[bree.name]'s head rears up, tearing her lips away from Minami's."
            "But it hardly matters, as Minami chooses that moment to cum."
            "[bree.name] quivers and shakes, clearly cumming too."
            show sandwich breeminami cumshot onface with hpunch
            "Both of them have their faces turned towards me as I shoot my load."
            with hpunch
            "Which means that each gets a spattering of hot, white cum across their cheeks."
            show sandwich breeminami dickcum cumshare with hpunch
            "It hits their lips too, but that doesn't stop them exchanging one last kiss."
            show sandwich breeminami -cumshot dickcum cumshare
            "I watch in silent fascination as they lick their tongues snake out."
            "And they lick the cum each other's faces."
            $ bree.sub += 1
            $ minami.sub += 1
    if fuck_choice == "bree_ass":
        $ bree.flags.anal += 1
    if fuck_choice == "minami_ass":
        $ minami.flags.anal += 1
    return

label minami_sasha_threesome_intro:
    $ CONDOM = False
    scene bg bedroom1
    show minami normal at left5
    show sasha normal at right5
    with fade
    "I know that I'm feeling more than a little nervous as we slip into my bedroom and close the door behind us."
    "And what makes it worse is the fact that I was planning on being the one to take Minami by the hand."
    "You know, be the guy that reassured her a threesome was crazy fun and nothing at all to worry about?"
    "But if anything, I'm feeling the exact same way Minami is, judging by the look on her face!"
    "Luckily for the both of us, Sasha seems to be immune to the nerves infecting us."
    show sasha joke
    "She turns and sees that we're looking lost, and instantly cracks a smile."
    sasha.say "Oh no..."
    sasha.say "No way!"
    sasha.say "You two aren't going shy on me, are you?"
    "I can instantly feel my cheeks flush at the accusation."
    "Sasha's question challenges my manhood and makes me feel pretty embarrassed."
    show minami blush
    "And a quick glance in her direction lets me see that Minami's blushing too."
    mike.say "N...no, Sasha!"
    mike.say "No way!"
    mike.say "I was just looking out for Minami, that's all!"
    show minami annoyed
    minami.say "Oh, thanks, big bro!"
    minami.say "Way to throw me under the bus!"
    show sasha happy at startle
    "Sasha lets out a peal of laughter and shakes her head."
    "But I can tell that her laughter isn't cruel in its nature."
    "In fact it's quite warm and affectionate."
    show sasha normal
    sasha.say "Aw, come on you guys!"
    sasha.say "This is supposed to be fun."
    sasha.say "And it IS going to be fun too!"
    show minami surprised
    "Before either of us can say another word, Sasha springs into action."
    show sasha at center, zoomAt(1.25, (740, 900))
    show minami at center, zoomAt(1.25, (480, 900))
    with dissolve
    "She grabs Minami and me by the hand and pulls us towards the bed."
    "We follow, more out of surprise than eagerness."
    "And as soon as we reach our destination, Sasha releases us."
    sasha.say "This is the point where we usually take of our clothes, okay?"
    sasha.say "So I'm gonna do that right now, and you're welcome to join me!"
    show sasha underwear with dissolve
    "Sasha's as good as her word, stripping off her clothes in front of us."
    show sasha naked with dissolve
    "And the sight seems to send a jolt through my entire body and mind."
    "She's right, I'm over-thinking this thing."
    "I need to just go with it."
    "Sasha nods as she sees me start to follow her lead."
    show minami normal underwear with dissolve
    "And a moment later, the same thing happens to Minami."
    show minami naked with dissolve
    "Pretty soon there are items of clothing strewn all across the floor."
    "Enough to ensure that when we're done, everyone's finally naked."
    minami.say "W...wow!"
    show minami blush
    minami.say "You look really good naked, Sasha!"
    sasha.say "You looked in a mirror lately, Minami?"
    sasha.say "Because when I look at you..."
    show sasha flirt
    sasha.say "Wow's what I think too!"
    "I know that I should keep my mouth shut."
    "But part of me can't help opening it."
    "And I swear I'm not in control of what comes out!"
    mike.say "Hey!"
    mike.say "What am I?"
    mike.say "Invisible or something?!?"
    show sasha normal
    show minami normal
    "Minami and Sasha both turn to look at me."
    "And I instantly regret speaking up."
    show sasha flirt
    sasha.say "Oh no - someone's jealous!"
    minami.say "You look good too, big bro!"
    show minami tehe
    minami.say "Of course you do!"
    "I nod and roll my eyes, wanting desperately to move on."
    mike.say "Yeah, yeah, yeah..."
    mike.say "Less talk and more action, right?"
    "At this, Minami and Sasha exchange a meaningful look."
    "Then they both stand before me, waiting to see what I do next..."
    show sasha normal
    show minami normal
    menu:
        "Fuck Minami":
            call minami_sasha_threesome from _call_minami_sasha_threesome
        "I'm up for a sandwich":
            call minami_sasha_sandwich from _call_minami_sasha_sandwich
    "Once it's all over, nobody seems to have the energy or the will to speak."
    "We simply lie there on the bed, a messy tangle of limbs and cooling sweat."
    "But from the smiles I can see on Sasha and Minami's faces, I think everyone is satisfied."
    "I certainly know that I am!"
    $ sasha.sexperience += 1
    $ minami.sexperience += 1
    $ game.pass_time(2)
    return

label minami_sasha_threesome:
    "I instinctively reach out to Minami first of all, wanting to reassure her."
    "And she jumps as soon as my hands grip her around the waist, yelping in surprise."
    show minami surprised
    minami.say "Oh..."
    minami.say "Big bro..."
    minami.say "What are you..."
    "But then she sees the intent in my eyes."
    "And the question dies on her lips."
    "Taking advantage, I guide Minami down onto the bed."
    scene threesome minamisasha with fade
    "I let her get down onto all fours."
    "But I prevent her from actually lying down."
    "All this time, Sasha's been watching my progress."
    "And it's now that she chooses to make her move."
    "Sasha slips between Minami and me, quick as a flash."
    "At first I guess Minami thinks it's me that's behind her."
    "But when she looks over her shoulder, it's Sasha's face she sees!"
    show threesome minamisasha sasha with dissolve
    minami.say "Huh?!?"
    minami.say "Sasha?"
    minami.say "Where'd you come from?"
    sasha.say "Shh!"
    sasha.say "This is going to be a blast!"
    "I roll my eyes as Sasha sets the bar real high for me."
    "But thankfully neither she nor Minami sees me do it."
    "So now all I have to do is live up to their expectations!"
    show threesome minamisasha mike with dissolve
    menu:
        "Fuck Minami":
            "This might sound bad, but Minami's the lower-hanging fruit right now."
            "And from the position she's in, I can fuck her much more easily than Sasha."
            "Plus that means I'm leaving other options open for later!"
            "So I tighten my grip on Minami's haunches and pull her backwards."
            "She lets out another yelp of surprise - or maybe it's anticipation this time?"
            "But I ignore it and thrust my cock firmly between her thighs."
            $ pussy_choice = False
            menu:
                "Fuck her pussy":
                    "I don't want to waste any time and have Minami get an attack of the nerves."
                    "And I also don't want to do something so crazy that it freaks her out either."
                    "Which is why I aim straight for her pussy, keeping things simple."
                    "And the moment I do that, I can't help smiling at what I feel."
                    call check_condom_usage (minami) from _call_check_condom_usage_52
                    if _return == False:
                        return
                    show threesome minamisasha fuckminami vaginal
                    if CONDOM:
                        show threesome minamisasha fuckminami vaginal condom
                    "Minami's lips are already slippery and soft against the head of my cock."
                    "That means for all her nerves, she's still massively turned-on!"
                    "Realising that, I feel myself spurred on in turn."
                    "All it takes is one quick thrust..."
                    "And I feel the head of my cock sink into her!"
                    $ pussy_choice = True
                "Fuck her ass":
                    "I have to be quick if I want to pull off what I have in mind."
                    "And so I waste no time in aiming my cock high and going for it."
                    show threesome minamisasha fuckminami anal
                    "Minami yelps for a third time as I push my way into her ass."
                    "But I don't stop for a moment, ignoring her reaction."
                    "She wriggles and squirms, but that just plays into my hands."
                    "As all Minami manages to do is work herself further into my cock!"
                    "All of a sudden, I feel a change in the sensation around the head."
                    "And then I gasp too as I sink into her ass in one smooth motion."
                    "It's like Minami's body surrenders all at once, her resistance melting away."
            minami.say "Oh..."
            minami.say "Oh, big bro..."
            show threesome minamisasha minamipleasure
            minami.say "You're so...so BIG!"
            "It feels so good to be inside of Minami right now."
            "And the compliments she's giving me are making my head swell too!"
            "So perhaps that's why I don't notice what Sasha's doing at the same time."
            sasha.say "Sure he's big, Minami..."
            sasha.say "Big enough for two!"
            "That's the exact moment I open my eyes and see Sasha's ass."
            "And I don't mean look down and see it either, because it's right there!"
            "Sasha's stretching her legs to make sure her ass is in my face!"
            "Looks like she's not going to miss out on her share of the action."
            "But that doesn't mean I can't choose where she gets it!"
            menu:
                "Lick Sasha's pussy":
                    "I can already see Sasha's pussy between her thighs."
                    "And the moment I catch the scent of it too, my mind's made up."
                    "I lean forwards and stick out my tongue, straining to reach..."
                    show threesome minamisasha licksasha
                    sasha.say "Mmm..."
                    sasha.say "Oh shit..."
                    "I feel the tingle against the tip of my tongue as Sasha moans."
                    "And nothing could make me hold back after that moment."
                    "I push my tongue in deeper still, probing and exploring as I go."
                    "My reward is feeling and hearing the effect it's having on Sasha."
                "Lick Sasha's ass":
                    "I can already see Sasha's tight little asshole between her buttocks."
                    "It looks so neat, perfect and inviting that I can't help myself."
                    "I lean forwards and stick out my tongue, straining to reach..."
                    show threesome minamisasha licksasha
                    sasha.say "Mmm..."
                    sasha.say "Oh shit..."
                    "I feel the tingle of Sasha's muscles against the tip of my tongue as she moans."
                    "And nothing could make me hold back after that moment."
                    "I push my tongue in deeper still, probing and exploring as I go."
                    "My reward is feeling and hearing the effect it's having on Sasha."
            show threesome minamisasha minaminormal
            minami.say "What about me, big bro?"
            minami.say "Don't forget about me!"
            "I realise that I've started to slow down on Minami while Sasha had me distracted."
            "And so I redouble my efforts while still trying to keep both girls satisfied."
            "Minami's body eats up everything that I have to give."
            "But it's still hungry for more no matter how hard I fuck her."
            show threesome minamisasha sashapleasure
            "At the same time, Sasha's making similar demands of my tongue."
            "Both of them are panting, slick with perspiration."
            "Which means it's getting harder to hold onto them too!"
            show threesome minamisasha minamipleasure
            minami.say "Don't stop now, big bro!"
            minami.say "I...I'm gonna cum!"
            sasha.say "Ah...me..."
            sasha.say "Me too!"
            "Those words come as a blessed relief, almost a mercy."
            "And I can already feel a barrier breaking inside of me."
            "Without warning, I pull my lips away from Sasha."
            "And then I cling onto Minami for dear life!"
            menu:
                "Cum inside":
                    with hpunch
                    "I'm thrusting into her so hard by now that I can't stop before it's too late!"
                    with hpunch
                    "And the moment that I start to shoot my load into Minami, Sasha loses her balance."
                    show threesome minamisasha creampie with hpunch
                    if pussy_choice and not CONDOM:
                        $ minami.impregnate()
                    "She tumbles forwards, almost doing a cartwheel onto the bed."
                    sasha.say "Wh...whoa!"
                    "All this happens as I fill Minami with all that I have."
                    minami.say "Ah...ah..."
                    show threesome minamisasha minamiahegao
                    minami.say "Oh...oh, big bro!"
                    minami.say "I love it when you cum inside me!"
                "Pull out":
                    "I have to pull out right now, or else it'll be too late!"
                    "But the moment I do, Sasha loses her balance."
                    "She tumbles forwards, almost doing a cartwheel onto the bed."
                    sasha.say "Wh...whoa!"
                    show threesome minamisasha cumshot -vaginal -anal with hpunch
                    "All this happens as I shoot my load over Minami's ass."
                    with hpunch
                    "She gasps as the hot cum paints her buttocks with sticky, white stripes."
                    with hpunch
                    "But then she looks back at me over her shoulder, giggling wickedly."
                    minami.say "Oh, big bro!"
                    minami.say "Look what a mess you made of me!"
            if not pussy_choice:
                $ minami.flags.anal += 1
        "Fuck Sasha instead":
            "Part of me feels like I should be putting Sasha in her place by fucking Minami instead."
            "After all, she's the least experienced of us when it comes to stuff like this."
            "But then maybe letting Sasha take the lead is just what Minami needs?"
            "You know, the more confident girl showing her the way?"
            "I take my hands off of Minami and instead grab hold of Sasha."
            show threesome minamisasha fucksasha vaginal
            "This earns me a gasp of surprise and maybe even disappointment from the former."
            "But it makes the latter nod eagerly, showing her ass against my groin."
            "I don't waste any time in making sure Sasha's right where I want her."
            "And then I aim my cock straight between her thighs..."
            $ pussy_choice = False
            menu:
                "Fuck her pussy":
                    "With Sasha pressing herself into me so hard, it's tricky to get things to go where I want them."
                    "So in the end, my cock finds its way to her pussy almost by accident."
                    call check_condom_usage (sasha) from _call_check_condom_usage_53
                    if _return == False:
                        return
                    show threesome minamisasha fucksasha vaginal
                    if CONDOM:
                        show threesome minamisasha fucksasha vaginal condom
                    "She's already more than willing, her lips wet and slippery."
                    "Meaning that the head's in there before I know it."
                    "Sasha moans and I swear she actually purrs too as it slides into her."
                    "And the feeling is pretty sensational from my side of things too!"
                    "I don't stop pushing until I can't go any deeper."
                    "Sasha's pussy swallowing me without any hint of hesitation."
                    $ pussy_choice = True
                "Fuck her ass":
                    "With Sasha pressing herself into me so hard, I have to make sure I end up where I want to be."
                    "Which is why I make the instant decision to go for the nearest and easiest target."
                    "So I aim higher than usual, right for that sweet spot hidden between her buttocks."
                    show threesome minamisasha fucksasha anal
                    sasha.say "Wha..."
                    sasha.say "Where are you..."
                    sasha.say "Oh fuck!"
                    "The muscles of Sasha's ass try their best to resist me."
                    "But I have gravity on my side."
                    "Well, that and the fact Sasha's a pretty dirty little bitch too!"
                    "Soon enough her muscles give up the fight, and she sinks slowly down onto my cock."
            sasha.say "Mmm..."
            sasha.say "That feels SO good!"
            sasha.say "Don't stop now, [hero.name]!"
            show threesome minamisasha sashapleasure
            "It's not like I need any encouragement!"
            "And I'm already starting to thrust in and out of Sasha with serious intent."
            "So all her words do is make me more determined to fuck her harder than ever!"
            "It feels so good to be inside of Sasha that I forget about everything else."
            "All that matters is the sensation of my cock as it moves back and forth."
            "That and the way she's moving beneath me, her body reacting to my motions."
            "It's only when I open my eyes for the first time that I remember something."
            "Sasha and I aren't alone in this act."
            "There's Minami, staring up at me in wide-eyed amazement!"
            "For a moment my pleasure is replaced by a feeling of guilt."
            "This is supposed to be a threesome."
            "And here I am just having my way with Sasha."
            "Sure, that's great for the two of us - but what about Minami?"
            mike.say "Ah..."
            mike.say "Minami, I..."
            minami.say "Oh..."
            minami.say "Oh, big bro..."
            minami.say "You're so...so BIG!"
            "I blink and shake my head, not quite believing my ears."
            "But the look in Minami's eyes is totally sincere."
            "She's watching me fuck Sasha, and she's enjoying it too!"
            "Minami must have read the amazement I'm feeling on my face."
            "Because a moment later she seems to become intent on doing all she can to help out."
            "Without being asked to do a thing, she begins to rub her head against Sasha's chest."
            "This isn't hard for her to pull off, as the other girl's breasts are right on top of it!"
            "Almost nestling her head between them, Minami opens her mouth and licks her lips."
            "And then she licks at one of Sasha's nipples, exploring it with her tongue."
            "The effect is instant, so strong that I feel it too."
            "Sasha's muscles squeeze my cock as she reacts to Minami's attentions."
            "I can't help gasping and panting as the sensation grips me."
            "And my own motions become more intense as a result."
            "Before I know it, I'm pounding away at Sasha like my life depends on it."
            sasha.say "Ah..."
            sasha.say "I..."
            sasha.say "I'm gonna cum!"
            "If I still had the power of speech, I'd have said 'me too'."
            "But I don't, so there's no chance to warn Sasha of what's about to happen..."
            menu:
                "Cum inside":
                    "There's no way I can hope to pull out before I lose it."
                    with hpunch
                    "And so I just hold onto Sasha as I feel myself cumming."
                    show threesome minamisasha creampie with hpunch
                    if pussy_choice and not CONDOM:
                        $ sasha.impregnate()
                    "Her climax seems to take her at almost the exact same moment."
                    show threesome minamisasha sashaahegao with hpunch
                    "And for a second it's like we're frozen in time."
                    "But then I feel her go limp in my grasp."
                    "Sasha collapses onto the bed and I go down with her."
                    "All of which means we both land on top of Minami!"
                "Pull out":
                    "Somehow I manage to use the last of my strength to pull out."
                    with hpunch
                    "The sensation of be doing so seems to be the last straw for Sasha."
                    show threesome minamisasha cumshot -vaginal -anal with hpunch
                    "She cums as I shoot my load over her slick, slippery ass."
                    show threesome minamisasha sashaahegao with hpunch
                    "And for a second it's like we're frozen in time."
                    "But then I feel her go limp in my grasp."
                    "Sasha collapses onto the bed and I go down with her."
                    "All of which means we both land on top of Minami!"
            if not pussy_choice:
                $ sasha.flags.anal += 1
    return

label minami_sasha_sandwich:
    "I didn't think I'd left it that long, just long enough to catch my breath."
    "But apparently Sasha isn't going to wait and see what I have in mind."
    "Instead she takes matters into her own hands, pushing Minami down onto the bed."
    "Minami looks at me for a moment, as if expecting me to intervene."
    "But all this gets her is a shrug and a smile."
    "If Sasha wants to take the lead, then I'm happy to let her!"
    "And Sasha seems to pick up on that too, as she eyes me sideways."
    "The look of amusement and impish delight on her face is plain to see."
    "Which makes me all the more interested in where this is going!"
    scene sandwich minamisasha with fade
    "Soon enough, Minami's on her back, and Sasha's laid on top of her."
    "The contrast between the former's innocence and the latter's confidence is plain to see."
    "And it's making my cock painfully hard as I watch them!"
    minami.say "Oooh..."
    minami.say "Sasha..."
    minami.say "What are you going to do to me?"
    "Sasha stops Minami's questions with her lips."
    "She kisses the other girl passionately and without restraint."
    "But at the same time she makes sure that she's holding my gaze."
    "And I know that this is an open invitation to get involved too!"
    "The only question is where am I going to do that?"
    "Minami's helpless as Sasha overwhelms her."
    "But Sasha's likewise wide open to whatever I can come up with."
    "All I have to do is decide where I go and what I do..."
    $ go_on = False
    $ minami_ass_filled = False
    $ minami_ass_licked = False
    $ minami_pussy_licked = False
    $ minami_pussy_filled = False
    $ sasha_ass_filled = False
    $ sasha_ass_licked = False
    $ sasha_pussy_licked = False
    $ sasha_pussy_filled = False
    while not go_on:
        menu:
            "Lick Sasha's ass" if not sasha_ass_licked:
                "Sasha's left herself so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "All it takes is a couple of seconds for me to get into position."
                "And then I grab Sasha by the haunches, leaning forwards at the same time."
                "There's just time for her to let out a yelp of surprise."
                show sandwich minamisasha mike lickasssasha
                "Then my tongue slides between her buttocks."
                "Sasha's ass is tight, neat and just begging to be licked."
                "I explore it with the tip, then push in deeper still."
                show sandwich minamisasha sashapleasure
                "Sasha moans as I try to get into her as deep as I can go."
                "The sound muffled as she continues to kiss Minami."
                "And now there's nothing that's going to hold me back!"
                "My face is practically buried between Sasha's buttocks."
                "All I can think about is the task at hand."
                show sandwich minamisasha -lickasssasha -mike
                $ sasha.sub += 1
                $ sasha_ass_licked = True
            "Lick Sasha's pussy" if not sasha_pussy_licked:
                "Sasha's left herself so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "All it takes is a couple of seconds for me to get into position."
                "And then I grab Sasha by the haunches, leaning forwards at the same time."
                "There's just time for her to let out a yelp of surprise."
                "Then my tongue slides between her thighs."
                show sandwich minamisasha mike lickpussysasha
                "Sasha's pussy is tight, neat and just begging to be licked."
                "She's already as wet as hell, and the taste in my mouth is amazing."
                "I explore her lips the tip, then push in deeper still."
                show sandwich minamisasha sashapleasure
                "Sasha moans as I try to get into her as deep as I can go."
                "The sound muffled as she continues to kiss Minami."
                "And now there's nothing that's going to hold me back!"
                "My face is practically buried between Sasha's thighs."
                "All I can think about is the task at hand."
                show sandwich minamisasha -lickpussysasha -mike
                $ sasha.love += 1
                $ sasha_pussy_licked = True
            "Lick Minami's ass" if not minami_ass_licked:
                "Sasha's left Minami so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "All it takes is a couple of seconds for me to get into position."
                "And then I grab Minami by the haunches, leaning forwards at the same time."
                "There's just time for her to let out a yelp of surprise."
                "Then my tongue slides between her buttocks."
                show sandwich minamisasha mike lickassminami
                "Minami's ass is tight, neat and just begging to be licked."
                "I explore it with the tip, then push in deeper still."
                "Minami moans as I try to get into her as deep as I can go."
                show sandwich minamisasha minamipleasure
                "The sound muffled as Sasha continues to kiss her."
                "And now there's nothing that's going to hold me back!"
                "My face is practically buried between Minami's buttocks."
                "All I can think about is the task at hand."
                show sandwich minamisasha -lickassminami -mike
                $ minami.sub += 1
                $ minami_ass_licked = True
            "Lick Minami's pussy" if not minami_pussy_licked:
                "Sasha's left Minami so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "All it takes is a couple of seconds for me to get into position."
                "And then I grab Minami by the haunches, leaning forwards at the same time."
                "There's just time for her to let out a yelp of surprise."
                "Then my tongue slides between her thighs."
                show sandwich minamisasha mike lickpussyminami
                "Minami's pussy is tight, neat and just begging to be licked."
                "She's already as wet as hell, and the taste in my mouth is amazing."
                "I explore her lips the tip, then push in deeper still."
                "Minami moans as I try to get into her as deep as I can go."
                show sandwich minamisasha minamipleasure
                "The sound muffled as she Sasha continues to kiss her."
                "And now there's nothing that's going to hold me back!"
                "My face is practically buried between Minami's thighs."
                "All I can think about is the task at hand."
                show sandwich minamisasha -lickpussyminami -mike
                $ minami.love += 1
                $ minami_pussy_licked = True
            "Use anal beads on Sasha" if hero.has_item("anal_beads") and not sasha_ass_filled:
                "Sasha's left herself so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "I can see her butthole and Minami's without even having to try."
                "And that reminds me of the anal beads I have under the bed."
                "Quick as a flash, I lean down and pluck them off the floor."
                "From there it's just a matter of picking my moment..."
                "And I push the first of the beads into Sasha's ass."
                show sandwich minamisasha sashabeads
                "She moans at the sensation, but doesn't stop for a moment."
                "Take this as a good sign, hurrying to push more of the beads in."
                "Soon enough the whole string is up there."
                show sandwich minamisasha sashapleasure
                "And then all I have to do is wait for the right moment."
                $ sasha.sub += 2
                $ sasha_ass_filled = True
            "Use anal beads on Minami" if hero.has_item("anal_beads") and not minami_ass_filled:
                "Sasha's left Minami so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "I can see her butthole and Minami's without even having to try."
                "And that reminds me of the anal beads I have under the bed."
                "Quick as a flash, I lean down and pluck them off the floor."
                "From there it's just a matter of picking my moment..."
                "And I push the first of the beads into Minami's ass."
                show sandwich minamisasha minamibeads
                "She moans at the sensation, but doesn't stop for a moment."
                "Take this as a good sign, hurrying to push more of the beads in."
                "Soon enough the whole string is up there."
                "And then all I have to do is wait for the right moment."
                "When I'm sure that Sasha and Minami are about to cum, I make my move."
                "Giving the end of the string a firm tug, I yank it out of Minami's ass."
                show sandwich minamisasha minamipleasure
                "The effect is instant and impressive, setting her off straight away."
                "Like an unstoppable avalanche, Minami loses it."
                $ minami.sub += 2
                $ minami_ass_filled = True
            "Use double dildo on both girls" if hero.has_item("double_dildo") and not (sasha_pussy_filled or minami_pussy_filled):
                "Sasha's left herself so wide open that she must want me to take advantage."
                "She's practically waving her ass in the air right in front of me!"
                "I can see her pussy and Minami's without even having to try."
                "And that reminds me of the double dildo I have under the bed."
                "Quick as a flash, I lean down and pluck them off the floor."
                "From there it's just a matter of picking my moment..."
                "And I push the thing into Sasha's pussy."
                "She moans at the sensation, but doesn't stop for a moment."
                show sandwich minamisasha dildo
                "Then I take the other end of the dildo and do the same to Minami."
                "Her reaction is pretty much the same, moans of pleasure as I get to work."
                "And her pussy swallows the thing with as much enthusiasm as Sasha's."
                "Inch by inch, the dildo works its way into them."
                "Their pussys eagerly swallow it ever deeper."
                "And the effect it's having on them is plain to see."
                show sandwich minamisasha minamipleasure sashapleasure
                "Sasha and Minami's pussys writhe and wriggle."
                "Riding the dildo like it was a living cock."
                $ sasha_pussy_filled = True
                $ minami_pussy_filled = True
                $ sasha.love += 1
                $ minami.love += 1
            "Fuck them":
                $ go_on = True
    menu:
        "Fuck Sasha's pussy" if not sasha_pussy_filled:
            "Sasha's left herself so wide open that she must want me to take advantage."
            "She's practically waving her ass in the air right in front of me!"
            "So is it any wonder that I point the head of my cock right between her thighs?"
            show sandwich minamisasha mike fucksasha
            "All it takes is a couple of seconds for me to get into position."
            "And then I grab Sasha by the haunches, thrusting forwards at the same time."
            "There's just time for her to let out a yelp of surprise."
            "Then my cock slides along the length of her pussy."
            "The lips are already slick and slippery."
            "And it's almost like her pussy is sucking me in!"
            "Seriously, all I have to do is rub the head against it."
            call check_condom_usage (sasha) from _call_check_condom_usage_54
            if _return == False:
                return
            if CONDOM:
                show sandwich minamisasha condom
            "The next thing I know it's already in there and going deeper by the second!"
            show sandwich minamisasha fucksasha vaginal
            "I feel like I couldn't stop it, even if I wanted to!"
            "It's like I'm just being swept along, powerless to resist."
            "Sasha moans as I sink into her as deep as I can go."
            show sandwich minamisasha sashapleasure
            "The sound muffled as she continues to kiss Minami."
            "And now there's nothing that's going to hold me back!"
            $ fuck_choice = "sasha_pussy"
        "Fuck Sasha's ass" if not sasha_ass_filled:
            "Sasha's left herself so wide open that she must want me to take advantage."
            "She's practically waving her ass in the air right in front of me!"
            "So is it any wonder that I point the head of my cock right between her thighs?"
            "All it takes is a couple of seconds for me to get into position."
            show sandwich minamisasha mike fucksasha
            "And then I grab Sasha by the haunches, thrusting forwards at the same time."
            "There's just time for her to let out a yelp of surprise."
            "Then my cock slips neatly between her buttocks."
            "I easily find her tight, enticing little ass."
            "But then it feels like she's the one pulling me in!"
            "I'm expecting the usual resistance before her muscles surrender."
            show sandwich minamisasha fucksasha anal
            "But I'm already in there and going deeper by the second!"
            "I feel like I couldn't stop it, even if I wanted to!"
            "It's like I'm just being swept along, powerless to resist."
            show sandwich minamisasha sashapleasure
            "Sasha moans as I sink into her as deep as I can go."
            "The sound muffled as she continues to kiss Minami."
            "And now there's nothing that's going to hold me back!"
            $ fuck_choice = "sasha_ass"
        "Fuck Minami's pussy" if not minami_pussy_filled:
            "Sasha's put Minami in such a precarious position that she must want me to take advantage."
            "She's practically waving her ass right in front of my face!"
            "So is it any wonder that I point the head of my cock right between Minami's thighs?"
            show sandwich minamisasha mike fuckminami
            "All it takes is a couple of seconds for me to get into position."
            "And then I grab Minami by the haunches, thrusting forwards at the same time."
            "There's just time for her to let out a yelp of surprise."
            "Then my cock slides along the length of her pussy."
            "The lips are already slick and slippery."
            "And it's almost like her pussy is sucking me in!"
            "Seriously, all I have to do is rub the head against it."
            call check_condom_usage (minami) from _call_check_condom_usage_55
            if _return == False:
                return
            if CONDOM:
                show sandwich minamisasha condom
            "The next thing I know it's already in there and going deeper by the second!"
            show sandwich minamisasha fuckminami vaginal
            "I feel like I couldn't stop it, even if I wanted to!"
            "It's like I'm just being swept along, powerless to resist."
            "Minami moans as I sink into her as deep as I can go."
            show sandwich minamisasha minamipleasure
            "The sound muffled as Sasha continues to kiss her."
            "And now there's nothing that's going to hold me back!"
            $ fuck_choice = "minami_pussy"
        "Fuck Minami's ass" if not minami_ass_filled:
            "Sasha's put Minami in such a precarious position that she must want me to take advantage."
            "She's practically waving her ass right in front of my face!"
            "So is it any wonder that I point the head of my cock right between Minami's thighs?"
            show sandwich minamisasha mike fuckminami
            "All it takes is a couple of seconds for me to get into position."
            "And then I grab Minami by the haunches, thrusting forwards at the same time."
            "There's just time for her to let out a yelp of surprise."
            "Then my cock slips neatly between her buttocks."
            "I easily find her tight, enticing little ass."
            "But then it feels like she's the one pulling me in!"
            "I'm expecting the usual resistance before her muscles surrender."
            show sandwich minamisasha fuckminami anal
            "But I'm already in there and going deeper by the second!"
            "I feel like I couldn't stop it, even if I wanted to!"
            "It's like I'm just being swept along, powerless to resist."
            show sandwich minamisasha minamipleasure
            "Minami moans as I sink into her as deep as I can go."
            "The sound muffled as Sasha continues to kiss her."
            "And now there's nothing that's going to hold me back!"
            $ fuck_choice = "minami_ass"
        "Just look":
            $ fuck_choice = "watch"
            "The girls works on each other in a way I never imagined."
            show sandwich minamisasha mike stroke
            "So I decide to just watch the show."
            pass

    show sandwich minamisasha minamipleasure sashapleasure
    "I can't keep this pace up for much longer, not unless I want to pass out!"
    "I'm on the brink of cumming, ready to shoot my load and collapse."
    "But the problem is that I don't know where I should do it."
    "There's literally two of everything involved here - in come cases three!"
    "All I know is that I have to make a decision fast, before it's too late!"
    menu:
        "Cum in Sasha's ass" if fuck_choice == "sasha_ass":
            "I decide that the plan here is not to go anywhere."
            with hpunch
            "So I keep right on pounding away at Sasha until the very end."
            with hpunch
            "This means that my cock is as deep inside of her as it'll go when I finally cum."
            show sandwich minamisasha fucksasha anal sashaahegao creampie with hpunch
            "Sasha cries out as I fill her ass, wriggling and writhing on my cock."
            "And for a second it's like we're frozen in time."
            "But then I feel her go limp in my grasp."
            "Sasha collapses onto the bed and I go down with her."
            "All of which means we both land on top of Minami!"
            $ sasha.sub += 1
            $ minami.love += 1
        "Cum in Sasha's pussy" if fuck_choice == "sasha_pussy":
            "I decide that the plan here is not to go anywhere."
            with hpunch
            "So I keep right on pounding away at Sasha until the very end."
            with hpunch
            "This means that my cock is as deep inside of her as it'll go when I finally cum."
            show sandwich minamisasha fucksasha vaginal sashaahegao creampie with hpunch
            "Sasha cries out as I fill her pussy, wriggling and writhing on my cock."
            "And for a second it's like we're frozen in time."
            "But then I feel her go limp in my grasp."
            "Sasha collapses onto the bed and I go down with her."
            "All of which means we both land on top of Minami!"
            $ sasha.love += 2
            $ minami.love += 1
        "Cum in Minami's ass" if fuck_choice == "minami_ass":
            "I decide that the plan here is not to go anywhere."
            with hpunch
            "So I keep right on pounding away at Minami until the very end."
            with hpunch
            "This means that my cock is as deep inside of her as it'll go when I finally cum."
            show sandwich minamisasha fuckminami vaginal minamiahegao creampie with hpunch
            "Minami cries out as I fill her ass, wriggling and writhing on my cock."
            "And for a second it's like we're frozen in time."
            "But then I feel her go limp in my grasp."
            "I collapse onto the bed at the same time, trapping Sasha between us!"
            $ sasha.love += 1
            $ minami.sub += 1
        "Cum in Minami's pussy" if fuck_choice == "minami_pussy":
            "I decide that the plan here is not to go anywhere."
            with hpunch
            "So I keep right on pounding away at Minami until the very end."
            with hpunch
            "This means that my cock is as deep inside of her as it'll go when I finally cum."
            show sandwich minamisasha fuckminami vaginal minamiahegao creampie with hpunch
            "Minami cries out as I fill her pussy, wriggling and writhing on my cock."
            "And for a second it's like we're frozen in time."
            "But then I feel her go limp in my grasp."
            "I collapse onto the bed at the same time, trapping Sasha between us!"
            $ sasha.love += 1
            $ minami.love += 2
        "Cum outside" if fuck_choice != "watch":
            "Somehow I manage to use the last of my strength to pull out."
            show sandwich minamisasha out
            "The sensation of be doing so seems to be the last straw for Sasha and Minami."
            show sandwich minamisasha cumshot with hpunch
            "They both begin to cum as I shoot my load over their slick, slippery bodies."
            with hpunch
            "I kneel over them, gasping for breath as it happens."
            show sandwich minamisasha bodycum with hpunch
            "And so I have the perfect view of them being painted with sticky, white stripes."
            $ sasha.love += 1
            $ minami.love += 1
        "Cum on their faces" if fuck_choice == "watch":
            "When I'm sure that Sasha and Minami are about to cum, I make my move."
            show sandwich minamisasha wank
            "They both begin to cum as I shoot my load over their slick, slippery bodies."
            "I kneel over them, gasping for breath as it happens."
            show sandwich minamisasha wank cumshot with hpunch
            "But quick as a flash they're up and grabbing hold of my cock."
            show sandwich minamisasha wank facecum with hpunch
            "I watch as their faces are painted with sticky, white stripes."
            "They smile and giggle as they lick the cum off their lips."
            "And then Sasha kisses Minami, who returns the gesture, tongues darting this way and that."
            "Cum mingles on their lips, and slips into their open mouths the whole time."
            $ sasha.sub += 1
            $ minami.sub += 1
    if fuck_choice == "minami_ass":
        $ minami.flags.anal += 1
    if fuck_choice == "sasha_ass":
        $ sasha.flags.anal += 1
    return

label foursome_bree_minami_sasha_intro:
    scene secondfloor
    show minami casual
    with fade
    "It's weird to admit as much, but I almost feel as nervous as Minami looks as I lead her towards Sasha's bedroom."
    "I mean, I know that I'm the one that's already a part of the thing that she's about to get into too."
    "But it's not like I had to do this myself when [bree.name], Sasha and I started doing this."
    "We were all new to it, and so we had to get over the issues and hang-ups that we had together."
    "The flipside of that was nobody had any more experience than the other two."
    "And so we all kind of helped to pull each other up and became that much stronger as a result."
    "Still, I'm feeling the nerves that Minami's giving off, and I can sympathise with her."
    "Sasha hasn't been all that open with me about what she's got planned."
    "Or for that matter why she insisted on it being in her room either."
    "So we're almost on the same level when it comes to knowing what we can expect when we get in there."
    "Reaching the door, I pause with my hand hovering above the handle."
    mike.say "Whatever happens, Minami, don't worry."
    mike.say "I'll be right there, looking out for you."
    show minami blush
    "Minami looks up at this, a smile on her face."
    "But I can see that she's still a little scared."
    minami.say "Thanks, big bro."
    minami.say "But I'll be fine - I promise!"
    "I offer her a nod in way of an answer."
    scene bg bedroom3 with fade
    "And then I open the door and walk into Sasha's bedroom."
    show minami casual with moveinleft
    sasha.say "Hey guys, what took you so long?"
    "Neither Minami nor I can actually manage to utter a response to the question."
    "The reason might have seemed to be that we just walked in on Sasha while she's totally naked."
    "But seriously, we're here for something that pretty much needs her to be in a state of total undress."
    "No, what stops the pair of us in our tracks is when Sasha turns around."
    show sasha strapon at right with dissolve
    show minami surprised at startle
    "Revealing for the first time that she is wearing something after all..."
    sasha.say "What's the matter?"
    sasha.say "You never seen a girl wearing a strap-on before?"
    show minami scared
    minami.say "Is...is she...going to use...that?"
    minami.say "On me?!?"
    show sasha joke
    sasha.say "Aww, don't be scared, Minami."
    sasha.say "It won't hurt all that much, I promise!"
    sasha.say "And if you don't believe me, ask [hero.name] here..."
    "Minami's eyes go wide at this."
    "She looks at me as though she's about to ask the dreaded question."
    show bree at left with moveinleft
    "But then the door bursts open, and [bree.name] strolls straight in."
    "And stops dead as she sees the scene playing out before her."
    show bree evil
    bree.say "Ooh, Sasha - what a big cock you have!"
    show sasha happy
    sasha.say "All the better to bang you with, my dear!"
    show bree happy at startle
    show sasha at startle
    "They both laugh, until Minami lets out a yelp of fear."
    show bree normal
    "[bree.name] turns to regard her, genuine concern in her expression as she does so."
    bree.say "Oh, Minami, I'm sorry."
    bree.say "I'm just so used to that thing by now, it doesn't bother me."
    bree.say "But it scared the hell out of me at first too."
    bree.say "Trust me though, there's nothing to be scared about."
    bree.say "[hero.name] and I will keep you safe from the Big Bad Sasha."
    "[bree.name]'s assurances are met with a peal of laughter from Sasha and another yelp from Minami."
    "Not wanting this thing to go south before it even gets started, I take this as my cue to step in."
    mike.say "[bree.name]'s right Minami - she's just screwing with you."
    mike.say "Aren't you, Sasha?"
    "For a moment, I actually think that she's going to go the other way."
    show sasha normal
    "But then Sasha shakes her head in amusement."
    sasha.say "Sure, of course I am."
    show bree at left5 with ease
    "[bree.name] leans in close to Minami, a bright and breezy smile on her face."
    bree.say "See, Minami - nothing to be afraid of!"
    show minami at startle
    "Minami nods, but then jumps a little as she finds [bree.name]'s hands upon her."
    show minami normal underwear norobe topless with dissolve
    "The other girl begins to undo and strip off her clothes, and I see Minami make to object."
    "But then she takes a deep breath, seemingly steeling herself for what lies ahead."
    show bree underwear with dissolve
    "And she smiles right back as she starts to return the favour for [bree.name]."
    "All the time I'm watching this in fascination, while slowly getting undressed myself."
    "It's only when I actually have my shorts off that I realise how hard it's already making me."
    show minami naked
    show bree naked
    with dissolve
    "What with Sasha already naked as well as [bree.name] and Minami soon to join her."
    "I hardly know where to look for fear of missing a glimpse of their amazing bodies."
    sasha.say "We were talking before, [bree.name] and myself."
    sasha.say "And we think you need something familiar to start with."
    bree.say "Yeah, Minami."
    bree.say "That's why we're gonna let you have dibs on [hero.name]'s cock this time."
    bree.say "I'd tell you it's a sweet ride."
    bree.say "But you already know that, right!"
    show minami blush
    "Minami blushes at this, and I can feel my cheeks flushing a little too."
    "Suddenly I feel the need to step up and be heard, not treated like an object here!"
    mike.say "I'm fine with that, as long as you are, Minami."
    mike.say "So, what do you say?"
    "Minami nods as she takes hold of my hand."
    minami.say "Sure thing, big bro."
    minami.say "I know I'm safe with you!"
    call foursome_bree_minami_sasha from _call_foursome_bree_minami_sasha_3
    call sleep (["bree", "minami", "sasha"]) from _call_sleep_foursome_bree_minami_sasha
    return

label foursome_bree_minami_sasha:
    scene foursome breeminamisasha with fade
    "And with that, she takes me by surprise, almost leaping into my arms and wrapping her legs around me."
    "I can hear equally amazed sounds coming from [bree.name] and Sasha as they rush to get involved too."
    "It's all that I can do to catch and hold Minami, staggering backwards until I hit the wall."
    "Already she has her lips pressed against mine, almost forcing her tongue down my throat."
    "But then I remember the nervous state she was in."
    "And I realise that she's clinging to something she knows, something she can trust."
    "It's then that I begin to return Minami's attentions with a similar vigour."
    "I hug her to me, pressing her petite breasts against my chest and kissing her back."
    "She wriggles her backside, and the head of my cock rubs against her lips."
    "For all that she was unsure, Minami's already getting nice and slick down there."
    "And so it's only a matter of moments before she scrabbles onto my dick."
    "As she lets herself sink down onto it, Minami breaks the kiss and leans her head on my shoulder."
    minami.say "Oh..."
    minami.say "Oh, big bro..."
    minami.say "You feel so right inside of me..."
    bree.say "Aww, that's so sweet!"
    bree.say "I can't believe I ever thought you two fucking would be icky!"
    sasha.say "Forget sweet, [bree.name] - this is hot as hell!"
    sasha.say "This is making me want to be fucked like that too!"
    sasha.say "Speaking of which..."
    "I can hear a distinct hint of mischief creeping into Sasha's tone as she says this."
    "And then there's the feeling of Minami being pulled down just a little lower than before."
    minami.say "Ah...oh no!"
    minami.say "Big bro...she's...she's putting it up..."
    minami.say "Up my ass!"
    "I glance over Minami's shoulder, seeing instantly that she's right."
    "Sasha's leaning in from behind her, already easing the dildo strapped to her waist into Minami's butt."
    "I feel Minami tense, the firm muscles of her pussy squeezing my cock inside of her."
    "Another time I might have sympathised with her and told Sasha to back off."
    "But the way her trepidation is being translated into sensations for me right now..."
    "All I want is for Sasha to go even further, maybe even all the way!"
    mike.say "It's...it's okay, Minami."
    mike.say "Trust me, Sasha knows what she's doing."
    minami.say "Ooh...big bro..."
    minami.say "I can feel it in me!"
    minami.say "It's...oh...oh shit!"
    show foursome breeminamisasha sashaevil
    "By now, Sasha has the dildo so far up Minami's ass that she loses the power of speech."
    "All that she can do is let her head drop back onto my shoulder."
    "She lets out short, almost desperate gasps as Sasha and I thrust into her from two directions at once."
    "I should have been able to look Sasha straight in the eye while doing this."
    "But I can already see that her eyes are almost completely glazed over too."
    "This puzzles me until a wet slit appears before me."
    "I instantly recognise it to be [bree.name]'s."
    "The next steps are obvious. So I start out slow and gentle."
    "Slowly and surely I make my way around her lips, moving inwards a little at a time."
    "My tongue snakes out and pushes further than ever before into her pussy, trying to react to her moans."
    "I could go on like this forever, if I only had the stamina for such a feat."
    "But as it is, I can already feel my legs beginning to shake."
    "I don't know how much longer I can keep this up..."
    menu:
        "Cum inside Minami":
            with vpunch
            "Using the very last of my strength, I hold onto Minami as I cum."
            with vpunch
            "The force of it means that she's lifted a little higher than before."
            "And so she rises almost the whole way off of the dildo in her ass too."
            with vpunch
            "But this also means that as soon as I've filled her, she sinks back down again."
            "So almost the second after she's thrown her head back from one thing, Minami's hit by another."
            "And this time the dildo goes deeper than ever, thanks to my own strength failing."
            show foursome breeminamisasha minamiahegao
            "Minami cries out as Sasha staggers to support her weight without being pulled down too."
            "All the while, I find myself sinking slowly down the wall."
            "And it's all I can do to end up in a heap and unhurt on the floor, with Minami and Sasha."
        "Pull out":
            "Somehow I manage to lift Minami higher than before, letting my cock slip out of her as I do so."
            show foursome breeminamisasha minamiahegao
            "She moans a little as this happens, but not enough to make me regret the move."
            "And the similar sound that I hear from Sasha at the same time tells the dildo is out of Minami's ass too."
            with vpunch
            "Using the very last of my strength, I hold onto Minami as I cum over her breasts and stomach."
            with vpunch
            "The semen lands in crazy stripes of white, running around her nipples and down towards her pussy."
            with vpunch
            "The sight fascinates me, making me forget for a moment that I'm the only thing keeping her aloft."
            "All the while, I find myself sinking slowly down the wall."
            "And it's all I can do to end up in a heap and unhurt on the floor, with Minami and Sasha."
    bree.say "Mmm..."
    bree.say "That was quite something, you guys!"
    "[bree.name] smiles happily as she sits down on the floor beside us."
    "She's still flushed from playing with herself and Sasha."
    "But in comparison to everyone else, she's in pretty good shape right now."
    bree.say "Welcome to the party, Minami."
    bree.say "But don't you go thinking you're going to get the cock every time!"
    $ minami.sexperience += 1
    return

label bree_minami_sasha_male_ending:
    $ game.room = "church"
    scene bg church wedding
    with fade
    "Part of me still can't believe I'm actually standing at the altar right now."
    "It's like I keep expecting to wake up and find that it was all some crazy dream."
    "So just for the sake of putting that feeling to rest, I reach into my trouser pocket and pinch myself."
    "And when I feel the little twinge of pain that it causes me, I know that all of this is for real."
    "Don't get me wrong, it's not the fact that I'm getting married that seems so far-fetched."
    "I'd always supposed that this would happen to me one day, once I found the right girl."
    "But never in my wildest dreams did I imagine that it would be to three girls all at once!"
    "Yet that's exactly what's about to happen - [bree.name], Sasha and Minami are all here."
    "And they're about to come walking down that aisle together and marry me."
    "So maybe you can begin to see why my life's been feeling like a dream lately?"
    "I mean, hitting it off with one of my hot housemates would have been an achievement."
    "But somehow I managed it with both of them and they were cool with it!"
    "And then, my little sister (who, let's not forget, is adopted) moved in."
    "I thought that alone might be enough to put a strain on things."
    "And I was sure of it when I discovered that she had designs on me too!"
    "So you can imagine how amazed I was when [bree.name] and Sasha agreed to let her in on what we had going."
    "Pretty soon we'd gone from being a household to some kind of harem!"
    "It just seemed to work - don't ask me how or why, but it did."
    "I'm not going to overthink it or pull it apart."
    "Instead I'm determined to enjoy every moment of the ride for as long as it lasts."
    "And I think the fact that we've here today says that it'll likely last for some considerable time!"
    show sasha wedding zorder 1 at center, zoomAt (1.0, (880, 740))
    show minami wedding normal zorder 3 at center, zoomAt (1.0, (640, 740))
    show bree wedding zorder 2 at center, zoomAt (1.0, (400, 740))
    with dissolve
    "But as the music begins to fill the chapel, there's no more time for reflection."
    show sasha at center, traveling (1.25, 4.0, (960, 900))
    show minami at center, traveling (1.25, 4.0, (640, 900))
    show bree at center, traveling (1.25, 4.0, (320, 900))
    "My brides are walking up the aisle, arm in arm as they approach the altar."
    "And the moment that I lay eyes upon them, everything else fades from my thoughts."
    "Each one of them looks amazing in the dresses that they've chosen."
    "But almost as important to me is the fact that none of them looks the least bit similar."
    show bree happy
    "[bree.name] is a vision in white as she walks towards me."
    "The only thing as striking as her dress is the smile on her face."
    show sasha happy
    "In contrast, Sasha is all black lace against pale skin."
    "Which makes her look like the sensual night to [bree.name]'s beaming day."
    show minami happy
    "And Minami, what can I say about my gorgeous little Minami?"
    "Her dress is of Japanese silk and traditional patterns."
    "But the cut is modern and unconventional, just like her."
    if bree.is_visibly_pregnant and minami.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of three large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not minami.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha and Minami as they stand beside me at the altar."
        "My three brides - soon to be my three wives!"
    else:
        if bree.is_visibly_pregnant:
            "I almost forget that [bree.name]'s so far along with her pregnancy."
            "The dress hides her bump so well and she's holding her bouquet over it too!"
            "Though it doesn't seem to be holding her back in the slightest."
        if sasha.is_visibly_pregnant:
            "It takes me a moment to see that Sasha actually looks a little paler than usual."
            "And that's most likely on account of her being pregnant right now."
            "So I make a mental note to keep an eye on her for any signs her colour getting worse!"
        if minami.is_visibly_pregnant:
            "As well made as her dress is, it can't hope to hide the fact that Minami's with child."
            "But she makes no effort to hide the fact - and why should she?"
            "I'm as proud to be the father as she is to be having my baby!"
    show bree normal
    show sasha normal
    show minami normal
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To witness the union of these four people in the bonds of holy matrimony."
    "There's nothing disapproving or irritable in the tone of the priest's voice."
    "But the beginning of the ceremony serves to snap us all back to reality."
    "Almost as one, our heads snap around and we're facing forwards, trying to look serious."
    "The words coming out of the priest's mouth are the usual lines."
    "They're the ones that you've heard before at every wedding your entire life."
    "But when it comes to the vows, that's when things get a little more interesting."
    "Apparently there's no hard and fast rule as to who goes first."
    "So we just decided to say girls before guys and then go in alphabetical order!"
    "Priest" "[bree.name], do you take Minami, Sasha and [hero.name] to be your lawful, wedded partners?"
    show bree happy at startle
    bree.say "I do!"
    "Priest" "Minami, do you take [bree.name], Sasha and [hero.name] to be your lawful, wedded partners?"
    show minami happy at startle
    minami.say "You bet I do!"
    "Priest" "Sasha, do you take [bree.name], Minami and [hero.name] to be your lawful, wedded partners?"
    show sasha happy at startle
    sasha.say "Yes, I do."
    "I hear the priest take a deep breath before he comes to me."
    "But it seems to be just from his being a little tired at all of the extra lines."
    "And so I don't feel the need to worry about the short pause in the proceedings."
    "Priest" "And finally, [hero.name], do you take [bree.name], Minami and Sasha to be your lawful, wedded partners?"
    mike.say "I do."
    "The priest nods, clearly eager to get on with things."
    "Priest" "I call upon all those present..."
    "Priest" "Should they know of any reason these four may not be wed, to speak now."
    "Priest" "Or forever hold their peace!"
    show bree normal
    show sasha normal
    show minami normal
    "There's the customary pause as everyone looks around with baited breath."
    "But it seems to me that if the four of us can make it this far, then we're probably safe."
    "And that suspicion is confirmed when the priest nods with obvious relief."
    "Priest" "Very good - I now pronounce you husband and wives."
    "Priest" "You may kiss...erm...well..."
    "Priest" "Each other, I suppose!"
    "It's not like we needed the permission to do that."
    show sasha at center, traveling (1.5, 1.0, (920, 1040))
    show bree at center, traveling (1.5, 1.0, (360, 1040))
    show minami at center, traveling (1.5, 1.0, (640, 1040))
    "[bree.name], Sasha and Minami come together with me in a four-way embrace."
    "Our heads come together, and we trade kisses between ourselves the whole time."
    "No one speaks in that moment, the looks that pass between us saying more than words."
    "We did it - we're all bound together with no need to hide our love behind closed doors."
    "I don't know what happens from this point on."
    "But if it's half as enjoyable as getting here was, I have a feeling that it'll be fun finding out!"

    scene home ending
    show home ending minami
    with fade
    minami.say "Ah, where to start!"
    minami.say "Well, I guess I should start at the start."
    minami.say "I can remember the first time I laid eyes on big bro..."
    show home ending bree with dissolve
    bree.say "Hey, wait a minute, Minami!"
    show home ending sasha with dissolve
    sasha.say "Yeah - what are you doing?"
    minami.say "Erm...nothing...nothing at all!"
    bree.say "Ah, you little liar!"
    sasha.say "You were going to do this without us - weren't you?!?"
    minami.say "No...I...well...kinda, I guess!"
    minami.say "Aw, come on you guys."
    minami.say "I have known big bro the longest!"
    bree.say "No way, Minami."
    bree.say "We're all married now, remember?"
    sasha.say "And that means we do things as a foursome, okay?"
    minami.say "But what about big bro, huh?"
    minami.say "Shouldn't we wait until he gets here too?"
    minami.say "Because right now we're just a threesome!"
    bree.say "Ooh, yeah."
    bree.say "Maybe she's got a point, Sasha!"
    sasha.say "Nope - this doesn't count."
    bree.say "Why not?"
    sasha.say "Because I say so - that's why!"
    bree.say "Oops..."
    bree.say "Okay, Sasha."
    bree.say "Y...you know there's a vein sticking out on your forehead right now?"
    minami.say "Yeah, Sasha - take a chill pill!"
    sasha.say "Whatever, so long as we get on with it."
    minami.say "Anyway, you should turn that frown upside down."
    bree.say "I hear you, Minami - married life is turning out pretty sweet."
    sasha.say "You got me there, guys."
    sasha.say "I never thought it would be, but it really is!"
    bree.say "Maybe that's because we were all friends before?"
    sasha.say "Well, apart from the times that we were at each other's throats!"
    minami.say "But that's good too, isn't it?"
    bree.say "It is?"
    minami.say "Yeah, sure it is."
    minami.say "It's like when big bro and I were kids together."
    minami.say "Sure we fought a lot, but we got to know each other so well too."
    sasha.say "I see that, Minami."
    sasha.say "Living together meant we got to see all sides of each other."
    bree.say "Oh, I get it now!"
    bree.say "So there were no nasty surprises after we tied the knot."
    sasha.say "Yeah, because we already knew about all of [hero.name]'s bad habits!"
    minami.say "Tell me about it!"
    minami.say "You should have tried growing up with him too!"
    bree.say "But it's sweet that the house is now really our home."
    sasha.say "Though it is starting to get a little crowded around here..."
    if bree.is_visibly_pregnant and minami.is_visibly_pregnant and sasha.is_visibly_pregnant:
        bree.say "Hmm...we kinda turned this place into a commune between us!"
        sasha.say "Yeah, well, [hero.name]'s to blame as well."
        sasha.say "He shouldn't be so damn fertile!"
        minami.say "Aww - big bro wanted to buy a sports car."
        minami.say "But he had to get a mini-van instead!"
    elif not bree.is_visibly_pregnant and not minami.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "Yeah, and there's always the chance of it getting even more crowded too!"
        minami.say "Huh...who else is moving in here?"
        sasha.say "She means the patter of tiny feet, Minami!"
        minami.say "Oh..."
        minami.say "Well, that could happen!"
    else:
        if bree.is_visibly_pregnant:
            bree.say "I know, I know."
            bree.say "Little Poppy's turning into such a tearaway since she learned to walk!"
        if minami.is_visibly_pregnant:
            minami.say "Mei having three mommies sure helps things go smoother."
            minami.say "But she's still such a handful!"
        if sasha.is_visibly_pregnant:
            sasha.say "I used to think that boys were easier to raise than girls."
            sasha.say "But wow, did Dahlia cure me of that one pretty quickly!"
    bree.say "So all in all, we're pretty happy with how things turned out."
    sasha.say "Apart from [hero.name]'s stinky shoes."
    minami.say "And his socks - he leaves those everywhere!"
    bree.say "Aww, that's not fair..."
    bree.say "No, wait...those REALLY do stink!"
    bree.say "But apart from that, he's pretty much perfect."
    sasha.say "Oh yeah, [bree.name]."
    sasha.say "Apart from his many flaws, he's the ideal man!"
    minami.say "That's my big bro!"
    sasha.say "Don't worry, Minami."
    sasha.say "Between the three of us, we'll iron out the kinks."
    bree.say "After all, we have our entire lives to do it in!"
    minami.say "YAY - big bro's so lucky to have us!"
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
