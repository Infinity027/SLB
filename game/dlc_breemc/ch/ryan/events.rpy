init python:
    Event(**{
    "name": "ryan_female_event_01",
    "label": "ryan_female_event_01",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsHour(11, 16),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("street")),
        PersonTarget(mike,
            Not(IsHidden()),
            MinStat("love", 75),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "ryan_female_event_02",
    "label": "ryan_female_event_02",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsDone("ryan_female_event_01"),
        HeroTarget(
            IsGender("female"),
            IsRoom("mall1")),
        PersonTarget(ryan,
            MinStat("love", 20),
            IsFlag("delay", False)
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "ryan_female_event_03",
    "label": "ryan_female_event_03",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsDone("ryan_female_event_02"),
        HeroTarget(
            IsGender("female"),
            IsRoom("church")),
        PersonTarget(ryan,
            MinStat("love", 40),
            IsFlag("delay", False)
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "ryan_female_event_04",
    "label": "ryan_female_event_04",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsDone("ryan_female_event_03"),
        HeroTarget(
            IsGender("female"),
            IsHour(22, 2),
            IsRoom("bedroom4")),
        PersonTarget(ryan,
            MinStat("love", 60),
            IsFlag("delay", False)
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "ryan_female_event_05",
    "label": "ryan_female_event_05",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsDone("ryan_female_event_04"),
        HeroTarget(
            IsGender("female"),
            IsHour(8, 22),
            Not(OnDate()),
            HasRoomTag("street"),
            ),
        PersonTarget(ryan,
            IsPresent(),
            MinStat("love", 80),
            IsFlag("delay", False)
            ),
        ],
    "do_once": True,
    })

label ryan_female_event_01:
    scene expression f"bg {game.room}" at center, zoomAt(1, (640, 720)) with fade
    show mike happy zorder 1 at center, zoomAt(0.65, (640, 720))
    show samantha happy zorder 2 at center, zoomAt(0.7, (840, 720))
    show ryan normal zorder 3 at center, zoomAt(0.7, (440, 720))
    "I could be all coy and innocent about my reaction when I see [mike.name] chatting to a couple of strangers."
    "You know, like pretend that I'm simply noting the fact while I go about my own business and all that?"
    "But the truth is that I can't help seeing that the girl is really pretty and the guy's kind of handsome too."
    "Plus there's the obvious signs from [mike.name]'s body-language that there aren't just a couple of randoms either."
    "I mean, I'm no expert on the subject, but he's totally leaning in as close to that girl as he possibly can."
    "And every time the guy opens his mouth, it's almost like [mike.name] winces in actual irritation."
    "All the while I'm observing this, I make a point of sidling closer to where they're standing."
    "Because I figure that I can make it look like I've accidentally stumbled into hearing range."
    "But the moment I'm just about close enough, something seems to happen that sets [mike.name] off."
    show ryan smile
    show samantha mindless
    show mike surprised at vshake
    mike.say "YOU'RE FUCKING KIDDING ME?!?"
    mike.say "You...you can't be serious, can you?"
    show mike down at startle(0.1, 5)
    show samantha normal
    "The sudden outburst is enough to make me jump back a little."
    "As well as causing me to let out a little yelp of genuine surprise."
    show bg street at center, vshake
    show mike at vshake
    show ryan at vshake
    show samantha at vshake
    bree.say "Aargh!"
    show mike surprised at traveling(1, 2, (640, 800))
    show samantha surprised at traveling(1.1, 2, (950, 820))
    show ryan whining at traveling(1.1, 2, (340, 820))
    show bg street at traveling(1.3, 2, (640, 720))
    "Suddenly I realise that none of them are talking to each other anymore."
    "And instead, all three are now staring straight at me."
    "Whatever made [mike.name] raise his voice seemingly forgotten."
    show mike at startle(0.1, 5)
    show ryan at startle(0.1, 5)
    show samantha at startle(0.1, 5)
    show bg street at startle(0.1, 5)
    bree.say "Oh..."
    bree.say "Erm..."
    if hero.morality >= 25:
        bree.say "Don't mind me - you made me jump, that's all!"
    elif hero.morality <= -25:
        bree.say "Wow, [mike.name] - you really know how to make a girl scream!"
    else:
        bree.say "Sorry, [mike.name] - you just made me jump, you know?"
    show mike annoyed
    "[mike.name] looks more than a little annoyed right now, and flustered too."
    "But I can't quite tell if that's on account of what I just did."
    "Or else it's actually whatever he heard from the couple in the seconds beforehand."
    show mike talkative at startle(0.1, 5)
    mike.say "I'm..."
    mike.say "I'm sorry, [hero.name]..."
    mike.say "I didn't see you there."
    show mike normal
    "I'm about to do the usual thing of accepting the apology and then asking for an explanation."
    "But someone else beats me to it, proving that I'm not the only one that's curious around here."
    "Because the handsome guy is now looking straight at me."
    show ryan evil at startle(0.1, 5)
    ryan.say "Goodness, [mike.name]..."
    ryan.say "It looks like your manners haven't improved any!"
    ryan.say "Aren't you going to introduce us to your friend here?"
    show ryan normal
    "As soon as the question is asked, the pretty girl inserts herself into the conversation too."
    show samantha talkative at startle(0.1, 5)
    samantha.say "Don't be so hard on him, babe..."
    samantha.say "We did just hit him with some big news."
    samantha.say "[mike.name] always did have a hard time processing that kind of thing."
    show samantha normal
    "Okay, so my sixth sense for this kind of thing is really starting to kick in now."
    "And it's telling me that these two know [mike.name] from way back."
    "Plus they're obviously a couple too."
    "Yet [mike.name]'s warm towards her and stand-offish with the guy - which is interesting."
    show mike at startle(0.1, 5)
    show ryan at startle(0.1, 5)
    show samantha at startle(0.1, 5)
    show bg street at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "Yeah, he can be a little like that, can't he?"
    elif hero.morality <= -25:
        bree.say "He'd get it quicker if you wrote it on a tight, wet T-shirt - right?!?"
    else:
        bree.say "Tell me about it, why don't you?!?"
    bree.say "I'm [hero.name], by the way."
    bree.say "One of [mike.name]'s housemates."
    "To me that's kind of a mundane piece of information."
    "It's no more interesting than, say, what I had for breakfast this morning."
    "But for some reason it seems to instantly arouse the interest of the pair."
    show samantha surprised at startle(0.1, 5)
    samantha.say "You are?!?"
    samantha.say "So are we!"
    show samantha stuned
    show ryan smile at startle(0.1, 5)
    ryan.say "Well we used to be..."
    ryan.say "Before we moved out and got a place together."
    show ryan normal
    "Until now, [mike.name] seemed to be stuck on the outside of the conversation."
    "Like he was still grappling with whatever these two just told him."
    "But now he seems to have finally gotten his head back together."
    show mike shout at startle(0.1, 5)
    mike.say "Hey..."
    mike.say "I'm still here, you know?"
    show mike talkative at startle(0.1, 5)
    mike.say "Okay, okay...[hero.name], meet Sam - my former housemate."
    show mike normal
    "Sam gives me what looks and feels like a genuinely warm smile."
    "And despite how pretty she is, I find myself instantly liking her."
    show samantha talkative at startle(0.1, 5)
    samantha.say "It's Samantha, obviously..."
    samantha.say "But you can call me Sam, if you like?"
    show samantha normal
    "I'm about to say something that I hope is pleasant in return."
    show ryan annoyed with dissolve
    "But then the handsome guy coughs and rolls his eyes."
    show ryan smile at startle(0.1, 5)
    ryan.say "Ahem..."
    ryan.say "Did I turn invisible all of a sudden?"
    show ryan normal
    show mike annoyed with dissolve
    "[mike.name] shoots him another one of those looks in response."
    "The kind that make me want to dig into their shared past."
    show mike talkative at startle(0.1, 5)
    mike.say "Okay, okay..."
    mike.say "This is Ryan, who I used to live with too."
    show mike normal
    show ryan evil at startle(0.1, 5)
    ryan.say "Always the joker, aren't you, [mike.name]?"
    show ryan normal
    show samantha talkative at startle(0.1, 5)
    samantha.say "Seriously though, [hero.name]..."
    samantha.say "It's great to finally meet you."
    samantha.say "[mike.name] mentioned he had new housemates."
    samantha.say "But it just seems so weird to imagine other people living in what used to be our house!"
    show samantha normal
    show ryan smile at startle(0.1, 5)
    ryan.say "It's not that hard to imagine, babe!"
    ryan.say "I can totally picture [hero.name] using the pool out back."
    ryan.say "Or sunbathing in the garden - right, [hero.name]?"
    show ryan normal
    "Okay...so that was a little forward, at least if you ask me!"
    "I have an awkward smile on my face as I look from Ryan to Sam."
    "But she doesn't seem to notice either that or what he just said."
    show mike down at stepback(0.1, 5,0)
    pause 0.5
    show mike down at stepback(0.1, 5,0)
    pause 0.5
    "And when I glance over at [mike.name], he just kind of frowns and shakes his head."
    show mike at startle(0.1, 5)
    show ryan at startle(0.1, 5)
    show samantha at startle(0.1, 5)
    show bg street at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "That's a little specific, don't you think?"
    elif hero.morality <= -25:
        bree.say "Oh yeah?"
        bree.say "Looks like I need to watch myself around you, Ryan!"
    else:
        bree.say "Erm...and doing things that don't need me to be almost naked too?"
    show samantha stuned
    "Again, Sam seems to totally miss what I'm saying and Ryan just acts like it's totally normal."
    "But luckily for me, [mike.name] chooses that exact moment to step in and take back control."
    show samantha normal
    show mike talkative at startle(0.1, 5)
    mike.say "You should tell [hero.name] all about your good news, yeah?"
    show mike annoyed
    "The suggestion seems to reset Sam and Ryan's brains in mere seconds."
    show samantha happy at startle(0.1, 5)
    show ryan smile at startle(0.1, 5)
    "Suddenly they're both all smiles and nods."
    show samantha happy at startle(0.1, 5)
    samantha.say "Oh, sure..."
    samantha.say "We were just telling [mike.name] that we're getting married."
    show samantha wink
    show ryan smile at startle(0.1, 5)
    ryan.say "Yeah, she finally roped me into it!"
    show ryan normal
    "Ryan makes a gesture of being collared and dragged along."
    show samantha flirt at stepback(0.1, 5,0)
    pause 0.5
    show samantha flirt at stepback(0.1, 5,0)
    pause 0.5
    "And Sam shakes her head, like it's somehow endearing."
    "Though now I get the impression that they're expecting me to say something in return."
    menu:
        "Congratulate Sam and Ryan warmly":
            "I don't want to look like I'm anything but happy for the pair of them."
            "So I put the biggest smile on my face that I can manage and nod in response."
            show mike at startle(0.1, 5)
            show ryan at startle(0.1, 5)
            show samantha at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "Oh wow..."
                bree.say "That's such amazing news!"
                bree.say "I'm so happy for the both of you."
            elif hero.morality <= -25:
                bree.say "Well, you know what that means, don't you?"
                bree.say "No more being wild in public."
                bree.say "Now you have to keep it all in the bedroom!"
            else:
                bree.say "Get out of here!"
                bree.say "You crazy couple of kids..."
                bree.say "I think that's such great news."
            show samantha happy at startle(0.1, 5)
            show ryan smile at startle(0.1, 5)
            "Sam and Ryan are smiling and nodding the whole time that I'm talking."
            "But I get the distinct impression they're not really paying much attention."
            "Like they're used to people gushing over the news of their impending nuptials."
            "And so they tune out the actual details when they hear it."
            show samantha flirt
            show ryan whining at startle(0.1, 5)
            ryan.say "What can I say, [hero.name]?"
            ryan.say "She wore me down!"
            show ryan normal
            show samantha happy at startle(0.1, 5), vshake
            samantha.say "Oh, Ryan..."
            samantha.say "You're so funny!"
            show samantha flirt
            show mike talkative at startle(0.1, 5)
            mike.say "Yeah..."
            mike.say "So funny I forgot to laugh."
            show mike annoyed
            $ samantha.flags.friendship += 1
            $ ryan.love += 1
        "Tease Ryan about being off the market":
            "Man, I never even met these people before now."
            "But all of a sudden I'm getting bombarded with the details of their lives."
            "So how in the hell am I supposed to react to all of this?"
            "But one thing I do know is that [mike.name] seems to like Sam more than Ryan."
            "And so I decide to turn my attention to him, so as not to seem like a rival to her."
            show mike at startle(0.1, 5)
            show ryan at startle(0.1, 5)
            show samantha at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "So no more bachelor life for you, Ryan?"
                bree.say "Sam's going to make an honest man out of you!"
            elif hero.morality <= -25:
                bree.say "Shame you're gonna be off the market, Ryan..."
                bree.say "Looks like we met at totally the wrong time!"
            else:
                bree.say "Ah, man - another eligible bachelor off the market!"
                bree.say "What are we poor girls going to do?"
            show ryan normal at startle(0.1, 5)
            pause 0.5
            show ryan at traveling(1.3, 1.2, (340, 920))
            "Ryan nods and leans in closer as soon as it's clear I'm talking to him."
            "And the fact doesn't seem to be lost on Sam and [mike.name] either."
            show ryan smile at startle(0.1, 5)
            ryan.say "What can I say, [hero.name]..."
            ryan.say "Your loss is Sam's gain!"
            show ryan normal
            show samantha happy at startle(0.1, 5), vshake
            samantha.say "Oh, Ryan..."
            samantha.say "You're so funny!"
            show samantha flirt
            show mike talkative at startle(0.1, 5)
            mike.say "Yeah..."
            mike.say "So funny I forgot to laugh."
            show ryan at traveling(1.1, 1, (340, 820))
            show mike annoyed
            $ samantha.flags.suspicion += 1
            $ ryan.love += 1
        "Keep neutral congratulations":
            "Okay, so I don't know these two from Adam."
            "And [mike.name] introduced us like, what, a couple of minutes ago?"
            "I don't want to sound like I'm being overly familiar here."
            "So the best thing would be to keep things as neutral as possible."
            show mike at startle(0.1, 5)
            show ryan at startle(0.1, 5)
            show samantha at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "That's wonderful news."
                bree.say "Your family and friends must be delighted."
            elif hero.morality <= -25:
                bree.say "That's great news for you two..."
                bree.say "Just make sure the wedding night is wild, okay?"
            else:
                bree.say "Congratulations, guys..."
                bree.say "You and your friends should have a great time come the big day!"
            show samantha sadsmile at startle(0.1, 5)
            show ryan sad at startle(0.1, 5)
            "Sam and Ryan nod as I congratulate them."
            "But I get the distinct feeling they were expecting more."
            show samantha talkative at startle(0.1, 5)
            samantha.say "Erm..."
            samantha.say "Thank you, [hero.name]."
            show samantha sadsmile
            show ryan whining at startle(0.1, 5)
            ryan.say "Yeah..."
            ryan.say "That was...nice."
            show ryan normal
    "There's an awkward silence once everyone seems to have said their piece."
    "And I feel like I'm waiting for someone, anyone to speak up and break it."
    show mike blush at startle(0.1, 5)
    mike.say "Oh..."
    mike.say "[hero.name]..."
    mike.say "I just thought of something!"
    show mike down
    "Before [mike.name] can say another word, Ryan cuts in on the conversation."
    show ryan smile at startle(0.1, 5)
    ryan.say "You should make a note of it, [hero.name]..."
    ryan.say "Because it doesn't happen that often!"
    show samantha normal
    show mike annoyed with dissolve
    "Ryan grins as [mike.name] shoots him a shady look."
    "But Sam doesn't seem to pick up on the obvious tension between them."
    show samantha surprised at startle(0.1, 5)
    samantha.say "Oh stop being so mean to poor [mike.name]!"
    samantha.say "I'm sure he has something important to say."
    show samantha talkative at startle(0.1, 5)
    samantha.say "Don't you, [mike.name]?"
    show samantha normal
    show mike annoyed
    "I can see that Sam thinks she's helping [mike.name] by coming to his defence."
    "But from the look on his face right now, that's not how it seems to him."
    show mike talkative at startle(0.1, 5)
    mike.say "Yeah..."
    mike.say "Thanks, Sam..."
    show mike blush
    mike.say "I was gonna ask, [hero.name]..."
    mike.say "I just got my invite to the wedding, and I need a plus one."
    mike.say "So...you wanna come with me?"
    show mike sadsmile
    menu:
        "Agree to be [mike.name]'s plus one":
            "I feel like there's a lot of backstory here that I don't know."
            "And so being at the wedding would be a good way to fill in the gaps."
            show mike at startle(0.1, 5)
            show ryan at startle(0.1, 5)
            show samantha at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            bree.say "Okay, [mike.name]..."
            bree.say "That sounds like a lot of fun."
            bree.say "So count me in."
            show samantha happy
            show ryan smile
            "Of course, [mike.name] looks instantly delighted with my answer."
            show mike happy at startle(0.1, 5)
            mike.say "That's great, [hero.name]!"
            show mike normal
            "Sam and Ryan seem to be pretty pleased too."
            show samantha happy at startle(0.1, 5)
            samantha.say "That's great news, [hero.name]!"
            samantha.say "Maybe we can find the time to get to know each other a little better?"
            show samantha normal
            show ryan smile at startle(0.1, 5)
            ryan.say "Or a LOT better!"
            show ryan normal
            $ mike.love += 1
            $ ryan.love += 1
            $ samantha.flags.friendship += 1
        "Refuse to be [mike.name]'s plus one":
            "Okay, this whole thing seems to be going way too fast for my liking."
            "I only just met these guys, and already [mike.name]'s inviting me along to their wedding!"
            show mike at startle(0.1, 5)
            show ryan at startle(0.1, 5)
            show samantha at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            bree.say "No, [mike.name]..."
            bree.say "I don't know Sam and Ryan well enough."
            bree.say "Surely you know someone else who you could take?"
            show mike sad with dissolve
            show samantha sad
            show ryan sad
            "[mike.name] looks instantly crestfallen at my refusal."
            "And I'm sure that he's about to try and change my mind."
            "But that's when Sam and Ryan wade into the discussion."
            show ryan whining at startle(0.1, 5)
            ryan.say "Ouch..."
            ryan.say "Looks like you crashed and burned again, [mike.name]!"
            ryan.say "You never did have much luck with the ladies."
            show ryan normal
            show samantha talkative at startle(0.1, 5)
            samantha.say "Don't listen to him, [mike.name]."
            samantha.say "It's okay if you have to come on your own."
            show samantha sadsmile
            $ mike.love -= 1
        "Ask for time to think about it":
            "I feel like there's a lot of backstory here that I don't know."
            "And so being at the wedding would be a good way to fill in the gaps."
            "But this whole thing seems to be going way too fast for my liking."
            "I only just met these guys, and already [mike.name]'s inviting me along to their wedding!"
            "Plus I kinda feel like I'm being drawn into whatever history there is between all of them."
            show mike at startle(0.1, 5)
            show ryan at startle(0.1, 5)
            show samantha at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            bree.say "Okay, [mike.name], here's what I'll do..."
            bree.say "I'll check my calendar and see if I'm free."
            bree.say "And if nothing else comes up - I'll think about it."
            show ryan normal
            show mike sad
            "[mike.name] looks instantly crestfallen at my refusing to say yes."
            "And I'm sure that he's about to try and change my mind."
            "But that's when Sam and Ryan wade into the discussion."
            show samantha talkative at startle(0.1, 5)
            samantha.say "Don't worry, [mike.name]..."
            samantha.say "I'm sure she'll say yes in the end."
            show samantha sadsmile
            show ryan whining at startle(0.1, 5)
            ryan.say "And if not, then what the hell?"
            ryan.say "It's not like it'll be the first time you crashed and burned with the ladies!"
            show ryan normal
    $ ryan.flags.delay = TemporaryFlag(True, 2)
    $ ryan.unhide()
    scene bg black with dissolve
    return

label ryan_female_event_02:
    if ryan.love.max < 40:
        $ ryan.love.max = 40
    scene bg mall1 at center, zoomAt(1.4, (640, 820)) with fade
    show ayesha at blacker, center, zoomAt(1.6, (640, 1020)), slide(2000, 2)
    show scottie at blacker, center, zoomAt(1, (640, 720)), slide(1500, 1)
    show sasha at blacker, center, zoomAt(1.4, (1640, 920)), slide(2200, 2.5)
    show shawn at blacker, center, zoomAt(1.2, (1640, 820)), slide(2000, 2.5)
    show aletta at blacker, center, zoomAt(1.6, (1640, 1020)), slide(2500, 3)
    show shiori at blacker, center, zoomAt(1, (1640, 720)), slide(3000, 5)
    "The mall's pretty busy today, most of the space inside thronging with shoppers."
    "But that's not something that's going to stop me getting what I came here for."
    "Because I'm an expert at weaving my way through the mass of heaving bodies."
    "Plus most of them are slow-moving and distracted with stuff like window-shopping."
    "Whereas I'm totally nimble and have my mind focussed like a laser-beam."
    show ryan at center, blacker, zoomAt (1.1, (940, 780)) with easeinright
    "At least that is until someone else seems to have the same idea as me."
    "Because as I step into a convenient gap between two other shoppers, another body tries to do the same thing."
    show ryan at blacker, traveling(4, 0.3, (640, 2620))
    show bg mall1 at center, traveling(1.8, 0.3, (640, 970))
    pause 0.3
    show ryan at blacker, traveling(3.2, 0.3, (640, 2020))
    show bg mall1 at center, traveling(1.6, 0.3, (640, 870))
    with vpunch
    show bg mall1 at blur(10) with dissolve
    "And the inevitable result is a collision, making the person who just ran into me drop the bags they're carrying."
    "Which is a little better than the deal I get - because I end up landing on my ass!"
    show bg mall1 at startle(0.1, 5)
    bree.say "Ouch..."
    show ryan at blacker, traveling(1.8, 0.3, (640, 1220))
    bree.say "Hey, buddy - watch where you're going!"
    hide ryan
    show ryan angry at center, zoomAt(1.8, (640, 1220))
    ryan.say "Urgh..."
    show ryan at hshake
    ryan.say "What are you talking about, you clumsy jerk?!?"
    "I'm still shaking my head as we exchange angry and irritable words."
    "And I haven't yet taken the time to actually look up at the other person."
    "But as I turn my gaze in their direction, I realise it sounds vaguely familiar."
    show ryan whining with dissolve
    show bg mall1 at blur(0) with dissolve
    ryan.say "Oh..."
    ryan.say "It's [hero.name], isn't it?"
    show ryan normal
    "At the same time as I hear him say my name, I look up and recognise the guy's face."
    show bg mall1 at startle(0.1, 5)
    bree.say "Ryan?"
    bree.say "As in Sam and Ryan?"
    show ryan upset
    "I see Ryan's brow furrow a little as I associate him with his fiancée."
    show ryan whining at stepback(0.1, 5,0)
    pause 0.5
    show ryan whining at stepback(0.1, 5,0)
    pause 0.5
    "But then he seems to shake it off as he remembers his manners and sticks a hand out towards me."
    show ryan whining at startle(0.1, 5)
    ryan.say "As in Ryan running around like a madman before the wedding!"
    scene bg mall1 at center, zoomAt(1.2, (640, 720))
    show ryan sad at center, zoomAt(1.4, (640, 970))
    with fade
    "I take the hand Ryan offers me and let him help me back to my feet."
    "And then I watch as he starts to pick up the bags he dropped in the collision."
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    bree.say "Oh..."
    bree.say "Here, Ryan..."
    bree.say "Let me help you with that!"
    "I hurry to pick up the last of the bags, as Ryan's wasting no time in grabbing them."
    with vpunch
    "But the result is that I take hold of the very last one a second before he does."
    "This means that his hand closes over mine, almost covering it completely."
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "So I pull it away as soon as I get the chance."
        bree.say "I...I'm so sorry, Ryan!"
    elif hero.morality <= -25:
        bree.say "I can't help noting that Ryan's hand feels pretty firm and strong."
        bree.say "And I let it linger there for a moment before I pull it away."
        bree.say "Whoops...good job you've got such strong hands!"
    else:
        bree.say "For a moment his hand lingers atop mine, but then I slowly pull it away."
        bree.say "Oops...sorry, Ryan!"
    "I'm expecting Ryan to pull away pretty quickly with a similar round of excuses."
    show ryan smile with dissolve
    "But instead he stands up slowly, a smile spreading across his face as he does so."
    show ryan at startle(0.1, 5)
    ryan.say "No need to be embarrassed, [hero.name]..."
    ryan.say "It was just an honest mistake."
    ryan.say "Maybe even a harmless little bit of flirting too?"
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    "All I can manage to do is nod and smile, already looking for a way to change the subject."
    "Which is when my gaze settles on the sheer number of bags Ryan's clutching."
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "Goodness, Ryan - that's a lot of shopping!"
    elif hero.morality <= -25:
        bree.say "Wow, Ryan - looks like you're a total mall-whore!"
    else:
        bree.say "Funny, Ryan - I didn't have you down as a hardcore shopper!"
    "Ryan takes a moment to look at all the bags too."
    show ryan upset with dissolve
    "And while he does so, I see his mood take a turn for the worse."
    show ryan whining at startle(0.1, 5)
    ryan.say "Urgh..."
    ryan.say "Normally I wouldn't be seen dead at the mall, [hero.name]..."
    ryan.say "Let alone on a shopping spree like this."
    show ryan normal
    "I can't help frowning, unable to believe anyone could hate the mall so much."
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    bree.say "Really?"
    bree.say "Then why are you..."
    show ryan upset
    "I can't even get the last of my words out before Ryan seems to snap."
    show ryan angry at vshake
    ryan.say "THE DAMN WEDDING!"
    "He almost spits the words at me, a vein standing out on his forehead as he does so."
    show ryan annoyed with dissolve
    pause 0.3
    show ryan sad
    "But then he seems to realise how crazy he looks, and visibly tries to get a hold of himself."
    show ryan whining at startle(0.1, 5)
    ryan.say "I..."
    show ryan smile
    ryan.say "I mean...the wedding - to which I am both devoted and totally excited about!"
    "Okay, okay...I know that this guy can be a little..."
    "Well, let's just say he can be a little flirtatious."
    "But I can't help feeling sorry for him right now."
    "Because he doesn't look anything but one hundred percent harassed."
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "I..."
        bree.say "I hear weddings can be..."
        bree.say "Well, pretty stressful."
    elif hero.morality <= -25:
        bree.say "Wedding stress, right?"
        bree.say "But is it from fear of losing out?"
        bree.say "Or pressure to perform on the big night?"
    else:
        bree.say "So..."
        bree.say "The wedding stress is really starting to kick in, huh?"
    show ryan upset with dissolve
    "Ryan seems to pick up on the gist of what I'm saying to him."
    "Though I can't help feeling he's not really listening to the specifics."
    "Which seems to be one of his defining characteristics."
    show ryan angry at startle(0.1, 5)
    ryan.say "Is it that obvious, [hero.name]?"
    show ryan whining at startle(0.1, 5)
    ryan.say "Uh..."
    ryan.say "Don't get me wrong, I'm totally onboard with the whole wedding thing."
    ryan.say "And I know this is Sam's big say, and all that stuff."
    ryan.say "But I can't help feeling like nobody's aware of MY needs, you know?"
    show ryan sad
    "All I can do is shrug and try to show sympathy for Ryan."
    "Even though I'm not quite sure I agree with what he's saying."
    show ryan at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    bree.say "Erm..."
    bree.say "Like..."
    bree.say "What's bugging you, Ryan?"
    bree.say "Because, you know, a problem shared..."
    show ryan annoyed with dissolve
    "Ryan lets out a weary sigh, which to me sounds just a little too performative."
    show ryan whining at startle(0.1, 5)
    ryan.say "Ah..."
    ryan.say "It's so hard, [hero.name] - and nobody understands."
    ryan.say "They're all like, 'you should be looking after Sam'..."
    ryan.say "Or telling me, 'it's all about the bride'!"
    ryan.say "And then there's all the stuff that the groom has to take care of too."
    ryan.say "Nobody wants to talk about my performance anxiety, or validate me when I need it!"
    show ryan sad at startle(0.1, 5)
    show bg mall1 at startle(0.1, 5)
    "I stand still and do the best I can to nod and smile as I listen to Ryan."
    "But then I notice he's staring straight at me, like he expects me to respond."
    menu:
        "Encourage Ryan to support Samantha":
            "It'd be pretty easy to tear Ryan a new hole right now."
            "To pull him apart for only thinking of himself when Sam needs him so much."
            "But with guys like him, taking a brutal approach never seems to work."
            "Because all they do is assume that you're attacking them."
            "So maybe I need to try something a little more subtle?"
            show ryan annoyed at startle(0.1, 5)
            show bg mall1 at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "I'm sure Sam's feeling the exact same way you are right now, Ryan."
                bree.say "And that's why you need each other - for mutual support."
                bree.say "After all, isn't that how marriages are supposed to work?"
            elif hero.morality <= -25:
                bree.say "Geez, Ryan - what kind of a moron are you?"
                bree.say "If you move heaven and earth for Sam now, think how grateful she'll be in the future."
                bree.say "You'll earn so much credit she'll practically have to offer herself up to you as a living sacrifice!"
            else:
                bree.say "I bet Sam's saying the same thing to someone like [mike.name] right now."
                bree.say "So you need to the be smarter one, Ryan..."
                bree.say "Because you're going to have to do all this and more when you're a husband!"
            "Ryan looks at me with a hard expression on his face all the time I'm thinking."
            show ryan normal with dissolve
            "But by the time I'm done explaining myself, he seems more thoughtful."
            show ryan smile at startle(0.1, 5)
            ryan.say "Hmm..."
            ryan.say "Maybe I have been thinking too short-term recently."
            ryan.say "Thanks, [hero.name] - you've given me a lot to think about."
            show ryan smile at startle(0.1, 5)
            pause 0.5
            show ryan at traveling(1.2, 1, (1600, 800))
            "With that, Ryan gives me a nod of the head and walks away."
            "Looking filled with a new sense of confidence and a spring in his step."
            $ samantha.flags.friendship += 1
        "Try to encourage Ryan with a little flirting":
            "Part of me is thinking that I should be cutting Ryan off at the knees right now."
            "You know, telling him to stop being such a self-pitying asshole and pull himself together?"
            "But the problem is that he's kind of charming, and pretty fun to flirt with."
            "And maybe what he really does need is a little boost in his confidence?"
            show ryan at startle(0.1, 5)
            show bg mall1 at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "I'm sure Sam really does appreciate all you do, Ryan."
                bree.say "She's probably just caught up in the wedding preparation."
                bree.say "And she'll prove it to you on the wedding night too!"
            elif hero.morality <= -25:
                bree.say "Oh don't let it get to you, Ryan."
                bree.say "I can tell that you're more than up to the challenge."
                bree.say "And if you need reminding of that, I'm sure there are plenty of girls willing to help out!"
            else:
                bree.say "Ah, don't let it get to you, Ryan."
                bree.say "You're a great guy - a real catch."
                bree.say "And I'm sure Sam knows that better than anyone."
            show ryan smile with dissolve
            "My words seem to have the desired effect on Ryan."
            show ryan at startle(0.1, 5)
            "As the smile returns to his face and soon enough, he's nodding."
            show ryan at startle(0.1, 5)
            ryan.say "You know what, [hero.name] - you are so right."
            ryan.say "And you're a woman of good taste too."
            ryan.say "Be sure to look me up at the wedding."
            ryan.say "Because I'd love to chat again."
            show ryan normal at startle(0.1, 5)
            pause 0.5
            show ryan at traveling(1.2, 1, (1600, 800))
            "With that, Ryan gives me a nod of the head and walks away."
            "Looking filled with a new sense of confidence and a spring in his step."
            $ ryan.love += 4
            $ ryan.flags.flirt = True
            $ samantha.flags.suspicion += 1
        "Lay down the law for Ryan":
            "Oh man, this guy's such a shameless flirt."
            "And he's totally vain to boot!"
            "What he needs is some tough love."
            "Or maybe just someone to be tough with him."
            show ryan annoyed at startle(0.1, 5)
            show bg mall1 at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "I really think Sam's the one you should be talking to, Ryan."
                bree.say "After all, she's the one you're marrying, remember?"
            elif hero.morality <= -25:
                bree.say "Look, Ryan - I know what you're tyring to do here."
                bree.say "But I'm not gonna be the one to prop you up."
                bree.say "Sam's the one you should go talk to."
            else:
                bree.say "What are you doing saying all of this to me, Ryan?"
                bree.say "We both know Sam's the one you should be talking to."
            show ryan upset with dissolve
            "Of course, that wasn't what Ryan wanted to hear."
            "And the frown on his face confirms my suspicions."
            show ryan angry at startle(0.1, 5)
            ryan.say "Oh come on, [hero.name]..."
            ryan.say "You know I was only asking for a little help."
            show ryan whining at startle(0.1, 5)
            ryan.say "Sam's always too busy to talk to me at the moment."
            show ryan sad at startle(0.1, 5)
            show bg mall1 at startle(0.1, 5)
            bree.say "Then maybe try talking to her about the wedding, Ryan..."
            bree.say "You know, rather than just banging on about yourself?"
            show ryan whining with dissolve
            "Ryan opens his mouth to say something in reply."
            show ryan at traveling(3, 0.8, (-500, 1500))
            show bg mall1 at traveling(1.4, 0.5, (640, 720))
            "But I put my head down and push past him."
            "Not wanting to discuss the matter any further."
            $ ryan.love -= 4
    $ ryan.flags.delay = TemporaryFlag(True, 2)
    return

label ryan_female_event_03:
    if ryan.love.max < 60:
        $ ryan.love.max = 60
    scene bg church wedding at center, zoomAt(1, (640, 720)) with fade
    "Back when [mike.name] first asked me to be his plus one for Sam and Ryan's wedding, it came right out of the blue."
    "In fact it was such a surprise that I almost made a point of saying no on the spot just as suddenly."
    "After all, I'd only met the pair of them a few moments before, when he introduced them to me."
    "But it didn't take me long to change my mind, not once I'd had the chance to really think about it."
    "Because it's not every day that you get invited to a wedding."
    "It's the perfect chance to get dressed up and dance in front of strangers."
    "Plus there's usually a free meal and even a couple of drinks thrown in for good measure."
    "And I get to hang out with [mike.name] for the whole day too, which is never a bad thing."
    "Because he's always so simple to tease and embarrass, it's almost too easy."
    show bg church wedding at traveling(1.2, 1, (640, 720))
    show mike date normal at center, zoomAt(1.1, (640, 750)) with easeinleft
    "So as we file into the chapel with all the other guests, I make a point of picking at his suit and tie."
    show mike normal at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "Ooh, [mike.name] - you look so cute in your suit!"
        bree.say "Ha...I made a rhyme!"
    elif hero.morality <= -25:
        bree.say "Wow, [mike.name] - you look so hot today..."
        bree.say "Once I've had a drink, I don't know if I'll be able to control myself!"
    else:
        bree.say "You should dress up like that more often, [mike.name]..."
        bree.say "You look great, you know - like a cheap bouncer!"
    show mike annoyed at traveling(1.05, 0.2, (640, 730))
    "[mike.name] makes a point of slapping my hands away as I fiddle with the lapels of his jacket."
    "And once he's managed to make me stop, he smooths down his tie too."
    show mike talkative at startle(0.1, 5)
    mike.say "Ssshhh!"
    mike.say "[hero.name], will you please behave yourself?"
    mike.say "Maybe do something useful instead?"
    show mike normal
    "Resigning myself to doing as I'm told, I ask the inevitable question."
    show mike at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    bree.say "Like what, exactly?"
    show mike talkative at startle(0.1, 5)
    mike.say "Like helping me figure out which side of the chapel is for Sam's guests."
    mike.say "I can't tell because I never met any of her family before today."
    mike.say "And all the friends I recognise, her, me and Ryan all had in common."
    show mike normal
    "I can't help frowning as I do my best to help [mike.name] out with the task he's set himself."
    "But at the same time, I'm not sure exactly why we have to be on Sam's side of the chapel."
    show mike at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    bree.say "What's up with that anyway?"
    show mike sad
    bree.say "Aren't all three of you friends?"
    bree.say "So what does it matter who's side we sit on?"
    show mike annoyed with dissolve
    "As soon as the words are out of my mouth, [mike.name] shoots me a look back over his shoulder."
    "And it's one that makes me almost leap backwards it's so fierce."
    show mike shout at vshake
    mike.say "I am NOT sitting on that asshole's side!"
    show mike annoyed at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    bree.say "Whoa..."
    bree.say "Take a chill-pill, [mike.name]!"
    show mike sad with dissolve
    "Suddenly [mike.name] seems to remember exactly where he is."
    "And I watch as he forces himself to calm down and regain control of himself."
    show mike blush at startle(0.1, 5)
    mike.say "Sorry, [hero.name], sorry..."
    mike.say "It's just that..."
    mike.say "Well...you've met Ryan, haven't you?"
    mike.say "So you know how he can be, right?"
    show mike sadsmile at startle(0.2, 5)
    show bg church wedding at startle(0.2, 5)
    "I can't help nodding as we get back to the task of finding Sam's side of the chapel."
    show mike sadsmile at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "I'm guessing you mean his...friendliness?"
        bree.say "Yeah, it can be a bit much at times."
    elif hero.morality <= -25:
        bree.say "Oh yeah, I've noticed alright..."
        bree.say "He's always eyeing up other women in front of Sam!"
    else:
        bree.say "Yeah, you don't have to remind me, [mike.name]..."
        bree.say "He's got quite the wandering eye!"
    show mike talkative at startle(0.1, 5)
    mike.say "Then you probably know why I don't want to sit on his side of the chapel then!"
    mike.say "Look, if I manage to get drunk enough later, I'll tell you all about it, okay?"
    mike.say "Until then, all of the gory details are staying inside of my head."
    mike.say "Where they've been making me miserable for bloody ages already!"
    show mike down
    "I'm about to say something more when I spot so a potential lead."
    bree.say "You know what, [mike.name]..."
    bree.say "That woman over there kind of looks like Sam, don't you think?"
    bree.say "But, like, if she was older and ate too much junk-food."
    show mike annoyed with dissolve
    "[mike.name] gives me a sideways look, like he's calling bullshit on what I just said."
    show mike surprised
    "But then I see a look of amazement spread over his face."
    show mike happy at startle(0.1, 5)
    mike.say "Fucking hell, [hero.name] - you're right!"
    mike.say "Come on, that's got to be Sam's side."
    show mike smile at traveling (1.05, 1, (320, 750))
    "I follow close on [mike.name]'s heels as he nips over to claim us seats close to the front."
    "And as we sit down, it becomes clear he's determined we're going to get a great view."
    show mike at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    bree.say "Erm, [mike.name]..."
    bree.say "Just for the sake of asking the question..."
    bree.say "You are just going to watch the ceremony, aren't we?"
    show mike talkative at startle(0.1, 5)
    mike.say "What are you trying to suggest?"
    show mike sadsmile at startle(0.1, 5)
    show bg church wedding at startle(0.1, 5)
    bree.say "Oh, nothing..."
    bree.say "Just checking I won't have to jump on you."
    bree.say "You know, at a certain time in the ceremony, when the priest asks a certain question?"
    show mike surprised with dissolve
    "[mike.name] gives me a pleading look."
    show mike talkative at startle(0.1, 5)
    mike.say "I..."
    mike.say "I'll do my best, okay?"
    mike.say "But I can't make any promises."
    show mike normal
    "He turns his gaze to where Ryan's already standing a the altar, casually chatting with the priest."
    show mike talkative at startle(0.1, 5)
    mike.say "Trust me, [hero.name]..."
    mike.say "You don't know that guy like I do."
    mike.say "And if you did..."
    play music "music/darren_curtis/camelot_monastery.ogg"
    "[mike.name]'s words are suddenly cut off by the swelling of music as it fills the chapel."
    show bg church wedding at traveling(1.1, 1, (640, 720))
    show mike annoyed at blur, traveling(1.2, 0.4, (50, 850))
    show ryan tux zorder 5000 at center, zoomAt (1, (450, 720)) with dissolve
    show master at center, blacker, zoomAt(1, (640, 720)) with dissolve
    show samantha wedding zorder 5000 at center, zoomAt (1.1, (1050, 780)) with easeinright
    "And, as one, the entire crowd of people packed into the pews turn to look over their shoulders."
    "So okay, I know that I already met Sam and noted that she's a pretty beautiful girl."
    "But damn, does she scrub-up well."
    "Because she walks into the chapel and down that aisle looking like a total princess!"
    show samantha at traveling (1, 1, (800, 750))
    "As she walks down the aisle, I happen to glance over at [mike.name]."
    "And that answers a lot of questions, as I see the way he's looking at her."
    "Oh boy - that guy's definitely holding a torch for his former housemate!"
    "Now that I get what's really eating away at [mike.name], the rest of the ceremony seems to fly by."
    "Before I know it, Sam and Ryan are exchanging their vows."
    show master at blacker, startle(0.1, 5)
    "Priest" "Do you, Samantha..."
    "Priest" "Take, Ryan to be your lawful, wedded husband?"
    show samantha happy at startle(0.1, 5)
    samantha.say "I do."
    show master at blacker, startle(0.1, 5)
    "Priest" "And do you, Ryan..."
    "Priest" "Take Samantha, to be your lawful, wedded wife?"
    show ryan smile at startle(0.1, 5)
    ryan.say "I do."
    show master at blacker, startle(0.1, 5)
    "Priest" "Then I call upon all those here present..."
    "Priest" "That if they know of any reason these two may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    menu:
        "Watch [mike.name] closely":
            show samantha at blur
            show ryan at blur
            show master at blacker, blur
            show bg church wedding at blur
            hide mike
            show mike date down at center, zoomAt(1.2, (50, 850))
            "I watch [mike.name] intently, waiting to see if he's actually going to speak up."
            "But though there's a battle written all over his face, he stays silent."
        "Take hold of [mike.name]'s hand":
            show samantha at blur
            show ryan at blur
            show master at blacker, blur
            show bg church wedding at blur
            hide mike
            show mike date down at center, zoomAt(1.2, (50, 850))
            "Thinking that [mike.name] might need some support, I reach over and take hold of his hand."
            "At first he looks up in surprise, but then I see his expression soften."
            "And he gives me a nod, then a smile that let me know he appreciates the gesture."
            $ mike.love += 1
        "Put my hand over [mike.name]'s mouth":
            show samantha at blur
            show ryan at blur
            show master at blacker, blur
            show bg church wedding at blur
            hide mike
            show mike date surprised at center, zoomAt(1.2, (50, 850)), startle(0.1, 5)
            "Worried that [mike.name]'s going to speak up and ruin the moment, I put a hand over his mouth."
            "He instantly turns his head to look at me in genuine surprise, but he also keeps quiet."
            "Now all I have to worry about is trying to explain what I just did to him!"
            $ mike.love -= 1
    show bg church wedding at zoomAt(1.1, (640, 720))
    show mike down
    hide ryan
    hide samantha
    show ryan tux smile at center, zoomAt(1, (450, 720))
    show samantha happy wedding at center, zoomAt(1, (800, 750))
    "Priest" "Then I now declare you husband and wife."
    hide master with dissolve
    show ryan at traveling(1, 0.5, (550, 730))
    show samantha at traveling(1, 0.5, (700, 740))
    "Sam and Ryan don't even wait for the priest to give them permission to kiss."
    "They're already doing it as everyone gets to their feet and starts clapping."
    "As soon as they're done, Sam turns her back and tosses her bouquet into the crowd."
    "And wouldn't you know it, the thing's flying straight towards me!"
    menu:
        "Catch the bouquet":
            show bg church wedding at vshake
            show ryan whining
            show samantha surprised
            show mike surprised
            "Without thinking, I reach up and catch the bouquet."
            "And as soon as I do, all attention is on [mike.name] and me."
            show mike talkative at startle(0.1, 5)
            mike.say "[hero.name]..."
            mike.say "What did you do that for?"
            show mike down
            bree.say "I..."
            bree.say "I'm sorry, I just kind of reacted!"
            show ryan smile at startle(0.1, 5)
            ryan.say "Good catch, [hero.name]!"
            show samantha happy at startle(0.1, 5)
            samantha.say "Oh, [mike.name] - could there be more wedding bells in the air?"
            show samantha normal
            "Sam and Ryan's comments only seem to make [mike.name] more embarrassed."
            "Making me cringe at having caught the bouquet in the first place."
            $ samantha.flags.friendship += 1
            $ samantha.flags.suspicion -= 1
        "Give [mike.name] a nudge so he catches the bouquet":
            "I reckon I could catch the bouquet myself."
            show mike surprised at hshake
            "But instead I give [mike.name] the slightest push."
            "And that means the bouquet lands right in his hands."
            show mike blush at startle(0.1, 5)
            mike.say "Wah..."
            mike.say "What the..."
            "Suddenly all eyes are on [mike.name]."
            show ryan smile at startle(0.1, 5)
            ryan.say "Good catch, [mike.name]!"
            show samantha talkative at startle(0.1, 5)
            samantha.say "Oh, [mike.name] - could there be more wedding bells in the air?"
            "I watch as he visibly cringes, hating all the attention that he's getting."
            show samantha normal
            $ mike.love -= 1
        "Deliberately avoid catching the bouquet":
            "I reckon I could catch the bouquet myself."
            "But instead I step back just enough to avoid it."
            "And one of the other female guests eagerly plucks it out of the air."
            "To be honest, I'm glad to have avoided the attention."
            "And [mike.name] looks like he feels the same way too."
            $ mike.love += 1
            $ samantha.flags.friendship -= 1
    scene bg restaurant at center, zoomAt(1.2, (640, 720)) with timelaps
    play music "music/roa_music/juice.ogg"
    show mike date normal at center, zoomAt(1.1, (640, 750))
    show ryan tux normal at center, zoomAt(1, (1000, 720))
    show samantha wedding normal at center, zoomAt(1, (1200, 720))
    with easeinright
    "Once the ceremony is over, everyone relocates to the venue hosting the reception."
    "And, much to [mike.name]'s apparent chagrin, we find ourselves seated pretty close to the head table."
    "This means that we get a great view of Sam and Ryan as they bask in the glory of their big day."
    show ryan annoyed with dissolve
    "But I can't help noticing that every time I look in their direction, Ryan's looking right back at me."
    "At first I think it's just my mind playing tricks on me, and yet it just seems to keep on happening."
    show ryan smile at startle(0.1, 5)
    "Of course they start with the usual speeches being made, everyone praising Sam and making gentle jokes about Ryan."
    show ryan annoyed with dissolve
    "But once all of the people who'd normally speak are done, Ryan turns his gaze in our direction again."
    show ryan smile at startle(0.1, 5)
    show samantha happy
    ryan.say "And last, and some people may say, least..."
    ryan.say "Sam and I would like to call on our old friend [mike.name], to say a few words."
    show mike surprised with dissolve
    ryan.say "So, [mike.name] - I yield the floor to you!"
    "Eyes wide with amazement, I turn to look at [mike.name]."
    "And I see that, if anything, his eyes are even wider than mine."
    show mike surprised at startle(0.1, 5)
    mike.say "What the fuck?"
    mike.say "What the actual fuck?!?"
    mike.say "[hero.name], you have to help me - I can't give a speech!"
    show mike blush
    "I look from [mike.name] to the head table and back again, realising that I'm going to have to save his ass."
    show mike surprised
    show samantha surprised
    show ryan whining
    "And so I take a deep breath, then push back my seat and stand up, clearing my throat as I do so."
    bree.say "Ahem..."
    bree.say "My name's [hero.name], and..."
    bree.say "Well, I'm [mike.name]'s friend - and Sam and Ryan's too!"
    bree.say "And I might have only met them pretty recently..."
    bree.say "But darn it, they're such great folks I can gush about them as much any old friend can!"
    menu:
        "Stick to praising the happy couple":
            "Best to keep this brief and stick to what people are expecting."
            if hero.morality >= 25:
                bree.say "So let's all raise a glass to the happy couple."
                bree.say "And wish a happy future to Sam and Ryan."
            elif hero.morality <= -25:
                bree.say "So wish them all the luck for the wedding night..."
                bree.say "Because they've got a lot to live up to!"
            else:
                bree.say "So raise a glass, before you're too drunk to manage it..."
                bree.say "And give a cheer to the bride and groom."
            show ryan smile
            show samantha happy
            show mike annoyed
            $ ryan.love += 1
            $ mike.love -= 1
            $ samantha.flags.friendship += 1
            $ samantha.flags.suspicion -= 1
        "Take a jab at Ryan's ego":
            "I know that I should keep this brief and as clean as possible."
            "But I just can't pass up the chance to take a shot at Ryan and his massive ego."
            if hero.morality >= 25:
                bree.say "[mike.name], myself and all of the bride and grooms friends love them..."
                bree.say "But not half as much as Ryan loves himself!"
            elif hero.morality <= -25:
                bree.say "Sam, if Ryan's manhood's half as big as his ego..."
                bree.say "Then you're in for quite a ride tonight!"
            else:
                bree.say "Sam, if everyone here loves you half as much as Ryan loves himself..."
                bree.say "Then you'll never want for love as long as you both live!"
            show ryan upset
            show samantha happy
            show mike smile
            $ ryan.love -= 1
            $ mike.love += 1
            $ samantha.flags.friendship -= 1
            $ samantha.flags.suspicion += 1
        "Keep it as short as possible":
            "Urgh...this is the last thing I wanted to be doing today!"
            "So the best thing would be to keep it short and sweet."
            if hero.morality >= 25:
                bree.say "So let's just raise a glass to how great they are!"
            elif hero.morality <= -25:
                bree.say "So let's just raise a glass to how totally fucking hot they are!"
            else:
                bree.say "So let's just all admit how fantastic they are!"
            show ryan normal
            show samantha normal
            show mike normal
    "Thankfully everyone seems to like what I said, or else they're too drunk to actually understand it."
    "There's a round of claps and cheers as I sink back down into my seat, shooting a serious glance at [mike.name]."
    show mike talkative at traveling(1.2, 0.5, (640, 800))
    mike.say "Thanks, [hero.name]..."
    mike.say "You totally saved my ass back there!"
    show mike normal
    bree.say "No sweat, [mike.name] - but you owe me one!"
    "Once the speeches are over, apparently it's time for the first dance."
    show samantha normal at traveling(1.2, 1, (940, 820))
    show ryan at traveling(1.3, 1, (320, 880))
    "But as Ryan and Sam walk past where [mike.name] and I are sitting, she drags us both out of our seats."
    show bg restaurant at vshake
    show ryan normal
    bree.say "What the..."
    show mike blush at startle(0.1, 5)
    mike.say "Sam, what the hell?"
    show ryan whining at startle(0.1, 5)
    ryan.say "Babe, what are you doing?"
    show samantha happy at startle(0.1, 5)
    samantha.say "I want a photograph of the four of us."
    samantha.say "Old friends and new, all together as we start a new part of our lives!"
    show samantha normal
    "Before anyone can say another word, the wedding photographer appears out of nowhere."
    "Seriously, the guy pops up like he's been summoned by Sam's very words."
    "And then he proceeds to snap away as we're forced to pose awkwardly."
    show ryan at traveling (1, 1, (-200, 750)) with easeinleft
    show samantha at traveling (1, 1, (-200, 750)) with easeinleft
    show mike down
    "As soon as it's over, Sam and Ryan head off to the dance-floor."
    "Which leaves [mike.name] and me standing there, kind of flummoxed in their wake."
    show mike talkative at startle(0.1, 5)
    mike.say "Okay..."
    mike.say "I SO do not want a copy of that photograph!"
    show mike normal
    bree.say "Yeah, I'm with you on that one."
    bree.say "Hey, there's a free bar tonight, isn't there?"
    show mike talkative at startle(0.1, 5)
    mike.say "I think so."
    show mike normal
    bree.say "Then let's go drink until we forget all about that damn photo."
    show mike happy at startle(0.1, 5)
    mike.say "You got it, [hero.name]."
    mike.say "And the best thing is, Ryan's paying for it all!"
    show mike smile
    scene bg black with fade
    $ ryan.flags.delay = TemporaryFlag(True, 3)
    return

label ryan_female_event_04:
    if ryan.love.max < 80:
        $ ryan.love.max = 80
    scene bg bedroom2 with fade
    show bree sleep normal at center, zoomAt(1.1, (400, 800)) with dissolve
    $ phone_show_hero = False
    $ nvl_mode = "phone"
    nvl clear
    "It's getting pretty late by now, and I keep glancing at my phone to check the time."
    "And every time I see the lateness of the hour, I keep telling myself that I should go to bed."
    "But you know how it is, right?"
    "You always find some excuse to put it off for a little longer."
    "Whether it's doom-scrolling on social media or checking your messages one last time."
    "It's only when I'm yawning and rubbing my eyes like crazy that I finally decide I'm done."
    show bree surprised at startle(0.1, 5)
    play sound msg_receive
    "And wouldn't you know it, that's the exact moment my phone chooses to buzz with a notification."
    show bree normal with dissolve
    "Even better, when I check the screen, it's not an annoying notification from a pointless app."
    "Instead it's an actual DM from a genuine human being!"
    "And that's the perfect excuse to stay up for another couple of minutes."
    "Pulling up the message, I'm only a little more than half awake as I check who it's from."
    "But as soon as I read Ryan's name on the thing, I shake of the sleepiness and stare at the screen."
    ryan_nvl "Hey, [hero.name] - what are you up to?"
    "Still thrown by getting a message from Ryan at such a late hour, I read the name again."
    "And no, I wasn't mistaken - Ryan is messaging me in the middle of the night."
    "And yeah, this is the same Ryan who's wedding I just attended the other day."
    "In fact he and Sam can't have been back from their honeymoon too long either."
    show bree normal
    "For a moment I think about ignoring the message altogether, just pretending I never saw it."
    "Then I consider leaving it until the morning and saying I didn't see it until then."
    "But the problem is that part of me is really curious as to what he might be after."
    "So I take a deep breath, and then I type my response."
    show bree sadsmile at startle(0.3, 5)
    if hero.morality >= 25:
        mchero_nvl "Can't talk now, Ryan."
        mchero_nvl "About to go to sleep."
        mchero_nvl "Unless it's an emergency?"
    elif hero.morality <= -25:
        mchero_nvl "You caught me at a bad time, Ryan."
        mchero_nvl "I was about to get into my pyjamas!"
        mchero_nvl "Is there some kind of a problem?"
    else:
        mchero_nvl "Hey, Ryan - about to turn in for the night."
        mchero_nvl "Why are you messaging me this late?"
        mchero_nvl "Is there something up?"
    "That should do the trick, right?"
    "Friendly and yet at the same time noncommittal."
    "At least that's how I hope it sounded."
    "I'm still thinking about the tone of the message when I get a response."
    ryan_nvl "No, nothing's up - why would there be?"
    ryan_nvl "Didn't think I needed a reason to message a friend!"
    "Okay, that sounds more than a little like he's got his excuses all lined up!"
    "Plus he's already doing a spot of the old gaslighting there too."
    "I think I need to press him for a more expansive answer."
    show bree stuned at startle(0.3, 5)
    if hero.morality >= 25:
        mchero_nvl "I'm not sure you should be messaging me so late at night."
        mchero_nvl "It'd be more appropriate to do it in the daytime."
        mchero_nvl "You know, like, when I'm awake?"
    elif hero.morality <= -25:
        mchero_nvl "Look, Ryan, I have a lot of fun late at night."
        mchero_nvl "But it's usually in person, rather than via text message."
        mchero_nvl "So why not message me tomorrow instead?"
    else:
        mchero_nvl "It's a bit late to be just chatting, Ryan."
        mchero_nvl "Why don't you drop me a line tomorrow instead?"
        mchero_nvl "I'll be more awake then too."
    "There's a longer pause between my sending the message and Ryan responding this time."
    "Because of course this time he's got to think up an excuse not to message me when Sam's around."
    "But when his response does finally come, it kind of catches me off-guard."
    show bree sadsmile
    ryan_nvl "I'm sorry, [hero.name] - I really missed talking to you."
    ryan_nvl "There was no time to chat to anyone at the wedding."
    ryan_nvl "And I felt like we totally connected the last time we spoke."
    ryan_nvl "I just...well...I guess I just get a little lonely at night."
    ryan_nvl "And Sam's great, totally the best..."
    ryan_nvl "But I wanted to talk to a friend, to someone that gets me, you know?"
    "Oh man - now I'm starting to understand why this guy makes [mike.name] so crazy."
    "On the one hand, I can see all of the moves that he's trying to put on me right now."
    "But on the other, that doesn't stop him being one pretty charismatic asshole!"
    "Okay, [hero.name]...focus!"
    "My response to all of that has to be as perfect as I can make it."
    menu:
        "Shut Ryan down":
            show bree annoyed with dissolve
            "And that's going to be me telling Ryan that this isn't acceptable."
            show bree at startle(0.3, 5)
            if hero.morality >= 25:
                mchero_nvl "This isn't being a friend, Ryan."
                mchero_nvl "This is you going behind Sam's back!"
            elif hero.morality <= -25:
                mchero_nvl "It'd be different if we were fucking, Ryan."
                mchero_nvl "But if we're just plain, vanilla friends, then I'm not into it."
            else:
                mchero_nvl "I'm cool with us being friends, Ryan."
                mchero_nvl "But guy friends don't message girl friends like this."
            "I guess that must have been like dropping a hand-grenade into the conversation."
            "Because Ryan's tone totally changes when he sends me his response."
            show bree stuned
            ryan_nvl "Whoa, [hero.name] - what are you even talking about?"
            ryan_nvl "We're totally friends, and nothing more than that!"
            ryan_nvl "Look, I'm sorry if I accidentally overstepped in invisible boundary, okay?"
            ryan_nvl "I'm still feeling things out when it comes to our friendship."
            "I spend a few minutes staring at my phone, frowning and rereading Ryan's messages."
            "Then I come to the conclusion that I managed to scare him into backing off."
            show bree annoyed at startle(0.3, 5)
            if hero.morality >= 25:
                mchero_nvl "Okay, Ryan, you're off the hook this time."
                mchero_nvl "But message me this late again, and I'll block you."
            elif hero.morality <= -25:
                mchero_nvl "Yeah, you'd better back off, mister."
                mchero_nvl "Otherwise I'll be talking to Sam and spilling the beans on you!"
            else:
                mchero_nvl "Whatever you say, Ryan."
                mchero_nvl "But message me again this and I'll send Sam a screenshot of it all!"
            "With that, I make a point of turning off my phone for the night."
            "Hoping as I do so that I won't turn it on again to more messages from Ryan."
            $ ryan.love -= 3
            $ samantha.flags.friendship += 1
            $ samantha.flags.suspicion -= 1
        "Be friendly but firm":
            "Which is to somehow strike a balance between helping Ryan and not leading him on."
            show bree sadsmile at startle(0.3, 5)
            if hero.morality >= 25:
                mchero_nvl "I feel like we have a connection too, Ryan."
                mchero_nvl "But I also think we should be talking in the daytime."
                mchero_nvl "When we're both more calm and rational, you know?"
            elif hero.morality <= -25:
                mchero_nvl "Oh, Ryan - you know that I think you're a great guy."
                mchero_nvl "And if you were single, I'd be all over you for sure."
                mchero_nvl "But if you message me at night, people are going to get suspicious!"
            else:
                mchero_nvl "Come on, Ryan, you know that I really like you too."
                mchero_nvl "But you're a married man and I'm a woman that's not your wife."
                mchero_nvl "If we don't talk in the daytime, other people are going to start talking about us!"
            "I wait a couple of minutes while my message sends and he has time to read it."
            "And I have to admit to being more than a little nervous as I do so."
            "Worried that Ryan might not be on the same page as me."
            "Or worse, that Sam might happen to look over his shoulder at the wrong moment."
            "So when his response arrives, I read it without hesitation."
            show bree normal with dissolve
            ryan_nvl "I guess you do have a point, [hero.name]."
            ryan_nvl "Sorry, I was too eager to talk to you again."
            ryan_nvl "I suppose I'll have to keep my enthusiasm for you in check from now on."
            ryan_nvl "We'll chat again at a more appropriate time."
            "After I finish reading the message, I make a point of turning off my phone for the night."
            "Because the bastard's gone and done it again, hasn't he?"
            "He's signed off by totally agreeing with everything I said."
            "But at the same time he's made it look like he's totally wounded by it too!"
            $ ryan.love += 1
        "Flirt with him":
            show bree flirt with dissolve
            "Which is to be a good friend to Ryan in what's obviously his time of need."
            "Because why else would a newly-married man be reaching out to me like this?"
            "It's obvious that needs help from someone that'll listen without judging him."
            "And sure, maybe even give his ego a little boost along the way too."
            show bree flirt at startle(0.3, 5)
            if hero.morality >= 25:
                mchero_nvl "This is SO risky of you, Ryan."
                mchero_nvl "But I have to be totally honest."
                mchero_nvl "I've really been wanting to talk to you too!"
            elif hero.morality <= -25:
                mchero_nvl "This is SO naughty, Ryan..."
                mchero_nvl "But it's totally exciting and a turn-on too!"
                mchero_nvl "I've got to admit, I've been wanting to talk to you too."
            else:
                mchero_nvl "Oh, Ryan - you're going to get me into so much trouble!"
                mchero_nvl "But I've got to be honest with myself, or I'll go nuts."
                mchero_nvl "I've been missing talking to you too."
            "Almost as soon as I've sent the message, I feel a sense of relief."
            "Like a great weight's been lifted off of my shoulders."
            "And it doesn't take long for Ryan's response to come back either."
            ryan_nvl "That's so great to hear, [hero.name]."
            ryan_nvl "Just knowing that we're on the same page and that you care..."
            ryan_nvl "You'll never know how much that means to me."
            ryan_nvl "I have to go now, but I'll message you again soon."
            "After I finish reading the last message, I make a point of leaving my phone on."
            "You know, just in case Ryan needs to contact me again in the night?"
            "Not that I'm desperate for him to message me back so soon, you know?"
            "It's just me wanting to be a good friend, that's all."
            $ ryan.love += 3
            $ samantha.flags.friendship -= 1
            $ samantha.flags.suspicion += 1
    scene bg black with fade
    $ phone_show_hero = True
    $ ryan.flags.delay = TemporaryFlag(True, 2)
    return

label ryan_female_event_05:
    if ryan.love.max < 100:
        $ ryan.love.max = 100
    scene expression f"bg {game.room}" at center, zoomAt(1, (640, 720))
    show samantha upset at center, zoomAt(0.7, (300, 720))
    show ryan annoyed at center, zoomAt(0.7, (500, 720))
    with fade
    "I'm just minding my own business, not really paying attention to what's going on around me."
    "Which is why the sudden sound of shouting and yelling makes me almost leap out of my skin."
    show ryan angry at startle(0.1, 5)
    ryan.say "I cannot believe you're being like this!"
    ryan.say "Even after all this time, after all we've been through..."
    ryan.say "You still don't trust me?!?"
    show ryan upset
    show samantha annoyed at startle(0.1, 5)
    samantha.say "Oh come off it, Ryan..."
    samantha.say "You're not fooling me this time."
    samantha.say "I know all of your little tricks too well for that!"
    show samantha upset
    "I recognise the rowing voices even before I set eyes on Ryan and Sam."
    "And the moment that I see them, locked in a raging argument."
    "I instinctively flatten myself against the nearest wall and keep quiet."
    "Seriously, as crazy as it sounds, I feel like an animal trying to camouflage itself."
    "Like, if I stay still and silent enough, they might just fail to notice my presence."
    show ryan angry at startle(0.1, 5)
    ryan.say "What are you saying, Sam?"
    ryan.say "Do I have to prove it to you?"
    ryan.say "Here - go through my phone if you like!"
    show ryan upset
    show samantha annoyed at startle(0.1, 5)
    samantha.say "Oh yeah, like you wouldn't have deleted all the incriminating stuff!"
    samantha.say "Urgh...you are SO infuriating sometimes."
    samantha.say "It makes me thing [mike.name] was right about you."
    show samantha upset
    "I can't help raising my eyebrows at the mere mention of [mike.name]'s name."
    "Because I already heard about his suppressed feelings for Sam from the guy's own lips."
    "And to me, that seems like Sam's throwing kerosene onto an already raging fire."
    show ryan angry at startle(0.1, 5)
    ryan.say "What did you say?"
    ryan.say "What's that loser been telling you?!?"
    show ryan upset
    show samantha annoyed at startle(0.1, 5)
    samantha.say "Shouldn't that tell you something, Ryan?"
    samantha.say "Never mind what [mike.name] might have said to me."
    samantha.say "Doesn't it bother you that our oldest friend talks to me and not you?"
    show samantha upset
    show ryan angry at startle(0.1, 5)
    ryan.say "We'll soon see about that, Sam..."
    ryan.say "We'll see what he has to say when I confront him about it!"
    show ryan upset
    "The look on Sam's face suddenly changes, and she rounds on Ryan."
    "And where before I was just raising my eyebrows, this time I actually flinch."
    "Because the expression Sam's wearing makes her look like she could lash out at Ryan any second!"
    show samantha annoyed at startle(0.1, 5)
    samantha.say "You will do no such thing!"
    samantha.say "All [mike.name]'s ever done is try to be a good friend to us both."
    samantha.say "And if you hurt him, I'll..."
    samantha.say "Well, let's just say I don't know what I'll do!"
    show samantha upset
    "Sam and Ryan keep on staring daggers at each other for a few more tense moments."
    "And then it's Sam that breaks the stand-off, turning and storming off."
    show ryan at center, traveling(1.2, 1.5, (840, 920))
    pause 1.5
    "That's when Ryan turns in the opposite direction, and sees me standing there."
    show ryan blank at center, zoomAt(1.2, (840, 920))
    "It only takes the blink of an eye for him to do that thing where he seems to reset himself."
    "And he goes from looking flustered and upset to smooth and nonchalant right before my eyes."
    show ryan smile with dissolve
    ryan.say "Oh..."
    ryan.say "Hey, [hero.name]..."
    ryan.say "I don't suppose you just got here, like, two seconds ago?"
    show ryan normal at startle(0.1, 5)
    show bg street at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "Ah, no..."
    if hero.morality <= -25:
        bree.say "Unfortunately not..."
    else:
        bree.say "Hell no..."
    show ryan smile with dissolve
    ryan.say "Ah..."
    ryan.say "Then you..."
    bree.say "Yeah, I saw the whole thing."
    show ryan upset at hshake
    "Ryan seems to realise that there's no putting a spin on what just happened."
    "And much to my surprise, he drops the act and lets his feelings out in front of me."
    "Groaning as he runs his hands through his hair and then over his face."
    show ryan angry at startle(0.1, 5)
    ryan.say "Urgh..."
    ryan.say "Normally things like that happen behind closed doors."
    ryan.say "But you heard the whole thing, right?"
    show ryan upset at startle(0.1, 5)
    show bg street at startle(0.1, 5)
    bree.say "Well, I heard most of it, I guess..."
    "Ryan doesn't seem to notice the noncommittal nature of my answer."
    "Or if he does, then he chooses to ignore it and keep right on badgering me."
    show ryan smile at startle(0.1, 5)
    ryan.say "Then you've got to see my side of things, right?"
    ryan.say "Don't you think that Sam's being unreasonable?"
    show ryan evil
    menu:
        "'You have to fix things with Sam yourself'":
            "The last thing I want to do is get pulled into a fight between Ryan and Sam."
            "So I decide to give him the best advice that I can come up with on the spot."
            "Which is to go and sort the mess out with her, rather than asking me for validation."
            show ryan upset at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "I'm not the one you should be talking to, Ryan..."
                bree.say "The only person who can resolve this for you is Sam."
            if hero.morality <= -25:
                bree.say "This isn't my mess, Ryan..."
                bree.say "You and Sam are the ones fucking - so go talk to her!"
            else:
                bree.say "Look, Ryan, I'm not the person you need to talk to."
                bree.say "This is between you and Sam - so go see her."
            show ryan sad
            "Ryan looks like he's going to argue with me for a moment."
            "But then his mask slips again, and his shoulders sag."
            show ryan smile
            ryan.say "Ah..."
            ryan.say "I suppose you're right, [hero.name]."
            ryan.say "Talking to you isn't going to solve the problem."
            ryan.say "So I guess I'll go and face the music."
            show ryan sad at center, traveling(0.7, 1, (500, 720))
            "With that, Ryan turns on his heel and trudges off after Sam."
            "Leaving me to watch him go, hoping that I just made the right decision."
            $ samantha.flags.friendship += 1
        "'You're not a bad guy'":
            "My instinct is to tell Ryan that what he really needs to do is go talk to Sam."
            "And I know that involving myself in a couple's arguments is a dumb thing to do."
            "But now he's getting that puppy-dog look in his eyes, the one that I just can't resist."
            "And it means that I have the overwhelming urge to say something to comfort him."
            show ryan upset at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "It's okay, Ryan - you're not the bad guy."
                bree.say "After all, nobody's perfect!"
            if hero.morality <= -25:
                bree.say "Ah, you should just let her cool off for a while."
                bree.say "I mean, it's not like you fucked another girl in front of her, is it?"
            else:
                bree.say "You shouldn't be too hard on yourself, Ryan..."
                bree.say "I'm sure there are faults on both sides."
            "Ryan listens intently to what I have to say, nodding along with me."
            "And when I'm done talking, he seems to have been cheered up by my words."
            show ryan evil at startle(0.1, 5)
            ryan.say "You're right, [hero.name]..."
            ryan.say "I shouldn't be putting myself down."
            ryan.say "Sam's the one that needs to take a long, hard look at herself!"
            show ryan upset at startle(0.1, 5)
            show bg street at startle(0.1, 5)
            bree.say "Erm..."
            bree.say "I'm not sure that's what I was getting at!"
            show ryan at center, traveling(0.7, 1, (500, 720))
            "But it's too late for me to add anything more."
            "As Ryan's already turned on his heel and strode off after Sam."
            "Which leaves me standing there alone, and wondering if I just made things even worse!"
            $ samantha.flags.suspicion += 1
        "Refuse to answer Ryan's question":
            "Okay, I might not know a whole lot about the really big questions in life."
            "But one thing I do know is that it's a really bad idea to get involved when couples are fighting."
            "No matter what you do or say, they're inevitably going to turn on you at some point."
            "So there's only one thing that I can do that'll help Ryan, Sam and me in this situation."
            "And that's keeping my big mouth shut!"
            "So that's why I respond to Ryan's questions with nothing more than a shrug of the shoulders."
            "And then I make a point of turning my back on him before he can press me further."
            "Walking away as I deliberately ignore whatever he's saying to me."
            "All the time hoping that they can sort this mess out between themselves."
    scene bg black with fade
    $ ryan.flags.delay = TemporaryFlag(True, 2)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
