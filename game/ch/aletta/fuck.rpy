init python:
    InteractActivity(**{
    "name": "aletta_event_04_sex",
    "display_name": "Fuck",
    "label": "aletta_event_04_sex",
    "icon": "fuck",
    "conditions": [
        IsDone("aletta_event_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("alettaoffice"),
            HasStamina(),
            MinStat("charm", 60),
            ),
        PersonTarget(aletta,
            IsActive(),
            MinStat("love", 60),
            ),
        ],
    "once_day": True,
    "music": "music/johny_grimes/levity.ogg",
    })

    InteractActivity(**{
    "name": "aletta_event_05b_sex",
    "display_name": "Fuck",
    "label": "aletta_event_05b_sex",
    "duration": 2,
    "icon": "fuck",
    "conditions": [
        IsDone("aletta_event_05b"),
        HeroTarget(
            IsGender("male"),
            IsRoom("forest"),
            HasStamina(),
            MinStat("charm", 90),
            ),
        PersonTarget(aletta,
            IsActive(),
            MinStat("love", 100),
            ),
        ],
    "once_day": True,
    "music": "music/johny_grimes/levity.ogg",
    })

    InteractActivity(**{
    "name": "aletta_fuck_mc_office",
    "display_name": "Fuck",
    "label": "aletta_fuck_mc_office",
    "conditions": [
        IsDone("aletta_event_04"),
        HeroTarget(
            HasRoomTag("mcoffice"),
            HasStamina(),
            ),
        PersonTarget(aletta,
            IsActive(),
            MinStat("love", 60),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    "music": "music/johny_grimes/levity.ogg",
    })

    Event(**{
    "name": "aletta_restaurant_blowjob",
    "label": "aletta_restaurant_blowjob",
    "conditions": [
        IsDone("aletta_kink_06"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        PersonTarget(aletta,
            OnDate(),
            MinStat("love", 100),
            IsFlag("restaurant_treat", False),
            ),
        ],
    "priority": 1000,
    "do_once": False,
    "once_week": True,
    })

    Event(**{
    "name": "aletta_restaurant_cunnilingus",
    "label": "aletta_restaurant_cunnilingus",
    "conditions": [
        IsDone("aletta_event_07"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        PersonTarget(aletta,
            OnDate(),
            MinStat("love", 120),
            IsFlag("restaurant_treat", False),
            ),
        ],
    "priority": 1000,
    "do_once": False,
    "once_week": True,
    })

    Event(**{
    "name": "aletta_hottub_sex_male",
    "label": "aletta_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(aletta,
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

label aletta_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ foreplay = False


    call aletta_fuck_date_intro_male (location) from _call_aletta_fuck_date_intro_male


    call aletta_dick_reactions from _call_aletta_dick_reactions


    call aletta_fuck_date_foreplay_male from _call_aletta_fuck_date_foreplay_male




    call aletta_fuck_date_choices_male from _call_aletta_fuck_date_choices_male


    call handle_npc_leaving (aletta, _return) from _call_handle_npc_leaving
    if _return:
        return


    hide aletta
    call aletta_sleep_date_fuck (location) from _call_aletta_sleep_date_fuck_1
    return

label aletta_fuck_date_intro_male(location="hero"):
    if aletta.sub <= 25:
        $ game.room = "house"
        scene bg house
        show aletta date happy
        with fade
        if game.days_played % 2 == 0:
            "I've been thinking all night that the date was going pretty well."
            "That Aletta was having just as good of a time as I was."
            "And when she hinted that we should go back to my place, I knew that I was right."
            scene bg livingroom
            show aletta date normal
            with fade
            "As soon as we walk in through the front door, Aletta takes hold of my hand."
            "She already knows where my room is, and starts to lead me there."
            show aletta normal b underwear with dissolve
            "But as she makes her way through the house, she starts to strip off her clothes."
            "Along the way, she peels off one thing after another, tossing them aside as she goes."
            show aletta b naked with dissolve
            "By the time we reach the stairs, she's already naked to the waist."
            "And when we get to the foot of them, only her underwear remains."
            "Aletta pauses by the door to my bedroom, bending over to pull off her panties."
            "These she tosses over her shoulder before slipping through the door."
            $ game.room = "bedroom1"
            scene bg bedroom1
            show aletta b naked
            with fade
            "She beckons for me to follow, and I hurry to do as I'm told."
            "I close the door and lean against it, my heart pounding in my chest."
            "For a moment I can't pull myself away from it."
            "Almost as if I'm afraid of someone bursting in and forcing us to stop before we've started."
            "For her part, Aletta seems amused by my ruffled state."
        else:
            $ game.room = "bedroom1"
            "It can be hard to read Aletta sometimes, as she almost always has a superior look on her face."
            "And she often smiles or laughs in a condescending manner that's similar to when she's being sincere."
            "So I find myself waiting to see how she acts before I know what she's actually feeling."
            "And this is one of those occasions, when we've just got back to my place after a date."
            "I mean, I thought that it went pretty well, that we both had a good time."
            scene bg bedroom1
            show aletta date happy
            with fade
            "But it's not until I close the door behind us that Aletta gives me a clue as to how she feels."
            aletta.say "Mmm..."
            aletta.say "I had a really great time tonight, [hero.name]."
            show aletta normal
            aletta.say "Actually, the best time I've had in a long while!"
            mike.say "R...really?"
            mike.say "That's great to hear, Aletta!"
            "I should also mention that knowing Aletta's in a good mood puts me in one too."
            "And knowing that she's in such a good mood while we're alone in my room..."
            "Well, that's enough to make me more than a little hot under the collar!"
            aletta.say "Of course it is, [hero.name]!"
            aletta.say "In fact..."
            aletta.say "You showed me such a good time that you deserve a reward."
            mike.say "I...I do?"
            aletta.say "Sure you do."
            aletta.say "How about these?"
            show aletta b flirt
            "Aletta thrusts her chest towards me."
            "At the same time she squeezes her breasts together."
            aletta.say "You've been staring at them all night, haven't you?"
            aletta.say "And I bet they've been making you nice and hard, haven't they?"
            "All I can manage to do in way of a response is nod my head eagerly."
            "Because she's absolutely right - I have been staring at her cleavage all night."
            "And the mere sight of those huge, heavy breasts has kept me hard as a rock!"
            aletta.say "Well, you hurry up and get undressed."
            aletta.say "And I'll see what I can do about that, okay?"
            show aletta b naked with dissolve
    elif aletta.sub <= 50:
        $ game.room = "bedroom1"
        scene bg bedroom1 with fade
        "Aletta isn't putting on too much of an act when she strides around, being a forceful bitch at the office throughout the working day."
        "She shows the exact same amount of dominance in the bedroom too, practically dragging me in through the door and beginning to strip me off the moment it closes behind us."
        "I try to return the favour, in between catching sudden and intense kisses that she plants on me at random instants and totally without warning."
        "It feels like all of Aletta's haughtiness outside of the bedroom has suddenly been transformed into an insatiable hunger inside of it."
        show aletta underwear with dissolve
        "And the more layers that I manage to strip off of her, the more aroused and determined Aletta seems to become."
        "But it's when I finally pull off her top and scramble to unhook her bra that she really starts to get delightfully aggressive with it."
        show aletta naked with dissolve
        "Almost as soon as her sizable breasts are released to stand proud upon her chest, Aletta thrusts them towards me, literally pressing them against me."
        aletta.say "Don't keep me waiting, [hero.name]..."
        aletta.say "I want to feel your hands all over me...starting right here!"
        "I'm more than happy to oblige, taking one of the heavy orbs in each of my hands."
        "As I begin to squeeze and caress her breasts, Aletta almost desperately pulls off the rest of her clothes."
        "I can't keep from staring at her nipples as they stiffen beneath my fingers and move under my thumbs."
        "But at the same time I can hear Aletta starting to pant and moan, as my playing with her makes her want more."
    else:
        $ game.room = "bedroom1"
        scene bg bedroom1 with fade
        "A part of me is still finding it hard to believe that I'm actually closing my bedroom door behind Aletta."
        "But as soon as I turn around, I see that she's not an illusion or a figment of my imagination."
        "She's still standing right there, large as life, right next to my bed."
        show aletta underwear with dissolve
        "And just to make sure that I can't quite shake off the notion I'm dreaming, she's stripping off her clothes too!"
        "I hurry over to the bed and begin to follow her lead, pulling off my own clothes as I do so."
        show aletta naked with dissolve
        "But I guess that most of my attention is on Aletta, as I almost trip over myself on the way."
        "Aletta looks over her shoulder at me, smiling at my clumsiness."
        "All I can hope is that she finds the effect she's having on me flattering, or else adorable."
    return

label aletta_fuck_date_foreplay_male:
    $ game.play_music("music/roa_music/city_nights.ogg")
    menu:
        "Let's use those tits" if 'aletta_stress_3' in DONE:
            call aletta_fuck_date_titjob from _call_aletta_fuck_date_titjob
        "Play with her ass":
            call aletta_fuck_date_assplay from _call_aletta_fuck_date_assplay
        "Just fuck her":
            return
    call stop_all_sfx from _call_stop_all_sfx
    scene bg bedroom1
    show aletta naked

    return _return

label aletta_fuck_date_choices_male:
    menu:
        "Cowgirl":
            call aletta_fuck_date_cowgirl (0) from _call_aletta_fuck_date_cowgirl
        "Missionary" if hero.sexperience >= 5:
            call aletta_fuck_date_missionary (5) from _call_aletta_fuck_date_missionary
        "Doggy" if hero.sexperience >= 10:
            call aletta_fuck_date_doggy (10) from _call_aletta_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_1

    return _return

label aletta_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show aletta naked
        if not aletta.is_sex_slave:
            aletta.say "[hero.name], what would you say to me staying the night with you?"
        else:
            aletta.say "Am I allowed to stay the night Master?"
        menu:
            "No":
                mike.say "Ah...I don't think that'd be a good idea..."
                mike.say "We both have work tomorrow, and coming in together would look a bit weird."
                "I want Aletta to stay, but I'm also not ready to handle everyone in the office knowing we slept together!"
                "Aletta tuts in a disapproving manner and begins to pick up her clothes."
                aletta.say "If that's what you think's best, I won't force myself on you!"
                "She raises an eyebrow at me and shakes her head before walking out."
                $ aletta.love -= 3
                call sleep from _call_sleep_35
            "Yes":
                show cuddle aletta with fade
                mike.say "Are you kidding, Aletta?!?"
                mike.say "I'd love you to stay!"
                "A look of triumph and satisfaction spreads across Aletta's face as she wraps herself around me like an amorous python."
                if not aletta.is_sex_slave:
                    aletta.say "Why, thank you, [hero.name]...I promise you won't regret it."
                else:
                    aletta.say "Why, thank you, Master...I promise you won't regret it."
                "I can only wonder at what Aletta plans to do to back those words up."
                "But for now, it's enough to know that I've made her happy as she curls up against me to sleep."
                if not aletta.is_sex_slave:
                    aletta.say "Good night, [hero.name]."
                else:
                    aletta.say "Good night, Master."
                mike.say "Good night to you too, Aletta."
                "I fall asleep soon after, unable to keep from nestling my head into the comfortable pillow of her breasts."
                $ aletta.love += 3
                call sleep ("aletta") from _call_sleep_36
    $ game.room = "bedroom1"
    return

label aletta_fuck_date_assplay:
    "She walks slowly over to the bed and sits down on the edge."
    "Crossing her legs, she leans back, resting her hands on the mattress."
    "I hear myself gulp as this spreads her breasts, which rise and fall with each breath."
    aletta.say "I take it you like what you see, [hero.name]?"
    "Aletta raises a quizzical eyebrow as she asks the question."
    "I can only nod, my head bobbing up and down crazily."
    aletta.say "Well, how about you return the favour?"
    "Still nodding like a fool, I scramble to start pulling off my own clothes."
    "But my efforts are nothing like Aletta's casual striptease on the way to my room."
    "I almost tear off what I'm wearing, unable to keep my eyes off of her as I do so."
    "Aletta smiles at my efforts, I hope because she's impressed with what she sees."
    "Or at least that she thinks the enthusiasm makes up for my lack of grace."
    aletta.say "Hmm..."
    aletta.say "I think I'd like a closer look!"
    "It's all that I can do to make myself walk the short distance to where Aletta's sitting."
    "My instinct is to cover the distance almost at a dash and pounce on her."
    "But I clamp down on that urge, afraid of looking utterly desperate and needy."
    "Which is exactly how she's making me feel inside right now!"
    aletta.say "That's right - come on over here."
    "As I draw close to her, Aletta uncrosses her legs and rises from the bed."
    "She still has that same approving smile on her face as she reaches out for me."
    "I close my eyes as she leans in for a kiss."
    show aletta kiss naked with fade
    $ aletta.flags.kiss += 1
    "But all the same I can feel the thrill passing through me as our naked bodies touch."
    "Aletta's breasts press against my chest, her flat stomach against mine."
    "Our legs twine themselves together, and I can feel the warmth between her thighs."
    "Suddenly, I feel Aletta's hand taking hold of mine once more."
    "The difference is that this time she's not leading me after her."
    "Instead she guides it slowly between her legs, silently letting me know just what she wants."
    "At first I stroke the sensitive skin around the lips of her pussy."
    "Enjoying the feel of the soft hair and even softer skin, I hear Aletta moan at my touch."
    "She's getting ever more wet with each moment that passes."
    "And the heat I thought I felt before now seems to be melting her too."
    show aletta blush b naked with fade
    "Without warning, Aletta breaks off the kiss."
    "Which leaves me standing there, literally open-mouthed."
    if aletta.flags.buttplug:
        show aletta doggy plug with fade
    else:
        show aletta doggy with fade
    "But then I see how she's bending over and beginning to kneel on the bed."
    "I watch as she spreads her buttocks, as if inviting me to take full advantage."
    "And it's not an invitation that I'm about to turn down either."
    "I lean in close, the fingers of one hand quickly finding their way back to Aletta's pussy."
    "This time, the way that she's spread her legs makes it that much easier."
    "My thumb and middle finger part her lips still further, while the index finger slips inside of her."
    "The sound that this makes is almost as good as the way it feels."
    "But what's better than both is the way Aletta begins to moan."
    "She looks back over her shoulder, almost panting at my efforts."
    "It's then that I remember how close I am to her ass too."
    "And it only takes a moment to pull her buttocks apart."
    if aletta.flags.buttplug:
        "At first, I'm more than a little surprised to discover something blocking my progress."
        "But then I remember that the rubbery object clenched in Aletta's ass is actually a butt plug."
        "Or to be more specific, the butt plug that I bought her myself!"
        "Smiling to myself at the thought it's been up there all evening, I reach out for it."
        $ aletta.sub += 1
        "And I give it a little tap and wiggle before moving on to where I really want to be."
        "Aletta groans in pleasure at even such a small manipulation of the toy."
        "The plug refuses to budge at first, as Aletta's muscles contract around it."
        "But with some determined pulling and twisting, it finally begins to work its way out."
        "The whole time this is happening, Aletta groans in pleasure at my efforts."
        "A sound that's only drowned out by the almost comical sound the plug makes when pops out of there."
    hide aletta
    show aletta rimming hand finger with fade
    "Then I let my tongue do the rest..."
    "At this, Aletta's moans become almost pained, and yet also desperate for more."
    "As my tongue licks and probes around her ass, I feel her hand grasping the back of my head."
    "It's all that I can do to keep her from forcing my face between her cheeks!"
    "But I still manage to keep it up all the same."
    aletta.say "My ass..."
    aletta.say "My ass..."
    aletta.say "Oh shit..."
    $ aletta.love += 1
    show aletta rimming hand finger ahegao
    aletta.say "Play with it...please!"
    "I do exactly as I'm told, teasing her with the promise before actually doing so."
    "And Aletta continues to melt, becoming like putty in my hands - or under my tongue!"
    aletta.say "I want more, [hero.name]."
    aletta.say "Please?!?"
    "Given the circumstances, how can a I even think of saying no?"
    return

label aletta_fuck_date_titjob:
    "I hurry over to the bed, tugging my clothes off as I go."
    "Aletta follows at a far more leisurely pace, chuckling to herself at my haste."
    "I have most of my clothes off in a matter of seconds, almost tripping over my pants."
    hide aletta with vpunch
    "But when I turn around, I lose my balance and fall backwards onto the bed."
    "And it's not because of my own clumsiness either."
    hide aletta
    show aletta close b naked
    "It has a lot more to do with the fact that I find Aletta's breasts thrust into my face!"
    "Somehow she's managed to strip off while I had my back turned."
    "And now she's looming over me, a knowing smile on her face."
    "Well, on the part of her face that I can actually see."
    "Aletta's breasts are more than big enough to get in the way!"
    aletta.say "Ah, will you look at that."
    aletta.say "You've fallen at my feet!"
    show aletta titjob with fade
    "Aletta kneels down on the floor by the bed, pushing my legs apart."
    "Resting her arms on my thighs, she shuffles as close to me as she can get."
    "As you might have guessed, my cock's as hard as it can get by now."
    "And it's standing straight up as Aletta comes closer."
    "Her breasts reach it before the rest of her catches up."
    "And I feel her nipples brushing against the shaft as they sway from side to side."
    "Aletta leans forwards, pulling her breasts apart as she does so."
    "As soon as my cock is in the space that this creates, she lets them go again."
    "The sensation of Aletta's boobs embracing my cock is something else."
    "They're soft and warm, obviously, like a pair of cushions."
    "But the weight of them instantly reminds me they're so much more than that."
    "And when she begins to press them together with her hands..."
    "The feeling's almost too good to put into words!"
    "But I'll try my best, okay?"
    aletta.say "You like that, huh?"
    aletta.say "You like the way that feels?"
    "This time I nod desperately, anything to keep Aletta going."
    "And she smiles in return, redoubling her efforts."
    "Aletta moves her chest up and down as she keeps on squeezing."
    "The motion is enough to make me gasp at the sensation it creates."
    "I keep on nodding the whole time, like I can't help it."
    "And that fact seems to amuse Aletta, who chuckles and purrs with delight."
    "A moment later, the head of my cock pops up from her cleavage."
    "Aletta gasps at the sight of it, as if she's spellbound."
    "Her breasts are travelling the entire length of the shaft by now."
    "Sinking down close to my balls and then climbing almost to the tip."
    "Whenever her breasts are near the bottom, Aletta's mouth is at the other end."
    show aletta titjob droll
    "Each time it comes dangerously close to her lips, she opens them wide."
    "All that comes out is a sigh, but I can see that she's teasing me."
    "Letting me think that, just maybe, she might slip it in there."
    "And the moment it moves out of range, she shoots me a knowing glance."
    "I can feel the desire rise in me every time she denies me like that."
    "It's almost doing as much to get me off as the boog-job itself!"
    "Aletta licks her lips and pouts, so that they glisten above me."
    "I've never wanted to kiss those lips as much as I do right now."
    "And the only other thing I can think about is being inside of Aletta too!"
    mike.say "Uh..."
    mike.say "Oh shit..."
    mike.say "Aletta, I'm going to cum!"
    if aletta.flags.submissive_interact:
        aletta.say "Then, use me as a target practice!"
    menu:
        "Cum on her breasts":
            show chest_insert aletta zorder 1 at zoomAt(1, (40, 160))
            "I feel like every bit of me's been squeezed between Aletta's breasts."
            "And now she's finally squeezed everything out of me too!"
            "So when it happens, where else is all that stuff going to go?"
            show aletta titjob surprised cumshot with vpunch
            "I shoot my load straight up in the air."
            show chest_insert aletta cum
            show aletta titjob -cumshot dickcum normal
            with vpunch
            $ aletta.love += 4
            "Which means that when it comes back down, it spatters all over Aletta's chest."
            "She lets out breathless gasps as she massages in into her skin."
            "Moaning with pleasure as she does so."
            hide chest_insert
        "Cum on her face":
            "At the last moment, Aletta leans in close."
            "Which means that she's right in the firing line!"
            show aletta titjob cumshot surprised with vpunch
            "I shoot my load, and it hits her square in the face."
            with vpunch
            "Aletta yelps in surprise as it does so."
            with vpunch
            "Lines of white cum stripe both of her cheeks."
            show aletta titjob -cumshot normal cum face
            $ aletta.sub += 2
            "Some runs down her nose and some lands in her open mouth."
            "The rest rolls downwards, dripping off her chin and onto her chest."
        "Cum in her mouth":
            "Finally, at the last possible moment, Aletta does it."
            show mouth_insert aletta zorder 1 at zoomAt(1, (40, 160))
            "She leans down and wraps her lips around the head of my cock."
            show mouth_insert aletta cum
            show aletta titjob cumshot
            with vpunch
            "I shoot my load literally the next second."
            with vpunch
            "Aletta licks and laps at the tip as it spurts out."
            with vpunch
            "She swallows most of it straight down."
            show aletta titjob -cumshot cum mouth
            $ aletta.love += 2
            $ aletta.sub += 1
            "But some dribbles out of her mouth as she does so."
            "And I watch as she chases these last few drops."
            show aletta titjob -cumshot -cum -mouth
            show mouth_insert aletta -cum
            "Licking her lips clean with a look of satisfaction on her face."
            hide mouth_insert
    "Afterwards I lay there, panting and exhausted."
    "Aletta climbs onto the bed beside me, more relaxed than spent."
    "I can feel the soft weight of her breasts against me."
    "And the sound of her breath is sighing into my ear."
    return

label aletta_fuck_date_missionary(sexperience_min):
    show aletta missionary nomc with fade
    "Without a single word passing her lips, Aletta slinks onto the bed and reclines on her back."
    "I can see the entirety of her naked body, laid out before me now."
    "She looks as beautiful as a work of art, and as sexy as fuck all at the same time."
    if not aletta.is_sex_slave:
        aletta.say "Well, what are you waiting for, [hero.name]?"
        aletta.say "A written invitation?"
        "I shake my head, trying to get back into the moment."
    else:
        aletta.say "Could you please use me, Master?"
    show aletta missionary -nomc with fade
    "She makes no effort to move as I crawl atop her, simply holding my eye and smiling."
    "I'm taken with the sight of her at the way she feels beneath me."
    "So much so that I totally fail to notice that Aletta remains patiently silent the whole time."
    "Suddenly I realise that she's waiting for me to do something, to take control of the situation."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and aletta.sub >= 50:
            "I could just stampede towards Aletta's pussy right now."
            "That would be a pretty natural thing to do."
            show aletta missionary anal
            "But it just seems so...I don't know...obvious!"
            "That's why, as I push my cock between Aletta's thighs, I go in lower than usual."
            "She doesn't notice anything amiss at first, just sighing in anticipation."
            "It's only when the tip of my cock first probed between her buttocks that she knows something's amiss."
            if not aletta.is_sex_slave:
                aletta.say "Ooh...[hero.name]!"
            else:
                aletta.say "Ooh...Master!"
            aletta.say "You're going to end up in my..."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "Before Aletta can finish uttering the words, I make my first thrust into her."
            aletta.say "ASS...ASS!"
            show aletta missionary pleasure
            aletta.say "You're in my ass!"
            "But all too soon her words begin to fade into mere moans."
            "And these come only in response to the sensation of my cock pushing further inside."
            "I watch in genuine fascination as Aletta's eyes begin to roll back into her head."
            "Then she seems to fall back into the pillows, her entire body surrendering."
            "The experience of being fucked up the ass seems to have overwhelmed Aletta."
            show aletta missionary normal at stepback(speed=0.1, h=10, v=5)
            "But for me it's only just begun, and I continue to pound into her as hard as I can."
            "Somehow this feels so much more intense than fucking her pussy."
            "And the effect that it's having on Aletta is almost as enjoyable as the sensation itself."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "Watching as this normally strong and confident woman is reduced to a quivering mass is pretty intense."
            "And knowing that it's all on account of me taking her like this makes it all the more enjoyable."
            "The usual expression of haughtiness and superiority has been completely wiped off of her face."
            show aletta missionary ahegao at stepback(speed=0.1, h=10, v=5)
            "Instead her eyes are glazed and her mouth hangs open, tongue lolling out like that of a dog."
            "It's not a modern or PC thought to have, but I feel kind of like I've conquered Aletta right now!"
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "But it's not like this conquest hasn't come at a price for me too."
            "And speaking of cumming..."
            if aletta.flags.submissive_interact:
                aletta.say "[hero.name], use me as a target practice!"
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            call cum_reaction (aletta, 'anal', sexperience_min) from _call_cum_reaction
            if _return == 'anal_inside':
                "I know that there's only a couple of seconds left before I lose it."
                "But I'm enjoying the sensation of being buried so deep inside of Aletta."
                show aletta missionary at stepback(speed=0.1, h=10, v=5)
                "So in the end, I just keep right on going and lose myself in her."
                "I have no idea if she's even aware of what's happening as I do so."
                show aletta missionary ahegao creampie inserts with hpunch
                "Her spaced-out expression and moans of pleasure continue throughout the whole thing."
                with hpunch
                "But for me it feels as though I have to force my cock as far up Aletta as possible."
                with hpunch
                "I ride her until the very last moment, savouring the sensation for all it's worth."
                "Afterwards I try to hold myself up on shaking arms, but collapse in exhaustion."
                "And I'm thankful for the pillow her breasts provide for my head."
                $ aletta.sub += 1
                $ aletta.love += 2
            elif _return == 'anal_outside':
                "I know that there's only a couple of seconds left before I lose it."
                "But as much as I'm enjoying the sensation of being buried so deep inside of Aletta, I want more."
                show aletta missionary at stepback(speed=0.1, h=10, v=5)
                "I feel like I need to make one last gesture, do something that'll top it all off."
                "And that's why I struggle to pull my cock out of her ass in the moments before I actually cum."
                show chest_insert aletta zorder 1 at zoomAt(1, (840, 100))
                show belly_insert aletta zorder 2 at zoomAt(1, (60, 140))
                show aletta missionary -anal
                "As I do so, Aletta's eyes begin to regain some focus, as if she's returning to her senses."
                "By the time I'm free of her and ready to blow, she's shaking her head like someone waking up from being dazed."
                show chest_insert aletta cum
                show aletta missionary cumshot
                with hpunch
                "But that's the very same instant in which I cum, loosing streams of warm semen over her breasts."
                show belly_insert aletta cum
                show aletta missionary cum onbody
                with hpunch
                "Most of it misses Aletta's face, but some does manage to spatter over her chin."
                "She opens her mouth wider at the sensation, as if trying to instinctively lap up the cum."
                "All I can do is pant and gasp as I watch her."
                $ aletta.sub += 2
                $ aletta.love += 1
                hide chest_insert
                hide belly_insert
            $ aletta.flags.anal += 1
        "Fuck her pussy":
            "There's a time and a place for getting adventurous, but I'm pretty sure this isn't it."
            "I have Aletta spread out before me, there for the taking."
            "So the last thing I'm going to do is overthink this thing."
            "I can see Aletta's pussy right now, and it's calling to me!"
            call check_condom_usage (aletta, 180) from _call_check_condom_usage
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show aletta missionary condom
            "As the head begins to rub against the folds of her pussy, Aletta lets out a soft moan."
            "It's such a quiet, gentle sound that it takes me by surprise coming from such a forceful woman."
            show aletta missionary vaginal at stepback(speed=0.1, h=10, v=5)
            "But her moans aren't the only thing that's soft, and my cock slips into her with almost no effort at all."
            "As I do so, I almost can't decide where to cast my eyes over Aletta's naked body spread out before me."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "Her beautiful face is a picture of arousal and delight, almost enough to make me cum on its own."
            "And yet then there's the sight of her breasts, huge and heavy as they heave upon her chest."
            "But perhaps it's the actual feeling of being so deep inside of Aletta that's the best thing of all."
            show aletta missionary pleasure at stepback(speed=0.1, h=10, v=5)
            "It feels so good that I move as slowly as I can, thrusting back and forth almost in slow-motion."
            "Aletta's so deep, soft and warm that I want to savour every single moment that I have my cock inside of her."
            "I lay myself almost flat atop her as I'm doing this, pressing my chest against her own."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "The feeling of Aletta's breasts as they're pressed beneath me only adds to the sensation."
            "And I can feel just how hard her nipples are getting as they rub against my skin."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "All of this is enough to make me quicken my pace, getting faster with each passing second."
            "And as I do so, the expression on Aletta's face begins to alter as well."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "Where before her features showed an expression of pleasure, now that becomes ever more intense and exaggerated."
            show aletta missionary ahegao
            "I watch in fascination as her eyes become glazed and her pupils actually roll back into her head."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "Every gasping breath that escapes her mouth leaves it wider and more slack."
            if aletta.flags.submissive_interact:
                aletta.say "U..."
                aletta.say "Use me as a..."
                aletta.say "A target practice..."
            "Soon Aletta's tongue is almost lolling between her lips like that of a dog."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "It's almost as though she's been taken to the point of no return and is about to fall off the edge."
            "The thought seems to have a profound effect on me, urging me towards my own end as well."
            show aletta missionary at stepback(speed=0.1, h=10, v=5)
            "No more than a moment later, I know that I'm about to cum..."
            call cum_reaction (aletta, 'vaginal', 5) from _call_cum_reaction_1
            if _return == "vaginal_outside":
                "There's only seconds left before I lose it completely."
                show aletta missionary at stepback(speed=0.1, h=10, v=5)
                "I'm enjoying the sensation of being buried so deep inside of Aletta, but I want more."
                "It's like I need to make one last gesture, do something that'll top it all off."
                "So I struggle to pull my cock out of her pussy before I actually cum."
                show chest_insert aletta zorder 1 at zoomAt(1, (840, 100))
                show belly_insert aletta zorder 2 at zoomAt(1, (60, 140))
                show aletta missionary -vaginal
                "Aletta's eyes begin to regain some focus, as if she's returning to her senses as I do so."
                "By the time I'm free of her and ready to blow, she's shaking her head like she's waking up."
                show chest_insert aletta cum
                show aletta missionary cumshot
                with hpunch
                "But that's the very same instant in which I cum, loosing streams of warm semen over her belly and breasts."
                show belly_insert aletta cum
                show aletta missionary cum onbody
                with hpunch
                "Most of it falls short of Aletta's face, but some does manage to spatter up and over her chin."
                "She opens her mouth wider at the sensation, as if trying to instinctively lap up the cum."
                "All I can do is pant and gasp as I watch her efforts."
                hide chest_insert
                hide belly_insert
                $ aletta.sub += 1
            elif _return == "vaginal_condom":
                "I'm painfully aware of how little time there is before I lose it."
                show aletta missionary at stepback(speed=0.1, h=10, v=5)
                "And it feels so good to be buried this deep inside of Aletta's pussy."
                "So I make no effort to pull out, just keeping right on until the end."
                "I don't know if Aletta's aware of what I'm doing."
                "Her expression is still one of simple, spaced-out pleasure."
                with hpunch
                "And so all I can do is keep right on, pushing into her as I cum."
                show aletta missionary ahegao inserts with hpunch
                "I stay inside of Aletta for as long as I can manage, but soon my strength gives out."
                with hpunch
                "And I collapse in utter exhaustion, her body meeting mine."
                "Unable to say a word, I bury my head in Aletta's breasts."
                $ aletta.love += 1
            elif _return == "vaginal_inside_pill":
                "In those last few moments, I remember the need to pull out."
                show aletta missionary at stepback(speed=0.1, h=10, v=5)
                "I try to yank my cock out of Aletta, but I feel her hands on my wrists as I do so."
                show aletta missionary normal
                aletta.say "No need..."
                aletta.say "Pill..."
                show aletta missionary pleasure
                "Her words are like music to my ears, and I instantly reverse my efforts."
                show aletta missionary ahegao creampie inserts with hpunch
                "This newfound enthusiasm catches Aletta off-guard, making her practically howl."
                with hpunch
                "She cums at almost the same second that I finally burst inside of her."
                with hpunch
                "And she rides my cock until the very last moment possible."
                $ aletta.love += 2
            elif _return == "vaginal_inside_pregnant":
                "I don't need to be told that it's safe to cum inside of Aletta."
                "The warm, welcoming curve of her belly beneath me is more than enough of a reminder."
                "It keeps me from leaning in closer as I lose myself in her."
                show aletta missionary ahegao creampie inserts with hpunch
                "But I can tell from the look on her face as she begins to return to her senses that I've done enough."
                with hpunch
                "As I slow down, becoming more gentle with my motions, I do all I can to make her cum too."
                with hpunch
                "And when she finally does, the moment between us is tender and gentle."
                "Quite the contrast to what came before it."
                "Maybe a glimpse at what the future holds for us."
                "And the life growing inside of her too..."
                $ aletta.love += 2
            elif _return == "vaginal_inside_mad":
                "I'm so caught up in the moment that I can't think of anything else."
                show aletta missionary ahegao creampie inserts with hpunch
                $ aletta.love -= 5
                # $ aletta.impregnate()
                "One moment I'm feeling the surge of my orgasm and the very next I'm cumming."
                hide aletta
                show aletta naked angry with fade
                "It's only when Aletta's voice cuts through it all that I realise what's happened."
                aletta.say "[hero.name]...[hero.name]!"
                aletta.say "Oh shit...shit!"
                mike.say "What is it, Aletta?"
                mike.say "What's the matter?"
                show fx anger
                aletta.say "You...you just came in me!"
                "My mouth moves, but no words come out."
                "Aletta and I can only stare at each other, stunned by the enormity of what just happened."
            elif _return == "vaginal_inside_happy":
                "I'm so caught up in the moment that I can't think of anything else."
                show aletta missionary ahegao creampie inserts with hpunch
                "One moment I'm feeling the surge of my orgasm and the very next I'm cumming."
                with hpunch
                "It's only when Aletta's voice cuts through it all that I realise what's happened."
                hide aletta
                show aletta naked blush
                with fade
                $ aletta.love += 6
                #$ aletta.impregnate()
                if not aletta.is_sex_slave:
                    aletta.say "[hero.name]...[hero.name]!"
                else:
                    aletta.say "Master...Master!"
                mike.say "Oh shit...Aletta..."
                mike.say "What have I done?!?"
                "Aletta shakes her head desperately, holding onto me tightly."
                aletta.say "No...no...it's okay."
                aletta.say "I want this...I want to have your baby!"
                "My mouth moves, but no words come out."
    return

label aletta_fuck_date_cowgirl(sexperience_min):
    "She shoves me backwards so that I collapse onto the bed, and then follows me down onto it."
    "I seem to fall back with Aletta atop me the whole time, rather than having her land upon me."
    "And she's clambering over me the whole time, trying to keep a hold."
    if aletta.sexperience == 0:
        "I can't recall how many times I've daydreamed about fucking Aletta in the past."
        "While watching her bending over the photocopier or crossing her legs in the middle of a boring meeting."
        "Pressing her up against the glass of my office window and making her scream for mercy."
        "But nothing could have prepared me for the experience of having her climb atop me, naked and intent upon having her way with me."
        "I can't help but run my hands up and down her pale-skinned body, tracing her curves."
        "Likewise I keep trying to kiss and nibble at her erect nipples as her breasts sway invitingly above me."
        if not aletta.is_sex_slave:
            aletta.say "[hero.name] - I want you to fuck me now."
            aletta.say "And I want you to fuck me hard."
            aletta.say "Have you got that?"
        else:
            aletta.say "Please Master..."
            aletta.say "Could you fuck your slave really hard?"
        "What can I possibly do, other than nod frantically and try to do as I'm told?"
    elif aletta.is_sex_slave:
        "I reach out instinctively and grab hold of the lead dangling from Aletta's collar."
        "She instantly feels the first yank that I give it, stopping her efforts to take the upper hand."
        "Instead, she sits up on her haunches, straddling me just below the waist and awaits further instructions."
        mike.say "That's a good girl, Aletta."
        mike.say "Enthusiasm's all well and good, but you need to wait for my orders first."
        "Aletta looks a little downcast, though she nods her head in submission."
        show aletta blush
        aletta.say "Yes, Master...I'm sorry, Master."
        mike.say "Apology accepted, Aletta."
        mike.say "I'm going to fuck you now, Aletta - would you like that?"
        aletta.say "Oh, yes, Master - I'd like that very much!"
    else:
        "Aletta entwines her fingers with mine, and we begin to play a game of each trying to overpower the other."
        "She tries to hold me down, while I try to push upwards and take her nipples in my mouth as she dangles them over me."
        "At the same time, I can feel the moments when the head of my now stiff cock rubs against her lips."
        "She's already slick and I can sense the desire in her each and every time we tease ourselves in this way."
        aletta.say "Ah...[hero.name]...I want you inside of me..."
        aletta.say "Please...don't make me wait for you!"
    "All I can feel right now is the heat of Aletta's slick pussy as it presses against my cock."
    menu:
        "Fuck her pussy":
            scene bg black
            show aletta cowgirl with fade
            "It'd be just as easy to slip my dick into Aletta's ass, she's already so well lubricated with sweat."
            "But her pussy just seems to be calling out to me right now, and it's not something that I'm going to ignore."
            call check_condom_usage (aletta, 180) from _call_check_condom_usage_1
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show aletta cowgirl condom
            "All it takes is one or two subtle moves on her part, and she has me just where she wants me."
            "I suppose it's a happy coincidence that's right where I want to be right now too."
            show aletta cowgirl vaginal
            "With a little twist of her waist that's translated into a movement of her buttocks, Aletta sinks down onto my cock."
            "Don't take this the wrong way, but Aletta's pussy is a lot like the girl herself."
            "It's impressive and more than a little intimidating at first."
            "But once you get into it, you discover a sensuality that's just as intense hiding beneath."
            show aletta cowgirl pleasure down
            "Aletta lowers herself slowly onto me, moaning a little more with each successive inch that enters her body."
            "She's tight, gripping me like a fist at times, but that just makes the sensation all the more intense and enjoyable."
            show aletta cowgirl raised
            "Once she's taken me as deep into her as possible, she leans forwards, so that my cock is almost horizontal."
            show aletta cowgirl down
            pause 0.35
            show aletta cowgirl raised
            pause 0.35
            show aletta cowgirl down
            "Then she begins to move back and forth, slowly at first, but with increasing speed as she uses me to get herself off."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            "Aletta's heavy breasts are being dragged up and down my chest the whole time, their nipples stroking my skin as they go."
            show aletta cowgirl raised cum
            pause 0.25
            show aletta cowgirl down bounce at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "I hardly have to move a muscle, as Aletta's doing enough to make me pant from the sheer pleasure on her own."
            show aletta cowgirl raised bounce ahegao
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "So I keep my hands occupied by stroking her thighs and squeezing her firm buttocks as she works herself towards her climax atop me."
            if aletta.flags.submissive_interact:
                aletta.say "[hero.name]! Use me as a target practice!"
            if CONDOM:
                "With nothing to hold me back, I feel myself let go inside of Aletta."
                "She makes the moment that much more intense by cumming a second later herself."
                "It's almost too hard to hold onto one another, with us bathed in each other's sweat."
                "But somehow we manage to cling together and ride it out with our faces pressed together, side by side."
            show aletta cowgirl smile
            "I bite my lip and try to remember where I am and what I'm doing."
            show aletta cowgirl raised bounce
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "But all I can feel is the approaching climax."
            menu:
                "Cum inside":
                    "I'm no more than seconds away from cumming when I realise that Aletta seems to be struggling with me."
                    "With no way to tell if she's reaching her own peak or trying to separate herself from me, I choose to hold onto her."
                    show aletta cowgirl raised
                    pause 0.15
                    show aletta cowgirl raised creampie cum with vpunch
                    "I cum no more than a heartbeat later, feeling myself burst inside of Aletta and not moving until it's all over."
                    with vpunch
                    if CONDOM:
                        if not aletta.is_sex_slave:
                            aletta.say "[hero.name]...you...you came inside me!"
                        else:
                            aletta.say "Master...you...you came inside me!"
                            aletta.say "Thank you so much!"
                    else:
                        if not aletta.is_sex_slave:
                            aletta.say "[hero.name]...you...you came inside me - without a rubber!"
                        else:
                            aletta.say "Master...you...you came inside me - without a rubber!"

                            aletta.say "Thank you so much!"
                    "I'm somehow more worried about the tone of her voice than the reality of what I just did."
                    "As I honestly can't remember hearing even a hint of fear in Aletta's voice before this moment."
                "Pull out" if hero.sexperience >= (sexperience_min + 10):
                    "Somehow I still have the presence of mind to pull out before I cum inside of her."
                    "But she's not going to make it easy for me, as Aletta is effectively pinning me down with her entire body."
                    "I wrestle with her for a few seconds, all the time expecting to cum at any second."
                    "Mistaking my efforts for some kind of final embrace, Aletta playfully grapples with me, frustrating my efforts."
                    show aletta cowgirl raised -vaginal cumshot with vpunch
                    "In the end I'm forced to twist sideways, casting her off me as I slip out of her and cum at the same instant."
                    show aletta cowgirl -cumshot dickcum with vpunch
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and aletta.sub >= 50:
            scene bg black
            show aletta cowgirl with fade
            "Maybe it's the devil in me, but as soon as I get the notion of taking Aletta up the ass, I can't think of anything else."
            "I just have to see what the expression on that haughty, arrogant face of hers will look like."
            "So as she reaches down to line my cock up with her pussy, I reach out and grab hold of her wrist."
            "She tries to fight me, but I'm just that bit too strong for her, and I manage to force her hand backwards by the exact amount needed."
            show aletta cowgirl anal pleasure down
            "And then I thrust with the entirety of my weight behind the effort."
            "I know that I've hit the target more from the expression that explodes onto Aletta's face than actually feeling my cock go up her ass."
            "At first it's shock at the sensation, then comes indignation, followed by a wave of embarrassment."
            show aletta cowgirl raised
            "But then, finally, her face melts into an almost delirious expression of pleasure."
            if not aletta.is_sex_slave:
                aletta.say "Oh...oh...[hero.name]..."
            else:
                aletta.say "Oh...oh...Master..."
            aletta.say "You're in my ass!"
            show aletta cowgirl down
            "I can feel the muscles clenching in protest, squeezing my cock in a way that only makes me want to push still further in."
            mike.say "Tell me how it feels, Aletta?"
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down
            "I've begun to thrust in and out of her now, meaning that Aletta can't help but writhe as I fuck her ass."
            show aletta cowgirl ahegao down
            aletta.say "It...it feels...incredible!"
            show aletta cowgirl raised
            mike.say "Do you like it, Aletta?"
            mike.say "Do you like having my cock up your ass?"
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            "She moans again, as I push harder."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            aletta.say "Yes...yes..."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            mike.say "Tell me what you like, Aletta."
            aletta.say "I...I like having your cock up my ass..."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            aletta.say "Please...don't stop...fuck my ass harder!"
            if aletta.flags.submissive_interact:
                aletta.say "Please... use my ass as a target practice!"
            show aletta cowgirl raised cum
            pause 0.25
            show aletta cowgirl down bounce at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "The combination of being inside of her and hearing those words from her is almost too much for me."
            show aletta cowgirl raised bounce ahegao
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "I can feel myself cumming a few moments later."
            show aletta cowgirl smile
            "I bite my lip and try to remember where I am and what I'm doing."
            show aletta cowgirl raised bounce
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "But all I can feel is the approaching climax."
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl raised creampie cum with vpunch
            "Still burning with shame and arousal, Aletta casts her head back as I cum deep inside of her ass."
            with vpunch
            "I can't see her face, but the evidence is clear that she's almost overwhelmed by the sensation."
            with vpunch
            "One hand kneads and massages her breasts as if to release some of the pent up energy."
            "The other slides down to her pussy and begins to stroke away in earnest for much the same reason."
            $ aletta.flags.anal += 1
    show aletta cowgirl pleasure
    "Aletta collapses into a panting heap, falling half across me as she does so."
    "I don't have the energy to turn her over, and so I do my best to turn our mess of slippery limbs into an embrace."
    show aletta cowgirl smile
    "For once, Aletta is still and utterly silent, and I can only assume that she's utterly satiated."
    "And exhausted too - as she slowly begins to make a curious noise that I take a while to identify as snoring."
    "Deep, long and satisfied - Aletta snores a little like a bustling sawmill."
    "Not that I'm complaining, as I quickly discover that I find the sound quite soothing."
    "And it's making me feel sleepy too..."
    return

label aletta_fuck_date_doggy(sexperience_min):
    $ game.play_music("music/roa_music/city_nights.ogg")
    show aletta doggy mike with fade
    "I thought that the date with Aletta tonight went well."
    "But now, she's down on all fours, right there in front of me."
    "It's pretty clear that there's only one thing that she wants from me."
    "And I'm damn sure it's the exact same thing I want from her too."
    "So the only logical thing to do is go right ahead and give it to her..."
    menu:
        "Fuck Aletta in the ass" if hero.sexperience >= (sexperience_min + 5):
            if foreplay:
                "Weird as it might sound, eating her ass out has given me a real taste for it."
                "And that's why I find my attentions fixated on that hole rather than the other one."
                "Somehow, I just know that I won't be satisfied until I feel my cock inside of it."
                "So I grab her firmly by the buttocks, spreading them to make this happen."
            "I take a moment to stare down at Aletta's ass, now that she's exposed."
            "Between her full, rounded buttocks is the most inviting hole I can imagine."
            "It looks so tight and neat, almost impossible to penetrate."
            "But all that does is make me all the more determined to get in there."
            "In fact, I can feel my cock stiffening at the mere thought."
            "So with Aletta's ass finally exposed, I don't waste another moment."
            "I aim my cock straight at the target, and push the tip inside."
            show aletta doggy mike hand anal pleasure
            "Aletta looks back over her shoulder as I do this, catching my eye."
            "She must have known what was coming the second she felt me part her buttocks."
            "But the look of surprise on her face as I sink into her is something else."
            "Of course, I'm feeling the sensations of forcing my way into her."
            show aletta doggy mike hand anal normal
            "But I can now see those same feelings reflected in her face too."
            aletta.say "Hmm..."
            aletta.say "Oh...that feels so good!"
            aletta.say "Please, don't stop..."
            if aletta.flags.submissive_interact:
                aletta.say "A target practice... Use me as a target practice!"
            "I take this as permission to start thrusting in and out more quickly."
            show aletta doggy mike hand anal ahegao
            "And I can see an almost instant reaction on Aletta's face."
            "Her mouth opens ever wider, and her eyes seem to almost glaze over."
            "Aletta's head sags forward, as if it's becoming too much effort to hold it up."
            "And at the same time, her words are lost amongst more animal sounds."
            "Every time I feel myself slapping against her buttocks, she seems to become more feral in nature."
            "For a girl that appears to be prim and controlled most of the time, it's quite a dramatic change."
            "But seeing my efforts reduce her to such a helpless state is a massive turn-on."
            "Before I know it, I'm all but pounding Aletta's ass with all my might."
            "Which quickly sees her dissolving into a mass of unresisting flesh around my cock."
            "In fact, I'm so engrossed in the act, that my climax comes as a complete surprise..."
            call cum_reaction (aletta, 'anal', sexperience_min) from _call_cum_reaction_2
            if _return == 'anal_inside':
                "There's no way that I'm even contemplating pulling out before the end."
                "I need to finish this thing the same way that I started it."
                "And that means keeping right on pounding Aletta's ass."
                show aletta doggy mike hand anal creampie with hpunch
                $ aletta.love += 2
                $ aletta.sub += 2
                "When I finally cum, it's in one last push that almost topples her over."
                with hpunch
                "But I have no idea if she's even aware of what's happening."
                "Afterwards, Aletta simply collapses onto the bed before me."
                "Her body slick with sweat and her breath coming in ragged gasps."
            elif _return == 'anal_outside':
                "I could just keep on pounding Aletta into the ground."
                "But something makes me stop before the inevitable happens."
                "I pull out with mere seconds to spare, hearing Aletta gasp as I do so."
                show aletta doggy mike -hand out cumshot with hpunch
                $ aletta.sub += 4
                "But what makes me smile is the sound that my cock makes as it comes out."
                show aletta doggy mike -hand out -cumshot cumbody with hpunch
                "Aletta keeps right on gasping as I cum over her buttocks and thighs."
                "Her head hanging down below her shoulders as she shudders from the force of the aftershocks in her muscles."
            $ aletta.flags.anal += 1
        "Fuck Aletta in the pussy":
            if foreplay:
                "All the time that I've been playing with Aletta's ass, I've been fingering her pussy too."
                "And when the moment comes to make a choice between the two, I don't even hesitate."
            "I can feel just how ready her pussy is for my cock, almost desperate for it."
            "So I waste no time in parting her buttocks just so, enough to let me get at my desired goal."
            call check_condom_usage (aletta, 180) from _call_check_condom_usage_2
            if _return == False:
                return "leave_without_gain"
            "I swear that I can already see the light reflecting off of Aletta's glistening lips."
            "And a moment later I feel them too, as the head of my cock slides along them."
            "Aletta shudders at the touch, and I feel myself doing the same in sympathy."
            "But then I take full advantage of just how ready for this she is right now."
            if CONDOM:
                show aletta doggy vaginal mike hand condom
            else:
                show aletta doggy vaginal mike hand
            "Wasting no more time, I push myself into Aletta's pussy in one smooth movement."
            "After the first instinctive resistance of her lips, there's nothing at all to hold me back."
            "And so I sink deep into her, feeling the way in which she responds to every inch of progress."
            "It's a sensation that I wish could go on for far longer, it's simply that good."
            "But all too soon I feel my skin pressing against Aletta's buttocks, telling me I can go no further."
            "I stay right there, motionless as seconds seem to stretch out."
            "I know that I should start moving soon, but I hate the idea of having any less of my cock inside of her."
            "In the end I settle for going as achingly slowly as I can, trying to savour each and every moment."
            "Aletta responds to this almost teasing pace better than I could have hoped."
            "Stoked from a smouldering desire and into a growing fire, she takes all that I can give her."
            "But as the motion of her body becomes ever faster, I find that my control is slipping away."
            "Pretty soon, Aletta's the one dictating the pace, as her voluptuous curves swing and sway."
            "All I can do is hold on for dear life as she begins to ride me without mercy."
            "In the space of mere moments, I've gone from feeling like the master to the slave!"
            "Aletta lets out moans and even what sound like grunts of sheer, naked arousal."
            "And then she surprises me by managing to actually speak through them too."
            aletta.say "Ah..."
            aletta.say "Yes...Yes..."
            aletta.say "I want all of it, [hero.name]..."
            aletta.say "I want all of it...NOW!"
            if aletta.flags.submissive_interact:
                aletta.say "Shoot me... Shoot me as a target practice!"
            "As if her words were an undeniable command, I feel my body leaping to obey."
            "I know that I'm about to cum."
            "And I know that it'll happen any second now!"
            call cum_reaction (aletta, 'vaginal', sexperience_min) from _call_cum_reaction_3
            if _return == "vaginal_outside":
                "There's nothing I want more than to keep going right now."
                "But I know that I have to stop and pull out before it's too late."
                "And when I do, the sound of dismay that Aletta makes could speak for us both."
                show aletta doggy mike -hand out cumshot with hpunch
                $ aletta.love += 1
                $ aletta.sub += 2
                "She continues to make the same low, almost desperate sounds as I finally cum."
                show aletta doggy mike out -cumshot cumbody with hpunch
                "Streamers of sticky, white semen paint her back, buttocks and thighs."
                "The whole time, her head hangs down, almost to the bedclothes as she gasps for breath."
            elif _return == "vaginal_condom":
                "I can't tell you how glad I am to have taken those couple of seconds to put on a condom."
                with hpunch
                "They mean that there's no interruption as I reach my climax, deep inside of Aletta."
                with hpunch
                "The feeling is incredible, but she instantly rewards me with her own reaction."
                with hpunch
                "Aletta writhes beneath me as if she's never felt anything like it before."
                show aletta doggy mike hand condom squirt ahegao with hpunch
                $ aletta.love += 1
                "And from that reaction, I'm pretty sure that she's cumming at almost the same time too."
                "Afterwards, there's nothing left to keep us upright, as we've spent all of our energies."
                "So we collapse together too, tumbling onto the bed in sheer exhaustion."
            elif _return == "vaginal_inside_pill":
                "Before I can even think of pulling out, I feel Aletta grab my wrist and hold on tight."
                aletta.say "Don't you...dare...stop!"
                aletta.say "I'm...on...the...pill!"
                "If there was any chance of me doing so, Aletta just put paid to it with her little speech!"
                show aletta doggy creampie vaginal mike hand squirt with hpunch
                $ aletta.love += 2
                "I cum almost as soon as she finishes gasping it out, filling her with all I have."
                with hpunch
                "Her words are washed away in a flood of panting and moaning at the sensation."
                with hpunch
                "I ride Aletta to the very end, enjoying every moment she's taking it."
            elif _return == "vaginal_inside_pregnant":
                "The sight of Aletta's swollen belly and massive breasts is all the reminder I need."
                "Pulling out would be pointless right now, as she's already as pregnant as I can hope to make her!"
                show aletta doggy creampie vaginal mike hand squirt with hpunch
                $ aletta.love += 3
                "This means that I can enjoy every last moment before I cum."
                with hpunch
                "And then savour the sensation of shooting my load, deep inside of her too."
                with hpunch
                "But I'm not alone in taking pleasure from this, as Aletta moans at the same time."
                "In fact, her lowing and the size of her almost reminds me of an animal giving birth!"
            elif _return == "vaginal_inside_mad":
                aletta.say "Wait...a...minute..."
                aletta.say "Did...you..."
                show aletta doggy creampie vaginal mike hand squirt with hpunch
                $ aletta.love -= 20
                $ aletta.sub -= 10
                #$ aletta.impregnate()
                "Before she can get the rest of her words out, I groan and shoot my load into Aletta."
                with hpunch
                "Instantly her head snaps around, and she fixes me with a fearful stare."
                "It's so unusual to see such an emotion on Aletta's face, that I can't help but pay attention."
                aletta.say "You...you came in me."
                aletta.say "Without a condom!"
                aletta.say "Oh, [hero.name] - this is not good, not good at all!"
            elif _return == "vaginal_inside_happy":
                "Before I can even think of pulling out, I feel Aletta grab my wrist and hold on tight."
                aletta.say "Don't you...dare...stop!"
                aletta.say "Cum...in...me...[hero.name]..."
                aletta.say "Use me...like...like a...cheap whore!"
                "If there was any chance of me doing so, Aletta just put paid to it with her little speech!"
                show aletta doggy creampie vaginal mike hand ahegao squirt with hpunch
                #$ aletta.impregnate()
                $ aletta.love += 6
                "I cum almost as soon as she finishes gasping it out, filling her with all I have."
                with hpunch
                "She makes meek little sighing noises as I finish off, almost delirious with pleasure at what I've done."
    return

label aletta_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "Normally when you invite a girl over to your place, you want to impress them, right?"
    "You're worried about giving off the right signals and coming over as a nice guy."
    "And with Aletta, there's all of that good stuff to deal with, just like any other girl."
    "But on top of it all, there's the fact that she also seems to have standards."
    "You know the kind of thing I mean - that there's a level below which she won't descend."
    "And sometimes the way she looks at me..."
    "Well, I have to wonder how close I am to that level myself!"
    "So when Aletta agrees to come over and take a dip in the hot-tub, I'm split down the middle."
    "On the one hand, I'm excited that she said yes."
    "But on the other, I can't help worrying she's going to be less than impressed by what she sees."
    "That's why I find myself sitting nervously in the tub, waiting for her to join me."
    show aletta swimsuit
    "And when she does walk out and strip off the towel she's wearing, I swallow audibly."
    show hottub aletta with fade
    "Aletta looks simply stunning as she walks over and climbs into the tub."
    "I'm not even aware that I'm staring until she looks at me with a frown on her face."
    aletta.say "[hero.name], whatever's the matter?"
    aletta.say "Your mouth is hanging open like you were slapped!"
    "I blink and shake my head, trying to wake myself up."
    "And I make sure to close my mouth until I regain the power of speech."
    aletta.say "Well, are you going to answer me?"
    aletta.say "What's the problem?"
    mike.say "Ah...yeah..."
    mike.say "Sorry, Aletta."
    mike.say "You just look so..."
    "Aletta raises an eyebrow, clearly starting to get annoyed."
    aletta.say "What, [hero.name]?"
    aletta.say "Come on, spit it out?"
    mike.say "Amazing, Aletta!"
    mike.say "You look so amazing!"
    "Aletta looks genuinely surprised at the compliment."
    "Almost like she's the one that's now lost for words."
    "I see her expression soften and a little smile appear on her face."
    "Sure, she might be a hard-ass when the need arises."
    "But she's still only human - and who doesn't like a compliment?"
    aletta.say "Why...thank you, [hero.name]."
    aletta.say "That's sweet of you to say."
    aletta.say "I...I don't get to wear this old thing very often."
    mike.say "Well, you should try to wear it more, Aletta."
    mike.say "It looks great on you!"
    "Aletta blushes a little, adding a bashful shake of the head."
    "But at the same time, she scoots closer to where I'm sitting in the tub."
    "Note for future reference - the way to Aletta's heart is through her ego!"
    aletta.say "You really think so?"
    aletta.say "Somebody once told me it was too revealing."
    mike.say "It's revealing, Aletta."
    mike.say "Sure it is."
    mike.say "But look at what it's revealing!"
    "I whistle and shake my head."
    "And now I can see that Aletta's cheeks are turning bright red."
    aletta.say "Oh, stop it, [hero.name]."
    aletta.say "You're making me blush!"
    "Aletta looks furtively around the yard and back at the house as she says this."
    aletta.say "Are...are your housemates in right now?"
    mike.say "Erm..."
    mike.say "No, Aletta - they're both out for a while."
    "Aletta nods at this, her gaze turned away from me."
    "But then she turns her head and looks me straight in the eye."
    aletta.say "In that case, forget what I just said, [hero.name]."
    aletta.say "Don't stop, okay?"
    aletta.say "Tell me just how good I look!"
    aletta.say "No, even better - show me how good I look!"
    "There's a fire in Aletta's eyes as she says this."
    "A need that she seems to want me to fulfil."
    "And so I don't hesitate to take hold of her a moment later."
    "Aletta makes a squealing noise as I grab her."
    "But I can't tell if it's from surprise or excitement."
    "Either way, she offers no resistance as I push her up against the edge of the tub."
    show hottub sex male aletta outside with fade
    "At the same time, I'm tugging down my trunks and kicking them away."
    "Being so close to Aletta means that I'm hard as a rock."
    "And I see her eyes go wide as she glimpses my stiff cock over her shoulder."
    call aletta_dick_reactions from _call_aletta_dick_reactions_1
    aletta.say "Mmm..."
    aletta.say "Now that does look good!"
    "A moment later, I part her buttocks and push it between them."
    "Aletta closes her eyes as I rub the head up and down the lips of her pussy."
    aletta.say "Oh..."
    aletta.say "It feels good too!"
    "I feel her open to me, and I don't hesitate to push inside."
    "And now it seems that she can't offer any more words to describe what she's feeling."
    show hottub sex male inside
    "Instead, Aletta lets out a long, low moan as I sink all the way into her."
    "By now, she's leaning against the edge of the tub as I push forwards."
    "And clinging onto it is all that seems to be keeping her from falling out."
    "But that doesn't stop me from keeping up the same pace that I've already set."
    "Aletta's pussy feels so good around my cock that I can't think of anything else."
    "All I want is to keep right on fucking her like this until the very end!"
    "And that's what she seems to want as well, nodding her head as I pound her."
    "But then again, maybe that's just her moving in sympathy with me?"
    "Whatever the reason, I don't let anything stop me."
    "And all too soon, I can feel the first stirrings down below."
    "I'm going to cum - and it'll be sooner, rather than later!"
    if aletta.flags.submissive_interact:
        aletta.say "[hero.name]! Use me as a target practice!"
    call cum_reaction (aletta, 'vaginal', 1) from _call_cum_reaction_4
    if _return == "vaginal_outside":
        show hottub sex male outside
        "Aletta moans as I pull my cock out of her before the final moments."
        show hottub cumshot with vpunch
        $ aletta.sub += 1
        "She looks back over her shoulder as I shoot my load over her buttocks and thighs."
        with hpunch
        "But I can't tell if she's grateful for me pulling out, or just for being fucked so hard."
    else:
        "Aletta seems to sense what's coming, looking back over her shoulder."
        show hottub cumshot with hpunch
        $ aletta.love += 1
        "And she holds my eye as I cum, filling her with all that I have to give."
        show hottub sex male ahegao with hpunch
        "Her cheeks are flushed and she's panting almost desperately."
        with hpunch
        "But she takes the whole thing without objection."
    "There's no mention of what Aletta thinks of my hot-tub after we've finished."
    "And there's likewise no mention of what I think of her swimsuit either."
    "It's as if what we just shared was enough to answer all of the questions we might have."
    "Well, for the time being, at least..."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ aletta.sexperience += 1
    $ game.active_date.clothes = None
    return

label aletta_fuck_mc_office:
    show aletta work at left with easeinleft
    "Aletta's true to her word, as I hear the sound of my door opening a few minutes later."
    show aletta at center with ease
    "But even so it feels like I've been waiting for an eternity until she comes striding in."
    "I can feel my cock stiffening the moment I lay eyes on her, my heart begin to beat faster."
    "And I know that I have to get my hands on her, no matter what the cost!"
    aletta.say "Well, here I am!"
    aletta.say "What's so important that you have to see me in person?"
    mike.say "Well...I..."
    show aletta annoyed
    aletta.say "Oh, come on - I haven't got all day!"
    mike.say "I want to have sex with you!"
    mike.say "Really badly, Aletta!"
    mike.say "I can't think about anything else!"
    "It all comes tumbling out of my mouth as Aletta presses me for an answer."
    "And I can see the change in her expression as I blurt out my confession."
    if aletta.sub < 0:
        show aletta flirt
        "Aletta raises an eyebrow and her lips curl into an ironic smile."
        "She lets out a low chuckle and shakes her head."
        aletta.say "Well, well..."
        aletta.say "Normally I'd have said no."
        aletta.say "But hearing you beg like that is SO amusing!"
    elif aletta.sub >= 75:
        show aletta blush
        "Aletta's whole demeanour changes as well, and dramatically so."
        "Before she had a confident and commanding presence."
        "But now Aletta nods and smiles, like she's eager to please me."
        if aletta.is_sex_slave:
            aletta.say "Why didn't you just come out and say that, Master?"
        else:
            aletta.say "Why didn't you just come out and say that, [hero.name]?"
        aletta.say "Of course you can have sex with me!"
        aletta.say "You can do ANYTHING you want to me!"
    else:
        show aletta happy
        "Aletta smiles and glances over her shoulder."
        "And I realise she's checking the door is closed."
        show aletta flirt
        "Then she turns her gaze back to me."
        if aletta.is_sex_slave:
            aletta.say "You could have just come out and said it, Master!"
        else:
            aletta.say "You could have just come out and said it, [hero.name]!"
        aletta.say "But yeah, we can have a little fun on company time!"
        aletta.say "Just so long as we don't get caught."
    "I'm up and out of my chair as soon as Aletta's done talking."
    "And I gesture for her to follow me over to the sofa in the corner."
    show aletta normal
    "Aletta follows, but at a far more relaxed pace."
    "She seems more than a little amused at my eagerness."
    "And this is reflected in the way that she begins to undress."
    "Where I tear off my clothes, Aletta removes them slowly."
    "This means that I'm teased with every step she takes."
    "Only when Aletta finally reaches the sofa does she her panties fall to the floor."
    if aletta.is_sex_slave:
        aletta.say "So how are we going to do this, Master?"
    else:
        aletta.say "So how are we going to do this, [hero.name]?"
    hide aletta
    call office_harem_fuck_choices ('aletta') from _call_office_harem_fuck_choices
    return

label aletta_fuck_office_choices:
    menu:
        "I'm up for a blowjob" if "aletta_kink_06" in DONE:
            call aletta_fuck_office_bj from _call_aletta_fuck_office_bj
        "We'll use the desk again." if "aletta_event_10" in DONE:
            call aletta_fuck_office_ceofuck from _call_aletta_fuck_office_ceofuck
        "I just want to eat you." if "aletta_event_04" in DONE:
            if game.week_day % 2 == 0:
                call aletta_event_04_sex from _call_aletta_event_04_sex
            else:
                call aletta_fuck_office_cunnilingus from _call_aletta_fuck_office_cunnilingus
        "I just want to eat you." if "aletta_event_04" not in DONE:
            call aletta_fuck_office_cunnilingus from _call_aletta_fuck_office_cunnilingus_1
        "It's time for your weekly training" if aletta.flags.weeklyspank and not aletta.flags.spankdelay and (game.days_played - aletta.flags.weeklyspank >= 7):
            call aletta_fuck_office_spank from _call_aletta_fuck_office_spank
        "I'm a little stressed today" if "aletta_stress_3" in DONE:
            call aletta_fuck_office_titjob from _call_aletta_fuck_office_titjob_1
        "You seem a little overstressed" if "aletta_kink_05" in DONE:
            call aletta_fuck_office_ropeplay from _call_aletta_fuck_office_ropeplay
        "Cowgirl":
            call aletta_fuck_office_cowgirl (0) from _call_aletta_fuck_office_cowgirl
        "Doggy" if hero.sexperience >= 10:
            call aletta_fuck_office_doggy (10) from _call_aletta_fuck_office_doggy
        "Forget it":
            aletta.say "Hum."
            $ hero.cancel_activity()
    return

label aletta_fuck_office_bj:
    mike.say "I want you to take out my cock and suck it - right now!"
    show aletta surprised
    "Aletta's eyes go wide at this new command."
    "But I see that it's not from offence or outrage."
    show aletta flirt
    "Instead it seems to actually be an eagerness to please!"
    "Aletta hurries to do as she's told, getting onto her knees and leaning in close."
    "She has my flies open in a matter of seconds and my cock out as quickly."
    scene aletta blowjob
    show aletta blowjob ceo
    with fade
    "I'm already getting hard from the sight of Aletta kneeling before me."
    "And the moment that her fingers are wrapped around the shaft, it's a done deal."
    "In any other circumstances, Aletta might have been more subtle."
    "And if not, I might have told her to take her time about it."
    "But she's acting on instinct, and I'm caught up in the moment too."
    show mouth_insert aletta zorder 1 at zoomAt(1, (860, 140))
    "This means that Aletta all but shoves my cock into her mouth."
    "She wastes no time in swallowing in as deep as she possibly can."
    show aletta blowjob pleasure
    "And then she begins to work away at it, head bobbing up and down."
    "I try my best to remain aloof, sipping my coffee the whole time."
    "But Aletta's putting so much sheer effort into it that I can't keep it up."
    "I drop the cup of coffee onto the floor and collapse backwards in my chair."
    "Gasping for breath, I hold onto the arms for dear life."
    "It feels like I can't hold on for a moment longer."
    "I'm going to cum!"










    "I just lie back and let Aletta finish the job all on her own."
    "And it doesn't take long for her to do it either."
    show mouth_insert aletta cum
    show aletta blowjob cum
    with vpunch
    "I shoot my load when my cock is as deep as it'll go."
    with vpunch
    "But for all her eagerness, Aletta's not ready for it."
    show aletta blowjob ahegao with vpunch
    "She coughs and gags as the cum hits the back of her throat."
    "Yet somehow she still manages to keep from spitting anything out."
    show mouth_insert aletta -cum
    show aletta blowjob -cum
    "And I watch as Aletta dutifully swallows every last drop."
    $ aletta.love += 1
    $ aletta.sub += 1
    hide mouth_insert
    return

label aletta_fuck_office_ceofuck:
    "I take a firm hold of Aletta."
    scene aletta ceofuck
    show aletta ceofuck vaginal
    with fade
    "And then I stand up, turning Aletta around and pushing her backwards onto the desk."
    "She cries out in surprise, but then realises what I'm doing."
    "Aletta braces her hands on the desktop, nodding eagerly."
    "And then I'm pounding her like my life depends on it."
    "Aletta keeps on nodding the whole time, urging me on."
    aletta.say "Oh yes..."
    if not aletta.is_sex_slave:
        aletta.say "Please, [hero.name]..."
    else:
        aletta.say "Please, Master..."
    aletta.say "Just like that..."
    aletta.say "Don't stop until you make me cum!"
    if aletta.flags.submissive_interact:
        aletta.say "Use me as your target practice!"
    show aletta ceofuck pleasure
    "Aletta's words are a turn-on for sure."
    "But it's not like I need the encouragement!"
    "It's like I can feel all the guilt draining out of me as I fuck her."
    "Every thrust and the moans it elicits from Aletta purge me of it."
    "She's right - Dwayne was an asshole that deserved everything he got."
    "And I deserve to be screwing Aletta in his office right now!"
    "All of my energy goes into one last thrust as I start to cum."
    show aletta ceofuck creampie with hpunch
    "Aletta moans as I shoot my load into her, wriggling her ass as she takes it."
    with hpunch
    "I keep my cock inside of her as she cums too, feeling every moment as she does so."
    $ aletta.love += 2
    $ aletta.sexperience += 1
    return

label aletta_fuck_office_spank:
    mike.say "Right here, Aletta."
    mike.say "I want you bending on my knees..."
    show aletta flirt blush
    "Knowing exactly what's going to happen, Aletta bends over my knees."
    hide aletta
    show spank aletta with fade
    "Aletta barely has time to cry out before I make my next move."
    "I take a firm hold of her skirt and hike it up to reveal her backside."
    show spank aletta spank
    play sound spank
    with hpunch
    "And then I lay the palm of my hand across it."
    "The sound it makes is like the crack of a whip."
    show spank aletta surprised
    "And Aletta cries out, more in surprise than pain."
    aletta.say "Ah..."
    aletta.say "M...my ass..."
    aletta.say "You...you spanked me!"
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "By way of an answer, I reverse the motion, catching Aletta on the backhand."
    "She cries out for a second time, looking back over her shoulder in surprise."
    mike.say "Noticed that, did you?"
    mike.say "Yeah, Aletta, I'm spanking you."
    mike.say "Again..."
    mike.say "And I'm not going to stop anytime soon either."
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "The third slap is almost as loud as the first."
    "It makes Aletta yelps in alarm."
    mike.say "The door's not locked, you know."
    mike.say "So anyone could walk in on us, Aletta."
    mike.say "And shouting out loud, well..."
    mike.say "That's just going to make it more likely someone will!"
    "Aletta regards me with an almost pleading look in her eyes."
    show spank aletta ready pleasure
    "But then she bites her lip and turns her head to look forwards."
    show spank aletta up
    "I take this as permission to continue, aiming another slap at Aletta's ass..."
    show spank aletta spank
    play sound spank
    with hpunch
    "Aletta whimpers as she takes the blow, her whole body quivering."
    "And I can feel the same shakes and thrills running through me too!"
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "Every time she moves or makes a sound, it turns me on just as much."
    "And it's not just the enjoyment I take from getting physical with Aletta."
    "I can honestly feel the constant fear of being discovered too."
    "What if someone walks in on us while I'm spanking Aletta?"
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "The mere thought of it spurs me on to spank harder and faster."
    "By now, Aletta is almost squealing with each contact I make."
    "The noises beginning to sound more like cries of pleasure all the time!"
    "Pretty soon there's no way to tell them apart."
    show spank aletta up
    pause 0.3
    show spank aletta spank marks
    play sound spank
    with hpunch
    "And I'm certain that Aletta can't tell the difference either."
    "Her buttocks have already turned a deep shade of red."
    "The shape of my hand actually becoming visible on her ass!"
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "Finally, Aletta can stand no more and she collapses on my knees."
    "I hurry to help her, worried that I might have gone too far."
    mike.say "Aletta..."
    mike.say "Are you okay?!?"
    scene expression f"bg {game.room}"
    "Aletta gasps, but still manages to nod her head."
    "And a few moments later, she's actually able to speak."
    show aletta pleasure blush
    aletta.say "I...I..."
    aletta.say "I feel...amazing!"
    show fx exclamation
    if not aletta.is_sex_slave:
        aletta.say "It's working, [hero.name]!"
    else:
        aletta.say "It's working, Master!"
    mike.say "I'm glad to hear that, Aletta."
    "Aletta looks away from me as she pulls down her skirt."
    "But I can see that the cheeks on her face are as red as the ones beneath it!"
    aletta.say "I guess we will reschedule next week?"
    $ aletta.flags.weeklyspank = game.days_played
    $ aletta.flags.spankdelay = TemporaryFlag(True, 7)
    $ aletta.sub += 1
    return

label aletta_fuck_surprise_office_spank:
    "The door to my office bursts open and Aletta strides in like a warrior queen."
    "I don't even have to look up from my work to know it's her."
    "I can sense it even before she opens her mouth to speak."
    mike.say "Hey, Aletta..."
    mike.say "What can I do for you?"
    aletta.say "H...how did you know?"
    show aletta annoyed
    aletta.say "How did you know it was me?"
    "I can't help smiling as I look Aletta in the eye."
    "The confidence in my voice takes her by complete surprise."
    "And I can see that it's left her off-balance and unsure."
    mike.say "Well, you are pretty predictable, Aletta!"
    mike.say "That means I can catch you off-guard whenever I want."
    aletta.say "Th...that's not true!"
    show aletta angry
    aletta.say "I'm the one in charge here, [hero.name]!"
    "My smile becomes wider as I hear the hesitation in her voice."
    mike.say "Okay, Aletta - let's test that theory, shall we?"
    "I push my chair back from the desk and pat my thigh."
    mike.say "Come over here and lay across my lap."
    mike.say "Right now, please!"
    show aletta surprised
    "Aletta's eyes go wide with amazement."
    "And she makes a snorting sound like an angry horse."
    "But I note that she takes an unconscious step towards me."
    "I nod and pat my thigh again, beckoning with the other hand."
    "Aletta takes a look over her shoulder, then glances back at me."
    "It's like she's having an internal debate, weighing her options."
    "Then it seems something inside of her snaps."
    "And she scurries around the desk as fast as she can."
    show aletta normal
    aletta.say "Alright, alright, [hero.name]."
    aletta.say "But this isn't you telling me what to do, okay?"
    aletta.say "I'm just curious!"
    "I nod at this, already guiding Aletta down onto my lap."
    "I wait for her to be looking the other way to roll my eyes."
    hide aletta
    show spank aletta
    "And then I pull up her skirt."
    aletta.say "Wh...what are you..."
    "I slap Aletta's bared buttocks before she can finish speaking."
    show spank aletta spank
    play sound spank
    with hpunch
    aletta.say "Oh...oh my!"
    show spank aletta surprised
    aletta.say "Please, [hero.name]...may I have another?"
    "I shake my head and let out an amused chuckle."
    "But I don't hesitate to give Aletta what she wants."
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "Each blow that lands makes her buttocks redder."
    show spank aletta up
    pause 0.3
    show spank aletta spank
    play sound spank
    with hpunch
    "And it makes her cheeks flush red too."
    "Aletta gasps and moans as I spank her for the sheer delight of it."
    show spank aletta ready pleasure
    "She nods, urging me on and I oblige her with as much force as I dare."
    "Soon enough my hand is getting numb and Aletta's panting desperately."
    show spank aletta up
    pause 0.3
    show spank aletta spank marks
    play sound spank
    with hpunch
    "I ease off, letting her know that the spanking is coming to an end."
    "Aletta stands up, pulling down her skirt and trying to regain her dignity."
    scene expression f"bg {game.room}"
    show aletta pleasure blush
    aletta.say "Ahem..."
    aletta.say "I think that covers everything, [hero.name]."
    aletta.say "I have to be going now."
    mike.say "No worries, Aletta - happy to help!"
    show aletta normal
    "With that, Aletta resumes her usual demeanour of casual superiority."
    hide aletta with easeoutleft
    "She nods and strides over to the door, lets herself out and disappears from sight."
    "I lean back in my seat, smiling with satisfaction."
    "Now if only all work meetings went as smoothly as that!"
    $ aletta.flags.spankdelay = TemporaryFlag(True, 7)
    $ aletta.sub += 1
    return

label aletta_fuck_office_titjob:
    show aletta -close
    "Aletta pulls a mock frown and shakes her head."
    "At the same time she begins to unbutton her top."
    aletta.say "We can't have that now, can we?"
    aletta.say "Stress causes a loss of productivity in the workplace!"
    aletta.say "So I think you should take off your clothes and let me handle it."
    show aletta topless with dissolve
    "As if to punctuate her suggestion, Aletta undoes the last button a moment later."
    "This means that her breasts spill out of her top, bouncing as they're freed."
    "They swing and sway as they submit to gravity, almost hypnotising me."
    "I nod eagerly, already tugging and pulling at my clothes."
    "And by the time I make it over to the couch, I'm almost completely naked."
    "Aletta follows me at a more leisurely pace, chuckling at my enthusiasm."
    "Just as I get the last of my clothes off, she shoves me backwards."
    hide aletta
    show aletta titjob office with fade
    "I land with a thump on the sofa, staring up at her."
    "Which means I get a magnificent view of her chest from below."
    "They're so big that I can't even see Aletta's face at first!"
    "I only make eye-contact with her again when she's almost on her knees."
    "By now my cock is hard as a rock and standing to attention."
    "It bobs right in front of Aletta's face, making it hard to see her expression."
    "But then she leans to one side and catches my eye."
    show aletta titjob droll
    "And with a smile, she flicks the head of my cock."
    "This makes it sway from side to side, but also hurts a little."
    "So I can't help yelping in pain."
    mike.say "Ow!"
    aletta.say "Ah..."
    aletta.say "So much stiffness and tension!"
    show aletta titjob normal
    if not aletta.is_sex_slave:
        aletta.say "You need a massage, [hero.name]..."
    else:
        aletta.say "You need a massage, Master..."
    "Aletta takes hold of the shaft with one hand, stroking gently up and down."
    "Then she leans forward, guiding the head between her heavy breasts."
    "All I can do is nod and keep on yelping."
    "But this time it's from anticipation, rather than pain."
    "I feel the weight of Aletta's breasts as my cock pushes between them."
    "She takes it slowly, letting me savour the sensation for as long as possible."
    "Slowly the head inches higher and more of the shaft disappears into her cleavage."
    "And only when it's almost completely swallowed does she begin to move."
    "Aletta rocks gently back and forth."
    "And at the same time she presses her breasts together."
    "The effect is immediate and almost breath-taking."
    "I feel like my cock is being massaged by soft, warm pillows."
    "But the view I have right now makes the feeling that much more intense."
    show aletta titjob droll
    "I can see Aletta's breasts as they heave and squeeze together."
    "And the look of mounting desire on her face is plain to see."
    "Aletta's lips are parted, and she's already panting heavily."
    "Her eyes dart between my expression and her own chest."
    "All of which makes me wonder if this was about relieving my tension at all."
    "Because Aletta is starting to look like she's going to blow her own top!"
    "A moment later, the head of my cock pops up from between her breasts."
    "And Aletta greets this with a cry that sounds like she just came!"
    "Her eyes focus on the tip with a renewed intensity."
    if aletta.flags.submissive_interact:
        aletta.say "[hero.name] don't miss the bullseye of your personal shooting target!"
    "And she begins working away at me like never before."
    "It's not just Aletta that's feeling it either."
    "I can feel my heart pounding in my chest right now."
    "My breath is coming in ragged gasps."
    "And I know I can't hold on much longer."
    "The only question is what's going to happen when I lose it?"
    menu:
        "Cum on her tits":
            show chest_insert aletta zorder 1 at zoomAt(1, (20, 220))
            "I've been staring at Aletta's breasts this whole time."
            "Hell, I've been all but hypnotised by those things!"
            "So where else am I going to want it to go?"
            "I pull myself downwards, just at the right moment."
            show chest_insert aletta cum
            show aletta titjob surprised cumshot
            with vpunch
            "Which means that when I cum, it spurts all over Aletta's chest."
            with vpunch
            "She lets out breathless gasps as I paint white stripes across her breasts."
            show aletta titjob -cumshot dickcum normal with vpunch
            $ aletta.love += 4
            "And then moans as she massages in into her skin."
        "Cum on her face":
            "Aletta keeps right on staring at the head of my cock."
            "Which means that she's looking down the barrel of a gun!"
            show aletta titjob cumshot surprised with vpunch
            "As soon as I shoot my load, she takes it straight in the face."
            with vpunch
            "Aletta cries out in surprise as it hits her."
            show aletta titjob -cumshot normal cum face with vpunch
            $ aletta.sub += 2
            "Warm stripes of sticky, white cum paint her cheeks."
            "Some spatters her lips, landing in her open mouth."
            "And then it begins to run downwards, dripping off her chin."
        "Cum in her mouth":
            "At the last moment, Aletta leans down even further."
            show mouth_insert aletta zorder 1 at zoomAt(1, (860, 140))
            "She takes the head of my cock in her open mouth."
            show mouth_insert aletta cum
            show aletta titjob cumshot
            with vpunch
            "And a second later, I shoot my load."
            with vpunch
            "Aletta desperately laps at the cum as it spurts out."
            with vpunch
            "She seems desperate to claim every last drop."
            show aletta titjob -cumshot cum mouth
            $ aletta.love += 2
            $ aletta.sub += 1
            "Almost like she's dying of her thirst for it."
            "I lie back and watch her swallow all that she can."
            show aletta titjob -cumshot -cum -mouth
            show mouth_insert aletta -cum
            "Even licking the last off her lips before she's done!"
    hide chest_insert
    hide mouth_insert
    hide aletta
    show aletta work topless with fade
    "While I'm still lying back on the sofa, Aletta stands up."
    "She cleans herself off quickly and efficiently, then straightens her clothes."
    show aletta work -topless with dissolve
    "Within less than a minute, she looks perfectly presentable."
    "Just as poised and professional as she did the moment she walked into my office."
    aletta.say "Mmm..."
    if not aletta.is_sex_slave:
        aletta.say "That was most helpful, [hero.name]."
    else:
        aletta.say "That was most helpful, Master."
    aletta.say "An effective use of both our time."
    mike.say "Ah..."
    mike.say "Yeah, Aletta - I guess so!"
    show aletta happy
    "With that, Aletta gives me a knowing smile and turns on her heel."
    hide aletta with easeoutleft
    "I watch her go, still reeling from what she just did to me."
    "And wondering how the hell I'm supposed to get my head back into my work!"
    return

label aletta_fuck_office_ropeplay:
    show aletta normal
    aletta.say "You're going to do it again... Don't you?"
    "I nod silently."
    if not aletta.is_sex_slave:
        aletta.say "Okay, [hero.name]."
    else:
        aletta.say "Okay, Master."
    scene aletta ropeplay
    "So much so that she doesn't ask the most obvious question."
    "Which is just what I plan to do with her once she's tied up."
    "So I guess that's going to be another surprise for her!"
    show aletta ropeplay b
    "Aletta obligingly lets me get to work."
    "And to my credit, I remember the knots and where they all go quite well."
    "All of which means that things go smoothly and I soon have Aletta all tied up."
    "Well...maybe not completely smoothly."
    show aletta ropeplay ropes
    "There are a couple of times that Aletta ends up wailing in pain."
    "And more than once a knot ends up in a compromising spot and I have to try again."
    "But those are just minor setbacks, and soon I have Aletta well and truly lashed to her chair."
    show aletta ropeplay gag
    "She even has a neat little gag securing her mouth too!"
    "Aletta stares at me helplessly from her seat."
    "And I stand back to admire my handiwork."
    "I can see from the look in her eyes that Aletta's getting a thrill out of this already."
    "Her cheeks are flushing with embarrassment and she's wriggling weakly against her bonds."
    "And the last touch is a blindfold over her eyes."
    show aletta ropeplay blindfold
    mike.say "There you are. Are you alright Aletta?"
    aletta.say "Mmm..."
    "All the knot play was exhausted. A coffee would be nice."
    mike.say "Aletta, I'll grab a coffee. Do you want one?"
    aletta.say "Mmm..."
    mike.say "Okay then. I'll be back ."
    if "aletta_stress_2" in DONE:
        "Just before leaving the room, I remembered I can relieve Aletta from her stress more efficiently."
        mike.say "I just forgot I can help you more with your stress."
        mike.say "Just open your legs a bit."
        show aletta ropeplay b ropes blindfold gag
        "In my bag, I quickly find what I'm looking for."
        show aletta ropeplay b ropes blindfold gag nopanties
        "Putting her panties aside, I jump to my next move."
        mike.say "There."
        show aletta ropeplay b ropes blindfold gag nopanties first
        aletta.say "Mmm..."
        mike.say "This one here."
        show aletta ropeplay b ropes blindfold gag nopanties first second
        aletta.say "Mmm..."
        mike.say "I guess this one can fit there."
        show aletta ropeplay b ropes blindfold gag nopanties first second third
        aletta.say "Mmm..."
        aletta.say "Mmm..."
        mike.say "Please, don't move until I'm done with this last one."
        show aletta ropeplay b ropes blindfold gag nopanties first second third fourth
        aletta.say "Mmm...mmm...MMM!"
        aletta.say "Mmm...mmm...MMM!"
        aletta.say "Mmm...mmm...MMM!"
    scene bg breakroom with fade
    "The girls are already in the break room gossiping."
    "Sipping my coffee, I take part in their conversation."
    "I enjoy the chitchat for a while, almost forgetting about Aletta."
    scene expression f"bg {game.room}" with fade
    "Seeing Aletta as I come back in my office, I feel almost sorry for her."
    scene aletta ropeplay
    if "aletta_stress_2" in DONE:
        show aletta ropeplay b ropes blindfold gag nopanties first second third fourth ahegao drool squirt
    else:
        show aletta ropeplay b ropes blindfold gag ahegao drool
    with fade
    "I pull the blindfold off of her eyes, but leave the gag intact."
    mike.say "I almost forgot about you."
    show aletta ropeplay -blindfold
    mike.say "But it looks like you behaved well while I was gone."
    "It's just as I finish speaking that I realise what the look in Aletta's eyes means."
    "She's regarding me with a mixture of frustration and sheer amazement right now."
    "And that's obviously because I've left her trussed up like a festive turkey!"
    "Taking a deep breath, I steel myself and begin to untie Aletta."
    "I have no idea what she'll do to me once she's free."
    "But I guess that I probably deserve whatever it is..."
    $ aletta.love += 2
    $ aletta.sub += 2
    return

label aletta_fuck_office_cowgirl(sexperience_min):
    "Aletta seems to know exactly what she wants and how to get it."
    "Because she wastes no time in pushing me down on the sofa."
    scene aletta cowgirl
    show aletta cowgirl office
    with fade
    "That done, she clambers atop me, pinning me beneath her."
    "Then she looks down at me, licking her lips in anticipation."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and aletta.sub >= 50:
            "And it's in this moment that I make my move."
            "Aletta seems to be contemplating what comes next."
            "But I'm already setting my plans in motion!"
            "Taking a firm hold of her waist, I lift her upwards."
            "Then I aim my cock at just the right point."
            "Which means that when she comes down, it slips between her buttocks."
            show aletta cowgirl anal
            aletta.say "Oh...oooh..."
            if not aletta.is_sex_slave:
                aletta.say "[hero.name]...you fiend!"
            else:
                aletta.say "Master...you fiend!"
            aletta.say "That's...that's my ass!"
            "For all of her protests, Aletta's too late."
            "Because I can already feel myself sinking into her."
            "She wriggles this way and that, yelping in alarm."
            show aletta cowgirl anal down
            "But all that does is work my cock further up her ass."
            "Aletta's muscles squeeze my shaft in protest, and it feels amazing."
            "So I can hardly help thrusting harder in response."
            aletta.say "Mmm..."
            aletta.say "Oh my..."
            aletta.say "You wicked, wicked man!"
            show aletta cowgirl anal pleasure down
            "Aletta lets out a deep moan as I sink all the way in."
            "She strokes herself with her hands at the same time."
            "Squeezing her breasts and pinching her nipples."
            "All as if she's unable to control herself."
            "Finally her cheeks flush a deep shade of red."
            aletta.say "P...please..."
            aletta.say "It feels so good..."
            aletta.say "I want more!"
            "Well, how can I possibly say no to a request like that?"
            show aletta cowgirl raised
            pause 0.35
            show aletta cowgirl down
            "Keeping my hands firmly on Aletta's waist, I start to move."
            show aletta cowgirl raised
            pause 0.35
            show aletta cowgirl down
            "Slowly at first, building speed carefully as I read her reactions."
            "And it doesn't take long to see that it's having an effect."
            show aletta cowgirl raised
            pause 0.35
            show aletta cowgirl down
            pause 0.35
            show aletta cowgirl raised
            pause 0.35
            show aletta cowgirl down
            "Aletta bites her lip as my cock moves in and out of her."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            "Then she whimpers and nods as the speed begins to increase."
            "The sensation of being inside her is incredible."
            show aletta cowgirl raised cum
            pause 0.25
            show aletta cowgirl down bounce at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "And it'd be more than enough to make me lose it."
            "But what really pushes me over the edge is the sight of Aletta above me."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down bounce at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "One of her hands is buried in her thick, dark hair."
            "While she has the other clasped over one of her breasts."
            "She's squeezing and pinching at the fleshy orb again."
            show aletta cowgirl raised bounce ahegao
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "Like the act will release some of the tension in her."
            "But all it seems to do is cause her desires to build."
            show aletta cowgirl raised bounce
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "I swear that from the look on her face, she's about to burst!"
            "But in the end, that's actually the effect she has on me..."
            if aletta.flags.submissive_interact:
                aletta.say "Shoot me... Shoot me as a target practice!"
            show aletta cowgirl down
            call cum_reaction (aletta, 'anal', sexperience_min) from _call_cum_reaction_5
            if _return == 'anal_inside':
                "I feel like Aletta's squeezing me too, draining me dry."
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl raised anal creampie cum with vpunch
                "So when I lose it, I feel like I've suddenly been released."
                with vpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                with vpunch
                "So she takes all I have to give, with nothing held back."
                with vpunch
                "Aletta groans as she cums too, grinding herself down onto me."
                "And then she flops backwards, barely able to hold herself up."
                $ aletta.love += 2
                $ aletta.sub += 2
            elif _return == 'anal_outside':
                "I use the last of my strength to lift Aletta up just a little."
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down anal cum with vpunch
                "Enough to drag my cock out of her ass before I lose it."
                "There's an almost comical popping sound as it comes out of her ass."
                "And Aletta moans at the sensation, beginning to cum too."
                show aletta cowgirl raised cumshot -anal with vpunch
                "The moment she sits back down atop me."
                with vpunch
                "Strings of warm cum paint Aletta's slick skin."
                show aletta cowgirl -cumshot dickcum with vpunch
                "And then she flops backwards, barely able to hold herself up."
            $ aletta.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (aletta, 180) from _call_check_condom_usage_3
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show aletta cowgirl condom
            "Aletta all but pounces on me, grabbing hold of my cock as she does so."
            "I can't help gasping in shock, my eyes going wide at the sensation."
            "Which in turn makes Aletta's grin become wolfish in nature."
            "She looks me in the eye as she rubs the head of my cock against her pussy."
            aletta.say "Mmm..."
            aletta.say "I'm feeling so hungry all of a sudden."
            aletta.say "I need something to fill up my pussy!"
            "Without warning, Aletta pushes my cock hard against her lips."
            "They're already slick and slippery in anticipation of what's to come."
            "And so there's only a moment of resistance before I slide into her."
            show aletta cowgirl vaginal
            mike.say "Oh fuck..."
            mike.say "Aletta..."
            mike.say "You can...you can eat me alive!"
            "Aletta lets out a wicked laugh at this."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            "And she begins to ride me, hard and without mercy."
            "All I can do is cling onto her waist with both hands."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            "She looks down on me the whole time, a wide smile on her face."
            "But the view is obscured by the heavy, fleshy orbs of breasts."
            show aletta cowgirl raised cum
            pause 0.25
            show aletta cowgirl down bounce at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "They bounce up and down in sympathy as she moves, parting and then slapping together."
            "And it's from between them that I catch glimpses of her face, her cheeks red and flushed."
            aletta.say "Your cock feels so good inside of me."
            aletta.say "Like I want to keep it there forever!"
            aletta.say "You'd like that, wouldn't you?"
            show aletta cowgirl raised pleasure
            pause 0.25
            show aletta cowgirl down bounce at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            aletta.say "You'd like to fuck me forever, right?"
            mike.say "Uh...uh..."
            mike.say "God...yeah..."
            mike.say "I'd love that, Aletta!"
            aletta.say "That's right you would!"
            aletta.say "Now be a good boy."
            show aletta cowgirl raised bounce
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            aletta.say "And...make...me...cum!"
            "I almost jump to obey Aletta's command, my whole body responding."
            show aletta cowgirl raised bounce
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "Before I know it, I'm picking up speed rapidly, thrusting in and out."
            "Every muscle in my body strains to give Aletta what she demands of me."
            show aletta cowgirl raised bounce
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "And the effects are plain to see as this happens."
            "Above me, Aletta bites her lip as my cock moves inside of her."
            "She whimpers and nods, urging me on to go faster still."
            "For me the sensation is like nothing I can describe."
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.25
            show aletta cowgirl raised
            pause 0.25
            show aletta cowgirl down at startle(0.05, -10)
            "And I know that I can't keep going at this pace much longer."
            "But what really pushes me over the edge is the sight of Aletta above me."
            "One of her hands is buried in her thick, dark hair."
            "While she has the other clasped over one of her breasts."
            "She's squeezing and pinching at the fleshy orb."
            "Maybe she hopes that it'll give her some measure of release."
            show aletta cowgirl raised bounce ahegao
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "But from the look on her face, it's having the opposite effect."
            "Aletta looks like she's about to burst!"
            if aletta.flags.submissive_interact:
                aletta.say "A target practice... Use me as a target practice."
                aletta.say "And don't miss!"
            show aletta cowgirl raised bounce
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.15
            show aletta cowgirl raised
            pause 0.15
            show aletta cowgirl down at startle(0.05, -10)
            pause 0.1
            show aletta cowgirl -bounce
            "But in the end, that's actually the effect she has on me..."
            call cum_reaction (aletta, 'vaginal', sexperience_min) from _call_cum_reaction_6
            if _return == "vaginal_outside":
                "I use the last of my strength to lift Aletta up just a little."
                "Enough to drag my cock out of her pussy before I lose it."
                show aletta cowgirl cumshot -vaginal cum with vpunch
                "There's an almost comical sound as it slides out from between her lips."
                with vpunch
                "And Aletta moans at the sensation, beginning to cum too."
                with vpunch
                "The moment she sits back down atop me, I spray her breasts and belly."
                with vpunch
                "Strings of warm cum paint Aletta's slick skin."
                show aletta cowgirl dickcum
                "And then she flops backwards, barely able to hold herself up."
                $ aletta.love += 1
                $ aletta.sub += 2
            elif _return == "vaginal_condom":
                "I feel like Aletta's squeezing me too, draining me dry."
                "So when I lose it, I feel like I've suddenly been released."
                "But thanks to use using protection, there's no danger of an accident."
                show aletta cowgirl down cum with vpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                with vpunch
                "So she takes all I have to give, with nothing held back."
                with vpunch
                "Aletta groans as she cums too, grinding herself down onto me."
                show aletta cowgirl -vaginal cumshot with vpunch
                "And then she flops backwards, barely able to hold herself up."
                $ aletta.love += 1
            elif _return == "vaginal_inside_pill":
                aletta.say "Cum in me...please?"
                aletta.say "I'm on the pill - remember?"
                "I feel like Aletta's squeezing me too, draining me dry."
                "So when I lose it, I feel like I've suddenly been released."
                show aletta cowgirl raised creampie cum with vpunch
                "But there's no danger of an accident, as she just reminded me."
                with vpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                with vpunch
                "So she takes all I have to give, with nothing held back."
                with vpunch
                "Aletta groans as she cums too, grinding herself down onto me."
                show aletta cowgirl -vaginal dickcum
                "And then she flops backwards, barely able to hold herself up."
                $ aletta.love += 2
            elif _return == "vaginal_inside_pregnant":
                aletta.say "Cum in me...please?"
                aletta.say "I...I'm already pregnant!"
                "I feel like Aletta's squeezing me too, draining me dry."
                "So when I lose it, I feel like I've suddenly been released."
                "But there's no danger of an accident, as she just reminded me."
                "My cock is as deep inside of Aletta as it can possibly go."
                show aletta cowgirl raised creampie cum with vpunch
                "So she takes all I have to give, with nothing held back."
                with vpunch
                "Aletta groans as she cums too, grinding herself down onto me."
                show aletta cowgirl -vaginal dickcum with vpunch
                "And then she flops backwards, barely able to hold herself up."
                $ aletta.love += 3
            elif _return == "vaginal_inside_mad":
                aletta.say "You have to pull out!"
                aletta.say "You can't cum inside me!"
                "I feel like Aletta's squeezing me too, draining me dry."
                "And I'm too busy trying to make her cum to hear the warning."
                "My cock is as deep inside of Aletta as it can possibly go."
                "So she takes all I have to give, with nothing held back."
                show aletta cowgirl raised creampie cum with vpunch
                #$ aletta.impregnate()
                "Aletta groans as she cums too, trying in vain to pull herself away."
                show aletta cowgirl -vaginal dickcum with vpunch
                "And then she flops backwards, shock and horror written all over her face."
                "Which is the exact same look on my own face too!"
                $ aletta.love -= 20
                $ aletta.sub -= 10
            elif _return == "vaginal_inside_happy":
                aletta.say "Cum in me!"
                aletta.say "Do it...please?"
                "I feel like Aletta's squeezing me too, draining me dry."
                "And her sudden, bizarre demand catches me totally unprepared."
                "My cock is as deep inside of Aletta as it can possibly go."
                "So she takes all I have to give, with nothing held back."
                show aletta cowgirl raised creampie cum with vpunch
                #$ aletta.impregnate()
                "Aletta groans as she cums too, grinding herself down onto me."
                with vpunch
                "And then she flops backwards, laughing happily."
                show aletta cowgirl -vaginal dickcum with vpunch
                "But I still can't believe what she just made me do!"
                $ aletta.love += 6
    $ aletta.sexperience += 1
    return

label aletta_fuck_office_doggy(sexperience_min):
    "Aletta seems more than happy to let me take the lead."
    "And so I waste no time in guiding her onto her hands and knees."
    hide aletta
    show aletta doggy office with fade
    "Aletta looks back over her shoulder, eyes wide with anticipation."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Now that I'm the one calling the shots, I decide to take full advantage."
            show aletta doggy mike hand
            "So I waste no time in grabbing hold of Aletta's buttocks and parting them."
            "And then I begin to push the head of my cock hard against her ass."
            "Aletta's eyes go wider still as she realises what I have in mind."
            show aletta doggy mike hand anal
            "I wait for a moment, wondering if she's going to object."
            "But then she lowers her head in a gesture of submission."
            "And that's all the permission I need."
            "Aletta moans as I thrust myself forwards and my cock enters her ass."
            "It's as tight as it can be, her muscles trying their best to resist."
            "But that just makes the sensation all the more enjoyable for me."
            "Soon enough I'm sinking ever deeper into her."
            "And I can feel her body quivering as it surrenders to me."
            aletta.say "Ahh..."
            aletta.say "Oh my god..."
            aletta.say "You're wicked...so wicked..."
            "I can see the way that Aletta's cheeks are flushing with colour."
            show aletta doggy mike hand anal pleasure
            "The humiliation is almost too much for her to bear."
            "And yet she's clearly enjoying the sensation as well."
            "She holds her head down low, nodding the whole time."
            aletta.say "It feels...so good..."
            aletta.say "Please don't stop..."
            aletta.say "I love it when you fuck my ass!"
            aletta.say "I want more!"
            "It's not like Aletta has to beg for what she wants."
            "But hearing the desperation in her voice is a massive turn-on."
            "And so I can't help stepping up the pace as soon as she speaks those words."
            "Soon enough I can hear the sound of my thighs slapping against her buttocks."
            "The noise is loud, but not loud enough to drown out the sounds that Aletta's making."
            "She cries out with each thrust that I make into her."
            "And I'm beginning to wonder how much more of this she can take!"
            "At the same time, Aletta's breasts are swaying beneath her."
            "Moving in sympathy with her body, they're almost hypnotic."
            aletta.say "Oh...Oh..."
            aletta.say "I'm going to..."
            aletta.say "I'm going to cum!"
            if aletta.flags.submissive_interact:
                aletta.say "Use me..."
                aletta.say "Use me as your target practice!"
            show aletta doggy mike hand anal ahegao
            "I can already feel the evidence of Aletta's warning."
            "Her muscles are starting to go into a twinging spasm around my cock."
            "And the effect is like being squeezed by a giant fist."
            "It's more than enough to take me along with her too!"
            call cum_reaction (aletta, 'anal', sexperience_min) from _call_cum_reaction_7
            if _return == 'anal_inside':
                "I feel like Aletta's squeezing me too, draining me dry."
                "So when I lose it, I feel like I've suddenly been released."
                "My cock is as deep inside of Aletta as it can possibly go."
                show aletta doggy mike hand anal creampie with hpunch
                "So she takes all I have to give, with nothing held back."
                with hpunch
                "Aletta groans as she cums too, pushing her ass against me."
                with hpunch
                "And then she flops forwards, barely able to hold herself up."
                $ aletta.love += 2
                $ aletta.sub += 2
            elif _return == 'anal_outside':
                "I use the last of my strength to push Aletta forwards just a little."
                "Enough to drag my cock out of her ass before I lose it."
                "There's an almost comical popping sound as it comes out of her ass."
                show aletta doggy mike -hand out cumshot with hpunch
                "And Aletta moans at the sensation, beginning to cum too."
                with hpunch
                "A moment later, I spray her buttocks and thighs."
                show aletta doggy mike -hand out -cumshot cumbody with hpunch
                "Strings of warm cum paint Aletta's slick skin."
                "And then she flops forwards, barely able to hold herself up."
                $ aletta.sub += 4
            $ aletta.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (aletta, 180) from _call_check_condom_usage_4
            if _return == False:
                return "leave_without_gain"
            "Aletta practically purrs with pleasure as I stroke my cock against her pussy."
            if CONDOM:
                show aletta doggy mike hand condom
            else:
                show aletta doggy mike hand
            "And I can feel my own heart beginning to beat faster in my chest too."
            "Because her lips are already nice and slick, like they're inviting me inside."
            aletta.say "Oh..."
            aletta.say "Don't tease me, please!"
            aletta.say "I want your cock in me so badly!"
            "I can't help chuckling at the way Aletta sounds so desperate."
            "Normally I'd take great pleasure in teasing her a little longer."
            "But right now I'm feeling almost as desperate as she is!"
            "And so I waste no more time in getting down to business."
            "All it takes is a quick thrust below the waist."
            show aletta doggy vaginal mike hand
            "There's a moment of token resistance, and then I'm in."
            "And when I say that, I mean I literally slide right in there."
            "Aletta opens up for me like a flower opening its petals to the sun."
            "She feels soft, smooth and yielding as I sink in the whole way."
            "And the noise she makes as I fill her..."
            "Well, it's all of those good things summed up sound!"
            aletta.say "Mmm..."
            aletta.say "Your cock feels SO good inside of me..."
            aletta.say "I...want it in me forever!"
            show aletta doggy vaginal mike hand pleasure
            aletta.say "Would you like that too?"
            aletta.say "Would you like to fuck me forever?"
            mike.say "Oh shit..."
            mike.say "God, Aletta..."
            mike.say "I'd love that!"
            "In fact, I think it's the only thing I'd love more than what I'm doing right now!"
            "Without a single conscious thought, I'm fucking Aletta harder and faster than ever."
            "It's like my entire body's on autopilot and I'm just along to enjoy the ride."
            "And of course, riding Aletta this hard is something else!"
            "I can hear the sound of my thighs slapping against her buttocks."
            "But only just, thanks to the louder noises that she's making herself."
            "Aletta pants and moans as she takes everything I have to give."
            "Her skin is slick with sweat and her cheeks are flushed red."
            "Each thrust makes her cries increase in volume."
            show aletta doggy vaginal mike hand ahegao
            "Aletta's heavy breasts are swaying beneath her."
            "Moving in a hypnotic fashion as they swing to and fro."
            aletta.say "Oh...Oh..."
            aletta.say "I'm going to..."
            aletta.say "I'm going to cum!"
            if aletta.flags.submissive_interact:
                aletta.say "Use me..."
                aletta.say "Use me as your target practice!"
            "The warning takes me by surprise, but I know she's telling the truth."
            "Aletta's pussy is twitching, it's muscles squeezing my cock."
            "It's like she's wringing the last of my strength out of me."
            "And she's going to make me cum too!"
            call cum_reaction (aletta, 'vaginal', sexperience_min) from _call_cum_reaction_8
            if _return == "vaginal_outside":
                "I use the last of my strength to push Aletta forwards just a little."
                "Enough to drag my cock out of her pussy before I lose it."
                "There's an almost comical popping sound as it comes out of her."
                show aletta doggy mike -hand out cumshot with hpunch
                "And Aletta moans at the sensation, beginning to cum too."
                with hpunch
                "A moment later, I spray her buttocks and thighs."
                show aletta doggy mike out -cumshot cumbody with hpunch
                "Strings of warm cum paint Aletta's slick skin."
                "And then she flops forwards, barely able to hold herself up."
                $ aletta.love += 1
                $ aletta.sub += 2
            elif _return == "vaginal_condom":
                "I feel like Aletta's squeezing me too, draining me dry."
                with hpunch
                "So when I lose it, I feel like I've suddenly been released."
                with hpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                with hpunch
                "So she takes all I have to give, with nothing held back."
                show aletta doggy mike hand condom squirt ahegao
                "But thanks to the fact we took precautions, none of that matters."
                "Aletta groans as she cums too, pushing her ass against me."
                "And then she flops forwards, barely able to hold herself up."
                $ aletta.love += 1
            elif _return == "vaginal_inside_pill":
                aletta.say "Cum in me...please?"
                aletta.say "I'm on the pill - remember?"
                "I feel like Aletta's squeezing me too, draining me dry."
                with hpunch
                "So when I lose it, I feel like I've suddenly been released."
                with hpunch
                "But there's no danger of an accident, as she just reminded me."
                with hpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                show aletta doggy creampie vaginal mike hand squirt
                "So she takes all I have to give, with nothing held back."
                "Aletta groans as she cums too, pushing her ass against me."
                "And then she flops forwards, barely able to hold herself up."
                $ aletta.love += 2
            elif _return == "vaginal_inside_pregnant":
                aletta.say "Cum in me...please?"
                aletta.say "I...I'm already pregnant!"
                "I feel like Aletta's squeezing me too, draining me dry."
                with hpunch
                "So when I lose it, I feel like I've suddenly been released."
                with hpunch
                "But there's no danger of an accident, as she just reminded me."
                show aletta doggy creampie vaginal mike hand squirt with hpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                "So she takes all I have to give, with nothing held back."
                "Aletta groans as she cums too, pushing herself against me."
                "And then she flops forwards, barely able to hold herself up."
                $ aletta.love += 3
            elif _return == "vaginal_inside_mad":
                aletta.say "You have to pull out!"
                aletta.say "You can't cum inside me!"
                "I feel like Aletta's squeezing me too, draining me dry."
                with hpunch
                "And I'm too busy trying to make her cum to hear the warning."
                with hpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                show aletta doggy creampie vaginal mike hand squirt with hpunch
                #$ aletta.impregnate()
                "So she takes all I have to give, with nothing held back."
                "Aletta groans as she cums too, trying in vain to pull herself away."
                "And then she flops forwards, shock and horror written all over her face."
                "Which is the exact same look on my own face too!"
                $ aletta.love -= 20
                $ aletta.sub -= 10
            elif _return == "vaginal_inside_happy":
                aletta.say "Cum in me!"
                aletta.say "Do it...please?"
                "I feel like Aletta's squeezing me too, draining me dry."
                "And her sudden, bizarre demand catches me totally unprepared."
                with hpunch
                "My cock is as deep inside of Aletta as it can possibly go."
                show aletta doggy creampie vaginal mike hand squirt with hpunch
                #$ aletta.impregnate()
                "So she takes all I have to give, with nothing held back."
                with hpunch
                "Aletta groans as she cums too, pushing herself against me."
                "And then she flops forwards, laughing happily."
                "But I still can't believe what she just made me do!"
                $ aletta.love += 6
    $ aletta.sexperience += 1
    return

label aletta_fuck_office_cunnilingus:
    "I swear that I can smell the scent of Aletta's pussy right now."
    "It's calling to me from between her thighs, and I have to answer!"
    "Without pausing to ask permission, I guide her down onto the sofa."
    "Aletta makes no effort to resist, chuckling to herself as she lies down."
    "But she does let out a gasp of surprise as I part her legs."
    scene aletta cunnilingus
    show aletta cunnilingus ceo
    with fade
    "And then lower my head between them, heading straight for her pussy."
    "I start by gently tracing the outline of her lips."
    "Just using the tip of my tongue, I start to tease her."
    "For all of her haughty demeanour, Aletta's body betrays her."
    "I can tell that she's already wet down here, slick with desire."
    "My tongue tingles as I lick between her folds."
    "And my ears are filled with the sound of Aletta beginning to moan."
    "This spurs me on, and I push my tongue deeper."
    "It slides between Aletta's lips, reaching inside of her."
    "But I want to go deeper still, as far as I can go."
    "I have my eyes closed, limiting the range of my senses."
    "And those that remain to me are overwhelmed too."
    "All I can feel, taste and hear is Aletta."
    "The only sensations I can make out the movements of her body."
    show aletta cunnilingus pleasure
    "But I can clearly hear the noises she's making."
    "As well as the words she manages to utter."
    aletta.say "Oh..."
    aletta.say "Oh god..."
    show aletta cunnilingus ahegao
    aletta.say "I'm cumming..."
    $ aletta.love += 2
    return

label aletta_restaurant_blowjob:
    hide aletta
    show restaurant meal aletta nomeals with fade
    "Aletta and I are just sitting down at our table, being handed the menus by the waiter."
    "But there's just something not right about the feeling I get once I'm in my seat."
    "I keep on shuffling this way and that, unable to get comfortable."
    aletta.say "I've been waiting to eat here for ages, [hero.name]."
    show restaurant meal aletta alettahappy
    aletta.say "Everyone is talking about the place, you know?"
    aletta.say "Saying that it's just the best!"
    show restaurant meal aletta bored
    mike.say "Erm..."
    mike.say "Yeah, Aletta..."
    mike.say "Whatever you say..."
    mike.say "Go ahead and order me one of those too!"
    show restaurant meal aletta -alettahappy
    "Aletta falls silent for the first time."
    "And that's enough to make me look her in the eye."
    "Oh boy - let's just say she doesn't look impressed!"
    show restaurant meal aletta alettabored
    aletta.say "Are you even listening to me, [hero.name]?"
    show restaurant meal aletta -bored
    mike.say "Sorry, Aletta!"
    mike.say "I don't know what's up with me."
    mike.say "I just can't seem to relax."
    "Aletta raises an eyebrow and lets out a snort of irritation."
    show restaurant meal aletta -alettabored
    "But then I see the expression on her face change."
    aletta.say "Well then..."
    aletta.say "We're just going to have to sort you out then."
    show restaurant meal aletta alettahappy
    aletta.say "Aren't we..."
    "Before I can answer the question, Aletta leaps into action."
    hide restaurant meal aletta
    show aletta flirt at center, zoomAt(1.5, (640, 1140))
    with fade
    "She pushes her chair back a little, making me think she's going to stand up."
    "But then she surprises me by sliding out of her seat and straight under the table!"
    hide aletta with easeoutbottom
    "I'm left speechless, wondering what in the hell she can be doing."
    "Glancing around the restaurant, I note that nobody seems to have noticed."
    "And unless anyone actually looks under the table, they'll be none the wiser."
    "So I can just tell them that Aletta went to the bathroom, I guess."
    mike.say "Aletta..."
    "I hiss as I try to get her attention without letting on what's happening."
    mike.say "Aletta..."
    mike.say "Aletta, what are you doing down there?"
    "There's no answer to my question, at least in the form of words."
    "But a moment later I feel the sensation of hands between my thighs."
    "And looking down, I see Aletta reaching out and unzipping my flies!"
    "I open my mouth to say something, but she looks up at me before I can speak."
    "And the smile on her face is more than enough to make me hold my tongue."
    "Aletta's eyes are also full of mischief and amusement."
    "It's almost like she's daring me to stop her."
    "Knowing that people could discover what's going on any second!"
    "I swallow audibly and lean back in my seat."
    "This means that I can see what's going on with greater ease."
    "Aletta seems to take this as permission to get down to business."
    "As a moment later she pulls my cock out of my pants."
    "Then she turns her eyes downwards and her attentions to my exposed member."
    "I don't have to tell you that I'm getting harder by the second."
    "The sensation of Aletta touching it, with her fingers and her lips."
    "And the danger of her doing it in the middle of a place like this."
    "Both are turning me on to an almost alarming degree right now."
    "Aletta takes full advantage of this, opening her mouth wide."
    show aletta blowjob restaurant with fade
    "Under other circumstances, she might have teased and played around with me."
    "But there's a real sense of urgency here, the need to get things going."
    "And so I feel her lips close around the head of my cock."
    show mouth_insert aletta zorder 1 at zoomAt(1, (880, 200))
    "Then she proceeds to swallow it as deep as she possibly can."
    "From there, Aletta's head begins to bob up and down."
    "At the same time I can feel her using her tongue, lips and even her teeth."
    "Holy fuck - she's even squeezing my balls too!"
    show aletta blowjob restaurant pleasure
    "I do the best I can to tear my eyes away from her."
    "I force myself to look up and stare at the menu."
    "Every second that passes sees me feeling ever more pleasure."
    "I have to bite my lip to keep from making a sound."
    "And I'm sure anyone looking in my direction must be suspicious."
    "Because nobody looks this excited just from reading a damn menu!"
    "More than once I see the waiter gazing in my direction."
    "And I have to look the other way before he makes eye-contact."
    "The last thing I want is for him to come over here and ask me to order."
    "Because whatever comes out of my mouth isn't going to be comprehensible words."
    "Risking another glance downwards, I see Aletta still working hard."
    "She's swallowed me so deep by now that I'm amazed she can breath at all!"
    "And from the way I'm feeling, that's going to get even harder."
    "Because I'm about to cum!"












    "There's no time for me to warn Aletta before it happens."
    "But luckily for me, she seems to be well prepared."
    show mouth_insert aletta cum
    with vpunch
    "I shoot my load with my cock deep in Aletta's throat."
    show aletta blowjob restaurant ahegao cum with vpunch
    "And she swallows every drop without faltering once."
    with vpunch
    "In fact, she gulps it down like she's dying of thirst."
    show mouth_insert aletta -cum
    "Still sucking on my cock afterwards, as if thirsty for more!"
    "Once I'm done, I hastily toss a napkin under the table for Aletta."
    "And I do the best I can to push my cock back into my pants without being seen."
    hide mouth_insert aletta
    hide aletta blowjob
    show aletta at center, zoomAt(1.5, (640, 1140)) with easeinbottom
    "I'm just about done when Aletta pops back up in her seat across the table."
    show aletta happy
    aletta.say "You see what I mean, [hero.name]?"
    aletta.say "You look so much more relaxed now."
    show aletta flirt
    aletta.say "Like you're ready for a good meal in good company!"
    mike.say "Ah..."
    mike.say "Yeah..."
    mike.say "You could say that, Aletta!"
    mike.say "But what about you?"
    mike.say "Have you still got an appetite after that?"
    show aletta happy at startle
    "Aletta chuckles and waves away my concerns."
    show aletta flirt
    aletta.say "Oh no, that was only a little snack."
    aletta.say "An aperitif, not even a starter."
    aletta.say "It takes a lot more than that to satisfy me!"
    "I take a deep breath an shake my head."
    "Because I can see that I'm in for a long, tiring night with Aletta."
    "I just hope I can keep up long enough to satisfy her!"
    $ aletta.love += 2
    $ aletta.sub += 1
    $ aletta.flags.restaurant_treat = TemporaryFlag(True, "day")
    return

label aletta_restaurant_cunnilingus:
    "I've been looking forward to taking Aletta out for a meal for quite a while now."
    "Plus the place where I've managed to snag us a table for the evening is pretty nice."
    "Definitely one of the places where I've wanted to eat since I heard about it."
    "But there's just something a little off-putting about Aletta's mood tonight."
    hide aletta
    show restaurant meal aletta alettabored nomeals with fade
    "Sure, she has a smile on her face and she's laughing at my jokes."
    "It just all seems a bit forced, you know?"
    "Looking at her over my menu, I decide that I have to ask the question."
    mike.say "Aletta..."
    mike.say "Are you feeling okay?"
    aletta.say "What?"
    show restaurant meal aletta alettahappy
    aletta.say "Why would you think that?"
    mike.say "Well..."
    mike.say "You just seem a little distracted, that's all."
    "Aletta sighs and puts her menu down."
    "Then she rubs her forehead with one hand."
    aletta.say "You noticed, huh?"
    aletta.say "It's not you, [hero.name]."
    show restaurant meal aletta alettabored
    aletta.say "I'm just kind of in a funk at the moment."
    aletta.say "I mean, this is all very nice."
    "Aletta gestures around the restaurant."
    aletta.say "But I kind of feel like I need some excitement, you know?"
    aletta.say "Maybe even to live a little dangerously for a change."
    "I nod as I listen to what Aletta has to say."
    "But then a thought occurs to me."
    "And it's a particularly wild thought too."
    "The kind that you either have to act on or forget."
    mike.say "I know exactly what you mean, Aletta."
    mike.say "You just sit right there and leave it to me..."
    show restaurant meal aletta alettahappy
    "Aletta looks confused, and she opens her mouth to question me."
    "But I'm already moving, sliding down in my chair."
    hide restaurant meal
    scene bg restaurant
    show aletta embarrassed at center, zoomAt(1.5, (640, 1140))
    with fade
    "And before she can object, I'm disappearing under the table."
    "As soon as I'm down there on the floor, I get to work."
    "I scuttle the short distance to Aletta's side, crouching low."
    "Her legs are right in front of me, slightly parted."
    "And they look so good it's all I can do to keep focused."
    "Putting a hand on each of her knees, I push her skirt upwards."
    show aletta surprised at startle
    aletta.say "Hey!"
    aletta.say "What are you doing?!?"
    "I look up at the sound of Aletta's hissed words."
    "And I see her looking down at me from above."
    "Rather than responding with words, I just offer her a wink."
    "Then I turn my attention back to the space between her legs."
    show aletta flirt
    "By now I have Aletta's skirt hitched up high enough."
    "And as soon as her panties are exposed, I pull them down too."
    "If I was into this before, now I'm totally focused."
    "Because I can see and smell what I'm hunting for at last."
    "Aletta's pussy is calling to me from between her thighs."
    "And from the scent I'm catching and the way it's glistening in the light..."
    "Well, let's just say that I know she's getting excited too!"
    scene aletta cunnilingus
    show aletta cunnilingus restaurant date
    with fade
    "I take a deep breath and then lean in closer still."
    "Because if I'm going to do this, then I have to be quick."
    "Wasting no time in getting started, my tongue darts from between my lips."
    "Normally I'd have taken my time and teased around the edges."
    "But the waiter could come back at any moment."
    "So I just push the tip of my tongue slowly into Aletta's pussy."
    "Instantly I feel her tense and the sound of her gasping."
    "But she doesn't try to stop me, and I take that as a good sign."
    "Pushing my tongue deeper still, I start to probe and explore."
    "My eyes are closed by now, and I'm going on touch and scent alone."
    "My tongue is tingling from the taste of Aletta's pussy."
    "And the smell of it is almost as intoxicating."
    "Every time I move my tongue inside of her, she jerks in her seat."
    "Like it's sending a jolt of electricity through her entire body."
    "And that's perhaps the main thing that keeps pushing me onwards."
    "The thought of Aletta trying to play it cool as I'm doing this to her."
    "Every stroke of my tongue seems to push her closer to losing it."
    show aletta cunnilingus pleasure
    "But she's sitting right in the middle of the restaurant."
    "And the moment she lets on, all eyes will be on her!"
    "Spurred on by the thought, I turn my attention elsewhere."
    "Looking for that magic spot nestled away at the top, I give it my all."
    "And when I find it, I swear I hear Aletta's hands tighten on the edge of the table."
    "Licking away at that one spot, I even hear what sounds like her nails gouging the wood!"
    show aletta cunnilingus ahegao
    "That's when Aletta's thighs clamp down on either side of my head."
    "She must be cumming, but does she have to smother me at the same time!"
    "I barely manage to extricate myself from her without rolling over backwards."
    hide aletta cunnilingus
    show restaurant meal aletta alettablush with fade
    "Then I scuttle back to my side of the table as quickly as I can."
    "Checking the coast is clear, I pop up in my seat."
    "And I try to act like nothing is amiss."
    "But when I see the flushed look on Aletta's face, I almost laugh out loud."
    "She's panting and still holding onto the table for dear life."
    "And yet I can see the sheer amount of will-power she's displaying too."
    "For all the world, Aletta looks like she just ate something a little too spicy for her."
    mike.say "Oh my, Aletta..."
    mike.say "You look a little flushed!"
    mike.say "Was it something you ate?"
    mike.say "Or someone that ate you?"
    aletta.say "I..."
    show restaurant meal aletta alettahappy
    aletta.say "You..."
    show restaurant meal aletta alettabored
    aletta.say "Urgh..."
    show restaurant meal aletta alettahappy
    "I can't help smiling as Aletta battles to regain control of herself."
    "Because after all, she was the one that said she wanted to spice things up a little."
    "So I guess she should be more careful what she asks for in future."
    $ aletta.love += 2
    $ aletta.sub += 1
    $ aletta.flags.restaurant_treat = TemporaryFlag(True, "day")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
