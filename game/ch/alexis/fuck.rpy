init python:
    Event(**{
    "name": "alexis_repeatable_cinema_event",
    "label": "alexis_repeatable_cinema_event",
    "conditions": [
        IsDone("alexis_event_04"),
        HeroTarget(
            IsGender("male"),
            IsActivity("date_watch_a_movie"),
            IsRoom("date_cinemaroom"),
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "alexis_repeatable_beach_event",
    "label": "alexis_repeatable_beach_event",
    "conditions": [
        IsDone("alexis_event_05"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach", "date_nudistbeach")
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/one_wish.ogg",
    "do_once": False,
    "once_month": True,
    })

label alexis_repeatable_cinema_event:
    show alexis
    mike.say "Alexis, remind me what you wanted?"
    "There's no immediate reply, and so I give her a gentle tap on the shoulder."
    alexis.say "Huh...what?"
    mike.say "What do you want to take into the film with you?"
    mike.say "Want to share a popcorn and soft-drink with me?"
    show alexis annoyed
    alexis.say "Oh, right...whatever's fine with me, [hero.name]."
    "I nod slowly and order the snacks, while trying to see where Alexis' attention was a moment beforehand."
    "Seems she could have been checking out the posters for the upcoming attractions."
    "Or else maybe she was checking out a bunch of guys on the other side of the lobby..."
    scene bg cinemaroom
    show alexis
    with fade
    "But as we make our way into the theatre and sit down, waiting for the film to start, I chide myself for being petty."
    "Of course guys are going to check Alexis out, she's gorgeous."
    "And if she chooses to glance back, then she's only human too."
    show alexis blush
    "I have to get over the fact that she cheated on me, as that happened so far into the past."
    "Sure, if she were getting up to stuff in the here and now, I'd be crazily pissed off."
    "But she's not, and that's the most important thing to remember."
    "Hell, it's not like I stopped eyeing up other women since we started seeing each other again, is it?"
    show alexis normal at center, zoomAt(1.5, (640, 1040))
    pause 0.5
    show alexis normal at center, zoomAt(1.5, (640, 1140)) with ease
    "Finding our seats, I can't help noting that the place is almost full."
    "I guess we weren't the only people who chose to see this movie and maybe thought it'd be a quiet time to do so."
    if alexis.flags.story == 2:
        show alexis happy at center, zoomAt(1.5, (640, 1140)), startle
        "Just as the house lights are going down, I hear Alexis chuckling to herself."
        "Intrigued by this, I lean in and whisper close to her ear."
        mike.say "What's so funny all of a sudden?"
        show alexis at center, zoomAt(1.5, (640, 1140)), startle
        "Alexis chuckles again, and then whispers back her answer."
        show alexis normal
        alexis.say "See that guy in the front row, the one with the badass haircut?"
        mike.say "Erm...yeah, I think so."
        mike.say "What about him?"
        alexis.say "He's been checking me out since we walked in."
        alexis.say "But his girlfriend just caught him doing it a couple of minutes ago."
        "I can now see the guy that Alexis must be talking about, sitting in the front row and looking decidedly uncomfortable."
        "She seems to be right, as the girl in the seat next to him is hissing something and jabbing a finger at him."
        "As the opening credits of the film roll, she gets up, empties a large drink into his lap and storms out."
        "He makes an alarmed sound and hurries after her, to the accompaniment of laughter from half the crowd and shushing from the other."
        "I look at Alexis, noting that she's one of those laughing."
        "And as I do so, it occurs to me that she must have been watching that guy at least as much as he was her."
        "How else could she have known what was going on?"
        "But then I shake my head, realising what a paranoid jerk I sound like."
        "We're sitting facing forwards, so of course she could see all of what just happened."
        "That letching moron just put on an impromptu pre-film show for the rest of us, that's all."
        "I shake my head at the thought of the hapless buffoon, and settle down to watch the film."
        scene bg cinemaroom at dark with dissolve
        "The next couple of hours pass in the pleasant alternate reality of the silver screen, and I forget all of my problems for almost the whole while."
        "All that manages to snap me out of it for a couple of seconds is the feeling of someone touching me in the darkness."
        "But then I realise it's just Alexis, taking my hand in hers and leaning her head on my shoulder."
        "After this, it doesn't take me long to lose myself in the film once more."
        scene bg cinemaroom
        show alexis blush at center, zoomAt(1.5, (640, 1040))
        with dissolve
        "On the way out of the room, Alexis is still hanging off of my arm, leaning into me with a smile on her face."
        alexis.say "This was fun, [hero.name]."
        alexis.say "I can't remember when I last went to see a film on a date."
        alexis.say "Well...maybe when I did and had such a great time!"
        mike.say "Me too, Alexis."
        mike.say "We shouldn't wait too long before we do this again."
        "I feel her squeeze my arm in response, and it gives me a feeling like something fluttering in my chest."
        "So what does it matter how many guys she looks at?"
        "So long as she's walking home on my arm at the end of the night."
        $ game.active_date.score += 10
    else:
        scene bg cinemaroom at dark with dissolve
        "By the time we're sitting in our seats, watching the trailers, I can already feel my eyes starting to close."
        "The dark theatre, plush seats and the way a film takes you out of reality all conspire to send me off to sleep."
        menu:
            "Try to stay awake":
                "But that doesn't mean I have to just sit back and let it happen."
                "I've had a tough week, with no chance to relax or unwind the whole time."
                "There's going to be plenty of time to sleep once I'm home and in bed."
                "And I'm not going to miss out on the chance to spend some quality time with Alexis either!"
                scene bg cinemaroom at dark with vpunch
                "I find my head drooping onto my shoulder, manage to jerk myself awake with a slight grunt of confusion."
                mike.say "Huh...wha..."
                show alexis surprised at center, zoomAt(1.5, (640, 1140)), vshake
                "The noise seems to make Alexis jump, as if she wasn't expecting it."
                show alexis confused
                "She whispers urgently to me a moment later."
                alexis.say "God's sake, [hero.name]!"
                alexis.say "You almost scared the life out of me."
                show alexis normal
                "I can't help getting the odd feeling that she was in the act of doing something or other."
                "Though as I'm still a little groggy from almost nodding off, I just write it off as my being confused."
                "In the end, I manage to keep from actually falling fully asleep before the end credits roll."
                "Hell, I even get to see the little scene they put in afterwards too, which is a bonus."
                "I still need to have Alexis fill me in on some of the major plot details."
                "But for some reason she's quite vague, as though she was distracted too."
                "Who knows - maybe she's just as tired as me, just better at hiding it?"
                $ game.active_date.score += 10
            "Don't resist":
                "All too soon I feel myself sinking into that weird place between sleep and waking."
                "That place where nothing seems to make sense and thoughts stretch into strange shapes without any effort whatsoever."
                "I don't know how long I'm actually asleep, but I don't get an elbow in the ribs, and so must not have been snoring."
                scene bg cinemaroom at dark with wipeup
                "And so when I finally wake up, I have literally no idea where I am for a good few minutes."
                "But slowly it starts to come back to me that I'm sitting in the cinema, with Alexis by my side."
                "Suddenly realising that I probably need to make an urgent apology to my date, I turn to look in her direction."
                "At first I think that she must have got up and slipped out to the bathroom or to refill her drink."
                "As when I gaze over, I can't see her in the seat at all."
                "But then I see something moving in the seat, and realise that she is one row further down the room."
                "The reason that I couldn't see her at first was because she's hunched over for some unknown reason."
                "There's an odd sound coming from down there too."
                "And at first I think she must be in the act of retching or actually throwing up, head between her knees."
                "Concerned for her well-being, I lean over a little to see what's going on."
                show alexis movie bj with fade
                "It's then that I see the guy sitting on the other side of her has his flies undone."
                "And worse, Alexis' head isn't between her knees at all."
                "It's actually buried in the lap of a complete stranger."
                "I can't believe what I'm seeing - she's giving him a blowjob while sitting right beside me!"
                menu:
                    "Leave":
                        "I know that I should stop her, or at least say something."
                        "But the truth is that the shock I'm feeling seems to put me into a kind of autopilot."
                        "Without uttering a single word, I get up from my seat and walk out to the hall."
                        scene bg cinema with fade
                        "I don't know if Alexis even notices that I'm gone."
                        "As she waited for me to fall asleep before making a move on some other guy, I doubt it."
                        "And whether or not she'll be surprised to find me gone, I have no idea."
                        "So here I am, waiting for the movie to end."
                    "Watch":
                        "All it'd take is for me to say something that one or both of them could hear."
                        "Or a simple tap on the shoulder would break the spell for good."
                        "Though I have no idea what would happen in the seconds that followed..."
                        "But for some reason, I do neither and simply continue to watch."
                        "After the way in which Alexis betrayed me when we were dating as kids, I should be outraged."
                        "And yet I keep on staring at the undeniable evidence that she hasn't changed one bit."
                        "Maybe it's because, before this moment, I'd never seen the evidence with my own eyes?"
                        show alexis movie bj up
                        "But whatever the reason, I can't stop watching in rapt disgust as her head bobs up and down in the guy's lap."
                        "I make sure not to turn my head in their direction, trying to keep from being seen."
                        "Still I can make out the fact that the stranger has his head leaned back, clearly enjoying the treatment."
                        "Why am I watching this?!?"
                        "She's making a fool out of me in public, and I can't tear my eyes away from the very act that's doing it!"
                        show alexis movie bj down
                        "I can feel my breathing becoming heavier as the blowjob becomes more intense."
                        "My heart's pounding in my chest and the blood's pounding in my ears."
                        "Oh god - am I actually getting off on this?"
                        "Is the real reason that I was so destroyed by Alexis' cheating the first time around not because of the infidelity?"
                        "Was it really because of the fact that I couldn't watch as she did so?"
                        "By now, the guy on the other side of Alexis is starting to make a desperately suppressed sound."
                        "At the same time, his hands are clutching at the arms of his seat."
                        show alexis movie bj cum
                        "No doubt he's moments away from cumming, and doing it right inside of her mouth too!"
                        "Before I have time to form another thought, he stiffens and Alexis makes a muffled gagging sound of her own."
                        "I watch out of the corner of my eye and with rapt fascination as she swallows every last drop of his cum."
                        "And then, without a single word passing between them, it's all over."
                        scene bg cinemaroom
                        show alexis blush at center, zoomAt(1.5, (640, 1140))
                        with fade
                        "Alexis sits up and come back to her seat while the guy begins to fasten up his flies."
                        "I hastily put my head back on my shoulder and close my eyes, feigning sleep."
                        alexis.say "Hey, sleepy-head!"
                        mike.say "Huh...what the hell..."
                        show alexis happy at center, zoomAt(1.0, (640, 1140)), startle
                        "Alexis laughs out loud, apparently buying my efforts to appear asleep."
                        alexis.say "I can't believe it - you slept through the whole film!"
                        mike.say "Wow...I must have been more tired than I thought!"
                        hide alexis
                        show alexis kiss with fade
                        $ alexis.flags.kiss += 1
                        "Still distracted by my own thoughts, I'm taken by surprise when Alexis kisses me without warning."
                        "I return the gesture, almost completely as a reflex action and with no hesitation, despite what I've seen her do."
                        "But then she goes further, sliding her tongue into my mouth and stepping into the kiss with more passion."
                        "At first I barely notice the hints of it still on her tongue even now."
                        "It only becomes apparent to me just what that odd, elusive taste is a couple of moments later."
                        "His cum...that's what it is."
                        "I can taste the last remnants of it on Alexis' tongue as she kisses me!"
                        hide alexis
                        show alexis happy
                        with fade
                        "Alexis jokes about my nodding off as we get up and leave the theatre."
                        "But she never once mentions what she was doing while I was supposedly asleep."
                        "I see her exchange a furtive glance with the guy himself as we pass in the lobby."
                        "But she seems happy to think that she's gotten clean away with it."
                        "And if I'm honest, that's not even what's troubling me the most right now."
                        "I'm more concerned by the fact that I just sat there and watched!"
                if alexis.flags.story == 1:
                    $ game.active_date.score += 10
                else:
                    $ game.active_date.score += 5
    $ hero.replace_activity()
    return


label alexis_repeatable_beach_event:
    show alexis happy
    "It seemed like a good idea at the time, when I remembered just how often Alexis and I used to hang-out at the beach back in high-school."
    "So much so, in fact, that going back there now seemed to be a complete no-brainer."
    if alexis.flags.story == 2:
        if game.room == "date_nudistbeach":
            show alexis happy naked at center with ease
        else:
            show alexis happy swimsuit at center with ease
        "But as we walk across the sand, looking for a spot to claim, it doesn't take long for me to see the essential flaw in my plan."
        "I've been wandering in Alexis' wake since we got out of the car, totally distracted by the sight of her in a swimsuit."
        "And it's only when we actually stop and I glance around that I begin to see I'm not the only guy that she's having that effect on."
        "Even though there's an entire beach that's almost full of scantily-clad women to ogle, all eyes seem to be on Alexis right now."
        "I'm not sure whether or not she's actually noticed the attention that she's getting from everyone else on the sand."
        "And for a moment, I wonder if I should say something to her, just in case she realises and it gets awkward."
        "But then I see her bend down to spread her towel out on the ground, visibly shaking her ass as she does so."
        "My suspicions are all but confirmed a moment later, when she reclines upon the towel and pulls out her sun-cream."
        "Alexis is one hundred percent aware of the attention that she's getting."
        "What's more, she's revelling in it too!"
        "I sit down beside her, trying to decide who's bothering me more."
        "Is it the dozens of guys that are currently checking out my date?"
        "Or Alexis herself, who seems to be loving every moment of it?"
        show alexis talkative
        alexis.say "[hero.name], would you be a darling?"
        show alexis normal
        mike.say "Huh...what was that?"
        "If Alexis is aware of just what's making me so distracted and edgy, she chooses to ignore it completely."
        "Instead, she extends the hand holding the sun-cream, giving me a cheeky smile as she does so."
        show alexis talkative
        alexis.say "Would you mind doing the honours?"
        show alexis normal
        mike.say "Oh...yeah, sure thing, Alexis!"
        "Of course I feel like a chump for just jumping to attention and following her every whim."
        "But seriously, what am I going to do about it?"
        "I can't make a scene in front of all these people and show her just how paranoid and insecure she makes me feel."
        "And what kind of message would that send to all of the other guys checking her out too?"
        hide alexis
        if game.room == "date_nudistbeach":
            show beach cream alexis naked with fade
        else:
            show beach cream alexis swimsuit with fade
        "So I obligingly squeeze the cream onto my hands and start to work it into Alexis' shoulders and back."
        "She lies flat on her belly while I do this, making appreciative noises as I progress down her spine and toward her waist."
        "I'd thought that my mind would be churning over the way Alexis flaunts herself, ruminating on the way she's silently showing me up."
        "But I soon find that I'm enjoying myself far more than I would have thought possible."
        "Alexis has such a fantastic body that being able to feel and caress it in such a manner is a real turn-on."
        "My worries melt away as I trace the shape of her lines and curves, making sure to cover every inch of her exposed flesh as I do so."
        "The sounds that she's now making are almost as arousing as the feel of her slick skin too."
        "Every sigh and moan that she lets slip makes me lick my lips and stiffen below the waist."
        "By now, I can't help shaking my head at just how paranoid I was letting myself become."
        "Sure, there might be anything up to a hundred guys, all of them staring at Alexis and thinking about what they'd like to do to her."
        "But I'm the only one that's actually getting to put his hands on her in and enjoy the experience."
        "I'd bet that every one of them is pretty jealous of me right now!"
        "How have I let myself forget that fact?"
        "Of course people are going to stare at Alexis - how could they not?"
        "But she's here with me, and looking isn't touching, is it?"
        show beach cream alexis nomc
        "I keep that in mind for the rest of the time that we spend at the beach."
        "And it means that I hardly notice the attention that she receives as we walk along the beach or play in the crashing waves."
        hide beach cream
        if game.room == "date_nudistbeach":
            show alexis flirt naked
        else:
            show alexis flirt swimsuit
        with fade
        "All the time, while it's clear that Alexis is still enjoying the feeling of having so many eyes upon her, she never once leaves my side."
        "I guess that's one of the things that I have to come to terms with myself, if I want to keep a hold of her this time around."
        "I need to stop thinking about other people noticing her, and make sure that enough of Alexis' attention is focused on me instead."
        $ game.active_date.score += 10
    else:
        if game.room == "date_nudistbeach":
            show alexis happy naked at center with ease
        else:
            show alexis happy swimsuit at center with ease
        "But I'm already starting to wonder if coming down here today was such a good idea after all."
        "The sun is just scorching, meaning that the sand is likewise almost too hot to walk on."
        "All around us, I can see people either trying to get out of the sun or else frying themselves under its relentless heat."
        mike.say "Erm, Alexis...you don't think it's too hot to be out here, do you?"
        "Alexis responds to this by raising her eyebrows and shaking her head in disbelief."
        show alexis talkative
        alexis.say "Really, [hero.name]?!?"
        alexis.say "Isn't that what sun-screen is for?"
        show alexis annoyed
        mike.say "I know, but..."
        show alexis whining
        alexis.say "Oh, don't be such a stick-in-the-mud about it."
        show alexis talkative
        alexis.say "If you burst into flames, just go jump in the sea!"
        show alexis normal
        "And with that, she puts on her sunglasses and lies down to take advantage of the sun's rays."
        hide alexis
        if game.room == "date_nudistbeach":
            show beach cream alexis naked nomc with fade
        else:
            show beach cream alexis swimsuit nomc with fade
        "I mutter something rather passive aggressive under my breath and start to plaster myself in sun-cream."
        "Alexis makes no sign that she's heard me, and for all I can tell she could already be asleep at my side."
        "I lie down too, only meaning to close my eyes for a couple of moments."
        "But the next thing that I know, I'm roused by something brushing against my side."
        mike.say "Huh...what's..."
        alexis.say "Don't wake up on my account."
        mike.say "Oh, Alexis..."
        mike.say "What are you getting up for?"
        mike.say "You only just laid down!"
        "Alexis chuckles at this and shakes her head once again."
        alexis.say "It's been more than an hour, [hero.name]!"
        alexis.say "You must have fallen asleep almost as soon as you shut your eyes."
        "I grab my phone, checking the time and finding that she's not pulling my leg."
        hide beach cream
        if game.room == "date_nudistbeach":
            show alexis naked talkative
        else:
            show alexis swimsuit talkative
        with fade
        alexis.say "Anyway, I'm thirsty."
        alexis.say "So I'm going to grab some water from the kiosk over by the dunes."
        alexis.say "You want anything?"
        show alexis normal
        mike.say "Sure, grab me one too."
        hide alexis with easeoutright
        "I watch Alexis walk a little way off, and then lay back down again."
        "The kiosk that she mentioned isn't too far, so she should be back in a couple of minutes at the most."
        "And so by the time she's been gone a good fifteen minutes, I'm beginning to get worried."
        menu:
            "Wait for her":
                "I can guess what's she doing right now. And I don't really want to confirm my suspicion."
                "So I just close my eyes and resign myself to waiting until she comes back in her own good time."
                if game.room == "date_nudistbeach":
                    show alexis naked blush with easeinright
                else:
                    show alexis swimsuit blush with easeinright
                "When she finally does so, I deliberately ignore the fact she's been gone almost an hour."
                mike.say "I was starting to worry there a little, Alexis."
                mike.say "Any longer and I'd have filed a missing person's report!"
                "Alexis looks this way and that, as if she's suddenly worried about something."
                show alexis annoyed
                "Which is odd behaviour for someone that just went to buy water."
                "But I've already promised myself that I won't read too much into her actions, so I ignore it."
                mike.say "I guess there was a queue?"
                mike.say "Weather like this, everyone'll be wanting some, right?"
                show alexis blush
                "For some reason, Alexis reddens at this and begins to shake her head."
                mike.say "Just joking - it's okay!"
                "Alexis nods and sinks down onto the towel beside me."
                $ game.active_date.score += 10
            "Look for her":
                "There's no way that it should be taking her this long to grab a bottle of water and get back here."
                "She probably found something else to keep her busy."
                "I stand up, glancing around."
                "But there's still no sign of her, and so I set off in the direction of the kiosk."
                "It doesn't take me long to arrive at my destination, or to see that Alexis isn't here either."
                "I wonder if she's walked on to another kiosk to get water instead."
                "The quickest way I know to reach the next one is the path that runs along the back of the beach-huts and in front of the dunes."
                "So I make straight for it. I've not gone far when I hear the sound of voices a little way off of the path."
                "Thinking that it might be Alexis, or at least someone that's seen her pass this way, I head in their general direction."
                "But as I get closer, my pace slows and I start to move as quietly as I can."
                "One reason for this is that I soon pick out two of the voices as male and pretty surly in tone."
                "The other is that I recognise the second as female, and more importantly as belonging to Alexis herself."
                "I creep closer and strain to see what's happening."
                "What I do see, in fact, doesn't really surprises me."
                show alexis beach threesome mike with fade
                "She's bent over in between the two guys I could hear just now, swimsuit around her ankles and breasts exposed."
                "The guys, who look like a couple of typical gang-bangers, both have their cocks out and are clearly rather excited."
                "Alexis licks her lips in anticipation as one cock looms towards her mouth and the other her ass."
                menu:
                    "Go back on the beach":
                        "I turn my head away the moment before the real action begins, and try to blot out the sounds that follow a moment later."
                        hide alexis beach threesome
                        show bg beach with fade
                        "Taking advantage of the fact that I'd been able to sneak up on the unpleasant scene unnoticed, I slip away in the same fashion."
                        "I don't think the full implications of what I've just seen becomes apparent until I'm back on the sand and gathering up my things."
                        "Alexis just wandered off for a bottle of water and what?"
                        "Just happened to come across a couple of dodgy-looking guys that she couldn't resist having a threesome with?"
                        "Did she plan this from the start, or was it a spur-of-the-moment kind of thing?"
                        "Anyway, I walk back to the beach and lie down on the towel."
                        "So I just close my eyes and resign myself to waiting until she comes back in her own good time."
                    "Watch":
                        "I know that I should say something, break this up before it goes too much further."
                        "But for all the horror that the sight of it inspires in me, there's an equal amount of fascination too."
                        "Maybe it's because of all the time that my mind's spent dwelling on the thought of Alexis betraying me."
                        show alexis beach threesome mike suck normal anal
                        "Or maybe I'm just a far bigger pervert than I ever imagined possible."
                        "Either way, once I pause long enough to be sure that she has a cock in her mouth and her ass, I can't keep from watching."
                        "One thing I know for certain is that it can't be lack of experience that makes me stay still and silent."
                        "I've been in the same position as each of those guys in the past, and I know just how good it feels."
                        show alexis beach threesome mike lick
                        "But somehow the sight of them basically turning Alexis into a human spit-roast between is something I can't tear my eyes away from."
                        show alexis beach threesome suck at stepback(speed=0.1, h=-10, v=-20)
                        "Neither of them is gentle, the one with his cock in her mouth thrusting suddenly and the other pushing mercilessly into her ass."
                        "And yet none of this rough treatment at both ends of her body does anything to lessen Alexis' pleasure."
                        "Indeed, she seems to positively revel in the way she's being manhandled."
                        show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                        "The more the one cock is forced into her mouth and the other between her buttocks, the more she seems to like it."
                        "When she isn't gagging, Alexis makes low, muffled moaning sounds around the cock she's sucking."
                        show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                        "Likewise, her body trembles and quivers each time the other man rams his hips against her buttocks."
                        "I can feel my mouth going dry at the same time as my cock is getting ever harder."
                        show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                        "I slip a hand into my shorts and begin to stroke myself as Alexis takes ever more from each man."
                        "The heat of the day and the way she's being used means that she's almost dripping with sweat by now."
                        show alexis beach threesome at stepback(speed=0.1, h=-10, v=-20)
                        "Every motion of her head and slapping of her ass sends her pendulous breasts swaying in time."
                        "And in that moment, I see beads of sweat running down them and collecting to drip from her painfully erect nipples."
                        show alexis beach threesome mike surprised cum with hpunch
                        "Then, without warning, they both cum within mere seconds of one another."
                        "Neither spares as much as a second thought for Alexis herself, simply using her as a vessel for what follows after."
                        show alexis beach threesome ahegao
                        "She chokes on the cum being spurted down her throat in one second."
                        "And then her body jerks as the muscles of her ass convulse from the same being done to it."
                        show alexis beach threesome out
                        "I see Alexis' legs buckle and then collapse beneath her as they pull out a moment later."
                        "Having got their use out of her, neither of the men as much as pauses to say a word to Alexis."
                        show alexis beach threesome -cum
                        "Instead, they seem to be amused by the sight of her as she lays there before them."
                        "Slipping their cocks back into their shorts, they wander off, laughing to each other as they go."
                        "Used, abused and then abandoned, Alexis is left in a helpless, writhing mess."
                        "Slick with a mixture of sweat and cum, she coughs and hacks until she spits out the last of what she was made to swallow."
                        "In all my life, I don't think I've ever seen a woman so utterly degraded as she is right now."
                        "And it's only when I feel myself cumming too that I realise I've been gratifying myself to the same sight the whole time."
                        hide alexis with fade
                        "Unable to make sense of the conflicting emotions that this inspires in me, I turn and hurry back to the sand."
                        "All the way I feel sure that all it'll take is one look at me for everyone to know what just took place back there."
                        "But of course, no one suspects a thing."
                        "I lay myself back down on the towel and try to regain control, waiting for Alexis to show herself again."
                        if game.room == "date_nudistbeach":
                            show alexis blush naked with easeinright
                        else:
                            show alexis blush swimsuit with easeinright
                        "When she finally does come back, she's done a remarkable job of cleaning herself up."
                        "And from the expression on her face, I could almost believe nothing out of the ordinary took place while she was gone."
                        "If, that is, I hadn't seen it with my own eyes..."
                        show alexis talkative
                        alexis.say "You wouldn't believe the time I've had!"
                        show alexis normal
                        mike.say "Oh, really?"
                        "I glance nonchalantly at my phone and then adopt an expression of feigned surprise."
                        mike.say "Wow, Alexis - you've been gone for ages!"
                        show alexis whining
                        alexis.say "Like I don't know that!"
                        alexis.say "The place was out of water, and so I had to walk all the way to the next kiosk."
                        alexis.say "Which took all this time..."
                        show alexis annoyed
                        mike.say "You do look pretty sweaty, Alexis!"
                        mike.say "And were they out of water too?"
                        "At the reference to the suspiciously absent bottle of water she supposedly set out for, Alexis looks more than a little furtive."
                        show alexis whining
                        alexis.say "I...ah...had to drink it on the way back...sorry!"
                        show alexis sad
                        mike.say "It's okay, Alexis - you look like you needed it more than I did!"
                        "And with that, I let the matter drop."
                        "But the mere thought of Alexis, slick and crawling around in humiliation, is enough to get me hard for days afterwards."
                if alexis.flags.story == 1:
                    $ game.active_date.score += 10
                else:
                    $ game.active_date.score += 5
    return

label alexis_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    if kylie.yandere >= 25 and not kylie.flags.arrest and ("kylie_voyeur" not in DONE or kylie.flags.canwatch) and randint(1, 5) == 1:
        call kylie_voyeur from _call_kylie_voyeur
        return

    $ game.room = "bedroom1"
    scene bg bedroom1
    show alexis


    call alexis_fuck_date_intro_male (location) from _call_alexis_fuck_date_intro_male


    call alexis_dick_reactions from _call_alexis_dick_reactions_2


    call alexis_fuck_date_foreplay_male from _call_alexis_fuck_date_foreplay_male




    call alexis_fuck_date_choices_male from _call_alexis_fuck_date_choices_male


    call handle_npc_leaving (alexis, _return) from _call_handle_npc_leaving_1
    if _return:
        return


    hide alexis
    call alexis_sleep_date_fuck (location) from _call_alexis_sleep_date_fuck
    return

label alexis_fuck_date_intro_male(location="hero"):
    if not alexis.sexperience >= 2:
        "Reconnecting with Alexis has been an odd kind of experience for me, one that I'd imagined many times in the past."
        "But the most surprising thing is just how little I seem to be able to remember of the girl that I used to know."
        "As well as how different the woman she's become is from the small details that I'm able to recall from back then."
        "It's like discovering new things about someone I thought I knew and meeting an entirely different person all at the same time."
        "And even as I was getting to know Alexis for the second time around and we were feeling each other out, I was always aware of that big question hanging over me."
        "What, exactly, would it be like and probably more importantly, how would I feel the first time we had sex?"
        "Well, let's be honest, it was IF we ended up having sex again."
        "I'm not that cocksure and confident!"
        "But there seems to have been more ups than downs since we started our tentative second attempt at something resembling a relationship."
        "And I don't know if it's the thrill of bedding a former lover on Alexis's part, or that she's mad keen on the guy that I've turned out to be."
        "Either way, we're about to take that next big step and follow up a pleasant date with, I hope, some equally pleasant adult time together."
        "I can also assure you that one of the major things that I don't have an accurate recollection of is just what Alexis looks like naked."
        "This means that I'm totally in the dark as we shut the door to my bedroom behind us and she starts to strip me off with some serious gusto."
        "I return the favour where and when I can, trying to pull off a piece of clothing from what Alexis is wearing."
        "But she always seems to be able to just about twist and turn enough to elude me."
        "Pretty soon I'm totally naked, and she's still looking like she did when we walked in off of the street."
        "Before I can get mad at this blatantly unfair situation, Alexis shoves me in the chest with the flat of her hand."
        call alexis_dick_reactions from _call_alexis_dick_reactions
        "The blow isn't enough to hurt me, but it's more than enough to send me tumbling backwards and onto the unmade bed."
    else:
        "Alexis makes no bones about just how she wants to end the night, leading me straight to the bed, stripping off her clothes as she does so."
        "I'm not going to make the mistake of saying this feels like remembering how to ride a bike, for obvious reasons."
        "But all the same, there's something deeply reassuring about the fact that we've been able to rekindle what we once had in this way."
        "It's almost as though Alexis and I are beyond the need for words in a situation like this, knowing instinctively what each other wants and needs."
        "Then again, when she climbs slowly onto the bed, shaking her arse at me and beckoning with a curled finger, it's not too hard to read her desires!"
        "I know a thoroughly modern guy like me is supposed to be all about the tenderness and the foreplay."
        "But right now, the thought of what's hidden between Alexis's buttocks is crowding all of that right out of my head."
        "And the fact that my cock's already standing to attention means that this is no time to get all woke and fluffy!"
    "I scramble up into a sitting position, about to object..."
    "And it's then that I see the absolutely filthy smile that's spreading across Alexis's face."
    "Still holding my gaze, she begins to pull her top upwards, revealing ever more of her smooth, curving stomach."
    "Well now I feel like a fool - I was about to complain about what turned out to be a private strip-tease, right here in my bedroom!"
    show alexis wink topless with dissolve
    "Alexis winks as quick as a flash before she whips her top off, letting me know that I was right to keep my mouth shut and let her get on with it."
    "As she pulls them free of her top, I see the heavy shape of her breasts moving in sympathy with her arms."
    "They're something that I definitely don't remember, so full and appealing to the eye that I'm sure I simply couldn't have forgotten them."
    "Seeing my eyes widen at the sight of them, Alexis shakes her head in amusement and reaches behind her back to unhook her bra."
    "I swear that they bounce, first down and then back up again as they come free and succumb to gravity."
    "Next she inches down her pants and knickers all at the same time, first one side and then the other until they're bunched up around her ankles."
    "All I can say is that the shape of her legs are well in keeping with her stunning chest."
    show alexis naked blush with dissolve
    "And her neatly-shaved pussy makes me want to bite my lip in spite of myself."
    alexis.say "I know that you like what you see, [hero.name]..."
    alexis.say "You didn't have to say a word - your little friend went and told on you already!"
    "She comes closer as she says this, casting her gaze down towards my dick, which only now do I see is already painfully erect."
    alexis.say "Aww, look...he's standing to attention for me."
    return

label alexis_fuck_date_foreplay_male:
    menu:
        "Have her suck you off" if alexis.sub >= 25:
            call alexis_fuck_date_blowjob from _call_alexis_fuck_date_blowjob
        "Give her some oral attention" if hero.sexperience >= 30:
            call alexis_fuck_date_cunnilingus from _call_alexis_fuck_date_cunnilingus
        "Fuck her":
            pass
    call stop_all_sfx from _call_stop_all_sfx_2

    return _return

label alexis_fuck_date_choices_male:
    menu:
        "Cowgirl":
            call alexis_fuck_date_cowgirl (0) from _call_alexis_fuck_date_cowgirl
        "Missionary" if hero.sexperience >= 5:
            call alexis_fuck_date_missionary (5) from _call_alexis_fuck_date_missionary
        "Doggy" if hero.sexperience >= 10:
            call alexis_fuck_date_doggy (10) from _call_alexis_fuck_date_doggy
        "Reverse Cowgirl" if hero.sexperience >= 15:
            call alexis_fuck_date_reverse (15) from _call_alexis_fuck_date_reverse
    call stop_all_sfx from _call_stop_all_sfx_3

    return _return

label alexis_fuck_date_blowjob:
    mike.say "Whoa..."
    mike.say "Alexis - what are you..."
    alexis.say "What does it look like, [hero.name]?"
    alexis.say "I've been wanting this all night!"
    "I open my mouth again, meaning to say protest."
    "But then I stop myself before I begin to form the words."
    "What in the hell am I doing?"
    "Why would I stop Alexis from having her way with me?!?"
    "I make to sit up, but Alexis shoves me back down the moment I do so."
    mike.say "Wha..."
    alexis.say "Just lie down and shut up."
    alexis.say "I'll take it from here!"
    "I stare at Alexis in stunned silence for a moment."
    "And then I do exactly as I'm told."
    "When a girl wants you this bad, why fight it?"
    "Now that she's the one in charge, Alexis doesn't waste another moment."
    show alexis bj with fade
    "She spreads my legs and lowers herself between them."
    "Soon she's laid on her belly, eyes level with my own."
    show alexis bj chub
    "And once there, she takes a hold of my already stiff cock."
    "All I can do is lie back and watch, panting at the feel of it."
    "Alexis stares at my cock hungrily, already stroking the shaft."
    show alexis bj pinch at startle(0.05,-10)
    "With her other hand she reaches out and tweaks one of my nipples."
    mike.say "Ouch..."
    mike.say "Hey, what was that for?!?"
    "Alexis let's out a wicked giggle."
    alexis.say "Oh, just checking you're awake!"
    "And with that, she gives my cock a hard squeeze."
    "But before I can object to such rough treatment, Alexis kicks it up a notch."
    show alexis bj speed at startle(0.05,-10)
    "Her hand begins to stroke the shaft up and down."
    "And at the same moment she licks the tip, tickling it with her tongue."
    "The protest dies in my throat, replaced with a moan."
    "I see Alexis smile at this, noting the reaction she's getting."
    show alexis bj blowjob
    "A reaction which only becomes more intense as she parts her lips."
    "I watch my cock disappear into Alexis's mouth."
    "Then I feel the sensation of her tongue as it goes to work."
    "Alexis still has the shaft in her hand, working it the whole time."
    "And the firm grip contrasts wildly with the softness at the other end."
    "Most of the time I can't actually tell what's caressing the tip."
    "Lips, teeth and tongue all seem to work together in perfect harmony."
    show alexis bj close
    "And as Alexis bobs her head up and down, I struggle to hold mine up."
    "I'm almost gasping for breath by now, heart pounding in my chest."
    "But Alexis shows no sign of tiring, nor slowing down."
    "My cock is going so deep with each downward motion."
    "It must be reaching all the way into her throat!"
    "Just as I begin to wonder how deep it can go, Alexis changes gear again."
    "I feel her cup my balls in the palm of her free hand."
    "Then she squeezes them tightly and without a hint of mercy."
    "I hear myself cry out, rather than know I'm doing it."
    "And my whole body seems to react to the sensation all at once."
    "But the only thing I can be sure of in that moment is that I'm about to cum!"
    menu:
        "Cum on her face":
            "With no more than a second to spare, I reach down between my thighs."
            "One hand on each side of Alexis's head, I pull her upwards."
            "Luckily for me she seems to have the same idea, and doesn't resist."
            show alexis bj hard
            "My cock pops out of her mouth with mere fractions of a second to spare."
            show alexis bj cumshot with vpunch
            "And Alexis gasps as she takes it straight in the face."
            show alexis bj cum onface with vpunch
            "Cum hits her between the eyes, making her blink."
            show alexis bj -speed -cumshot with vpunch
            "Some spreads up her forehead, but most travels south."
            "It dribbles down her nose and cheeks, cling to her hair too."
            "But none of this seems to dampen Alexis's spirits in the slightest."
            show alexis bj open
            "Instead she smiles up at me, still panting from her efforts."
            "And when the cum reaches her lips, she laps at it with her tongue."
            "The look of satisfaction on her face telling that's what she was hungry for all along."
        "Cum in her mouth":
            show mouth_insert alexis zorder 1 at zoomAt(1, (20, 180))
            "I know just how hungry Alexis seems to be right now."
            "And so I make no effort to move a muscle."
            "Instead I just lie back and let nature take it's course."
            show mouth_insert alexis cum
            show alexis bj -speed cum inmouth
            with vpunch
            "A moment later, I shoot my load straight into her mouth."
            with vpunch
            "Just as I thought, Alexis doesn't miss a beat."
            with vpunch
            "Instead she hungrily begins to swallow as fast as she can."
            "Alexis never even stops to gasp for breath as she does so."
            "And she never spills as much as a drop either."
            show mouth_insert alexis -cum
            show alexis bj -cum -inmouth hard open
            "Only when I'm totally spent does she release my cock."
            "And then she finally lets out a sigh of sheer exhaustion."
            "But I can see from the look in her eyes that she's finally sated."
            "Alexis smiles up at me, exhausted by her efforts."
            "It's plain to read the emotions on her face."
            "And they tell me that she got what she was hungry for all along."
            hide mouth_insert alexis
    return

label alexis_fuck_date_cunnilingus:
    mike.say "Ah..."
    mike.say "I've been waiting for this all night!"
    mike.say "I just knew you were up for it too, Alexis."
    mike.say "You had this look in your eye..."
    "I stop mid sentence, as Alexis claps her hand over my mouth."
    "Once she's silenced me, she looks me straight in the eye."
    alexis.say "Sometimes you talk too much, [hero.name]."
    alexis.say "From now on, I want you to shut up, okay?"
    alexis.say "Just shut up and use your mouth for something else!"
    "I nod eagerly, which seems to be enough to make Alexis remove her hand."
    "But then I catch myself opening my mouth without thinking."
    alexis.say "Hey - what did I just tell you?!?"
    "In response, I shut my mouth and nod again."
    "She looks at me with amusement in her eyes."
    alexis.say "Don't worry, [hero.name]."
    alexis.say "Your mouth's going to have all the work it can handle soon enough!"
    show alexis lick with fade
    "She lays me down on my back and then straddles my chest."
    "Her pussy is no more than an inch from my face right now."
    "And I can already smell the alluring scent of it too!"
    "Alexis looks down at me, a superior smile spreading across her face."
    "She points to the point between her legs, as if there's any need for it."
    alexis.say "There you go, [hero.name]."
    alexis.say "There's something for that big mouth of yours to do!"
    "And with that, she surprises me by pushing her pussy into my face!"
    "For a moment I'm caught off-guard, almost smothered."
    "But then I shake off the feeling and remember what's going on."
    "Alexis's pussy is right there, front and centre."
    "It's all I can see and all that I can smell."
    "And it's a thing of beauty!"
    "I reach up, putting my arms under Alexis's legs."
    show alexis lick spread pleasure
    "My fingers begin to stroke and caress her lips."
    "Alexis moans softly as I start to touch her, letting me know how much she wants this."
    show alexis lick miketongue
    "And when I push my tongue into the gap that I've created, her moans become all the more intense."
    "It's not like I need any more encouragement to continue."
    "The taste of her on my tongue is incredible, almost impossible to describe."
    "Instinctively, I push it ever deeper, probing into her pussy."
    "Everything else fades into the background as I focus on the task at hand."
    "All that matters to me right now is making sure that Alexis has a good time."
    "And in order to ensure that, I listen carefully to the sounds she makes."
    "Each and every time something I do is followed by an appreciative moan, I take note."
    "And then I either repeat the same action or redouble it."
    "It doesn't take long for Alexis to become helpless under the attention of my tongue."
    "By now she's so wet and slick that the juices are flowing freely out of her."
    "I can actually feel them running down and over my face the whole time!"
    "But it's not something that I'm going to let stop me."
    "I push right on, my tongue now as far inside of Alexis as possible."
    "My fingers are working around the edges of her pussy too."
    "And they help to lighten the load on my tongue."
    show alexis lick ahegao
    "In the end, I'm so wrapped up in what I'm doing that I don't notice Alexis cumming."
    "The only warning I get is the sensation of her pressing down harder still."
    "It's all I can do to keep on breathing as she pins my head with her thighs!"
    show alexis lick squirt
    "Then she takes me completely by surprise, shooting her juices into my face!"
    "And she keeps on squeezing the whole time that her orgasm lasts too."
    show alexis -spread -miketongue -squirt pleasure mikewet
    "Finally I feel the muscles of her legs loosen their grip on me."
    "At the same time, Alexis all but collapses into a heap."
    "She lands to one side of me, gasping and helpless."
    "The only movements she makes come when the aftershocks shake her limp body."
    return

label alexis_fuck_date_reverse(sexperience_min):
    "Once undressed, we almost collapse onto the bed."
    hide alexis
    show alexis reverse out with fade
    "I land on my back with Alexis atop me."
    "She eyes my now painfully stiff cock and makes a grab for it."
    "But I catch her wrist before she can claim her prize."
    "Alexis glances back at me, surprised that I stopped her."
    mike.say "Not so fast, Alexis!"
    mike.say "I'm the one guessing what you want - remember?"
    "Alexis looks annoyed for a moment, but then nods in agreement."
    "Sensing the need to keep her sweet, I make my next move quickly."
    "I guide Alexis to straddle my thighs, her back to me as she does so."
    "Now I have her right where I want her, within my grasp and staring down at my cock."
    "I can even hear her breathing become faster as she waits to see what I'll do next."
    "With my hands firmly holding her haunches, I make Alexis raise herself up."
    "Not far, just enough for her to be hovering over the head of my cock."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and alexis.sub >= 50:
            "And then I pull her down, suddenly and without warning."
            "The first thing that Alexis knows about my intentions comes a second later."
            "Which is when she feels my cock push between her buttocks and into her ass."
            show alexis reverse eyes_surprised mouth_scream
            alexis.say "Whoa!"
            alexis.say "You think..."
            alexis.say "You think I want that?!?"
            show alexis reverse mouth_hurt
            "I don't pause to offer an answer in the form of words."
            "Instead I pull Alexis down for a second time."
            "And on this occasion, it's enough to get maybe an inch inside."
            "She moans as the muscles of her backside clench and squeeze in protest."
            "But one more good thrust is all it takes, and her body surrenders to me."
            show alexis reverse anal at startle(0.05,-10)
            "Alexis begins to make small sounds of pleasure as she sinks further down."
            "So that by the time I'm as deep as I can go, her resistance has melted away."
            show alexis reverse mouth_pleasure
            alexis.say "Oh..."
            show alexis reverse mouth_scream
            alexis.say "I...I do..."
            alexis.say "I do want it!"
            show alexis reverse mouth_hurt
            "I know Alexis can't see my face, but I treat myself to a smile all the same."
            "The feeling of being inside her ass is incredible all on its own."
            "But seeing her come round to it like that is almost as much of a thrill."
            show alexis reverse at startle(0.05,-10)
            "I start to move beneath her, slowly building my speed as I go."
            "The urge is to pound her as hard as possible."
            "But that would ruin the groundwork I've already laid down."
            show alexis reverse at startle(0.05,-10)
            "And so I keep a close eye on how Alexis wriggles and writhes above me."
            show alexis reverse at startle(0.05,-10)
            "When I'm sure that she can take it, I kick it up a notch."
            show alexis reverse at startle(0.05,-10)
            "Even going slowly, she's soon riding me like a bucking horse."
            "I can hear the sound of her buttocks slapping against my thighs."
            show alexis reverse at startle(0.05,-10)
            "And louder still is the sound of Alexis panting in sheer delight."
            "All the while the muscles of her ass are squeezing me like a fist."
            show alexis reverse at startle(0.05,-10)
            "At any moment I feel like all it needs is one harder clench from Alexis."
            "Just one squeeze that's more intense than the last."
            show alexis reverse at startle(0.05,-10)
            "And when it finally happens, I know I'm about to cum!"
            call cum_reaction (alexis, 'anal', sexperience_min) from _call_cum_reaction_9
            if _return == "anal_inside":
                "I'm so deep into her by now and she's holding onto me so tightly."
                "Both of those things make it seem natural to keep on going to the end."
                show alexis reverse mouth_ahegao with vpunch
                "And so when the moment arrives, I shoot my load straight into Alexis."
                show alexis reverse cum with vpunch
                "She seems unprepared for the intensity of the sensation that hits her."
                with vpunch
                "I see Alexis toss her head this way and that, crying out as I fill her."
                "And then, when it's all over, she slides off of me and onto the mattress."
            elif _return == "anal_outside":
                show alexis reverse out
                show chest_insert alexis zorder 1 at zoomAt(1, (860, 80))
                show belly_insert alexis zorder 2 at zoomAt(1, (20, 280))
                "With the very last of my strength, I lift Alexis off of my cock."
                "She wails in surprise at the sensation of it being dragged out of her."
                show chest_insert alexis cum
                show belly_insert alexis cum
                show alexis reverse mouth_ahegao cum
                with vpunch
                "And then she wails all over again as I shoot my load on her chest."
                with vpunch
                "Alexis moans and massages her breasts as it begins to run down to her belly."
                with vpunch
                "But without the support of my cock inside her, she soon collapses onto the mattress."
                "She lies there, panting and trying to catch her breath as my cum cools on her skin."
                hide chest_insert
                hide belly_insert
            $ alexis.flags.anal += 1
        "Fuck her pussy":
            "I tease Alexis a little to begin with, just to see what her reaction will be."
            "Stroking the head of my cock against the lips of her pussy, I pretend to pull her downwards."
            "She gasps in anticipation, but then sighs with frustration as she's denied at the last."
            call check_condom_usage (alexis, 180) from _call_check_condom_usage_5
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show alexis reverse condom
            "I tease Alexis a second time, enjoying the heightened desire in her moans."
            "But then I surprise her by pulling her down and onto my cock."
            "In one smooth motion I'm inside of her and she's sinking onto me."
            show alexis reverse vaginal at startle(0.05,-10)
            mike.say "Did I do it?"
            mike.say "Did I find what you wanted so badly?"
            "At first, all Alexis can do is quiver and make little yelps."
            "It's only when she shivers all over and surrenders that she seems able to talk."
            show alexis reverse mouth_scream at startle(0.05,-10)
            alexis.say "Ah...ah..."
            alexis.say "Y...yes..."
            alexis.say "I want it..."
            alexis.say "Please, give it to me!"
            show alexis reverse eyes_normal
            "Well, when a lady asks for something in such a way, it'd be churlish to refuse her!"
            "I begin to move myself inside of Alexis, slowly but steadily building up speed."
            "But it's not long before I begin to see the effects of what I'm doing."
            "Alexis instantly begins to moan and almost whimper."
            "The sounds that she's making increasing in volume as I go ever faster."
            show alexis reverse eyes_closed at startle(0.05,-10)
            "Before too long, Alexis is riding me for all I'm worth."
            "I hold nothing back now, although I am worried she might fall off!"
            "But she clings to me like a limpet, refusing to loosen her grip."
            show alexis reverse at startle(0.05,-10)
            "Indeed, I can feel Alexis pressing all of her weight down on me now."
            "I know that she's trying as best she can to stay atop me."
            "And yet the same force she's applying makes it more intense for me too!"
            show alexis reverse mouth_pleasure at startle(0.05,-10)
            "I hear myself grunting with the effort that I'm putting into each thrust."
            "All I can think about is the need to keep on going for as long as I can."
            show alexis reverse at startle(0.05,-10)
            "My hands are gripping Alexis's haunches tightly, adding to the sensations as well."
            "The tips of my fingers are pressing into the soft flesh of her thighs."
            show alexis reverse at startle(0.05,-10)
            "I want to keep on going, but I can already feel myself starting to cum."
            call cum_reaction (alexis, 'vaginal', sexperience_min) from _call_cum_reaction_10
            if _return == "vaginal_condom":
                "But the fact that I chose to put on a condom means that's not a problem."
                "All I need to do is keep up the same pace, thrusting into Alexis until the last moment."
                show alexis reverse mouth_ahegao with vpunch
                "She cums just after I do, my own climax pushing her over the edge too."
                show alexis reverse cum with vpunch
                "Alexis throws her head back and squeezes me with her thighs."
                with vpunch
                "And it feels like she's trying to wring the last drops out of me the whole time!"
                "Once she's spent, she slides off, flopping onto the mattress beside me."
            elif _return == "vaginal_outside":
                "Thankfully I have the presence of mind to remember that I went bare-back tonight."
                show alexis reverse out
                "Which means there's just enough time for me to pull out of Alexis before it's too late!"
                "She lets out a cry of surprise as I yank my cock from her pussy."
                if not CONDOM:
                    show chest_insert alexis cum zorder 1 at zoomAt(1, (860, 80))
                    show belly_insert alexis cum zorder 2 at zoomAt(1, (20, 280))
                    show alexis reverse cum
                    with vpunch
                    "And then she follows it with another as I shoot my load up her chest."
                    with vpunch
                    "The cum spatters Alexis's breasts and belly, striping them white."
                    $ alexis.love += 1
                    "She can't help rubbing it into her skin as she caresses her slick breasts."
                    hide chest_insert
                    hide belly_insert
                else:
                    with vpunch
                    "And then she follows it with another as I shoot my load while she caresses her breasts."
            elif _return == "vaginal_inside_pill":
                alexis.say "Let me have it, [hero.name]!"
                alexis.say "Fill me up!"
                "For a moment I think the sex has affected Alexis's brain."
                "But then I remember that she's on the pill right now."
                "All I need to do is keep thrusting into Alexis until the last moment."
                $ alexis.love += 2
                show alexis reverse mouth_ahegao cum with vpunch
                "We both cum a moment later, making Alexis throw her head back and squeeze me with her thighs."
                with vpunch
                "Once she's spent, she slides off, flopping onto the mattress beside me."
            elif _return == "vaginal_inside_pregnant":
                "There's no need to stop what's happening, Alexis and I both know it."
                "She's already visibly pregnant, so no harm can come from me cumming inside her."
                "I keep right on going, thrusting into her until I lose it."
                $ alexis.love += 3
                show alexis reverse mouth_ahegao cum with vpunch
                "She cums a moment later too, pushed over the edge by the sensation."
                with vpunch
                "Alexis almost howls as she squeezes me with her thighs."
                "And then, all at once, she goes limp."
                "She slides off and flops onto the mattress beside me."
            elif _return == "vaginal_inside_happy":
                alexis.say "No..."
                alexis.say "No...don't..."
                alexis.say "Don't stop now..."
                "I'd been all ready to pull out at the last moment, not wanting to cum inside of her."
                "But Alexis throws me with her sudden demand for me to do the opposite."
                "And in that moment, my hesitation gives her what she wants."
                $ alexis.love += 5
                #$ alexis.impregnate()
                show alexis reverse mouth_ahegao cum with vpunch
                "I shoot my load into Alexis as she clings onto me to dear life."
                with vpunch
                "Which leaves me wondering what the hell she's thinking!"
            elif _return == "vaginal_inside_mad":
                alexis.say "Oh shit..."
                alexis.say "[hero.name]..."
                alexis.say "We can't..."
                "Listening to Alexis, I take my mind off of what I'm doing for just a second."
                #$ alexis.impregnate()
                show alexis reverse mouth_ahegao cum with vpunch
                "And that's all it takes for me to lose it inside of her."
                $ alexis.love -= 5
                with vpunch
                "Alexis looks back over her shoulder at me, her mouth dropping open."
                "We stare at each other in shocked silence, suddenly aware of what we've done!"
    return

label alexis_fuck_date_doggy(sexperience_min):
    hide alexis
    show alexis doggy nomc with fade
    "But now that I'm as naked as Alexis and clambering after her onto the bed, a real dilemma presents itself."
    "Taking one buttock firmly in each hand and parting them slightly, I'm presented with the option of two different goals."
    "Each one looks just as inviting as the other, and I just can't seem to feel the pull towards either of them!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and alexis.sub >= 50:
            "I guess that I'm just feeling a little more adventurous than usual, and wanting to see if Alexis is the same way inclined."
            show alexis doggy -nomc
            "That's why I aim my cock at the tight little target of her asshole and begin to push my way inside."
            "My first clue that Alexis was not expecting this in the slightest comes in the form of a sudden squeal of surprise."
            "She makes an instinctive move to crawl away from me, but I counter this by taking hold of her around the waist."
            show alexis doggy anal hurt
            alexis.say "Ah...[hero.name]!"
            alexis.say "What are you doing?!?"
            "I don't give her the luxury of an answer, partly for fear of her begging off and partly because I'm already an inch inside of her."
            "Alexis squeals again as I push in still further and her own muscles begin to help my progress."
            "It feels almost as if her body is betraying her and wanting me in there more than her brain right now."
            alexis.say "[hero.name]..."
            alexis.say "Oh...[hero.name]...you're in my ass!"
            "Her voice melts from a pained cry and into a deeper tone of surrender as she says this."
            "And at the same time I can feel her body relax and begin to shudder as she passes through the pain barrier."
            "I take it slowly now, moving in and out of Alexis in a smooth, firm motion."
            "The sensation of her ass as its muscles squeeze my cock is something else, and I want to savour every moment that I can."
            "Alexis too is succumbing to the experience, looking back over her shoulder at me the whole time."
            alexis.say "Uh...ah...yeah..."
            alexis.say "Please...please fuck my ass!"
            "This is the last thing that she manages to say, before her tongue actually begins to loll out of her open mouth."
            "I watch as Alexis's eyes glaze over and roll up into the back of their sockets."
            "Right before my eyes, I see her turn into a mass of animal instincts and carnal appetites."
            "She loses first the ability to speak and then the means to keep her mind focused on the moment."
            "Seeing her sink into such a state of ecstasy only serves to push me firmly in the same direction."
            "And it's only a matter of seconds before I feel myself cumming."
            call cum_reaction (alexis, 'anal', sexperience_min) from _call_cum_reaction_11
            if _return == 'anal_inside':
                "Alexis is out of it badly, but the truth is that I'm not too far behind her either."
                with vpunch
                "And as I let go inside of her ass, I couldn't pull out even if I wanted to."
                with vpunch
                "So instead I use the last of my strength to make one last push into Alexis."
                with vpunch
                "She grunts and moans in response to this, collapsing onto her face as I force her forwards."
                show alexis doggy pleasure ahegao cum
                "This means that the last of the sounds she makes are muffled by the pillow into a vague mewling."
                "And she likely doesn't hear me panting and gasping for breath either."
            elif _return == 'anal_outside':
                "Just as Alexis is starting to fall forwards, her arms giving out on her, I move backwards."
                "The effect of this is that my cock is strained against the walls of her ass for a moment."
                show alexis doggy out cum with vpunch
                "And then it literally pops out of her with a sound that's far from masculine or sexy in nature."
                with vpunch
                "But she hardly notices the noise, as this last few seconds of pressure makes Alexis grunt in a less than feminine manner too!"
                "I doubt she feels it when I cum all over her buttocks and thighs as she lays slumped before me either."
            $ alexis.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (alexis, 180) from _call_check_condom_usage_6
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show alexis doggy condom -nomc
            "Call me a traditionalist if you like, but when I see the slick and already glistening lips of Alexis's pussy, my mind's made up."
            show alexis doggy -nomc
            "Angling my cock down just enough to be sure of missing her asshole, I slide the head along the length of her folds."
            "Alexis responds almost in the same moment, lowering herself instinctively and letting out a deep moan as she does so."
            "Somehow we manage to time things just right, meaning I find myself pressing on the right point at the right time."
            "My cock slips straight into Alexis, and she instantly lowers herself further still."
            "Hungry for all that she can take, my cock sinks into Alexis until it can go no further."
            show alexis doggy vaginal hurt
            alexis.say "Oh, [hero.name]..."
            alexis.say "God but I missed the feel of your cock inside of me!"
            "Talk like that would be enough to get a guy to give his best coming from almost any girl in her current position."
            "But there's just something about it coming from Alexis's lips that makes me want to try that much harder!"
            "I start to move, slowly at first, enjoying the sensation of how tight she feels around my cock."
            "And then I begin to add more speed and force to my thrusts, sensing the changes in her reactions as they have an effect."
            "The more I give her, the more Alexis seems to want to take, soaking it all up like a sponge."
            "With each and every new effort that I put in, she lowers herself a little more, spreads a little wider."
            "It's almost as though she's becoming more of an animal with each second that passes."
            "The noises that she's making by now are certainly adding to the effect too."
            "I can hear no more clear words coming from Alexis's lips, just groans and cries."
            "But even these are becoming more muffled and indistinct as he face is pushed ever further into the pillows."
            "Normally I'd be keeping myself aware of how close my partner seemed to be to cumming."
            "Yet for some reason, I can't think of anything but continuing to pound away at Alexis."
            "Am I trying to make up for lost time?"
            "Or somehow stake a claim in her so deep that she'll never leave me again?"
            "Either way, I can't keep this pace up for much longer."
            "And pretty soon I feel myself on the brink of cumming..."
            call cum_reaction (alexis, 'vaginal', sexperience_min) from _call_cum_reaction_12
            if _return == "vaginal_outside":
                "At the very last moment I manage to shake off the haze that's settled over my mind."
                show alexis doggy out cum
                "I push Alexis forward at the very same moment that I pull myself backwards."
                "The result is that my cock is yanked out of her and instantly bobs upwards as it comes free."
                show alexis doggy out -cum bodycum
                "A second later I cum without warning, spattering the whole thing down over Alexis's backside."
                "I watch as it runs down and over her thighs, listening to the sound of us both panting in exhaustion."
                $ alexis.love += 1
            elif _return == "vaginal_condom":
                "I don't even try to pull out of Alexis as I finally cum, safe in the knowledge we used protection."
                "The result is that she feels every last moment of what follows, right until the final second."
                "She's breathing heavily and clearly exhausted, Alexis still finds the energy to glance back over her shoulder at me."
                "The look of satisfaction on her face is more than enough to make wearing the condom worth the effort."
                "Though her cheeks are flushed with colour and her hair a veritable rat's nest, I've rarely seen Alexis looking happier."
            elif _return == "vaginal_inside_pill":
                "I pause for a moment, trying to steel myself to pull out of Alexis, as much as I want to keep going."
                "Sensing my hesitation, she looks back over her shoulder at me."
                alexis.say "Don't stop...not now!"
                alexis.say "I'm on...the pill...remember!"
                show alexis doggy pleasure ahegao cum with vpunch
                "Breathing a sigh of relief that soon turns into a gasp of release, I finally let myself go."
                with vpunch
                "I cum inside of Alexis, enjoying the sensation of doing so with nothing at all between us."
            elif _return == "vaginal_inside_pregnant":
                "I pause for a moment, not sure of whether I should go on or pull out before it's too late."
                "Sensing my hesitation, she looks back over her shoulder at me."
                alexis.say "Don't stop...not now!"
                alexis.say "You can't...get me...more pregnant!"
                show alexis doggy pleasure ahegao cum with vpunch
                "I shake my head, realising that she's one hundred percent right."
                with vpunch
                "Pushing on, I feel the weight of Alexis's belly beneath her as I finally cum."
                with vpunch
                "She takes all of it, everything that I have."
                "And then finally collapses, hugging her stomach in a protective embrace."
            elif _return == "vaginal_inside_mad":
                "I can feel myself about to cum, but I try to hide the signs as best I can."
                "But the fact that I'm currently balls deep inside of Alexis means that she's in a unique position to sense what's happening."
                alexis.say "Uh...[hero.name]...[hero.name]..."
                alexis.say "Are you gonna..."
                show alexis doggy ahegao cum with vpunch
                "I let go at the very same moment that she says this, moaning as I fill her."
                hide alexis
                show alexis naked angry
                with vpunch
                #$ alexis.impregnate()
                alexis.say "Ah...ah...shit, shit, shit!"
                alexis.say "Shit - you came in me, you stupid bastard!"
                "I'm in no fit state to reply, as Alexis scrambles around beneath me."
                "She keeps up a litany of curses as she wriggles off of my already slackening cock."
                "And if looks could kill, I'd be needing the services of an undertaker right now..."
                $ alexis.love -= 5
            elif _return == "vaginal_inside_happy":
                "I can feel myself about to cum, and so I make to pull out of Alexis before it's too late."
                "But at the sensation of me doing so, she looks back at me and shakes her head urgently."
                alexis.say "Ah...[hero.name]...no, don't!"
                alexis.say "Please...don't..."
                "I know that I should ignore her and do as I intended to."
                "But the look on her face is so desperate and so full of pleading..."
                "In the moment that I'm weighing up Alexis's plea, I feel myself finally lose it."
                show alexis doggy pleasure ahegao cum with vpunch
                #$ alexis.impregnate()
                "Even if I hadn't known it myself, the sound of Alexis almost screaming in delight would have told me all I needed to know."
                with vpunch
                "She rides me to the last, making sure that every last drop is spent as deep inside of her as possible."
                "And then she slides off of me, a look of pure bliss and happiness spreading across her face as she does so."
    return

label alexis_fuck_date_cowgirl(sexperience_min):
    mike.say "I guess I just couldn't help myself."
    mike.say "You just have that effect on me, Alexis!"
    "Alexis smiles at this, letting me know that she's flattered."
    "She nods her head and lets out a little chuckle."
    alexis.say "Lie down on the bed."
    alexis.say "And don't worry - I'll make sure you have the best view in the house!"
    "I hurry to do as I'm told."
    "But Alexis doesn't show the same haste in her own movements."
    "Instead she takes her time as she climbs onto the bed."
    "She straddles my thighs at the same casual speed."
    show alexis cowgirl with fade
    "And she begins to stroke my stiffening cock slowly too."
    alexis.say "Hmm..."
    alexis.say "Now what should we do with this?"
    show alexis cowgirl chub
    "All of a sudden I can feel it welling up inside of me again."
    "The same hunger that I had for Alexis the moment we were alone."
    "Sure, it's fun to let her take control and lead me where she likes."
    show alexis cowgirl hard
    "But right now all I can think about is taking control myself."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and alexis.sub >= 50:
            mike.say "How about this, Alexis?"
            "Before she can say a word, I take hold of Alexis's waist."
            "And before she even knows what's going on, I pull her downwards."
            show alexis cowgirl -hard anal ahegao
            "My cock slips straight between her buttocks."
            "The head aimed straight for what lies hidden down there."
            alexis.say "Ah..."
            alexis.say "Oh my god..."
            show alexis cowgirl pleasure
            alexis.say "My ass..."
            "I feel the muscles of Alexis's ass as I push into her."
            "They flex and contract, squeezing me like a fist."
            "But all that does is make me all the more determined."
            "And I push onwards, feeling my cock sink ever deeper."
            alexis.say "Oh...[hero.name]..."
            alexis.say "What are you doing to me?!?"
            "There's only one answer that Alexis is going to get."
            "And that's the sensation of me beginning to fuck her."
            "As I thrust upwards, she seems to lose the power of speech."
            "Instead all I hear are moans and cries from her."
            "It's like she regresses more with every second that passes."
            "As though Alexis reverts into an animal as she takes it."
            "And my god, it's a sight to see!"
            "Alexis is riding me like her life depends on it."
            "She's clinging onto me, determined to hang on."
            "Her mouth hangs open as she pants audibly."
            "And her breasts are bouncing like rubber balls!"
            "There's only one thing better than the sight of it."
            "And that's the way it feels to have my cock inside of her right now."
            "Every motion that I just described seems to touch it."
            "Every twitch of Alexis's muscles, I feel tugging at it."
            "At first I thought that I was the one in charge here."
            "I felt that I was the one fucking Alexis nice and hard."
            "But now it's starting to feel like we're changing roles."
            "Now I feel like she's the one making use of me!"
            "The way she's squeezing my cock..."
            "Could I pull it out of her even if I wanted to?"
            "It's a question that suddenly becomes redundant a moment later."
            "And that's because I can feel myself beginning to cum!"
            call cum_reaction (alexis, 'anal', sexperience_min) from _call_cum_reaction_13
            if _return == 'anal_inside':
                "Alexis has such a tight hold on me as I lose it."
                "Tight enough that it seems pointless to resist."
                "And so I just lie back and let it happen."
                show alexis cowgirl ahegao creampie with vpunch
                "She cries out as I shoot my load into her."
                with vpunch
                "And I feel her muscles squeezing like never before."
                with vpunch
                "It's almost like Alexis is trying to milk my cock."
                "Like she wants to wring out every last drop."
                "She tenses for a moment, eyes glazed from her own orgasm."
                "Then she collapses atop me, her muscles turning to water."
                "And I can feel her gasping for breath an inch from my ear."
            elif _return == 'anal_outside':
                show alexis cowgirl -anal hard ahegao
                show chest_insert alexis zorder 1 at zoomAt(1, (860, 80))
                show belly_insert alexis zorder 2 at zoomAt(1, (20, 280))
                "Somehow I manage to pull my cock out of Alexis before it's too late."
                "But she must have been holding on with all of her strength."
                "Because as soon as I'm free, she almost falls over backwards."
                "At the last moment, Alexis manages to steady herself."
                show alexis cowgirl cumshot with vpunch
                "Which means that she's in range as I shoot my load over her."
                show chest_insert alexis cum
                show alexis cowgirl cum onbody
                with vpunch
                "The sticky, white threads of cum spatter across Alexis's chest."
                show belly_insert alexis cum
                show alexis cowgirl -cumshot
                with vpunch
                "And from there they run downwards, mingling with the sweat slicking her skin."
                show alexis cowgirl pleasure chub
                "Alexis gazes down at their progress, eyes glazed and mouth open."
                "I can hear the sound of her gasping for breath the whole time."
                "But only just above the sound of my own ragged breathing."
                hide chest_insert
                hide belly_insert
            $ alexis.flags.anal += 1
        "Fuck her pussy":
            mike.say "How about this Alexis?"
            "I smile up at Alexis as I guide her downwards."
            "And she returns the gesture as she realises my intentions."
            call check_condom_usage (alexis, 180) from _call_check_condom_usage_7
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show alexis cowgirl condom

            alexis.say "Now..."
            alexis.say "Where were we?"
            "Alexis says this as she pushes the head of my cock home."
            show alexis cowgirl -hard vaginal
            "And the next moment she's sinking down onto me."
            mike.say "Oh..."
            mike.say "Fuck..."
            mike.say "Alexis...that feels good!"
            "Alexis smiles down at me the whole time."
            "And I can see that she's trying to hold it together."
            "She's trying to look like she's the one that's in control."
            "But she keeps slipping as she feels it too."
            alexis.say "Mmm..."
            alexis.say "I...oh shit..."
            alexis.say "It feels good...really good!"
            "And from that second on, Alexis can't hide it any longer."
            "It's like she simply can't keep from showing what she feels."
            "I'm pulling her onto me with all my strength."
            "And at the same time, thrusting into her too."
            "But she still seems to need more, to feel more."
            "I can feel the force of her pushing down on me."
            "Feel her grinding herself into my lap."
            "Alexis's entire body is moving by now."
            "Her thighs slapping against my own."
            "Her arms grasping as she holds onto me."
            "And her breasts bouncing up and down, hypnotising me with their motion."
            "This is what I wanted from the moment that we were alone."
            "I wanted Alexis with this much desperation and desire."
            "But what takes me by surprise is that she wants it too."
            "And for everything I want from Alexis, she demands more in return!"
            "So what more can I do?"
            "I give her all that I have."
            "Right up until the moment I lose it..."
            call cum_reaction (alexis, 'vaginal', sexperience_min) from _call_cum_reaction_14
            if _return == "vaginal_outside":
                "I want to keep right on going, but I know that I can't."
                "Which is why I use the last of my strength to pull out."
                show alexis cowgirl -vaginal hard
                if not CONDOM:
                    show chest_insert alexis zorder 1 at zoomAt(1, (860, 80))
                    show belly_insert alexis zorder 2 at zoomAt(1, (20, 280))
                    show alexis cowgirl cumshot with vpunch
                    "She regains her balance just as I shoot my load over her."
                    show chest_insert alexis cum
                    show alexis cowgirl cum onbody
                    with vpunch
                    "The sticky, white threads of cum spatter across Alexis's chest."
                    show belly_insert alexis cum
                    show alexis cowgirl -cumshot
                    with vpunch
                    "Then it runs downwards, mingling with the sweat slicking her skin."
                    "Alexis gazes at it, eyes glazed and mouth open."
                    hide chest_insert
                    hide belly_insert
                else:
                    show alexis cowgirl cum
                "I can hear the sound of her gasping for breath the whole time."
                "But only just above the sound of my own ragged breathing."
                $ alexis.love += 1
            elif _return == "vaginal_condom":
                "I keep in mind the fact that we took precautions earlier."
                with vpunch
                "And I just keep right on going, shooting my load into Alexis."
                with vpunch
                "She cries out at the sensation, her eyes glazing over."
                show alexis cowgirl cum with vpunch
                "But she still manages to stay atop me as she cums too."
                "It's only when she's spent that Alexis finally collapses."
                "As the exhaustion takes her, she flops forwards."
                "And I end up with her laid atop me, panting for breath."
                $ alexis.love += 1
            elif _return == "vaginal_inside_pill":
                alexis.say "I'm on the pill..."
                alexis.say "Remember?!?"
                show alexis cowgirl ahegao creampie with vpunch
                "I cum a second later, shooting my load into Alexis."
                with vpunch
                "She cries out at the sensation, her eyes glazing over."
                with vpunch
                "But she still manages to stay atop me as she cums too."
                show alexis cowgirl pleasure -vaginal drip
                show pussy_insert alexis cum zorder 1 at zoomAt(0.75, (40, 200))
                "It's only when she's spent that Alexis finally collapses."
                "As the exhaustion takes her, she flops forwards."
                "And I end up with her laid atop me, panting for breath."
                $ alexis.love += 2
            elif _return == "vaginal_inside_pregnant":
                alexis.say "Cum in me..."
                alexis.say "Please?!?"
                "I do as Alexis says, but only because she's pregnant."
                show alexis cowgirl ahegao creampie with vpunch
                "I cum a second later, shooting my load into Alexis."
                with vpunch
                "She cries out at the sensation, her eyes glazing over."
                with vpunch
                "But she still manages to stay atop me as she cums too."
                show alexis cowgirl pleasure -vaginal drip
                show pussy_insert alexis cum zorder 1 at zoomAt(0.75, (40, 200))
                "It's only when she's spent that Alexis finally collapses."
                "As the exhaustion takes her, she flops forwards."
                "And I end up with her laid atop me, panting for breath."
                $ alexis.love += 3
            elif _return == "vaginal_inside_mad":
                alexis.say "Pull out..."
                alexis.say "Pull out now!"
                mike.say "Wha..."
                mike.say "Oh shit!"
                "The tone of Alexis's voice is almost desperate."
                "So much so that it makes me forget what I'm doing for a moment."
                "Just a single moment, but long enough for disaster to strike."
                show alexis cowgirl creampie with vpunch
                "I shoot my load into Alexis a second later."
                with vpunch
                #$ alexis.impregnate()
                "Afterwards we both fall silent."
                "All we can do is stare at each other in horror."
                $ alexis.love -= 5
            elif _return == "vaginal_inside_happy":
                alexis.say "Cum in me..."
                alexis.say "Please?!?"
                "The tone of Alexis's voice is almost desperate."
                "So much so that it makes me forget what I'm doing for a moment."
                "Just a single moment, but long enough for disaster to strike."
                show alexis cowgirl ahegao creampie with vpunch
                "I shoot my load into Alexis, to her apparent delight."
                #$ alexis.impregnate()
                with vpunch
                "But all I can feel is the sense of dread in my gut."
                "Why did she ask me to do that?"
                "And why didn't I stop myself from doing it?!?"
                $ alexis.love += 5
    return

label alexis_fuck_date_missionary(sexperience_min):
    "She's laid out before me, totally naked and beaming with happiness."
    "Wow..."
    "She looks so amazing..."
    alexis.say "Hey, [hero.name]!"
    alexis.say "Are you just going to stare at me all night?"
    "I shake off the momentary trance that I've fallen into."
    "And it takes more effort than I anticipated too!"
    mike.say "Ah..."
    mike.say "Sorry, Alexis!"
    mike.say "I probably could have."
    mike.say "Stared at you all night, that is!"
    "I see a little colour begin to creep into Alexis's cheeks."
    "And I realise that she's more than a little touched by the implied compliment."
    "But she shakes her head and tries to get back to the matter at hand."
    alexis.say "Well..."
    alexis.say "I don't just want to be stared at, [hero.name]."
    alexis.say "So get over here and start touching too!"
    "I nod eagerly as I rush to do as I'm told."
    "Alexis might not have been very specific in asking for what she wants."
    "But I'm more than ready to have some serious fun improvising!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and alexis.sub >= 50:
            "I might have been staring at Alexis in sheer awe just now."
            "But that doesn't mean that I'm just going to toe the line."
            show alexis missionary with fade
            if randint(1, 2) == 1:
                show alexis missionary stockings
            "So I watch as Alexis crosses her legs and hoists them in the air."
            "And I see the perfect chance present itself as she does so."
            show alexis missionary chub
            "Without pausing to let her guess what I have in mind, I make my move."
            "Alexis watches, anticipation filling her eyes."
            show alexis missionary hard
            "But she can't hope to see that my cock is aimed a little lower than her pussy."
            "The first thing she knows about it is the head poking between her buttocks."
            alexis.say "Ah..."
            alexis.say "Hey!"
            alexis.say "I think you missed the target!"
            "I can't help smiling at the way Alexis tries to play it off as just an error on my part."
            show alexis missionary anal pleasure
            "And I reward her efforts by pushing my cock further between her cheeks."
            alexis.say "Whoa..."
            alexis.say "Are you trying to..."
            alexis.say "Oh...oh...ooh!"
            "Alexis continues to protest until the moment that my cock actually sinks into her ass."
            "And then I can hear the way that her body melts in the sounds that she's making."
            "The way that her body seems to overrule Alexis's will is a massive turn-on."
            "It's like she can't help but surrender to the sensation of it entering her."
            "And before either of us knows it, she's quivering as she takes the entire length."
            "Like I said, Alexis might have hesitated, but her ass does nothing of the sort."
            "I feel the muscles up there squeezing the shaft almost like a fist."
            show alexis missionary blush
            "At first it makes me gasp, wondering if I can stand it for the duration."
            "But then I begin to feel how Alexis's muscles are flexing then relaxing."
            "And the whole thing starts to feel more like a hand-job than an actual fuck!"
            "Reassured that I can make it to the natural conclusion, I hurry to quicken my pace."
            "Of course, this only serves to make Alexis buck and writhe on my cock all the more."
            "So soon we're trapped in a vicious circle, both pushing the other further still."
            "The harder I fuck her, the more her ass squeezes my cock."
            "And more her ass squeezes my cock, the harder I fuck her."
            "Before too long, we're both moaning and panting, bathed in sweat from out efforts."
            "So much so that I almost fail to notice the fact that I'm cumming!"
            call cum_reaction (alexis, 'anal', sexperience_min) from _call_cum_reaction_15
            if _return == 'anal_inside':
                "Which means that I don't have time to even think of pulling out."
                "And maybe Alexis's ass wouldn't let me go even if I tried!"
                with vpunch
                "Instead I push my cock as deep into her as it can possibly go."
                show alexis missionary creampie with vpunch
                "At which point I lose it, shooting my entire load into her."
                with vpunch
                "Alexis closes her eyes and seems to trip out as it hits her."
                "I don't know if she's cumming too, but she's quivering all around me."
                "And in the end, it's only my cock starting to go soft that let it drop out at all!"
            elif _return == 'anal_outside':
                "I don't know how I manage to do it before I shoot my load."
                show alexis missionary -anal hard
                "But somehow my cock is out of Alexis's ass with mere seconds to spare."
                "Deprived of it, her muscles seem to keep on quivering the whole time."
                show alexis missionary cumshot with vpunch
                "And she stares up at me, a smile on her face as I finally cum."
                show alexis missionary cumshot cum onbody with vpunch
                "All that I have to give spurts down onto Alexis's ass and thighs."
                show alexis missionary -cumshot with vpunch
                "She pants the whole time, struggling to catch her breath as her heart pounds away."
                "But I can see that she's more than satisfied by my efforts."
            $ alexis.flags.anal += 1
        "Fuck her pussy":
            "The only part of Alexis's body that's as beautiful as her face is her pussy."
            "And that's where I'm headed right now!"
            call check_condom_usage (alexis, 180) from _call_check_condom_usage_8
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show alexis missionary condom outside

            show alexis missionary
            if randint(1, 2) == 1:
                show alexis missionary stockings
            "Alexis crosses her legs and hoists them into the air before me."
            show alexis missionary chub
            "I don't even have to try to reach her pussy, she makes it so easy."
            show alexis missionary hard
            "Likewise, when I brush the head of my cock against her lips, she's already slick."
            "This takes me by surprise, as I'd been expecting the need to push inside of her."
            show alexis missionary -outside vaginal pleasure
            "And the extra force that I put into the first thrust meets almost no resistance."
            "Before I know it, the head of my cock slips between Alexis's lips."
            "It doesn't stop there either, sinking straight into her in one motion."
            "In fact, I don't stop until I'm buried balls deep in Alexis."
            mike.say "Whoa..."
            alexis.say "Ah..."
            show alexis missionary normal
            alexis.say "Wha...what are you waiting for?"
            alexis.say "I already let you in - now do your thing!"
            "Alexis's words snap me out of it, reminding me that there's a job to be done."
            show alexis missionary pleasure
            "And so I set to work, eager to make the most of the opportunity."
            "Before more than a couple of seconds have passed, I'm hard at it."
            "Thrusting in and out of her like my life depends on it."
            "But that's not to say it feels like hard work or a chore."
            "Every moment that I'm inside of Alexis feels incredible."
            "And she takes all that I have to give with an almost insatiable appetite too!"
            show alexis missionary blush
            "Alexis sighs and moans with each thrust, giving voice to her desires."
            "Her mouth hangs open, her tongue almost lolling out the whole time."
            "And it's no great surprise for me to see her eyes roll up into her head."
            "Not that the sight does anything to dampen my own spirits."
            "Quite the opposite, it makes me push that much harder."
            "Pretty soon I'm beginning to feel the same way as Alexis beneath me."
            "I'm panting and can feel myself shuddering with each and every motion."
            "My head's starting to get dizzy, feeling lighter all the time."
            "And so it's a relief to feel myself starting to cum!"
            call cum_reaction (alexis, 'vaginal', sexperience_min) from _call_cum_reaction_16
            if _return == "vaginal_outside":
                "I almost don't manage to pull out in time."
                show alexis missionary -vaginal hard outside
                "But somehow I have my cock out of Alexis's pussy a moment before I cum."
                "Deprived of it, she moans at the sudden sensation of loss."
                "Though the smile on her face as she looks up at me tells a different story."
                if not CONDOM:
                    show alexis missionary cumshot with vpunch
                    "I shoot my load a second later, over Alexis's butt and thighs."
                    show alexis missionary -cumshot cum onbody
                else:
                    show alexis missionary cum with vpunch
                    "I shoot my load a second later."
                with vpunch
                "She gasps, trying to catch her breath for the first time since we started."
                "And she looks ready to collapse, satisfied and utterly spent."
                $ alexis.love += 1
            elif _return == "vaginal_condom":
                "And it's an even bigger relief to know that we took the time to use protection too."
                "Because it means that I can keep right on going until the very last moment."
                with vpunch
                "All of the energy that I have left goes into one final thrust."
                show alexis missionary ahegao with vpunch
                "Alexis moans as I do so, letting me know that she's cumming too."
                with vpunch
                "It feels good to be able to shoot my load so deep inside of her."
                "And even better to know that she's in the same place at the same time as me."
                $ alexis.love += 1
            elif _return == "vaginal_inside_pill":
                alexis.say "Don't stop now..."
                "For a brief moment I think Alexis must have gone crazy with lust."
                "But then I remember that she's the one taking precautions tonight."
                "The fact that she's on the pill means that I can keep right on going."
                show alexis missionary ahegao with vpunch
                "And when I make one final thrust into her, Alexis moans in satisfaction."
                show alexis missionary creampie with vpunch
                "As much as I feel good to have cum inside of her, she looks more delighted still."
                show alexis missionary -creampie -vaginal cum dripping
                show pussy_insert alexis cum zorder 1 at zoomAt(0.75, (820, 200))
                with vpunch
                "Alexis smiles up at me as it starts to seep out of her around my cock."
                $ alexis.love += 2
            elif _return == "vaginal_inside_pregnant":
                alexis.say "Don't stop now..."
                "I'm thankful for Alexis reminding me that I don't need to pull out."
                "After all, her rounded belly is proof that she couldn't get any more pregnant than she already is!"
                "Even better, it means that I can keep right on going!"
                show alexis missionary ahegao with vpunch
                "I make one final thrust into her, causing Alexis to moan in satisfaction."
                show alexis missionary creampie with vpunch
                "She practically beams as I cum inside of her."
                show alexis missionary -creampie -vaginal cum dripping
                show pussy_insert alexis cum zorder 1 at zoomAt(0.75, (820, 200))
                with vpunch
                "And she's still smiling as it begins to seep out of her around my cock."
                $ alexis.love += 3
            elif _return == "vaginal_inside_mad":
                alexis.say "Ah..."
                alexis.say "[hero.name]..."
                alexis.say "Don't..."
                "By the time Alexis manages to get the words out, it's already too late."
                show alexis missionary creampie with vpunch
                "I cum as deep inside of her as possible literally seconds later."
                #$ alexis.impregnate()
                with vpunch
                "What should have been an incredible moment is instantly tainted."
                "And all we can do is stare at each other, horrified at what we've done."
                $ alexis.love -= 5
            elif _return == "vaginal_inside_happy":
                alexis.say "Ah..."
                alexis.say "Don't..."
                alexis.say "Don't stop..."
                "I do as Alexis asks more out of being puzzled than anything else."
                "Her demand that I cum inside of her throws and confuses me in the moment."
                "And that's all it takes for her to get what she wants."
                show alexis missionary ahegao creampie with vpunch
                #$ alexis.impregnate()
                "Alexis throws back her head, riding me to the very last."
                with vpunch
                "But I'm left wondering why she just asked me to do that."
                $ alexis.love += 5
    return

init python:
    Event(**{
    "name": "alexis_hottub_sex_male",
    "label": "alexis_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(alexis,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

label alexis_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "It didn't take much for me to get Alexis over to my place and into the hot-tub with me."
    "In fact, she'd been mentioning the fact that I had one for a while before I actually asked her."
    "And so I guess she was probably fishing for an invite to begin with!"
    "But what the hell - am I really going to pass up the chance?"
    "Sure, I could say I'm the one in control then."
    "But I'd also be the guy who'd said no to hopping into the water with Alexis!"
    show alexis swimsuit
    "And the moment that I see her, sitting in the tub and waiting for me..."
    "Well, let's just say that I forget all about who asked who and why!"
    alexis.say "Hey, [hero.name]."
    alexis.say "Quit looking at me like that!"
    mike.say "Like what, Alexis?"
    alexis.say "Don't play the innocent."
    alexis.say "You know what I mean!"
    hide alexis
    show hottub alexis with fade
    "I can't help smiling as I climb into the tub and sit across from Alexis."
    "I know exactly what she means, and I know that she knows I know too."
    "But we both know that this is just a little game we're playing."
    "There's no hiding the fact that Alexis looks stunning in her swimsuit."
    "And I know the look in her eyes well enough to be aware of what's on her mind."
    "She's loving the fact that I can't keep from looking at her right now."
    mike.say "No I don't, Alexis!"
    mike.say "I thought we were just taking a dip together, right?"
    mike.say "Just kicking back letting the bubbles do their thing!"
    "I lean back against the side of the tub to emphasize the point."
    "Which makes Alexis chuckle and shake her head in amusement."
    alexis.say "Well, if we're going to do our thing..."
    "Alexis slides towards me as she says this."
    alexis.say "Then this is mine!"
    "I make no effort to stop Alexis as she sits on my lap."
    "After all - why would I want to stop her?"
    "She leans back against me, pressing her weight down as she does so."
    mike.say "Ah..."
    mike.say "Your thing feels pretty good, Alexis!"
    "Alexis looks over her shoulder at me, still smiling."
    alexis.say "Oh, this isn't my thing, [hero.name]."
    alexis.say "This is just me lining my thing up!"
    alexis.say "Which means lining your thing up too..."
    "I raise my eyebrows, not understanding what she means by that."
    "Until the moment that I feel her hand inside of my trunks."
    "My eyes go suddenly wide as Alexis starts to massage my cock."
    "And it doesn't take long for her touch to get me good and hard."
    mike.say "Oh, shit, Alexis..."
    mike.say "I...I think I like your thing!"
    alexis.say "I knew you would, [hero.name]!"
    show hottub sex male alexis outside with fade
    "Together, Alexis and I yank down my trunks and toss them aside."
    call alexis_dick_reactions from _call_alexis_dick_reactions_1
    "She still has a firm hold on my cock, not letting go for an instant."
    "And as soon as it's freed from it's prison, she raises herself up from my lap."
    "Then she sits down again, aiming the head squarely at her pussy."
    "Even though she seems to want this like crazy, there's still some resistance."
    "But all that means is that I get to feel the sensation of Alexis coaxing herself."
    "She teases the lips of her pussy, rubbing them against the head of my cock."
    show hottub sex male alexis inside
    "And as she inches it inside of her, I can feel my heart pounding in my chest."
    "The whole time that she's lowering herself onto me, Alexis is panting too."
    "She keeps one hand down there to direct traffic."
    "But the other one she uses to free her breasts from her swimsuit."
    "My eyes go even wider than before as she begins to squeeze them."
    "The whole time it's as if Alexis is feeling too much pleasure to bear."
    "And the only way she can bleed it off is to play with her own body!"
    "I can't help but reach out and take a firm hold of her chest myself."
    "And as soon as I do so, she releases her own grip, as if passing them to me."
    "There's no way that I can be gentle or take my time here."
    "Which means that I instantly start to massage Alexis's breasts without holding back."
    "But she shows no sign of discomfort, quite the opposite!"
    "The more I squeeze and press them between my fingers, the more she seems to love it."
    "Alexis grinds herself ever deeper into my lap the whole time."
    "Her moans have now been replaced by deep, sensual groans."
    "Alexis is moving her ass in a circular motion."
    "And so my cock is being moved in the same way too."
    "It's getting to feel like I'm going to explode any moment."
    "I guess that's because I'm mere moments from shooting my load!"
    call cum_reaction (alexis, 'vaginal', 1) from _call_cum_reaction_17
    if _return == "vaginal_outside":
        "As Alexis grinds in my lap, I choose the exact moment to make my move."
        "When she's at the highest point of the circle she's describing, I pull my groin downwards."
        show chest_insert alexis zorder 1 at zoomAt(1, (860, 80))
        show hottub sex outside
        "My cock pops straight out of her pussy, sitting up out of the water between her thighs."
        "Alexis yelps in surprise, at first because of the sensation she's feeling."
        show chest_insert alexis cum
        show hottub cumshot
        with vpunch
        $ alexis.sub += 1
        "But then she yelps again, higher still as I cum over her belly and chest."
        with vpunch
        "I watch as Alexis seizes her breasts, rubbing the sticky, white stuff into them."
        hide chest_insert
    else:
        "Alexis has almost all of her weight pressing down on me right now."
        "But she must know that I'm dangerously close to cumming too."
        "So I assume she also realises what that means in terms of where it'll end up."
        show hottub cumshot with vpunch
        $ alexis.love += 1
        "And the matter's taken out of my hands a second later when I lost it inside of her!"
        show hottub ahegao with vpunch
        "Alexis stiffens, sitting upright as I fill her pussy to the limit."
        with vpunch
        "Then she flops down in my lap like a puppet with severed strings."
    "All of the attitude and sass that Alexis was showing off before we did it seems to have vanished."
    "And once we're both spent, she's happy to simply slump against me in the tub, breathing hard."
    "I'm not in any better kind of a state myself, and so I simply leave her to lie there."
    "Right now, I couldn't move even if I wanted to!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ alexis.sexperience += 1
    $ game.active_date.clothes = None
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
