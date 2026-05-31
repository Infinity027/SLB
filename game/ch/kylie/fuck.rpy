init python:
    Event(**{
    "name": "kylie_hottub_sex_male",
    "label": "kylie_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(kylie,
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
    "name": "fuck_kylie_jail",
    "display_name": "Conjugal visit",
    "label": "fuck_kylie_jail",
    "conditions": [
        HeroTarget(
            IsRoom("jail"),
            HasStamina(),
            ),
        PersonTarget(kylie,
            IsActive(),
            Not(IsActivity("sleep")),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            IsFlag("agreed_conjugal_visit")
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "kylie_university_blowjob",
    "label": "kylie_university_blowjob",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("classroom"),
            ),
        Or(
            HeroTarget(IsActivity("study")),
            And(
                HeroTarget(IsActivity("study_with")),
                PersonTarget(kylie,
                    IsActive(),
                    ),
                ),
            ),
        PersonTarget(kylie,
            HasRoomTag("uni"),
            MinStat("love", 100),
            MinStat("sub", 50),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "once_week": True,
    "once_day": False,
    "do_once": False,
    "chances": 20,
    "music": "music/roa_music/dreamy.ogg",
    })

label kylie_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "Believe it or not, I actually invited Kylie over for a dip in the hot-tub with nothing else in mind."
    "In my head, it was just a chance for us to kick back and relax, you know?"
    "Us doing something that was chilled out and would let us spend some quality time together."
    "But almost as soon as I walk out of the house in my trunks, I know that Kylie has other ideas."
    "It's clear in the way that she's watching me from the tub and the look in her eyes."
    show kylie swimsuit with dissolve
    "And the way that she beckons me to hurry and join her is enough to confirm it."
    kylie.say "Hurry up and get in here, [hero.name]."
    kylie.say "The water's just right!"
    "I think about sticking to the original plan all the same."
    "But there's just something about the sight of Kylie in her swimsuit."
    "And it's nothing mysterious or hard to explain either."
    "She just looks so damn hot right now - how am I supposed to resist?"
    mike.say "Okay, Kylie."
    mike.say "I'm coming as fast as I can!"
    "Kylie giggles to herself at my choice of words."
    "The sound of it only serves to turn me on even more."
    hide kylie
    show hottub kylie
    with fade
    "And that's all it takes to send me running to join Kylie in the hot-tub."
    "The promise of getting closer to that body of hers makes me as obedient and eager as a puppy!"
    kylie.say "Mmm..."
    kylie.say "This is nice, [hero.name]."
    kylie.say "I always thought we'd have a hot-tub, you and me!"
    "I wrinkle my brows at the odd statement, not quite knowing what to make of it."
    mike.say "Well, Kylie..."
    mike.say "Technically the tub's not mine."
    mike.say "It kind of belongs to the house..."
    "Kylie shakes her head at this, dismissing my words completely."
    kylie.say "Don't be silly, [hero.name]."
    kylie.say "I didn't mean this specific hot-tub."
    kylie.say "I meant the one we're going to have in the future."
    kylie.say "You know, when we're married and settled down together?"
    "I'm not sure where that came from, all the talk about the future."
    "But I guess that Kylie's just joking, trying to make me paranoid or something like that."
    mike.say "Ha, ha..."
    mike.say "Sounds like you've got it all planned out, Kylie!"
    "Kylie smiles at this."
    "But she has an odd look on her face at the same time."
    kylie.say "Of course I do, [hero.name]!"
    kylie.say "I planned our lives together down to the smallest detail!"
    "I laugh again, still thinking that she must be joking around."
    kylie.say "Anyway, that's enough about the future."
    kylie.say "Let's talk about the here and now, okay?"
    kylie.say "Like how handsome you look in those trunks, [hero.name]."
    kylie.say "And how I've never done it in a hot-tub."
    kylie.say "Until now..."
    "Suddenly any thought of the weird stuff that Kylie's been saying vanishes from my mind."
    "And all that I can think of is the way that she's looking at me right now!"
    "Kylie leans back against the edge of the hot-tub, holding my gaze."
    "She parts her legs, and then raises her eyebrows in the most suggestive manner possible."
    "But I don't need to have it spelled out to me with gestures as well as words."
    "And I close the distance between us in a matter of seconds."
    show hottub sex male kylie outside with fade
    "Kylie welcomes me into her arms with another one of her disarming giggles."
    "She wraps her hands around my neck and pulls me in for a kiss."
    "At the same time, my own hands are already pulling down my trunks."
    "Kylie must be able to feel what I'm doing down there and guess why."
    "Because she doesn't hesitate to thrust herself towards me a moment later."
    "She frees one hand to reach down and take hold of my cock."
    call kylie_dick_reactions from _call_kylie_dick_reactions_1
    kylie.say "Ooh, [hero.name]..."
    kylie.say "It's so big and hard!"
    kylie.say "And it's all for me..."
    "All of a sudden, Kylie tightens her grip on the shaft of my cock."
    "There's no warning, and I let out a pained groan, breaking the kiss."
    show hottub sex male kylie inside
    "Before I can utter a single coherent word, she pushes it against the lips of her pussy."
    "And then it's inside of her, and I feel the urge to push harder taking over!"
    "Nothing else seems to matter to me from that point on."
    "All I can think about is getting hold of Kylie and giving her what she wants."
    "Which is what I do with all the strength in my possession."
    "Kylie laughs in delight as she feels me thrusting into her."
    "But as soon as I'm in up to my balls, she begins to moan instead."
    "And it's a sound she keeps up as I move back and forth."
    "Normally I'd think twice about being as forceful as I am right now."
    "I seem to have gone from a standing start to pounding Kylie mere seconds."
    "But her body is absorbing all that I have to give her without complaint."
    "And one look in her eyes is enough to let me know that she's loving every minute of it too!"
    "Kylie seems to be willing me on the whole time, soaking up my efforts like a sponge."
    "I almost feel like laughing to myself as I keep on giving it to Kylie."
    "So this is what happens when I let her have her own way?"
    "And if so, maybe I should give in to all of her demands!"
    "But while Kylie can probably take this all day, I can't keep it up nearly as long..."
    menu:
        "Cum inside":
            "I can hardly forget just how desperate Kylie was to get me inside of her."
            "So I don't worry for a second about losing it inside of her too."
            show hottub sex male cumshot with hpunch
            $ kylie.love += 1
            "And the moment that I shoot my load, I know that I was right."
            with hpunch
            "Kylie clings to me the whole time, refusing to loosen her grip for an instant."
            show hottub sex male ahegao with hpunch
            "Even afterwards she keeps holding on, almost like she's obsessed."
            "I don't think she lets a single drop escape from her pussy!"
        "Pull out":
            "I can recall how eager Kylie was to have me inside of her."
            "But I feel the sudden need to make a gesture of rebellion, no matter how small."
            show hottub sex male kylie outside
            "And so I use the last of my strength to pull out of her, just before I cum."
            "Kylie looks surprised as I do so, then even a little annoyed."
            "But then she seems to wipe that expression off of her face."
            show hottub sex male cumshot with vpunch
            $ kylie.sub += 1
            "Instead she smiles with wicked amusement as I cum on her breasts and belly."
    hide hottub
    show hottub kylie
    with fade
    "Kylie purrs like a cat once it's all over and she's reclining in my arms."
    "She seems to sweet and relaxed at times like this, when she's totally satisfied."
    "And I'm sure that's the way that she'll always be."
    "So long as I'm sure to keep her that way."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ kylie.sexperience += 1
    $ game.active_date.clothes = None
    return

label kylie_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")


    call kylie_fuck_date_intro_male (location) from _call_kylie_fuck_date_intro_male


    call kylie_dick_reactions from _call_kylie_dick_reactions_3


    call kylie_fuck_date_foreplay_male from _call_kylie_fuck_date_foreplay_male


    $ used_ropes = False

    call kylie_fuck_date_choices_male from _call_kylie_fuck_date_choices_male


    call handle_npc_leaving (kylie, _return) from _call_handle_npc_leaving_12
    if _return:
        return


    hide kylie
    call kylie_sleep_date_fuck (location) from _call_kylie_sleep_date_fuck
    return

label kylie_fuck_date_intro_male(location="hero"):
    if not kylie.sexperience:
        scene bg livingroom
        "Even as I open the front door and usher Kylie into the hallway, I'm still not sure that I'm doing the right thing by inviting her back to my place."
        "Don't get me wrong, I'm no prude and it's not like she's twisted my arm to get herself invited over the threshold for some post-date action."
        "But there's always that feeling of her being somehow a little different to most of the girls that I tend to meet and get to take out on dates."
        "It's hard for me to put my finger on the precise word for it, and maybe I'm guilty of overthinking the whole thing."
        "I just keep remembering that she's still Alexis's little sister."
        "Not to mention the crazy stories that she's told me about being into me since she was pretty much a young girl."
        "And when I say crazy, I obviously mean amazing, not insane!"
        show kylie smile with dissolve
        "Standing in the middle of the hallway, Kylie seems to be taking her time to have a good look around the place."
        show kylie blush
        kylie.say "So this is it - the house of [hero.name]!"
        show kylie normal
        "Not prepared in the least for such a strange comment, I try to shrug it off before I become too embarrassed."
        mike.say "Ah...there's no need to talk about it like you're on a tour of the Vatican or something!"
        mike.say "It's just your average rental in the suburbs - nothing to write home about..."
        show kylie smile at startle
        "At this, Kylie spins on her heel and treats me to one of those odd, beguiling smiles that she's capable of pulling off."
        "The kind of smile that I can never tell whether she's being genuine and innocent, or condescending towards me."
        show kylie blush
        kylie.say "But it's not just any house, [hero.name] - it's YOUR house."
        kylie.say "You don't know how often I imagined the place where you'd live..."
        show kylie smile
        mike.say "Yeah, well...I don't live here alone."
        mike.say "I'm pretty sure my housemates are out for most of the night."
        mike.say "But maybe we should be quiet all the same, just in case I'm wrong?"
        show kylie annoyed
        "At the mention of my housemates, Kylie's expression darkens a shade, and her mouth curls into something approaching a frown."
        kylie.say "Oh yeah - Flea and Rasher, right?"
        mike.say "[bree.name] and Sasha, actually..."
        "Sensing that we're in danger of drifting away from the matter at hand, I clear my throat, perhaps a little too loudly."
        mike.say "Ahem, anyway...I don't think that we've got time for the grand tour right now."
        mike.say "So I was thinking that maybe you'd settle for an extended visit to my room instead?"
        "I turn my head towards the stairs, looking upwards and then back at Kylie so as to leave no room for confusion."
        show kylie smile
        "The effect is almost instantaneous, like a switch just flipped inside of her head."
        "All trace of her distaste at the mention of [bree.name] and Sasha seems to vanish."
        "And she becomes suddenly bashful in a manner that makes me want her more than ever."
        show kylie blush
        kylie.say "Oh, [hero.name] - you lure me back to your lair, and then you make me an offer that you know I just can't refuse!"
        kylie.say "This is literally a dream come true!"
        kylie.say "Drinks, a meal and now you're finally going to make a woman out of me - I'm so excited!"
        "Her hand is in mine and I'm leading her down the stairs before something that she just said truly registers in my mind."
        mike.say "Kylie...when you say 'make a woman out of me' - what do you mean, exactly?"
        "Kylie looks a little surprised at this question."
        "Her eyes are telling me that she assumes I should already know the answer."
        kylie.say "Well...I...I saved myself for you, [hero.name]."
        kylie.say "I always knew that you were the only guy for me."
        kylie.say "So I could never have slept with someone else..."
        "Oh shit - I'm sneaking a virgin with a complex about me up to my room with the intention of deflowering her!"
        "I hide my trepidation about what Kylie's just told me behind what I hope is a confident smile."
        "After all, there's nothing illegal about taking the virginity of a girl who's legal."
        "And besides, she's practically begging me to do the act as well."
        "I have to get all of this stuff about her holding a candle for me under control in my own mind."
        "If I don't, then I'm going to blow it with her, big time!"
        mike.say "I'm glad you told me that, Kylie."
        mike.say "It's...pretty romantic of you!"
        "I seem to have managed to say just the right thing, as Kylie beams at me and allows herself to be led straight to my bedroom door."
        "Looking at that face and the body that goes with it, knowing that she's saved herself just for me - it's all I can do to open the door and show her inside."
    scene bg bedroom1
    $ game.room = "bedroom1"
    $ randintro = randint(1, 3)
    if randintro == 1:
        "It's right about now that I remember what a state I left my room in before I rushed out to meet Kylie earlier."
        "There are clothes strewn across the floor and books piled on the desk from when I was last studying up here."
        "Instead of turning on the ceiling light, I dart over and flick the switch for the lamps at the side of my bed."
        "I figure that I can explain this away as mood lighting, and hope that it'll obscure, or at least soften the view of my mess."
        show kylie with dissolve
        "Luckily for me though, it seems that Kylie's too caught up in the moment to either notice or care what state my room's in."
        "She smiles as I turn my back for a moment, trying to at least make the bed for her benefit."
        show kylie underwear with dissolve
        "But when I turn back to face her, I see that she's already unbuttoned her shirt and is sliding in off of her shoulders."
        if not kylie.sexperience:
            "I slump down onto the bed, eyes wide as I see her almost naked to the waist for the first time."
        "And if I hadn't fallen down, she could have tapped me and sent me reeling backwards."
        "Hell - she could have blown me down!"
        "Kylie smiles, clearly delighted with the effect her beginning to strip off has had on me."
        show kylie topless with dissolve
        "Next, she pulls down the straps of her bra, reaching back to unhook it and free her breasts."
        "They stand proud of her chest, large and inviting, and all I can think of doing is burying my head deep between them."
        "Kylie lets her skirt and panties drop next, stepping out of them neatly while rolling down her stockings."
        show kylie naked with dissolve
        "And this is the girl that insists I'm the man of HER dreams?!?"
        "Right now I'd be hard pressed to dream up anything more desirable than what I can see before me!"
        if not kylie.sexperience:
            kylie.say "I guess this is the point where I'm supposed to ask you be gentle with me."
            kylie.say "But I'd really rather you weren't..."
        else:
            kylie.say "Please don't be gentle..."
        "Before I can even manage a response to that, she walks over and starts to pull off my own clothes."
        "I struggle to catch up, and between us I'm as naked as she is within what must be less than a minute."
        call kylie_dick_reactions from _call_kylie_dick_reactions
        "And then she's just standing there before me, waiting for me to make the next move."
    elif randintro == 2:
        "I've had a great time on my date with Kylie tonight."
        "And I'm pretty sure she's feeling the same way too."
        "She's certainly keen to make it back to my place."
        show kylie with dissolve
        "And wastes no time in hustling me to my bedroom once we're back!"
        "Of course I'm more than happy to let Kylie have her way."
        "She shoves me down onto my bed and then hurries to lock the door."
        "And I just watch her as she goes, enjoying the way her body moves."
        "I've never seen curves like those on Kylie, not in the flesh."
        "Everything about them is hypnotic, not to mention arousing in the extreme!"
        "I'm only half aware of the fact I'm getting undressed as she turns to face me."
        show kylie underwear with dissolve
        "And everything else fades into the background as Kylie begins to strip-off too."
        show kylie blush
        kylie.say "You'd better be naked by the time I get over there, [hero.name]."
        kylie.say "Because when I do, you're going to do your manly duty!"
        kylie.say "And I'm not going to be satisfied until you make me scream!"
        show kylie normal
        "The smile on Kylie's face is intense, as is the look in her eyes."
        "But why in the hell shouldn't it be?"
        show kylie topless with dissolve
        "She's a healthy girl with a more than healthy appetite for it."
        "I should just count myself lucky for being the guy that's giving it to her!"
        mike.say "You bet, Kylie!"
        mike.say "I'll be ready!"
        mike.say "You're getting me hard already!"
        "I look down, as if I need to see my own cock to confirm it."
        "But Kylie follows my gaze and I hear her giggle at the sight."
        show kylie blush
        kylie.say "Oh my..."
        kylie.say "Is that down to little old me?"
        kylie.say "Did I get you all excited, [hero.name]?"
        show kylie normal
        "I nod as I lay back on the bed."
        "Kylie's standing by the edge of the mattress."
        show kylie naked with dissolve
        "She's finished stripping off her clothes and now she's completely naked."
        "Hands on her hips, she starts to climb onto the bed and towards me."
        mike.say "Y...yeah, Kylie!"
        mike.say "This is all you!"
        mike.say "I can't help it - you're so hot!"
        "By now, Kylie's crawling towards me."
        "She's getting closer by the second."
        "Her broad hips sway as she comes, her huge breasts swinging beneath her."
        show kylie blush
        kylie.say "Well, I'd better do something about it then, hadn't I?"
        show kylie normal
    else:
        "I've been waiting for this moment all day, the chance to finally close my bedroom door behind me."
        show kylie with dissolve
        "Then to turn around and see Kylie waiting for me, a mischievous smile on her face and hunger in her eyes!"
        "She just looks so good standing there, cascading blonde hair, milky pale skin and curves to die for."
        "And best of all, I know full well that she wants me almost as much as I want her right now!"
        show kylie smile at startle
        "As if reading my mind, Kylie lets out a giggle and begins to strip off her clothes."
        "I feel my mouth go dry as I watch her."
        "I feel my heart start to pound in my chest too."
        "And of course, I feel my cock getting hard inside of my pants!"
        show kylie blush
        kylie.say "Mmm..."
        kylie.say "I love it when you look at me like that, [hero.name]."
        kylie.say "Like I'm the only thing that you want in the whole, wide world."
        "I'm fumbling to pull off my own clothes as she says all of this."
        "Almost tripping over myself as I struggle to keep on watching her too."
        mike.say "Y...yeah, Kylie?"
        mike.say "I want you...pretty bad!"
        "By now Kylie's stripped down to her bra and panties."
        show kylie underwear with dissolve
        "She unhooks the former, letting her beautiful, heavy breasts fall upon her chest."
        show kylie topless with dissolve
        "And then she leans forwards to pull down her panties, holding my eye as she does so."
        show kylie naked with dissolve
        kylie.say "You know what I want, [hero.name]?"
        kylie.say "I want you inside of me!"
        if kylie.sexperience:
            kylie.say "I want your big, hard cock in me!"
        "Kylie begins to back towards the bed, beckoning me to follow her."
        "I'm mostly undressed too, and I begin to follow her like I'm in a trance."
    return

label kylie_fuck_date_foreplay_male:
    $ kylie_cunni = kylie_bj = False
    $ foreplay = kylie.flags.sexperience % 3
    if foreplay == 0:
        call kylie_fuck_date_cunnilingus from _call_kylie_fuck_date_cunnilingus
        $ kylie_cunni = True
    elif foreplay == 1:
        call kylie_fuck_date_blowjob from _call_kylie_fuck_date_blowjob
        $ kylie_bj = True
    menu:
        "Have a taste of her" if not kylie_cunni and kylie.sub >= 15:
            call kylie_fuck_date_cunnilingus from _call_kylie_fuck_date_cunnilingus_1
        "Bring her to her knees" if not kylie_bj and kylie.sub >= 30:
            call kylie_fuck_date_blowjob from _call_kylie_fuck_date_blowjob_1
        "Fuck her":
            pass
    call stop_all_sfx from _call_stop_all_sfx_21

    return _return

label kylie_fuck_date_choices_male:
    "As soon as I reach out and place my hands on Kylie's curvy thighs, intent on pulling her down onto me, I realise I have no idea what position would be best."
    "I guess that I have a couple of seconds at most to make a decision, as Kylie beams down at me, waiting for my next move."
    menu:
        "Missionary":
            call kylie_fuck_date_missionary (0) from _call_kylie_fuck_date_missionary
        "Cowgirl" if hero.sexperience >= 5:
            call kylie_fuck_date_cowgirl (5) from _call_kylie_fuck_date_cowgirl
        "Doggy" if hero.sexperience >= 10:
            call kylie_fuck_date_doggy (10) from _call_kylie_fuck_date_doggy
        "Use ropes" if hero.sexperience >= 15 and "bondage_ropes" in hero.inventory and hero.has_skill("shibari") and kylie.sub >= 75:
            call kylie_fuck_date_bondage (15) from _call_kylie_fuck_date_bondage
            $ used_ropes = True
        "Spoon" if hero.sexperience >= 20:
            call kylie_fuck_date_spoon (20) from _call_kylie_fuck_date_spoon
    call stop_all_sfx from _call_stop_all_sfx_22

    return _return

label kylie_sleep_date_fuck(location="hero"):
    scene bg bedroom1
    show kylie naked blush
    with fade
    if used_ropes:
        "Afterwards I follow Kylie's instructions to get her untied."
        "And as soon as she's free, she flops down onto the bed."
        "The sight reminds me of a puppet with it's strings cut."
        "But I see that Kylie has a smile on her face and a satisfied look in her eyes."
        "She regards me fondly as she rubs the life back into her wrists."
        "And I can't help wondering just what other secrets she's keeping in that head of hers."
        "Who knows, maybe they'll be as fun to discover as this one was!"
    else:
        "Later, as she begins to idly dress herself from the piles of clothes scattered around the room, Kylie looks at me and smiles."
        kylie.say "I feel like the princess in a fairy tale right now!"
        mike.say "Really?"
        mike.say "I guess I should take that as a compliment!"
        "I fall silent for a moment, trying to think of the best way to say what's on my mind."
        mike.say "You were amazing too, Kylie."
        if not kylie.sexperience:
            mike.say "I feel...well, I feel pretty honoured to have been your first..."
            "At this, Kylie smiles sweetly and waves away my comments as if they're nothing at all."
            kylie.say "Oh, that's okay - you were always destined to be the one anyway."
            kylie.say "I just never imagined it'd be so much fun!"
            "I nod and offer her a weak smile in return."
            "Honestly, I had been hoping that our relationship becoming physical might cure Kylie of her more eccentric notions about our story being written in the stars."
            "But it seems that, if anything, it's only served to make her all the more convinced of the fact."
            "Perhaps sensing my slight feelings of unease, Kylie sits by me on the bed and wraps her arms around me."
        show cuddle kylie with fade
        kylie.say "It's okay, [hero.name] - everything's working out just how it's supposed to for us."
        kylie.say "You don't have to worry about anything, because it's just you and me now."
        if not kylie.sexperience:
            kylie.say "Together forever, just how it should be!"
            "What exactly does she mean by that?"
            "All we did was fuck just now!"
            "Sure, I popped her cherry - but that's not like a declaration of marriage!"
            "I think Kylie and I are going to have to sit down and have a long, very frank talk about where we're headed."
            "But I don't think now would be a good time..."
    if game.hour > 19 or game.hour < 6:
        call sleep ("kylie") from _call_sleep_59
        $ game.room = "bedroom1"
    return

label kylie_fuck_date_blowjob:
    if not kylie_bj and not kylie_cunni:
        kylie.say "We're all alone."
        kylie.say "And now I've got you right where I want you!"
        "Kylie speaks with such unadulterated passion that it's almost scary."
        "But that's probably me just failing to be as caught up in the moment."
        "I mean she's a girl and I'm a guy, so that's natural, yeah?"
        mike.say "Ah, okay, Kylie..."
        mike.say "It's not like you have to corner me or anything."
        mike.say "I mean...I'm not going to run away from you!"
        "Kylie pauses for a moment, looking deep into my eyes."
        show kylie happy
        "And then she makes me jump by bursting out laughing."
        "Sure, it's a little freaky to hear a sound like that."
        "But I just chalk it down to her evident enthusiasm."
        kylie.say "You couldn't run away from me if your tried, [hero.name]."
        kylie.say "Because I'd just catch you, and break your legs!"
        "Kylie does that thing where she stares into my eyes again."
        "And for a moment I don't know if she's serious or joking."
        "Then she laughs for a second time, and I can breath again."
        show kylie normal
        kylie.say "Ah, lighten-up, [hero.name]!"
        "With that, Kylie grabs me by the wrist."
        "Her grip is remarkably strong, almost painful."
        "But she doesn't give me time to react at all."
        "And instead, I find myself dragged over to the bed."
        "Once there, Kylie makes it clear she's the one in control."
    hide kylie
    show kylie bj naked
    with fade
    "She gets down on her knees before me, smiling as she glances upwards."
    "Kylie seems to sense the thrill I'm getting from all this."
    "And she responds in kind, her head darting towards my cock."
    "She opens her mouth wide, showing off a set of large, white teeth."
    "Which means that I think for a moment she's actually going to bite me!"
    show kylie bj tongue
    show mouth_insert kylie zorder 1 at zoomAt(1, (860, 140))
    "But at the last second, Kylie's tongue darts out of her mouth."
    "And with it she begins to lick and caress the head of my cock."
    "I can't help letting out a sigh of genuine relief."
    "The sound seems to amuse Kylie, and she redoubles her efforts."
    show kylie bj blow pleasure -tongue
    "I watch in stunned silence as she takes ever more of me into her mouth."
    "Kylie works with a determination that matches her intensity of mood."
    "And I can feel my pleasure mounting with each second that passes."
    "She's far from delicate, moving with speed and power."
    "Yet the experience is that much better for it too."
    "Kylie's head starts to move back and forth, faster and faster."
    "There's no way I'm going to tell her to slow things down."
    "I mean, would she even listen to me if I did?"
    "Soon enough I can feel my cock almost going down Kylie's throat."
    "She's taking me so deep that I daren't move a muscle."
    "All I can do is stand as still as I can manage."
    "That and let her have her way!"
    show kylie bj normal
    "Kylie somehow manages to up the stakes a moment later."
    "Her tongue wraps itself around the shaft."
    "And it feels like the thing has a mind of it's own!"
    "I feel the pressure increase as she squeezes me."
    "Then there's the sudden sensation of release."
    "And I know that I'm about to cum!"
    menu:
        "Facial":
            "I feel like I don't have a hope of pulling my cock out of Kylie's mouth."
            "Which is why it comes as such a surprise to feel her making it happen herself!"
            show kylie bj out
            "Kylie pulls herself off me in the same manner she swallowed it to begin with."
            "Swiftly and without stopping along the way, she drags my cock from her mouth."
            show kylie bj cumshot with vpunch
            "And she manages it just in time to have me shoot my load straight into her face!"
            with vpunch
            "But rather than flinch, Kylie takes it with a smile, eyes wide open."
            show kylie bj -cumshot dickcum cum onface with vpunch
            $ kylie.love += 1
            $ kylie.sub += 2
            "I watch as the cum rains down on her forehead, nose and cheeks."
            show kylie bj tongue
            show mouth_insert kylie cum
            "Some even lands on her tongue and drips from her chin too."
            "And all the time she looks up at me."
            "Her eyes telling me that she's loving every moment."
        "Swallow":
            "I feel like I don't have a hope of pulling my cock out of Kylie's mouth."
            "But then it's not like she seems to be letting go of me either!"
            show kylie bj cumshot surprised
            show mouth_insert kylie cum
            with vpunch
            "Kylie keeps on sucking away at my cock until the moment I lose it."
            with vpunch
            "And then she doesn't miss a beat as she gulps down every last drop!"
            show kylie bj pleasure with vpunch
            $ kylie.love += 2
            $ kylie.sub += 1
            "I'm expecting her to cough or gag as she does so."
            "But Kylie doesn't miss a beat, breathing through her nose the whole time."
            show kylie bj normal -cumshot out dickcum tongue
            show mouth_insert kylie -cum
            "I watch in stunned silence as she mops up all I have to give."
            "And all the time she looks up at me."
            "Her eyes telling me that she's loving every moment."
    hide mouth_insert
    return

label kylie_fuck_date_cunnilingus:
    if not kylie_cunni and not kylie_bj:
        "Still smiling, Kylie sits herself down on the edge of the bed."
        "Then she spreads her legs apart and beckons to me with her finger."
        kylie.say "Here it is, [hero.name]."
        kylie.say "Come and get it!"
        "I can't help smiling as I kneel down and get into position."
        show kylie cunnilingus with fade
        "Part of me wants to stand back and admire Kylie for a little longer."
        "To take in the impressive curves of her body and her cute face."
        "But I've been given a job to do, and an important one at that."
        "So I comfort myself with admiring what I can see between her legs instead."
        "For a start, the legs themselves are something, with those thighs like pillows."
        "But they're not as special as the sight of Kylie's neat little pussy."
        "There it is, nestled between her thighs, just waiting for me!"
        "I catch the scent of it just before I'm close enough to touch it."
        "Musky and sweet, it almost makes my mouth water in anticipation."
    "As if reacting in sympathy, I see that Kylie's lips are getting wet too."
    hide kylie
    show kylie cunnilingus middle
    "Not wanting to wait another moment, I start to lick around the edges."
    "I go slowly, wanting to make the experience last."
    "And Kylie seems to sense this, gasping and making sounds of approval."
    "Soon enough I'm tracing the lines between her folds with my tongue."
    "Marvelling at the way she tastes and how she makes my lips tingle."
    "I feel like I should be taking my time, spinning this out."
    "But part of me just wants to forget all that and go for it."
    show kylie cunnilingus up pleasure handjob
    "And pretty soon it seems to win out, as I push my tongue in deeper."
    "Kylie moans at the sensation, and she begins to squeeze me with her thighs."
    "They're wonderfully soft, pressing and melding into me like pillows"
    "Right now I feel like I have Kylie in the palm of my hand."
    "I could do pretty much anything I like to her..."
    menu:
        "Use my tongue":
            show kylie cunnilingus down
            "But all I want to do right now is keep on working her with my tongue."
            "Seriously, Kylie's filling all of my senses right now."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "All I can feel and taste is her pussy."
            "All I can hear is the sound of her moaning with pleasure."
            "And I'm practically pinned in place by the weight of her thighs."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "But there's nowhere else that I'd rather be!"
            "So I do the best I can to use all of my mouth to please her."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            pause 0.1
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "My tongue is as deep into her pussy as it can go."
            "I use it to explore the soft cave inside of her."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            pause 0.1
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "At the same time, my lips are amongst the outer folds."
            "I honestly feel like I'm French kissing her pussy!"
        "Finger her ass" if hero.sexperience >= 30:
            show kylie cunnilingus down
            "And did I already mention how much I like those generous thighs Kylie has?"
            "I also like the buttocks at the top of them almost as much - maybe even more!"
            "Somehow I manage to pull one of my hands out from under Kylie's thigh."
            "Then I use it to reach around and caress her butt."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "I don't think she notices at first, too wrapped up in what my tongue's doing."
            show kylie cunnilingus middle finger anal
            "But she certainly notices when I push a finger between her buttocks and into her ass."
            "I can't hear what Kylie's actually saying right now."
            "The padding of her thighs means my ears are never going to pick it up."
            "What I do know is that she seems to be enjoying the sensation."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            pause 0.1
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "I push my tongue deeper into her pussy at the same time."
            "And a wicked part of me wonders if the two might meet up in there."
            "If my finger and tongue might actually be able to feel each other!"
        "Use the dildo" if hero.has_item("dildo") and hero.sexperience >= 15:
            show kylie cunnilingus down
            "Somehow I manage to pull one of my arms out from under Kylie's thigh."
            "And then I use it to root around under the bed."
            "I'm searching for a certain something that I know is down there."
            "And when my fingers brush what I know is a dildo, I grab hold of it."
            if randint(0, 1) == 0:
                show kylie cunnilingus dildo vaginal middle
                "Kylie's still out of it when I begin to stroke it against the lips of her pussy."
            else:
                show kylie cunnilingus dildo anal middle
                "Kylie's still out of it when I begin to stroke it against her ass."
            "In fact, I'm not sure she even notices until I actually push it inside of her."
            "But when I do, the change in her is instant and dramatic."
            "Where before she was moaning, now I can tell that Kylie's crying out."
            "And suddenly her thighs are wrapped even more tightly around my head."
            "This means it's lucky for me that I don't have my lips against her pussy."
            "Otherwise Kylie might have smothered me in an instant!"
            "As soon as I recover myself, I keep right on with the dildo."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "But that doesn't mean my tongue and lips are out of the game."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            pause 0.1
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "I use those to tickle and tease the edges of Kylie's pussy."
            "All of which only serves to add to the sounds she's making."
        "Use the anal beads" if hero.has_item("anal_beads") and hero.sexperience >= 15:
            show kylie cunnilingus down
            "Somehow I manage to pull one of my arms out from under Kylie's thigh."
            "And then I use it to root around under the bed."
            "I'm searching for a certain something that I know is down there."
            "And when my fingers brush what I know is a string of anal beads, I grab hold of it."
            "Then I use the same hand to reach around and caress her butt."
            show kylie cunnilingus beads anal middle
            "I don't think she notices at first, until I push the first bead into her."
            "I can't hear what Kylie's actually saying right now."
            "The padding of her thighs means my ears are never going to pick it up."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "What I do know is that she seems to be enjoying the sensation."
            "Because she gets louder with each bead I push into her ass."
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            pause 0.1
            show kylie cunnilingus middle
            pause 0.1
            show kylie cunnilingus up
            pause 0.1
            show kylie cunnilingus down
            "I keep on working away at her with my tongue too."
            "Pushing Kylie on as I push the last of the beads into her."
            "And then I wait a moment, letting her get used to the feeling."
            "That done, I yank the beads back out again without a second's warning."
    show kylie cunnilingus middle
    pause 0.1
    show kylie cunnilingus up
    pause 0.1
    show kylie cunnilingus down
    pause 0.1
    show kylie cunnilingus middle
    pause 0.1
    show kylie cunnilingus up
    pause 0.1
    show kylie cunnilingus down
    "Kylie's cries get louder and louder."
    show kylie cunnilingus down ahegao squirt with vpunch
    "Until, all of a sudden, they come to an abrupt end."
    with vpunch
    "A moment later there's a thud on the mattress."
    show kylie cunnilingus pleasure -squirt
    "I drag my head up from between her legs, fearing the worst."
    "But then I see that Kylie's collapsed backwards onto the bed."
    "Looks like I managed to make her cum, and it was almost too much for her!"
    "She lies there, eyes closed and a satisfied smile on her face."
    "And the only sound she makes is an exhausted panting."
    return

label kylie_fuck_date_missionary(sexperience_min):
    hide kylie
    scene kylie missionary
    with fade
    if not kylie.sexperience:
        "As this is her first time, I want to ease Kylie into it, and be able to do most of the work myself."
    "I gently pull her down onto the bed and don't stop until she's laid flat on her back."
    "Then I straddle her, pushing her thighs apart so that she's laid bare and vulnerable before me."
    "Kylie smiles up at me, her eyes full of anticipation and looking so innocent that it's almost distracting."
    "Maybe I should have thought of trying some kind of foreplay before getting to this point."
    "But from the way that even the subdued light in the room is making Kylie's neat little pussy glisten, I don't think it'll be an issue."
    call check_condom_usage (kylie, love=50) from _call_check_condom_usage_68
    if _return == False:
        return "leave_without_gain"
    scene kylie missionary
    scene kylie missionary mike
    if CONDOM:
        show kylie missionary mike condom
    "Lowering myself onto her, I guide my cock between her legs with one hand while holding myself up with the other by her head."
    show kylie missionary vaginal closed
    if not kylie.sexperience:
        "Kylie wraps her legs around me as I begin to push inside of her, only making it a short way before I feel the obstruction of her hymen."
        "Now here comes the tricky part."
        "I may have more experience in the bedroom than Kylie, but I confess this is the first time that I've had to deal with a hymen."
        "I know that I have to break through it, but my instinct is not to hurt Kylie too much if I can avoid it."
        show kylie missionary vaginal closed with dissolve
        kylie.say "Ah...shit..."
        "I glance up at her, worried that she's in too much pain as the head of my cock presses against the natural seal inside of her pussy."
        "But she bites her lip and nods vigorously, urging me to go on and ignore her cries of pain."
        show kylie missionary vaginal closed blood with dissolve
        "So I push on, soon feeling the sensation of something tearing within Kylie's body."
    else:
        "Kylie wraps her legs around me as I begin to push inside of her."
        "But she bites her lip and nods vigorously, urging me to go on."
        "So I push on, soon feeling the sensation of something wet and silky pussy around my cock."
    show kylie missionary vaginal ahegao
    kylie.say "Oh god...oh...god..."
    kylie.say "[hero.name]...I can feel you..."
    kylie.say "You're inside of me...for real!"
    "Suddenly I feel Kylie clamp her legs around me, pulling me closer to her."
    "My belly is pressed against hers, my chest against her large breasts."
    "And if that's what she wants, then I'm more than willing to oblige her."
    "I begin to thrust in and out of Kylie then, giving her all of my attention and energy."
    "Sure, I've fucked girls plenty of times in the past."
    if not kylie.sexperience:
        "But never while knowing for certain that I was the first guy to put his cock inside of them."
    else:
        "But never while knowing for certain that I was the only guy to ever put his cock inside of them."
    "That thought turns the act of fucking Kylie from an incredible lay into a truly memorable experience."
    if not kylie.sexperience:
        "And the fact that every move she makes and sound that comes out of her mouth is new only serves to make it more so."
    else:
        "And the fact that every move she makes and sound that comes out of her mouth is mine alone only serves to make it more so."
    show kylie missionary vaginal closed
    "I'm actually making her dreams come true right now!"
    "And maybe it's that very thought that makes me realise that I'm about to cum myself..."
    "My muscles stiffen and I thrust my cock as deeply into Kylie's pussy as I can manage."
    show kylie missionary vaginal xray ahegao with vpunch
    "She groans in anticipation, knowing that she's about to make me cum."
    call cum_reaction (kylie, 'vaginal', sexperience_min) from _call_cum_reaction_99
    if _return == "vaginal_outside":
        show kylie missionary mike -vaginal -xray
        show sexinserts chest kylie zorder 1 at center, zoomAt(1, (700, 770))
        show sexinserts belly kylie as bellycum zorder 2 at center, zoomAt(1, (-140, 990))
        "I manage to pull my cock out of Kylie no more than a second before I shower her with cum."
        show kylie missionary mike cum
        show sexinserts chest kylie cum zorder 1 at center, zoomAt(1, (700, 770))
        show sexinserts belly kylie cum as bellycum zorder 2 at center, zoomAt(1, (-140, 990))
        with vpunch
        "She yelps in surprise, both at the sensation and the spattering she gets straight afterwards."
        show kylie missionary mike -cum bellycum with vpunch
        "But from the way she tried to cling to me and the look of melancholy in her eyes, I can't help thinking she was disappointed that I didn't cum inside of her just now."
        hide sexinserts
        hide bellycum
    elif _return == "vaginal_condom":
        show kylie missionary vaginal condom xray
        with vpunch
        "The effects of me going off are enough to make Kylie cum a few moments later, adding a new dimension to her cries."
        with vpunch
        "But even though I've supposedly made her dreams come true by making love to her just now, I can see that there's a hint of dissatisfaction in her eyes."
        "I can't understand what could be upsetting her, and I don't want to ruin the moment by prying, so I simply try to forget it."
    else:
        if not kylie.sexperience:
            "I didn't wear protection because I wanted the experience to be as natural as possible for Kylie her first time."
        "I push in as deep as possible and feel myself cum mere moments later."
        show kylie missionary vaginal ahegao cum xray with vpunch
        $ kylie.impregnate()
        with vpunch
        "The look on Kylie's face as she realises what I've done is simply ecstatic, beaming at the sensation filling her insides as she rides me to the very last."
    return

label kylie_fuck_date_cowgirl(sexperience_min):
    hide kylie

    if not kylie.sexperience:
        "It might be her first time, but that doesn't mean things have to be boring for Kylie or myself."
    "I take hold of Kylie's hands and guide her onto the bed, making her climb atop me as she comes."
    "Once she's straddling my thighs, I bring her to a halt, my erect cock mere inches from the lips of her pussy."
    "Kylie eyes it with what I can only describe as hunger, and she fingers herself down there in anticipation."
    "Any thought of her needing foreplay leaves my head when I see how slick and slippery this makes her fingertips."
    "I pull her forwards the last little bit of the way and have her raise herself up a little."
    call check_condom_usage (kylie, love=50) from _call_check_condom_usage_69
    if _return == False:
        return "leave_without_gain"
    show kylie cowgirl vaginal
    if CONDOM:
        show kylie cowgirl condom
    "Just enough so that the head of my cock is pressing on her pussy."
    kylie.say "Ooh...fuck..."
    "I take a firmer hold of her hands, both to reassure her and keep her from pulling away."
    if not kylie.sexperience:
        mike.say "It'll only hurt a little to begin with, trust me."
        "Kylie nods, biting her lip against the pain as her own weight and gravity take over."
        "I feel the sensation of her hymen against the head of my cock, and then something gives way."

    "And she literally sinks down onto me, casting her head back from the intensity of the experience."
    "Kylie doesn't stop until her groin meets mine, putting the palms of her hands on my belly, as though afraid of sinking further still."
    "I find myself looking up into her eyes, wide and full of emotion."
    show kylie cowgirl ahegao
    kylie.say "You're...you're inside of me, [hero.name]!"
    kylie.say "I can feel you...like...like you're a part of me..."
    kylie.say "Please...please fuck me!"
    "With my hands all over her, caressing every inch of her sweat-slick skin that I can reach, I'm more than happy to oblige."
    "Holding Kylie just below her breasts, I begin to thrust in and out of her, using the weight of her own body to add more force to each movement."
    "I can't believe that I'm actually making a girl's dreams come true by doing this!"
    "And it seems totally crazy that each sigh and moan that Kylie lets out is a sign that she's getting what she's always desired."
    "I always thought that granting someone's fondest wish would be much harder work and far less pleasant of an experience."
    if not kylie.sexperience:
        "I just hope that her first time riding a cock is as memorable as she always hoped it would be."
    "But now, with her blonde locks flying and her breasts bouncing, Kylie's about to make me cum..."
    "My muscles stiffen and I thrust my cock as deeply into Kylie's pussy as I can manage."
    "She groans in anticipation, knowing that she's about to make me cum."
    call cum_reaction (kylie, 'vaginal', sexperience_min) from _call_cum_reaction_100
    if _return == "vaginal_outside":
        show sexinserts chest kylie zorder 1 at center, zoomAt(1, (700, 770))
        show sexinserts belly kylie as bellycum zorder 2 at center, zoomAt(1, (-140, 990))
        "I manage to pull my cock out of Kylie no more than a second before I shower her with cum."
        show kylie cowgirl hard cumshot
        show sexinserts chest kylie cum zorder 1 at center, zoomAt(1, (700, 770))
        show sexinserts belly kylie cum as bellycum zorder 2 at center, zoomAt(1, (-140, 990))
        with vpunch
        "She yelps in surprise, both at the sensation and the spattering she gets straight afterwards."
        with vpunch
        "But from the way she tried to cling to me and the look of melancholy in her eyes, I can't help thinking she was disappointed that I didn't cum inside of her just now."
        hide sexinserts
        hide bellycum
    elif _return == "vaginal_condom":
        with vpunch
        "The effects of me going off are enough to make Kylie cum a few moments later, adding a new dimension to her cries."
        with vpunch
        "But even though I've supposedly made her dreams come true by making love to her just now, I can see that there's a hint of dissatisfaction in her eyes."
        "I can't understand what could be upsetting her, and I don't want to ruin the moment by prying, so I simply try to forget it."
    else:
        if not kylie.sexperience:
            "I didn't wear protection because I wanted the experience to be as natural as possible for Kylie her first time."
        show kylie cowgirl vaginal creampie with vpunch
        $ kylie.impregnate()
        "I push in as deep as possible and feel myself cum mere moments later."
        with vpunch
        "The look on Kylie's face as she realises what I've done is simply ecstatic, beaming at the sensation filling her insides as she rides me to the very last."
    return

label kylie_fuck_date_doggy(sexperience_min):
    if kylie.sexperience and kylie.sub >= 90 and kylie.sexperience % 3 == 1:
        mike.say "On the bed...now!"
        "Recognising the tone of my voice as one of command, Kylie hurries to obey."
        "I watch silently as she crawls on the bed and then remaining perfectly still on her hands and knees."
        show kylie doggy with fade
        "Rather than getting up and taking advantage of her prone position straight away, I regard her for a time in complete silence."
        "While I get off on seeing Kylie's strikingly beautiful body spread out before me like this, the true thrill comes from something infinitely more subtle."
        "And that's watching the sense of anticipation and longing that's building inside of her, becoming greater with every second that passes."
        "I know that Kylie desperately wants me inside of her, has told me it's almost literally a dream come true for her."
        "So keeping her hanging on when she's so achingly close to getting what she wants is something that I get an immense kick out of."
        "I can see how she presented herself out before me, the desire in her eyes, even the way that her pussy is now so wet and slick that it's glistening in the light."
        "Slowly I stand over her, still not sure if her nakedness or expression is what's turning me on more."
        call check_condom_usage (kylie, love=50) from _call_check_condom_usage_70
        if _return == False:
            return "leave_without_gain"
        show kylie doggy mike
        if CONDOM:
            show kylie doggy condom
        "Not pausing to either ask permission or even tell her what I intend to do, I take a firm hold of Kylie's waist."
        "Her eyes widen as she's pulled towards me and her backside is hoisted unceremoniously into the air."
        "From there, I push my weight down onto her thighs, almost folding her in half and bringing my cock to within an inch of her now exposed pussy."
        "I know that she's going to enjoy what I plan to do for her...eventually."
        "But none of that is as important as her learning who's in charge and who takes the orders in our relationship."
        "That's why I give her no warning before I push the head of my cock into her now soaking pussy."
        show kylie doggy vaginal surprised
        "The sound of it going in is made all the more sweet thanks to being accompanied by that of Kylie almost squealing at the sensation."
        "And I simply push harder, Kylie's squeals now turn into a genuine scream."
        "So I push on, enjoying the feeling of her pussy as I listen to her cries become ever more filled with desperate pleasure of her own."
        "Every downward thrust is absorbed by her thighs, buttocks and pussy as though she's enjoying the punishment and eager for more."
        show kylie doggy crazy
        "A small part of me wonders if this is what Kylie imagined when she dreamed of this moment."
        "But I can already see the hunger that being fucked like this is inspiring inside of her."
        "If I've done my job correctly, she'll beg to be taken as roughly as this every time she spreads her legs for me."
        "And the thought of her, wet, willing and obedient is enough to make me lose myself..."
    else:
        show kylie doggy
        if not kylie.sexperience:
            "This might well be Kylie's first time, but there's still a pecking order in our relationship that I'm keen to maintain."
            "With this in mind, I take her hands and get up from the bed myself, guiding her onto it in my place."
        else:
            "I take her hands and get up from the bed myself, guiding her onto it in my place."
        "She obligingly crawls onto it, but when she makes to lie down on her back, I take a firmer hold to keep her on her hands and knees."
        "Rather than being alarmed or annoyed by the fact that I'm asserting myself over her, Kylie merely looks back over her shoulder and smiles."
        "Which I choose to interpret as a silent acceptance of the position in which I've put her and the fact that I'm the one in control here."
        "With her spread and the way this in turn parts her buttocks, it's easy to see that Kylie's not putting on a brave face right now."
        "The lips of her pussy are already wet and glistening in the subdued light of the room."
        call check_condom_usage (kylie, love=50) from _call_check_condom_usage_71
        if _return == False:
            return "leave_without_gain"
        show kylie doggy mike
        if CONDOM:
            show kylie doggy condom
        "I climb onto the bed behind her, letting my cock lead the way and enjoying her reaction when it brushes against her thighs and then goes further still."
        "Putting one hand on her buttocks, I take the time to let the head slide up and down the slick folds, teasing Kylie with every single movement."
        "I can hear her beginning to whimper in anticipation, her body almost shivering at the prospect of what's to come next."
        "But she's a good, obedient girl that knows her place, and she never once opens her mouth to question or demand of me."
        show kylie doggy vaginal surprised
        "When I suddenly dig my fingers into her buttocks and thrust myself into her, those whimpers become actual cries and almost screams."
        if not kylie.sexperience:
            "I feel the resistance of her hymen for no more than mere seconds before it tears away and my cock sinks deeply into her."
        "Kylie's cries become long, almost agonised moans as I allow her no chance to recover."
        if not kylie.sexperience:
            "Instead I fuck her with a vigour that comes from knowing that this is her first time."
            "A vigour that also knows what kind of a lasting impression being taken so hard and fast will leave upon her."
        show kylie doggy crazy
        "Kylie has handfuls of the bedclothes clutched in her hands and her head pushed down into them, drooling into the sheets."
        "When I manage to catch a glimpse of them, her eyes seem to be almost glazed over from the pleasure of being fucked so hard and so fast."
        "I can see her large breasts swaying beneath her and the ripples along her curvaceous thighs as I continue to pound her without mercy."
        "A small part of me can't help worrying that this moment is something that Kylie always told me she'd dreamed about."
        "And I wonder if she saw herself in a position like this when she did so."
        "But then I remember that she's a big girl now, and there's nothing at all to keep her from crying out for me to stop."
        "So while ever she's consenting to all of this by way of her silence, there's nothing at all to keep me from enjoying myself."
        show kylie doggy normal
        "It's then that I manage to catch Kylie's eye, as a glimmer of awareness returns to it for what may only be a brief moment."
        "She looks at me not with anger or fear, but rather with an acceptance of what I'm doing to her that says she'll take all I have to give and more."
        "Knowing that I have her complete submission, I feel a wash of emotion that pushes me over the edge..."
    "My muscles stiffen and I thrust my cock as deeply into Kylie's pussy as I can manage."
    "She groans in anticipation, knowing that she's about to make me cum."
    call cum_reaction (kylie, 'vaginal', sexperience_min) from _call_cum_reaction_101
    if _return == "vaginal_outside":
        "I manage to pull my cock out of Kylie no more than a second before I shower her with cum."
        show kylie doggy -vaginal cumshot with hpunch
        "She yelps in surprise, both at the sensation and the spattering she gets straight afterwards."
        show kylie doggy -cumshot cum onbody with hpunch
        "But from the way she tried to cling to me and the look of melancholy in her eyes, I can't help thinking she was disappointed that I didn't cum inside of her just now."
    elif _return == "vaginal_condom":
        with hpunch
        "The effects of me going off are enough to make Kylie cum a few moments later, adding a new dimension to her cries."
        with hpunch
        "But even though I've supposedly made her dreams come true by making love to her just now, I can see that there's a hint of dissatisfaction in her eyes."
        "I can't understand what could be upsetting her, and I don't want to ruin the moment by prying, so I simply try to forget it."
    else:
        if not kylie.sexperience:
            "I didn't wear protection because I wanted the experience to be as natural as possible for Kylie her first time."
        show kylie doggy vaginal creampie ahegao with hpunch
        $ kylie.impregnate()
        "I push in as deep as possible and feel myself cum mere moments later."
        with hpunch
        "The look on Kylie's face as she realises what I've done is simply ecstatic, beaming at the sensation filling her insides as she rides me to the very last."
    return

label kylie_fuck_date_bondage(sexperience_min):
    "But just as I'm about to reach her, Kylie skips aside."
    "My hands miss her by an inch, and I look up in confusion."
    "Which is when I see that she's holding something in her hands."
    "The way she's slapping it on the palm of one hand makes me think it's a whip."
    "What's Kylie got in mind?"
    "Is she going to use that thing on me?"
    "Because I think I might be into that idea!"
    "But then she stretches it out between her hands, pulling it taught with a snap."
    "And it's now that I see she's actually holding a length of rope."
    "Where in the hell was she hiding that?!?"
    kylie.say "Uh, uh, uh..."
    kylie.say "First you've got to do something for me, [hero.name]."
    kylie.say "I want you to tie me to the bed."
    show kylie happy
    kylie.say "Do that and then I'm all yours, okay?"
    "I look at the rope, then up at Kylie."
    "I didn't know she was into that kind of shit!"
    "But if that's what she wants, then who am I to judge?"
    "Tied up or not, I'm still getting to fuck Kylie!"
    "I nod and take the ropes from Kylie when she offers them to me."
    mike.say "I was never a boy scout, Kylie."
    mike.say "The best I can do is tie my shoelaces!"
    show kylie normal
    kylie.say "Don't worry, [hero.name]."
    kylie.say "I'll talk you through it."
    kylie.say "This isn't the first time I've tied somebody up!"
    "Kylie says this in such a nonchalant way I almost question her about it."
    "But then she turns her back on me, climbing onto the bed."
    "And I'm instantly distracted by the sight of her glorious ass in motion!"
    show taming bondage with fade
    "Over the next few minutes, Kylie gives me a crash course in basic bondage."
    "Once I'm done, I stand back to admire my handiwork."
    show taming bondage ropes
    "Her wrists are bound together above her head."
    "And her legs are spread apart, hoisted into the air."
    "Literally everything is laid bare for me to see."
    "Kylie giggles again and pretends to struggle against the ropes."
    kylie.say "Oh no, [hero.name]..."
    kylie.say "You've tied me up so tight that I'll never escape!"
    kylie.say "Whatever are you going to do to me now?"
    "The smile on Kylie's face is something else."
    "It's equal parts wicked and wanton."
    "And it's turning me on almost as much as her naked body!"
    mike.say "Hmm..."
    mike.say "Now let me see..."
    mike.say "What should I do with you?"
    mike.say "Or should say TO you?"
    "I'm climbing onto the bed as I say this, crawling towards Kylie."
    "She makes a show of squealing in mock alarm and struggling against her bonds."
    "But I can still see the thrill of it all reflected in her eyes."
    "Kylie looks down, biting her lip and I reach her."
    "She really is helpless right now, totally at my mercy."
    show taming bondage mike
    "So what am I going to do with her in such a position?"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kylie.sub >= 50:
            mike.say "My, my..."
            mike.say "What do we have here?"
            "I take hold of Kylie's ass, parting her buttocks."
            "In response, she let's out a squeal of feigned alarm."
            mike.say "Such a sweet little asshole."
            mike.say "Be a shame if someone were to..."
            mike.say "I don't know...maybe stick a big cock into it?"
            "Kylie doesn't say a word to this."
            show taming bondage surprised
            "Instead I see her eyes go wide."
            "And she struggles as best she can to see what I'm doing."
            "But I think the most that she manages to glimpse is the head of my cock."
            "Even then she couldn't have got more than the slightest glimpse."
            "Not before I push it between the cheeks of her ass!"
            show taming bondage shy anal
            "I watch the look on her face as I work it in there."
            "Feeling her muscles try to resist is amazing enough."
            "But watching the way Kylie reacts makes it so much better."
            "Every fraction of an inch that I squeeze in there, her face shows it."
            "Kylie stares up at me as I push ever further into her."
            "I'm more than halfway in by now, getting deeper with every second."
            "And there's nothing she can do to stop me!"
            kylie.say "Oh..."
            kylie.say "Oh my god..."
            kylie.say "My poor little asshole!"
            kylie.say "You fiend, you're SO big!"
            show taming bondage angry
            kylie.say "It's never going to be the same again!"
            "I have to admit, Kylie plays a pretty good damsel in distress!"
            "Her act is so good that it almost instantly spurs me into action."
            "Before I know it, I'm as deep into her ass as I can go."
            "I give it one last thrust, feeling satisfied as I do so."
            show taming bondage shy
            "Kylie wriggles and writhes on my cock, helpless to resist."
            "And then I'm thrusting in and out of her."
            "I move as fast as I possibly can, slamming into her thighs."
            "Kylie's ass feels so tight around my cock right now."
            "I'm gasping from the way it's squeezing me."
            "Kylie closes her eyes and her head falls back."
            "This means that my own eyes are free for the first time."
            "They wander over the form of her body, taking it all in."
            "I watch as Kylie's breasts bounce and giggle on her chest."
            "The sound they're making is almost as loud as me pounding her."
            "Realising that I don't have to hold her up, I reach out with both hands."
            "And almost as soon as I begin to squeeze Kylie's breasts, her head rises up again."
            "But when her eyes open once more, the look in them is distant and confused."
            "Kylie moans and sighs more with every thrust."
            show taming bondage ahegao
            "Sometimes I think she's trying to form actual words."
            "But most of what comes out of her mouth makes no sense."
            "In the moment, I have no idea if she's still putting on an act."
            "For all I know, I could have fucked her ass so hard she's delirious."
            "And the mere thought of that is enough to make me lose it..."
            call cum_reaction (kylie, 'anal', sexperience_min) from _call_cum_reaction_102
            if _return == 'anal_inside':
                "With Kylie helpless to resist me, I can do as I please."
                "And so I choose to keep right on until the very end."
                "Just as I know I'm about to cum, I thrust with all my might."
                show taming bondage creampie with vpunch
                "This is enough to make sure I shoot my load deep inside of Kylie."
                with vpunch
                "Her eyes roll back into her head, and then it flops backwards too."
                with vpunch
                "Kylie groans as I fill her, cumming until it starts to seep out around my cock."
                $ kylie.sub += 1
                $ kylie.love += 2
            elif _return == 'anal_outside':
                "With Kylie helpless to resist me, I can do as I please."
                "And so I choose to pull my cock out before the end."
                show sexinserts chest kylie zorder 1 at center, zoomAt(1, (700, 990))
                show sexinserts belly kylie as bellycum zorder 2 at center, zoomAt(1, (-140, 1040))
                "Kylie's eyes roll back into her head, and then it flops backwards too."
                show taming bondage -anal cumshot with vpunch
                "She groans as I aim it over her helpless form."
                with vpunch
                "But I don't know it she feels it spurt over her a moment later."
                show sexinserts chest kylie cum zorder 1 at center, zoomAt(1, (700, 990))
                show sexinserts belly kylie cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1040))
                with vpunch
                "Hot, sticky white lines appear on Kylie's belly."
                "And then it runs down, over her thighs and onto her pussy."
                hide sexinserts
                hide bellycum
                $ kylie.sub += 2
                $ kylie.love += 1
            $ kylie.flags.anal += 1
        "Fuck her pussy":
            "I could literally do anything I want right now."
            "I could take any of Kylie's holes without even having to try."
            "But there's just something about the idea of her being helpless."
            "It makes me want to keep things simple."
            "Maybe because that way I can better appreciate the situation."
            mike.say "Well hello..."
            mike.say "What's that I see down there?"
            mike.say "Would it happen to be a neat little pussy?"
            "I lean forwards, reaching between Kylie thighs."
            "She struggles to see what I'm doing down there."
            "But the position she's in makes that impossible."
            call check_condom_usage (kylie, love=50) from _call_check_condom_usage_72
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show taming bondage condom
            "Then we're ready to get back into it."
            "I use one hand to stroke the lips of Kylie's pussy."
            "And the other I employ to steer my cock towards its target."
            kylie.say "What are you doing down there?"
            show taming bondage surprised
            kylie.say "Oh, you fiend!"
            "I can't help grinning at the way Kylie's putting on an act."
            "She's hardly a typical damsel in distress most of the time."
            "But the character she's playing right now is pretty sexy."
            mike.say "Can't you feel what I'm doing?"
            mike.say "If you can't, then you soon will!"
            "With that, I push the head of my cock hard against Kylie's pussy."
            "She's already excited and that's making her lips nice and slippery."
            "And there's only a token moment of resistance before she surrenders to me."
            "Then I feel my cock slide smoothly into her."
            show taming bondage vaginal shy
            "So smoothly in fact that I almost sink in as far as I can go."
            "Kylie makes a whimpering sound as I fill her."
            "And she nods her head the whole time."
            kylie.say "Oh..."
            kylie.say "Oh my god..."
            kylie.say "My poor little pussy!"
            kylie.say "You fiend, you're SO big!"
            show taming bondage angry
            kylie.say "It's never going to be the same again!"
            "Chuckling at Kylie's protestations, I get straight to work."
            "There's no need to start slowly and build up speed."
            show taming bondage shy
            "I'm too excited to be able to pace myself like that."
            "And Kylie's already begging for all that I can give her."
            "So almost as soon as I start to move inside her, I'm going as fast as I can."
            "I don't need her to tell me that this is what she wants either."
            "As Kylie keeps on nodding, the cries she makes becoming almost desperate."
            "I'm used to her having a very healthy appetite for sex."
            "But being tied up like this seems to let something out."
            "Like it was hidden inside of her, just waiting to be released."
            "I thought I was the one in charge here."
            "I thought that with Kylie restrained, I'd be setting the pace."
            "But the truth is that I'm doing all I can to satisfy her!"
            "My heart is pounding in my chest and I'm gasping for breath."
            "And yet Kylie's eating up everything that I give her."
            "Finally I feel a change come over Kylie, her body tensing for something."
            "When I realise that she's about to cum, it's with a genuine sense of relief!"
            "But then I feel the same thing happening to me."
            "Kylie's going to take me with her!"
            call cum_reaction (kylie, 'vaginal', sexperience_min) from _call_cum_reaction_103
            if _return == "vaginal_outside":
                "With Kylie helpless to resist me, I can do as I please."
                "And so I choose to pull my cock out before the end."
                show sexinserts chest kylie zorder 1 at center, zoomAt(1, (700, 990))
                show sexinserts belly kylie as bellycum zorder 2 at center, zoomAt(1, (-140, 1040))
                show taming bondage -vaginal
                "Kylie's eyes roll back into her head, and then it flops backwards too."
                show taming bondage ahegao cumshot with vpunch
                "She groans as I aim it over her helpless form."
                with vpunch
                "But I don't know it she feels it spurt over her a moment later."
                show sexinserts chest kylie cum zorder 1 at center, zoomAt(1, (700, 990))
                show sexinserts belly kylie cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1040))
                with vpunch
                "Hot, sticky white lines appear on Kylie's belly."
                "And then it runs down, over her thighs and onto her pussy."
                hide sexinserts
                hide bellycum
                $ kylie.sub += 1
            elif _return == "vaginal_condom":
                "With Kylie helpless to resist me, I can do as I please."
                "And so I choose to keep right on until the very end."
                "After all, we used protection, so why not?"
                "Just as I know I'm about to cum, I thrust with all my might."
                with vpunch
                "This is enough to make sure I shoot my load deep inside of Kylie."
                show taming bondage ahegao with vpunch
                "Her eyes roll back into her head, and then it flops backwards too."
                with vpunch
                "Kylie groans as I fill her, cumming until it starts to seep out around my cock."
                $ kylie.love += 1
            elif _return == "vaginal_inside_pill":
                kylie.say "Don't..."
                kylie.say "Don't stop..."
                kylie.say "I'm...on the...pill!"
                "I mentally thank Kylie for the timely reminder, then keep right on going."
                "Just as I know I'm about to cum, I thrust with all my might."
                show taming bondage ahegao creampie with vpunch
                "This is enough to make sure I shoot my load deep inside of Kylie."
                with vpunch
                "Her eyes roll back into her head, and then it flops backwards too."
                with vpunch
                "Kylie groans as I fill her, cumming until it starts to seep out around my cock."
                $ kylie.love += 2
            elif _return == "vaginal_inside_pregnant":
                kylie.say "Don't..."
                kylie.say "Don't stop..."
                kylie.say "I...can't get...anymore pregnant!"
                "I can't help smiling as I wonder why Kylie thinks I need to be reminded of that fact."
                "She's already carrying around a huge belly, even months before the kid is due!"
                "I shake my head, then keep right on going."
                "Just as I know I'm about to cum, I thrust with all my might."
                show taming bondage ahegao creampie with vpunch
                "This is enough to make sure I shoot my load deep inside of Kylie."
                with vpunch
                "Her eyes roll back into her head, and then it flops backwards too."
                with vpunch
                "Kylie groans as I fill her, cumming until it starts to seep out around my cock."
                $ kylie.love += 2
            elif _return == "vaginal_inside_mad":
                kylie.say "Pull out!"
                show taming bondage angry
                kylie.say "You have to do it now!"
                "The tone of Kylie's voice and the look in her eyes stop me dead."
                "Which is more then enough to make sure I shoot my load deep inside of Kylie."
                kylie.say "NO!"
                kylie.say "Please don't!"
                show taming bondage creampie ahegao with vpunch
                $ kylie.love -= 5
                $ kylie.impregnate()
                "Her eyes roll back into her head, and then it flops backwards too."
                with vpunch
                "Kylie groans as I fill her, cumming until it starts to seep out around my cock."
                with vpunch
                "But all I can think is how badly I just fucked up."
            elif _return == "vaginal_inside_happy":
                "With Kylie helpless to resist me, I can do as I please."
                "But then I remember that we didn't use any protection."
                "Just as I know I'm about to cum, I make to pull out."
                kylie.say "NO!"
                show taming bondage angry
                kylie.say "Please don't!"
                "The tone of Kylie's voice and the look in her eyes stop me dead."
                with vpunch
                "Which is more then enough to make sure I shoot my load deep inside of Kylie."
                with vpunch
                "Her eyes roll back into her head, and then it flops backwards too."
                show taming bondage creampie ahegao with vpunch
                $ kylie.love += 6
                $ kylie.impregnate()
                "Kylie laughs as I fill her, cumming until it starts to seep out around my cock."
                "But all I can think is how badly I just fucked up."

    return

