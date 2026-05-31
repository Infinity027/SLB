init python:
    SpecificTalkSubject(**{
    "name": "ask_bree_about_lexi",
    "display_name": "About Lexi",
    "label": "ask_bree_about_lexi",
    "duration": 0,
    "icon": "button_lexi",
    "conditions": [
        PersonTarget("lexi",
                Not(IsHidden()),
            ),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("asklexiinhomeharem"),
            IsFlag("ongoinghomeharem", "lexi"),
            IsFlag("lexirefusedinhomeharem", False),
            ),
        PersonTarget(bree,
            IsActive(),
            InHarem('home'),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "ask_minami_about_lexi",
    "display_name": "About Lexi",
    "label": "ask_minami_about_lexi",
    "duration": 0,
    "icon": "button_lexi",
    "conditions": [
        PersonTarget("lexi",
            Not(IsHidden()),
            ),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("asklexiinhomeharem"),
            IsFlag("ongoinghomeharem", "lexi"),
            IsFlag("lexirefusedinhomeharem", False),
            ),
        PersonTarget(minami,
            IsActive(),
            InHarem('home'),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "ask_sam_about_lexi",
    "display_name": "About Lexi",
    "label": "ask_sam_about_lexi",
    "duration": 0,
    "icon": "button_lexi",
    "conditions": [
        PersonTarget("lexi",
            Not(IsHidden()),
            ),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("asklexiinhomeharem"),
            IsFlag("ongoinghomeharem", "lexi"),
            IsFlag("lexirefusedinhomeharem", False),
            ),
        PersonTarget(samantha,
            IsActive(),
            InHarem('home'),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "ask_sasha_about_lexi",
    "display_name": "About Lexi",
    "label": "ask_sasha_about_lexi",
    "duration": 0,
    "icon": "button_lexi",
    "conditions": [
        PersonTarget("lexi",
            Not(IsHidden()),
            ),
        IsHour(8, 22),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsFlag("asklexiinhomeharem"),
            IsFlag("ongoinghomeharem", "lexi"),
            IsFlag("lexirefusedinhomeharem", False),
            ),
        PersonTarget(sasha,
            IsActive(),
            InHarem('home'),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lexi_moving_in",
    "priority": 500,
    "label": "lexi_moving_in",
    "duration": 2,
    "conditions": [
        IsHour(8, 17),
        HeroTarget(
            Not(OnDate()),
            IsFlag("ongoinghomeharem", "lexi"),
            ),
        PersonTarget("lexi",
            IsPresent(),
            Not(IsHidden()),
            IsFlag("canmovein"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "threesome_bree_lexi",
    "label": "bree_lexi_threesome_intro",
    "priority": 500,
    "conditions": [
        TogetherInHarem('home', 'bree', 'lexi'),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom1")
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("home"),
            Not(IsActivity("sleep")),
            MinStat("love", 150),
            ),
        PersonTarget("lexi",
            HasRoomTag("home"),
            Not(IsActivity("sleep")),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "lexi_sasha_alternative_nightclub",
    "label": "lexi_sasha_alternative_nightclub",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("lexi_sasha_1"),
        TogetherInHarem('home', 'lexi', 'sasha'),
        HeroTarget(
            IsGender("male"),
            IsRoom("nightclub", "date_nightclub")
            ),
        PersonTarget("lexi",
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("nightclub", "date_nightclub"),
            Not(HasCheated()),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            MinStat("love", 100),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "threesome_lexi_sasha",
    "label": "lexi_sasha_threesome_intro",
    "priority": 500,
    "conditions": [
        TogetherInHarem('home', 'lexi', 'sasha'),
        HeroTarget(
            IsGender("male"),
            IsRoom("bedroom1")
            ),
        PersonTarget("lexi",
            HasRoomTag("home"),
            Not(IsActivity("sleep")),
            MinStat("love", 150),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            Not(IsActivity("sleep")),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_lexi_pregnant_showdown",
    "label": "bree_lexi_pregnant_showdown",
    "duration": 1,
    "conditions": [
        Not(TogetherInHarem('home', 'bree', 'lexi')),
        PersonTarget(bree,
                IsPresent(),
                IsVisiblyPregnant(),
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                ),
        PersonTarget("lexi",
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


label ask_bree_about_lexi:
    "Of all the girls that I live with, [bree.name] is the one that I'm the least worried about talking to."
    "Sure, she's only human and could be reluctant to have Lexi move in with us for a while."
    "But I also know that she's the most open and caring of my housemates too."
    "Not that the others are a bunch of callous bitches, you understand."
    "It's just that [bree.name] wears her heart on her sleeve most of the time."
    "And I know she's the type to help out wherever she can."
    mike.say "Hey, [bree.name]!"
    mike.say "Have you got a minute spare?"
    show bree with dissolve
    "[bree.name] smiles and nods, giving me all of her attention without question."
    "In fact, her face is so beaming and cute that I almost forget what I have to say."
    bree.say "Sure thing, [hero.name]."
    show fx question
    bree.say "What's the matter?"
    mike.say "Erm...I..."
    mike.say "Oh yeah - I wanted to ask a favour."
    "[bree.name] nods again, encouraging me to go on."
    bree.say "Okay, [hero.name] - ask away!"
    mike.say "Well, you see..."
    mike.say "A friend of mine just ran into some bad luck."
    mike.say "A lot of bad luck, actually - their home burnt down."
    show bree sad
    "A look of sudden concern appears on [bree.name]'s face."
    "She gasps in horror at the implications of what I just said."
    show bree surprised
    bree.say "Oh no!"
    show fx exclamation
    bree.say "That's terrible news!"
    bree.say "So they're what...homeless now?!?"
    "I nod hastily, not prepared for [bree.name] to make that leap herself."
    "I was fully expecting to have to explain myself from start to finish."
    "But she's already filling in the gaps faster than I can keep up!"
    mike.say "Yeah, [bree.name], that's exactly it."
    mike.say "They lost everything in the fire too!"
    show bree annoyed
    "[bree.name] shakes her head, obviously empathising with Lexi's plight."
    bree.say "And where are they going to stay in the meantime, [hero.name]?"
    bree.say "Don't tell me they'll have to sleep on the street or something!"
    "I don't think I'll get a better chance than the one [bree.name] just handed to me."
    "And so I take a deep breath, preparing to get to the point."
    mike.say "That was kind of where I was going, [bree.name]."
    mike.say "I wanted to ask if they could maybe sleep on the sofa here?"
    mike.say "You know, just while they get back on their feet?"
    show bree normal
    "[bree.name]'s nodding even more emphatically now."
    "So much so that I'm worried her head might topple off of her shoulders."
    bree.say "Of course, [hero.name]."
    bree.say "That sounds like a great idea!"
    mike.say "Thanks, [bree.name]."
    mike.say "It'd really help Lexi!"
    "[bree.name] stops and looks me straight in the eye."
    show bree dazed
    "It's like she just realised something for the very first time."
    show bree surprised
    show fx question
    bree.say "Wait a minute - you're talking about a GIRL?!?"
    "Shit, this could go south really quickly!"
    "Maybe I can play off her concerns as paranoia?"
    mike.say "Uhm, yeah..."
    mike.say "Does it make a difference?"
    show bree annoyed
    bree.say "I...I know it shouldn't..."
    bree.say "But..."
    if Harem.find(samantha, name='home') and Harem.find(minami, name='home') and sasha.flags.acceptlexi and samantha.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to the others about it."
        mike.say "And they all agreed."
    elif Harem.find(samantha, name='home') and Harem.find(minami, name='home') and samantha.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to Minami and Sam about it."
        mike.say "And they both agreed."
    elif Harem.find(samantha, name='home') and sasha.flags.acceptlexi and samantha.flags.acceptlexi:
        mike.say "I already spoke to Sam and Sasha about it."
        mike.say "And they both agreed."
    elif Harem.find(minami, name='home') and sasha.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to Minami and Sasha about it."
        mike.say "And they both agreed."
    elif Harem.find(minami, name='home') and minami.flags.acceptlexi:
        mike.say "I already spoke to Minami about it."
        mike.say "And she's agreed."
    elif Harem.find(samantha, name='home') and samantha.flags.acceptlexi:
        mike.say "I already spoke to Sam about it."
        mike.say "And she's agreed."
    elif sasha.flags.acceptlexi:
        mike.say "I already spoke to Sasha about it."
        mike.say "And she's agreed."
    else:
        mike.say "I haven't spoken to the others yet."
        mike.say "But if you're up for it, I know we can convince them too."
    show bree normal
    "This seems to go a long way towards allaying [bree.name]'s fears."
    "And she nods, as if making a final decision in her mind."
    bree.say "You're right, [hero.name]."
    bree.say "It shouldn't matter if your friend is a guy or a girl."
    bree.say "They need help, and it's the right thing to do!"
    "I nod and smile, relieved to have talked [bree.name] round to my way of thinking."
    $ bree.flags.acceptlexi = True
    call lexi_can_move_in from _call_lexi_can_move_in
    return

label ask_minami_about_lexi:
    "I decide that the best thing to do is just come straight out and ask Minami about Lexi moving in."
    "I don't know if I'm fooling myself in thinking it, but I reckon she should be the easiest to sell the idea to."
    "After all, she's the youngest person living in the house and she's my little sister too."
    "Maybe I can come over as older and wiser, get her to agree with me as her dear old big brother?"
    "Or maybe she'll just see right through me and think I want to move Lexi into my own bedroom!"
    "But either way, I'm not going to find out until I actually ask the question."
    show minami at right with moveinright
    "So I choose my moment, catching Minami as she comes breezing past."
    show minami at left4 with move
    "Hoping that I catch her a little off guard too..."
    mike.say "Hey, Minami!"
    show minami happy at center with ease
    "She stops and turns on her heel, smiling at the sound of my voice."
    "Minami puts her hands behind her back and cocks her head on one side."
    show minami normal
    minami.say "Oh, hi, big bro!"
    minami.say "What's up?"
    minami.say "Or are you just stoked to see me?"
    "I smile back at her, trying to look innocent the whole time."
    "The last thing I want to do is spoil her good mood."
    "Because that'd only make asking her about Lexi that much harder."
    mike.say "I'm always happy to see you, Minami - you know that."
    mike.say "You're just so upbeat and so much fun."
    mike.say "You could get on with anyone, right?"
    "I thought that I'd done well in dropping in the question at the end there."
    "You know, been subtle enough to steer the conversation in the desired direction?"
    "But I see Minami's nose wrinkle, almost like she's scented something suspicious."
    show minami annoyed
    minami.say "Hey, big bro..."
    minami.say "Why are you being extra nice to me all of a sudden?"
    "I shrug my shoulders and shake my head in an attempt to throw her off."
    "And maybe that's a mistake, as it only seems to make me look more shifty and evasive."
    mike.say "What?!?"
    mike.say "No way, Minami."
    mike.say "That's crazy talk!"
    minami.say "No it's not, big bro."
    minami.say "You always get like this when you want something."
    minami.say "So you'd better spit it out - and be quick about it!"
    "I let out a sigh of surrender."
    "Which is as good as admitting that she's blown my cover."
    mike.say "Okay, Minami, okay."
    mike.say "You got me."
    mike.say "I need to ask a favour."
    "Minami's eyebrows shoot up in sudden interest."
    "I guess she senses the chance to have me in her debt."
    show minami normal
    minami.say "I'm listening, big bro."
    minami.say "What kind of a favour is it, huh?"
    mike.say "Well..."
    mike.say "A friend of mine just lost their home."
    mike.say "And they have nowhere to go right now."
    mike.say "I said I'd ask you and the others if they could crash here a while."
    "Minami looks more intrigued than ever, nodding the whole time."
    show fx exclamation
    minami.say "Aw, that sucks, big bro!"
    minami.say "We should definitely help them out."
    "But then I see her expression change as she considers the possibilities."
    show minami tehe
    show fx question
    minami.say "Who is this friend?"
    minami.say "Some cute guy from college?"
    show minami normal
    "I force a smile onto my face, trying again not to look shifty."
    mike.say "Erm, no..."
    mike.say "Not exactly, Minami..."
    mike.say "It's a she - and her name is Lexi!"
    "I'm fully expecting Minami to change her mind on the spot."
    "She can be insanely jealous and possessive of me."
    "So it wouldn't be a stretch for her to hate the idea of Lexi living under the same roof as us."
    show minami annoyed
    minami.say "Eww..."
    minami.say "Isn't she the trampy girl that lives on a trailer park?"
    mike.say "Well, not since her trailer burnt down!"
    mike.say "But she's down on her luck, Minami."
    mike.say "What happened to us having to help her out?"
    "Minami goes quiet for a moment, and I know that she's thinking it over."
    "She obviously sees Lexi as a potential rival."
    "But she'll make herself look bad in my eyes if she says no too."
    if Harem.find(samantha, name='home') and bree.flags.acceptlexi and sasha.flags.acceptlexi and samantha.flags.acceptlexi:
        mike.say "I already spoke to the others about it."
        mike.say "And they all agreed."
    elif bree.flags.acceptlexi and sasha.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] and Sasha about it."
        mike.say "And they both agreed."
    elif Harem.find(samantha, name='home') and bree.flags.acceptlexi and samantha.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] and Sam about it."
        mike.say "And they both agreed."
    elif Harem.find(samantha, name='home') and sasha.flags.acceptlexi and samantha.flags.acceptlexi:
        mike.say "I already spoke to Sam and Sasha about it."
        mike.say "And they both agreed."
    elif bree.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] about it."
        mike.say "And she's agreed."
    elif sasha.flags.acceptlexi:
        mike.say "I already spoke to Sasha about it."
        mike.say "And she's agreed."
    elif Harem.find(samantha, name='home') and samantha.flags.acceptlexi:
        mike.say "I already spoke to Sam about it."
        mike.say "And she's agreed."
    else:
        mike.say "I haven't spoken to the others yet."
        mike.say "But if you're up for it, I know we can convince them too."
    "At the mention of our other housemates, I see a change come over Minami."
    show minami normal
    "Sure, she's jealous of sharing me with other girls."
    "But she's already given into them on that score."
    "Plus she sees them almost like older sisters, and wants to earn their approval."
    minami.say "Okay, big bro."
    minami.say "If everyone else is okay with it, I am too."
    mike.say "Thanks, Minami."
    mike.say "You know that it's the right thing to do!"
    "Minami nods and gives me a little smile at this."
    "But I can see from the look in her eyes that she expects me to deliver on that promise."
    $ minami.flags.acceptlexi = True
    call lexi_can_move_in from _call_lexi_can_move_in_1
    return


label ask_sam_about_lexi:
    "Sam should be an easy sell when it comes to the idea of letting Lexi move in here, right?"
    "I mean, she's a pretty compassionate kind of girl and likes to help out those in need."
    "Plus she, since her marriage to Ryan ended, she seems to getting more and more adventurous too."
    "If there's anyone that's going to be okay with a girl like Lexi moving in, it has to be Sam."
    "All of that's running around in my head as I choose my moment to ask her what she thinks."
    "And even though I've talked myself into thinking she'll say yes, I still have some last minute nerves."
    if samantha.flags.nickname == "cupcake":
        mike.say "Sam..."
    else:
        mike.say "Cupcake..."
    mike.say "I wondered if I could ask you something?"
    show samantha with dissolve
    "Sam looks up from what she was doing, noticing me for the first time."
    show samantha happy
    "She smiles broadly, looking happy to see me and making me sure she's in a good mood."
    "And I hope an open-minded one too..."
    samantha.say "Oh, hey, [hero.name]."
    show samantha normal
    samantha.say "Sure you can."
    samantha.say "Ask away!"
    mike.say "Well, if you heard that someone was in bad place."
    if samantha.flags.nickname == "cupcake":
        mike.say "You'd want to help them - wouldn't you, Cupcake?"
    else:
        mike.say "You'd want to help them - wouldn't you, Sam?"
    "Sam cocks her head on one side a little as she looks at me."
    "And I can see that she's trying to guess where I'm going with this."
    samantha.say "I suppose so, [hero.name]."
    show samantha annoyed
    samantha.say "In theory, at least."
    mike.say "In theory?"
    samantha.say "Yeah, [hero.name]."
    samantha.say "I'd need to know what their problem was."
    samantha.say "I can hardly agree to help someone if I don't know that."
    mike.say "I...I guess you're right."
    show samantha normal
    samantha.say "And speaking of guesses, let me make one right now."
    samantha.say "You want to help someone."
    show fx question
    samantha.say "But you need my help to do it, right?"
    "I suppose Sam knows me far better than I thought!"
    "There seems to be no point in denying it anymore."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah...yeah, Cupcake - you got me!"
    else:
        mike.say "Ah...yeah, Sam - you got me!"
    samantha.say "And this someone is a girl, I suppose?"
    "This time she really catches me off guard."
    "And I can feel myself starting to blush too."
    mike.say "Wow..."
    mike.say "Am I really that easy to see through?"
    show samantha happy at startle
    "Sam chuckles at this, shaking her head."
    show samantha normal
    samantha.say "To me, you're pretty much transparent!"
    samantha.say "But if you have a friend that needs help, why not just say so?"
    mike.say "Well..."
    mike.say "This friend - she's called Lexi, by the way."
    mike.say "Her trailer burned down and she's basically homeless right now."
    mike.say "She wondered if she could move in here."
    mike.say "Just while she gets herself back on her feet."
    "Sam nods, seeing the full picture for the first time."
    samantha.say "And you thought that I might say no?"
    mike.say "I was worried you might..."
    show samantha blush
    samantha.say "Oh, [hero.name]..."
    samantha.say "I already told you I don't mind you seeing other girls."
    samantha.say "But what do the others think about this?"
    samantha.say "You were planning on asking them, I take it?"
    if Harem.find(minami, name='home') and sasha.flags.acceptlexi and bree.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to the others about it."
        mike.say "And they all agreed."
    elif sasha.flags.acceptlexi and bree.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] and Sasha about it."
        mike.say "And they both agreed."
    elif Harem.find(minami, name='home') and bree.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] and Minami about it."
        mike.say "And they both agreed."
    elif Harem.find(minami, name='home') and sasha.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to Minami and Sasha about it."
        mike.say "And they both agreed."
    elif bree.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] about it."
        mike.say "And she's agreed."
    elif sasha.flags.acceptlexi:
        mike.say "I already spoke to Sasha about it."
        mike.say "And she's agreed."
    elif Harem.find(minami, name='home') and minami.flags.acceptlexi:
        mike.say "I already spoke to Minami about it."
        mike.say "And she's agreed."
    else:
        mike.say "I haven't spoken to the others yet."
        mike.say "But if you're up for it, I know we can convince them too."
    show samantha happy -blush
    "Sam nods, seemingly satisfied with where things are at right now."
    samantha.say "Looks like we might be getting a new housemate!"
    show samantha normal
    samantha.say "And she sounds pretty interesting too."
    samantha.say "I don't think I ever met someone that lived on a trailer park before!"
    "I nod and smile, all the while hoping that Sam's right."
    $ samantha.flags.acceptlexi = True
    call lexi_can_move_in from _call_lexi_can_move_in_2
    return

label ask_sasha_about_lexi:
    "If I'm honest, I'm kind of nervous about asking Sasha to let Lexi move into the house with us."
    "Don't get me wrong - I'm not suggesting that Sasha won't be sympathetic to Lexi's plight."
    "I'm sure she'd be willing to do anything to help the girl out, within reason."
    "But actually letting Lexi come and live under the same roof as her?"
    "Well, let's just say that her reaction has yet to be seen!"
    "So it's with not a little trepidation that I bring the subject up..."
    mike.say "Ah...Sasha?"
    mike.say "Have you got a minute?"
    show sasha with dissolve
    "The moment that Sasha looks up and meets my eye, I'm sure I've already blown it."
    "She has that look on her face, the one with the arched eyebrow."
    "The one that means she's cynically amused to hear what I have to say."
    sasha.say "Sure thing, [hero.name]."
    sasha.say "I'm all ears."
    mike.say "Great, Sasha...that's great!"
    mike.say "Well..."
    "I swallow audibly before steeling myself and pushing on."
    mike.say "You know how they say that charity starts at home?"
    "At this, Sasha's eyebrow raises itself higher still."
    show sasha annoyed
    sasha.say "Yeah, [hero.name]."
    sasha.say "I've heard that SOME people say that."
    "I can't help laughing, as if she's joking."
    mike.say "Okay, Sasha, here's the thing..."
    mike.say "A friend of mine just had some really bad luck."
    mike.say "They came home to find their trailer burned to the ground."
    "Sasha nods as I begin to get to the meat of the story."
    sasha.say "Yup, that sounds like a whole lot of bad luck."
    sasha.say "But what has it got to do with you and me?"
    mike.say "Well, now that they're homeless..."
    mike.say "I wondered if they could..."
    show sasha a
    "Sasha holds up her hand, cutting me off before I can finish."
    show sasha normal
    sasha.say "Let me guess, [hero.name]."
    sasha.say "You wondered if they could come and stay here, right?"
    mike.say "Ah...yeah, that's exactly it!"
    show sasha normal
    "Sasha nods again, a knowing smile starting to spread across her face."
    sasha.say "And this friend of your's..."
    show fx question
    sasha.say "She wouldn't happen to be a girl, would she?"
    mike.say "Y...yeah, she would."
    mike.say "How did you know?"
    show sasha happy
    "Sasha shakes her head at this, chuckling at my surprise."
    show sasha normal
    sasha.say "Oh, [hero.name], you're pretty bad at hiding stuff from me!"
    sasha.say "If you were talking about a guy, you'd have just come out and said it."
    show sasha annoyed
    sasha.say "That or I'd have walked into the sitting room and found him asleep on the sofa!"
    show sasha normal
    sasha.say "But with a girl, you'd never pull something like that."
    mike.say "Geez, Sasha - you know me so well!"
    mike.say "So, what do you say?"
    mike.say "Are you okay with it - even though she's a girl?"
    show sasha annoyed
    "Sasha screws her face up into a thoughtful frown."
    sasha.say "Hmm...I dunno."
    sasha.say "What about the others?"
    show fx question
    sasha.say "What do they think?"
    if Harem.find(samantha, name='home') and Harem.find(minami, name='home') and bree.flags.acceptlexi and samantha.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to the others about it."
        mike.say "And they all agreed."
    elif Harem.find(minami, name='home') and bree.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] and Minami about it."
        mike.say "And they both agreed."
    elif Harem.find(samantha, name='home') and bree.flags.acceptlexi and samantha.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] and Sam about it."
        mike.say "And they both agreed."
    elif Harem.find(samantha, name='home') and Harem.find(minami, name='home') and samantha.flags.acceptlexi and minami.flags.acceptlexi:
        mike.say "I already spoke to Sam and Minami about it."
        mike.say "And they both agreed."
    elif bree.flags.acceptlexi:
        mike.say "I already spoke to [bree.name] about it."
        mike.say "And she's agreed."
    elif Harem.find(minami, name='home') and minami.flags.acceptlexi:
        mike.say "I already spoke to Minami about it."
        mike.say "And she's agreed."
    elif Harem.find(samantha, name='home') and samantha.flags.acceptlexi:
        mike.say "I already spoke to Sam about it."
        mike.say "And she's agreed."
    else:
        mike.say "I haven't spoken to the others yet."
        mike.say "But if you're up for it, I know we can convince them too."
    show sasha normal
    "Sasha nods her head, seemingly pleased with my explanation of current opinion."
    sasha.say "I suppose we should help her out."
    sasha.say "I'd hope people would do the same for me."
    "I nod too, pleased to have managed to get Sasha on my side."
    $ sasha.flags.acceptlexi = True
    call lexi_can_move_in from _call_lexi_can_move_in_3
    return

label lexi_can_move_in:
    if Harem.find(samantha, name='home') and Harem.find(minami, name='home') and Harem.find(bree, name='home') and samantha.flags.acceptlexi and minami.flags.acceptlexi and bree.flags.acceptlexi and sasha.flags.acceptlexi:
        $ lexi.flags.canmovein = True
    elif Harem.find(samantha, name='home') and not Harem.find(minami, name='home') and Harem.find(bree, name='home') and samantha.flags.acceptlexi and bree.flags.acceptlexi and sasha.flags.acceptlexi:
        $ lexi.flags.canmovein = True
    elif not Harem.find(samantha, name='home') and Harem.find(minami, name='home') and Harem.find(bree, name='home') and minami.flags.acceptlexi and bree.flags.acceptlexi and sasha.flags.acceptlexi:
        $ lexi.flags.canmovein = True
    elif not Harem.find(samantha, name='home') and not Harem.find(minami, name='home') and Harem.find(bree, name='home') and bree.flags.acceptlexi and sasha.flags.acceptlexi:
        $ lexi.flags.canmovein = True
    return

label lexi_moving_in:





    "When I finally manage to find Lexi I can see that Lexi's is eager to hear the news."
    show lexi happy with dissolve
    lexi.say "Hey there, [hero.name]!"
    show lexi normal
    lexi.say "Or should I say housemate?!?"
    mike.say "Ah..."
    mike.say "Hi, Lexi."
    mike.say "You could say that, I guess."
    show lexi surprised
    show fx question
    lexi.say "So they DID say yes?"
    mike.say "That's right, they said yes."
    show lexi happy
    "Lexi lets out a loud sight of relief, sagging a little as she does so."
    "And that sound serves to remind me of just how serious of a trauma she's suffered."
    "She might well be a veteran of the streets and come over like she's as tough as they come."
    "But the reality is that Lexi's every bit as human and vulnerable as anyone else."
    show fx exclamation
    lexi.say "Whew!"
    lexi.say "That's a relief, [hero.name]."
    show lexi normal
    lexi.say "At least I know where I'm going to be sleeping tonight!"
    "I nod with enthusiasm and relief, trying not to feel guilty."
    "Part of me feels like I've gotten too tangled up in getting my housemates onboard."
    "And in doing so, I've almost lost sight of why I was actually doing this in the first place."
    mike.say "Well, maybe not exactly where."
    mike.say "We can clear up whether it's the sofa or whatever when you actually move in!"
    "Now it's Lexi's turn to nod eagerly."
    lexi.say "Okay - so what are we waiting for?"
    mike.say "Erm..."
    mike.say "What do you mean, Lexi?"
    show lexi annoyed
    "At this, she looks around and shrugs her shoulders."
    lexi.say "I don't see anything else holding us up around here!"
    show lexi normal
    lexi.say "So let's get over to your place right now."
    mike.say "You mean right now as in right now?!?"
    mike.say "I haven't had time to get the place ready!"
    lexi.say "No problem, [hero.name]."
    lexi.say "I'm only sleeping on the couch, apparently!"
    mike.say "Ah...I..."
    mike.say "Don't you need to grab your stuff?"
    show lexi sad
    lexi.say "Ah...hello?"
    lexi.say "It all burned to ashes, remember?"
    lexi.say "All I got left is the clothes I'm standing up in!"
    play sound spank
    with vpunch
    "All I can do is slap myself on the forehead and roll my eyes."
    "Why in the world am I even trying to argue with Lexi on this one?"
    "After all, it makes no difference if she moves in now or in a week's time."
    "At least not to my housemates and me."
    "But every minute that I try to put her off is another minute that Lexi has to spend homeless."
    mike.say "Of course, Lexi, of course."
    mike.say "I don't know what I was thinking."
    mike.say "Let's get going."
    show lexi happy at center, zoomAt(1.5, (640, 1040))
    "Lexi smiles and wraps her arm in mine as we walk away."
    lexi.say "This is going to be SO great."
    lexi.say "A house without wheels on it."
    lexi.say "A bunch of live-in girlfriends."
    lexi.say "And best of all - you always within easy reach!"
    "Lexi presses herself against me as she says this, smiling happily."
    "And I smile too, reminded of how her body feels when it's up so close."
    "As well as thinking how close she's going to be for a good while to come too!"
    scene bg house with fade
    "I honestly don't know what I'd been expecting to happen once I brought Lexi home to stay."
    "In the past I'd shown potential housemates around the place, giving them the grand tour."
    "And that's what I'm thinking as I open the front door and make to usher her into the hall."
    "But Lexi takes me by surprise, almost elbowing me in the ribs to push her way past."
    "She's inside and wandering off so quickly that I have to hurry to slam the door and keep up!"
    play sound door_slam
    scene bg livingroom
    show lexi happy
    with fade
    lexi.say "Ooh..."
    lexi.say "This place is great, [hero.name]!"
    lexi.say "So fancy and sophisticated - not like the trailer park!"
    scene bg secondfloor with fade
    "I find myself following on Lexi's heels as she goes from one room to the next."
    "She cranes her head around doors, going inside and poking around as the urge takes her."
    "All I can do is travel in her wake, trying to make it look like I'm somehow in control."
    "But I have no idea if Lexi is even listening to a single word I'm saying the whole time!"
    "I guess it's not that bad, as everyone else seems to be out of the house right now."
    "So maybe bringing Lexi home without any warning and in the middle of the day will pay off!"
    scene bg bathroom
    show lexi happy
    with fade
    show fx exclamation
    lexi.say "Look at the size of that bathtub!"
    show lexi blush
    lexi.say "You could have some serious fun in there..."
    mike.say "Ah...yeah..."
    scene bg pool
    show lexi happy
    with fade
    lexi.say "You have a large pool - with a wall around it."
    show fx exclamation
    lexi.say "I can sunbathe topless as much as I like!"
    mike.say "You can what?!?"
    scene bg bedroom1
    show lexi happy
    with fade
    lexi.say "This bed is so springy, [hero.name]."
    show fx exclamation
    lexi.say "Look - I can bounce on it like a trampoline!"
    mike.say "Lexi, stop that."
    mike.say "I think I'm going to go blind!"
    scene bg livingroom with fade
    "Eventually we wind up walking into the sitting room."
    "Well, if I'm honest, with me following Lexi in there."
    "Which is when I realise that we're no longer alone."
    "Four pairs of eyes are suddenly staring at us from the sofas."
    "And that's because all of my housemates are sitting right there!"
    show lexi
    mike.say "Ah...these..."
    mike.say "These are the other housemates, Lexi!"
    "It's all I can think to say on the spur of the moment."
    "But I can already see that it's ruffled some feathers."
    show bree angry at left
    bree.say "Hey, [hero.name]!"
    bree.say "We deserve a better introduction than that!"
    show sasha annoyed at right
    sasha.say "Yeah - we're not a feature of the house!"
    sasha.say "You just showed us off like you would with the hot-tub!"
    if Harem.find(samantha, name='home') and Harem.find(minami, name='home'):
        "But while [bree.name] and Sasha are prickling, Minami and Sam are more quiet."
        "And I can easily see that they're studying Lexi with real interest."
    elif Harem.find(samantha, name='home'):
        "But while [bree.name] and Sasha are prickling, Sam is more quiet."
        "And I can easily see that she is studying Lexi with real interest."
    elif Harem.find(minami, name='home'):
        "But while [bree.name] and Sasha are prickling, Minami is more quiet."
        "And I can easily see that she is studying Lexi with real interest."
    show bree normal
    show sasha normal
    mike.say "Lexi, this is [bree.name] and Sasha."
    show lexi blush
    lexi.say "Hey Sasha, nice to see you again."
    lexi.say "[bree.name], I'm Lexi - like he said!"
    hide bree
    hide sasha
    if Harem.find(samantha, name='home') and Harem.find(minami, name='home'):
        show minami at left
        show samantha at right
        with fade
        if samantha.flags.nickname == "cupcake":
            mike.say "And over here we have Minami and Cupcake."
        else:
            mike.say "And over here we have Minami and Sam."
        show lexi happy -blush
        lexi.say "Charmed, I'm sure!"
        minami.say "I'm his little sister."
        mike.say "ADOPTED little sister!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake's actually lived here the longest, technically."
        else:
            mike.say "Sam's actually lived here the longest, technically."
        mike.say "As she lived here before [bree.name] and Sasha moved in."
        mike.say "And then she moved back in again."
        samantha.say "It's a bit more complicated than that."
        samantha.say "But basically, yeah."
    elif Harem.find(samantha, name='home'):
        show samantha at right
        with fade
        if samantha.flags.nickname == "cupcake":
            mike.say "And over here there's Cupcake."
        else:
            mike.say "And over here there's Sam."
        show lexi happy -blush
        lexi.say "Charmed, I'm sure!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake's actually lived here the longest, technically."
        else:
            mike.say "Sam's actually lived here the longest, technically."
        mike.say "As she lived here before [bree.name] and Sasha moved in."
        mike.say "And then she moved back in again."
        samantha.say "It's a bit more complicated than that."
        samantha.say "But basically, yeah."
    elif Harem.find(minami, name='home'):
        show minami at left
        with fade
        mike.say "And over here there's Minami."
        show lexi happy -blush
        lexi.say "Charmed, I'm sure!"
        minami.say "I'm his little sister."
        mike.say "ADOPTED little sister!"
    hide minami
    hide samantha
    with fade
    "Lexi smiles sweetly at the assembled girls as she flops down on the empty sofa."
    "She bounces up and down on it a couple of times, as if trying it on for size."
    "But then she leans forward, elbows on knees and chin on the palms of her hands."
    lexi.say "[hero.name] here told me that I could crash on one of the sofas."
    lexi.say "But I think there's a way more casual arrangement going on around here."
    lexi.say "Am I right or am I right?"
    "I watch with a mounting sense of horror as Lexi looks from one face to the next."
    "[bree.name], Sasha, Sam and Minami all seem to be playing dumb right now."
    "They shake their heads and exchange confused glances, pretending not to understand the question."
    show fx exclamation
    lexi.say "Oh, come on, you guys!"
    lexi.say "Four girls and one guy, all under the same roof?"
    show lexi blush
    show fx question
    lexi.say "You're fucking each other, aren't you?"
    if Harem.find(samantha, name='home') and Harem.find(minami, name='home'):
        lexi.say "All five of you are in on it or else I'm going crazy!"
        hide lexi
        show bree annoyed blush at mostleft4
        show sasha annoyed at left4
        show minami angry blush at right4
        show samantha annoyed blush at mostright4
        with fade
        "All girls" "You can't think that...\nWhat are you trying to say...\nBig bro, is she...\nWait just a minute..."
    elif Harem.find(samantha, name='home'):
        lexi.say "All four of you are in on it or else I'm going crazy!"
        hide lexi
        show bree annoyed blush at left
        show sasha annoyed at middle
        show samantha annoyed blush at right
        with fade
        "All girls" "You can't think that...\nWhat are you trying to say...\nWait just a minute..."
    elif Harem.find(minami, name='home'):
        lexi.say "All four of you are in on it or else I'm going crazy!"
        hide lexi
        show bree annoyed blush at left
        show sasha annoyed at middle
        show minami angry blush at right
        with fade
        "All girls" "You can't think that...\nWhat are you trying to say...\nBig bro, is she..."
    else:
        lexi.say "All three of you are in on it or else I'm going crazy!"
        hide lexi
        show bree annoyed blush at left
        show sasha annoyed at right
        with fade
        "All girls" "You can't think that...\nWhat are you trying to say..."
    "For a moment they're all talking at once, speaking over the top of each other."
    "Either trying to feign ignorance or else call Lexi out on what she's suggesting."
    "But in the end, I feel like it's well before time that I spoke up and hand my say."
    mike.say "Ah, give it up, you guys."
    mike.say "Lexi here's seen more action than all of you put together."
    hide bree
    hide sasha
    hide minami
    hide samantha
    show lexi angry at center, vshake
    show fx exclamation at center, zoomAt (1.0, (680, 740))
    lexi.say "Hey!"
    show lexi annoyed
    mike.say "Sorry, Lexi - but it's true!"
    mike.say "She's onto us, so let's just stop trying to deny it, okay?"
    show lexi normal
    "The other girls exchange glances as they blush and then look down at the ground."
    show bree normal blush at left with dissolve
    bree.say "I...I guess we should be honest with our newest housemate."
    show sasha normal at right with dissolve
    sasha.say "Yeah, we can't sneak around behind her back the whole time she's here!"
    if Harem.find(samantha, name='home'):
        hide bree
        show samantha normal at left
        with fade
        samantha.say "Besides, she could probably show all of us a thing or two!"
    if Harem.find(minami, name='home'):
        hide sasha
        show minami normal at right
        with fade
        minami.say "Ooh, I'd like to learn from a real pro!"
    show lexi happy
    "Lexi leans back on the sofa, a look of smug triumph on her face."
    lexi.say "You know what - I think I'm gonna like living here!"
    "All of the other girls smile at this and let out little peals of laughter."
    "And I don't know if they're excited at Lexi's presence and promise or a little scared."
    "But it's probably a combination of both."
    "Because I know that's what I'm feeling right now!"
    $ Harem.join_by_name("home", "lexi")
    $ game.flags.ongoinghomeharem = False
    $ lexi.flags.schedule = "harem"
    $ game.room = "livingroom"
    scene bg black with dissolve
    return

label bree_lexi_threesome_intro:
    $ CONDOM = False
    scene bg bedroom1 with fade
    "I'm just laying on my bed, minding my own business when it happens."
    "The door to my room bursts open, and Lexi rushes in with [bree.name] right behind her."
    show bree normal at mostright4
    show lexi normal nophone at right4
    with moveinright
    lexi.say "There he is, [bree.name]!"
    lexi.say "What did I tell you!"
    show lexi happy
    bree.say "And I bet he was just masturbating!"
    show bree surprised
    show lexi surprised
    lexi.say "EWW!"
    bree.say "EWW!"
    show bree annoyed
    show lexi annoyed
    "I sit up on my bed, throwing aside the magazine that I was just reading."
    "Not because I don't want them to see it, you understand?"
    "But because I'm so mad at them barging into my room like this!"
    mike.say "Hey!"
    mike.say "I was not masturbating!"
    mike.say "I mean, I could if I wanted to - but that's not the point!"
    mike.say "What are you two even doing in here?!?"
    show bree a normal at right5
    show lexi normal at left5
    with move
    "[bree.name] and Lexi pretty much stride over to the side of my bed."
    "Once there, they cross their hands over their chests."
    "They're both staring down at me, serious looks on their faces."
    "Suddenly I go from feeling annoyed to more than a little worried."
    mike.say "Ah..."
    mike.say "I don't think I like where this is going, guys!"
    mike.say "Why are you looking at me like that?"
    "[bree.name] and Lexi exchange a quick glance, then a nod."
    show lexi happy
    lexi.say "[bree.name] and I have been talking, [hero.name]."
    show lexi flirt
    lexi.say "And we've come to the conclusion that we're horny."
    "I blink a couple of times, not sure I just heard her right."
    mike.say "Sorry..."
    mike.say "Did you just say you were...horny?!?"
    show bree blush
    "Now it seems to be [bree.name]'s turn to pipe up."
    "And she does so, adding another layer to the craziness."
    show bree flirt
    bree.say "That's right, [hero.name] - we're horny."
    bree.say "And you're the man of the house."
    bree.say "So it's your job to do something about it!"
    "I look up at them in amazement for a couple of seconds."
    show bree surprised
    show lexi surprised blush
    "But then I can't help bursting into laughter."
    show bree annoyed
    "A reaction which doesn't seem to go down at all well."
    show lexi angry
    lexi.say "Hey, what gives?!?"
    lexi.say "Why are you laughing at us?"
    bree.say "Yeah, [hero.name]!"
    show bree angry
    bree.say "We're serious!"
    "I sit up on my bed, swinging my legs onto the floor."
    "At the same time I'm holding up one hand to ward them off."
    mike.say "I'm sorry, guys!"
    mike.say "It's just so hilarious."
    mike.say "You two walking in here like a couple of protestors on a picket line!"
    mike.say "Well...maybe like over-sexed protestors..."
    show lexi surprised
    lexi.say "What's wrong with that?"
    show bree surprised
    bree.say "What should we do, genius?"
    "I shrug and shake my head, still trying to keep from laughing."
    mike.say "I don't know..."
    mike.say "Maybe just ask me if I was up for it?"
    show bree normal
    show lexi normal
    "At this, [bree.name] and Lexi exchange glances."
    show bree blush
    "And I can see their cheeks starting to flush red."
    bree.say "Well...are you?"
    show bree flirt -blush
    bree.say "Are you up for it?"
    lexi.say "Yeah, are you?"
    show lexi flirt
    lexi.say "Will you fuck us, [hero.name]?"
    show lexi normal blush
    "I'm starting to realise that I've got this whole situation back to front."
    "I've gone and let the way they marched in here make me forget what they actually want."
    "As I look from [bree.name] to Lexi and back again, I feel like slapping myself."
    "What does it matter how they asked or what I was doing before they showed up?"
    "I have two hot, horny blondes standing right in front of me."
    "And they're begging me to make love to them!"
    "Even I'm not that big of a fool!"
    mike.say "Ah..."
    mike.say "I guess you're right."
    mike.say "It is my responsibility to satisfy everyone under this roof!"
    show lexi happy
    show bree happy
    "As soon as they hear those words, [bree.name] and Lexi are delighted."
    "They clap their hands together and bounce up and down on the spot."
    "But I have one more question to ask them."
    mike.say "So how are we going to do this thing?"
    show bree surprised blush
    "[bree.name] stops bouncing and looks a little puzzled."
    bree.say "Oh dear..."
    show bree annoyed
    bree.say "I hadn't thought that far ahead!"
    show lexi angry
    lexi.say "WHAT?!?"
    lexi.say "Like we need to waste time thinking about that!"
    show lexi annoyed
    lexi.say "Just do what I do - get naked and pounce on his ass!"
    "I find myself laughing again as [bree.name] and Lexi do just that."
    show bree normal topless
    show lexi normal topless
    with dissolve
    "They hastily pull off their clothes right in front of me."
    "And though it's not an elegant strip-tease, the sight turns me on all the same."
    show bree naked
    show lexi naked
    with dissolve
    "I'm almost done taking off my own clothes when they make good on their promise."
    show bree naked at center, zoomAt (1.5, (860, 1050))
    show lexi naked at center, zoomAt (1.5, (420, 1050))
    with vpunch
    "[bree.name] and Lexi jump onto the bed, making it creak with their weight."
    "And then they're all over me in a frenzy of hands, lips and tongues."
    "I don't know where to go or what to caress in that moment."
    "But it's a wonderful feeling to have them wrapped around me like this."
    "The problem is that I only have one cock."
    "It's getting hard on account of them both."
    "But I can only use it on one of them..."
    menu:
        "Fuck [bree.name]":
            call bree_lexi_threesome_breefuck from _call_bree_lexi_threesome_breefuck
            $ bree.sexperience += 1
        "Fuck Lexi":
            call bree_lexi_threesome_lexifuck from _call_bree_lexi_threesome_lexifuck
            $ lexi.sexperience += 1
    scene bg bedroom1
    show multisleep homeharem bree lexi
    with fade
    "Afterwards, we collapse into another tangle of limbs on the bed."
    "Sweaty bodies rubbing against each other as the aftershock still grips us."
    "I can't help chuckling at the way [bree.name] and Lexi walked in here earlier."
    "The way they demanded that I do my duty as the man of the house."
    "They certainly seem to have got all that they were asking for, and more besides!"
    "Maybe there's something to be said for that kind of arrangement?"
    "And if so, I wonder what I can demand from them in return?"
    "Because surely the women of the house have duties just like the man."
    "Finding out just what those are sounds like a lot of fun."
    $ game.pass_time(2)
    return

label bree_lexi_threesome_breefuck:
    "Somehow I manage to find an identifying mark on a certain piece of naked skin."
    "And that lets me know I'm grabbing hold of [bree.name] and not Lexi."
    "After that, all it takes is a little manoeuvring on my part."
    "And soon enough, [bree.name] pops up like a Jack-in-the-Box!"
    bree.say "Whoa..."
    show bree surprised
    bree.say "What's happening?!?"
    bree.say "What are you..."
    lexi.say "What does it look like, [bree.name]?"
    show lexi flirt
    lexi.say "I guess you're the one getting some cock tonight!"
    scene threesome breelexi breefuck with fade
    "Before [bree.name] even has the chance to answer, I'm under her."
    "She must feel my cock, hard between her legs."
    "Because she makes a surprised yelp as I choose my target."
    menu:
        "Fuck her pussy":
            "The moment my cock rubs against [bree.name]'s pussy, I can't think about anything else."
            "It's warm and soft, slick from the fact that she's very much in the mood right now."
            "Every fibre of me wants to sink into it the moment that sensation hits me."
            mike.say "That feels good, [bree.name]..."
            mike.say "So fucking good!"
            "I feel [bree.name] begin to quiver in my arms."
            "And she nods, her blonde tresses sweeping as her head moves."
            bree.say "Feels..."
            bree.say "Feels good to me too!"
            bree.say "Are you going to..."
            "By way of answer, I push against [bree.name]'s lips."
            call check_condom_usage (bree) from _call_check_condom_usage_47
            if _return == False:
                return
            show threesome breelexi breefuck vaginal
            if CONDOM:
                show threesome breelexi breefuck vaginal condom
            "I make it gentle, but at the same time firm and insistent."
            "And as I feel her pussy resist me, her words melt into mere sounds of pleasure."
            "At the same time, I can feel the physical manifestation of those same sounds."
            "[bree.name]'s lips part as her muscles stop resisting, and I sink slowly into her."
            "I don't stop until I can't get any deeper."
            "But once I reach that point, there's no holding back."
            "My hands clasp [bree.name] around the waist."
            "My hips begin to move beneath her."
            "And just like that, I'm thrusting into her from below."
            "[bree.name] begins to wail with pleasure almost the same second I begin."
            "Gravity's pulling her down onto me and I'm pushing up from below."
            "All of which means that she's trapped in the middle with nowhere else to go!"
            show threesome breelexi breefuck lexi with dissolve
            "At first I only see Lexi out of the corner of my eye."
            "I'm too tied up in what I'm doing to pay her much attention."
            "But then I hear [bree.name] begin talking."
            "And she suddenly has me watching her intently."
            bree.say "Oh yeah..."
            bree.say "Please, Lexi..."
            bree.say "Touch me down there!"
            "I strain to see as Lexi leans in ever closer to [bree.name]."
            "At the same time, I have to be sure to keep on pounding her at the same time!"
            "But it's worth the effort, as Lexi's hands explore [bree.name]'s exposed body."
            "Everywhere she's touch, [bree.name] shivers with pleasure."
            show threesome breelexi breefuck lick
            "And I feel it reflected in her body while I'm inside of her too!"
            "By the time Lexi leans in to kiss [bree.name] full on the lips, I'm affected as well."
            "I feel like she's kissing me too!"
            "Part of me is beginning to feel like Lexi's trying to outdo me."
            show threesome breelexi breefuck pleasure
            "Silly, I know - but I start working harder all the same."
            "Before Lexi's even finished kissing [bree.name], I'm going faster than ever."
            "As soon as it breaks, [bree.name] seems to realise what's happening."
            bree.say "Oh fuck..."
            bree.say "I...I can't take much more!"
            bree.say "I'm going to cum!"
            "She's not alone either."
            "Redoubling my efforts means that I'm about to lose it too!"
            menu:
                "Cum inside":
                    "I keep a firm hold of [bree.name] as I feel myself beginning to cum."
                    "She squirms and wriggles, but my grip is enough to keep her in place."
                    show threesome breelexi breefuck creampie with vpunch
                    if not CONDOM:
                        $ bree.impregnate()
                    "I also make sure to thrust at the very last moment possible."
                    with vpunch
                    "[bree.name] throws her head back as I shoot my load into her."
                    show threesome breelexi breefuck ahegao with vpunch
                    "And she rides my cock until the very last."
                "Pull out":
                    "[bree.name] squirms and wriggles as I try to pull my cock out of her in time."
                    "More than once she almost slides off me completely, but I hold on tight."
                    "I hear her moan as it pops out of her pussy with an audible sound."
                    show threesome breelexi breefuck cumshot -vaginal with vpunch
                    "Then I shoot my load over her back and buttocks."
                    with vpunch
                    "Every last drop spatters down on [bree.name]'s glistening skin."
                    show threesome breelexi breefuck ahegao with vpunch
                    "Painting her back with sticky white stripes."
        "Fuck her ass":
            "The moment my cock is sandwiched between [bree.name]'s buttocks, I can't think about anything else."
            "It's warm and welcoming, tight despite the fact that she's very much in the mood right now."
            "Every fibre of me wants to sink into it the moment that sensation hits me."
            mike.say "That feels good, [bree.name]..."
            mike.say "So fucking good!"
            "I feel [bree.name] begin to quiver in my arms."
            "And she nods, her blonde tresses sweeping as her head moves."
            bree.say "Feels..."
            bree.say "Feels good to me too!"
            bree.say "Are you going to..."
            bree.say "Are you going to do me up the ass?!?"
            "By way of answer, I push against [bree.name]'s hole."
            show threesome breelexi breefuck anal
            "I make it gentle, but at the same time firm and insistent."
            "And as I feel her ass resist me, her words melt into mere sounds of pleasure."
            "At the same time, I can feel the physical manifestation of those same sounds."
            "[bree.name]'s lips part as her muscles stop resisting, and I sink slowly into her."
            "I don't stop until I can't get any deeper."
            "But once I reach that point, there's no holding back."
            "My hands clasp [bree.name] around the waist."
            "My hips begin to move beneath her."
            "And just like that, I'm thrusting into her from below."
            "[bree.name] begins to wail with pleasure almost the same second I begin."
            "Gravity's pulling her down onto me and I'm pushing up from below."
            "All of which means that she's trapped in the middle with nowhere else to go!"
            "At first I only see Lexi out of the corner of my eye."
            show threesome breelexi breefuck lexi with dissolve
            "I'm too tied up in what I'm doing to pay her much attention."
            "But then I hear [bree.name] begin talking."
            "And she suddenly has me watching her intently."
            bree.say "Oh yeah..."
            bree.say "Please, Lexi..."
            bree.say "Touch me down there!"
            "I strain to see as Lexi leans in ever closer to [bree.name]."
            "At the same time, I have to be sure to keep on pounding her at the same time!"
            "But it's worth the effort, as Lexi's hands explore [bree.name]'s exposed body."
            "Everywhere she's touch, [bree.name] shivers with pleasure."
            show threesome breelexi breefuck lick
            "And I feel it reflected in her body while I'm inside of her too!"
            "Of course Lexi's fingers spend most of that time stroking [bree.name]'s pussy."
            "By the time Lexi leans in to kiss [bree.name] full on the lips, I'm affected as well."
            "I feel like she's kissing me too!"
            "Part of me is beginning to feel like Lexi's trying to outdo me."
            show threesome breelexi breefuck pleasure
            "Silly, I know - but I start working harder all the same."
            "Before Lexi's even finished kissing [bree.name], I'm going faster than ever."
            "As soon as it breaks, [bree.name] seems to realise what's happening."
            bree.say "Oh fuck..."
            bree.say "I...I can't take much more!"
            bree.say "I'm going to cum!"
            "She's not alone either."
            "Redoubling my efforts means that I'm about to lose it too!"
            menu:
                "Cum inside":
                    "I keep a firm hold of [bree.name] as I feel myself beginning to cum."
                    "She squirms and wriggles, but my grip is enough to keep her in place."
                    with vpunch
                    "I also make sure to thrust at the very last moment possible."
                    show threesome breelexi breefuck creampie with vpunch
                    "[bree.name] throws her head back as I shoot my load into her."
                    show threesome breelexi breefuck ahegao with vpunch
                    "And she rides my cock until the very last."
                "Pull out":
                    "[bree.name] squirms and wriggles as I try to pull my cock out of her in time."
                    "More than once she almost slides off me completely, but I hold on tight."
                    "I hear her moan as it pops out of her ass with an audible sound."
                    show threesome breelexi breefuck cumshot -anal with vpunch
                    "Then I shoot my load over her back and buttocks."
                    with vpunch
                    "Every last drop spatters down on [bree.name]'s glistening skin."
                    show threesome breelexi breefuck ahegao with vpunch
                    "Painting her back with sticky white stripes."
            $ bree.flags.anal += 1
    return

label bree_lexi_threesome_lexifuck:
    "Don't ask me how I know one set of buttocks from another."
    "Let's just say there are little things that I'm intimately familiar with."
    scene threesome breelexi lexifuck with fade
    "And that's how I know that I'm grabbing hold of Lexi's ass, rather than [bree.name]'s!"
    "My hands grab hold of her, earning me a yelp of surprise from Lexi."
    "She's on her belly when I catch her, but soon gets onto all fours."
    "And she makes a spirited effort to crawl away from me across the bed."
    "Not that it gets her very far, as my hands move upwards far more quickly."
    "Soon enough I have one hand on Lexi's breasts."
    "And the other I send exploring between her thighs."
    show threesome breelexi lexifuck mike with dissolve
    "Lexi whimpers, quivering as I stroke her with both hands."
    "Now I've got her right where I want her."
    "The only question that remains is exactly how I want her..."
    menu:
        "Fuck her pussy":
            "By now I'm practically mounting Lexi from behind."
            "Which means that my cock is already sliding between her thighs."
            "And the moment I do that, I almost have my mind made up for me."
            "The head of my cock pushes against the lips of her pussy."
            "Then it's drawn almost along the entire length of those soft, wet folds."
            "As well as feeling that myself, I also feel Lexi shiver too."
            lexi.say "Oh fuck..."
            lexi.say "That feels good!"
            lexi.say "Gimmie some more of that shit!"
            "Sometimes I don't know what's hotter."
            "The sight of Lexi's naked body."
            "Or the filthy shit that comes out of her mouth!"
            "But either way, she's going to get exactly what she wants."
            call check_condom_usage (lexi) from _call_check_condom_usage_48
            if _return == False:
                return
            "With both hands on her breasts, I pull Lexi backwards."
            show threesome breelexi lexifuck vaginal
            if CONDOM:
                show threesome breelexi lexifuck vaginal condom
            "This pushes her hard against my cock, pressing it against her lips."
            "Lexi whimpers and moans as the muscles of her pussy resist for a moment."
            "But then those same sounds turn into a groan of pleasure as it give up the fight."
            "I hardly need to hear the change in tone, as I'm the one inching my way into her."
            "Which means I can feel every subtle change telling me that I'm getting my way."
            "I make sure that my cock sinks into Lexi as slowly as possible."
            "That means I can savour the sensation of filling her a little at a time."
            "And by the time I'm balls deep in her, she's helpless to resist."
            "I can't help enjoying myself right now, having Lexi in a position like this."
            "My hands are all over her breasts, squeezing and pinching."
            "I'm thrusting in and out of her, going faster all the time."
            show threesome breelexi lexifuck lexipleasure
            "Lexi looks back over her shoulder at me, her mouth hanging open."
            "I think she's about to say something, so I lean forwards to hear."
            "But that's the exact moment [bree.name] decides to make her move."
            show threesome breelexi lexifuck bree with dissolve
            "Until now, she's been watching us go at it in silence."
            "Though maybe she was just biding her time."
            "Standing on the bed, she pretty much thrusts her pussy into Lexi's face!"
            bree.say "There you go, Lexi."
            bree.say "There's something to keep your mouth busy!"
            "I look up at [bree.name], amazed that she's be so bold."
            "And I can see from the look on her face she's pleased with my surprise."
            "[bree.name] smiles as Lexi does exactly as she's told."
            show threesome breelexi lexifuck lick
            "But the expression doesn't last too long."
            "And that's because Lexi doesn't do things by halves."
            "Ordered to lick [bree.name]'s pussy, she goes straight to work."
            "Which means that [bree.name]'s face is soon a picture of ecstatic delight."
            bree.say "Mmm..."
            bree.say "Shit, Lexi..."
            bree.say "What are you doing to me?!?"
            show threesome breelexi lexifuck breepleasure
            "At the same time as I'm watching all of this, it's spurring me on too."
            "The more Lexi works away at [bree.name]'s pussy, the harder I pound her."
            "We can't go on like this for much longer."
            "Something's going to give."
            "And it looks like that something is going to be me!"
            mike.say "Oh fuck..."
            mike.say "Here it comes!"
            mike.say "Lexi, you'd better be ready for it!"
            menu:
                "Cum inside":
                    "While Lexi's preoccupied with [bree.name]'s pussy, I'm in total control."
                    "But all the same I'm sure to keep an extra tight hold on her while it happens."
                    "That means I can push on until the very last moment, then let myself go."
                    show threesome breelexi lexifuck creampie with hpunch
                    if not CONDOM:
                        $ lexi.impregnate()
                    "I lose it with one last thrust, shooting my load into Lexi as I do so."
                    with hpunch
                    "She bucks and twists, but I hold on until the very end."
                    show threesome breelexi lexifuck lexiahegao with hpunch
                    "Right until the cum begins to seep out around my cock."
                "Pull out":
                    "While Lexi's preoccupied with [bree.name]'s pussy, I'm in total control."
                    "Which means I can pull my cock out of her at my leisure."
                    show threesome breelexi lexifuck -vaginal cumshot with hpunch
                    "And I do just that, a few seconds before I shoot my load."
                    with hpunch
                    "Lexi bucks and twists as I pull out of her, but I hold her firmly."
                    show threesome breelexi lexifuck lexiahegao with hpunch
                    "My cock bobs up, then the warm, sticky cum stripes her buttocks."
        "Fuck her ass":
            "By now I'm practically mounting Lexi from behind."
            "Which means that my cock is already sliding between her thighs."
            "And the moment I do that, I almost have my mind made up for me."
            "The head of my cock gets caught between Lexi's buttocks."
            "And that's all I need to be fixated on the idea of fucking her ass."
            "Parting her buttocks, I press the head of my cock against her tight little hole."
            lexi.say "Oh fuck..."
            lexi.say "You want my ass?!?"
            lexi.say "You naughty boy!"
            lexi.say "Bu that does feel good!"
            lexi.say "Gimmie some more of that shit!"
            "Sometimes I don't know what's hotter."
            "The sight of Lexi's naked body."
            "Or the filthy shit that comes out of her mouth!"
            "But either way, she's going to get exactly what she wants."
            "With both hands on her breasts, I pull Lexi backwards."
            show threesome breelexi lexifuck anal
            "This pushes her hard against my cock, pressing it against her hole."
            "Lexi whimpers and moans as the muscles of her ass resist for a moment."
            "But then those same sounds turn into a groan of pleasure as it give up the fight."
            "I hardly need to hear the change in tone, as I'm the one inching my way into her."
            "Which means I can feel every subtle change telling me that I'm getting my way."
            "I make sure that my cock sinks into Lexi as slowly as possible."
            "That means I can savour the sensation of filling her a little at a time."
            "And by the time I'm balls deep in her, she's helpless to resist."
            "I can't help enjoying myself right now, having Lexi in a position like this."
            "My hands are all over her breasts, squeezing and pinching."
            "I'm thrusting in and out of her, going faster all the time."
            show threesome breelexi lexifuck lexipleasure
            "Lexi looks back over her shoulder at me, her mouth hanging open."
            "I think she's about to say something, so I lean forwards to hear."
            "But that's the exact moment [bree.name] decides to make her move."
            show threesome breelexi lexifuck bree with dissolve
            "Until now, she's been watching us go at it in silence."
            "Though maybe she was just biding her time."
            "Standing on the bed, she pretty much thrusts her pussy into Lexi's face!"
            bree.say "There you go, Lexi."
            bree.say "There's something to keep your mouth busy!"
            "I look up at [bree.name], amazed that she's be so bold."
            "And I can see from the look on her face she's pleased with my surprise."
            show threesome breelexi lexifuck lick
            "[bree.name] smiles as Lexi does exactly as she's told."
            "But the expression doesn't last too long."
            "And that's because Lexi doesn't do things by halves."
            "Ordered to lick [bree.name]'s pussy, she goes straight to work."
            "Which means that [bree.name]'s face is soon a picture of ecstatic delight."
            bree.say "Mmm..."
            bree.say "Shit, Lexi..."
            bree.say "What are you doing to me?!?"
            show threesome breelexi lexifuck breepleasure
            "At the same time as I'm watching all of this, it's spurring me on too."
            "The more Lexi works away at [bree.name]'s pussy, the harder I pound her."
            "We can't go on like this for much longer."
            "Something's going to give."
            "And it looks like that something is going to be me!"
            mike.say "Oh fuck..."
            mike.say "Here it comes!"
            mike.say "Lexi, you'd better be ready for it!"
            menu:
                "Cum inside":
                    "While Lexi's preoccupied with [bree.name]'s pussy, I'm in total control."
                    "But all the same I'm sure to keep an extra tight hold on her while it happens."
                    "That means I can push on until the very last moment, then let myself go."
                    show threesome breelexi lexifuck creampie with hpunch
                    "I lose it with one last thrust, shooting my load into Lexi as I do so."
                    with hpunch
                    "She bucks and twists, but I hold on until the very end."
                    show threesome breelexi lexifuck lexiahegao with hpunch
                    "Right until the cum begins to seep out around my cock."
                "Pull out":
                    "While Lexi's preoccupied with [bree.name]'s pussy, I'm in total control."
                    "Which means I can pull my cock out of her at my leisure."
                    show threesome breelexi lexifuck -anal cumshot with hpunch
                    "And I do just that, a few seconds before I shoot my load."
                    with hpunch
                    "Lexi bucks and twists as I pull out of her, but I hold her firmly."
                    show threesome breelexi lexifuck lexiahegao with hpunch
                    "My cock bobs up, then the warm, sticky cum stripes her buttocks."
            $ lexi.flags.anal += 1
    return

label lexi_sasha_threesome_intro(from_event=True):
    if from_event:
        scene bg bedroom1 with fade
        play sound door_knock
        "I hear a knock at my bedroom door and that makes me forget all about what I was doing."
        "It's odd, because my housemates are pretty rude and lacking in basic manners."
        "I'd have expected them to just come bursting into my room without bothering to knock."
        mike.say "Hang on..."
        mike.say "I'm coming!"
        "I cross the room in less than half-a-dozen steps."
        "And then I open the door to see who's outside."
        scene bg livingroom at dark, dark
        show lexi normal at left5
        show sasha normal at right5
        with wiperight
        lexi.say "Yeah, [hero.name], you got that right!"
        lexi.say "You're gonna be cumming real soon."
        lexi.say "And in one of us too!"
        show lexi smile
        show sasha talkative
        sasha.say "Surprise, [hero.name]!"
        sasha.say "We're the penis inspection squad!"
        sasha.say "And this is a surprise inspection!"
        scene bg bedroom1 with fade
        show lexi smile at right4
        show sasha normal at mostright4
        with easeinright
        "Before I can say another word, Lexi and Sasha push their way into my room."
        show sasha at center, zoomAt (1.5, (860, 1050))
        show lexi at center, zoomAt (1.5, (420, 1050))
        with vpunch
        "They each grab one of my arms and begin to drag me towards the bed."
        "And if I offer any hint of resistance, it's only thanks to sheer confusion!"
        mike.say "Wha..."
        mike.say "Hey!"
        mike.say "What are you doing?!?"
        "Lexi and Sasha are already pulling off my clothes by this point."
        "And my questions don't do anything to stop their progress."
        mike.say "If you guys want to get it on with me..."
        mike.say "All you had to do was ask!"
        show lexi happy
        lexi.say "Nah, [hero.name]..."
        show lexi wink
        lexi.say "It's more fun this way!"
        show sasha happy
        sasha.say "She's right..."
        show sasha joke
        sasha.say "This way we don't have to ask for what we want."
        sasha.say "We just take it!"
    else:
        "Before I can say another word, Lexi and Sasha grab me into my room."
        scene bg bedroom1
        show sasha at center, zoomAt (1.5, (860, 1050))
        show lexi at center, zoomAt (1.5, (420, 1050))
        with vpunch
        "They each grab one of my arms and begin to drag me towards the bed."
        "And if I offer any hint of resistance, it's only thanks to sheer confusion!"
        mike.say "Wha..."
        mike.say "Hey!"
        mike.say "What are you doing?!?"
        "Lexi and Sasha are already pulling off my clothes by this point."
        "And my questions don't do anything to stop their progress."
    "I'm totally naked by now, and I can't do anything to hide my feelings."
    "Needless to say, my cock is already getting pretty hard."
    "Of course this doesn't escape the girl's notice."
    "Lexi and Sasha share a bout of filthy giggling at the sight."
    show lexi topless
    "And they begin to strip themselves off in anticipation."
    show sasha topless
    lexi.say "Mmm..."
    show lexi naked normal
    lexi.say "That looks pretty damn good!"
    show sasha happy
    sasha.say "Oh yeah, Lexi!"
    show sasha naked joke
    sasha.say "But I bet it'll feel better than it looks."
    show lexi happy
    lexi.say "You mean feel good once it's inside of me!"
    show sasha annoyed
    sasha.say "No, Lexi - I mean when it's inside of ME!"
    show lexi annoyed
    "Lexi and Sasha aren't exactly arguing over my cock right now."
    show sasha at center, zoomAt (1.35, (860, 950))
    show lexi at center, zoomAt (1.35, (420, 950))
    with vpunch
    "More like they're having a friendly bit of sparring over it."
    "But that does provide me with a chance to gather my wits."
    "And to decide that the time's come to assert myself a little."
    "While the girls are distracted, I make my move."
    play sound spank
    show sasha surprised with hpunch
    "Clapping my hands on Sasha's haunches, I push her forwards."
    "It's a gentle push, but it catches her totally off-guard."
    "Which means that she stumbles forwards and onto the bed."
    scene nightclub threesome
    show nightclub threesome bedroom sashanaked lexinaked
    with hpunch
    sasha.say "Whoa!"
    sasha.say "What the..."
    "Sasha ends up crouched on all-fours upon the bed."
    "And I don't give her any time to regain her senses."
    "I simply step forwards and push my cock between her thighs."
    show nightclub threesome mike with dissolve
    mike.say "What's the matter, Sasha?"
    mike.say "You said you wanted to inspect it, right?"
    "Lexi giggles as she climbs onto the bed."
    lexi.say "Yeah, Sasha..."
    show nightclub threesome lexi with dissolve
    lexi.say "Looks like you get to be the guinea-pig!"
    sasha.say "Urgh..."
    sasha.say "Okay, okay..."
    sasha.say "So what are you waiting for, huh?"
    $ lexi_bj = False
    menu:
        "Let Lexi take the initiative":
            lexi.say "What's HE waiting for?!?"
            lexi.say "HA!"
            lexi.say "You snooze, you lose, Sasha!"
            "Lexi pretty much vaults onto Sasha's back."
            "She lands facing me, both hands grabbing my cock."
            "And then she lunges forwards and takes in into her mouth!"
            show nightclub threesome suck
            sasha.say "HEY!"
            sasha.say "WHAT THE HELL?!?"
            mike.say "Oh fuck!"
            mike.say "Mmm..."
            "Sasha's protests come too late to do any good."
            "Because Lexi's already well into it."
            "And I'm not about to stop her when she's sucking my cock!"
            "Lexi doesn't waste any time either."
            "Probably fearing Sasha trying to dislodge her, she's straight down to business."
            "Her head is going up and down at an almost alarming rate."
            "But that doesn't seem to be doing anything to affect the quality of her performance."
            "I'm soon gasping and panting at the sensation of her efforts."
            "Lexi uses her lips, tongue and teeth to great effect."
            "And all I can do is keep a firm hold on Sasha the whole time."
            sasha.say "Lexi!"
            sasha.say "Lexi, you bitch!"
            sasha.say "That cock was mine!"
            mike.say "Uhh..."
            mike.say "Sasha..."
            mike.say "Y...you're next!"
            "As if fearing that she's going to be thrown off, Lexi redoubles her efforts."
            "I feel her squeezing my balls without mercy."
            mike.say "SHIT!"
            mike.say "LEXI!"
            menu:
                "Cum over Lexi and Sasha's faces":
                    "Never in my entire life have I wanted to have two cocks as I do right now!"
                    "If my cock goes off in either mouth or pussy, someone's getting a raw deal."
                    "So I figure that it's better to slightly disappoint them both, rather than thoroughly piss one of them off."
                    "Lexi stares at me in surprise as I pull my cock out of her mouth."
                    "And Sasha chooses that same moment to look back over her shoulder."
                    hide nightclub threesome
                    scene nightclub 3bj
                    show nightclub 3bj bedroom naked dick
                    with fade
                    "I barely enough time to maneuver both of them into position on the ground."
                    "And I manage this just in time, as I cum a moment later."
                    show nightclub 3bj cumshot with vpunch
                    "Lexi and Sasha wait patiently until I shoot my load."
                    with vpunch
                    "Then they close their eyes as it rains down on them."
                    show nightclub 3bj -cumshot cum -dick with vpunch
                    $ lexi.sub += 2
                    $ sasha.sub += 2
                    "Cum spatters across their cheeks and begins to run down their chins."
                    "And I can hear them giggling as they lick it off their lips."
                "Cum in her mouth":
                    "Lexi doesn't seem to hear a word I say."
                    "But then I realise that she's waiting for something to happen."
                    show nightclub threesome cum with vpunch
                    "A moment later I shoot my load with my cock in her mouth."
                    with vpunch
                    "Lexi swallows without any visible effort, taking it all in one go."
                    $ lexi.love += 2
                    show nightclub threesome -suck -cum with vpunch
                    "She greedily gulps down everything I have to give."
                    "And she doesn't let me go until the last drop is spent."
            sasha.say "Fucking hell, Lexi!"
            sasha.say "Are you done now?"
            sasha.say "Can I actually get some of that cock too?!?"
            $ lexi_bj = True
        "Go for Sasha":
            pass
    scene nightclub threesome
    show nightclub threesome bedroom sashanaked lexinaked mike lexi
    with fade
    menu:
        "Fuck her pussy":
            "Sasha's damn right."
            "What am I waiting for?"
            "I was the one wanting to assert myself here."
            "So that's exactly what I should be doing!"
            "Without another word, I thrust myself forwards."
            "There's no time to take careful aim."
            "But luckily for me, the target's straight ahead."
            sasha.say "Oh yeah..."
            sasha.say "That's what I'm talking about!"
            "Hearing Sasha's words as I stroke my cock along her lips seems to spark something in me."
            "Sure, it feels great on it's own - but knowing she loves it too makes it that much more intense!"
            "All it takes is a couple of passes like that."
            "Sasha's moans getting louder with each one."
            "Then I feel something begin to give way."
            "And a moment later, her pussy stops resisting me."
            show nightclub threesome vaginal sashamoan
            "I feel myself sinking straight into Sasha."
            "I try to keep it slow, wanting to savour the moment."
            "But her body seems to be hungry for it."
            "And I'm into her as deep as I can go before I can stop myself!"
            show nightclub threesome sashanormal
            sasha.say "Oh, [hero.name]..."
            sasha.say "It's...it's so big!"
            show nightclub threesome sashamoan
            sasha.say "Don't stop now..."
            sasha.say "Fuck me - please!"
            "Spurred on by Sasha's pleas, I leap into action."
            "Any thought of trying to assert myself vanishes in an instant."
            "Now all I want to do is please her, to make her wishes come true."
            "Because everything I do to that end gives me pleasure too."
            "Sasha seems helpless as I thrust in and out of her."
            "The sensation of my cock filling her overloading her senses."
            "But Lexi isn't enjoying any of that treatment."
            "So she devotes herself to getting off in different ways."
            "She flits between Sasha and me, like a sexual gadfly."
            "One moment she's playing with Sasha's breasts."
            show nightclub threesome sashanormal
            "The next she's pushing her breasts into my face."
            "All of which only serves to make us both more aroused than ever."
            "My fingers are digging into the soft flesh of Sasha's thighs."
            "So much so I'm worried I might leave behind bruises."
            "But that does nothing to lessen her ardour."
            "Sasha's practically slamming her ass into me by now."
            "Her buttocks are slapping against my thighs too!"
            show nightclub threesome sashamoan
            sasha.say "Oh..."
            sasha.say "Oh fuck..."
            sasha.say "Gonna...gonna cum!"
            "The breathless sound of desperation in Sasha's voice seals the deal."
            "And I can feel her taking me with her too!"
            menu:
                "Cum inside":
                    "I'm pounding away so hard and fast right now."
                    "There's no way I'm going to stop, even for a moment!"
                    "And so I keep right on thrusting into Sasha."
                    "That is until I finally lose it."
                    show nightclub threesome cum sashaahegao
                    $ sasha.love += 3
                    "Then I shoot my load as deep into her as I can."
                    "Sasha's back arches as she takes it."
                    "And I can feel the muscles of her pussy contracting as she cums too."
                "Cum in Lexi's mouth":
                    "As one final act of defiance, I pull my cock out of Sasha."
                    show nightclub threesome sashaahegao -anal
                    "I do this the moment before I shoot my load."
                    "Cum spurts the moment my cock is free."
                    show nightclub threesome suck cum
                    $ lexi.love += 3
                    "But instead of painting Sasha's back, it ends in Lexi's mouth."
                    "I didn't realize it, but as soon as my cock freed from Sasha's pussy, Lexi's mouth was already on it."
                    "So I ended up filling Lexi's mouth."
                    "Which doesn't seem to bother her at all."
                "Cum over Lexi and Sasha's faces":
                    "It doesn't seem fair to keep Lexi on the sidelines."
                    "So I resolve to get her in on this before it's too late."
                    hide nightclub threesome
                    scene nightclub 3bj
                    show nightclub 3bj bedroom naked dick
                    "Pulling my cock out of Sasha, I make her turn around."
                    "At the same time, I have Lexi kneel beside her."
                    "And I manage this just in time, as I cum a moment later."
                    show nightclub 3bj cumshot
                    $ sasha.love += 2
                    $ lexi.love += 2
                    "Lexi and Sasha wait patiently until I shoot my load."
                    "Then they close their eyes as it rains down on them."
                    show nightclub 3bj -cumshot cum -dick
                    "Cum spatters across their cheeks and begins to run down their chins."
                    "And I can hear them giggling as they lick it off their lips."
        "Fuck her ass":
            "Sasha's damn right."
            "What am I waiting for?"
            "I was the one wanting to assert myself here."
            "So that's exactly what I should be doing!"
            "Without another word, I thrust myself forwards."
            "There's no time to take careful aim."
            "But luckily for me, the target's straight ahead."
            sasha.say "Oh yeah..."
            sasha.say "That's what I'm talking about!"
            "Hearing Sasha's words as I stroke my cock along her lips seems to spark something in me."
            "Sure, it feels great on it's own - but knowing she loves it too makes it that much more intense!"
            "All it takes is a couple of passes like that."
            "Sasha's moans getting louder with each one."
            "Then I make up my mind."
            "I'm going to assert a little bit of control here."
            "So I angle my cock in a slightly different way."
            sasha.say "What are you..."
            show nightclub threesome sashamoan
            sasha.say "Ooh..."
            sasha.say "That's my ass!"
            show nightclub threesome sashanormal
            "I can't help smiling as I keep on pushing into her."
            "Then I feel something begin to give way."
            "And a moment later, her ass stops resisting me."
            show nightclub threesome anal sashamoan
            "I feel myself sinking straight into Sasha."
            "I try to keep it slow, wanting to savour the moment."
            "But her body seems to be hungry for it."
            "And I'm into her as deep as I can go before I can stop myself!"
            sasha.say "Oh, [hero.name]..."
            show nightclub threesome sashanormal
            sasha.say "It's...it's so big!"
            sasha.say "Don't stop now..."
            show nightclub threesome sashamoan
            sasha.say "Fuck me - please!"
            "Spurred on by Sasha's pleas, I leap into action."
            "Any thought of trying to assert myself vanishes in an instant."
            "Now all I want to do is please her, to make her wishes come true."
            "Because everything I do to that end gives me pleasure too."
            "Sasha seems helpless as I thrust in and out of her."
            "The sensation of my cock filling her overloading her senses."
            "But Lexi isn't enjoying any of that treatment."
            "So she devotes herself to getting off in different ways."
            "She flits between Sasha and me, like a sexual gadfly."
            show nightclub threesome sashanormal
            "One moment she's playing with Sasha's breasts."
            "The next she's pushing her breasts into my face."
            "All of which only serves to make us both more aroused than ever."
            "My fingers are digging into the soft flesh of Sasha's thighs."
            "So much so I'm worried I might leave behind bruises."
            "But that does nothing to lessen her ardour."
            "Sasha's practically slamming her ass into me by now."
            "Her buttocks are slapping against my thighs too!"
            show nightclub threesome sashamoan
            sasha.say "Oh..."
            sasha.say "Oh fuck..."
            sasha.say "Gonna...gonna cum!"
            "The breathless sound of desperation in Sasha's voice seals the deal."
            "And I can feel her taking me with her too!"
            menu:
                "Cum inside":
                    "I'm pounding away so hard and fast right now."
                    "There's no way I'm going to stop, even for a moment!"
                    "And so I keep right on thrusting into Sasha."
                    "That is until I finally lose it."
                    show nightclub threesome sashaahegao cum with hpunch
                    $ sasha.sub += 3
                    "Then I shoot my load as deep into her as I can."
                    with hpunch
                    "Sasha's back arches as she takes it."
                    with hpunch
                    "And I can feel the muscles of her ass contracting as she cums too."
                "Cum in Lexi's mouth":
                    "As one final act of defiance, I pull my cock out of Sasha."
                    show nightclub threesome sashaahegao -anal with hpunch
                    "I do this the moment before I shoot my load."
                    with hpunch
                    "Cum spurts the moment my cock is free."
                    show nightclub threesome suck cum with hpunch
                    $ lexi.sub += 3
                    "But instead of painting Sasha's back, it ends in Lexi's mouth."
                    "I didn't realize it, but as soon as my cock freed from Sasha's ass, Lexi's mouth was already on it."
                    "So I ended up filling Lexi's mouth."
                    "Which doesn't seem to bother her at all."
                "Cum over Lexi and Sasha's faces":
                    "It doesn't seem fair to keep Lexi on the sidelines."
                    "So I resolve to get her in on this before it's too late."
                    hide nightclub threesome
                    scene nightclub 3bj
                    show nightclub 3bj bedroom naked dick
                    with hpunch
                    "Pulling my cock out of Sasha, I make her turn around."
                    "At the same time, I have Lexi kneel beside her."
                    "And I manage this just in time, as I cum a moment later."
                    show nightclub 3bj cumshot with vpunch
                    $ sasha.sub += 2
                    $ lexi.sub += 2
                    "Lexi and Sasha wait patiently until I shoot my load."
                    with vpunch
                    "Then they close their eyes as it rains down on them."
                    show nightclub 3bj -cumshot cum -dick with vpunch
                    "Cum spatters across their cheeks and begins to run down their chins."
                    "And I can hear them giggling as they lick it off their lips."
            $ sasha.flags.anal += 1
    if not lexi_bj:
        lexi.say "Hey!"
        lexi.say "What about me?!?"
        "Lexi almost vaults onto Sasha's back."
        "She lands facing me, both hands grabbing my cock."
        "And then she lunges forwards and takes in into her mouth!"
        show nightclub threesome bedroom sashanaked lexinaked mike lexi suck
        sasha.say "Wha..."
        sasha.say "What's happening?!?"
        mike.say "Lexi..."
        mike.say "I'm running on fumes here!"
        mike.say "Oh fuck!"
        mike.say "Mmm..."
        "Sasha's protests come too late to do any good."
        "Because Lexi's already well into it."
        "And I'm not about to stop her when she's sucking my cock!"
        "Lexi doesn't waste any time either."
        "Probably fearing Sasha collapsing beneath her, she's straight down to business."
        "Her head is going up and down at an almost alarming rate."
        "But that doesn't seem to be doing anything to affect the quality of her performance."
        "I'm soon gasping and panting at the sensation of her efforts."
        "Lexi uses her lips, tongue and teeth to great effect."
        "And all I can do is keep a firm hold on Sasha the whole time."
        sasha.say "Lexi!"
        sasha.say "Lexi, you're going to break my back!"
        mike.say "Uhh..."
        mike.say "Lexi..."
        mike.say "How the fuck?"
        mike.say "I'm going to cum again!"
        "As if fearing that she's going to be thrown off, Lexi redoubles her efforts."
        "I feel her squeezing my balls without mercy."
        mike.say "SHIT!"
        mike.say "LEXI!"
        menu:
            "Cum over Lexi and Sasha's faces":
                "Never in my entire life have I wanted to have two cocks as I do right now!"
                "If my cock goes off in either mouth or pussy, someone's getting a raw deal."
                "So I figure that it's better to slightly disappoint them both, rather than thoroughly piss one of them off."
                "Lexi stares at me in surprise as I pull my cock out of her mouth."
                "And Sasha chooses that same moment to look back over her shoulder."
                hide nightclub threesome
                scene nightclub 3bj
                show nightclub 3bj bedroom naked dick
                with hpunch
                "I barely enough time to maneuver both of them into position on the ground."
                "And I manage this just in time, as I cum a moment later."
                show nightclub 3bj cumshot with vpunch
                "Lexi and Sasha wait patiently until I shoot my load."
                with vpunch
                "Then they close their eyes as it rains down on them."
                show nightclub 3bj -cumshot cum -dick with vpunch
                $ lexi.love += 2
                $ sasha.love += 2
                "Cum spatters across their cheeks and begins to run down their chins."
                "And I can hear them giggling as they lick it off their lips."
            "Cum in her mouth":
                "Lexi doesn't seem to hear a word I say."
                "But then I realise that she's waiting for something to happen."
                "A moment later I shoot my load with my cock in her mouth."
                show nightclub threesome cum with vpunch
                $ lexi.love += 3
                "Lexi swallows without any visible effort, taking it all in one go."
                with vpunch
                "She greedily gulps down everything I have to give."
                with vpunch
                "And she doesn't let me go until the last drop is spent."
    scene bg bedroom1
    show multisleep homeharem sasha lexi
    with fade
    "Afterwards, all three of us are spent."
    "All we can do is lie on the bed in a tangle of limbs."
    "There's no need to speak a word."
    "And I doubt any of us could if we tried."
    "So we just lie there, enjoying the sensation of a three-way afterglow."
    $ sasha.sexperience += 1
    $ lexi.sexperience += 1
    return

label lexi_sasha_alternative_nightclub:
    scene bg nightclub at center, zoomAt(1.25, (480, 880))
    show layer master at lparty
    with fade
    "I don't recall which one of us came up with the idea to hit a club tonight."
    "And likewise I'm more than a little hazy as to just which one we've ended up in too."
    "Even the music that's playing right now escapes me, and I'm already on the dance-floor."
    show sasha sexydate zorder 1 at center, zoomAt(1.25, (640, 880)), slide(45, 1.5) with dissolve
    "The reason for all of this is that I'm totally fixated on Sasha."
    "She's been commanding every last ounce of my attention all night."
    "And now that she's moving in time to the music, I feel almost hypnotised."
    "Neither of us speaks as we dance together, not needing words to communicate."
    show sasha at center, traveling(1.35, 1.0, (640, 920)), slide(45, 1.5)
    "Sasha leads and I follow, but that's fine by me."
    "I'm more than a little under the influence, and perfectly happy to be led."
    "And Sasha seems to be enjoying the chance to make me dance to her tune."
    "Every move that she makes keeps me on my toes, hurrying to follow her."
    show sasha at center, traveling(1.25, 1.0, (640, 880)), slide(45, 1.5)
    "But somehow she manages to stay forever just out of reach."
    "In this manner, the dance soon becomes a constant tease."
    "Sasha tempts me with the offer of her body, and I eagerly take the bait."
    "And then she deftly twists and turns, keeping my hands off of her."
    "This goes on for what feels like an eternity, time meaning nothing to my clouded senses."
    "But then I feel the presence of something else entering into our shared orbit."
    "My impaired brain has already begun to imagine Sasha as some kind of sexy goddess."
    "One that's dark and sensual, but always slightly out of reach."
    show sasha at center, traveling(1.25, 1.0, (840, 880)), slide(45, 1.5)
    "Now we're joined on the dance-floor by something that feels more like a debauched deity."
    "A goddess of pure lust, and one that exudes her pheromones without knowing shame."

    $ previous_sexy = lexi.flags.sexydate
    $ previous_slutty = lexi.flags.sluttydate
    $ lexi.flags.sexydate = False
    $ lexi.flags.sluttydate = False
    show lexi date nophone zorder 2 at center, zoomAt(1.25, (440, 880)), slide(45, 1.5) with easeinleft
    "It's Lexi, of course - who else?"
    "By the way, apologies for all of the flowery descriptions I'm using here."
    "But I'm already pretty far gone, and that's the only excuse I can offer..."
    "Where Sasha was happy to lead me on a merry dance, Lexi's not nearly so coy."
    show lexi at center, traveling(1.5, 1.0, (440, 1000)), slide(30, 1.0)
    "Without even bothering to say hello, she's pressed up against me as close as she can manage."
    "Shit - she's even straddling my thigh, shamelessly rubbing herself up and down!"
    "In my impaired state, I can't help but be drawn towards her and away from Sasha."
    "I'm like a guy being tempted away from a steak dinner by the smell of a dirty burger..."
    show sasha zorder 3 at center, traveling(1.5, 1.0, (840, 1000)), slide(30, 1.0)
    "But before I can forget that Sasha's even there, she steps between Lexi and me."
    "She's not so crude as to simply push Lexi out of the way."
    "So instead she begins to play the other girl at her own game."
    "And that's how I find myself with one of them working away on each leg."
    "My head flicks this way and that, trying to watch both of the girls at once."
    "It's impossible to choose between them, or say that one's sexier than the other."
    "Lexi just drips with unashamed lust, making me want her like crazy."
    "But now that Sasha's kicked it up a notch, she's making me painfully hard too."
    "In fact, if this goes on much longer, I'm going to cum in my shorts!"
    show sasha embarrassed
    show lexi wink
    "It's then that I see a glance exchanged between Lexi and Sasha."
    "No words are spoken, but each seems to understand the other perfectly."
    show sasha normal blush
    show lexi smile blush
    "And then, just like that, they're united in their efforts."
    "Like a couple of over-sexed snakes, they begin to wrap themselves around me."
    scene bg nightclub
    show 3dance_mike
    show 3dance_girl_lexi at slide(10, 0.9)
    if lexi.is_visibly_pregnant:
        show 3dance_pregnancy_lexi_pregnant at slide(10, 0.9)
    if lexi.is_collared:
        show 3dance_collars_lexi_collar at slide(10, 0.9)
    show 3dance_girl_sasha at slide(10, 0.8)
    if sasha.is_visibly_pregnant:
        show 3dance_pregnancy_sasha_pregnant at slide(10, 0.8)
    if sasha.is_collared:
        show 3dance_collars_sasha_collar at slide(10, 0.8)
    if sasha.flags.boobjob:
        show 3dance_sasha_boobjob at slide(10, 0.8)
    if sasha.flags.haircut:
        show 3dance_haircuts_sasha_haircut at slide(10, 0.8)
    show layer master at lparty
    with fade
    "Lexi and Sasha circle me, as close as they possibly can."
    "Their hands caress, stroke and squeeze the whole time."
    with vpunch
    "And in no time at all, I lose control."
    "I stand on the dance-floor, gasping for breath and glad to have worn dark pants."
    "Even over the sound of the pounding music, I can hear Lexi and Sasha as they laugh at my predicament..."
    $ lexi.flags.sexydate = previous_sexy
    $ lexi.flags.sluttydate = previous_slutty
    return
































label bree_lexi_pregnant_showdown:
    show bree zorder 2 at center
    hide lexi
    with fade
    show lexi bubblegum zorder 1 at right with easeinright
    "I'm chatting with [bree.name] about everything and nothing when Lexi happens to walk by."
    show lexi at left4 with ease
    pause 0.1
    show bree annoyed
    "For a moment, [bree.name] stops talking and gives the other girl a really hard look."
    show lexi at left5 with ease
    "I can instantly feel my buttocks clenching as she does so."
    show lexi at left with ease
    "Because so far I've managed to keep a lid on the fact that I'm fucking both of them."
    show lexi at top_mostleft with ease
    "And one of the most important things about that is making sure I keep them apart."
    "So having [bree.name] staring a hole through Lexi right now isn't ideal!"
    hide lexi with easeoutleft
    show bree angry
    bree.say "Urgh..."
    show bree evil
    bree.say "That girl is SUCH trash!"
    bree.say "She looks like she's pregnant."
    show bree angry
    bree.say "And I bet she has no idea who the father is too!"
    mike.say "Erm..."
    mike.say "You might want to keep your voice down, [bree.name]!"
    show bree surprised at right4 with ease
    "Bree turns to look at me, surprise written all over her face."
    bree.say "And just why would I care about that tramp hearing me?"
    lexi.say "You'd better care about it, [bree.name]!"
    lexi.say "Because this tramp sure as hell CAN hear you!"
    show bree annoyed at right5
    show lexi annoyed nophone at left5
    with hpunch
    "I turn around to see Lexi standing beside us."
    "She has a frown on her face and her arms crossed over her chest."
    "All of which seems to mean she's ready to make trouble!"
    mike.say "Girls, girls, girls..."
    mike.say "There's no need for this!"
    mike.say "Surely there isn't?"
    "Both [bree.name] and Lexi snort at this."
    "But it's [bree.name] that gets in there first."
    bree.say "What's she getting mad for, [hero.name]?"
    show bree angry
    bree.say "All I did was state the obvious."
    bree.say "She's pregnant and she's a whore!"
    bree.say "You can't disagree with that!"
    "Before I can say another word, Lexi fires back."
    show lexi angry
    lexi.say "Are you really going to let her talk to me like that?"
    lexi.say "Aren't you going to defend me?"
    lexi.say "Aren't you going to defend the baby?!?"
    show lexi annoyed
    show bree evil
    bree.say "Why would he do that?"
    bree.say "I doubt you know who's kid that is."
    bree.say "So he definitely doesn't!"
    show bree annoyed
    "Everything from this point on seems to happen in slow-motion."
    "And there's nothing I can do to stop it!"
    show lexi angry
    lexi.say "Of course I know who the father is!"
    lexi.say "And so does [hero.name] - because it's him!"
    show lexi annoyed
    show bree surprised
    "Bree's mouth drops open and she turns to face me."
    bree.say "She's talking shit, right?"
    bree.say "[hero.name], tell me she's lying!"
    bree.say "You can't have been fucking her while we were in a serious relationship!"
    "Now it's Lexi's turn to get mad."
    show lexi angry
    lexi.say "Whoa, whoa, whoa..."
    lexi.say "WE'RE the ones in a relationship here!"
    lexi.say "He must have been fucking you on the side!"
    show lexi annoyed
    "Now they're both staring at me, their expressions demanding an explanation."
    mike.say "Okay, okay..."
    mike.say "You got me..."
    mike.say "I've been seeing you both at the same time."
    mike.say "And now you've found out - so I guess it's all over!"
    "I look from [bree.name] to Lexi, expecting them to confirm my statement."
    "But much to my surprise, it looks like there's doubt in their eyes!"
    if bree.love >= 125 and lexi.love >= 125:
        show bree annoyed
        bree.say "I...know this sounds weird."
        bree.say "But I forgive you, [hero.name]."
        show bree normal
        bree.say "You're only human, and we all make mistakes."
        show lexi angry
        lexi.say "You know what, [bree.name]..."
        show lexi normal
        lexi.say "You're right!"
        lexi.say "And maybe we can work all of this out."
        "The girls leave me stunned with their answers."
        "I was sure they'd both dump my ass in a heartbeat."
        "But they seem to be working it out before my very eyes!"
        mike.say "I mean...sure..."
        mike.say "Of course we can work it out!"
        mike.say "I love you both, really I do!"
        show lexi at left4
        show bree at right4
        with ease
        "Bree and Lexi are glancing at each other as I say all of this."
        "And it's almost like they're sizing each other up too!"
        bree.say "Well..."
        bree.say "I'll give it a go if you will, Lexi?"
        lexi.say "Same here, [bree.name]."
        "I nod and smile the whole time."
        "Partly because I'm eager to avoid conflict."
        "And partly because I can't believe my luck."
        "Two girls at once!"
        "And they're both cool with it too!"
    elif lexi.love > bree.love and lexi.love >= 100:
        show lexi angry
        show bree annoyed
        lexi.say "Come on, [bree.name]..."
        show lexi normal
        lexi.say "We're only human, all of us!"
        lexi.say "[hero.name] just made a mistake is all."
        "Lexi's answer leaves me speechless."
        "I was sure she'd be the first one to dump my ass!"
        "But her answer seems to make [bree.name] even more angry."
        show bree angry
        bree.say "You're the mistake, Lexi!"
        bree.say "You're one huge, walking mistake!"
        bree.say "And you two deserve each other!"
        mike.say "Bree, please..."
        mike.say "Let's talk about this, yeah?"
        mike.say "I'm sure we can work it out!"
        hide bree with easeoutright
        "Bree turns on her heel and begins to walk away."
        "All the time ignoring my pleas for us to talk."
        $ bree.set_gone_forever()
        $ Room.find("bedroom2").hide()
    elif bree.love > lexi.love and bree.love >= 100:
        show bree annoyed
        bree.say "I...know this sounds weird."
        bree.say "But I forgive you, [hero.name]."
        show bree normal
        bree.say "You're only human, and we all make mistakes."
        "Bree's answer leaves me speechless."
        "I was sure she'd be the first one to dump my ass!"
        "But her answer seems to make Lexi even more angry."
        show lexi angry
        lexi.say "Yeah, well - he already made a mistake when he got me pregnant!"
        lexi.say "And he's making another if he doesn't kick you to the kerb!"
        show lexi annoyed
        mike.say "Lexi, please..."
        mike.say "Let's talk about this, yeah?"
        mike.say "I'm sure we can work it out!"
        hide lexi at left with ease
        "Lexi turns on her heel and begins to walk away."
        lexi.say "Nah, I think I'll pass!"
        lexi.say "You two deserve each other!"
        hide lexi with easeoutleft
        $ lexi.set_gone_forever()
    else:
        show bree angry
        bree.say "Screw the both of you!"
        bree.say "I never want to see you again!"
        show bree b at center, zoomAt(1.5, (680, 1000))
        play sound spank
        pause 0.2
        with screenshot
        with hpunch
        "Bree underlines this by slapping me hard in the face."
        hide bree with easeoutright
        "And then she storms off, leaving me reeling from the slap."
        "But just as I'm starting to regain my balance, it happens again!"
        show lexi b at center, zoomAt(1.5, (680, 1000))
        play sound spank
        pause 0.2
        with screenshot
        with hpunch
        "Lexi slaps me from the opposite direction."
        show lexi angry
        lexi.say "You made a mistake when you got me pregnant."
        lexi.say "But you really blew it when you went behind my back!"
        "Lexi follows [bree.name]'s example."
        hide lexi with easeoutleft
        "Only she storms off in the opposite direction."
        "Which leaves me standing alone."
        "My cheeks stinging from the slaps."
        "And my head spinning from losing the both of them."
        $ lexi.set_gone_forever()
        $ bree.set_gone_forever()
        $ Room.find("bedroom2").hide()
    return

label bree_lexi_minami_sasha_male_ending:
    $ game.room = "church"
    scene bg church wedding
    with fade
    "It's hard to square the impression I had of Lexi when we first met with where we are now."
    "Even harder to believe that she's turned out to be the girl I'm about to marry!"
    "It was hard enough to get to grips with the fact that I managed to hook up with [bree.name] or Sasha."
    "So it felt crazy to become involved with the pair of them at the same time."
    "But then who'd have thought I'd be marrying my former adopted sister too!"
    "But instead she wound up getting in on the action too, which none of us saw coming."
    "I glance back over my shoulder at the chapel filled with all of our guests."
    "They're an interesting bunch of people to be sure, from all walks of life."
    "But it reassures me to see that the place is pretty much full."
    "That and the fact that all I see are smiling faces too."
    "It's at that moment the music starts to play, filling the chapel."
    "And on cue, all of the guests get to their feet as one."
    "I'm still looking back as the bridal procession appears in the aisle..."
    show lexi wedding normal nophone at center, zoomAt (1.0, (1020, 730)) with dissolve
    "Lexi, the girl that I've always thought of as the princess of the trailer park."
    "Well, let's just say she looks more like a princess than ever."
    "She'll always be trash."
    "But who knew that trash could look so good?"
    show bree wedding normal at center, zoomAt (1.0, (260, 730)) with dissolve
    "[bree.name]'s dress is perhaps the closest to the traditional, being white and floaty."
    "But somehow she manages to make it come alive with the warmth of her smile."
    show sasha wedding normal at center, zoomAt (1.0, (500, 730)) with dissolve
    "Sasha is almost the exact opposite, clad in black that contrasts her pale skin."
    "She's every bit as mysterious and intriguing as [bree.name] is open and honest."
    show minami wedding normal at center, zoomAt (1.0, (780, 730)) with dissolve
    "Next comes Minami, the shortest of the four, but the most bursting with life."
    "Her dress is made of traditional, patterned silk."
    "But the cut is modern and quirky, just like her."
    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and minami.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of four large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not minami.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha, Minami and Lexi as they stand beside me at the altar."
        "My four brides - soon to be my four wives!"
    else:
        if bree.is_visibly_pregnant:
            "[bree.name]'s dress looks like it's performing a minor miracle."
            "Her bump is getting huge, but I can hardly see it right now!"
            "Not that either of us wants to hide the fact she's expecting."
        if sasha.is_visibly_pregnant:
            "Sure, Sasha has a lot of make-up on today, but she's looking pale under it all."
            "For a moment I worry that she's not doing well, glancing at her swollen belly."
            "She seems to note my concern, nodding and smiling to assure me that she's okay."
        if minami.is_visibly_pregnant:
            "Minami's dress could never hope to hide the fact that she's pregnant."
            "And I guess that's because she's more than proud to show off the fact."
            "She's crazily happy to be carrying my baby, and I feel the same way too!"
        if lexi.is_visibly_pregnant:
            "It's a cliche for a trailer park girl to be sporting a swollen belly."
            "But somehow it just serves to make Lexi look all the more desirable, at least in my eyes."
            "She carries it so well that I just know she's going to make a wonderful mother."
    "There's barely enough time for the five of us to exchange glances and nervous smiles."
    "And that's because the priest leaps into the ceremony almost as soon as the music come to an end."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these FIVE people in the bonds of holy matrimony!"
    "The priest's tone is a little exasperated, but more amused than anything."
    "And there's an appreciative ripple of laughter from the assembled guests too."
    show bree wedding flirt blush
    show minami wedding normal blush
    "Even the five of us share a round of giggles and laughter, some cheeks flushing too."
    "Sure, this is all legal now, but it's still pretty new for all concerned."
    "I guess this is just part of the journey to it becoming part of the new normal."
    "The priest dives into the task ahead, doing the best he can to keep up."
    "Before too long, we're already at the point where we're making our vows!"
    "Priest" "Do you, [bree.name], take Sasha, Minami, Lexi and [hero.name], to be your lawful, wedded partners?"
    show bree wedding happy -blush at startle
    bree.say "Oh, I do!"
    "Priest" "Do you, Sasha, take [bree.name], Minami, Lexi and [hero.name], to be your lawful, wedded partners?"
    show sasha wedding happy at startle
    sasha.say "Yeah, I do."
    "Priest" "Do you, Minami, take [bree.name], Sasha, Lexi and [hero.name], to be your lawful, wedded partners?"
    show minami wedding happy at startle
    minami.say "I sure do!"
    "Priest" "Do you, Lexi, take [bree.name], Sasha, Minami and [hero.name], to be your lawful, wedded partners?"
    show lexi wedding happy at startle
    lexi.say "Hell yeah, I do!"
    "The priest makes a dramatic pause, filling his lungs for the final push."
    "Priest" "And do you, [hero.name], take [bree.name], Sasha, Minami and Lexi, to be your lawful, wedded partners?"
    "Now it's my turn to take an equally deep breath before answering."
    mike.say "I do."
    "The priest nods, clearly happy to be reaching the end of the ceremony."
    "Priest" "If anyone present knows of any lawful reason these five may not be joined in holy matrimony..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "There's the usual pause and nervous laughter as he surveys the crowd."
    "I can't help feeling nervous as the seconds seem to stretch on."
    "Any moment I expect the doors to fly open to reveal [bree.name]'s dad, Scottie, Danny or my own parents."
    "I can even imagine an unholy alliance of all five of them, united in their desire to derail our wedding!"
    "But nobody leaps to their feet to call a halt to the proceedings."
    "Priest" "The I hereby pronounce you husband and wives."
    "Priest" "You may kiss the brides."
    "Priest" "Or each other..."
    "Priest" "I'm not sure how this bit is supposed to work!"
    show sasha at center, traveling (1.3, 1.0, (500, 880))
    show bree at center, traveling (1.3, 1.0, (260, 880))
    show minami at center, traveling (1.3, 1.0, (780, 880))
    show lexi at center, traveling (1.3, 1.0, (1020, 880))
    "Neither are we, and so we come together in a kind of group hug."
    "We exchange kisses with each other, each one as passionate as the last."
    "And we did it - the five of us actually managed to tie the knot!"
    "We're not doing this behind closed doors anymore - we're a fivesome in the eyes of the law!"

    scene home ending
    show home ending sasha
    with fade
    sasha.say "Don't sweat it, guys."
    sasha.say "I've got this one."
    show home ending bree with dissolve
    bree.say "Huh - what does that mean?"
    sasha.say "Well, I was the first to move in with [hero.name]."
    sasha.say "That means I've known him the longest."
    bree.say "Ah...no way, Sasha!"
    bree.say "There's like a couple of days in it at the most."
    bree.say "And [hero.name] hit if off with me before you!"
    show home ending minami with dissolve
    minami.say "Erm, hello - adorably spunky and cute little sister here!"
    minami.say "None of you guys have known big bro as long as I have."
    show home ending lexi with dissolve
    lexi.say "That's sweet, Minami."
    lexi.say "But did he rescue you from the clutches of a bad guy?"
    lexi.say "[hero.name] kicked that piece of shit's ass."
    lexi.say "And he did it all for me!"
    minami.say "Urgh..."
    minami.say "I've heard that story like a hundred times already!"
    lexi.say "Okay, okay - but my story's still awesome."
    sasha.say "Yeah, you got me there, Lexi."
    sasha.say "It is a lot more fun with four other people to make it up to!"
    bree.say "Oh yeah!"
    minami.say "Totally!"
    lexi.say "Only four people?"
    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and minami.is_visibly_pregnant and sasha.is_visibly_pregnant:
        bree.say "Are we still technically a fivesome?"
        sasha.say "Yeah, we might have accidentally become a tribe somewhere along the way!"
        sasha.say "[hero.name] could be the founder of a whole new nation."
        lexi.say "Ah...weird!"
        minami.say "No - that's sweet."
        minami.say "But please don't tell big bro that."
        lexi.say "I agree - his head's big enough as it is!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not minami.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "Yeah, always room for more!"
        lexi.say "Squeeze a couple in there, huh?"
        minami.say "Erm...is someone else moving in?"
        sasha.say "She means the patter of tiny feet, Minami!"
        bree.say "You know - babies?"
        minami.say "Oh..."
    else:
        if bree.is_visibly_pregnant:
            bree.say "Yeah - don't forget Poppy."
            bree.say "She's loud enough to count for two!"
        if minami.is_visibly_pregnant:
            minami.say "I sometimes forget that Mei's just my kid."
            minami.say "You guys are so good with her and she loves you all so much!"
        if sasha.is_visibly_pregnant:
            sasha.say "Dahlia's a tearaway, I know."
            sasha.say "But what do you expect from a kid with five moms!"
        if lexi.is_visibly_pregnant:
            lexi.say "Chantel and Tyrone make it feel like there's four of them, let alone two!"
            lexi.say "Good job there are so many pairs of hands to throw in."

    bree.say "It would have been nice to be able to stay in the old house."
    bree.say "You know, where all of this got started?"
    sasha.say "Nah, it was getting cramped when there were only three of us!"
    sasha.say "That's why we ended up pooling our resources for a new place."
    minami.say "And I LOVE our place in the suburbs - it has everything!"
    lexi.say "I still think we should have bought a couple of trailers."
    lexi.say "We could have claimed most of the park where I was living..."
    minami.say "Oh, Lexi - don't start with that again!"
    bree.say "Anyway, it doesn't matter where we're living."
    bree.say "What matters is that we're all together."
    lexi.say "Yeah, and that we outnumber [hero.name] four to one!"
    sasha.say "Poor guy - I almost feel sorry for him!"
    minami.say "Oh, don't be silly."
    minami.say "Big bro loves it really!"
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label bree_lexi_samantha_sasha_male_ending:
    $ game.room = "church"
    scene bg church wedding
    with fade
    "You know, some days it feels like the most normal and natural thing in the world to be marrying four girls."
    "I mean it's legal, we're all consenting adults that are more or less sane, and nobody's being blackmailed into it."
    "But on the other hand, I can sometimes find myself feeling like the leader of some crazy sex cult too!"
    "It was hard enough to get to grips with the fact that I managed to hook up with [bree.name] or Sasha."
    "So it felt crazy to become involved with the pair of them at the same time."
    "Likewise I'd written Sam off as the one that got away."
    "After all, she was married and I was spoken for three times over."
    "Yet somehow she not only found out about the threesome I had going, but joined it too!"
    "And then there was Lexi..."
    "Wow..."
    "How do you factor someone like Lexi into any picture?"
    "Let alone how do you fit her into what was going on between me and four other girls?"
    "But somehow she just seemed to slot right in there, like it was meant to be!"
    "And there was no need to sugar-coat it for her either."
    "Lexi just jumped straight in there and took to the whole thing like a duck to water!"
    "In the end, it all worked out well."
    "So well, in fact, that we decided to make it official."
    "Which is how I come to be here."
    "Standing at the altar and waiting for four brides to walk down the aisle!"
    "Even when the music begins to play, it still doesn't quite feel real."
    "And I actually consider pinching myself just to check I'm not dreaming."
    "But what snaps me out of it in the end is the sight of the girls coming towards me."
    show bree wedding normal at center, zoomAt (1.0, (260, 730))
    show sasha wedding normal at center, zoomAt (1.0, (500, 730))
    show samantha wedding normal at center, zoomAt (1.0, (780, 730))
    show lexi wedding normal nophone at center, zoomAt (1.0, (1020, 730))
    with dissolve
    "[bree.name], Sasha, Sam and Lexi walk down the aisle together."
    "They come in a loose knot, rather than turning it into some kind of procession."
    "This means that they look like a group of friends and equals, for which I'm glad."
    "Because them trooping up one after another would have made this feel a little too weird!"
    "They chose to keep their dresses under wraps while we were planning all of this."
    "And so I'm seeing them for the very first time as they walk towards me."
    "Every one of them is different, their choices a perfect reflection of their personalities."
    show bree happy
    "[bree.name]'s dress is perhaps the closest to the traditional, being white and floaty."
    "But somehow she manages to make it come alive with the warmth of her smile."
    show sasha happy
    "Sasha is almost the exact opposite, clad in black that contrasts her pale skin."
    "She's every bit as mysterious and intriguing as [bree.name] is open and honest."
    show samantha happy
    "Sure, I've seen Sam in a wedding dress before now."
    "Though I find myself forgetting that mental image as soon as I see her in this one."
    "Somehow she looks a million times better from the altar than from amongst the guests!"
    show lexi happy
    "And Lexi, the girl that I've always thought of as the princess of the trailer park."
    "Well, let's just say she looks more like a princess than ever."
    "She'll always be trash."
    "But who knew that trash could look so good?"
    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of four large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha, Sam and Lexi as they stand beside me at the altar."
        "My four brides - soon to be my four wives!"
    else:
        if bree.is_visibly_pregnant:
            "[bree.name]'s dress looks like it's performing a minor miracle."
            "Her bump is getting huge, but I can hardly see it right now!"
            "Not that either of us wants to hide the fact she's expecting."
        if sasha.is_visibly_pregnant:
            "Sure, Sasha has a lot of make-up on today, but she's looking pale under it all."
            "For a moment I worry that she's not doing well, glancing at her swollen belly."
            "She seems to note my concern, nodding and smiling to assure me that she's okay."
        if samantha.is_visibly_pregnant:
            "One thing's very different to the last time I saw Sam in a wedding dress."
            "And that's the fact that she's visibly pregnant."
            "But then I guess that, based on how her last marriage turned out, the difference can only be a good thing!"
        if lexi.is_visibly_pregnant:
            "It's a cliche for a trailer park girl to be sporting a swollen belly."
            "But somehow it just serves to make Lexi look all the more desirable, at least in my eyes."
            "She carries it so well that I just know she's going to make a wonderful mother."
    "There's barely enough time for the five of us to exchange glances and nervous smiles."
    "And that's because the priest leaps into the ceremony almost as soon as the music come to an end."
    show bree normal
    show sasha normal
    show samantha normal
    show lexi normal
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these FIVE people in the bonds of holy matrimony!"
    "The priest's tone is a little exasperated, but more amused than anything."
    "And there's an appreciative ripple of laughter from the assembled guests too."
    show bree wedding flirt blush
    show samantha wedding flirt
    "Even the five of us share a round of giggles and laughter, some cheeks flushing too."
    "Sure, this is all legal now, but it's still pretty new for all concerned."
    "I guess this is just part of the journey to it becoming part of the new normal."
    "The priest dives into the task ahead, doing the best he can to keep up."
    "Before too long, we're already at the point where we're making our vows!"
    "Priest" "Do you, [bree.name], take Sasha, Sam, Lexi and [hero.name], to be your lawful, wedded partners?"
    show bree wedding happy -blush at startle
    bree.say "Oh, I do!"
    "Priest" "Do you, Sasha, take [bree.name], Sam, Lexi and [hero.name], to be your lawful, wedded partners?"
    show sasha wedding happy at startle
    sasha.say "Yeah, I do."
    "Priest" "Do you, Sam, take [bree.name], Sasha, Lexi and [hero.name], to be your lawful, wedded partners?"
    show samantha wedding happy at startle
    samantha.say "I do."
    "Priest" "Do you, Lexi, take [bree.name], Sasha, Sam and [hero.name], to be your lawful, wedded partners?"
    show lexi wedding happy at startle
    lexi.say "Hell yeah, I do!"
    "The priest makes a dramatic pause, filling his lungs for the final push."
    "Priest" "And do you, [hero.name], take [bree.name], Sasha, Sam and Lexi, to be your lawful, wedded partners?"
    "Now it's my turn to take an equally deep breath before answering."
    mike.say "I do."
    "The priest nods, clearly happy to be reaching the end of the ceremony."
    "Priest" "If anyone present knows of any lawful reason these five may not be joined in holy matrimony..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "There's the usual pause and nervous laughter as he surveys the crowd."
    "I can't help feeling nervous as the seconds seem to stretch on."
    "Any moment I expect the doors to fly open to reveal [bree.name]'s dad, Scottie, Danny or Ryan."
    "I can even imagine an unholy alliance of all four of them, united in their desire to derail our wedding!"
    "But nobody leaps to their feet to call a halt to the proceedings."
    "Priest" "The I hereby pronounce you husband and wives."
    "Priest" "You may kiss the brides."
    "Priest" "Or each other..."
    "Priest" "I'm not sure how this bit is supposed to work!"
    show sasha at center, traveling (1.3, 1.0, (500, 880))
    show bree at center, traveling (1.3, 1.0, (260, 880))
    show samantha at center, traveling (1.3, 1.0, (780, 880))
    show lexi at center, traveling (1.3, 1.0, (1020, 880))
    "Neither are we, and so we come together in a kind of group hug."
    "We exchange kisses with each other, each one as passionate as the last."
    "And we did it - the five of us actually managed to tie the knot!"
    "We're not doing this behind closed doors anymore - we're a fivesome in the eyes of the law!"

    scene home ending
    show home ending sasha
    with fade
    sasha.say "Don't sweat it, guys."
    sasha.say "I've got this one."
    show home ending bree with dissolve
    bree.say "Huh - what does that mean?"
    sasha.say "Well, I was the first to move in with [hero.name]."
    sasha.say "That means I've known him the longest."
    bree.say "Ah...no way, Sasha!"
    bree.say "There's like a couple of days in it at the most."
    bree.say "And [hero.name] hit if off with me before you!"
    show home ending samantha with dissolve
    samantha.say "Are you two for real?"
    samantha.say "I was living with [hero.name] before you were even in the picture!"
    samantha.say "And he was hung up on me from the moment that I moved out too."
    show home ending lexi with dissolve
    lexi.say "That's sweet, Sam."
    lexi.say "But did he rescue you from the clutches of a bad guy?"
    lexi.say "[hero.name] kicked that piece of shit's ass."
    lexi.say "And he did it all for me!"
    samantha.say "This isn't getting us anywhere."
    samantha.say "We're supposed to be telling our side of the story."
    samantha.say "How we're all living happily ever after, yeah?"
    sasha.say "You're right, Sam."
    bree.say "Yeah, I guess so."
    lexi.say "Okay, okay - but my story's still awesome."
    samantha.say "Ah, it's alright."
    samantha.say "I guess we're going to be on different pages sometimes."
    samantha.say "There are five of us involved in this relationship after all!"
    lexi.say "There's five of us for now!"
    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        bree.say "Are we still technically a fivesome?"
        sasha.say "Yeah, we might have accidentally become a tribe somewhere along the way!"
        sasha.say "[hero.name] could be the founder of a whole new nation."
        lexi.say "Ah...weird!"
        samantha.say "Don't tell [hero.name] - his head's big enough as it is!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "Yeah, always room for more!"
        lexi.say "Squeeze a couple in there, huh?"
    else:
        if bree.is_visibly_pregnant:
            bree.say "Yeah - don't forget Poppy."
            bree.say "She's loud enough to count for two!"
        if sasha.is_visibly_pregnant:
            sasha.say "Dahlia's a tearaway, I know."
            sasha.say "But what do you expect from a kid with five moms!"
        if samantha.is_visibly_pregnant:
            samantha.say "Ha...Jemima's already got us all wrapped around her finger."
            samantha.say "I hate to think what she'll be like when she's older!"
        if lexi.is_visibly_pregnant:
            lexi.say "Chantel and Tyrone make it feel like there's four of them, let alone two!"
            lexi.say "Good job there are so many pairs of hands to throw in."
    bree.say "It would have been nice to be able to stay in the old house."
    bree.say "You know, where all of this got started?"
    sasha.say "Nah, it was getting cramped when there were only three of us!"
    samantha.say "That's why we ended up pooling our resources for a new place."
    lexi.say "I still think we should have bought a couple of trailers."
    lexi.say "We could have claimed most of the park where I was living..."
    samantha.say "Anyway, it doesn't matter where we're living."
    samantha.say "What matters is that we're all together."
    bree.say "Yeah, and that we outnumber [hero.name] four to one!"
    sasha.say "Poor guy - I almost feel sorry for him!"
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label bree_lexi_sasha_male_ending:
    $ game.room = "church"
    scene bg church wedding
    with fade
    "It's hard to square the impression I had of Lexi when we first met with where we are now."
    "Even harder to believe that she's turned out to be the girl I'm about to marry!"
    "It was hard enough to get to grips with the fact that I managed to hook up with [bree.name] or Sasha."
    "So it felt crazy to become involved with the three of them at the same time."
    "I glance back over my shoulder at the chapel filled with all of our guests."
    "They're an interesting bunch of people to be sure, from all walks of life."
    "But it reassures me to see that the place is pretty much full."
    "That and the fact that all I see are smiling faces too."
    "It's at that moment the music starts to play, filling the chapel."
    "And on cue, all of the guests get to their feet as one."
    "I'm still looking back as the bridal procession appears in the aisle..."
    show lexi wedding normal nophone at center, zoomAt (1.0, (640, 730)) with dissolve
    "Lexi, the girl that I've always thought of as the princess of the trailer park."
    "Well, let's just say she looks more like a princess than ever."
    "She'll always be trash."
    "But who knew that trash could look so good?"
    show lexi wedding at center, zoomAt (1.0, (340, 730)) with ease
    show bree wedding normal at center, zoomAt (1.0, (640, 730)) with dissolve
    "Next comes [bree.name], her white and floaty dress is perhaps the closest to the traditional."
    "The only thing as striking as her dress is the smile on her face."
    show bree wedding at center, zoomAt (1.0, (940, 730)) with ease
    show sasha wedding at center, zoomAt (1.0, (640, 730)) with dissolve
    "Sasha is almost the exact opposite, clad in black that contrasts her pale skin."
    "She's every bit as mysterious and intriguing as [bree.name] is open and honest."
    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of three large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha and Lexi as they stand beside me at the altar."
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
        if lexi.is_visibly_pregnant:
            "It's a cliche for a trailer park girl to be sporting a swollen belly."
            "But somehow it just serves to make Lexi look all the more desirable, at least in my eyes."
            "She carries it so well that I just know she's going to make a wonderful mother."
    "We only have time to exchange smiles once everyone is in place."
    "Because a moment later the priest clears his throat and gets things started."
    "This is it - we're really doing this!"
    show bree normal
    show sasha normal
    show lexi normal
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today to unite these people in holy matrimony."
    "We've practiced this before, so everyone knows what's expected of them."
    "And I must have seen weddings play out a thousand times on TV and in movies."
    "So maybe that's why it all seems to pass so quickly."
    "It feels like we've reached the vows in the blink of an eye!"
    "Priest" "Do you, [hero.name], take Lexi to be your lawful wedded wife?"
    "Priest" "Oh, and Sasha!"
    "Priest" "And [bree.name] too!"
    mike.say "I do."
    "Priest" "And do you, Lexi, take [hero.name] to be your lawful, wedded husband?"
    "Priest" "And Sasha."
    "Priest" "And [bree.name]."
    show lexi happy at startle
    lexi.say "Yeah, I guess I do!"
    "Priest" "[bree.name], do you take Lexi, Sasha and [hero.name] to be your lawful, wedded partners?"
    show bree happy at startle
    bree.say "I do!"
    "Priest" "Do you, Sasha, take these others to be your lawful, wedded partners?"
    show sasha happy at startle
    sasha.say "Yes, I do."
    "The priest nods, looking pleased to have made it this far without any mishaps."
    "Priest" "I now call upon all those present."
    "Priest" "If any know of a lawful reason that these people may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause as everyone looks around with baited breath."
    "But it seems to me that if the four of us can make it this far, then we're probably safe."
    "And that suspicion is confirmed when the priest nods with obvious relief."
    "But the moment passes, and everyone lets out a sigh of relief."
    "Priest" "Good..."
    "Priest" "Then it gives me great pleasure to proclaim you married."
    "Priest" "At this point it's traditional to kiss, if you like..."
    show sasha at center, traveling (1.5, 1.0, (640, 1040))
    show bree at center, traveling (1.5, 1.0, (920, 1040))
    show lexi at center, traveling (1.5, 1.0, (360, 1040))
    "We do just that, and it feels better than ever."
    "The kiss isn't just for the sake of rounding off the ceremony either."
    "It feels like a release of all the stuff that we were hanging on to from before."
    "Like the beginning of an entirely new chapter for all of us!"

    scene home ending
    show home ending lexi
    with fade
    lexi.say "I guess they want to hear from me."
    lexi.say "Which is only right, because I wear the pants in this relationship!"
    show home ending sasha with dissolve
    sasha.say "Hey, Lexi!"
    sasha.say "What gives?!?"
    show home ending bree with dissolve
    bree.say "Wait, wait, wait!"
    lexi.say "Ah, hey you guys..."
    lexi.say "I didn't see you there."
    lexi.say "That was just a little joke, you know?"
    lexi.say "Something to break the ice and set the tone!"
    sasha.say "Yeah, sure thing, Lexi."
    bree.say "I don't think it was very funny."
    lexi.say "Whatever..."
    lexi.say "We're supposed to be here to talk about [hero.name], anyway."
    bree.say "You're right."
    sasha.say "Yeah, I guess so."
    lexi.say "You gotta admit, it's pretty random and crazy."
    lexi.say "I mean, all of us winding up together in the end."
    lexi.say "It's almost like one of those crazy games."
    lexi.say "With [hero.name] making all of the decisions!"
    bree.say "It's kind of scary to think he was in charge of everything!"
    sasha.say "Yeah, he's kind of a screw-up!"
    lexi.say "And now we're all starting a life together."
    lexi.say "We make one crazy family!"
    if lexi.is_visibly_pregnant:
        lexi.say "I don't know who Tyrone and Chantel take after yet."
        lexi.say "But I do know that their daddy loves them."
    if sasha.is_visibly_pregnant:
        sasha.say "I think [hero.name] likes not being the only guy around here."
        sasha.say "That's why he spoils Dahlia every chance he gets!"
    if bree.is_visibly_pregnant:
        bree.say "Yeah - don't forget Poppy."
        bree.say "She's loud enough to count for two!"
    lexi.say "Like I said - one crazy family."
    lexi.say "But I think it works out pretty well."
    bree.say "You're right there, Lexi."
    bree.say "It works for me!"
    sasha.say "On paper, it sure as hell looks like it shouldn't!"
    sasha.say "But in reality, it actually does."
    lexi.say "Yeah, agreed."
    lexi.say "But it's not like we have to tell [hero.name] that!"
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
