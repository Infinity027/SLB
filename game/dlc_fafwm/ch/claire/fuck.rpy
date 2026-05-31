init python:
    InteractActivity(**{
    "name": "fuck_claire",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(claire,
            IsActive(),
            MinStat("love", 100),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "claire_hottub_sex_male",
    "label": "claire_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(claire,
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


label claire_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    play sound door_knock
    "I'm still in the middle of running around the house trying to tidy up the place when I hear a knock at the door."
    "And the very next second I drop what I'm doing and hurry into the hallway to answer it, sure I know who's there."
    mike.say "Coming..."
    mike.say "I'm coming!"
    mike.say "Wait a second, okay?"
    "I know that there's no chance of anyone else getting to the door and answering it before me."
    "Because I've gone to great pains to make sure that everyone else is out and won't be home for a while."
    "Begging, cajoling and even offering bribes to make sure that I have the place to myself for as long as I need it."
    "Well, not exactly all to myself - more so that I can be alone with the person on the other side of the door."
    play sound door_open
    scene bg house
    show claire
    with fade
    mike.say "Hi, Claire!"
    "The words are out of my mouth even before I've got the door fully open."
    "But much to my relief, I see that it really is Claire standing out on the porch."
    show claire talkative
    claire.say "Oh, hello, [hero.name]…"
    claire.say "Did I hear you talking to someone just now?"
    claire.say "Because I thought that you said we had your house to ourselves?"
    show claire normal
    mike.say "Oh no, that was me trying to talk to you..."
    mike.say "You know, through the door?"
    mike.say "Although I should have known you wouldn't hear me..."
    mike.say "So I don't know why I was doing that."
    "By now Claire's looking at me with one of those bland smiles on her face."
    "The kind people give you when they have no idea what you're going on about."
    "But at the same time they're doing their level best to be nice and not say so."
    mike.say "Sorry, Claire..."
    mike.say "I've just been so looking forward to having you over, you know?"
    mike.say "I guess it's made me a little nervous."
    "Claire's smile changes to one that's far more bright and breezy."
    "And she makes a dismissive gesture with her hand as she steps into the hallway."
    play sound door_close
    scene bg livingroom with fade
    show claire talkative with easeinleft
    claire.say "I know exactly what you mean, really I do."
    claire.say "It's been so long since I did something like this."
    claire.say "I'd almost forgotten what it was like to be excited to see someone!"
    show claire normal
    "I'm nodding and doing the best I can to look like I get what Claire's saying."
    "But inside I'm practically turning cartwheels, because she's excited to see me!"
    "I nod for Claire to follow me, leading the way through the house."
    mike.say "The hot-tub's this way, just on he patio out back."
    mike.say "Sorry about the state of the place, Claire..."
    mike.say "My housemates are a proper couple of pigs!"
    "Claire chuckles and shakes her head."
    show claire talkative
    claire.say "Oh, I know how messy girls can be!"
    claire.say "And it's so unfair they left you to clean up their mess too."
    claire.say "Now if it were me, I'd have this place spick and span in no time."
    show claire normal
    mike.say "Oh, I couldn't let you do that, Claire..."
    mike.say "Not when you're my guest."
    show claire talkative
    claire.say "Don't be silly, [hero.name]!"
    claire.say "It would be my pleasure to show you true domestic bliss."
    claire.say "And once you've tasted it, I guarantee you'll never look back!"
    show claire normal
    "I do my best to keep on shaking my head and laughing at Claire's promises."
    "But just the thought of her bustling around the place in an apron is affecting me."
    "So much so that I can already feel my cock getting hard as I picture her bending down in the kitchen."
    "Or, come to think of it, in any room of the house!"
    scene bg pool at center, zoomAt(1.2, (640, 820))
    with fade
    claire.say "Ooh..."
    show claire surprised at center, zoomAt(1.4, (640, 920)) with easeinleft
    claire.say "You really did all of this for me?"
    show claire stuned
    "Claire looks gobsmacked as we walk out on to the patio and she sees the hot-tub for the first time."
    "And I mean sure, I did go to the trouble of lighting some candles and opening a bottle of wine."
    "But it's not like I rented her a health spa for the day or flew her to a private tropical island."
    show claire normal
    mike.say "Of course I did, Claire..."
    mike.say "I just wish I could have done more."
    "Claire turns on her heel to face me, putting a finger to my lips."
    show claire talkative
    claire.say "No, [hero.name], don't apologise."
    claire.say "This is just perfect, and it makes me feel so special."
    show claire normal
    "I nod and Claire's good enough to remove her finger."
    "And that's when I realise that I'm already in my swimming trunks, and she's fully clothed."
    mike.say "Oh..."
    mike.say "The water's just about at the right temperature."
    mike.say "So if you want to go and get changed, there's a bathroom just off the hallway."
    "Claire's stepping out of her shoes as I say all of this."
    "But she seems to be more than a little amused by my words."
    "Which is weird, as I assume she's not going to jump into the tub with her clothes on."
    show claire talkative
    claire.say "No need for that!"
    show claire c normal
    "Claire says this as she reaches up and tugs at a part of her dress."
    "And it's only now that I see it looks like a knot of some kind."
    show claire a swimsuit
    "So when she undoes it, the whole thing just drops away."
    "Seriously, it's just one of those wrap-around kind of dresses."
    "But to my smitten eyes, it looks like some kind of awesome magic trick."
    "Because suddenly Claire's naked, right in front of my eyes!"
    "Well...not totally naked...she has a bikini on underneath."
    "It's just that now the exquisite curves of her body are on show."
    "And I'm totally spellbound by the sight of them."
    mike.say "WOW..." with hpunch
    show bg pool at center, traveling(1.2, 1, (640, 720))
    show claire at center, traveling(1.4, 1, (640, 720))
    pause 2
    mike.say "Claire, you look incredible!"
    show bg pool at center, traveling(1.2, 1, (640, 820))
    show claire at center, traveling(1.4, 1, (640, 920))
    pause 2
    mike.say "Did you get that bikini just for today?"
    show claire conceited
    "Claire makes a point of rolling her eyes and shaking her head."
    "As if she's dismissing my compliments and questions as nothing at all."
    show claire evil blush
    "But there's no way she can hide the flush that's spreading over her cheeks."
    "And she's clearly loving the reaction that her swimming-costume is getting."
    "A reminder of the fact that she's usually so criminally starved of attention."
    show claire careless at startle(0.1, -5)
    claire.say "What?!?"
    claire.say "This old thing?"
    show claire startle
    claire.say "This is just something I threw on before I ran out of the door."
    claire.say "But I am glad that you approve - a girl does like to be noticed!"
    show claire wink
    show claire normal
    "Peeling off my top, I hold out a hand for Claire to take."
    show hottub claire swimsuit with fade
    "Then I step into the hot-tub with her, lowering myself slowly into the water."
    "We end up sitting just a little way apart, the level of the water around our waists."
    "And this strikes me as the perfect time to reach for the wine bottle and glasses."
    play sound wine_serving
    queue sound glass_wine
    "Claire nods eagerly as I fill the glasses then hand one to her."
    "Taking a sip and giggling like she can't believe this is actually happening to her."
    claire.say "Oh, [hero.name]…"
    claire.say "You're so naughty, spoiling me like this!"
    mike.say "Ah, now you're the one being silly, Claire."
    mike.say "A woman as beautiful as you and with such a great personality..."
    mike.say "Why, you should be getting this kind of treatment on a daily basis!"
    claire.say "Stop it [hero.name]…"
    claire.say "You're making me blush!"
    "Claire takes a hasty sip of wine and then another in quick succession."
    "And I can see that it's not exactly doing anything to help her blushing."
    claire.say "You know what, [hero.name]…"
    claire.say "Fuck it for all I care."
    claire.say "Don't ever stop it!"
    "Claire sounds more than a little breathless as she leans forwards."
    "Putting her glass down and reaching out for me with both hands."
    "I haven't drunk nearly as much of my own wine, but I still act on pure instinct."
    "Seeing Claire reach for me, I put my glass down too and return the favour."
    "In fact I seem to react more quickly than she can act."
    "Which means that I end up meeting Claire and pushing her backwards."
    "She parts her legs as I press her up against the edge of the tub."
    "And in the next second, we come together, lips meeting and mouths opening."
    "Fucking hell, I feel like I've been holding my breath, waiting for this very moment."
    "Because as soon as I have Claire in my arms and start kissing her, it's like breathing again."
    "I feel more alive than I have in ages, like I'm exactly where I need to be."
    "Totally lost in the experience of kissing Claire, I'm oblivious to everything else."
    "Which means I'm taken by surprise when she pulls down my trunks a moment later."
    "Breaking off the kiss with a ragged gasp, I just have time to see Claire's hand move."
    "And then I groan as she takes a firm hold on the shaft of my cock!"
    claire.say "Mmm…"
    claire.say "Is that for me, [hero.name]?"
    claire.say "Did I do that to you?"
    "It goes without saying that my cock is already pretty hard by now and standing to attention."
    "But as soon as Claire's handling it, the thing begins to grow bigger and harder still."
    "And she's really starting to squeeze it tightly now - not that it's a bad thing."
    mike.say "Y...yeah...yeah, you did."
    mike.say "Just the thought of you makes me hard, Claire..."
    mike.say "And actually being with you...that makes me crazy!"
    "I see what can only be desire flare in Claire's eyes as I describe my feelings for her."
    "And the next thing I know, she parts her legs and pulls me towards her, leaning back as she does so."
    "Of course the only problem with all of this is that Claire currently only has a hold of my cock."
    "So that's what takes all of the strain as she closes the distance between us!"
    mike.say "Argh..."
    mike.say "Claire..."
    mike.say "Go easy on me!"
    "Claire doesn't seem to even hear my pleas for her to be gentle."
    "She just pulls me between her open legs with the one hand."
    "And with the other she reaches down and pulls aside the gusset of her bikini bottoms."
    claire.say "Yes, [hero.name], yes..."
    claire.say "If I made you this hard, then I need to see it through."
    claire.say "I need you to stick that thing inside of me and put it to good use!"
    "Before I can even think of responding, Claire presses the head of my cock against the lips of her pussy."
    "And man, does it ever feel good!"
    "In that same moment, all of my resistance vanishes."
    "And now all I want to do is give Claire exactly what she wants."
    "Because it's the exact same thing that I want too!"
    menu:
        "Fuck her pussy":
            scene hottub sex male claire swimsuit with fade
            "Starting to move back and forth, I draw the tip of my cock up and down."
            "Making one slow pass of Claire's pussy each time that I do so."
            "I can see the effect that even something as small as this is having on her."
            "She's now relying totally on the side of the tub to support herself."
            "Almost floating in the shallow water as I lift her legs up from below."
            "And most importantly, she's offering no resistance whatsoever as I rub against her."
            "Claire's cheeks are more than flushed now, they're practically red and glowing."
            "But I can already feel that there's blood rushing to another part of her body too."
            "Because every second makes the sensation of her lips softer and more pliant."
            "Right up until the moment when we seem to pass some invisible point of no return."
            "Which is when all resistance simply vanishes, and Claire opens up to me like a flower."
            "I only wish that I could describe my part in what happens next as poetically."
            "And that's because the second I feel myself slipping into her, I seem to lose it."
            "The feeling is too much for me, the gratification overwhelming my senses."
            "All I can think to do is push ahead, literally driving myself all the way into her."
            "Claire moans with pleasure as I fill her in one rough thrust."
            "And once I'm there, I hold still and just enjoy the feeling of it."
            "Something that's made all the more intense by how Claire wriggles and writhes."
            "Totally unable to escape the position that I have her pinned down in."
            claire.say "Ah..."
            claire.say "Squeeze..."
            claire.say "Squeeze me!"
            "Claire's hand flies to her chest, tugging desperately at her bikini top."
            "And it doesn't take much to dislodge something of their size from such a flimsy prison either."
            "Soon enough, her generous breasts are swinging free on her chest, begging to be touched."
            "Without thinking, I reach out and grab hold of them with my own hands, one over each."
            "Then I start to do just as Claire demanded, squeezing and massaging them like warm dough."
            "Of course Claire doesn't stay still while all of this is happening to her."
            "Oh no, she moans and cries out more than ever, almost thrashing in the water."
            "And her base, animal response elicits the very same thing in me."
            "Soon enough I'm moving again, drawing myself back and then thrusting forwards for all I'm worth."
            "This means that I'm pounding away at Claire, fucking her without a hint of mercy."
            "But the thing is that she seems to love every second of it."
            "Her body soaks up everything that I have to give without protest."
            "And she seems to be nodding the whole time."
            "Though that could be more to do with being rocked back and forth..."
            "Soon enough I can feel Claire's legs pull together and her back arch."
            "She's about to lose it, and there's no way that I can hope to regain control."
            "Which means that when it happens, she takes me along with her!"
            call cum_reaction (claire, 'vaginal', 1) from _call_cum_reaction_324
            if _return == "vaginal_outside":
                "With Claire holding onto me so tightly, I only have one chance to make my move."
                show hottub sex male outside
                "So with one last step backwards, I pull myself all the way out of Claire."
                show hottub cumshot with vpunch
                $ claire.sub += 1
                "The motion her seconds after her own orgasm begins for real, instantly doubling the effect."
                with vpunch
                "Leaving her helpless as she floats in the water, head lolling on the edge of the tub."
            else:
                "With Claire holding onto me so tightly, there's really only one course of action I can take."
                show hottub cumshot with vpunch
                $ claire.love += 1
                "So with one last thrust forwards, I let go and shoot my load straight into Claire."
                with vpunch
                "It hits her seconds after her own orgasm begins for real, instantly doubling the effect."
                "Leaving her helpless as she floats in the water, head lolling on the edge of the tub."
        "Fuck her ass":
            scene hottub sex male claire swimsuit with fade
            "Well, maybe I want a slight variation on what Claire does."
            "Starting to move back and forth, I draw the tip of my cock up and down."
            "Pushing it a little further between Claire's buttocks each time that I do so."
            "And it doesn't take me long to feel it pressing at the edge of her hole."
            "I can see the effect that even something as small as this is having on her."
            "She's now relying totally on the side of the tub to support herself."
            "Almost floating in the shallow water as I lift her legs up from below."
            "And most importantly, she's offering no resistance whatsoever as I rub against her."
            "Claire's cheeks are more than flushed now, they're practically red and glowing."
            "But I can already feel that there's blood rushing to another part of her body too."
            "Because every second makes the sensation of her hole softer and more pliant."
            "Right up until the moment when we seem to pass some invisible point of no return."
            "Which is when all resistance simply vanishes, and Claire's ass opens up to me like a flower."
            "I only wish that I could describe my part in what happens next as poetically."
            "And that's because the second I feel myself slipping into her, I seem to lose it."
            "The feeling is too much for me, the gratification overwhelming my senses."
            "All I can think to do is push ahead, literally driving myself all the way into her."
            "Claire moans with pleasure as I fill her in one rough thrust."
            "And once I'm there, I hold still and just enjoy the feeling of it."
            "Something that's made all the more intense by how Claire wriggles and writhes."
            "Totally unable to escape the position that I have her pinned down in."
            claire.say "Ah..."
            claire.say "Squeeze..."
            claire.say "Squeeze me!"
            "Claire's hand flies to her chest, tugging desperately at her bikini top."
            "And it doesn't take much to dislodge something of their size from such a flimsy prison either."
            "Soon enough, her generous breasts are swinging free on her chest, begging to be touched."
            "Without thinking, I reach out and grab hold of them with my own hands, one over each."
            "Then I start to do just as Claire demanded, squeezing and massaging them like warm dough."
            "Of course Claire doesn't stay still while all of this is happening to her."
            "Oh no, she moans and cries out more than ever, almost thrashing in the water."
            "And her base, animal response elicits the very same thing in me."
            "Soon enough I'm moving again, drawing myself back and then thrusting forwards for all I'm worth."
            "This means that I'm pounding away at Claire, fucking her without a hint of mercy."
            "But the thing is that she seems to love every second of it."
            "Her body soaks up everything that I have to give without protest."
            "And she seems to be nodding the whole time."
            "Though that could be more to do with being rocked back and forth..."
            "Soon enough I can feel Claire's legs pull together and her back arch."
            "She's about to lose it, and there's no way that I can hope to regain control."
            "Which means that when it happens, she takes me along with her!"
            call cum_reaction (claire, 'anal', 1) from _call_cum_reaction_325
            if _return == "anal_outside":
                "With Claire holding onto me so tightly, I only have one chance to make my move."
                show hottub sex male outside
                "So with one last step backwards, I pull myself all the way out of Claire's ass."
                show hottub cumshot with vpunch
                $ claire.sub += 1
                "The motion her seconds after her own orgasm begins for real, instantly doubling the effect."
                with vpunch
                "Leaving her helpless as she floats in the water, head lolling on the edge of the tub."
            else:
                "With Claire holding onto me so tightly, there's really only one course of action I can take."
                show hottub cumshot with vpunch
                $ claire.love += 1
                "So with one last thrust forwards, I let go and shoot my load straight into Claire's ass."
                with vpunch
                "It hits her seconds after her own orgasm begins for real, instantly doubling the effect."
                "Leaving her helpless as she floats in the water, head lolling on the edge of the tub."
    "I sag back in the water, pushing myself backwards until I reach the edge of the tub."
    "And then I prop myself up against the side, letting it take all of my weight."
    claire.say "Oh..."
    claire.say "Oh yes..."
    claire.say "I really must come and visit you more often!"
    call stop_all_sfx from _call_stop_all_sfx_72
    show bg black with fade
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ claire.sexperience += 1
    $ game.active_date.clothes = None
    return


label claire_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show claire


    call claire_fuck_date_intro_male (location) from _call_claire_fuck_date_intro


    call claire_dick_reactions from _call_claire_dick_reactions


    call claire_fuck_date_foreplay_male from _call_claire_fuck_date_foreplay_male


    call claire_fuck_date_choices_male from _call_claire_fuck_date_choices_male


    call handle_npc_leaving (claire, _return) from _call_handle_npc_leaving_31
    if _return:
        return


    hide claire
    call claire_fuck_date_sleep (location="hero") from _call_claire_fuck_date_sleep
    return

label claire_fuck_date_intro_male(location="hero"):
    if claire.sexperience == 0:
        scene bg house
        show claire at center, zoomAt(1.25, (640, 880))
        with fade
        "I'm feeling on a high as Claire and I arrive back at my place."
        "The date that we've just been on went really well."
        "Or at least I think it did."
        "And Claire's not giving me any signals that would suggest it didn't."
        scene bg door entrance at center, zoomAt(1.25, (640, 880)) with fade
        "But it's as we're hurrying up the path towards the front door that I realise something."
        "Now I have to make it from the door all the way to my bedroom without anything going wrong."
        mike.say "Erm..."
        mike.say "Okay, Claire..."
        mike.say "Once we're inside, we make a dash for my room, okay?"
        "I'm fumbling with the lock as I say all of this."
        scene bg house
        show claire stuned at center, zoomAt(1.25, (640, 880))
        with fade
        "And I only manage to look back over my shoulder as the door swings open."
        "But when I do, I see that Claire's looking at me with a puzzled expression."
        show claire surprised
        if claire.sub >= 25:
            claire.say "But why, [hero.name]?"
            claire.say "Are you worried your housemates might see me?"
            claire.say "That I might embarrass you in front of them?"
        else:
            claire.say "But I already saw inside of your house, [hero.name]."
            show claire talkative
            claire.say "And yes, it did seem to be a little on the messy side..."
            claire.say "Which isn't something you need to be ashamed of."
        show claire normal
        "I can't help rubbing the back of my neck and grimacing as Claire steps inside."
        scene bg livingroom
        show claire at center, zoomAt(1.25, (640, 880))
        with fade
        "Then I hastily lock the door behind her, all the time trying to be as quiet as possible."
        mike.say "No, no, no..."
        mike.say "That's not it at all."
        mike.say "I just don't want my housemates to see you!"
        mike.say "Because I...I didn't tell them I'm dating an older woman yet."
        show claire happy
        "Claire smiles and shakes her head."
        show claire talkative
        if claire.sub >= 25:
            claire.say "That's okay, [hero.name]…"
            claire.say "I quite like the idea of being your little secret!"
        else:
            claire.say "Well, I'll do what I can to keep your secret, [hero.name]."
            claire.say "But you know what we cougars can be like in bed, don't you?"
            claire.say "Sometimes we just can't help making yowling sounds!"
        show claire normal
        "I kind of feel like Claire's playing with me right now."
        "Like she's enjoying the chance to make me sweat, rather than being annoyed."
        "And so I do the best I can to put a smile on my face and get into the same mood."
        mike.say "That's great, Claire..."
        mike.say "But let's hurry it up a little, yeah?"
        mike.say "My room's just down here."
        hide claire with easeoutleft
        "Claire lets me take her by the hand and lead the way to my bedroom door."
        scene bg bedroom1 with fade
        show claire normal at center, zoomAt(1.25, (640, 880)) with easeinright
        "And she seems pretty amused as I hastily open it and usher her inside too."
        "So much so that when I close it and turn around, she's actually giggling."
        mike.say "So..."
        mike.say "This is where the magic happens!"
        mike.say "Hey..."
        mike.say "What's so funny?"
        show claire talkative
        if claire.sub >= 25:
            claire.say "Oh, nothing at all."
            claire.say "I bet you've pulled all kinds of magic tricks in this room!"
        else:
            claire.say "Oh, I just knew you were going to say something like that!"
            claire.say "They always say that on the program where the famous people give tours of their houses."
            claire.say "You know, when they go into the bedroom?"
        show claire normal
        "I'm not sure exactly how to react to that."
        "And so I decide to show Claire around instead."
        "Which is precisely when I remember just how nerdy the décor in here must look."
        mike.say "Okay..."
        mike.say "So most of what you're seeing are collectibles..."
        show claire talkative
        claire.say "It's okay, [hero.name]…"
        claire.say "I kind of like that your room reminds me of a teenage boy's."
        claire.say "It makes me feel young and adventurous all over again!"
        show claire normal
        "As if her words weren't enough, Claire begins to peel off her top."
        "Like she's trying to show me just how adventurous she's feeling right now!"
        mike.say "Oh..."
        mike.say "Yeah..."
        mike.say "I can totally understand that."
        show claire naked with dissolve
        "Claire nods as she continues to strip-off in front of me, tossing her clothes aside."
        "And once she's done, I get the same treatment, being quickly stripped to my birthday suit!"
        claire.say "Mmm…"
        show claire talkative
        claire.say "Less talk, more action!"
        return
    else:
        scene bg house
        show claire at center, zoomAt(1.25, (640, 880))
        with fade
        "By now Claire's no stranger to my place, and she wastes no time as we arrive on my doorstep."
        "Almost as soon as I have the front-door open, she takes a firm hold of my hand and pulls me inside."
        "Hurrying down the hallway, she makes straight for my bedroom door and throws it open."
        scene bg bedroom1
        show claire at center, zoomAt(1.25, (640, 880))
        with fade
        "Then we rush inside, already beginning to pull off our clothes and toss them aside."
        "There's no need to stop along the way and exchange as much as a single word."
        show claire naked at center, zoomAt(1.35, (640, 960)) with fade
        "Because we both know why we're here and what's going to happen next."
        "It's only the finer details that still need to be thrashed out."
    $ game.room = "bedroom1"
    return

label claire_fuck_date_foreplay_male:
    menu:
        "Eat her pussy" if hero.sexperience >= 5:
            call claire_fuck_date_cunnilingus from _call_claire_fuck_date_cunnilingus
        "Suggest a blowjob" if claire.sub >= 10:
            call claire_fuck_date_blowjob from _call_claire_fuck_date_blowjob
        "Ask for a reverse 69" if hero.sexperience >= 15:
            call claire_fuck_date_reverse_sixty_nine from _call_claire_fuck_date_reverse_sixtynine
        "Fuck her right now":
            pass
    call stop_all_sfx from _call_stop_all_sfx_61

    return _return

label claire_fuck_date_choices_male:
    menu:
        "Missionary":
            call claire_fuck_date_missionary (0) from _call_claire_fuck_date_missionary
        "Doggy" if hero.sexperience >= 5:
            call claire_fuck_date_doggy (5) from _call_claire_fuck_date_doggy
        "Full Nelson" if hero.sexperience >= 10:
            call claire_fuck_date_fullnelson (10) from _call_claire_fuck_date_fullnelson
    call stop_all_sfx from _call_stop_all_sfx_62

    return _return

label claire_fuck_date_sleep(location="hero"):
    scene bg bedroom1
    if game.hour > 19 or game.hour < 6:
        show claire naked talkative at center, zoomAt(1.25, (640, 880))
        if claire.is_sex_slave:
            claire.say "May I share your bed tonight, Master?"
        else:
            claire.say "Mmm...you cool with me spending the night here?"
        show claire normal
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Claire frowns in disappointment, clearly trying to shrug off the sense of rejection."
                claire.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ claire.love -= 3
                call sleep from _call_sleep_128
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle claire
                "Claire curling up against me beneath the covers is almost as good as the sex - almost..."
                if claire.is_sex_slave:
                    claire.say "Sweet dreams, Master..."
                else:
                    claire.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Claire..."
                $ claire.love += 3
                call sleep ("claire") from _call_sleep_129
    return

label claire_fuck_date_blowjob:
    "Now that we're both naked, I can see Claire's eyes looking me up and down."
    "And that, combined with my desire for her, is really starting to turn me on."
    "So much so that my cock is already getting hard and beginning to rise."
    "Claire's eyebrows rise too as she notices what's happening down there."
    show claire talkative
    if claire.sub >= 25:
        claire.say "Oh, hello!"
        claire.say "Aren't you a big boy?"
    else:
        claire.say "Oh my!"
        claire.say "Am I really that exciting?"
    show claire normal
    "I can't help looking flustered as my body betrays my true feelings."
    "And I end up sitting down on the bed, as if that will help to hide it."
    mike.say "I..."
    mike.say "Well..."
    mike.say "The thing is, Claire..."
    mike.say "I always kind of had a fantasy about you..."
    mike.say "That involved your mouth...and my..."
    "without being able to help it, my eyes turn to where my cock is now fully erect."
    "Of course, Claire's gaze is drawn right along, so that she's looking at it too."
    "And I'm about to say more, when she seems to just straight-up read my mind."
    scene bg black
    show claire bj hurt down naked
    with fade
    "Because without another word, Claire kneels down and lowers her head."
    show claire bj closed happy
    "I watch with baited breath as her eyes close and her lips slowly part."
    "Is she?"
    "Oh my god, she is!"
    play sexsfx1 bj_openmouth
    show claire bj oral tongue
    "Gently and with care, Claire takes the head of my cock into her mouth."
    "Almost like she's kissing it at first, I feel her tongue wrap around the tip."
    "Claire lets out a moan of satisfaction as she opens her mouth wider."
    "And I can't help mimicking the sound as she takes it in deeper still."
    play sexsfx1 bj_sucking loop
    show claire bj up -tongue blowjob at startle(0.1, 10)
    "Taking her time and making every moment last, Claire moves her head up and down."
    show claire bj open at startle(0.1, 10)
    pause 0.2
    show claire bj at startle(0.1, 10)
    "Using lips, tongue and even her teeth, she renders me helpless, totally at her mercy."
    "I always imagined she'd be good at this kind of thing."
    "But I wasn't prepared for her to be a genuine expert!"
    show claire bj at startle(0.1, 10)
    pause 0.2
    show claire bj at startle(0.1, 10)
    "Because I seriously cannot remember the last time it felt this good."
    "By now it feels like my cock must actually be reaching down Claire's throat."
    show claire closed bj at startle(0.1, 10)
    pause 0.2
    show claire bj at startle(0.1, 10)
    "Almost every inch of it being worked on so that I'm frozen in place."
    "Then I feel the sensation of her fingers closing around my balls."
    "She squeezes them just so, knowing exactly how to work it."
    show claire bj open at startle(0.1, 10)
    pause 0.2
    show claire bj at startle(0.1, 10)
    "And the perfect combination of pain and pleasure only adds to the experience."
    "Part of me can't believe that Claire's literally making my fantasy a reality."
    "That this is all something that I've dreamed up and it'll prove to be an illusion."
    show claire bj pleasure at startle(0.1, 10)
    pause 0.2
    show claire bj at startle(0.1, 10)
    "But then the reality of the situation sinks in, as I feel myself begin to quiver."
    "And I know that I'm on the verge of losing it!"
    menu:
        "Cum on her face" if claire.sub >= 25:
            "And a massive part of that fantasy I just mentioned involves Claire taking it in the face!"
            play sexsfx1 slide_out
            show claire bj out with vpunch
            "So I make a move to pull back and slide myself out of her mouth before the inevitable happens."
            "Claire seems to realise what I'm doing in good time, as she pulls back and releases me too."
            play sexsfx1 cum_outside
            show claire bj cum with vpunch
            "Then she waits patiently as my cock bobs in front of her face for a couple of second."
            show claire bj facecum with vpunch
            "And when I finally shoot my load, she lets it spatter over her cheeks and nose."
            stop sexsfx1
            $ claire.love += 2
            $ claire.sub += 1
        "Cum in her mouth" if claire.sub >= 50:
            "And a massive part of that fantasy I just mentioned involves having Claire swallow my load."
            "So I make sure to keep perfectly still and let nature take it's course."
            play sexsfx1 bj_gulp
            show claire bj cum with vpunch
            "Claire seems to realise what I'm doing too, and keeps up her side of things."
            with vpunch
            "But as soon as I begin to cum, she handles it like a pro, swallowing without incident."
            play sexsfx1 slide_out
            show claire bj cum down oral tongue saliva with vpunch
            "In fact she handles every last drop without missing a beat."
            stop sexsfx1
            $ claire.love += 4
            $ claire.sub += 2
        "Hold on":
            "Part of me really wants to have Claire swallow my load or else take it in the face."
            play sexsfx1 slide_out
            show claire bj out with vpunch
            "But I also want this to be nothing more than foreplay, a prelude to what comes next."
            show claire bj down oral tongue with vpunch
            "And so I steel myself, doing all that I can to hold it in and keep from cumming."
            "Claire seems to sense what I'm doing and understand why."
            "As she gently releases me, opening her mouth and pulling her head back too."
    return

label claire_fuck_date_cunnilingus:
    "Now that we're both naked, I can see Claire's eyes looking me up and down."
    "And that, combined with my desire for her, is really starting to turn me on."
    "So much so that my cock is already getting hard and beginning to rise."
    "Claire's eyebrows rise too as she notices what's happening down there."
    show claire talkative
    if claire.sub >= 25:
        claire.say "Oh, hello!"
        claire.say "Aren't you a big boy?"
    else:
        claire.say "Oh my!"
        claire.say "Am I really that exciting?"
    show claire normal
    "I can't help looking flustered as my body betrays my true feelings."
    "And I end up sitting down on the bed, as if that will help to hide it."
    mike.say "I..."
    mike.say "Well..."
    mike.say "The thing is, Claire..."
    mike.say "I always kind of had a fantasy about you..."
    mike.say "That involved my mouth...and your pussy!"
    "Claire sits down on the bed, holding my eye as she does so."
    "And then she crawls backwards, spreading her legs as she goes."
    scene bg black
    show claire cunnilingus naked
    with fade
    claire.say "Okay, [hero.name]..."
    claire.say "How about we make your fantasy come true?"
    "Claire casts her gaze down as she says this, and my eye is drawn along with it."
    "That's when I see that she's already stroking herself in a suggestive manner."
    "I watch in total amazement as Claire traces the outline of her own pussy."
    "And I'm so engrossed that I don't seem to realise I've started to crawl towards her."
    "Before I know it, my head is sinking down between her thighs, getting ever closer."
    "I feel like I'm going into autopilot, like I have no control over my own actions."
    "I must have imagined this moment a thousand times, pictured it happening in my head."
    "And now my body seems to be turning those mental images into actual physical movements."
    show claire cunnilingus closed finger1
    "Putting my hands on Claire's thighs, I close my eyes and part my lips."
    "I catch the scent of her sex before the tip of my tongue touches it."
    "The musky aroma is just how I always imagined it, almost drawing me in."
    show claire cunnilingus finger2
    "And the very moment that my tongue tastes Claire, I'm totally lost."
    "I feel like I have to explore every crease and fold of her pussy."
    "To be able to say that I've traced every inch of it and committed the details to memory."
    show claire cunnilingus hurt finger3
    "And I can hear the result of my obsession all the while I'm doing so."
    "Claire gasps, moans and coos at my efforts, forced to express the pleasure she's feeling."
    show claire cunnilingus tongue
    "Soon enough my tongue has worked its way into the centre of her pussy."
    "And from there it begins to sink deeper still, trying to delve as far as possible."
    "I turn my head this way and that in an effort to get even a fraction of an inch more."
    "Wishing the whole time that I could make my tongue as long as needed on a whim."
    "But the one thing that I'm not paying attention to is how close Claire is getting."
    "How my efforts are pushing her to the point of no return."
    "So it comes as a genuine surprise to me when her thighs press down on me."
    show claire cunnilingus pleasure ahegao with vpunch
    "Using her legs like a pair of pincers, Claire pins me in place as she cums."
    with vpunch
    "And I have no choice but to keep right on going."
    with vpunch
    "Pleasuring her even as she writhes and wriggles in the grip of her orgasm."
    return

label claire_fuck_date_reverse_sixty_nine:
    "Now that we're both naked, I can see Claire's eyes looking me up and down."
    "And that, combined with my desire for her, is really starting to turn me on."
    "So much so that my cock is already getting hard and beginning to rise."
    "Claire's eyebrows rise too as she notices what's happening down there."
    show claire talkative
    if claire.sub >= 25:
        claire.say "Oh, hello!"
        claire.say "Aren't you a big boy?"
    else:
        claire.say "Oh my!"
        claire.say "Am I really that exciting?"
    show claire normal
    "I can't help looking flustered as my body betrays my true feelings."
    "And I end up sitting down on the bed, as if that will help to hide it."
    mike.say "I..."
    mike.say "Well..."
    mike.say "The thing is, Claire..."
    mike.say "I always kind of had a fantasy about you..."
    mike.say "That involved my mouth...and your pussy!"
    show claire talkative
    claire.say "Well, I'm sure we can make that little dream of yours come true!"
    show claire normal
    mike.say "Ah..."
    mike.say "But it also involves you doing the same thing to me...at the same time."
    show claire talkative
    claire.say "Ooh..."
    claire.say "You want to do a sixty-nine?"
    show claire normal
    "Claire's already crawling onto the bed as she says this, turning her back to me."
    "And I watch as she lays on her back, spread out before me."
    claire.say "What are you waiting for, [hero.name]?"
    claire.say "This is your fantasy - so take the lead already!"
    "Claire casts her gaze down as she says this, and my eye is drawn along with it."
    "That's when I see that she's already stroking herself in a suggestive manner."
    "I watch in total amazement as Claire traces the outline of her own pussy."
    scene bg black
    show claire sixtynine naked
    with fade
    "And I'm so engrossed that I don't seem to realise I've started to crawl towards her."
    "Before I know it, my head is sinking down between her thighs, getting ever closer."
    "I feel like I'm going into autopilot, like I have no control over my own actions."
    "I must have imagined this moment a thousand times, pictured it happening in my head."
    "And now my body seems to be turning those mental images into actual physical movements."
    "Putting my hands on Claire's thighs, I close my eyes and part my lips."
    "I catch the scent of her sex before the tip of my tongue touches it."
    "The musky aroma is just how I always imagined it, almost drawing me in."
    "And the very moment that my tongue tastes Claire, I'm totally lost."
    "I feel like I have to explore every crease and fold of her pussy."
    "To be able to say that I've traced every inch of it and committed the details to memory."
    "And I can hear the result of my obsession all the while I'm doing so."
    play sexsfx1 bj_sucking loop
    show claire sixtynine lick
    "Claire gasps, moans and coos at my efforts, forced to express the pleasure she's feeling."
    "Soon enough my tongue has worked its way into the centre of her pussy."
    "And from there it begins to sink deeper still, trying to delve as far as possible."
    "I turn my head this way and that in an effort to get even a fraction of an inch more."
    "And that's when I almost stop what I'm doing entirely."
    show claire sixtynine blowjob
    "As I feel Claire's lips wrap themselves around my cock."
    "Now don't get me wrong, this isn't like some skilful blow-job."
    "Claire simply latches onto me and starts to work away for all she's worth."
    show claire sixtynine lick drool
    "She licks and sucks as though trying to express what she's feeling herself."
    "And the result is rough and ready, but more than enough to spur me on."
    show claire sixtynine blowjob closed makeup -drool
    "So I redouble my efforts, even as Claire is beginning to do the same to me."
    "The only problem is that I'm so excited by now that Claire's attentions are hitting me so hard."
    "I can already feel the sensation of myself starting to cum."
    menu:
        "Cum on her face" if claire.sub >= 25:
            "And a massive part of that fantasy I just mentioned involves Claire taking it in the face!"
            play sexsfx1 slide_out
            show claire sixtynine out pleasure with vpunch
            "So I make a move to pull back and slide myself out of her mouth before the inevitable happens."
            "Claire seems to realise what I'm doing in good time, as she pulls back and releases me too."
            "Then she waits patiently as my cock bobs in front of her face for a couple of second."
            play sexsfx1 cum_outside
            show claire sixtynine cumshot closed with vpunch
            pause 0.2
            show claire sixtynine cum onface pleasure with vpunch
            "And when I finally shoot my load, she lets it spatter over her cheeks and nose."
            $ claire.love += 2
            $ claire.sub += 1
        "Cum in her mouth" if claire.sub >= 50:
            "And a massive part of that fantasy I just mentioned involves having Claire swallow my load."
            "So I make sure to keep perfectly still and let nature take it's course."
            "Claire seems to realise what I'm doing too, and keeps up her side of things."
            play sexsfx1 bj_gulp
            show claire sixtynine cum inmouth pleasure with vpunch
            "But as soon as I begin to cum, she handles it like a pro, swallowing without incident."
            with vpunch
            "In fact she handles every last drop without missing a beat."
            $ claire.love += 4
            $ claire.sub += 2
        "Hold on":
            "Part of me really wants to have Claire swallow my load or else take it in the face."
            show claire sixtynine pleasure
            "But I also want this to be nothing more than foreplay, a prelude to what comes next."
            "And so I steel myself, doing all that I can to hold it in and keep from cumming."
            "Claire seems to sense what I'm doing and understand why."
            play sexsfx1 slide_out
            show claire sixtynine out happy
            "As she gently releases me, opening her mouth and pulling her head back too."
    return

label claire_fuck_date_missionary(sexperience_min):
    "By now it's obvious that Claire's getting a kick out of how big a deal all of this is for me."
    "I know full well that her husband is an asshole that doesn't appreciate just how lucky he is."
    "So maybe I'm flattering myself here, but it must be a thrill for Claire to have me in awe of her."
    "Because the honest truth is that I can't help just looking her up and down in total amazement."
    show claire talkative
    if claire.sub >= 25:
        claire.say "[hero.name], why are you looking at me like that?"
        claire.say "I'm going to start blushing if you keep it up!"
    else:
        claire "What are you staring at me like that for?"
    claire.say "Haven't you ever seen a naked woman before?"
    show claire normal blush
    mike.say "I thought I had, Claire..."
    mike.say "But that was until I saw you!"
    "Now I can see that Claire's cheeks are flushing with colour, and she makes to wave my words away."
    "But at the same time I feel like I can sense something more in her reaction too."
    "A second rush of blood in her that's deeper and more powerful than the one in her cheeks."
    "And I'm proved right when she lays herself out on the bed in front of me."
    "Because now I can see that there's a genuine hunger in Claire's eyes."
    "One that's making her spread herself out before me, as if she's issuing a challenge."
    show claire talkative
    if claire.sub >= 25:
        claire.say "You're so charming, [hero.name]…"
        claire.say "So charming that I can't refuse you anything!"
    else:
        claire.say "You're a sweet-talker, [hero.name]…"
        claire.say "But let's see if you can deliver on those promises of yours!"
    show claire normal
    "In the past I must have seen or heard of a thousand positions to do it in."
    "But right now, all of them seem to fade into the background as I look at Claire."
    scene bg black
    show claire missionary naked
    with fade
    "Because all I can think of doing is climbing onto the bed and then atop her."
    "So that's exactly what I do, keeping things straight up and simple."
    menu:
        "Fuck her pussy":
            "Claire looks up at me as I get into position, a smile on her face."
            "And as I push her legs apart, she begins to nod her head at my efforts."
            "Needless to say that my cock is getting harder by the second."
            "And I can see Claire checking it out as I get ever closer."
            "But soon enough my eyes are focussed solely on the lips of her pussy."
            call check_condom_usage (claire) from _call_check_condom_usage_164
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show claire missionary condom
            show claire missionary closed hurt
            with fade
            "Leaning forwards, I take aim for Claire's lower lips."
            "As I do so, I make a point of slipping my left arm under her right leg."
            "Lifting it as I get closer means that her thighs are spread further apart."
            "And so I have a wider space to move myself into as we come together."
            show claire missionary wide
            "For her own part, Claire seems to be totally comfortable in my hands."
            "Just lying back and letting me have my way with her in complete silence."
            "I have to admit that the feeling is more than a little intoxicating."
            "Here's a woman that I spent most of my teenage years secretly lusting after."
            "And now she's literally giving herself to me, totally and completely."
            "Claire stays silent until the very moment that our bodies meet in the middle."
            "But when the shaft of my cock presses against the lips of her pussy, she can't hold back anymore."
            claire.say "Mmm…"
            show claire missionary happy
            claire.say "Please, [hero.name]…"
            claire.say "I want it inside of me!"
            show claire missionary hurt
            "I nod as I begin to move back and forth, stroking myself against Claire."
            "At the same time I feel her begin to move too, matching her motions to mine."
            "She's already more than a little excited down there, slippery and supple."
            "But I swear that I can feel her getting wetter and softer by the second."
            "I'm doing the best I can to keep things moving, to build up slowly."
            "Because part of me is still keen to show Claire that I'm in control."
            "You know, that I'm a mature kind of guy that knows what he's doing?"
            "But I guess we're both too eager for that to work right now."
            "As a moment later I feel myself move at a different angle."
            play sexsfx1 slide_in
            show claire missionary vaginal hurt closed at stepback(speed=0.07, h=10, v=0)
            "And suddenly there's no more resistance holding me back."
            mike.say "Oh..."
            mike.say "Oh fuck..."
            mike.say "Am I...am I in?!?"
            show claire missionary wide happy
            claire.say "Y...yes..."
            claire.say "You very definitely are!"
            "Suddenly all of my pretensions seem to vanish in an instant."
            "I find myself staring into Claire's eyes, and she's smiling up at me."
            "All it takes is for her to nod eagerly, to give me her approval."
            play sexsfx1 fuck_calm loop
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "And then I'm away, moving ever faster inside of her."
            "The only thinh I can think about is what I'm doing right now."
            "Because being inside of Claire is like nothing I could have imagined."
            play sexsfx1 fuck_calm loop
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "Soon enough I'm thrusting in and out of her as fast as I can."
            "Pounding away as she wriggles and gasps beneath me."
            "At first I think that Claire must be nodding, liking what I'm doing."
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "But then I realise that it could just be me making her rock back and forth."
            if claire.flags.buttplug:
                "Somehow the thought of Claire's ass pops into my head."
                "Specifically that it's totally empty right about now."
                "And with that in mind, I reach down and rummage under the bed."
                "Finding what I want, I pull it back and inspect my prize."
                "There, in the palm of my hand, is a rubber butt-plug."
                show claire missionary hurt buttplug at stepback(speed=0.07, h=10, v=0)
                "Which I waste no time in working between Claire's buttocks."
                "She moans as the toy sinks into her ass, only adding to her pleasure."
            else:
                "With that in mind, I focus my mind on the task at hand."
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "By now I'm sure that Claire's almost overwhelmed by my efforts to please her."
            "Of course my most honest hope is that I'm the best she's ever had."
            "But hell, I'll even settle for reminding her of how good it used to be!"
            play sexsfx1 fuck_speed loop
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            pause 0.15
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            "Heaven knows that I'm having the best time right now, and I hope she is too."
            "And all of that is going through my head just a second before I feel something change."
            "Suddenly I'm almost overwhelmed by the sensation of Claire clamping down on me."
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            pause 0.15
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            "The walls of her pussy seem to be squeezing my cock for all it's worth."
            "And I realise that she must have reached her climax, that she must be cuming."
            if claire.flags.buttplug:
                "And I see this as the perfect moment to whip out the butt-plug."
                play sexsfx1 pop_out
                show claire missionary hurt -buttplug at stepback(speed=0.05, h=10, v=0)
                "So I reach down and grab hold of the end, then pull it out in one smooth motion."
                "Instantly Claire's orgasm seems to intensify, almost like it's doubling in strength."
            else:
                "The effects of my efforts paying off in a spectacular fashion."
            play sexsfx1 fuck_sprint loop
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            pause 0.15
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            "But while all of this is happening, Claire's pushing me harder too."
            "And soon her orgasm has the same effect on me, as I lose it as well."
            call cum_reaction (claire, 'vaginal', sexperience_min) from _call_cum_reaction_298
            if _return == "vaginal_condom":
                "It's at times like this that I'm glad we remembered to use protection."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                play sexsfx1 final_thrust
                show claire missionary pleasure ahegao with hpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with hpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_happy":
                "In the end I just decide to surrender and let nature take it's course."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 5
                $ claire.impregnate()
                play sexsfx1 final_thrust
                show claire missionary pleasure ahegao cum with hpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with hpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_mad":
                show claire missionary hurt wide
                claire.say "Stop...pull out"
                claire.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ claire.impregnate()
                play sexsfx1 final_thrust
                show claire missionary cum pleasure with hpunch
                "Claire moans as I shoot my load deep inside of her."
                with hpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide claire
                show claire naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ claire.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_outside":
                play sexsfx1 slide_out
                show claire missionary out with hpunch
                "I wait until the last possible moment, and then I pull all the way out of Claire."
                "The motion makes me gasp, and it seems to have a similar effect on her too."
                play sexsfx1 final_thrust
                show claire missionary pleasure ahegao cum with hpunch
                "And she wriggles beneath me as I shoot my load onto her belly and thighs."
                show claire missionary onclaire onmike with hpunch
                "Leaving me to watch as the look of sheer ecstasy passes over her face."
                $ claire.love += 1
            elif _return == "vaginal_inside_pill":
                show claire missionary pleasure happy
                claire.say "Do it, [hero.name]…"
                claire.say "I'm on...the Pill!"
                "I silently thank Claire for the timely reminder that she just delivered."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 2
                play sexsfx1 final_thrust
                show claire missionary pleasure ahegao cum with hpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with hpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_pregnant":
                show claire missionary pleasure happy
                claire.say "Do it, [hero.name]…"
                claire.say "I'm pregnant...remember?!?"
                "I silently thank Claire for the timely reminder that she just delivered."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 3
                play sexsfx1 final_thrust
                show claire missionary pleasure ahegao cum with hpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with hpunch
                "Watching as the look of sheer ecstasy passes over her face."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Claire looks up at me as I get into position, a smile on her face."
            "And as I push her legs apart, she begins to nod her head at my efforts."
            "Needless to say that my cock is getting harder by the second."
            "And I can see Claire checking it out as I get ever closer."
            "But soon enough my eyes are focussed solely on the curve of her buttocks."
            show claire missionary closed hurt
            "Leaning forwards, I take aim for the space between Claire's butt-cheeks."
            "As I do so, I make a point of slipping my left arm under her right leg."
            "Lifting it as I get closer means that her thighs are spread further apart."
            "And so I have a wider space to move myself into as we come together."
            show claire missionary wide
            "For her own part, Claire seems to be totally comfortable in my hands."
            "Just lying back and letting me have my way with her in complete silence."
            "I have to admit that the feeling is more than a little intoxicating."
            "Here's a woman that I spent most of my teenage years secretly lusting after."
            "And now she's literally giving herself to me, totally and completely."
            "Claire stays silent until the very moment that our bodies meet in the middle."
            "But when the shaft of my cock presses against the edge of her hole, she can't hold back anymore."
            claire.say "Mmm…"
            show claire missionary happy
            claire.say "Please, [hero.name]…"
            claire.say "I want it inside of me!"
            show claire missionary hurt
            "I nod as I begin to move back and forth, stroking myself against Claire."
            "At the same time I feel her begin to move too, matching her motions to mine."
            "She's already more than a little excited down there, as things are already starting to relax."
            "But I swear that I can feel her getting softer by the second."
            "I'm doing the best I can to keep things moving, to build up slowly."
            "Because part of me is still keen to show Claire that I'm in control."
            "You know, that I'm a mature kind of guy that knows what he's doing?"
            "But I guess we're both too eager for that to work right now."
            "As a moment later I feel myself move at a different angle."
            play sexsfx1 slide_in
            show claire missionary anal hurt closed at stepback(speed=0.07, h=10, v=0)
            "And suddenly there's no more resistance holding me back."
            mike.say "Oh..."
            mike.say "Oh fuck..."
            mike.say "Am I...am I in?!?"
            show claire missionary wide happy
            claire.say "Y...yes..."
            claire.say "You very definitely are!"
            "Suddenly all of my pretensions seem to vanish in an instant."
            "I find myself staring into Claire's eyes, and she's smiling up at me."
            "All it takes is for her to nod eagerly, to give me her approval."
            play sexsfx1 fuck_calm loop
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "And then I'm away, moving ever faster inside of her."
            "The only thinh I can think about is what I'm doing right now."
            "Because being inside of Claire is like nothing I could have imagined."
            play sexsfx1 fuck_calm loop
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "Soon enough I'm thrusting in and out of her as fast as I can."
            "Pounding away as she wriggles and gasps beneath me."
            "At first I think that Claire must be nodding, liking what I'm doing."
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "But then I realise that it could just be me making her rock back and forth."









            "With that in mind, I focus my mind on the task at hand."
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            pause 0.2
            show claire missionary at stepback(speed=0.07, h=10, v=0)
            "By now I'm sure that Claire's almost overwhelmed by my efforts to please her."
            "Of course my most honest hope is that I'm the best she's ever had."
            "But hell, I'll even settle for reminding her of how good it used to be!"
            play sexsfx1 fuck_speed loop
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            pause 0.15
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            "Heaven knows that I'm having the best time right now, and I hope she is too."
            "And all of that is going through my head just a second before I feel something change."
            "Suddenly I'm almost overwhelmed by the sensation of Claire clamping down on me."
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            pause 0.15
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            "The muscles of her ass seem to be squeezing my cock for all it's worth."
            "And I realise that she must have reached her climax, that she must be cuming."





            "The effects of my efforts paying off in a spectacular fashion."
            play sexsfx1 fuck_sprint loop
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            pause 0.15
            show claire missionary at stepback(speed=0.05, h=10, v=0)
            "But while all of this is happening, Claire's pushing me harder too."
            "And soon her orgasm has the same effect on me, as I lose it as well."
            call cum_reaction (claire, 'anal', sexperience_min) from _call_cum_reaction_319
            if _return == "anal_inside":
                "In the end I just decide to surrender and let nature take it's course."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                play sexsfx1 final_thrust
                show claire doggy pleasure ahegao cum with hpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire's ass."
                with hpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "anal_outside":
                play sexsfx1 pop_out
                show claire missionary out with vpunch
                "I wait until the last possible moment, and then I pull all the way out of Claire's ass."
                "The motion makes me gasp, and it seems to have a similar effect on her too."
                play sexsfx1 final_thrust
                show claire missionary pleasure ahegao cum with vpunch
                "And she wriggles beneath me as I shoot my load onto her belly and thighs."
                show claire missionary onclaire onmike with hpunch
                "Leaving me to watch as the look of sheer ecstasy passes over her face."
    return

label claire_fuck_date_doggy(sexperience_min):
    "By now it's obvious that Claire's getting a kick out of how big a deal all of this is for me."
    "I know full well that her husband is an asshole that doesn't appreciate just how lucky he is."
    "So maybe I'm flattering myself here, but it must be a thrill for Claire to have me in awe of her."
    "Because the honest truth is that I can't help just looking her up and down in total amazement."
    show claire talkative
    if claire.sub >= 25:
        claire.say "[hero.name], why are you looking at me like that?"
        claire.say "I'm going to start blushing if you keep it up!"
    else:
        claire.say "What are you staring at me like that for?"
    claire.say "Haven't you ever seen a naked woman before?"
    show claire normal blush
    mike.say "I thought I had, Claire..."
    mike.say "But that was until I saw you!"
    "Now I can see that Claire's cheeks are flushing with colour, and she makes to wave my words away."
    "But at the same time I feel like I can sense something more in her reaction too."
    "A second rush of blood in her that's deeper and more powerful than the one in her cheeks."
    "And I'm proved right when she lays herself out on the bed in front of me."
    "Because now I can see that there's a genuine hunger in Claire's eyes."
    "One that's making her spread herself out before me, as if she's issuing a challenge."
    show claire talkative
    if claire.sub >= 25:
        claire.say "You're so charming, [hero.name]…"
        claire.say "So charming that I can't refuse you anything!"
    else:
        claire.say "You're a sweet-talker, [hero.name]…"
        claire.say "But let's see if you can deliver on those promises of yours!"
    show claire normal
    "As if wanting to underline what she just said, Claire stretches out on the bed."
    "And then she slowly rises onto her hands and knees, moving like a cat."
    "But the thing is that the image of her in that position puts me in mind of a different animal entirely."
    "Because all it says to me is doggy, and now that idea is firmly lodged in my mind."
    scene bg black
    show claire doggy hurt naked
    with fade
    "So I hurry to get up and onto my knees, hauling myself into place behind Claire."
    "And then I slap the palms of my hands down onto her haunches, getting a firm grip."
    show claire doggy happy
    claire.say "Oh..."
    claire.say "Oh my goodness!"
    show claire doggy hurt
    mike.say "Right there, Claire..."
    mike.say "That's exactly where I want you."
    "Claire nods her head, seeming to get where I'm coming from and what I want."
    menu:
        "Fuck her pussy":
            "She turns her head back around to face the front."
            "And at the same time leans forwards and down."
            "Pushing her ass towards me as she does so."
            call check_condom_usage (claire) from _call_check_condom_usage_165
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show claire doggy condom
            show claire doggy
            with fade
            "My plan had been to pull Claire slowly backwards and so gradually onto me."
            "But by now she's lowered herself down so much that simply won't work."
            "And so instead I'm forced to raise myself up in order to get things moving."
            "This means that my cock is aimed down at an angle, pointed at Claire's pussy."
            "But it's not like any of that is going to stop me getting what I want here."
            "Oh no, in fact this new and unexpected angle has its advantages too."
            "Because now all of my weight is behind me as I start to tease Claire's lips."
            "And I have even more control as the tip slides the entire length of her pussy."
            "For me the sensation is quite something, urging me on to do more of the same."
            "But I can already hear how it's making Claire gasp and moan."
            "Plus she's doing all she can to rub herself against me down there too."
            "All the time I'm holding onto her haunches for all I'm worth."
            play sexsfx1 slide_in
            show claire doggy vaginal at startle(0.05, 10)
            "Trying to keep myself on target and work my way inside at the same time."
            "In fact I seem to be concentrating so hard that I miss the moment it actually happens."
            "One second I'm grinding away, tyring to get in there, and the next I'm almost halfway inside!"
            show claire doggy happy
            claire.say "Oh..."
            claire.say "Oh fuck..."
            claire.say "Oh fuck yeah!"
            show claire doggy hurt
            "As if I needed any encouragement to capitalise on the moment, Claire's cries spur me on."
            play sexsfx1 fuck_calm loop
            show claire doggy at startle(0.07, 10)
            pause 0.2
            show claire doggy at startle(0.07, 10)
            "And I go from holding on and pushing to thrusting into her in the blink of an eye."
            "Now I really do feel like I'm riding Claire, like I've properly mounted her."
            "So the only logical thing to do is make sure it's a memorable experience for us both."
            if claire.flags.buttplug:
                "Somehow the thought of Claire's ass pops into my head."
                "Specifically that it's totally empty right about now."
                "And with that in mind, I reach down and rummage under the bed."
                "Finding what I want, I pull it back and inspect my prize."
                "There, in the palm of my hand, is a rubber butt-plug."
                "Which I waste no time in working between Claire's buttocks."
                show claire doggy hurt closed buttplug at startle(0.05, 10)
                "She moans as the toy sinks into her ass, only adding to her pleasure."
            else:
                "With that in mind, I focus my mind on the task at hand."
            play sexsfx1 fuck_moderate loop
            show claire doggy at startle(0.07, 10)
            pause 0.2
            show claire doggy at startle(0.07, 10)
            "Soon enough I find that pressing down from above is squashing Claire into the mattress."
            "Every time I thrust into her, she's almost smothered by the sheets and unable to breathe."
            "And in the heat of the moment, there's only one remedy that my brain can come up with."
            "Reaching out with one hand, I take a firm hold of Claire's ponytail."
            show claire doggy at startle(0.07, 10)
            pause 0.2
            show claire doggy at startle(0.07, 10)
            "Then I pull it backwards, gently but firmly lifting her upwards."
            "Claire doesn't resist or object, rising up on her hands as I pull."
            "In fact she seems to be really getting into the notion of a little hair-pulling."
            "Playfully tossing her head and gasping, all of which lets me know she's excited."
            play sexsfx1 fuck_speed loop
            show claire doggy at startle(0.05, 10)
            pause 0.15
            show claire doggy at startle(0.05, 10)
            "Of course it has an effect on me too, urging me to go harder and faster then before."
            "Because now I really feel like I'm taking Claire and taming her with my efforts."
            "The more she writhes and wriggles, the more I try to keep her in check."
            "All the while we're both moving faster and pushing back harder too."
            if claire.flags.buttplug:
                "But I think that I might have just the thing to push it further still."
                "I see this as the perfect moment to whip out the butt-plug."
                play sexsfx1 pop_out
                show claire doggy hurt closed -buttplug at startle(0.05, 10)
                "So I reach down and grab hold of the end, then pull it out in one smooth motion."
                "Instantly Claire's movements to intensify, and I can sense that she's starting to cum."
            else:
                "The effect being that we're soon teetering on the edge of losing it."
            play sexsfx1 fuck_sprint loop
            show claire doggy at startle(0.05, 10)
            pause 0.15
            show claire doggy at startle(0.05, 10)
            "There it is, the sensation of her muscles clamping down on my cock!"
            "I might have been able to see Claire's orgasm coming, but it still hits me like a wave."
            "And in mere seconds, I know that I'm going to be swept along with her."
            call cum_reaction (claire, 'vaginal', sexperience_min) from _call_cum_reaction_299
            if _return == "vaginal_condom":
                "It's at times like this that I'm glad we remembered to use protection."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                play sexsfx1 final_thrust
                show claire doggy pleasure ahegao drool with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_happy":
                "In the end I just decide to surrender and let nature take it's course."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 5
                $ claire.impregnate()
                play sexsfx1 final_thrust
                show claire doggy pleasure ahegao drool cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_mad":
                show claire doggy hurt wide
                claire.say "Stop...pull out"
                claire.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ claire.impregnate()
                play sexsfx1 final_thrust
                show claire doggy cum pleasure with vpunch
                "Claire moans as I shoot my load deep inside of her."
                with vpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide claire
                show claire naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ claire.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_outside":
                play sexsfx1 slide_out
                show claire doggy outside with vpunch
                "I wait until the last possible moment, and then I pull all the way out of Claire."
                "The motion makes me gasp, and it seems to have a similar effect on her too."
                show claire doggy pleasure ahegao drool cum with vpunch
                "And she wriggles beneath me as I shoot my load onto her buttocks and thighs."
                with vpunch
                "Leaving me to watch as the look of sheer ecstasy passes over her face."
                $ claire.love += 1
            elif _return == "vaginal_inside_pill":
                claire.say "Do it, [hero.name]…"
                claire.say "I'm on...the Pill!"
                "I silently thank Claire for the timely reminder that she just delivered."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 2
                play sexsfx1 final_thrust
                show claire doggy pleasure ahegao drool cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_pregnant":
                claire.say "Do it, [hero.name]…"
                claire.say "I'm pregnant...remember?!?"
                "I silently thank Claire for the timely reminder that she just delivered."
                with vpunch
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 3
                play sexsfx1 final_thrust
                show claire doggy pleasure ahegao drool cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "She turns her head back around to face the front."
            "And at the same time leans forwards and down."
            "Pushing her ass towards me as she does so."
            "My plan had been to pull Claire slowly backwards and so gradually onto me."
            "But by now she's lowered herself down so much that simply won't work."
            "And so instead I'm forced to raise myself up in order to get things moving."
            "This means that my cock is aimed down at an angle, pointed at Claire's ass."
            "But it's not like any of that is going to stop me getting what I want here."
            "Oh no, in fact this new and unexpected angle has its advantages too."
            "Because now all of my weight is behind me as I start to tease Claire's hole."
            "And I have even more control as the tip slides the entire circle of the hole."
            "For me the sensation is quite something, urging me on to do more of the same."
            "But I can already hear how it's making Claire gasp and moan."
            "Plus she's doing all she can to rub herself against me down there too."
            "All the time I'm holding onto her haunches for all I'm worth."
            play sexsfx1 slide_in
            show claire doggy anal at startle(0.05, 10)
            "Trying to keep myself on target and work my way inside at the same time."
            "In fact I seem to be concentrating so hard that I miss the moment it actually happens."
            "One second I'm grinding away, tyring to get in there, and the next I'm almost halfway inside!"
            show claire doggy happy
            claire.say "Oh..."
            claire.say "Oh fuck..."
            claire.say "Oh fuck yeah!"
            show claire doggy hurt
            "As if I needed any encouragement to capitalise on the moment, Claire's cries spur me on."
            play sexsfx1 fuck_calm loop
            show claire doggy at startle(0.07, 10)
            pause 0.2
            show claire doggy at startle(0.07, 10)
            "And I go from holding on and pushing to thrusting into her in the blink of an eye."
            "Now I really do feel like I'm riding Claire, like I've properly mounted her."
            "So the only logical thing to do is make sure it's a memorable experience for us both."
            if hero.has_item("dildo") and claire.sub >= 60:
                "Somehow the thought of Claire's pussy pops into my head."
                "Specifically that it's totally empty right about now."
                "And with that in mind, I reach down and rummage under the bed."
                "Finding what I want, I pull it back and inspect my prize."
                "There, in the palm of my hand, is a rubber dildo."
                "Which I waste no time in working between Claire's thighs."
                show claire doggy hurt closed at startle(0.05, 10)
                "She moans as the toy sinks into her pussy, only adding to her pleasure."
            else:
                "With that in mind, I focus my mind on the task at hand."
            play sexsfx1 fuck_moderate loop
            show claire doggy at startle(0.07, 10)
            pause 0.2
            show claire doggy at startle(0.07, 10)
            "Soon enough I find that pressing down from above is squashing Claire into the mattress."
            "Every time I thrust into her, she's almost smothered by the sheets and unable to breathe."
            "And in the heat of the moment, there's only one remedy that my brain can come up with."
            "Reaching out with one hand, I take a firm hold of Claire's ponytail."
            show claire doggy at startle(0.07, 10)
            pause 0.2
            show claire doggy at startle(0.07, 10)
            "Then I pull it backwards, gently but firmly lifting her upwards."
            "Claire doesn't resist or object, rising up on her hands as I pull."
            "In fact she seems to be really getting into the notion of a little hair-pulling."
            "Playfully tossing her head and gasping, all of which lets me know she's excited."
            play sexsfx1 fuck_speed loop
            show claire doggy at startle(0.05, 10)
            pause 0.15
            show claire doggy at startle(0.05, 10)
            "Of course it has an effect on me too, urging me to go harder and faster then before."
            "Because now I really feel like I'm taking Claire and taming her with my efforts."
            "The more she writhes and wriggles, the more I try to keep her in check."
            "All the while we're both moving faster and pushing back harder too."
            if hero.has_item("dildo") and claire.sub >= 60:
                "But I think that I might have just the thing to push it further still."
                "I see this as the perfect moment to whip out the dildo."
                play sexsfx1 slide_out
                show claire doggy hurt closed at startle(0.05, 10)
                "So I reach down and grab hold of the end, then pull it out of her pussy in one smooth motion."
                "Instantly Claire's movements to intensify, and I can sense that she's starting to cum."
            else:
                "The effect being that we're soon teetering on the edge of losing it."
            play sexsfx1 fuck_sprint loop
            show claire doggy at startle(0.05, 10)
            pause 0.15
            show claire doggy at startle(0.05, 10)
            "There it is, the sensation of her muscles clamping down on my cock!"
            "I might have been able to see Claire's orgasm coming, but it still hits me like a wave."
            "And in mere seconds, I know that I'm going to be swept along with her."
            call cum_reaction (claire, 'anal', sexperience_min) from _call_cum_reaction_320
            if _return == "anal_inside":
                "In the end I just decide to surrender and let nature take it's course."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                play sexsfx1 final_thrust
                show claire doggy pleasure ahegao drool cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire's ass."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "anal_outside":
                play sexsfx1 pop_out
                show claire doggy outside with vpunch
                "I wait until the last possible moment, and then I pull all the way out of Claire's ass."
                "The motion makes me gasp, and it seems to have a similar effect on her too."
                show claire doggy pleasure ahegao drool cum with vpunch
                "And she wriggles beneath me as I shoot my load onto her buttocks and thighs."
                with vpunch
                "Leaving me to watch as the look of sheer ecstasy passes over her face."
    return

label claire_fuck_date_fullnelson(sexperience_min):
    "By now it's obvious that Claire's getting a kick out of how big a deal all of this is for me."
    "I know full well that her husband is an asshole that doesn't appreciate just how lucky he is."
    "So maybe I'm flattering myself here, but it must be a thrill for Claire to have me in awe of her."
    "Because the honest truth is that I can't help just looking her up and down in total amazement."
    show claire talkative
    if claire.sub >= 25:
        claire.say "[hero.name], why are you looking at me like that?"
        claire.say "I'm going to start blushing if you keep it up!"
    else:
        claire.say "What are you staring at me like that for?"
    claire.say "Haven't you ever seen a naked woman before?"
    show claire normal blush
    mike.say "I thought I had, Claire..."
    mike.say "But that was until I saw you!"
    "Now I can see that Claire's cheeks are flushing with colour, and she makes to wave my words away."
    "But at the same time I feel like I can sense something more in her reaction too."
    "A second rush of blood in her that's deeper and more powerful than the one in her cheeks."
    "And I'm proved right when she lays herself out on the bed in front of me."
    "Because now I can see that there's a genuine hunger in Claire's eyes."
    "One that's making her spread herself out before me, as if she's issuing a challenge."
    show claire talkative
    if claire.sub >= 25:
        claire.say "You're so charming, [hero.name]…"
        claire.say "So charming that I can't refuse you anything!"
    else:
        claire.say "You're a sweet-talker, [hero.name]…"
        claire.say "But let's see if you can deliver on those promises of yours!"
    show claire normal
    "I'm already nodding as I start to formulate a plan in my head."
    "Determined to show Claire that I'm an original thinker when it comes to the bedroom."
    "Doing the best I can to play it cool, I lie down next to Claire."
    "All the time acting like I'm just going to match her own pose."
    menu:
        "Fuck her pussy":
            call check_condom_usage (claire) from _call_check_condom_usage_166
            if _return == False:
                return "leave_without_gain"
            "But the moment that I'm in position, I make my move."
            "Slipping behind Claire, I slide my hands under her thighs."
            "And then I starts to almost fold her in half."
            scene bg black
            if CONDOM:
                show claire fullnelson condom hurt
            show claire fullnelson hurt
            with fade
            "Before she even knows what's happening, my hands are behind her head."
            "And I hastily knit my fingers together, meaning that she's pinned in place."
            show claire fullnelson happy
            if claire.sub >= 25:
                claire.say "Oh..."
                claire.say "Oh my goodness!"
            else:
                claire.say "[hero.name]…"
                claire.say "What...what are you doing?!?"
            show claire fullnelson hurt
            "Rather than explaining myself with words, I decide to use actions instead."
            "The position that I have Claire in means that I have total control over her."
            "And she's in the perfect spot for what I have in mind too."
            "So I quickly lower her down a little, just enough for two things to meet."
            show claire fullnelson happy
            claire.say "Oh..."
            claire.say "Ah..."
            show claire fullnelson hurt
            claire.say "Mmm…"
            "Claire begins to gasp and moan as the head of my cock presses against her."
            "The tip slipping and sliding over the lips of her pussy, making her wriggle in my arms."
            "And the best thing is that there's nowhere for her to go, no way to escape."
            show claire fullnelson at startle(0.07, -10)
            pause 0.2
            show claire fullnelson at startle(0.07, -10)
            "All I have to do is sit on the bed and keep moving her up and down."
            "Each successive pass making Claire more aroused and desperate than the last."
            "I swear that I can actually feel her pussy getting warmer and wetter."
            "Her body becoming ever more desperate as I continue to tease her with my cock."
            "Until finally she seems to melt in my arms, her body surrendering to me."
            "But even so the process is achingly slow and more than a little intense."
            show claire fullnelson vaginal at startle(0.07, -10)
            "At first Claire sinks down no more than an inch onto me as her lips part."
            "Even so the effect on both of us is still pretty intense."
            show claire fullnelson happy
            claire.say "Oh fuck..."
            show claire fullnelson hurt
            mike.say "Urgh..."
            show claire fullnelson at startle(0.07, -10)
            "Bracing myself, I lift Claire again and bring her back down."
            show claire fullnelson at startle(0.07, -10)
            "This time my cock goes almost half the way into her in one motion."
            show claire fullnelson at startle(0.07, -10)
            "But on the third attempt, all resistance disappears and Claire sinks down all the way."
            "For a moment I feel almost overwhelmed by the sensations of pleasure."
            "That is until I remember where I am and what we're doing right now."
            show claire fullnelson at startle(0.07, -10)
            pause 0.2
            show claire fullnelson at startle(0.07, -10)
            "The thought spurs me back into action, making me lift and lower Claire again."
            "And soon enough we've settled into a rhythm and I'm working like a machine."
            if claire.flags.buttplug:
                "Somehow the thought of Claire's ass pops into my head."
                "Specifically that it's totally empty right about now."
                "And with that in mind, I reach down and rummage under the bed."
                "Finding what I want, I pull it back and inspect my prize."
                "There, in the palm of my hand, is a rubber butt-plug."
                show claire fullnelson hurt closed buttplug at startle(0.05, -10)
                "Which I waste no time in working between Claire's buttocks."
                "She moans as the toy sinks into her ass, only adding to her pleasure."
            else:
                "Thinking only of pleasuring Claire, I focus my mind on the task at hand."
            "All the time that I'm fucking Claire, part of me can't actually believe it's happening."
            "That I have the woman I lusted after through my teenage years tied up like a human knot."
            show claire fullnelson at startle(0.07, -10)
            pause 0.2
            show claire fullnelson at startle(0.07, -10)
            "And she's currently bouncing up and down on my cock, gasping and panting with pleasure."
            "Oh man, if only teenage me could see present-day me right now!"
            "Making Claire's tongue hang out of her mouth as she drools helplessly."
            "The mere thought of how much I'm winning right now makes me redouble my efforts."
            show claire fullnelson at startle(0.05, -10)
            pause 0.15
            show claire fullnelson at startle(0.05, -10)
            "Thrusting into Claire from below as I push her down and onto me from above."
            "And it doesn't take long for me to feel the effects of this renewed vigour either."
            "Because now I can tell that Claire's muscles are starting to tense and squeeze."
            "Massaging my cock as she's beginning to succumb to her inevitable orgasm."
            if claire.flags.buttplug:
                "And I see this as the perfect moment to whip out the butt-plug."
                play sexsfx1 pop_out
                show claire fullnelson hurt closed -buttplug at startle(0.05, -10)
                "So I reach down and grab hold of the end, then pull it out in one smooth motion."
                "Instantly Claire's orgasm seems to intensify, almost like it's doubling in strength."
            else:
                "The effects of my efforts paying off in a spectacular fashion."
            play sexsfx1 fuck_sprint loop
            show claire fullnelson at startle(0.05, -10)
            pause 0.15
            show claire fullnelson at startle(0.05, -10)
            "But of course it's not like I can just ride all of this out in a passive manner."
            "Claire's climax effects me too, pushing me over the edge soon after it begins."
            "Which means that I have to make a decision as to what happens next."
            call cum_reaction (claire, 'vaginal', sexperience_min) from _call_cum_reaction_300
            if _return == "vaginal_condom":
                "It's at times like this that I'm glad we remembered to use protection."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                play sexsfx1 final_thrust
                show claire fullnelson pleasure ahegao with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_happy":
                "In the end I just decide to surrender and let nature take it's course."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 5
                $ claire.impregnate()
                play sexsfx1 final_thrust
                show claire fullnelson pleasure ahegao cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_mad":
                show claire fullnelson hurt wide
                claire.say "Stop...pull out"
                claire.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ claire.impregnate()
                play sexsfx1 final_thrust
                show claire fullnelson cum pleasure with vpunch
                "Claire moans as I shoot my load deep inside of her."
                with vpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide claire
                show claire naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ claire.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_outside":
                play sexsfx1 slide_out
                show claire fullnelson out with vpunch
                "I wait until the last possible moment, and then I pull all the way out of Claire."
                "The motion makes me gasp, and it seems to have a similar effect on her too."
                show claire doggy pleasure ahegao cum with vpunch
                "And she wriggles beneath me as I shoot my load onto her buttocks and thighs."
                show claire fullnelson onclaire with vpunch
                "Leaving me to watch as the look of sheer ecstasy passes over her face."
                $ claire.love += 1
            elif _return == "vaginal_inside_pill":
                claire.say "Do it, [hero.name]…"
                claire.say "I'm on...the Pill!"
                "I silently thank Claire for the timely reminder that she just delivered."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 2
                play sexsfx1 final_thrust
                show claire fullnelson pleasure ahegao cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "vaginal_inside_pregnant":
                claire.say "Do it, [hero.name]…"
                claire.say "I'm pregnant...remember?!?"
                "I silently thank Claire for the timely reminder that she just delivered."
                with vpunch
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                $ claire.love += 3
                play sexsfx1 final_thrust
                show claire fullnelson pleasure ahegao cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "But the moment that I'm in position, I make my move."
            "Slipping behind Claire, I slide my hands under her thighs."
            "And then I starts to almost fold her in half."
            "Before she even knows what's happening, my hands are behind her head."
            "And I hastily knit my fingers together, meaning that she's pinned in place."
            show claire fullnelson happy
            if claire.sub >= 25:
                claire.say "Oh..."
                claire.say "Oh my goodness!"
            else:
                claire.say "[hero.name]…"
                claire.say "What...what are you doing?!?"
            show claire fullnelson hurt
            "Rather than explaining myself with words, I decide to use actions instead."
            "The position that I have Claire in means that I have total control over her."
            "And she's in the perfect spot for what I have in mind too."
            "So I quickly lower her down a little, just enough for two things to meet."
            show claire fullnelson happy
            claire.say "Oh..."
            claire.say "Ah..."
            show claire fullnelson hurt
            claire.say "Mmm…"
            "Claire begins to gasp and moan as the head of my cock presses against her."
            "The tip slipping and sliding between the cheeks of her ass, making her wriggle in my arms."
            "And the best thing is that there's nowhere for her to go, no way to escape."
            "All I have to do is sit on the bed and keep moving her up and down."
            "Each successive pass making Claire more aroused and desperate than the last."
            "I swear that I can actually feel her muscles starting to relax and surrender."
            "Her body becoming ever more desperate as I continue to tease her with my cock."
            "Until finally she seems to melt in my arms, her body surrendering to me."
            show claire fullnelson anal at startle(0.07, -10)
            "But even so the process is achingly slow and more than a little intense."
            "At first Claire sinks down no more than an inch onto me as I sink into her hole."
            "Even so the effect on both of us is still pretty intense."
            show claire fullnelson happy
            claire.say "Oh fuck..."
            show claire fullnelson hurt
            mike.say "Urgh..."
            show claire fullnelson at startle(0.07, -10)
            "Bracing myself, I lift Claire again and bring her back down."
            show claire fullnelson at startle(0.07, -10)
            "This time my cock goes almost half the way into her in one motion."
            show claire fullnelson at startle(0.07, -10)
            "But on the third attempt, all resistance disappears and Claire sinks down all the way."
            "For a moment I feel almost overwhelmed by the sensations of pleasure."
            "That is until I remember where I am and what we're doing right now."
            show claire fullnelson at startle(0.07, -10)
            pause 0.2
            show claire fullnelson at startle(0.07, -10)
            "The thought spurs me back into action, making me lift and lower Claire again."
            "And soon enough we've settled into a rhythm and I'm working like a machine."









            "Thinking only of pleasuring Claire, I focus my mind on the task at hand."
            "All the time that I'm fucking Claire, part of me can't actually believe it's happening."
            "That I have the woman I lusted after through my teenage years tied up like a human knot."
            "And she's currently bouncing up and down on my cock, gasping and panting with pleasure."
            "Oh man, if only teenage me could see present-day me right now!"
            "Making Claire's tongue hang out of her mouth as she drools helplessly."
            "The mere thought of how much I'm winning right now makes me redouble my efforts."
            "Thrusting into Claire from below as I push her down and onto me from above."
            "And it doesn't take long for me to feel the effects of this renewed vigour either."
            "Because now I can tell that Claire's muscles are starting to tense and squeeze."
            "Massaging my cock as she's beginning to succumb to her inevitable orgasm."





            play sexsfx1 fuck_sprint loop
            show claire fullnelson at startle(0.05, 10)
            pause 0.15
            show claire fullnelson at startle(0.05, 10)
            "The effects of my efforts paying off in a spectacular fashion."
            "But of course it's not like I can just ride all of this out in a passive manner."
            "Claire's climax effects me too, pushing me over the edge soon after it begins."
            "Which means that I have to make a decision as to what happens next."
            call cum_reaction (claire, 'anal', sexperience_min) from _call_cum_reaction_321
            if _return == "anal_inside":
                "In the end I just decide to surrender and let nature take it's course."
                "Because it means that I can enjoy these last few moments and the sensations they bring."
                play sexsfx1 final_thrust
                show claire fullnelson pleasure ahegao cum with vpunch
                "And then I get to just let go, feeling myself explode, deep inside of Claire's ass."
                with vpunch
                "Watching as the look of sheer ecstasy passes over her face."
            elif _return == "anal_outside":
                play sexsfx1 slide_out
                show claire fullnelson out with vpunch
                "I wait until the last possible moment, and then I pull all the way out of Claire's ass."
                "The motion makes me gasp, and it seems to have a similar effect on her too."
                show claire fullnelson pleasure ahegao cum with vpunch
                "And she wriggles beneath me as I shoot my load onto her belly and thighs."
                show claire fullnelson onclaire with vpunch
                "Leaving me to watch as the look of sheer ecstasy passes over her face."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
