init python:
    InteractActivity(**{
    "name": "lavish_fuck_date_livingroom",
    "display_name": "Fuck",
    "label": "lavish_fuck_date_livingroom",
    "conditions": [
        IsSeason(0, 1),
        HeroTarget(
            IsRoom("date_livingroom"),
            HasStamina(),
            ),
        PersonTarget(lavish,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })


    InteractActivity(**{
    "name": "fuck_lavish",
    "display_name": "Fuck",
    "label": "lavish_fuck_ROOM",
    "conditions": [
        HeroTarget(
            Not(IsRoom("date_livingroom")),
            HasStamina(),
            ),
        PersonTarget(lavish,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_lavish_personal",
    "display_name": "Fuck",
    "label": "lavish_fuck_mc_office",
    "conditions": [
        IsDone("lavish_office_bj"),
        HeroTarget(
            HasRoomTag("mcoffice"),
            HasStamina(),
            ),
        PersonTarget(lavish,
            IsActive(),
            MinStat("love", 125),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "lavish_hottub_sex_male",
    "label": "lavish_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(lavish,
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


label lavish_fuck_date_livingroom:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ lavish.sexperience += 1
    scene bg livingroom
    show lavish
    lavish.say "Hey..."
    "There's something mischievous about her voice, and it snaps my attention to her immediately, and the sultry look she's shooting me."
    "The tip of one well-kept nail taps softly at the corner of her lips, curled into a devilish smile."
    "Still, what she says sounds innocuous enough."
    lavish.say "You've got a pool, right?"
    mike.say "Yeah, in the back."
    lavish.say "Why don't we go take a dip? It's such a beautiful day."
    "I'm more than okay with that."
    mike.say "You brought a suit?"
    "She gives a low, unbothered hum."
    show lavish wink
    lavish.say "I have a bra and panties. That's close enough, isn't it?"
    "For a moment, I debate whether or not I should go upstairs and change into my swim trunks."
    show lavish normal underwear with dissolve
    "But when Lavish stands up and pulls her shirt off over her head, and I see that her bra is a lacey, purple against her deep skin, I know that it doesn't matter what I change into."
    "It's not staying on. Lavish is the kind of woman that I know has matching panties on, and I know she knows exactly what happens to white when it gets wet."
    scene bg pool
    show lavish underwear
    with fade
    "Instead, I unbuckle my pants, tossing my shirt onto the couch before we make our way out back."
    "The sun seems to glitter on her bare upper body as we step into it, and she looks like a poster for some tropical resort when she shields her eyes from it with her hand."
    "She steps over to the edge of the pool and dips her toes in, and I stand back, watching her, fascinated."
    mike.say "How's the water?"
    show lavish happy
    "She smiles back at me over her shoulder."
    lavish.say "Just right."
    show lavish normal
    "She hooks her thumbs under her waistband and slips off the last of her clothing, leaving only the generous view of pristine white lace panties shielding her from the world."
    "I unzip my jeans and step out of them, allowing them to fall beside the edge of the pool."
    "I feel a throb behind the thin fabric of my boxers, knowing that they won't hide anything at all from her if I get hard."
    "When I get hard."
    "She makes her way over to the stairs and strides down them, tantalizingly slowly."
    "Finally, the water creeps up her calves, her thighs, and then her hips, and I watch it seep through and dampen the delicate white fabric."
    "It goes immediately transparent, clinging to her tanned skin and outlining the full curve of both of her ass cheeks, puddling transparently in the crease between them."
    "Something surges through the flesh barely hidden beneath my boxers, and I feel my blood begin to vacate south."
    "When she reaches the bottom stair, she bends her knees and submerges herself up to her shoulders, kicking off and swimming a bit into deeper waters."
    "I'm hypnotized by her lean, toned legs and ass as they scissor through the water, her panties only a ghost between my prying eyes and her prize."
    scene swimmingrace_bg_03 at center, zoomAt(1.75, (1000, 1040)), blur(5)
    show lavish underwear at center, zoomAt(1.5, (640, 1140))
    with fade
    "She flips onto her back to float and stroke away from me, a coy smile on her lips as she presents herself at the water's surface."
    "The way her panties are clinging to her pussy lips somehow hits me harder than if she'd been fully naked."
    "I make my way down the steps into the water."
    "As my boxers get soaked, too, they hang with a gentle pressure against my shamelessly stiffening meat before I submerge it into the weightlessness of the water."
    lavish.say "I love being in the water."
    "She arches her back gracefully, dipping her front half beneath the surface into a handstand."
    "Her legs straighten and kick back fluidly into the air, straight up at first, and then separating into a split that makes the humble fabric of her panties strain against the soft, rounded lips between her thighs."
    "She knows what she's doing. I reach my hand beneath the water and grip my cock, already rock hard."
    "Lavish turns the handstand into a flip and arches beneath the water to swim back over to me, stopping to stand a few feet away."
    "I can see her dark, pert nipples from beneath the cups of her bra."
    "She moves in close, closer, and, when her face is tantalizingly close to mine, she reaches beneath the water and lays her hand over mine."
    "I release my grip and allow her to take it instead, running her fingers slowly up and down my shaft. I can't help but let out a low groan of appreciation."
    lavish.say "Maybe this underwear doesn't do much as a swimsuit."
    mike.say "It works perfectly fine for me..."
    show lavish naked with dissolve
    "My words are practically grunted, my breath catching in my chest as she slips her fingers deftly between the folds of my boxers and grazes them against the head."
    "I'm throbbing already. She gives it an appreciative squeeze in return."
    "I allow my hands to make their way to her waist, slipping over her skin beneath the chlorine, and slide my own fingers beneath the waistband of her skimpy panties, getting a firm, greedy grip on her ass."
    "She moans back softly in response as I squeeze and pull her closer to me, practically lifting her off her feet. She complies, laying her other hand on my shoulder and bringing her legs up to lock around my waist."
    "Her labia are pressed firmly against my cock now, and as I carry her over to the edge of the pool she grinds them against the stiffness, stimulating me beneath the water in a way that could easily drive me crazy."
    "I don't waste any time when we get to the pool's edge. I heft her up onto it and sit her there, removing her panties in the same motion and tossing them aside onto the patio."
    if game.calendar.is_night:
        "Her legs are locked together for a second, but they part easily as I press my hands to her knees and spread them, getting a good look at her slick pink folds, glimmering in the bright moonlight."
    else:
        "Her legs are locked together for a second, but they part easily as I press my hands to her knees and spread them, getting a good look at her slick pink folds, glimmering in the bright sunlight."
    "My fingers slide in effortlessly when I trail them down, eliciting a full body shiver from her as they trail over her clit before plunging inside. She's soaking wet."
    "Her head tilts back with a low, lusting moan, and I pump my fingers two, three, four times against her tight inner walls before I can't take the tease anymore."
    "She apparently can't take it either."
    show lavish flirt
    lavish.say "[hero.name]..."
    "Her voice is a whispered plea. I don't need to hear more."










    hide lavish
    show lavish pool sex
    with fade
    "I pull her forward from the edge of the pool so that she's standing again and turn her around."
    "My boxers had slid off easily, revealing the thick rod she's caused before I plunge it, deep, into the hot, waiting tightness she's prepared for me."
    "She gasps and then moans again, maybe a bit too loudly, considering we are outside and we do have neighbors. But that passing thought doesn't remain in my mind for more than a split second."
    "Holding her by the clasp of her bra for leverage, I drive myself in deep, pumping in an out against the rushing grip of the water between us."
    "With my free hand, I reach around and slip the cups of her bra up and over her breasts, clutching at one of them and feeling it ripple in my hand beneath the force of my thrusts."
    lavish.say "Oh... oh, god... [hero.name]...!"
    "She tilts her head back a little, trying to look at me."
    "I release my grip on her brastrap and plunge my fingers into her hair instead, gripping it tight and pulling her head back so I can see her pretty face better, too."
    "Her eyes are gleaming with lust, her lips parted with the gasping moans I'm pounding out of her."
    "Her teeth clench, and she sucks in air between them in a hissing gasp."
    lavish.say "Yes... yes! Ohh fuck me, fuck... m--"
    "Her words are cut short as her eyes roll back and then close."
    "She cries out, reaching her hands back to my thighs and digging her fingers into me as she shudders, her inner walls squeezing me rhythmically as the ramming pressure of my cock inside of her pushes her over the edge."
    "I'm nearing my own peak, and I push her upper half down onto the edge of the pool, bending her at a 90 degree angle as I pick up speed, slamming my hips against her perfect, round ass."
    "She's almost mewling before me, bringing her fingers up on one hand to bite down on, though it's far too late for being subtle or quiet."
    "Her breaths pick up again, not just breathing but sharp, pitched whimpers."
    with hpunch
    "And when she cums again around me I lose it and bust with her, grunting as I pump my seed deep inside of her with final, deep, stroking thrusts into her deepest parts."
    with hpunch
    "Both of us stand there, panting and rubber-legged, for a while before we regather ourselves and our clothes and stumble our way back inside onto the couch."
    "She lays against me beneath one arm for an hour or two, dazed and satisfied, before either of us manage to get our clothes back on."
    return

label lavish_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")

    call lavish_fuck_date_intro_male (location) from _call_lavish_fuck_date_intro_male


    call lavish_dick_reactions from _call_lavish_dick_reactions_5


    call lavish_fuck_date_foreplay_male from _call_lavish_fuck_date_foreplay_male




    call lavish_fuck_date_choices_male from _call_lavish_fuck_date_choices_male


    call handle_npc_leaving (lavish, _return) from _call_handle_npc_leaving_13
    if _return:
        return


    hide lavish
    call lavish_sleep_date_fuck (location) from _call_lavish_sleep_date_fuck
    return

label lavish_fuck_date_intro_male(location="hero"):
    $ randintro = randint(1, 4)
    if randintro == 1:
        scene bg bedroom1
        show lavish
        with fade
        "We make it back to my bedroom."
        "Her hand is in mine, her delicate fingers laid soft and warm across my palm, with mine curled protectively over them as I use them to lead her through my doorway."
        "The both of us know why we're here."
        "Reluctantly, I let her go and shut the door behind us, missing the warm of her skin the moment it's gone."
        "I know it'll be back."
        "When I turn back around, I see her facing me, her hands trailing up her body to the top button of her shirt."
        show lavish naked blush with dissolve
        "Lavish locks her eyes on me, watching me from beneath seductively lowered lashes as she tantalizingly undoes her top and then her bra, dropping the both of them aside to the floor."
    elif randintro == 2:
        scene bg bedroom1
        show lavish blush
        with fade
        "Lavish leans her back against the door of my room after shutting it behind her."
        "I'm used to her being pretty coy and behaving politely when we're out in public."
        "But I can see a change coming over her now that we're in private and alone."
        "It's a hot thing to watch, and it never fails to turn me on when I get to see it."
        "It's the realisation that this hot, stunning girl's been watching you all night."
        "And now she's finally able to let it all out, for you and you alone!"
        show lavish happy
        lavish.say "Ah, I feel like I can breathe again!"
        show lavish wink
        lavish.say "Like I can finally do what I want to."
        "I nod eagerly, trying to look like I'm not beginning to sweat."
        mike.say "Erm..."
        mike.say "What's that, Lavish?"
        mike.say "What is it that you want to do?"
        show lavish flirt
        "As if I needed to ask!"
        hide lavish
        show lavish kiss
        with fade
        $ lavish.flags.kiss += 1
        "Lavish answers my question by walking over and wrapping her arms around me."
        "She kisses me full on the lips, pressing her body into mine."
        "I'm stunned for a moment, but then I recover myself just a little."
        "Just enough to return her show of affection with equal intensity."
        "After that, there's no need for anymore questions."
        "Hell, there's hardly any need for another word between us!"
        hide lavish
        show lavish blush
        with fade
        "The very moment that the kiss is over, we hurry over to the bed."
        "Lavish and I are clumsily trying to undress each other."
        show lavish naked with dissolve
        "And we're also trying to pull off our own clothes at the same time too."
    elif randintro == 3:
        scene bg bedroom1
        show lavish
        with fade
        "Lavish seems eager to get the door closed behind us and get down to business."
        "In fact, she's already standing by the bed, half-undressed, by the time I turn around."
        show lavish blush
        "She must have read the look of surprise on my face, because she blushes and chuckles."
        lavish.say "[hero.name]!"
        lavish.say "Why are you looking at me like that?"
        show lavish embarrassed
        lavish.say "I...I've just been waiting for this, that's all!"
        "I shake my head, trying to reassure Lavish that it's nothing."
        mike.say "I...I'm not, Lavish, honestly."
        mike.say "I'm looking forward to it too - obviously!"
        mike.say "It's just good to know that we're both on the same page."
        show lavish normal
        "Lavish smiles at me and beckons me over to where she's standing."
        show lavish naked with dissolve
        "By now she's stripped off the last of her clothes."
        "And I hurry to do the same as I make my way over to her."
        "Lavish let's out a playful cry of exaggerated alarm at this."
    else:
        scene bg house
        show lavish
        with fade
        "I can hardly wait to get Lavish out of the cab and into the house."
        "The night's been going so well and we've been having such a great time."
        "Neither of us wants it to end, and there's still more fun to be had."
        scene bg bedroom1
        show lavish normal
        with fade
        "Lavish can't seem to help smiling at me as I show her into my bedroom."
        show lavish happy
        "She shakes her head and laughs, but without a hint of malice."
        lavish.say "Will you stop that?"
        mike.say "Ah..."
        mike.say "Stop what, Lavish?"
        show lavish embarrassed blush
        lavish.say "Stop looking at me like that, [hero.name]!"
        lavish.say "It's embarrassing!"
        lavish.say "And you're making me blush too!"
        "Now it's my turn to laugh."
        "I rub the back of my neck, feeling awkward."
        mike.say "I can't help it, Lavish."
        mike.say "You just look so hot right now!"
        show lavish -blush flirt
        "Lavish bites her lip and looks away for a moment."
        "And I see the shade of red on her cheeks deepen."
        "Then she looks me in the eye and flutters her eyelids."
        lavish.say "Actually, don't stop!"
        lavish.say "Tell me again how hot I am, [hero.name]!"
        lavish.say "Y...you're turning me on!"
        "I swallow audibly at this."
        "If only Lavish knew how much she was turning me on too!"
        mike.say "You're so hot, Lavish!"
        mike.say "You make me feel like I'm going crazy!"
        lavish.say "Crazy enough to fuck me?"
        lavish.say "That crazy?"
        "My jaw drops as Lavish takes me by the hand."
        "She leads me across the room and to the side of my bed."
        "I follow without hesitation."
        "But right now she could lead me straight off a cliff!"
        "Lavish places my hands on her shoulders."
        "And then she motions for me to begin undressing her."
        show lavish underwear with dissolve
        "I do as I'm told, stripping off her clothes."
        "Lavish turns on the spot, slipping out of one garment after another."
        show lavish naked with dissolve
        "And I feel like I'm unwrapping the best gift I ever got given."
    show lavish kiss naked with fade
    $ lavish.flags.kiss += 1
    "My pulse is racing already as I step forward and cup a hand hungrily to one of her breasts, massaging it against my palm as I use the other hand to pull her forward and nip one of her full lips into mine."
    return

label lavish_fuck_date_foreplay_male:
    $ game.room = "bedroom1"
    menu:
        "Go down on her":
            call lavish_fuck_date_cunnilingus from _call_lavish_fuck_date_cunnilingus
        "Make her suck you off" if lavish.sub >= 50:
            call lavish_fuck_date_blowjob from _call_lavish_fuck_date_blowjob
        "Fuck her":
            pass
    call stop_all_sfx from _call_stop_all_sfx_23

    return _return

label lavish_fuck_date_choices_male:
    menu:
        "Go missionary style":
            call lavish_fuck_date_missionary (0) from _call_lavish_fuck_date_missionary
        "Go cowgirl style" if hero.sexperience >= 10:
            call lavish_fuck_date_cowgirl (10) from _call_lavish_fuck_date_cowgirl
        "Go doggy style" if hero.sexperience >= 15:
            call lavish_fuck_date_doggy (15) from _call_lavish_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_24

    return _return

label lavish_fuck_date_cunnilingus:
    "Lavish backs into the bed, her attention fixed upon me."
    "She lets out a yelp as she tumbles over backwards and lands on the mattress."
    "I hurry after her, all but pouncing on her as she lays there."
    mike.say "All I want is to taste you, Lavish."
    mike.say "I want to eat you up..."
    "Lavish's thighs are wide enough apart for me to make my next move."
    "Before she knows what's happening, my head is between them."
    show lavish cunnilingus with fade
    "Even I don't know if I'm really acting all of this out by now."
    "The scent of her pussy is the only thing that I can smell."
    "And it fills my senses, drowning out everything else."
    "It's all that I want, all that I can think about."
    "I barely hear Lavish moan as I begin to explore down there."
    show lavish cunnilingus up
    pause 0.25
    show lavish cunnilingus down
    "Instead my tongue thrills at the taste and textures being revealed to it."
    "Even on the very edges and amongst the outer folds, it's pretty intense."
    "Apparently Lavish was already excited long before I got my hands on her."
    "Which means that everything down here is slick and slippery."
    show lavish cunnilingus up climax
    pause 0.25
    show lavish cunnilingus down
    pause 0.25
    show lavish cunnilingus up
    pause 0.25
    show lavish cunnilingus down
    "It's almost by accident that my tongue slips deeper."
    "I wanted to take my time over this, build up slowly."
    show lavish cunnilingus up
    pause 0.25
    show lavish cunnilingus down
    pause 0.25
    show lavish cunnilingus up
    pause 0.25
    show lavish cunnilingus down
    "But Lavish is so well-lubricated that I just can't help it."
    "My tongue seems to be drawn deeper with every move it makes."
    lavish.say "Mmm..."
    show lavish cunnilingus normal
    lavish.say "Oh, [hero.name]..."
    lavish.say "What are you doing to me?"
    "I hear Lavish's words and they make perfect sense to me."
    "But I barely register the fact that she asked a question."
    "I take them simply as a sign that she wants more of the same."
    show lavish cunnilingus up climax
    pause 0.25
    show lavish cunnilingus down
    pause 0.25
    show lavish cunnilingus up
    pause 0.25
    show lavish cunnilingus down
    "Which is why I choose that very moment to push my tongue deeper still."
    "In fact, I push it as far into Lavish's pussy as it will possibly go."
    show lavish cunnilingus up
    pause 0.15
    show lavish cunnilingus down
    pause 0.15
    show lavish cunnilingus up
    pause 0.15
    show lavish cunnilingus down
    pause 0.15
    show lavish cunnilingus up
    pause 0.15
    show lavish cunnilingus down
    pause 0.15
    show lavish cunnilingus up
    pause 0.15
    show lavish cunnilingus down
    "Now there's no change of her speaking as much as a single word."
    "All I can hear from Lavish are animalistic sounds of sheer pleasure!"
    menu:
        "Finish with tongue":
            "There's no hint of criticism or discomfort in the sounds that Lavish is making."
            "And I'm so into the act of going down on her that I don't even think of stopping."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "My tongue moves like a snake, trying to cover every inch of her pussy."
            "I turn my head this way and that, letting it be lead by my tongue too."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Lavish seems to have stopped moaning now."
            "But that doesn't mean she's suddenly gone quiet on me."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Instead she seems to be gasping, almost keening."
            "Trying to push her even further, my hands reach out for her."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "My fingers pull the lips of her pussy as far apart as they can."
            "And once this is done, I thrust my tongue back into her."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            "Lavish pants and begins to squirm on the bed."
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            "She can't keep this up much longer - at least that's what I hope!"
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            "I can feel the muscles of my tongue starting to tire."
            show lavish cunnilingus up squirt with vpunch
            $ lavish.love += 2
            "And so when she bucks and twitches, beginning to cum, I breathe a sigh of relief."
            with vpunch
            "Lavish hardly seems to notice as I ease off licking her pussy."
            show lavish cunnilingus -squirt with vpunch
            "She simply lies there, helpless and gasping as she cums."
        "Finish with tongue and finger in ass":
            "Lavish keeps on lifting her pelvis the whole time I'm going down on her."
            "Not that I mind having her pussy pushed in my face, as it makes my job easier!"
            "But it does make a wicked thought pop into my head, one that just won't quit."
            "And so I wait for the next time she does it, and slip a hand underneath her raised ass."
            show lavish cunnilingus up anal
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "All it takes is a little probing with my finger..."
            lavish.say "Oh..."
            show lavish cunnilingus normal
            lavish.say "Oooh..."
            lavish.say "[hero.name]...my ass!"
            show lavish cunnilingus up climax
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Lavish moans as I push that finger into her tight little ass."
            "Her muscles try to resist, but they can't hope to hold out for long."
            "And then my finger sinks all the way in to the knuckle."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Of course, Lavish tries to raise herself up to escape."
            "But all that does is push her pussy against me all the more."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "I take full advantage, worming my tongue further into her pussy."
            "Now Lavish seems to lose the power of speech entirely."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            "She writhes on the bed, squirming as I work her from both sides."
            "There's nothing she can do to hold on."
            show lavish cunnilingus up squirt with vpunch
            $ lavish.love += 1
            $ lavish.sub += 2
            "And I feel her beginning to cum a moment later."
            with vpunch
            "Lavish hardly seems to notice as I ease off licking her pussy."
            show lavish cunnilingus -squirt with vpunch
            "She simply lies there, helpless and gasping as she cums."
        "Finish with tongue and dildo in pussy":
            "Lavish keeps on lifting her pelvis the whole time I'm going down on her."
            "Not that I mind having her pussy pushed in my face, as it makes my job easier!"
            "But it does make a wicked thought pop into my head, one that just won't quit."
            "And so I slip a hand under the bed and wait for the next time she does it."
            "As soon as her tight little ass lifts off the mattress, I make my move."
            show lavish cunnilingus up dildo
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Pulling my head back, I rub the dildo I just grabbed against Lavish's pussy."
            lavish.say "Ah..."
            show lavish cunnilingus normal
            lavish.say "Wha...what's that?"
            lavish.say "[hero.name], what are you..."
            "Not giving Lavish the time to finish her question, I plunge the dildo home."
            show lavish cunnilingus up climax
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "It pushes between her slick lips with ease, sinking deep into her."
            "Lavish moans, losing the power of speech entirely."
            "I watch in fascination as her eyes roll back into her head."
            "She wriggles and squirms as I begin to fuck her with the toy."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "And the faster I go, the more she seems to like it!"
            "Pretty soon Lavish seems to be almost in a trance."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "She moans and tosses her head as her body twitches with pleasure."
            "At first I think she's so far gone that she's completely out of it."
            show lavish cunnilingus up climax
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "But then I see the way she's nodding her head desperately."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            "She's actually begging me for more!"
            "I do my best to give her what she wants."
            show lavish cunnilingus up squirt with vpunch
            $ lavish.love += 4
            "And I feel her beginning to cum a moment later."
            with vpunch
            "Lavish hardly seems to notice as I pull the dildo out of her pussy."
            show lavish cunnilingus -squirt with vpunch
            "She simply lies there, helpless and gasping as she cums."
        "Finish with tongue and dildo in ass":
            "Lavish keeps on lifting her pelvis the whole time I'm going down on her."
            "Not that I mind having her pussy pushed in my face, as it makes my job easier!"
            "But it does make a wicked thought pop into my head, one that just won't quit."
            "And so I slip a hand under the bed and wait for the next time she does it."
            "As soon as her tight little ass lifts off the mattress, I make my move."
            show lavish cunnilingus up dildo anal
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Pulling my head back, I rub the dildo I just grabbed against Lavish's ass."
            "At the same time, I probe her ass with my tongue..."
            lavish.say "[hero.name]..."
            show lavish cunnilingus normal
            lavish.say "What are you..."
            lavish.say "What's that and where's your hand going?"
            show lavish cunnilingus up climax
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Not giving Lavish the time to finish her question, I plunge the dildo home."
            "It pushes between her tight little ass with ease, sinking deep into her."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "A moment later I push my tongue into her slick lips."
            "Her muscles try to resist, but they can't hope to hold out for long."
            "And then my tongue sinks all the way in to the knuckle."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Of course, Lavish tries to raise herself up to escape."
            "But all that does is push the dildo deeper into her still."
            "I watch in fascination as she's trapped between the two."
            "The more she struggles against one, the more the other penetrates her."
            show lavish cunnilingus up climax
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            "Pretty soon ever movement that Lavish makes only serves to drive her further."
            "She becomes trapped there."
            show lavish cunnilingus up
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            pause 0.15
            show lavish cunnilingus up at startle(0.05,-10)
            pause 0.15
            show lavish cunnilingus down
            "Trapped and working herself into more of a frenzy with each second that passes!"
            "There's nothing she can do to hold on."
            show lavish cunnilingus up squirt with vpunch
            $ lavish.love += 1
            $ lavish.sub += 3
            "And I feel her beginning to cum a moment later."
            with vpunch
            "Lavish hardly seems to notice as I ease the dildo out of her ass."
            show lavish cunnilingus -squirt with vpunch
            "She simply lies there, helpless and gasping as she cums."
    return

label lavish_fuck_date_blowjob:
    hide lavish
    show lavish naked flirt
    "She smiles then, slow and suggestive."
    lavish.say "You're a dirty boy - you know that?"
    lavish.say "But lucky for you, you're a good boy too!"
    lavish.say "And good boys deserve a reward..."
    show lavish close naked flirt
    "Without another word, Lavish takes hold of my hand."
    "She leads the way to the bed and then turns to face me, taking a firm hold of my cock."
    "I offer no resistance as she begins to strip off my clothes."
    "And all it takes is the occasional glance from her to keep me as still as a statue."
    "Lavish strips me slowly, but with a definite purpose, not stopping once."
    "As soon as I'm naked, she takes a firm hold of my cock."
    call lavish_dick_reactions from _call_lavish_dick_reactions
    "I gasp as I'm compelled to follow her closely, being lead where she wills."
    show lavish bj with fade
    "Lavish climbs onto the bed and lays flat on her belly."
    "She looks up at me, smiling as she massages my cock."
    "Needless to say it's stiffening more with each passing second."
    "And soon it's standing to attention, bobbing before Lavish's face."
    lavish.say "Mmm..."
    lavish.say "That looks so good!"
    lavish.say "I want to see how it tastes..."
    "Lavish parts her lips and sticks out her tongue."
    show lavish bj blow
    show sexinserts head lavish zorder 1 at center, zoomAt(1, (720, 760))
    "And then she leans forward and begins to lick at the base of my cock."
    "She looks up at me the whole time she's doing it, holding my eye."
    "Sure, it feels incredible, like a dream come true."
    "But it's the sight of her about to suck my cock that really blows my mind."
    "Lavish is intelligent, brilliant and driven, not to mention beautiful."
    "To have a girl like that giving me head..."
    "Well, it's almost unbelievable!"
    "But it's actually happening."
    show lavish bj hold
    "Lavish brings home the reality of the moment as she starts to suck on my balls."
    "At the same time she's working the shaft with one hand too."
    "It seems she's as efficient and dedicated in the bedroom as she is in the office!"
    show lavish bj pleasure
    "Slowly and with deliberate effort, Lavish works her way higher."
    "She licks and kisses the shaft of my cock, leaving it slick as she does so."
    "And by the time she reaches the head, I'm a panting mess."
    "Lavish is fully aware of the effect that she's having on me."
    show lavish bj out normal
    "She takes a moment to pause and offer me a smile."
    show lavish bj deep blow pleasure
    "And then she takes the head of my cock into her mouth for the first time."
    "As good as it's been up to this point, now it gets better still."
    "Not only that, it gets better quickly too!"
    show lavish bj tip
    "It feels like Lavish has been building up to this moment."
    "It's like she's lulled me into a false belief that she's going to go slowly."
    "But now she seems to become like a woman possessed, fixated on one thing only."
    show lavish bj deep
    "And that's getting as much of me into her mouth as possible!"
    "Before I can fully feel the sensation of her tongue and lips, she's swallowing me whole."
    "I swear that half of my cock disappears into her mouth in one motion."
    show lavish bj tip
    "Lavish's head bobs up and down constantly as she works away on me."
    "It's a shock to realise that she's this voracious."
    "She always seems to prim and dignified when we're out in public."
    show lavish bj deep
    "And now here she is, swallowing cock like her life depends on it!"
    "I hardly notice that she's taking me deep into her throat."
    "But that's exactly what she's doing right now."
    show lavish bj tip normal
    "I hear the unmistakable sucking and slapping, see her swallowing it whole!"
    "Lavish still holds my eye, even while she's deep-throating me."
    "But there's no look of discomfort or displeasure in her eyes."
    show lavish bj deep pleasure
    "Quite the opposite - she's clearly enjoying every second of this."
    "I feel myself begin to stiffen then, gasping for breath."
    "I'm going to lose it, to cum any second now!"
    menu:
        "Cum in her mouth":
            "I can't cum with my cock this far down Lavish's throat."
            "But that doesn't mean I have to pull all the way out either."
            show lavish bj normal
            "I begin to pull back, and she seems to understand what I'm doing."
            show lavish bj tip
            "Lavish lets me pull back until the head of my cock is resting on her tongue."
            show lavish bj creampie pain
            show sexinserts head lavish cum zorder 1 at center, zoomAt(1, (720, 760))
            with hpunch
            "And only then do I shoot my load."
            with hpunch
            "She holds onto my cock with both hands, keeping it steady."
            with hpunch
            "Lavish makes sure that not one drop is spilled."
            show lavish bj pleasure
            "Most of it she swallows straight down."
            "But some escapes her lips when she finally gasps for breath a moment later."
            hide sexinserts
        "Cum on her face":
            "I'd love to see Lavish swallowing all that I have to give."
            "But there's just something about that pretty face of hers."
            "It's so perfect that I want to make my mark all over it..."
            hide sexinserts
            show lavish bj tip out normal
            "Pulling my cock out of Lavish's mouth, I ignore her moan of disappointment."
            "She doesn't try to stop me, just stares up with those huge, dark eyes."
            "Likewise she doesn't try to move a moment later when I lose it."
            show lavish bj cumshot pain with hpunch
            "The cum spatters down on Lavish's upturned face and she yelps is surprise."
            show lavish bj cum onface -cumshot with hpunch
            "It paints white stripes across her perfect dark skin."
            "And she licks her lips as it starts to run downwards over her lips."
    show lavish bj normal
    "Lavish smiles up at me, not speaking a single word."
    "But I can tell that she's pleased with herself and with the look on my face."
    return

label lavish_fuck_date_missionary(sexperience_min):
    hide lavish
    show lavish kiss naked
    with fade
    $ lavish.flags.kiss += 1
    "She's willing and eager, kissing me back immediately with a fire that I know I lit in her. Her hands make their way up my back, fingertips pressing into my shoulder blades as we make out and I lead her with careful steps back toward the bed, our mouths never parting."
    "Her tongue glides over mine, slick and sweet, and I feel her draw a brief, cold breath from my mouth in a gasp as I flick my thumb over her pert nipple, eliciting goosebumps over her flesh that drive me wild."
    hide lavish
    show lavish missionary normal
    with fade
    "The back of her knees hit the bed, and she lays herself down onto it without a word, only a breathless pant as our mouths part."
    "Something's burning in her eyes as she slides her hands down to her hips and removes the rest of her clothing, making me throb there before her. Her curves, her hips, the silky perfection of her skin makes me almost dizzy."
    call lavish_dick_reactions from _call_lavish_dick_reactions_1
    "She draws her legs up and spreads them, reaching down a graceful hand to rub a moment over the soft mounds of her pussy."
    "Then, using two fingers, she spreads them, giving me a clear show of the slick, pink folds waiting for me."
    "She's glistening, almost dripping wet. My heart gives a hard thud in my chest."
    call check_condom_usage (lavish, 175) from _call_check_condom_usage_73
    if _return == False:
        return "leave_without_gain"
    "My cock gives an eager, appreciative throb at her presentation as I step forward over her, positioning myself at her entrance."
    hide lavish
    if CONDOM:
        show lavish missionary normal vaginal condom
    else:
        show lavish missionary normal vaginal
    "A soft, mewling moan escapes her when I press the tip against her clit, guiding it up and down her slick folds for a moment, coating myself in her silky nectar."
    "She's wanted this from that first moment she laid eyes on me at my cubicle."
    "Her lips part in her flushed, knit-browed panting as she looks up at me with puppy dog eyes that beg for my entrance."
    "I'm more than happy to comply."
    "With a grunt, I slide myself into her, gliding myself deep into her, and she utters a low, musical moan, tilting her head against the bed and letting her eyes roll back before closing."
    lavish.say "Ohhh, yes."
    "She's breathless already, and I haven't even thrust."
    lavish.say "I'm yours."
    mike.say "I know."
    "I slam myself in to the hilt, and she yelps, her hands flying up to her breasts, squeezing them together for me, digging her fingers in deep to her own flesh."
    "I'm taking what's mine."
    "Unable and unwilling to hold back any longer, I take one of her full thighs in my hand and pull it against my body, using it as leverage as I draw back and slam myself back into her."
    "She's louder than I thought."
    "I expected reserved and modest from her, but she's letting loose, full-lunged gasps and moans and yelps as I fuck her, intermittently calling my name."
    "I can tell she's dreamed of this moment for a while."
    "To be honest, so have I."
    "I throb deep inside of her as I drive the both of us further and further into the throes of our pleasure, pounding her with every ounce of strength I have, losing myself as I watch her tits bounce in her hands."
    "Her tongue lolling out occasionally in the pure pleasure against her full bottom lip as she tries futilely to catch her breath."
    "I'm not going to last much longer like this, but it's obvious that neither is she."
    "Her moment comes first, her fingernails digging first into her breasts, then aimlessly down to her hips, one moving up to her mouth to press against her bottom lips as the other clutches desperately into my bedsheets."
    "I feel her spasming around my cock, twitching, and I know she's losing her mind even before she tells me so."
    if CONDOM:
        show lavish missionary orgasm vaginal condom
    else:
        show lavish missionary orgasm vaginal
    lavish.say "Yes... Yes! I'm cuh... cum... cumming..."
    "Her gasps reach a feverish pitch and she yelps, her legs latching forward and around me as her back arches sharply."
    "Both hands slapping down into my mattress to dig in deep as she shudders, grinding her hips greedily against my thrusts as she rides out her orgasm on my pulsing rod."
    "I'm about there with her, especially with her squirming, screaming, and drawing me in deeper, deeper into her as she cums."
    if not CONDOM:
        show lavish missionary orgasm vaginal creampie
        $ lavish.impregnate()
    with hpunch
    "It takes only a few more solid thrusts before I bust, too..."
    with hpunch
    "...groaning and gripping the flesh of her thighs as I pump my load deep inside of her..."
    with hpunch
    "...her spasming walls milking what feels like every last drop out of me."
    with hpunch
    "Her breaths are shuddered whimpers as I pull out, collapsing onto the bed next to her."
    return

label lavish_fuck_date_cowgirl(sexperience_min):
    hide lavish
    show lavish cowgirl
    with fade
    "We topple onto the bed in a tangle of limbs."
    "I land on my back with Lavish atop me."
    "She tries to struggle upright, but I hold onto her tightly."
    "Almost instantly she stops trying to escape and instead gives in."
    "All the energy that Lavish was putting into that effort goes elsewhere."
    "And she uses it to begin pushing down on me, wriggling as she does so."
    "I can feel her pussy rubbing against my cock the whole time."
    "It's wet and slick, begging to be fucked."
    "And if I don't take control of things, it'll be inside of her in mere moments!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Don't get me wrong, I want to be inside of Lavish right now."
            "There's nothing that I want more than that."
            "But I want to have some say in how and where it happens too!"
            "She's almost desperate, and so am I."
            "Neither of us wants to stop and take precautions."
            "So that leaves me with only one other option..."
            lavish.say "Oh..."
            lavish.say "Oh, [hero.name]..."
            lavish.say "I love it when you squeeze my ass like that!"
            "I smile up at Lavish, grateful for the distraction."
            "It means that I can part her buttocks a second later."
            show lavish cowgirl anal ahegao
            "And then pull her down and onto me without warning."
            lavish.say "Ah..."
            lavish.say "Oh...my...god...oh my god..."
            lavish.say "Your cock...it's in...my ass!"
            "I see every fraction of an inch written on Lavish's face."
            "Every tiny degree that my cock sinks into her ass."
            "And that makes the sensation of so much sweeter too."
            show lavish cowgirl pleasure
            "Lavish bites her lips and whimpers a little."
            "But she makes no objection and never tries to stop me."
            "In fact, by the time she's taken me in the whole way, a change has come over her."
            "Slowly her expression transforms into one of odd surprise, and then pleasure."
            "Now her whimpers are turning into gasps as her muscles surrender."
            lavish.say "It feels...good!"
            lavish.say "Please, [hero.name]..."
            lavish.say "I want more!"
            "What the lady wants, the lady gets!"
            "I begin slowly, moving in and out of her a little with each thrust."
            "But it soon becomes apparent that Lavish wasn't kidding."
            "She wants more, and only seems happy when she's getting it!"
            "Soon enough my speed has picked up and I'm pounding her hard."
            "Lavish takes all that I have to give her, soaking it up like a sponge."
            "But the more she gets, the greater her appetite seems to become."
            "I'm supposed to be the one that's got her in the palm of my hand."
            "And yet she's dictating the pace, demanding all that I can give her!"
            show lavish cowgirl ahegao
            "Lavish is moaning and crying out, not forming any actual words."
            "But I know without needing to be told that she's urging me on."
            "I'm so distracted that I hardly notice I'm about to cum..."
            call cum_reaction (lavish, 'anal', sexperience_min) from _call_cum_reaction_104
            if _return == 'anal_inside':
                show lavish cowgirl creampie with vpunch
                $ lavish.sub += 2
                "Lavish only stops urging me to fuck her harder when I lose it."
                with vpunch
                "My cock is buried deep inside of her as I shoot my load."
                with vpunch
                "And she falls silent as I fill her, gasping and wide-eyed."
                with vpunch
                "I can feel her muscles twitching around my cock, squeezing it tight."
                show lavish cowgirl pleasure out dickcum
                "A moment later she cums too, clinging onto me for dear life."
                "My cock slides out of Lavish as she slumps onto me."
                "She's slick with sweat, quivering with exhaustion."
                "And I wrap her in my arms as she gasps against my chest."
            elif _return == 'anal_outside':
                show lavish cowgirl out pleasure
                show sexinserts chest lavish zorder 1 at center, zoomAt(1, (700, 770))
                show sexinserts belly lavish as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "Lavish moans in disappointment as I pull my cock out of her."
                "But she only has a moment to contemplate her loss."
                show lavish cowgirl cumshot with vpunch
                "Because a second later I shoot my load all over her belly and breasts."
                show sexinserts chest lavish cum zorder 1 at center, zoomAt(1, (700, 770))
                show sexinserts belly lavish cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                with vpunch
                "Taken by surprise, she has no chance to cover herself."
                show lavish cowgirl dickcum bodycum -cumshot with vpunch
                $ lavish.sub += 1
                "And so the sticky strands of cum strip her slick skin."
                "It's then that she seems to cum too, quivering all over."
                "Lavish reaches instinctively for her breasts, pinching her nipples."
                "And as she tries to find release, she massages the cum into her skin."
                "I lay back and watch, enjoying the show that she's putting on for me."
                hide sexinserts
            $ lavish.flags.anal += 1
        "Fuck her pussy":
            "Not that I don't want to get inside of Lavish, you understand?"
            "I just want to do it on my own terms!"
            call check_condom_usage (lavish, 175) from _call_check_condom_usage_74
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show lavish cowgirl condom
            "Now that we're all set to go, I take a firm hold of Lavish around the waist."
            "She lets out a yelp of surprise, which quickly turns into a giggle of delight."
            "And that's because she feels the sensation of my cock against her pussy."
            "I'm guessing it must feel good on her side, because it feels fantastic from mine!"
            lavish.say "Hey..."
            lavish.say "Enough teasing, [hero.name]!"
            "Well, how can I argue with a demand like that?"
            show lavish cowgirl vaginal
            "Not wasting another moment, I pull Lavish downwards."
            "At the same time I push upwards from below."
            "There's a wonderful few seconds of resistance."
            "And then she surrenders to me completely."
            "My cock slips between her lips and all the way into her."
            "I don't even think of stopping until I'm as deep as I can go."
            "Lavish sinks slowly down, everything she's feeling written on her face."
            "Her mouth hangs open."
            "And I can hear her panting almost desperately the whole time."
            "She hardly needs to nod in order to let me know she's liking it."
            "I can feel the need in her body, in every movement of her muscles."
            "My instinct is to hurry to meet that need, to go as fast as I can."
            "But I reign it in and instead begin with a slow, steady pace."
            "This means that Lavish gets a little of what she wants at a time."
            "Every gradual increase in speed still leaves her wanting more."
            "This way I can keep her feeling that same level of need."
            "And everything that I give her means that she feels it intensely."
            "Lavish grasps for every second of pleasure that she can get."
            "She winds herself up like a spring, more so with each second that passes."
            "Pretty soon she has her eyes screwed tightly shut."
            "And she's shuddering as I thrust in and out of her."
            "Lavish begins to whimper gently, nodding the whole time."
            "My guess is that she's on the verge of cumming."
            "And that's enough to push me over the edge too!"
            call cum_reaction (lavish, 'vaginal', sexperience_min, love_min=185) from _call_cum_reaction_105
            if _return == "vaginal_outside":
                "I want to keep right on going until the very end."
                "But I remember all too well that we're not using a condom."
                show lavish cowgirl out
                if not CONDOM:
                    show sexinserts chest lavish zorder 1 at center, zoomAt(1, (700, 770))
                    show sexinserts belly lavish as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "And so I make sure that I pull out before it's too late."
                "Lavish sighs in disappointment, but makes no effort to stop me."
                show lavish cowgirl cumshot with vpunch
                "She seems to cum as my cock slides out of her."
                if not CONDOM:
                    show sexinserts chest lavish cum zorder 1 at center, zoomAt(1, (700, 770))
                    show sexinserts belly lavish cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with vpunch
                    "Which means that she sighs and quivers as I shoot my load over her."
                    show lavish cowgirl dickcum bodycum -cumshot with vpunch
                    "It paints sticky, white stripes over her dark, perfect skin."
                    hide sexinserts
                $ lavish.love += 1
            elif _return == "vaginal_condom":
                "It's now that I'm glad I took the time to wear protection."
                "As it means that I can savour every moment, right to the end."
                with vpunch
                "Lavish and I climax at almost the same instant."
                with vpunch
                "I shoot my load and she tosses her head from side to side."
                with vpunch
                "We cling tightly to each other, refusing to be separated."
                show lavish cowgirl out cumshot
                "Then, as we relax, Lavish lies down atop me."
                "And I swear I can feel her heart beating against my chest."
            elif _return == "vaginal_inside_pill":
                lavish.say "Pill..."
                lavish.say "Remember..."
                lavish.say "I'm on the pill!"
                show lavish cowgirl creampie ahegao with vpunch
                $ lavish.love += 2
                "Lavish and I climax at almost the same instant."
                with vpunch
                "I shoot my load and she tosses her head from side to side."
                with vpunch
                "We cling tightly to each other, refusing to be separated."
                "Then, as we relax, Lavish lies down atop me."
                "And I swear I can feel her heart beating against my chest."
            elif _return == "vaginal_inside_pregnant":
                "We both know there's no danger in me going all the way."
                "And Lavish cradles her belly, as if to underline the point."
                show lavish cowgirl creampie ahegao with vpunch
                $ lavish.love += 3
                "Lavish and I climax at almost the same instant."
                with vpunch
                "I shoot my load and she tosses her head from side to side."
                with vpunch
                "We cling tightly to each other, refusing to be separated."
                "Then, as we relax, Lavish lies down atop me."
                "And I swear I can feel her heart beating against my chest."
            elif _return == "vaginal_inside_mad":
                lavish.say "No..."
                lavish.say "Stop - right now!"
                "Lavish comes to her senses before I do."
                "But it's still too late to avert disaster."
                with vpunch
                "I cum inside of her a moment later, as deep as I can go."
                show lavish cowgirl creampie with vpunch
                $ lavish.love -= 5
                $ lavish.impregnate()
                "Lavish stares down at me in horror."
                "And I stare back up, my face a mirror of hers."
                "Neither of us speaks, but we both know that we fucked up."
                "We fucked up big-time!"
            elif _return == "vaginal_inside_happy":
                lavish.say "No..."
                lavish.say "Don't stop now!"
                "Lavish catches me completely off-guard as she says this."
                "And that robs me of the chance to pull out before it's too late."
                show lavish cowgirl ahegao creampie with vpunch
                $ lavish.love += 5
                $ lavish.impregnate()
                "She gasps as I shoot my load into her, looking ecstatic."
                with vpunch
                "But all I can think of is the fact that I just came inside of her."
                "And I did so while not wearing a condom too!"
    return

label lavish_fuck_date_doggy(sexperience_min):
    if game.week_day % 2 == 0:
        hide lavish
        "Lavish turns her back."
        show lavish doggy with fade
        "She bends down, leaning on the bed, and beckons to me."
        call lavish_dick_reactions from _call_lavish_dick_reactions_2
        lavish.say "What are you waiting for?"
        lavish.say "I want you inside me, [hero.name]!"
        "I shake my head, like I'm shaking off a funk."
        "Lavish giggles at my enthusiasm."
        show lavish doggy mike lust
        "Kneeling down behind her, I reach out to touch Lavish..."
        "And I swear it almost feels like there's electricity when my fingers brush her skin!"
        show lavish doggy happy
        "Lavish looks back over her shoulder at me."
        "Her eyes telling me that she's more than ready to go..."
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "I don't know where the notion comes from."
                "It kind of just pops into my head out of nowhere."
                "But the moment it does, I can't think of anything else."
                "I aim my cock at the target."
                show lavish doggy anal
                "And I part Lavish's pert, perfect buttocks."
                lavish.say "Ooh!"
                lavish.say "What are you doing back there?"
                show lavish doggy pleasure
                lavish.say "Oh...oh my!"
                "Lavish begins to sigh as I push into her."
                "Her muscles fight to keep me out."
                "But she makes no effort to stop me."
                "And so I push into her a little at a time."
                show lavish doggy happy
                lavish.say "Oh, [hero.name]..."
                lavish.say "I didn't expect...this..."
                lavish.say "You...you feel SO good in there!"
                "There's a purring quality in Lavish's voice as she takes it."
                "Reminding me of a satisfied cat that's getting what it wants."
                "And the sound turns me on all the more."
                "By now I'm almost as deep inside of her as I can get."
                "It feels almost indescribable, like heaven."
                show lavish doggy lust
                "So when I start to move in and out, I keep it slow."
                "I want to enjoy this sensation for as long as I can."
                "And from the sounds she's making, so does Lavish!"
                "She spends the whole time pinned against the bed."
                "Leaning on her elbows, head on the palms of her hands."
                "All the time her ass is squeezing my cock."
                "Every movement I make it clasps and caresses me."
                "And at times I feel like I'm battling to keep from exploding."
                "But somehow I manage to keep from losing it too soon."
                "My stamina is just enough to hold on in there."
                show lavish doggy pleasure
                "To hold on until I can feel Lavish's ass surrender."
                "Finally those tight muscles begin to give up the fight."
                "And then her ass is as pliant as can be."
                "Only now do I begin to pick up the pace."
                "Lavish moans as I assert myself, her eyes glazing over."
                "I thrust my cock in and out of her ass without stopping."
                "This is the very last of my energy, the last reserve of stamina."
                "And when it runs out, there's nothing left to hold me back."
                "I feel myself let go..."
                call cum_reaction (lavish, 'anal', sexperience_min) from _call_cum_reaction_106
                if _return == 'anal_inside':
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.sub += 2
                    "Lavish's eyes roll back into her head as I cum."
                    with hpunch
                    "I can't get deeper than this, and she knows it."
                    with hpunch
                    "She pants and wriggles under me, struggling with all her strength."
                    "But there's nowhere for her to go, no escape from what's happening."
                    show lavish doggy pleasure
                    "Lavish lets out one last groan, and then she flops onto the bed."
                    "And if I weren't holding her up, I'm sure she'd collapse onto the floor!"
                elif _return == 'anal_outside':
                    show lavish doggy -anal happy
                    "I pull my cock out of Lavish's ass just in time."
                    "But I have to pin her to the bed in order to keep her upright!"
                    "She pants and wriggles under me, the muscles of her ass still twitching."
                    show lavish doggy cumshot pleasure with hpunch
                    $ lavish.sub += 1
                    "And then I shoot my load over her quivering buttocks."
                    with hpunch
                    "Lavish sighs as the cum rains down on her."
                    with hpunch
                    "She flops onto the bed, eyes rolling into her head."
                    "And if I weren't holding her up, I'm sure she'd collapse onto the floor!"
                $ lavish.flags.anal += 1
            "Fuck her pussy":
                "I can already see Lavish's pussy between her thighs."
                "Like her it's beautiful to behold, tight and enticing."
                "And the moment that I lay eyes on it, I know that I want it!"
                "I put my hands on Lavish's pert, perfect buttocks..."
                call check_condom_usage (lavish, 175) from _call_check_condom_usage_75
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show lavish doggy condom
                show lavish doggy vaginal lust
                "Lavish quivers as I rub the head of my cock against her pussy."
                lavish.say "Oh..."
                lavish.say "That's good..."
                lavish.say "That's what I want!"
                "It's just as she's urging me on that I slip inside."
                show lavish doggy pleasure
                "So as the lips of her pussy part, Lavish's words fade away."
                "In their place, she lets out a moan of pure release and satisfaction."
                "I do the best I can to push into her in one smooth motion."
                "And every second of that first push feels like sinking into heaven."
                "Part of me wants to prolong the moment, to remain still."
                "But my instinct is to satisfy Lavish."
                "And so I start to move back and forth slowly."
                "Every time I go back and forth, she nods, urging me on."
                "She soaks up all that I give her like a sponge."
                lavish.say "Ah..."
                show lavish doggy happy
                lavish.say "More, [hero.name]..."
                lavish.say "I want more!"
                "I have no idea what it would take for me to disobey Lavish now."
                "As I find myself leaping to meet her demands without a conscious thought."
                show lavish doggy pleasure
                "Before I even know it myself, I'm gaining speed rapidly."
                "I thrust my cock into and out of her faster with each second that passes."
                "And true to her word, Lavish takes everything that I have to give."
                "Lavish is almost clinging to be bed by now."
                "Holding on for dear life as I pound away."
                "But she shows no sign of letting up just yet."
                "Her head flops forwards, swaying with the motion of her body."
                "Yet she still nods and urges me on every chance that she gets."
                "At this rate, I'll be the one that passes out before the end!"
                "Because I don't know if I can satisfy her!"
                "It's just as this thought crosses my mind that I feel it."
                "The sensation of Lavish wriggling and writhing under me."
                "She must be about to cum!"
                "And that knowledge pushes me over the edge too!"
                call cum_reaction (lavish, 'vaginal', sexperience_min, love_min=185) from _call_cum_reaction_107
                if _return == "vaginal_outside":
                    "I pull my cock out of Lavish's pussy just in time."
                    show lavish doggy -vaginal happy
                    "But I have to pin her to the bed in order to keep her upright!"
                    "She pants and wriggles under me, the muscles of her ass still twitching."
                    show lavish doggy cumshot pleasure with hpunch
                    $ lavish.love += 1
                    "And then I shoot my load over her quivering buttocks."
                    with hpunch
                    "Lavish sighs as the cum rains down on her."
                    with hpunch
                    "She flops onto the bed, eyes rolling into her head."
                    "And if I weren't holding her up, I'm sure she'd collapse onto the floor!"
                elif _return == "vaginal_condom":
                    "Lavish's eyes roll back into her head as I cum."
                    show lavish doggy creampie with hpunch
                    "I can't get deeper than this, and she knows it."
                    with hpunch
                    "But the fact we used protection means we can enjoy every second."
                    with hpunch
                    "She pants and wriggles under me, struggling with all her strength."
                    "But there's nowhere for her to go, no escape from what's happening."
                    $ lavish.love += 1
                    "Lavish lets out one last groan, and then she flops onto the bed."
                    "And if I weren't holding her up, I'm sure she'd collapse onto the floor!"
                elif _return == "vaginal_inside_pill":
                    lavish.say "Mmm..."
                    lavish.say "Please cum in me!"
                    lavish.say "I'm on the pill!"
                    "I'm more than happy to do as Lavish asks."
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.love += 2
                    "Her eyes roll back into her head as I cum."
                    with hpunch
                    "I can't get deeper than this, and she knows it."
                    with hpunch
                    "She pants and wriggles under me, struggling with all her strength."
                    "But there's nowhere for her to go, no escape from what's happening."
                    show lavish doggy pleasure
                    "Lavish lets out one last groan, and then she flops onto the bed."
                    "And if I weren't holding her up, I'm sure she'd collapse onto the floor!"
                elif _return == "vaginal_inside_pregnant":
                    lavish.say "Mmm..."
                    lavish.say "Go ahead..."
                    lavish.say "I'm already knocked up!"
                    "I'm more than happy to do as Lavish asks."
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.love += 3
                    "Her eyes roll back into her head as I cum."
                    with hpunch
                    "I can't get deeper than this, and she knows it."
                    with hpunch
                    "She pants and wriggles under me, struggling with all her strength."
                    "But there's nowhere for her to go, no escape from what's happening."
                    show lavish doggy pleasure
                    "Lavish lets out one last groan, and then she flops onto the bed."
                    "And if I weren't holding her up, I'm sure she'd collapse onto the floor!"
                elif _return == "vaginal_inside_mad":
                    lavish.say "Oh god..."
                    lavish.say "You have to pull out!"
                    lavish.say "NOW!"
                    mike.say "Wha..."
                    mike.say "What the hell?!?"
                    "By the time I blurt out the words, it's already too late."
                    show lavish doggy creampie with hpunch
                    $ lavish.love -= 5
                    $ lavish.impregnate()
                    "I shoot my load inside of Lavish while she struggles to escape."
                    with hpunch
                    "I can hear her swearing and cursing, but I'm too stunned to move."
                    with hpunch
                    "Oh shit - what did I just do?"
                elif _return == "vaginal_inside_happy":
                    lavish.say "Mmm..."
                    lavish.say "Where'd you think you're going?"
                    mike.say "Lavish..."
                    mike.say "What are you..."
                    "By the time I blurt out the words, it's already too late."
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.love += 5
                    $ lavish.impregnate()
                    "I shoot my load inside of Lavish while she holds onto me."
                    with hpunch
                    "She seems ecstatic with the result of her actions."
                    with hpunch
                    "But I'm shocked and confused, unable to make sense of what she just did."
    else:
        hide lavish with fade
        "She clambers onto the bed, looking back over her shoulder."
        show lavish doggy with fade
        "Of course, all of her play-acting only serves to make me want her all the more."
        "And I'm stripped off and following her onto the bed in record time."
        call lavish_dick_reactions from _call_lavish_dick_reactions_3
        "I notice that Lavish is careful as to just how fast she moves."
        "Quick enough to make a good show of it, sure."
        "But also slow enough that I don't have too much trouble catching her!"
        "I grab lavish by the haunches, my hands making a dramatic crack as I do so."
        show lavish doggy mike lust
        "She obliges me by instantly ceasing her efforts to escape."
        "And instead she begins to wriggle and squirm in my grasp."
        lavish.say "Ah..."
        lavish.say "[hero.name]...you caught me!"
        show lavish doggy happy
        lavish.say "Now, what are you going to do with me?!?"
        "I don't waste even a second in answering that question."
        "I think we both know exactly what I have in mind right now."
        "And I'm pretty sure it's what Lavish has in mind too!"
        "Pulling Lavish backwards is the first clue that I give her as to my intentions."
        "Her buttocks slap against my thighs with an audible clap."
        "She yelps again, but I note that she also pushes against me too."
        "I can feel her grinding her ass into my groin."
        "And I don't need much more of an invitation than that!"
        if lavish.is_collared:
            "I grab hold of Lavish's collar with one hand."
            "With the other I snatch up a leash that's close to hand."
            "The lead clips to the collar with a metallic click."
            "And I wrap it around my wrist, using it to reign her in."
        "The head of my cock is already between her buttocks."
        "All I have to do now is decide exactly where it's going..."
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "Lavish is basically offering me her ass, right?"
                "So the logical thing to do is take it."
                "I take a firmer grip of her buttocks, parting them as I do so."
                "She gasps and glances back over her shoulder."
                "I can see that her eyes are full of curiosity and anticipation."
                "But I still don't think she's expecting what happens next!"
                show lavish doggy anal
                "I quickly push the head of my cock into her exposed hole."
                "Lavish shudders as she becomes aware of what I'm doing."
                lavish.say "Oh, [hero.name]..."
                lavish.say "Where are you going?"
                lavish.say "What are you doing to me?"
                show lavish doggy pleasure
                "It doesn't take long for Lavish to lose the power of speech."
                "With every inch that I make it into her ass, she becomes less coherent."
                "And by the time I'm up to my balls inside of her, she's moaning like and animal."
                "Of course, that sound only makes me want her more."
                "It doesn't take long for me to build up speed either."
                "In what feels like record time, I'm pounding Lavish for all I'm worth."
                "She writhes and tosses her head the whole time."
                "And I can feel the muscles of her ass quivering as I thrust in and out."
                "But she never once asks me to slow down or stop."
                show lavish doggy lust
                "Instead, when she looks back over her shoulder, I see her nod."
                "It's not just from the tossing of her head either."
                "Lavish actually catches my eye and nods her head emphatically."
                "And knowing that she's loving it spurs me on again."
                "I redouble my efforts, putting all of my energy into it."
                "Which is instantly rewarded with a cry from Lavish."
                "Or perhaps a growl would be closer to the truth!"
                "Because the sound that she makes isn't human at all."
                show lavish doggy pleasure
                "Lavish is just growling with sheer pleasure now."
                "Like every thrust is almost pushing her over the edge."
                "And she's not alone in that."
                "I can feel myself cumming too!"
                call cum_reaction (lavish, 'anal', sexperience_min) from _call_cum_reaction_108
                if _return == 'anal_inside':
                    "All it takes is one last push..."
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.sub += 2
                    "And then I shoot my load deep into Lavish's ass."
                    with hpunch
                    "She howls as I do so, like a wounded animal."
                    with hpunch
                    "But then she begins to pant and moan more gently."
                    "And I realise the first sound she made was on account of her cumming."
                    show lavish doggy pleasure
                    "As soon as she's done, Lavish slides off my cock and slums over."
                    "She collapses onto the bed and lies still, panting and exhausted."
                elif _return == 'anal_outside':
                    "I use the very last of my strength to pull out."
                    show lavish doggy -anal happy
                    "She howls as I do so, like a wounded animal."
                    "But then she begins to pant and moan more gently."
                    "And I realise the first sound she made was on account of her cumming."
                    show lavish doggy cumshot pleasure with hpunch
                    $ lavish.sub += 1
                    "I hold her up right as I shoot my load over her back and buttocks."
                    with hpunch
                    "But as soon as I loosen my hold on her, Lavish collapses onto the bed."
                    with hpunch
                    "And then she lies there, panting and exhausted."
                $ lavish.flags.anal += 1
            "Fuck her pussy":
                "I can already feel the lips of Lavish's pussy."
                "It's slick and wet, more than ready for me."
                "And so what's the point in holding back?"
                call check_condom_usage (lavish, 175) from _call_check_condom_usage_76
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show lavish doggy condom
                show lavish doggy vaginal lust
                "I waste no time in thrusting myself forwards."
                "And I'm rewarded with the sound of Lavish moaning a second later."
                "I can feel the head of my cock as it slides against her lips a second time."
                "And she's even more slick now than she was before."
                "This means that I'm almost inside of her before I know it's happening."
                "Lavish's pussy seems to swallow me whole, betraying how much she wants it."
                show lavish doggy pleasure
                "She nods almost desperately as I sink in as deep as I can go."
                "And her breath is coming in short, sharp gasps."
                lavish.say "Oh...Oh...yes..."
                lavish.say "Please...[hero.name]..."
                show lavish doggy happy
                lavish.say "Please...fuck me...hard!"
                "It's not like I need to be told to do that!"
                "And I'm already thrusting on and out of her as she begs me to do it."
                "Normally I'd take my time about something like this."
                "I'd start slow and build up, make sure she was on the same page as me."
                "But what's the point of that here and now?"
                "Especially when she's basically begging me to pound her senseless!"
                "And don't worry about me not taking my time and savouring he moment."
                "Because I'm enjoying myself right now, having a crazily good time!"
                "Being inside of Lavish feels incredible, like it's taking my breath away."
                show lavish doggy pleasure
                "Going this fast just seems to make it feel that much more intense."
                "My groin is slapping against her buttocks as I go at her."
                "And every time it does, she quivers from the impact."
                "But soon I can see that there's something else behind it too."
                "Lavish is beginning to shake on her own, like she's about to cum!"
                "And it looks like I am too..."
                call cum_reaction (lavish, 'vaginal', sexperience_min, love_min=185) from _call_cum_reaction_109
                if _return == "vaginal_outside":
                    "I have something else to worry about too."
                    show lavish doggy -vaginal happy
                    "And that's the fact I'm not wearing a condom!"
                    "I manage to pull out a moment before it's too late."
                    "Which leaves Lavish gasping and twitching as she cums."
                    show lavish doggy cumshot pleasure with hpunch
                    $ lavish.love += 1
                    "I shoot my load almost as soon as I'm out of her."
                    with hpunch
                    "So as Lavish slumps for wards, I paint her back with white stripes."
                    with hpunch
                    "She lays there, panting as it rains down on her back, buttocks and thighs."
                elif _return == "vaginal_condom":
                    "Luckily for me, we remembered to take precautions."
                    show lavish doggy creampie with hpunch
                    "So all I have to worry about is enjoying the moment."
                    with hpunch
                    "I don't know which one of us actually cums first."
                    with hpunch
                    "But I can see the effect it has on Lavish."
                    with hpunch
                    "She rides my cock until it's all over."
                    "And then she slumps forwards onto the bed."
                    "Which leaves me kneeling upright, panting for breath."
                elif _return == "vaginal_inside_pill":
                    lavish.say "I'm on the pill!"
                    lavish.say "It's okay...I'm on the pill!"
                    "I didn't need to be reminded of the fact."
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.love += 2
                    "And I'm already cumming as Lavish desperately does just that."
                    with hpunch
                    "She rides my cock until it's all over."
                    show lavish doggy pleasure with hpunch
                    "And then she slumps forwards onto the bed."
                    "Which leaves me kneeling upright, panting for breath."
                elif _return == "vaginal_inside_pregnant":
                    "Lavish's swelling belly is a constant reminder of her being pregnant."
                    "But now it also means I can go all the way without worrying about it too!"
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.love += 3
                    "And so I do just that, shooting my load into her without stopping."
                    with hpunch
                    "She rides my cock until it's all over."
                    with hpunch
                    "And then she slumps forwards onto the bed."
                    "Which leaves me kneeling upright, panting for breath."
                elif _return == "vaginal_inside_mad":
                    lavish.say "Stop..."
                    lavish.say "[hero.name]..."
                    lavish.say "You have to stop!"
                    "But for all of her protesting, it's already too late."
                    with hpunch
                    "I feel myself cumming, deep inside of Lavish."
                    show lavish doggy creampie with hpunch
                    $ lavish.love -= 5
                    $ lavish.impregnate()
                    "She looks back over her shoulder at me."
                    "She's horrified and I'm stunned into silence."
                    "I just came in her - and without a condom too!"
                elif _return == "vaginal_inside_happy":
                    lavish.say "Don't stop now!"
                    lavish.say "[hero.name]..."
                    lavish.say "Don't you dare stop!"
                    "I can't seem to make sense of what Lavish is demanding."
                    "She's confusing me, making me second-guess myself."
                    show lavish doggy creampie ahegao with hpunch
                    $ lavish.love += 5
                    $ lavish.impregnate()
                    "And that's all it takes for me to shoot my load inside of her."
                    with hpunch
                    "She looks ecstatic, but I can feel my guts turn to water."
                    "I just came in here without a condom!"
    return

label lavish_sleep_date_fuck(location="hero"):
    scene bg bedroom1
    show cuddle lavish
    with fade
    "Within seconds she's magnetized to my side, the soft skin of her palm sliding across my chest as her beautiful face nestles in to my shoulder."
    "Her full, long lashes are closed, resting daintily against her cheeks, her expression that of peaceful, dreamy bliss."
    "I feel it flood through me, too, at the sight, and, sighing contentedly, I curl my arm around her and let my eyes fall closed, too."
    scene bg bedroom1
    call sleep ("lavish") from _call_sleep_60
    $ game.room = "bedroom1"
    return

label lavish_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "It took a little bit of convincing on my part, but I finally sold Lavish on the idea of the hot-tub."
    "Well, to be more precise, the idea of the hot-tub at my place and her coming over to take a dip in it."
    "I had to assure her it'll be just the two of us and that no one will be able to see us while we're in there."
    "But once she's had enough time for the notion to sink in, she seems really excited at the prospect."
    "And needless to say I'm more than a little excited too!"
    "I'd like to be able to say that it's just for the chance to spend some quality time with Lavish."
    "But I'd be lying if I said I wasn't looking forward to seeing her in a swimsuit!"
    "All the same, I try to play it straight as I sit in the tub and wait for Lavish to join me."
    "There's no point in making myself look like a drooling pervert and scaring her off."
    "Not before I've managed to convince her that a little bit of perversion might be a good thing!"
    lavish.say "Ready or not, [hero.name]."
    lavish.say "Here I come!"
    "I can tell from the sound of her voice that Lavish is trying her best to sound confident."
    "But the hints are still there under the surface, telling me that she's nervous."
    show lavish swimsuit with dissolve
    "I look up to see her hurrying towards the tub, still wrapped in a towel."
    "She lifts one shapely, elegant leg over the side."
    "But then she stops, as if realising for the first time that she hasn't shed the towel."
    mike.say "Probably best if you leave that out of the tub, Lavish!"
    "I see her cheeks flush at this."
    "But she shakes it off and unwraps the towel all the same."
    lavish.say "Sure...of course..."
    lavish.say "How silly of me!"
    "I start to say something that I hope will be reassuring."
    "And then the words die in my throat as I see what's under the towel."
    "I swallow audibly at the sight of Lavish's body in the tight, revealing swimsuit."
    "How can a girl so hot be worried about anyone seeing what I can see right now?"
    "She's practically perfect in every way!"
    hide lavish
    show hottub lavish
    with fade
    lavish.say "What's the matter, [hero.name]?"
    lavish.say "Why are you staring at me like that?"
    mike.say "I...I'm sorry, Lavish."
    mike.say "You just look so...well, so amazing!"
    "Lavish's cheeks become a deeper shade of red as she hears the compliment."
    "She looks away for a moment, shaking her head like she thinks I'm kidding her."
    lavish.say "I thought it might be too revealing, you know?"
    lavish.say "But if you like it..."
    mike.say "I love it, Lavish!"
    "Lavish smiles as she lowers herself into the water."
    "And my approval seems to go a long way to curing her former shyness."
    "She inches over to where I'm sitting and leans almost close enough to touch me."
    lavish.say "Mmm..."
    lavish.say "The bubbles feel really nice against my skin!"
    "Lavish kicks her legs up and down a little in the water, splashing as she does so."
    "But then she seems to become aware of herself again."
    "And she stops as quickly as she started."
    lavish.say "So..."
    lavish.say "What do you do when you're in here, [hero.name]?"
    mike.say "Well, it depends on the kind of mood I'm in."
    mike.say "Sometimes I like to hang out with friends."
    lavish.say "Like we're doing now?"
    mike.say "Yeah, Lavish, I guess so."
    mike.say "And sometimes I just like to relax, you know?"
    "Lavish smiles sweetly at me, but then she looks down at the water."
    "I see her eyes go wide as she notices something under the surface."
    lavish.say "Well, I can see one part of you that's definitely not relaxed!"
    "I follow her gaze, only realising as I do so that I have a massive erection."
    "It's so large that it's actually straining the elastic of my trunks."
    "I must have gotten so used to having a hard-on around Lavish that I don't notice anymore!"
    mike.say "Oh...well..."
    mike.say "I did say that you looked amazing just now, Lavish."
    mike.say "And I meant it too!"
    "Lavish bites her lip as she looks down at my groin."
    "The look in her eyes is beginning to change."
    "She's starting to look almost hungry."
    "To look as though she sees something that she wants!"
    lavish.say "Ah, [hero.name]..."
    lavish.say "Your housemates are all out, right?"
    mike.say "Yeah, Lavish."
    mike.say "There's only the two of us here."
    lavish.say "And nobody can see what we're doing?"
    mike.say "I already said so."
    mike.say "But yeah, this part of the house is totally private."
    "Lavish surprises me then by leaning in close and grabbing hold of my cock."
    lavish.say "Then we could totally do it in here!"
    lavish.say "And no one would find out!"
    "Wait a minute..."
    "Is she actually suggesting we have sex herself?!?"
    "That's what I've been trying to build up to all this time!"
    mike.say "S...sure, Lavish..."
    mike.say "If that's what you want to do!"
    "My voice falters a little and I stutter out the words."
    "On the one hand this is because I don't want to sound too eager."
    "But on the other it's also on account of just how hard a grip she has on my cock!"
    lavish.say "I think we should just go crazy and do it, [hero.name]."
    lavish.say "Then it can be our little secret that we did it in a hot-tub!"
    show hottub sex male lavish outside with fade
    "I nod and begin to pull down my trunks, Lavish still holding my cock the whole time."
    "And as soon as I'm free of them, she aims it straight between her thighs."
    call lavish_dick_reactions from _call_lavish_dick_reactions_4
    "Lavish sits down on it slowly, smiling over her shoulder at me as she does so."
    "But when I start to feel it pressing against the lips of her pussy, her expression changes."
    show hottub sex male lavish inside
    "Now she starts to breath more heavily, almost whimpering as it pushes inside of her."
    "The sound is a massive turn on, matching the look in her huge, doe-like eyes."
    "Lavish nods, letting me know that she's liking the sensation too."
    "And by the time I'm balls deep in her, it feels more like I'm in heaven!"
    "As soon as she's conquered her misgivings, Lavish is a woman unleashed."
    "She doesn't just lie back and let me do all the work."
    "Instead she rides my cock like it's a wild horse, grinding on me ever harder."
    "And she practically grabs my hands, guiding them to her breasts."
    "Lavish's nipples are stiff as I squeeze them between my fingers."
    "She rewards my efforts by squealing with delight."
    "I swear that the muscles of her pussy clamp down that much harder on my cock too."
    "It's more than I can take, and I can already feel myself cumming..."
    call cum_reaction (lavish, 'vaginal', 1) from _call_cum_reaction_110
    if _return == "vaginal_outside":
        "It might feel like Lavish has a firm hold on me, but I know better."
        show hottub sex male lavish outside
        "And all it takes is a backwards motion from me to free my cock at the last moment."
        "Lavish moans as she feels me pull out of her pussy, quivering as I go."
        show hottub sex male lavish cumshot with vpunch
        $ lavish.sub += 1
        "But then I cum, shooting my load up her stomach and onto her breasts."
    else:
        "I feel almost like Lavish is milking me with her pussy, determined not to let me go."
        "And if that's the case, it works like a charm."
        $ lavish.love += 1
        show hottub sex male lavish cumshot with vpunch
        "I lose it moments later, filling her with everything I have to give."
        show hottub sex male lavish ahegao with vpunch
        "Lavish quivers and twitches as she takes it, gasping with each and every thrust."
    hide hottub
    show hottub lavish
    with fade
    "Lavish wraps her arms around my neck and collapses against me once it's over."
    "Her breath comes in little pants and I can feel her heart beating quickly in her chest."
    "But she makes no complaints, allowing me to hold her as she recovers from her exertions."
    "And it's something that I'm more than happy to do, enjoying the feel of her body against mine."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ lavish.sexperience += 1
    $ game.active_date.clothes = None
    return

label lavish_fuck_mc_office:
    $ game.play_music("music/roa_music/city_nights.ogg")
    lavish.say "How can I help you today [hero.name]?"
    call office_harem_fuck_choices ('lavish') from _call_office_harem_fuck_choices_2
    return

label lavish_fuck_office_choices:
    menu:
        "Spank her" if lavish.flags.start_spanking and not lavish.flags.spankingdelay:
            call lavish_office_spank from _call_lavish_office_spank
        "Give me a blowjob" if "lavish_office_bj" in DONE:
            call lavish_office_bj (True) from _call_lavish_office_bj
        "Forget it":
            lavish.say "All right [hero.name]."
            $ hero.cancel_activity()
    return

label lavish_office_spank:
    mike.say "I'd like to spank you, Lavish."
    lavish.say "Okay, let's..."
    show lavish surprised
    lavish.say "Wait...what?!?"
    mike.say "You heard what I said, Lavish."
    mike.say "I want to spank you."
    mike.say "It get's my blood flowing, makes me more efficient."
    mike.say "So I'll be that much more attentive when I write you annual report for HR this afternoon!"
    show lavish angry
    lavish.say "This is blackmail!"
    mike.say "I'd say it's more of a chance for you to earn some karma in the workplace, Lavish!"
    "Lavish looks at the door and then back at me."
    "I can see that her mind's racing as she weighs up her options."
    show lavish embarrassed
    lavish.say "Okay, okay..."
    lavish.say "But you'd better make it quick!"
    show lavish wink blush
    lavish.say "And I'd better get a shining writ-up in your report too!"
    "I nod and smile, pushing my chair back from the desk."
    "I'm about to pat my thigh to show Lavish where I want her."
    hide lavish
    show spank lavish
    with fade
    "But she's around the desk and hitching up her skirt before I have the chance!"
    "Lavish lies herself down over my lap, ass bared and ready for whatever comes next."
    lavish.say "Just do me one favour, okay?"
    mike.say "Anything, Lavish - just name it!"
    lavish.say "Tell me off like I'm not working hard enough, okay?"
    mike.say "Sure, Lavish, if that's what you want..."
    show spank lavish up
    "Lavish nods and then stares at the wall."
    show spank lavish spank surprised
    play sound spank
    with hpunch
    "I shake my head and give her the first slap across the ass."
    mike.say "Your work isn't good enough, Lavish!"
    "She yelps and wriggles in my lap."
    show spank lavish up
    "But I can't tell if it's from the slap or the verbal dressing down!"
    mike.say "You're sloppy and lax - you need to shape up!"
    show spank lavish spank
    play sound spank
    with hpunch
    "Lavish gasps as more slaps crack against her buttocks."
    "And I use all the bullshit office talk I know to dress her down."
    show spank lavish up
    pause 0.3
    show spank lavish spank marks
    play sound spank
    with hpunch
    "Her ass cheeks are turning red from the spanking."
    "And the cheeks on her face are burning with shame too!"
    show spank lavish up
    pause 0.3
    show spank lavish spank
    play sound spank
    with hpunch
    mike.say "You're lazy, Lavish - and you need to be taught a lesson!"
    mike.say "I'll keep on spanking you until you're a model employee!"
    show spank lavish ready
    lavish.say "Mmm..."
    show spank lavish up
    lavish.say "I know I'm a bad girl..."
    show spank lavish spank
    play sound spank
    with hpunch
    lavish.say "Please...punish me...make me behave!"
    show spank lavish ready
    lavish.say "I'll be good...I promise I will!"
    "By the time we're finished, both of us are panting like crazy."
    hide spank
    show lavish flirt
    "Lavish gets up from my lap and gingerly pulls down her skirt."
    $ lavish.sub += 1
    $ lavish.flags.spankingdelay = TemporaryFlag(True, 1)
    $ lavish.flags.spank_counter += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