label kylie_fuck_date_spoon(sexperience_min):
    kylie.say "Hmm...how about this..."
    kylie.say "How about I let you put it inside of me, huh?"
    kylie.say "Would you like that?"
    scene kylie spoon with fade
    "Kylie turns so that her back is against my belly as she says this."
    "She nestles herself into me, rubbing her ass into my groin."
    kylie.say "And you can put it wherever you like too!"
    kylie.say "I won't stop you, I promise!"
    "I'm in too much of a tangle to be able to respond to that."
    "Any words coming out of my mouth would just be meaningless babble."
    "So I just put my arms around Kylie and pull her close against me."
    "She sighs happily at my touch, letting me take her weight."
    "And it seems like she's giving herself over to me completely."
    "So the only question now is - what am I going to do with her?"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kylie.sub >= 50:
            "Well, if Kylie seems determined to put me in the driver's seat."
            "So why wouldn't I take full advantage of that offer?"
            "If you get offered a free meal, you ask for the steak, not the soup - right?"
            "That's why I lift Kylie's leg, spreading her thighs wide apart."
            "This means that I can see the neat little hole between her buttocks."
            "Kylie seems to catch on to what's happening as soon as I do this."
            "She lets out a mock gasp of surprise, looking over her shoulder at me."
            kylie.say "Oh, [hero.name]..."
            kylie.say "You naughty boy!"
            kylie.say "Are you going to take advantage of me?"
            kylie.say "Oh my..."
            kylie.say "But I DID promise, didn't I?"
            kylie.say "Just you promise me you'll be gentle!"
            "I can't help grinning as I press the head of my cock against Kylie's ass."
            "I know full well that she's putting on an outrageous act right now."
            "But it's turning me on even more, making me want her like crazy."
            "Kylie keeps on sighing and gasping as I start to push into her."
            "Her muscles are playing along with the act, trying to keep me out."
            "But I'm getting more determined with each moment that passes."
            "And so they can't keep my cock from inching into her ass."
            play sexsfx1 slide_in
            show kylie spoon opened anal
            kylie.say "Oh..."
            kylie.say "My poor little hole!"
            kylie.say "It's never going to be the same again!"
            kylie.say "But...but don't stop now, please!"
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            pause 1
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            kylie.say "Oh...oh shame on me!"
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            pause 1
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            kylie.say "I think I'm starting to like the way it feels!"
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            pause 0.5
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            "As soon as I'm as deep into Kylie as I can go, I change gear."
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            pause 0.5
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            "No longer pushing slowly into her, I begin to move back and forth."
            play sexsfx1 fuck_calm loop
            with hpunch
            "It doesn't take long for me to be thrusting in and out of her."
            "And the effect this has on her is instant and visible."
            show kylie spoon closed
            "Kylie seems to lose the ability to support her own weight."
            "She flops against me, like a sagging doll in my arms."
            "So it looks like I'm really in control now."
            "Like I have Kylie in the palm of my hand."
            "Or on the end of my cock, if you like."
            play sexsfx1 fuck_moderate loop
            "There's nothing quite like what I'm feeling right now."
            "Being inside of Kylie so deep, holding her so close to me."
            "And knowing that she's completely in my power for as long as this lasts."
            "Every time I thrust into her, she seems to surrender just a little more."
            "Until I actually begin to worry that she might be on the verge of passing out!"
            play sexsfx1 fuck_speed loop
            show kylie spoon speed with hpunch
            "But that doesn't stop me keeping right on, from pounding her until the last."
            "I reach around and begin to stroke Kylie's pussy at the same time."
            "It's right there for the taking and glistening wet thanks to her current state."
            "She moans as I slowly push my fingers between the soft lips."
            "The effect is so powerful that it even stirs Kylie into speaking."
            show kylie spoon opened
            kylie.say "Yes..."
            kylie.say "Please..."
            kylie.say "Play with me, [hero.name]..."
            kylie.say "Make me cum!"
            show kylie spoon closed
            "The sound of her voice as she begs me is just too much."
            "I know that Kylie's pleading with me to do it for her."
            "But right now I can't stop myself from cuming too!"
            call cum_reaction (kylie, 'anal', sexperience_min) from _call_cum_reaction_291
            if _return == 'anal_inside':
                "So why in the hell would I even think of pulling out of her now?"
                "Surely the best chance I have of making Kylie cum is to do it inside of her?"
                "And it's not like she's in any kind of position to stop me, is she?"
                "Letting nature take it's course, I make one final thrust into Kylie."
                play sexsfx1 final_thrust
                show kylie spoon opened creampie -speed
                with hpunch
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                with hpunch
                "And that's because I just gave her everything I have to give."
                with hpunch
                "Kylie's ass quivers and her muscles twitch as I fill her up."
                "She pants with exhaustion as the cum starts to seep out of her ass."
                $ kylie.sub += 1
                $ kylie.love += 2
            elif _return == 'anal_outside':
                "Maybe what Kylie needs to push her over the edge is a sudden surprise?"
                play sexsfx1 slide_out
                pause 0.5
                play sexsfx1 pop_out
                show kylie spoon -speed -anal
                "And to make that happen, I yank my cock out of her ass without warning."
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                "And that's because Kylie starts to cum a moment before I do myself."
                with hpunch
                "She twitches and quivers in my arms, her orgasm taking over her entire body."
                show kylie spoon -anal cumshot
                with hpunch
                "At the same time I shoot my load up Kylie's back in thick spurts."
                with hpunch
                "It runs downwards, covering the both of us as she squirms against me."
                "Then she collapses into my arms, panting with exhaustion."
                $ kylie.sub += 2
                $ kylie.love += 1
            $ kylie.flags.anal += 1
        "Fuck her pussy":
            "I lift Kylie's leg, spreading her thighs wide apart."
            "This gives me a perfect view of everything on offer down there."
            "Her ass looks so inviting, just there for the taking."
            "But then I lay eyes on her pussy, already slick and glistening."
            "And that's it, all thought of Kylie's ass vanishes from my mind."
            "It's got to be her pussy, and nothing else will do!"
            call check_condom_usage (kylie, love=50) from _call_check_condom_usage_153
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kylie spoon condom
            "Now that we're finally ready, Kylie can't keep a lid on her impatience."
            "She reaches back, taking a firm hold of my cock and aims it at her pussy."
            kylie.say "Come on, [hero.name]!"
            kylie.say "Let's get this thing started already!"
            kylie.say "Put inside of me, before I lose it!"
            "Well, how can a guy refuse a request like that?"
            "Especially when it's so eloquently put!"
            "The truth is that I'm every bit as desperate as Kylie right now."
            "But as a guy, I feel the need to play it down."
            "You know, for fear of being labelled a sleaze?"
            "That's why Kylie's demands come as such a relief to me."
            "As they mean I can pretty much indulge myself and her at the same time!"
            "Kylie's rubbing the head of my cock against the lips of her pussy."
            "Like she's trying to tease me into action."
            "So all it takes from me is a firm thrust of the hips..."
            "And sure enough, I feel them begin to part."
            "Kylie moans as my cock starts to sink into her."
            "She lets go of it and instead uses her arms to cling to me."
            play sexsfx1 slide_in
            show kylie spoon vaginal opened
            kylie.say "Mmm..."
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            pause 1
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            kylie.say "Oh yeah..."
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            pause 1
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.1, h=-10, v=0)
            kylie.say "That's it..."
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            pause 0.5
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            kylie.say "That's what I want!"
            play sexsfx1 slide_out
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            pause 0.5
            play sexsfx1 slide_in
            show kylie spoon at stepback(speed=0.08, h=-10, v=0)
            "I can't help smiling as I begin to pick up speed."
            play sexsfx1 fuck_calm loop
            with hpunch
            "This should be a piece of cake."
            "Because Kylie and I want the exact same thing."
            play sexsfx1 fuck_calm loop
            "I want to pound her as hard as I possibly can."
            "And she wants to be pounded to within an inch of her life!"
            play sexsfx1 fuck_moderate loop
            "It doesn't take long for me to be going as fast as I can."
            show kylie spoon paf
            "My cock's practically shooting in and out of Kylie."
            "My thighs are slapping against her own curvy haunches."
            "And I can see over her shoulder, noting how her breast bounce and jiggle."
            "There really isn't a single part of Kylie that's not animated right now."
            play sexsfx1 fuck_speed loop
            show kylie spoon speed closed with hpunch
            "It's like her entire body is turned on and dancing to the tune of my cock!"
            "The fact that I'm holding her leg in the air makes a hell of a difference too."
            "With her stretched so wide, I can thrust longer and harder from this angle."
            "Each and every time it goes as deep into Kylie as possible."
            "And each time it does, she moans and pushes herself back against me."
            show kylie spoon opened
            kylie.say "Oh..."
            kylie.say "Oh, [hero.name]..."
            kylie.say "You're going to..."
            kylie.say "Going to make me cum!"
            show kylie spoon closed
            "As soon as the meaning of Kylie's words sink in, everything changes."
            "I realise that I'm on the verge of cuming too."
            "Which means I have to make a decision right now!"
            call cum_reaction (kylie, 'vaginal', sexperience_min) from _call_cum_reaction_292
            if _return == "vaginal_condom":
                "So why in the hell would I even think of pulling out of her now?"
                "Surely the best chance I have of making Kylie cum is to do it inside of her?"
                "And we took the time to use a condom, so why not?"
                "Letting nature take it's course, I make one final thrust into Kylie."
                play sexsfx1 final_thrust
                show kylie spoon -speed
                with hpunch
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                with hpunch
                "And that's because I just gave her everything I have to give."
                with hpunch
                "Kylie's pussy quivers and her muscles twitch as I fill her up."
                "She pants with exhaustion as the cum starts to seep out of her pussy."
                $ kylie.love += 1
            elif _return == "vaginal_outside":
                "Maybe what Kylie needs to push her over the edge is a sudden surprise?"
                "I need to pull out anyway, as we didn't bother to use a condom."
                "And to make that happen, I yank my cock out of her pussy without warning."
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                "And that's because Kylie starts to cum a moment before I do myself."
                with hpunch
                "She twitches and quivers in my arms, her orgasm taking over her entire body."
                play sexsfx1 slide_out
                pause 0.5
                play sexsfx1 pop_out
                show kylie spoon cumshot -vaginal -paf -speed
                with hpunch
                "At the same time I shoot my load up Kylie's back in thick spurts."
                with hpunch
                "It runs downwards, covering the both of us as she squirms against me."
                "Then she collapses into my arms, panting with exhaustion."
                $ kylie.sub += 1
            elif _return == "vaginal_inside_pill":
                kylie.say "Don't stop..."
                kylie.say "I'm on the Pill..."
                "I silently thank Kylie for the timely reminder."
                "Because it means that I can keep right on going."
                "Letting nature take it's course, I make one final thrust into Kylie."
                play sexsfx1 final_thrust
                show kylie spoon -speed creampie
                with hpunch
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                with hpunch
                "And that's because I just gave her everything I have to give."
                with hpunch
                "Kylie's pussy quivers and her muscles twitch as I fill her up."
                "She pants with exhaustion as the cum starts to seep out of her pussy."
                $ kylie.love += 2
            elif _return == "vaginal_inside_pregnant":
                kylie.say "Don't stop..."
                kylie.say "Already pregnant..."
                "I silently thank Kylie for the timely reminder."
                "Because it means that I can keep right on going."
                "Letting nature take it's course, I make one final thrust into Kylie."
                play sexsfx1 final_thrust
                show kylie spoon -speed creampie
                with hpunch
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                with hpunch
                "And that's because I just gave her everything I have to give."
                with hpunch
                "Kylie's pussy quivers and her muscles twitch as I fill her up."
                "She pants with exhaustion as the cum starts to seep out of her pussy."
                $ kylie.love += 2
            elif _return == "vaginal_inside_happy":
                kylie.say "Don't stop..."
                kylie.say "Please don't stop..."
                "The desperation in Kylie's voice catches me by surprise."
                "And worse, it means that I can't do anything to stop what happens next."
                "Nature takes it's course, I make one final thrust into Kylie."
                play sexsfx1 final_thrust
                show kylie spoon -speed creampie
                with hpunch
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                with hpunch
                "And that's because I just gave her everything I have to give."
                with hpunch
                "Kylie's pussy quivers and her muscles twitch as I fill her up."
                "She pants with exhaustion as the cum starts to seep out of her pussy."
                "I can hear her giggling with pleasure."
                "But I'm already starting to freak out!"
                $ kylie.love += 6
                $ kylie.impregnate()
            elif _return == "vaginal_inside_mad":
                kylie.say "Stop..."
                kylie.say "Please stop..."
                "The desperation in Kylie's voice catches me by surprise."
                "And worse, it means that I can't do anything to stop what happens next."
                "Nature takes it's course, I make one final thrust into Kylie."
                play sexsfx1 final_thrust
                show kylie spoon -speed creampie
                with hpunch
                "She moans in pleasure at the sensation, but then the sound goes higher still."
                with hpunch
                "And that's because I just gave her everything I have to give."
                with hpunch
                "Kylie's pussy quivers and her muscles twitch as I fill her up."
                "She pants with exhaustion as the cum starts to seep out of her pussy."
                kylie.say "No..."
                kylie.say "It's not supposed to happen like this!"
                "All I can do is stare helplessly at Kylie."
                "And in my head, I'm already starting to freak out."
                $ kylie.love -= 5
                $ kylie.impregnate()
    stop sexsfx1 fadeout 1.0
    "I finally let myself fall backwards onto the pillows, panting with exhaustion."
    "All Kylie has to do is let herself fall with me, sinking against me as I lie down."
    "For the first time tonight she seems to be in no mood to talk."
    "Instead she's so satisfied with my efforts that she just lies there in silence."
    "I find myself enjoying the softness and the warmth of her body."
    "It's almost as pleasant as the act of making love to her."
    "Almost, but not quite."
    return

