init python:
    Event(**{
    "name": "mike_hottub_sex_female",
    "label": "mike_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(mike,
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

    InteractActivity(**{
    "name": "fuck_mike_female",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasStamina(),
            ),
        IsHour(20, 0),
        PersonTarget(mike,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

label mike_hottub_sex_female:
    $ game.active_date.clothes = "swimsuit"
    scene bg livingroom with dissolve
    "It's been a hot day that's now slowly turning into a warm night."
    "And there's nothing else to do but find a way to relax and enjoy it."
    "So when [mike.name] suggests that we fire up the hot-tub, I agree at once."
    "It's always sitting out there, taking up so much real estate in the back yard."
    "And I find myself thinking that we should be making more use of it."
    scene bg pool with fade
    "So after changing into my swim-suit, I head out to join [mike.name] for a soak."
    "But as soon as I walk out there, I stop and look around in surprise."
    bree.say "Whoa..."
    bree.say "What's all this?"
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "The lights around the hot-tub have all been turned down."
    "But those under the water are turned up to the max."
    "That helps to make the water in the tub look even more inviting."
    "And when I take a closer look at the steam curling off the water, I see that's not all."
    "Are there...yeah, I was right!"
    "There are rose petals floating on the surface too!"
    mike.say "I hope you like it, [hero.name]."
    mike.say "Just trying to make it a little bit special!"
    scene bg pool
    show mike swimsuit blush
    with dissolve
    "I turn to see [mike.name] standing by the side of the hot-tub."
    "Obviously he's in his shorts, ready to jump in there."
    "But he's also rubbing the back of his head, like he's nervous."
    bree.say "Are you kidding, [mike.name]?!?"
    bree.say "Of course I like it!"
    bree.say "This is so thoughtful."
    bree.say "So...romantic!"
    hide mike
    show mike kiss swimsuit
    with dissolve
    $ mike.flags.kiss += 1
    "I walk over and plant a kiss on [mike.name]'s unsuspecting lips."
    "At first his eyes pop open in genuine surprise."
    "But then I feel him relax and begin to return the kiss."
    "I wrap my arms around his waist, and he seems to get the hint."
    "Because a moment later, I feel his arms around me too."
    "And then I can feel his body against mine."
    "Sure, [mike.name]'s no beefcake."
    "But he's always off down to the gym, and it shows."
    "I can't help but feel a little thrilled as we embrace."
    "His muscles are firm and they move in such a pleasant way."
    "Then I feel something else."
    "Something beginning to stir below his waist..."
    hide mike kiss
    show mike swimsuit blush
    with dissolve
    mike.say "Erm..."
    mike.say "We...we should get in!"
    mike.say "Don't you think we should get in, [hero.name]?"
    "I stand back, stepping out of [mike.name]'s embrace and chuckling."
    "How can he suggest we do something as intimate as share a hot-tub."
    "And yet get so embarrassed when I brush against his manhood?"
    "I don't know why, but that's one of the things that makes me like the guy."
    "He's such a strange mixture of bravado and nerves."
    "One moment the big man and the next a cautious little boy!"
    bree.say "Okay, [mike.name]..."
    bree.say "Last one in's a loser!"
    "I trot over to the edge of the tub and climb right in."
    show hottub mike valentine with fade
    "The water's as warm and welcoming as I expected it to be."
    "And I don't hesitate to sink in up to my neck."
    "Then I look up and beckon for [mike.name] to come join me."
    "He hesitates for a moment, like he's distracted."
    "Then he hurries to follow my lead."
    "But I can't help realising what was distracting him just now."
    "Call me vain if you want, but he must have been watching me!"
    "It's odd, because most of the time a guy perving on me is a pain."
    "And sometimes it even gets to the point of being making me contemplate violence."
    "But when [mike.name] looks at me in that way, I don't react the same way."
    "With him it's more like the admiration's flattering."
    "I mean yeah, I know that he's looking at me in that way guy's always do."
    "But somehow I kinda like knowing that [mike.name]'s checking out the merchandise!"
    "[mike.name] doesn't come straight over to me once he's in the tub."
    "Instead he settles down on the other side and facing me."
    "I can't help raising an eyebrow at this."
    bree.say "You comfortable over there, [mike.name]?"
    bree.say "Because there's plenty of room on my side of the tub!"
    "[mike.name] gives me a nervous smile at this."
    "And he shakes his head."
    mike.say "I...I'm okay, [hero.name]."
    mike.say "We're supposed to be relaxing, aren't we?"
    mike.say "You know, kicking back and just chilling out?"
    "For a moment I feel a little slighted by his reaction."
    "After all, he's gone to all the effort of getting me here."
    "Not to mention the rose petals and subdued lighting!"
    "But then I remember how [mike.name] can be a little timid at times."
    "He's probably been building this up in his head all day."
    "And now that it's actually happening, he's afraid of screwing it up."
    "Well, that just means I'm going to have to take the lead!"
    bree.say "Don't worry, [mike.name]."
    bree.say "You can sit right there."
    bree.say "In fact you don't have to move a muscle."
    bree.say "Just leave everything to me..."
    "Without another word, I push myself through the water."
    "It's just deep enough for me to float over to [mike.name]'s side."
    "And I begin to stand up just as I reach him."
    "This has the effect of making me rise out of the water as I come."
    "He raises his head to keep looking me in the eye."
    "And I can see the look of fascination in them the whole time!"
    mike.say "[hero.name]..."
    mike.say "I..."
    "I put a finger to [mike.name]'s lips, silencing him."
    "And I add the sweetest smile I can to seal the deal."
    bree.say "Shh..."
    bree.say "You went to all this effort for me."
    bree.say "Now let me do something for you..."
    "[mike.name] swallows, making an audible sound."
    "And he nods, his eyes still wide with anticipation."
    "I decide to begin slowly, lowering myself down in front of him."
    "Putting one hand on his shoulder, I reach down with the other."
    "This hand goes under the water and between his thighs."
    "Then I slide it up the leg of his trunks."
    "[mike.name] gasps as my fingers close around his cock."
    "He nods again, but the gesture really doesn't mean anything to me."
    "Because by now I'm more than committed to my current course of action."
    "Using a subtle mixture of squeezing and stroking, I coax him to life."
    "Truth be told, he was already beginning to stir down there."
    "So all I really have to do is speed things up a little."
    "I look [mike.name] in the eye as I do all of this."
    "And I can't help enjoying the look of helplessness on his face."
    "Even more so the fact that it quickly turns into one of surrender."
    "And then, as I watch, it becomes one of pleasure."
    "I have his cock out of his trunks by now."
    "The tip is sticking up out of the water."
    bree.say "Ooh..."
    bree.say "Look at this..."
    bree.say "It's just like an iceberg, [mike.name]!"
    "[mike.name]'s face twists, showing his confusion."
    mike.say "Huh?"
    mike.say "What's that supposed to mean?"
    bree.say "It's like an iceberg because there's so much more of it under the water!"
    "I make my point by stroking the shaft of [mike.name]'s cock."
    "He gasps and nods, urging me on without saying a word."
    "But it's not like I need any kind of serious encouragement!"
    "I begin to work [mike.name]'s cock faster and harder now."
    "My hand is moving up and down under the water."
    "And it's impossible to see what's happening save for a disturbance on the surface."
    "[mike.name] seems to be getting into it more with each second that passes."
    "Because I see him lean back, stretching his arms out on the side of the tub."
    "At the same time he begins to float in the water, legs rising to the surface."
    "Of course this means that his manhood emerges before anything else."
    "And I have to stifle a giggle, as it reminds me of those scenes in monster movies."
    "The ones where the huge thing that's like a dinosaur rises from the depths of the ocean!"
    "Luckily for me, it seems that [mike.name]'s too laid back to have a chance of noticing."
    "In fact, his eyes are starting to look a little glazed over!"
    "Maybe that means it's time I started thinking about pleasuring myself too?"
    show hottub sex female mike valentine with fade
    "I turn my back on [mike.name] slowly, still holding his cock in one hand."
    "With the other I reach down and pull the crotch of my swimsuit aside."
    "Then I lower myself down and onto him, slowly and with great care."
    "As soon as the tip of [mike.name]'s cock touches me down there, I can't help shivering."
    "It feels so good and the promise of what's to come next fills me with excitement."
    "What, you think it was just [mike.name] getting hot and bothered in the tub?"
    "All this time I've been working myself into a state too."
    "And this is where I get to blow some of that off!"
    "I use the tip of [mike.name]'s cock to trace the lines of my pussy."
    "I can feel it sliding along the folds of sensitive skin."
    "Finally I know that the time is right, and I close my eyes."
    "Then I push down, holding onto it the whole time."
    bree.say "Oh..."
    bree.say "Oh fuck..."
    "I feel myself parting and letting [mike.name] begin to inch inside."
    "It can't take more than a few seconds for him to fill me."
    "But somehow that short space of time stretches out."
    "And I feel like it takes an age for his cock to go all the way in."
    "For a moment I think that [mike.name]'s totally out of it."
    "That I'm going to be the one doing all of the work here."
    "But then I feel the sensation of his hands on my hips."
    "It seems like he's suddenly come back to life!"
    "Looking over my shoulder, I see that he's sleepy, but certainly awake."
    bree.say "You ready back there?"
    bree.say "Huh, [mike.name]?"
    "I wriggle around a little, feeling his cock twitch inside of me."
    "And this seems to do the trick, making [mike.name] nod in recognition."
    mike.say "Uh-huh, [hero.name]..."
    mike.say "Let's do this thing!"
    "I nod and then turn my head back."
    "But the moment I do, I feel [mike.name] come back to life."
    "He doesn't leap into action or move at any great speed."
    "Rather he starts slowly, making deep and fulsome motions."
    "Now it's my turn to feel myself beginning to melt inside."
    "The way [mike.name]'s thrusting in and out of my, deep and slow."
    "It means that I feel everything he does down to my bones!"
    "Before I was the one calling the shots while [mike.name] laid back."
    "But now those roles are reversed, as his efforts render me helpless."
    "I didn't know how ready I was for him to do this to me."
    "Or how much my body was longing for his attentions either."
    "All I can do is nod my head, urging him to keep it up."
    "And soon enough those nods become nothing more then sympathetic motions."
    "There's no danger of [mike.name] going too fast or one of us cumming too soon."
    "We seem to be moving in slow-motion most of the time."
    "Seconds stretching out to impossible lengths as we make love."
    "I can feel my own hands moving over my body."
    "And I know that there are beads of moisture running over my skin."
    "But I can't say if they're water from the hot-tub."
    "Or if it's my own perspiration."
    "All I know is that [mike.name]'s efforts have left me totally at his mercy."
    mike.say "Fuck..."
    mike.say "Here it comes!"
    "I half turn to see what [mike.name]'s talking about."
    with vpunch
    "But in that same moment he tenses and I feel an explosion inside of me."
    with vpunch
    "[mike.name]'s hands clamp down like vices, holding me in place as he cums."
    with vpunch
    "And there's nothing I can do but ride it out while he's deep inside me."
    $ mike.impregnate()
    "I can't keep myself from being swept along with him too."
    with vpunch
    "My own orgasm hits a few seconds later, redoubling all that I'm feeling."
    "Slowly, I feel [mike.name]'s hands slacken as he subsides and his orgasm fades."
    "This leaves me to slide down into the water, curling myself against him."
    "His cock slips out of me at the same time, making me moan one last time."
    "[mike.name] falls silent again, his sudden burst of energy over."
    "And I do the same, leaning my head on his shoulder."
    "Which leaves us enjoying the sensation of the bubbling water on our bodies."
    "That and the fading afterglow of all we've just done."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ mike.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return

label mike_fuck_bathroom_female:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ mike.sexperience += 1
    if sasha.room == game.room and not sasha.hidden and sasha.sexperience >= 3:
        "Should Sasha join in?"
        menu:
            "Yes":
                call home_harem_bree_sasha_shower_female from _call_shower_ffm_female
                return
            "No":
                $ sasha.love -= 2
    $ mike.flags.showersex = True
    scene bg bathroom
    "Pulling off my top and kicking off my shorts, my feet hardly make a sound as I pad over to the shower door and open it with infinite care not to make as much as a sound."
    "The first thing that [mike.name] knows about me being there is the sensation of my hands, as they reach out and grab his already soapy dick."
    show mike naked
    mike.say "Whoa - what the fuck?!?"
    "He jumps backwards in surprise, almost slipping on the wet floor of the shower as he does so."
    "As he tries to steady himself on the equally slick tiled walls, I can't help but giggle at his state of surprise."
    bree.say "Don't shit yourself, [mike.name] - it's only me!"
    mike.say "Yeah, [hero.name]...I can see that!"
    mike.say "You just made me jump, that's all."
    "I keep a hold of his cock as he talks, enjoying the sensation of just how slippery it feels between my fingers."
    bree.say "Hmm...seems like at least one part of you's glad to see me!"
    "I'm not making it up just for the sake of teasing him."
    "I can already feel it stiffening in my hand."
    mike.say "Well...yeah, of course I am."
    mike.say "But I was just trying to take a shower, that's all!"
    "I keep on laughing at whatever he says, shaking my head a little as I do so."
    "By now I'm standing so close to [mike.name] that my nipples are starting to brush against his chest."
    "The sensation is beginning to have pretty much the same effect on me as my fondling of his cock is on [mike.name]."
    "I might have snuck in here with mischief more on my mind than anything else, but I can already feel that I need more."
    "Not scratching that itch now will only end up with me lying in bed, feeling frustrated for most of the night."
    "Sure, I could easily take care of my self - but it's never as satisfying when you know what you could have had the real thing instead."
    bree.say "Oh come on, [mike.name] - you can take a shower anytime."
    bree.say "You can only take me when I let you..."
    "I lean in and kiss him, full and slow on the lips."
    "He responds after perhaps a couple of seconds, wrapping his arms around me and leaning into the kiss."
    "I have his cock between my thighs now, working it up and down until it comes tantalisingly close to my neatly-shaved pussy."
    "Finally, once we're well into the thing and pressed against each other like a couple of amorous seals, [mike.name] starts to wake up to just what's happening."
    "I can feel his hands begin to travel all over my body, exploring me as if he's never laid a finger on me before this moment."
    "It thrills me to my core whenever his touch passes over one of the seriously sensitive parts that are within his reach."
    "But even when he's doing nothing supposedly more erotic than stroking my arms or running his hands through my hair, the effect is almost the same."
    "By now I feel as though I'm going to beg if he doesn't do more, and soon."
    show bree showersex wet
    bree.say "Ah...[mike.name]...put it inside of me...please!"
    "I twist in his arms, taking advantage of the fact that we're both slippery from the water."
    "Only stopping when I have his belly to my back, I grind my backside into his groin, too desperate for him to be in any way subtle."
    "He responds to me by looping his larger, more muscular arms under my own."
    "And then he pulls me backwards with a sudden and quite unexpected show of strength."
    "Taken by surprise, I have mere moments to guess at what's going on before I'm almost literally impaled."
    "[mike.name] controls me with surprising ease, making sure that I go nowhere save for straight onto his eagerly awaiting cock."
    "Using his greater height and holding me at just the right angle, I sink down onto him gradually."
    "Even though I'm already slick down there and have been wanting this the whole while, there's still a degree of resistance."
    "But of course this only serves to make the sensation of his head stubbornly forcing it's way into me all the more intense."
    "The whole time it takes him to push into me as deeply as he's able can't be more than maybe ten seconds."
    "Yet to me it seems to stretch on into far longer, as the seconds become elastic and the feelings from down there matter more than the passage of time."
    "[mike.name] holds me there, once he's buried himself as deep as he can go, tensed and stiff as an iron bar."
    "I can feel him starting to push me up against the wall, using it to make the angle at which he's inside all the more acute."
    "And then he begins to move, proving to me that I'd been wrong to think things couldn't get any better than they already were."
    "Only his lower body actually becomes animated, the rest of him tasked with holding me firmly in place."
    "But is it ever enough to make the entirety of mine feel like it's suddenly come to life on a whole new level."
    show bree showersex wet speed
    "I can't keep myself from beginning to moan and cry at the way in which he's making me feel as he thrusts in and out of me."
    "Flushed from the heat inside of the shower and the intensity of having him inside of me, I seem to be burning up more intensely with each moment that passes."
    "Soon I can sense the first tell-tale signs that [mike.name] is getting ever closer to cumming."
    "His pace not only quickens still more, but becomes almost frantic as he tries to extract as much pleasure from me as possible before the inevitable happens."
    "And he begins to grunt with the continued effort of it all, like an animal fast approaching the end of its endurance."
    "As his body bucks and twinges, I can feel him trying to separate himself from me, fearful of the consequences if he does not."
    bree.say "No...[mike.name]..."
    bree.say "Stay inside of me!"
    $ mike.impregnate()
    $ mike.love += 1
    "Somehow he manages to hear and obey my last, gasped instructions mere moments before he's taken by his climax."
    "It can be touch and go as to whether a guy going off inside of me can push me over the edge."
    "But this time there was just no room for doubt, and [mike.name] sets me off like one match lighting another."
    "I'm actually crying out now, unable to keep myself from doing so as my orgasm takes me and takes over all at once."
    "My legs give way, their muscles suddenly refusing to support my weight, and I'm grateful for [mike.name] supporting me the whole time."
    "In all honesty, his support is also for the sake of keeping his cock in me until the very last possible moment, but I'm still grateful all the same."
    "We stay there, locked in an embrace until the last motes of strength has fled from our limbs and all there is left to do is collapse."
    return

label mike_fuck_date_female(location="hero"):
    $ game.room = "bedroom4"
    $ game.play_music("music/roa_music/city_nights.ogg")
    call mike_fuck_date_intro_female (location) from _call_mike_fuck_date_intro_female
    if mike.sexperience >= 2:
        call mike_fuck_date_titfuck from _call_mike_fuck_date_titfuck

    menu:
        "Missionary":
            call mike_fuck_date_missionary (0) from _call_mike_fuck_date_missionary
        "Spoon" if hero.sexperience >= 5:
            call mike_fuck_date_spoon (5) from _call_mike_fuck_date_spoon
        "Doggy" if hero.sexperience >= 10:
            if hero.sexperience >= 20:
                menu:
                    "Vanilla":
                        call mike_fuck_date_doggy (10) from _call_mike_fuck_date_doggy_1
                    "Rough":
                        call mike_fuck_date_doggy_rough (20) from _call_mike_fuck_date_doggy_rough
            else:
                call mike_fuck_date_doggy (10) from _call_mike_fuck_date_doggy
        "Cowgirl" if hero.sexperience >= 15:
            call mike_fuck_date_cowgirl (15) from _call_mike_fuck_date_cowgirl
        "Reverse Cowgirl" if hero.sexperience >= 20:
            call mike_fuck_date_reverse_cowgirl (20) from _call_mike_fuck_date_reverse_cowgirl

    if _return == "leave_without_gain":
        return
    $ mike.sexperience += 1
    if _return == "leave_with_gain":
        return
    hide mike
    call mike_sleep_date_fuck (location) from _call_mike_sleep_date_fuck
    return

label mike_fuck_date_intro_female(location="hero"):
    $ result = game.days_played % 8
    if result == 0:
        scene bg bedroom4
        show mike
        with fade
        "The two of us find ourselves in my room, laughing and joking about something or another, before an awkward silence begins to fill the air."
        "I've had a fun time, but the night isn't over yet, and thanks to where we're both stood it's pretty clear what's about to come next."
        "The two of us give each other sheepish looks as [mike.name] builds up the courage to act, standing for just a little too long for comfort before stepping forwards and pressing his lips against mine."
        "I'm took slightly off guard, his movements having been swift and sudden, but I quickly begin melting into the embrace, wrapping my fingers around his in return as he presses his body against mine more and more."
        "My eyes flutter closed to focus ever more on his lips against mine, on the way that he gently sucks my lip, his teeth brushing lightly against me, his saliva swapping with mine and taste filling my mouth."
        "His movements, while filled with intent, are a touch clumsy, yet his sheer earnestness more than makes up for it."
        "I lose myself as his hand snakes around my waist, pulling me closer still until I can feel his bulge pressing against me through our clothing."
        "It feels like it's only been moments before he pulls away but logic tells me it's been minutes, stood there in silence and simply enjoying one another."
        "I let out a quiet little whine, feeling my need bubbling up from within, desperate to lean forwards and reignite what we just had, but I hold myself back."
        "Our eyes meet and we smile, pausing for a moment to collectively catch our breath before [mike.name] spins around and playfully pushes me down."
        "I let out a quiet yelp as I hit the bed with a soft pomf, my eyes quickly finding [mike.name]'s again as I slowly crawl backwards, getting comfortable."
        show mike underwear blush with dissolve
        "He begins pulling his shirt over his head, his bare chest quickly distracting me from following his lead."
        "His shirt has barely hit the floor as he begins crawling onto the bed after me, ever so slowly clambering over my body as his hand fumbles with his pants."
        "Not wanting to be left behind, I quickly begin tearing my own clothes away, quickly reducing myself to naught but my underwear."
        "A cold breeze washes over my near naked form but I'm quickly warmed again as [mike.name] descends on me, his lips meeting mine yet again as his body presses against mine."
        "His hands trace my thighs, gently dancing across my skin, teasing me needlessly as his tongue invades me, passionately dancing with my own."
        "Once again my eyes close, my mind drifting to the large tent his own underwear proudly showcased, the size both intimidating and intriguing."
        "With my sight cut off, the way his fingers gently explore my flesh is more effective than ever, especially when I feel them slipping behind my back, my bra soon being torn away."
        "My erect nipples brush freely against [mike.name]'s chest as we kiss now, one of my arms slung around his neck while the other begins attempting to mimic the man."
        "I trail it down his chest, slowly, stopping at his midriff for a moment, before going further, and further, until my palm made contact with his rod."
        "The thin fabric of his boxers still separate us, but from the way he gasps within our embrace as I gently begin tracing his length I can tell he still feels well enough."
        "Not one to be outdone, or his patience simply beginning to wear thin, I feel the same hand that removed my bra grasp the rim of my panties, tearing them away and leaving me entirely open."
        show mike naked blush with dissolve
    elif result == 1:
        show bg livingroom
        show mike
        with fade
        "You know what, I've had a pretty good night on my date with [mike.name]."
        "He's been a really good boy and made sure that things went great."
        "So I'm going to give him a little treat now that we're back home."
        "And I'm going to let you in on a secret too."
        "Girls don't always hate it when you stare at their breasts."
        "It's like everything - you just gotta be in the mood, you know?"
        "Like right now, [mike.name]'s been checking mine out for a while."
        "And it's kind of a turn-on."
        "Like it means that I know he's crazy into me."
        "And that's why I'm going to use them to reward him."
        "As soon as we're in the house, I take hold of his hand."
        mike.say "Whoa, [hero.name]..."
        mike.say "Where are we going?"
        bree.say "My room, [mike.name]."
        bree.say "There's something I want to show you!"
        show mike blush
        "[mike.name]'s a little drunk, but he seems to get the message."
        "Because his eyes light up at the prospect and her nods his head."
        mike.say "Oh..."
        mike.say "Okay, [hero.name]..."
        mike.say "Let's go!"
        "I nod and smile, leading him upstairs and straight to my room."
        show bg bedroom4
        show mike blush
        with fade
        "Oh, I should have mentioned that I'm a little drunk too!"
        "So I can already feel the excitement building inside of me."
        "Ushering [mike.name] inside, I close the door behind us."
        "He waits just inside my room, waiting for my next instruction."
        "And he doesn't resist for a second when I walk him over to the bed."
        bree.say "Take a seat."
        bree.say "And strip while you're at it."
        "[mike.name] nods and flops down on the bed."
        show mike underwear with dissolve
        "The mattress and frame creak as he strips of his clothes."
        show mike naked with dissolve
        "All the time I'm trying to keep a seductive smile on my face."
    elif result == 2:
        show bg livingroom
        show mike
        with fade
        "The moment [mike.name] and I make it back to the house, we both know what we want."
        "And there's no need for either of us to speak as much as a single word."
        "I just take hold of his hand and lead him upstairs to my bedroom."
        show bg bedroom4
        show mike
        with fade
        "[mike.name] keeps a silent look-out as I open the door, and then we slip inside."
        "And once it's closed, we leap into action!"
        "Seriously, it's like someone throws a switch."
        "I pretty much pounce on [mike.name], and he's ready to catch me too."
        show mike kiss with fade
        $ mike.flags.kiss += 1
        "Our lips meet at the same moment we wrap our arms around each other."
        "And the first chance I get, I slip my tongue into [mike.name]'s mouth."
        "I can feel his hands all over me, just squeezing and caressing at first."
        "But then he starts to pull at my clothes, trying to undress me."
        "It's a clumsy effort, as he can't see what he's doing and he's already distracted."
        "Yet that doesn't stop me from starting to do the same thing in return."
        show mike kiss underwear with fade
        "This strange dance continues, and more than once we almost topple over."
        "But somehow we manage to strip each other down to our underwear."
        show mike kiss naked with fade
        "Finally, [mike.name] almost tears my bra off me, spilling my breasts."
        "And I haul down his shorts, making his cock pop-up like a Jack-in-the-box!"
        hide mike kiss
        show mike naked perv at center, zoomAt(1.5, (640, 1040))
        with fade
        "Both of us step back, breaking the kiss as we pant for breath."
        "I can see the way [mike.name]'s looking at me right now."
        "Like he's a starving man and I'm the meal that could save his life!"
        "And I've got to admit, the way I'm staring at him is pretty much the same."
        "His eyes follow my breasts as they sway from side to side."
        "The motion of his now fast rising cock making mine do the same too."
        mike.say "W...well..."
        show mike blush
        mike.say "Are we going to do it?"
        mike.say "Or what?"
        "The sound of forced bravado in [mike.name]'s voice makes me smile."
        "But I keep myself from laughing, instead nodding my head."
        bree.say "Oh yeah, [mike.name]."
        bree.say "Don't you worry."
        bree.say "We're going to get it on!"
        "I take a step backwards as I pull down my panties."
        "Turning my back on [mike.name], I toss them straight at him."
        show mike at startle
        "He flinches, but still manages to catch them."
        "Then he watches in stunned silence as I climb onto the bed."
        "I make it as slow and sensual as I can."
        "Because I want to give him a show."
        "To make him crazy desperate to get his hands on me."
    elif result == 3:
        show bg livingroom
        show mike normal
        with fade
        "I have to admit that I was a little sceptical about how tonight might go."
        "Sure, [mike.name]'s a great guy and one that's great to hang around the house with."
        "But there's always been that nagging doubt in the back of my mind."
        "Even when we started dating, I was still worried he might turn out not to be boyfriend material."
        "Then tonight happened - and boy, did he prove me wrong!"
        "I don't know if it's sheer luck, or if he's really done his homework."
        "But [mike.name] sure stepped up to the plate and scored a goal tonight!"
        "Maybe I'm a little drunk, but he's really impressed me a lot."
        "So when we make it back to the house, I keep a tight hold on his hand."
        mike.say "So..."
        mike.say "Here we are, [hero.name]."
        mike.say "Back home again..."
        bree.say "Yeah, [mike.name]."
        bree.say "I kinda noticed that!"
        mike.say "Erm..."
        show mike blush
        mike.say "Are you, like...tired or anything?"
        "I can't help chuckling as [mike.name] stumbles over his words in front of me."
        "But the truth is I'm really grateful that he is."
        "Because it's helping to hide how nervous I am too!"
        bree.say "Not too tired to do this..."
        show mike kiss with fade
        $ mike.flags.kiss += 1
        "[mike.name] doesn't resist as I pull him closer and plant a kiss on his lips."
        "In fact, with every second that passes, I can feel his confidence growing."
        "It's a real turn-on to notice how he's beginning to take a little more control."
        "Because guys that are all shy and nervous can be sweet."
        "But there's just something so sexy about confidence."
        "You know, real confidence?"
        "Not arrogance or cockiness."
        hide mike kiss with fade
        "When the kiss ends, the look on [mike.name]'s face says he knows what he wants."
        "So I don't even have to explain myself as I lead him towards my bedroom."
        show bg bedroom4
        show mike blush
        with fade
        "Once we're safely inside, he starts to take the lead a little more."
        "He begins by undressing me, gently but with a firm purpose in mind."
        "I do the same to him, stripping off his clothes one by one."
        show mike naked with dissolve
        "But we're not going fast or doing it with a sense of desperation."
        "Hands linger on bodies and there's time for a little diversion here and there too."
        "And by the time we're both naked, it's clear where this is going."
        "I walk the last few feet to bed."
    elif result == 4:
        show bg livingroom
        show mike normal
        with fade
        "When we get back to the house, I can see that [mike.name]'s pretty tired."
        "He's trying to keep his eyes open and the conversation going."
        "But he keeps zoning out and then snapping back to reality the whole time."
        "Truth be told, I'm feeling beat too."
        "But I've had too good of a time to want to spend the night alone."
        mike.say "Oh man..."
        mike.say "Sorry, [hero.name]..."
        show mike down
        mike.say "I've been working too hard recently!"
        "[mike.name]'s yawn is infectious, setting me off too."
        bree.say "Oooh..."
        bree.say "No worries, [mike.name]..."
        mike.say "I guess we'd better both get some sleep, yeah?"
        bree.say "Well...yeah..."
        bree.say "But it doesn't have to be alone, you know?"
        "[mike.name] looks more than a little surprised."
        mike.say "You want to sleep together?"
        mike.say "Even when we're both dead tired?"
        bree.say "Why not?"
        bree.say "It might actually be nice..."
        show mike blush
        "I see the expression on [mike.name]'s face undergo a subtle change."
        "He's starting to smile as the possibilities go through his mind."
        "And then he nods, letting me know that I've won him over."
        mike.say "Why not, [hero.name]!"
        mike.say "We can just snuggle up and keep each other warm."
        mike.say "Then see how we feel when we wake up in the morning!"
        "He adds a wicked little wink at the end there."
        "As if I needed to have his true meaning explained to me."
        bree.say "Come on, Mister Romance!"
        bree.say "My room's closer."
        "I take hold of [mike.name]'s hand, leading him the rest of the way."
        "Then we shuffle into my room and start to get undressed."
        scene bg bedroom4 with fade
        "Then we shuffle into his room and start to get undressed."
        "And no, there's nothing sexy about the process either!"
        show mike underwear with dissolve
        "[mike.name] and I just tug off our clothes and toss them in a pile."
        show mike naked with dissolve
        "Then we jump into bed, because we're that tired."
        "I can already feel myself curling into a ball as soon as I'm under the covers."
    elif result == 5:
        "I don't know what it is with me today, honestly I don't."
        "It's kind of like I got out of bed on the wrong side."
        "But the weird thing is that it's not made cranky or pissed."
        "More like it's left me wired and wanting to take on the world."
        "All day I've been up for anything, taking on whatever's in my path."
        "And the date I've just been on with [mike.name] is no exception either."
        "Normally I'd have been trying to keep from messing up."
        "You know, letting my doubts get in the way of having a good time."
        "But tonight I just went for it, throwing caution to the wind."
        "And it seems to have paid off too."
        show mike blush
        "[mike.name]'s been following me round like a love-sick puppy."
        "I mean, hanging on my every word and all that stuff!"
        "So when we get back, I don't see any need to change things up either."
        bree.say "Come on, [mike.name]!"
        show mike surprised
        mike.say "Huh?"
        bree.say "Come on!"
        bree.say "We're going to my room."
        show mike blush
        mike.say "We...we are?"
        "Rather than answering the question, I grab [mike.name] by the hand."
        scene bg secondfloor with fade
        "And without another word, I drag him up the stairs towards my room."
        "As I was hoping, [mike.name] doesn't resist for a moment."
        "Instead he obediently hurries after me."
        scene bg bedroom4 with fade
        show mike blush at center with easeinright
        "Once we're there, I open the door and push him inside."
        mike.say "Whoa..."
        mike.say "Okay, [hero.name], okay!"
        mike.say "I get the message!"
        bree.say "Then what are you waiting for, [mike.name]?"
        bree.say "Take off your damn clothes!"
        "[mike.name] jumps a little as I bark the order at him."
        "But then he nods and begins to strip off."
        "I nod too, already doing the same thing myself."
        show mike naked with dissolve
        "As soon as we're both naked, I walk over to him."
        show mike at center, zoomAt(1.5, (640, 1040))
        "Putting one hand on his cheek, I stroke his cock with the other."
        hide mike
        show mike kiss naked with fade
        $ mike.flags.kiss += 1
        "Then I plant a kiss on his lips, feeling it harden as I do so."
        "All it takes is a little tug on his cock."
        "Just one in the direction of the bed."
        "And then [mike.name]'s staggering towards it like he's hypnotised."
        "Once we're there, I let go of him and step away."
        hide mike
        show mike blush naked at center, zoomAt(1.5, (640, 1040))
        "[mike.name] looks surprised, almost like he's been slapped awake."
        "But he soon recovers when he sees me crawling onto the bed."
        "I do the best I can to make sure it's slow and sensual."
        "My breasts swaying and my ass wiggling, I mount the bed."
        "Then I look back over my shoulder at [mike.name]."
        "And I hope the look in my eyes lets him know that I want him to mount me next!"
        "Luckily for me, [mike.name] doesn't take much convincing."
        "His own eyes might look a little glazed over."
        "But a quick glance down at his cock tells me it's working."
        "He's getting good and hard, rising to the occasion."
        "And it seems like his cock is the one doing the thinking for him too!"
    elif result == 6:
        scene bg taxi car with fade
        "Normally after a date you have that awkward moment- you know the one."
        "When you wonder if you're going to be asked back to their place?"
        "Or if you're feeling really brave, you pluck up the courage to invite them to yours."
        "But when you're dating one of your housemates, it's a hundred times worse."
        "I mean, it's not like you can get away from them if the date went bad."
        "Because you're both going home to the exact same address!"
        "And even if things went well, you still have a difficult decision to make."
        scene bg house
        show mike date
        with fade
        "The one that [mike.name] and I have to make as soon as the taxi drops us off outside the house."
        "As we walk up to the front door, I take a deep breath."
        "And then I just come out with it."
        bree.say "So..."
        bree.say "Your place or mine?"
        show mike happy at startle
        "[mike.name] chuckles and shakes his head as he opens the door."
        mike.say "Well, my room is closer."
        mike.say "Doesn't that clinch it?"
        show mike normal
        "I frown and shake my head."
        bree.say "No it doesn't!"
        bree.say "I want to be able to fall asleep afterwards."
        bree.say "And my bed is more comfortable than yours!"
        "[mike.name] shrugs at this."
        mike.say "Where's the problem with that?"
        mike.say "Just get up and go to your room when we're done."
        bree.say "No way, [mike.name]!"
        bree.say "I'll be way too tired for that."
        show mike annoyed
        "[mike.name] looks thoughtful for a moment."
        show mike happy
        "Then his face lights up, like he's figured it all out."
        mike.say "I know, I know..."
        mike.say "We can do it on neutral ground."
        mike.say "How about we use Sasha's room?"
        "I know instantly that [mike.name]'s joking."
        show mike normal
        "But also that he's trying to make a point."
        "The discussion is starting to get a little silly."
        bree.say "Look, [mike.name]..."
        bree.say "Can we use my room?"
        bree.say "Just this once for no other reason than I want to?"
        scene bg secondfloor
        show mike date
        with fade
        "[mike.name] nods, and then we hurry upstairs."
        "We make it to my room in a matter of seconds."
        scene bg bedroom4
        show mike date
        with fade
        "And as soon as the door is closed behind us, we're straight down to business."
        "[mike.name] grabs hold of my shirt as I walk past him."
        "Then he pulls it up and over my head!"
        "I make a good show of pretending to be outraged."
        "And then I do the exact same thing to him in return."
        show mike naked with dissolve
        "We keep this up, each stripping the other of an item of clothing."
        "And we don't stop until we're both standing there totally naked."
    else:
        scene bg livingroom
        show mike normal
        with fade
        "The moment that we make it back home from our date, I know exactly what I want."
        "And I know that [mike.name]'s been spending most of his time behaving like a sensitive guy."
        "But underneath it all, he's still a man - so I know that I can get what I want too!"
        "All I have to do is make it look like it was his idea in the first place..."
        bree.say "Ooh..."
        bree.say "Listen to me yawning!"
        bree.say "I really should get into bed..."
        mike.say "Erm..."
        show mike blush
        mike.say "Maybe I could come along too, [hero.name]?"
        mike.say "You know, like share the bed with you?"
        "I put on my best suspicious expression and study [mike.name] closely."
        bree.say "Hmm..."
        bree.say "I don't know, [mike.name]."
        bree.say "Are you going to behave yourself?"
        "[mike.name] nods eagerly, sensing his chance to change my mind."
        show mike perv
        mike.say "Sure thing, [hero.name]!"
        mike.say "I'll do whatever you say, honest."
        "I nod slowly, still studying him as I do so."
        scene bg bedroom4 with fade
        "But at the same time I open the door to my bedroom."
        "Then I beckon for [mike.name] to follow me inside."
        show mike normal at right with easeinright
        "He hurries to follow me in."
        show mike at right5 with ease
        "Then he steps aside as I close the door behind him."
        bree.say "Make yourself at home."
        bree.say "But the right side of the bed is mine!"
        mike.say "Ah, okay, [hero.name]!"
        mike.say "You'll be joining me soon, right?"
        "I give [mike.name] a quick nod and a smile."
        hide mike with dissolve
        "Then I turn my back and start to get undressed."
        "And the size of the smile grows as I hear what he's doing."
        "[mike.name] noisily pulls of his clothes and tosses them aside."
        "Then I hear him throw himself onto the bed and scuttle under the covers."
        "I wasn't lying to him either - I am getting undressed right now."
        "It's just that I'm doing it at a slower pace."
        "One that's slow enough to make sure he's watching me the whole time!"
        "Stripping from top to bottom and by layers, I can hear [mike.name]'s reaction."
        "I don't let him see too much, leaving most of it to his imagination."
        show mike surprised naked at center, zoomAt(1.25, (640, 940)) with dissolve
        "So when I finally turn around, the sight almost makes his eyes pop out!"
        show mike at startle
        mike.say "WHOA!"
        show mike perv
        mike.say "[hero.name]!"
        bree.say "You like what you see, huh?"
        "[mike.name] nods like a dog being teased with a premium steak."
        "I make a mental note of the fact I can see his shorts on the floor."
        "The sly bastard was probably hoping he's get some action that way."
        "Maybe rub his cock up against my ass when I was half-asleep!"
        "But luckily for him, I have something a lot more energetic in mind."
        bree.say "Well?"
        bree.say "What are you waiting for?"
        bree.say "Pull back the covers and let me in there too!"
        show mike happy
        "[mike.name] does as he's told, moving the bedclothes aside."
        "This shows me at a glance that he really is naked."
        "And that he's really been enjoying my little show too."
        "His cock is practically standing to attention right now!"
        "That's what seals the deal for me."
        "I want that thing inside of me as soon as possible!"
        "With that in mind, I dash across the room."
        "Then I launch myself at [mike.name]."
        show mike surprised naked at center, zoomAt(1.5, (640, 1140))
        with vpunch
        "Totally unprepared, he gasps as I land astride him."
        mike.say "Oof..."
        mike.say "What the..."
        mike.say "I thought you were..."
        mike.say "That you were tired?!?"
        bree.say "Hah!"
        bree.say "Fooled you!"
        bree.say "Now give me what I want, and nobody gets hurt!"
        "Even though he's still surprised, [mike.name] nods."
        "And he doesn't protest as I make a grab for his cock."
        "I give it a nice, hard squeeze, enjoying how it makes his eyes bulge."
    return

label mike_fuck_date_titfuck:
    bree.say "I noticed you staring at these all night, [mike.name]."
    bree.say "So I guess you must like what you see, huh?"
    "I look down at my breasts, then back up at him."
    mike.say "NO!"
    show mike blush
    mike.say "I...I mean yes..."
    mike.say "Look, I know I should be looking you in the eye!"
    mike.say "But..."
    bree.say "Shh!"
    bree.say "It's okay, [mike.name]."
    bree.say "I just wondered if you'd like a closer look?"
    bree.say "That's all..."
    "I'm busy unbuttoning my top as I say all of this."
    "And I hear [mike.name] swallow as more of my cleavage comes into view."
    "By the time they're actually free, he's totally spell-bound."
    show mike perv
    mike.say "B...b...b..."
    bree.say "Breasts, boobies, bangers?"
    bree.say "Whatever you want to call them, [mike.name]!"
    "I keep on smiling as I kneel down in from of him."
    "And [mike.name] offers no resistance as I part his legs and shuffle closer still."
    "He only gasps and jumps a little when he feels my hands on his crotch."
    mike.say "Whoa..."
    bree.say "Settle down, [mike.name]!"
    bree.say "Or else you'll blow it before I'm even started!"
    "[mike.name] nods and leans back on the bed, watching me intensely."
    "Then I reach his cock."
    "I feel a thrill as I wrap my fingers around it."
    "He's already getting nice and hard from my efforts."
    "So pushing him the last bit of the way shouldn't be difficult."
    show breemc titfuck with fade
    "Once I have it out of his pants, I brush my breasts against it."
    "That and making sure the head touches my nipples does the trick."
    "Now he's as hard as I can get him."
    "So it's time to get this show on the road!"
    bree.say "You know why it's okay to stare at my breasts, [mike.name]?"
    mike.say "Uh..."
    mike.say "N...no, [hero.name]!"
    show breemc titfuck tongueout
    bree.say "Because I can't help staring at this!"
    "I give his cock a little squeeze."
    "Just enough to make my point."
    bree.say "I stare at it thinking the same things you do about my breasts."
    bree.say "How big it is, how much I'd like to touch it..."
    show breemc titfuck up
    "I lean forwards as I say this, pushing his cock between my breasts."
    "[mike.name] gasps again, his eyes going wide at the sight."
    "It's hard for me to keep in mind I'm supposed to be treating him."
    "Because the sensation of his cock between them is pretty damn nice."
    "And the look on his face right now is very gratifying indeed!"
    "Trying to keep my mind on the task at hand, I push them together."
    show breemc titfuck down
    "This pins [mike.name]'s cock in place and makes him gasp."
    show breemc titfuck smile
    bree.say "Oh?"
    bree.say "You like that, huh?"
    "[mike.name] nods."
    mike.say "Y...yeah!"
    mike.say "You bet I like it, [hero.name]!"
    "I give him a giggle and a wink."
    show breemc titfuck up
    "And then I get down to work."
    "Moving my breasts up and down, I start to massage [mike.name]'s cock."
    "I confess that I haven't done this a whole lot before now."
    "But the principle's got to be the same as with a hand-job, right?"
    show breemc titfuck down
    "So I keep trying to be firm and yet gentle at the same time."
    "My efforts seem to be paying off too."
    "From the look on [mike.name]'s face, I'd say he's loving it!"
    show breemc titfuck up
    "And the sense of power it's giving me is having an effect too."
    "I'm amazed by how easily I can use my body to keep [mike.name] captivated like this."
    "Seriously, I wonder what else I could make him do?"
    "Anyway..."
    show breemc titfuck down
    "I squeeze a little tighter, and the head pops up between my breasts."
    "Which leaves the both of us looking more than a little surprised!"
    bree.say "Oh!"
    bree.say "Hello there, little guy!"
    mike.say "Hey!"
    mike.say "What do you mean, little?!?"
    "I roll my eyes and shake my head."
    "Unable to believe [mike.name] could be so sensitive at a time like this."
    "But all it takes is a little more effort on my part to placate him."
    "Soon enough his eyes start to glaze over again."
    "And from the sounds he's making, I think something's about to happen."
    mike.say "Urgh..."
    mike.say "Oh shit..."
    show breemc titfuck up tongueout
    "Sure, I have [mike.name]'s cock pinned down between my breasts."
    "But that doesn't mean I'm safe when it finally goes off!"
    with vpunch
    "[mike.name] shoots his load with an impressive display."
    show breemc titfuck down cum closed with vpunch
    "For a moment it's like I have a fountain going off in my face."
    with vpunch
    "And then it's coming down again, striping my breasts with cum!"
    show breemc titfuck tonguecum facecum -cum
    $ mike.love += 2
    "At the same time, [mike.name]'s slumping back on the bed, utterly spent."
    show breemc titfuck swallow -tonguecum
    "I can't help smiling as I release his cock and let it flop onto his pants."
    "He looks pretty helpless, lying there on the bed."
    "I could probably do anything I wanted to him right now."
    show breemc titfuck open smile
    "But then I look down at myself, noting the state of my breasts."
    "Hmm...maybe I should lean myself up before I do anything else."
    $ mike.love += 1
    return

label mike_fuck_date_missionary(sexperience_min):
    if game.days_played % 5 == 0:
        "A string of saliva still joins us as [mike.name] pulls back, taking his own underwear off too before I could attempt to do it for him, tossing it carelessly across the room as his cock springs into the open."
        "I'm mesmerised by it for a brief moment, watching it twitch in the open air, stand to attention, almost flattered at how quickly [mike.name] got quite this pent up."
        "I subtly spread my legs, feeling the moisture between them practically drip onto the bedsheets, and realise that the feeling is mutual."
        "My arousal is almost painful but I almost suspect [mike.name]'s actually is, the two of us staying like that for a few moments as he hastily puts on a condom."
        "Then, with any necessary prep work out of the way, he leans over me once more, our naked bodies pressing together again as I feel his tip begin to trace my entrance."
        scene bg black
        show mike missionary
        with fade
        "It rubs my sensitive slit up, then down, doing so several times apparently just to tease me before shifting himself to rub his entire length at once, coating it in my juices."
        "I whimper as he does this again, and again, bucking my hips into him in a desperate desire to feel him inside me already."
        "Fortunately, it doesn't take long before he happily obliges, pulling back one final time, positioning his cock with his hand, then slowly coming forwards once more."
        show mike missionary vaginal
        "All is silent except the squelch of his cock steadily forcing it's way into my tight passage, my whimpers eventually filling the air to join it."
        "He's large, larger than I'm used to, and my body wraps itself around him tightly enough that he has to put his weight behind his thrust."
        "It hurts, but I bear it, something made ever easier by the unbelievable sensations that come hand in hand with the pain."
        "The deeper he gets the better it feels, his cock exploring and poking my deepest reaches and going further still."
        "My worries that I won't be able to accommodate all of him are quickly relieved when his waist slaps against mine, his cock fully buried within me."
        mike.say "Are. Are you alright?"
        "The first words he's spoken since we arrived ring out in the room, forcing me to open my eyes, meeting his concerned gaze."
        "His arms are trembling, and a bead of sweat is already forming on his brow, threatening to roll down his face at even the slightest movement."
        "Despite having only just broken our kiss his lips look dry, parched, and although there's overwhelming arousal in his gaze, there's equal parts worry and restraint."
        show mike missionary pleasure
        bree.say "I think so."
        show mike missionary normal
        "My voice comes out weak, quiet, barely a squeak in fact, but it's hard to sound convincing with a cock buried deep within you."
        "I can feel how shaky my breath seems to be, and can only imagine what I look like to prompt [mike.name] pausing."
        show mike missionary pleasure
        bree.say "Don't stop."
        "I purposefully whisper that part, attempting to entice him back into action, insisting he shouldn't have stopped in the first place, and thankfully, he responds with a simple nod, pausing for a moment before beginning to move once more."
        show mike missionary at stepback(0.1, 10, 0)
        "He pulls out slowly, but not as slowly as he entered, and he pushes back inside a touch faster still."
        "Despite his size I'm positive that my own arousal is enough for easy entrance. He's trying to be considerate of me."
        show mike missionary at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary at stepback(0.1, 10, 0)
        "I let out a low moan as he begins moving faster still, steadily building up to a rhythm, our hips slapping together over and over as he pumps in and out."
        mike.say "Oh shit. You're so tight."
        "His voice sounds strained, shaky, even those few words difficult to spit out, and yet they send shivers down my spine."
        mike.say "You're wrapping around me so much."
        show mike missionary at stepback(0.1, 10, 0)
        "He continues, leaning forwards so his softer inflection can be heard over my own steadily increasing moans."
        mike.say "The way you're clamping down. You want it, don't you?"
        "I wasn't expecting such a direct question, and at first I don't answer him, too absorbed in the way his hand has just grasped my breast, massaging it as he claims me."
        "Thankfully, he's patient, deciding to gently nibble on my ear as he waits for me to be more vocal outside of the formless cries I've been giving him in earnest."
        bree.say "Yes, I want it, [mike.name]."
        "I myself am surprised at how sultry I sound, but have little time to dwell on the matter as a particularly strong sudden thrust forces a gasp out of me."
        mike.say "You're so sexy, [hero.name]."
        mike.say "I'm so lucky."
        "His voice so close to my ear, all he has to do is whisper to near debilitate me, his soft spoken tone contrasting the way his hips begin to grow ever more violent and frantic."
        "His cock, while large, fits me perfectly, rubbing against every little bump and nook in my wet, sopping cunt, each subtle movement of his hips sending waves crashing over me."
        show mike missionary at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary at stepback(0.1, 10, 0)
        "Not that his movements are even close to being subtle."
        "I can barely form his name thanks to the way that my body seems to have started to disobey me, moving on it's own to begin bucking my hips forwards into [mike.name]'s thrusts."
        "My arms reaching up to wrap around his chest and hold him close as his breath washes across my neck, his lips playfully planting kiss after kiss on my bare skin as he fucks me silly."
        show mike missionary ahegao at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary at stepback(0.1, 10, 0)
        bree.say "[mike.name]. Ah! [mike.name]! It feels so good~!"
        "I manage to take back control, moaning [mike.name]'s name rather than just empty cries, something that the man noticeably seems to enjoy, finding newfound strength to put behind every pump of his hips."
        show mike missionary at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary at stepback(0.1, 10, 0)
        "I find the wind quickly knocked out of me as he begins caring less and less for my comfort, his arousal taking over and beginning to control his actions."
        mike.say "You sound so sexy when you're screaming my name."
        "His voice in my ear alone makes me throw my head back, clutching desperately for something to hold but finding naught but air, and [mike.name]'s back that is, my fingernails digging a little deep."
        bree.say "[mike.name]! I'm close! Oh god! I'm close to cumming!"
        show mike missionary at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary at stepback(0.1, 10, 0)
        "I let my own inhibitions fall too, screaming as loud as I like, calling out over the frantic sounds of our bodies colliding."
        show mike missionary at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary at stepback(0.1, 10, 0)
        "The pressure in my loins keeps steadily building, more and more and more even still, and from the way I feel his rod twitching and his movements becoming less and less practised, his next words don't surprise me."
        mike.say "Fuck, so am I, [hero.name]. Cum! Cum for me!"
        "He doesn't have to tell me twice."
        show mike missionary at stepback(0.1, 10, 0)
        pause 0.15
        show mike missionary creampie with hpunch
        $ mike.impregnate()
        $ mike.love += 1
        "With one final, grand thrust, I feel an explosion, my body shaking within [mike.name]'s grasp as white hot pleasure overcomes me."
        with hpunch
        "I scream in ecstasy, my voice melding with [mike.name]'s own in a perfect, wonderful melody of pure bliss."
        with hpunch
        "His grip of me almost hurts, definitely leaving a mark at least, but my nails digging into him tell a similar story, and through the haze of a quickly fading orgasm I don't care."
        with hpunch
        "He collapses on-top of me, the two of us panting heavily."
        "His cock is still inside me, and for a moment I wonder if he'll even pull out before he answers the question with a quiet grunt, freeing his cock from the prison of my pussy."
        show mike missionary -vaginal pleasure
        "I can see from here just how much semen is pooled inside the condom, but apparently [mike.name] caught me looking, and a devious look floats across his face as he slips the rubber off his cock."
        "He holds it in front of my face, letting me get a good look at just how much is stored within, before smirking, leaning in so his ears are next to my ear once again."
        mike.say "Can't let this go to waste now, can we?"
        "I look between the rubber, then him, before grinning in return."
        mike.say "That'd be such a shame."
        "I open my mouth wide, sticking my tongue out and bracing myself as [mike.name] slowly pours the thick, heavy, creamy contents down my throat, it's salty and unfamiliar taste lingering long after I force myself to swallow it all."
        "Well aware the taste still lingers on my lips, I quickly swivel and give [mike.name] a quick kiss."
        "He laughs, but wipes his mouth with the back of his hand, pulling a slightly disgusted face as he does so, apparently not having enjoyed the brief payback."
        mike.say "You're amazing, you know that?"
        "My cheeks begin to feel hot, now of all times surprisingly enough, so I shut him up with another kiss."
        bree.say "So are you."
    else:
        "Then I throw myself backwards onto the mattress."
        "I beckon [mike.name] over with one finger and what I hope is a wicked grin."
        "It seems to work, as he hurries after me, climbing onto the bed."
        "I can't help biting my lip as he lowers himself down to lie atop me."
        "This is going to be an interesting ride!"
        menu:
            "Guide him to my pussy":
                "I reach up, wrapping my arms around [mike.name]'s neck."
                "Looking him in the eye as he settles himself."
                "I keep catching glimpses of what's going on down there."
                "And I have to say it's more than a little impressive!"
                "I'm kind of getting giddy to see how this will feel."
                show mike missionary
                call check_condom_usage (mike) from _call_check_condom_usage_115
                if _return == False:
                    return "leave_without_gain"
                "I feel the head of [mike.name]'s cock brushing against me down there."
                "The sensation is pretty nice, and it makes me sigh just a little."
                "He stops at the sound, looking at me with concern in his eyes."
                "I nod, trying to urge him on and reassure him at the same time."
                "And it seems to work, as he looks instantly more confident."
                "Just to be sure, I reach down with one hand, taking hold of him."
                "Then I guide him home, pressing the head against the folds of my pussy."
                "The grip I have on [mike.name] seems to take him a little by surprise."
                show mike missionary at stepback(0.1, 10, 0)
                "He shudders and pushes himself forwards without thinking."
                "But that's just enough to make a difference, enough to get him inside."
                show mike missionary vaginal
                if CONDOM:
                    show mike missionary vaginal condom
                bree.say "Mmm..."
                show mike missionary pleasure
                bree.say "Oh yeah..."
                show mike missionary normal
                mike.say "[hero.name[0]]...[hero.name]..."
                mike.say "You like that?"
                show mike missionary pleasure
                bree.say "Oh god, [mike.name]..."
                bree.say "I love it!"
                bree.say "Gimmie some more, please?"
                show mike missionary normal
                "Sure, you always want to big a guy up to get him motivated."
                "But right now I'm not telling [mike.name] anything but the truth."
                "He feels pretty damn good inside of me."
                show mike missionary at stepback(0.1, 10, 0)
                "And as he hurries to do as I ask, it just gets better!"
                "I can almost feel the eagerness and apprehension battling it out in him."
                show mike missionary at stepback(0.1, 10, 0)
                "Which means that he's doing all he can to please me."
                "But at the same time he's keeping himself under control too."
                show mike missionary at stepback(0.1, 10, 0)
                "This means that [mike.name] takes his time, yet doesn't spare any effort."
                "Normally I'd be all over this, really trying to take control."
                "But almost the moment that I think I want something, [mike.name] does it."
                "I feel that I want him to go harder or deeper."
                "Then he makes it happen."
                "I want his hands on me somewhere."
                show mike missionary arm
                "Then they're there a second later."
                "All I have to do is lie back and leave him to it!"
                show mike missionary at stepback(0.1, 10, 0)
                pause 0.15
                show mike missionary at stepback(0.1, 10, 0)
                "[mike.name] takes care of everything."
                "Sometimes he even seems to know what I want before I do myself!"
                show mike missionary at stepback(0.1, 10, 0)
                pause 0.15
                show mike missionary at stepback(0.1, 10, 0)
                "And when I can feel that I'm about to cum, he senses it too."
                show mike missionary pleasure
                mike.say "Ah..."
                mike.say "[hero.name]..."
                show mike missionary at stepback(0.1, 10, 0)
                pause 0.15
                show mike missionary at stepback(0.1, 10, 0)
                bree.say "Yeah..."
                bree.say "I know!"
                call cum_reaction (mike, 'vaginal', sexperience_min) from _call_cum_reaction_200
                if _return == "vaginal_outside":
                    bree.say "We didn't...use protection..."
                    bree.say "Remember?"
                    bree.say "Pull out...now!"
                    "[mike.name] nods eagerly, leaping to do as he's told."
                    show mike missionary -vaginal ahegao with hpunch
                    "He pulls his cock out of me, and that's what does it."
                    with hpunch
                    "I feel it happen deep inside of me, and it hits me like a wave."
                    show mike missionary cumshot cum onbelly with hpunch
                    "At the same time, [mike.name] is shooting his load over me."
                    show mike missionary -cumshot onboobs with hpunch
                    "And I find myself clinging to him for dear life!"
                    $ mike.love += 1
                    "[mike.name]'s arms and legs give way almost the same moment he's done."
                    "He collapses half atop me and half on the bed to my side."
                    "Neither of us makes an effort to move or even speak."
                    "It's enough to lie there in silence, still feeling the afterglow."
                elif _return == "vaginal_condom":
                    bree.say "We...used protection..."
                    bree.say "Remember?"
                    bree.say "Keep...going!"
                    "[mike.name] nods eagerly, leaping to do as he's told."
                    "And that last little bit of effort really makes a difference."
                    "But what surprises me is that [mike.name] cums before I do!"
                    with hpunch
                    "I feel it happen deep inside of me, and it hits me like a wave."
                    show mike missionary ahegao with hpunch
                    "My own orgasm is that much more intense as a result."
                    $ mike.love += 2
                    with hpunch
                    "And I find myself clinging to him for dear life!"
                    "[mike.name]'s arms and legs give way almost the same moment he's done."
                    "He collapses half atop me and half on the bed to my side."
                    "Neither of us makes an effort to move or even speak."
                    "It's enough to lie there in silence, still feeling the afterglow."
                elif _return == "vaginal_inside_mad":
                    "What surprises me is that [mike.name] cums before I do!"
                    show mike missionary creampie with hpunch
                    "I feel it happen deep inside of me, and it hits me like a wave."
                    with hpunch
                    "My own orgasm is that much more intense as a result."
                    show mike missionary ahegao with hpunch
                    "And I find myself clinging to him for dear life!"
                    "But then I see the look on his face."
                    $ mike.love -= 5
                    $ mike.impregnate()
                    mike.say "[hero.name[0]]...[hero.name]..."
                    mike.say "Are you on the pill or something?"
                    mike.say "Because if not, we just fucked up!"
                else:
                    "What surprises me is that [mike.name] cums before I do!"
                    show mike missionary creampie with hpunch
                    "I feel it happen deep inside of me, and it hits me like a wave."
                    with hpunch
                    "My own orgasm is that much more intense as a result."
                    with hpunch
                    "And I find myself clinging to him for dear life!"
                    show mike missionary ahegao with hpunch
                    "[mike.name]'s arms and legs give way almost the same moment he's done."
                    $ mike.love += 5
                    $ mike.impregnate()
                    "He collapses half atop me and half on the bed to my side."
                    "Neither of us makes an effort to move or even speak."
                    "It's enough to lie there in silence, still feeling the afterglow."
            "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
                "I reach up, wrapping my arms around [mike.name]'s neck."
                "Looking him in the eye as he settles himself."
                "I keep catching glimpses of what's going on down there."
                "And I have to say it's more than a little impressive!"
                "I'm kind of getting giddy to see how this will feel."
                show mike missionary
                "I feel the head of [mike.name]'s cock brushing against me down there."
                "The sensation is pretty nice, and it makes me sigh just a little."
                "He stops at the sound, looking at me with concern in his eyes."
                "I nod, trying to urge him on and reassure him at the same time."
                "And it seems to work, as he looks instantly more confident."
                "Just to be sure, I reach down with one hand, taking hold of him."
                "Then I guide him home, pressing the head between my buttocks."
                "The grip I have on [mike.name] seems to take him a little by surprise."
                "He shudders and looks at me for reassurance."
                show mike missionary anal
                mike.say "Where...where are you putting it, [hero.name]?"
                mike.say "That feels like..."
                bree.say "My ass?"
                bree.say "That's where I want it, [mike.name]."
                bree.say "If you can deal with that?"
                mike.say "Uh...sure, [hero.name] - of course!"
                "[mike.name] hurries to push inside, eager to please me."
                "And I help to guide him home as he pushes against my muscles."
                "There's just enough resistance to make me gasp."
                "Just enough pain to spice up the pleasure too."
                show mike missionary at stepback(0.1, 10, 0)
                "And then he begins to win the battle, inching his way inside me."
                bree.say "Mmm..."
                show mike missionary pleasure
                bree.say "Oh yeah..."
                show mike missionary normal
                mike.say "[hero.name[0]]...[hero.name]..."
                mike.say "You like that?"
                show mike missionary pleasure
                bree.say "Oh god, [mike.name]..."
                bree.say "I love it!"
                bree.say "Gimmie some more, please?"
                show mike missionary normal
                "Sure, you always want to big a guy up to get him motivated."
                "But right now I'm not telling [mike.name] anything but the truth."
                "He feels pretty damn good inside of me."
                show mike missionary at stepback(0.1, 10, 0)
                "And as he hurries to do as I ask, it just gets better!"
                "I can almost feel the eagerness and apprehension battling it out in him."
                show mike missionary at stepback(0.1, 10, 0)
                "Which means that he's doing all he can to please me."
                "But at the same time he's keeping himself under control too."
                show mike missionary at stepback(0.1, 10, 0)
                "This means that [mike.name] takes his time, yet doesn't spare any effort."
                "Normally I'd be all over this, really trying to take control."
                "But almost the moment that I think I want something, [mike.name] does it."
                "I feel that I want him to go harder or deeper."
                "Then he makes it happen."
                "I want his hands on me somewhere."
                show mike missionary arm
                "Then they're there a second later."
                "All I have to do is lie back and leave him to it!"
                "[mike.name] takes care of everything."
                "Sometimes he even seems to know what I want before I do myself!"
                show mike missionary at stepback(0.1, 10, 0)
                pause 0.15
                show mike missionary at stepback(0.1, 10, 0)
                "And when I can feel that I'm about to cum, he senses it too."
                show mike missionary pleasure
                mike.say "Ah..."
                mike.say "[hero.name]..."
                show mike missionary at stepback(0.1, 10, 0)
                pause 0.15
                show mike missionary at stepback(0.1, 10, 0)
                bree.say "Yeah..."
                bree.say "I know!"
                call cum_reaction (mike, 'anal', sexperience_min) from _call_cum_reaction_282
                if _return == 'anal_inside':
                    bree.say "We...used may ass..."
                    bree.say "Remember?"
                    bree.say "Keep...going!"
                    "[mike.name] nods eagerly, leaping to do as he's told."
                    "And that last little bit of effort really makes a difference."
                    show mike missionary creampie with hpunch
                    "But what surprises me is that [mike.name] cums before I do!"
                    with hpunch
                    "I feel it happen deep inside of me, and it hits me like a wave."
                    show mike missionary ahegao with hpunch
                    "My own orgasm is that much more intense as a result."
                    $ mike.love += 2
                    "And I find myself clinging to him for dear life!"
                elif _return == 'anal_outside':
                    bree.say "I want...you to..."
                    bree.say "Pull out...now!"
                    "[mike.name] nods eagerly, leaping to do as he's told."
                    show mike missionary -vaginal ahegao with hpunch
                    "He pulls his cock out of me, and that's what does it."
                    with hpunch
                    "I feel it happen deep inside of me, and it hits me like a wave."
                    show mike missionary cumshot cum onbelly with hpunch
                    "At the same time, [mike.name] is shooting his load over me."
                    show mike missionary -cumshot onboobs with hpunch
                    "And I find myself clinging to him for dear life!"
                    $ mike.love += 1
                with hpunch
                "[mike.name]'s arms and legs give way almost the same moment he's done."
                "He collapses half atop me and half on the bed to my side."
                "Neither of us makes an effort to move or even speak."
                "It's enough to lie there in silence, still feeling the afterglow."
    return

label mike_fuck_date_spoon(sexperience_min):
    show cuddle mike with fade
    "I feel [mike.name] slide in right behind me."
    "He doesn't make any effort to keep to his side of the bed."
    "Instead he wraps himself around me, so that we're spooning."
    "I don't object for a second, because the feeling is so nice."
    "He's warm and his body's firm, wrapping around me under the covers."
    "It feels like he's protecting me as we sleep, keeping me warm too!"
    "Actually..."
    "It's kind of making me feel pissed that I said I was so tired."
    "Because the way his cock feels right now is pretty good too!"
    bree.say "Ah, [mike.name]..."
    mike.say "Yeah, [hero.name]?"
    bree.say "You know when I said I was dead tired?"
    mike.say "Yeah, [hero.name] - me too."
    bree.say "Well...I might have been telling a little lie there."
    bree.say "I think I have just a little bit left in me."
    mike.say "Yeah, [hero.name] - me too."
    mike.say "About being tired and having a little left in the tank."
    bree.say "So..."
    bree.say "You want to..."
    mike.say "Uh-huh."
    mike.say "But on one condition."
    bree.say "Which is?"
    mike.say "Neither of us has to move."
    bree.say "Works for me!"
    "Without another word, I slide my hand around behind my back."
    scene mike spoon with fade
    "And I use it to stroke [mike.name]'s cock through his shorts."
    "I'm surprised to find that it's already about halfway there."
    "So either he was lying about being sleepy just now."
    "Or else his body was conspiring against him!"
    "Not that it matters either way."
    "[mike.name] soon responds to my touch, his cock getting ever harder."
    "Then I feel his hand on my body too."
    "They're on my stomach, then tracing a line upwards."
    "[mike.name] finds my breasts, beginning to caress them a moment later."
    "Now it's my turn to feel my body responding."
    "The touch of his fingers makes my nipples stiffen."
    "And I bite my lip as the sensation makes my pussy begin to stir too."
    "Both fly out from under the covers, and then we're down to it for real!"
    menu:
        "Guide him to my pussy":
            "Now I have a good, firm hold on [mike.name]'s cock."
            "And it's more than ready for what we have in mind."
            call check_condom_usage (mike) from _call_check_condom_usage_114
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show mike spoon condom
            "I'm eager not to waste any time here."
            "Not when we're both on the verge of falling asleep."
            "But I also don't want to seem to desperate either."
            "So I force myself to go as slowly as I dare."
            "[mike.name] seems happy to lie back and let me guide his cock home."
            "He only starts to move once he knows that I have it where I want it."
            "And even then his motions are slow and gentle."
            "That suits me fine, waking me up down there nice and steady."
            "[mike.name] pushes himself against my back, working his cock against me."
            bree.say "Mmm..."
            bree.say "That's good..."
            bree.say "Just like that, yeah?"
            "I feel him nodding eagerly at my instructions."
            "Then I feel the actual sensations of him acting on them too."
            "And somehow I know the exact moment it's going to happen."
            "Just as I predicted, I can feel myself opening up to him."
            "It's slow and sensual, just like it needs to be."
            show mike spoon vaginal
            "Every little bit of progress he makes is a delight all of its own."
            mike.say "Oh, [hero.name]..."
            mike.say "That feels..."
            bree.say "Ah..."
            bree.say "I know, I know..."
            bree.say "Just keep doing that to me!"
            show mike spoon mouth_pain
            "[mike.name] does just as I ask, like he's taken a fucking oath or something!"
            "I feel him start moving inside of me, slowly and with infinite care."
            "And I wasn't making shit up to save hurting his feelings either."
            "What he's doing to me feels pretty fucking amazing."
            "The fact I'm so beat means all I can do is lie here and take it."
            "[mike.name]'s cock is turning my fatigue into something else entirely."
            "It's like he's melting me with every move he makes."
            "I'm not feeling tired anymore, instead I feel like I'm drifting into a state of pure bliss."
            "But that's not all he does to me."
            "Somehow [mike.name] finds the energy to keep his hands playing over my helpless body."
            "He keeps on caressing my breasts, kissing my neck too."
            "At times I can't help wondering if one or even both of us has actually fallen asleep."
            "And our bodies have just kept going on auto-pilot as our minds wander off into slumber."
            "The only chance of us waking up a little comes towards the end."
            show mike spoon eyes_pleasure mouth_pleasure
            "And that's when I start to feel a subtle change in [mike.name]'s movements."
            bree.say "Wuh..."
            bree.say "[mike.name], are you gonna..."
            mike.say "Y...yeah, [hero.name]..."
            mike.say "I kinda think I am!"
            call cum_reaction (mike, 'vaginal', sexperience_min) from _call_cum_reaction_201
            if _return == "vaginal_outside":
                "Remembering at the last moment we didn't use a condom, I take action."
                "[mike.name]'s too sleepy to object to me wriggling off his cock."
                show mike spoon out with hpunch
                "He just moans as it slides out of me and he starts to cum."
                with hpunch
                "I feel it shooting up my naked back."
                show mike spoon cum with hpunch
                $ mike.love += 2
                "Then I surrender myself to the sensation."
                show mike spoon eyes_ahegao mouth_ahegao with hpunch
                "And soon enough, I can feel myself cumming too."
            elif _return == "vaginal_condom":
                "I just smile and push myself backwards."
                "This drives [mike.name] even deeper into me."
                with hpunch
                "And it makes sure he shoots his load while he is too."
                show mike spoon cum with hpunch
                $ mike.love += 1
                "I silently smile at the knowledge we used a condom."
                with hpunch
                "Then I surrender myself to the sensation."
                show mike spoon eyes_ahegao mouth_ahegao with hpunch
                "And soon enough, I can feel myself cumming too."
            elif _return == "vaginal_inside_mad":
                with hpunch
                "[mike.name]'s deep inside me when I feel him lose it."
                show mike spoon cum with hpunch
                "I surrender myself to the sensation."
                show mike spoon eyes_ahegao mouth_ahegao with hpunch
                "And soon enough, I can feel myself cumming too."
                mike.say "Urgh..."
                mike.say "I hope you went on the pill, [hero.name]!"
                mike.say "Or this is one of your safe days!"
                $ mike.love -= 5
                $ mike.impregnate()
                bree.say "What are you..."
                bree.say "Oh shit!"
                bree.say "We didn't use a condom!"
                "For the first time since we got back, I'm totally awake."
                "And [mike.name] seems to be coming round to why as well!"
            else:
                with hpunch
                "[mike.name]'s deep inside me when I feel him lose it."
                show mike spoon cum with hpunch
                "I surrender myself to the sensation."
                show mike spoon eyes_ahegao mouth_ahegao with hpunch
                "And soon enough, I can feel myself cumming too."
                mike.say "Urgh..."
                mike.say "I hope you went on the pill, [hero.name]!"
                mike.say "Or this is one of your safe days!"
                $ mike.love += 5
                $ mike.impregnate()
                "The sensation pushes me over the edge, and I lose it too."
                "Each of us feels wave after wave of pleasure."
                "Pushed ever higher by the orgasm of the other."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "Now I have a good, firm hold on [mike.name]'s cock."
            "And it's more than ready for what we have in mind."
            "I'm eager not to waste any time here."
            "Not when we're both on the verge of falling asleep."
            "But I also don't want to seem to desperate either."
            "So I force myself to go as slowly as I dare."
            "[mike.name] seems happy to lie back and let me guide his cock home."
            "He only starts to move once he knows that I have it where I want it."
            "And even then his motions are slow and gentle."
            "That suits me fine, waking me up down there nice and steady."
            "[mike.name] pushes himself against my back, working his cock against me."
            bree.say "Mmm..."
            bree.say "That's good..."
            bree.say "Just like that, yeah?"
            show mike spoon anal eyes_surprised mouth_pain
            mike.say "Erm..."
            mike.say "Wait a minute..."
            mike.say "Isn't that your ass?!?"
            bree.say "Yeah, [mike.name]..."
            bree.say "I just kinda want it in there tonight!"
            bree.say "Okay?"
            mike.say "Are you sure?"
            bree.say "I'm sure - go ahead and put it up there!"
            "I feel him nodding eagerly at my instructions."
            "Then I feel the actual sensations of him acting on them too."
            "And somehow I know the exact moment it's going to happen."
            "Just as I predicted, I can feel myself opening up to him."
            "It's slow and sensual, just like it needs to be."
            "Every little bit of progress he makes is a delight all of its own."
            mike.say "Oh, [hero.name]..."
            mike.say "That feels..."
            bree.say "Ah..."
            bree.say "I know, I know..."
            bree.say "Just keep doing that to me!"
            "[mike.name] does just as I ask, like he's taken a fucking oath or something!"
            "I feel him start moving inside of me, slowly and with infinite care."
            "And I wasn't making shit up to save hurting his feelings either."
            "What he's doing to me feels pretty fucking amazing."
            "The fact I'm so beat means all I can do is lie here and take it."
            "[mike.name]'s cock is turning my fatigue into something else entirely."
            "It's like he's melting me with every move he makes."
            "I'm not feeling tired anymore, instead I feel like I'm drifting into a state of pure bliss."
            "But that's not all he does to me."
            "Somehow [mike.name] finds the energy to keep his hands playing over my helpless body."
            "He keeps on caressing my breasts, kissing my neck too."
            "At times I can't help wondering if one or even both of us has actually fallen asleep."
            "And our bodies have just kept going on auto-pilot as our minds wander off into slumber."
            "The only chance of us waking up a little comes towards the end."
            "And that's when I start to feel a subtle change in [mike.name]'s movements."
            show mike spoon eyes_closed mouth_pleasure
            bree.say "Wuh..."
            bree.say "[mike.name], are you gonna..."
            mike.say "Y...yeah, [hero.name]..."
            mike.say "I kinda think I am!"
            call cum_reaction (mike, 'anal', sexperience_min) from _call_cum_reaction_202
            if _return == 'anal_inside':
                "I just smile and push myself backwards."
                "This drives [mike.name] even deeper into me."
                "And it makes sure he shoots his load while he is too."
                show mike spoon cum with hpunch
                $ mike.love += 2
                "I silently smile, smug in the knowledge I made him fuck my ass."
                with hpunch
                "Then I surrender myself to the sensation."
                show mike spoon eyes_ahegao mouth_ahegao with hpunch
                "And soon enough, I can feel myself cumming too."
            elif _return == 'anal_outside':
                "Feeling a little evil, I pull [mike.name] out of me at the last possible moment."
                show mike spoon -anal
                $ mike.sub += 1
                "[mike.name]'s too sleepy to object to me wriggling off his cock."
                "He just moans as it slides out of me and he starts to cum."
                show mike spoon cum with hpunch
                "I feel it shooting up my naked back."
                with hpunch
                "Then I surrender myself to the sensation."
                show mike spoon eyes_ahegao mouth_ahegao with hpunch
                "And soon enough, I can feel myself cumming too."
    return

label mike_fuck_date_doggy(sexperience_min):
    scene mike doggy
    show mike doggy bedroom4
    with fade
    "On my hands and knees, I crawl around on the bed."
    "And once I have my back to him, I finally stop and look over my shoulder."
    bree.say "So what are you waiting for, huh?"
    bree.say "Get over here and ride me already!"
    "I add a pretty over the top butt-wiggle to underline my point."
    "And it seems to have the desired effect."
    "[mike.name] reacts like he's been slapped across the face."
    "Then he hurries to close the distance between us."
    "I turn my head as I feel [mike.name] land on the bed."
    "Then I can't help yelping as he grabs hold of my ass."
    bree.say "Ahh..."
    bree.say "Whoa..."
    bree.say "Hello there!"
    "I just have time to hear [mike.name] chuckle."
    "Then he pushes himself forwards."
    "And I feel his cock jutting between my thighs!"
    bree.say "Oh..."
    bree.say "And hello to you too!"
    menu:
        "Guide him to my pussy":
            "I like that [mike.name]'s playing along with the mood I'm trying to create here."
            "He's being as cocky as I am, pushing the envelope whenever the chance presents itself."
            "But I don't want to let him catch me off-guard and take total control here."
            "So I reach down and take a firm hold of his cock, squeezing it for good measure."
            mike.say "Urgh..."
            mike.say "Whoa, [hero.name]!"
            mike.say "Be a little more gentle, okay?"
            bree.say "Ah, don't be such a baby, [mike.name]!"
            bree.say "Trust me - you're gonna love this!"
            call check_condom_usage (mike) from _call_check_condom_usage_116
            if _return == False:
                return "leave_without_gain"
            "Not wanting to waste another moment, I decide to get things moving."
            "Which involves me keeping a tight hold on [mike.name]'s cock."
            "And I use this to rub it against the lips of my pussy."
            "I'm not being particularly subtle about it either."
            "By now my body's starting to ache for it pretty badly."
            "And the only thing that's going to fix that is getting him inside of me!"
            bree.say "Mmm..."
            bree.say "I'm getting wet, [mike.name]..."
            bree.say "I can feel it happening right now!"
            mike.say "Oh man..."
            mike.say "I...I think I can feel it too!"
            mike.say "[hero.name] - I want you so badly!"
            "I can hear the desperation in [mike.name]'s voice as I tease him."
            "He's already champing at the bit to get going."
            "And the thought is more than enough to make me melt."
            mike.say "Oh fuck..."
            mike.say "[hero.name]!"
            bree.say "Oooh..."
            bree.say "Oh god!"
            "I can't say anything more than that."
            "And I can't keep up the teasing any longer."
            if CONDOM:
                show mike doggy condom vaginal
            else:
                show mike doggy vaginal
            "That's because I feel the lips of my pussy part and let him in."
            "As [mike.name]'s cock inches it's way into me, everything changes."
            "I go from feeling like I'm the one in control to losing it altogether."
            "And by the time he's filling me up, I'm totally at his mercy."
            "[mike.name] doesn't seem to need my encouragement any more."
            "In fact, he's growing in confidence with each passing second."
            "I can feel him starting to thrust in and out of me."
            "Getting faster and bolder with each movement of his body."
            show mike doggy speed
            "All I can do is lower my head in submission, nodding it too."
            "Before now, I felt like [mike.name]'s hands were clinging onto me almost in desperation."
            "But now the sensation is more like he's holding me in place, pinning me to the bed."
            "Is this what it feels like to be an animal?"
            show mike doggy scream
            "A beast captured and broken by a human set on bending the creature to their will?"
            "I always thought that would suck, be a huge turn-off."
            "But the position [mike.name]'s got me in right now..."
            "It's making me feel sensual as hell!"
            "My entire body is buzzing."
            "My skin feels like it's on fire."
            "My pussy..."
            "Well, let's just say that's about to go supernova!"
            bree.say "[mike.name[0]]...[mike.name]..."
            bree.say "I'm...gonna..."
            bree.say "Gonna cum!"
            mike.say "Shit..."
            mike.say "Me too!"
            call cum_reaction (mike, 'vaginal', sexperience_min) from _call_cum_reaction_203
            if _return == "vaginal_outside":
                bree.say "Pull out now!"
                bree.say "Before it's too late!"
                "[mike.name] scrambles to do as he's told."
                "And much to my relief, he manages it."
                "He cums just a few seconds later."
                show mike doggy -vaginal cumshot with hpunch
                "I feel the warm drops of cum spattering my back and buttocks."
                "The sensation pushes me over the edge, and I lose it too."
                show mike doggy -cumshot cumonass with hpunch
                "Each of us feels wave after wave of pleasure."
                with hpunch
                "Pushed ever higher by the orgasm of the other."
                "Once [mike.name] lets go of me, there's nothing to hold me up anymore."
                "So I slump forward onto the pillows, my muscles turning to jelly."
                "[mike.name] doesn't fare any better either, landing right beside me."
                "And pretty soon there's nothing to worry about save for falling asleep."
                $ mike.love += 2
            elif _return == "vaginal_condom":
                "[mike.name] makes good on his promise just a few seconds later."
                show mike doggy vaginal condom with hpunch
                "Neither of us panics as he shoots his load into me."
                "And that's because we remembered to use a condom."
                "Instead the experience is a perfect ending to what came before."
                "The sensation pushes me over the edge, and I lose it too."
                with hpunch
                "Each of us feels wave after wave of pleasure."
                with hpunch
                "Pushed ever higher by the orgasm of the other."
                "Once [mike.name] lets go of me, there's nothing to hold me up anymore."
                "So I slump forward onto the pillows, my muscles turning to jelly."
                "[mike.name] doesn't fare any better either, landing right beside me."
                "And pretty soon there's nothing to worry about save for falling asleep."
                $ mike.love += 1
            elif _return == "vaginal_inside_mad":
                "[mike.name] makes good on his promise just a few seconds later."
                show mike doggy vaginal cuminpussy with hpunch
                "Neither of us panics as he shoots his load into me."
                "The sensation pushes me over the edge, and I lose it too."
                with hpunch
                "Each of us feels wave after wave of pleasure."
                with hpunch
                "Pushed ever higher by the orgasm of the other."
                $ mike.impregnate()
                "But then we both seem to remember something in the same moment."
                bree.say "The condom!"
                mike.say "We didn't use one!"
                mike.say "Oh shit!"
                $ mike.love -= 5
                bree.say "Oh shit indeed!"
            else:
                "[mike.name] makes good on his promise just a few seconds later."
                show mike doggy vaginal cuminpussy with hpunch
                "Neither of us panics as he shoots his load into me."
                "The sensation pushes me over the edge, and I lose it too."
                $ mike.love += 5
                $ mike.impregnate()
                with hpunch
                "Each of us feels wave after wave of pleasure."
                with hpunch
                "Pushed ever higher by the orgasm of the other."
                "Once [mike.name] lets go of me, there's nothing to hold me up anymore."
                "So I slump forward onto the pillows, my muscles turning to jelly."
                "[mike.name] doesn't fare any better either, landing right beside me."
                "And pretty soon there's nothing to worry about save for falling asleep."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "I like that [mike.name]'s playing along with the mood I'm trying to create here."
            "He's being as cocky as I am, pushing the envelope whenever the chance presents itself."
            "But I don't want to let him catch me off-guard and take total control here."
            "So I reach down and take a firm hold of his cock, squeezing it for good measure."
            mike.say "Urgh..."
            mike.say "Whoa, [hero.name]!"
            mike.say "Be a little more gentle, okay?"
            bree.say "Ah, don't be such a baby, [mike.name]!"
            bree.say "Trust me - you're gonna love this!"
            "Not wanting to waste another moment, I decide to get things moving."
            "Which involves me keeping a tight hold on [mike.name]'s cock."
            "And I use this to push it between the cheeks of my ass."
            "I'm not being particularly subtle about it either."
            "By now my body's starting to ache for it pretty badly."
            "And the only thing that's going to fix that is getting him inside of me!"
            bree.say "Mmm..."
            bree.say "I'm getting wet, [mike.name]..."
            bree.say "I can feel it happening right now!"
            mike.say "Oh man..."
            mike.say "I...I think I can feel it too!"
            mike.say "[hero.name] - I want you so badly!"
            mike.say "But are you sure you want it up the ass?!?"
            "I can hear the desperation in [mike.name]'s voice as I tease him."
            "He's already champing at the bit to get going."
            show mike doggy anal
            "And the thought is more than enough to make me melt."
            bree.say "Yeah, that's exactly where I want it!"
            mike.say "Oh fuck..."
            mike.say "[hero.name]!"
            bree.say "Oooh..."
            bree.say "Oh god!"
            "I can't say anything more than that."
            "And I can't keep up the teasing any longer."
            "That's because I feel the muscles of my ass part and let him in."
            "As [mike.name]'s cock inches it's way into me, everything changes."
            "I go from feeling like I'm the one in control to losing it altogether."
            "And by the time he's filling me up, I'm totally at his mercy."
            "[mike.name] doesn't seem to need my encouragement any more."
            "In fact, he's growing in confidence with each passing second."
            "I can feel him starting to thrust in and out of me."
            "Getting faster and bolder with each movement of his body."
            "All I can do is lower my head in submission, nodding it too."
            "Before now, I felt like [mike.name]'s hands were clinging onto me almost in desperation."
            "But now the sensation is more like he's holding me in place, pinning me to the bed."
            show mike doggy anal scream
            "Is this what it feels like to be an animal?"
            "A beast captured and broken by a human set on bending the creature to their will?"
            "I always thought that would suck, be a huge turn-off."
            "But the position [mike.name]'s got me in right now..."
            "It's making me feel sensual as hell!"
            "My entire body is buzzing."
            "My skin feels like it's on fire."
            "My ass..."
            show mike doggy anal speed
            "Well, let's just say that's about to go supernova!"
            bree.say "[mike.name[0]]...[mike.name]..."
            bree.say "I'm...gonna..."
            bree.say "Gonna cum!"
            mike.say "Shit..."
            mike.say "Me too!"
            call cum_reaction (mike, 'anal', sexperience_min) from _call_cum_reaction_204
            if _return == "anal_inside":
                "[mike.name] makes good on his promise just a few seconds later."
                "Neither of us panics as he shoots his load into me."
                show mike doggy anal cuminass with hpunch
                "And that's another bonus of him doing me up the ass."
                "Instead the experience is a perfect ending to what came before."
                with hpunch
                "The sensation pushes me over the edge, and I lose it too."
                with hpunch
                "Each of us feels wave after wave of pleasure."
                "Pushed ever higher by the orgasm of the other."
                "Once [mike.name] lets go of me, there's nothing to hold me up anymore."
                "So I slump forward onto the pillows, my muscles turning to jelly."
                "[mike.name] doesn't fare any better either, landing right beside me."
                "And pretty soon there's nothing to worry about save for falling asleep."
                $ mike.love += 2
            elif _return == "anal_outside":
                bree.say "Pull out now!"
                bree.say "Before it's too late!"
                "[mike.name] scrambles to do as he's told."
                show mike doggy -anal cumshot with vpunch
                "And much to my relief, he manages it."
                "He cums just a few seconds later."
                "I feel the warm drops of cum spattering my back and buttocks."
                "The sensation pushes me over the edge, and I lose it too."
                with hpunch
                "Each of us feels wave after wave of pleasure."
                show mike doggy cumonass -cumshot with vpunch
                "Pushed ever higher by the orgasm of the other."
                "Once [mike.name] lets go of me, there's nothing to hold me up anymore."
                "So I slump forward onto the pillows, my muscles turning to jelly."
                "[mike.name] doesn't fare any better either, landing right beside me."
                "And pretty soon there's nothing to worry about save for falling asleep."
                $ mike.sub += 1
    return

label mike_fuck_date_doggy_rough(sexperience_min):
    bree.say "Come and get it, [mike.name]!"
    bree.say "And don't be too gentle about it either, okay?"
    "[mike.name] nods eagerly as he clambers onto the bed."
    "Then I feel his hands grabbing hold of me."
    "And a shiver of excitement passes through my body."
    "Because it looks like I'm about to get exactly what I want!"
    menu:
        "Guide him to my pussy":
            "[mike.name]'s grip on me is pretty tight."
            "And I can feel his cock pressing against my ass too!"
            call check_condom_usage (mike) from _call_check_condom_usage_120
            if _return == False:
                return "leave_without_gain"
            show mike rough doggy
            if CONDOM:
                show mike rough doggy condom
            with fade
            "Now I'm starting to wonder what he made of my request."
            "What he'll make of me asking him not to be too gentle."
            "And then, as if he's reading my mind, I find out."
            "Because I can feel a hand reaching out and grabbing my hair."
            "[mike.name] twines his fingers into it, getting a damn good hold."
            "And then he gives it an experimental tug."
            bree.say "Oh yeah!"
            show mike rough doggy pleasure
            bree.say "That's what I'm talking about!"
            mike.say "Oh...I..."
            mike.say "It is?"
            mike.say "I mean...yeah, of course it is!"
            "I try as hard as I can not to chuckle at [mike.name]'s attempt at bravado."
            "But it's so cute to hear him trying to style himself as the big man."
            "So I decide that I'm going to let him have his moment in the spotlight."
            bree.say "Oh, [mike.name]!"
            bree.say "You're SO manly!"
            mike.say "You bet I am, [hero.name]!"
            "It's right about now that I choose to take hold of [mike.name]'s cock."
            "And I press it hard against the lips of my pussy."
            show mike rough doggy normal vaginal
            "[mike.name]'s pulling on my hair at the same time."
            "And by now I'm more than ready for him."
            "So there's almost no resistance from me, nothing to stop him sinking in."
            "All it takes is one more lurch forwards from [mike.name]..."
            bree.say "Mmm..."
            show mike rough doggy pleasure
            bree.say "Oh god!"
            "I hear [mike.name] grunt with satisfaction as he finally enters me."
            "But after that, I'm overwhelmed by what I'm feeling myself."
            "It took a while for us to get here, but it was well worth it."
            "Normally I'd want [mike.name] to start slow and build up steadily."
            "What he's doing right now is the exact opposite of that."
            "He starts hard and fast, and if anything, he steps it up too."
            "[mike.name] has one hand tangled in my hair and the other holding my waist."
            "That means he's pulling me backwards as he's thrusting forwards."
            "Sure, there's a little bit of pain mixed in there."
            "But I know that I can trust [mike.name] not to go too far."
            "So there's far more pleasure involved."
            show mike rough doggy blush
            "I think it's also helping that I'm totally going along with him too."
            "There's no resistance in my body, it's moving in sympathy with [mike.name]."
            "Which means he can put all of his energy into fucking me harder still!"
            "I can feel myself sinking down onto the bed."
            "But when that happens, he gives my hair a tug."
            "Which makes me stand up and get back into it."
            "Sure, part of me is thinking that I should be more assertive."
            "That it's wrong for a modern woman to be so passive during sex."
            show mike rough doggy boobs
            "But that's part of what's adding spice to the whole thing."
            "For just a little while, I can allow myself to be submissive."
            "To be totally dominated by a man that I love and trust."
            "And that temporary feeling of submission is what pushes me over the edge."
            "I begin to buck and twist on [mike.name]'s cock, unable to hold back."
            bree.say "[mike.name[0]]...[mike.name]..."
            bree.say "I'm...I'm gonna cum!"
            call cum_reaction (mike, 'vaginal', sexperience_min, 150) from _call_cum_reaction_215
            if _return == "vaginal_condom":
                "Luckily for the both of us, we remembered to use a condom."
                "Because I don't know if either of us could have stopped in time."
                with hpunch
                "[mike.name] gives my hair one last tug, bending me like a bow."
                with hpunch
                "And then he shoots his load into me, holding nothing back."
                show mike rough doggy ahegao -boobs with hpunch
                "I cum almost the instant it hits me, panting and gasping with pleasure."
                "And I'm glad that [mike.name]'s holding onto me as it happens."
                "Because I'd have fallen on my face otherwise!"
                $ mike.love += 1
            elif _return == "vaginal_outside":
                "Luckily for me, [mike.name] seems to remember we didn't use a condom."
                "I feel him loosening his grip on me, just in time."
                "This means his cock slides out before he shoots his load."
                show mike rough doggy -vaginal -boobs with hpunch
                "And then he showers me with it, holding nothing back."
                show mike rough doggy ahegao cum with hpunch
                "I cum almost the instant it hits me, panting and gasping with pleasure."
                show mike rough doggy bodycum dickcum -cum with hpunch
                "And I'm glad that [mike.name]'s holding onto me as it happens."
                "Because I'd have fallen on my face otherwise!"
                $ mike.love += 2
            elif _return == "vaginal_inside_mad":
                with hpunch
                "[mike.name] gives my hair one last tug, bending me like a bow."
                show mike rough doggy ahegao cum -boobs with hpunch
                "And then he shoots his load into me, holding nothing back."
                with hpunch
                "I cum almost the instant it hits me, panting and gasping with pleasure."
                "And I'm glad that [mike.name]'s holding onto me as it happens."
                "Because I'd have fallen on my face otherwise!"
                mike.say "Oh shit!"
                $ mike.impregnate()
                mike.say "[hero.name]..."
                mike.say "Are you on the pill or something?"
                mike.say "Because if not, we just fucked up big time!"
                "I look back over my shoulder, horror twisting my guts."
                $ mike.love -= 5
                "Oh fuck...he just came in me!"
            else:
                with hpunch
                "[mike.name] gives my hair one last tug, bending me like a bow."
                show mike rough doggy ahegao cum -boobs with hpunch
                $ mike.impregnate()
                "And then he shoots his load into me, holding nothing back."
                with hpunch
                "I cum almost the instant it hits me, panting and gasping with pleasure."
                "And I'm glad that [mike.name]'s holding onto me as it happens."
                "Because I'd have fallen on my face otherwise!"
                mike.say "Oh shit!"
                mike.say "[hero.name]..."
                mike.say "Are you on the pill or something?"
                mike.say "Because if not, we just fucked up big time!"
                "I look back over my shoulder."
                $ mike.love += 5
                "Oh fuck...he just came in me!"
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "[mike.name]'s grip on me is pretty tight."
            "And I can feel his cock pressing against my ass too!"
            "Now I'm starting to wonder what he made of my request."
            "What he'll make of me asking him not to be too gentle."
            "And then, as if he's reading my mind, I find out."
            "Because I can feel a hand reaching out and grabbing my hair."
            "[mike.name] twines his fingers into it, getting a damn good hold."
            "And then he gives it an experimental tug."
            bree.say "Oh yeah!"
            show mike rough doggy pleasure
            bree.say "That's what I'm talking about!"
            mike.say "Oh...I..."
            mike.say "It is?"
            mike.say "I mean...yeah, of course it is!"
            "I try as hard as I can not to chuckle at [mike.name]'s attempt at bravado."
            "But it's so cute to hear him trying to style himself as the big man."
            "So I decide that I'm going to let him have his moment in the spotlight."
            bree.say "Oh, [mike.name]!"
            bree.say "You're SO manly!"
            mike.say "You bet I am, [hero.name]!"
            show mike rough doggy normal vaginal
            "It's right about now that I choose to take hold of [mike.name]'s cock."
            "And I push it between the cheeks of my ass."
            "[mike.name]'s pulling on my hair at the same time."
            "And by now I'm more than ready for him."
            "But the choice of ass over pussy seems to have thrown him a little."
            mike.say "Erm, [hero.name]..."
            mike.say "You realise that's your butt, right?"
            bree.say "Yeah, [mike.name]..."
            bree.say "You got a problem with that?"
            mike.say "No...no problem at all!"
            mike.say "Just checking..."
            "As if trying to make up for his hesitation, [mike.name] pushes on."
            "And soon enough I can feel him pushing into my ass."
            "My muscles fight for a few moments."
            "But then they seem catch onto the fact that I want this pretty bad."
            "Then they surrender to the inevitable, an there's nothing to stop him sinking in."
            "All it takes is one more lurch forwards from [mike.name]..."
            bree.say "Mmm..."
            show mike rough doggy pleasure
            bree.say "Oh god!"
            "I hear [mike.name] grunt with satisfaction as he finally enters me."
            "But after that, I'm overwhelmed by what I'm feeling myself."
            "It took a while for us to get here, but it was well worth it."
            "Normally I'd want [mike.name] to start slow and build up steadily."
            "What he's doing right now is the exact opposite of that."
            "He starts hard and fast, and if anything, he steps it up too."
            "[mike.name] has one hand tangled in my hair and the other holding my waist."
            "That means he's pulling me backwards as he's thrusting forwards."
            "Sure, there's a little bit of pain mixed in there."
            "But I know that I can trust [mike.name] not to go too far."
            "So there's far more pleasure involved."
            "I think it's also helping that I'm totally going along with him too."
            "There's no resistance in my body, it's moving in sympathy with [mike.name]."
            show mike rough doggy boobs
            "Which means he can put all of his energy into fucking me harder still!"
            "I can feel myself sinking down onto the bed."
            "But when that happens, he gives my hair a tug."
            "Which makes me stand up and get back into it."
            "Sure, part of me is thinking that I should be more assertive."
            "That it's wrong for a modern woman to be so passive during sex."
            "But that's part of what's adding spice to the whole thing."
            "For just a little while, I can allow myself to be submissive."
            "To be totally dominated by a man that I love and trust."
            "And that temporary feeling of submission is what pushes me over the edge."
            "I begin to buck and twist on [mike.name]'s cock, unable to hold back."
            bree.say "[mike.name[0]]...[mike.name]..."
            bree.say "I'm...I'm gonna cum!"
            call cum_reaction (mike, 'anal', sexperience_min) from _call_cum_reaction_216
            if _return == "anal_inside":
                "Luckily for the both of us, I wanted to be fucked up the ass."
                "Because I don't know if either of us could have stopped in time."
                with hpunch
                "[mike.name] gives my hair one last tug, bending me like a bow."
                with hpunch
                "And then he shoots his load into me, holding nothing back."
                show mike rough doggy ahegao cum -boobs with hpunch
                "I cum almost the instant it hits me, panting and gasping with pleasure."
                "And I'm glad that [mike.name]'s holding onto me as it happens."
                "Because I'd have fallen on my face otherwise!"
                $ mike.love += 2
            elif _return == "anal_outside":
                bree.say "[mike.name]..."
                bree.say "Pull out - NOW!"
                show mike rough doggy -vaginal -boobs
                "Somehow asserting myself flips a switch in [mike.name]'s brain."
                "And he hurries to do as he's told."
                "I feel him loosening his grip on me, just in time."
                with hpunch
                "This means his cock slides out before he shoots his load."
                show mike rough doggy ahegao cum with hpunch
                "And then he showers me with it, holding nothing back."
                show mike rough doggy bodycum dickcum -cum with hpunch
                "I cum almost the instant it hits me, panting and gasping with pleasure."
                "And I'm glad that [mike.name]'s holding onto me as it happens."
                "Because I'd have fallen on my face otherwise!"
                $ mike.sub += 1
    return

label mike_fuck_date_cowgirl(sexperience_min):
    bree.say "Okay..."
    bree.say "Let's get down to business!"
    scene mike cowgirl with fade
    menu:
        "Guide him to my pussy":
            "Now that I have [mike.name] right where I want him, it's time for some fun."
            show mike cowgirl out
            "Still holding onto his cock, I lean forwards, rubbing it between my legs."
            bree.say "Mmm..."
            bree.say "I like the way that feels!"
            bree.say "How about you?"
            mike.say "Y...yeah, [hero.name]!"
            mike.say "I like it too!"
            bree.say "But that's just how it feels on the outside."
            bree.say "Imagine how it'll feel on the inside!"
            call check_condom_usage (mike) from _call_check_condom_usage_121
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show mike cowgirl condom
            "[mike.name]'s nodding like crazy by now, making me want to tease him even more."
            "But the truth is that I can feel what's going on inside of me right now."
            "Just being able to see his cock, to hold it in my hand like this."
            "I'm starting to get so wet I'm scared that I'm going to slide right off him!"
            "That's why I begin working the head of his cock against the lips of my pussy."
            "I'm trying to make it look like I'm teasing [mike.name]."
            "But in reality I want to push it straight in there."
            "And I have to fight pretty hard to keep from giving in to temptation."
            "Every pass the head of his cock makes it gets harder too."
            "And by that I mean resisting the temptation to push it in there."
            "I don't know how [mike.name] could actually get any harder than he is right now!"
            mike.say "Oh fuck..."
            mike.say "[hero.name]!"
            bree.say "Hold on, [mike.name]..."
            bree.say "Here we go!"
            "All at once I find that can't hold back any longer."
            show mike cowgirl vaginal
            "The lips of my pussy open up like a flower."
            "And suddenly the position I'm in starts to play a part."
            "All of my weight is pressing down on [mike.name]."
            "Which means that I can't help sliding rapidly down and onto his cock."
            "I can feel him filling me at what feels like an alarming rate."
            "And before I know it, there's nowhere left for me to go."
            "I'm sitting there, pretty much impaled on him!"
            "But in that same instant, I know that it's not enough."
            "I need more before I can satisfy the need inside of me."
            "On instinct I thrown out my hands, planting them on [mike.name]'s shoulders."
            "He tries to sit up as I do so, but isn't prepared for my strength."
            "And his eyes go wide as he feels himself being pinned to the bed."
            "In the next instant, I'm moving atop [mike.name]."
            "Going back and forth, I can feel him moving inside me."
            "This is it - this is the way I'm going to do it!"
            "I need to keep on riding [mike.name] just like this."
            "For his part, [mike.name] seems to be getting almost as much out of this as me."
            "I don't hear any complaints from him."
            "In fact he looks totally blissed out!"
            "If we keep on going like this, I know that I can do it."
            "I can ride [mike.name] until I cum."
            "Or until I burst a blood-vessel in my brain and die."
            show mike cowgirl pleasure
            bree.say "Ah..."
            bree.say "What the..."
            bree.say "Oh god!"
            "I guess it serves me right for forgetting all about [mike.name] like that."
            "Because now he has his hands all over my breasts!"
            "And is he ever doing a good job of playing with them too!"
            "Every time [mike.name] squeezes and massages them, I feel myself shudder."
            "And when he starts to pinch at my nipples, I can feel it in my pussy."
            "That's just too much for me to handle."
            "I can feel myself starting to lose it already..."
            show mike cowgirl ahegao
            call cum_reaction (mike, 'vaginal', sexperience_min) from _call_cum_reaction_217
            if _return == "vaginal_outside":
                "I know that I have to pull out before it's too late."
                "It sucks, but that's the price you pay for not using a condom."
                show mike cowgirl out
                "With a massive effort, I haul myself off [mike.name]'s cock."
                show mike cowgirl cumshot with vpunch
                "He starts to cum almost the moment he's free, spattering my breasts and belly with cum."
                show mike cowgirl -cumshot resting dickcum cum onbody with vpunch
                "And that seems to set me off too, making my arms buckle and sending me toppling over onto my side."
            elif _return == "vaginal_condom":
                "I feel a surge of relief when I remember we bothered to use a condom."
                "Because it means that I can simply surrender to what comes next."
                with vpunch
                "And that's [mike.name] shooting his load into me as I begin to cum."
                with vpunch
                "Now I'm glad that I held on so tightly before."
                with vpunch
                "As I feel myself bucking and rocking in the throes of my orgasm."
            elif _return == "vaginal_inside_mad":
                "I can simply surrender to what comes next."
                with vpunch
                "And that's [mike.name] shooting his load into me as I begin to cum."
                show mike cowgirl creampie pleasure -blush with vpunch
                $ mike.impregnate()
                "Now I'm glad that I held on so tightly before."
                with vpunch
                "As I feel myself bucking and rocking in the throes of my orgasm."
                mike.say "[hero.name[0]]...[hero.name]..."
                mike.say "No condom!"
                bree.say "You...you have to be kidding!"
                show mike cowgirl -creampie resting dickcum cum onpussy with vpunch
                $ mike.love -= 5
                bree.say "Oh fuck - what are we going to do?!?"
            else:
                "I can simply surrender to what comes next."
                with vpunch
                "And that's [mike.name] shooting his load into me as I begin to cum."
                show mike cowgirl creampie up with vpunch
                $ mike.impregnate()
                "Now I'm glad that I held on so tightly before."
                with vpunch
                "As I feel myself bucking and rocking in the throes of my orgasm."
                $ mike.love += 5
                "Each of us feels wave after wave of pleasure."
                "Pushed ever higher by the orgasm of the other."
                "Once [mike.name] lets go of me, there's nothing to hold me up anymore."
                show mike cowgirl -creampie resting dickcum cum onpussy with vpunch
                "So I slump forward onto the pillows, my muscles turning to jelly."
                "[mike.name] doesn't fare any better either, landing right beside me."
                "And pretty soon there's nothing to worry about save for falling asleep."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "Now that I have [mike.name] right where I want him, it's time for some fun."
            show mike cowgirl out
            "Still holding onto his cock, I lean forwards, rubbing it between my legs."
            bree.say "Mmm..."
            bree.say "I like the way that feels!"
            bree.say "How about you?"
            mike.say "Y...yeah, [hero.name]!"
            mike.say "I like it too!"
            bree.say "But that's just how it feels on the outside."
            bree.say "Imagine how it'll feel on the inside!"
            "[mike.name]'s nodding like crazy by now, making me want to tease him even more."
            "But the truth is that I can feel what's going on inside of me right now."
            "Just being able to see his cock, to hold it in my hand like this."
            "I'm starting to get so wet I'm scared that I'm going to slide right off him!"
            "That's why I begin working the head of his cock further back and closer to my ass."
            "I'm trying to make it look like I'm teasing [mike.name]."
            "But in reality I want to push it straight up there."
            "And I have to fight pretty hard to keep from giving in to temptation."
            "Every pass the head of his cock makes it gets harder too."
            "And by that I mean resisting the temptation to push it in there."
            "I don't know how [mike.name] could actually get any harder than he is right now!"
            show mike cowgirl anal blush
            mike.say "Oh fuck..."
            mike.say "[hero.name]!"
            show mike cowgirl down
            mike.say "That feels like your ass!"
            bree.say "Ah, [mike.name] - you rumbled me!"
            bree.say "Hold on, [mike.name]..."
            bree.say "Here we go!"
            show mike cowgirl smile
            "All at once I find that can't hold back any longer."
            "The muscles of my ass open up like a flower."
            "And suddenly the position I'm in starts to play a part."
            "All of my weight is pressing down on [mike.name]."
            "Which means that I can't help sliding rapidly down and onto his cock."
            "I can feel him filling me at what feels like an alarming rate."
            "And before I know it, there's nowhere left for me to go."
            "I'm sitting there, pretty much impaled on him!"
            show mike cowgirl pleasure
            "But in that same instant, I know that it's not enough."
            "I need more before I can satisfy the need inside of me."
            "On instinct I thrown out my hands, planting them on [mike.name]'s shoulders."
            "He tries to sit up as I do so, but isn't prepared for my strength."
            "And his eyes go wide as he feels himself being pinned to the bed."
            "In the next instant, I'm moving atop [mike.name]."
            "Going back and forth, I can feel him moving inside me."
            "This is it - this is the way I'm going to do it!"
            "I need to keep on riding [mike.name] just like this."
            "For his part, [mike.name] seems to be getting almost as much out of this as me."
            "I don't hear any complaints from him."
            "In fact he looks totally blissed out!"
            "If we keep on going like this, I know that I can do it."
            "I can ride [mike.name] until I cum."
            "Or until I burst a blood-vessel in my brain and die."
            bree.say "Ah..."
            bree.say "What the..."
            show mike cowgirl ahegao
            bree.say "Oh god!"
            "I guess it serves me right for forgetting all about [mike.name] like that."
            "Because now he has his hands all over my breasts!"
            "And is he ever doing a good job of playing with them too!"
            "Every time [mike.name] squeezes and massages them, I feel myself shudder."
            "And when he starts to pinch at my nipples, I can feel it in my pussy."
            "That's just too much for me to handle."
            "I can feel myself starting to lose it already..."
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_218
            if _return == "anal_inside":
                "I feel a surge of relief that I chose to let [mike.name] do me up the ass."
                "Because it means that I can simply surrender to what comes next."
                with vpunch
                "And that's [mike.name] shooting his load into me as I begin to cum."
                show mike cowgirl creampie up with vpunch
                $ mike.sub += 2
                "Now I'm glad that I held on so tightly before."
                with vpunch
                "As I feel myself bucking and rocking in the throes of my orgasm."
            elif _return == "anal_outside":
                "I have no idea why."
                "But I know that I have to pull out before the end."
                "There's no real reason other than satisfying my own desires."
                "But isn't that what this is all about?"
                show mike cowgirl out
                "With a massive effort, I haul myself off [mike.name]'s cock."
                show mike cowgirl cumshot with vpunch
                $ mike.sub += 1
                "He starts to cum almost the moment he's free, spattering my breasts and belly with cum."
                show mike cowgirl -cumshot resting dickcum cum onbody with vpunch
                "And that seems to set me off too, making my arms buckle and sending me toppling over onto my side."
            $ mike.flags.anal += 1
    return

label mike_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        $ game.room = "bedroom4"
        show mike naked
        if game.week_day % 4 == 0:
            "Afterwards neither of us moves as much as an inch."
            "We stay wrapped together, as close as possible."
            "I can feel things cooling, and in the morning I'll need a shower for sure!"
            "But I can feel myself falling asleep, so I won't care until then anyway."
            "The last thing I hear before I drop off is the sound of [mike.name] snoring."
            "And I must be tired if even something as loud as that can't keep me awake!"
        elif game.week_day % 4 == 1:
            "Afterwards I find tiredness creeping over me."
            "And this time it's for real."
            "I raise my head, meaning to say as much to [mike.name]."
            "But I see that his eyes have already closed and he's snoring softly."
            "And that's the last thing I see before my eyes close too."
        elif game.week_day % 4 == 2:
            "I break only to return the favour, the two of us grinning madly at each other, before yet again [mike.name]'s arms wrap themselves around me and pull me close."
            "I return the embrace, satisfied and happy, my eyes closing as I relax, content with the moment and, perhaps most of all, excited for what the next date might bring."
        else:
            "As soon as [mike.name] loosens his grip on me, I collapse onto the bed."
            "I have no idea where I land or where he ends up once I do so."
            "All that I know is the fact I'm exhausted, totally and utterly spent."
            "Which is why my eyes close and I drift off to sleep a few moments later."
        call sleep ("mike") from _call_sleep_62
    return

label give_mike_lapdance:
    "I keep sneaking a look between the curtains at my next customer."
    "Because part of me can't actually believe that it's [mike.name] sitting there."
    "I know that he knows I've been dancing at the strip-club."
    "But what I don't know is if he came here tonight because of that."
    "Is [mike.name] here so that he can get a dance from me?"
    "Or is this just something that he does all the time?"
    "Urgh...I don't know which of those is worse!"
    "Oh, come on, [hero.name] - pull yourself together."
    "The fact is that it doesn't matter which of those things is true."
    "If I want to make this thing work, then I have to be able to dance for him."
    "In fact, if I can dance for [mike.name], then I should be able to do it for anyone."
    "That's it - I need to see this as a challenge and beat it!"
    "With that in mind, I nod for my music."
    scene mike lapdance
    show mike lapdance nomc
    with fade
    "And when it begins, I part the curtains and reveal myself to [mike.name]."
    "The moment that I make eye-contact with him, he looks shocked."
    "Maybe that's because he wasn't expecting it to be me."
    "Or maybe he was, and the reality of it is more than he expected."
    "Either way, it gives me a sudden boost of confidence."
    "The fact I know him doesn't chance the dynamic here."
    "I'm still the one that's in control."
    "Or at least that's what I keep telling myself!"
    "I make sure to keep moving as I walk over to him."
    "Making every step a part of the dance."
    "That way I can maintain the feel of this being different"
    "Distinct from the circumstances under which we normally meet."
    "Here the rules are not the same as they are at home or in the street."
    "And a guy can get slung out on his ass if he forgets that."
    show mike lapdance nomc at center, zoomAt(1.5, (420, 1040))
    mike.say "[hero.name[0]]...[hero.name[0]]...[hero.name]!"
    bree.say "Yeah, [mike.name], that's right."
    bree.say "It's [hero.name[0]]-[hero.name[0]]-[hero.name]!"
    bree.say "I'm gonna take the stuttering as a compliment!"
    "I don't want to waste time here by getting into a conversation."
    "Instead I keep on moving in time to the music."
    scene bg black
    show mike lapdance
    with fade
    "Letting the sight of my scantily clad body keep [mike.name] spellbound."
    "The last thing that I want is for him to regain control of his senses."
    "Like I said, I'm wearing as little as I can get away with already."
    "So the largest part of my act can't be the stripping-off."
    "If it were, I'd be in and out of there in less than a minute."
    "And the customers would be demanding a refund!"
    "So I take things as slowly as I can in that department."
    "And I keep moving the whole time, turning and twisting."
    "Before I know it, the last of my clothes comes off."
    scene bg black
    show mike lapdance worried bree_naked
    with fade
    "That leaves me dancing naked in front of [mike.name]."
    "But I can already see that I've managed to pull it off."
    "His eyes are wide and they follow my every move without fail."
    "It's almost like I've put him into a trance!"
    "I don't feel any of the fear or anxiety that had hold of me before."
    show mike lapdance normal
    "Instead I feel like I'm the one in a position of power."
    "This means that I don't hesitate to make use of my entire body."
    "As it moves, things sway and bob in sympathy too."
    "Turning around, I see how close I can get my breasts and ass to [mike.name]."
    "Each time they seem to come closer to his face and hands."
    "The unconscious twitch this creates in his body making me grin with delight."
    "It's like his instinct is to reach out and grab me every time."
    "But at the last moment, his brain kicks in and stops him from doing it."
    "Part of me knows that I shouldn't push my luck too far."
    "Because too much teasing could make [mike.name] lose control."
    "But I can't help myself, because the thrill is too great."
    "Finally, something seems to snap inside of [mike.name]."
    "Like he can't hold it in any longer."
    "He reaches out for me."
    "But I make sure to dance out of his grasp."
    mike.say "Urgh..."
    mike.say "[hero.name]..."
    show mike lapdance worried
    bree.say "Uh-uh!"
    bree.say "No touching, you naughty boy!"
    show mike lapdance normal
    bree.say "If you want more, then you'll just have to pay for another dance..."
    scene expression f"bg {game.room}" with fade
    "With that, I hurry over to the curtains and slip between them."
    "As soon as I'm out of sight, I feel myself starting to crash."
    "The adrenaline that must have been seeing me through is draining away."
    "And the reality of what just happened is starting to sink in."
    "But I keep on telling myself that I did it."
    "I pulled off dancing for [mike.name]."
    "And what's better, I left him wanting more!"
    return

label mike_fuck_date_reverse_cowgirl(sexperience_min):
    hide mike
    show mike reverse cowgirl at center, zoomAt (1.65, (1000, 1140))
    with fade
    "That's when [mike.name] walks up behind me and starts kissing my neck."
    show mike reverse cowgirl closed
    "It feels great, and it'd be more than enough to get me in the mood on its own."
    "But at the same time I can feel the sensation of his body pressed against mine."
    "My back to his belly, which means I can feel every inch of his muscles!"
    "And...oh yeah, I can feel his manhood too!"
    show mike reverse cowgirl at center, traveling (1.0, 1.0, (640, 720))
    pause 1.0
    with vpunch
    "So is it any wonder that I totally surrender when he pulls me down onto my bed?"
    "[mike.name]'s sitting on the edge of it, with me on his lap."
    "And I can already feel my heart starting to beat harder, my pulse quicken."
    "Because I can hardly wait for what's coming next!"
    show mike reverse cowgirl normal
    "[mike.name] pauses kissing me for a moment."
    "Just long enough to ask one question."
    mike.say "So, [hero.name]..."
    mike.say "Where do you want me?"
    menu:
        "Fuck my pussy":
            "I nod eagerly, already anticipating what we're about to do."
            "So much so that I almost forget to answer [mike.name]'s question!"
            bree.say "Oh..."
            bree.say "The pussy, [mike.name]!"
            bree.say "That's where I want it!"
            mike.say "Okay, [hero.name]..."
            mike.say "What the lady wants, the lady gets!"
            call check_condom_usage (mike) from _call_check_condom_usage_131
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show mike reverse cowgirl condom
            show mike reverse cowgirl closed
            "I can't help biting my lip in anticipation as [mike.name] pulls me onto his lap."
            "He's careful in the extreme as he manoeuvres me into the exact spot he wants me."
            "And then he gently lowers me down until I can feel the very tip of his manhood."
            show mike reverse cowgirl pain vaginal
            "Even with all the warnings and gentle treatment, this still makes me let out a squeal."
            "It's not the kind of sound I make when I can help it."
            show mike reverse cowgirl blush
            "And the helpless nature of it makes my cheeks flush with the embarrassment."
            "But if [mike.name] notices, he's enough of a gentleman to keep it to himself."
            "As he doesn't pause or hesitate, just keeps right on going."
            "Ever so slowly, he begins to move up and down beneath me."
            "This has the effect of drawing the head of his cock along the lips of my pussy."
            "And from that moment on, I seem to forget about everything else."
            "The sensations that it stirs inside of me are enough to occupy me entirely."
            show mike reverse cowgirl pleasure
            "I'm quivering and shaking, beginning to gasp."
            "And he's still only on the outside!"
            "But that's about to change, I know that for sure."
            "Already I can feel the muscles down there starting to weaken."
            "Or maybe melt would be a better way to describe it?"
            "Either way, all I know is that I can't resist much longer."
            "With each pass that [mike.name] makes, I think it's going to happen."
            "Yet when it does, I find that I'm not in the least bit prepared."
            "Suddenly the tip of his cock doesn't slide any further."
            "Instead it sinks in, beginning to push into me."
            "And that's all it takes for things to change."
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.35
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.35
            show mike reverse cowgirl at startle(0.05,-10)
            "[mike.name] pushes harder, pulling me down with more force than before."
            "He has gravity on his side, turning my weight to his advantage."
            "And so I sink down and onto him."
            "Unable, and more importantly unwilling, to stop my progress."
            "For a moment I don't think it's ever going to stop."
            "I think that I'm going to be sinking down onto [mike.name] forever."
            "But when it does, there's no time to take stock of how it feels."
            "Because that's when I feel [mike.name] take a firm hold of me."
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.3
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.3
            show mike reverse cowgirl at startle(0.05,-10)
            "And without warning, he begins to move in earnest."
            "I feel myself being bounced up and down in his lap."
            "Which also means that I'm going up and down on his cock too!"
            "Where before he was going slowly, now [mike.name]'s picking up serious speed."
            "I start to feel like I'm riding some kind of mechanical bull!"
            show mike reverse cowgirl clit
            "That's why I'm so surprised to feel [mike.name]'s hands roaming all over my body."
            "I was sure that he'd need them to hold me up and make this work."
            show sexinserts belly bree as bellycum zorder 2 at center, zoomAt(1, (-140, 1100))
            "But there they are, caressing the curve of my belly."
            "And...oh my!"
            show sexinserts chest bree zorder 1 at center, zoomAt(1, (730, 760))
            "And finding their way up to my breasts!"
            "Somehow [mike.name]'s got enough strength down there to do all of this."
            "And I feel myself melting even more as he begins to play with my breasts too!"
            "He massages them, one in each hand."
            "His palms squeezing them while his fingers pinch at my nipples."
            show mike reverse cowgirl pain at startle(0.05,-10)
            pause 0.2
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.2
            show mike reverse cowgirl at startle(0.05,-10)
            "Oh god!"
            "I don't think I can take much more of this!"
            "Wait...I know that I can't - because I recognise that feeling."
            show mike reverse cowgirl pleasure
            "I recognise the one building up inside of me."
            bree.say "Ungh..."
            bree.say "[mike.name]..."
            bree.say "Gonna...gonna cum!"
            bree.say "Right now!"
            mike.say "Me...too..."
            call cum_reaction (mike, 'vaginal', sexperience_min) from _call_cum_reaction_241
            if _return == "vaginal_outside":
                show mike reverse cowgirl -vaginal
                "I lurch upwards at the last moment, making [mike.name]'s cock pop out of me."
                show mike reverse cowgirl cumshot
                show sexinserts chest bree zorder 1 at center, zoomAt(1, (730, 760))
                show sexinserts belly bree as bellycum zorder 2 at center, zoomAt(1, (-140, 1100))
                with vpunch
                "He loses it a second later, showering me with hot, stick cum."
                show mike reverse cowgirl ahegao with vpunch
                "But I'm too wrapped up in my own orgasm to even notice."
                with vpunch
                "The sensation of that is just too much, almost making me black out!"
                "Thankfully [mike.name] holds onto me until the very last, making sure I'm safe and sound."
            elif _return == "vaginal_condom":
                "I hold on until the very last moment, and then I just let go."
                with vpunch
                "And I think that I can't feel anything more intense."
                with vpunch
                "That is until [mike.name] loses it inside of me a second later."
                show mike reverse cowgirl ahegao with vpunch
                "The sensation of that is just too much, almost making me black out!"
                "But he holds onto me until the very last, making sure I'm safe and sound."
            else:
                "I hold on until the very last moment, and then I just let go."
                with vpunch
                "And I think that I can't feel anything more intense."
                show mike reverse cowgirl creampie with vpunch
                "That is until [mike.name] loses it inside of me a second later."
                show mike reverse cowgirl ahegao with vpunch
                "The sensation of that is just too much, almost making me black out!"
                "But he holds onto me until the very last, making sure I'm safe and sound."
        "Fuck my ass" if hero.sexperience >= (sexperience_min + 5):
            "I nod eagerly, already anticipating what we're about to do."
            "So much so that I almost forget to answer [mike.name]'s question!"
            bree.say "Oh..."
            bree.say "The ass, [mike.name]!"
            bree.say "That's where I want it!"
            mike.say "Okay, [hero.name]..."
            mike.say "What the lady wants, the lady gets!"
            show mike reverse cowgirl closed
            "I can't help biting my lip in anticipation as [mike.name] pulls me onto his lap."
            "He's careful in the extreme as he manoeuvres me into the exact spot he wants me."
            "And then he gently lowers me down until I can feel the very tip of his manhood."
            show mike reverse cowgirl pain anal
            "Even with all the warnings and gentle treatment, this still makes me let out a squeal."
            "It's not the kind of sound I make when I can help it."
            show mike reverse cowgirl blush
            "And the helpless nature of it makes my cheeks flush with the embarrassment."
            "But if [mike.name] notices, he's enough of a gentleman to keep it to himself."
            "As he doesn't pause or hesitate, just keeps right on going."
            "Ever so slowly, he begins to move up and down beneath me."
            "This has the effect of pushing the head of his cock between my buttocks."
            "And from that moment on, I seem to forget about everything else."
            "The sensations that it stirs inside of me are enough to occupy me entirely."
            show mike reverse cowgirl pleasure
            "I'm quivering and shaking, beginning to gasp."
            "And he's still only on the outside!"
            "But that's about to change, I know that for sure."
            "Already I can feel the muscles down there starting to weaken."
            "Or maybe melt would be a better way to describe it?"
            "Either way, all I know is that I can't resist much longer."
            "With each pass that [mike.name] makes, I think it's going to happen."
            "Yet when it does, I find that I'm not in the least bit prepared."
            "Suddenly the tip of his cock doesn't slide any further."
            "Instead it sinks in, beginning to push into me."
            "And that's all it takes for things to change."
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.35
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.35
            show mike reverse cowgirl at startle(0.05,-10)
            "[mike.name] pushes harder, pulling me down with more force than before."
            "He has gravity on his side, turning my weight to his advantage."
            "And so I sink down and onto him."
            "Unable, and more importantly unwilling, to stop my progress."
            "For a moment I don't think it's ever going to stop."
            "I think that I'm going to be sinking down onto [mike.name] forever."
            "But when it does, there's no time to take stock of how it feels."
            "Because that's when I feel [mike.name] take a firm hold of me."
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.3
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.3
            show mike reverse cowgirl at startle(0.05,-10)
            "And without warning, he begins to move in earnest."
            "I feel myself being bounced up and down in his lap."
            "Which also means that I'm going up and down on his cock too!"
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.2
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.2
            show mike reverse cowgirl at startle(0.05,-10)
            "Where before he was going slowly, now [mike.name]'s picking up serious speed."
            "I start to feel like I'm riding some kind of mechanical bull!"
            show mike reverse cowgirl clit
            "That's why I'm so surprised to feel [mike.name]'s hands roaming all over my body."
            "I was sure that he'd need them to hold me up and make this work."
            show sexinserts belly bree as bellycum zorder 2 at center, zoomAt(1, (-140, 1100))
            "But there they are, caressing the curve of my belly."
            "And...oh my!"
            show sexinserts chest bree zorder 1 at center, zoomAt(1, (730, 760))
            "And finding their way up to my breasts!"
            "Somehow [mike.name]'s got enough strength down there to do all of this."
            "And I feel myself melting even more as he begins to play with my breasts too!"
            "He massages them, one in each hand."
            "His palms squeezing them while his fingers pinch at my nipples."
            show mike reverse cowgirl pain at startle(0.05,-10)
            pause 0.2
            show mike reverse cowgirl at startle(0.05,-10)
            pause 0.2
            show mike reverse cowgirl at startle(0.05,-10)
            "Oh god!"
            "I don't think I can take much more of this!"
            "Wait...I know that I can't - because I recognise that feeling."
            show mike reverse cowgirl pleasure
            "I recognise the one building up inside of me."
            bree.say "Ungh..."
            bree.say "[mike.name]..."
            bree.say "Gonna...gonna cum!"
            bree.say "Right now!"
            mike.say "Me...too..."
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_242
            if _return == "anal_inside":
                "I hold on until the very last moment, and then I just let go."
                with vpunch
                "And I think that I can't feel anything more intense."
                show mike reverse cowgirl creampie with vpunch
                "That is until [mike.name] loses it inside of me a second later."
                show mike reverse cowgirl ahegao with vpunch
                "The sensation of that is just too much, almost making me black out!"
                "But he holds onto me until the very last, making sure I'm safe and sound."
            elif _return == "anal_outside":
                show mike reverse cowgirl -anal
                "I lurch upwards at the last moment, making [mike.name]'s cock pop out of me."
                show mike reverse cowgirl cumshot
                show sexinserts chest bree zorder 1 at center, zoomAt(1, (730, 760))
                show sexinserts belly bree as bellycum zorder 2 at center, zoomAt(1, (-140, 1100))
                with vpunch
                "He loses it a second later, showering me with hot, stick cum."
                show mike reverse cowgirl ahegao with vpunch
                "But I'm too wrapped up in my own orgasm to even notice."
                with vpunch
                "The sensation of that is just too much, almost making me black out!"
                "Thankfully [mike.name] holds onto me until the very last, making sure I'm safe and sound."
            $ mike.flags.anal += 1
    $ mike.love += 2
    hide sexinserts
    hide bellycum
    show cuddle mike
    with fade
    "Afterwards we both collapse onto my bed, totally spent."
    "Everything I said about wanting to fall asleep in comfort is forgotten too."
    "Because we simply pass out in a heap of tangled limbs."
    "I guess we'll wake up stiff and cranky in the morning."
    "But right now, neither of us seems to care."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
