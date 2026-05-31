init python:
    Event(**{
    "name": "palla_hottub_sex_male",
    "label": "palla_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(palla,
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

    Event(**{
    "name": "palla_date_restaurant_bj",
    "label": "palla_date_restaurant_bj",
    "conditions": [
        IsDone("palla_event_06"),
        HeroTarget(
            IsGender("male"),
            IsActivity("date_order_for_her")),
        PersonTarget(palla,
            OnDate(),
            ),
        ],
    "priority": 1000,
    "do_once": False,
    "once_week": True,
    "chances": 25,
    "duration": 1,
    })

    InteractActivity(**{
    "name": "fuck_palla",
    "display_name": "Fuck",
    "label": "palla_apartment_sex",
    "conditions": [
        IsTimeOfDay("evening"),
        IsDone("palla_apartment_sex"),
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(palla,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            HasRoomTag("pallahome"),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

label palla_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show palla

    if not "palla_fuck_date_first" in DONE:
        call palla_fuck_date_first from _call_palla_fuck_date_first
        call handle_npc_leaving (palla, _return) from _call_handle_npc_leaving_18
    elif not "palla_fuck_date_second" in DONE:
        call palla_fuck_date_second from _call_palla_fuck_date_second

        call handle_npc_leaving (palla, _return) from _call_handle_npc_leaving_19
        if _return:
            return
    elif not "palla_fuck_date_third" in DONE:
        call palla_fuck_date_third from _call_palla_fuck_date_third
        call handle_npc_leaving (palla, _return) from _call_handle_npc_leaving_20
    else:


        call palla_fuck_date_intro_male (location) from _call_palla_fuck_date_intro


        call palla_dick_reactions from _call_palla_dick_reactions_2


        call palla_fuck_date_foreplay_male from _call_palla_fuck_date_foreplay_male




        call palla_fuck_date_choices_male from _call_palla_fuck_date_choices_male


        call handle_npc_leaving (palla, _return) from _call_handle_npc_leaving_21
        if _return:
            return


    if palla.love > 190:
        if palla.sub > 90:
            palla.say "I love you so much, master."
        else:
            palla.say "I love you so much."
    hide palla
    call palla_sleep_date_fuck (location) from _call_palla_sleep_date_fuck_1
    return

label palla_fuck_date_foreplay_male:
    menu:
        "Let her have some control":
            call palla_fuck_date_blowjob from _call_palla_fuck_date_blowjob
        "Spank her" if palla.sub >= 30:
            call palla_fuck_date_spank from _call_palla_fuck_date_spank
        "Fuck her":
            pass
    call stop_all_sfx from _call_stop_all_sfx_31

    return _return

label palla_fuck_date_choices_male:
    menu:
        "Cowgirl":
            call palla_fuck_date_cowgirl (0) from _call_palla_fuck_date_cowgirl
        "Missionary" if hero.sexperience >= 5:
            call palla_fuck_date_missionary (5) from _call_palla_fuck_date_missionary
        "Doggy" if hero.sexperience >= 10:
            call palla_fuck_date_doggy (10) from _call_palla_fuck_date_doggy
        "Standing" if hero.sexperience >= 10:
            call palla_fuck_date_standing (10) from _call_palla_fuck_date_standing
    call stop_all_sfx from _call_stop_all_sfx_32

    return _return


label palla_fuck_date_first:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ DONE["palla_fuck_date_first"] = game.days_played
    "I can't help but wonder if Palla actually gets the way she sounds, or is aware of the effect of the words coming out of her mouth."
    "All night she's been tossing out catty comments and downright rude opinions on anything and everything that her gaze happens to fall on."
    "I was just glad she had so many other targets for her vapid bile that I didn't become the focus for it instead."
    scene bg taxi with fade
    pause 0.5
    show bg taxi car with dissolve
    "But after we grab a taxi and head back to my place, all of that changes."
    "Palla's comments inevitably turn to how suburban my neighbourhood is, how twee the house looks, and on, and on."
    scene bg livingroom
    show palla
    with fade
    "Even when we get inside she's still going on, about how cramping it must be to live with housemates and the blandness of the decor."
    "By the time we get to my room, I'm almost fuming."
    "But that's the weird thing - I'm not even thinking of telling her to get lost."
    "It seems the more that Palla winds me up, the more I want to get my hands on her in the most physical way possible."
    "She makes me fume, but it's almost like it affects me in the same way as flirting or foreplay should."
    scene bg bedroom1
    show palla
    with fade
    "There's just something about the arrogance and haughtiness about her."
    "Combined with the fact that she's physically stunning, it feels like an open challenge to step up and somehow rub her face in it."
    "Palla kicks off her expensive and very uncomfortable looking shoes and sits down on my bed."
    show palla underwear with dissolve
    "She starts to strip off in an almost desultory manner, her face showing an ironic cast as I begin to follow her lead."
    show palla naked with dissolve
    call palla_dick_reactions from _call_palla_dick_reactions
    "It strikes me that she's very much intent on us getting intimate, despite her constant carping and complaining."
    "I guess she's so used to it that it seems normal...or maybe grousing like that turns her on?"
    palla.say "Well, at least I get treated to an actual bed this time!"
    mike.say "I didn't hear you complaining the last time."
    palla.say "Erm, hello...we were fucking in a three foot square cubicle surrounded by strangers."
    palla.say "At least now we won't have someone walk in on us."
    show palla annoyed
    palla.say "Unless it's one of those two skanks that you live with!"
    "My face must show my exasperation at this last comment, as Palla smiles with sudden relish."
    show palla happy
    palla.say "Oh, have I hit a nerve?"
    show palla joke
    palla.say "Or is that something you were hoping might happen?"
    "That's it, she's really pushing my buttons now."
    "I'm mad, but not enough to do anything truly stupid - but does she realise that?"
    mike.say "Okay, Palla - it's time I shut you up and gave you just what you're asking for."
    show palla naked surprised blush
    "Palla's expression becomes more than a little shocked, and she begins to say something in protest."
    show palla at center, zoomAt(1.5, (640, 1040)) with hpunch
    "But I'm on the bed and onto her before she can get as much as a word out."
    "I know I'm banking on my hunch being right, that Palla's goading me into dominating her more than a little."
    "But I'm committed now, so I'd look like a massive tool if I backed off now."
    with hpunch
    "I put a hand in her hair and get a good grip."
    "Not yanking painfully, but firm enough to make her think it might go that way if she struggles."
    palla.say "Hey, - what the hell?!?"
    hide palla
    show palla naked blush
    with vpunch
    "From there I guide her onto all fours, facing away from me, buttocks pointed in my direction."
    "Despite my hold on her hair, Palla tries to look back over her shoulder at me."
    "I catch a glimpse of surprise, anticipation and maybe even a little bit of fear in her eyes."
    call palla_doggy_menu from _call_palla_doggy_menu
    "Palla remains silent afterwards, and I don't feel like I have anything to say either."
    "Though she's not speaking to me, she's notably not tearing a strip off of me for what I did to her either."
    "In the silence, I reflect on the fact that, ironically, we seem to have communicated far better just now than ever before."
    "And all without either of us saying a single word."

    $ palla.flags.nodate = True
    $ palla.flags.talksex = True
    return

label palla_fuck_date_second:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ DONE["palla_fuck_date_second"] = game.days_played
    scene bg house
    show palla
    with fade
    "When we get to the house, Palla looks it up and down."
    palla.say "You live in a suburban wasteland, [hero.name]."
    mike.say "Sure, but it's MY suburban wasteland."
    scene bg livingroom
    show palla
    with fade
    palla.say "I don't understand why you live here anyway. You make good money, you don't need those bimbo roommates."
    menu:
        "Ignore it":
            pass
        "Roommates are off limits!":
            mike.say "Time out, Palla. [bree.name] and Sasha are off limits. You can say what you want about me, about my house, about my job."
            mike.say "But if you can't come up with something nice to say about them, don't talk about them at all."
            show palla joke
            palla.say "What, you going to kick me out?"
            mike.say "They live here, you don't. I've got a good relationship with them."
            if Harem.find_by_name("home"):
                palla.say "Oh yes, I know all about your good relationship with them."
                mike.say "Jealous, much?"
                show palla flirt
                palla.say "No way, like I said before, I think it's kind of hot."
                mike.say "Then be nice to them!"
                show palla annoyed
                "Palla rolls her eyes at me."
            show palla annoyed
            palla.say "Fine, whatever."
            $ palla.sub += 3
    show palla normal
    palla.say "Let's just get to your bedroom so I don't have to look at this place any more."
    mike.say "Are you {b}trying{/b} to piss me off?"
    palla.say "Hey, you know how you said I was hot when I'm angry?"
    show palla wink
    palla.say "Well, same's true for you, [hero.name]. That really gets me wet!"
    show palla normal
    palla.say "Now, are you going to come fuck me senseless or what?"
    hide palla with easeoutleft
    "And with that, she darts toward my room and I actually have to chase her."
    play sound ["<from 0 to 0.2>sd/SFX/fight/woosh_punch.ogg", "<from 2.4 to 3.4>sd/SFX/doors/door_banging.ogg"]
    pause 0.2
    scene bg bedroom1
    show palla at right
    with hpunch
    "She runs down the stairs and into my bedroom and nearly slams the door in my face. I put my arms up just in time, and it SLAMS back open."
    mike.say "Hey! Be quiet, I have roommates!"
    show palla joke
    palla.say "Fuck 'em."
    show palla at center with ease
    "That's it. That's absolutely it. I close the door behind me, this time trying not to slam."
    show palla normal
    mike.say "No, fuck YOU. Now take your clothes off and shut up, bitch, before I decide to kick your ass out."
    if palla.sub < 30:
        palla.say "Fuck you, [hero.name], don't talk to me like that!"
        menu:
            "Kick her out":
                mike.say "That's it! I've had it with you. Get out!"
                show palla sad
                palla.say "Wait, no! I just got here and we had a good time, and I was just..."
                menu:
                    "I'm serious, get out":
                        mike.say "I'm serious, get the fuck out of my house."
                        show palla angry
                        "Palla's face goes through a series of expressions: angry, sad, humiliated, and then finally back to angry."
                        hide palla with easeoutright
                        "She grabs her stuff and storms out of the house."
                        $ palla.flags.nodate = True
                        $ palla.flags.nokiss = True
                        return "leave_without_gain"
            "Be nicer":
                "It takes some effort, but I decide to be nicer. It's tough, given how much she's been spinning me up."
                mike.say "If you want me to be nicer, don't purposefully make me angry."
                mike.say "Now, please, take your clothes off."
                show palla annoyed
                "Palla does so, but she actually looks a little disappointed. I guess I shouldn't be surprised, it's obvious she wanted me angry."
                $ palla.love += 1
            "Make her":
                mike.say "Take your clothes off, Palla, or I will get the belt out and punish you."
                show palla surprised
                "Palla's eyes go wide."
                show palla blush
                palla.say "Punish me?"
                mike.say "I will whip that ass so red you won't feel it when I stick my dick in your ass."
                "I expect her to fight it more, but she doesn't! She quickly starts undressing."
                $ palla.sub += 5
    else:
        "Palla looks, for a moment, like she's going to object, but then suddenly her clothes start to come off."
    show palla flirt underwear with dissolve
    mike.say "And now the bra and panties."
    palla.say "You first."
    mike.say "{b}Now{/b}!"
    "Palla does what she is told, and when the bra comes off, I see that her nipples are hard as rocks."
    show palla naked with dissolve
    mike.say "Now, get down on all fours."
    if palla.flags.anal:
        palla.say "Please don't fuck my ass again!"
    else:
        palla.say "Please don't fuck my ass! It'll hurt!"
    mike.say "I will fuck you wherever I please. Now get on all fours!"
    "Palla moves only very slowly to do what she's told, so I step up and help her out, grabbing her hair and roughly moving her into position."
    "She doesn't resist at all, though she does continue pleading me not to do her ass."
    call palla_doggy_menu from _call_palla_doggy_menu_1
    "Palla moans quietly after I pull out of her, and she rolls over to look up at me."
    show cuddle palla with fade
    "I drop myself down and lay next to her. She pulls close and cuddles for a bit, and I see something I rarely see in her: True happiness."
    "I reflect that the thing this haughty and it turns out naughty bitch really wants is to be taken rough."
    "And I admit I do enjoy doing that."
    return

label palla_fuck_date_third:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ DONE["palla_fuck_date_third"] = game.days_played
    call palla_fuck_date_intro_male (location) from _call_palla_fuck_date_intro_1
    menu:
        "Fuck her from behind":
            mike.say "Now, get down on all fours."
            if palla.flags.anal == 0:
                palla.say "Please don't fuck my ass! It'll hurt!"
            elif palla.flags.anal < 3:
                palla.say "Please don't fuck my ass again!"
            else:
                palla.say "Are you going to fuck my ass again?"
            mike.say "I will fuck you wherever I please. Now get on all fours!"
            "Palla moves only very slowly to do what she's told, so I step up and help her out, grabbing her hair and roughly moving her into position."
            "She doesn't resist at all, though she does continue pleading me not to do her ass."
            call palla_doggy_menu from _call_palla_doggy_menu_2
            "Palla moans quietly after I pull out of her, and she rolls over to look up at me."
            $ palla.flags.anal += 1
        "Fuck her on her back":
            mike.say "Lie down on the bed and spread your legs. Wide."
            "Palla just stands there."
            mike.say "Do as you're told!"
            "Palla offers me a wry smile."
            palla.say "Make me!"
            "If that's what she wants...I walk up to her, take her by the shoulders and throw her roughly on the bed."
            show palla missionary out with fade
            "I stand over her, with my dick out. Her pussy is wet and ready. So am I, but I also realize I want to savor this moment too."
            mike.say "You ready for this big cock, bitch?"
            palla.say "Get on with it already!"
            mike.say "Not until you're ready."
            palla.say "What?"
            mike.say "Beg for it. Beg me to stick this giant cock inside your hole."
            palla.say "No, I'm not begging!"
            mike.say "Oh. So you don't want it?"
            "I start to draw back from her. Her eyes go wide as I pull away."
            palla.say "Don't!"
            mike.say "Then you know what to do."
            palla.say "Please?"
            mike.say "Beg."
            "Palla bites her lip, resisting. But the humiliation is continuing to turn her on, as evidence by her wet pussy actively dripping now."
            palla.say "Put it in me. Put your big cock in me."
            $ palla.love += 5
            menu:
                "Fuck her pussy with a condom" if hero.has_condom():
                    $ CONDOM = hero.use_condom()
                    "I only pause long enough to slip a condom on, before lining myself up with Palla's exposed pussy. And then I thrust it in. I want to take it slow, but I'm so turned on I just can't, and I go all the way in on the first try."
                    show palla missionary condom pleasure
                    "Palla shrieks. As wet and ready as she was, she wasn't quite ready for that."
                    "I slowly withdraw about halfway, and then pound in again. Her slick mound surrounds me, gripping my cock tightly."
                    palla.say "Oh. Oh [hero.name]!"
                    "I set myself up into a rhythm, struggling to keep it slow so I don't just orgasm right away."
                    show palla missionary pleasure
                    "With each thrust, Palla moans louder."
                    palla.say "Fuck me harder!"
                    with vpunch
                    "I speed up, and she grips the sheets so hard she nearly rips them off the bed. It doesn't take long..."
                    show palla missionary ahegao with vpunch
                    "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                    show palla missionary with vpunch
                    "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into the latex that covers my cock."
                    with vpunch
                "Fuck her pussy raw":
                    "I slip my cock into her dripping pussy and, grasping her by the hips, thrust myself all the way inside."
                    show palla missionary vaginal
                    "Palla shrieks. As wet and ready as she was, she wasn't quite ready for that."
                    "I slowly withdraw about halfway, and then pound in again. Her slick mound surrounds me, gripping my cock tightly."
                    palla.say "Oh. Oh [hero.name]!"
                    "I set myself up into a rhythm, struggling to keep it slow so I don't just orgasm right away."
                    show palla missionary pleasure
                    "With each thrust, Palla moans louder."
                    palla.say "Fuck me harder!"
                    "I speed up, and she grips the sheets so hard she nearly rips them off the bed. It doesn't take long..."
                    show palla missionary ahegao with vpunch
                    "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                    menu:
                        "Pull out":
                            "Realizing that her orgasm is about to make me explode, I quickly pull my cock out of her."
                            show belly_insert palla cum zorder 1 at zoomAt(1, (20, 120))
                            show palla missionary cumshot out pleasure
                            with vpunch
                            "I'm just barely clear of her when I spray my load all over her."
                            show palla missionary -cumshot cum onbody with vpunch
                            "There's something about the sight of Palla, lying there on her back with my cum all over her belly. It makes me feel possessive, like I've won something."
                        "Cum inside":
                            show palla missionary cumshot with vpunch
                            "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                            show pussy_insert palla cum zorder 1 at zoomAt(0.75, (780, 420))
                            $ palla.impregnate()
                    "When I'm finally spent, I just stand there, panting, looking down at her."
                    "And for a moment, there's no abusive banter between us. We're not an asshole and a bitch. We're just two people, who shared an intimate moment. And it was really, really good."
                "Fuck her ass" if palla.sub >= 25:
                    "There's something about sticking my huge cock in Palla's tight asshole that is just about the most arousing thing I can think of."
                    $ palla.love += 5
                    $ palla.sub += 5
                    if palla.flags.anal > 5:
                        mike.say "Well, I guess after the punishment I've given her, it isn't that tight anymore."
                        "I press my dick into the pucker of her ass, which willingly opens up for me. Enough of her pussy juice has already dripped down to her anus that her ass is ready, and it takes a little effort, but I get all the way into her."
                    else:
                        "I touch my cock to her waiting anus, and Palla shrieks even before I get in."
                        palla.say "No no no! You are not going in the back door this time!"
                        mike.say "Shut up, bitch. You're going to take it, and you're going to take it again. And again and again."
                        "And to show her I mean it, I shove it in. It only gets in as far as the head before I can't push any further, but that's all right."
                        "Palla shrieks again."
                        mike.say "Your ass is mine for the taking."
                        "Except for the problem that I can't get in there. But...her pussy is wet and ready. There's lubricant right there!"
                        show palla missionary vaginal pleasure
                        "So I pull out and shove it all the way into her cunt. I stroke a couple of times just to get it wet."
                        palla.say "Oh, thank--"
                        "...and once it is wet, back to her ass. And with the fresh lubricant, I'm able to fit it all the way in, albeit with a little work."
                    show palla missionary anal pleasure
                    palla.say "{b}Ow!{/b} Ow ow that hurts, you monster!"
                    mike.say "Give it a minute!"
                    "I thrust in and out of her. Each time is accompanied with a shriek. The first few times it's a shriek of pain."
                    show palla missionary anal normal
                    "But it doesn't take long before her shrieks of pain turn into shrieks of pleasure."
                    mike.say "Yeah, bitch, how do you like me now?"
                    if palla.love >= 160:
                        palla.say "I love you!"
                        "Her words are slurred from the pounding, but they're music to my ears nonetheless."
                    else:
                        palla.say "I hate you! I hate this!"
                        mike.say "Your words say one thing, my darling. But your body says quite another."
                    mike.say "Do you want me to stop?"
                    if palla.love < 160 and palla.sub < 60:
                        palla.say "Yes!"
                        mike.say "Too bad. Your ass is mine."
                    else:
                        palla.say "No!"
                        mike.say "Even if it hurts?"
                        palla.say "Fuck you!"
                    with vpunch
                    "And with that, I can't hold back any more."
                    show palla missionary anal ahegao cumshot with vpunch
                    "My load spills deep into Palla's ass, filling her with my hot liquid."
                    with vpunch
                    palla.say "Oh. Oh fuck, oh fuck oh fuck."
                    mike.say "You okay?"
                    palla.say "Oh fuck I'm coming too!"
                    "When I look down, I see that glops of her pussy juice are mixing with my semen right where my dick is disappearing into her anus."
                    mike.say "And here I thought you hated this."
                    palla.say "Fuck you!"
                    mike.say "I think you just did, hon."
                    $ palla.flags.anal += 1
        "Let her be on top":
            "I lie down on the bed, turning my hips so that my stiff cock points straight up."
            mike.say "Get on."
            palla.say "Really. You actually want me to be on top?"
            mike.say "Do you want my cock?"
            palla.say "Oh. Oh fuck yes, I want that thing inside me!"
            mike.say "Then get your sexy ass on me!"
            $ palla.love += 5
            show palla cowgirl outside pleasure
            "Palla crawls atop me, and my cock touches just between her asscheeks."
            palla.say "Now what, big guy?"
            menu:
                "Fuck her pussy with a condom" if hero.has_condom():
                    "I put on a condom and thrust my cock deep into her wet, waiting pussy."
                    show palla cowgirl condom pleasure
                    palla.say "Mmmm, oh fuck, [hero.name]!"
                    "I grab her hips with my hands, pulling her down against me as I thrust up, then pushing her up and away as I pull out."
                    "She works with me and we get a good rhythm going."
                    palla.say "Ohhhhhhh!"
                    palla.say "Faster, [hero.name]! Fuck me harder!"
                    show palla cowgirl ahegao with vpunch
                    "So I do, moving faster and faster until finally I explode, filling the condom with the hot, sticky mess that is my load."
                    with vpunch
                    palla.say "Oh god, I'm coming!"
                    with vpunch
                    "Palla's orgasm is almost violent, and it's almost like she is dancing on top of me. Her legs squeeze my hips and push me deeper into the bed."
                    palla.say "That...was fucking amazing!"
                    if palla.love < 180:
                        $ palla.sub -= 5
                "Fuck her pussy raw":
                    "I slip my cock into her dripping pussy and, grasping her by the hips, thrust myself all the way up inside her."
                    show palla cowgirl vaginal pleasure
                    palla.say "Mmmm, oh fuck, [hero.name]!"
                    "I grab her hips with my hands, pulling her down against me as I thrust up, then pushing her up and away as I pull out."
                    "She works with me and we get a good rhythm going."
                    "With each thrust, Palla moans louder."
                    palla.say "Fuck me harder!"
                    "I speed up, and she grabs my shoulders so hard she leaves claw marks on them. It doesn't take long..."
                    show palla cowgirl ahegao with vpunch
                    "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                    menu:
                        "Pull out":
                            "Realizing that her orgasm is about to make me explode, I quickly pull my cock out of her."
                            show palla cowgirl outside cum pleasure with vpunch
                            "I'm just barely clear of her when I spray my load all over her back."
                            show palla cowgirl after pleasure with vpunch
                            if palla.love < 180:
                                $ palla.sub -= 5
                        "Cum inside":
                            show palla cowgirl cum with vpunch
                            "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                            $ palla.impregnate()
                "Fuck her ass" if palla.sub >= 25:
                    "There's something about sticking my huge cock in Palla's tight asshole that is just about the most arousing thing I can think of."
                    $ palla.love += 5
                    $ palla.sub += 5
                    if palla.flags.anal > 5:
                        mike.say "Well, I guess after the punishment I've given her, it isn't that tight anymore."
                        "I press my dick into the pucker of her ass, which willingly opens up for me. Enough of her pussy juice has already dripped down to her anus that her ass is ready, and it takes a little effort, but I get all the way into her."
                    else:
                        "I touch my cock to her waiting anus, and Palla shrieks even before I get in."
                        palla.say "No no no! You are not going in the back door this time!"
                        mike.say "Shut up, bitch. You're going to take it, and you're going to take it again. And again and again."
                        "And to show her I mean it, I shove it in. It only gets in as far as the head before I can't push any further, but that's all right."
                        "Palla shrieks again."
                        mike.say "Your ass is mine for the taking."
                        "Except for the problem that I can't get in there. But...her pussy is wet and ready. There's lubricant right there!"
                        show palla cowgirl vaginal pleasure
                        "So I pull out and shove it all the way into her cunt. I stroke a couple of times just to get it wet."
                        palla.say "Oh, thank--"
                        "...and once it is wet, back to her ass. And with the fresh lubricant, I'm able to fit it all the way in, albeit with a little work."
                    show palla cowgirl anal pain
                    palla.say "{b}Ow!{/b} Ow ow that hurts, you monster!"
                    mike.say "Give it a minute!"
                    "I thrust in and out of her. Each time is accompanied with a shriek. The first few times it's a shriek of pain."
                    show palla cowgirl anal ahegao
                    "But it doesn't take long before her shrieks of pain turn into shrieks of pleasure."
                    mike.say "Yeah, bitch, how do you like me now?"
                    if palla.love >= 160:
                        palla.say "I love you!"
                        "Her words are slurred from the pounding, but they're music to my ears nonetheless."
                    else:
                        palla.say "I hate you! I hate this!"
                        mike.say "Your words say one thing, my darling. But your body says quite another."
                    mike.say "Do you want me to stop?"
                    if palla.love < 160 and palla.sub < 60:
                        palla.say "Yes!"
                        mike.say "Too bad. Your ass is mine."
                    else:
                        palla.say "No!"
                        mike.say "Even if it hurts?"
                        palla.say "Fuck you!"
                    with vpunch
                    "And with that, I can't hold back any more."
                    show palla cowgirl anal ahegao cum with vpunch
                    "My load spills deep into Palla's ass, filling her with my hot liquid."
                    with vpunch
                    palla.say "Oh. Oh fuck, oh fuck oh fuck."
                    mike.say "You okay?"
                    palla.say "Oh fuck I'm coming too!"
                    "When I look down, I see that glops of her pussy juice are mixing with my semen right where my dick is disappearing into her anus."
                    mike.say "And here I thought you hated this."
                    palla.say "Fuck you!"
                    mike.say "I think you just did, hon."
                    $ palla.flags.anal += 1
    hide belly_insert
    hide pussy_insert
    "I drop myself down and lay next to her. She pulls close and cuddles for a bit, and I see something I rarely see in her: True happiness."
    "I reflect that the thing this haughty and it turns out naughty bitch really wants is to be taken rough."
    "And I admit I do enjoy doing that."
    return

label palla_fuck_date_spank:
    "I'm pretty sure that Palla's up for it right now."
    "But there's just something weird about how she's acting."
    "She's normally all stuck-up and superior, demanding what she wants."
    "Yet right now she doesn't seem to be able to tell me what that is!"
    show palla blush
    palla.say "I..."
    palla.say "I'd..."
    show palla sad
    palla.say "Oh dear..."
    mike.say "What is it, Palla?"
    mike.say "What are you trying to ask me for?"
    "I look on in amazement as Palla actually starts to flush with colour."
    "The rude, demanding girl that I'm dating normally relishes confrontation."
    "But here she is blushing!"
    palla.say "The other day..."
    palla.say "When you got mad with me..."
    mike.say "Erm..."
    mike.say "Yeah, Palla..."
    mike.say "I meant to say sorry about that!"
    "As soon as I begin to apologise, Palla rushes to stop me."
    show palla blush
    palla.say "No!"
    palla.say "Oh no!"
    palla.say "Don't say sorry, [hero.name]!"
    palla.say "Nobody ever put me in my place like that before."
    palla.say "It made me feel bad...but in a good way!"
    show palla sad
    palla.say "Does that make sense to you?"
    "I can feel a smile spreading across my face as she says this."
    "Because I'm starting to realise what all of this is about."
    mike.say "Oh really?"
    mike.say "Well, Palla..."
    mike.say "It sounds to me like being called a bad girl turns you on!"
    mike.say "I think you secretly like being punished too!"
    show palla blush
    "Palla looks more than a little worried as she digests all of this."
    show palla flirt
    "But then she bites her lip and nods."
    palla.say "I...I think you might be right!"
    palla.say "Would you...would you punish me some more?"
    "Still smiling, I sit down and beckon Palla over to me."
    "She does as she's told, still looking unsure of herself."
    mike.say "You know what, Palla..."
    mike.say "Bad girls should always be spanked."
    mike.say "Spanked until they learn their lesson!"
    "I gesture to my lap."
    "And for a moment I honestly think Palla's going to refuse the invitation."
    hide palla
    show palla close normal
    "But then she looks left and right, before lowering herself over my thighs."
    show palla spank with fade
    "I'm still smiling as I feel Palla's weight in my lap."
    "It feels good."
    "And I can already feel the effect it's having on me down there."
    show palla spank down
    "With one hand I take hold of her skirt and lift it up."
    "And I don't stop until I've exposed her ass, panties and all."
    "Then I pull these down to, showing off her bare buttocks."
    "Palla shivers and lets out a squeal of anticipation."
    mike.say "You've been a bad girl, Palla."
    mike.say "But this is going to hurt me more than it hurts you!"
    "Who am I trying to kid?"
    "I'm loving every moment of this!"
    show palla spank speed
    pause .25
    show palla spank hit impact surprised
    play sound spank
    "The first slap makes a sound like a whip cracking."
    "Palla squeals again and squirms around in my lap."
    show palla spank middle -impact
    pause .25
    show palla spank speed
    pause .25
    show palla spank hit impact
    play sound spank
    "I land a second one before she has the chance to recover from the first."
    "And the effect is even more pronounced this time around!"
    show palla spank hit -impact pleasure
    palla.say "Ah!"
    palla.say "Mmm..."
    palla.say "Oh god!"
    show palla spank middle
    pause .25
    show palla spank speed
    pause .25
    show palla spank hit impact surprised
    play sound spank
    pause .25
    show palla spank middle -impact pleasure
    pause .25
    show palla spank speed
    pause .25
    show palla spank hit impact marks surprised
    play sound spank
    pause .25
    "A third and then a fourth slap follow soon afterwards."
    "Then I'm away, the task at hand totally taking over."
    "My hand paddles Palla's ass without pausing for a second."
    "And soon I can see red patches beginning to appear on her cheeks."
    show palla spank hit -impact marks pleasure
    palla.say "Oh yeah..."
    palla.say "Spank me harder!"
    palla.say "I'm a bad...BAD girl!"
    "All this time Palla's wriggling around on top of my cock."
    "Which is hard as rock from what we're doing."
    $ palla.sub += 2
    show palla spank middle
    pause .15
    show palla spank speed
    pause .15
    play sound spank
    show palla spank hit impact surprised with hpunch
    pause .15
    show palla spank middle pleasure -impact
    pause .15
    show palla spank speed
    pause .15
    play sound spank
    show palla spank hit impact surprised with hpunch
    pause .15
    show palla spank middle pleasure -impact
    pause .15
    show palla spank speed
    pause .15
    play sound spank
    show palla spank hit impact surprised with hpunch
    "I can feel my own hand starting to get numb by now."
    "So maybe Palla's had enough?"
    show palla spank middle pleasure -impact
    "Once I stop, she sags over my knees like a rag-doll."
    "But I can hear her trying to say something all the same."
    palla.say "P...please..."
    palla.say "Please, [hero.name]..."
    palla.say "Fuck me...I want you to fuck me!"
    return

label palla_doggy_menu:
    $ game.play_music("music/roa_music/city_nights.ogg")
    menu:
        "Fuck her pussy with a condom" if hero.has_condom():
            $ CONDOM = hero.use_condom()
            show palla doggy with fade
            "I only pause long enough to slip a condom on, before lining myself up with Palla's exposed pussy."
            palla.say "What's going on back there?"
            "Without explaining a single thing to her, I thrust forwards and force myself into her with some considerable urgency."
            palla.say "Wha...aaa...aaah!"
            "Despite her protests, Palla's more than ready to take me in."
            "Her pussy is already wet and accommodating, her muscles yielding without similar protests as I begin to push in and out."
            "Palla's arms tremble at first, trying to keep her upright as she begins to quiver from the sensation of being roughly fucked from behind."
            "Then they simply collapse as she sags forwards amongst the sheets, allowing me to get an even more acute angle inside of her."
            show palla doggy orgasm
            "She's still making some small mewling sounds, perhaps the last gasp of her previous protests."
            "But even these are muffled into almost nothing by the sheets."
            "I redouble my efforts, feeling my ardour rise as Palla starts to yelp in response to each more intense thrust into her."
            if not CONDOM and not palla.flags.pill:
                $ palla.impregnate()
        "Fuck her pussy raw":
            $ palla.love += 5
            show palla doggy with fade
            if palla.sexperience < 3 or palla.sub < 40:
                palla.say "Hey, what are you..."
                "That's all she manages to get out before I stroke my cock against the lips of her pussy and begin to slowly push into her."
                palla.say "Ohh...noo...ohh!"
                "While she might have been making sounds of disapproval, the slick feeling of Palla's pussy reveals the truth of the matter."
                "Another time I might have slowed down and really tried to savour the sensation of making Palla twitch and writhe like this."
                "But her queen bitch attitude only makes me want to fuck her ever harder and faster."
                "She's stopped protesting now, and begun to merely moan in response to the ferocity of my thrusts into her."
            else:
                "I hear Palla take a sharp breath as I press my cock up against the lips of her pussy."
                "She cries out in delight as I sink into her."
                "She responds by pressing her ass back into me, and as she does so I pull on her hair, eliciting another cry of joy."
                palla.say "Yes, [hero.name], faster! Harder!"
            "Palla sags forward into the sheets and pillows, the motion of being banged so hard from behind driving her downwards."
            "From this angle there's nothing to stop me pounding her with almost all of my weight, and I do so."
            "I try not to think that I'm punishing Palla, more like disciplining her in a roundabout way."
            show palla doggy orgasm
            "Every thrust that elicits a moan of enforced pleasure feels like an appropriate reply to her earlier catty and annoying jibes."
            $ palla.impregnate()
        "Fuck her ass" if palla.sub >= 25:
            $ palla.love += 5
            $ palla.sub += 5
            show palla doggy with fade
            if palla.flags.anal < 1:
                "Even though Palla is already on all-fours and fully open to me, it's not enough for what I have in mind."
                "Without asking permission, I push her arms out from under her and send her face tumbling into the piled sheets."
                "This only succeeds in muffling her protests for a moment, as she can already feel just where the head of my cock is probing now that her anus is full exposed."
                palla.say "Oh god, - not that!"
                "I ignore her completely, grabbing a handful of hair on her scalp in my right hand and gripping a ponytail's worth behind her head with my left."
                palla.say "Please, please, please - don't fuck me in the ass!"
                palla.say "Please - I don't even like the thought of it!"
                "By now I have the tip of my dick all lined up and ready to go, and I know she can tell I'm teetering on the brink."
                palla.say "PLEASE, I'm begging you not to!"
                palla.say "I hate it...I hate it...it'll...hurt me..."
                "Were it not for her bitchy comments and acid tongue, I might have been moved by her pleas."
                "But as it is, I think that she's about to get what she so richly deserves."
                "Keeping a firm hold on Palla's hair, I force my cock into her unwilling ass."
                show palla doggy orgasm
                "She shivers bodily as I enter her anus, making a deep moaning sound that turns into quieter whimpers as the full length slides inside of her."
                "I hold myself quite still once I've pushed in as far as I can manage, enjoying the sensation of Palla's muscles quivering around my cock."
                "At first I keep my movements small and slow, only building up speed a little at a time."
                "Palla continues to make incoherent sounds that are part pain and part humiliation."
                show palla doggy ahegao
                "But as my thrusts become more intense and lengthy, the sounds begin to rise in volume and change in tone."
                "They turn back into whimpers, then into moans, and finally evolve into what I can only describe as almost cries of increasing pleasure."
                "The change affects me as well, knowing that the humiliation Palla's feeling has somehow broken through her catty demeanour and laid her wide open."
                "The more she cries in guilty pleasure, the closer I come to losing myself, deep in her anus."
            else:
                mike.say "Ready for another ass-pounding?"
                if palla.sub > 80:
                    "Palla spreads her cheeks wide for me, at the same time burying her face and chest into the pillows."
                    "I line myself up and press the tip right against her anus, pushing it open just slightly, but not entering."
                    mike.say "Tell me you want it."
                    palla.say "I...I want it."
                    mike.say "Tell me you need it."
                    palla.say "I need it, [hero.name], I need it!"
                    mike.say "Tell me you LOVE it!"
                    "Palla's breathing gets heavier, even though I haven't even started."
                    palla.say "I love it, [hero.name]! Oh God, I love it!"
                    if palla.love > 190:
                        palla.say "And I love you too!"
                    "The talk has made me as hard I've ever been, and I press into her anus. It gives way easily and I plunge in."
                    "Palla shrieks into the sheets, her muffled cries a combination of pain and pleasure."
                    show palla doggy orgasm
                    "And on my really hard thrusts, my hands pull her away from the sheets by her hair. It must hurt, but she loves it so much I can't tell."
                    "I thrust back and forth, not sparing her at all as I may have in the past."
                    "Her cries get louder, and after a few moments, I join her with a guttural yelp."
                    mike.say "Take THAT, bitch!"
                    mike.say "And THAT!"
                    show palla doggy ahegao
                    "Palla's cries might've included a yes, but she is so beyond words it was hard to tell."
                    "It doesn't take me long before I'm ready to blow, either."
                else:
                    palla.say "No, please! Not again! It hurts! It's torture!"
                    mike.say "And you love it, bitch! Open up and take it!"
                    "Palla buries her face in the sheets and despite her protestations, her asshole is open and ready for me."
                    "I line myself up and press the tip right against her anus, pushing it open just slightly, but not entering."
                    mike.say "Tell me you want it."
                    palla.say "Mmf! No! I don't want it!"
                    "I smack her across one ass cheek; hard enough to make a good snapping sound, but not hard enough to hurt. Much."
                    "Palla yelps!"
                    mike.say "Tell me you want it."
                    palla.say "I don...no...I don...I want it."
                    "I press myself into her anus, pushing just the head in to open her up."
                    mike.say "Say it again, bitch!"
                    "Palla nearly cries out, this time."
                    palla.say "I want it!"
                    mike.say "You want it!"
                    palla.say "I want it!"
                    "The talk has made me as hard I've ever been, and I press into her anus. It gives way easily and I plunge in."
                    "Palla shrieks into the sheets, her muffled cries a combination of pain and pleasure."
                    show palla doggy orgasm
                    "And on my really hard thrusts, my hands pull her away from the sheets by her hair. It must hurt, but she loves it so much I can't tell."
                    "I thrust back and forth, not sparing her at all as I may have in the past."
                    "Her cries get louder, and after a few moments, I join her with a guttural yelp."
                    mike.say "Take THAT, bitch!"
                    mike.say "And THAT!"
                    show palla doggy ahegao
                    "Palla's cries might've included a yes, but she is so beyond words it was hard to tell."
                    "It doesn't take me long before I'm ready to blow, either."
            $ palla.flags.anal += 1
    "With Palla's almost ragged cries ringing in my ears, I know it's only going to be a matter of seconds before I inevitably cum."
    menu:
        "Cum inside":
            "After managing to humble Palla like that, the last thing I'm about to do is keep from cumming inside of her."
            "I tighten my grip on her hair and the intensified pain of this goes some way to keeping the tell-tale signs of my muscles twitching from her notice."
            with hpunch
            "This means that when I finally lose myself inside of her, Palla is taken almost completely by surprise."
            with hpunch
            "She writhes and groans as my climax goes off entirely within one of the most sensitive parts of her body."
            with hpunch
            "But my firm grip and her submissive position mean that she can only endure it, even when her own orgasm overtakes her too."
        "Pull out":
            "I might have been able to make Palla shut up and take it how I wanted to give it to her."
            "But I see that there's another way I can humble her - by pulling out and giving her a little shower to end things with."
            "Palla makes a long and almost mournful sound as I extricate myself from her and aim my dick over her back."
            with hpunch
            "When my orgasm comes over me a few seconds later, cum sprays down over her, landing in her hair and splattering down her back."
            with hpunch
            "Palla remains crouched there, feeling the aftershocks of having me inside her, with fast-cooling cum running off her back and down her sides to drip onto the sheets below."
    return

label palla_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show palla naked
        if palla.love < 160 and palla.sub < 70:
            "Palla starts gathering up her belongings, clearly getting ready to leave."
            menu:
                "Stay":
                    mike.say "What, you're just going to leave? After that?"
                    palla.say "Yep!"
                    "She seems cheerful as she starts getting dressed."
                    mike.say "You should stay."
                    palla.say "Why would I want to do that?"
                    mike.say "If not for the cuddling, then how about for the morning sex?"
                    "Palla laughs."
                    if palla.sub < 30:
                        palla.say "Morning sex and morning breath. No thanks."
                        "And with that, Palla makes her way out."
                        "I fall asleep alone, but at least I'm satisfied."
                        call sleep from _call_sleep_122
                        $ game.room = "bedroom1"
                        return
                    else:
                        palla.say "You're not very convincing."
                        mike.say "How about...get your sexy ass in my bed so I wake up to something beautiful?"
                        palla.say "Wow, that...that's more charming than you can usually manage. Was the sex that good?"
                        mike.say "It wasn't bad."
                        "She raises both her eyebrows."
                        palla.say "I'm supposed to stay for \"It wasn't bad\"?"
                        mike.say "I just don't want your head to get too big."
                        "She taps her foot on the floor."
                        mike.say "Fine, it was fantastic? Are you going to lay down now?"
                        show cuddle palla
                        "Palla lays down beside me and a broad smile adorns her face."
                        call palla_sleep_pillow_talk from _palla_sleep_date_fuck
                "Let her go":
                    "Palla makes her way out without another word."
                    call sleep from _call_sleep_32
                    $ game.room = "bedroom1"
                    return
        else:
            menu:
                "You should leave":
                    mike.say "I am done with you and I have to get up early tomorrow, you should leave."
                    palla.say "Oh. I...fine. I won't stay where I'm not wanted."
                    "Frowning, Palla goes to collect her clothes from where she'd let it fall earlier."
                    "She then heads up the stairs."
                    $ palla.love -= 5
                    $ palla.sub += 1
                    call sleep from _call_sleep_37
                    $ game.room = "bedroom1"
                    return
                "You should sleep here":
                    show cuddle palla
                    mike.say "Stay with me so I have something beautiful to wake up to."
                    if palla.is_sex_slave:
                        palla.say "Yes, Master."
                    else:
                        palla.say "Well how can I refuse an invitation like that?"
                    "We curl up spooning together in bed, drifting toward sleep."
                    $ palla.love += 1
                    call palla_sleep_pillow_talk from _palla_sleep_date_fuck2
    call sleep ("palla") from _call_sleep_8
    $ game.room = "bedroom1"
    return

label palla_sleep_pillow_talk:
    show cuddle palla
    $ renpy.dynamic("topics", "topic")
    $ topics = ["smell", "me", "big_dick"]
    if "palla_sleep_pillow_talk_audrey" not in DONE:
        $ topics.append("audrey")
    if "palla_sleep_pillow_talk_piercings" not in DONE and (palla.piercings.nipples.worn or palla.piercings.clit.worn):
        $ topics.append("piercings")
    if palla.love >= 180:
        $ topics.append("love")
    if palla.love < 160 or not "palla_event_07b" in DONE:
        $ topics.append("thing")
    $ topic = randchoice(topics)
    call expression "palla_sleep_pillow_talk_" + topic from _palla_sleep_pillow_talk
    return

label palla_sleep_pillow_talk_thing:
    "As Palla nuzzles my shoulder and drifts off to sleep, I can hear her voice, just barely a whisper."
    palla.say "Don't think this means we're a thing, though."
    return

label palla_sleep_pillow_talk_love:
    "As Palla nuzzles my shoulder and drifts off to sleep, I can hear her voice, just barely a whisper."
    palla.say "I love you, [hero.name]! Thanks for..."
    "But she falls asleep before she can finish."
    return

label palla_sleep_pillow_talk_smell:
    "As Palla nuzzles my shoulder and drifts off to sleep, I can hear her voice, just barely a whisper."
    palla.say "You smell so nice after sex. Anyone ever tell you that?"
    return

label palla_sleep_pillow_talk_me:
    "As Palla nuzzles my shoulder and drifts off to sleep, I can hear her voice, just barely a whisper."
    palla.say "Aren't you lucky to have a girl like me sleeping on your shoulder?"
    mike.say "Something like that."
    "But she doesn't hear my response, she's already asleep."
    return

label palla_sleep_pillow_talk_big_dick:
    "As Palla nuzzles my shoulder and drifts off to sleep, I can hear her voice, just barely a whisper."
    palla.say "I love having your big dick inside me, [hero.name]. That's the only reason I stayed."
    return

label palla_sleep_pillow_talk_audrey:
    $ DONE["palla_sleep_pillow_talk_audrey"] = game.days_played
    "Palla lifts her head from my shoulder."
    palla.say "So, what do you think of Audrey?"
    mike.say "At the moment I'm just thinking of you."
    palla.say "That's sweet, really, but I'm serious."
    "I know Audrey is her best friend, but she drives me crazy sometimes. I'm not sure I can safely answer this."
    mike.say "I, uh. She's okay?"
    palla.say "Is she hot?"
    menu:
        "Smokin'":
            mike.say "Yeah, she's smokin' hot. Why?"
        "Not as hot as you":
            mike.say "She's not as hot as you are."
            palla.say "Sure, but no one is, that's not an answer."
            mike.say "Well as long as we're clear on that, yeah she's hot. Why?"
        "Not really":
            mike.say "She's not really my type. Why?"
    palla.say "I was just...imagining you fucking her."
    if audrey.sexperience >= 2:
        palla.say "She told me, you know. She described your cock in loving detail."
        mike.say "Oh. Um, I, uh."
        palla.say "Don't be embarrassed, it's okay. I think it's hot."
        mike.say "You're...definitely unusual that way."
    else:
        palla.say "It's hot. Her, writhing under you, begging you to smack her a few times. She's a kinky bitch, you know."
    mike.say "So why tell me this?"
    "Palla presses her face into my shoulder."
    palla.say "I dunno. I just keep thinking about it, and, you know. What it'd be like. To actually watch you fuck her."
    mike.say "You actually want to do that?"
    palla.say "I dunno! Maybe. Do you want to?"
    menu:
        "Sounds hot":
            mike.say "That sounds hot. Maybe."
            $ palla.lesbian += 1
        "I don't need that":
            mike.say "I don't really need that. You're enough for me."
            $ palla.love += 5
            palla.say "I know you're probably full of it, but that sounds nice anyway."
        "Yes, but not with her" if audrey.sexperience < 1:
            mike.say "Yes, but...not with her. Audrey's not my type. Plus she works for me, that wouldn't be right."
            mike.say "But maybe there's someone else you and I both like."
            $ palla.flags.noaudrey = True
            palla.say "Mm. Maybe. We'll see."
    "And then she drifts off to sleep with her head against my shoulder."
    return

label palla_sleep_pillow_talk_piercings:
    $ DONE["palla_sleep_pillow_talk_piercings"] = game.days_played
    if palla.piercings.nipples.worn:
        "Palla lies next to me, gently fondling the piercings on her nipples with small, almost careless movements."
    else:
        "Palla lies next to me, gently fondling the piercing in her clit with small, almost careless movements."
    palla.say "Why did you get me this, anyway?"
    menu:
        "It makes you beautiful":
            mike.say "Because they make you beautiful."
            palla.say "I'm already beautiful, I spend half my waking hours on it."
            mike.say "Fine, makes you more beautiful."
            palla.say "That's kind of weird."
            mike.say "Kind of beautiful, if you ask me. Which you did."
            $ palla.love += 1
        "To mark you":
            mike.say "To mark you. Those are mine."
            $ palla.sub += 5
            "Palla shivers, and goosebumps run all the way down her body."
            palla.say "Your ego is even bigger than your dick. And you're a pretty big dick."
            mike.say "I think you mean I've got a pretty big dick."
            palla.say "I didn't stutter."
        "I have a thing for them":
            mike.say "I just have a thing for them. They're a giant turn on for me. Not for you?"
            palla.say "I never really thought about it, honestly."
            if palla.sub > 70:
                palla.say "But I'm glad they turn you on."
            $ palla.love += 1
    "And then she drifts off to sleep with her head against my shoulder."
    return

label palla_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "I'm not usually the kind of guy that likes to show off in order to impress a girl."
    "But I do think that having a hot-tub as well as a swimming pool at home is pretty cool."
    "I mean, we never had one when I was growing up and that makes it seem special to me."
    "And yet apparently it's nowhere near enough to impress Palla, not even in the slightest."
    "Sure, she agreed to come over and take a dip with me when I told her about it."
    "But she still managed to make me feel like she was doing me a favour by saying yes."
    "Which leaves me sitting in the bubbling water, feeling a little awkward as I wait for her to join me."
    show palla swimsuit at left with easeinleft
    "That said, the moment she walks out of the house, I forget all about my former misgivings."
    show palla at center with ease
    palla.say "Well, here I am."
    show palla happy
    palla.say "And you're really lucky, [hero.name]."
    show palla normal
    palla.say "Because you're the first person to see me in my new swimsuit!"
    show palla at center, zoomAt(1.5, (640, 1040)) with fade
    "I nod eagerly as Palla walks the short distance to the tub and climbs in."
    "She really didn't need to sell the sight of herself to me, not in the slightest."
    "Palla looks simply stunning right now, a genuine knockout!"
    mike.say "You're right, Palla."
    mike.say "I sure am a lucky guy!"
    "It's impossible for me to hide just how much I love what I'm seeing."
    hide palla
    show hottub palla
    with fade
    "And Palla smiles with equally obvious gratification as she lowers herself into the water."
    "In fact, I'm pretty sure that if she were a cat, she'd be purring like crazy."
    palla.say "Mmm..."
    palla.say "This feels nice, [hero.name]."
    palla.say "Maybe your little hot-tub isn't so bad after all!"
    "I keep on nodding, agreeing with everything that Palla says."
    "Keeping her happy seems to be the best way to go."
    "And it's certainly the best way to keep her open to having some serious fun too."
    mike.say "It's certainly better for having you in it, Palla."
    mike.say "Thanks again for coming over and hopping in here with me!"
    "I can see that buttering her up is having the desired effect."
    "As Palla doesn't hesitate to keep on smiling the whole time."
    "But the real giveaway comes when she begins to inch closer to me as well."
    palla.say "Ah, that's okay, [hero.name]."
    palla.say "It's nice to feel appreciated."
    palla.say "It makes a girl so much more at ease..."
    "It's only as she trails off that I realise where Palla has her hands."
    "Somehow she managed to hold my eye and my attention as she slipped them under the water."
    "And now she has one of them inside my trunks, already stroking my cock!"
    "I nod hastily, already laying back in the tub to let Palla have her way."
    "She seems to understand that she's in control of the situation now."
    "And her grin becomes wider still as she uses her other hand to pull down my trunks."
    palla.say "That's right, [hero.name]."
    palla.say "Just sit back and let me have my way."
    palla.say "Do that, and I promise you'll like it too!"
    "Once she has my trunks off, Palla keeps on working my cock."
    "By now she has a firm grip on the shaft, rubbing it until it gets good and hard."
    call palla_dick_reactions from _call_palla_dick_reactions_1
    "At the same time, she uses her free hand to do the same thing to herself too."
    "My eyes are fixated on the way that she rubs her own pussy under the water."
    "Pretty soon Palla begins to pluck away at her clit as well."
    "And each time she lets out a low, almost desperate moan of desire."
    "I lick my own lips as she plays with the ones between her thighs."
    "And I swallow slowly, already imagining how they must feel."
    show hottub palla naked with dissolve
    "In an elegant move, she takes off her swimsuit, exposing her incredible body to my lustful gaze."
    show hottub sex male palla outside naked with fade
    "When she's finally ready to go further, Palla slips onto my lap."
    "She reaches back and wraps one hand around my neck, pulling herself up."
    show hottub sex male palla inside
    "Then she lowers herself back down, using the other to steer my cock home."
    palla.say "Ah..."
    palla.say "Yeah..."
    palla.say "That's it - right there!"
    "It sounds like Palla's getting almost desperate to have me inside of her."
    "But all the same there's some resistance as the head slips between her lips."
    "Not that the sensation is enough to out either of us off for as much as a second."
    "In fact, the way that my cock inches into her makes the whole thing even more intense!"
    "And by the time I'm as deep into Palla as I can go, she's panting desperately."
    "Palla leans back against me, letting me take her weight as she does so."
    "I don't know if it's her intention, but the gesture places her completely in my hands."
    "And that means I can immediately start to move beneath her."
    "I begin slowly, still enjoying the sensation of her tight pussy around my cock."
    "But as I start to pick up some speed, I can feel Palla start to melt."
    "Where before she was hesitant and needed to be convinced, she quickly becomes eager."
    "Palla glances back at me over her shoulder, her eyes wide."
    "She could be nodding in an effort to urge me on."
    "But then again, that might just be the motion of me pounding her from below!"
    "By now, Palla seems to be letting out a sharp cry with each and every thrust."
    "Her cheeks are flushed and I swear that I can hear her heart pounding inside of her chest."
    "And it's not just her feeling the effects either."
    "I'm practically grunting with the effort I'm putting in."
    "So much so that I can already feel the first signs that I'm going to cum!"
    menu:
        "Cum inside":
            "Knowing that, I keep a tight hold on Palla as I lose it."
            show hottub sex male palla inside cumshot
            $ palla.love += 1
            "And the sensation of her coming down one last time is what pushes me over the edge."
            with vpunch
            "Palla practically wails as I let go deep inside of her."
            show hottub sex male palla ahegao with vpunch
            "She squeezes her eyes tight shut and writhes against me the whole time."
            with vpunch
            "Her own weight keeping her on my cock the whole time."
        "Cum outside":
            "As Palla goes up, I make sure that I go down at just the right moment."
            show hottub sex male palla outside
            show chest_insert palla zorder 1 at zoomAt(1, (840, 100))
            show belly_insert palla zorder 2 at zoomAt(1, (840, 380))
            "This means that my cock pops out of her a second later, much to her surprise."
            "Palla wails at the sensation, squeezing her eyes shut as she falls back into the water."
            show chest_insert palla cum
            show belly_insert palla cum
            show hottub sex male palla outside cumshot
            with vpunch
            $ palla.sub += 1
            "And at the same time, I shoot my load over her breasts and belly."
            show hottub sex male palla outside -cumshot with vpunch
            "She pants almost desperately as the cum runs down her body and disappears in the water."
    "Palla almost collapses onto me, utterly spent and unable to support her own weight."
    "All she seems capable of doing right now is floating silently in the tub."
    hide chest_insert
    hide belly_insert
    hide hottub sex male
    show hottub palla
    with fade
    "For my part, I feel satisfied and more than a little vindicated by what we just did."
    "Sure, my hot-tub might not be anymore special than the next one."
    "But I think Palla would agree that the service on offer her is second to none!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ palla.sexperience += 1
    $ game.active_date.clothes = None
    return

label palla_fuck_date_intro_male(location="hero"):
    if game.week_day % 2 == 0:
        scene bg house
        show palla
        with fade
        "When we arrive at my house, Palla looks around with her usual, dubious look."
        mike.say "Say one word about how twee the house is, or how much you hate my roommates and so help me, Palla, I'll whip your ass with my belt."
        if palla.sub >= 60 or palla.love >= 160:
            palla.say "How else am I supposed to get you all hot and bothered?"
            mike.say "I don't know, why don't you try stripping and showing off your tits."
            scene bg livingroom
            show palla annoyed at right
            with fade
            "Palla makes a show of looking around."
            show palla at center with ease
            palla.say "In here? What if your roommates come out. You think they'd join in?"
            if Harem.find_by_name("home"):
                mike.say "Maybe. Except for the part where they think you're a stuck up bitch. I don't think they'd accept you."
            else:
                mike.say "While hot, that doesn't seem likely."
            palla.say "Well, no accounting for taste. Yours or theirs."
            scene chatting_bg_livingroom_03
            show palla at flip, center, zoomAt(1.4, (540, 800))
            with fade
            pause 0.5
            show palla normal at flip, center, zoomAt(1.4, (400, 920)) with ease
            "Palla plops down on the couch and pulls her phone out."
            palla.say "So, what do you want to do?"
            mike.say "I thought I'd start by fucking your ass so hard you can't walk."
            show palla happy
            palla.say "Really, you want to start with dessert?"
            mike.say "It's not like you appreciate guys who hem and haw about what they want."
            show palla normal
            "Palla looks up at me, over her phone."
            palla.say "So what do I get out of it?"
            mike.say "Dick?"
            show palla sad
            palla.say "Well, you said it. You have fun, I get dick, Typical men."
            mike.say "Palla, sweetheart, just shut up and go to the bedroom like a good girl."
            show palla normal
            palla.say "And what{b}ever{/b} led you to believe that I'm a good girl?"
            if palla.is_collared:
                mike.say "Well, that collar around your neck, for starters."
            elif palla.sub >= 80:
                mike.say "Your mouth, when it's filled with my dick."
            else:
                mike.say "You're right, evidence is you're not."
            mike.say "Get in there before I'm forced to punish you."
            palla.say "Oh, you're going to punish me, are you? Isn't that what fucking my ass so hard I can't walk is?"
            mike.say "No, that's the dessert. Punishing you is grabbing my belt and whipping your ass until you remember how to behave."
            show palla blush
            "Seriously, every time I talk to her like this, I expect her to grab her stuff and storm out. It's not like storming out isn't her thing. But this is our normal. This is what she likes!"
            palla.say "You'd better not!"
            mike.say "Then get your ass in gear, bitch, and do what you're told!"
        else:
            scene bg livingroom
            show palla angry at right
            with fade
            palla.say "Are you threatening me?"
            mike.say "I just don't want to hear your bullshit about them tonight. They're my friends."
            show palla annoyed at center with ease
            palla.say "Maybe I wasn't going to say anything about them this time?"
            mike.say "Pull the other one, it's got bells on."
            palla.say "If you want me to pull anything tonight, Mister, you'd better drop the attitude."
            mike.say "Like you'd fuck me if I didn't have the attitude."
            show palla normal
            palla.say "What if I don't fuck you at all?"
            mike.say "I could make you."
            show palla surprised
            "Palla's eyebrows go up."
            palla.say "Did you just threaten me again?"
            mike.say "Oh please, the girl who dares me to follow her, tells me not to be a creep, then has the biggest, fullest orgasms when it's all dirty and rough."
            show palla flirt
            palla.say "You're getting me hot now. Take me to your bedroom and take me before I remember how much I hate assholes like you and leave."
        scene bg bedroom1
        show palla normal
        with fade
        mike.say "Strip."
        if palla.sub < 30:
            palla.say "You first."
        else:
            palla.say "Make me."
        mike.say "Do you want a red ass?"
        show palla blush underwear with dissolve
        "Palla's clothes come off quickly, tossed carelessly to the side."
        "She stands there, showing off her incredibly sexy body for me. The talk has been getting her hot, too; her nipples are hard, even through her bra, and her cheeks are flushed."
        "And that, in turn, gets {b}me{/b} hot. Part of me wants to speed this up and get right to the action, but part of me wants to savor this."
        "Because watching her stand there, doing as I command, is almost as sexy as fucking her will be."
        mike.say "And now the bra."
        if palla.sub < 60 and not palla.is_collared:
            palla.say "You first."
            mike.say "{b}Now{/b}!"
        elif palla.flags.mikeNickname:
            palla.say "Yes, [hero.name]."
        else:
            palla.say "As you wish."

        "Palla does what she is told, and when the bra comes off, goosebumps tighten all the flesh in her upper body."
        show palla underwear topless with dissolve
        mike.say "Oh. Yeah. Show me those tits, bitch."
        if palla.sub < 30:
            palla.say "Call me bitch again and I'm out of here."
            mike.say "Oh sure, all the way in here, showing me your goods, and now you're angry at being called bitch? What else should I call you? Slut? Whore? Cunt? Tell me what you want."
            "Palla's mouth opens, then closes."
            mike.say "Do you want me to put my dick in there?"
            "Her eyes widen, and she makes a little squeak."
        else:
            "Palla thrusts her chest out, acting like a model demonstrating, well. Her tits. And damn, they are a fine pair of tits at that."
        mike.say "And now the panties."
        "Palla's slender fingers make quick work of the panties. She steps out of them and leaves them on the floor at her feet."
        show palla naked
    else:
        show bg bedroom1 at center, zoomAt(1.2, (640, 720)) with fade
        "I'm feeling pretty pleased with myself as I show Palla through the door and into my bedroom."
        "Because we've just got back from a date that went really well, even if I do say so myself."
        "And when you've managed to score so highly earlier in the night, that has to mean something, right?"
        "So I'm feeling pretty confident that we're not just heading in there for a pleasant little chat."
        play sound door_close
        show palla normal at center, zoomAt(1, (640, 720)) with dissolve
        "Closing the door behind me, I turn to see Palla standing in the middle of the room."
        "And she seems to be taking in the ambience that my personal choice in décor creates."

        if palla.sub <= 80:
            show palla b
            "Palla has her arms crossed, looking from one piece of sci-fi memorabilia to the next."
            show palla talkative at startle(0.1, 5)
            palla.say "Wow..."
            palla.say "And here I was thinking that Shawn was the king of the nerds!"
            show palla normal
            "I don't know what makes me prickle more, being called a nerd or Palla mentioning Shawn."
        else:

            show palla stuned
            "Palla's got her hands behind her back as she gazes at the contents of my bedroom."
            show palla talkative at startle(0.1, 5)
            palla.say "My goodness..."
            palla.say "I always thought that Shawn had a lot of toys in his bedroom."
            palla.say "But you seem to have a lot more, [hero.name]!"
            show palla normal
            "I don't know what makes me prickle more, the idea that my collectibles are toys or Palla mentioning Shawn."
        "But either way I feel the need to change the subject before she says anything more on the subject."
        show palla at startle(0.1, 5)
    return


label palla_fuck_date_cowgirl(sexperience_min):
    "I lie down on the bed, turning my hips so that my stiff cock points straight up."
    mike.say "Get on."
    palla.say "Really. You actually want me to be on top?"
    mike.say "Do you want my cock?"
    palla.say "Oh. Oh fuck yes, I want that thing inside me!"
    mike.say "Then get your sexy ass on me!"
    show palla cowgirl outside pleasure with fade
    "Palla crawls atop me, and my cock touches just between her asscheeks."
    palla.say "Now what, big guy?"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "There's something about sticking my huge cock in Palla's tight asshole that is just about the most arousing thing I can think of."
            if palla.flags.anal > 5:
                mike.say "Well, I guess after the punishment I've given her, it isn't that tight anymore."
                "I press my dick into the pucker of her ass, which willingly opens up for me. Enough of her pussy juice has already dripped down to her anus that her ass is ready, and it takes a little effort, but I get all the way into her."
            else:
                "I touch my cock to her waiting anus, and Palla shrieks even before I get in."
                palla.say "No no no! You are not going in the back door this time!"
                mike.say "Shut up, bitch. You're going to take it, and you're going to take it again. And again and again."
                "And to show her I mean it, I shove it in. It only gets in as far as the head before I can't push any further, but that's all right."
                "Palla shrieks again."
                mike.say "Your ass is mine for the taking."
                "Except for the problem that I can't get in there. But...her pussy is wet and ready. There's lubricant right there!"
                show palla cowgirl vaginal pleasure
                "So I pull out and shove it all the way into her cunt. I stroke a couple of times just to get it wet."
                palla.say "Oh, thank--"
                "...and once it is wet, back to her ass. And with the fresh lubricant, I'm able to fit it all the way in, albeit with a little work."
            show palla cowgirl anal pain
            palla.say "{b}Ow!{/b} Ow ow that hurts, you monster!"
            mike.say "Give it a minute!"
            "I thrust in and out of her. Each time is accompanied with a shriek. The first few times it's a shriek of pain."
            show palla cowgirl anal ahegao
            "But it doesn't take long before her shrieks of pain turn into shrieks of pleasure."
            mike.say "Yeah, bitch, how do you like me now?"
            if palla.love >= 160:
                palla.say "I love you!"
                "Her words are slurred from the pounding, but they're music to my ears nonetheless."
            else:
                palla.say "I hate you! I hate this!"
                mike.say "Your words say one thing, my darling. But your body says quite another."
            mike.say "Do you want me to stop?"
            if palla.love < 160 and palla.sub < 60:
                palla.say "Yes!"
                mike.say "Too bad. Your ass is mine."
            else:
                palla.say "No!"
                mike.say "Even if it hurts?"
                palla.say "Fuck you!"
            with vpunch
            "And with that, I can't hold back any more."
            show palla cowgirl anal ahegao cum with vpunch
            "My load spills deep into Palla's ass, filling her with my hot liquid."
            with vpunch
            palla.say "Oh. Oh fuck, oh fuck oh fuck."
            mike.say "You okay?"
            palla.say "Oh fuck I'm coming too!"
            "When I look down, I see that glops of her pussy juice are mixing with my semen right where my dick is disappearing into her anus."
            mike.say "And here I thought you hated this."
            palla.say "Fuck you!"
            mike.say "I think you just did, hon."
            $ palla.love += 2
            $ palla.sub += 1
            $ palla.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (palla) from _call_check_condom_usage_94
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show palla cowgirl condom
            else:
                show palla cowgirl vaginal pleasure
            "I slip my cock into her dripping pussy and, grasping her by the hips, thrust myself all the way up inside her."
            palla.say "Mmmm, oh fuck, [hero.name]!"
            "I grab her hips with my hands, pulling her down against me as I thrust up, then pushing her up and away as I pull out."
            "She works with me and we get a good rhythm going."
            "With each thrust, Palla moans louder."
            palla.say "Ohhhhhhh!"
            palla.say "Faster, [hero.name]! Fuck me harder!"
            "I speed up, and she grabs my shoulders so hard she leaves claw marks on them. It doesn't take long..."
            show palla cowgirl ahegao
            call cum_reaction (palla, 'vaginal', sexperience_min) from _call_cum_reaction_145
            if _return == "vaginal_outside":
                "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                "Realizing that her orgasm is about to make me explode, I quickly pull my cock out of her."
                show palla cowgirl outside cum pleasure with vpunch
                "I'm just barely clear of her when I spray my load all over her back."
                show palla cowgirl after pleasure with vpunch
                $ palla.love += 1
            elif _return == "vaginal_condom":
                with vpunch
                "So I do, moving faster and faster until finally I explode, filling the condom with the hot, sticky mess that is my load."
                with vpunch
                palla.say "Oh god, I'm coming!"
                with vpunch
                "Palla's orgasm is almost violent, and it's almost like she is dancing on top of me. Her legs squeeze my hips and push me deeper into the bed."
                palla.say "That...was fucking amazing!"
                $ palla.sub += 1
            elif _return == "vaginal_inside_pill":
                with vpunch
                "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                show palla cowgirl cum with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                $ palla.love += 2
            elif _return == "vaginal_inside_pregnant":
                with vpunch
                "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                show palla cowgirl cum with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                $ palla.love += 2
            else:
                with vpunch
                "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                show palla cowgirl cum with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                $ palla.love += 5
                $ palla.impregnate()
    return

label palla_fuck_date_missionary(sexperience_min):
    mike.say "Lie down on the bed and spread your legs. Wide."
    "Palla just stands there."
    mike.say "Do as you're told!"
    "Palla offers me a wry smile."
    palla.say "Make me!"
    "If that's what she wants...I walk up to her, take her by the shoulders and throw her roughly on the bed."
    show palla missionary out with fade
    "I stand over her, with my dick out. Her pussy is wet and ready. So am I, but I also realize I want to savor this moment too."
    mike.say "You ready for this big cock, bitch?"
    palla.say "Get on with it already!"
    mike.say "Not until you're ready."
    palla.say "What?"
    mike.say "Beg for it. Beg me to stick this giant cock inside your hole."
    palla.say "No, I'm not begging!"
    mike.say "Oh. So you don't want it?"
    "I start to draw back from her. Her eyes go wide as I pull away."
    palla.say "Don't!"
    mike.say "Then you know what to do."
    palla.say "Please?"
    mike.say "Beg."
    "Palla bites her lip, resisting. But the humiliation is continuing to turn her on, as evidence by her wet pussy actively dripping now."
    palla.say "Put it in me. Put your big cock in me."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "There's something about sticking my huge cock in Palla's tight asshole that is just about the most arousing thing I can think of."
            if palla.flags.anal > 5:
                mike.say "Well, I guess after the punishment I've given her, it isn't that tight anymore."
                "I press my dick into the pucker of her ass, which willingly opens up for me. Enough of her pussy juice has already dripped down to her anus that her ass is ready, and it takes a little effort, but I get all the way into her."
            else:
                "I touch my cock to her waiting anus, and Palla shrieks even before I get in."
                palla.say "No no no! You are not going in the back door this time!"
                mike.say "Shut up, bitch. You're going to take it, and you're going to take it again. And again and again."
                "And to show her I mean it, I shove it in. It only gets in as far as the head before I can't push any further, but that's all right."
                "Palla shrieks again."
                mike.say "Your ass is mine for the taking."
                "Except for the problem that I can't get in there. But...her pussy is wet and ready. There's lubricant right there!"
                show palla missionary vaginal pleasure
                "So I pull out and shove it all the way into her cunt. I stroke a couple of times just to get it wet."
                palla.say "Oh, thank--"
                "...and once it is wet, back to her ass. And with the fresh lubricant, I'm able to fit it all the way in, albeit with a little work."
                show palla missionary anal
                palla.say "{b}Ow!{/b} Ow ow that hurts, you monster!"
                mike.say "Give it a minute!"
                show palla missionary anal normal
                "I thrust in and out of her. Each time is accompanied with a shriek. The first few times it's a shriek of pain."
            show palla missionary anal ahegao
            "But it doesn't take long before her shrieks of pain turn into shrieks of pleasure."
            mike.say "Yeah, bitch, how do you like me now?"
            if palla.love >= 160:
                palla.say "I love you!"
                "Her words are slurred from the pounding, but they're music to my ears nonetheless."
            else:
                palla.say "I hate you! I hate this!"
                mike.say "Your words say one thing, my darling. But your body says quite another."
            mike.say "Do you want me to stop?"
            if palla.love < 160 and palla.sub < 60:
                palla.say "Yes!"
                mike.say "Too bad. Your ass is mine."
            else:
                palla.say "No!"
                mike.say "Even if it hurts?"
                palla.say "Fuck you!"
            with vpunch
            "And with that, I can't hold back any more."
            show palla missionary anal ahegao cumshot with vpunch
            "My load spills deep into Palla's ass, filling her with my hot liquid."
            with vpunch
            palla.say "Oh. Oh fuck, oh fuck oh fuck."
            mike.say "You okay?"
            palla.say "Oh fuck I'm coming too!"
            "When I look down, I see that glops of her pussy juice are mixing with my semen right where my dick is disappearing into her anus."
            mike.say "And here I thought you hated this."
            palla.say "Fuck you!"
            mike.say "I think you just did, hon."
            $ palla.love += 2
            $ palla.sub += 1
            $ palla.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (palla) from _call_check_condom_usage_95
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show palla missionary condom
            show palla missionary vaginal
            "I slip my cock into her dripping pussy and, grasping her by the hips, thrust myself all the way inside."
            "Palla shrieks. As wet and ready as she was, she wasn't quite ready for that."
            "I slowly withdraw about halfway, and then pound in again. Her slick mound surrounds me, gripping my cock tightly."
            palla.say "Oh. Oh [hero.name]!"
            "I set myself up into a rhythm, struggling to keep it slow so I don't just orgasm right away."
            show palla missionary pleasure
            "With each thrust, Palla moans louder."
            palla.say "Fuck me harder!"
            "I speed up, and she grips the sheets so hard she nearly rips them off the bed. It doesn't take long..."
            show palla missionary ahegao
            call cum_reaction (palla, 'vaginal', sexperience_min) from _call_cum_reaction_146
            if _return == "vaginal_outside":
                show chest_insert palla zorder 1 at zoomAt(1, (440, 40))
                show belly_insert palla zorder 2 at zoomAt(1, (40, 480))
                show palla missionary out
                with vpunch
                "Realizing that her orgasm is about to make me explode, I quickly pull my cock out of her."
                show chest_insert palla cum
                show belly_insert palla cum
                show palla missionary out cumshot pleasure
                with vpunch
                "I'm just barely clear of her when I spray my load all over her."
                show palla missionary -cumshot cum onbody with vpunch
                "There's something about the sight of Palla, lying there on her back with my cum all over her belly. It makes me feel possessive, like I've won something."
                $ palla.love += 1
            elif _return == "vaginal_condom":
                with vpunch
                "...before Palla's orgasm explodes. She screeches in sheer pleasure, and at the same time her pussy grips my cock so hard it almost feels like she's going to rip it off."
                show palla missionary ahegao with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into the latex that covers my cock."
                $ palla.sub += 1
            elif _return == "vaginal_inside_pill":
                show palla missionary cumshot ahegao with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                $ palla.love += 2
            elif _return == "vaginal_inside_pregnant":
                show palla missionary cumshot ahegao with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                $ palla.love += 2
            else:
                show palla missionary cumshot ahegao with vpunch
                "The sheer power of her orgasm triggers me, and I unload spurt after spurt of hot semen right into her. It feels like it goes on for several minutes."
                $ palla.love += 5
                $ palla.impregnate()
            with vpunch
            "When I'm finally spent, I just stand there, panting, looking down at her."
            "And for a moment, there's no abusive banter between us. We're not an asshole and a bitch. We're just two people, who shared an intimate moment. And it was really, really good."
            hide chest_insert
            hide belly_insert
    return

label palla_fuck_date_doggy(sexperience_min):
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            show palla doggy
            if palla.flags.anal < 1:
                "Even though Palla is already on all-fours and fully open to me, it's not enough for what I have in mind."
                "Without asking permission, I push her arms out from under her and send her face tumbling into the piled sheets."
                "This only succeeds in muffling her protests for a moment, as she can already feel just where the head of my cock is probing now that her anus is full exposed."
                palla.say "Oh god, - not that!"
                "I ignore her completely, grabbing a handful of hair on her scalp in my right hand and gripping a ponytail's worth behind her head with my left."
                palla.say "Please, please, please - don't fuck me in the ass!"
                palla.say "Please - I don't even like the thought of it!"
                "By now I have the tip of my dick all lined up and ready to go, and I know she can tell I'm teetering on the brink."
                palla.say "PLEASE, I'm begging you not to!"
                palla.say "I hate it...I hate it...it'll...hurt me..."
                "Were it not for her bitchy comments and acid tongue, I might have been moved by her pleas."
                "But as it is, I think that she's about to get what she so richly deserves."
                "Keeping a firm hold on Palla's hair, I force my cock into her unwilling ass."
                show palla doggy orgasm
                "She shivers bodily as I enter her anus, making a deep moaning sound that turns into quieter whimpers as the full length slides inside of her."
                "I hold myself quite still once I've pushed in as far as I can manage, enjoying the sensation of Palla's muscles quivering around my cock."
                "At first I keep my movements small and slow, only building up speed a little at a time."
                "Palla continues to make incoherent sounds that are part pain and part humiliation."
                show palla doggy ahegao
                "But as my thrusts become more intense and lengthy, the sounds begin to rise in volume and change in tone."
                "They turn back into whimpers, then into moans, and finally evolve into what I can only describe as almost cries of increasing pleasure."
                "The change affects me as well, knowing that the humiliation Palla's feeling has somehow broken through her catty demeanour and laid her wide open."
                "The more she cries in guilty pleasure, the closer I come to losing myself, deep in her anus."
            else:
                mike.say "Ready for another ass-pounding?"
                if palla.sub > 80:
                    "Palla spreads her cheeks wide for me, at the same time burying her face and chest into the pillows."
                    "I line myself up and press the tip right against her anus, pushing it open just slightly, but not entering."
                    mike.say "Tell me you want it."
                    palla.say "I...I want it."
                    mike.say "Tell me you need it."
                    palla.say "I need it, [hero.name], I need it!"
                    mike.say "Tell me you LOVE it!"
                    "Palla's breathing gets heavier, even though I haven't even started."
                    palla.say "I love it, [hero.name]! Oh God, I love it!"
                    if palla.love > 190:
                        palla.say "And I love you too!"
                else:

                    palla.say "No, please! Not again! It hurts! It's torture!"
                    mike.say "And you love it, bitch! Open up and take it!"
                    "Palla buries her face in the sheets and despite her protestations, her asshole is open and ready for me."
                    "I line myself up and press the tip right against her anus, pushing it open just slightly, but not entering."
                    mike.say "Tell me you want it."
                    palla.say "Mmf! No! I don't want it!"
                    "I smack her across one ass cheek; hard enough to make a good snapping sound, but not hard enough to hurt. Much."
                    "Palla yelps!"
                    mike.say "Tell me you want it."
                    palla.say "I don...no...I don...I want it."
                    "I press myself into her anus, pushing just the head in to open her up."
                    mike.say "Say it again, bitch!"
                    "Palla nearly cries out, this time."
                    palla.say "I want it!"
                    mike.say "You want it!"
                    palla.say "I want it!"
                "The talk has made me as hard I've ever been, and I press into her anus. It gives way easily and I plunge in."
                "Palla shrieks into the sheets, her muffled cries a combination of pain and pleasure."
                show palla doggy orgasm
                "And on my really hard thrusts, my hands pull her away from the sheets by her hair. It must hurt, but she loves it so much I can't tell."
                "I thrust back and forth, not sparing her at all as I may have in the past."
                "Her cries get louder, and after a few moments, I join her with a guttural yelp."
                with hpunch
                mike.say "Take THAT, bitch!"
                with hpunch
                mike.say "And THAT!"
                show palla doggy ahegao with hpunch
                "Palla's cries might've included a yes, but she is so beyond words it was hard to tell."
                "It doesn't take me long before I'm ready to blow, either."
            $ palla.flags.anal += 1
            $ palla.love += 2
            $ palla.sub += 1
        "Fuck her pussy":
            call check_condom_usage (palla) from _call_check_condom_usage_96
            if _return == False:
                return "leave_without_gain"
            show palla doggy
            "I hear Palla take a sharp breath as I press my cock up against the lips of her pussy."
            "She cries out in delight as I sink into her."
            "She responds by pressing her ass back into me, and as she does so I pull on her hair, eliciting another cry of joy."
            palla.say "Yes, [hero.name], faster! Harder!"
            "Palla sags forward into the sheets and pillows, the motion of being banged so hard from behind driving her downwards."
            "From this angle there's nothing to stop me pounding her with almost all of my weight, and I do so."
            "Her pussy is already wet and accommodating, her muscles yielding without similar protests as I begin to push in and out."
            "Palla's arms tremble at first, trying to keep her upright as she begins to quiver from the sensation of being roughly fucked from behind."
            show palla doggy orgasm
            "Then they simply collapse as she sags forwards amongst the sheets, allowing me to get an even more acute angle inside of her."
            "With Palla's almost ragged cries ringing in my ears, I know it's only going to be a matter of seconds before I inevitably cum."
            call cum_reaction (palla, 'vaginal', sexperience_min) from _call_cum_reaction_147
            if _return == "vaginal_outside":
                "I might have been able to make Palla shut up and take it how I wanted to give it to her."
                "But I see that there's another way I can humble her - by pulling out and giving her a little shower to end things with."
                "Palla makes a long and almost mournful sound as I extricate myself from her and aim my dick over her back."
                with hpunch
                "When my orgasm comes over me a few seconds later, cum sprays down over her, landing in her hair and splattering down her back."
                with hpunch
                "Palla remains crouched there, feeling the aftershocks of having me inside her, with fast-cooling cum running off her back and down her sides to drip onto the sheets below."
                $ palla.love += 1
            elif _return == "vaginal_condom":
                "After managing to humble Palla like that, the last thing I'm about to do is keep from cumming inside of her."
                "I tighten my grip on her hair and the intensified pain of this goes some way to keeping the tell-tale signs of my muscles twitching from her notice."
                with hpunch
                "This means that when I finally lose myself inside of her, Palla is taken almost completely by surprise."
                show palla doggy ahegao with hpunch
                "She writhes and groans as my climax goes off entirely within one of the most sensitive parts of her body."
                with hpunch
                "But my firm grip and her submissive position mean that she can only endure it, even when her own orgasm overtakes her too."
                $ palla.sub += 1
            elif _return == "vaginal_inside_pill":
                "After managing to humble Palla like that, the last thing I'm about to do is keep from cumming inside of her."
                "I tighten my grip on her hair and the intensified pain of this goes some way to keeping the tell-tale signs of my muscles twitching from her notice."
                with hpunch
                "This means that when I finally lose myself inside of her, Palla is taken almost completely by surprise."
                show palla doggy ahegao with hpunch
                "She writhes and groans as my climax goes off entirely within one of the most sensitive parts of her body."
                with hpunch
                "But my firm grip and her submissive position mean that she can only endure it, even when her own orgasm overtakes her too."
                $ palla.love += 2
            elif _return == "vaginal_inside_pregnant":
                "After managing to humble Palla like that, the last thing I'm about to do is keep from cumming inside of her."
                "I tighten my grip on her hair and the intensified pain of this goes some way to keeping the tell-tale signs of my muscles twitching from her notice."
                with hpunch
                "This means that when I finally lose myself inside of her, Palla is taken almost completely by surprise."
                show palla doggy ahegao with hpunch
                "She writhes and groans as my climax goes off entirely within one of the most sensitive parts of her body."
                with hpunch
                "But my firm grip and her submissive position mean that she can only endure it, even when her own orgasm overtakes her too."
                $ palla.love += 2
            else:
                "After managing to humble Palla like that, the last thing I'm about to do is keep from cumming inside of her."
                "I tighten my grip on her hair and the intensified pain of this goes some way to keeping the tell-tale signs of my muscles twitching from her notice."
                with hpunch
                "This means that when I finally lose myself inside of her, Palla is taken almost completely by surprise."
                show palla doggy ahegao with hpunch
                "She writhes and groans as my climax goes off entirely within one of the most sensitive parts of her body."
                with hpunch
                "But my firm grip and her submissive position mean that she can only endure it, even when her own orgasm overtakes her too."
                $ palla.love += 5
                $ palla.impregnate()
    return

label palla_fuck_date_standing(sexperience_min):
    show palla stand bedroom
    palla.say "Do you want it, [hero.name]?"
    palla.say "Do you want to fuck my pussy?"
    palla.say "It's so wet and slippery..."
    show palla stand bedroom wet pleasure
    "I don't even realise that I'm moving."
    "The first thing I know is that I have Palla up against the wall."
    "She's pressed against the glass of the mirror."
    "And she looks back over her shoulder at me, eyes wide with anticipation."
    "Palla doesn't say a word, but she nods her head."
    "Which is all the permission that I need."
    "And then my hands are all over Palla once more."
    "One spills her breasts."
    show palla stand dick
    "The other guides my cock between her thighs."
    "She wasn't kidding when she said she was wet either."
    "All it takes is for my cock to press against the lips of her pussy."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I can see now that I'm not going to need anything in the way of foreplay."
            "Palla seems physically ready for me, despite her probably feigned reluctance."
            "I could swear that she even spreads her feet a little wider apart as she feels the brush of my cock on her buttocks."
            show palla stand -dick ahegao
            "She yelps again as I push into her as far as I can go and remain there for a moment."
            "I can see her cheeks reddening in the mirror, and she closes her eyes now, fully engaged in what's happening."
            "I begin to thrust into Palla, every movement pushing the frustration of the day into the rearview mirror."
            "Fucking her as hard as possible seems to be the best form of therapy for her particular brand of annoyance."
            "All it takes is the constant view of Palla's haughty face in such an undignified position, her breasts squashed almost flat against the mirror, the feeling of pounding her deep."
            "God she's hot! Especially like this."
            "I know that I can't keep from cumming too much longer."
            "So I need to make a decision as to where she's going to have to take it."
            call cum_reaction (palla, 'anal', sexperience_min) from _call_cum_reaction_148
            if _return == 'anal_inside':
                "I'm having such a good time of using Palla's own ass to purge me of the stress she causes me that I'm staying right where I am until I cum."
                "Since there's no chance of dragging this thing out and we might be rumbled at any moment, I step up my efforts."
                "Now I'm literally thrusting into Palla with as much force as I can muster."
                "She too seems to be on the same wavelength, doing nothing to keep me from fucking her ever harder."
                "Palla's pressed right up against the glass now, her breath steaming it up and the sweat from her body making it slick to the touch."
                "Her breasts are making a squeaking sound in time with my thrusts, like someone dragging a fingertip down a windowpane."
                "I can see her biting her lip in an effort to suppress a cry as she begins to cum."
                show palla stand cum pleasure with hpunch
                "That pushes me over the edge, and I lose myself inside of her a second later."
                with hpunch
                "I remain where I am, keeping Palla pinned to the mirror, even after I'm finished cumming."
            elif _return == 'anal_outside':
                "I've become so fixated on the mirror and Palla's reflection in it, that I simply have to involve it somehow."
                "I adjust my angle so that I can slide out of her ass in one smooth motion."
                show palla stand dick wet
                "That done, I make good use of the lubricant she's thoughtfully provided, and the sweat forming between her thighs to push my cock into the tight gap."
                "Despite her curvaceous thighs and their generous circumference, the head easily emerges from between them."
                "I can feel the cold touch of the mirror and the warm embrace of Palla's thighs all at once."
                "It's an incredible sensation, and I begin to move back and forth again, enjoying this almost as much as being inside of her."
                "Palla too seems to be getting off on it, as the shaft of my cock rubs against the splayed folds of her pussy."
                show palla stand cum pleasure with hpunch
                "She starts to twitch and moan, letting me know that she's close to cumming herself, and that finishes me too."
                show palla stand cumscreen with hpunch
                "I cum whilst the head of my cock is poking out from between her thighs, splattering the mirror as well as Palla's thighs and belly."
            $ palla.flags.anal += 1
            $ palla.love += 2
            $ palla.sub += 1
        "Fuck her pussy":
            "And then I hear her gasp as I slip smoothly inside of her."
            show palla stand -dick ahegao
            "I don't stop moving until I'm as deep into Palla as I can go."
            "And once there, I keep on pushing forwards."
            "This pushes Palla into the mirror, her breath fogging the glass."
            "But before she can collect herself, I start to move inside her."
            "I don't bother to start slow and build up speed."
            "Instead my thrusts are as fast and powerful as I can make them."
            "Palla's already teased me into a state of almost desperate arousal."
            "And so all that I want to do is take her as quickly as I can."
            "My groin slaps noisily against her exposed buttocks."
            "Her breasts are squashed against the wall, over and over again."
            show palla stand normal
            "Palla looks back over her shoulders at me as I pound her without mercy."
            "She's gasping the whole time, almost squealing with each thrust."
            "Palla might have claimed she wanted to be a mermaid princess."
            "But she's throwing herself into the role of being a wanton siren right now!"
            palla.say "Fuck me..."
            palla.say "Fuck me harder..."
            palla.say "Make me cum!"
            "That's more than I can take, the limit of my resistance."
            show palla stand ahegao cum with hpunch
            "I lose it all at once, shooting my load into Palla."
            with hpunch
            "She lets out a scream of pure release, her muscles turning to water."
            "Palla leans against the tiled wall and slides slowly downwards."
            "She slips off of my cock and collapses onto the bedroom floor."
            "All I can do is stand there, panting and leaning against the wall."
            "I know that I should help her up, at least check she's okay."
            "But I'm afraid that I'd just end up collapsing beside her."
            $ CONDOM = False
            call cum_reaction (palla, 'vaginal', sexperience_min) from _call_cum_reaction_149
            if _return == "vaginal_outside":
                "I've become so fixated on the mirror and Palla's reflection in it, that I simply have to involve it somehow."
                "I adjust my angle so that I can slide out of her pussy in one smooth motion."
                show palla stand dick wet
                "That done, I make good use of the lubricant she's thoughtfully provided, and the sweat forming between her thighs to push my cock into the tight gap."
                "Despite her curvaceous thighs and their generous circumference, the head easily emerges from between them."
                "I can feel the cold touch of the mirror and the warm embrace of Palla's thighs all at once."
                "It's an incredible sensation, and I begin to move back and forth again, enjoying this almost as much as being inside of her."
                "Palla too seems to be getting off on it, as the shaft of my cock rubs against the splayed folds of her pussy."
                show palla stand cum pleasure with hpunch
                "She starts to twitch and moan, letting me know that she's close to cumming herself, and that finishes me too."
                show palla stand cumscreen with hpunch
                "I cum whilst the head of my cock is poking out from between her thighs, splattering the mirror as well as Palla's thighs and belly."
                $ palla.love += 1
            elif _return == "vaginal_condom":
                with hpunch
                "I lose it all at once, shooting my load into Palla."
                show palla stand ahegao cum with hpunch
                "She lets out a scream of pure release, her muscles turning to water."
                "Palla leans against the tiled wall and slides slowly downwards."
                "She slips off of my cock and collapses onto the bedroom floor."
                "All I can do is stand there, panting and leaning against the wall."
                "I know that I should help her up, at least check she's okay."
                "But I'm afraid that I'd just end up collapsing beside her."
                $ palla.sub += 1
            elif _return == "vaginal_inside_pill":
                with hpunch
                "I lose it all at once, shooting my load into Palla."
                show palla stand ahegao cum with hpunch
                "She lets out a scream of pure release, her muscles turning to water."
                "Palla leans against the tiled wall and slides slowly downwards."
                "She slips off of my cock and collapses onto the bedroom floor."
                "All I can do is stand there, panting and leaning against the wall."
                "I know that I should help her up, at least check she's okay."
                "But I'm afraid that I'd just end up collapsing beside her."
                $ palla.love += 2
            elif _return == "vaginal_inside_pregnant":
                with hpunch
                "I lose it all at once, shooting my load into Palla."
                show palla stand ahegao cum with hpunch
                "She lets out a scream of pure release, her muscles turning to water."
                "Palla leans against the tiled wall and slides slowly downwards."
                "She slips off of my cock and collapses onto the bedroom floor."
                "All I can do is stand there, panting and leaning against the wall."
                "I know that I should help her up, at least check she's okay."
                "But I'm afraid that I'd just end up collapsing beside her."
                $ palla.love += 2
            else:
                with hpunch
                "I lose it all at once, shooting my load into Palla."
                show palla stand ahegao cum with hpunch
                "She lets out a scream of pure release, her muscles turning to water."
                "Palla leans against the tiled wall and slides slowly downwards."
                "She slips off of my cock and collapses onto the bedroom floor."
                "All I can do is stand there, panting and leaning against the wall."
                "I know that I should help her up, at least check she's okay."
                "But I'm afraid that I'd just end up collapsing beside her."
                $ palla.love += 5
                $ palla.impregnate()
    return

label palla_date_restaurant_bj:
    show palla date at center, zoomAt(1.5, (640, 1140)) with fade
    "As soon as we're seated at our table and handed the menus, I'm scanning mine for options."
    "And that's because I'm in the mood for something seriously spicy and adventurous!"
    mike.say "Ooh!"
    mike.say "Look at this, Palla!"
    mike.say "They have a steak that's marinated in garlic for ages!"
    mike.say "Then they smother it in hot, chilli sauce too!"
    "I'm grinning at Palla like a fool, expecting her to show serious interest."
    "Maybe even to give me the nod and let me know that she's cool with me ordering it."
    "Which I guess is pretty naive of me."
    "Because instead she looks less than impressed."
    palla.say "Urgh..."
    show palla annoyed
    palla.say "Do you even realise what you smell like after eating stuff like that?"
    palla.say "I can catch your breath from a couple of rooms away, [hero.name]!"
    "I frown at Palla's comments."
    "And then I leap to defend myself."
    mike.say "You know what, Palla..."
    mike.say "You can be a real buzz-kill sometimes."
    mike.say "Why else do you think I need to order stuff like that?"
    mike.say "It's because I want to liven things up on our dates, that's why!"
    "I regret saying that the moment the words are out of my mouth."
    "And I doubly regret it when I see the look Palla gives me in response."
    palla.say "What's that supposed to mean?"
    show palla angry
    palla.say "Are you trying to say I'm boring?!?"
    "I feel myself starting to squirm in my seat."
    "Already thinking up excuses to get myself off the hook."
    mike.say "Not boring, Palla, not boring."
    mike.say "More like you have everything planned out in advance, you know?"
    mike.say "You're just not very...spontaneous, yeah?"
    "I watch as Palla's jaw literally drops open."
    "She crosses her arms over her chest as she glares at me."
    palla.say "Spontaneous?"
    palla.say "You want me to be spontaneous?"
    palla.say "Okay, [hero.name], I'll show you spontaneous!"
    "Before I can say another word, Palla scrapes her chair backwards."
    hide palla at zoomAt(1.5, (640, 1140)) with moveoutbottom
    "And then she slides under the table, still looking me in the eye."
    "As soon as she's out of sight, I can feel myself beginning to panic."
    "I'm glancing around at the other people in the restaurant."
    "Wondering if any of them overhead our little spat just now."
    "Or worse, if they saw Palla go under the table."
    "But then I feel someone pawing at my groin."
    "And all of my attention is focused on looking down."
    "That's where I see the top of Palla's head between my legs."
    "And her hands in the process of unzipping my flies."
    show palla restaurantbj with fade
    "I open my mouth to object, but then bite my tongue."
    "All that'll do is cause a scene, draw attention to us."
    "So I feel like all I can do is lie back and leave her to it!"
    "Because I think I know what's coming next."
    "Sure enough, Palla wastes no time in pulling out my cock."
    "It's already well on the way to being hard."
    "And Palla soon makes sure that it's standing proud."
    "She strokes and squeezes with her hands."
    "All before she even goes near it with her lips or tongue."
    "But when she finally does, things begin to get interesting."
    "Palla goes for it the moment her lips touch the head."
    show palla restaurantbj kissdick
    "Her tongue snakes out and wraps around it."
    "Then my hands clamp down on the arms of my chair."
    "And I might as well be strapped into a fucking roller-coaster!"
    "Palla takes my dick into her mouth an inch at a time."
    "Pausing to nipple and lick as she does so."
    "The head goes deeper and deeper, as she goes ever lower."
    show palla restaurantbj suckdick
    "I keep expecting Palla to start gagging any moment."
    "Yet she seems more than capable of handling it."
    "Then her head starts to move up and down."
    "I can feel my finger-nails digging into the arms of the chair."
    "And the sense of excitement is building up inside me."
    "If I were on a roller-coaster, this would be the build-up to the big drop."
    "The point where you're teetering on the edge before plummeting down."
    "Just then, Palla takes me deeper than ever."
    "There's no way I can hold back as she does so."
    "And I let out a gasp of pure pleasure that's plain to hear."
    "I do the best I can to turn it into a yawn as heads turn towards me."
    "But I can feel the eyes looking straight at me all the same."
    "Ah shit...I hope Palla winds this thing up soon!"
    "As if sensing my thoughts, Palla kicks things up a gear."
    "She squeezes my balls with her free hand."
    "And at the same time she presses my cock with her lips and tongue."
    "That'll do it, right there!"
    "Now I know that I'm about to cum!"
    menu:
        "Cum on her face":
            "As if to make her point, Palla raises her head."
            "This means that my cock slides out of her mouth."
            show palla restaurantbj kissdick with hpunch
            "Then it bobs up and down in front of her face."
            with hpunch
            "A moment later I shoot my load, and she takes it right between the eyes."
            show palla restaurantbj kissdick face with hpunch
            "Well, more like across the cheeks and the bridge of her nose!"
            "Palla stares up at me as the sticky cum runs down her cheeks."
            "And the smile on her face is one that's filled with defiance."
        "Cum in her mouth":
            "Palla doesn't let up for a moment, holding my cock in her mouth the whole time."
            with hpunch
            "This means that when I finally cum, everything I have to give hits the back of her throat."
            show palla restaurantbj suckdick dick with hpunch
            "I think I see her eyes bulge for a few seconds, which makes me sure she's going to gag."
            "But then Palla seems to pull through on sheer force of will and bloody-mindedness."
            with hpunch
            "She swallows again and again, taking down the entire lot."
            show palla restaurantbj kissdick face
            "And only when I'm done does she let go of my cock, gasping and panting for breath."
    "Afterwards I feel Palla retreat towards her side of the table."
    show palla date normal at zoomAt(1.5, (640, 2040)) with fade
    show palla at zoomAt(1.5, (640, 1140)) with ease
    "So I hastily push my cock back into my pants and try to act the innocent."
    "And when Palla finally pops up in her seat, she looks like nothing at all happened."
    show palla date happy
    "Giving me a knowing smile, she picks up her menu and begins to study it."
    palla.say "Now..."
    palla.say "Where was that garlic chilli steak you were talking about?"
    palla.say "I'm suddenly in the mood for something exciting myself..."
    $ palla.love += 2
    $ palla.sub += 1
    $ hero.cancel_activity()
    $ palla.flags.orderedrestaurant = TemporaryFlag(True, "day")
    return

label palla_fuck_date_blowjob:
    if game.week_day % 2 == 0:
        "I'm nodding eagerly as Palla gives my shoulder a hard shove."
        with vpunch
        "I collapse backward, my head landing on the pillows."
        "But before I can protest, Palla pounces on me."
        show palla blowjob noglasses with fade
        "And I mean that literally - she jumps on me like an animal on it's prey!"
        "I instinctively raise my legs, parting them to give her the space she needs."
        "And that's because even in a state of confusion, I know what Palla's doing."
        "Her head is between my thighs, hovering over the head of my cock."
        play sexsfx1 bj_sucking loop
        show palla blowjob lick
        "Then she goes lower, parting her lips - and I feel her swallow me!"
        "Part of me wants to crane my neck and lean forwards."
        "To see with my own eyes the sight of Palla sucking my dick."
        "But the only problem with that is the fact she's so damn good at it!"
        show palla blowjob at startle(0.1,-10)
        pause 0.2
        show palla blowjob at startle(0.1,-10)
        "Seriously, Palla's head bobs up and down as she picks up speed."
        "And with each passing second I feel myself surrendering to her more completely."
        "She knows how to use her lips, tongue and even her teeth to amazing effect."
        "Of course I always fantasised about what head from Palla would feel like."
        show palla blowjob at startle(0.1,-10)
        pause 0.2
        show palla blowjob at startle(0.1,-10)
        "But there's no way I could have imagined anything like this."
        if palla.sub <= 0:
            "Just when I'm settling into the experience, I feel something lower down."
            "The sensation of something pushing between the cheeks of my ass."
            show palla blowjob finger
            "And then it starts to probe around my actual hole!"
            "It can only be Palla's fingers, probing ever deeper into my butt."
            "And it only takes a couple of seconds for the initial shock to pass."
            "But by then it's obvious that Palla knows exactly what she's doing."
            "As she hits a spot that makes my eyes pop open from the sensation."
            "Oh man - that must be like, my prostate gland, or something?"
            "I remember hearing it called the male G-spot, but I never believed it."
            "Now Palla's giving me an education around the pleasure centres of my own body!"
            "You can probably guess that I've pleasured myself manually many times before now."
            "But it was never accompanied by anything like this."
        show palla blowjob at startle(0.1,-10)
        pause 0.2
        show palla blowjob at startle(0.1,-10)
        "I'm gasping for breath as the sensations wash over me."
        "And there's no way that I can hope to hold on for much longer."
        menu:
            "Cum on her face":
                "At the last moment, Palla releases me from her mouth."
                "Then she waits patiently for nature to take it's course."
                $ palla.sub += 2
                show palla blowjob cum hurt with vpunch
                "And she doesn't flinch a moment later, when I paint her face with sticky, white stripes."
            "Cum in her mouth":
                "Palla keeps me in her mouth until the very end."
                "And when it comes, she's more than ready."
                show palla blowjob cum hurt with vpunch
                "I watch in amazement as she swallows every drop."
                with vpunch
                "Staying in control and not gagging even once."
        stop sexsfx1 fadeout 0.3
        show palla blowjob -cum normal
    else:
        show bg bedroom1 at center, zoomAt(1.2, (640, 720))
        show bg bedroom1 at center, traveling(1.2, 0.5, (700, 720))
        "So I make a point of walking over to the bed and sitting down on the edge of the mattress."
        "Looking up at Palla with a smile on my face, I pat the spot next to me."
        mike.say "Never mind the décor, Palla..."
        mike.say "Why don't you come over here and sit down?"

        if palla.sub <= 80:
            "Palla raises an eyebrow at this, as if she sees right through me."
            show palla stuned at startle(0.1, 5)
            "But more importantly, she does as I suggest."
        else:

            "Palla's expression changes the moment I make the suggestion."
            show palla happy at startle(0.1, 5)
            "She nods eagerly and hurries to so as I suggest."
        show petite_4some_foreplay_bg_bedroom at center, blur, zoomAt(1.2, (640, 720))
        show palla normal zorder 1000 at zoomAt(1.4, (640, 950))
        "But once she's sitting by my side, I feel my nervousness begin to lessen."
        "Because as intimidating as Palla's beauty is, it's also pretty intoxicating too."
        "And having her so close to me means that there's little else I can think of."
        show petite_4some_foreplay_bg_bedroom at startle(0.1, 5)
        show palla zorder 1000 at startle(0.1, 5)
        mike.say "I..."
        mike.say "I had a really good time tonight, Palla."
        mike.say "In fact, it was the best night out I've had in ages!"

        if palla.sub <= 80:
            "Palla raise an eyebrow as she gazes into my eyes."
            show palla annoyed with dissolve
            "As if the statement were somehow provocative in nature."
            show palla joke at startle(0.1, 5)
            palla.say "HAD a good time?"
            palla.say "You make it sound like the night's already over, you know?"
            palla.say "Like there's nothing I could do to make it even better."
            show palla normal
        else:

            "Palla looks at me with something like disbelief in her eyes."
            "As if there were something scandalous about the statement I just made."
            show palla submissive at startle(0.1, 5)
            palla.say "But, [hero.name]…"
            palla.say "You're talking like the night's already over!"
            palla.say "But I can make it better still, I promise you..."
            show palla flirt
        "I'm about to open my mouth and explain that I didn't mean anything of the sort."
        "But that's when I feel something touching me below the waist."
        "And a quick glance down there confirms my suspicions."
        "In the time that we've been talking, Palla's slid her hand down there without my noticing."
        "And now she's stroking and caressing my groin, making things stir more with each passing second."
        show petite_4some_foreplay_bg_bedroom at startle(0.1, 5)
        show palla zorder 1000 at startle(0.1, 5)
        mike.say "Oh..."
        mike.say "Well, if that's what you want, Palla..."
        mike.say "Don't let me stand in your way!"
        "I put my hands out behind me, using them to prop myself up on the bed."
        "But the move also has the symbolic gesture of putting my hands well out of the way."
        "Which kind of means that I'm surrendering myself to Palla's intention."
        "Effectively letting her know that she's free to do whatever she has in mind."
        show palla talkative at traveling(1.5, 0.5, (640, 1000))
        palla.say "Okay, [hero.name]…"
        palla.say "Just sit back and leave everything to me."
        show palla flirt
        "Palla's looking me straight in the eye as she says this."
        "But as soon as I nod my head, she turns her gaze downwards."
        show palla at traveling(1.5, 1, (640, 1500))
        "At the same time Palla slides off the bed and onto the floor."
        "She repositions herself in front of my, settling between my legs."
        "All the while her hands are still on my groin, unzipping my flies."
        "A feat which she achieves with startling ease and dexterity."
        "Because before I know it, I feel the sensation of her fingers sliding into my shorts."
        "I can't help gasping as Palla takes a firm hold of my cock and begins to release it."
        "Don't get me wrong, it's not that she's being especially rough with me right now."
        "Oh no, it's more that the excitement and anticipation is already building inside of me."
        show palla blowjob at center, zoomAt(1, (640, 720)) with fade
        "That means every time she touches me, the sensation is heightened to a significant degree."
        "Even so, it's not yet fully erect when she pulls it out and begins to get to work."
        "In a way, that makes what comes next all the more enjoyable for me."
        "As Palla instantly starts to stroke and squeeze the shaft."
        show palla blowjob lick at center, zoomAt(1, (640, 720)) with dissolve
        play sexsfx1 bj_sucking loop
        "And when she chooses to also lean in and begin to use her lips too..."
        "Well, you can probably imagine how much that speeds things up."
        "At first Palla only uses her mouth on the lowest parts, kissing and licking at the base."
        "She's still using her hand higher up to encourage me to get stiffer."
        "But as things progress, she seems to be keeping a close eye on how hard I'm getting."
        show palla blowjob at startle(0.1, 5)
        "Because as soon as the hand is no longer needed, her lips start to move higher."
        "Staring down I watch in silent, helpless fascination as her mouth kisses my cock."
        "Palla doesn't look up to return the gaze, not even once."
        "And I get the impression that, for her, this is a lot like a professional gig."
        "Not that I mean she's doing all of this out of a desire for money, not at all."
        "More that she's approaching the task with the same kind of intense focus that she does in her working life."
        "I can feel the evidence of that too, the attention to detail translating into sensations of sheer pleasure."
        show palla blowjob at startle(0.1, 5)
        "And by the time Palla's mouth reaches the head of my cock, I'm completely in her power."
        "So when she parts her lips and takes it into her mouth, I let out an almost desperate whimper."
        show palla blowjob at startle(0.1, 5)
        "Luckily for me, Palla doesn't seem to notice the sound, and simply presses on."
        "I'm still watching Palla closely, almost fighting to keep from holding my breath."
        "After all of the steady build that she's engaged in up to this point, I'm expecting more of the same."
        "To see her ease her way downwards again, but this time with it inside of her mouth."
        "And I guess that Palla's totally aware of the affect her efforts are having on me."
        "Because she suddenly throws all of that caution to the wind, and changes pace."
        "Rather than going slow and steady, she almost dives into my cock."
        "Within a few seconds it's all the way into her open mouth."
        "And then she's into it, head bobbing up and down as she sucks like a plunger."
        "Now my hands are literally grabbing onto bunches of the bedclothes."
        "Like I'm trying to hold myself in place for fear of falling off the bed."
        "None of what I'm doing seems to be concerning Palla in the slightest."
        "But my guess is that she knows exactly what she's doing to me right now."
        show palla blowjob at startle(0.1, 5)
        "Because the effect it's having on me is pretty dramatic."
        "I can feel the sweat starting to bead on my forehead."
        "The pleasure coursing through me making my heart pound in my chest."
        show palla blowjob at startle(0.1, 5)
        "Palla seems to be reading my mind right now, as she instantly kicks it up a notch."
        "Now I can feel my cock starting to go even deeper into Palla's mouth."
        "So deep in fact that it must be slipping down into the top of her throat."
        "The mere thought of that is enough to make me rise to the same level as Palla."
        "But almost as soon as I'm sure that it's in Palla's throat, I feel myself begin to lose it."
        "As much as I'd love for this to keep on going, there's just no way I can hold on any longer."
        "I know that at any moment I'm going to explode, and the sensation makes me look down."
        "Which is when I realise that Palla's gazing up at me too."
        "In that moment I realise she's every but as aware of it as I am."
        "And that she's silently asking me what's going to happen next."
        stop sexsfx1
        menu:
            "Swallow":
                "I make a desperate gesture downwards with one hand."
                "And much to my relief, Palla seems to catch on instantly."
                "Because she redoubles her efforts, taking me even deeper than before."
                "Which, of course, means that I instantly lose control of myself."
                show palla blowjob cum at vpunch
                "And the next thing I know, I'm shooting my load straight down Palla's throat."
                "But as she's prepared, everything goes off without a hitch."
                "As Palla swallows every last drop without hesitation."
            "Facial":
                "I make a desperate gesture upwards with one hand."
                "And much to my relief, Palla seems to catch on instantly."
                "Because she opens her mouth and raises her head."
                "Which of course means that my cock slides straight out of her mouth."
                "And once it's free, she waits patiently on the same spot."
                show palla blowjob cum at vpunch
                "Not moving an inch as I shoot my load straight into her face."
                "Palla simply sits there as it paints stripes across her nose and cheeks."
                "Making no attempt to shield herself from the white, sticky shower."
    $ palla.sexperience += 2
    $ hero.energy -= 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
