init python:
    Event(**{
    "name": "kylie_female_event_01",
    "label": "kylie_female_event_01",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsHour(11, 16),
        MinDaysPlayed(11),
        HeroTarget(
            IsGender("female"),
            IsRoom("classroom")),
        PersonTarget(mike,
            Not(IsHidden()),
            MinStat("love", 75),
            ),
        ],
    "once_day": True,
    "do_once": True,
    })

    Event(**{
    "name": "kylie_female_event_02",
    "label": "kylie_female_event_02",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsHour(11, 16),
        HeroTarget(
            IsGender("female"),
            IsRoom("classroom")),
        PersonTarget(mike,
            Not(IsHidden()),
            ),
        PersonTarget(kylie,
            Not(IsHidden()),
            MinStat("love", 20),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kylie_female_event_03",
    "label": "kylie_female_event_03",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsHour(18, 23),
        HeroTarget(
            IsGender("female"),
            IsRoom("house")),
        PersonTarget(mike,
            Or(
                Not(IsActivity("tv")),
                IsHidden(),
                IsGone(),
                ),
        PersonTarget(sasha,
            Or(
                Not(IsActivity("tv")),
                IsHidden(),
                IsGone(),
                ),
        PersonTarget(kylie,
            Not(IsHidden()),
            MinStat("love", 40),
            ))),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kylie_female_event_04",
    "label": "kylie_female_event_04",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        "game.from_room not in ['house', 'firstfloorbathroom', 'kitchen', 'livingroom', 'secondfloor', 'bathroom', 'bedroom1', 'bedroom2', 'bedroom3', 'attic']",
        IsHour(20, 21),
        HeroTarget(
            IsGender("female"),
            IsRoom("house")),
        PersonTarget(mike,
            IsRoom("kitchen"),
            ),
        PersonTarget(kylie,
            IsFlag("delay", False),
            MinStat("love", 60),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kylie_female_event_05",
    "label": "kylie_female_event_05",
    "duration": 1,
    "music": "music/roa_music/dreamy.ogg",
    "conditions": [
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom")),
        PersonTarget(mike,
            Not(HasRoomTag("home")),
            ),
        PersonTarget(kylie,
            IsFlag("delay", False),
            MinStat("love", 80),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kylie_kiss_me_female",
    "label": "kylie_kiss_me_female",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsPresent(),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/dreamy.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })


label kylie_female_event_01:
    scene bg classroom at center, zoomAt(1.0, (640, 720)) with fade
    $ kylie.unhide()
    "I'm feeling like my brain's pretty frazzled, even after the first lecture of the day, so I head out into the quadrangle to get some fresh air and natural light before the next one."
    "It's not as though I have any particular plan in mind, just the desire to do something unstructured and free to distract me from the intellectual grind for a couple of minutes."
    "A few familiar faces pass me by as I wander aimlessly, but no one seems to want to strike up a conversation, and I'm happy to be alone in my own space right now."
    show mike b casual annoyed zorder 2 at center, zoomAt(1.0, (1050, 740)) with dissolve
    "I only spot [mike.name] by sheer chance, as he turns in my direction just as I happen to walk past, and I doubt he'd even have noticed if I hadn't waved and started towards him."
    show kylie casual shy zorder 1 at center, zoomAt(1.0, (720, 720)) with dissolve
    "Honestly though, it's not my housemate that's really caught my attention, but rather the girl that he's talking to right now."
    "Don't get me wrong, a pretty girl chatting to [mike.name] isn't all that rare of a thing."
    "He's no male model in terms of his looks, but he's cute and a pretty sweet guy to boot."
    "But the girl's more than enough to turn heads, and to keep them turned as well."
    "She's a platinum blonde with one of those bodies that's kept in bombastic shape by its owner being young enough to still get away without needing a gym membership."
    "And even worse, I can instantly see that she's one of those types that's charming to guys and probably a cold-hearted bitch to her fellow girls."
    "Don't ask me how I know, because a woman just knows - she can either spot them a mile off, or else she's one herself."
    "Of course, being a guy, [mike.name] won't realise any of this and will just think that she's sweetness and light."
    show kylie happy at center, zoomAt(1.0, (740, 720)) with ease
    "I can see it in the way she leans closer to him, wrapping her hair around her fingers and giggling like a little slut."
    show kylie shy
    "That's why it's pretty much my duty, as his friend, to check this girl out and see just what her intentions are towards him."
    menu:
        "Talk to them":
            "I decide to play the innocent female friend, not wanting the girl to suspect that I'm checking her out and put on an act of her own."
            show bg classroom at center, traveling(1.25, 1.0, (485, 880))
            show mike b normal at center, traveling(1.25, 1.0, (840, 880))
            show kylie sad at center, traveling(1.25, 1.0, (440, 900))
            bree.say "Hey, [mike.name]!"
            bree.say "Aren't you going to introduce me to your new friend?"
            show mike b smile
            "[mike.name]'s face tells me that he's pretty happy to see me."
            show kylie angry
            "But to look at the girl's expression, you'd think she'd just found me stuck to the bottom of her shoe."
            "Oh she doesn't show it, but I can tell by the way she narrows her eyes at me."
            show mike happy
            mike.say "Oh...hi, [hero.name]."
            mike.say "This is Kylie - I used to know her back in high-school."
            mike.say "I had no idea she went here too until she spotted me just now."
            show mike smile
            show kylie shy
            "Kylie responds to this by nodding and giving [mike.name] a sickly smile."
            show kylie shout
            kylie.say "Yeah, we go WAY back - so I'm really more like an old friend than anything else!"
            show kylie normal
            "Wow - that was a nice little jab in the ribs disguised as a casual comment if I ever heard one!"
            show mike happy
            mike.say "Kylie, this is [hero.name]...my housemate."
            show mike smile
            "Hmm - a pause and then he calls me his housemate, rather than his friend or anything more intimate."
            "I guess [mike.name]'s a little confused about his feelings when it comes to this girl."
            bree.say "I have to ask, Kylie - because you just look so young and fresh-faced."
            bree.say "How did you know [mike.name] in high-school?"
            bree.say "He must have been way older than you, right?"
            $ kylie.yandere += 5
            show kylie angry
            "Kylie looks annoyed by my question, as though she doesn't want to admit the answer."
            "But of course, [mike.name]'s a guy, and so he doesn't pick up on any of that."
            show mike talkative
            mike.say "Yeah, Kylie was younger than me - I knew her because I was dating her older sister at the time."
            mike.say "But, well...that didn't work out too well for me."
            show mike smile
            "Score one for me right there!"
            "She might have grown up to be pure man-bait, but this Kylie was once someone's snotty little sister."
            "No matter what she does in the here and now, that image of her will always be in the back of [mike.name]'s mind!"
            "Seeing that [mike.name]'s starting to recall more of his memories from back then, and perhaps more about his ex-girlfriend than her sister, I feel my job here is done."
            bree.say "Well, I've gotta run if I want to make it to my next lecture on time."
            bree.say "See you back home later, [mike.name]."
            bree.say "Great to meet you too, Kylie!"
            show mike happy
            mike.say "See you tonight, [hero.name]."
            show mike smile
            show kylie vangry
            kylie.say "Yeah, whatever..."
            show kylie angry
            pause 0.5
            scene bg classroom with fade
            "As I walk away, I can't help feeling a little smug at having put Kylie in her place in front of [mike.name]."
            "Hopefully she'll take the hint and be a bit more wary of me around him in future."
            "And if I'm really lucky, I may not see too much more of her at all."
        "Kiss [mike.name]" if mike.flags.kiss and hero.morality < 25:
            "Call me a slut or a manipulative bitch if you like - it's not like I'll feel any worse about myself for it."
            "But with a girl like this sniffing around, you have to be willing to mark out your territory and defend it from the start."
            show bg classroom at center, traveling(1.25, 1.0, (485, 880))
            show mike at center, traveling(1.25, 1.0, (840, 880))
            show kylie at center, traveling(1.25, 1.0, (440, 900))
            "That's why I make no effort to announce myself to either of them, standing there in silence until the girl notices me and glances in my direction."
            show kylie sad
            "After a moment of looking at her in that typically clueless way he has, [mike.name] turns around too."
            show mike surprised
            "By the time he's turned to face me, his mouth is already half open to ask a question."
            "Which is all the better for what I have in mind..."
            hide mike
            hide kylie
            show bree kiss casual
            with hpunch
            $ bree.flags.kiss += 1
            $ kylie.yandere += 10
            $ mike.love += 5
            "Wrapping my arms around his neck and pulling him down to my level, I pretty much clamp my lips over his."
            "I make sure that the other girl can see my tongue dart in there as well, and then I'm Frenching [mike.name] mercilessly."
            "He's too stunned to even think about resisting, and I think that I can just about guess what his little friend must be thinking right now."
            "In fact, the thought of a 'little friend' gives me all the inspiration I need to kick things up a notch."
            "I press myself against [mike.name] so that we're body to body, making sure that every part of me is in contact with him."
            "And then I take one hand from around his neck and use it to reach down towards his crotch."
            "As I take hold of his cock through his pants and give him a good, hard squeeze, I can feel that he's already standing to attention."
            "It feels pretty good to know that I can have that kind of effect on him from a cold start."
            "Even better when he's just been chatting away to that flirting little harpy too."
            "I can feel that [mike.name]'s getting into it now, his initial confusion no longer making him stiff and awkward in my arms."
            "But it's another small victory for me that, even though he's regained his composure, he's not making any effort to pull away from me."
            "I let him enjoy the feeling of being passionately kissed while I stroke his cock for just a little longer."
            "And then I slowly release him, keeping him wanting more."
            scene bg classroom at center, zoomAt(1.25, (485, 880))
            show mike casual surprised at center, zoomAt(1.25, (840, 880))
            show kylie casual angry at center, zoomAt(1.25, (440, 900))
            bree.say "Hey, [mike.name]...I missed you so much!"
            "[mike.name] looks about as confused and flustered as I'd expect him too."
            "The girl, on the other hand, is clearly looking daggers at me right now."
            "But not at him, which is interesting..."
            bree.say "Well, don't just stand there like a slapped fish."
            bree.say "Aren't you going to introduce me to your little friend here?"
            show mike blush
            mike.say "Erm...ah...Kylie, this...this is [hero.name]."
            mike.say "[hero.name]...this is Kylie."
            mike.say "She's someone I used to know...back in high-school."
            mike.say "And you're my..."
            show mike smile
            bree.say "That's right, [mike.name] - I'm yours and you're mine!"
            show mike casual surprised zorder 2 at center, zoomAt(1.75, (940, 1220)) with hpunch
            "I grab his arm and cling to it, as though I'd rather tear it off at the shoulder than be dragged an inch from his side."
            show mike smile
            "By now, Kylie has crossed her arms over her chest and has a distinctly sour look on her face."
            "But as I've not technically done anything that violates the rules of polite conduct, she has no choice but to pretend to be pleasant in return."
            show kylie sadhappy
            kylie.say "So you go here too, yeah?"
            show kylie angry
            bree.say "Oh yeah - I go anywhere that [mike.name] goes!"
            bree.say "We're inseparable -aren't we, honey?"
            show mike surprised
            mike.say "We are?"
            show mike smile
            bree.say "Ha ha...of course we are, silly!"
            bree.say "Well, I have to run if I want to get to my next lecture on time."
            bree.say "Nice to meet you, Kylie."
            show kylie sadhappy
            kylie.say "Likewise."
            show kylie angry
            bree.say "See you back home tonight, [mike.name]."
            bree.say "I'll be waiting for you..."
            scene bg classroom with fade
            "As I walk away, I can't help feeling a little smug at having put Kylie in her place in front of [mike.name]."
            "Hopefully she'll take the hint and be a bit more wary of me around him in future."
            "And if I'm really lucky, I may not see too much more of her at all."
    return

label kylie_female_event_02:
    if kylie.love.max < 40:
        $ kylie.love.max = 40
    scene bg university at center, zoomAt(1.1, (640, 720)) with fade
    show mike b casual normal zorder 2 at center, zoomAt(1.0, (640, 740)) with dissolve
    show kylie casual shy zorder 1 at left, blacker, zoomAt(0.85, (220, 720)) with dissolve
    "Normally I have a terrible memory for faces, you know what I mean?"
    "It's like, I can see someone a couple of times, even be introduced to them."
    "But the next time I see that person, there's no spark of recollection, nothing."
    "And they end up staring at me in amazement as I have to ask who the hell they are all over again."
    "Which is why when the opposite happens, it totally freaks me out."
    show mike at startle(0.1, 5)
    show kylie at blacker, zoomAt(1, (220, 720)), startle(0.1, 5)
    show bg university at startle(0.1, 5)
    bree.say "[mike.name]..."

    if hero.morality >= 25:
        bree.say "Who's that creepy girl over there?"

    elif hero.morality <= -25:
        bree.say "Who's the creepy girl with the extra chunky thighs?"
    else:

        bree.say "I meant to ask, who actually is that?"
    show mike at center, traveling(1.6, 1.2, (640, 1080))
    "[mike.name] turns to stare at me for a moment, like he's thrown by the question."
    show mike a casual blush
    pause 0.7
    hide kylie
    show kylie casual normal zorder 1 at center, zoomAt(0.85, (220, 720))
    with dissolve
    "But then he follows my gaze and seems to spot the girl I'm talking about."
    show kylie shy
    show mike b talkative at startle(0.1, 5)
    mike.say "Oh..."
    mike.say "That's just Kylie - she's harmless, even if she is a little intense!"
    mike.say "I used to date her older sister in high-school."
    mike.say "Remind me to tell you that story some time, it's quite a tale!"
    show mike b normal
    "I can't help feeling puzzled at how dismissive [mike.name] seems to be towards the girl."
    "Even now she's still looking right at him, staring a hole through the back of his head."
    show mike at startle(0.1, 5)
    show kylie at startle(0.1, 5)
    show bg university at startle(0.1, 5)
    bree.say "So what's her story?"
    bree.say "Does she like you or something?"
    bree.say "Or did you once like her?"
    show mike a sadsmile at stepback(0.05, 3,0)
    pause 0.05
    show mike a sadsmile at stepback(0.05,-3,0)
    pause 0.1
    "[mike.name] chuckles at this, shaking his head as he turns to walk away."
    show mike a talkative at startle(0.1, 5)
    mike.say "Nah, [hero.name]..."
    mike.say "It's like I already said - Kylie's just a bit of a quirk, that's all."
    show mike b normal at traveling(1.1, 2, (1500, 780))
    show kylie smile at zoomAt(0.85, (220, 720)) with dissolve
    "I turn to look back at the girl as [mike.name] walks off."
    show kylie smile at traveling(1.6, 0.7, (640, 1050))
    pause 0.7
    with vpunch
    "And I almost jump out of my skin, as she's suddenly a few feet closer!"
    "I mean logically she must have moved when we were talking just now."
    "But it's still more than a little unnerving."
    "Even more so now that I can hear that she's saying something to herself."
    show kylie shy at startle(0.1, 5)
    kylie.say "I know what he likes..."
    kylie.say "Yes, my precious one..."
    kylie.say "I know better than anyone!"
    show kylie smile
    "I find myself standing there, staring a the creepy girl and usure of what to do next."
    "But at the same time I know that I have to do something, because I she gives me a bad feeling."
    "Like what she's doing is wrong, and if it goes unchallenged, it's only going to get worse."
    menu:
        "Call Kylie out":
            "[mike.name] might be all blasé and whatever about this Kylie girl."
            "But that's probably because he thinks he knows her from when they were kids."
            "Plus he's a guy, and I guess she's cute, in a kind of pear-shaped way."
            "But I can see through all that, and if he wont confront her, then I will!"
            show kylie at startle(0.1, 5)
            show bg university at startle(0.1, 5)
            bree.say "Hey, you..."
            bree.say "Hey, Kylie!"
            show kylie stuned at startle(0.1, 5)
            "At the sound of her name, Kylie turns her head to look straight at me."
            "But somehow she manages to do it in the creepiest way possible."
            "Like, she turns her head really slowly, and she cocks it on one side too."
            "Plus she still has that weird smile on her face, and her eyes are almost glazed over."
            show kylie talkative at startle(0.1, 5)
            kylie.say "Huh?"
            kylie.say "Did I hear a little mouse squeaking?"
            kylie.say "What are you squeaking about, little mouse?"
            show kylie impressed
            "Eww...what a total creep!"
            show kylie at startle(0.1, 5)
            show bg university at startle(0.1, 5)

            if hero.morality >= 25:
                bree.say "Look, Kylie, I know what you're up too."
                bree.say "You just keep away from [mike.name], and me too!"

            elif hero.morality <= -25:
                bree.say "Cut the crap, Kylie..."
                bree.say "And quit following [mike.name] around too!"
            else:

                bree.say "Get a life, you creepy little bitch."
                bree.say "If [mike.name] was gonna fuck you, it'd have happened already!"
            "Kylie stares at me in silence for a prolonged moment."
            "Far too long for her to simply be considering what I just said to her."
            "But just long enough to make me start sweating as holds my gaze."
            show kylie talkative at startle(0.1, 5)
            kylie.say "Huh..."
            kylie.say "I have no idea what you're even talking about."
            hide kylie with easeoutleft
            "Just like that, Kylie spins on her heel and walks away."
            "I guess I should be happy that she's going in the opposite direction to me."
            "But some base instinct, deep down in my guts is telling me this isn't over."
            "Not by a long way."
            $ kylie.yandere += 5
            $ kylie.love -= 1
        "Ignore Kylie as best I can":
            "But then [mike.name] is the only one of us that actually knows her."
            "And if he's so sure she's harmless, maybe I should trust his instincts?"
            "After all, she hasn't really done anything to prove him wrong."
            "So taking one last look in her direction, I follow [mike.name]'s lead."
            "Which means that I turn on my heel and walk after him."
            "But some base instinct, deep down in my guts is telling me this isn't over."
            "Not by a long way."
            $ kylie.yandere += 2
        "Try to be friendly to Kylie":
            "[mike.name] might be all blasé and whatever about this Kylie girl."
            "But that's probably because he thinks he knows her from when they were kids."
            "Plus he's a guy, and I guess she's cute, in a kind of pear-shaped way."
            "But I know that it can be tough being an attractive girl."
            "And I wonder if anyone actually takes the time to talk to her at all?"
            show kylie at startle(0.1, 5)
            show bg university at startle(0.1, 5)
            bree.say "Hey..."
            bree.say "Hey, Kylie?"
            show kylie stuned at startle(0.1, 5)
            "At the sound of her name, Kylie turns her head to look straight at me."
            "But somehow she manages to do it in the creepiest way possible."
            "Like, she turns her head really slowly, and she cocks it on one side too."
            "Plus she still has that weird smile on her face, and her eyes are almost glazed over."
            show kylie talkative at startle(0.1, 5)
            kylie.say "Huh?"
            kylie.say "Did I hear a little mouse squeaking?"
            kylie.say "What are you squeaking about, little mouse?"
            show kylie normal
            "Okay, that was way creepier than I was expecting it to be!"
            show kylie at startle(0.1, 5)
            show bg university at startle(0.1, 5)
            show kylie stuned
            bree.say "Erm..."
            bree.say "No mice, Kylie - just me."
            bree.say "My name's [hero.name], by the way."
            bree.say "[mike.name] was just telling me he knows you from high-school?"
            bree.say "That he used to date your sister?"

            if hero.morality >= 25:
                bree.say "So you were friends, right?"

            if hero.morality <= 25:
                bree.say "Let me guess - you secretly wanted to fuck him, yeah?"
            else:

                bree.say "Is that why you're always watching him?"
            "At first Kylie watches me with that same glazed-over expression."
            "But as soon as I mention her past connection to [mike.name], all of that changes."
            show kylie impressed
            "I see a light flare in her eyes, and she seems to come to life."
            "Admittedly it's a creepy, almost disturbing kind of life."
            "But that seems to be kind of Kylie's whole thing."
            "So what am I going to do about it?"
            show kylie sadhappy at startle(0.1, 5)
            kylie.say "Alexis never deserved him, never appreciated him..."
            kylie.say "All she did was use poor [mike.name] and then cast him aside!"
            show kylie shy
            "I feel like there's a certain sadness in Kylie's voice now."
            "As if I've managed to touch a nerve without intending to."
            "I'm about to ask her something else, but she doesn't seem to be looking at me any more."
            show kylie normal at traveling(1, 1, (-300, 720))
            "And as I watch, she turns away and starts to wander off in the opposite direction."
            "All the while still muttering to herself as she alternates between nodding and shaking her head."
            "Part of me is glad to see Kylie walking away from me."
            "But some base instinct, deep down in my guts is telling me this isn't over."
            "Not by a long way."
            $ kylie.yandere += 3
            $ kylie.love += 1
    scene bg black with dissolve
    return

label kylie_female_event_03:
    if kylie.love.max < 60:
        $ kylie.love.max = 60
    show bg house with fade
    "It's been one of those days when I've given everything that I have just to get through it."
    "And by the time I make it back home, I'm total on auto-pilot, ready to just collapse onto the sofa."
    "So it comes as a genuine relief to see that the lights are on low as I walk up to the front-door."
    "Because that means that Sasha and [mike.name] are either doing something quiet or else they're still out."
    "Not feeling like a conversation even if the former is true, I open the door as quietly as I can."
    play sound door_open
    show bg livingroom at center, dark, zoomAt(1.2, (640, 720)) with fade
    "Then I slide into the hallway, closing it so as not to make any sound that's likely to be heard."
    "And the last thing that I'm thinking of doing right now is actually calling out to anyone else in the house."
    "In fact my plan is to just head straight for my bedroom and hide away in there for the time being."
    show bg livingroom at center, traveling(1.2, 0.5, (700, 720))
    "Maybe I'll feel more like being sociable later on, at least after I've had a little rest."


    show bg livingroom at vshake, zoomAt(1.2, (700, 720))
    "The only problem is that I haven't made it to the stairs before I hear a sound."
    "And then I feel the sensation of my heart sinking in my chest as I see someone moving down the hallway."
    show bg livingroom at startle(0.5, 1), zoomAt(1.2, (700, 720))

    if hero.morality >= 25:
        bree.say "Erm..."
        bree.say "Sasha?"
        bree.say "[mike.name]?"
        bree.say "Who's there?"

    if hero.morality <= 25:
        bree.say "What are you doing slinking around in the shadows?"
        bree.say "Getting up to something naughty, are we?"
    else:

        bree.say "Oh, hey - I didn't see you there!"
        bree.say "I'm just gonna go to my room, okay?"
    stop sound
    "Almost as soon as the words are out of my mouth, the figure freezes."
    show kylie at right, blacker, zoomAt(1, (1000, 720)) with easeinright
    "And I can feel them staring at me, even while they're hidden in the shadows."
    "Which is really freaky and weird, as why would [mike.name] or Sasha react like that?"
    "Without thinking, my hand shoots out to hit the light-switch."


    show bg livingroom at brighter, zoomAt(1.2, (700, 720))
    show kylie annoyed zorder 1000 at brighter
    with hpunch
    pause 0.3
    stop sound
    "And a second later, the hallway is flooded with light."
    "I can't help squinting at the sudden brightness."
    show kylie annoyed
    "But the other person seems to be more acutely affected."
    "As they throw their hands up to cover their eyes as if blinded."
    "Though not before I recognise just who they actually are."
    show bg livingroom at startle(0.1, 5), zoomAt(1.2, (700, 720))
    show kylie at startle(0.1, 5)
    bree.say "Kylie?"
    bree.say "What in the hell are you doing here?!?"
    "As Kylie seems to adjust to the light, I see that she has something in her hands."
    "It's a garment of some kind, and one that I soon realise is familiar to me."
    bree.say "Hey, that's one of [mike.name]'s shirts!"
    bree.say "What are you doing with it?"
    show kylie stuned
    "Kylie has an oddly cold look in her eye as she glances down at the shirt."
    "And it persists as she then looks back up at me, almost making me shiver."
    show kylie shy
    "Then a smile spreads across her face, as if she's just remembered to put one on for my sake."
    "Yet the look in her eyes is still enough to seriously creep me out."
    show kylie sadhappy at center, traveling(1, 1, (640, 720))
    kylie.say "Oh..."
    kylie.say "Hello, [hero.name]."
    kylie.say "[mike.name] let me in..."
    kylie.say "But then there was an emergency, and he had to leave."
    kylie.say "He said that I could wait for him until he came back."
    show kylie normal
    "I narrow my eyes as I listen to Kylie's explanation."
    "Because none of it sounds very plausible to me."
    menu:
        "Kick Kylie out":
            "Urgh...this girl is the creepiest!"
            "And the idea of her slinking around the house..."
            "Well, it's enough to give me nightmares."
            show bg livingroom at traveling(1, 1, (640, 720))
            play sound door_open
            show kylie at traveling(0.9, 1, (700, 720))
            "So I walk back over to the door and open it wide."
            "Then I point outside and give Kylie my hardest stare."
            show kylie at startle(0.1, 5)
            show bg livingroom at startle(0.1, 5)

            if hero.morality >= 25:
                bree.say "You have to get out of here, right now."
                bree.say "And if you don't, I'll call the police - I mean it!"

            if hero.morality <= 25:
                bree.say "If you're looking for a booty-call, this is not the way to get one."
                bree.say "Now get out, before I paddle your crazy ass!"
            else:

                bree.say "I don't care, Kylie..."
                bree.say "Just get the fuck out of my house - NOW!"
            show kylie stuned with dissolve
            "Suddenly Kylie's mask seems to slip, and the smile is gone."
            "In it's place is a venemous sneer, and a crazy fire in her eyes."
            "And she hisses at me, her voice barely above a whisper."
            show kylie vangry at startle(0.1, 5)
            kylie.say "You'll regret this, bitch..."
            kylie.say "You'll regret pushing me out!"
            show kylie stuned at traveling(1, 1, (-300, 720)) with easeoutleft
            "With that, Kylie rushes straight past me and out of the door."
            play sound door_slam
            show bg livingroom with hpunch
            "And I hastily slam it closed behind her, securing all of the locks."
            play sound door_lock
            "Then I make a point of scouring the entire house, trying to find how she got in."
            "But in the end I have to settle for just locking the doors and windows."
            "That and hoping she doesn't come back any time soon."
            $ kylie.love -= 3
            $ kylie.yandere += 3
            $ hero.morality -= 3
        "Calmly tell Kylie to leave":
            "My instinct is to grab Kylie by the hair and toss her out the door!"
            "Or maybe, if I'm more honest, to open it and tell her to leave."
            "After all, she is pretty scary!"
            "But there's the chance that she might get violent if I provoke her."
            show bg livingroom at traveling(1, 1, (640, 720))
            play sound door_open
            show kylie stuned at traveling(0.9, 1, (700, 720))
            "So instead I slowly open the door and gesture to it."
            show kylie at startle(0.1, 5)
            show bg livingroom at startle(0.1, 5)

            if hero.morality >= 25:
                bree.say "If you go now, Kylie..."
                bree.say "Maybe we can forget all about this?"

            if hero.morality <= 25:
                bree.say "Look, Kylie, whatever freaky action you want, you're not getting it here."
                bree.say "So why don't you make like a tree, and leave?"
            else:

                bree.say "We both know [mike.name] didn't let you in, Kylie..."
                bree.say "So I'm giving you the chance to leave now, before he comes back."
            show kylie sad with dissolve
            "Kylie's expression changes as I make the offer."
            "And for a moment she almost looks sad."
            "As if my being a little kind to her breaks something on the inside."
            show kylie stuned
            "But then, quick as a flash, she reverts back to looking totally crazy."
            show kylie surprised at startle(0.1, 5)
            kylie.say "You're wrong, bitch..."
            kylie.say "[mike.name] wants me, he just hasn't admitted it yet."
            kylie.say "And I'm keeping this as a memento of him!"
            show kylie impressed at traveling(1, 1, (-300, 720)) with easeoutleft
            "With that, Kylie rushes straight past me and out of the door, still clutching [mike.name]'s shirt."
            play sound door_slam
            with hpunch
            "And I hastily slam it closed behind her, securing all of the locks."
            play sound door_lock
            "Then I make a point of scouring the entire house, trying to find how she got in."
            "But in the end I have to settle for just locking the doors and windows."
            "That and hoping she doesn't come back any time soon."
            $ kylie.love += 1
            $ kylie.yandere += 1
        "Try to talk to Kylie":
            "My instinct is to grab Kylie by the hair and toss her out the door!"
            "Or maybe, if I'm more honest, to open it and tell her to leave."
            "After all, she is pretty scary!"
            "But there's a part of me that wonders if all this is just a cry for help."
            "Like, does anyone really take the time to talk to this poor girl?"
            show kylie at startle(0.1, 5)
            show bg livingroom at startle(0.1, 5)

            if hero.morality >= 25:
                bree.say "It's okay, Kylie..."
                bree.say "You're not in any kind of trouble."
                bree.say "Would you like to talk about it?"
                bree.say "About why you're here?"

            if hero.morality <= 25:
                bree.say "Look, girl - I know what it feels like to want a guy's attention."
                bree.say "But this is SO not the way to go about it, you know?"
                bree.say "Maybe what you need is someone to talk to?"
            else:

                bree.say "Just stay calm, Kylie..."
                bree.say "Nobody's mad with you, I promise."
                bree.say "In fact, we can talk about it..."
                bree.say "If that'd help?"
            show kylie sad
            "Kylie's expression changes as I make the offer."
            "And for a moment she almost looks sad."
            "As if my being a little kind to her breaks something on the inside."
            show kylie sadhappy at startle(0.1, 5)
            kylie.say "I..."
            kylie.say "I just..."
            kylie.say "I don't want to be alone!"
            show kylie sad
            "I'm about to say something more to her, to try to draw her out further."
            "But then I realise that Kylie seems to be talking to herself more than to me."
            "She drops the shirt on the floor and starts walking slowly towards the door."
            show kylie at stepback(0.3, 5,0)
            pause 0.3
            show kylie at stepback(0.3, 5,0)
            pause 0.3
            "Still muttering under her breath and shaking her head as she goes."
            play sound door_open
            show kylie sad at traveling(1, 2, (-300, 720)) with easeoutleft
            "Kylie even seems to ignore me as I open the door to let her out."
            play sound door_close
            pause 1
            play sound door_lock
            "And then I close it slowly behind her, locking it as soon as she's gone."
            "Then I make a point of scouring the entire house, trying to find how she got in."
            play sound door_lock
            "But in the end I have to settle for just locking the doors and windows."
            "That and hoping she doesn't come back any time soon."
            $ hero.morality += 3
            $ kylie.love += 3
            $ kylie.yandere -= 3
    show bg black with dissolve
    $ kylie.flags.delay = TemporaryFlag(True, 2)
    return

label kylie_female_event_04:
    if kylie.love.max < 80:
        $ kylie.love.max = 80
    play sound door_close
    show bg livingroom with fade
    play sound door_close
    "Walking in through the front door, my mind's occupied by the usual obsessions at this time of day."
    "And I'd like to say that's a whole load of different things concerning how I'm going to spend my evening."
    "But who am I kidding?"
    "The main thing that's going through my head is the rumblings from my stomach!"
    "I'm starving, and what's worse, I'm going to have to put in the effort to feed myself too."
    bree.say "[mike.name]..."
    bree.say "Sasha..."
    bree.say "I'm h...h...h..."
    "I'm all set to say the word 'home' and announce my arrival to my housemates."
    "But as soon as the scent filling the hallway hits my nostrils, I forget everything else."
    "Because it's the divine smell of food - something I can never remember smelling this good."
    bree.say "Hungry!"
    bree.say "I'm hungry!"
    "Tossing my things into a heap at the bottom of the stairs, I turn towards the kitchen."
    "And then it's all that I can do to keep from dashing straight in there."
    "Seriously, I could be carried along on the scent, like a character in an old-fashioned cartoon!"
    "But once I make it to the open doorway, that's the time to start getting myself under control."
    "Because I don't want to rush in there looking like some kind of food-crazed lunatic."
    scene bg kitchen
    show mike b at center
    with wipeleft
    bree.say "Hello in there..."
    bree.say "Smells like someone's been busy?"
    show mike happy
    mike.say "Oh..."
    mike.say "Hi, [hero.name]!"
    show mike smile
    "[mike.name] turns around to give me a wave as he spots me standing in the doorway."
    "He's right in the middle of putting the finishing touches to something on the stove."
    "And from the smile on his face, I'd guess that he's pleased to see me."
    "Which is good, as it probably means he's intending on feeding me too!"
    show mike happy
    mike.say "Sorry about the mess in here."
    mike.say "I just got the urge to cook, you know how it is?"
    show mike normal
    bree.say "Oh, sure..."
    bree.say "It just takes hold of you, right?"
    bree.say "And before you know it, you've knocked up a banquet!"
    "Okay that's a total lie - I fucking hate to cook."
    "But I'm not going to admit that when there's a free meal to be had."
    show mike a happy
    mike.say "Well, I don't know about an entire banquet!"
    mike.say "But I can certainly handle cooking for three."
    show mike normal
    "I'm nodding away as I start to saunter into the room."
    "Making sure to keep smiling at [mike.name] as I inhale the aroma of his cooking."
    "It's important to reassure him it smells incredible, that I'm eager to try it."
    "Or else he might never volunteer to do this kind of thing again."
    bree.say "So what..."
    bree.say "It's just you, me and Sasha tonight?"
    bree.say "Don't tell me you couldn't get a date in time?"
    "I'm expecting [mike.name] to shrug and make some kind of excuse."
    "But instead he smiles and shakes his head at me."
    "Then I hear the sound of someone coughing, just out of sight."
    kylie.say "Ahem!"
    "Somehow I just know who it's going to be before I turn around."
    "You know how with some people, you can recognise the sound of their voice, even when it's just a cough?"
    show kylie at right with easeinright
    bree.say "KYLIE!" with hpunch
    show mike b surprised
    "[mike.name] seems to be pretty surprised at the volume that came out of me at."
    "But to her credit, Kylie doesn't even flinch."
    "She just stays where she is, sitting and staring at me."
    show mike talkative
    mike.say "Erm..."
    mike.say "Yeah, [hero.name] - it's Kylie alright."
    mike.say "Though I'm not sure why you'd be so surprised to see her again."
    mike.say "You know the two of us have been spending more time together recently."
    show mike normal
    bree.say "Yeah, I noticed."
    bree.say "Looks like this time you invited her around yourself."
    bree.say "Rather than her just inviting herself!"
    show mike upset with dissolve
    "[mike.name] looks puzzled by the comment, frowning at me."
    "But, of course, Kylie knows exactly what I'm talking about."
    "I mean, did she just expect me to forget about how she literally broke in here the other day?!?"
    "So she's super quick to interject before [mike.name] can ask what the hell I'm talking about."
    show kylie talkative
    kylie.say "Obviously what [hero.name] means is that it was about time you invited me over, [mike.name]."
    show kylie smile
    kylie.say "Otherwise I'd have been forced to invite myself over just to see you!"
    show kylie normal
    "To me that sounds like a massive, steaming pile of horseshit."
    show mike normal
    "But for some reason [mike.name] just seems to swallow it whole and smile."
    "For a moment I think that he's just tired or distracted with all the cooking."
    show mike smile at startle(0.2, -10)
    "But then I see him give Kylie a certain kind of look, and it dawns on me."
    "The poor guy's only gone and started falling for this total fruitcake of a girl!"
    show mike happy
    mike.say "Oh, babe..."
    show mike at startle(0.05, 5)
    mike.say "That is SO like you."
    mike.say "Just waiting to be invited over the threshold of my home."
    show mike smile
    bree.say "Yeah..."
    bree.say "Just like a vampire!"
    show kylie angry
    "As if on cue, Kylie shoots me a venomous look."
    "And I'm not kidding, the girl actually hisses at me!"
    show kylie crazysad
    kylie.say "Hsssss!"
    show kylie angry
    "But rather than being freaked out, as he damn well should be, [mike.name] bursts out laughing."
    show mike a happy
    mike.say "HA!"
    mike.say "Sweet Dracula impression, babe!"
    mike.say "You're lucky Kylie's got such a great sense of humour, [hero.name]."
    show mike normal
    "I'm about to say something in protest, but the stove pings."
    "Which means [mike.name] instantly turns his back on me to attend to the food."
    show mike happy
    mike.say "Okay, guys..."
    mike.say "No more time for chit-chat and joking around."
    mike.say "Because it's time to eat!"
    show mike normal
    "Oh man, this is turning into one of those really awkward situations."
    "You know the ones - where the girls are looking daggers at each other?"
    "But the guy's just totally oblivious and carrying on as normal?"
    "There's no way that I can just come right out and call Kylie on her craziness though."
    "Because she's obviously managed to charm [mike.name] and convince him she's all sweetness and light."
    "So instead I force a smile onto my face and sit down on the opposite side of the table."
    show mike happy
    mike.say "I hope you girls are hungry..."
    mike.say "Because I made enough to feed an army!"
    show mike normal
    "I do the best I can to keep the smile on my face as [mike.name] dishes up the food."
    "And I have to admit that he's cooked up a pretty decent meal for the three of us."
    "Which helps to distract me for a while, as I start tucking into it."
    bree.say "Mmm..."
    bree.say "This is really good, [mike.name]!"
    bree.say "Why'd you never cook this for me before?"
    "Obviously, [mike.name]'s more than pleased to accept my praise for his cooking."
    "And he adopts that kind of knowing, cocky demeanour guys get when their egos are being stroked."
    show mike talkative
    mike.say "Well, [hero.name]..."
    mike.say "Maybe you and Sasha never asked me."
    show mike happy
    mike.say "Did you ever think of that?"
    "[mike.name] and I are sharing a little moment of mutual amusement as we eat."
    "Not really flirting in any sense, just joking around, like friends do."
    show mike surprised with vpunch
    "But then there's the sound of metal scraping against porcelain."
    "It's high-pitched and piercing, setting my teeth on edge."
    "Both of us look around at the same time, glancing at Kylie."
    "And I see that she's deliberately dragging her knife across the plate in front of her."
    show kylie zorder 9 at right, traveling(1.2, 1, (840, 820))
    pause 1
    show kylie shout
    kylie.say "I sincerely hope you mean that, [hero.name]."
    kylie.say "Because I can't stand people that lie so casually."
    show kylie angry
    pause 1
    show kylie at right, traveling(1.4, 1, (800, 920))
    pause 1
    show kylie crazyhappy at startle(0.05, 5)
    kylie.say "Lies are like a cancer, did you know that?"
    kylie.say "If you don't cut them out, then they fester..."
    show kylie vangry
    kylie.say "And then they spread!"
    "There's an obvious tension building in the air as Kylie speaks."
    "And I know that I'm not the only one feeling it."
    "Because [mike.name]'s looking more than a little concerned too."
    show mike b at center, traveling(1.2, 0.5, (540, 820))
    pause 0.5
    "Problem is, I think he's too into this whack-job to do anything about it."
    menu:
        "Call Kylie a dangerous psychopath":
            "But while he might be under the spell of the psycho-siren, I'm not."
            "And the whole busty serial-killer thing is starting to wear thin."
            bree.say "Okay, Kylie..."
            bree.say "I'm done being nice with you."
            bree.say "And I'm done listening to your Hannibal Lecter with tits bullshit!"
            show mike surprised at hshake
            "[mike.name] literally drops his cutlery as he hears me laying down the law."
            "His eyes so wide they're almost popping out of their sockets with amazement."
            "And his lips moving at the same time, with no sound coming out of his mouth."
            "But one glace at Kylie is more than enough to make me sure I made the right call."
            "Whereas [mike.name]'s shocked into silence, she's glaring at me with cold, calculating hatred in her eyes."
            show kylie crazyhappy
            kylie.say "So you were lying just now, [hero.name]."
            kylie.say "Thank you for proving me right."
            kylie.say "Thank you for showing [mike.name] what a lying little bitch you are!"
            show mike upset
            "[mike.name] seems to have finally regained the ability to speak."
            "And I'm waiting for him to come wading into the argument."
            "Probably on the side of Kylie, as she's got him wrapped around her little finger."
            show mike angry
            mike.say "Whoa, whoa, whoa..."
            mike.say "Let's all just chill out here, okay!"
            show mike normal
            "I look at him in surprise, not having expected him to play the peacemaker."
            "But Kylie's shock probably comes from her assuming he'd be taking her side exclusively."
            bree.say "I don't need to calm down, [mike.name]..."
            bree.say "You need to see this psycho for what she really is."
            bree.say "She's fucking dangerous!"
            "I leap to my feet as I say this, and Kylie mirrors the move."
            "But what I hadn't counted on was her still having the knife in her hand."
            "Which she slashes through the air in a way that looks pretty serious."
            show kylie crazysad
            kylie.say "Cut them, cut them out..."
            kylie.say "Cut out the lies!"
            "Before [mike.name] or I can say another word, Kylie makes a run for the door."
            "She knocks over her chair and darts into the hallway."
            hide kylie with easeoutright
            "[mike.name] and I are just in time to see her vanish through the front door."
            show mike angry
            mike.say "Oh dear..."
            mike.say "Somebody's going to be all cross in the morning!"
            show mike normal
            with hpunch
            bree.say "What the hell is that supposed to mean?!?"
            bree.say "Didn't you see that bitch just try to kill me?"
            mike.say "Oh come on, [hero.name] - she just waved her cutlery in the air, that's all."
            mike.say "You must have noticed that Kylie's a little highly-strung."
            play sound door_close
            "I shake my head as I close the door and make sure it's locked tight."
            bree.say "If by that you mean she's bat-shit crazy..."
            bree.say "Then yeah, I totally did!"
            $ hero.morality -= 3
            $ kylie.love -= 3
            $ kylie.yandere += 3
        "Defuse the situation with humour":
            "The best way that I know to diffuse a situation like this is humour."
            "And so I raise my eyebrows at Kylie's little diatribe."
            "Making it obvious that I'm not taking her at all seriously."
            bree.say "Wow, Kylie..."
            bree.say "I thought this was a meal, not an autopsy!"
            bree.say "Hey, [mike.name]..."
            bree.say "Do you remember the cause of death?"
            bree.say "I'm guessing you slaughtered the veggies yourself?"
            bree.say "Drowned them, if I'm not mistaken?"
            show mike happy at startle(0.05, 5)
            pause 0.3
            show mike smile with dissolve
            "[mike.name] covers his mouth with one hand and looks down at his plate."
            "But it's plain to see that he's chuckling to himself."
            "Doing the best he can not to openly laugh at my mocking Kylie."
            show mike talkative
            mike.say "Ah..."
            mike.say "I confess, [hero.name]..."
            show mike happy at startle(0.05, 5)
            mike.say "I'm a mass-murderer - at least when it comes to vegetables!"
            "Knowing that I have [mike.name] on side, I risk a sideways glance at Kylie."
            "And that's when I almost find myself freezing in my seat."
            "Because she's not frowning like I was expecting her to be."
            show kylie angry at center, traveling(1.6, 1.7, (700, 1020))
            "Instead she's staring straight at me, eyes wide open."
            "And the neutral expression on her face is somehow scarier than any grimace could ever hope to be."
            show kylie crazysad
            kylie.say "Ha...ha...ha..."
            kylie.say "Oh, [hero.name]..."
            kylie.say "You're so funny."
            show kylie crazyhappy at startle(0.05, 5)
            kylie.say "Just be careful that you don't DIE laughing."
            "Feeling my appetite disappear in the blink of an eye, I push back my chair."
            "And then I stand up, shaking my head and glancing at the door."
            bree.say "Erm..."
            bree.say "I think I'm full, guys!"
            bree.say "So I'm gonna go sleep it off in my room, okay?"
            show mike talkative
            mike.say "Are you sure, [hero.name]?"
            mike.say "I got ice-cream in for dessert."
            show mike normal
            "I'm already at the door as [mike.name] says all of this."
            "And I don't hesitate to shake my head as I step into the hallway."
            bree.say "No, no..."
            bree.say "You two just have some nice, quiet time together, okay?"
            "I make a point of hurrying off before [mike.name] can say another word."
            "And I don't stop until I'm behind the door of my bedroom."
            play sound door_open
            scene bg bedroom2 with fade
            play sound door_close
            "Even then I have to fight the urge to push a piece of furniture in front of it."
            $ kylie.love += 1
            $ kylie.yandere += 1
        "Tell Kylie that I'm worried about her":
            "Okay, so this girl seems to be totally crazy, and she's serioulsy freaking me out."
            "But there's got to be a reason that she ended up like this, right?"
            "And if [mike.name]'s too smitten to see that she's a complete fruit-loop..."
            "Then he's also going to be blind to the fact she probably needs help too."
            bree.say "Tell me something, Kylie..."
            bree.say "Does saying stuff like that really help?"
            bree.say "I mean, does it make the voices inside your head stop for even a moment?"
            "The questions seem to be even more shocking than Kylie's own words."
            "Because now I see that I have both her and [mike.name] staring at me."
            show mike angry
            mike.say "Hey, [hero.name]..."
            mike.say "Where do you get off saying stuff like that?"
            mike.say "I'm sure Kylie was just joking around before..."
            show mike happy at startle(0.05, 5)
            mike.say "Weren't you, babe?"
            "He nods to Kylie as he says this, obviously trying to get her to agree."
            "But she doesn't even seem to be hearing the words coming out of his mouth."
            "And for a moment I think Kylie's going to suddenly explode with rage."
            show kylie sad with dissolve
            "But then she shocks me by noisily dropping her knife onto the table."
            show kylie shy
            kylie.say "I..."
            kylie.say "I don't know..."
            kylie.say "I don't know what's wrong with me!"
            show kylie sad
            "For a long, drawn-out moment, [mike.name] and I just stare at each other."
            "Neither of is seeming to know what to do or say."
            "But in the end, I decide that I need to remove myself from the scene."
            "So I stand up and push my chair backwards, edging away from the table."
            bree.say "Okay..."
            bree.say "I am going to leave the two of you alone."
            bree.say "Because it looks like you maybe need to talk."
            bree.say "So if anybody wants me, I'll be in my room."
            "I make a point of hurrying off before [mike.name] can say another word."
            "And I don't stop until I'm behind the door of my bedroom."
            play sound door_open
            scene bg bedroom2 with fade
            play sound door_close
            "Because if there's one thing scarier than Kylie's psycho behaviour..."
            "It's the prospect of being the shoulder she's about to start crying on!"
            $ hero.morality += 3
            $ kylie.love += 3
            $ kylie.yandere -= 3
    show bg black with dissolve
    $ kylie.flags.delay = TemporaryFlag(True, 2)
    return

label kylie_female_event_05:
    if kylie.love.max < 100:
        $ kylie.love.max = 100
    scene bg livingroom with fade
    "Walking from one room to another in the house is one of those weird little bits of dead time."
    "Short little snippets of your life where you're neither one place or the other for those few seconds."
    "Normally they pass briefly and are forgotten, not even lingering in your memory once you get to where you're going."
    "But then there are the times when something totally unexpected happens along the way."
    "And that's when they flip, becoming something that you'll never be able to forget."
    "Like right now, for example - I can't remember where I was supposed to be going, or exactly where I came from."
    "All that's on my mind is the fact that I can hear a voice coming from inside of [mike.name]'s room."
    "And no, I'm not normally in the habit of listening at other people's doors."
    "It's just that this voice definitely doesn't belong to [mike.name] himself."
    "Instead it sounds female, and I could swear that it's crying or moaning."
    "Okay, okay...I know where your mind just went, I totally do."
    "But I mean the kind of crying and moaning that's not associated with good things, yeah?"
    "Part of me wants to just pretend that I didn't hear anything and keep on walking."
    "But, against my better judgement, I turn and approach the bedroom door instead."
    "Seeing that it's ajar, I lean in closer and peek through the gap, trying to see who's in there."
    scene bg bedroom6 at dark, dark
    show kylie b zorder 1 at center, zoomAt(1, (0, 720))
    show black as foreground zorder 99 at center, zoomAt(1, (640, 720))
    show black as foreground at center, traveling(1, 1.5, (800, 720))
    "And it doesn't take me long to recognise the person I see inside when I do."
    show kylie a talkative with dissolve
    kylie.say "[mike.name]...[mike.name]...[mike.name]..."
    show kylie b sad with dissolve
    "There's a curvy, blonde girl in there, hunched in front of a mirror."
    "She has her hands stretched out in front of her, reaching for the glass."
    "At first I think she must be trying to wipe something off the surface of the mirror."
    "But then I realise her fingertips are actually touching it, like she's clawing at the glass."
    "And I don't need to see the reflection of her face to know that I'm looking at Kylie right now."
    show kylie a talkative with dissolve
    kylie.say "[mike.name]...[mike.name]...[mike.name]..."
    show kylie b sad with dissolve
    "I keep straining to make out what the word is that she's repeating to herself."
    "It sounds like it begins with an M and it's quite short."
    "Mine?"
    "Mark?"
    "Mink?"
    show kylie a talkative with dissolve
    kylie.say "[mike.name]...[mike.name]...[mike.name]..."
    show kylie b sad with dissolve
    "Suddenly I seem to be able to make sense of the word, and it all falls into place."
    "[mike.name]...she's saying [mike.name]'s name over and over again."
    "But while I know what she's saying, I still have no idea as to why she's saying it."
    "And there's no way I'm going to find out while I'm peeking through the door like this."
    menu:
        "Leave Kylie alone":
            "Okay, this girl just keeps getting weirder by the day."
            "At this rate they're going to be coming for her with a butterfly net."
            "And until that day comes, I'm going to keep my distance."
            "As quietly as possible, I stand up straight and take a step backwards."
            "Then I turn on my heel and start walking in the direction I was previously headed."
            show black as foreground zorder 99 at center, traveling(1, 1.5, (640, 720))
            pause 1.5
            scene bg livingroom with fade
            "At the same time doing the best I can to push the image of what I just saw out of my head."
            "Because if [mike.name]'s determined to put his dick in crazy, then he can handle it himself."
            $ kylie.yandere += 3
        "Confront her harshly":
            "Okay, this kind of thing might be acceptable in a rubber room at the nuthouse."
            "But I'm not about to put up with it happening under my own roof."
            "So I make a point of pushing the door open and striding into [mike.name]'s room."
            "Not caring that I make a whole lot of noise in the process of doing so."
            "Because the last thing I want is for Kylie to think I'm sneaking up on her."
            play sound door_open
            hide black as foreground with easeoutright
            scene bg bedroom6
            show kylie b at center, zoomAt(1, (0, 720))
            with dissolve
            bree.say "Okay, that's enough of that!"
            show kylie a surprised at vshake
            kylie.say "Aargh!"
            "The room is suddenly bathed in light from the corridor outside."
            "And Kylie raises her hands to cover her eyes from the glare."
            "Something that only serves to make her look that much more ghoulish in aspect."
            kylie.say "What's...what's going on?!?"
            show kylie stuned at center, traveling(1, 0.7, (320, 720))
            bree.say "I don't know, Kylie..."
            bree.say "Why don't you tell me?"
            show kylie annoyed
            bree.say "I'm not well up on why someone would be clawing at a mirror."
            bree.say "Let alone saying my housemates name over and over again at the same time!"
            show kylie angry with dissolve
            "Kylie's surprised expression doesn't last for long."
            show kylie at center, traveling(1.6, 1, (440, 1050))
            "And as she regains full control of her senses, she begins to glare at me."
            show kylie at center, traveling(1.8, 0.7, (480, 1160))
            pause 0.3
            show kylie vangry at startle(0.05, 10)
            kylie.say "You're only lying to yourself, bitch!"
            show kylie at center, traveling(2, 0.5, (520, 1270))
            pause 0.3
            show kylie vangry at startle(0.05, 10)
            kylie.say "You know as well as I do that you want him too."
            show kylie at center, traveling(2.2, 0.3, (560, 1380))
            pause 0.3
            show kylie vangry at startle(0.05, 10)
            kylie.say "That you'll do anything to steal him from me!"
            show kylie angry
            "I shake my head in amazement."
            "Unable to believe what I'm being accused of."
            bree.say "Have you lost your mind?"
            bree.say "Oh...yeah...I guess you probably have!"
            bree.say "But anyway, you're wrong, Kylie."
            bree.say "I'm not trying to take [mike.name] away from you."
            bree.say "In fact, I want to help you, if I can."
            show kylie sad with dissolve
            "For a moment I swear there's a change in Kylie's expression."
            "A certain glimmer in her eyes that tells me something's different."
            "And when she speaks, it's like I'm talking to some else entirely."
            show kylie talkative
            kylie.say "Huh...[hero.name]?"
            kylie.say "Please..."
            kylie.say "Please, help me?"
            show kylie sad
            "I open my mouth to say that I will."
            "I even start to reach out with my hand."
            show kylie impressed
            "But in the blink of an eye, Kylie snaps back to her normal, crazy self."
            hide kylie with easeoutright
            with hpunch
            "She leaps to her feet, darting past me even as I jump to the side."
            "And then she's gone, running towards the front-door, which I hear close a moment later."
            $ kylie.love += 1
            $ kylie.yandere += 1
        "Try to comfort her":
            "I might not be, like, a trained counsellor or anything."
            "But I've seen enough movies and TV series to know how it goes."
            "You just walk slowly towards the person and talk to them nicely, right?"
            play sound door_open
            hide black as foreground with easeoutright
            scene bg bedroom6 at dark
            show kylie yandere b at center, zoomAt(1, (0, 720))
            with dissolve
            "And so, with that in mind, I gently push the door open and tiptoe into [mike.name]'s bedroom."
            bree.say "Erm..."
            bree.say "Hi there, Kylie..."
            bree.say "It's me, [hero.name] - you remember me, right?"
            "I'm doing the best I can to keep my voice low and level."
            show kylie at center, traveling(1.2, 1, (220, 810))
            "Because the last thing that I want is to startle someone as obviously troubled as this girl."
            "Though all the same, the moment she hears me speaking, Kylie's head twists in my direction."
            "Honestly, it might be the dim lighting in [mike.name]'s bedroom or my nerves that does it."
            "But I swear Kylie's head almost turns through one hundred and eighty degrees!"
            show kylie impressed with dissolve
            kylie.say "[hero.name!u]!"
            kylie.say "What are you doing in here?"
            kylie.say "Are you...are you trying to steal him from me?!?"
            show kylie impressed
            "I can see that Kylie's fingers are still clawing at the mirror as she says this."
            "But know they're forming into what look almost like claws, as if she's preparing to strike."
            bree.say "Okay, Kylie..."
            bree.say "You need to calm down a little, yeah?"
            bree.say "I don't know what you're even talking about right now."
            bree.say "And I'm not here to take anyone away from anyone."
            bree.say "It's just you and me here now."
            "For a moment I honestly think that Kylie's going to attack."
            "That she's going to launch herself at me and do something crazy."
            "Like...I dunno...try to gouge my eyes out or the like."
            "But then something inside of her seems to break."
            show kylie sad with dissolve
            "The fire in her eyes dims, and she turns her head back to the mirror."
            "Though this time she simply stares into the glass, looking at her own reflection."
            show kylie shy
            kylie.say "He's not in there, is he?"
            show kylie sad
            bree.say "What do you mean, Kylie?"
            bree.say "In the mirror?"
            bree.say "No, there's nobody in there - just your reflection."
            "Kylie lets out a weary sigh."
            "And the sound makes me wonder how long she's been like this."
            "Whether she's been teetering on the edge of madness for years."
            show kylie shy
            kylie.say "I thought..."
            kylie.say "I thought that if I could have him..."
            kylie.say "Then I'd matter, right?"
            show kylie sad
            "I nod my head, more out of the desire to make Kylie keep talking than anything else."
            bree.say "You're talking about [mike.name], aren't you?"
            bree.say "All of this is somehow about him, isn't it?"
            "Kylie doesn't show any signs of disagreeing with me."
            "But then she doesn't nod her head either."
            show kylie sadhappy
            kylie.say "But it's not happening - no matter how hard I try."
            kylie.say "All it's doing is hurting me!"
            show kylie sad
            bree.say "I don't know what you're going through, Kylie."
            bree.say "But I really think that you need some professional help."
            bree.say "You know, like, to talk to a counsellor or something?"
            "As I'm saying this, Kylie rises to her feet and turns towards the door."
            "Then she starts to walk out and into the hallway, as if I'm not here at all."
            "For a moment I think about putting a hand on her shoulder to stop her."
            "Hell, I even consider slapping her to make her snap out of it."
            "But in the end, fear of what she might do afterwards stays my hand."
            "Instead I watch in silence as she proceeds to walk to the front door and let herself out."
            "And I keep on watching out of the window as Kylie walks down the path and onto the street."
            "All the while she seems almost to be in a trance, lost in a world of her own."
            "And even though I feel concern for her, part of me is still glad that she's gone."
            $ hero.morality += 3
            $ kylie.love += 3
            $ kylie.yandere -= 3
    show bg black with dissolve
    $ kylie.flags.delay = TemporaryFlag(True, 2)
    return

label kylie_kiss_me_female:
    show kylie
    "I feel like there's a spark between Kylie and me, you know?"
    "Like an unspoken connection that we're both aware of."
    "Sometimes I catch her looking at me in a certain kind of way."
    "And I'm getting to be convinced that my hunch is right."
    "I keep meaning to say something to Kylie, to bring it up with her."
    "The next time we're alone together, I sense the chance to do so."
    show kylie at center, zoomAt(1.5, (640, 1040))
    "But as I lean in and try to whisper something to her, Kylie beats me to it."
    hide kylie
    show kylie kiss
    with fade
    $ kylie.flags.kiss += 1
    "She doesn't say a word, just plants her lips against mine."
    "I freeze, totally taken by surprise and with no idea what to do next."
    "But I soon realise that it's not from fear."
    "Because as soon as Kylie starts kissing me, I surrender to the experience."
    "It just feels so right, explaining in a flash all that I've been feeling for her."
    "And it answers all of the questions I had in my mind too."
    "Far better than any conversation could have hoped to."
    show bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