label fuck_kylie_jail:
    if "fuck_kylie_jail" not in DONE:
        call fuck_kylie_jail_1 from _call_fuck_kylie_jail_1
    else:
        call fuck_kylie_jail_2 from _call_fuck_kylie_jail_2
    return

label fuck_kylie_jail_1:
    scene bg policestation
    "I feel more than a little nervous as I wait to be let in to see Kylie."
    "It's not like this is the first time I've come to visit her in prison."
    "But it is the first time the visit has been of a conjugal nature."
    "I know that Kylie has every right to this kind of thing."
    scene bg jail with fade
    "And yet I still feel like everyone's staring at me the whole time."
    "Like they know I'm the guy that's here to have sex with the crazy girl!"
    "As the door slides open to let me into Kylie's cell, I try to clear my mind."
    "I try to remember that I'm doing this for her benefit too."
    "It's not just a chance for me to get some hot jail-house action!"
    mike.say "Erm..."
    mike.say "Hi, Kylie!"
    scene kylie_bj_bg_jail at center, dark with fade
    "I lean into the cell, unable to see Kylie from the doorway."
    "That's when she chooses to pounce on me."
    "And I mean that literally."
    show kylie close jail happy with vpunch
    "Kylie leaps from nowhere and lands atop me."
    "She wraps her arms around my neck and her legs around my waist."
    "And I can feel her squeezing me like a python crushing its prey."
    hide kylie
    show kylie kiss jail
    with fade
    $ kylie.flags.kiss += 1
    "Kylie claps her lips over mine, kissing me passionately."
    "Her tongue is in my mouth, like a writhing serpent in its own right."
    "It's all I can do to hold her up and keep from falling on my ass!"
    with hpunch
    "And in the end, I just manage to stagger to the bunk against the wall."
    hide kylie
    show kylie close jail blush
    with fade
    "Once there, I collapse onto the mattress."
    "Kylie lands atop me, and the jolt breaks off the kiss."
    "But it does nothing at all to slow her down."
    kylie.say "Aah..."
    kylie.say "I've been waiting for this..."
    kylie.say "I need you, [hero.name]..."
    kylie.say "I want your cock inside me!"
    "I nod eagerly, doing the best I can to make that happen."
    "Though it's not like Kylie seems to need any help."
    "She's already tearing off my clothes without asking permission."
    show kylie close bottomless
    "And I do the best I can to return the favour."
    "The prison uniform she's wearing is basically a jumpsuit."
    "So it doesn't take me long to strip her to the waist."



    "Somehow the rest of our clothes are torn off a moment later."
    "Then Kylie clambers onto her hands and knees on the bed."
    hide kylie
    show kylie doggy jail
    with fade
    kylie.say "Shit..."
    kylie.say "I'm so hot...so horny!"
    kylie.say "I feel like a bitch in heat!"
    show kylie doggy mike
    "Kylie shoves her ass against me without warning."
    "And I can feel the warmth coming off of her pussy."
    "Needless to say, I'm as hard as a rock right now."
    kylie.say "Fuck me, [hero.name]!"
    kylie.say "Fuck me like an animal!"
    mike.say "Okay, Kylie, okay..."
    mike.say "I'm on it!"
    "I grab a hold of Kylie's broad thighs, one hand on each side."
    "And then I pull her sharply backwards with all my strength."
    "At the same time, I thrust my cock forwards and between her legs."
    "My aim is spot on, as a moment later I feel Kylie's lips."
    "They feel hot and warm, inviting me inside and urging me on."
    show kylie doggy vaginal
    "There's almost no resistance as I sink all the way into her."
    "But Kylie's pussy still feels nice and tight, squeezing my cock hard."
    "And she show how much she's enjoying herself the moment I'm inside of her."
    "Kylie moans, a deep and sensual sound."
    "One that only serves to make her seem more like an animal."
    "I have no intention of stopping, but I still glance around."
    "Because for the first time I'm worried that we're being watched."
    "Sure, this is supposed to be a conjugal visit."
    "But does that actually mean nobody's keeping an eye on Kylie?"
    "She's proven that she can be dangerous in the past."
    "So maybe there's a guard watching everything we're doing."
    "Rather than killing the mood, the notion starts to appeal."
    "The idea that we're being spied on as I fuck Kylie turns me on."
    show kylie doggy crazy
    "I thrust my cock into her, harder and faster than before."
    "And she lets out an even louder moan of pleasure."
    "Before I know it, I'm literally pounding away at Kylie."
    "The sound of my thighs slapping against hers is loud."
    "Even louder than the cries that she's bleating out."
    "Kylie's buttocks and thighs are shaking from the motion."
    "And her huge breasts are swinging crazily beneath her too!"
    mike.say "Ah..."
    mike.say "You...you like that, huh?"
    mike.say "You like it when I fuck you hard?"
    mike.say "When I fuck you like a fucking animal?!?"
    kylie.say "Aaah..."
    kylie.say "Oh...oh god...yes!"
    kylie.say "I love it...I love being fucked!"
    kylie.say "Cum in me, [hero.name]....please!"
    "Before now I was feeling like I was the one in control here."
    "It was like I was calling the shots and dictating the pace."
    "But the moment Kylie speaks those words, everything changes."
    "As if they were a magic spell of some kind, I do as I'm told."
    show kylie doggy ahegao creampie with hpunch
    "One last thrust is all it takes to make me cum in spectacular fashion."
    with hpunch
    "I cling onto Kylie the whole time, trying to push deeper inside."
    with hpunch
    "And she rides my cock until the very last moment."
    with hpunch
    "Then she cums too, and I feel every twitch and spasm."
    show kylie doggy -creampie -vaginal vaginaldrip crazy dickcum
    "Kylie crawls forwards, dragging herself off my cock."
    "And then she drops onto her belly, panting and exhausted."
    show kylie doggy -mike normal
    "I lay beside her on the narrow bunk, enjoying the warmth of her body."
    "I have no idea how much time there is left before I have to leave."
    "But right now, all I want to do is lie right here beside her."
    "She may be locked up in a cell."
    "She may be crazy too."
    "But she's also mine."
    $ kylie.sexperience += 1
    return

