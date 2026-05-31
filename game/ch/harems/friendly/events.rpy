init python:
    Event(**{
    "name": "emma_samantha_showdown",
    "priority": 500,
    "label": "emma_samantha_showdown",
    "conditions": [
        HeroTarget(
            IsRoom("date_mall1"),
            ),
        PersonTarget(emma,
            OnDate(),
            MinStat("love", 125)
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            IsFlag("divorced"),
            MinStat("love", 125)
            ),
        "Person.showdown(emma, samantha)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "emma_samantha_threesome",
    "priority": 500,
    "label": "emma_samantha_threesome_intro",
    "conditions": [
        TogetherInHarem('friendly', 'emma', 'samantha'),
        IsTimeOfDay("afternoon", "evening"),
        GameTarget(
            IsFlag("friendly_delay", False),
            ),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(emma,
            Not(IsHidden()),
            ),
        PersonTarget(samantha,
            Not(IsHidden()),
            Or(
                And(
                    InHarem('home'),
                    HasRoomTag("home"),
                    ),
                Not(InHarem('home')),
                ),
            ),
        Not("emma_too_small(10)")
        ],
    "do_once": True,
    })

label emma_samantha_showdown:
    "I was racking my brains before the day of my date with Emma came around."
    "But no matter how hard I tried, I just couldn't seem to come up with anything."
    "Every place I thought up for us to go was either closed or booked up in advance."
    "So when the time came around, I was still struggling to think of anywhere to go."
    "In the end, I just suggest that we go down to the mall."
    "And much to my surprise, Emma seems to think this is a great idea."
    show emma happy
    emma.say "Sure, [hero.name]..."
    emma.say "A date at the mall would be wonderful!"
    mike.say "Really, Emma?"
    mike.say "Are you sure?"
    mike.say "I tried to think of something more exciting..."
    show emma normal
    "Emma shakes her head at this."
    "Then she takes hold of my hand and gives it a squeeze."
    emma.say "Don't worry about it."
    emma.say "We can just stroll along together."
    emma.say "We'll have all the time in the world to chat."
    emma.say "And we don't need to worry about the weather turning bad either!"
    "So that's how we end up at the mall, strolling around the place."
    "We're walking hand in hand, just talking about whatever comes to mind."
    "Occasionally we stop to look at something in the window of a store."
    "But mostly we're just having a great time enjoying each other's company."
    emma.say "You see?"
    emma.say "Didn't I say this was a great idea?"
    mike.say "Yeah, Emma..."
    mike.say "I guess you were right."
    mike.say "All we needed was the chance to spend some time together."
    show emma happy
    "Emma smiles and pulls on my hand, urging me to continue our stroll."
    "But as soon as we do so, I see that there's somebody standing in our way."
    show emma normal at left4
    show samantha normal at right
    with moveinright
    samantha.say "Oh, hey, [hero.name]!"
    samantha.say "I thought it was you."
    "I stop dead in my tracks at the sound of the familiar voice."
    "It's Sam alright, standing right there in front of us."
    if samantha.is_girlfriend or emma.flags.samgirlfriend:
        "I can already feel myself starting to sweat."
        "Did she follow us here?"
        "Is she spying on me?!?"
        "All it would take is one word from her to blow everything up!"
    else:
        "Sam gazes down, seeing that Emma and I are holding hands."
    samantha.say "Aww..."
    samantha.say "Aren't you two cute!"
    show samantha happy
    samantha.say "Looks like you're getting on pretty well!"
    mike.say "Ah...yeah, sure!"
    show emma annoyed at left5
    show samantha normal at right5
    with move
    "This is a little awkward!"
    "I mean sure, Sam was the one that introduced Emma and me."
    "But she never said that she did it with the idea of getting us together in mind!"
    "Emma looks more than a little shy at the way Sam's just walked straight up to us."
    "But I can see that she's doing the best she can to smile and deal with it."
    "Sometimes I forget that Emma's just not as forward as someone like Sam."
    show emma normal
    emma.say "Erm..."
    emma.say "Hello, Sam!"
    "Yeah, this is getting awkward fast!"
    "I need to do something to change that."
    mike.say "Maybe we could go grab a bite to eat or something?"
    mike.say "That way we can sit down and catch up properly, yeah?"
    samantha.say "Hmm..."
    show samantha happy
    samantha.say "I could spare the time to grab a coffee."
    show emma happy
    emma.say "Oh...that sounds like a good idea."
    emma.say "Let's do that!"
    scene bg coffeeshop
    show emma normal at left5
    show samantha normal at right5
    with fade
    "The three of us make our way to the nearest coffee shop."
    "Luckily there's a table free and we're soon ordering our drinks."
    "Then it's down to the serious business of sharing the gossip."
    "I open my mouth to begin the conversation."
    "But Sam beats me to it!"
    samantha.say "So, Emma..."
    samantha.say "What's the story with you two?"
    "Emma blushes a little, but still manages to reply."
    emma.say "Well, Sam..."
    emma.say "It's all been a bit of a whirlwind, really."
    emma.say "It feels like one minute I was just meeting him."
    emma.say "And the very next second, we were dating!"
    if emma.love >= 150 and samantha.love >= 150 and samantha.flags.nonexclusive:
        "As soon as Emma mentions the fact we're dating, Sam's expression changes."
        "Before she looked genuinely interested in pumping us for information."
        "But now she's smiling, and I think that I know why."
        samantha.say "You're dating [hero.name]?"
        show samantha surprised
        samantha.say "What a coincidence, Emma!"
        show samantha normal
        samantha.say "So am I!"
        "For a moment, Emma looks like she's been slapped in the face."
        show emma annoyed
        "She stares at Sam in silence, her mouth hanging open."
        "But as soon as she recovers, Emma turns to face me."
        emma.say "What is she talking about, [hero.name]?"
        show emma sad
        emma.say "Is this...is this some kind of joke?"
        mike.say "Erm...no, Emma."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake and I have been sort of seeing each other for a while now."
        else:
            mike.say "Sam and I have been sort of seeing each other for a while now."
        mike.say "I guess we're such old friends, so close that it didn't click for me until now."
        "Emma opens her mouth to say something."
        "But Sam cuts her off before she can speak."
        samantha.say "I get it, Emma, I do."
        samantha.say "But you really shouldn't be mad at [hero.name]."
        samantha.say "He was there for me when my marriage fell apart recently."
        show samantha flirt
        samantha.say "He was the only one that stuck by me, that gave me what I needed..."
        "Emma frowns at Samantha."
        "And she doesn't seem mollified by her explanation either."
        emma.say "And I suppose what you needed was sex?"
        show emma normal
        emma.say "Lots of it, huh?"
        "Sam shrugs, but then she nods."
        show samantha normal
        samantha.say "He's a pretty special guy, Emma."
        samantha.say "And I'm not the possessive type, I promise you."
        samantha.say "I'd be willing to share him - with the right girl..."
        if all([person.lesbian >= 9 and person.sub >= 25 for person in [emma, samantha]]):
            emma.say "Wh...what do you mean?"
            show emma annoyed
            emma.say "How would we share him?"
            mike.say "Hey!"
            mike.say "I'm right here you know?"
            mike.say "You guys are talking about me like I'm a hotel room or something!"
            "The looks that Emma and Sam shoot me are clear."
            show emma angry
            show samantha angry
            "Right now both of them want me to shut the hell up!"
            samantha.say "What I mean, Emma..."
            show samantha normal
            samantha.say "Is that he's been good for me."
            samantha.say "And he'll be good for you too."
            samantha.say "But he could be good for both of us - at the same time!"
            show emma annoyed
            "Emma looks more than a little nervous as Sam's meaning sinks in."
            "But I note that she hasn't rejected the idea out of hand."
            "Which has to be a good thing."
            emma.say "I...I could give it a try, I suppose."
            show emma normal
            emma.say "So long as I don't have to do anything I don't want to!"
            "Sam smiles as she holds up her hands in a gesture of surrender."
            samantha.say "I promise, Emma."
            samantha.say "No pressure."
            samantha.say "What do you say, [hero.name]?"
            "I can't help bristling a little as I'm finally let in on the conversation."
            "But then reality dawns on me and I make a supreme effort to push my annoyance aside."
            "For one thing, it looks like I'm getting away with seeing two girls at once."
            "And on top of that, this could end up in a pretty fun threesome!"
            mike.say "I'm in, you guys!"
            mike.say "So when and where are we going to get it on?"
            "At this, Emma and Sam exchange a knowing glance along with a shake of the head."
            "But I'm not about to let that get to me, not when there's a threesome in the making!"
            $ Harem.join_by_name("friendly", "emma", "samantha")
            $ game.active_date.score += 20
            $ game.flags.friendly_delay = TemporaryFlag(True, 2)
        else:
            "Emma frowns and shakes her head."
            "Then she stands up as well."
            show emma angry
            emma.say "I can't believe what I'm hearing."
            emma.say "First I find you're cheating on me, [hero.name]."
            emma.say "Then I find out it's with the girl that introduced us!"
            "Now I'm on my feet too."
            "And I have a hand stretched out towards Emma."
            mike.say "Emma, please!"
            mike.say "You're reading too much into all this..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake's just an old friend, that's all."
            else:
                mike.say "Sam's just an old friend, that's all."
            mike.say "She's had a hard time of it recently."
            "I look to Sam for some support."
            "But she just smiles and shrugs."
            with vpunch
            emma.say "Well you ARE her friend, [hero.name]."
            emma.say "And it sounds like you've been comforting her."
            emma.say "Comforting her while she lays on her back with her legs open!"
            "With that, Emma storms off too."
            hide emma
            "Which leaves me sitting with Sam."
            samantha.say "Don't worry, [hero.name]."
            show samantha flirt
            samantha.say "You've still got me."
            if samantha.flags.nickname == "cupcake":
                mike.say "Yeah, Cupcake..."
            else:
                mike.say "Yeah, Sam..."
            mike.say "Thanks for reminding me!"
            $ emma.set_gone_forever()
            $ hero.cancel_activity()
            $ game.room = "street"
            $ game.active_date.stay = False
            return
    elif emma.love >= samantha.love and emma.love >= 125 and not samantha.flags.nonexclusive:
        "As soon as Emma mentions the fact we're dating, Sam's expression changes."
        "Before she looked genuinely interested in pumping us for information."
        "But now she looks like she's getting angrier by the second!"
        show samantha angry
        samantha.say "You're what?"
        with vpunch
        samantha.say "Are you frikin kidding me?!?"
        "Sam jumps to her feet, almost turning over the table."
        "Then she turns on her heel and storms out of the coffee shop."
        hide samantha
        $ samantha.set_gone_forever()
        "It's all over before Emma or I can even manage to react."
        emma.say "Wh...what was that about?"
        show emma annoyed at center
        emma.say "Why would she storm off like that?"
        emma.say "I mean...all I did was say that we were dating!"
        "All I can do is shrug helplessly."
        mike.say "I have no idea, Emma!"
        mike.say "Honestly I don't!"
        if emma.sub >= 25:
            "Emma nods, letting me know that she believes me."
            show emma normal
            "Then she takes a deep breath and stares down at her coffee."
            emma.say "Is your relationship with everyone that weird, [hero.name]?"
            emma.say "Because if they are, I think you need to warn me."
            emma.say "You know - BEFORE, we bump into them!"
            mike.say "No, Emma...most of my relationships are pretty normal."
            if samantha.flags.nickname == "cupcake":
                mike.say "And I thought my one with Cupcake was too."
            else:
                mike.say "And I thought my one with Sam was too."
            "After that, we try to get back to our date."
            "But it's just not the same, no matter what we do."
            "That weird encounter with Sam seems to have spoiled the mood."
            $ game.active_date.score -= 10
        else:
            "Emma frowns and shakes her head."
            "Then she stands up as well."
            emma.say "I don't think I believe you, [hero.name]."
            show emma angry
            emma.say "Because that's just how I'd react if I found out someone was cheating on me!"
            emma.say "I think there's something about Sam that you're not telling me!"
            "Now I'm on my feet too."
            "And I have a hand stretched out towards Emma."
            mike.say "Emma, please!"
            mike.say "You're reading too much into all this..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake's just an old friend, that's all."
            else:
                mike.say "Sam's just an old friend, that's all."
            mike.say "She's had a hard time of it recently."
            mike.say "Maybe that's why she went off like that?"
            emma.say "Well you're such good friends, [hero.name]."
            emma.say "Go run after her and comfort her!"
            emma.say "Just don't try and follow me!"
            "With that, Emma storms off too."
            hide emma
            "Which leaves me sitting alone in the coffee shop."
            $ emma.set_gone_forever()
            $ hero.cancel_activity()
            $ game.room = "map"
            $ game.active_date.stay = False
            return
    else:
        "Sam's face breaks into a smile at the mere mention of us dating."
        samantha.say "Really?"
        show samantha happy
        samantha.say "That's so great to hear."
        samantha.say "[hero.name]'s been so good to me, Emma."
        samantha.say "I'm so happy you're making him happy!"
        "Emma looks a little overwhelmed by Sam's reaction."
        "She even flushes a bit and turns to me for support."
        mike.say "Ah..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake's exaggerating a bit, Emma."
        else:
            mike.say "Sam's exaggerating a bit, Emma."
        mike.say "I just did what any friend would do under the circumstances, that's all!"
        "At this, Sam shakes her head."
        show samantha normal
        samantha.say "Don't listen to him, Emma."
        samantha.say "Okay, you remember I found out that my husband was cheating on me, yeah?"
        samantha.say "Nobody but him had the courage to tell me the truth."
        show samantha happy
        samantha.say "And he was there every step of the way, even at my worst times!"
        "I smile and shrug at Sam's praise."
        "Trying to downplay all of this to Emma."
        mike.say "Like I said - I was just being a friend!"
        show samantha normal
        samantha.say "Will you shut up and let me tell her how great you are!"
        samantha.say "I was a mess, Emma - vulnerable and needy."
        samantha.say "And he never once ghosted me or took advantage."
        emma.say "I..."
        emma.say "Well I..."
        emma.say "Wow...I must be a lucky girl!"
        "Sam smiles and nods, pleased with Emma's reaction."
        "I have a smaller smile on my face, as I'm still embarrassed."
        "But I can feel Emma holding my hand under the table."
        "And she gives it an extra hard squeeze as she leans into me."
        "Which I choose to take as a positive gesture."
        $ game.active_date.score += 10
    hide samantha
    return

label emma_samantha_threesome_intro:
    "You know those days when you're just going about your business at home?"
    "You've got nothing planned and you're just thinking about totally random stuff."
    "The most you're expecting to get out of the day is maybe playing a little Zbox."
    "Then something happens that totally blows everything out of the water."
    "Well that's pretty much what's happening to me right now."
    "I'm just mooching about the house, doing this and that."
    "I think the most exciting thing that's happened to me so far is opening the mail."
    play sound door_knock
    "But then I hear the sound of a knock at the door."
    "My head turns in that direction and my body follows along."
    "Even as I walk to the front door, I'm still in a pretty meh state of mind."
    "It's probably just going to be someone delivering a package or selling some random crap."
    "But when I open the door, my mood suddenly changes and my brain comes buzzing to life."
    scene bg house
    if Harem.find(samantha, name='home') and Room.has_tag(samantha.room, 'home'):
        show emma casual normal
        with wiperight
        "Because it's Emma that I find standing on the doorstep."
        emma.say "Hi, [hero.name]!"
        show emma happy
        emma.say "Surprise!"
        emma.say "As she's home, Sam said I should drop by for a visit!"
        "I stand there in silence for a moment."
        "And I have to blink a couple of times before I actually believe it."
        mike.say "Whoa..."
        mike.say "This is a surprise!"
        mike.say "Y...you'd better come in, I guess!"
        "I stand aside and let her come into the house."
        scene bg livingroom
        show emma casual normal at left
        with fade
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake shouldn't be too far. I'll call her."
        else:
            mike.say "Sam shouldn't be too far. I'll call her."
        show samantha casual happy at right with moveinright
        samantha.say "Hi Emma! I'm so glad you came!"
        samantha.say "Erm..."
        samantha.say "Sorry this place is such a mess."
        show samantha annoyed
        samantha.say "Someone forgot to do his chores."
        "Emma shake her head."
        emma.say "That's okay, [hero.name]."
        show samantha normal
        emma.say "I came to see you, not judge your housekeeping!"
    else:
        with wiperight
        "Because it's Emma and Sam that I find standing on the doorstep."
        show emma casual normal at left
        show samantha casual normal at right
        with dissolve
        samantha.say "Hi, [hero.name]!"
        emma.say "Surprise!"
        show samantha happy
        samantha.say "We thought we'd drop by for a visit!"
        "I stand there in silence for a moment."
        "And I have to blink a couple of times before I actually believe it."
        mike.say "Whoa..."
        mike.say "This is a surprise!"
        mike.say "Y...you'd better come in, I guess!"
        "I stand aside and let them come into the house."
        "Then I close the door behind them, already regretting not having cleaned the house."
        scene bg livingroom
        show emma casual normal at left
        show samantha casual normal at right
        with fade
        mike.say "Erm..."
        mike.say "Sorry this place is such a mess, guys."
        mike.say "I wasn't expecting visitors today!"
        "Emma and Sam shake their heads as one."
        "And they wave away my concerns as soon as they hear them."
        samantha.say "That's okay, [hero.name]."
        samantha.say "We came to see you, not judge your housekeeping!"
    emma.say "And we don't have to hang out around here anyway."
    show emma happy
    emma.say "If we go to your room, then we can just enjoy each other's company."
    emma.say "What do you say?"
    "I take one final glance around the hallway, noting the general chaos."
    "Then my gaze falls back onto Emma and Sam, both smiling sweetly at me."
    "How is that any kind of choice?"
    mike.say "You know what..."
    mike.say "That sounds like a great idea."
    mike.say "Let's go."
    "Emma and Sam follow close behind me as I lead the way to my room."
    scene bg bedroom1
    show emma casual normal at left
    show samantha casual normal at right
    with fade
    "I open the door and let them inside, stepping after them and closing it quickly."
    "But as I turn around, ready to say something clever, I get a surprise."
    "Emma and Sam haven't wasted any time making themselves comfortable."
    "In fact, they're both reclining on my bed while gazing back at me."
    "And neither of them is hiding the fact that they're trying to catch my eye."
    samantha.say "What are you staring at, [hero.name]?"
    show samantha flirt
    samantha.say "We're just making ourselves comfortable, that's all!"
    emma.say "Y...yeah, [hero.name]..."
    show emma blush
    emma.say "You want to come join us?"
    "Well, this is certainly taking an interesting turn!"
    "I know the mischievous look on Sam's face all too well."
    "But I've never known Emma put on a show like this before."
    "I know that Sam's probably the brains behind this little escapade."
    "Yet seeing Emma try to act sexy in the same way is really intriguing."
    "It's almost like the fact she's so bad at is actually makes it a turn-on!"
    mike.say "Wait a minute..."
    mike.say "I just want to check..."
    mike.say "We're having a threesome here, right?"
    "I sense that my question has kind of broken the spell a little."
    "As Sam and Emma sit up and exchange puzzled glances."
    show samantha annoyed
    samantha.say "Well...yeah!"
    show emma normal
    emma.say "We did say we were going to share you - remember?"
    "I can't help laughing as I walk over to the bed and sit down between them."
    mike.say "Of course I do."
    mike.say "I just never got the memo we were at this stage already!"
    mike.say "But just for the record, I'm totally on board!"
    "Sam and Emma exchange another glance, nodding eagerly."
    show samantha normal
    samantha.say "Oh...okay then!"
    emma.say "That's great news!"
    "I barely see them nod to each other before it happens."
    "First Sam and then Emma pounces on me, pinning me to the bed."
    "One of them plants a kiss on my lips while the other tugs at my clothes."
    "In the confusion I honestly can't tell who is doing what to me."
    "And more than once I'm sure that they actually manage to swap places!"
    "In this fashion I find myself being stripped naked as a tongue explores my mouth."
    "When they finally let me up, I find myself completely stripped off."
    "And my cock is standing to attention too, swaying as I move."
    "But all of my attention is focused on what Sam and Emma are doing now."
    "They've used my moment of disorientation to slide off the bed."
    "And now they're undressing each other right in front of me."
    "I can tell that this is meant as a show for my titillation."
    show samantha topless at right4
    show emma topless at left4
    with move
    "So I watch closely as two girls I desire flaunt themselves before me."
    "Sam takes the lead, as I'd have expected."
    "And Emma follows her example attentively."
    "One item at a time, they strip each other."
    show samantha naked
    show emma naked
    "And by the time they're both naked, I'm spellbound."
    "The pair of them are standing before me, wearing only a smile."
    "But it takes me a moment to realise why they're not making a move."
    "Then I understand that they're waiting for me to tell them what to do!"
    call emma_samantha_threesome from _call_emma_samantha_threesome
    $ game.pass_time(2)
    return

label emma_samantha_threesome_appointment_intro(appointment=None):
    "It's finally time for our date."
    play sound door_bell
    "I almost ran to then door when I heard the doorbell."
    scene bg house
    if Harem.find(samantha, name='home') and Room.has_tag(samantha.room, 'home'):
        show emma casual normal
        "Emma is standing on the doorstep."
        emma.say "Hi, [hero.name]!"
        "I stand aside and let her come into the house."
        "Samantha shows up a few seconds later"
        show samantha casual happy at right
        samantha.say "Hi, Emma!"
    else:
        "Emma and Sam are standing on the doorstep."
        show emma casual normal at left
        show samantha casual normal at right
        samantha.say "Hi, [hero.name]!"
        emma.say "Hello, [hero.name]!"
        "I stand aside and let them come into the house."
    scene bg livingroom
    show emma casual normal at left
    show samantha casual normal at right
    mike.say "Shall we go?"
    "Emma and Sam follow close behind me as I lead the way to my room."
    scene bg bedroom1
    show emma casual normal at left
    show samantha casual normal at right
    "I open the door and let them inside."
    "Emma and Sam haven't wasted any time making themselves comfortable."
    "In fact, they're both reclining on my bed while gazing back at me."
    "And now they're undressing each other right in front of me."
    "I can tell that this is meant as a show for my titillation."
    show samantha topless at right4 with moveinright
    show emma topless at left4 with moveinleft
    "So I watch closely as two girls I desire flaunt themselves before me."
    "Sam takes the lead, as I'd have expected."
    "And Emma follows her example attentively."
    "One item at a time, they strip each other."
    show samantha naked
    show emma naked
    "And by the time they're both naked, I'm spellbound."
    "The pair of them are standing before me, wearing only a smile."
    "But it takes me a moment to realise why they're not making a move."
    "Then I understand that they're waiting for me to tell them what to do!"
    call emma_samantha_threesome from _call_emma_samantha_threesome_1
    $ game.pass_time(2)
    return

label emma_samantha_threesome_now_intro(from_girl="samantha"):
    if from_girl == "samantha":
        if Room.has_tag(game.room, 'home'):
            samantha.say "I'll call Emma and tell her to come here."
            play sound door_bell
            "A few moment later, the sound of the doorbell rings through the house."
        else:
            samantha.say "I'll call Emma and tell her to meet us home."
            "Once back home, Emma is already at the front of the house."
        show bg house
        show emma casual happy at left
        emma.say "Hi, [hero.name]!"
        show samantha casual happy at right
        samantha.say "Hi, Emma!"
    elif from_girl == "emma":
        emma.say "I'll call Samantha and tell her to meet us home."
        "Once back home, Samantha is already at the front of the house."
        show bg house
        show samantha casual happy at right
        samantha.say "Hi, [hero.name]!"
        show emma casual happy at left
        emma.say "Hi, Emma!"
    mike.say "Shall we go?"
    "Emma and Sam follow close behind me as I lead the way to my room."
    scene bg bedroom1
    show emma casual normal at left
    show samantha casual normal at right
    "I open the door and let them inside."
    "Emma and Sam haven't wasted any time making themselves comfortable."
    "In fact, they're both reclining on my bed while gazing back at me."
    "And now they're undressing each other right in front of me."
    "I can tell that this is meant as a show for my titillation."
    show samantha topless at right4 with moveinright
    show emma topless at left4 with moveinleft
    "So I watch closely as two girls I desire flaunt themselves before me."
    "Sam takes the lead, as I'd have expected."
    "And Emma follows her example attentively."
    "One item at a time, they strip each other."
    show samantha naked
    show emma naked
    "And by the time they're both naked, I'm spellbound."
    "The pair of them are standing before me, wearing only a smile."
    "But it takes me a moment to realise why they're not making a move."
    "Then I understand that they're waiting for me to tell them what to do!"
    call emma_samantha_threesome from _call_emma_samantha_threesome_2
    $ game.pass_time(2)
    return

label emma_samantha_threesome:
    menu:
        "Blowjob":
            "By way of an answer, I stand up and walk the short distance to where they're standing."
            "Sam and Emma watch as I approach, remaining still and silent as I do so."
            "When I make it over to them, I put a hand on each of their shoulders."
            "Then I gently push them downwards, nodding my head in that direction too."
            "Emma looks more than a little confused as all this happens."
            "But Sam seems to sense this and so takes the lead."
            show friendly harem bj
            "And one look at her expression tells me that she knows exactly what I want."
            "Sam guides Emma down further still, guiding her hands to my balls."
            show friendly harem bj emma
            "At the same time she takes a firm hold of my cock."
            "Then she opens her mouth and sticks out her tongue."
            "Both Emma and I watch in fascination as she closes her eyes and goes to work."
            "Sam teases the hip of my cock at first, hardly touching it with her lips."
            show friendly harem bj emma blow
            "But little by little, she takes more into her mouth."
            "I watch as Emma seems to be fascinated by the sight."
            "And slowly she begins to copy what she's seeing Sam do."
            "I gasp as Emma opens her mouth and starts to suck on my balls."
            show friendly harem bj emma blow licking
            "She's enthusiastic, rather than skilled, and I can feel it all that she does."
            "But Emma still manages to make Sam's efforts all the more intense."
            show friendly harem bj emma blow licking middle
            "At the same time, Sam's picking up the pace."
            "She starts taking ever more of my cock into her mouth."
            show friendly harem bj emma blow licking up
            "Her head's bobbing up and down the whole time."
            "And I'm starting to wish that I'd held onto something before they got started!"
            show friendly harem bj emma blow licking upper
            "Seriously, they're working me so well that I almost feel like I'm getting dizzy."
            "It all comes to a head when Sam starts squeezing my cock as well."
            show friendly harem bj emma blow licking up
            "There's not a part of it that's escaping their attention."
            "And in a situation like that, nobody can hold on too long."
            show friendly harem bj emma blow licking middle
            "Sam seems to know this too, as she quickly releases my cock from her mouth."
            "Then she pulls Emma up until they're kneeling in front of me together."
            show friendly harem bj emma -blow licking down samhj
            emma.say "Huh?"
            emma.say "What happens now?"
            "Sam just smiles and opens her mouth."
            show friendly harem bj emma samhj cumshot
            "And a moment later I shoot my load into her faces."
            show friendly harem bj emma samhj cum onface
            emma.say "Ah..."
            emma.say "Oh god..."
            "Sam might have had her mouth open in anticipation."
            "Which means that I manage to shoot it into her!"
            "The rest stripes her cheeks and splatters over her chins."
            "Sam laughs as she swallows her mouthful."
        "Fuck Samantha":
            "Emma still seems to be hanging back a little, like she's intimidated."
            "I can see it clearly, and a glance in Sam's direction tells me she does too."
            "Neither of us is going to say it out loud and make Emma feel awkward."
            "But almost as one we start making moves to show her the way ahead."
            "Sam clambers atop me, forcing me backwards and down onto the bed."
            "And within mere seconds she's straddling my thighs."
            "I'm almost totally engrossed in what Sam's doing to me right now."
            "But somehow I still manage to steal a glance in Emma's direction."
            "And I'm seriously relieved to see that she's creeping ever closer."
            show friendly harem cowgirl
            if renpy.has_label("friendly_harem_achievement_2") and not game.flags.cheat:
                call friendly_harem_achievement_2 from _call_friendly_harem_achievement_2
            "That pretty much means that I can devote my attentions to Sam."
            "Something that becomes all the more pressing as I feel her reach down and grab my cock!"
            samantha.say "Okay, [hero.name]..."
            samantha.say "Let's get down to business!"
            menu:
                "Fuck her pussy":
                    "For all that Sam says those words with an air of authority, she's not taking over."
                    "Because I'm every bit as ready and wanting to get things started as she is."
                    "That's why the next thing to come out of her mouth is a yelp of surprise."
                    "Grabbing Sam around the waist, I pull her downwards."
                    "And thanks to the hold she has on my cock, I don't even have to aim."
                    "She's pointing the head squarely at her own pussy."
                    "So that's exactly where it ends up, rubbing against her lips."
                    "And those lips are getting slicker by the second!"
                    samantha.say "Ooh..."
                    samantha.say "Oh my..."
                    mike.say "You like that, huh?"
                    "Sam nods desperately, still whimpering."
                    mike.say "You want more, yeah?"
                    "Sam nods again, already pushing herself down and onto me."
                    "I nod and smile, all too willing to indulge her."
                    call check_condom_usage (samantha) from _call_check_condom_usage_56
                    if _return == False:
                        return "leave_without_gain"
                    if CONDOM:
                        show friendly harem cowgirl condom
                    "And all it takes is a little thrust on my part and a wriggle on hers."
                    "Then I feel the sensation of Sam's lips beginning to part."
                    "At first I expect her to slide down slowly, a little at a time."
                    "But all of a sudden there's almost no resistance there at all."
                    "This means that Sam sinks down onto me in one motion."
                    show friendly harem cowgirl vaginal
                    "She moans as my cock fills her, unable to slow things down."
                    "And once I can't get any deeper, she groans with satisfaction."
                    "Everything happened so quickly that I almost feel obliged to change the pace."
                    "That's why I start to thrust in and out of Sam as slowly as I can manage."
                    "She seems to appreciate my efforts, nodding as I begin to fuck her."
                    "And she props herself up on my chest, allowing me to have my way with her."
                    "It's only now that I notice Sam moving and moaning in odd ways."
                    show friendly harem cowgirl pleasure
                    "Moving like she's getting pleasure from some other source."
                    "The mystery is solved when I catch a glimpse of Emma over her shoulder."
                    "Part of me thought that she might actually sit this one out entirely."
                    "That maybe she'd just watch Sam and I get it on this time."
                    "But now I can see that Emma's actually taking advantage of the situation."
                    "As Sam and I are preoccupied, she can pretty much do as she likes."
                    "And she's using that freedom to caress Sam's body."
                    show friendly harem cowgirl tongue
                    "Emma's playing with Sam, almost experimenting with her."
                    "And when she does something that the other girl seems to like, she takes note."
                    "For her part, Sam hardly seems to notice that Emma's there at all."
                    "She's far too busy bouncing up and down on my cock right now!"
                    "But I can see how much of an effect Emma's efforts are having on her."
                    "Looking over the other girl's shoulder, Emma catches my eye."
                    "And when she does, she gives me a wicked smile."
                    "It sounds weird, but that's almost as much of a thrill as being inside of Sam!"
                    "Emma's so quiet and shy most of the time, so retiring."
                    show friendly harem cowgirl analfinger
                    "Seeing her being so naughty and wanton is pretty crazy!"
                    samantha.say "Mmm..."
                    samantha.say "I...I can't take it..."
                    samantha.say "I can't take anymore of it..."
                    "Even as Sam's saying this I can feel a change coming over her."
                    "Where before she was just riding me, now she's bearing down."
                    "It's like she's holding on for dear life, knowing what comes next."
                    "I don't know if she's getting ready for her own climax."
                    "Or if she can sense that I'm about to cum."
                    "But both of those things are about to happen..."
                    menu:
                        "Cum inside":
                            "Emma keeps on playing with Sam and I keep on thrusting into her."
                            show friendly harem cowgirl creampie -analfinger
                            "She's held in place by the both of us as she begins to cum."
                            "And when I shoot my load into her too, she really loses it!"
                            if not CONDOM:
                                $ samantha.impregnate()
                            "Sam collapses on top of me, like she's clinging on for dear life."
                            "And I close my eyes too, losing myself in the moment."
                        "Cum outside":
                            "Emma keeps right on playing with Sam until the very last moment."
                            "But I take advantage of this to pull my cock out of her before I lost it."
                            show friendly harem cowgirl -vaginal -analfinger
                            "Sam's moaning becomes that much louder as I do this, though it doesn't stop me."
                            "I cum almost the same second my cock is out of her."
                            show friendly harem cowgirl cumshot
                            "So I shoot my load over her breasts and belly above me."
                            show friendly harem cowgirl -cumshot cum
                        "Pull out and cum in Emma's mouth":
                            "Before it's too late, I disentangle myself from Sam."
                            show friendly harem cowgirl -anal
                            "Then I get up off the bed and beckon for them to do likewise."
                            "Sam catches on first, but Emma looks more than a little confused."
                            "But Sam seems to sense this and so takes the lead."
                            "And one look at her expression tells me that she knows exactly what I want."
                            "Sam guides Emma down further still."
                            "I gasp as Emma opens her mouth and starts to suck on my balls."
                            "She's enthusiastic, rather than skilled, and I can feel it all that she does."
                            "Then she opens her mouth and sticks out her tongue."
                            "Emma teases the hip of my cock at first, hardly touching it with her lips."
                            show friendly harem cowgirl blow
                            "But little by little, she takes more into her mouth."
                            "She starts taking ever more of my cock into her mouth."
                            "Her head's bobbing up and down the whole time."
                            "And I'm starting to wish that I'd held onto something before they got started!"
                            "And in a situation like that, nobody can hold on too long."
                            "Sam seems to know this too and just smiles knowing what's coming next."
                            "And a moment later I shoot my load right into Emma's mouth."
                            show friendly harem cowgirl creampie
                            "I see her eyes go wide as I lose it."
                            "She coughs and chokes, struggling to handle it."
                            "Emma might have wanted to spit it out."
                            "But all she can do is desperately swallow!"
                "Fuck her ass":
                    "For all that Sam says those words with an air of authority, she's not taking over."
                    "Because I'm every bit as ready and wanting to get things started as she is."
                    "That's why the next thing to come out of her mouth is a yelp of surprise."
                    "Grabbing Sam around the waist, I pull her downwards."
                    "She's trying to aim my cock towards her pussy."
                    "But that's not what I've got in mind for her."
                    "So I make a few last minute adjustments."
                    samantha.say "Wha..."
                    samantha.say "What are you..."
                    "By the time Sam feels my cock between her cheeks, it's already too late."
                    "I pull her down with a little more force, wedging the head into her ass."
                    show friendly harem cowgirl anal
                    samantha.say "Ooh..."
                    samantha.say "Oh my..."
                    mike.say "You like that, huh?"
                    "Sam nods desperately, still whimpering."
                    mike.say "You want more, yeah?"
                    "Sam nods again, already pushing herself down and onto me."
                    "I nod and smile, all too willing to indulge her."
                    "And all it takes is a little thrust on my part and a wriggle on hers."
                    "Then I feel the sensation of Sam's lips muscles to part."
                    "At first I expect her to slide down slowly, a little at a time."
                    "But all of a sudden there's almost no resistance there at all."
                    "This means that Sam sinks down onto me in one motion."
                    "She moans as my cock fills her, unable to slow things down."
                    "And once I can't get any deeper, she groans with satisfaction."
                    "Everything happened so quickly that I almost feel obliged to change the pace."
                    "That's why I start to thrust in and out of Sam as slowly as I can manage."
                    "She seems to appreciate my efforts, nodding as I begin to fuck her."
                    "And she props herself up on my chest, allowing me to have my way with her."
                    "It's only now that I notice Sam moving and moaning in odd ways."
                    show friendly harem cowgirl pleasure
                    "Moving like she's getting pleasure from some other source."
                    "The mystery is solved when I catch a glimpse of Emma over her shoulder."
                    "Part of me thought that she might actually sit this one out entirely."
                    "That maybe she'd just watch Sam and I get it on this time."
                    "But now I can see that Emma's actually taking advantage of the situation."
                    show friendly harem cowgirl tongue
                    "As Sam and I are preoccupied, she can pretty much do as she likes."
                    "And she's using that freedom to caress Sam's body."
                    "Emma's playing with Sam, almost experimenting with her."
                    "And when she does something that the other girl seems to like, she takes note."
                    "For her part, Sam hardly seems to notice that Emma's there at all."
                    "She's far too busy bouncing up and down on my cock right now!"
                    "But I can see how much of an effect Emma's efforts are having on her."
                    "Looking over the other girl's shoulder, Emma catches my eye."
                    "And when she does, she gives me a wicked smile."
                    "It sounds weird, but that's almost as much of a thrill as being inside of Sam!"
                    "Emma's so quiet and shy most of the time, so retiring."
                    "Seeing her being so naughty and wanton is pretty crazy!"
                    samantha.say "Mmm..."
                    samantha.say "I...I can't take it..."
                    samantha.say "I can't take anymore of it..."
                    "Even as Sam's saying this I can feel a change coming over her."
                    "Where before she was just riding me, now she's bearing down."
                    "It's like she's holding on for dear life, knowing what comes next."
                    "I don't know if she's getting ready for her own climax."
                    "Or if she can sense that I'm about to cum."
                    "But both of those things are about to happen..."
                    menu:
                        "Cum inside":
                            "Emma keeps on playing with Sam and I keep on thrusting into her."
                            show friendly harem cowgirl creampie
                            "She's held in place by the both of us as she begins to cum."
                            "And when I shoot my load into her too, she really loses it!"
                            "Sam collapses on top of me, like she's clinging on for dear life."
                            "And I close my eyes too, losing myself in the moment."
                        "Cum outside":
                            "Emma keeps right on playing with Sam until the very last moment."
                            "But I take advantage of this to pull my cock out of her before I lost it."
                            show friendly harem cowgirl -anal
                            "Sam's moaning becomes that much louder as I do this, though it doesn't stop me."
                            show friendly harem cowgirl cumshot
                            "I cum almost the same second my cock is out of her."
                            show friendly harem cowgirl -cumshot cum
                            "So I shoot my load over her breasts and belly above me."
                        "Pull out and cum in Emma's mouth":
                            "Before it's too late, I disentangle myself from Sam."
                            show friendly harem cowgirl -anal
                            "Then I get up off the bed and beckon for them to do likewise."
                            "Sam catches on first, but Emma looks more than a little confused."
                            "But Sam seems to sense this and so takes the lead."
                            "And one look at her expression tells me that she knows exactly what I want."
                            "Sam guides Emma down further still."
                            "I gasp as Emma opens her mouth and starts to suck on my balls."
                            "She's enthusiastic, rather than skilled, and I can feel it all that she does."
                            "Then she opens her mouth and sticks out her tongue."
                            "Emma teases the hip of my cock at first, hardly touching it with her lips."
                            show friendly harem cowgirl blow
                            "But little by little, she takes more into her mouth."
                            "She starts taking ever more of my cock into her mouth."
                            "Her head's bobbing up and down the whole time."
                            "And I'm starting to wish that I'd held onto something before they got started!"
                            "And in a situation like that, nobody can hold on too long."
                            "Sam seems to know this too and just smiles knowing what's coming next."
                            "And a moment later I shoot my load right into Emma's mouth."
                            show friendly harem cowgirl creampie
                            "I see her eyes go wide as I lose it."
                            "She coughs and chokes, struggling to handle it."
                            "Emma might have wanted to spit it out."
                            "But all she can do is desperately swallow!"
                    $ samantha.flags.anal += 1
        "Fuck Emma":
            "Sam seems pretty eager to get things started."
            "But even as she clambers onto the bed, she's looking back at Emma."
            "My attention has been one hundred percent on Sam until now."
            "And it's only when I see she's distracted that I look at Emma too."
            "She's holding back, like her nerves are getting the better of her."
            samantha.say "Emma..."
            samantha.say "Come here..."
            samantha.say "I have something to tell you, yeah?"
            "Emma looks at Sam, then at me."
            "I smile and nod, trying my best to play along."
            "And I'm sure not to move an inch while Emma climbs onto the bed."
            show friendly harem doggy
            if renpy.has_label("friendly_harem_achievement_2") and not game.flags.cheat:
                call friendly_harem_achievement_2 from _call_friendly_harem_achievement_2_1
            "It's a pretty tough challenge as well, watching her naked body move like that."
            "But somehow I manage to keep a hold on my desire for Emma as she crawls past me."
            "Sam beckons her closer, until they could whisper to each other."
            "Then she winks at me over her shoulder, letting me know we're ready to go."
            samantha.say "Emma..."
            emma.say "What is it, Sam?"
            samantha.say "Behind you!"
            "Taking this as my cue, I pounce on Emma."
            show friendly harem doggy mike
            "She yelps in surprise, not fast enough to react."
            "But as soon as I have a hold of her, everything changes."
            "It's like I can feel her resistance ebbing away, like she's melting in my arms."
            "Emma looks back over her shoulder at me."
            "Her eyes are wide and she's biting her lip."
            "But she's also nodding, urging me on!"
            "At the same time, Sam reaches up and pulls her down."
            "This means that Emma ends up on all fours."
            "Her head between Sam's thighs and her ass firmly in my hands!"
            menu:
                "Fuck her pussy":
                    "Emma's still looking back over her shoulder at me as I lean forwards."
                    "And I'm one hundred percent aware of just how nervous she still looks."
                    "That means I need to take things slowly here, to make her feel safe."
                    "For that reason I put any thoughts of getting creative out of my head."
                    "Instead I aim the head of my cock low, straight towards Emma's pussy."
                    emma.say "P...please, [hero.name]..."
                    emma.say "Be gentle with me?"
                    "I nod and smile as I begin to rub my cock against Emma's lips."
                    "And almost instantly my care begins to reward me."
                    "She gasps with evident delight, the expression beginning to change."
                    "Where before she was tense and nervous, Emma now becomes calm and delighted."
                    "She slowly closes her eyes and turns her head away from me."
                    "Which I take as a show of trust on her part, that she's putting herself in my hands."
                    "I keep quiet, concentrating on what I'm feeling at that moment."
                    "My cock is gently stroking Emma's lips, going back and forth."
                    "She's quivering at the sensation, her entire body shivering."
                    "But I can tell that it's in anticipation of what's coming next."
                    call check_condom_usage (emma) from _call_check_condom_usage_57
                    if _return == False:
                        return "leave_without_gain"
                    if CONDOM:
                        show friendly harem doggy condom
                    "And then I apply just a little more pressure..."
                    emma.say "Mmm..."
                    emma.say "Oh wow..."
                    emma.say "Y...you're inside me!"
                    show friendly harem doggy vaginal
                    "Emma hardly need to tell me that, as it's all I can feel right now!"
                    "Her pussy opens like a flower, gently parting to allow me inside."
                    "Emma feels tight around my cock, squeezing it even as I sink into her."
                    "And the sensation is amazing, incredible and addictive!"
                    "Emma moans and gasps as I move back and forth."
                    "The motion of my cock inside her is making her move too."
                    "She pushes back as I push forwards, making the most of my motion."
                    "This way my cock goes as deep as it possibly can each time."
                    "Emma's moans become ever louder, until Sam decides to intervene."
                    samantha.say "Come on down here, Emma."
                    samantha.say "Put that mouth of yours to better use!"
                    "Before Emma can protest, Sam pulls her down further still."
                    "Her lips brush those of Sam's pussy, and that's all it seems to take."
                    "Without needing to be shown what to do, Emma begins to work on Sam."
                    show friendly harem doggy down
                    "Instinct takes over and she wastes no time in using her lips and tongue."
                    "Soon enough, Sam's head sinks back into the pillows at the head of the bed."
                    show friendly harem doggy middle
                    "And Emma devotes herself to the task of giving the other girl head."
                    "All the time I'm still thrusting in and out of Emma."
                    show friendly harem doggy up
                    "But now her moans are replaced by similar sounds out of Sam's mouth."
                    "And no matter how hard I try, I can't keep from picking up the pace."
                    show friendly harem doggy upper
                    "I find myself starting to pound away at Emma."
                    "My promise to be gentle is forgotten as I become ever more excited."
                    show friendly harem doggy up
                    "In turn, this causes Emma to push her tongue deeper into Sam."
                    "And the sounds that Sam makes again push me to fuck Emma harder still."
                    show friendly harem doggy middle pleasure
                    "It feels like all three of us are trapped in an inescapable circle."
                    "Each pushing the next one on harder, building the intensity the whole time."
                    show friendly harem doggy down
                    "We can't go on like this forever, something has to give."
                    "And pretty soon we all know it's going to be Sam!"
                    show friendly harem doggy middle
                    samantha.say "Oh fuck..."
                    samantha.say "I...I can't take it..."
                    show friendly harem doggy up
                    samantha.say "I can't take anymore of it..."
                    "Sam wraps her legs around Emma, who in turn pushes hard against me."
                    show friendly harem doggy upper
                    "The sudden intensity is too much for me."
                    "And I can feel myself starting to cum too!"
                    menu:
                        "Cum inside":
                            "Emma keeps on licking away at Sam and I keep on thrusting into her."
                            show friendly harem doggy up
                            "She begins to cum as I do, her pussy squeezing my cock harder than ever."
                            "And when I shoot my load into her too, she really loses it!"
                            show friendly harem doggy creampie -up
                            if not CONDOM:
                                $ emma.impregnate()
                            "Emma raises her head, abandoning Sam's pussy and almost screaming out loud."
                            "All I can do is close my eyes, losing myself in the moment."
                        "Pull out":
                            "Emma keeps on licking away at Sam and I keep on thrusting into her."
                            show friendly harem doggy up
                            "But at the last moment I yank my cock right out of her pussy."
                            show friendly harem doggy -up -vaginal
                            "And when I shoot my load over her too, she really loses it!"
                            show friendly harem doggy cumshot
                            "Emma raises her head, abandoning Sam's pussy and almost screaming out loud."
                            show friendly harem doggy cum -cumshot
                            "All I can do is close my eyes, losing myself in the moment."
                "Fuck her ass":
                    "Emma's still looking back over her shoulder at me as I lean forwards."
                    "And I'm one hundred percent aware of just how nervous she still looks."
                    "But that doesn't mean I'm going to go easy on her."
                    "And if I did, how would she get used to this kind of thing?"
                    emma.say "P...please, [hero.name]..."
                    emma.say "Be gentle with me?"
                    "I nod and smile as I begin to rub my cock against Emma's lips."
                    "But my smile is more on account of knowing my own intentions than anything else."
                    "I can feel Emma starting to get slick and wet in anticipation."
                    "And at the same time she also lets her guard down."
                    "She's so sure she knows what's coming next, she doesn't suspect a thing."
                    "So when I pull back and stick my cock between her buttocks, she's helpless!"
                    show friendly harem doggy anal
                    emma.say "Oh..."
                    emma.say "Oh god..."
                    emma.say "My hole!"
                    "I keep on going, feeling my cock begin to work its way in there."
                    "Emma wriggles and squirms at first."
                    "But then I feel her relax as the sensations hit her."
                    emma.say "Mmm..."
                    emma.say "Oh wow..."
                    emma.say "Y...you're inside me!"
                    "Emma hardly need to tell me that, as it's all I can feel right now!"
                    "Her ass is already surrendering to me, muscles gently parting to allow me inside."
                    "Emma feels tight around my cock, squeezing it even as I sink into her."
                    "And the sensation is amazing, incredible and addictive!"
                    "Emma moans and gasps as I move back and forth."
                    "The motion of my cock inside her is making her move too."
                    "She pushes back as I push forwards, making the most of my motion."
                    "This way my cock goes as deep as it possibly can each time."
                    "Emma's moans become ever louder, until Sam decides to intervene."
                    samantha.say "Come on down here, Emma."
                    samantha.say "Put that mouth of yours to better use!"
                    "Before Emma can protest, Sam pulls her down further still."
                    "Her lips brush those of Sam's pussy, and that's all it seems to take."
                    "Without needing to be shown what to do, Emma begins to work on Sam."
                    show friendly harem doggy down
                    "Instinct takes over and she wastes no time in using her lips and tongue."
                    "Soon enough, Sam's head sinks back into the pillows at the head of the bed."
                    show friendly harem doggy middle
                    "And Emma devotes herself to the task of giving the other girl head."
                    "All the time I'm still thrusting in and out of Emma."
                    show friendly harem doggy up
                    "But now her moans are replaced by similar sounds out of Sam's mouth."
                    "And no matter how hard I try, I can't keep from picking up the pace."
                    show friendly harem doggy upper
                    "I find myself starting to pound away at Emma."
                    "My promise to be gentle is forgotten as I become ever more excited."
                    show friendly harem doggy up
                    "In turn, this causes Emma to push her tongue deeper into Sam."
                    "And the sounds that Sam makes again push me to fuck Emma harder still."
                    show friendly harem doggy middle
                    "It feels like all three of us are trapped in an inescapable circle."
                    "Each pushing the next one on harder, building the intensity the whole time."
                    show friendly harem doggy down pleasure
                    "We can't go on like this forever, something has to give."
                    "And pretty soon we all know it's going to be Sam!"
                    show friendly harem doggy middle
                    samantha.say "Oh fuck..."
                    samantha.say "I...I can't take it..."
                    show friendly harem doggy up
                    samantha.say "I can't take anymore of it..."
                    "Sam wraps her legs around Emma, who in turn pushes hard against me."
                    show friendly harem doggy upper
                    "The sudden intensity is too much for me."
                    "And I can feel myself starting to cum too!"
                    menu:
                        "Cum inside":
                            "Emma keeps on licking away at Sam and I keep on thrusting into her."
                            show friendly harem doggy middle
                            "She begins to cum as I do, her ass squeezing my cock harder than ever."
                            "And when I shoot my load into her too, she really loses it!"
                            show friendly harem doggy creampie
                            "Emma raises her head, abandoning Sam's pussy and almost screaming out loud."
                            "All I can do is close my eyes, losing myself in the moment."
                        "Pull out":
                            "Emma keeps on licking away at Sam and I keep on thrusting into her."
                            show friendly harem doggy middle
                            "But at the last moment I yank my cock right out of her ass."
                            show friendly harem doggy -anal -middle
                            "And when I shoot my load over her too, she really loses it!"
                            show friendly harem doggy cumshot
                            "Emma raises her head, abandoning Sam's pussy and almost screaming out loud."
                            show friendly harem doggy cum
                            "All I can do is close my eyes, losing myself in the moment."
                    $ emma.flags.anal += 1
    "Once it's all over, everyone collapses onto the bed."
    "All three of us are utterly exhausted, all out energy spent."
    "But we're all smiling too, with satisfied looks on our faces."
    "And I can't help thinking this could be the start of something special."
    $ emma.love += 2
    $ emma.sexperience += 1
    $ samantha.love += 2
    $ samantha.sexperience += 1
    return


label emma_samantha_propose_male:
    "I've been planning this moment in my head ever since the idea occurred to me."
    "Replaying it a million times, trying to think of every possible outcome."
    "And the one thing that I know for sure is that it has to be perfect."
    "Emma and Sam are literally the girls of my dreams, so they deserve as much."
    "And when I propose to the pair of them, it has to be a moment we'll all remember."
    "Plus the rings that I've picked out for them are weighing be down as I wait for that moment to come."
    "I can literally feel myself starting to sweat as time ticks on."
    "Luckily for me, it seems that Emma and Sam are none the wiser."
    "They just keep on chatting away to each other, oblivious to my mental torture."
    show emma casual normal at right5
    show samantha casual normal at left5
    with dissolve
    "In fact, they only seem to snap out of it when I actually put my plan into action."
    show emma casual annoyed at right5
    emma.say "[hero.name]?"
    emma.say "What are you doing?"
    show samantha casual annoyed at left5
    samantha.say "Huh?"
    samantha.say "Whoa..."
    samantha.say "Yeah, [hero.name] - what's going on?"
    "I'm already down on one knee by the time I'm being questioned."
    "So it seems like the only logical answer is to make my proposal."
    "Reaching into my pocket, I pull out the rings."
    "Then I hold them up to Emma and Sam."
    mike.say "Emma..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake..."
    else:
        mike.say "Sam..."
    mike.say "Will you marry me?"
    show emma surprised at startle
    show samantha surprised at startle
    "I've never seen such surprise on either of their faces."
    "Emma and Sam look like they've been slapped with a wet fish!"
    "All I can do is keep on kneeling and smiling."
    "Hoping that they snap out of it soon."
    if emma.love >= 195 and samantha.love >= 195:
        "And when they do, I almost jump out of my skin."
        show samantha happy at startle
        samantha.say "YES!"
        samantha.say "Of course I will!"
        samantha.say "I've been waiting so long for you to ask, [hero.name]."
        samantha.say "Part of me was afraid you never would."
        "Emma looks more than a little surprised by Sam's reaction."
        "But she soon recovers enough to answer for herself."
        show emma happy at startle
        emma.say "I will, [hero.name]."
        emma.say "I...I'm just so bowled over at being asked!"
        emma.say "But the answer's yes."
        emma.say "I will marry you!"
        "I'm feeling a little bowled over myself too."
        "But I still manage to get to my feet."
        "And then I slide the rings onto their fingers."
        mike.say "Wow..."
        mike.say "We're really doing it!"
        mike.say "We're getting married!"
        "Emma and Sam nod happily, admiring their rings."
        "And I'm happy just to be able to say this went so well."
        $ emma.set_fiance()
        $ samantha.set_fiance()
    elif emma.love >= 195 and samantha.love < 195:
        "And when they do, I almost jump out of my skin."
        samantha.say "Oh no, [hero.name]!"
        show samantha annoyed
        samantha.say "I just got out of one marriage."
        samantha.say "What makes you think I want to jump straight into another?"
        "Emma looks more than a little surprised by Sam's reaction."
        "But she soon recovers enough to answer for herself."
        show emma happy at startle
        emma.say "I will, [hero.name]."
        emma.say "I...I'm just so bowled over at being asked!"
        emma.say "But the answer's yes."
        emma.say "I will marry you!"
        "I'm feeling a little bowled over myself too."
        "But I still manage to get to my feet."
        "I hadn't really figured on one saying yes and the other saying no."
        "All I can do is slip the ring onto Emma's finger."
        "Looking at Sam in confusion as I do so."
        "Because I have no idea what this means for the three of us."
        "Can we stay together as a threesome if we're not all married?"
        "Will Sam even want to stay with Emma and me if we do?"
        $ emma.set_fiance()
        $ samantha.love -= 25
        $ samantha.sub -= 25
    elif emma.love < 195 and samantha.love >= 195:
        "And when they do, I almost jump out of my skin."
        show samantha happy at startle
        samantha.say "YES!"
        samantha.say "Of course I will!"
        samantha.say "I've been waiting so long for you to ask, [hero.name]."
        samantha.say "Part of me was afraid you never would."
        "Emma looks more than a little surprised by Sam's reaction."
        "But she soon recovers enough to answer for herself."
        emma.say "I can't marry you either, [hero.name]."
        show emma annoyed
        emma.say "Not after all that stuff about seeing me in your dreams."
        emma.say "I need to know that you love me for me."
        emma.say "You know, the real me?"
        "I'm feeling a little bowled over myself too."
        "But I still manage to get to my feet."
        "I hadn't really figured on one saying yes and the other saying no."
        "All I can do is slip the ring onto Sam's finger."
        "Looking at Emma in confusion as I do so."
        "Because I have no idea what this means for the three of us."
        "Can we stay together as a threesome if we're not all married?"
        "Will Emma even want to stay with Sam and me if we do?"
        $ samantha.set_fiance()
        $ emma.love -= 25
        $ emma.sub -= 25
    else:
        "And when they do, I can feel my spirits plummet."
        samantha.say "Oh no, [hero.name]!"
        show samantha annoyed
        samantha.say "I just got out of one marriage."
        samantha.say "What makes you think I want to jump straight into another?"
        "Emma nods as she hears what Sam has to say."
        "The she adds her own answer to the mix."
        emma.say "I can't marry you either, [hero.name]."
        show emma annoyed
        emma.say "Not after all that stuff about seeing me in your dreams."
        emma.say "I need to know that you love me for me."
        emma.say "You know, the real me?"
        "Looking more than a little shocked, I stare at them in amazement."
        "And I get back to my feet slowly, shaking my head."
        "This was supposed to go well, to be perfect."
        "And I thought I knew these guys well enough to be sure it would."
        mike.say "I..."
        mike.say "I don't know what to say..."
        mike.say "Neither of you wants to marry me?"
        show emma sad
        show samantha sad
        "Emma and Sam exchange a worried glance."
        "As if they're only now becoming aware of how much they've hurt me."
        samantha.say "Well..."
        show samantha normal
        samantha.say "Not right now, [hero.name]."
        emma.say "But who knows..."
        show emma normal
        emma.say "That might change!"
        "I try to force a smile onto my face."
        "But it still feels like I'm dying inside."
        $ emma.love -= 25
        $ emma.sub -= 25
        $ samantha.love -= 25
        $ samantha.sub -= 25
    return

label emma_samantha_male_ending:

    if renpy.has_label("friendly_harem_achievement_3") and not game.flags.cheat:
        call friendly_harem_achievement_3 from _call_friendly_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I can't believe that I'm actually standing here right now, that this day's actually come."
    "In fact, I feel the need to pinch myself, just to make sure I'm not dreaming..."
    "Ouch!"
    "Definitely not dreaming!"
    "I really am standing at the alter, all dressed up in a fancy suit."
    "And I really am waiting for the girls of my dreams to come walking down the aisle too!"
    "The chapel is packed to the rafters with wedding guests, all straining for the best view."
    "I recognise my own friends and family sitting out there."
    "And I can see the faces that Emma and Sam have introduced to me too."
    "I have to admit that I don't recognise half as many of them as I'd like."
    "But I can sort all of that out at the reception when the ceremony's over."
    "Suddenly music begins to play, and everyone seems to come to life."
    "All eyes turn towards the back of the chapel, looking for the brides."
    "And when the doors open to let them in, I feel like I can breathe a sigh of relief."
    show emma wedding normal zorder 4 at center, zoomAt (1.0, (880, 740))
    show samantha wedding normal zorder 5 at center, zoomAt (1.0, (400, 740))
    with fade
    "Emma and Sam come sweeping into the chapel a moment later."
    "They're walking down the aisle, side by side."
    "But I have to take a moment to appreciate each of them alone."
    "As they're such strikingly different girls."
    "My eyes fall on Emma first, the shorter and slighter of my brides."
    "She's perfect in her dress, cut to flatter her petite figure."
    "But the most beautiful thing about her is the smile on her face."
    if emma.is_visibly_pregnant:
        "Part of the reason for that might be the size of her belly!"
        "Because I know that Emma's very proud of the fact she's pregnant."
        "And there's no way she's ever going to hide that fact."
    "In contrast, Sam's tall, full-figured and confident."
    "She strides down the aisle with the confidence of someone that's done this before."
    "But to me she looks impossibly better today than she did when she married Ryan."
    if samantha.is_visibly_pregnant:
        "Her dress doesn't try to hide the fact that she's expecting."
        "And that's something that makes me swell with pride."
        "Because it's a statement of the new start we're making together."
    "I'm so busy staring at the two of them that I'm totally distracted."
    show emma at center, zoomAt (1.65, (840, 1140))
    show samantha blush at center, zoomAt (1.65, (440, 1140))
    with vpunch
    "So when they actually reach the alter, I almost jump in surprise."
    emma.say "[hero.name]!"
    show emma normal
    emma.say "Wake up!"
    samantha.say "You're not supposed to fall asleep until tonight."
    show samantha normal
    samantha.say "And not until you've done your duty either!"
    "Priest" "Ahem..."
    "This time it's Emma and Sam's turn to jump as the priest coughs."
    "And I can't help chuckling as they hurry to do as they're told."
    "Priest" "Shall we begin?"
    "Priest" "Very good..."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people..."
    "Priest" "In the bonds of holy matrimony."
    "The rest of the ceremony is the usual affair."
    "And it all goes smoothly and without hitch."
    "So before I know it, we're onto the vows!"
    "Priest" "Do you, Emma..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show emma happy at startle
    emma.say "I do."
    show emma normal
    "Priest" "Very good."
    "Priest" "Do you, Sam..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show samantha happy at startle
    samantha.say "I do."
    show samantha normal
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    show emma happy
    show samantha happy
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these three may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "Everyone else in the chapel does the usual, looking around and chuckling."
    if not game.flags.ryandead:
        "But Sam and I exchange a brief glance, both of us worried about the same thing."
        "We talked about the chances of Ryan showing up at this point to cause trouble."
        "I feel like we're holding our breath and waiting..."
    "Priest" "Very well."
    "Priest" "It is therefore my pleasure to pronounce you married."
    "Priest" "You may celebrate in a way that you find fitting."
    show emma normal
    show samantha normal
    "Sam and I let out a sigh of relief."
    "Emma seems not to notice, which is a relief."
    show emma happy zorder 4 at center, zoomAt (2.0, (820, 1340))
    show samantha happy zorder 5 at center, zoomAt (2.0, (460, 1340))
    with fade
    "Then we come together and embrace."
    "And the kiss that follows is something to remember."
    "We did it - we're married!"
    "And now we have the rest of our lives to spend together."

    scene bg park
    show emma casual annoyed at left5
    with fade
    emma.say "Ooh..."
    emma.say "I don't know if this is a good idea, Sam!"
    show samantha casual surprised at right5 with dissolve
    samantha.say "Huh?"
    samantha.say "What are you talking about, Emma?"
    samantha.say "You're literally [hero.name]'s dream girl!"
    show samantha happy
    samantha.say "Your story's like a fairy-tale!"
    emma.say "Oh...but that's just it, Sam."
    emma.say "It's like something that's made up."
    emma.say "Who's going to believe that he saw me in his dreams?"
    show emma blush
    emma.say "It sounds so stupid!"
    emma.say "Not like the story you and he have."
    samantha.say "Don't be silly, Emma."
    show samantha normal
    samantha.say "We just liked each other while we were with other people, that's all!"
    samantha.say "It's hardly a romantic epic of a tale."
    emma.say "Oh yeah?"
    show emma normal
    emma.say "Now who's the one being silly, Sam?"
    emma.say "[hero.name] calls you his cupcake."
    emma.say "He held a torch for you all that time."
    show emma blush
    emma.say "And he was your knight in shining armour when Ryan betrayed you!"
    samantha.say "Okay, Emma, okay..."
    show samantha annoyed
    samantha.say "This is turning into us running ourselves down."
    samantha.say "Can we just agree that [hero.name] loves us both?"
    show emma normal
    emma.say "Sorry, Sam..."
    emma.say "You're right."
    emma.say "We all bring something unique to this relationship."
    show samantha normal
    samantha.say "So remind me what [hero.name] brings?"
    samantha.say "Like, is he the one that steals all the blankets at night?"
    emma.say "Oh, Sam!"
    show emma annoyed
    emma.say "That's so bad!"
    emma.say "But it is true."
    show emma happy
    samantha.say "They say it's those little quirks that make you love some one."
    samantha.say "And [hero.name] has so many, that must be why we adore him!"
    emma.say "Seriously though, I do think we make a neat little household."
    show emma normal
    emma.say "It's just a shame that [bree.name] and Sasha chose to move out."
    samantha.say "I mean, I liked those girls."
    samantha.say "But it was getting crowded around here."
    samantha.say "Plus now we have [hero.name] all to ourselves!"
    if (emma.is_visibly_pregnant or emma.flags.mikeBabies >= 1) and (samantha.is_visibly_pregnant or samantha.flags.mikeBabies >= 1):
        emma.say "Hmm..."
        emma.say "Funny how having Cora and [hero.name] Junior around doesn't make it feel that way."
        samantha.say "That's different, Emma."
        samantha.say "I don't mind giving up space for our own kids!"
    elif emma.is_visibly_pregnant or emma.flags.mikeBabies >= 1:
        emma.say "Hmm..."
        emma.say "Funny how having little Cora around doesn't make it feel that way."
        samantha.say "That's different, Emma."
        samantha.say "I don't mind giving up space for a child that grew inside of you!"
    elif samantha.is_visibly_pregnant or samantha.flags.mikeBabies >= 1:
        samantha.say "Well, when he's not being wrapped around [hero.name] Junior's finger!"
        emma.say "Oh yeah!"
        emma.say "That little tearaway sure loves his daddy!"
    else:
        emma.say "That could change if we have any new additions!"
        emma.say "We'd be up to our noses in nappies and bottles!"
        samantha.say "That's different, Emma."
        samantha.say "I don't mind giving up space for our own kids!"
    emma.say "Maybe you're right, Sam."
    show emma blush
    emma.say "Maybe I should just accept that we're living in a dream come true."
    samantha.say "On one condition, Emma."
    emma.say "What's that?"
    samantha.say "You never tell [hero.name] that!"
    show samantha happy
    samantha.say "You don't want him to start thinking that he can slack off, do you?"
    samantha.say "I mean, can you even imagine how big his head would get if you told him?"
    emma.say "Oh..."
    show emma normal
    emma.say "So you think we need to sort of...treat him mean to keep him keen?"
    samantha.say "Maybe not as strong as that."
    show samantha normal
    samantha.say "More like just keep him on his toes."
    samantha.say "So he keeps us in the style to which we've become accustomed."
    show samantha happy
    samantha.say "You know - living the dream!"
    scene bg black with dissolve
    pause 2.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
