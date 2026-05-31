init python:
    Event(**{
    "name": "dwayne_hottub_sex_female",
    "label": "dwayne_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(dwayne,
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
    "name": "fuck_dwayne",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasStamina(),
            MaxStat("morality", 50),
            ),
        PersonTarget(dwayne,
            IsActive(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })


label dwayne_hottub_sex_female:
    scene bg livingroom with dissolve
    "I have to say that I'm quite nervous about having Dwayne over for a dip in the hot-tub."
    "Not because I have any problems spending time alone with the guy, you understand?"
    "It's more on account of the fact that he's the CEO of a big-time company in the city."
    "Hell, one of my housemates even works for the guy!"
    "And I just know that means he must live in a huge mansion, or even a palace!"
    "So I have no idea what he's going to think when she sees my place."
    "I'm hoping that he's going to be impressed by what he sees."
    "And even if he's not, he should have the manners to keep it to himself, right?"
    "I mean, I've done the best I can to make the place look good."
    "The lights above the water are turned down low."
    "And the ones in the bottom of the tub are turned up high."
    "I've lined up what I hope is a nice bottle of wine with two glasses."
    "I even went to the trouble of scattering rose petals around the tub in the water too!"
    "So when Dwayne makes it over, I'm kind of on tenterhooks to see his reaction."
    scene bg pool with fade
    show dwayne at left with easeinleft
    "Dwayne strides out into the yard and then stops, hands planted on his hips."
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I watch in silence as he surveys the scene."
    dwayne.say "Well, well, well..."
    dwayne.say "Isn't this quaint!"
    "Quaint?"
    "What in the Hell does he mean by quaint?!?"
    "I'm about to open my mouth and demand an explanation."
    scene bg pool
    show dwayne at left
    with fade
    show dwayne at center with ease
    "But then Dwayne turns his gaze to me."
    dwayne.say "Oh-oh!"
    dwayne.say "Here's something a little different."
    dwayne.say "Here's something that looks positively divine!"
    "I already have my swimsuit on in preparation for getting in the tub."
    "And the compliment that Dwayne just paid me catches me totally off-guard."
    bree.say "Oh..."
    bree.say "I..."
    bree.say "Thank you, Dwayne!"
    bree.say "Do you really think I look that good?"
    "Dwayne shoots me one of his million dollar smiles."
    dwayne.say "Of course I do, [hero.name]!"
    dwayne.say "I'd never lie to a beautiful woman."
    dwayne.say "Now, I think I'm a little over-dressed at the moment..."
    "I swear that Dwayne somehow strips off his clothes in one go."
    "Kind of like you see those strippers with the velcro pants do it."
    "One moment he's standing there fully clothed."
    $ game.active_date.clothes = "swimsuit"
    show dwayne swimsuit with dissolve
    "And the next he's posing in just his trunks."
    "It's so quick that I take a step back in surprise."
    "But Dwayne seems to think that it's because I'm impressed with what I see."
    dwayne.say "Hey, [hero.name]..."
    dwayne.say "I know it's a lot."
    dwayne.say "The hair, the face, the bod!"
    dwayne.say "Just remember, I'm not really a demi-god!"
    "I shoot Dwayne a wry smile and shake my head."
    bree.say "I've got to admit, Dwayne..."
    bree.say "You keep yourself in damn good shape."
    bree.say "But I don't think you're any kind of god!"
    show dwayne at startle
    "Dwayne laughs and waves a hand in my general direction."
    dwayne.say "Ah, I'm just messing with you, [hero.name]!"
    dwayne.say "So are we going to get in this hit-tub or not?"
    "I nod and walk over to the edge of the tub, beckoning for Dwayne to follow me."
    "And as I'm lowering myself into the water, I catch him watching me."
    "As soon as he notices that I'm onto him, Dwayne climbs into the water too."
    show hottub dwayne valentine with fade
    "Sitting on the opposite side of the tub, he reaches for the bottle of wine."
    dwayne.say "Allow me, [hero.name]..."
    "Dwayne deftly opens the bottle and pours out two glasses."
    "He hands one to me and takes the other for himself."
    dwayne.say "Here's to us, [hero.name]!"
    dwayne.say "Bottoms up!"
    "I smile and raise my glass to my lips, taking a sip of the wine."
    "But Dwayne shoots me a quizzical glance when I do this."
    "And it's then that I notice he's drained off maybe half of his own glass."
    dwayne.say "What's the matter, [hero.name]?"
    dwayne.say "The wine not to your taste?"
    bree.say "Oh no, Dwayne..."
    bree.say "I'm just used to drinking a little slower than you!"
    dwayne.say "What are you saying, [hero.name]?"
    dwayne.say "That I'm some kind of alcoholic?"
    bree.say "No, of course not!"
    bree.say "I just...well..."
    bree.say "Okay, okay..."
    "I can't think of anything else that might remedy the situation."
    "So I raise my glass to my lips and drink off as much as I can manage."
    "And then I gulp it down, hoping that will satisfy Dwayne."
    "To my relief, it does seem to do the trick."
    "He nods and smiles."
    dwayne.say "There, you see?"
    dwayne.say "Now you're getting into the right mood!"
    "I nod and smile."
    "But even as I do so, I can feel myself getting dizzy."
    "If feels like the wine's gone straight to my head."
    "That can't be right - I'm not that much of a light-weight!"
    "Wait a minute...did I eat anything before Dwayne came over?"
    "I thought I did, but my heads been in such a crazy place."
    "It's possible that I didn't and just forgot all about it."
    bree.say "Ooh..."
    bree.say "I feel a little..."
    bree.say "A little wobbly!"
    "I do the best I can to steady myself."
    "But I'm too far away to reach the edge of the tub."
    "And when I reach for it, I almost topple face first into the water."
    show hottub dwayne valentine nomc
    with hpunch
    bree.say "Whoa..."
    "Luckily for me I manage to get my hands out in front of me."
    play sound water_splash
    with vpunch
    "And they hit the bottom of the tub before my head goes under the water."
    "But that still leaves me on all fours, with my ass in the air."
    "Worse still, it's pointing at Dwayne!"
    "I glance back over my shoulder, already beginning to blush."
    bree.say "Dwayne..."
    bree.say "This is SO embarrassing!"
    bree.say "Don't look at..."
    "My words trail off as I see what Dwayne's doing right now."
    "He's staring at me with an intense look in his eyes."
    "And when I glance downwards, I see he has his hand inside of his trunks."
    "There's no way to hide what's in there with it either."
    "Dwayne's got a massive erection."
    "One that he must have got from watching me flail about in the water."
    "My cheeks are still burning with embarrassment."
    "But now I can feel other parts of me beginning to warm up too."
    "I glance back up from Dwayne's groin, making eye contact with him."
    "And in that moment something passes between us."
    "Neither of us says a single word out loud."
    "But somehow we both know exactly what the other seems to want."
    show hottub sex female dwayne with fade
    "Dwayne pulls down the waistband of his trunks to expose his cock."
    "And the moment that I see it in the flesh, I nod eagerly."
    "I'm sure to stay exactly where I am as Dwayne pulls out his cock."
    "But once it's out, I scuttle backwards, closing the distance between us."
    "Dwayne's already waiting for me, cock in one hand."
    "He uses the other to grab hold of my ass, squeezing one of my buttocks."
    "His hold on me isn't gentle, but that hardly seems to matter right now."
    "And I don't complain once as he pulls aside the crotch of my swimsuit either."
    "Because I know now that I want this more than anything right now."
    "I can almost feel my pussy getting wetter by the moment."
    "Feel it loosening up in anticipation of what's coming next!"
    "And then I feel the tip of Dwayne's cock between my butt-cheeks."
    with hpunch
    "He pushes it hard against the lips of my pussy."
    "But even though I want it, they don't yield straight away."
    "This means that I'm treated to a delightful few moments before they do."
    "In that time, Dwayne grunts and grinds away at me."
    "The head of his cock slides up and down my pussy."
    "And the feeling is amazing, making me want him in me all the more."
    "Which means that when my body finally surrenders, it's that much more intense!"
    dwayne.say "Heads up, [hero.name]..."
    dwayne.say "Here I come!"
    "I hardly need Dwayne's cocky warning about what's happening back there."
    "And I try to ignore his words in favour of enjoying the experience."
    "Like I already said, Dwayne's not holding back."
    "And he comes thundering in like a charging bull."
    "I'm not going to lie, the guy has a pretty impressive manhood."
    "And he certainly knows how to use it like a battering ram!"
    with hpunch
    play sexsfx1 slide_in
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop volume 10
    "I can't help gasping and moaning as he pushes as far into me as possible."
    "Once he's there, Dwayne stay's still, probably savouring the sensation."
    "Which is exactly what I'm doing at the same time."
    play sexsfx1 fuck_calm loop
    play sound "sd/moans/sasha/sasha_panting.ogg" loop volume 10
    "But as soon as he starts to move inside me, it gets far more intense."
    "I can feel him thrusting in and out of me like a fucking machine."
    "If you pardon the pun!"
    "Dwayne seems to make love like he's got a point to prove."
    play sexsfx1 fuck_moderate loop
    play sound "sd/moans/sasha/sasha_moans_hard_low.ogg" loop volume 10
    "Though I don't know what it is, apart from the fact he's a genetic jackhammer!"
    "I'm panting and moaning by now, unable to keep quiet."
    "For all of his posturing and posing, I've got to admit one thing."
    "Dwayne really knows what he's doing back there!"
    scene dwayne grab cheeks
    show swimmingrace_bg_03 zorder 1 at center, zoomAt(1.75, (1000, 1040)), blur(5)
    show dwayne grab cheeks zorder 2 at flip
    with hpunch
    play sound "sd/moans/sasha/sasha_moans_hard_medium.ogg" loop volume 10
    bree.say "Ah..."
    bree.say "Harder, Dwayne!"
    bree.say "Fuck me harder!"
    dwayne.say "God dammit, girl!"
    dwayne.say "What does it take..."
    dwayne.say "To...satisfy you?!?"
    scene bg black
    show hottub sex female dwayne
    with hpunch
    play sexsfx1 fuck_speed loop
    "For all his complaining, Dwayne steps up to the challenge."
    "Pretty soon I can feel his pace increasing, him thrusting harder."
    "And he certainly manages to give me what I was asking for."
    "Oh fuck...what was I even thinking?"
    "I can't remember the last time I got pounded like this!"
    "It feels so damn good - but I know I can't take much more of it."
    scene dwayne grab cheeks
    show swimmingrace_bg_03 zorder 1 at center, zoomAt(1.75, (1000, 1040)), blur(5)
    show dwayne grab cheeks zorder 2 at flip
    with hpunch
    play sound "sd/moans/sasha/sasha_moans_hard_high.ogg" loop volume 10
    bree.say "Argh..."
    bree.say "Dwayne..."
    bree.say "You're going to..."
    bree.say "Make me cum!"
    scene bg black
    show hottub sex female dwayne
    with hpunch
    play sexsfx1 fuck_sprint loop
    play sound "sd/moans/sasha/sasha_moans_hard_orgasm.ogg" loop volume 10
    "I can feel my orgasm taking hold even as I'm saying all of this."
    "All I can do is throw my head around as it takes a hold of me."
    "But a moment later I feel something else happening too."
    "I guess the ego-rub must have had a serious effect on Dwayne."
    with hpunch
    "Because he's cumming too!"
    with hpunch
    "And it's no pathetic little spurt either."
    with hpunch
    "Dwayne shoots his load like an erupting volcano."
    with hpunch
    "I feel it surging inside of me, hot and enough to fill me completely."
    $ dwayne.impregnate()
    play sexsfx1 final_thrust
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop volume 10
    "My arms and legs are wobbling as my muscles give up the fight."
    "Once they collapse, I slide off Dwayne's cock and into the water."
    "And all I can do is float there, still feeling my climax making my muscles twitch."
    stop sexsfx1
    stop sound
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ dwayne.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return


label dwayne_hottub_sex_female_old:
    scene bg livingroom with dissolve
    "I have to say that I'm quite nervous about having Dwayne over for a dip in the hot-tub."
    "Not because I have any problems spending time alone with the guy, you understand?"
    "It's more on account of the fact that he's the CEO of a big-time company in the city."
    "Hell, one of my housemates even works for the guy!"
    "And I just know that means he must live in a huge mansion, or even a palace!"
    "So I have no idea what he's going to think when she sees my place."
    "I'm hoping that he's going to be impressed by what he sees."
    "And even if he's not, he should have the manners to keep it to himself, right?"
    "I mean, I've done the best I can to make the place look good."
    "The lights above the water are turned down low."
    "And the ones in the bottom of the tub are turned up high."
    "I've lined up what I hope is a nice bottle of wine with two glasses."
    "I even went to the trouble of scattering rose petals around the tub in the water too!"
    "So when Dwayne makes it over, I'm kind of on tenterhooks to see his reaction."
    scene bg pool with fade
    show dwayne at left with easeinleft
    "Dwayne strides out into the yard and then stops, hands planted on his hips."
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I watch in silence as he surveys the scene."
    dwayne.say "Well, well, well..."
    dwayne.say "Isn't this quaint!"
    "Quaint?"
    "What in the Hell does he mean by quaint?!?"
    "I'm about to open my mouth and demand an explanation."
    scene bg pool
    show dwayne at left
    with fade
    show dwayne at center with ease
    "But then Dwayne turns his gaze to me."
    dwayne.say "Oh-oh!"
    dwayne.say "Here's something a little different."
    dwayne.say "Here's something that looks positively divine!"
    "I already have my swimsuit on in preparation for getting in the tub."
    "And the compliment that Dwayne just paid me catches me totally off-guard."
    bree.say "Oh..."
    bree.say "I..."
    bree.say "Thank you, Dwayne!"
    bree.say "Do you really think I look that good?"
    "Dwayne shoots me one of his million dollar smiles."
    dwayne.say "Of course I do, [hero.name]!"
    dwayne.say "I'd never lie to a beautiful woman."
    dwayne.say "Now, I think I'm a little over-dressed at the moment..."
    "I swear that Dwayne somehow strips off his clothes in one go."
    "Kind of like you see those strippers with the velcro pants do it."
    "One moment he's standing there fully clothed."
    show dwayne swimsuit with dissolve
    "And the next he's posing in just his trunks."
    "It's so quick that I take a step back in surprise."
    "But Dwayne seems to think that it's because I'm impressed with what I see."
    dwayne.say "Hey, [hero.name]..."
    dwayne.say "I know it's a lot."
    dwayne.say "The hair, the face, the bod!"
    dwayne.say "Just remember, I'm not really a demi-god!"
    "I shoot Dwayne a wry smile and shake my head."
    bree.say "I've got to admit, Dwayne..."
    bree.say "You keep yourself in damn good shape."
    bree.say "But I don't think you're any kind of god!"
    show dwayne at startle
    "Dwayne laughs and waves a hand in my general direction."
    dwayne.say "Ah, I'm just messing with you, [hero.name]!"
    dwayne.say "So are we going to get in this hit-tub or not?"
    "I nod and walk over to the edge of the tub, beckoning for Dwayne to follow me."
    "And as I'm lowering myself into the water, I catch him watching me."
    "As soon as he notices that I'm onto him, Dwayne climbs into the water too."
    show hottub dwayne valentine with fade
    "Sitting on the opposite side of the tub, he reaches for the bottle of wine."
    dwayne.say "Allow me, [hero.name]..."
    "Dwayne deftly opens the bottle and pours out two glasses."
    "He hands one to me and takes the other for himself."
    dwayne.say "Here's to us, [hero.name]!"
    dwayne.say "Bottoms up!"
    "I smile and raise my glass to my lips, taking a sip of the wine."
    "But Dwayne shoots me a quizzical glance when I do this."
    "And it's then that I notice he's drained off maybe half of his own glass."
    dwayne.say "What's the matter, [hero.name]?"
    dwayne.say "The wine not to your taste?"
    bree.say "Oh no, Dwayne..."
    bree.say "I'm just used to drinking a little slower than you!"
    dwayne.say "What are you saying, [hero.name]?"
    dwayne.say "That I'm some kind of alcoholic?"
    bree.say "No, of course not!"
    bree.say "I just...well..."
    bree.say "Okay, okay..."
    "I can't think of anything else that might remedy the situation."
    "So I raise my glass to my lips and drink off as much as I can manage."
    "And then I gulp it down, hoping that will satisfy Dwayne."
    "To my relief, it does seem to do the trick."
    "He nods and smiles."
    dwayne.say "There, you see?"
    dwayne.say "Now you're getting into the right mood!"
    "I nod and smile."
    "But even as I do so, I can feel myself getting dizzy."
    "If feels like the wine's gone straight to my head."
    "That can't be right - I'm not that much of a light-weight!"
    "Wait a minute...did I eat anything before Dwayne came over?"
    "I thought I did, but my heads been in such a crazy place."
    "It's possible that I didn't and just forgot all about it."
    bree.say "Ooh..."
    bree.say "I feel a little..."
    bree.say "A little wobbly!"
    "I do the best I can to steady myself."
    "But I'm too far away to reach the edge of the tub."
    "And when I reach for it, I almost topple face first into the water."
    show hottub dwayne valentine nomc
    with hpunch
    bree.say "Whoa..."
    "Luckily for me I manage to get my hands out in front of me."
    play sound water_splash
    with vpunch
    "And they hit the bottom of the tub before my head goes under the water."
    "But that still leaves me on all fours, with my ass in the air."
    "Worse still, it's pointing at Dwayne!"
    "I glance back over my shoulder, already beginning to blush."
    bree.say "Dwayne..."
    bree.say "This is SO embarrassing!"
    bree.say "Don't look at..."
    "My words trail off as I see what Dwayne's doing right now."
    "He's staring at me with an intense look in his eyes."
    "And when I glance downwards, I see he has his hand inside of his trunks."
    "There's no way to hide what's in there with it either."
    "Dwayne's got a massive erection."
    "One that he must have got from watching me flail about in the water."
    "My cheeks are still burning with embarrassment."
    "But now I can feel other parts of me beginning to warm up too."
    "I glance back up from Dwayne's groin, making eye contact with him."
    "And in that moment something passes between us."
    "Neither of us says a single word out loud."
    "But somehow we both know exactly what the other seems to want."
    show hottub sex female dwayne with fade
    "Dwayne pulls down the waistband of his trunks to expose his cock."
    "And the moment that I see it in the flesh, I nod eagerly."
    "I'm sure to stay exactly where I am as Dwayne pulls out his cock."
    "But once it's out, I scuttle backwards, closing the distance between us."
    "Dwayne's already waiting for me, cock in one hand."
    "He uses the other to grab hold of my ass, squeezing one of my buttocks."
    "His hold on me isn't gentle, but that hardly seems to matter right now."
    "And I don't complain once as he pulls aside the crotch of my swimsuit either."
    "Because I know now that I want this more than anything right now."
    "I can almost feel my pussy getting wetter by the moment."
    "Feel it loosening up in anticipation of what's coming next!"
    "And then I feel the tip of Dwayne's cock between my butt-cheeks."
    with hpunch
    "He pushes it hard against the lips of my pussy."
    "But even though I want it, they don't yield straight away."
    "This means that I'm treated to a delightful few moments before they do."
    "In that time, Dwayne grunts and grinds away at me."
    "The head of his cock slides up and down my pussy."
    "And the feeling is amazing, making me want him in me all the more."
    "Which means that when my body finally surrenders, it's that much more intense!"
    dwayne.say "Heads up, [hero.name]..."
    dwayne.say "Here I come!"
    "I hardly need Dwayne's cocky warning about what's happening back there."
    "And I try to ignore his words in favour of enjoying the experience."
    "Like I already said, Dwayne's not holding back."
    "And he comes thundering in like a charging bull."
    "I'm not going to lie, the guy has a pretty impressive manhood."
    "And he certainly knows how to use it like a battering ram!"
    with hpunch
    "I can't help gasping and moaning as he pushes as far into me as possible."
    "Once he's there, Dwayne stay's still, probably savouring the sensation."
    "Which is exactly what I'm doing at the same time."
    "But as soon as he starts to move inside me, it gets far more intense."
    "I can feel him thrusting in and out of me like a fucking machine."
    "If you pardon the pun!"
    "Dwayne seems to make love like he's got a point to prove."
    "Though I don't know what it is, apart from the fact he's a genetic jackhammer!"
    "I'm panting and moaning by now, unable to keep quiet."
    "For all of his posturing and posing, I've got to admit one thing."
    "Dwayne really knows what he's doing back there!"
    scene dwayne grab cheeks
    show swimmingrace_bg_03 zorder 1 at center, zoomAt(1.75, (1000, 1040)), blur(5)
    show dwayne grab cheeks zorder 2 at flip
    with hpunch
    bree.say "Ah..."
    bree.say "Harder, Dwayne!"
    bree.say "Fuck me harder!"
    dwayne.say "God dammit, girl!"
    dwayne.say "What does it take..."
    dwayne.say "To...satisfy you?!?"
    scene bg black
    show hottub sex female dwayne
    with hpunch
    "For all his complaining, Dwayne steps up to the challenge."
    "Pretty soon I can feel his pace increasing, him thrusting harder."
    "And he certainly manages to give me what I was asking for."
    "Oh fuck...what was I even thinking?"
    "I can't remember the last time I got pounded like this!"
    "It feels so damn good - but I know I can't take much more of it."
    scene dwayne grab cheeks
    show swimmingrace_bg_03 zorder 1 at center, zoomAt(1.75, (1000, 1040)), blur(5)
    show dwayne grab cheeks zorder 2 at flip
    with hpunch
    bree.say "Argh..."
    bree.say "Dwayne..."
    bree.say "You're going to..."
    bree.say "Make me cum!"
    scene bg black
    show hottub sex female dwayne
    with hpunch
    "I can feel my orgasm taking hold even as I'm saying all of this."
    "All I can do is throw my head around as it takes a hold of me."
    "But a moment later I feel something else happening too."
    "I guess the ego-rub must have had a serious effect on Dwayne."
    with hpunch
    "Because he's cumming too!"
    with hpunch
    "And it's no pathetic little spurt either."
    with hpunch
    "Dwayne shoots his load like an erupting volcano."
    with hpunch
    "I feel it surging inside of me, hot and enough to fill me completely."
    $ dwayne.impregnate()
    "My arms and legs are wobbling as my muscles give up the fight."
    "Once they collapse, I slide off Dwayne's cock and into the water."
    "And all I can do is float there, still feeling my climax making my muscles twitch."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ dwayne.sexperience += 1
    scene bg black with dissolve
    return

label dwayne_fuck_date_female(location="hero"):
    $ renpy.dynamic("random_result")
    $ game.room = "bedroom4"
    $ random_result = game.days_played % 2
    call dwayne_fuck_date_intro_female (location) from _call_dwayne_fuck_date_intro_female

    if random_result == 0:
        call dwayne_fuck_date_kiss_foreplay from _call_dwayne_fuck_date_kiss_foreplay
    else:
        call dwayne_fuck_date_finger from _call_dwayne_fuck_date_finger
    menu:
        "Stand":
            call dwayne_fuck_date_stand (0) from _call_dwayne_fuck_date_stand
        "Missionary" if hero.sexperience >= 5:
            call dwayne_fuck_date_missionary (5) from _call_dwayne_fuck_date_missionary
    if _return == "leave_without_gain":
        return
    $ dwayne.sexperience += 1
    if _return == "leave_with_gain":
        return
    scene bg bedroom4 with fade
    "Dwayne and I lie on the bed, exhausted and covered in sweat that's quickly cooling."
    "I make to say something, some small talk."
    "But I can already hear his snoring, loud as a chainsaw, in my ear."
    "I guess now the only decision left is to either kick him out, or else let him sleep it off here."
    call sleep ("dwayne") from _call_sleep_89
    return

label dwayne_fuck_date_intro_female(location="hero"):
    $ result = game.days_played % 2
    if result == 0:
        scene bg house with fade
        "I have to admit that I'm kind of worried about bringing Dwayne back to my place."
        "The date we were just on seemed to go great, and neither of us is ready to call it a night."
        "But he's not made any kind of suggestion about the possibility of going to his place."
        "So it feels like it's either this or ending the date prematurely."
        "I mean, it's not like Dwayne turns his nose up when I suggest my place."
        "I just know that he's used to something a lot better!"
        "Knowing this, I deliberately avoid turning on the lights once we're inside."
        scene bg livingroom at dark with fade
        bree.say "It's this way, Dwayne."
        bree.say "Just follow me, okay?"
        show dwayne at center, zoomAt(1.25, (840, 880)) with easeinright
        dwayne.say "Okay, [hero.name]..."
        dwayne.say "Just let me..."
        show dwayne vangry at stepback
        dwayne.say "OUCH!"
        bree.say "What's the matter?"
        show dwayne angry
        dwayne.say "Nothing..."
        show dwayne normal
        dwayne.say "I'm fine..."
        dwayne.say "I just walked into something and banged my knee."
        bree.say "Sorry about that, Dwayne..."
        bree.say "Here, take my hand and I'll lead the way."
        show dwayne at center, traveling(1.35, 0.5, (640, 960))
        "Dwayne does as he's told."
        "But he's not going to just let it go."
        show dwayne happy
        dwayne.say "Aren't you going to turn some lights on in here?"
        dwayne.say "Surely you're not struggling to pay the electricity bill?"
        dwayne.say "I mean, one of your housemates does work for me."
        dwayne.say "Is he not paying his way or something?"
        show dwayne normal
        "We're just about to my bedroom door by now."
        "And I make sure to hurry Dwayne inside before I answer his questions."
        scene bg bedroom4
        show dwayne at center, zoomAt(1.25, (640, 880))
        with fade
        "When I finally close the door and turn around, I see Dwayne standing in front of me."
        "He has his arms crossed over his chest and his gaze focused in my direction."
        "Instantly I feel like I'm on trial, like I've been caught out by a real adult."
        show dwayne annoyed
        dwayne.say "Okay, [hero.name]..."
        dwayne.say "What's going on here?"
        dwayne.say "Why are you acting so strangely?"
        bree.say "Okay, Dwayne, okay..."
        bree.say "I'm kind of embarrassed to be bringing you back here."
        bree.say "You live in a giant mansion, so this must be like slumming it for you!"
        show dwayne happy
        show dwayne at startle(0.14,-20)
        pause 0.2
        show dwayne at startle(0.14,-20)
        pause 0.2
        show dwayne at startle(0.14,-20)
        "Dwayne lets out a booming laugh and shakes his head."
        show dwayne smile
        "And I can't help notice that he starts unbuttoning his shirt too."
        show dwayne happy
        dwayne.say "Oh please..."
        dwayne.say "I didn't come here to judge you, [hero.name]."
        show dwayne at traveling (1.5, 0.3, (640, 1040))
        dwayne.say "I came here to get it on!"
        dwayne.say "Now are we going to fuck, or what?"
        show dwayne swimsuit smile with dissolve
        "By now Dwayne's stripped to the waist, showing off his buff torso."
        "I watch as he pulls down his pants to reveal his equally impressive legs."
        "Even before he takes off his shorts, I can see the size of his manhood."
        "And that's more than enough to banish all of my misgivings."
        bree.say "Well..."
        bree.say "When you put it like that..."
        "I'm still staring at Dwayne's member as I begin to pull off my own clothes."
        "But he doesn't stay standing on the same spot as I get undressed."
        "Instead Dwayne walks around me, forcing me to follow him with my gaze."
    elif result == 1:
        "I've been hanging off of Dwayne's arm all night, every chance I've gotten."
        "The date that we've just rounded off was a total win from my point of view."
        "We went to fancy, expensive places where Dwayne likes to show off his largesse."
        "And the whole night he made a point of showing me off to everyone that saw us."
        "At times I felt like I was totally there to make him look like as big of a man as possible."
        "And the knowledge that he was using me in that way made me feel so excited."
        "Almost like it was a kind of sexual excitement at times too!"
        "Now that we're finally alone, I'm beginning to feel like it's building up inside of me."
        "And I want Dwayne to do something about it, as quickly as I can make him."
        "So that's how I end up holding his hand with both of mine."
        "That and pulling him into the bedroom after me."
        scene bg livingroom
        show dwayne at center, zoomAt(1.25, (640, 880))
        with fade
        bree.say "Dwayne, honey..."
        bree.say "I've been good all night, right?"
        bree.say "Like, I've been a REALLY good girl, yeah?"
        show dwayne smile
        "Dwayne has a huge smile on his face right now."
        scene bg secondfloor
        show dwayne happy at center, zoomAt(1.25, (640, 880))
        with fade
        "And I know that he's letting me lead him into the bedroom."
        "Because with muscles like his, there's no way I could move him an inch if he tried to stop me."
        "Which lets me know that Dwayne's receptive to my pleas, indulging me to see where this is going."
        show dwayne happy
        dwayne.say "I'd agree with that, [hero.name]."
        dwayne.say "You've been a regular delight this evening."
        dwayne.say "And I've been proud to be able to show you off too."
        show dwayne smile
        "I'm nodding eagerly as Dwayne says all of this."
        "Smiling up at him in what I hope is an endearing manner."
        bree.say "So..."
        bree.say "That means I deserve a reward, right?"
        bree.say "I've been nice to you, so you have to be nice to me?"
        scene bg bedroom4
        show dwayne at center, zoomAt(1.25, (640, 880))
        with fade
        "By now we're inside the bedroom, and Dwayne turns away for a moment."
        "At first I'm afraid that he's going to pull away from me or leave the room."
        "But then, to my immense relief, I see that he's just shutting the bedroom door."
        "Though when I hear the sound of the lock clicking a moment later, my heart almost skips a beat."
        "Because I'm getting ever more sure that he's on the same wavelength as me!"
        show dwayne happy
        dwayne.say "It doesn't work quite like that, [hero.name]."
        dwayne.say "This isn't a case of you doing things for me and then my reciprocating."
        dwayne.say "That would imply that our relationship is somehow one of equality."
        show dwayne smile at traveling (1.5, 0.3, (640, 1040))
        "Dwayne turns to face me, a knowing smile on his face."
        show dwayne happy
        dwayne.say "It's more like I require you to do nice things for me."
        dwayne.say "That's what earns you my continuing affection and attention."
        dwayne.say "Any affection that flows in the opposite direction does so at my own say so."
        dwayne.say "And I can assure you that it has nothing whatsoever to do with your efforts."
        show dwayne therock
        "I can feel my mood beginning to sink."
        "All because I'm starting to feel like Dwayne's not going to be nice to me tonight!"
        bree.say "Oh, Dwayne!"
        bree.say "Are you saying you're going to be mean to me tonight?"
        "Dwayne shakes his head at this."
        show dwayne shout
        dwayne.say "Oh by no means, [hero.name]..."
        dwayne.say "I was simply restating the terms of our relationship."
        dwayne.say "But I am in the mood to 'be nice to you'..."
        dwayne.say "As you so quaintly put it!"
        dwayne.say "So you better start stripping off those clothes, right now!"
        show dwayne normal
        "It's all that I can do to keep myself from clapping my hands with glee."
        "Because the moment Dwayne speaks those words, all of my doubts disappear."
        "I totally forget about my earlier misgivings and instead focus on the matter at hand."
        "Which, of course, is the urgent need to show Dwayne that I'm obedient and grateful."
        "I'm already unbuttoning my clothes before he takes a step backwards."
        "And I know that he's doing so to give me more room to work with."
        "So I don't hesitate to take advantage of that fact."
        "But rather I use it to make my little strip show more alluring."
        "Everything that I take off I'm sure wave in front of Dwayne's face."
        "Then I drop it on the floor and move on to take off the next item of clothing."
        show dwayne therock
        "Dwayne seems to approve of what he's seeing too."
        "He has one hand on his chin, stroking it thoughtfully."
        "And I hardly need to be looking in his direction to know his eyes are on me."
        "It's actually like I can feel them watching me, sense his gaze moving over my body."
        "I keep up the act, not stopping until the very last item of clothing is in my hand."
        bree.say "Ta-da!"
        bree.say "What do you think of that, Dwayne honey?"
    else:
        scene bg house
        show dwayne at center, zoomAt(1.25, (840, 880))
        with fade
        bree.say "Okay, Dwayne..."
        bree.say "I know that you're kind of used to a more palatial kind of house..."
        bree.say "And it's not like I've had a lot of notice to get the place clean either..."
        bree.say "So just don't judge me when we get inside, okay?"
        "I'm saying all of this with my back pressed against the front door of the house."
        "And while gazing up at Dwayne as he stands there, towering over me too."
        "We've just got back to my place after a date that's been a total success."
        "And now it's hitting me that I live in a hovel compared to Dwayne's home address!"
        show dwayne happy
        dwayne.say "What are you talking about, [hero.name]?"
        dwayne.say "This looks like a great little place to live."
        dwayne.say "And the mess isn't a problem either."
        dwayne.say "Unless you have live racoons burrowing through literal piles of garbage in there!"
        show dwayne smile
        "Dwayne's smiling in a way that makes it pretty clear he's joking with me."
        "But I'm already feeling so paranoid that I just can't take it in the way it's intended."
        bree.say "And what if there are racoons and garbage?"
        bree.say "No...pretend I didn't say that, okay?"
        bree.say "Just come inside."
        "I turn around so that my back is to Dwayne and unlock the door."
        "Then taking a deep breath, I open it and wave for him to follow me inside."
        scene bg livingroom at dark with fade
        show dwayne at center, zoomAt(1.25, (840, 880)) with easeinright
        "I deliberately turn on only the smaller lights as I lead Dwayne through the house."
        "And I don't even hint at taking him into the sitting room or dining room."
        scene bg secondfloor
        show dwayne happy at center, zoomAt(1.25, (640, 880))
        with fade
        "Instead I just head straight for the stairs and begin climbing them."
        dwayne.say "Looks like someone knows exactly what they want tonight!"
        "Dwayne says this just as we reach the landing and the door to my bedroom."
        "And I realise he's mistaking my eagerness to keep him from seeing the state of the house for something else."
        "But then how in the hell am I supposed to explain it to him without making it look like I don't want sex tonight?"
        "Suddenly I feel like I'm caught in a trap of my own devising."
        "And the simplest way out if would just be to pander to Dwayne's take on the matter."
        if hero.morality <= -25:
            bree.say "Oh, you know what I want, Dwayne..."
            bree.say "I want every inch of you inside of me..."
            bree.say "And I want it now!"
        elif hero.morality >= 25:
            bree.say "Erm..."
            bree.say "Of course, Dwayne..."
            bree.say "I...I just can't get enough of you!"
        else:
            bree.say "You know me, Dwayne..."
            bree.say "When I see something I want, I make sure I get it!"
        scene bg bedroom4
        show dwayne smile at center, zoomAt(1.25, (640, 880))
        with fade
        "Dwayne's practically beaming at me as I open the door to my room and lead him inside."
        hide dwayne with fade
        "While I turn my back for a moment to close the door, I can hear him doing something."
        "But I'm not prepared for the sight that greets me when I turn around again."
        "I swear that I only had my back turned for a couple of seconds at the most."
        show dwayne naked at center, zoomAt(1.25, (640, 880)) with fade
        "And yet I'm greeted by the sight of Dwayne reclining on my bed."
        "He has his head propped up on one hand as he shoots me a grin."
        "Oh, and I should also explain that he's totally naked too!"
        bree.say "H...how..."
        bree.say "How in the hell?"
        bree.say "Dwayne, strippers take longer than that to get undressed!"
        show dwayne smile
        "Dwayne raises an eyebrow, and his smile broadens as he drinks in my amazement."
        show dwayne happy
        dwayne.say "I'm a man of many talents, [hero.name]..."
        dwayne.say "A lot of which you have yet to witness."
        dwayne.say "And I promise you, some are a lot more impressive than this!"
        show dwayne normal
        "Dwayne uses his free hand to indicate his nakedness."
        "But then something seems to occur to him."
        show dwayne happy
        dwayne.say "I should be clear, [hero.name]..."
        dwayne.say "I mean more impressive than getting undressed so quickly."
        dwayne.say "There's precious little that's more impressive than this bod!"
        dwayne.say "Now..."
        dwayne.say "How about you take off a couple of layers and join me?"
        show dwayne normal
        if hero.morality <= -25:
            "I see the chance to show Dwayne just how seductive I can be."
            "So I make sure to strip-off slowly as I saunter over to the bed."
            "And I shake my assets every step of the way too."
        elif hero.morality >= 25:
            "I nod, trying as best I can to hide my nerves."
            "And I tug off my clothes as quickly as I can."
            "Rushing over to the bed while covering my bits with my hands."
        else:
            "I make sure there's a knowing smile on my face as I begin to strip-off."
            "Because I want to give Dwayne a little show as I walk over."
            "But at the same time I want to retain a little control too."
        show dwayne naked at center, traveling(1.5, 1.0, (640, 1080))
        "Dwayne watches me as I approach the bed, nodding his approval."
        "And when I reach it, he shuffles backwards on the mattress."
        "Then he pats the space directly in front of him."
        "I'm beginning to climb onto the bed when I feel something brush against my leg."
        "Without thinking, I look down to see what it could be."
        "And I see Dwayne's cock, already starting to rise into the air!"
        show dwayne happy
        dwayne.say "What can I say, [hero.name]..."
        dwayne.say "You have such an effect on me."
        dwayne.say "Every part of me wants to give you a standing ovation!"
        show dwayne smile
        "I give Dwayne a playful push on the shoulder as I lie down beside him."
        "But at the same time, I can't help staring at his member as it rises and gets steadily bigger."
        "No wonder this guy strides around like he's the king of the entire world."
        "With something like that hidden in his pants, he must feel like a total Giga-Chad!"



















































    return

label dwayne_fuck_date_kiss_foreplay:
    "I'm expecting him to maybe give me a little round of applause."
    show dwayne therock
    "Perhaps heap some praise onto me for my performance."
    "But what I wasn't prepared for is for him to step quickly forwards."
    "And nothing could have made me predict that Dwayne would take hold of me either."
    "Don't get me wrong, Dwayne doesn't grab me or manhandle me in any way."
    hide dwayne
    show dwayne grab cheeks mc_naked
    with fade
    "Rather I find his hands holding either side of my head."
    "I can feel the strength in each individual finger right now."
    "Yet somehow he's gentle enough to cause me no pain at all."
    bree.say "Erm..."
    bree.say "Dwayne..."
    bree.say "What are you doing?!?"
    "My voice sounds weird, as my lips are kind of puckered in his grip."
    "But all the same, I make an effort to twist then into what I hope is recognisable as a smile."
    dwayne.say "I'm just admiring my girl, [hero.name]..."
    dwayne.say "Getting a real good look at how pretty she is."
    dwayne.say "In fact she's so pretty, that I really want to kiss her!"
    "Dwayne's words do a lot to reassure me in the moment."
    "And I keep smiling, pleased with the prospect of being kissed."
    "But as Dwayne leans in closer, he makes no effort to release me."
    "Instead he squeezes my cheeks even tighter than before."
    "This means that I can't keep my tongue from popping out between my puckered lips."
    "Dwayne parts his own lips, then wraps them around my protruding tongue."
    "What follows is one of the weirdest kisses I've ever experienced."
    hide dwayne grab cheeks
    show dwayne forced kiss
    with fade
    $ dwayne.flags.kiss += 1
    "In a way it's more like Dwayne sucking on my tongue and lips for his own pleasure."
    "But as that makes it sound even stranger than it looks, I banish the thought."
    "All he's doing is showing his affection for me in a unique manner."
    "Once I have that settled in my own head, I can start to enjoy myself."
    "Closing my eyes and letting the pleasure build, I lean into the experience."
    "And pretty soon I can feel the tingle of excitement start to spread through me."
    "Oh yeah...this is actually quite a nice sensation."
    "Sure, it's unusual, but in life you have to embrace difference."
    "Otherwise how are you ever going to expand your horizons?"
    "It's just as I'm thinking this that I feel Dwayne's tongue begin to wander."
    "My eyes pop open again as it slides down and onto my chin."
    "Then they follow its progress up my cheek and towards my forehead."
    "Erm...okay..."
    "So Dwayne wants to lick the entirety of my face."
    "That's no stranger than what I he was doing before, I guess."
    "My eyes keep in following him as he crosses my forehead."
    "Then his tongue travels down the opposite side of my face too."
    "I'm a little OCD at times, so I get that."
    "The need to complete a full circle of my face."
    "That makes sense to me, I swear it does!"
    "Luckily for me, I suddenly feel the sensation of Dwayne's hands all over my body."
    "He's chosen this moment to start feeling me up, stroking my curves and crevices."
    "So it looks like we're kicking it up a stage now."
    hide dwayne forced kiss
    show dwayne grab cheeks mc_naked
    with fade
    "Going from simple kissing to full-on foreplay."
    "And boy, is that ever a relief!"
    "The way that Dwayne's stirring my body, waking it up..."
    "It feels so good that I soon begin to forget about his odd way of kissing."
    "In fact I can hardly tell what he's doing above the neck at all anymore."
    "All that's on my mind is where this is going and what we're doing next."
    "Because it promises to be something that'll totally blow my mind."
    return

label dwayne_fuck_date_finger:
    "Dwayne's sitting down on the sofa, reclining and looking in my direction."
    "I can feel his eyes on me, travelling up and down my body."
    "And from the look on Dwayne's face, he very much approves of what he sees!"
    "But then he suddenly slaps his left hand down onto his thigh."
    "The movement is so quick and the sound so loud."
    "I can't help squealing and jumping in surprise."
    bree.say "Aargh!"
    "Of course, this makes Dwayne throw back his head and bellow with laughter."
    dwayne.say "Ha ha!"
    dwayne.say "There's no need to be scared, [hero.name]..."
    dwayne.say "I won't bite - unless you want me to?"
    if hero.morality >= 25:
        "The best that I can manage in the way of an answer is to shake my head."
        "That and hurry over to Dwayne in the hope of keeping him from saying more."
    elif hero.morality <= -25:
        bree.say "I can bite too, Dwayne."
        bree.say "But I don't tend to ask permission first!"
        "I'm walking towards Dwayne as I say this, holding his eye the whole time."
    else:
        "I put what I hope is a wry smile on my face and shake my head."
        "Not dismissing the possibility, more showing my amusement at it."
        "And at the same time I begin to walk over to the sofa."
    "He watches with evident approval as reach the sofa and then sit down on his lap."
    "Sliding one arm around Dwayne's neck, I lean myself against him."
    scene dwayne foreplay finger with fade
    "Oh wow..."
    "He's so built, so solid."
    "I feel like I'm sitting on a recliner made of muscle!"
    "But now that I'm here and within his grasp, something seems to change in Dwayne."
    "Where before he was trying to lure me in to sit with him, now he finally has me."
    "And he doesn't waste any time taking full advantage of the fact."
    "The first thing I feel is the sensation of his hands all over my body."
    "They slide here and there, stroking and squeezing as they go."
    "But before their touch makes me utter a sound, his lips touch mine."
    "And the next thing I know, his tongue is exploring my mouth."
    "The passion is rising within me now, getting stronger by the second."
    "So I don't hold anything back, and I kiss Dwayne with an equal passion."
    "I can already feel the sensation of his cock getting hard beneath me."
    "And the mere thought of what he could do with it is sending me crazy."
    if hero.morality >= 25:
        "I'm more than a little afraid of what he might do with me."
        "But I know, deep down, that I want it too!"
    elif hero.morality <= -25:
        "I can imagine a hundred things that I want him to do to me."
        "And the mystery of what he'll choose is already making me wet!"
    else:
        "I can already imagine all the things he might do to me."
        "And the thought of them is already turning me on!"
    "So when I feel one of his hands slipping between my thighs, I quiver with anticipation."


    "And when his fingers begin to stroke my pussy, I know what's coming next."
    show dwayne foreplay finger fingering
    "Dwayne keeps right on kissing me as he plays with me down below."
    "His other hand still lingering on one of my breasts too."
    "And I can picture every movement that he's making down there."
    "His hands are large, his fingers as big as sausages."
    "Yet somehow he has a precise, almost delicate touch."
    "Which means that I'm treated to intense, expert attention."
    show dwayne foreplay finger closed
    "And part of me is glad that he's kissing me so passionately too."
    "Because otherwise I'm sure that I'd be crying out right now."
    "Unable to keep myself from expressing what I'm feeling."
    "Soon enough, Dwayne has more than one finger deep inside of me."
    "And he's working away diligently, every second bringing me closer to losing control."
    "Part of me wishes that he could go on doing this forever, or at least until I pass out."
    show dwayne foreplay finger opened
    "But I can already feel my body reaching it's natural limits."
    if hero.morality >= 25:
        "Helpless and unable to resist, I succumb to my orgasm."
        show dwayne foreplay finger squirt with vpunch
        "All the while wriggling in Dwayne's grasp."
        "Feeling embarrassed and even a little dirty."
        "But deep down, loving every moment."
    elif hero.morality <= -25:
        "I surrender myself to the fact that I'm cumming."
        show dwayne foreplay finger squirt with vpunch
        "All the while wanting more of his fingers inside me."
        "And clinging onto him for dear life."
    else:
        "There's nothing I can do to hold on."
        "And a moment later I lose it."
        show dwayne foreplay finger squirt with vpunch
        "Clinging onto Dwayne as I cum."
    return

label dwayne_fuck_date_stand(sexperience_min):
    "By the time I'm naked too, he's standing behind me."
    "And I can feel my heart starting to beat faster by the second."
    "All because I'm wondering what he's going to do back there."
    hide dwayne
    show dwayne stand eyes_surprised mouth_pleasure
    with vpunch
    "Suddenly I feel Dwayne's arms wrap around me."
    "It comes as such a surprise that I can't help crying out."
    "But that doesn't seem to put him off at all."
    bree.say "Argh!"
    dwayne.say "Ha ha!"
    dwayne.say "I got you now, [hero.name]!"
    dwayne.say "So..."
    dwayne.say "Where do you want it?"
    menu:
        "Ravage my pussy":
            "I can't think of anything other than having Dwayne inside of me right now."
            "And I know exactly where I want it too."
            show dwayne stand eyes_open mouth_normal
            bree.say "My pussy, Dwayne..."
            bree.say "I want it in my pussy!"
            dwayne.say "Whatever you say, [hero.name]..."
            call check_condom_usage (dwayne) from _call_check_condom_usage_128
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                $ hero.morality += 4
                show dwayne stand condom
            "I can't help yelping a second time as Dwayne leaps into action."
            "Dwayne's cock is right there, bobbing up and down."
            "From this angle it looks longer and thicker than I've ever seen it."
            "And I can't help wondering how the hell it's ever going to fit!"
            "But it looks like I'm going to find out for certain."
            "As Dwayne's already lowering me down onto it!"
            "I try to keep looking at the head as I get ever closer."
            show dwayne stand eyes_closed
            "But in the end I find myself closing my eyes before it happens."
            "And as I feel the very tip touching me down there, I squeeze them tightly closed."
            "Of course Dawyne can't see any of this, and I doubt he's stop even if he could."
            show dwayne stand blush mouth_pleasure
            "All I feel is the pressure of the head pressing against the lips of my pussy below."
            "I can't claim to be anything but aroused by now."
            "Wanting to feel the sensation of him inside me."
            "And I know that things are getting slick down there thanks to the sensations I'm feeling."
            "All the same, some parts of my body don't seem to be in agreement with that."
            "My pussy in particular is intent upon putting up a token resistance."
            "The lips steadfastly refuse to part as Dwayne lowers me down and onto him."
            "But what's happening between us feels as inevitable and inescapable as gravity."
            show dwayne stand mouth_hurt vaginal
            "And slowly but surely, I can feel that resistance beginning to disappear."
            "I don't need to see it happen to know that my pussy's opening up to Dwayne."
            "I can feel him starting to creep into me, a fraction of an inch at a time."
            "Dwayne's sure to make things go slowly, and I'm grateful to him for it."
            "Part of me worries what all that cock going straight into me would feel like."
            "I don't know if I could actually handle it!"
            "This way I can feel everything that's going on down there."
            "Little by little I realise that my body's stretching and shifting."
            show dwayne stand down mouth_pleasure
            "And by some unbelievable adaptability, it's actually making room for him!"
            "Even so, I'm still grateful for the fact Dwayne's taking it slowly."
            "That way I feel like I can come to terms with it, to cope with his size and girth."
            show dwayne stand eyes_open -blush
            "And by the time he's totally filled me up, I'm starting to feel quietly confident."
            "This isn't so bad after all."
            show dwayne stand mouth_normal
            "In fact, it feels really good."
            "I'm sure that I can handle it."
            show dwayne stand eyes_surprised mouth_pleasure
            "But a moment later I feel Dwayne begin to actually move inside of me."
            "And in an instant, all of that former confidence vanishes."
            "Because now I'm totally at Dwayne's mercy."
            "And I get the impression he's not going to hold back."
            show dwayne stand mouth_hurt eyes_ahegao
            "All at once he's thrusting up from below, forcing his cock deep into me."
            "But at the same time, Dwayne pushes me down as well."
            "This means that one moment I'm sliding helplessly up and down his cock."
            "And the next I'm straining to contain him as he fills me once again."
            "I've never been with a guy that possessed this kind of strength either."
            "Dwayne's so big and powerful that he has no trouble tossing me around like a doll."
            "I'm not moving a muscle of my own accord as all of this is happening."
            "At least none of the ones that move the limbs attached to my body."
            "But the ones on the inside of it are another story altogether."
            "Those feel like they're getting the workout of a lifetime."
            show dwayne stand mouth_pleasure blush
            "And the pleasure that I'm feeling right now is almost too much to describe."
            "I reassure myself with the thought that I've held on this far."
            "If I can just ride it out to the end, I should be okay."
            dwayne.say "Get...ready...[hero.name]..."
            dwayne.say "I'm going to..."
            dwayne.say "Going to cum!"
            show dwayne stand mouth_hurt eyes_closed
            "Oh god!"
            "That changes everything!"
            call cum_reaction (dwayne, 'vaginal', sexperience_min) from _call_cum_reaction_235
            if _return == "vaginal_outside":
                bree.say "Dwayne..."
                bree.say "You have to...pull out..."
                bree.say "Right now!"
                "Luckily for me, Dwayne seems to hear me and act on my words."
                show dwayne stand up mouth_pleasure out openpussy
                pause 0.3
                show dwayne stand cum with vpunch
                $ dwayne.sub += 1
                "I feel myself being lifted up and his cock sliding out of me."
                "All the same I find myself hanging on for dear life."
                "Because the sensation is enough to push me over the edge."
                "I feel like I'm about to be thrown up and through the roof."
                "And when that happens, I'm grateful for how he's holding me up."
                "Because I know that my legs wouldn't be able to support me right now."
            else:
                if CONDOM:
                    "Since we remembered to use a condom, I'm perfectly safe."
                    "But all the same I find myself hanging on for dear life."
                else:
                    $ hero.morality -= 4
                    "I find myself hanging on for dear life."
                show dwayne stand up eyes_ahegao mouth_pleasure cum with vpunch
                $ dwayne.love += 2
                "Because when Dwayne really does lose it, things kick up a gear."
                with vpunch
                "I feel myself cumming almost as soon as he begins to."
                if CONDOM:
                    show dwayne stand eyes_closed mouth_ahegao out openpussy with vpunch
                else:
                    show dwayne stand eyes_closed mouth_ahegao out openpussy vaginaldrip with vpunch
                    $ dwayne.impregnate()
                "And when that happens, I'm grateful for how he's holding me up."
                "Because I know that my legs wouldn't be able to support me right now."
        "Wreck my rear" if hero.sexperience >= (sexperience_min + 5):
            "I can't think of anything other than having Dwayne inside of me right now."
            "And I know exactly where I want it too."
            show dwayne stand eyes_open mouth_normal
            $ hero.morality -= 2
            bree.say "My ass, Dwayne..."
            bree.say "I want it in my ass!"
            dwayne.say "Whatever you say, [hero.name]..."
            "I can't help yelping a second time as Dwayne leaps into action."
            "Dwayne's cock is right there, bobbing up and down."
            "From this angle it looks longer and thicker than I've ever seen it."
            "And I can't help wondering how the hell it's ever going to fit!"
            "But it looks like I'm going to find out for certain."
            "As Dwayne's already lowering me down onto it!"
            "I try to keep looking at the head as I get ever closer."
            show dwayne stand eyes_closed
            "But in the end I find myself closing my eyes before it happens."
            "And as I feel the very tip touching me down there, I squeeze them tightly closed."
            "Of course Dawyne can't see any of this, and I doubt he's stop even if he could."
            show dwayne stand blush mouth_pleasure
            "All I feel is the pressure of the head pressing against the opening of my ass below."
            "I can't claim to be anything but aroused by now."
            "Wanting to feel the sensation of him inside me."
            "And I know that things are getting slick down there thanks to the sensations I'm feeling."
            "All the same, some parts of my body don't seem to be in agreement with that."
            "My ass in particular is intent upon putting up a token resistance."
            "The muscles steadfastly refuse to part as Dwayne lowers me down and onto him."
            "But what's happening between us feels as inevitable and inescapable as gravity."
            show dwayne stand mouth_hurt anal
            "And slowly but surely, I can feel that resistance beginning to disappear."
            "I don't need to see it happen to know that my pussy's opening up to Dwayne."
            "I can feel him starting to creep into me, a fraction of an inch at a time."
            "Dwayne's sure to make things go slowly, and I'm grateful to him for it."
            "Part of me worries what all that cock going straight into me would feel like."
            "I don't know if I could actually handle it!"
            "This way I can feel everything that's going on down there."
            "Little by little I realise that my body's stretching and shifting."
            show dwayne stand down mouth_pleasure
            "And by some unbelievable adaptability, it's actually making room for him!"
            "Even so, I'm still grateful for the fact Dwayne's taking it slowly."
            "That way I feel like I can come to terms with it, to cope with his size and girth."
            show dwayne stand eyes_open -blush
            "And by the time he's totally filled me up, I'm starting to feel quietly confident."
            "This isn't so bad after all."
            "In fact, it feels really good."
            "I'm sure that I can handle it."
            show dwayne stand eyes_surprised mouth_pleasure
            "But a moment later I feel Dwayne begin to actually move inside of me."
            "And in an instant, all of that former confidence vanishes."
            "Because now I'm totally at Dwayne's mercy."
            "And I get the impression he's not going to hold back."
            show dwayne stand mouth_hurt eyes_ahegao
            "All at once he's thrusting up from below, forcing his cock deep into me."
            "But at the same time, Dwayne pushes me down as well."
            "This means that one moment I'm sliding helplessly up and down his cock."
            "And the next I'm straining to contain him as he fills me once again."
            "I've never been with a guy that possessed this kind of strength either."
            "Dwayne's so big and powerful that he has no trouble tossing me around like a doll."
            "I'm not moving a muscle of my own accord as all of this is happening."
            "At least none of the ones that move the limbs attached to my body."
            "But the ones on the inside of it are another story altogether."
            "Those feel like they're getting the workout of a lifetime."
            show dwayne stand mouth_pleasure blush
            "And the pleasure that I'm feeling right now is almost too much to describe."
            "I reassure myself with the thought that I've held on this far."
            "If I can just ride it out to the end, I should be okay."
            dwayne.say "Get...ready...[hero.name]..."
            dwayne.say "I'm going to..."
            dwayne.say "Going to cum!"
            show dwayne stand mouth_hurt eyes_closed
            "Oh god!"
            "That changes everything!"
            call cum_reaction (dwayne, 'anal', sexperience_min) from _call_cum_reaction_236
            if _return == "anal_outside":
                bree.say "Dwayne..."
                bree.say "I want you to...pull out..."
                bree.say "Right now!"
                "Luckily for me, Dwayne seems to hear me and act on my words."
                show dwayne stand up mouth_pleasure out
                pause 0.3
                show dwayne stand cum with vpunch
                $ dwayne.sub += 1
                "I feel myself being lifted up and his cock sliding out of me."
                "All the same I find myself hanging on for dear life."
                "Because the sensation is enough to push me over the edge."
                "I feel like I'm about to be thrown up and through the roof."
                "And when that happens, I'm grateful for how he's holding me up."
                "Because I know that my legs wouldn't be able to support me right now."
            else:
                "Since I chose to let him fuck my ass, I'm perfectly safe."
                "But all the same I find myself hanging on for dear life."
                show dwayne stand up eyes_ahegao mouth_pleasure cum with vpunch
                $ dwayne.love += 2
                "Because when Dwayne really does lose it, things kick up a gear."
                with vpunch
                "I feel myself cumming almost as soon as he begins to."
                show dwayne stand eyes_closed mouth_ahegao out with vpunch
                "And when that happens, I'm grateful for how he's holding me up."
                "Because I know that my legs wouldn't be able to support me right now."
    return

label dwayne_fuck_date_missionary(sexperience_min):
    bree.say "Okay, Dwayne..."
    bree.say "That's all very flattering."
    bree.say "But what kind of a performance are you going to put on for me tonight, huh?"
    show dwayne happy
    dwayne.say "You know, [hero.name]..."
    dwayne.say "Sometimes there's no beating a classic."
    show dwayne normal
    "As he says this, Dwayne reaches out and puts his hands on my shoulders."
    "Then he pushes be down and onto the mattress."
    "His touch is firm and yet gentle at the same time."
    scene dwayne missionary zorder 2
    show bg black zorder 1
    show dwayne missionary out zorder 2
    with fade
    "Not that I feel the need to resist him for a moment."
    "I have my arms stretched out on the bed, waiting to see what Dwayne does next."
    "But then I feel, rather than see him push his thighs under mine."
    "This raises the lower half of my body into the air."
    "And it also means that everything down there is well withing his reach."
    "Which Dwayne demonstrates a moment later by stroking his fingers between my thighs."
    show dwayne missionary blush
    bree.say "Ah..."
    bree.say "Oh..."
    bree.say "Mmm..."
    dwayne.say "So..."
    dwayne.say "What is the lady in the mood for tonight?"
    menu:
        "Guide him to my pussy":
            "Dwayne's doing a good job of getting me flustered right now."
            "But somehow I can still think straight enough to know what I want."
            if hero.morality <= -25:
                bree.say "Fuck my pussy, Dwayne..."
                bree.say "Fuck it real hard!"
            elif hero.morality >= 25:

                bree.say "Oh, Dwayne..."
                bree.say "Please use the front door..."
                bree.say "Not the back!"
            else:
                bree.say "Oh fuck..."
                bree.say "My pussy, Dwayne..."
                bree.say "That's where I want it!"

            "My pleas only seem to make Dwayne's smile grow larger."
            "And a quick glance shows me they're also making his cock larger still!"
            dwayne.say "Whatever the lady wants, the lady gets!"
            call check_condom_usage (dwayne) from _call_check_condom_usage_143
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show dwayne missionary condom
            dwayne.say "Okay, [hero.name]..."
            dwayne.say "I hope you're ready for this?"
            dwayne.say "Because I won't be holding anything back tonight!"
            "I can't help chuckling at Dwayne's macho little speech."
            "And I'm just about to say something in return."
            "But then I feel him shift under me."
            "And what follows cuts me off completely."
            "Sure, it's only the first sensation of Dwayne's cock against my pussy."
            "But it's so big and it's trying to push its way inside of me so hard."
            "I hear myself already gasping and panting, but only distantly."
            "Because the feeling of what's happening down there is overwhelming my other senses."
            "Dwayne doesn't stop after one attempt to get in there."
            "He instantly tries again and again, like a machine repeating a programmed task."
            "The first time, despite the sensations, my body holds firm and keeps him out."
            "But the same thing happens over and over again, and faster too."
            "Each time he erodes a little more of that resistance."
            "I start to lose count of the times that he's done it to me."
            show dwayne missionary vaginal up
            "And so when he finally makes a break-through, it comes as a genuine surprise."
            "The lips of my pussy part, just enough for the head of his cock to sink inside."
            "But obviously that's not going to satisfy Dwayne, not in the slightest."
            "As soon as he's in me, he redoubles his efforts."
            show dwayne missionary vaginal down hurt
            "The first thrust he makes after that pushes halfway into me."
            "And it also leaves me lying helplessly on my back too."
            show dwayne missionary poke hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke open
            "So when the next one totally fills me, I swear it stops me from moving even an inch."
            "Dwayne pauses for a moment, probably savouring the sensation of being all the way inside."
            "A thing that must feel like a victory for him, as it feels like total submission for me."
            "But of course he was never going to stop there either."
            "Now Dwayne's claimed his prize, he's going to make it his own."
            show dwayne missionary poke hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke open
            "And the first I feel of that is him beginning to move inside of me."
            "All of those huge, bulging muscles now come into play as he does so."
            "And I can soon feel that they're not just intended for showing-off."
            show dwayne missionary poke hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke open
            "Dwayne's body moves like some kind of well-oiled machine."
            show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke -speed up
            "And it works on me in the same manner, hammering me into complete surrender."
            show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke -speed up
            "I can't remember the last time I was taken like this, with such confident force."
            "But at the same time he never once hurts me or goes too far."
            show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke -speed up
            "It's like he instinctively knows just how much I can take."
            "And he delivers it to the exact places it's needed too."
            show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke -speed up
            "Looking down at what he's doing, I can see my entire body moving."
            "But most of all I see my breasts bouncing up and down like crazy."
            show dwayne missionary poke speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke -speed up
            "Every thrust Dwayne makes sends them jiggling in sympathy."
            "I have no idea how long he can keep this up."
            show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -poke -speed
            "But I do know that I won't be able to hold on for more than few moments."
            bree.say "D..."
            show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.1
            show dwayne missionary -poke -speed
            bree.say "Dwayne..."
            show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.1
            show dwayne missionary -poke -speed
            bree.say "I'm...I'm gonna cum!"
            show dwayne missionary poke open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.1
            show dwayne missionary -poke -speed
            call cum_reaction (dwayne, 'vaginal', sexperience_min) from _call_cum_reaction_271
            if _return == "vaginal_outside":
                bree.say "Don't it, Dwayne..."
                bree.say "Do it now..."
                bree.say "Pull out!"
                show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -poke -speed
                "I say the words for the sake of making my desires plain."
                "And for a moment I think that Dwayne's going to ignore me."
                show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -poke -speed
                "Because he keeps right on pounding away until the very last moment."
                show dwayne missionary out ahegao at stepback(speed=0.1, h=-20, v=0)
                "But then he pulls out of me, making me gasp at the sensation."
                with hpunch
                "My head falls back onto the mattress, and the room spins around me."
                show dwayne missionary cum with hpunch
                "And I can only vaguely feel Dwayne's cum as it spatters onto my belly."
            else:
                bree.say "Don't do it..."
                bree.say "Don't pull out!"
                show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -poke -speed
                "I say the words for the sake of making my desires plain."
                "But I hardly think that Dwayne needs any encouragement."
                show dwayne missionary poke ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -poke -speed
                "Because he keeps right on pounding away until the very last moment."
                show dwayne missionary cum with hpunch
                "Then he shoots his load into me, and it feels like a cannon shot going off."
                with hpunch
                "My head falls back onto the mattress, and the room spins around me."
        "Guide him to my ass":

            "Dwayne's doing a good job of getting me flustered right now."
            "But somehow I can still think straight enough to know what I want."
            if hero.morality <= -25:
                bree.say "Fuck my ass, Dwayne..."
                bree.say "Fuck it real hard!"
            elif hero.morality >= 25:
                bree.say "Oh, Dwayne..."
                bree.say "Please use the back door..."
                bree.say "I want to be naughty!"
            else:
                bree.say "Oh fuck..."
                bree.say "My ass, Dwayne..."
                bree.say "That's where I want it!"
            "My pleas only seem to make Dwayne's smile grow larger."
            "And a quick glance shows me they're also making his cock larger still!"
            dwayne.say "Whatever the lady wants, the lady gets!"
            dwayne.say "Okay, [hero.name]..."
            dwayne.say "I hope you're ready for this?"
            dwayne.say "Because I won't be holding anything back tonight!"
            "I can't help chuckling at Dwayne's macho little speech."
            "And I'm just about to say something in return."
            "But then I feel him shift under me."
            "And what follows cuts me off completely."
            "Sure, it's only the first sensation of Dwayne's cock between my buttocks."
            "But it's so big and it's trying to push its way inside of me so hard."
            "I hear myself already gasping and panting, but only distantly."
            "Because the feeling of what's happening down there is overwhelming my other senses."
            "Dwayne doesn't stop after one attempt to get in there."
            "He instantly tries again and again, like a machine repeating a programmed task."
            "The first time, despite the sensations, my body holds firm and keeps him out."
            "But the same thing happens over and over again, and faster too."
            "Each time he erodes a little more of that resistance."
            "I start to lose count of the times that he's done it to me."
            show dwayne missionary anal up
            "And so when he finally makes a break-through, it comes as a genuine surprise."
            "The muscles of my ass weaken, just enough for the head of his cock to sink inside."
            "But obviously that's not going to satisfy Dwayne, not in the slightest."
            "As soon as he's in me, he redoubles his efforts."
            show dwayne missionary anal down hurt
            "The first thrust he makes after that pushes halfway into me."
            "And it also leaves me lying helplessly on my back too."
            show dwayne missionary hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary open
            "So when the next one totally fills me, I swear it stops me from moving even an inch."
            "Dwayne pauses for a moment, probably savouring the sensation of being all the way inside."
            "A thing that must feel like a victory for him, as it feels like total submission for me."
            "But of course he was never going to stop there either."
            "Now Dwayne's claimed his prize, he's going to make it his own."
            show dwayne missionary hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary open
            "And the first I feel of that is him beginning to move inside of me."
            "All of those huge, bulging muscles now come into play as he does so."
            "And I can soon feel that they're not just intended for showing-off."
            show dwayne missionary hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary open
            "Dwayne's body moves like some kind of well-oiled machine."
            show dwayne missionary hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary open
            "And it works on me in the same manner, hammering me into complete surrender."
            show dwayne missionary speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary open -speed up
            "I can't remember the last time I was taken like this, with such confident force."
            "But at the same time he never once hurts me or goes too far."
            show dwayne missionary speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary open -speed up
            "It's like he instinctively knows just how much I can take."
            "And he delivers it to the exact places it's needed too."
            show dwayne missionary speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -speed up
            "Looking down at what he's doing, I can see my entire body moving."
            "But most of all I see my breasts bouncing up and down like crazy."
            show dwayne missionary speed hurt at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -speed up
            "Every thrust Dwayne makes sends them jiggling in sympathy."
            "I have no idea how long he can keep this up."
            show dwayne missionary open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.2
            show dwayne missionary -speed
            "But I do know that I won't be able to hold on for more than few moments."
            bree.say "D..."
            show dwayne missionary open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.1
            show dwayne missionary -speed
            bree.say "Dwayne..."
            show dwayne missionary open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.1
            show dwayne missionary -speed
            bree.say "I'm...I'm gonna cum!"
            show dwayne missionary open down speed at stepback(speed=0.1, h=-20, v=0)
            pause 0.1
            show dwayne missionary -speed
            call cum_reaction (dwayne, 'anal', sexperience_min) from _call_cum_reaction_272
            if _return == "anal_outside":
                bree.say "Don't it, Dwayne..."
                bree.say "Do it now..."
                bree.say "Pull out!"
                show dwayne missionary ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -speed
                "I say the words for the sake of making my desires plain."
                "And for a moment I think that Dwayne's going to ignore me."
                show dwayne missionary ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -speed
                "Because he keeps right on pounding away until the very last moment."
                show dwayne missionary out ahegao at stepback(speed=0.1, h=-20, v=0)
                "But then he pulls out of me, making me gasp at the sensation."
                with hpunch
                "My head falls back onto the mattress, and the room spins around me."
                show dwayne missionary cum with hpunch
                "And I can only vaguely feel Dwayne's cum as it spatters onto my belly."
            else:
                bree.say "Don't do it..."
                bree.say "Don't pull out!"
                show dwayne missionary ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -speed
                "I say the words for the sake of making my desires plain."
                "But I hardly think that Dwayne needs any encouragement."
                show dwayne missionary ahegao speed at stepback(speed=0.1, h=-20, v=0)
                pause 0.1
                show dwayne missionary -speed
                "Because he keeps right on pounding away until the very last moment."
                show dwayne missionary cum with hpunch
                "Then he shoots his load into me, and it feels like a cannon shot going off."
                with hpunch
                "My head falls back onto the mattress, and the room spins around me."












    return

label dwayne_fuck_date_ceo_female:
    scene bg ceo
    "The view from the windows really is pretty impressive and totally worth it."
    "Which is why I find myself standing there, hands pressed against the glass."
    "All while I enjoy seeing what feels like the whole of the city spread out before me."
    dwayne.say "So, [hero.name]..."
    dwayne.say "What do you think of the view?"
    "I don't turn to face Dwayne as he asks the question."
    "Instead I keep on looking out of the window."
    "But I make a point of nodding my head and answering him all the same."
    bree.say "It's amazing!"
    bree.say "I don't know how you get any work done in here."
    bree.say "I'd be staring at this all day long."
    "Dwayne lets out one of his typically deep, loud and booming laughs."
    dwayne.say "Ha, ha..."
    dwayne.say "Everyone that comes in here says that."
    dwayne.say "But they're not talking about the view out of the window."
    "I can hear Dwayne's voice getting closer as he says all of this."
    "And I figure that means he's walking across the office towards me."
    show dwayne at center, zoomAt (1.65, (640, 1140)) with dissolve
    "I turn around just in time to see that he's now standing behind me."
    "And with his height, that also means he's towering over me too!"
    bree.say "Oh..."
    bree.say "There's another view in here?"
    bree.say "Where is that?"
    show dwayne smile
    "Dwayne's lips part to reveal his almost too perfect white teeth."
    "And it takes me a moment to realise that he's actually smiling."
    "Then he kind of strikes a pose and points his thumbs at his own chest."
    show dwayne happy
    dwayne.say "Isn't it obvious, [hero.name]?"
    dwayne.say "You're looking right at it!"
    show dwayne smile
    "I think that Dwayne was expecting me to be blown away."
    "Either that or totally offended by his flaunting himself."
    "But I definitely don't think he was prepared for me to laugh at him."
    bree.say "Oh, Dwayne..."
    bree.say "That's so cheesy!"
    show dwayne annoyed
    dwayne.say "What do you mean it's cheesy?!?"
    dwayne.say "No...wait..."
    show dwayne happy
    dwayne.say "I read once that humour can be a way of dealing with things."
    dwayne.say "So you're obviously using it to handle the awesome sight of yours truly!"
    dwayne.say "I mean, will you look at this work of art..."
    show dwayne smile
    "Dwayne starts to unbutton his shirt as he says all of this."
    "And at first I just keep right on laughing at him."
    "But as each successive button is popped open, more of his chest is revealed."
    "Sure, Dwayne might be a swaggering corporate type that's way too full of himself."
    "But even I can't deny the fact that he's got a god-level bod!"
    "I can feel my eyes getting wider with each second that passes."
    "And even worse, Dwayne can see it too."
    show dwayne smile swimsuit with dissolve
    dwayne.say "Ah..."
    dwayne.say "Now you get it, don't you?"
    dwayne.say "Now you see why this is the view everyone wants to see!"
    "I can't help reaching up and putting my hands all over Dwayne."
    "Suddenly I'm running them over his huge, rock-hard muscles."
    "Hell, I even help to push the shirt off of his wide shoulders too!"
    "As all of this is happening, I hardly notice what Dwayne's doing to me."
    "So it comes as some surprise a moment later."
    "When I feel his hands on my naked skin."
    "Looking down, I see that Dwayne's been undressing me too."
    "And the fact that I don't object tells me that we're already into something here."
    "That something's started between us and it's too late to back out now."
    "Not that I want to back out - quite the opposite."
    "I can already feel myself warming to the idea of having some fun."
    "And when Dwayne's shorts come down, the sight I'm presented with seals it for me."
    dwayne.say "Oh yeah, [hero.name]..."
    dwayne.say "That's an impressive feature too!"
    "I can't help myself as I reach out and begin to stroke Dwayne's cock."
    "It's big, impressive and bold, just like he is."
    "And the mere sight of it makes me want the thing inside of me!"
    bree.say "Mmm..."
    bree.say "Is it a feature I get to try out for myself?"
    show dwayne happy
    dwayne.say "Of course it is."
    dwayne.say "But most takers use it while they take in the view."
    dwayne.say "Here, let me show you..."
    hide dwayne
    show dwayne stand ceo mouth_pleasure
    with fade
    "We're both naked by now."
    "So there's nothing to keep us apart for a second longer."
    "Dwayne wraps his arms around me, literally sweeping me off the ground."
    "He does it so quickly that I can't help letting out a yelp of surprise."
    bree.say "Argh!"
    menu:
        "Please my pussy":
            "I can tell that Dwayne's trying to scoop me up into his arms."
            "And it's a no-brainer where that's going to lead next."
            "I find myself being turned around in his grasp."
            "His hands pass under my thighs, and then he turns me to face the window."
            "Dwayne's got my back to his belly, my legs spreads apart too."
            "And right now I should be looking out of the window."
            "I should be taking in the vista of the city spread out before me."
            "But instead I'm staring down at the head of his cock."
            "And that's because I'm being lowered towards it!"
            "I only have time to say one thing before I reach it."
            "So I'd better make it count!"
            show dwayne stand mouth_normal
            bree.say "My pussy, Dwayne..."
            bree.say "Please, put it in my pussy!"
            bree.say "It looks way too big for my ass!"
            "Dwayne chuckles at this."
            "But he doesn't stop lowering me towards it."
            dwayne.say "Whatever you want, [hero.name]."
            dwayne.say "You'd better hold on tight now."
            dwayne.say "Because we're about to get started!"
            "I think that I try to say something more."
            "But I can't really be sure of that."
            "I could have just been making a random noise."
            "Because a moment later it becomes impossible for me to speak anyway."
            show dwayne stand vaginal eyes_surprised mouth_pleasure
            "As soon as the head of Dwayne's cock touches the lips of my pussy, it's hopeless."
            "All I can do is pant and sigh as sensations of anticipated pleasure pulse through me."
            "From my point of view, it looks almost ridiculously massive."
            "And I'm almost convinced that there's no way it can ever fit."
            "My body seems to have the same concerns as me too."
            show dwayne stand down eyes_closed mouth_hurt at startle(0.05, -10)
            "Because as Dwayne starts to move me up and down, it stoically resists his efforts."
            "But that doesn't faze him for a moment."
            "Instead Dwayne begins to move me in a certain manner."
            show dwayne stand up eyes_open
            "One that draws the head of his cock over my exposed lips."
            "I go up and down while it traces a line in the opposite direction."
            "And all the time this is happening, I can feel myself getting ever more aroused."
            "Soon any hint of friction is gone, as my pussy gets wetter."
            show dwayne stand eyes_closed mouth_pleasure
            "I find myself opening my mouth a little, just to gasp."
            "And at almost the same time, the lips down there seem to move in sympathy too."
            "That's all it takes, one small hint of relaxation, of resistance lessening."
            "Somehow the head of Dwayne's cock subtly changes angle."
            show dwayne stand down eyes_surprised mouth_hurt at startle(0.05, -10)
            "And the next time he pulls me downwards, it juts a little way inside."
            "It can't have gone more than a fraction of an inch into me."
            "Yet I feel it like a sea-change in the sensations I'm experiencing."
            show dwayne stand up eyes_ahegao mouth_ahegao
            "And from that moment on, I'm helpless, totally at his mercy."
            "Dwayne doesn't retreat this time."
            "Instead he pulls me down harder still, driving his cock a full inch or more inside."
            "My mouth opens as I cry out in silence, feeling myself stretching to accommodate him."
            show dwayne stand down eyes_closed at startle(0.05, -10)
            "Dwayne doesn't stop until he's all the way inside now."
            "Making me slide down the entire length of the shaft."
            "Then he leaves me there for an agonising moment."
            "And I mean agonising because of the intensity of it all."
            "There's no hint of pain."
            "But then this pleasure is more overwhelming than any pain I can recall."
            "I don't know how there can be more to feel than this."
            show dwayne stand up
            "But then Dwayne starts to move inside of me, and I know how wrong I was."
            "I'm not moving a muscle myself, at least not voluntarily."
            show dwayne stand down eyes_ahegao mouth_pleasure at startle(0.05, -10)
            "It's Dwayne that's holding me up and causing me to go up and down."
            "All I can do is wrestle with the sensations I'm feeling as he does so."
            show dwayne stand up eyes_closed
            "I can feel every inch of his cock as it moves inside me."
            "And I swear that I couldn't know the thing better if I held it in my hand."
            show dwayne stand down at startle(0.05, -10)
            "Every ridge, line and tiny imperfection seems to become familiar to me."
            "In fact, it feels like I'm being moulded to the shape of his cock down there."
            show dwayne stand up
            "Like once he's pulled it out of me, things will stay like that forever!"
            "Dwayne doesn't hold back either."
            "He seems to be going at it like he has something to prove to himself."
            "And I say that because he's got nothing left to prove to me."
            "I can't hold on for another second."
            show dwayne stand down eyes_ahegao mouth_hurt at startle(0.05, -10)
            bree.say "D...Dwayne..."
            bree.say "I'm...gonna..."
            bree.say "I'm gonna...cum!"
            "My admission seems to serve as a victory for Dwayne."
            "As I can feel him starting to twitch and jerk too."
            "All of which makes me believe that he's about to cum."
            show dwayne stand up
            "And that he's been holding on for me to go first."
            menu:
                "Cum in meeee!!!":
                    "When it happens, there's nothing I can do to save myself."
                    $ dwayne.love += 4
                    show dwayne stand down mouth_ahegao cum with vpunch
                    "Dwayne shoots his load like a bomb going off inside of me."
                    with vpunch
                    "And the sensation instantly makes me cum for a second time."
                    with vpunch
                    "I'm still twitching and babbling to myself afterwards."
                    show dwayne stand up eyes_closed out
                    "When he puts me down on the couch in the corner so that I can come back to my senses."
                "Wait! Pull out!":
                    show dwayne stand eyes_surprised
                    "I'm kind of scared to have Dwayne lose it inside of me."
                    "Like it'll blow my head off, or something stupid like that."
                    show dwayne stand up
                    "So I hurry to work myself off his cock before it's too late."
                    show dwayne stand out out
                    "But when it happens, the sensation is almost too much."
                    show dwayne stand eyes_ahegao
                    "And it instantly makes me cum for a second time."
                    $ dwayne.sub += 1
                    show dwayne stand cum with vpunch
                    "Dwayne shoots his load, but I hardly notice."
                    with vpunch
                    "I'm still twitching and babbling to myself afterwards."
                    show dwayne stand down eyes_closed
                    "When he puts me down on the couch in the corner so that I can come back to my senses."
        "Treat my ass":
            "I can tell that Dwayne's trying to scoop me up into his arms."
            "And it's a no-brainer where that's going to lead next."
            "I find myself being turned around in his grasp."
            "His hands pass under my thighs, and then he turns me to face the window."
            "Dwayne's got my back to his belly, my legs spreads apart too."
            "And right now I should be looking out of the window."
            "I should be taking in the vista of the city spread out before me."
            "But instead I'm staring down at the head of his cock."
            "And that's because I'm being lowered towards it!"
            "I only have time to say one thing before I reach it."
            "So I'd better make it count!"
            show dwayne stand mouth_normal
            bree.say "My ass, Dwayne..."
            bree.say "Please, put it in my ass!"
            bree.say "It looks way too big for my pussy!"
            "Dwayne chuckles at this."
            "But he doesn't stop lowering me towards it."
            dwayne.say "Whatever you want, [hero.name]."
            dwayne.say "You'd better hold on tight now."
            dwayne.say "Because we're about to get started!"
            "I think that I try to say something more."
            "But I can't really be sure of that."
            "I could have just been making a random noise."
            "Because a moment later it becomes impossible for me to speak anyway."
            show dwayne stand anal eyes_surprised mouth_pleasure
            "As soon as the head of Dwayne's cock touches the ring of my ass, it's hopeless."
            "All I can do is pant and sigh as sensations of anticipated pleasure pulse through me."
            "From my point of view, it looks almost ridiculously massive."
            "And I'm almost convinced that there's no way it can ever fit."
            "My body seems to have the same concerns as me too."
            show dwayne stand down eyes_closed mouth_hurt at startle(0.05, -10)
            "Because as Dwayne starts to move me up and down, it stoically resists his efforts."
            "But that doesn't faze him for a moment."
            "Instead Dwayne begins to move me in a certain manner."
            show dwayne stand up eyes_open
            "One that draws the head of his cock around my hole."
            "I go up and down while it traces a line in the opposite direction."
            "And all the time this is happening, I can feel myself getting ever more aroused."
            "Soon any hint of friction is gone, as my ass begins to relax."
            "I find myself opening my mouth a little, just to gasp."
            show dwayne stand eyes_closed mouth_pleasure
            "And at almost the same time, the muscles down there seem to move in sympathy too."
            "That's all it takes, one small hint of relaxation, of resistance lessening."
            "Somehow the head of Dwayne's cock subtly changes angle."
            show dwayne stand down eyes_surprised mouth_hurt at startle(0.05, -10)
            "And the next time he pulls me downwards, it juts a little way inside."
            "It can't have gone more than a fraction of an inch into me."
            "Yet I feel it like a sea-change in the sensations I'm experiencing."
            show dwayne stand up eyes_ahegao mouth_ahegao
            "And from that moment on, I'm helpless, totally at his mercy."
            "Dwayne doesn't retreat this time."
            "Instead he pulls me down harder still, driving his cock a full inch or more inside."
            "My mouth opens as I cry out in silence, feeling myself stretching to accommodate him."
            show dwayne stand down eyes_closed at startle(0.05, -10)
            "Dwayne doesn't stop until he's all the way inside now."
            "Making me slide down the entire length of the shaft."
            "Then he leaves me there for an agonising moment."
            "And I mean agonising because of the intensity of it all."
            "There's no hint of pain."
            "But then this pleasure is more overwhelming than any pain I can recall."
            "I don't know how there can be more to feel than this."
            show dwayne stand up
            "But then Dwayne starts to move inside of me, and I know how wrong I was."
            "I'm not moving a muscle myself, at least not voluntarily."
            show dwayne stand down eyes_ahegao mouth_pleasure at startle(0.05, -10)
            "It's Dwayne that's holding me up and causing me to go up and down."
            "All I can do is wrestle with the sensations I'm feeling as he does so."
            show dwayne stand up eyes_closed
            "I can feel every inch of his cock as it moves inside me."
            "And I swear that I couldn't know the thing better if I held it in my hand."
            show dwayne stand down at startle(0.05, -10)
            "Every ridge, line and tiny imperfection seems to become familiar to me."
            "In fact, it feels like I'm being moulded to the shape of his cock down there."
            show dwayne stand up
            "Like once he's pulled it out of me, things will stay like that forever!"
            "Dwayne doesn't hold back either."
            "He seems to be going at it like he has something to prove to himself."
            "And I say that because he's got nothing left to prove to me."
            "I can't hold on for another second."
            show dwayne stand down eyes_ahegao mouth_hurt
            bree.say "D...Dwayne..."
            bree.say "I'm...gonna..."
            bree.say "I'm gonna...cum!"
            "My admission seems to serve as a victory for Dwayne."
            "As I can feel him starting to twitch and jerk too."
            "All of which makes me believe that he's about to cum."
            "And that he's been holding on for me to go first."
            menu:
                "Cum in meeee!!!":
                    "When it happens, there's nothing I can do to save myself."
                    $ dwayne.love += 2
                    show dwayne stand down mouth_ahegao cum with vpunch
                    "Dwayne shoots his load like a bomb going off inside of me."
                    with vpunch
                    "And the sensation instantly makes me cum for a second time."
                    with vpunch
                    "I'm still twitching and babbling to myself afterwards."
                    show dwayne stand up eyes_closed out
                    "When he puts me down on the couch in the corner so that I can come back to my senses."
                "Wait! Pull out!":
                    show dwayne stand eyes_surprised
                    "I'm kind of scared to have Dwayne lose it inside of me."
                    "Like it'll blow my head off, or something stupid like that."
                    show dwayne stand up
                    "So I hurry to work myself off his cock before it's too late."
                    show dwayne stand out out
                    "But when it happens, the sensation is almost too much."
                    show dwayne stand eyes_ahegao
                    "And it instantly makes me cum for a second time."
                    $ dwayne.sub += 2
                    show dwayne stand cum with vpunch
                    "Dwayne shoots his load over my belly, but I hardly notice."
                    with vpunch
                    "I'm still twitching and babbling to myself afterwards."
                    show dwayne stand down eyes_closed
                    "When he puts me down on the couch in the corner so that I can come back to my senses."
    return

label dwayne_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show dwayne naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Dwayne straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ dwayne.love -= 1
                $ dwayne.sub += 1
                call sleep from _call_sleep_105
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ dwayne.love += 1
                call sleep ("dwayne") from _call_sleep_106
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