label fuck_kylie_jail_2:
    scene bg policestation
    "It's visitor's day at the prison, and I promised Kylie that I'd be there to see her."
    "And there's no way I'm going to break the promise that I made to her."
    "But I'm still a little worried about how things are going to go down this time."
    scene bg jail with fade
    "I know that she's dealing with a lot, locked up with only her thoughts for company."
    "Kylie's been getting frustrated and I really want to do all I can to help."
    "But how can I put this subtly...this isn't a conjugal visit, you know?"
    "And I'm worried that she's going to be wound up like a spring when I see her."
    scene kylie_bj_bg_jail at center, dark
    show kylie sad jail zorder 1 at center, zoomAt (1.1, (860, 800)), dark
    show kylie_bj_bars as bars1 zorder 2 at center
    show kylie_bj_bars as bars2 zorder 3 at center, zoomAt (1.0, (0, 720))
    with fade
    "But when I walk up to the door of her cell, Kylie takes me by surprise."
    show kylie jail happy
    kylie.say "Hello, [hero.name]..."
    kylie.say "Ooh, it's SO great to see you!"
    "Kylie's practically beaming at me from the other side of the bars."
    "In fact, she looks so upbeat and happy it totally throws me."
    "And I can't think of anything to say in response."
    show kylie normal
    kylie.say "Well, aren't you going to say hello back?"
    kylie.say "Shouldn't I be the one that's got nothing to say?"
    kylie.say "After all, I'm the one locked in here with only the walls to talk to!"
    "I make an effort to shake of my surprise."
    "And only then do I manage to say something in return."
    mike.say "S...sorry, Kylie..."
    mike.say "I just didn't expect you to be so..."
    mike.say "So happy...that's all!"
    kylie.say "And why wouldn't I be happy, huh?"
    show kylie happy
    show fx heart at right
    kylie.say "I have the love of my life here to see me!"
    "I give this what I hope is a genuine smile."
    "Kylie's being super intense right now, for sure."
    "But I don't want to dampen her spirits, not when she's locked up in here."
    mike.say "I was worried, you know?"
    mike.say "About coming to see you today."
    "Kylie cocks her head on one side."
    "And her expression becomes quizzical."
    kylie.say "Why would you be?"
    kylie.say "It's just little old me!"
    "I can feel my cheeks starting to flush."
    "But I push on all the same, wanting to say my piece."
    mike.say "Well...today's a normal visit, yeah?"
    mike.say "Not one of those special ones."
    show kylie normal
    "Realisation dawns on Kylie's face all of a sudden."
    "And she smiles, shaking her head at me."
    kylie.say "Oh, [hero.name]!"
    kylie.say "You can be so silly sometimes."
    show kylie happy
    kylie.say "But that's okay, because it's kind of cute!"


    pause 0.5
    scene kylie_bj_bg_jail at center, zoomAt (1.5, (340, 1040)), dark
    show kylie happy jail zorder 1 at center, zoomAt (2.0, (700, 1340))
    show kylie_bj_bars zorder 2 at center, zoomAt (1.5, (340, 1040))
    with hpunch
    "Before I even realise she's moving, Kylie reaches through the bars."
    "She pulls me hard against them, displaying a disturbing amount of strength."
    "But perhaps more disturbing is the way that she giggles as she does so."
    show kylie blush
    kylie.say "And don't worry..."
    kylie.say "These bars aren't strong enough to keep us apart!"
    "I'm still reeling from being pulled into the bars."
    "And so there's nothing I can do to protest as Kylie unzips my flies."
    scene kylie bj jail mikeshirt mikepants with fade
    "A moment later she has my cock out and is down on her knees."
    "I wasn't hard to begin with, but that soon changes."
    "The combination of surprise and danger must be a factor too."
    "Because I can feel myself getting hard in Kylie's hands."
    "She giggles in delight, and then makes a moaning sound of pure pleasure."
    show kylie bj blow pleasure
    show mouth_insert kylie zorder 1 at zoomAt(1, (860, 140))
    "And just like that, she has my cock in her mouth!"
    "I turn my head this way and that, unsure of what I should do."
    "There's nobody else around that I can see."
    "But I'm sure we're being watched by at least one security camera."
    "Any moment I'm expecting guards to come barging in."
    "But time passes, and nobody storms through the door to stop Kylie."
    "And all the while, she's working away at me like crazy."
    show kylie bj normal
    "I gaze down to see Kylie looking back up at me."
    "Her head is already bobbing up and down."
    "And she has an almost desperate look in her eyes."
    "I bite my lip, unsure of just what I should do."
    "And then I make my choice, holding onto the bars for dear life."
    "This isn't about me getting my cock sucked, oh no."
    "This is about me doing what's right for Kylie."
    "If she needs to do this for the sake of her sanity, then so be it!"
    "I'll just have to hang on in there and let her have her way with me."
    "And it's not like that's turning out to be anything like a chore either."
    show kylie bj pleasure
    "Kylie had my cock stiff as a board within moments of getting it out."
    "And now she's got me panting like I've just run a marathon too."
    "I can't begin to imagine what her tongue's actually doing down there."
    "But it's more than enough to make me forget where I am right now."
    "All I can do is hold onto the bars and gasp for breath."
    show kylie bj normal
    "Kylie takes me ever deeper into her mouth."
    "And she's still looking up at me with those huge eyes of hers."
    "In moments like this I can almost forget what landed her in here."
    "All of that craziness doesn't seem to matter like it did when she was free."
    "Maybe that's what we needed as a couple?"
    "For Kylie to be caged in a place like this."
    "Somewhere she can't hurt herself or others."
    "I mean, she seems to be happy right now, like she has a purpose."
    "And you hear of women marrying guys on death row, right?"
    "I know that I could come to like it if visits always went like this!"
    "The thought makes me feel instantly guilty."
    "As it would kind of be like me keeping Kylie in a cage."
    "Almost like she was some kind of animal."
    "But it also makes a smile spread across my face too."
    "Kylie notices this and seems to take it as a sign of my approval."
    show kylie bj pleasure
    "She redoubles her efforts, and I feel the effect almost instantly."
    "I can't hold on any longer - I'm going to cum!"
    menu:
        "Facial":
            show kylie bj out tongue
            "At the last possible moment, Kylie pulls her head backwards."
            "This means that my cock slithers out of her mouth and stands proud."
            hide mouth_insert
            show kylie bj cumshot with vpunch
            "And a mere second later, she takes everything I have in the face."
            with vpunch
            "Kylie gasps and smiles in delight as I shower her with cum."
            with vpunch
            "In fact, she reacts like she was caught in a warm summer rain."
            show kylie bj -cumshot dickcum cum onface with vpunch
            $ kylie.love += 1
            $ kylie.sub += 2
            "And all the while stripes of sticky semen stripe her cheeks."
            show kylie bj normal
            "She licks her lips eagerly, catching all she can as it runs down to her chin."
        "Swallow":
            "Kylie clings to me like a leach, refusing to let go for a second."
            show mouth_insert kylie cum
            show kylie bj cumshot surprised
            with vpunch
            "This means she has my cock deep in her mouth when I cum."
            with vpunch
            "I see her eyes go wide as I unload everything I have."
            show kylie bj pleasure with vpunch
            "But she still manages to swallow without gagging."
            "Kylie gulps down every last drop, like she's dying of thirst."
            hide mouth_insert
            show kylie bj out -cumshot dickcum normal
            $ kylie.love += 2
            $ kylie.sub += 1
            "And the look in her eyes as she does so says it all."
            "She's satisfying much more than her literal thirst right now."
    scene kylie_bj_bg_jail at center, dark
    show kylie normal jail zorder 1 at center, zoomAt (1.1, (860, 800)), dark
    show kylie_bj_bars as bars1 zorder 2 at center
    show kylie_bj_bars as bars2 zorder 3 at center, zoomAt (1.0, (0, 720))
    with fade
    "Once she's done, I hurry to shove my cock back into my pants."
    "Kylie gasps for breath as she pulls herself up in the bars."
    "But I can see a look of satisfaction in her eyes too."
    "She seems calm, almost like she's at peace - at least for now."
    "Kylie wipes her mouth with the back of her hand."
    "And then she leans against the bars of her cell."
    show kylie blush
    kylie.say "That should keep me from getting hungry for a while."
    kylie.say "At least until visiting time comes round again!"
    return

