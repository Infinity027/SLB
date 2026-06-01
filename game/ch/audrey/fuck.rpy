init python:
    Event(**{
    "name": "audrey_hottub_sex_male",
    "label": "audrey_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(audrey,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

    InteractActivity(**{
    "name": "audrey_fuck_mc_office",
    "display_name": "Fuck",
    "label": "audrey_fuck_mc_office",
    "conditions": [
        IsDone("audrey_event_06"),
        HeroTarget(
            HasRoomTag("mcoffice"),
            HasStamina(),
            ),
        PersonTarget(audrey,
            IsActive(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "audrey_boardgame_sex",
    "label": "audrey_boardgame_sex",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_play_boardgame")),
        PersonTarget(audrey,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 5),
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": False,
    "once_week": True,
    "duration": 1,
    })

    InteractActivity(**{
    "name": "fuck_audrey",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(audrey,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

label audrey_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "I should be over the moon that Audrey agreed to come over to my place to use the hot-tub."
    "I mean, who wouldn't want to share that hot bubbling water with a girl that's just as hot?"
    "It's just that I know Audrey better than that by now, and I know what to expect too!"
    "Sure, she might have said yes, but there's got to be a catch somewhere."
    "She's the kind of girl that thrives on conflict and drama."
    "So I'm on the lookout for the signs almost as soon as she turns up on the doorstep."
    show audrey swimsuit at center, zoomAt(1.2, (640, 820))
    "Well, that is until I catch sight of her in a swimsuit..."
    audrey.say "Hey, [hero.name]."
    "Audrey saunters out of the house and towards the hot-tub."
    "And I'm instantly glad that I'm already sitting in the water."
    "Because it means she can't see the effect she's having on my cock right now!"
    "All the same, Audrey looks me in the eye as she climbs into the tub."
    audrey.say "I see the way you're looking at me, [hero.name]!"
    audrey.say "You should be thankful we're not at work."
    audrey.say "Because I'd be reporting you for sexual harassment!"
    "I laugh nervously, choosing to take what Audrey just said as a joke."
    "But Audrey just holds my eye, not changing the look on her face."
    "The serious look on her face makes me start to feel nervous."
    "I swallow audibly, starting to think that she's serious."
    show audrey happy at startle(0.1, -5)
    play sound audrey_laughs_light_2
    audrey.say "Got you, [hero.name]!"
    audrey.say "Shit - the look on your face!"
    show audrey normal
    "Audrey laughs as if it's the funniest thing in the world."
    "But all I can manage is a nervous chuckle."
    mike.say "Ah, yeah, Audrey."
    mike.say "Real funny..."
    show audrey talkative at startle(0.1, -5)
    audrey.say "But seriously though, [hero.name]."
    audrey.say "You rent this place, right?"
    hide audrey
    show hottub audrey with fade
    "The question comes completely out of the blue."
    "And I can't for the life of me see what it has to do with anything."
    mike.say "Ah, yeah, Audrey."
    mike.say "That's right."
    "Audrey screws up her nose a little."
    "She looks down at the water and then back up at me."
    audrey.say "So that means everyone that lived here before you used this tub too."
    audrey.say "Urgh..."
    audrey.say "Imagine how many people must have screwed in here before now!"
    mike.say "I...I guess, Audrey."
    mike.say "I never really thought about it before now!"
    audrey.say "Yeah, there must be more semen in here than in a sperm bank!"
    audrey.say "In fact, I bet I could get pregnant just sitting on one of the water jets!"
    "I can already feel my confusion turning into anger."
    "Why did Audrey even bother to come here if she wanted to insult me?"
    "Why did she even get into a hot-tub that makes her feel that way?"
    "But as my blood begins to bubble and boil like the water in the tub, I remember something."
    "This is Audrey we're talking about, and she likes to get a rise out of people."
    "In fact, she always seems to be at her happiest when she's making someone mad."
    "And right now, that someone is me!"
    "So what else can I do but play along with her little game?"
    mike.say "You want to watch your mouth, Audrey."
    mike.say "Some guys wouldn't like to hear you talking to them like that!"
    "I see a light appear in Audrey's eyes as I say this."
    "The tone of my voice seems to perk up her interest too."
    audrey.say "Oh yeah?"
    audrey.say "And just what would a guy like that do about it, [hero.name]?"
    audrey.say "As if you'd even know!"
    mike.say "Well, Audrey..."
    mike.say "He might do something like this..."
    "I give Audrey's ass a little tap, splashing water in the air as I do so."
    "It wasn't enough to even be called an attempt at spanking her."
    "But even so, the effect it has on Audrey is instant and dramatic."
    "She lets out what can only be described as a squeal of pleasure."
    "And I find her ass rising out of the water and being thrust in my direction."
    audrey.say "Oh, [hero.name]!"
    audrey.say "You beast!"
    audrey.say "You absolute beast!"
    if audrey.sub >= 25:
        show hottub sex male audrey outside naked
    else:
        show hottub sex male audrey outside
    with fade
    "Sure, I know all too well that I'm playing Audrey's sick little game."
    "But the sight of her as she turns her back on me and presents her backside..."
    "Well, it's too good of an opportunity for me to pass up."
    "I reach out with one hand, taking a firm hold of Audrey."
    "And I use the other to pull down my trunks."
    "My cock is already good and hard from Audrey's teasing."
    "So it only takes me a moment to have it pressed up against her ass."
    call audrey_dick_reactions from _call_audrey_dick_reactions_1
    "Audrey makes a good show of wriggling and squirming as I do so."
    "But there's no way she's doing anything other than putting on an act."
    "Because I see her look over her shoulder a moment later."
    "And it's pretty obvious that she's making sure I'm on target!"
    "There's no need for her to be concerned in that department though."
    "I feel the head of my cock press against her pussy."
    show hottub sex male inside
    play sexsfx1 slide_in
    play sound audrey_generic_oh_1
    "And then I give it a firm push, parting her lips with relative ease."
    "Audrey lets out a moan of almost desperate release as I enter her."
    "The noise doesn't stop until I'm all the way in either."
    play sexsfx1 fuck_moderate loop
    play sound audrey_moans_happy_medium loop
    "And even then she keeps on panting as I begin to thrust in and out."
    "There's nothing subtle or sweet about what follows between us."
    "Audrey provoked me into giving it to her without holding back."
    "And that's just what she's getting from me now."
    "The only thing that changes is the speed that I'm pounding her at."
    "That and the amount of energy that I put into my efforts too."
    play sexsfx1 fuck_speed loop
    play sound audrey_moans_happy_high loop
    "But to her credit, Audrey takes everything that I give her."
    "Not only that, she keeps up with me the whole time, almost begging for more!"
    "Normally I'd be trying to keep it up for as long as I was able."
    "But the sheer amount of energy I've already put into it is taking it's toll."
    "I can already feel the end coming, my climax approaching..."
    call cum_reaction (audrey, 'vaginal', 1) from _call_cum_reaction_24
    if _return == "vaginal_outside":
        "I might have been playing Audrey's game up until now."
        "But I have one last trick up my sleeve before it's all over."
        show hottub outside
        play sexsfx1 pull_out
        play sound audrey_generic_oh_3
        queue sound audrey_moans_happy_orgasm_1
        "Just before I finally cum, I yank my cock out of her without warning."
        "Audrey all but shudders and cries out at the sudden sensation."
        show hottub cumshot with vpunch
        pause 0.2
        with vpunch
        pause 0.2
        with vpunch
        $ audrey.sub += 1
        "And she looks over her shoulder in surprise as I shoot my load over her."
    else:
        "There's no chance of me being able to pull out of Audrey before the end."
        "And I doubt that either one of us actually wants that to happen."
        "So I keep right on until the end, pushing as deep into her as possible."
        show hottub cumshot ahegao with hpunch
        play sexsfx1 final_thrust
        play sound audrey_generic_oh_3
        queue sound audrey_moans_happy_orgasm_1
        pause 0.2
        with hpunch
        pause 0.2
        with hpunch
        $ audrey.love += 1
        "When I lose it, Audrey writhes on the end of my cock, loving every moment."
    hide hottub
    show hottub audrey
    with fade
    "Afterwards, Audrey seems satisfied and almost subdued."
    "But there's an unmistakable glint in her eyes that lets me know she's gloating in silence."
    "After all, she got exactly what she wanted, making me dance to her tune."
    "And yet it's not like I didn't enjoy being manipulated by her too..."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ audrey.sexperience += 1
    $ game.active_date.clothes = None
    return

label audrey_fuck_date_male(location="hero"):
    $ renpy.dynamic(skip_foreplay=False)
    $ game.play_music("music/roa_music/city_nights.ogg")
    if location == "hero":
        scene bg livingroom
    else:
        scene bg audreylivingroom
    show audrey kiss
    with fade
    $ audrey.flags.kiss += 1
    "As soon as the door is closed I pick Audrey up and she wraps her legs around my waist as I kiss her heavily."
    menu:
        "Lay her on the couch":
            $ audrey.love += 1
            "I quickly take her over to the couch and lay her down."
            "I climb on top of her and start to kiss her deeper and leave bite marks on her neck."
            if location == "hero":
                "Suddenly she puts her hands on my chest to stop me."
                hide audrey
                show audrey blush annoyed at center, zoomAt(1.5, (640, 1040))
                with hpunch
                audrey.say "This is a little bit too open for me... What if your roommates come home?"
                "I sigh."
                "She's right."
                "If one of the girls walk in we will have to stop and it will ruin the night."
                mike.say "Okay, we can go to my room."
                hide audrey
                show audrey kiss with fade
                "I lean down and start to kiss her again."
                "After she has her arms and legs wrapped around me I carry her to the bedroom."
            else:
                "Suddenly she puts her hands on my chest to stop me."
                hide audrey
                show audrey blush annoyed at center, zoomAt(1.5, (640, 1040))
                with hpunch
                audrey.say "Wait, let's got to my room."
                "She takes my hand and lead me in her bedroom."
        "Go to the bedroom.":
            $ audrey.sub += 1
            "I press my tongue into her mouth and she runs her fingers through my hair trying to make the kiss even deeper."
            "Hardly being able to see what I am doing I carry her to the bedroom almost falling into the wall once."
    if location == "hero":
        $ game.room = "bedroom1"
        scene bg bedroom1 with fade
    else:
        $ game.room = "audreybedroom"
        scene bg audreybedroom with fade

    if not audrey.flags.oral and randint(1, 3) == 1:
        call audrey_fuck_date_oral_intro from _call_audrey_fuck_date_oral_intro
        call audrey_fuck_date_oral from _call_audrey_fuck_date_oral
        $ skip_foreplay = True
    else:

        call audrey_fuck_date_intro_male (location) from _call_audrey_fuck_date_intro_male


    call audrey_dick_reactions from _call_audrey_dick_reactions


    if not skip_foreplay:
        call audrey_fuck_date_foreplay_male from _call_audrey_fuck_date_foreplay_male




    call audrey_fuck_date_choices_male from _call_audrey_fuck_date_choices_male


    call handle_npc_leaving (audrey, _return) from _call_handle_npc_leaving_3
    if _return:
        return


    hide audrey
    call audrey_sleep_date_fuck (location) from _call_audrey_sleep_date_fuck
    return

label audrey_fuck_date_intro_male(location="hero"):
    $ randintro = audrey.sexperience % 7
    if randintro == 0:
        show audrey
        "There's something in the air tonight as I open the door to my room and usher Audrey inside."
        "Not in the traditional, romantic sense of the term, when people mean that everything feels magical."
        "With her it's more like there's some kind of repressed tension hanging around the place."
        "Audrey just has that kind of edgy, almost dangerous air about her most of the time."
        "And as she eyes up the decor of my room, she certainly seems to be living up to that tonight."
        show audrey mock
        audrey.say "Whoa - someone's clinging onto their adolescence around here!"
        audrey.say "I hope you can get as big of a hard-on for me as you do for sci-fi movies..."
        "Shake my head at her words, determined not to rise to the bait this time."
        mike.say "Teasing someone about their taste in movies, Audrey?"
        mike.say "Isn't that a little childish too?"
        show audrey happy
        "A smile spreads across her face at my retort."
        "A smile that's equal parts infuriating and seductive."
        audrey.say "I could say the same thing about arguing tit-for-tat, [hero.name]!"
        show audrey underwear with dissolve
        "Audrey begins to strip off her clothes as she says this."
        audrey.say "But what do you say I give you a chance, huh?"
        audrey.say "A chance to prove just how manly you really are..."
        "Jesus - how does she do that?!?"
        "I don't know which would give me more pleasure right now - fucking her or throttling her?"
        "But that being said, I know very well which of the two won't land me in jail for the rest of my life."
        "So I hastily start to follow her lead, pulling off my own clothes as fast as I can."
        show audrey naked with dissolve
    elif randintro == 1:
        show audrey kiss
        "Luckily my door wasn't locked and we go right in, pausing long enough for me to lock it behind us so we won't be interrupted."
        "I carry her to the bed and lay her down as we continue to make out."
        "I lose track of anything else around me when suddenly she pulls away for air."
        hide audrey
        show audrey blush
        with fade

























        mike.say "Take your clothes off!"
        show audrey underwear with dissolve
        "Audrey gets up and submissively comply to my order."
        show audrey naked with dissolve
        mike.say "You look amazing."
        show audrey naked blush
        "I see Audrey smile."
        audrey.say "Thanks babe. Does it make you wanta do anything?"
        show audrey naked
    elif randintro == 2:
        show audrey
        "Sometimes it's really nice to have a long, gradual build-up to indulging yourself."
        "You know, a nice meal or watching a something on TV that gets you relaxed and in the mood."
        "Then you follow that with a slow-burning kiss, maybe some gentle foreplay..."
        "Or in that case of Audrey and myself, you skip all of that and just fuck each other senseless!"
        "The door flies open and slams loudly against the wall as we stagger into my bedroom."
        "It could have left a dent or even fallen off of the hinges for all I know."
        show audrey flirt
        "But I don't care, as all of my attention is on Audrey."
        "Or to be more precise, on her tongue as she shoves it down my throat."
        show audrey kiss with fade
        "That and her hands as they roughly tug at my flies, trying to get at my cock."
        "Not that this thing is at all one-sided in nature, as mine are trying to undress her too."
        "I've always been turned on by the sight of Audrey's body, and right now she's got me hard."
        "But knowing that she wants me inside of her so badly is more encouragement than I ever needed!"
        "We're both naked by the time I feel my legs hit the side of the bed."
        hide audrey
        show audrey naked with fade
    elif randintro == 3:
        show audrey
        "One thing that's great about Audrey is the way that she communicates in the bedroom."
        "Sure, outside of it she can be pretty confusing, even infuriating sometimes."
        "But once that door is closed, she knows what she wants and goes about getting it!"
        show audrey happy
        "And tonight is no exception, with her almost pouncing on me the moment we're alone."
        "I already thought that the date went well, and it seems like Audrey does too!"
        show audrey kiss with fade
        "The kiss that she plants on me is so passionate that it takes me by surprise."
        "And I can feel her grinding herself against me the whole time our lips are pressed together."
        "Needless to say, it doesn't take me long to get hard!"
        "I make to return the kiss with just as much passion."
        hide audrey
        show audrey flirt
        with fade
        "But that's when Audrey breaks it off and twists herself out of my grasp."
        "She leaves me standing there, mouth hanging open and arms outspread."
        "And then her laughter hits me like a slap to the face, almost feeling like a physical sting."
        "Of course, how could I have been so stupid?"
        "This is Audrey we're talking about here."
        "She's the biggest tease I've ever met!"
        "All I can do is stand there as Audrey walks over to the bed and starts to strip off."
        show audrey happy
        "But then she laughs out loud, shaking her head at my reaction."
        audrey.say "What did you think, [hero.name]?"
        audrey.say "That I wasn't going to make you work for it?!?"
        audrey.say "Well, are you just going to stand there like a slapped fish?"
        show audrey naked with dissolve
        "By now she's almost completely naked, tossing her clothes aside."
        "And all I'm doing is standing still, rooted to the spot as I watch her."
        "She's damn right - what in the hell am I waiting for?"
        "Without wasting another second, I shake my head, snapping myself out of it."
        "And a moment later I'm right by her side, almost beating her to the punch."
        "In fact, I'm moving so fast that she only just manages to get naked before me!"
    elif randintro == 4:
        show audrey kiss
        "Once we're inside, we don't so much close the door as collapse against it."
        "Audrey all but pounces on me, actually jumping and clinging onto me!"
        mike.say "Whoa..."
        mike.say "Audrey..."
        mike.say "Slow it down a little!"
        "Audrey's tearing at my clothes and kissing my neck."
        "But she manages to find time to gasp out an answer all the same."
        show audrey flirt at center, zoomAt(1.5, (640, 1040))
        audrey.say "Nah..."
        audrey.say "Fuck that..."
        audrey.say "I want your cock...NOW!"
        "Well, when she puts it like that - how can I say no?"
        hide audrey
        show audrey kiss with fade
        "From that moment on I stop even trying to hold back."
        "As Audrey is desperately trying to undress me, I do the same to her."
        show audrey kiss underwear with dissolve
        "She still tries her best to cling to me as we stagger towards the bed too."
        "This makes our progress slow and awkward, dragging things out."
        "But it also means that I have my hands all over her the whole time."
        "And Audrey's fingers are moving across my body too."
        hide audrey
        show audrey underwear
        "So when we finally reach the bed, we're both hot and panting."
        show audrey naked with dissolve
        "Audrey tears off the last of my clothes, tossing them aside."
        "Then she shoves me backwards onto the bed." with vpunch
    elif randintro == 5:
        show audrey
        "Audrey's definitely in the mood to have some fun when we get back to my place."
        "She leads me into my bedroom by the hand, smiling at me the whole time."
        show audrey happy
        "And I can feel my own enthusiasm growing by the second as we walk towards the bed."
        "There's just something so sexy about the way Audrey moves when she's in the mood."
        "All of that urge to provoke and tease gets translated into sheer sexiness."
        audrey.say "Hey!"
        show audrey flirt
        audrey.say "Why are you looking at me like that?"
        "Audrey's question catches me off-guard, bringing me back to reality."
        "Sure, she still looks hot as hell right now."
        "But she's looking at me with a quizzical expression."
        mike.say "Huh?"
        mike.say "What do you mean, Audrey?"
        mike.say "I was just checking you out."
        mike.say "You know, because you look so hot?"
        "Audrey laughs and shakes her head."
        audrey.say "Oh, [hero.name]..."
        show audrey joke
        audrey.say "Do you ever think anything you don't say?"
        "I frown, not sure what to make of the question."
        "But it seems like Audrey's not interested in an answer anyway."
        "Because she pushes me down onto the bed, still shaking her head."
        show audrey normal
        audrey.say "Never mind, [hero.name]."
        audrey.say "I don't want to over-tax your brain."
        audrey.say "Let's just fuck, okay?"
        "Now that's something I can understand!"
        "I nod, already pulling off my clothes in anticipation."
        "Audrey nods approvingly, as she stands up by the side of the bed."
        "But when she starts to strip-off, she does it with more style."
        "I've got most of my clothes off by this point, but I start to slow down."
        "And that's because I'm spell-bound as I watch Audrey remove one garment at a time."
        show audrey underwear with dissolve
        "With each one that goes, I get to see ever more of her body beneath."
        "Sure, I've seen it before, more than a few of times."
        "But that doesn't stop me getting excited as I'm seeing it now."
        "Audrey knows it too, and she's enjoying the power she has over me."
        show audrey underwear topless with dissolve
        "She smiles as each item of clothing comes off and is dropped to the floor."
        "Loving the way I'm staring at her, like there's nothing else in the world."
        "As she finally inches down her panties, Audrey gives me a wink."
        audrey.say "You ready for me, [hero.name]?"
        audrey.say "Because I'm ready for you!"
        show audrey naked with dissolve
        "I nod eagerly, almost tearing off the last of my clothes."
        "Then I spread my arms wide, beckoning Audrey towards me."
        "She giggles wickedly and hurries towards the bed."
    elif randintro == 6:
        show audrey
        "Audrey's been teasing me all night, the whole time that we've been on our date."
        "Sure, she hasn't come out and admitted it, because that's not her style."
        "But the way she's been walking around in those high-heels she has on..."
        "Well, I'm on hundred percent sure she knows the effect they have on how she moves."
        "The way they show off the shape of her legs and the curve of her butt!"
        "More than once she's caught me staring with helpless desire."
        "And every time she's made sure to give me a chuckle and a knowing wink."
        "It's only when we finally get back to my place that she actually admits it."
        "As I close my bedroom door, I turn around to see Audrey strutting up and down."
        show audrey frown
        show fx question
        audrey.say "What's the matter, [hero.name]?"
        audrey.say "Looks like something's distracting you!"
        hide fx
        "I pretty much end up leaning with my back against the door."
        "All I can do is stare at Audrey's legs, they look that fucking good!"
        audrey.say "So what is it, [hero.name]?"
        show audrey joke
        audrey.say "Are you a leg guy?"
        audrey.say "Or one of those dudes that's really kinky?"
        audrey.say "The kind that like a girl to walk on them and stuff?"
        "I shake my head at the second option."
        "All the time still staring at Audrey's legs."
        mike.say "Just a leg guy, Audrey."
        mike.say "Especially when they look like that!"
        "Audrey rewards me with a laugh and a smile."
        show audrey close flirt
        "Then she reaches out and cups my chin in her hand."
        "This finally forces me to tear my gaze away from her legs."
        "And I find myself staring her in the face for the first time."
        audrey.say "Then we need to make sure you get a good look at them."
        audrey.say "We need to make sure you can see them all the time you're fucking me!"
        "I'm nodding as she says all of this."
        "And I don't seem to remember even starting to take off my clothes."
        "But a quick glance downwards shows me that I'm already halfway done."
        show audrey underwear b -close with dissolve
        "And when I look back up again, I see that Audrey's following my lead."
        "Yet somehow she's still managed to strip off more than I have."
        "I guess she was just wearing less to begin with!"
        "Not that it seems to matter - this isn't a race."
        show audrey naked with dissolve
        "And the fact that Audrey's naked first soon becomes a bonus for me."
        "Because she's the kind of girl that always enjoys having eyes on her."
        "That means Audrey can't help starting to pose and pout as I finish stripping off."
    return

label audrey_fuck_date_foreplay_male:
    menu:
        "Blowjob" if audrey.sub >= 25:
            call audrey_fuck_date_blowjob from _call_audrey_fuck_date_blowjob
        "Oral" if audrey.flags.oral and hero.sexperience >= 5:
            call audrey_fuck_date_oral from _call_audrey_fuck_date_oral_2
    call stop_all_sfx from _call_stop_all_sfx_6

    return _return

label audrey_fuck_date_choices_male:
    menu:
        "Missionary":
            call audrey_fuck_date_missionary (0) from _call_audrey_fuck_date_missionary
        "Spoon" if hero.sexperience >= 5 and game.room != "audreybedroom":
            call audrey_fuck_date_spoon (5) from _call_audrey_fuck_date_spoon
        "Doggy" if hero.sexperience >= 10:
            call audrey_fuck_date_doggy (10) from _call_audrey_fuck_date_doggy
        "Cowgirl" if hero.sexperience >= 15:
            call audrey_fuck_date_cowgirl (15) from _call_audrey_fuck_date_cowgirl
        "Reverse cowgirl" if hero.sexperience >= 20 and "audrey_sub_event_02" in DONE:
            call audrey_fuck_date_reverse_cowgirl (20) from _call_audrey_fuck_date_reverse_cowgirl
        "Stand" if hero.sexperience >= 25:
            call audrey_fuck_date_stand (25) from _call_audrey_fuck_date_stand
    call stop_all_sfx from _call_stop_all_sfx_7

    return _return

label audrey_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        if location == "hero":
            scene bg bedroom1
            show audrey naked
            if audrey.is_sex_slave:
                audrey.say "May I share your bed tonight, Master?"
            else:
                audrey.say "Mmm...you cool with me spending the night here?"
            menu:
                "No":
                    mike.say "No...I have to be up really early in the morning."
                    "The sex was beyond incredible, but now I want to be alone."
                    "Audrey frowns in disappointment, clearly trying to shrug off the sense of rejection."
                    audrey.say "Okay...sleep well, I guess."
                    "She shakes her head as she collects her things and leaves my bedroom."
                    $ audrey.love -= 3
                    call sleep from _call_sleep_24
                    $ game.room = "bedroom1"
                "Yes":
                    mike.say "YES...I mean, yes...if you want to!"
                    "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                    show cuddle audrey with fade
                    "Audrey curling up against me beneath the covers is almost as good as the sex - almost..."
                    audrey.say "Sweet dreams, [hero.name]..."
                    mike.say "You too, Audrey..."
                    $ audrey.love += 3
                    call sleep ("audrey") from _call_sleep_12
                    $ game.room = "bedroom1"
        else:
            $ game.room = "street"
            $ game.pass_time(2, True)
    return

label audrey_fuck_date_blowjob:
    scene
    show audrey bj
    with fade
    "I only have the chance to blink once before she's on me."
    "Audrey peels of the last of her clothes so that she's standing over me naked."
    "There's no time to appreciate the view though, as she moves like lightning."
    audrey.say "There it is!"
    audrey.say "Gimmie that thing!"
    "Audrey slithers over the bed, reaching out to grab hold of my cock."
    "I wince as her hand closes around the shaft with an iron grip."
    mike.say "Go easy on me, Audrey!"
    mike.say "It's not like I'm resisting!"
    "Audrey shoots me a look that shuts me up in an instant."
    "Her eyes are wide and full of predatory instinct."
    "And she give my cock an even harder squeeze, just to make her point."
    "My cock was already getting hard before we even got into my bedroom."
    "But now that it's in Audrey's hands, it's getting harder still."
    "It seems like the more she squeezes and tugs, the more I like it!"
    "So I just hold my hands up and stop protesting."
    "This gets me a knowing half-smile from Audrey."
    "Then she lowers her head, still holding my eye."
    "Her hand moves downwards as her lips part."
    "I watch Audrey's tongue emerge from between her lips."
    "Only now does she turn her eyes to the task at hand."
    show audrey bj blink
    "Audrey stops looking at me the same moment her tongue goes into action."
    "Which is a relief, as I soon feel like I'm losing my mind!"
    "From the very first moment she begins licking the tip, I'm entranced."
    "Audrey doesn't look like she's going through the motions of giving head."
    "It seems more like she's doing something that she needs in order to live!"
    "She kisses, licks and nibbles between pants and moans of pleasure."
    "And of course I'm soon making the same kind of sounds myself."
    "Audrey works the shaft of my cock with one hand."
    "The other she uses to pinch her nipples at first."
    "Then she slides it between her legs, stroking her own pussy."
    "Just when I think that I can't get anymore aroused, Audrey kicks it up a notch."
    play sound audrey_moans_blowjob_low loop
    show audrey bj blowjob normal
    "Without warning she wraps her lips around my cock."
    show audrey bj at startle (0.1, 10)
    "And then she swallows it deep into her mouth in one smooth motion."
    mike.say "Oh fuck..."
    mike.say "Audrey..."
    "If she hears me cry out, then Audrey makes no show of it."
    show audrey bj blink at startle (0.075, 10)
    pause 0.2
    show audrey bj at startle (0.075, 10)
    "Instead she moves faster still, head bobbing up and down."
    "She seems to be swallowing almost all of me each and every time."
    "And the feeling of being in her mouth is impossibly good."
    show audrey bj at startle (0.075, 10)
    pause 0.2
    show audrey bj at startle (0.075, 10)
    "Audrey's hands goes down as her head goes up."
    "Each time I honestly think I'm going to lose it."
    "But somehow I still manage to hang on, gasping for breath."
    show audrey bj normal at startle (0.075, 10)
    pause 0.2
    show audrey bj at startle (0.075, 10)
    "Audrey seems to sense that I'm getting close to the end."
    "And she looks up at me for the first time."
    "I think she's trying to guess where I want this thing to go!"
    menu:
        "Cum on her face":
            "I motion upwards, and Audrey seems to catch on straight away."
            play sexsfx1 pull_out
            play sound audrey_moans_breathing_fast
            queue sound audrey_moans_breathing_slow
            show audrey bj blink out
            "She lets my cock slide out of her mouth as she raises her head."
            "Then she closes her eyes, a knowing smile spreading across her face."
            $ audrey.love += 2
            play sexsfx1 cum_outside
            play sound audrey_generic_oh_2
            show audrey bj cumshot with vpunch
            "A moment later I lose it, shooting my load straight at her."
            with vpunch
            "Audrey gasps as the hot, sticky cum spatters across her cheeks."
            show audrey bj dickcum -cumshot with vpunch
            "Then she laughs as it runs down and over her lips."
            "Audrey lick it up eagerly, as if she's savouring the taste."
        "Cum in her mouth":
            "I motion downwards, and Audrey seems to catch on straight away."
            show audrey bj blink
            play sound audrey_moans_blowjob_high loop
            "She gets herself into a safe position and prepares for what's coming next."
            "Then she closes her eyes, a knowing smile spreading across her face."
            $ audrey.sub += 2
            show audrey bj cumshot with vpunch
            "A moment later I lose it, shooting my load straight down her throat."
            play sound audrey_moans_blowjob_swallow
            with vpunch
            "Audrey's cheeks bulge for a few seconds, and then she starts to swallow."
            with vpunch
            "Not missing a beat, she gulps down every drop of cum I have to give."
            show audrey bj normal
            "And she looks like she's enjoying every second of it too!"
    stop sexsfx1 fadeout 1
    stop sound fadeout 1
    hide audrey
    scene expression f"bg {game.room}"
    show audrey close naked
    with fade
    "Afterwards, Audrey props herself up on her elbows and regards me."
    "I smile down at her, wondering if this will mark a change in her."
    "Maybe this is the start of a new, more sensitive and caring Audrey?"
    "And that's the very moment Audrey chooses to squeeze my balls as hard as she can!"
    mike.say "Aargh!"
    mike.say "What the hell, Audrey?!?"
    show audrey close flirt
    audrey.say "Just keeping you on your toes, [hero.name]."
    audrey.say "I don't like you staring at me dreamily."
    audrey.say "You know, like I'm some kind of fairy-tale princess!"
    show audrey close happy
    audrey.say "Just you remember - I bite!"
    "I nod, wondering how I could ever have thought otherwise."
    return

label audrey_fuck_date_oral_intro:
    "Audrey's one of those girls that just can't hide it when she has something on her mind."
    "Especially when it's something that's to do with what goes on in the bedroom too."
    "You know what I mean by that, right?"
    "She might not say anything out loud or drop any clues by accident."
    "But she still can't help shooting you those brief, sideways glances."
    "That and she'll have a knowing smile on her face the whole time as well."
    "And yet she'll flat out deny it."
    "Just like Audrey does when I try to call her bluff."
    "We've just made it back to my room after a pretty great date night."
    "But it's been bugging me all the way back here."
    "And so as soon as I close the door behind me, I ask the question."
    mike.say "Audrey..."
    mike.say "What's on your mind?"
    "I was at least hoping the question might surprise Audrey."
    show audrey happy
    "But she just lets out a peal of laughter and shakes her head."
    show audrey flirt
    audrey.say "Oh, wouldn't you like to know!"
    show audrey normal
    mike.say "Ah, come on, Audrey!"
    mike.say "It's going to be bugging me all night."
    mike.say "And you don't want me asking you while we're doing it, do you?"
    show audrey happy underwear with dissolve
    "Audrey laughs again as she begins to strip off her clothes."
    audrey.say "Okay, [hero.name], okay."
    audrey.say "That's just not going to happen."
    audrey.say "Not with what I have in mind!"
    show audrey naked with dissolve
    "The possibilities of what Audrey just said has me instantly intrigued."
    "And I hurry to follow her lead, stripping off as I walk to the bed."
    "Audrey smirks at me, knowing full well that I've fallen for it."
    "I offer no resistance as she pushes me down onto the bed."
    "And I can already feel my cock getting hard as she looks down at me."
    "Audrey climbs slowly onto the bed, straddling my thighs."
    "Her breasts hang down as she lowers herself onto me."
    "And her nipples almost brush my stomach as she does so."
    "I swallow as I wait for the sensation of her pussy against my cock."
    "But this is Audrey we're talking about - and she's a total tease!"
    show audrey naked flirt
    "Smiling wickedly, she dips her groin over and again."
    "Each time it almost rubs the lips of her pussy against me."
    "And yet she never lets herself get close enough to actually touch."
    "All the time she's doing this, Audrey is still gazing down at me."
    "I can see from the look on her face how much she's enjoying herself."
    "And so I just hang on in there, telling myself that I'll get my rewards soon enough."
    "But then I notice that Audrey's begun to move forwards."
    "She inches her way up my body and further away from my cock."
    "And I could flatter myself by exaggerating the length of it here."
    "But she's still out of its reach before too long."
    mike.say "Hey, Audrey!"
    mike.say "What are you doing?!?"
    audrey.say "Ah, [hero.name]."
    audrey.say "You talk too much."
    audrey.say "Time you put that mouth to better use..."
    "And with that, Audrey thrusts her herself forward."
    return

label audrey_fuck_date_oral:
    show audrey cunnilingus with fade
    "Before I know what's happening, my head is between her thighs."
    "But she doesn't stop there, and I feel Audrey pressing down on me."
    "An unconscious urge takes over, and I open my mouth to protest."
    "Which is just what Audrey was waiting for."
    "She pushes her pussy against my lips, never once pausing to ask permission."
    "It's clear that Audrey's only going to give me two choices here."
    "Either I get to work with my mouth."
    "Or else she suffocates me with her pussy!"
    "The second option sounds like a great way to go out."
    "But I think I'd rather take the first and live to see another day!"
    "Taking hold of Audrey's thighs with my hands, I set myself to the task ahead."
    "Which is, of course, to give her head!"
    "I begin by licking around the edges of Audrey's pussy."
    "I'm taking my time, being slow and deliberate where she was forward and less than subtle."
    "And by making sure I slow things down, I can be the one teasing Audrey for a change."
    "A quick glance up shows that it's working too."
    "Audrey is gazing down at me in complete silence."
    "She's also biting her lip as she tries to keep from crying out loud!"
    "Turning my attention back to her pussy, I begin to work my way inwards."
    "My tongue explores each fold as I get ever closer to the middle."
    "Audrey's all I can taste and the only scent in the air right now."
    show audrey cunnilingus pleasure
    play sound audrey_moans_happy_low loop
    "And I can hear her starting to moan, unable to hold it in any longer."
    "But when I finally plunge my tongue into the centre of her pussy, the effect is dramatic."
    show audrey cunnilingus gasp
    play sound audrey_generic_oh_4
    "Audrey cries out and I feel her hand grasp my cock."
    play sound audrey_moans_happy_medium loop
    "She begins to work the shaft as I plunge in further still."
    "And it feels like her hand is moving in time with my tongue."
    "Of course, the sensations is fantastic."
    show audrey cunnilingus pleasure
    "Not only that, but it also pushes me to up my game as well."
    "I redouble my efforts, exploring as deep into Audrey's pussy as I can."
    play sound audrey_moans_happy_high loop
    "In turn, her moans of pleasure intensify and she works my cock faster still."
    "Soon what we have going feels like it's feeding off of itself."
    "I lick Audrey deeper, she squeezes me harder, which makes me lick deeper than ever."
    "It feels like we could go on like this forever."
    "But we're only human, and we have human limits."
    show audrey cunnilingus pleasure cumshot with vpunch
    "I feel myself cumming, shooting my load into the air."
    show audrey cunnilingus pleasure cumonhand with vpunch
    "It runs over Audrey's fingers, making her grip on me slip."
    show audrey cunnilingus ahegao squirt with vpunch
    play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
    "And she cums too, desperately pulling herself away from me as she does so."
    show audrey cunnilingus pleasure -cumshot
    "From where I'm sitting, I can feel every moment of Audrey's orgasm."
    "It spreads out from her pussy, making her entire body quiver and quake."
    "She tosses her head this way and that, riding out the last moments for all they're worth."
    "And then she slithers down and lies herself across me, panting from the effort."
    $ audrey.love += 2
    "I'm tempted to say something to Audrey."
    "But I think my mouth already did it's best work of the night."
    "Anything I could actually say would just pale in comparison."
    "And so I keep quiet, enjoying the silence and the afterglow alike."
    stop sound fadeout 1
    $ audrey.flags.oral = True
    return

label audrey_fuck_date_missionary(sexperience_min):
    "Already ahead of me, Audrey finishes stripping-off before I'm even halfway done."
    "She climbs backwards onto the bed, chuckling at my efforts."
    "And she makes no effort whatsoever to hide an inch of her astonishing body as she does so."
    "This means that by the time I'm finally naked and climbing onto the bed, I'm as hard as a rock."
    "Audrey keeps her mouth shut now, simply raising her eyebrows in what I hope is anticipation."
    "She welcomes me literally with open arms, letting me embrace her as roughly as I like."
    show audrey kiss naked with fade
    $ audrey.flags.kiss += 1
    "I kiss her hungrily, feeling like she has an electric charge running through her body."
    "A charge that I need to restore my own energy, that I need to be able to live."
    "Yeah, I know how dramatic that sounds - but that's honestly the effect she has on me!"
    "There's no need for words or hints between us right now."
    "Audrey wants to be fucked."
    "And I want to fuck her."
    "Anything else is just a needless complication."
    show audrey missionary nomike with fade
    "I'll be inside of her as soon as I can manage it."
    "But where is it going to end up..."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            $ audrey.sub += 1
            show audrey missionary -nomike
            "I can't help the urge, and so I aim my cock low and push between Audrey's buttocks."
            "I'm not a sadist, and I'm not trying to break her in like you would a horse."
            "But there is a part of me that thinks she deserves to be fucked up the ass."
            "The kind of girl she is, I just know that she'll enjoy it more than she lets on."
            play sound audrey_generic_ah_3
            audrey.say "Wha...my...my ass!"
            audrey.say "You're gonna fuck my..."
            play sexsfx1 slide_in
            play sound audrey_generic_ah_5
            play sound audrey_moans_pained_low loop
            show audrey missionary anal
            audrey.say "Aaahh..."
            "Audrey's words melt away into a surprised moan as I feel my cock enter her anus."
            "And within moments of the shaft slowly and inexorably following the head, the moans are tinged with pleasure."
            "At the same time, her previously tight muscles surrender."
            play sexsfx1 fuck_calm
            "Which means I can begin to push in and out of her with more speed."
            "Audrey seems to surrender to me then, laying back on the bed, eyes rolling back into her head."
            "Her chin is cast back, exposing her neck."
            menu:
                "Choke her" if hero.fitness >= 50:
                    $ audrey.sub += 1
                    show audrey missionary choke
                    "It's in that moment I remember how much Audrey's into breath-play."
                    "Gingerly I reach out with both hands, placing them around her neck."
                    "I squeeze gently at first, just to let her know what I have in mind."
                    "Her eyes never open, but she nods her head just enough for me to notice."
                    show audrey missionary ahegao
                    play sound audrey_moans_pained_medium loop
                    audrey.say "Yeah...please..."
                    "Keeping up the rhythm of my cock thrusting into her ass, I tighten my grip on her neck."
                    "I figure it's best to build up, rather than just throttle her from the first."
                    "And so I slowly put on more pressure, until I see a reaction."
                    "Audrey's cheeks soon begin to flush, and she makes small gasping sounds."
                    "These increase steadily as I pile on more pressure and pound her ass at the same time."
                    "I can feel her body trembling from what I'm doing."
                    "And though I never thought I'd admit this - it's turning me on seeing her reaction!"
                    "The more Audrey writhes and struggles, the closer I get to cumming."
                "Don't choke her":
                    "Seeing her give in so completely to what I'm doing is a massive turn on."
                    "And I respond by quickening my pace as I pound into Audrey's ass."
                    "Her body absorbs the force of each and every thrust."
                    "And I watch as her breasts bounce in sympathy, nipples painfully erect."
                    "It feels good to be the one making Audrey moan and writhe on the bed."
                    show audrey missionary pleasure
                    "Not out of any cruel sense of revenge or need to demean her."
                    "But rather from the point of knowing that she's not as superior as she pretends to be."
                    "A part of me is quickly coming to the conclusion that she likes to play games."
                    "And being soundly fucked by someone that she's goaded seems to be the end result."
                    "Who knows, maybe she thinks that she doesn't deserve to be fucked unless it's fuelled by annoyance?"
                    "Whatever the reason, I've almost completely forgotten what she said to me before this."
                    "Instead, all I can think about is the sensation of my cock in her ass."
                    "That and the sight of her taking everything that I have to give."
            "My mind is pretty chaotic right now, but I still somehow know what's about to happen."
            "I only have a couple of moments before I tip over the edge and lose myself..."
            call cum_reaction (audrey, 'anal', sexperience_min) from _call_cum_reaction_25
            if _return == "anal_inside":
                "I couldn't pull out of Audrey now, not even if my life depended on it."
                "My cock is buried so deep inside of her that I wonder if I'll ever get it out again."
                show audrey missionary cum with hpunch
                $ audrey.love += 1
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "So when I shoot my load, it happens literally where the sun doesn't shine."
                with hpunch
                "Audrey bucks and twists in what I hope is a show of pleasure at taking it all."
                with hpunch
                "And I stay inside of her until the moment passes and my cock grown slack once more."
            elif _return == "anal_outside":
                $ audrey.sub += 1
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                "Call me cruel, but I want to add just one more little bit of humiliation to what I've already managed."
                show audrey missionary -anal
                "And so I plant my hands on Audrey's thighs and yank my cock out of her ass."
                play sexsfx1 pop_out
                play sound audrey_generic_oh_4
                queue sound audrey_moans_pained_orgasm_1
                "She moans and twists under me at the sudden sensation, but can't keep me inside of her."
                show audrey missionary cum
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                with hpunch
                "Almost the very second that it's freed, my cock bobs up and over her belly."
                show sexinserts chest audrey cum zorder 1 at center, zoomAt(1, (710, 740))
                with hpunch
                "Streamers of hot cum are instantly thrown across Audrey's curled abdomen and up her breasts."
                show audrey missionary bodycum dickcum with hpunch
                "I lean back and watch, as she writhes around, rubbing the semen all over her now glistening body."
                hide sexinserts
                hide bellycum
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            show audrey missionary -nomike
            "After all the time that Audrey's spent teasing and taunting me, I don't want to waste any more."
            "I don't hesitate to push the head of my cock against the lips of her pussy."
            play sound audrey_moans_discreet_low
            "She makes an appreciative sound at my efforts, letting me know that she's ready and willing."
            "But the fact that she's already soft and slick down there kind of gives that away."
            audrey.say "That's it..."
            audrey.say "Show me what I'm missing!"
            call check_condom_usage (audrey, 180) from _call_check_condom_usage_12
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show audrey missionary condom
            play sexsfx1 slide_in
            "The feeling of my cock sliding into Audrey is simply incredible."
            if CONDOM:
                show audrey missionary vaginal condom
            else:
                show audrey missionary vaginal
            "After so much goading beforehand, actually getting my hands on her is just so gratifying."
            "And it seems to be pretty much the same for Audrey too."
            "She lies back on the pillows as I get as deep into her as I can manage."
            play sound audrey_moans_happy_medium
            "And finally her cutting words are replaced by deep moans of pure pleasure."
            "Audrey seems to surrender to me then, laying back on the bed, eyes rolling back into her head."
            "Her chin is cast back, exposing her neck."
            menu:
                "Choke her" if hero.fitness >= 50:
                    $ audrey.sub += 1
                    show audrey missionary vaginal choke pleasure
                    "It's in that moment I remember how much Audrey's into breath-play."
                    "Gingerly I reach out with both hands, placing them around her neck."
                    "I squeeze gently at first, just to let her know what I have in mind."
                    "Her eyes never open, but she nods her head just enough for me to notice."
                    show audrey missionary vaginal ahegao
                    play sound audrey_moans_pained_high
                    audrey.say "Yeah...please..."
                    "Keeping up the rhythm of my cock thrusting into her pussy, I tighten my grip on her neck."
                    "I figure it's best to build up, rather than just throttle her from the first."
                    "And so I slowly put on more pressure, until I see a reaction."
                    "Audrey's cheeks soon begin to flush, and she makes small gasping sounds."
                    "These increase steadily as I pile on more pressure and pound her pussy at the same time."
                    "I can feel her body trembling from what I'm doing."
                    "And though I never thought I'd admit this - it's turning me on seeing her reaction!"
                    "The more Audrey writhes and struggles, the closer I get to cumming."
                "Do not choke her":
                    $ audrey.love += 1
                    show audrey missionary vaginal
                    "Seeing her give in so completely to what I'm doing is a massive turn on."
                    "And I respond by quickening my pace as I pound into Audrey's pussy."
                    "Her body absorbs the force of each and every thrust."
                    "And I watch as her breasts bounce in sympathy, nipples painfully erect."
                    "It feels good to be the one making Audrey moan and writhe on the bed."
                    "Not out of any cruel sense of revenge or need to demean her."
                    show audrey missionary vaginal pleasure
                    play sound audrey_moans_happy_high
                    "But rather from the point of knowing that she's not as superior as she pretends to be."
                    "A part of me is quickly coming to the conclusion that she likes to play games."
                    "And being soundly fucked by someone that she's goaded seems to be the end result."
                    "Who knows, maybe she thinks that she doesn't deserve to be fucked unless it's fuelled by annoyance?"
                    "Whatever the reason, I've almost completely forgotten what she said to me before this."
                    "Instead, all I can think about is the sensation of my cock in her pussy."
                    "That and the sight of her taking everything that I have to give."
            "And it won't be long before I do just that!"
            "As in the very next moment, I can feel myself ready to blow."
            call cum_reaction (audrey, 'vaginal', sexperience_min) from _call_cum_reaction_26
            if _return == "vaginal_condom":
                "Safe and secure in the knowledge that I've taken precautions, I keep right on going."
                "This means that I can spend the last ounce of my energies on making Audrey scream."
                $ audrey.love += 1
                show audrey missionary vaginal ahegao condom with hpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "And she does just that, wriggling and squirming on my cock as she cums too."
                with hpunch
                "Afterwards she collapses into a panting, but otherwise silent mass."
                show audrey missionary -vaginal condom cum
                "And all I can do is slide down atop her, equally exhausted and spent."
            elif _return == "vaginal_outside":
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                "I'd dearly love to keep right on going, to lose myself inside of Audrey."
                "But there's no way I'm feeling that reckless and stupid right now."
                show audrey missionary -vaginal
                "And so I put my hands on her thighs and yank my cock out of her."
                $ audrey.sub += 1
                play sexsfx1 pull_out
                play sound audrey_generic_oh_4
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                show audrey missionary cum
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                with hpunch
                "Audrey makes a sound that's filled with sensuality and not a little disappointment."
                show audrey missionary cum dickcum
                show sexinserts chest audrey cum zorder 1 at center, zoomAt(1, (710, 740))
                with hpunch
                "But she doesn't complain or chastise me, simply lying there as my cum hits her belly and breasts."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_inside_pill":
                audrey.say "No..."
                audrey.say "Don't you dare..."
                audrey.say "I'm on the damn pill!"
                "By the time her words have sunk in, she's made sure of what she wants anyway."
                $ audrey.love += 2
                show audrey missionary cum with hpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "I lose myself as deep inside of Audrey as I can, filling her completely."
                with hpunch
                "She rides me to the last, squeezing all that she can out of my now lifeless cock."
            elif _return == "vaginal_inside_pregnant":
                "I smile as I feel the curve of Audrey's pregnant belly against my own."
                show audrey missionary cum with hpunch
                "And it's all the licence that I need to lose myself inside of her."
                $ audrey.love += 3
                with hpunch
                "She moans in pleasure at the sensation, and I savour it too."
                "It feels as good right now as it did the moment that I made her pregnant too!"
            elif _return == "vaginal_inside_mad":
                show audrey missionary cum with hpunch
                #$ audrey.impregnate()
                play sexsfx1 cum_inside
                play sound audrey_generic_ah_3
                audrey.say "Oh shit...oh shit!"
                mike.say "What is it?"
                audrey.say "Did you just cum in me?"
                mike.say "Uh...yeah...I guess so."
                $ audrey.love -= 5
                audrey.say "No condom...no fucking condom!"
                "We stare at each other, wide-eyed as the reality of what we've just done hits home."
            elif _return == "vaginal_inside_happy":
                "Remembering that I'm not wearing a condom, I make to pull out before it's too late."
                "But then I realise that Audrey's clinging onto me for dear life."
                mike.say "What the actual fuck..."
                audrey.say "No, [hero.name]..."
                audrey.say "Cum in me..."
                audrey.say "Please!"
                show audrey missionary cum with hpunch
                #$ audrey.impregnate()
                play sexsfx1 cum_inside
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "A moment later, she gets her wish."
                $ audrey.love += 5
                "And the look of happiness on her face is one of pure bliss."
    stop sexsfx1 fadeout 1
    stop sound fadeout 1
    return

label audrey_fuck_date_spoon(sexperience_min):
    "I nod quickly as she walks back over to me and kneels on the bed."
    audrey.say "Why do you still have so many clothes on? This is looking rather one-sided here."
    mike.say "Oh... right. Why don't you help me out of some of these?"
    "She smirks and comes closer."
    "She put her hands on my hips and then slowly slide her hands up my shirt until was lifting it up and over my head."
    "She looks over my abs and trails her finger down them."
    audrey.say "The gyms done you some good, babe."
    "The compliment makes me even more eager to get started again."
    "I grab her again and push her back down on the bed."
    "I start nibbling her ear again as she feels for my zipper to undo my pants."
    "As soon as she has succeeded on getting them undone I help her slip them down and off my legs."
    menu:
        "Grind on her":
            "I grind against her slowly at first and then rougher as the kissing gets hotter."
        "Don't Grind":
            "I continue the kiss but don't do anything else yet because I am unsure of myself again."
            audrey.say "Do something already!"
    "She bucks her hips up into mine and whispers..."
    audrey.say "What are you waiting for, fuck me you idiot."
    "I look her in the eyes and she seems to be daring me to do it as she lets her legs fall open slowly to either side."
    call check_condom_usage (audrey, 180) from _call_check_condom_usage_13
    if _return == False:
        return "leave_without_gain"
    hide audrey
    if CONDOM:
        show audrey spoon condom
    show audrey spoon limp with fade
    "I push her on the bed and slide behind her, my hand caressing her tits."
    show audrey spoon vaginal
    play sexsfx1 slide_in
    play sound audrey_generic_oh_2
    "I shove in all the way without warning and she lets out a scream."
    play sexsfx1 fuck_calm
    play sound audrey_moans_happy_low loop
    "Finally I thought, I'm what is making her scream."
    "Just like I wanted to on the rollercoaster."
    "I pull out and push back in more gently, realizing how tight she is and trying to find a pace that won't make me lose it embarrassingly fast."
    play sexsfx1 fuck_moderate
    "In this position I am able to hit deeper and thrust hard, her hand started rubbing her clit."
    "I can't help myself though and a few times I buck my hips up wanting to help make friction between us."
    "Suddenly a thought comes to me..."
    show audrey spoon choke
    play sexsfx1 fuck_speed
    play sound audrey_moans_happy_medium loop
    "My hand goes up from her right tit to her neck and I start choking her."
    "Her breathing starts getting heavier and her moaning stronger as I shut down her air pipe."
    "When I release my grip a little she manages to let her voice out."
    audrey.say "More, please be rougher, be brutal..."
    play sexsfx1 fuck_sprint
    play sound audrey_moans_happy_high loop
    "After that my hand goes back to her neck preventing her from talking and I start slamming myself in her pussy harder."
    "It isn't long and I feel a pressure building up inside me."
    "We both start panting hard and I can't seem to make my thrusts fast enough."
    "Just when I think I am about to cum I turn her back around so I can see her face when she does."
    "I wait as long as I can, and the moment she cries out in bliss and I feel her walls tighten around me it was all I could take."
    call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_27
    if _return == "vaginal_outside":
        play sexsfx1 pull_out
        play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
        if not CONDOM:
            show audrey spoon hard cumshot ahegao with hpunch
        else:
            show audrey spoon hard ahegao -condom condomcum with hpunch
        if not CONDOM:
            audrey.say "Yes, mark me, I am yours... [hero.name]!"
            show audrey spoon limp -cumshot cumbody
        $ audrey.sub += 1
    elif _return == "vaginal_condom":
        play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
        show audrey spoon ahegao with hpunch
        audrey.say "Yes, That's soooo good... [hero.name]!"
        $ audrey.love += 2
    else:
        if persistent.xray:
            show audrey spoon xray xraycream ahegao
        else:
            show audrey spoon creampie ahegao
        audrey.say "Yes, fill me up, I am yours... [hero.name]!"
        #$ audrey.impregnate()
        play sexsfx1 cum_inside
        with hpunch
        play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
        $ audrey.love += 5
    if audrey.lesbian > MIN_LES_GIRL_SEX:
        $ audrey.lesbian -= 1
    with hpunch
    "I pant to catch my breath."
    mike.say "I think that was the most powerful orgasm I have ever had."
    audrey.say "Me... too. Me too."
    hide audrey
    return

label audrey_fuck_date_doggy(sexperience_min):
    "Audrey wastes no time in pushing me backwards and down onto it."
    "Before I can gather myself from the fall onto the mattress, she pounces on me."
    "I can feel her fingers as they close around the shaft of my cock."
    "Then she's angling hastily it towards the lips of her waiting pussy."
    "Another time I might have been content to just sit back and let Audrey have her way."
    "But right now, my blood's up and I want to play the same game that she does."
    "I take hold of Audrey's shoulders and twist her over so that she lands on her belly."
    "Taken by surprise, she tries to crawl out of reach."
    "But I'm on her before she can get more than a couple of inches."
    scene audrey doggy
    show audrey doggy bedroom
    play sound audrey_moans_breathing_slow loop
    with fade
    "I seize her hair in one hand, wrapping it firmly around my fingers."
    "The first time she feels this is when she tries to crawl away for a second time."
    "I do nothing more than holding on, and she provides all of the motion herself."
    "Audrey yelps in pain, but instantly stops her struggling."
    "Now that I have her under control, I pull on her hair to encourage Audrey onto her hands and knees."
    "She does as she's told without any hint of defiance, glancing over her shoulder as she does so."
    "In Audrey's eyes, I can see that same glimmer of excitement I know so well."
    "For her, discipline of this kind is a massive turn-on."
    "But I'm still getting used to it, trying to learn where the boundaries lie."
    "Though the look she's giving me is enough to know that I'm getting it right."
    "She wants it, and I want to give it to her."
    "The only question that remains is where she's going to get it..."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Still thinking about what to do next, I almost absently slap Audrey across the buttocks."
            "This makes her yelp for a second time, and shiver in anticipation so that her backside shakes."
            "It's then that I catch sight of her asshole, almost hidden between those rounded cheeks."
            "I don't know why, but I suddenly feel like it's winking at me, daring me to take it."
            "Before I can think better of it, I find myself leaning against Audrey's ass."
            "I part her buttocks, and then use my free hand to guide my cock towards the target."
            show audrey doggy inside
            play sexsfx1 slide_in
            play sound audrey_generic_oh_1
            "It's hard going at first, but Audrey offers no objections as I begin to push it into her."
            play sexsfx1 fuck_calm loop
            play sound audrey_moans_pained_low loop
            "Indeed, her yelps are soon replaced by a deep groaning as she accepts what's being done."
            "Soon enough I'm pushing her down onto the mattress with all of my weight."
            "The whole time that I'm thrusting my cock into her ass, Audrey looks back at me over her shoulder."
            "I watch in fascination as the normally defiant expression that she wears seems to melt away."
            "In it's place is a look of complete surrender, as if what I'm doing has left her helpless to resist."
            "By the time I'm as deep as I can go, Audrey's eyes are almost rolling back into her head."
            "And they close completely as I finally begin to thrust in and out of her."
            show audrey doggy pleasure
            play sexsfx1 fuck_moderate loop
            play sound audrey_moans_pained_medium loop
            audrey.say "Oh..."
            audrey.say "Oh shit..."
            audrey.say "Oh, [hero.name]..."
            audrey.say "I love it when you fuck my ass..."
            "Needless to say, Audrey's words are like music to my ears!"
            "I have no way of knowing if she really means what she's saying."
            "Maybe it's just pillow-talk to get me even more fired up than I already am."
            "But either way, it has the desired effect upon me."
            play sexsfx1 fuck_speed loop
            play sound audrey_moans_pained_high loop
            "Almost instantly, I begin pounding away on Audrey like never before."
            "Her words dissolve into more moans of pleasure."
            "And this time, her eyes really do roll back into her head."
            "But almost as loud as the sound of Audrey's moaning is that of my groin slapping her ass."
            "This isn't a pace I can keep up forever, and I can already feel myself cumming..."
            call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_28
            if _return == "anal_inside":
                "So the obvious thing to do is just double down on what I'm doing right now."
                "I keep right on thrusting as deep into Audrey as possible, rattling her with each motion."
                "Already I can feel her arms and legs beginning to shake, as if she's reaching the limits of her endurance."
                show audrey doggy ahegao with hpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_pained_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 1
                "Her moans have become gasps, almost perfectly timed to my own motions."
                with hpunch
                "And so when I finally lose myself inside of her ass and stop, she keeps on moving just the same."
                with hpunch
                "I watch as Audrey rides my cock, still going until her endurance gives out on her."
                "Then her head falls onto the bed, and she crumples into a sweaty heap atop the bedclothes."
            elif _return == "anal_outside":
                "I could just keep right on pounding Audrey's ass to the end."
                "But I feel like she needs something more to really top it all off."
                show audrey doggy -inside
                "And so I yank my cock out of her, just before I finally cum."
                play sexsfx1 pop_out
                play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.sub += 1
                show audrey doggy cum bodycum with hpunch
                "Audrey gasps and sucks in a sudden breath at the sensation."
                show audrey doggy ahegao with hpunch
                "Then she jumps in surprise as the warm, sticky cum spatters up her back."
                with hpunch
                "She seems to reach the end of her endurance then."
                "The last of the cum rains down on her as she crumples into a sweaty heap atop the bedclothes."
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            "Suddenly, my thoughts return to the way that Audrey tried to steer my cock into her pussy."
            call check_condom_usage (audrey, 180) from _call_check_condom_usage_145
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show audrey doggy condom
            "Making sure that my cock is at just the right angle, I give a gentle but firm tug on her hair."
            "I hear Audrey make a sharp gasp, and then hurry to shuffle backwards in order to loosen my grip."
            "She only stops when her path inevitably leads to the head of my cock jabbing her in the ass."
            "But another tug seems to be all it takes to let Audrey know what's expected of her next."
            "Obediently, she raises her ass and wiggles backwards."
            play sound audrey_moans_breathing_slow
            "The motion spreads her buttocks and begins to work my cock between them."
            "Audrey sighs audibly as the head rubs at the lips of her pussy, already threatening to slip inside."
            show audrey doggy inside
            play sexsfx1 slide_in
            play sound audrey_generic_oh_1
            "Only when I'm sure that it's in just the right spot do I reach out and grab her."
            show audrey doggy pleasure
            play sexsfx1 fuck_calm
            play sound audrey_moans_happy_low loop
            "Audrey lets out a yelp of surprise as I pull her straight onto my cock."
            "She's more than ready for what I have to give, the anticipation making sure of it."
            "And so I push into her without more than a second of resistance."
            "Audrey collapses onto the mattress, trapped beneath my weight."
            stop sound
            audrey.say "Oh..."
            audrey.say "Oh fuck..."
            audrey.say "Oh, [hero.name]..."
            audrey.say "Please, fuck me real hard..."
            play sexsfx1 fuck_moderate
            play sound audrey_moans_happy_medium loop
            "As if I needed any more encouragement, Audrey's words still serve to urge me on."
            "She could be completely sincere in what she's saying."
            "Or it could be her way of making sure that I give her all that I have."
            play sexsfx1 fuck_speed
            play sound audrey_moans_happy_high loop
            "Whatever the truth of it might be, I instantly feel the urge to give her just what she's asking for."
            "Without even bothering to build up from a gentle start, I begin to pound Audrey mercilessly."
            "The grip that I still have on her hair shortens these thrusts, making them all the more intense."
            play sfx1 spank
            with hpunch
            play sound audrey_generic_oh_3
            "And with my free hand, I can't seem to help slapping her buttocks at random."
            play sfx1 [spank, spank]
            play sound audrey_generic_oh_4
            "Audrey bucks and twitches under this combination of fucking and spanking."
            play sfx1 spank
            play sound audrey_generic_oh_4
            "But not once does she try to wriggle her way free or plead for me to stop."
            "All I can think about is keeping up this same, breakneck pace."
            "And yet I can already feel that I'm getting close to losing it..."
            call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_29
            if _return == "vaginal_condom":
                "But thanks to the fact that I took precautions before we got this far, that's not something I have to worry about."
                "Instead I'm able to keep right on thrusting in and out of Audrey until the moment that I cum."
                "Only then do I finally stop spanking her and take a firm hold of her haunches as I do so."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 1
                "Pushing my cock as deep into her as it can go, I savour every second of the sensation."
                "Something that's only made all the more enjoyable by the way in which Audrey moans the whole time."
                "And then, exhausted and slick with sweat, her head falls onto the bed."
            elif _return == "vaginal_outside" and not audrey.flags.pill:
                "As much as I'm getting to like the kink Audrey has for being punished, cumming in her like this doesn't fit the bill."
                "Getting her pregnant would be more like a life sentence for the both of us!"
                show audrey doggy -inside
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "And so that's why I pull out of her the moment before I actually cum."
                $ audrey.sub += 1
                show audrey doggy ahegao
                "Audrey gasps and pants in desperate surprise as she feels me do so."
                show audrey doggy cum bodycum with hpunch
                "But then she shivers and cries out as the cum spatters over her back."
                with hpunch
                "The last of the cum rains down on her as she lays in a sweaty heap atop the bedclothes."
            elif _return == "vaginal_outside" and audrey.flags.pill:
                "Audrey's kinky side always gets me hot, and I honestly always feel like she drags me along with her schemes."
                "With a small grin on my face, I enjoy knowing that I'll be pulling one on her this time."
                show audrey doggy -inside
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "And so that's why I pull out of her the moment before I actually cum."
                $ audrey.sub += 1
                show audrey doggy ahegao
                "Audrey gasps and pants in desperate surprise as she feels me do so."
                show audrey doggy cum bodycum with hpunch
                "But then she shivers and cries out as the cum spatters over her back."
                with hpunch
                "The last of the cum rains down on her as she lays in a sweaty heap atop the bedclothes."
            elif _return == "vaginal_inside_pill":
                stop sound
                audrey.say "Ah...ah..."
                audrey.say "Pill, [hero.name]..."
                audrey.say "Don't...stop...now!"
                "I take Audrey's words as permission for what I do next, pushing into her as far as possible."
                show audrey doggy ahegao with hpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "A second later I feel myself cumming as deep inside of her pussy as I can manage."
                $ audrey.love += 2
                with hpunch
                "Audrey lets out a final moan of pleasure, and then I feel her legs and arms begin to tremble."
                with hpunch
                "I let go of her, my cock slides out, leaving her helpless on the bed in a state of utter exhaustion."
            elif _return == "vaginal_inside_pregnant":
                "There's no danger of cumming inside of Audrey, not when she's already pregnant."
                "In fact, I'm pretty sure that her belly's all that's holding her up right now!"
                show audrey doggy ahegao with hpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "Thrusting deep into her, I savour every last second before I finally cum."
                $ audrey.love += 3
                with hpunch
                "And Audrey moans beneath me, letting me know that she's more than satisfied too."
                "Afterwards, she rolls onto her side, arms hugging her ever-growing belly in a protective gesture."
            elif _return == "vaginal_inside_mad":
                stop sound
                audrey.say "Wait..."
                audrey.say "Don't you..."
                #$ audrey.impregnate()
                play sexsfx1 cum_inside
                with hpunch
                "But it's already too late, as I feel myself cumming inside of Audrey."
                with hpunch
                "She looks back over her shoulder at me, an unfamiliar look of fear on her face."
                audrey.say "[hero.name]..."
                audrey.say "You came in me!"
                $ audrey.love -= 5
                audrey.say "H...how...how could you?!?"
            elif _return == "vaginal_inside_happy":
                "I know that I've only got a couple of seconds to pull out of Audrey."
                "But the moment that I make a move to do so, she grabs hold of me with an iron grip."
                stop sound
                audrey.say "No, [hero.name]..."
                audrey.say "Don't do it!"
                play sexsfx1 final_thrust
                play sound audrey_moans_happy_orgasm_1
                $ audrey.love += 5
                show audrey doggy ahegao with hpunch
                #$ audrey.impregnate()
                "She takes me by complete surprise, and I lose myself inside of her a moment later."
                with hpunch
                "Audrey rides my cock until the very last, gasping in delight as she does so."
                audrey.say "Oh, yes..."
                audrey.say "Fuck, yes..."
                audrey.say "I've been so bad [hero.name]..."
                audrey.say "Give me what I deserve..."
    return

label audrey_fuck_date_cowgirl(sexperience_min):
    audrey.say "Whoa..."
    audrey.say "What the..."
    "Before she can say another word, I have a hold of Audrey's hands."
    "And then I'm dragging her down onto the bed."
    "She lets out a yelp of surprise as she falls atop me."
    scene
    show audrey cowgirl bedroom
    with fade
    mike.say "What's the matter, Audrey?"
    mike.say "I thought you wanted me to put the work in?"
    "Audrey pops up, throwing her hair back as she regains her balance."
    "She looks shaken-up and more than a little flustered."
    "But all the same I can see that she's not going to cry foul."
    "And after all, how can she?"
    "Wasn't she the one that goaded me into taking action just now?"
    "Audrey looks down at me with a look in her eyes that can only be a challenge."
    "It's a look that I know all too well, one I've seen her wearing before."
    "It's the look that means it's time for me to make good on my promises."
    "And so I take a firm hold of Audrey's haunches and pull her downwards..."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Audrey's head sways and falls backwards as I move her."
            "She throws her arms back, putting her palms flat on the mattress to support herself."
            "Which means that she's good and distracted when I take aim with my cock!"
            audrey.say "What the..."
            audrey.say "Hey, that's my..."
            show audrey cowgirl anal
            play sexsfx1 slide_in
            audrey.say "My...oh...oh god!"
            "But any kind of protest is far too late."
            "And that's because my cock is already sinking into her ass."
            show audrey cowgirl pleasure
            play sexsfx1 fuck_calm loop
            play sound audrey_moans_pained_low loop
            "In mere seconds, Audrey goes from shock to submission."
            "I can feel the way that she gives in from the change in the tone of her voice."
            "But even better is the sensation of her muscles putting up a fight at first."
            "And then there's the almost indescribable feeling of them giving way."
            play sexsfx1 fuck_moderate loop
            play sound audrey_moans_pained_medium loop
            "Before she truly knows what's happening to her, I have Audrey right where I want her."
            "It feels good to be doing this, taking the lead and being the one in control."
            "And it's not like I have to worry about feeling guilty either."
            "As I just remind myself of how much Audrey likes to tease me."
            "I'm not doing anything to her other than the exact thing that she wants."
            "It just so happens that I want it too, almost as badly as she does!"
            show audrey cowgirl speed
            play sexsfx1 fuck_speed loop
            play sound audrey_moans_pained_high loop
            "Audrey picks up speed as she rides my cock."
            "She bounces up and down as she straddles my lap."
            "And all I can hear is the sound of her thighs slapping against mine."
            "Well, that and the desperate panting of her breathing too!"
            "Any chance of Audrey speaking is long since past."
            "Now all she seems capable of doing is holding on for dear life."
            "And I don't think that she'll have to hold on for much longer."
            "Going at Audrey so hard might have felt really good."
            "But it means I'm ready to shoot my load before I know it!"
            call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_30
            if _return == "anal_inside":
                "If I thought Audrey moaned before now, she's all but crying out now."
                $ audrey.love += 1
                play sexsfx1 final_thrust
                play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                show audrey cowgirl creampie with vpunch
                "I cum when she presses down on me, meaning I'm as deep as I can go."
                with vpunch
                "For a moment I have the crazy thought that she's not going to stop."
                with vpunch
                "That she's just going to keep on riding me until she snaps it off!"
                show audrey cowgirl ahegao -speed
                "But then I feel a slackening in all of her muscles."
                "And she slides off of me like a puppet with broken strings."
                "I'm so utterly spent myself that it's all I can do to keep her from tumbling off the bed!"
            elif _return == "anal_outside":
                show sexinserts chest audrey zorder 1
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "Using the very last of my strength, I lift Audrey as high as I can manage."
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                show audrey cowgirl -anal
                "She's pressing down on me for all she's worth, and her skin is slick with sweat."
                "Yet somehow I find the will to yank my cock out of her ass before I cum."
                "Audrey wriggles and squirms in my grasp, trying as best she can to get back on it."
                show audrey cowgirl cumshot with vpunch
                $ audrey.sub += 1
                "But it's too late for that now, and all she manages to do is line herself up perfectly."
                show audrey cowgirl dickcum
                show sexinserts chest audrey cum zorder 1
                with vpunch
                "Which means that when I shoot my load, it hits Audrey square in the chest."
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                show audrey cowgirl onbody
                with vpunch
                "All that I have to give is spread over her breasts and belly in sticky, white lines."
                show audrey cowgirl -cumshot
                "And as she watches it happen, Audrey almost slides off of me and the bed too!"
                hide sexinserts
                hide bellycum
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            "My cock slides against the lips of Audrey's pussy."
            "And I hear her gasp at the sensation, unable to hide her delight."
            "But now a smile spreads across my own face."
            "As I have a chance to turn the tables on Audrey and torment her!"
            call check_condom_usage (audrey, 180) from _call_check_condom_usage_170
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show audrey cowgirl condom
            "All it takes is a slight pull on Audrey's thighs."
            "And then I feel the head of my cock slide into her."
            "For all of her teasing and tempting, she's as slick as she can be."
            show audrey cowgirl vaginal
            play sexsfx1 slide_in
            play sound audrey_generic_oh_1
            "This means that there's little resistance as I push myself into her."
            "And the desire she has for it also shows in how she moans as I do so."
            audrey.say "Mmm..."
            audrey.say "Oh, [hero.name]..."
            audrey.say "That's it...right there!"
            show audrey cowgirl pleasure
            play sexsfx1 fuck_calm loop
            play sound audrey_moans_happy_low loop
            "I let Audrey sink down and onto my cock as slowly as I can."
            "Every moment that she's taking me into her feels better than the last."
            "And when she's finally straddling my lap, she doesn't sit still either."
            "Stretching her arms out behind her for support, Audrey begins to move."
            "She writhes and wriggles atop me, grinding herself on my cock."
            "And only when she's made me gasp out loud does she start to ride me."
            show audrey cowgirl speed
            play sexsfx1 fuck_moderate loop
            play sound audrey_moans_happy_high loop
            "Audrey pants too, her face flushing red as she bobs up and down."
            "I can't tell if the colour in her cheeks is from the effort she's putting into it."
            "Or else the thrill that she's feeling is the reason that she's the colour of a tomato."
            "Either way, she's picking up more speed with every moment that passes."
            "Soon enough the sound of her thighs slapping against mine is all I can hear."
            "It drowns out both of our groans, no matter how loud they become."
            "And it easily overcomes the noises that my tortured bed is making too."
            "At this rate I'm actually getting worried that we might break it!"
            "But that still doesn't mean I'm happy to feel myself about to cum..."
            call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_31
            if _return == "vaginal_condom":
                "In fact, all I have to worry about is keeping right on going until the very end."
                $ audrey.love += 1
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                with vpunch
                "And when I finally shoot my load into Audrey, it's safe in the knowledge that we took precautions."
                with vpunch
                "This means that I can enjoy every last moment of the feeling as she rides my cock."
                with vpunch
                "Audrey clings onto it to the last, squeezing every last drop out of me."
                "And then she slides off, collapsing onto the bed at my side."
            elif _return == "vaginal_outside":
                show sexinserts chest audrey zorder 1
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "With all the strength I have left, I pull myself out of Audrey."
                "She feels the way I'm moving and tries as best she can to stop me."
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                show audrey cowgirl -vaginal
                "But despite this, I manage to free myself before I cum."
                "Audrey wriggles and squirms, trying to get back on it."
                "But it's too late, and all she manages to do is get herself into the perfect position."
                show audrey cowgirl cumshot
                show sexinserts chest audrey cum zorder 1
                with vpunch
                "When I shoot my load, it hits Audrey square in the chest."
                $ audrey.sub += 1
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                show audrey cowgirl dickcum onbody
                with vpunch
                "It spreads over her breasts and belly in sticky, white lines."
                show audrey cowgirl -cumshot
                "As she watches, Audrey almost slides off of me and the bed too!"
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_inside_pill":
                stop sound
                audrey.say "Keep going..."
                audrey.say "On...the...pill!"
                "I push as deep into Audrey as I can, grateful for her permission."
                show audrey cowgirl ahegao with vpunch
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "Everything that I have explodes out of me a moment later."
                $ audrey.love += 2
                with vpunch
                "Audrey moans as she writhes atop me, feeling the whole thing."
                show audrey cowgirl -vaginal
                show pussy_insert audrey cum zorder 1 at zoomAt(0.75, (40, 200))
                with vpunch
                "And then she slides off, collapsing onto the bed at my side."
            elif _return == "vaginal_inside_pregnant":
                "Audrey holds her belly in a protective gesture the as I begin to cum."
                $ audrey.love += 3
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                show audrey cowgirl ahegao creampie with vpunch
                "She moans and wriggles atop me, taking everything that I have to give."
                with vpunch
                "But the whole time she cradles her belly to make sure that it's safe."
                show audrey cowgirl -vaginal
                show pussy_insert audrey cum zorder 1 at zoomAt(0.75, (40, 200))
                with vpunch
                "And then she slides off, collapsing onto the bed at my side."
            elif _return == "vaginal_inside_mad":
                play sound audrey_generic_oh_1
                pause 0.5
                audrey.say "No..."
                audrey.say "Don't..."
                "I only realise the mistake I've made as Audrey tries to clamber off of me."
                show audrey cowgirl creampie with vpunch
                play sexsfx1 cum_inside
                #$ audrey.impregnate()
                "But it's too late, and a second later I cum deep inside of her."
                $ audrey.love -= 5
                with vpunch
                "She fixes me with a horrified stare as it happens."
                "Which is somehow worse than having her screaming in my face."
            elif _return == "vaginal_inside_happy":
                stop sound
                audrey.say "Don't stop now..."
                audrey.say "I want to feel you cum in me!"
                mike.say "Wait..."
                mike.say "We didn't use a..."
                play sexsfx1 final_thrust
                show audrey cowgirl creampie ahegao with vpunch
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                #$ audrey.impregnate()
                "But it's too late, as I'm already shooting my load inside of Audrey."
                "I fix her with a horrified look as I do so, expecting to see her doing the same."
                $ audrey.love += 5
                "And yet she seems to be smiling, as if she's pleased with what's happening!"
    return

label audrey_fuck_date_reverse_cowgirl(sexperience_min):
    "As she crawls onto the mattress, I reach out for her."
    with vpunch
    "But Audrey slaps my hands away, still laughing."
    mike.say "Hey!"
    mike.say "What the hell, Audrey?"
    audrey.say "Hands off until I say so, [hero.name]!"
    show audrey mock
    audrey.say "Until then, I'm the only one that gets to touch!"
    "I frown at Audrey's demands, but I can see the look in her eyes."
    "They're full of the usual mischief she deals in."
    "So I hold up my hands and lie back on the bed."
    "If she has something in mind, then it's best to let her have her way."
    "Because the rewards for indulging her are almost always well worth it."
    "Audrey nods and then clambers onto me, straddling my thighs."
    "But once she settles down, she has her back to me."
    scene audrey reverse cowgirl
    show audrey reverse cowgirl naked
    with fade
    mike.say "Hey, Audrey!"
    mike.say "All I can see is the back of your head!"
    "Audrey looks back over her shoulder at me, shaking her head."
    audrey.say "Look, [hero.name]..."
    audrey.say "I know what I'm doing."
    audrey.say "So just shut the Hell up, okay?"
    "Audrey doesn't wait for an answer."
    "Instead she turns her gaze back to the front."
    "And then she leaps into action."
    "Instantly I feel her take a firm hold of my cock, squeezing it playfully."
    "It was already getting hard, but that process now speeds up as Audrey plays with me."
    "And I gasp at the sensation, loving the mixture of pain and pleasure it causes."
    audrey.say "You like that, huh?"
    mike.say "Ah..."
    mike.say "Y...yeah, Audrey!"
    mike.say "I love it!"
    audrey.say "You want some more, right?"
    mike.say "Please, Audrey..."
    mike.say "Yeah...I want more!"
    "This time Audrey's laugh is equal parts filthy and wicked."
    "And she wastes no time in going to work on my cock."
    "Audrey rubs her hand up and down the shaft, stroking it hard."
    "But she also rubs it against her belly and between her thighs."
    "This means that I can also feel how warm her skin is against it."
    "That and the way she's getting wetter all the time down there!"
    audrey.say "Now that feels like it's good and hard."
    audrey.say "Let's see what we can do with it..."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I feel Audrey inching forwards, sliding her pussy towards my cock."
            "Which lets me know that she's thinking this is going to be pretty straight up."
            "And I can't help smiling as I think of what I have in mind instead."
            "Let's just say that Audrey's not the only one that can be mischievous."
            "Audrey takes a firm hold of my cock and raises herself up on her haunches."
            audrey.say "Mmm..."
            audrey.say "This is going to be fun!"
            "She lowers herself down a little."
            "Just enough for the head of my cock to brush against her pussy."
            "I can't help shivering a little at the sensation, it feels so good."
            "Audrey tries to laugh at my reaction, like she's the one teasing me."
            "But I can feel the way that her body shuddered at the same time."
            "And so I know that she's feeling just as excited as I am right now."
            "So I don't have any hesitation in putting my hands on Audrey's waist."
            "And then pulling her down, but at a slightly different angle to the one she expects."
            audrey.say "Hey!"
            audrey.say "Don't be so impatient!"
            audrey.say "You're going to get pussy..."
            audrey.say "You just have to..."
            show audrey reverse cowgirl anal
            play sexsfx1 slide_in
            audrey.say "OH FUCK..."
            show audrey reverse cowgirl audreyahegao
            "The tone of Audrey's voice changes dramatically as I pull her downwards."
            "In no time at all she goes from sounding like she's in control to completely helpless and in my power."
            "Where before she was speaking in coherent sentences, now all she can manage are moans and gasps of pleasure."
            "Audrey has her eyes squeezed tightly closed as she sinks down onto my cock."
            "She just wasn't expecting it to be pushing it's way into her ass!"
            "But I can see that she's nodding the whole time, silently urging me on without words."
            "The deeper I get into Audrey, the more she seems to lose control of her body."
            show audrey reverse cowgirl audreypleasure
            play sexsfx1 fuck_calm
            play sound audrey_moans_pained_low loop
            "Where before her limbs were supporting her, now they're becoming limp and lifeless."
            "She slumps back against me as her muscles surrender, needing me to hold her up."
            "I'm enjoying the change in the dynamic almost as much as the sensation of fucking Audrey."
            "Almost, but not quite - nothing feels as good as being this deep inside of her!"
            "But I am loving the way that she's being overwhelmed by what I'm doing to her."
            "All Audrey seems capable of doing is pressing herself against me."
            "That and clinging onto me as I thrust upwards and into her."
            "Maybe it's because she's such a mischievous bitch most of the time."
            "One of those girls that loves to push your buttons and cause chaos."
            "That once you've managed to get her helplessly addicted to you, it feels so damn good!"
            "Audrey's almost melting in my arms right now, hopelessly lost in her own pleasure."
            "Her head sways on my shoulder."
            "Her breasts bounce up and down."
            "Her breath comes in ragged gasps."
            "In fact, I'm not sure she's kept the power of speech."
            "That is until she begins to gasp and shake her head."
            stop sound
            audrey.say "I..."
            audrey.say "I'm gonna..."
            audrey.say "Cum...I'm gonna cum!"
            show audrey reverse cowgirl audreyahegao
            play sound audrey_moans_pained_high loop
            "Audrey's true to her word, beginning to twitch and twist in my arms."
            "I hold onto her tighter than ever as the orgasm takes hold."
            "She's clinging onto me as if for dear life."
            "Her nails digging into my skin, almost drawing blood."
            "And her ass is clenching tightly too, squeezing my cock!"
            "Looks like she's going to take me along with her..."
            call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_32
            if _return == "anal_inside":
                "I silently smile and feel smug that I chose to fuck Audrey up the ass."
                "Because it means that I can just relax and enjoy what happens next."
                show audrey reverse cowgirl creampie with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 1
                with vpunch
                "And that's the sensation of shooting my load into Audrey."
                with vpunch
                "I'm shaking, loving every moment of the feeling."
                with vpunch
                "And it seems to renew what she's feeling too."
                "Even after I'm done cumming, Audrey doesn't regain her senses."
                "Instead she remains clutched in my arms, almost insensible."
            elif _return == "anal_outside":
                show sexinserts belly audrey zorder 2 at center, zoomAt(1, (740, 970))
                "I make a concerted effort to pull my cock out of Audrey before it's too late."
                play sexsfx1 pop_out
                pause 0.5
                show audrey reverse cowgirl out
                play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "She wails in what might be a protest or simply a reaction to the sensation."
                "But there's nothing she can do to stop me, and I keep right on going."
                "I'm shaking, loving every moment of the feeling."
                show sexinserts belly audrey cum zorder 2 at center, zoomAt(1, (740, 970))
                show audrey reverse cowgirl cumshot
                with vpunch
                $ audrey.sub += 1
                "Shooting my load over Audrey's belly."
                with vpunch
                "And it seems to renew what she's feeling too."
                "Even after I'm done cumming, Audrey doesn't regain her senses."
                "Instead she remains clutched in my arms, almost insensible."
                "Squirming as she rubs my own cum into my lap."
                hide sexinserts
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (audrey, 180) from _call_check_condom_usage_14
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show audrey reverse cowgirl condom
            "Audrey takes a firm hold of my cock and raises herself up on her haunches."
            audrey.say "Mmm..."
            audrey.say "This is going to be fun!"
            "She lowers herself down a little."
            "Just enough for the head of my cock to brush against her pussy."
            "I can't help shivering a little at the sensation, it feels so good."
            "Audrey tries to laugh at my reaction, like she's the one teasing me."
            "But I can feel the way that her body shuddered at the same time."
            "And so I know that she's feeling just as excited as I am right now."
            "So I don't have any hesitation in putting my hands on Audrey's waist."
            "And then pulling her down, gently but firmly onto my cock."
            audrey.say "Hey!"
            audrey.say "Don't be so impatient!"
            audrey.say "You're going to get pussy..."
            audrey.say "You just have to..."
            show audrey reverse cowgirl vaginal
            play sexsfx1 slide_in
            audrey.say "OH FUCK..."
            show audrey reverse cowgirl audreyahegao
            "The tone of Audrey's voice changes dramatically as I pull her downwards."
            "In no time at all she goes from sounding like she's in control to completely helpless and in my power."
            "Where before she was speaking in coherent sentences, now all she can manage are moans and gasps of pleasure."
            "Audrey has her eyes squeezed tightly closed as she sinks down onto my cock."
            "But I can see that she's nodding the whole time, silently urging me on without words."
            "The deeper I get into Audrey, the more she seems to lose control of her body."
            show audrey reverse cowgirl audreypleasure
            play sexsfx1 fuck_calm
            play sound audrey_moans_happy_low loop
            "Where before her limbs were supporting her, now they're becoming limp and lifeless."
            "She slumps back against me as her muscles surrender, needing me to hold her up."
            "I'm enjoying the change in the dynamic almost as much as the sensation of fucking Audrey."
            "Almost, but not quite - nothing feels as good as being this deep inside of her!"
            "But I am loving the way that she's being overwhelmed by what I'm doing to her."
            "All Audrey seems capable of doing is pressing herself against me."
            "That and clinging onto me as I thrust upwards and into her."
            "Maybe it's because she's such a mischievous bitch most of the time."
            "One of those girls that loves to push your buttons and cause chaos."
            "That once you've managed to get her helplessly addicted to you, it feels so damn good!"
            "Audrey's almost melting in my arms right now, hopelessly lost in her own pleasure."
            "Her head sways on my shoulder."
            "Her breasts bounce up and down."
            "Her breath comes in ragged gasps."
            "In fact, I'm not sure she's kept the power of speech."
            "That is until she begins to gasp and shake her head."
            audrey.say "I..."
            audrey.say "I'm gonna..."
            audrey.say "Cum...I'm gonna cum!"
            show audrey reverse cowgirl audreyahegao
            play sound audrey_moans_happy_high loop
            "Audrey's true to her word, beginning to twitch and twist in my arms."
            "I hold onto her tighter than ever as the orgasm takes hold."
            "She's clinging onto me as if for dear life."
            "Her nails digging into my skin, almost drawing blood."
            "And her pussy is clenching tightly too, squeezing my cock!"
            "Looks like she's going to take me along with her..."
            call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_33
            if _return == "vaginal_condom":
                "I silently smile and feel smug that we remembered to use a condom."
                "Because it means that I can just relax and enjoy what happens next."
                show audrey reverse cowgirl out cumshot
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 1
                with vpunch
                "And that's the sensation of shooting my load into Audrey."
                with vpunch
                "I'm shaking, loving every moment of the feeling."
                with vpunch
                "And it seems to renew what she's feeling too."
                "Even after I'm done cumming, Audrey doesn't regain her senses."
                "Instead she remains clutched in my arms, almost insensible."
            elif _return == "vaginal_outside":
                show sexinserts belly audrey zorder 2 at center, zoomAt(1, (740, 970))
                "I make a concerted effort to pull my cock out of Audrey before it's too late."
                play sexsfx1 pull_out
                pause 0.5
                show audrey reverse cowgirl out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "She wails in what might be a protest or simply a reaction to the sensation."
                "But there's nothing she can do to stop me, and I keep right on going."
                "I'm shaking, loving every moment of the feeling."
                show audrey reverse cowgirl cumshot
                show sexinserts belly audrey cum zorder 2 at center, zoomAt(1, (740, 970))
                with vpunch
                $ audrey.sub += 1
                "Shooting my load over Audrey's belly."
                with vpunch
                "And it seems to renew what she's feeling too."
                with vpunch
                "Even after I'm done cumming, Audrey doesn't regain her senses."
                "Instead she remains clutched in my arms, almost insensible."
                "Squirming as she rubs my own cum into my lap."
                hide sexinserts
            elif _return == "vaginal_inside_pill":
                "I silently smile and feel smug that Audrey's on the pill."
                "It means that we didn't need to bother with a condom."
                "And it also means that I can just relax and enjoy what happens next."
                with vpunch
                "And that's the sensation of shooting my load into Audrey."
                show audrey reverse cowgirl creampie with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 2
                "I'm shaking, loving every moment of the feeling."
                with vpunch
                "And it seems to renew what she's feeling too."
                with vpunch
                "Even after I'm done cumming, Audrey doesn't regain her senses."
                "Instead she remains clutched in my arms, almost insensible."
            elif _return == "vaginal_inside_pregnant":
                "I silently smile and feel smug that Audrey's pregnant."
                "It means that we didn't need to bother with a condom."
                "And it also means that I can just relax and enjoy what happens next."
                with vpunch
                "And that's the sensation of shooting my load into Audrey."
                show audrey reverse cowgirl creampie with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 3
                "I'm shaking, loving every moment of the feeling."
                with vpunch
                "And it seems to renew what she's feeling too."
                with vpunch
                "Even after I'm done cumming, Audrey doesn't regain her senses."
                "Instead she remains clutched in my arms, almost insensible."
            elif _return == "vaginal_inside_mad":
                "At the last moment I remember that I need to pull out."
                "We didn't use a condom and I can't cum inside of Audrey."
                stop sound
                audrey.say "Mmm..."
                audrey.say "Oh shit..."
                audrey.say "Don't cum in me!"
                "Suddenly Audrey seems to shake off the haze she's been under."
                "Before I can do anything, I realise it's too late!"
                "There's no way I can pull out of her in time."
                with vpunch
                "I shoot my load deep into Audrey, helpless to stop myself."
                show audrey reverse cowgirl creampie with vpunch
                play sexsfx1 cum_inside
                with vpunch
                #$ audrey.impregnate()
                "Audrey desperately tries to clamber off me, but it's no good."
                $ audrey.love -= 5
                "What on earth did I just do?"
                "And what are the consequences going to be for us both?"
            elif _return == "vaginal_inside_happy":
                "At the last moment I remember that I need to pull out."
                "We didn't use a condom and I can't cum inside of Audrey."
                audrey.say "Mmm..."
                audrey.say "No you don't!"
                "Suddenly Audrey seems to shake off the haze she's been under."
                "Before I can do anything, she's clinging to me like a limpet!"
                "There's no way I can pull out of her in time."
                with vpunch
                "I shoot my load deep into Audrey, helpless to stop myself."
                show audrey reverse cowgirl creampie with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                #$ audrey.impregnate()
                with vpunch
                "But she seems delighted, grinding herself on me the whole time."
                $ audrey.love += 5
                "What on earth did she just do?"
                "And what are the consequences going to be for us both?"
    return

label audrey_fuck_date_stand(sexperience_min):
    "She walks past me slowly, making sure to hold my eye the whole time."
    show audrey standing bedroom with fade
    "And when she finally reaches the wall, she stops and leans a hand against it."
    "Then she pushes her ass backwards, stretching her legs out too."
    "Audrey looks back over her shoulder at me while she does all of this."
    "And there's no need for her to say as much as a single word."
    "Because I can read the signals she's sending out easier than I could any book!"
    "Hopping as I pull off the very last of my clothes, I hurry over to her."
    "Audrey's eyes drift downwards as she notices what's happening to my body."
    "I don't need to look down there, as I can already feel my cock getting hard."
    "In fact, it's swinging from side to side as I close the space between us!"
    "And when Audrey looks up again, I can see desire and excitement in her eyes."
    "Which, of course, only serves to increase the same emotions in me too."
    audrey.say "What are you waiting for?"
    audrey.say "Get over here and fuck me already!"
    mike.say "I...I'm coming, Audrey!"
    mike.say "Don't worry, I'm cumming!"
    audrey.say "Not for a while yet, I hope?"
    "For a moment Audrey's question throws me."
    "My head's so full of desire for her that I can't think straight."
    "But then I somehow manage to work it through my lust-addled brain."
    "And I shake my head, laughing at her little joke."
    mike.say "No, Audrey..."
    mike.say "No danger of that happening!"
    "Audrey snorts with laughter."
    "But at the same time she thrusts her ass out even further."
    "And I don't need to be told what she means this time either!"
    show audrey standing pleasure
    "I reach out and grab hold of Audrey at the waist."
    "Then I lean in closer, letting her feel my cock against her ass."
    audrey.say "Oh, hello!"
    audrey.say "Where are you going to put that thing?"
    show audrey standing normal
    audrey.say "I wonder..."
    menu:
        "Fuck her pussy":
            "I pull Audrey closer still."
            "Already thinking about how it's going to feel to be inside of her."
            call check_condom_usage (audrey, 180) from _call_check_condom_usage_15
            if _return == False:
                return "leave_without_gain"
            "And I guess that me being inside of her is all that's on Audrey's mind too."
            "As she wastes no time in grabbing hold of my cock and thrusting it between her thighs."
            "But as she does so, I feel something taking over inside of me."
            "I want to be the one in control this time, the one calling the shots."
            "So as soon as my cock is where I want it to be, I take hold of Audrey's wrist."
            "I don't use anywhere near all of my strength, and I don't force her either."
            show audrey standing pleasure
            play sound audrey_moans_discreet_medium loop
            "Because as soon as I start to assert myself, Audrey seems to react accordingly."
            "She allows me to pull her arm back, then use it almost to control her."
            "At the same time, I'm pushing forwards, my cock rubbing against her pussy."
            show audrey standing normal blush
            "Audrey whimpers in anticipation as I apply ever more pressure."
            "And she begins to gasp as her body surrenders to the inevitable."
            show audrey standing pleasure -blush
            play sexsfx1 slide_in
            play sound audrey_moans_happy_low loop
            "My cock sinks into her slowly, allowing me to savour every second."
            "Audrey's moans only serve to make the whole thing that much better too."
            "It's like all of her will to resist is melting away as I enter her."
            "And by the time I'm as deep as I can go, I feel like she's in the palm of my hand."
            "Audrey only makes the feeling more real when she looks back over her shoulder."
            "Because when she does, I can see the unusual quality of submission in her eyes."
            "She hardly needs to nod her head in order to tell me that she's at my mercy."
            play sexsfx1 fuck_calm
            play sound audrey_moans_happy_medium loop
            "Spurred on by this revelation, I find that I can't hold back for a second."
            "Normally everything is a battle of wits with Audrey."
            "Sure, she's willing to share herself with me."
            "But normally it's a battle of wills that she always wins."
            "Now she's offering herself up to me without reservation."
            play sexsfx1 fuck_moderate
            "And I'm like a starving man set loose in an all-you-can-eat buffet!"
            "My ears are filled with the sound of my thighs pounding Audrey's buttocks."
            "That and my own laboured breathing, mixed with her desperate panting."
            "My hand kneads her like she's made of clay."
            "But the real thrill is coming from the sensation of my cock inside her."
            show audrey standing normal blush
            play sexsfx1 fuck_speed
            play sound audrey_moans_happy_high loop
            "Audrey feels so good around it, like she was made to take it."
            "Each and every motion seems to feel better than the last."
            "Part of me wants to keep on doing this to her forever."
            "But a more rational part of me is already aware of where this is going."
            "I can't keep myself from reaching the end, not for much longer."
            stop sound
            audrey.say "Aah..."
            audrey.say "Mmm..."
            show audrey standing pleasure
            audrey.say "Can't...can't take more..."
            audrey.say "You're gonna...make me cum!"
            play sound audrey_moans_happy_high loop
            "True to her word, Audrey starts to twitch and squirm."
            "Her muscles squeeze my cock, making me follow her lead."
            call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_34
            if _return == "vaginal_condom":
                "None of which is a problem, because we remembered to use a condom!"
                "All I have to do is stand back and enjoy what follows soon afterwards."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 1
                with vpunch
                "Which is the amazing sensation of losing it inside of Audrey."
                with vpunch
                "I keep on thrusting, using the last of my energy as I do so."
                "And she all but collapses against the wall, held up by it and me alike."
            elif _return == "vaginal_outside":
                "In the hurry to start fucking, neither of us remembered to use a condom."
                "But I soon solve that problem by pulling my cock out of Audrey in short order."
                "There's nothing that she can do to stop me, just moan at the sudden sensation."
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.sub += 1
                with vpunch
                pause 0.2
                with vpunch
                pause 0.2
                with vpunch
                "And then she moans more quietly as I shoot my load over her back and buttocks."
                "And she all but collapses against the wall, held up by it and me alike."
            elif _return == "vaginal_inside_pregnant":
                stop sound
                audrey.say "Don't stop now!"
                audrey.say "Cum...in...me!"
                play sound audrey_moans_happy_high loop
                "Luckily for Audrey, the fact that she's pregnant means I can do just that."
                "Taking care to support her swollen belly, I give her exactly what she wants."
                "All I have to do is stand back and enjoy what follows soon afterwards."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 3
                show audrey standing cum ahegao -blush with vpunch
                "Which is the amazing sensation of losing it inside of Audrey."
                with vpunch
                "I keep on thrusting, using the last of my energy as I do so."
                show pussy_insert audrey cum zorder 1 at zoomAt(0.75, (820, 200))
                with vpunch
                "And she all but collapses against the wall, held up by it and me alike."
            elif _return == "vaginal_inside_pill":
                stop sound
                audrey.say "Don't stop now!"
                audrey.say "Cum...in...me!"
                play sound audrey_moans_happy_high loop
                "Luckily for Audrey, the fact that she's on the pill means I can do just that."
                "All I have to do is stand back and enjoy what follows soon afterwards."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 2
                show audrey standing cum ahegao -blush with vpunch
                "Which is the amazing sensation of losing it inside of Audrey."
                with vpunch
                "I keep on thrusting, using the last of my energy as I do so."
                show pussy_insert audrey cum zorder 1 at zoomAt(0.75, (820, 200))
                with vpunch
                "And she all but collapses against the wall, held up by it and me alike."
            elif _return == "vaginal_inside_happy":
                stop sound
                audrey.say "Don't stop now!"
                audrey.say "Cum...in...me!"
                play sound audrey_moans_happy_high loop
                "Audrey's words come as a surprise, reminding me we didn't use a condom."
                "But even as I try to pull out, I can feel her holding onto me."
                play sexsfx1 cum_inside
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 5
                #$ audrey.impregnate()
                show audrey standing cum ahegao with vpunch
                "There's no way I can stop myself from losing it inside of her."
                with vpunch
                "And while I'm almost frantic, Audrey seems delighted with the result."
                "I swear I can even hear her laughing as she all but collapses against the wall, held up by it and me alike."
            elif _return == "vaginal_inside_mad":
                stop sound
                audrey.say "Stop!"
                audrey.say "Don't...cum...in...me!"
                play sound audrey_moans_happy_high loop
                "Audrey's words come as a surprise, reminding me we didn't use a condom."
                "But even as I try to pull out, I realise it's already too late."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love -= 5
                #$ audrey.impregnate()
                show audrey standing cum normal -blush with vpunch
                "There's no way I can stop myself from losing it inside of her."
                with vpunch
                "We're both frantic, but neither of us can do anything to change what just happened."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I pull Audrey closer still."
            "Already thinking about how it's going to feel to be inside of her."
            "And I guess that me being inside of her is all that's on Audrey's mind too."
            "As she wastes no time in grabbing hold of my cock and thrusting it between her thighs."
            "But as she does so, I feel something taking over inside of me."
            "I want to be the one in control this time, the one calling the shots."
            "So as soon as my cock is where I want it to be, I take hold of Audrey's wrist."
            "I don't use anywhere near all of my strength, and I don't force her either."
            show audrey standing pleasure
            play sound audrey_moans_discreet_medium loop
            "Because as soon as I start to assert myself, Audrey seems to react accordingly."
            "She allows me to pull her arm back, then use it almost to control her."
            "At the same time, I'm pushing forwards, my cock rubbing against her pussy."
            "And that's the exact moment I choose to reveal my true intentions."
            "I pull back, now aiming my cock between Audrey's buttocks."
            audrey.say "Wha..."
            audrey.say "What are you..."
            "In answer, I begin to push the head of my cock into her ass."
            show audrey standing normal blush
            "Audrey whimpers in anticipation as I apply ever more pressure."
            "And she begins to gasp as her body surrenders to the inevitable."
            show audrey standing pleasure -blush
            play sexsfx1 slide_in
            play sound audrey_moans_happy_low loop
            "My cock sinks into her slowly, allowing me to savour every second."
            "Audrey's moans only serve to make the whole thing that much better too."
            "It's like all of her will to resist is melting away as I enter her."
            "And by the time I'm as deep as I can go, I feel like she's in the palm of my hand."
            "Audrey only makes the feeling more real when she looks back over her shoulder."
            "Because when she does, I can see the unusual quality of submission in her eyes."
            "She hardly needs to nod her head in order to tell me that she's at my mercy."
            play sexsfx1 fuck_calm
            play sound audrey_moans_pained_medium loop
            "Spurred on by this revelation, I find that I can't hold back for a second."
            "Normally everything is a battle of wits with Audrey."
            "Sure, she's willing to share herself with me."
            "But normally it's a battle of wills that she always wins."
            "Now she's offering herself up to me without reservation."
            "And I'm like a starving man set loose in an all-you-can-eat buffet!"
            "My ears are filled with the sound of my thighs pounding Audrey's buttocks."
            "That and my own laboured breathing, mixed with her desperate panting."
            "My hand kneads her like she's made of clay."
            "But the real thrill is coming from the sensation of my cock inside her."
            show audrey standing normal blush
            play sexsfx1 fuck_speed
            play sound audrey_moans_pained_high loop
            "Audrey feels so good around it, like she was made to take it."
            "Each and every motion seems to feel better than the last."
            "Part of me wants to keep on doing this to her forever."
            "But a more rational part of me is already aware of where this is going."
            "I can't keep myself from reaching the end, not for much longer."
            audrey.say "Aah..."
            audrey.say "Mmm..."
            show audrey standing pleasure
            audrey.say "Can't...can't take more..."
            audrey.say "You're gonna...make me cum!"
            "True to her word, Audrey starts to twitch and squirm."
            "Her muscles squeeze my cock, making me follow her lead."
            call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_35
            if _return == "anal_inside":
                "None of which is a problem, because I'm balls deep in Audrey's ass!"
                "All I have to do is stand back and enjoy what follows soon afterwards."
                play sexsfx1 final_thrust
                play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 1
                show audrey standing cum ahegao with vpunch
                "Which is the amazing sensation of losing it inside of Audrey."
                with vpunch
                "I keep on thrusting, using the last of my energy as I do so."
                "And she all but collapses against the wall, held up by it and me alike."
            elif _return == "anal_outside":
                "I could just keep right on going and cum in Audrey's ass."
                "But I want to keep her guessing, to make this a surprise."
                "So I choose to pull my cock out of Audrey in short order."
                "There's nothing that she can do to stop me, just moan at the sudden sensation."
                play sexsfx1 pop_out
                play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.sub += 1
                with vpunch
                pause 0.2
                with vpunch
                pause 0.2
                with vpunch
                "And then she moans more quietly as I shoot my load over her back and buttocks."
                "And she all but collapses against the wall, held up by it and me alike."
            $ audrey.flags.anal += 1
    return

label audrey_fuck_mc_office:


    audrey.say "What is it [hero.name]?"
    call office_harem_fuck_choices ('audrey') from _call_office_harem_fuck_choices_1
    return

label audrey_fuck_office_choices:
    menu:
        "Use her on the desk" if "audrey_event_06" in DONE:
            call audrey_fuck_office_desk from _call_audrey_fuck_office_desk_1
        "Spank her" if "audrey_spanking_2" in DONE:
            call audrey_fuck_office_spank from _call_audrey_fuck_office_spank
        "Cowgirl" if "audrey_event_08" in DONE and hero.sexperience >= 5:
            call audrey_fuck_office_cowgirl from _call_audrey_fuck_office_cowgirl_1
        "Doggy" if "audrey_event_08" in DONE and hero.sexperience >= 10:
            call audrey_fuck_office_doggy from _call_audrey_fuck_office_doggy_1
        "Missionary" if hero.sexperience >= 15:
            call audrey_fuck_office_missionary (15) from _call_audrey_fuck_office_missionary
        "Cunnilingus" if audrey.flags.oral and hero.sexperience >= 20:
            call audrey_fuck_office_cunnilingus from _call_audrey_fuck_office_cunnilingus
        "Forget it":
            audrey.say "Hum."
            $ hero.cancel_activity()
    return

label audrey_fuck_office_desk:
    hide audrey
    show audrey desk work spank close with hpunch
    play sexsfx1 spank
    "My free hand flashes out, catching Audrey a vicious slap with the palm of my hand."
    show audrey desk mark -spank
    "A second later she feels the other side as it deals her a backhander on the return."
    "Before she can as much as cry out, I force her head down onto the desk and hold it there, hand in her hair."
    show audrey desk open
    "I spread her legs by kicking at her heels until she does as I desire, and then I press my weight onto her as she's leant over the desk."
    "The hand not pinning her roughly tugs down her short and knickers almost to her knees."
    "I seem to have lost the power of speech this entire time, as though no words will explain what I'm doing or why."
    show audrey desk close
    "The first sound that I hear Audrey make is a strained moan as I rub my fingers harshly against her pussy."
    "For some reason, the fact that it's already moist, the scent of it detectable on the air, makes me even more incensed."
    "I push first two, then three and finally four fingers into Audrey's slippery lips."
    "This isn't some attempt to coax her gently towards being ready for it."
    "More like it's a way of mocking and humiliating while she's helpless."
    "Even as she makes more incoherent sounds, I feel my desire to degrade her growing alongside my cock."
    "I drag my fingers out of her and almost tear open my flies."
    show audrey desk mike
    "Leaning in close, I make sure Audrey can feel the head of my cock against her burning pussy."
    mike.say "You remember this guy, Audrey?"
    show audrey desk open
    "She moans again, making no sense whatsoever."
    mike.say "Sure you do - you were all over him the other night."
    mike.say "Until you ran off and left him in the lurch..."
    show audrey desk vaginal
    play sound audrey_generic_oh_3
    "I push myself just far enough inside of her to get the reaction I'm looking for."
    mike.say "He wants to show you what you missed out on by cutting and running..."
    mike.say "And this time, he's not taking no for an answer!"
    show audrey desk close forth
    play sexsfx1 slide_in
    play sound audrey_moans_discreet_low loop
    "I don't want to make this some kind of kinky tease for her, so I shove myself inside as roughly as I can."
    "She makes a sound that's more like an animal that's been kicked in the gut than a human being."
    "If I'm honest, I get more gratification from that sound than I do the sensation of being inside of her."
    "My incandescent rage means that I barely perceive what my cock is feeling."
    mike.say "You had me open and exposed back then, Audrey..."
    mike.say "What do you say about returning the favour, eh?"
    show audrey desk pulled open
    "I pull her up by her hair just so that I can reach around and grasp the front of her blouse."




    play sound audrey_moans_happy_low loop
    play sexsfx1 slide_out
    show audrey desk back lookback
    pause 0.35
    play sexsfx1 slide_in
    show audrey desk forth
    pause 0.35
    play sexsfx1 slide_out
    show audrey desk back
    pause 0.35
    play sexsfx1 slide_in
    show audrey desk forth
    pause 0.35
    play sexsfx1 slide_out
    show audrey desk back
    pause 0.35
    play sexsfx1 slide_in
    show audrey desk forth with hpunch
    "Audrey's hands are groping amongst the papers and paraphernalia on my desk now."
    "Her fingers clasp around and crease up handfuls of paper as I keep on pounding into her the whole time."
    "Suddenly I have a moment of clarity, realising that there are several heavy objects well within her reach."
    "She could snatch one up and swing it at me with ease, should the idea form in her mind."
    "But then I catch a glimpse of Audrey's face in the reflective surface of the window."
    "And I instantly know that there's no way she could manage such a thing."
    play sound audrey_moans_happy_medium loop
    play sexsfx1 slide_out
    show audrey desk back
    pause 0.25
    play sexsfx1 slide_in
    show audrey desk forth open with hpunch
    pause 0.25
    play sexsfx1 slide_out
    show audrey desk back
    pause 0.25
    play sexsfx1 slide_in
    show audrey desk forth with hpunch
    pause 0.25
    play sexsfx1 slide_out
    show audrey desk back
    pause 0.25
    play sexsfx1 slide_in
    show audrey desk forth with hpunch
    "Audrey's cheeks and forehead are a vivid shade of red, her eyes crossed and almost rolling back into her head."
    "Her tongue is lolling out of her mouth as she pants like an exhausted dog."
    "I've never seen anything like it before...and its strangeness snaps me back to reality."
    "What freaks me out isn't the extreme nature of her expression, but the fact that it seems to suggest she's in a state of sheer ecstasy."
    "Already I can feel my heart rate slowing and my cock beginning to shrink."
    play sexsfx1 pull_out
    play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
    pause 0.5
    show audrey desk normal close out back squirt
    with hpunch
    "I know that I should take more care, but I just can't help pulling out and stepping quickly away from Audrey."
    "Without me to support her, she crumples to the floor and lays there in an untidy heap."
    show audrey desk -squirt
    "Her body is still quivering even then, and I can hear her moaning as she rides out the last of what must be an orgasm."
    show audrey desk open
    "All I can do is stare at her, wondering just what the hell motivates this baffling woman."
    "Did she actually..."
    "Is there a chance that she..."
    "Fuck - am I really thinking that she might have goaded me into doing this because she wanted it?!?"
    $ audrey.sexperience += 1
    return

label audrey_fuck_office_doggy:
    scene audrey doggy
    if game.room == 'ceo':
        show audrey doggy ceo
    "Audrey crawls onto the table, turning her back to me as she goes."
    "This means that I get a glorious view of her legs and ass the whole time."
    "But when she looks back over her shoulder at me, I see something in her eyes."
    "It's something new, something that I've never seen there before."
    "The usual mocking look is gone, replaced by a need that's impossible to miss."
    "It makes me think that I'm actually starting to understand Audrey."
    "To realise that she behaves like this to serve a deep and overwhelming need."
    "And right now, that makes two of us."
    "Because I have an overwhelming need to have my cock inside of her!"
    "I strip my own clothes off as quickly as I can, tossing them carelessly aside."
    "And then I climb onto the desk after Audrey."
    "I grab her firmly around the thighs, using my weight to pin her down."
    "She yelps in alarm as I do so, but I know for certain that she's faking it."
    "And that's because she also grinds herself hard against my groin."
    audrey.say "Oh, [hero.name]..."
    audrey.say "What are you going to do to me?"
    if audrey.flags.mikeNickname not in nickname_master:
        mike.say "That's Mister [hero.family_name] to you, Audrey."
        mike.say "And what I'm going to do..."
    mike.say "I'm going to stick my cock in you and make you cum!"
    "Audrey actually gasps in anticipation at this."
    "And I feel her rubbing her ass against in what seems almost like desperation!"
    audrey.say "Oh yeah..."
    audrey.say "Please, [hero.name]!"
    audrey.say "I'm a bad, bad girl."
    audrey.say "Please fuck me hard!"
    "How can I turn down an invitation like that?"
    "I don't waste any time with foreplay or teasing."
    "Sure, there's a time and a place for that kind of thing."
    "But this isn't it."
    "This is just a quick, dirty fuck."
    "Audrey let's out an animal moan as I thrust my cock against her pussy."
    "It's slicker than I expected, offering almost no resistance whatsoever."
    show audrey doggy inside
    play sexsfx1 slide_in
    "This means that I slide straight into her, going almost the whole way in one motion."
    play sexsfx1 slide_out
    "Audrey arches her back, taking all that I have to give."
    play sexsfx1 fuck_speed loop
    play sound audrey_moans_happy_medium loop
    "And a moment later, I'm pounding away at her like my life depends on it."
    "The air is filled with the sound of my groin slapping against Audrey's ass."
    "I reach one hand around to squeeze her breasts."
    "And the other I use to grab a handful of her hair."
    show audrey doggy pleasure
    play sexsfx1 fuck_sprint loop
    play sound audrey_moans_happy_high loop
    "That done, I pull her head backwards, bending her double to kiss her lips."
    "Every thrust into her pushes Audrey's tongue further into my mouth."
    "And I feel like I could go right on like this until I cum inside of her."
    "But the animal seems to be taking over in me, making me want to mark my territory."
    play sexsfx1 pull_out
    pause 0.5
    show audrey doggy -inside
    play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
    "And so, when I feel myself about to cum, I yank my cock straight out of Audrey."
    "I do it in one go, feeling her groan as I'm still kissing her."
    "But I don't let go of her hair for a moment, holding her still."
    show audrey doggy cum bodycum with hpunch
    "A moment later, I shoot my load over Audrey's buttocks."
    show audrey doggy ahegao with hpunch
    "She wriggles and writhes beneath me the whole time."
    "Her tongue doing likewise inside of my mouth."
    $ audrey.sexperience += 1
    return

label audrey_fuck_office_cowgirl:
    "Audrey crawls backwards onto the desk as I begin to strip off my own clothes."
    "I can see that she's already getting worked up, cheeks flushing in anticipation."
    "And so it doesn't take long for my cock to start getting hard as I follow her."
    scene audrey cowgirl
    if game.room == "ceo":
        show audrey cowgirl ceo
    "Audrey bites her lip for a moment, and then crawls atop me."
    "Her pussy is already getting good and slick, betraying that she's more than ready."
    "Neither of us says a word, but we seem to be focused on the same goal."
    "This isn't going to be a case of slow and gentle love-making."
    "It's a quick and dirty fuck between two people that are desperate for it!"
    "So it comes as no surprise when Audrey grabs hold of my cock a moment later."
    "Straddling my thighs, she rubs it roughly against the lips of her pussy."
    audrey.say "Mmm..."
    audrey.say "Oh fuck..."
    audrey.say "This is gonna feel so good inside of me!"
    "And with that, she pushes herself down and onto me."
    show audrey cowgirl vaginal
    play sexsfx1 slide_in
    play sound audrey_generic_oh_3
    "I gasp as I feel the sensation of Audrey's lips resisting me."
    "It only lasts for the briefest of moments before they part."
    "But it somehow makes the feeling of her sliding onto my cock all the more intense."
    show audrey cowgirl pleasure
    play sexsfx1 fuck_calm loop
    "Audrey sinks as low as she can, trying to force it deeper still."
    "And then she wriggles and squirms against me, grinding my cock into her."
    "All I can do is lay back, breathing heavily as she rides me."
    "Audrey has her arms stretched out behind her and her legs braced against the desktop."
    "And she uses this position to move her groin up and down."
    "She goes slowly at first, allowing the pleasure this brings to mount."
    "But soon enough she picks up speed, and it starts to build in intensity."
    show audrey cowgirl speed
    play sexsfx1 fuck_moderate loop
    audrey.say "Ah..."
    audrey.say "I was...right..."
    audrey.say "Your cock...feels SO good!"
    play sound audrey_moans_happy_medium loop
    "It feels pretty damn good to be inside of Audrey too."
    "In fact, I can feel all of the stress of my workload falling away."
    "All I can think about now is getting the most out of fucking Audrey."
    "Which is something that doesn't seem to be a problem."
    "And that's because she has the same agenda herself!"
    "By now her thighs are hitting mine with a loud slapping sound."
    play sexsfx1 fuck_speed loop
    play sound audrey_moans_happy_high loop
    show audrey cowgirl ahegao
    "There's no more talking from her either, as she pants and moans."
    "And then I can feel it - I'm about to cum!"
    "I crawl backwards and push Audrey in the opposite direction."
    play sexsfx1 pull_out
    play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
    show audrey cowgirl -vaginal -speed
    show sexinserts head audrey zorder 1 at center, zoomAt(1, (720, 710))
    show sexinserts chest audrey as chestcum zorder 2 at center, zoomAt(1, (-140, 910))
    "Taken by surprise, she wails as my cock pops out of her."
    show audrey cowgirl cumshot with vpunch
    "Which means that her mouth is wide open when I shoot my load a moment later!"
    show sexinserts head audrey cum zorder 1 at center, zoomAt(1, (720, 710))
    with vpunch
    "My cum spatters over Audrey's lips and tongue."
    show sexinserts chest audrey cum as chestcum zorder 2 at center, zoomAt(1, (-140, 910))
    show audrey cowgirl dickcum onbody -cumshot
    with vpunch
    "But most of it hits her square in the chest, soaking into her clothes."
    "All she can do is stare at me, wide-eyed, as she struggles to catch her breath."
    hide sexinserts
    hide chestcum
    $ audrey.sexperience += 1
    return

label audrey_fuck_office_missionary(sexperience_min):
    scene audrey missionary
    show audrey missionary nomike office
    with fade
    "Audrey lies back on the sofa, inviting me to join her."
    "I lie myself down atop her and take a deep breath."
    "Because I know that I'm going to enjoy this!"
    menu:
        "Fuck her ass" if hero.sexperience >= sexperience_min + 5:
            "And that's because I know what I have in mind and Audrey doesn't."
            "I waste no time in spreading her legs even further apart."
            show audrey missionary -nomike
            "That and pushing against her a little."
            "Not much, just enough to lift her an inch or two off the sofa."
            "Which exposes the part of her body that I'm looking for..."
            audrey.say "Ah..."
            audrey.say "Where are you..."
            "I have to make my move before Audrey gets a sense of what's happening."
            "So I give it one hard push forwards, and I feel myself hitting the target."
            play sexsfx1 slide_in
            show audrey missionary anal
            audrey.say "Whoa..."
            audrey.say "My...my ass!"
            "The reaction that I'm feeling down there mirror's the sound of Audrey's voice."
            "Her muscles are tense and reluctant at first, unconsciously trying to keep me out."
            "But it doesn't take long for them to begin to melt as I push onwards."
            "And I can hear a distinct change in Audrey's tone as I do so too."
            audrey.say "Oh fuck..."
            audrey.say "Oh fuck yes..."
            show audrey missionary pleasure
            audrey.say "Don't stop now...please!"
            "It feels pretty good to hear Audrey begging for more like that."
            "But the truth is that she hardly needs to ask for it!"
            "And that's because I'm already doing all I can to deliver."
            "There's not an ounce of resistance left in her body by now."
            "Which means that I can bury myself as deep into her as possible."
            "My speed also picks up, almost without me even realising it."
            play sexsfx1 fuck_speed loop
            play sound audrey_moans_pained_medium loop
            "So before I know what's happening, I'm going as fast as I can."
            "And as hard too, beginning to sweat as I exert myself."
            "But it's not like my efforts go unrewarded."
            "Audrey's desperate for all that I can give her and more besides."
            "She nods her head as I move in and out of her."
            "And it's going faster than her breasts are bobbing."
            "Which means I know it's not just in sympathy with my own thrusts."
            "Audrey holds my eye the whole time."
            "Her breath comes in short, sharp gasps."
            "I'm breathing hard too, feeling the effect of my exertions."
            "But there's no way I'm going to stop before this is done."
            "Using the last of my energy, I step things up again."
            "And my efforts cause an immediate reaction in Audrey."
            show audrey missionary ahegao
            play sexsfx1 fuck_sprint loop
            play sound audrey_moans_pained_high loop
            "I can feel her muscles tighten and her body tense."
            "Then the floodgates open and she starts to cum."
            "The sight of it alone is something to see."
            "But I have my cock buried deep inside of her right now."
            "Which means I can feel every twitch and twinge of her muscles."
            "And it's more than enough for her to take me along for the ride!"
            call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_36
            if _return == "anal_inside":
                "All of my efforts are going into pushing forwards."
                "And all of Audrey's weight is pushing down on me too."
                "So naturally the best solution is just to keep right on going."
                show audrey missionary creampie with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "With one last thrust, I let go and shoot my load."
                with vpunch
                "Audrey's already shaking from her own orgasm."
                with vpunch
                "But feeling mine inside of her seems to set her off again."
                $ audrey.love += 1
                "And she moans the whole time that I'm cumming."
            elif _return == "anal_outside":
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                "It takes everything I have to stop and reverse course."
                "And Audrey makes it even harder by trying to cling onto me too!"
                show audrey missionary -anal
                play sexsfx1 pop_out
                play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "But somehow I still manage to pull my cock out of her in time."
                "I barely have a chance to draw breath before I shoot my load."
                show audrey missionary cum
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                with vpunch
                "And I hear Audrey gasp as I shower her belly with cum."
                show sexinserts chest audrey cum zorder 1 at center, zoomAt(1, (710, 740))
                with vpunch
                "She gazes down at the sight, eyes wide with surprise."
                $ audrey.sub += 1
                show audrey missionary -cum dickcum with vpunch
                "But she stays quiet the whole time, still lost for words."
                hide sexinserts
                hide bellycum
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (audrey, 180) from _call_check_condom_usage_16
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show audrey missionary condom
            show audrey missionary -nomike
            "Audrey must be as eager for this as I am."
            "Because all it takes is a slight push from me."
            "And just like that, I feel my cock slip inside of her."
            play sexsfx1 slide_in
            show audrey missionary vaginal
            "I don't stop moving until it's as deep as it can go."
            "Every fraction of an inch feels incredible."
            "And I can hear Audrey moaning as sink into her."
            "So I'm guessing that she's feeling the same way too."
            audrey.say "Hmm..."
            audrey.say "That's right..."
            audrey.say "That's what I'm talking about!"
            "Audrey smiles up at me as she says all of this."
            "And I can see she has that mischievous glint in her eye."
            "The pair of us should be hard at work right now."
            "But instead we're fucking like crazy on company time."
            show audrey missionary vaginal pleasure
            play sexsfx1 fuck_moderate loop
            play sound audrey_moans_discreet_low loop
            "She's loving the danger too, the fear of being caught in the act."
            "I can feel my heart begin to beat faster too."
            "It's like she's infecting me with her rebellious nature."
            "And every second that I spend inside of her makes it more intense."
            audrey.say "Ah...ha..."
            audrey.say "They're paying us..."
            audrey.say "Paying us to fuck!"
            audrey.say "How good does that make my pussy feel, huh?"
            audrey.say "You can fuck me senseless and still pay the bills!"
            "Audrey's everything that's wrong for the job she does here."
            "She's lazy, disrespectful and likes to stir up trouble."
            "But that just makes me want her around all the more."
            "Especially if she's going to be up for more of this."
            play sexsfx1 fuck_speed loop
            play sound audrey_moans_happy_low loop
            mike.say "You're a bad girl, Audrey..."
            mike.say "Such a bad girl..."
            audrey.say "That's right..."
            audrey.say "So bad...so bad..."
            "Audrey nods desperately as I begin to pick up speed."
            "Her body's rocking as I thrust in and out of her."
            "My thighs slap against hers, louder and louder."
            "And her breasts jiggle and bounce on her chest."
            play sound audrey_moans_happy_medium loop
            "Audrey's moans are getting louder too."
            "They began as low gasps of pleasure."
            "But now they're fast becoming helpless cries."
            "I'm getting worried that somebody will hear them soon."
            "That one of the other girls might come to investigate."
            "But then I begin to wonder if that's what Audrey wants."
            "Maybe she's hoping someone will stick their head round the door."
            "She does like the danger a little too much."
            "So I resolve to finish this before that scenario can play out."
            play sexsfx1 fuck_sprint loop
            play sound audrey_moans_happy_high loop
            "Using my last reserves of strength, I kick it into a higher gear."
            "Audrey reacts almost instantly, her muscles tighten and her body tenses."
            "Then I feel something snap inside of her, and she starts to cum."
            "I'm as deep inside of her as I can go when it happens right now."
            "Which means I can feel every twitch and twinge of her muscles."
            "And it's more than enough for her to take me along for the ride!"
            call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_37
            if _return == "vaginal_condom":
                "All of my efforts are going into pushing forwards."
                "And all of Audrey's weight is pushing down on me too."
                "So naturally the best solution is just to keep right on going."
                "And thanks to the fact we took precautions, it's safe to do so."
                with vpunch
                "With one last thrust, I let go and shoot my load."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                show audrey missionary vaginal ahegao with vpunch
                "Audrey's already shaking from her own orgasm."
                with vpunch
                "But feeling mine inside of her seems to set her off again."
                $ audrey.love += 1
                "And she moans the whole time that I'm cumming."
            elif _return == "vaginal_outside":
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                "It takes everything I have to stop and reverse course."
                "And Audrey makes it even harder by trying to cling onto me too!"
                show audrey missionary -vaginal
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "But somehow I still manage to pull my cock out of her in time."
                "I barely have a chance to draw breath before I shoot my load."
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                show audrey missionary cum
                with vpunch
                "And I hear Audrey gasp as I shower her belly with cum."
                show sexinserts chest audrey cum zorder 1 at center, zoomAt(1, (710, 740))
                with vpunch
                "She gazes down at the sight, eyes wide with surprise."
                $ audrey.sub += 1
                show audrey missionary -cumshot dickcum with vpunch
                "But she stays quiet the whole time, still lost for words."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_inside_pill":
                audrey.say "What are you waiting for?"
                audrey.say "I'm on the pill for god's sake!"
                "All of my efforts are going into pushing forwards."
                "And all of Audrey's weight is pushing down on me too."
                "So naturally the best solution is just to keep right on going."
                "And, as she's so delicately reminded me, there's nothing to stop me doing just that!"
                show audrey missionary creampie ahegao with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "With one last thrust, I let go and shoot my load."
                with vpunch
                "Audrey's already shaking from her own orgasm."
                with vpunch
                "But feeling mine inside of her seems to set her off again."
                $ audrey.love += 2
                "And she moans the whole time that I'm cumming."
            elif _return == "vaginal_inside_pregnant":
                audrey.say "What are you waiting for?"
                audrey.say "You can't knock me up twice!"
                "All of my efforts are going into pushing forwards."
                "And all of Audrey's weight is pushing down on me too."
                "So naturally the best solution is just to keep right on going."
                "And, as she's so delicately reminded me, there's nothing to stop me doing just that!"
                show audrey missionary creampie ahegao with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "With one last thrust, I let go and shoot my load."
                with vpunch
                "Audrey's already shaking from her own orgasm."
                with vpunch
                "But feeling mine inside of her seems to set her off again."
                $ audrey.love += 3
                "And she moans the whole time that I'm cumming."
            elif _return == "vaginal_inside_happy":
                audrey.say "Oh no...no way!"
                audrey.say "You're not getting away from me!"
                "All of my efforts are going into pushing forwards."
                "And all of Audrey's weight is pushing down on me too."
                "Add that crazy little declaration to the mix and you have the perfect distraction."
                "I have no chance of pulling out before it's too late."
                show audrey missionary creampie ahegao with vpunch
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                #$ audrey.impregnate()
                "And so, with one last thrust, I let go and shoot my load."
                with vpunch
                "Audrey's already shaking from her own orgasm."
                with vpunch
                "But feeling mine inside of her seems to set her off again."
                $ audrey.love += 5
                "And she moans the whole time that I'm cumming."
                "Leaving me to panic about the fact I just came inside her without a condom!"
            elif _return == "vaginal_inside_mad":
                audrey.say "Oh no...no way!"
                audrey.say "You have to pull out -NOW!"
                audrey.say "What are you waiting for?"
                audrey.say "I'm not on the pill for god's sake!"
                "All of my efforts are going into pushing forwards."
                "And all of Audrey's weight is pushing down on me too."
                "I have no chance of pulling out before it's too late."
                play sexsfx1 final_thrust
                $ audrey.love -= 5
                show audrey missionary creampie ahegao with vpunch
                #$ audrey.impregnate()
                "And so, with one last thrust, I let go and shoot my load."
                with vpunch
                "Audrey's already shaking from her own orgasm."
                with vpunch
                "But feeling mine inside of her seems to set her off again."
                "And she moans the whole time that I'm cumming."
                "Leaving me to panic about the fact I just came inside her without a condom!"
    $ audrey.sexperience += 1
    return

label audrey_fuck_office_cunnilingus:
    "I have no idea if this was what Audrey had in mind."
    "And maybe I'm playing right into her hands by doing this."
    "But who the hell cares?"
    "I can see Audrey's pussy, right there in front of me."
    "And there's nothing going to stop me from getting my hands on it!"
    "I all but pounce on Audrey a moment later, leaping onto the desk."
    "Sure, Audrey's pretty cool and collected."
    "But even she can't help letting out a yelp of surprise."
    hide audrey
    show audrey cunnilingus office with fade
    audrey.say "Hey - what the hell?!?"
    "A moment later, I have my head between Audrey's thighs."
    "And my tongue is exploring around the lips of her pussy."
    "All of which seems to bring about a sudden change in her mood."
    audrey.say "Oh..."
    audrey.say "Oh yeah..."
    audrey.say "Now that's what I'm talking about!"
    play sound audrey_moans_discreet_low loop
    "I can't help smiling at Audrey's reaction."
    "Even though my mouth is currently buried into her pussy."
    "And it makes me want to live up to her expectations too."
    "My tongue darts out of my mouth and between her lips."
    show audrey cunnilingus gasp
    "I use it to trace the lines and creases down there."
    "And all the time I'm also working it ever deeper inside."
    "Audrey begins to buck and twitch above me."
    "In fact she seems to move whenever I flick my tongue."
    audrey.say "Mmm..."
    audrey.say "Oh my god..."
    audrey.say "You're gonna make me cum!"
    show audrey cunnilingus pleasure
    play sound audrey_moans_happy_medium loop
    "I smile again at Audrey's sudden exclamation."
    "After all, that was kind of the idea from the start!"
    "And it seems like I'm almost there too."
    "Audrey practically shoves her pussy into my face."
    "At the same time her thighs clamp together, trapping my head!"
    show audrey cunnilingus ahegao squirt
    play sound audrey_moans_happy_orgasm_2
    "I feel her shudder around me, and I know that she's cumming right now."
    "But all I can do is ride it out and wait for the moment to pass."
    "Then Audrey goes limp, falling back onto the sofa."
    audrey.say "Sh...shit..."
    audrey.say "You can...you can have me..."
    audrey.say "Do whatever you like to me...after that!"
    $ audrey.love += 2
    $ audrey.sexperience += 1
    return

label audrey_fuck_office_spank:
    if audrey.flags.nickname == "toy":
        mike.say "Good [game.calendar.time_of_day_name], Toy."
    else:
        mike.say "Good [game.calendar.time_of_day_name], Audrey."
    mike.say "Everything's fine ?"
    "Audrey cocks her head on one side."
    "And a nonchalant expression appears on her face."
    audrey.say "No...not really."
    show audrey frown
    audrey.say "I'm just SO fucking bored right now."
    audrey.say "I thought I'd stop working and go for a stroll!"
    "She's sauntering ever closer to my desk as she says all of this."
    "And her eyes are wandering here and there, focused on nothing in particular."
    mike.say "So you're basically saying that you're too bored to do any actual work?"
    if audrey.flags.nickname == "toy":
        mike.say "Am I right, Toy?"
    else:
        mike.say "Am I right, Audrey?"
    show audrey normal
    audrey.say "Yeah...pretty much!"
    "Audrey's reached my desk by now, and that's where she stops."
    "She looks down at the piles of work spread out across it."
    audrey.say "Say, you look busy!"
    audrey.say "Be a shame if someone were to..."
    audrey.say "I don't know...do something like this!"
    "That's all the warning I get before Audrey sweeps her arm across the desk."
    "She sends most of the paperwork cascading to the floor."
    "And the stuff that doesn't fall is thrown into disarray all the same."
    audrey.say "Oops!"
    show audrey joke
    audrey.say "Did I do a bad thing?"
    if audrey.flags.nickname == "toy":
        mike.say "Yes, Toy - that was a very bad thing."
    else:
        mike.say "Yes, Audrey - that was a very bad thing."
    audrey.say "So...what are you going to do about it, huh?"
    "I'm out of my chair before Audrey's even finished her challenge."
    "I grab her around the waist, and she lets out a yelp of surprise."
    "But she doesn't resist for a moment, letting me know this is what she wants."
    "I'm on auto-pilot now, putting her over my lap."
    hide audrey
    show spank audrey pulled with fade
    if audrey.flags.sexywork:
        "A moment later I have Audrey laying on my thighs, her ass exposed."
    else:
        "A moment later I have Audrey's skirt lowered down and her ass exposed."
    "She makes a show of wriggling and squirming, but never enough to escape my clutches."
    "I don't wait a second longer, just start paddling her ass with my hand."
    show spank audrey up
    pause 0.3
    show spank audrey spank surprised
    play sexsfx1 spank
    with vpunch
    "Every blow makes her gasp and wriggle across my lap."
    show spank audrey up
    pause 0.3
    show spank audrey spank pleasure marks
    play sexsfx1 spank
    with vpunch
    "And I can feel myself getting harder the whole time."
    hide spank
    show audrey normal blush
    with fade
    "Once I'm done, Audrey leaps to her feet and pulls down her skirt."
    $ audrey.sub += 1
    $ audrey.sexperience += 1
    return

label audrey_boardgame_sex:
    $ sexperience_min = 5
    scene bg livingroom
    "The board is all set up in the middle of the sitting-room floor."
    show board games audrey island with fade
    "I've gone over the rules of the game with Audrey more than once."
    "And we're well into playing a game of Plutocracy."
    audrey.say "Urgh..."
    audrey.say "How long does this last again?"
    "Well, at least I'm well into the game."
    "Trying to be patient, I force a smile onto my face."
    mike.say "We've only been playing a couple of minutes, Audrey!"
    mike.say "And it's my turn to choose what we do for our date too."
    hide board games
    show audrey casual normal with fade
    audrey.say "Yeah, yeah, yeah..."
    show audrey mock
    audrey.say "And you want to play a BORED game!"
    "I choose to ignore Audrey's complaints and instead hand her the dice."
    hide audrey
    show board games audrey island
    with fade
    "She takes them and pretty much tosses them without looking."
    mike.say "Six and a seven, Audrey..."
    mike.say "Oh-oh!"
    mike.say "You landed on Cockfosters Close!"
    mike.say "I own that!"
    audrey.say "Fuck-a-doodle-doo!"
    mike.say "You know what that mean, right?"
    audrey.say "That you're a slum landlord?"
    "I frown and shake my head."
    mike.say "No, Audrey."
    mike.say "It means you owe me fifty dollars."
    mike.say "So pay up!"
    "Audrey grins and shakes her own head."
    audrey.say "Nah - I don't have it."
    mike.say "What are you talking about, Audrey?!?"
    mike.say "You just passed Go last turn and got two hundred dollars."
    mike.say "I can see the money in your hand!"
    hide board games
    show audrey casual normal with fade
    "Audrey holds up the play-money and shakes her head again."
    audrey.say "What, this?"
    show audrey joke
    audrey.say "No, you see I need this to pay off my dealer."
    audrey.say "Otherwise he said he'd break my legs!"
    mike.say "Audrey!"
    mike.say "You're not playing the game properly!"
    "Feeling frustrated, I make a grab for the play-money."
    "But Audrey jerks it back and out of my reach."
    show audrey mock
    audrey.say "Help, help!"
    audrey.say "I'm being oppressed!"
    "Just like that, we're scuffling on the sitting-room floor over a board-game."
    "I land on top of Audrey, pinning her to the ground."
    "But as I get a good look at her face, I see she's actually smiling."
    audrey.say "Oh no, please, Mister Landlord!"
    audrey.say "Surely there's another way I can pay?"
    "I feel her hand on my cock as she's saying this."
    "And all of a sudden, I find myself forgetting about the board game!"
    "Suddenly my hands are all over Audrey."
    "I'm caressing, stroking and squeezing everything I can get hold of."
    "And she's nodding with increasing desperation."
    "Her hands struggling to pull down my pants."
    audrey.say "You don't want fake money, [hero.name]..."
    audrey.say "Not when you can have real pussy!"
    "A moment later I feel her fingers close around my cock."
    "And I strip down her clothes, ready to play a different kind of game..."
    scene bg black
    show audrey missionary livingroom naked
    with fade
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Audrey's nodding like crazy by now, urging me on."
            "But it's not like I need that much encouragement."
            "I can feel the head of my cock rubbing against the lips of her pussy."
            "And that's more than enough to make me forget all about board-games."
            "Now I'm thinking about being the one to play her instead."
            "All it takes is a slight adjustment of angle, a bit of a push and some pressure..."
            show audrey missionary anal
            audrey.say "Mmm..."
            audrey.say "Ah..."
            audrey.say "Oh wait..."
            audrey.say "That's...that's my ass!"
            play sexsfx1 slide_in
            "I slide slowly into Audrey even as her muscles try to resist."
            "It's a gradual surrender, every inch feeling a little more intense."
            "Until I'm as deep into her as I can possibly go."
            "Audrey's still nodding, like she's the one in charge here."
            "But I'm balls deep in her, and she's been getting me seriously worked-up."
            "So I don't stop to give her any kind of warning."
            play sexsfx1 slide_in
            "Instead I simply start to move up and down atop her."
            play sexsfx1 slide_out
            "Only the first thrust is slow, to measure my movements."
            play sexsfx1 slide_in
            "Then I just throw caution to the wind and go for it."
            play sexsfx1 slide_out
            "My speed picks up as soon as I'm thrusting into her for the second time."
            play sexsfx1 fuck_calm
            play sound audrey_moans_pained_low
            show audrey missionary pleasure
            "And by the third, Audrey's eyes are wide open."
            audrey.say "Oh god..."
            audrey.say "That's good..."
            audrey.say "So good!"
            audrey.say "Please...give it to me!"
            audrey.say "Please fuck my ass?"
            "I'm pleased to hear Audrey's words of encouragement."
            "But it's not like I need them to motivate me right now."
            "My hands are all over her body as I use my weight to pin her down."
            "And the sensation of my cock as it's buried in her ass over and over again..."
            "It's like nothing else I can begin to imagine."
            play sexsfx1 fuck_moderate
            play sound audrey_moans_pained_medium
            "I can see the effect it's having on Audrey too."
            "The way her muscles are shuddering and twitching."
            "The gasps and moans that escape her mouth."
            "And the way her eyes are beginning to glaze over too!"
            "She must be so close to cumming right now."
            "But it looks like I'm going to beat her to the punch!"
            call cum_reaction (audrey, 'anal', sexperience_min) from _call_cum_reaction_38
            if _return == "anal_inside":
                "I'm proven right a moment later as my entire body stiffens."
                "I make one last thrust into Audrey and then it happens."
                play sexsfx1 final_thrust
                play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                with vpunch
                "I shoot my load inside her, as deep as I can make it."
                show audrey missionary creampie with vpunch
                $ audrey.love += 1
                "That pushes her over the edge too, sending her into orbit."
                with vpunch
                "Audrey writhes and wriggles with my cock inside of her."
                "Clinging onto me as if her life depended on it."
            elif _return == "anal_outside":
                $ audrey.sub += 1
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                "I'm proven right a moment later as my entire body stiffens."
                "There's barely enough time for me to pull out of Audrey."
                show audrey missionary -anal with vpunch
                play sexsfx1 pop_out
                play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "And then it happens, I shoot my load over her."
                show audrey missionary cum with vpunch
                "Pulling out seems to have pushed Audrey over the edge too."
                show sexinserts chest audrey cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                with vpunch
                "She writhes and wriggles as I spatter her belly with cum."
                show audrey missionary -cumshot dickcum
                "Then she lies still beneath me, gasping for breath."
                hide sexinserts
                hide bellycum
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            "Audrey's nodding like crazy by now, urging me on."
            "But it's not like I need that much encouragement."
            "I can feel the head of my cock rubbing against the lips of her pussy."
            "And that's more than enough to make me forget all about board-games."
            "All it takes is a little bit of a push and some pressure..."
            audrey.say "Mmm..."
            audrey.say "Ah..."
            audrey.say "Oh yeah..."
            play sexsfx1 slide_in
            "I slide slowly into Audrey as her lips part."
            call check_condom_usage (audrey) from _call_check_condom_usage_17
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show audrey missionary condom
            "It's a gradual surrender, every inch feeling a little more intense."
            "Until I'm as deep into her as I can possibly go."
            if CONDOM:
                show audrey missionary vaginal condom
            else:
                show audrey missionary vaginal
            "Audrey's still nodding, like she's the one in charge here."
            "But I'm balls deep in her, and she's been getting me seriously worked-up."
            "So I don't stop to give her any kind of warning."
            play sexsfx1 slide_in
            "Instead I simply start to move up and down atop her."
            play sexsfx1 slide_out
            "Only the first thrust is slow, to measure my movements."
            play sexsfx1 slide_in
            "Then I just throw caution to the wind and go for it."
            play sexsfx1 slide_out
            "My speed picks up as soon as I'm thrusting into her for the second time."
            play sexsfx1 fuck_calm
            play sound audrey_moans_happy_low
            "And by the third, Audrey's eyes are wide open."
            audrey.say "Oh god..."
            audrey.say "That's good..."
            audrey.say "So good!"
            show audrey missionary vaginal pleasure
            "I'm pleased to hear Audrey's words of encouragement."
            "But it's not like I need them to motivate me right now."
            "My hands are all over her body as I use my weight to pin her down."
            "And the sensation of my cock as it's buried in her pussy over and over again..."
            "It's like nothing else I can begin to imagine."
            play sexsfx1 fuck_moderate
            play sound audrey_moans_happy_medium
            "I can see the effect it's having on Audrey too."
            "The way her muscles are shuddering and twitching."
            "The gasps and moans that escape her mouth."
            "And the way her eyes are beginning to glaze over too!"
            "She must be so close to cumming right now."
            "But it looks like I'm going to beat her to the punch!"
            call cum_reaction (audrey, 'vaginal', sexperience_min) from _call_cum_reaction_39
            if _return == "vaginal_outside":
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                "I'm proven right a moment later as my entire body stiffens."
                "There's barely enough time for me to pull out of Audrey."
                show audrey missionary -vaginal with vpunch
                play sexsfx1 pull_out
                play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                "And then it happens, I shoot my load over her."
                with vpunch
                "Pulling out seems to have pushed Audrey over the edge too."
                $ audrey.sub += 1
                show sexinserts chest audrey zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (740, 970))
                show audrey missionary cum ahegao
                with vpunch
                "She writhes and wriggles as I spatter her belly with cum."
                show audrey missionary -cumshot dickcum
                "Then she lies still beneath me, gasping for breath."
                hide sexinserts
                hide bellycum
            else:
                "I'm proven right a moment later as my entire body stiffens."
                "I make one last thrust into Audrey and then it happens."
                with vpunch
                "I shoot my load inside her, as deep as I can make it."
                play sexsfx1 final_thrust
                play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                $ audrey.love += 2
                show audrey missionary creampie ahegao with vpunch
                "That pushes her over the edge too, sending her into orbit."
                with vpunch
                "Audrey writhes and wriggles with my cock inside of her."
                "Clinging onto me as if her life depended on it."
    hide audrey missionary
    scene bg livingroom
    show audrey naked happy
    with fade
    "Afterwards, Audrey crawls around on the floor as she gathers up her clothes."
    "And it's only now that I notice we totally trashed the game when we were fucking."
    mike.say "Ah shit!"
    mike.say "I had that game since I was a kid."
    "Audrey stops what she's doing to look over my shoulder."
    "Then she makes a snorting noise and shakes her head."
    audrey.say "Quit whinging, [hero.name]."
    show audrey naked annoyed
    audrey.say "How many other guys got laid thanks to a board-game?"
    audrey.say "You must be like the King of the Nerds or something!"
    $ hero.cancel_activity()
    return

label audrey_fuck_audreylivingroom:
label audrey_fuck_audreybedroom:
label audrey_fuck_audreyhome:
    if not "audrey_apartment_sex" in DONE:
        $ DONE["audrey_apartment_sex"] = game.days_played
    scene bg black with dissolve
    pause 0.1
    scene bg audreybedroom with wiperight
    $ game.room = "audreybedroom"
    "I'm walking into Audrey's bedroom as she holds the door open for me."
    "And I'm doing the very best I can to look like I'm totally in control as I do so."
    "Because I want to give her the impression that this is one hundred percent cool."
    "That I'm completely casual and laid-back at the idea of being here with her."
    "But of course the truth of the matter is that I'm pretty much shitting myself right now!"
    "And that's simply because I'm so thrilled to be invited into Audrey's bedroom."
    "I mean, the very fact that I'm in here means that we're going to have sex, right?"
    "If she just wanted to sit down and chat about random shit, we'd be in the sitting-room."
    play sound door_slam
    "But even as I'm telling myself this, I can't help jumping a little as Audrey slams the door behind me."
    mike.say "Whoa..."
    mike.say "Erm..."
    show audrey at center, zoomAt(1.25, (340, 880)) with easeinleft
    mike.say "Is there really any need to slam the door like that, Audrey?"
    mike.say "I mean, there's only you and me in the apartment right now."
    mike.say "And it's not like I'm going to try to escape, now is it?"

    if audrey.sub >= 80:
        "Audrey looks instantly concerned as she walks over to me."
        "Looking like she's more than keen to reassure me."
        show audrey talkative
        audrey.say "Well, I'd hope not!"
        audrey.say "I'll certainly do my best to make sure you don't want to do that!"
    else:

        "Audrey cocks her head on one side as I say all of this."
        "And I can see that she has a crooked smile on her face."
        show audrey mock
        audrey.say "Geez, [hero.name]…"
        audrey.say "How can you be so jumpy?"
        audrey.say "You think that I'm going to eat you alive or something?"
    show audrey normal at center, traveling(1.5, 0.3, (640, 1040))
    "Before I have the chance to answer her, Audrey reaches out and takes hold of my hand."
    "Then she leads me over to the bed, pulling me down with her as she sits on the mattress."
    "Of course I don't do anything to stop it from happening."
    "More because I'm now almost totally in Audrey's power than anything else."
    "It just so happens that she seems to want the exact same thing as me right now."
    "And as soon as we're sitting next to each other, Audrey keeps me from speaking again."
    hide audrey
    show audrey kiss
    with fade
    "Because she leans straight in and plants her lips against mine."
    "Instantly I feel my nerves beginning to settle and my anxiety melting away."
    "And I can't help leaning into the kiss that Audrey initiated."
    "Soon enough I can feel her hands all over me, stroking and caressing my body."
    "But it takes me a few more moments to realise that's not all she's doing."
    "Audrey's somehow managing to start undoing the buttons and zips of my clothing."
    "And the next thing I know, things are being peeled off of my body."
    "I struggle to do the same thing, feeling totally clumsy and hopeless as I do so."
    show audrey kiss naked with dissolve
    "But somehow I seem to be able to at least begin peeling off some of Audrey's clothes too."
    "Though part of me thinks that most of what I get done is helped by her efforts to help."
    "The kiss keeps on going until the pair of us are completely naked."
    hide audrey kiss
    show audrey naked at center, zoomAt(1.5, (640, 1040))
    "And only then does Audrey break away from me, panting as she does so."

    if audrey.sub >= 80:
        show audrey embarrassed blush
        audrey.say "So..."
        audrey.say "What do you want me to do next?"
    else:

        show audrey talkative
        audrey.say "Okay, big man..."
        audrey.say "Where do we go from here?"
    show audrey normal
    menu:
        "Blowjob" if audrey.sub >= 25:
            jump audrey_fuck_audreybedroom_blowjob
        "Fuck":
            jump audrey_fuck_audreybedroom_fuck
    return

label audrey_fuck_audreybedroom_blowjob:
    "Being this close to Audrey is normally more than enough to get me pretty hot."
    "But add into the equation the fact that we're both naked, and wow!"
    "It's no surprise to me that I can feel myself getting harder by the second."
    "Soon enough I can't keep from looking down at what's rising from between my thighs."
    "And obviously that instantly draws Audrey's eyes to it as well."

    if audrey.sub >= 80:
        audrey.say "Oh my, my, my!"
        audrey.say "Is all of that because of little me?"
    else:

        audrey.say "Well hello there."
        audrey.say "Looks like one part of you knows what it wants, [hero.name]!"
    "By now I'm almost beginning to blush as Audrey stares at my erection."
    "And I feel like I have to play it down while also trying to get what I want."
    mike.say "Ah..."
    mike.say "You can't really blame me for being excited, Audrey!"
    mike.say "It's because of you that I'm in a state like this."
    mike.say "So do you think you could maybe...help me out?"

    if audrey.sub >= 80:
        "Audrey begins to eagerly nod her head almost as soon as I ask the question."
        "Letting me know that she's ready to do whatever it takes to relieve me."
    else:

        "Audrey doesn't say a thing in response to that."
        "But the knowing look that she gives me speaks volumes."
        "Telling me that she's loving having me in the palm of her hand like this."


    scene bg black
    show audrey bj audreybedroom
    with fade
    "I almost hold my breath as Audrey slides onto the bed next to me."
    "Then she kneels so she can get closer still."
    "All the time she's doing this, her eyes are focussed solely on my manhood."
    "Audrey reaches out with one hand first, gently taking hold of the shaft."
    "Beginning at the base, she strokes and caresses me with her fingers."
    "Moving upwards in a steady, measured manner that speaks of a definite plan, Audrey inches ever higher."
    show audrey bj blink
    "And the moment that there's enough space below her hand, she leans forwards, adding her lips to the equation."
    "I can't keep from gasping at the sensation as I feel Audrey begin using her mouth on me."
    "At first she keeps it to just her lips, which are soft and sensual."
    "But soon enough I feel the first hints of her tongue and teeth getting in on the act."
    "The higher Audrey's mouth goes, the more of it she seems to bring into play."
    "As if teasing me and building anticipation for the moment she reaches the top."
    "Because once she's there, her mouth opens wider than ever before."
    "And my eyes go wide too, watching as she takes the tip between her lips."
    "Audrey doesn't pause for me to prepare myself, she just does it."
    play sexsfx1 audrey_moans_blowjob_low loop
    show audrey bj blowjob at startle (0.1, 10)
    "She wraps her tongue around the head of my cock and then seems to almost pull it inside her mouth."
    "I know that can't be what's actually happening, that she must be lowering her head at the same time."
    "But the effect is uncanny, making me think she's using her tongue like a frog catching a fly."
    show audrey bj at startle (0.1, 10)
    "A moment later her lips close around it, and then her head descends."
    "That's when I feel my eyes half closing as the feelings become even more intense."
    show audrey bj at startle (0.075, 10)
    pause 0.2
    show audrey bj at startle (0.075, 10)
    "Audrey doesn't start to move crazily fast, in fact she keeps a regular pace."
    "It's the way she uses her tongue and teeth that ramps up the intensity for me."
    "Suddenly I feel like I'm clinging onto the mattress for fear of letting go."
    "As if the pleasure Audrey's causing me to feel could sweep me away."
    show audrey bj blink
    "And as she gradually takes me deeper still, it only gets that much more intense."
    "Of course I have no idea how far my cock has gotten inside of Audrey's mouth."
    play sexsfx1 audrey_moans_blowjob_medium loop
    show audrey bj at startle (0.075, 10)
    pause 0.2
    show audrey bj at startle (0.075, 10)
    "But for all the world it's starting to feel like it must be getting into her throat by now."
    "And the mere thought of that is enough to make me begin shuddering with pleasure."
    "All of which means that it's not long before I can feel myself starting to lose it."
    show audrey bj normal
    "Luckily for me, Audrey seems to be able to read my every movement."
    "Because she looks up at me, gesturing up and then down with one hand."
    play sexsfx1 audrey_moans_blowjob_high loop
    show audrey bj at startle (0.075, 10)
    pause 0.2
    show audrey bj at startle (0.075, 10)
    "And I don't need any help to understand what any of that means."
    "She's asking me whether I want her to swallow or let me go."
    menu:
        "Cum in her mouth":
            "As quickly as I can, I replicate the downwards motion Audrey just made with my own hand."
            "She nods, instantly knowing that what I want is for her to keep my cock firmly in her mouth."
            stop sexsfx1
            show audrey bj blink
            "That done, Audrey closes her eyes and redoubles her efforts, working away on me until the very last moment."
            play sexsfx1 audrey_moans_blowjob_swallow
            $ audrey.sub += 2
            show audrey bj cumshot with vpunch
            "And when it comes, she's more than prepared for my exploding inside of her mouth."
            with vpunch
            "Without missing a beat, Audrey gulps down every last drop that shoots out of my cock."
            show audrey bj out dickcum -cumshot normal with vpunch
            "Ensuring that I'm pleasured until the very end, and she can finally release me."
        "Cum on her face":
            "As quickly as I can, I replicate the upwards motion Audrey just made with my own hand."
            "She nods, instantly knowing that what I want is for her to release my cock from her mouth."
            "That done, Audrey parts her lips and begins to draw back her head."
            stop sexsfx1
            show audrey bj blink out
            "This means that my cock slides smoothly out of her mouth, bobbing in front of her face."
            "But once it's freed, Audrey doesn't move another inch, staying right where she is."
            $ audrey.love += 2
            show audrey bj cumshot with vpunch
            "Which means that when I lose it a moment later, she takes the whole thing square in the face."
            with vpunch
            "And she even smiles as the lines of sticky, white cum paint stripes across her features too."
            show audrey bj dickcum -cumshot normal with vpunch
    stop sexsfx1
    hide audrey
    show audrey talkative blush naked at center, zoomAt(1.5, (640, 1040))
    audrey.say "So..."
    audrey.say "What's next?"
    show audrey normal

label audrey_fuck_audreybedroom_fuck(sexperience_min=10):
    if audrey.sub >= 80:
        "Without saying a word, I put my hands on Audrey's shoulders."
        "And then I push her down onto the bed, not stopping until she's horizontal."
        "Audrey makes no effort whatsoever to resist me, allowing herself to be moved."
        "And all the time she's looking up at me with wide eyes and a smile on her face."
        mike.say "I'm what's going to happen now, Audrey..."
        mike.say "Is that I'm going to have my way with you."
        mike.say "Which means doing to you whatever I desire."
        mike.say "Whatever happens to pop into my head, no matter how crazy."
        "None of what I'm saying seems to come as a surprise to Audrey."
        "In fact she nods her head eagerly, as if keen to satisfy my desires."
        show audrey talkative
        audrey.say "Y...yes, master!"
        audrey.say "I'm yours to do with as you please."
        audrey.say "Just tell me what it is that you desire."
        show audrey normal
        "By now I've crawled onto the bed and I'm leaning over Audrey."
        hide audrey
        show spank audrey audreybedroom ready
        with fade
        "So it's easy as can be to side a hand under her thighs and lift them off the mattress."
        show spank audrey up
        pause 0.3
        show spank audrey spank surprised
        play sexsfx1 spank
        with hpunch
        pause 0.3
        show spank audrey ready
        "Then use the other one to deliver a gentle slap to her backside."
        "The sound of me spanking Audrey is louder than I expected."
        "And she lets out the most delightful yelp imaginable too."
        show spank audrey pleasure
        audrey.say "Ooh!"
        audrey.say "Mmm..."
        audrey.say "Please, master - may I have another?"
        "I can't help smiling as I give Audrey exactly what she's asking for."
        show spank audrey up
        pause 0.3
        show spank audrey spank surprised
        play sexsfx1 spank
        play sound audrey_generic_ah_2
        with hpunch
        pause 0.3
        show spank audrey ready
        "The second slap is harder and louder than the first, as is Audrey's reaction."
        show spank audrey pleasure
        audrey.say "Aah..."
        audrey.say "Have I really been that bad, master?"
        audrey.say "Then I guess I deserve to be spanked!"
        show spank audrey up
        pause 0.3
        show spank audrey spank surprised
        play sound audrey_generic_ah_3
        play sexsfx1 spank
        with hpunch
        pause 0.3
        show spank audrey up pleasure
        pause 0.3
        show spank audrey spank surprised marks
        play sexsfx1 spank
        play sound audrey_generic_ah_4
        with hpunch
        pause 0.3
        show spank audrey ready
        "The third and fourth slaps follow close on the heels of the third."
        "And soon Audrey's squealing and wriggling is really starting to turn me on."
        "So much so that I know just spanking her ass isn't going to cut it anymore."
        "Not with my cock as hard as it is right now."
        hide spank
        show audrey missionary naked audreybedroom nomike
        with fade
        "I need something more satisfying, and I need it quickly."
        menu:
            "Fuck Audrey's pussy":
                "With Audrey's legs hiked up pretty high, I can already see my prize quite clearly."
                "And ever glimpse of her neat little pussy I get makes me even more sure that I want it."
                "So with my mind made up, I set about getting my hands on it."
                scene bg black
                show audrey missionary audreybedroom naked
                with fade
                call check_condom_usage (audrey, 180) from _call_check_condom_usage_171
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show audrey missionary audreybedroom condom
                "Laying atop Audrey, I make sure to aim my cock straight at the target I've chosen."
                "And she does nothing to keep me from beginning my efforts to claim my prize straight away."
                "In fact Audrey does nothing but lie there, unresisting and totally open to letting me have my way with her."
                "I swear that I can see a certain sparkle in her eyes as I start to stroke her pussy with the shaft of my cock too."
                "A look that tells me while she's keeping as quiet as possible, she's also thrilled to see what I have in store for her."
                "That she's getting off on the act of putting herself completely in my hands and offering no resistance whatsoever."
                "In turn that's giving me a similar kind of thrill too, making me almost painfully hard."
                "Which is why it comes as some relief to feel just how wet Audrey already is down there."
                "And the way that she sighs and moans as we make contact below is music to my ears."
                "I was already pretty certain that she'd totally submitted herself to me by now."
                show audrey missionary vaginal pain at startle(0.05,-10)
                play sexsfx1 slide_in
                play sound audrey_generic_oh_3
                "But now I'm simply amazed at the sensation of my cock simply sliding straight into her."
                "I can't remember the last time I made love to a woman and didn't have to work hard to get inside of her."
                "Yet here's Audrey, literally opening to me like a flower to the sun."
                "She nods eagerly as the head disappears into her and the shaft follows on behind it."
                "All I can do is keep right on moving forwards, amazed at the sensations I'm feeling."
                "Because once I'm all the way in there, I realise that the softness is on the outside only."
                "Now I can feel the walls of Audrey's vagina around my, the sensation is totally different."
                "On the inside she's firm, almost tight around the shaft of my cock."
                "But far from being uncomfortable, I find the feeling of it instantly compelling."
                "It's like Audrey's unconsciously doing all that she can to cling onto me."
                "Her body manifesting the desire that she has for me and refusing to let go."
                "Still I manage to begin moving inside of her despite all of this."
                show audrey missionary vaginal at startle(0.1,-10)
                "Slowly starting to pull back and the thrust forwards."
                "Making sure to move with all the caution I can manage on the first swing."
                show audrey missionary vaginal at startle(0.1,-10)
                "But then gaining speed as soon as the second one is underway as my confidence grows."
                show audrey missionary vaginal at startle(0.1,-10)
                "And by the time I'm doing the third, it doesn't feel like anything on earth could stop me."
                "Audrey seems more than happy to simply lie back and take everything I have to give her."
                play sexsfx1 fuck_calm loop
                show audrey missionary vaginal at startle(0.75,-10)
                pause 0.2
                show audrey missionary vaginal at startle(0.75,-10)
                "Body rocking under me as I move in and out, burying myself in her and then pulling out again."
                "And I'm already assuming that she's simply going to surrender herself to me."
                "To offer me her body from now until the moment that what we're doing is over."
                show audrey missionary vaginal at startle(0.75,-10)
                pause 0.2
                show audrey missionary vaginal at startle(0.75,-10)
                "Which is why it comes as a surprise when her arms begin to move a moment later."
                "Without saying a word, Audrey reaches up with both hands."
                "And then she takes a hold of my wrists, beginning to move my arms."
                "I'm so stunned and unprepared for the move that I don't do a thing to stop her."
                show audrey missionary choke
                play sound audrey_moans_gagged loop
                "Which means that she's able to place my hands exactly where she wants them."
                "And that seems to be around her own throat!"
                "Part of me wants to pull them away the moment that I realise what Audrey's doing."
                "But the moment I try to do so, she shakes her head vigorously and holds on more tightly than ever."
                "Truth be told, I'm kind of a stranger to this type of thing in the bedroom."
                "Well, I'm a stranger to choking people in general!"
                "But Audrey seem to be insistent on me doing it to her here and now."
                "So I nod and begin to tighten my grip around her throat."
                "Almost the same moment my fingers close upon it, Audrey lets out a desperate whimper."
                "Obviously I make damn sure that I'm not actually going to strangle her for real."
                "But I can see how even the slightest pressure I apply sends a thrill coursing through her."
                show audrey missionary vaginal pleasure
                play sexsfx1 fuck_moderate loop
                "Audrey's face flushes red and her eyes go wide as she looks up at me."
                show audrey missionary vaginal at startle(0.75,-10)
                pause 0.2
                show audrey missionary vaginal at startle(0.75,-10)
                "And in that moment I begin to get a sense of what she's getting out of this."
                "How the danger and the flirting with it can be so exciting."
                "And trust me, the manifestation of that livens things up for me too."
                show audrey missionary vaginal at startle(0.05,-10)
                pause 0.2
                show audrey missionary vaginal at startle(0.05,-10)
                pause 0.2
                show audrey missionary vaginal at startle(0.05,-10)
                "Within moments, Audrey is writing and wriggling beneath me like never before."
                "Wrapping her legs around me as she holds on and pulls me closer than ever."
                "I swear that I can even feel the muscles around my cock clenching more tightly too!"
                play sexsfx1 fuck_speed loop
                show audrey missionary vaginal at startle(0.05,-10)
                pause 0.15
                show audrey missionary vaginal at startle(0.05,-10)
                pause 0.15
                show audrey missionary vaginal at startle(0.05,-10)
                "As I watch the look on her face and feel the movement of her body, something else becomes clear."
                "That's the fact Audrey's going to cum any moment now."
                show audrey missionary vaginal at startle(0.05,-10)
                pause 0.15
                show audrey missionary vaginal at startle(0.05,-10)
                pause 0.15
                show audrey missionary vaginal at startle(0.05,-10)
                "And at the rate she's going, she's gonna take me with her when she does!"
                call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_307
                if _return == "vaginal_condom":
                    show audrey missionary -choke at startle(0.05,-10)
                    "Releasing my grip, I lean back, secure in the knowledge we chose to use a condom."
                    "Which means that I can simply relax and let nature take it's course."
                    "A moment later I feel it happening, and then I can't do a thing to stop it."
                    show audrey missionary vaginal ahegao condom with hpunch
                    play sexsfx1 final_thrust
                    play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    "I lose it as I'm all the way inside of Audrey, filling her with all I have to give."
                    with hpunch
                    "All the while she writhes on the bed beneath me, helpless in the throes of her own orgasm."
                elif _return == "vaginal_outside":
                    show audrey missionary -choke at startle(0.05,-10)
                    "Releasing my grip, I lean back, letting the motion pull my cock out of Audrey."
                    show audrey missionary ahegao with hpunch
                    "She writhes on the bed beneath me, already helpless in the throes of her own orgasm."
                    with hpunch
                    "But the sensation of me pulling out only seems to add to it all, making her eyes roll back into her head."
                    play sexsfx1 pull_out
                    play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    if CONDOM:
                        show audrey missionary -vaginal condom cum with hpunch
                        "All of this happens while I gasp and twitch myself, shooting my load."
                    else:
                        show audrey missionary -vaginal cum with hpunch
                        "All of this happens while I gasp and twitch myself, shooting my load over Audrey's exposed belly."
                else:
                    show audrey missionary -choke at startle(0.05,-10)
                    "Releasing my grip, I lean back, happy to relax and let nature take it's course."
                    "A moment later I feel it happening, and then I can't do a thing to stop it."
                    show audrey missionary cum ahegao with hpunch
                    play sexsfx1 final_thrust
                    play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    "I lose it as I'm all the way inside of Audrey, filling her with all I have to give."
                    show audrey missionary creampie with hpunch
                    "All the while she writhes on the bed beneath me, helpless in the throes of her own orgasm."
            "Fuck Audrey's ass" if hero.sexperience >= sexperience_min + 5:
                scene bg black
                show audrey missionary audreybedroom naked
                with fade
                "With Audrey's legs hiked up pretty high, I can already see my prize quite clearly."
                "And ever glimpse of her neat little ass I get makes me even more sure that I want it."
                "So with my mind made up, I set about getting my hands on it."
                "Laying atop Audrey, I make sure to aim my cock straight at the target I've chosen."
                "And she does nothing to keep me from beginning my efforts to claim my prize straight away."
                "In fact Audrey does nothing but lie there, unresisting and totally open to letting me have my way with her."
                "I swear that I can see a certain sparkle in her eyes as I start to stroke around the edge of her hole with the shaft of my cock too."
                "A look that tells me while she's keeping as quiet as possible, she's also thrilled to see what I have in store for her."
                "That she's getting off on the act of putting herself completely in my hands and offering no resistance whatsoever."
                "In turn that's giving me a similar kind of thrill too, making me almost painfully hard."
                "Which is why it comes as some relief to feel just how accommodating Audrey already is down there."
                "And the way that she sighs and moans as we make contact below is music to my ears."
                "I was already pretty certain that she'd totally submitted herself to me by now."
                show audrey missionary anal pain at startle(0.05,-10)
                play sexsfx1 slide_in
                play sound audrey_generic_oh_3
                "But now I'm simply amazed at the sensation of my cock simply sliding straight into her."
                "I can't remember the last time I made love to a woman and didn't have to work hard to get inside of her."
                "Yet here's Audrey, literally opening to me like a flower to the sun."
                "She nods eagerly as the head disappears into her and the shaft follows on behind it."
                "All I can do is keep right on moving forwards, amazed at the sensations I'm feeling."
                "Because once I'm all the way in there, I realise that the softness is on the outside only."
                "Now I can feel the walls of Audrey's rear hole around my, the sensation is totally different."
                "On the inside she's firm, almost tight around the shaft of my cock."
                "But far from being uncomfortable, I find the feeling of it instantly compelling."
                "It's like Audrey's unconsciously doing all that she can to cling onto me."
                "Her body manifesting the desire that she has for me and refusing to let go."
                "Still I manage to begin moving inside of her despite all of this."
                show audrey missionary at startle(0.1,-10)
                "Slowly starting to pull back and the thrust forwards."
                "Making sure to move with all the caution I can manage on the first swing."
                show audrey missionary at startle(0.1,-10)
                "But then gaining speed as soon as the second one is underway as my confidence grows."
                show audrey missionary at startle(0.1,-10)
                "And by the time I'm doing the third, it doesn't feel like anything on earth could stop me."
                "Audrey seems more than happy to simply lie back and take everything I have to give her."
                show audrey missionary at startle(0.75,-10)
                pause 0.2
                show audrey missionary at startle(0.75,-10)
                "Body rocking under me as I move in and out, burying myself in her and then pulling out again."
                "And I'm already assuming that she's simply going to surrender herself to me."
                "To offer me her body from now until the moment that what we're doing is over."
                show audrey missionary at startle(0.75,-10)
                pause 0.2
                show audrey missionary anal at startle(0.75,-10)
                "Which is why it comes as a surprise when her arms begin to move a moment later."
                "Without saying a word, Audrey reaches up with both hands."
                "And then she takes a hold of my wrists, beginning to move my arms."
                "I'm so stunned and unprepared for the move that I don't do a thing to stop her."
                show audrey missionary choke
                play sound audrey_moans_gagged loop
                "Which means that she's able to place my hands exactly where she wants them."
                "And that seems to be around her own throat!"
                "Part of me wants to pull them away the moment that I realise what Audrey's doing."
                "But the moment I try to do so, she shakes her head vigorously and holds on more tightly than ever."
                "Truth be told, I'm kind of a stranger to this type of thing in the bedroom."
                "Well, I'm a stranger to choking people in general!"
                "But Audrey seem to be insistent on me doing it to her here and now."
                "So I nod and begin to tighten my grip around her throat."
                "Almost the same moment my fingers close upon it, Audrey lets out a desperate whimper."
                "Obviously I make damn sure that I'm not actually going to strangle her for real."
                "But I can see how even the slightest pressure I apply sends a thrill coursing through her."
                show audrey missionary anal pleasure
                play sexsfx1 fuck_moderate loop
                "Audrey's face flushes red and her eyes go wide as she looks up at me."
                show audrey missionary anal at startle(0.75,-10)
                pause 0.2
                show audrey missionary anal at startle(0.75,-10)
                "And in that moment I begin to get a sense of what she's getting out of this."
                "How the danger and the flirting with it can be so exciting."
                "And trust me, the manifestation of that livens things up for me too."
                show audrey missionary anal at startle(0.05,-10)
                pause 0.2
                show audrey missionary anal at startle(0.05,-10)
                pause 0.2
                show audrey missionary anal at startle(0.05,-10)
                "Within moments, Audrey is writing and wriggling beneath me like never before."
                "Wrapping her legs around me as she holds on and pulls me closer than ever."
                "I swear that I can even feel the muscles around my cock clenching more tightly too!"
                play sexsfx1 fuck_speed loop
                show audrey missionary anal at startle(0.05,-10)
                pause 0.15
                show audrey missionary anal at startle(0.05,-10)
                pause 0.15
                show audrey missionary anal at startle(0.05,-10)
                "As I watch the look on her face and feel the movement of her body, something else becomes clear."
                "That's the fact Audrey's going to cum any moment now."
                show audrey missionary anal at startle(0.05,-10)
                pause 0.15
                show audrey missionary anal at startle(0.05,-10)
                pause 0.15
                show audrey missionary anal at startle(0.05,-10)
                "And at the rate she's going, she's gonna take me with her when she does!"
                call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_308
                if _return == "anal_inside":
                    show audrey missionary -choke at startle(0.05,-10)
                    "Releasing my grip, I lean back, happy to relax and let nature take it's course."
                    "A moment later I feel it happening, and then I can't do a thing to stop it."
                    show audrey missionary cum ahegao with hpunch
                    "I lose it as I'm all the way inside of Audrey's ass, filling her with all I have to give."
                    show audrey missionary creampie with hpunch
                    play sexsfx1 final_thrust
                    play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    "All the while she writhes on the bed beneath me, helpless in the throes of her own orgasm."
                elif _return == "anal_outside":
                    show audrey missionary -choke at startle(0.05,-10)
                    "Releasing my grip, I lean back, letting the motion pull my cock out of Audrey's ass."
                    show audrey missionary ahegao with hpunch
                    "She writhes on the bed beneath me, already helpless in the throes of her own orgasm."
                    play sexsfx1 pop_out
                    play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    show audrey missionary -anal
                    with hpunch
                    "But the sensation of me pulling out only seems to add to it all, making her eyes roll back into her head."
                    show audrey missionary cum with hpunch
                    "All of this happens while I gasp and twitch myself, shooting my load over Audrey's exposed belly."
                $ audrey.flags.anal += 1
    else:

        show audrey at center, zoomAt(1.25, (640, 880)) with fade
        "Even as she asks me the question, Audrey is already getting up off the bed."
        "And as soon as she's standing in front of me, I understand the question was rhetorical in nature."
        "Because she knows exactly what she wants, taking hold of my hand and pulling me to my feet too."
        "As soon as I'm looking her in the eye, I feel Audrey take a firm hold of my cock too."
        show audrey talkative
        audrey.say "Come on, [hero.name]..."
        audrey.say "Do I always need to have hold of a part of you?"
        audrey.say "To lead you where I want us to go?"
        show audrey normal at center, traveling(1.5, 0.5, (640, 1040))
        "Giving my member a pretty hard yank, Audrey makes me close the distance between us."
        mike.say "Argh..."
        mike.say "Audrey, be gentle with me!"
        "But for all of my protesting, it seems like she's not in the mood to listen."
        "Because Audrey keeps right on doing the same thing."
        "Only now she's rubbing the head of my cock hard against her pussy!"
        show audrey mock
        audrey.say "Ah, quit complaining already."
        audrey.say "And get this damn thing inside of me, okay?!?"
        show audrey normal
        menu:
            "Fuck Audrey's pussy":
                "There's just something about the way that Audrey makes that demand of me."
                "Some part of it really serves to strike a spark inside of me."
                "And that spark instantly catches, turning into a flame."
                "I decide that I'm not going to sit back and let her tell me what's going to happen next."
                "And with that in mind, I reach around and grab hold of her buttocks, one in each hand."
                mike.say "Okay, Audrey..."
                mike.say "If that's what you want, that's what you'll get."
                scene bg black
                show audrey cowgirl audreybedroom
                with fade
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show audrey cowgirl audreybedroom condom
                "Now that I have Audrey right where I want her, I don't waste another moment."
                "Holding her tightly, I make sure my cock is between her thighs and I'm close enough."
                "And then I make my move, pulling her closer as I push it upwards at the same time."
                "This means that the head slides straight over the lips of Audrey's pussy."
                "The effect is instant and even more impressive than I'd hoped it would be."
                "As she seems to be electrified by the contact between us, shivering in my arms."
                "Part of me is convinced that this is going to be enough to render her totally helpless."
                "That I'm going to have to find a way to hold her up for the whole time we're making love."
                "But in the next moment, Audrey seems to regain her senses and control of her body."
                "Because she reaches down there again, using a hand to direct traffic."
                "And as I keep on moving the tip against her, she guides it home the whole time."
                "It looks like Audrey's not willing to leave anything up to chance tonight."
                "She wants this every bit as much as I do."
                "And she's determined to see that she gets it too!"
                "The effect of her hand on my manhood doesn't take long to become apparent either."
                "Audrey seems to know exactly where it needs to be, adjusting he movements accordingly."
                "Which is how I feel the sensation of those lips getting ever wetter and softer."
                "In fact it doesn't feel like Audrey's muscles are relaxing to let me enter her."
                "To me it feels more like her pussy is melting at the touch of my cock."
                show audrey cowgirl vaginal pleasure at startle(0.07, -15)
                play sexsfx1 slide_in
                play sound audrey_generic_oh_3
                "And when I feel myself begin to sink into her, she feels like plunging into a warm liquid."
                "Everything is made more intense thanks to the fact I feel compelled to go slowly."
                "As if I'm afraid that moving faster would somehow serve to break the spell of the moment."
                "But the truth is that the feeling of inching a little into Audrey at a time is totally worth it."
                "Every time I sink deeper into her, the sensations become even more overwhelming."
                "So much so that I almost want to stay still and just enjoy them without moving."
                show audrey cowgirl normal
                "The only problem with that is Audrey herself, who has other ideas."
                "Already I swear I can feel the need building inside of her."
                "The knowledge that simply filling her isn't going to be enough."
                show audrey cowgirl pleasure at startle(0.05, -15)
                "Audrey drives this point home by making sure to push me harder as I go deeper."
                "At the same time she's trying to almost ride me, to dictate the pace of it all."
                "So rather than turn this into a battle of wills, I decide to give her what she wants."
                play sexsfx1 fuck_calm loop
                show audrey cowgirl at startle(0.07, -10)
                pause 0.25
                show audrey cowgirl at startle(0.07, -10)
                "Beginning to raise my speed slowly, I do the best I can to match her own intensity."
                "At first I feel like this is going to be one of us against the other."
                show audrey cowgirl at startle(0.07, -10)
                pause 0.25
                show audrey cowgirl at startle(0.07, -10)
                "A contest to see who's going to be the one setting the pace."
                "But to my surprise, Audrey seems to read my intentions as soon as I begin."
                show audrey cowgirl speed at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "And she rises to meet me in the middle, moving to match my own motions."
                "Without the need to speak a word, she almost wraps herself around me."
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "This means that I can easily keep on thrusting in and out of her."
                "And the angle she's at to me means that she can press down with her own weight too."
                "Soon enough all thought of conflict is gone, replaced by carnal cooperation."
                play sexsfx1 fuck_moderate loop
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "All I can feel is the sensation of my cock as it slides in and out of Audrey."
                "At the same time she's got her arms wrapped around me, nodding and urging me on."
                "Any sense of time and place seems to vanish as we're totally consumed by the act."
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "The only thing that exists for us is the need to keep on doing what we're doing."
                "The desperate need to be locked together and expressing our need for each other."
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "So it comes as a shock a moment later to hear the sound of Audrey's voice."
                audrey.say "Ah..."
                audrey.say "[hero.name]..."
                audrey.say "I'm gonna...gonna cum!"
                call cum_reaction (audrey, "vaginal", sexperience_min) from _call_cum_reaction_309
                if _return == "vaginal_condom":
                    show audrey cowgirl ahegao with vpunch
                    "I can almost feel Audrey begin to sag in my arms as her orgasm takes hold."
                    "And the fact we chose to use protection means I can devote all of my attention to her."
                    show audrey cowgirl with vpunch
                    play sexsfx1 final_thrust
                    play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    $ audrey.love += 2
                    "Holding her up as I begin to lose it too, already shooting my load into her."
                    with vpunch
                    "And using the last of my strength to keep her from collapsing into a heap on the floor."
                elif _return == "vaginal_outside":
                    show sexinserts chest audrey zorder 1
                    show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    show audrey cowgirl ahegao
                    with vpunch
                    "Audrey seems to lose the ability to hold herself up at the same moment she starts to cum."
                    show audrey cowgirl -vaginal
                    play sexsfx1 pull_out
                    play sound [audrey_generic_oh_4, audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    "And the situation isn't helped by the fact that I make sure to pull out before it's too late."
                    if CONDOM:
                        show audrey cowgirl cumshot
                        with vpunch
                        "Holding her up as I begin to lose it too, I shoot my load."
                        show audrey cowgirl
                        with vpunch
                    else:
                        show audrey cowgirl cumshot
                        show sexinserts chest audrey cum zorder 1
                        with vpunch
                        "Holding her up as I begin to lose it too, I shoot my load over Audrey's belly."
                        show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                        show audrey cowgirl dickcum onbody
                        with vpunch
                    "At the same time using the last of my strength to keep her from collapsing into a heap on the floor."
                    $ audrey.sub += 1
                else:
                    show audrey cowgirl ahegao with vpunch
                    "I can almost feel Audrey begin to sag in my arms as her orgasm takes hold."
                    "And so, while letting nature run its course, I devote all of my conscious attention to her."
                    show audrey cowgirl creampie with vpunch
                    play sexsfx1 final_thrust
                    play sound [audrey_moans_happy_orgasm_1, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    $ audrey.love += 2
                    "Holding her up as I begin to lose it too, already shooting my load into her."
                    with vpunch
                    "And using the last of my strength to keep her from collapsing into a heap on the floor."
            "Fuck Audrey's ass" if hero.sexperience >= sexperience_min + 5:
                "There's just something about the way that Audrey makes that demand of me."
                "Some part of it really serves to strike a spark inside of me."
                "And that spark instantly catches, turning into a flame."
                "I decide that I'm not going to sit back and let her tell me what's going to happen next."
                "And with that in mind, I reach around and grab hold of her buttocks, one in each hand."
                mike.say "Okay, Audrey..."
                mike.say "If that's what you want, that's what you'll get."
                "Now that I have Audrey right where I want her, I don't waste another moment."
                "Holding her tightly, I make sure my cock is between her thighs and I'm close enough."
                "And then I make my move, pulling her closer as I push it upwards at the same time."
                "This means that the head slides straight into the crevice of Audrey's butt."
                "And then I feel it pressing against the edge of her hole."
                "The effect is instant and even more impressive than I'd hoped it would be."
                "As she seems to be electrified by the contact between us, shivering in my arms."
                "Part of me is convinced that this is going to be enough to render her totally helpless."
                "That I'm going to have to find a way to hold her up for the whole time we're making love."
                "But in the next moment, Audrey seems to regain her senses and control of her body."
                "Because she reaches down there again, using a hand to direct traffic."
                "And as I keep on moving the tip against her, she guides it home the whole time."
                "It looks like Audrey's not willing to leave anything up to chance tonight."
                "She wants this every bit as much as I do."
                "And she's determined to see that she gets it too!"
                "The effect of her hand on my manhood doesn't take long to become apparent either."
                "Audrey seems to know exactly where it needs to be, adjusting he movements accordingly."
                "Which is how I feel the sensation of her hole losing the fight to resist me."
                "In fact it doesn't feel like Audrey's muscles are relaxing to let me enter her."
                "To me it feels more like her hole is melting at the touch of my cock."
                show audrey cowgirl anal
                play sexsfx1 slide_in
                play sound audrey_generic_oh_3
                "And when I feel myself begin to sink into her, she feels like plunging into a warm liquid."
                "Everything is made more intense thanks to the fact I feel compelled to go slowly."
                "As if I'm afraid that moving faster would somehow serve to break the spell of the moment."
                "But the truth is that the feeling of inching a little into Audrey at a time is totally worth it."
                show audrey cowgirl pleasure at startle(0.05, -15)
                "Every time I sink deeper into her, the sensations become even more overwhelming."
                "So much so that I almost want to stay still and just enjoy them without moving."
                "The only problem with that is Audrey herself, who has other ideas."
                "Already I swear I can feel the need building inside of her."
                "The knowledge that simply filling her isn't going to be enough."
                show audrey cowgirl pleasure at startle(0.05, -15)
                "Audrey drives this point home by making sure to push me harder as I go deeper."
                "At the same time she's trying to almost ride me, to dictate the pace of it all."
                "So rather than turn this into a battle of wills, I decide to give her what she wants."
                play sexsfx1 fuck_calm loop
                show audrey cowgirl at startle(0.07, -10)
                pause 0.25
                show audrey cowgirl at startle(0.07, -10)
                "Beginning to raise my speed slowly, I do the best I can to match her own intensity."
                "At first I feel like this is going to be one of us against the other."
                show audrey cowgirl at startle(0.07, -10)
                pause 0.25
                show audrey cowgirl at startle(0.07, -10)
                "A contest to see who's going to be the one setting the pace."
                "But to my surprise, Audrey seems to read my intentions as soon as I begin."
                show audrey cowgirl speed at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "And she rises to meet me in the middle, moving to match my own motions."
                "Without the need to speak a word, she almost wraps herself around me."
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "This means that I can easily keep on thrusting in and out of her."
                "And the angle she's at to me means that she can press down with her own weight too."
                "Soon enough all thought of conflict is gone, replaced by carnal cooperation."
                play sexsfx1 fuck_moderate loop
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "All I can feel is the sensation of my cock as it slides in and out of Audrey."
                "At the same time she's got her arms wrapped around me, nodding and urging me on."
                "Any sense of time and place seems to vanish as we're totally consumed by the act."
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "The only thing that exists for us is the need to keep on doing what we're doing."
                "The desperate need to be locked together and expressing our need for each other."
                show audrey cowgirl at startle(0.05, -10)
                pause 0.2
                show audrey cowgirl at startle(0.05, -10)
                "So it comes as a shock a moment later to hear the sound of Audrey's voice."
                audrey.say "Ah..."
                audrey.say "[hero.name]..."
                audrey.say "I'm gonna...gonna cum!"
                call cum_reaction (audrey, "anal", sexperience_min) from _call_cum_reaction_310
                if _return == "anal_inside":
                    $ audrey.love += 1
                    show audrey cowgirl ahegao with vpunch
                    "I can almost feel Audrey begin to sag in my arms as her orgasm takes hold."
                    "And so, while letting nature run its course, I devote all of my conscious attention to her."
                    $ audrey.love += 1
                    show audrey cowgirl creampie with vpunch
                    play sexsfx1 final_thrust
                    play sound [audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    "Holding her up as I begin to lose it too, already shooting my load into her ass."
                    show audrey cowgirl -speed with vpunch
                    "And using the last of my strength to keep her from collapsing into a heap on the floor."
                elif _return == "anal_outside":
                    show sexinserts chest audrey zorder 1
                    show sexinserts belly audrey as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    show audrey cowgirl ahegao
                    with vpunch
                    "Audrey seems to lose the ability to hold herself up at the same moment she starts to cum."
                    show audrey cowgirl -anal
                    play sexsfx1 pop_out
                    play sound [audrey_generic_oh_4,audrey_moans_pained_orgasm_2, audrey_moans_breathing_fast, audrey_moans_breathing_slow]
                    "And the situation isn't helped by the fact that I make sure to pull out of her ass before it's too late."
                    show audrey cowgirl cumshot
                    show sexinserts chest audrey cum zorder 1
                    with vpunch
                    "Holding her up as I begin to lose it too, I shoot my load over Audrey's belly."
                    $ audrey.sub += 2
                    show sexinserts belly audrey cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    show audrey cowgirl dickcum onbody
                    with vpunch
                    "At the same time using the last of my strength to keep her from collapsing into a heap on the floor."
                $ audrey.flags.anal += 1
    "Once we're both totally satisfied and utterly spent, I collapse onto the bed."
    "And much to my relief, Audrey does the same, landing by my side."
    "Neither of us seems to feel the need to speak another word."
    "Or maybe that's more on account of how we're both incapable of coherent speech right now!"
    "Whatever the case, the prevailing silence is fine by me, and so I keep my mouth shut."
    "Content to simply lie still and bask in the afterglow of what we just did together."
    $ audrey.sexperience += 2
    $ hero.energy -= 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