label kylie_university_blowjob:
    scene bg classroom
    "Sometimes it's hard to concentrate in the middle of a lecture, you know?"
    "You could be tired from studying late into the night the day before."
    "You might be feeling under the weather after overindulging at the pub."
    "Or else the subject might be one that you're just not clicking with."
    "But in my case I know exactly what kept me from paying attention."
    show kylie at center, zoomAt(1.5, (840, 1140)) with dissolve
    "It was having Kylie sitting right next to me while I was trying to listen to the professor."
    "And it's not like I was the only one failing to pay attention either."
    "I mean, Kylie was innocent party to all of this - hell no!"
    "She kept on stroking my thigh under the desk, squeezing it too."
    "And giving me these sideways glances, all knowing and sexy!"
    "Obviously I'm not opposed to this kind of thing, not at all."
    "It's just there's a time and a place for getting flirty."
    "And I'm pretty sure a lecture isn't it!"
    "I hate to have to do this, but what choice do I have?"
    "As soon as we're out of the lecture theatre, I confront her about it."
    "I lean in close to Kylie, whispering into her ear."
    mike.say "In here...now!"
    "Kylie offers no resistance as I lead her into an empty classroom."
    "And once we're alone inside, she leans against one of the desks."
    "I mean she leans in a REALLY suggestive way too!"
    mike.say "Erm, Kylie..."
    show kylie annoyed
    kylie.say "Yeah, [hero.name]?"
    "Ah shit, this just got SO much harder!"
    "Kylie's voice is all breathy and seductive."
    "It's like she's on heat or something!"
    mike.say "C...could you stop doing that in the middle of lectures?"
    mike.say "It's kind of distracting, you know?"
    show kylie blush
    "By way of answer, Kylie lets out a mischievous giggle."
    "And then she literally licks my ear, making me leap backwards."
    "I'm confused and a little disoriented for a moment."
    "But when I regain my senses, Kylie's nowhere to be seen."
    "I turn my head this way and that, wondering where she's gone."
    "Then I feel the sensation of someone touching me below the belt."
    "And I have the answer to that question - she's kneeling down on the floor!"
    scene kylie bj with fade
    "I look down to see Kylie, well into the act of opening my flies."
    "I open my mouth, about to tell her to stop what she's doing."
    "But then the precarious nature of my position dawns upon me."
    "All it would take is a sudden noise or movement on my part."
    "And then everyone in the corridor outside would hear us."
    "Kylie glances up, a knowing look in her eyes."
    "Which tells me that she knows exactly what she's doing!"
    "I have no choice but to sit as still as I can."
    "And Kylie takes this as her chance to get on with her task."
    "She has my flies open now and reaches deftly inside."
    "It's all I can do to keep from gasping out loud as she handles me."
    "Yet despite my anxiety, my body seems not to feel the same way."
    "My cock is already half awake when Kylie pulls it out."
    "And it soon begins to stiffen and stand to attention as she handles it."
    "All it takes is for her to lick her lips in anticipation."
    "And there you have it - I'm rock-hard!"
    call kylie_dick_reactions from _call_kylie_dick_reactions_2
    "Kylie wastes no time in beginning to lick around my balls."
    show kylie bj tongue
    show sexinserts head kylie zorder 1 at center, zoomAt(1, (720, 780))
    "She casts an eye up at me as she does so, winking suggestively."
    "I want to keep on looking down at her as she gets to work."
    "But instead I force myself to look up and try to act normal."
    "This is made so much harder when I feel Kylie moving upwards."
    "She licks the shaft of my cock, climbing higher and higher."
    "And when she reaches the top, she wraps her lips around the tip."
    show kylie bj blow pleasure -tongue
    "My hands clench a moment later."
    "This happens because Kylie swallows my cock for the first time."
    "With the head between her lips, she begins to move up and down."
    "Kylie's head bobs under the desk as she works away on me."
    "It's a miracle that she doesn't bang it on the underside!"
    "But I have to admit that she's doing an amazing job right now."
    show kylie bj normal
    "I'm biting my lip to keep from letting it show too."
    "Sure, Kylie's not taking her time like she might have in a more private setting."
    "Yet that doesn't mean that she's skimping with what she is doing."
    "Her lips and tongue are working overtime down there."
    show kylie bj pleasure
    "And she keeps giving my balls the occasional squeeze too!"
    "In fact, she squeezes them so hard I let out a yelp."
    "I'm fast approaching my limit, and I'm about to blow!"
    menu:
        "Facial":
            "I don't know if Kylie realises what's about to happen."
            "Or if she just chooses that moment to catch her breath."
            show kylie bj out tongue
            hide sexinserts
            "Either way she releases my cock and gasps for air."
            "And a moment later I shoot my load."
            show kylie bj cumshot with vpunch
            "There's no way Kylie can escape, and she takes it straight in the face."
            with vpunch
            "By some minor miracle, she manages to keep quiet as it spatters her features."
            show kylie bj -cumshot dickcum cum onface with vpunch
            "Cum paints Kylie's nose and cheeks, dripping down to her chin."
            show kylie bj normal
            "She struggles to clean herself up as I pant with relief."
            $ kylie.love += 1
            $ kylie.sub += 2
        "Swallow":
            "I have no idea if Kylie's ready for what's about to happen."
            "But my cock is so deep in her mouth that there's no time to warn her."
            "I shoot my load a moment later, and I feel it hit the back of her throat."
            show kylie bj cumshot surprised
            show sexinserts head kylie cum zorder 1 at center, zoomAt(1, (720, 780))
            with vpunch
            "Kylie's eyes pop open, going wide as she struggles to swallow in time."
            with vpunch
            "Luckily for me, the fact she has a cock in her mouth muffles the sound."
            show kylie bj pleasure with vpunch
            "And it's only when she's stopped gagging that I begin to pull it out."
            show kylie bj out -cumshot dickcum normal
            "Kylie gasps for breath as I do so, cum dripping from her lips."
            hide sexinserts
            $ kylie.love += 2
            $ kylie.sub += 1
    scene bg classroom
    show kylie blush at center, zoomAt(1.5, (840, 1140)) with dissolve
    with fade
    "I hastily shove my cock back into my pants as Kylie catches her breath."
    "She just got up to some of the worst mischief I can imagine in an empty classroom."
    "Yet when she pops back up to her feet, she looks like the picture of innocence."
    "I try as best I can to keep my eyes off of her and concentrate on making myself decent."
    "But if I was distracted by her before, it's a hundred times worse now!"
    $ hero.replace_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
