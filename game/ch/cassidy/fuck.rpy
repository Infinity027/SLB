init python:
    InteractActivity(**{
    "name": "cassidy_fuck_mc_office",
    "display_name": "Fuck",
    "label": "cassidy_fuck_mc_office",
    "conditions": [
        HeroTarget(HasRoomTag("mcoffice")),
        PersonTarget(cassidy,
            IsActive(),
            IsFlag("status", "pet", "sex slave"),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    "music": "music/roa_music/no_regrets.ogg"
    })

    Event(**{
    "name": "cassidy_hottub_sex_male",
    "label": "cassidy_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(cassidy,
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
    "name": "fuck_cassidy",
    "display_name": "Fuck",
    "label": "cassidy_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(cassidy,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })


label cassidy_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "Ever since she heard that I have a hot-tub, Cassidy's been bugging me to use it."
    "And trust me, it's not like I don't want to have her over and hop in there with her."
    "I mean, who wouldn't want that, right?"
    "It's just that something always seemed to come up when I'd remember she wanted to come over."
    "Which means that by the time I finally manage to invite her, Cassidy's almost champing at the bit!"
    show cassidy swimsuit with dissolve
    "I'm already in my trunks when she turns up, with the tub all ready and bubbling away."
    cassidy.say "Hi, [hero.name]!"
    cassidy.say "I got here as fast as I could."
    "I can't help smiling like a fool at Cassidy's enthusiasm."
    "It makes her look even more stunning than usual - if that's even possible!"
    mike.say "Hey, Cassidy."
    mike.say "You're here, that's all that matters."
    "I cock my head towards the hot-tub, inviting her to follow me over there."
    mike.say "You see, it does actually exist."
    mike.say "I hope it was worth the wait."
    "Cassidy nods as she walks over to join me by the side of the tub."
    "She seems happy with what she sees, if not blown away by it."
    "And a thought occurs to me then."
    "Something that's been on my mind the whole time."
    mike.say "Cassidy..."
    cassidy.say "Yeah, [hero.name]?"
    mike.say "You've been in a hot-tub before, right?"
    mike.say "I mean, you wanted to come over and try mine out so badly."
    mike.say "I just wondered why?"
    "Cassidy chuckles at my question and rolls her eyes."
    cassidy.say "Don't be silly, [hero.name]."
    cassidy.say "Of course I've been in one before!"
    cassidy.say "Daddy always had a hot-tub."
    cassidy.say "But I never did it inside..."
    "Before I can fully comprehend what she just said, Cassidy takes off her coat."
    "She lets it drop to the ground in a deliberate gesture intended to grab my attention."
    "And it sure does, as she's wearing nothing underneath except her swimsuit!"
    mike.say "I..."
    mike.say "Erm..."
    mike.say "Wow, Cassidy..."
    show cassidy happy
    "Cassidy laughs again, louder this time."
    "And her entire body shakes as she does so."
    "All of which means my eyes become wider with every passing second."
    show cassidy normal
    cassidy.say "You wanna do it, [hero.name]?"
    cassidy.say "Then come on, what are you waiting for?"
    hide cassidy
    show hottub cassidy
    with fade
    "With that, Cassidy turns her back on me and climbs into the tub."
    "She glances back over her shoulder, making sure that I'm following."
    "But she needn't have worried, as I'm practically on her heels!"
    "Cassidy lets out another one of those intoxicating chuckles as she sinks into the water."
    "I reach out as I slide into the tub after her, but she slips out of my grasp."
    "By now my cock is getting painfully hard for her."
    "And as when she eludes me, I swear I can feel a twinge of need down there!"
    "When I finally catch her on the far side of the tub, I grab Cassidy and hold on tight."
    "She yelps and squeals with sheer delight, thrashing about in the water as I do so."
    cassidy.say "Oh, [hero.name] - you got me!"
    cassidy.say "Whatever are you going to do with me, huh?"
    "I couldn't answer that even if I tried."
    "And that's because I'm already yanking down my trunks with one hand."
    show hottub sex male cassidy outside with fade
    call cassidy_dick_reactions from _call_cassidy_dick_reactions
    "The other I keep on Cassidy as she squirms and wriggles before me."
    "Her giggles turn into moans of anticipation as I finally pin her down."
    show hottub sex male cassidy inside
    "And Cassidy looks back over her shoulder as I push my cock between her thighs."
    "She holds my eye the entire time, so I can see every moment of her reaction."
    "Which makes the sensation of pushing inside her tight pussy that much more intense."
    cassidy.say "Oh..."
    cassidy.say "Oh, [hero.name]..."
    cassidy.say "You're so big!"
    mike.say "Shit, Cassidy..."
    mike.say "I want to fuck you so hard!"
    cassidy.say "Mmm..."
    cassidy.say "So do I!"
    "That's all the permission I need."
    "I make one final thrust, pushing my cock as deep into Cassidy as I can."
    "Her words trail off into a deep, almost desperate moan."
    "A moan that sounds almost as good as it feels to be inside of her."
    "But I don't waste any time in savouring the moment."
    "Instead I begin to pound Cassidy with all my might."
    "There's a time to be subtle and use the lightest touch."
    "And this is definitely not it!"
    "Cassidy lets me know that this is what she wants by nodding her head desperately."
    "But I hardly need the reassurance, as he body responds in kind."
    "No matter how much I give her, Cassidy takes it almost greedily."
    "She soaks it up and seems to ask for more!"
    "By now, Cassidy is panting, her eyes glazing over as I pound her."
    "I'm putting so much into each and every thrust, I expect to cum with each one."
    "But somehow the sheer excitement that I get from doing Cassidy keeps me going."
    "Evert thrust seems to push her further and make me want her that much more!"
    "So when I finally do feel myself starting to cum, it takes me by complete surprise..."
    menu:
        "Cum inside":
            "I'm so deep into Cassidy and so lost in the moment I can't hope to pull out."
            $ cassidy.love += 1
            show hottub sex male cassidy cumshot with hpunch
            "All I can do is grab hold of her and cling on for dear life as I cum."
            show hottub sex male cassidy ahegao with hpunch
            "She quivers as I grasp her haunches and pull her backwards."
            with hpunch
            "And then she actually whimpers as I shoot my load into her."
        "Pull out":
            show hottub sex male cassidy outside
            "It takes the very last of my energy to pull it off in time."
            show hottub sex male cassidy cumshot with hpunch
            $ cassidy.sub += 1
            "But somehow I manage to drag my cock out of Cassidy the moment before I cum."
            with hpunch
            "Her entire body quivers at the sensation and she whimpers quietly."
            with hpunch
            "All I can do is pant as I shoot my load over her ass and thighs."
    "Cassidy and I collapse into the water, our muscles turning to jelly in a moment."
    "There's no way either of us can hold onto the other, our limbs are too weak."
    "Instead we end up in a tangle of limbs, floating together in the bubbling water."
    "We can't speak either, only pant and gasp as we try to slow our hammering heartbeats."
    "But all the same, I feel Cassidy rest her head gently on my shoulder, pressing herself against me."
    "And that tells me, as sure as words ever could, that she's happy and satisfied with my efforts."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ cassidy.sexperience += 1
    $ game.active_date.clothes = None
    return

label cassidy_fuck_date_nudistbeach:
label cassidy_fuck_date_beach:
label cassidy_fuck_beach:
    $ game.play_music("music/roa_music/no_regrets.ogg")
    scene bg beach
    show cassidy
    "The sun is shining, the sky is a clear blue, studded with wispy and the sea seems to stretch on forever."
    "All in all, it's the perfect day to be at the beach, when nature's looking too good to be true."
    "But the one thing that's looking even better right now is Cassidy, sitting beside me on the sand!"
    "Seriously, she's making it super hard to appreciate the natural beauty all around us."
    "Because all I want to do is spend the whole time staring at her!"
    show cassidy angry
    cassidy.say "Hey!"
    cassidy.say "Will you quit doing that?"
    "I turn my head away the moment that she says this, trying to play the innocent."
    mike.say "What are you talking about, Cassidy?"
    mike.say "I wasn't doing anything!"
    cassidy.say "Oh, the hell you weren't!"
    cassidy.say "You're so full of it, [hero.name]!"
    show cassidy normal blush
    "As soon as I sneak a look back in her direction, I see Cassidy smirking."
    "And she's actually blushing a little too, letting me know what to do next."
    "When a girl's enjoying a gentle bit of teasing, you'd best go with it."
    mike.say "Okay, Cassidy, okay."
    mike.say "You got me - bang to rights."
    mike.say "I just can't stop looking at you!"
    mike.say "But you're right - I'll look at something else instead."
    mike.say "Maybe there's a cute seagull that I could stare at?"
    mike.say "Or a hot seal?"
    show cassidy happy
    "Cassidy shakes her head, blushing even more."
    cassidy.say "Oh, stop it!"
    cassidy.say "I don't mind you looking at me, okay?"
    show cassidy normal
    cassidy.say "I just don't like you being all furtive about it."
    cassidy.say "It's fine to look at me and for me to know you're looking at me..."
    "Cassidy stops and shakes her head again, realising that she's beginning to babble."
    mike.say "I get it, Cassidy."
    mike.say "No need to tie yourself up in a knot!"
    "Cassidy sighs and gives me a smile."
    "But I can see there's something else on her mind."
    show cassidy annoyed
    cassidy.say "I'm sorry, [hero.name]."
    cassidy.say "It's not just that."
    cassidy.say "I'm...well..."
    cassidy.say "Feeling a little...frisky...you know?"
    "I nod my head eagerly at this, suddenly feeling myself come alive."
    "In truth I had no idea that Cassidy was up for anything of an amorous nature."
    "But sitting next to her in that swimsuit's given me a case of sex on the brain!"
    mike.say "Ah...yeah, Cassidy."
    mike.say "I can understand that!"
    show cassidy normal
    show fx exclamation
    cassidy.say "You can?"
    show cassidy happy
    cassidy.say "Oh thank god for that - I thought it was just me!"
    cassidy.say "Being out here in nature, you're supposed to commune with it."
    cassidy.say "But here I am, just thinking about sex!"
    "I shrug as I try to explain Cassidy's concerns away."
    mike.say "Well...sex IS perfectly natural, Cassidy."
    mike.say "So if we did it, we'd kind of be communing with nature, right?"
    show cassidy normal
    "Cassidy cocks her head on one side as she considers my point."
    show cassidy happy
    "And then she gives me a smile and a quick nod."
    "A smile that I can feel make my cock beging to harden."
    if game.room != "date_nudistbeach":
        show cassidy naked
        "Before I can say another word, Cassidy begins to strip off her swimsuit."
        "I look around, worried that somebody might be able to see."
        mike.say "Cassidy!"
        mike.say "What are you doing?!?"
        cassidy.say "Just what comes naturally!"
        show cassidy normal
        cassidy.say "Come on, [hero.name]!"
        cassidy.say "Who cares if someone sees us?"
        cassidy.say "That's their problem!"
        "I hesitate for a moment, torn between my desire for her and the fear of discovery."
        "But in the end, it's my desire that wins out."
        "I follow Cassidy's example and tear off my shorts."
    show cassidy happy
    "She giggles in surprise at the sudden show of enthusiasm on my part."
    show cassidy cowgirl beach with fade
    "And then she turns over, quickly climbing on top of me."
    "I don't need to be told that this is an open invitation."
    "I'm up and taking hold of her around the waist a moment later."
    "Cassidy lets out a cry of surprise as I grab her."
    "But then she follows that with a gasp of anticipation."
    "And that's because I slide my cock between her thighs and upwards."
    "I can almost feel Cassidy's pussy starting to get wet."
    "Her lips becoming slicker every time the head of my cock strokes them."
    cassidy.say "Hmm..."
    cassidy.say "That feels good!"
    "I smile as Cassidy seems to be speaking for the both of us."
    "But the sensation gets even better a moment later."
    show cassidy cowgirl pleasure vaginal
    "Because that's when the lips of her pussy begin to part."
    "My cock inches its way inside of her, a little at a time."
    "I have the urge to push as hard and fast as I can."
    "But somehow I manage to hold back and draw it out."
    cassidy.say "Oh, [hero.name]..."
    cassidy.say "That feels even better!"
    "Everything seems to flow naturally from that point on."
    "Like we really are making love and communing with nature all at once."
    "Cassidy rides me slowly and surely, using her weight to great effect."
    "At times it seems like she's hardly moving at all."
    "The sunlight means that sometimes she's outlined like a silhouette."
    "But then the sun will disappear behind a cloud, letting me see her again."
    "When this happens it almost takes my breath away, as it reveals Cassidy in all her glory."
    "She runs her hands through her hair, traces the lines of her body and clutches her breasts."
    "All the time she's riding my cock with a deliberate motion."
    "Her face is a work of art too, expressing all that she's feeling."
    "Cassidy has her eyes closed the whole time, her mouth open."
    "And I swear I can feel my movements matching her breathing in and out."
    "All I can do is watch her as she rides me."
    "I seem to lose track of time, getting lost in the moment."
    "So when I feel myself about to cum, it's like being jolted back to reality."
    "Cassidy feels it too, her face becoming animated at the same time."
    cassidy.say "Oh..."
    cassidy.say "I can...I can feel it..."
    cassidy.say "Here it comes!"
    show cassidy cowgirl creampie ahegao with vpunch
    "I let go without holding a single thing back, giving myself over to the moment."
    with vpunch
    "Cassidy nods and bites her lip as I fill her with everything I have."
    with vpunch
    "Desperate whimpers of pleasure escape from her as she bucks on my cock."
    "And as my orgasm subsides, she begins to slow down too."
    "But the whole time she looks down over me, smiling with satisfaction."
    show cassidy cowgirl pleasure dickcum -creampie -vaginal
    "Cassidy lowers herself down onto me, letting my cock slide out of her."
    "She lays half atop me and half on the ground to my side."
    "And neither of us feels the need to say a word."
    "We just lie together on the sand in complete silence."
    "Knowing that what we just did speaks for itself."
    $ cassidy.sexperience += 1
    hide cassidy
    return

label cassidy_fuck_date_male(location="hero"):
    if cassidy.status == 'mistress':
        call cassidy_fuck_date_dom (location) from _call_cassidy_fuck_date_dom
    else:
        call cassidy_fuck_date_sub (location) from _call_cassidy_fuck_date_sub
    return


label cassidy_fuck_date_sub(location="hero"):
    $ game.room = "bedroom1"
    $ r = randint(1, 4)
    if r == 1:
        "I take Cassidy's hand and we meander back to my house. I'm not in any hurry."
        scene bg bedroom1
        show cassidy
        "We get to the house and wordlessly, I take Cassidy down into my bedroom. She looks around without much interest at my stuff."
        "This can't be anything like what she's used to. She's got the best of everything, and I've got...well, it's my place and I like it."
        if cassidy.love < 120:
            cassidy.say "What would you like me to do?"
        else:
            show cassidy happy
            cassidy.say "How may I serve you, Master?"
        mike.say "You can start, my sexy slave, by taking off your clothes and showing me your incredibly sexy body."
        if cassidy.love < 120 or cassidy.sub < 75:
            show cassidy naked with dissolve
            "Without any ceremony, she slips quickly and efficiently out of her clothes, leaving them on the floor."
        else:
            show cassidy topless with dissolve
            "She smiles at me and works slowly, slipping her top off just enough that I can see her breasts sticking out."
            "She cups her hands beneath them and shows them off."
            show cassidy naked happy
            cassidy.say "Do you like what you see?"
            mike.say "Oh fuck yeah, I do. Damn, girl, you are fine, so fine."
            $ cassidy.love += 1
    elif r == 2:
        "There are times when Cassidy can be something of a pill to swallow."
        "Sure, she's pretty vain and likes to be the centre of attention."
        "But she just seems to get away with it because she's SO hot!"
        "And when she's in the right kind of mood, that pays off in spades too."
        "Like tonight, when everything seems to have gone right."
        "She got just the right amount of compliments."
        "And the required number of heads turned in her direction too."
        "Which means she's on top of the world when we get back to my place."
        scene bg bedroom1
        show cassidy
        with fade
        "Cassidy breezes into my bedroom without a care."
        "And when I turn around from closing the door, I almost jump in surprise."
        show cassidy naked happy with dissolve
        "Cassidy already has some of her clothes off, tossing them aside."
        "She smiles at me and shakes her head."
        show cassidy normal
        cassidy.say "What's the matter, [hero.name]?"
        cassidy.say "You never seen a girl strip off before?"
        "Shake my head and hastily walk over to where she's standing."
        mike.say "N...no, Cassidy..."
        mike.say "Of course I have!"
        mike.say "You just surprised me, that's all!"
        cassidy.say "What, you didn't think we were going to do it?"
        cassidy.say "Why else would we come back to your place?"
        "I nod, sensing that I need to move the conversation on."
        "There's no way I want to blow sex by getting hung up on silly shit."
        mike.say "Sure, Cassidy, sure."
        mike.say "Just ignore me."
        mike.say "You're so cute you're making my head spin, that's all!"
        show cassidy happy
        "Cassidy smiles broadly and nods."
        "Which lets me know the flattery's worked."
    elif r == 3:
        "Everything seems to be going right for me tonight, like I'm on some kind of roll."
        "Cassidy and I just wrapped up a date that delivered on all fronts."
        "And even better, it looks like she's not ready for the night to end just yet."
        scene bg bedroom1
        show cassidy
        with fade
        "So as soon as we make it back to my place, she almost hustles me into my room."
        hide cassidy
        show cassidy kiss
        with fade
        $ cassidy.flags.kiss += 1
        "In fact, the moment I turn around from closing the door, Cassidy's all over me."
        "It's like she can't decide between sticking her tongue down my throat or pulling off my clothes!"
        hide cassidy
        show cassidy close
        with fade
        mike.say "Wh...whoa, Cassidy!"
        mike.say "Slow down a little!"
        "It only takes me a second to realise how dumb I sound saying something like that."
        "And so I shake my head and do the best that I can to match Cassidy's enthusiasm."
        mike.say "Actually, forget what I just said, Cassidy."
        mike.say "You go as fast as you like!"
        show cassidy happy
        "I hear her chuckle as my hands travel all over her body."
        show cassidy topless with dissolve
        "But she doesn't do anything to stop me stripping her off too."
        hide cassidy
        show cassidy naked
        with dissolve
        "Cassidy and I half walk, half hop in the direction of the bed."
        "And luckily for us, we're all but naked by the time we collapse onto it."
        "By sheer luck, Cassidy comes up on top of me, gasping in delight."
        "She pins my wrists down onto the mattress, staring at me intently."
        cassidy.say "I had a great time tonight, [hero.name]."
        cassidy.say "I mean a REALLY great time!"
        cassidy.say "But now I want more..."
        "As she says this, Cassidy's gaze travels downwards."
        "I can see the desire in her eyes, and it sparks the same feeling in me too."
        "So by the time she's looking down at my cock, it's already stirring."
        "Cassidy watches as it stands to attention, her eyes full of anticipation."
        "Then she looks back up at me, and lets out a wicked giggle."
        cassidy.say "Oh, [hero.name]!"
        cassidy.say "Is all of that for me?"
        mike.say "That's the idea, Cassidy."
        mike.say "You think you can handle it?"
        call cassidy_dick_reactions from _call_cassidy_dick_reactions_1
        "Cassidy lets out another giggle and shakes her head."
        "She's clearly enjoying the chance to tease and be teased in turn."
    else:
        "I've been buzzing all night, just from being seen out and about with Cassidy on my arm."
        "Maybe like me you'd always winced at the thought of dating a girl that was a little princess."
        "You know the kind - daddy always spoiled them rotten and mummy dressed them up like a doll."
        "The result is that they're demanding, entitled and needy, a real handful to deal with."
        "But none of that seems to matter when they're as hot as Cassidy!"
        "Every look she gets from another guy, or even another girl, makes me grin like a fool."
        "She's the centre of attention everywhere we go, but she's only interested in me!"
        scene bg bedroom1 with fade
        "By the time we make it back to my place, I totally understand how she gets away with it too."
        "I'm so wrapped up in pleasing her that it almost becomes second nature."
        "I'd do anything to keep that sweet smile on her beautiful face!"
        "And when we finally make it back to my room, I'm hanging on her every word."
        show cassidy sad naked with dissolve
        cassidy.say "Ah, [hero.name]?"
        cassidy.say "Are you feeling okay?"
        cassidy.say "You're, like, staring at me."
        cassidy.say "And it's kind of freaking me out!"
        "I shake my head as I hear this, trying to get back to reality."
        "And thankfully it seems to work, as my mental fog begins to clear."
        mike.say "Sorry, Cassidy, sorry!"
        mike.say "It's just that you look so pretty tonight."
        mike.say "I just can't stop admiring you!"
        show cassidy happy
        "This seems to be the right kind of excuse to make in Cassidy's case."
        "As she smiles and looks to be genuinely flattered."
        "I'm sure she's used to getting complimented all the time."
        "But that still doesn't mean she's immune to being told how beautiful she is."
        cassidy.say "Aw..."
        cassidy.say "That's so sweet of you to say!"
        cassidy.say "I mean, I know that it's the truth..."
        cassidy.say "But it's still sweet of you to say so!"
        show cassidy normal
        "Suddenly I see a change come over Cassidy's face."
        "Her expression goes from flattered to secretive in a flash."
        "And she leans in close, as if she's afraid of being overheard."
        "I know that we're alone, but I lean in too all the same."
        cassidy.say "You want a reward for being so nice?"
        cassidy.say "You think I look pretty right now, yeah?"
        cassidy.say "So how about I show you how pretty I am after I strip-off?"
        "My own expression must look as dumb as a box of rocks right now."
        "And all that I can do in response is nod eagerly."
        show cassidy happy
        "Cassidy giggles at this, and runs over to the side of my bed."
        "I follow at a slower pace, already entranced by what she's doing."
        show cassidy normal topless with dissolve
        "And the effect only gets more intense as I watch her take off her clothes."
        "Which makes me almost stumble and stagger towards the bed in a daze."
        show cassidy -topless naked with dissolve
        "By the time I make it there, I seem to have undressed myself too."
        "I don't even remember doing this, just staring longingly at Cassidy."
        "And I'm also surprised by the way she pulls me onto the bed beside her!"
    $ game.room = "bedroom1"
    show cassidy normal
    cassidy.say "Now what?"

    $ fuck_pos = None
    $ cassidy_sad = False
    menu:
        "Titty job":
            mike.say "Get down on your knees and suck my fat cock."
            if cassidy.is_sex_slave:
                cassidy.say "Yes, Master!"
            else:
                cassidy.say "Yes, [hero.name]!"
            call cassidy_tittyfuck (topless=True) from _call_cassidy_tittyfuck
        "Slave play":
            mike.say "Lie down on my bed and spread your legs."
            if cassidy.is_sex_slave:
                cassidy.say "Yes, Master!"
            else:
                cassidy.say "Yes, [hero.name]!"
            "She does as instructed, lying on her back. I get on my knees next to her and grab her ankles to spread her legs as wide as I can."
            show cassidy missionary with fade
            mike.say "Are you comfortable, my slave."
            cassidy.say "No, I mean yes. I mean my legs hurt just a little."
            mike.say "Only a little?"
            cassidy.say "Only a little bit."
            mike.say "Do you want me?"
            if cassidy.love < 80:
                "She doesn't answer."
                mike.say "Cassidy, tell me you want me."
                show cassidy missionary eyes_close
                "She closes her eyes."
                cassidy.say "I...want you."
                "It doesn't sound like her heart is in it."
                mike.say "I don't believe you. Tell me again, and make me believe you."
                cassidy.say "Yes, Master. I want you."
                mike.say "I want you too, my beautiful slave."
            elif cassidy.love < 160:
                show cassidy missionary eyes_close
                "She closes her eyes."
                cassidy.say "I...want you."
                "It doesn't sound like her heart is in it."
                mike.say "I don't believe you. Tell me again, and make me believe you."
                cassidy.say "Yes, Master. I want you."
                mike.say "I want you too, my beautiful slave."
            else:
                "She answers without any hesitation."
                cassidy.say "I want you! I want you so much! I want you right now!"
                mike.say "Tell me you love me!"
                if cassidy.love < 180:
                    show cassidy missionary mouth_pleasure
                    "She answers, but not before hesitating just for a second."
                cassidy.say "I love you, Master! I need you, Master! Fuck me now, Master!"
                $ cassidy.sub += 1
            $ cassidy.love += 1
            $ cassidy.sub += 1
            call cassidy_missionary (0) from _call_cassidy_missionary
            if _return == "leave_without_gain":
                return
            $ cassidy.sexperience += 1
            if cassidy.lesbian > MIN_LES_GIRL_SEX:
                $ cassidy.lesbian -= 1
            if _return == "leave_with_gain":
                return
            call cassidy_sleep_date_fuck_sub (location) from _call_cassidy_sleep_date_fuck_sub_1
            return
        "Fuck her":
            pass
    scene bg bedroom1
    show cassidy naked
    with fade
    menu:
        "Missionary":
            show cassidy missionary eyes_open
            mike.say "Lie down on my bed and spread your legs."
            if cassidy.is_sex_slave:
                cassidy.say "Yes, Master!"
            else:
                show cassidy missionary eyes_open
                cassidy.say "Yes, [hero.name]!"
            "She does as instructed, lying on her back. I get on my knees next to her and grab her ankles to spread her legs as wide as I can."
            call cassidy_missionary (0) from _call_cassidy_missionary_1
        "Doggy" if hero.sexperience >= 15:
            call cassidy_doggy (15) from _call_cassidy_doggy
        "Cowgirl" if hero.sexperience >= 20 and cassidy.sub > 20:
            call cassidy_cowgirl (20) from _call_cassidy_cowgirl
        "Reverse Cowgirl" if hero.sexperience >= 25 and cassidy.sub > 30:
            call cassidy_reverse_cowgirl (25) from _call_cassidy_reverse_cowgirl
    if _return == "leave_without_gain":
        return
    $ cassidy.sexperience += 1
    if cassidy.lesbian > MIN_LES_GIRL_SEX:
        $ cassidy.lesbian -= 1
    if _return == "leave_with_gain":
        return
    hide cassidy
    call cassidy_sleep_date_fuck_sub (location) from _call_cassidy_sleep_date_fuck_sub
    return

label cassidy_missionary(sexperience_min):

    menu:
        "Fuck her pussy":
            call check_condom_usage (cassidy, love=200, sub=100) from _call_check_condom_usage_32
            if _return == 'sad':
                $ cassidy_sad = True
            elif _return == 'anal':
                call cassidy_missionary_anal_sub from _call_cassidy_missionary_anal_sub
                return
            elif _return == False:
                return "leave_without_gain"
            call cassidy_missionary_pussy_sub from _call_cassidy_missionary_pussy_sub
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            call cassidy_missionary_anal_sub from _call_cassidy_missionary_anal_sub_1
    return

label cassidy_missionary_pussy_sub:
    show cassidy missionary vaginal
    if CONDOM:
        show cassidy missionary vaginal condom

    if cassidy.love < 80 or cassidy_sad:
        show cassidy missionary mouth_hurt eyes_close
        "Cassidy whimpers softly as I push my cock into her pussy. There is some resistance as she isn't really wet yet."
        if not cassidy_sad or cassidy.love > 150:
            show cassidy missionary mouth_normal
            "It doesn't take long, however, for her juices to flow, and I am able to press deeply into her with ease."
    elif cassidy.love < 160:
        show cassidy missionary mouth_pleasure eyes_ahegao
        "Cassidy takes a sharp breath as I enter her, the sound of the air through her teeth almost a spasm of anticipation."
        cassidy.say "Oh! Oh my God!"
    else:
        show cassidy missionary mouth_pleasure
        "Cassidy moans as soon as I enter her, her cunt wet and swollen, ready for me."
        if cassidy.is_sex_slave:
            cassidy.say "Fuck me, Master! Fuck me hard!"
        else:
            cassidy.say "Fuck me, [hero.name]! Fuck me hard!"

    "Holding her legs as far apart as I can, I slowly thrust my dick into her, going a little deeper every stroke until I can feel the tip of my head pressing against her cervix."
    if cassidy_sad or cassidy.love < 100:
        show cassidy missionary mouth_hurt eyes_close
        "She makes little noises, a mix of pain and pleasure. She isn't particularly enjoying this, but she doesn't have to. This is what she gets for what she tried to do to me!"
    elif cassidy.love < 160:
        show cassidy missionary mouth_pleasure eyes_close
        "She makes little noises, moans in the back of her throat that grow louder with each thrust."
        cassidy.say "Oh! Oh! Ohhhhhhh!"
        "Each moan comes in time with my thrust, the loudest sound coming while I'm deepest inside her."
    else:
        "She makes little noises, moans in the back of her throat that grow louder with each thrust."
        show cassidy missionary mouth_pleasure eyes_ahegao
        if cassidy.is_sex_slave:
            cassidy.say "Oh yes! Yes, Master, that's...oh God yes!"
        else:
            cassidy.say "Oh yes! Yes, [hero.name], that's...oh God yes!"
        "I can feel her pussy spasm repeatedly as she orgasms, and then she goes limp, smiling at me while I finish."
    "Just a few more thrusts and I'll be ready to blow!"

    call cum_reaction (cassidy, "vaginal", sexperience_min) from _call_cum_reaction_69
    if _return == "vaginal_condom":
        with vpunch
        "When I finally can't take anymore, I orgasm, filling the condom up with my sticky cum."
        show cassidy missionary mouth_pleasure cum with vpunch
    elif _return == "vaginal_outside":
        show cassidy missionary out cum with vpunch
        "Just when I can't take any more, I pull out and blow my load all over her tits and belly."
        show cassidy missionary -cum squirt with vpunch
        if cassidy_sad:
            $ cassidy.love += 2
            $ cassidy.sub += 1
            "The relief on Cassidy's face that I didn't cum inside her is massive."
            if cassidy.is_sex_slave:
                cassidy.say "Oh, thank you, Master, thank you so much."
            else:
                cassidy.say "Oh, thank you, [hero.name], thank you so much."
            if cassidy.sub > 80:
                cassidy.say "I promise to be a good girl for you! I swear I will!"
    else:
        with vpunch
        "I can't take any more, and my cock explodes with full fury, filling her up with my cum."
        show cassidy missionary mouth_pleasure cum with vpunch
        if cassidy_sad:
            $ cassidy.love -= 10
            $ cassidy.sub -= 10

            "Cassidy cries out in anguish, clearly hurt and upset that I ignored her pleas."
        elif cassidy.love > 160:
            "Cassidy relaxes and stares at me with a soft, happy smile on her face."
            if cassidy.is_sex_slave:
                cassidy.say "I love you, Master!"
            else:
                cassidy.say "I love you, [hero.name]!"
        #$ cassidy.impregnate()
    "When it's all over, I pull out of her and go limp."
    return

label cassidy_missionary_anal_sub:
    $ renpy.dynamic("hurt", "hurtsogood")

    $ hurt = True if (20 - (4 * cassidy.flags.anal) - (cassidy_love // 5)) > 0 else False

    $ hurtsogood = cassidy.flags.anal < 3 and not hurt
    show cassidy missionary anal with fade
    "I pull her legs apart, spreading her cheeks and pressing the tip of my cock against her asshole."
    if cassidy.flags.anal < 1:
        "Cassidy yelps in surprise as her rectum parts for my swollen head."
        cassidy.say "Wait! I've never been fucked there before!"
        "I don't wait, though, and I push my cock further in."
    if hurt:
        show cassidy missionary eyes_close mouth_hurt
        cassidy.say "It hurts!"
        menu:
            "Go slow and gentle":
                mike.say "Give it a moment, honey. I know it hurts right now, but it will feel good soon, I promise! I'll be gentle!"
                show cassidy missionary eyes_close
                "And as I promised, I do go slow, pushing in just a little, then back out. Rocking gently and stopping as soon as it looks like the pain will be too much."
                $ cassidy.love += 1
                $ cassidy.sub += 2
            "A little pain is good for her":
                $ cassidy_sad = True
                mike.say "Get used to it, bitch! Your ass is mine for what you did to me, and I want your sexy ass!"
                $ cassidy.love -= 5
                $ cassidy.sub -= 5
                "I push my way as deep into her anus as I can go, which isn't all the way. As soon as I do, Cassidy nearly screams."
                cassidy.say "But you promised!"
                show cassidy missionary eyes_close
                "She's right, I did promise. So I slow down a little."
                mike.say "You're right, I did promise. I'll go slower."
    else:
        if hurtsogood:
            show cassidy missionary mouth_hurt
            "My cock goes in deeper than it did last time, but not all the way. Cassidy's expression looks pained, but she doesn't make any noise."
            mike.say "Are you okay?"
            cassidy.say "It hurts but don't stop!"
            $ cassidy.sub += 2
        else:
            "I push my cock into her ass, which is ready and opens for me easily. I can fit it almost all of the way in there."
            "And now that she's loose enough that it no longer hurts, Cassidy looks like she's enjoying herself too!"
    "I gently thrust in and out of Cassidy's anus."
    if hurt and not hurtsogood:
        "Cassidy whimpers softly, but as she loosens up, this passes, and by the time I'm ready to explode, she's starting to get into it."
    elif hurtsogood:
        "Cassidy whimpers softly, but every time she does, it's accompanied by a half-choked shout of \"More!\""
    else:
        "Cassidy moans softly, enjoying."
    show cassidy missionary eyes_open mouth_pleasure out cum
    "Just when I'm about to cum, I pull out."
    show cassidy missionary out cum with vpunch
    "Which showers her tits and belly with my hot, sticky cum, mixed with all the secretions that came from her anus."
    with vpunch

    if hurt and not hurtsogood:
        cassidy.say "Oh thank God that's over."
    elif hurtsogood:
        if cassidy.is_sex_slave:
            cassidy.say "I love you, Master, even if it hurts!"
        else:
            cassidy.say "I love you, [hero.name], even if it hurts!"
    else:
        cassidy.say "That was so good!"
    $ cassidy.flags.anal += 1
    return

label cassidy_doggy(sexperience_min):
    "I hurry to take off my own clothes, trying to catch up."
    "And Cassidy reclines on the edge of the bed, happy to watch."
    "Once I'm done, she nods again and beckons me over."
    "As I approach, she climbs onto the bed."
    "And then she lowers herself onto her belly."
    "Cassidy waves her ass in the air, giggling as she does so."
    "And I don't need to be told what she wants me to do next!"
    show cassidy doggy pleasure with fade
    "I waste no time in climbing onto the bed behind Cassidy."
    "Then I take a firm hold of her around the waist."
    "She wriggles in my grasp, but not enough to break free."
    "And the motion only serves to help get my cock nice and hard."
    show cassidy doggy normal
    "Cassidy glances back over her shoulder."
    "I can see the look of anticipation in her eyes."
    "And that urges me on to make my next move..."
    menu:
        "Fuck her ass" if hero.sexperience >= sexperience_min + 5:
            "Maybe I'm feeling a little bit rebellious tonight."
            "Or else maybe I think Cassidy's throwing down the gauntlet."
            "Because I suddenly have the urge to do something to shock her."
            show cassidy doggy anal
            "I know that I have to move quickly, and so I just go for it."
            "Before Cassidy knows what's happening, my cock is between her buttocks."
            cassidy.say "W...what are you..."
            cassidy.say "[hero.name]...that's my..."
            cassidy.say "That's my ass...ho..."
            "Of course I can feel Cassidy's ass clench the moment I push in there."
            "But all that serves to do is make the sensation more intense."
            show cassidy doggy pleasure
            "And I respond by pushing that much harder too."
            cassidy.say "Oh..."
            cassidy.say "Oh my god..."
            cassidy.say "That's...that's good!"
            "I can't help nodding in agreement as I sink into Cassidy."
            "After the initial resistance, her ass surrenders to me."
            "And I enjoy every moment of sinking into her until I can't get deeper."
            show cassidy doggy normal blush
            "Cassidy stares back over her shoulder at me."
            "Her eyes wide and her mouth hanging open."
            "Now she seems to have lost the power of speech."
            "But I can see how much she's getting off on this."
            "Her eyes seem to plead for more."
            "And her breath comes in ragged gasps."
            "I do the best I can to give Cassidy what she wants."
            "But her ass is just so tight that I have to take it slowly."
            "All the time I'm inside her I can feel her squeezing me."
            "It's like an intense hand-job as well as sex."
            "The best of both worlds in one neat little package."
            "Every thrust I manage is a battle with Cassidy's body."
            "And each one makes me think that I'm about to lose it too."
            "Somehow I manage to keep holding on as I'm hammering her ass."
            show cassidy doggy pleasure
            "Cassidy shows her approval by moaning in time with my motions."
            "In fact, I wouldn't be surprised if she clapped her hands and barked like a seal!"
            "Reaching out with both hands, I put them under Cassidy's chin."
            "And then I give one final thrust, using the last of my energy."
            call cum_reaction (cassidy, 'anal', sexperience_min) from _call_cum_reaction_70
            if _return == 'anal_inside':
                show cassidy doggy creampie ahegao with hpunch
                $ cassidy.sub += 2
                "Cassidy wails as I shoot my load deep inside her ass."
                with hpunch
                "But there's nowhere she can go and no chance of escape."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                show cassidy doggy pleasure
                "And I only relent once I know that we're both done."
                "Releasing her from my grasp, I lower her onto the bed."
                "And the only sound I can hear is us both panting hard."
            elif _return == 'anal_outside':
                show cassidy doggy -anal
                "Cassidy wails as I pull my cock out of her ass."
                "But there's nowhere she can go to escape what happens next."
                show cassidy doggy cumshot with hpunch
                "Held tight in my arms, she's showered in cum a moment later."
                show cassidy doggy -cumshot dickcum with hpunch
                $ cassidy.sub += 1
                "It rains down on her ass and begins to run down her legs."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                show cassidy doggy normal
                "And I only relent once I know that we're both done."
                "Releasing her from my grasp, I lower her onto the bed."
                "And the only sound I can hear is us both panting hard."
            $ cassidy.flags.anal += 1
        "Fuck her pussy":
            "All it takes is one little glimpse between Cassidy's thighs."
            "Just the smallest glimpse of what's waiting for me down there."
            "And all I want is to get my hands on the work of art that is her pussy!"
            "It's glistening in the light, almost calling out to me!"
            call check_condom_usage (cassidy, 200) from _call_check_condom_usage_33
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cassidy doggy condom
            "Once I finally have my cock between Cassidy's thighs, everything clicks."
            "The feeling of her lips as I slide the tip along them."
            "The scent of her that I can just catch as it reaches me."
            "The way she moans in anticipation of what's to come next."
            cassidy.say "Mmm..."
            cassidy.say "What are you waiting for?"
            cassidy.say "Please, [hero.name] - don't make me beg for it!"
            "That right there maybe the closest that Cassidy's ever come to actually begging!"
            "And the gravity of the situation is not lost on me either."
            "I don't know if it's the control that she often has over me."
            "Or else I it's me feeling like I'm the one on control for a change."
            "Either way I hurry to give Cassidy just what she wants."
            "And I do that not in the least because it's what I want too!"
            show cassidy doggy vaginal
            "In the end, all it takes is the slightest push."
            "There's a moment of resistance from Cassidy."
            show cassidy doggy pleasure
            "And then she opens like a flower to me."
            "I slide into her in one smooth motion."
            "And I don't stop until I'm as deep as I can possibly go."
            "The whole time Cassidy pants and moans."
            "Making every inch feel that much more intense."
            "I pause only for a couple of seconds."
            show cassidy doggy blush
            "Because I can already see Cassidy's head bobbing up and down."
            "She's still gasping, but she's also nodding, urging me on."
            "Guessing that she doesn't want me to go slow, I set a quickening pace."
            "My speed builds steadily, and her nodding becomes faster still."
            "But it's not like it's hard to fuck Cassidy like this."
            "In fact, she makes it feel like the easiest thing in the world."
            "Just the sight of her body moving while I'm inside of her."
            "That and the sounds that she's making as I thrust into her too!"
            "Hell, maybe she is right to be such an uppity bitch sometimes!"
            "I feel like she's right to make a guy work hard to earn a shot at this."
            "All too soon I can feel myself starting to cum."
            "Reaching out with both hands, I put them under Cassidy's chin."
            "And then I give one final thrust, using the last of my energy."
            call cum_reaction (cassidy, 'vaginal', sexperience_min) from _call_cum_reaction_71
            if _return == "vaginal_outside":
                show cassidy doggy -vaginal
                "Cassidy wails as I pull my cock out of her pussy."
                "But there's nowhere she can go to escape what happens next."
                show cassidy doggy cumshot with hpunch
                "Held tight in my arms, she's showered in cum a moment later."
                show cassidy doggy -cumshot dickcum with hpunch
                $ cassidy.love += 1
                "It rains down on her ass and begins to run down her legs."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                show cassidy doggy normal
                "And I only relent once I know that we're both done."
                "Releasing her from my grasp, I lower her onto the bed."
                "And the only sound I can hear is us both panting hard."
            elif _return == "vaginal_condom":
                show cassidy doggy creampie with hpunch
                "Cassidy wails as I shoot my load deep inside her pussy."
                with hpunch
                "But there's nowhere she can go and no chance of escape."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                show cassidy doggy normal
                "And I only relent once I know that we're both done."
                "Releasing her from my grasp, I lower her onto the bed."
                "And the only sound I can hear is us both panting hard."
            elif _return == "vaginal_inside_pill":
                cassidy.say "Pill..."
                cassidy.say "I'm on the pill!"
                show cassidy doggy creampie ahegao with hpunch
                $ cassidy.love += 2
                "Cassidy wails as I shoot my load deep inside her pussy."
                with hpunch
                "But there's nowhere she can go and no chance of escape."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                show cassidy doggy pleasure
                "And I only relent once I know that we're both done."
                "Releasing her from my grasp, I lower her onto the bed."
                "And the only sound I can hear is us both panting hard."
            elif _return == "vaginal_inside_pregnant":
                "Carefully cradling her swollen belly, I let go."
                show cassidy doggy creampie ahegao with hpunch
                $ cassidy.love += 3
                "Cassidy wails as I shoot my load deep inside her pussy."
                with hpunch
                "But there's nowhere she can go and no chance of escape."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                show cassidy doggy pleasure
                "And I only relent once I know that we're both done."
                "Releasing her from my grasp, I lower her onto the bed."
                "And the only sound I can hear is us both panting hard."
            elif _return == "vaginal_inside_mad":
                cassidy.say "Don't..."
                cassidy.say "Stop..."
                mike.say "Huh...what?!?"
                show cassidy doggy -blush
                cassidy.say "Please don't cum in me!"
                "Even as she speaks the words, it's already happening."
                show cassidy doggy creampie normal with hpunch
                #$ cassidy.impregnate()
                $ cassidy.love -= 5
                "Cassidy wails as I shoot my load deep inside her pussy."
                with hpunch
                "There's nothing I can do to keep it from happening."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                "Releasing her from my grasp, I lower her onto the bed."
                "My mind already racing with the gravity of what just happened."
            elif _return == "vaginal_inside_happy":
                cassidy.say "Don't...stop..."
                mike.say "Huh...what?!?"
                cassidy.say "Cum in me, please!"
                "Even as she speaks the words, it's already happening."
                show cassidy doggy creampie ahegao with hpunch
                #$ cassidy.impregnate()
                $ cassidy.love += 5
                "Cassidy wails as I shoot my load deep inside her pussy."
                with hpunch
                "There's nothing I can do to keep it from happening."
                with hpunch
                "She twitches and writhes in my grasp, cumming too."
                "Releasing her from my grasp, I lower her onto the bed."
                "My mind already racing with the gravity of what just happened."
    return

label cassidy_cowgirl(sexperience_min):
    "Before I know it, I'm on my back, staring up at the ceiling."
    "But only for a moment, as Cassidy looms over me a second later."
    show cassidy cowgirl with fade
    "She's straddling my thighs, pinning me down to the mattress."
    "But what the hell do I care?"
    "She could pin me down and flog me if she wanted to!"
    cassidy.say "Hold on, [hero.name]."
    cassidy.say "Because here we go!"
    menu:
        "Fuck her ass" if hero.sexperience >= sexperience_min + 5:
            "I'm still nodding and smiling like a fool as Cassidy says this."
            "But my body seems to be able to function independently of my head."
            "Almost without realising it, my hands reach out for Cassidy's buttocks."
            "And I part them before she even realises what's going on."
            cassidy.say "Huh?"
            cassidy.say "What are you..."
            show cassidy cowgirl ahegao anal
            cassidy.say "Oh...oh my...OH MY GOD!"
            "I hear all of this while I'm pushing the head of my cock into Cassidy's ass."
            "And the tone of her voice goes from surprised to alarmed before I'm an inch inside."
            "All of which makes the sensation that much sweeter from my point of view!"
            "Sure, Cassidy is yelping and moaning as she sinks onto my cock."
            "But she's not protesting or trying to wriggle out of my grasp."
            "And I take that to mean that she's not adverse to what I'm doing."
            "A notion that Cassidy confirms herself a few moments later."
            show cassidy cowgirl pleasure
            cassidy.say "Oh...you..."
            cassidy.say "You bad man..."
            cassidy.say "I didn't say you could do THAT to me!"
            cassidy.say "But it feels SO good!"
            "Cassidy nods her head, showing that she means every word."
            "And as I begin to thrust in and out from below, she moves too."
            "Cassidy matches my pace and mirrors my movements almost perfectly."
            "But that doesn't mean that the muscles of her ass are passive."
            "Instead they squeeze me hard the whole time, adding to the sensation."
            "This combines with Cassidy's weight, pressing down from above."
            "Soon enough she's not the only one sighing and moaning."
            "I let out the same kind of sounds with her every movement."
            "And I can see from the look on her face that she approves."
            "But then why wouldn't she?"
            "I'm looking up at her with what must be pure amazement in my eyes."
            "That's because I have an almost perfect view of Cassidy as she looms over me."
            "I can see every curve of her belly and breasts, he stiff nipples too."
            "Combine the that the feeling of being inside her at the same time."
            "And you have a sure-fire recipe for perfection."
            "Though it's the look on Cassidy's face that tops it all off."
            "That self-satisfied expression that says she deserves all of this."
            "That any man would be this helpless were she to give herself to him."
            "It's more than enough to make me want her like crazy."
            "And, in the end, I think it's what finishes me off too!"
            mike.say "Ah..."
            mike.say "Cassidy..."
            mike.say "I'm gonna cum!"
            call cum_reaction (cassidy, 'anal', sexperience_min) from _call_cum_reaction_72
            if _return == 'anal_inside':
                "I can see the look of realisation dawn on Cassidy's face."
                "But it's too late for her to be able to do anything about it."
                show cassidy cowgirl ahegao creampie with vpunch
                $ cassidy.sub += 2
                "I let go a second later, cumming deep inside of her ass."
                with vpunch
                "Instantly her face shows that she feels it, and she keens helplessly."
                with vpunch
                "I can feel the muscles of her ass, twitching and flexing around my cock."
                "And then Cassidy slumps forwards, overtaken by the sensations she's feeling."
            elif _return == 'anal_outside':
                show cassidy cowgirl normal -anal
                "I manage to pull my cock out of Cassidy's ass the moment before I cum."
                "She doesn't seem prepared for this, and the sensation only seems to confuse her more."
                "All of this means she's just not ready for what happens next."
                show cassidy cowgirl pleasure cumshot with vpunch
                "Cassidy yelps in surprise and alarm as cum shoots upwards and over her."
                show cassidy cowgirl dickcum -cumshot with vpunch
                $ cassidy.sub += 1
                "It spatters her breasts and paints her belly with warm, sticky streamers."
                with vpunch
                "And all the while, she stares at me, wide-eyed and confused."
            $ cassidy.flags.anal += 1
        "Fuck her pussy":
            "I'm still nodding and smiling like a fool as Cassidy says this."
            "And I'm more than happy to follow her lead like an obedient puppy too."
            "So when she reaches down and takes a hold of my cock I keep right on nodding."
            "And I nod even faster when she begins to rub it against the lips of her pussy too!"
            call check_condom_usage (cassidy, 200) from _call_check_condom_usage_34
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cassidy cowgirl condom
            "I'm still nodding as Cassidy pushes my cock between her lips."
            show cassidy cowgirl vaginal
            "And my head only starts to bob faster as I feel it pushing inside of her."
            "Cassidy holds my eye the whole time this is happening."
            "She nods too, but more from knowing what effect she's having on me."
            cassidy.say "You like that, yeah?"
            cassidy.say "You like the way it feels?"
            cassidy.say "How my pussy feels around your cock?"
            "But her expression changes a moment later, when I spring into action."
            "Without hesitating, my hand take hold of Cassidy by the haunches."
            show cassidy cowgirl pleasure
            "And I pull her suddenly downwards, not stopping until I can go no further."
            cassidy.say "Ah..."
            cassidy.say "Oh...oh...fuck!"
            "Now her eyes are wide with surprise, and something else too."
            "I can see that the sensation is threatening to overwhelm her."
            "And now it's Cassidy's turn to be the one nodding in desperation."
            cassidy.say "That..."
            cassidy.say "That feels so good..."
            cassidy.say "Please...please fuck me like that?"
            "When you get a request like that, how can you turn it down?"
            "By now I'm already shifting into a higher gear anyway."
            "And I would have been doing all that I could to fuck Cassidy that hard."
            "But she doesn't know that, and there's no reason to burst her bubble."
            "Better to let her enjoy herself and believe that I'm doing as she asks."
            "Before long, all I can hear is the sound of Cassidy moaning with pleasure."
            "At the same time I'm grunting and gasping from my own efforts."
            "She nods, tossing her head this way and that."
            "And I take that as a show of her approval."
            "Cassidy has her eyes closed right now."
            "So she can't see that I'm staring up at her in amazement."
            "I have a perfect view of her as she looms over me."
            "I can see every curve and line of her body."
            "Her perfect belly, full breasts, even her stiff nipples."
            "All of this while feeling the sensation of being inside her."
            "Right now there's no place on earth I'd rather be."
            "The expression on Cassidy's face is so different as well."
            "She looks serene, satisfied and almost humble."
            "Is this what it takes to make her go soft?"
            "It's more than enough to make me want her like crazy."
            "And, in the end, I think it's what finishes me off too!"
            mike.say "Ah..."
            mike.say "Cassidy..."
            mike.say "I'm gonna cum!"
            call cum_reaction (cassidy, 'vaginal', sexperience_min) from _call_cum_reaction_73
            if _return == "vaginal_outside":
                show cassidy cowgirl normal -vaginal
                "I manage to pull my cock out of Cassidy's pussy the moment before I cum."
                "She doesn't seem prepared for this, and the sensation only seems to confuse her more."
                "All of this means she's just not ready for what happens next."
                show cassidy cowgirl cumshot with vpunch
                if CONDOM:
                    "Cassidy yelps in surprise as I cum."
                else:
                    show cassidy cowgirl pleasure with vpunch
                    "Cassidy yelps in surprise and alarm as cum shoots upwards and over her."
                    show cassidy cowgirl dickcum -cumshot with vpunch
                    $ cassidy.love += 1
                    "It spatters her breasts and paints her belly with warm, sticky streamers."
                "And all the while, she stares at me, wide-eyed and confused."
            elif _return == "vaginal_condom":
                "I can see the look of realisation dawn on Cassidy's face."
                "But it's too late for her to be able to do anything about it."
                "And we already took the precaution of using a condom."
                "So there's nothing to worry about."
                with vpunch
                "I let go a second later, cumming deep inside of her pussy."
                with vpunch
                "Instantly her face shows that she feels it, and she keens helplessly."
                with vpunch
                "I can feel the muscles of her pussy, twitching and flexing around my cock."
                "And then Cassidy slumps forwards, overtaken by the sensations she's feeling."
            elif _return == "vaginal_inside_pill":
                cassidy.say "Do it...."
                cassidy.say "Cum in me..."
                cassidy.say "I'm on the pill!"
                "I nod at the timely reminder from Cassidy."
                "And I'm thankful for the excuse not to have to pull out."
                show cassidy cowgirl ahegao creampie with vpunch
                $ cassidy.love += 2
                "I let go a second later, cumming deep inside of her pussy."
                with vpunch
                "Instantly her face shows that she feels it, and she keens helplessly."
                "I can feel the muscles of her pussy, twitching and flexing around my cock."
                "And then Cassidy slumps forwards, overtaken by the sensations she's feeling."
            elif _return == "vaginal_inside_pregnant":
                cassidy.say "Do it...."
                cassidy.say "Cum in me..."
                cassidy.say "I'm pregnant!"
                "Like I needed to be reminded of that!"
                "But I am thankful for the excuse not to have to pull out."
                show cassidy cowgirl ahegao creampie with vpunch
                $ cassidy.love += 3
                "I let go a second later, cumming deep inside of her pussy."
                with vpunch
                "Instantly her face shows that she feels it, and she keens helplessly."
                with vpunch
                "I can feel the muscles of her pussy, twitching and flexing around my cock."
                "And then Cassidy slumps forwards, overtaken by the sensations she's feeling."
            elif _return == "vaginal_inside_mad":
                cassidy.say "No...no...no!"
                cassidy.say "You have to stop now!"
                cassidy.say "Don't cum in me!"
                "Cassidy tries to clamber off of me as she says this."
                "And in the confusion I suddenly remember I'm not wearing a condom!"
                show cassidy cowgirl creampie with vpunch
                $ cassidy.love -= 5
                #$ cassidy.impregnate()
                "I let go a second later, cumming deep inside of her pussy."
                with vpunch
                "Instantly Cassidy's face shows that she feels it, and she keens helplessly."
                with vpunch
                "I can feel the muscles of her pussy, twitching and flexing around my cock."
                "And then Cassidy slumps forwards, overtaken by the sensations she's feeling."
                show cassidy cowgirl normal
                "She lays there, a look of horror on her face."
                "While I begin to feel fear churning in my gut."
                "What have we done?!?"
            elif _return == "vaginal_inside_happy":
                cassidy.say "No...no...no!"
                cassidy.say "Don't stop now!"
                cassidy.say "Keep going!"
                "Cassidy pushes all her weight down on me as she says this."
                "And in the confusion I suddenly remember I'm not wearing a condom!"
                show cassidy cowgirl ahegao creampie with vpunch
                $ cassidy.love += 5
                #$ cassidy.impregnate()
                "I let go a second later, cumming deep inside of her pussy."
                with vpunch
                "Instantly Cassidy's face shows that she feels it, and she keens helplessly."
                with vpunch
                "I can feel the muscles of her pussy, twitching and flexing around my cock."
                "And then Cassidy slumps forwards, overtaken by the sensations she's feeling."
                show cassidy cowgirl pleasure
                "She lays there, a smile on her face."
                "While I begin to feel fear churning in my gut."
                "What have I done?!?"

    return

label cassidy_reverse_cowgirl(sexperience_min):
    "Cassidy shoots me a cheeky grin and nods her head."
    "Then she turns herself around so that she has her back to me."
    show cassidy reverse cowgirl
    "But at the same time she's sure to make me feel every movement she makes."
    "Stroking the delicate prize between her legs against my cock as she does so."
    cassidy.say "Okay, [hero.name], I'm ready."
    cassidy.say "Now's your chance to surprise me!"
    menu:
        "Fuck her ass" if hero.sexperience >= sexperience_min + 5:
            "I can't help smiling as I take a firm hold of Cassidy's haunches."
            "As I know that I'm about to put her flippant comments to the test."
            "If she doesn't want to see what I'm doing, then so be it."
            "But I'm damned if I'm going to miss the chance to have my way with her!"
            "That's why I wait until the very last moment to part her buttocks."
            "And then I aim the head of my cock squarely at her exposed ass."
            cassidy.say "H...hey..."
            cassidy.say "Wait a damn minute..."
            cassidy.say "I never said you could..."
            show cassidy reverse cowgirl anal ahegao
            "But by the time Cassidy manages to get the words out, it's too late."
            "My cock is already more than an inch into the tight circle of her ass."
            "And the sound of her protests only urges me to push on further."
            show cassidy reverse cowgirl normal
            "Cassidy's body seems to surrender below the neck."
            "Ignoring the objections coming out of her mouth."
            "Her muscles begin to soften and allow me ever further inside."
            "And her head is forced to catch up with the rest of her body."
            show cassidy reverse cowgirl pleasure
            cassidy.say "Oooh..."
            cassidy.say "Th...that's good..."
            cassidy.say "That's actually...REALLY fucking good!"
            "I can see Cassidy nodding her head from behind."
            "And I don't need more encouragement than that."
            "I begin to work harder with each passing second."
            "But I'm sure to pick up speed slowly at first."
            "That way I can watch as my efforts take effect."
            "Cassidy move as slowly as I do at the start."
            "Her hands moving over her body as she caresses herself."
            "But soon enough this delicate touch doesn't seem to be enough."
            "I can feel he muscles of her ass squeezing me tightly."
            "And Cassidy's hands seem to be doing the same thing to her body."
            "She's not being gentle with herself anymore, not at all."
            "Instead she clutches at her breasts, massaging them like dough."
            "Cassidy catches her nipples between thumb and finger."
            "And she pinches at them as if desperate for release."
            "I'm going as fast and hard as I can by now."
            "Giving Cassidy all that I have and holding nothing back."
            "But even so, she seems to be almost insatiable!"
            "And she's not sitting back and leaving the work to me either."
            "For all that I'm pushing up, Cassidy's pushing down too."
            "She grinds herself into my lap, using all of her strength."
            "I don't think I could get any further into her right now!"
            "Which means it comes as some relief to hear Cassidy moaning."
            "She lets out a long, low sound that can mean only one thing."
            "She's about to cum, and it looks like she's taking me with her too!"
            call cum_reaction (cassidy, 'anal', sexperience_min) from _call_cum_reaction_74
            if _return == 'anal_inside':
                "I don't think I could get out from under Cassidy if I tried."
                "And so I just lie back and let nature take its course."
                "As her muscles begin to quiver and shake, she sets me off too."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                $ cassidy.sub += 2
                "I shoot my load while I'm as deep in her ass as I can get."
                with vpunch
                "And it only seems to make her orgasm that much more intense."
                with vpunch
                "Cassidy rides my cock until the very last moment, gasping and panting."
                show cassidy reverse cowgirl pleasure flacid dickcum analdrip -creampie
                "Then she keels over, tumbling off of me and onto the bed."
            elif _return == 'anal_outside':
                show sexinserts chest cassidy zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "I have to wait for the exact moment Cassidy's weight is in the air."
                "And when I feel it happen, I make my move without hesitation."
                show cassidy reverse cowgirl -anal
                "My cock slides out of her ass before she knows what's happening."
                "The sound of her surprise mixes with the moans of her orgasm."
                show cassidy reverse cowgirl cumshot with vpunch
                "And the second she sits back down, I shoot my load over her."
                show cassidy reverse cowgirl dickcum -cumshot
                show sexinserts chest cassidy cum zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                with vpunch
                $ cassidy.sub += 1
                "It spatters up Cassidy's body, running down over her slick skin."
                "She sits upright for a moment longer, gasping and panting."
                show cassidy reverse cowgirl normal flacid
                "Then she keels over, tumbling off of me and onto the bed."
                hide sexinserts
                hide bellycum
            $ cassidy.flags.anal += 1
        "Fuck her pussy":
            "I can't wait to get my hands on Cassidy right now."
            "Especially after I got a feel of her pussy a few moments ago!"
            "And so I don't waste anytime in getting down to business."
            call check_condom_usage (cassidy, 200) from _call_check_condom_usage_35
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cassidy reverse cowgirl condom
            "Taking a firm hold of Cassidy's haunches, I pull her downwards."
            "This means that she sits squarely on my cock, just as I intended."
            "I feel the tip slide along the lips of her pussy."
            show cassidy reverse cowgirl pleasure
            "And in that moment, both of us let out a gasp of anticipation."
            cassidy.say "Mmm..."
            cassidy.say "That feels good!"
            show cassidy reverse cowgirl normal
            cassidy.say "Please, [hero.name]...put it in me?"
            "Cassidy gets her wish a moment later, as gravity makes it happen."
            "I feel the token resistance that her pussy puts up."
            "But then she parts like the petals of a flower."
            show cassidy reverse cowgirl pleasure vaginal
            "And all of her weight pushes her down and onto my cock."
            "I slide into Cassidy with a smooth motion, not stopping until I fill her."
            "But at the same time, the feeling of doing so is incredibly intense."
            "Cassidy's pussy feels tight and her muscles squeeze me like a fist one moment."
            "Yet at the same time she's soft and yielding in the next."
            "It's a contrast that almost takes my breath away."
            "And I find myself responding without conscious thought."
            "Before I know it, I'm moving with ever more speed."
            "The intensity of my thrusts getting stronger by the moment."
            "But Cassidy shows no signs of objection to the pace I'm setting."
            "Instead she eagerly takes everything that I have to give."
            show cassidy reverse cowgirl normal
            cassidy.say "Oh...oh yeah..."
            cassidy.say "That's what I want..."
            cassidy.say "Give it to me...PLEASE!"
            "It's not like I need to be told twice."
            "And so I redouble my efforts."
            show cassidy reverse cowgirl pleasure
            "Now I'm hammering away at Cassidy for all I'm worth."
            "Any notion of holding back or pacing myself falls at the wayside."
            "I keep a tight hold of Cassidy as my thighs slam against her buttocks."
            "And she pushes down with all of her weight too."
            "I'm not sure if she does this to force my cock deeper into herself."
            "Or if she's trying to cling on for dear life as we push ourselves to the limit."
            "But either way it leaves her hands free to roam all over her body."
            "Cassidy caresses herself the whole time I'm inside of her."
            "I watch as she traces the lines of her body, up and down."
            "And I have to bite my lip as she plays with her chest."
            "She's not being gentle with herself, not at all."
            "Instead she clutches at her breasts, massaging them like dough."
            "Cassidy catches her nipples between thumb and finger."
            "And she pinches at them as if desperate for release."
            "The sound of her moaning seems to say the same thing too."
            "Cassidy's on the verge of losing it, about to explode."
            "And she's going to take me with her too!"
            call cum_reaction (cassidy, 'vaginal', sexperience_min) from _call_cum_reaction_75
            if _return == "vaginal_outside":
                show sexinserts chest cassidy zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "I have to wait for the exact moment Cassidy's weight is in the air."
                "And when I feel it happen, I make my move without hesitation."
                show cassidy reverse cowgirl -vaginal
                "My cock slides out of her pussy before she knows what's happening."
                "The sound of her surprise mixes with the moans of her orgasm."
                show cassidy reverse cowgirl cumshot with vpunch
                if CONDOM:
                    "And the second she sits back down, I shoot my load."
                else:
                    "And the second she sits back down, I shoot my load over her."
                    show cassidy reverse cowgirl pleasure dickcum -cumshot
                    show sexinserts chest cassidy cum zorder 1 at center, zoomAt(1, (700, 820))
                    show sexinserts belly cassidy cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    $ cassidy.love += 1
                    "It spatters up Cassidy's body, running down over her slick skin."
                with vpunch
                "She sits upright for a moment longer, gasping and panting."
                with vpunch
                "Then she keels over, tumbling off of me and onto the bed."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_condom":
                "I don't think I could get out from under Cassidy if I tried."
                "But we already took precautions, so I don't have to worry."
                "And so I just lie back and let nature take its course."
                "As her muscles begin to quiver and shake, she sets me off too."
                with vpunch
                "I shoot my load while I'm as deep in her pussy as I can get."
                with vpunch
                "And it only seems to make her orgasm that much more intense."
                with vpunch
                "Cassidy rides my cock until the very last moment, gasping and panting."
                "Then she keels over, tumbling off of me and onto the bed."
            elif _return == "vaginal_inside_pill":
                cassidy.say "I'm on the pill..."
                cassidy.say "So you can let it happen...okay?!?"
                "I don't think I could get out from under Cassidy if I tried."
                "Which makes me all the more thankful for that timely reminder."
                "And so I just lie back and let nature take its course."
                "As her muscles begin to quiver and shake, she sets me off too."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                $ cassidy.love += 2
                "I shoot my load while I'm as deep in her pussy as I can get."
                with vpunch
                "And it only seems to make her orgasm that much more intense."
                with vpunch
                "Cassidy rides my cock until the very last moment, gasping and panting."
                show cassidy reverse cowgirl pleasure flacid dickcum vaginaldrip -creampie
                "Then she keels over, tumbling off of me and onto the bed."
            elif _return == "vaginal_inside_pregnant":
                cassidy.say "You already got me pregnant..."
                cassidy.say "So you can let it happen...okay?!?"
                "I don't think I could get out from under Cassidy if I tried."
                "Which makes me all the more thankful for that timely reminder."
                "And so I just lie back and let nature take its course."
                "As her muscles begin to quiver and shake, she sets me off too."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                $ cassidy.love += 3
                "I shoot my load while I'm as deep in her pussy as I can get."
                with vpunch
                "And it only seems to make her orgasm that much more intense."
                with vpunch
                "Cassidy rides my cock until the very last moment, gasping and panting."
                show cassidy reverse cowgirl pleasure flacid dickcum vaginaldrip -creampie
                "Then she keels over, tumbling off of me and onto the bed."
            elif _return == "vaginal_inside_mad":
                show cassidy reverse cowgirl normal
                cassidy.say "No, no, no..."
                cassidy.say "Don't do it..."
                cassidy.say "You have to pull out!"
                "Cassidy's desperate warnings snap me back to reality."
                "And I struggle to get out from under her."
                "But it's already too late."
                show cassidy reverse cowgirl pleasure creampie with vpunch
                #$ cassidy.impregnate()
                $ cassidy.love -= 5
                "I shoot my load while I'm as deep in her pussy as I can get."
                with vpunch
                "And it only seems to make her orgasm that much more intense."
                with vpunch
                "Cassidy rides my cock until the very last moment, gasping and panting."
                show cassidy reverse cowgirl normal flacid dickcum vaginaldrip -creampie
                "Then she keels over, tumbling off of me and onto the bed."
                "She stares up at me, a look of horror on her face that mirrors my own."
            elif _return == "vaginal_inside_happy":
                "I remember that I need to pull out before it's too late."
                "But the moment I try to do so, Cassidy presses herself down onto me."
                show cassidy reverse cowgirl normal
                cassidy.say "No, no, no..."
                cassidy.say "Don't do it..."
                cassidy.say "I want you to cum in me!"
                "I struggle to get out from under Cassidy."
                "But it's already too late."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                #$ cassidy.impregnate()
                $ cassidy.love += 5
                "I shoot my load while I'm as deep in her pussy as I can get."
                with vpunch
                "And it only seems to make her orgasm that much more intense."
                with vpunch
                "Cassidy rides my cock until the very last moment, gasping and panting."
                show cassidy reverse cowgirl pleasure flacid dickcum vaginaldrip -creampie
                "Then she keels over, tumbling off of me and onto the bed."
                "Which leaves me to worry about what she just did."
    return

label cassidy_sleep_date_fuck_sub(location="hero"):
    scene bg bedroom1
    show cassidy naked
    if cassidy_sad or cassidy.love < 120:
        if cassidy_sad:
            show cassidy sad
        cassidy.say "Can I go home now?"
        mike.say "You don't want to stay and cuddle?"
        if cassidy_sad:
            cassidy.say "Not after what you did."
        else:
            cassidy.say "I guess, if that's what you want, Master."
        menu:
            "You may go":
                show cassidy normal
                mike.say "Fine, you were a good pet. You can go."
                $ cassidy.love += 1
                "Cassidy gathers her things and without any other words and heads up the stairs."
                call sleep from _call_sleep_63
                $ game.room = "bedroom1"
            "Stay":
                show cassidy sad
                mike.say "No, stay. I want to use those big, beautiful boobs as pillows tonight."
                $ cassidy.love -= 3
                $ cassidy.sub += 1
                cassidy.say "Very well, Master."
                show cuddle cassidy
                "Cassidy stretches out on my bed and makes herself available. I curl up next to her and fall asleep with my head between those two gorgeous tits."
                call sleep ("cassidy") from _call_sleep_77
    else:
        cassidy.say "Would you like me to stay the night, Master?"
        menu:
            "You should go":
                mike.say "I have an early morning tomorrow, I'm sorry."
                $ cassidy.love -= 1
                if cassidy.love > 160:
                    "Cassidy gathers her things, and gives me a goodbye kiss before leaving."
                else:
                    "Cassidy gathers her things and without any other words, heads up the stairs."
                call sleep from _cassidy_sleep_date_fuck_sub
                $ game.room = "bedroom1"
            "I'd love that":
                mike.say "Yes, my darling, you should stay here."
                $ cassidy.love += 1
                $ cassidy.sub += 1
                show cuddle cassidy
                cassidy.say "Thank you, Master."
                if cassidy.love > 160:
                    cassidy.say "I love you so much, Master!"
                    mike.say "I love you too, my beautiful pet!"
                "Cassidy stretches out on my bed and makes herself available. I curl up next to her and fall asleep with my head between those two gorgeous tits."
                call sleep ("cassidy") from _call_sleep_29
    $ game.room = "bedroom1"
    return


label cassidy_fuck_date_dom(location="hero"):
    $ game.room = "livingroom"
    $ cassidy.sexperience += 1
    scene bg livingroom
    show cassidy annoyed
    with fade
    cassidy.say "Wow, [hero.name], you have a good job. Why do you live...here? You could afford something really nice!"
    mike.say "Perhaps you overestimate how much I make."
    show cassidy normal
    cassidy.say "Maybe. Whatever. Take me to your bedroom."
    scene bg bedroom1
    $ game.room = "bedroom1"
    show cassidy
    with fade
    menu:
        "Get on the bed":
            mike.say "Get on the bed."
            $ cassidy.love -= 5
            $ cassidy.sub += 5
            cassidy.say "Just who do you think is in charge here, [hero.name]?"
            mike.say "I, uh."
            cassidy.say "Yeah, it's not you."
        "What do you want me to do?":
            mike.say "What would you like me to do?"
            $ cassidy.love += 1
            $ cassidy.sub -= 1
    $ result = randint(1, 2)
    if cassidy.love < 160 or result == 1:
        call cassidy_dom_oral from _call_cassidy_dom_oral
    else:
        cassidy.say "Tonight I'll let you fuck my pussy, if you use a condom."
        menu:
            "Agree" if hero.has_condom():
                call cassidy_missionary_pussy_dom from _call_cassidy_missionary_pussy_dom
            "No":
                cassidy.say "Well, in that case..."
                call cassidy_dom_oral from _call_cassidy_dom_oral_1
    return

label cassidy_missionary_pussy_dom:
    $ CONDOM = hero.use_condom()
    show cassidy missionary out with vpunch
    "Cassidy lays down on the bed while I'm putting on the condom requested."
    "This is quite a step for her, allowing herself to be vulnerable, even though she still sees herself as in charge."
    "It's possible this relationship could work out after all."
    show cassidy missionary condom vaginal
    cassidy.say "Do me now before I change my mind, [hero.name]!"
    "Cassidy takes a sharp breath as I enter her, the sound of the air through her teeth almost a spasm of anticipation."
    cassidy.say "Oh! Oh my God!"
    "Holding her legs as far apart as I can, I slowly thrust my dick into her, going a little deeper every stroke until I can feel the tip of my head pressing against her cervix."
    "She makes little noises, moans in the back of her throat that grow louder with each thrust."
    show cassidy missionary eyes_close mouth_pleasure
    cassidy.say "Oh yes! Yes, [hero.name], that's...oh God yes!"
    "I can feel her pussy spasm repeatedly as she orgasms, and then she goes goes limp, smiling at me while I finish."
    "Just a few more thrusts and I'll be ready to blow!"
    with vpunch
    "When I finally can't take anymore, I orgasm, filling the condom up with my sticky cum."
    show cassidy missionary eyes_ahegao cum with vpunch
    "When it's all over, I pull out of her and go limp."
    with vpunch
    if cassidy.lesbian > MIN_LES_GIRL_SEX:
        $ cassidy.lesbian -= 1
    hide cassidy missionary
    show cassidy naked happy
    with fade
    return

label cassidy_sleep_date_fuck_dom(location="hero"):
    if cassidy.love > 160:
        cassidy.say "Oh, that was so good. Snuggle me tonight and keep me warm, [hero.name]."
        show cuddle cassidy
        "I do as she bids, pressing my body alongside hers and pulling the blankets over both of us."
        "As she drifts off to sleep, she says sleepily..."
        cassidy.say "I love you."
        mike.say "I love you too, my Mistress."
        "We drift off to sleep, spooning for the entire night."
        $ cassidy.love += 5
        $ cassidy.sub -= 2
        call sleep ("cassidy") from _call_sleep_80
    else:
        cassidy.say "That was fun, [hero.name]! See you tomorrow!"
        menu:
            "Demand she stay":
                mike.say "No, stay!"
                $ cassidy.love -= 5
                $ cassidy.sub += 2
                show cassidy angry
                cassidy.say "[hero.name], you're the bitch in this scenario, not me. You heel, not me. Sit, stay, bark? That's you."
                "She grabs her things and departs quickly, leaving no argument. I hear the front door slam on her way out."
                call sleep from _call_sleep_81
            "Beg she stay":
                mike.say "Please, Mistress! Stay with me for the night?"
                $ cassidy.love += 5
                $ cassidy.sub -= 2
                if cassidy.love > 120:
                    cassidy.say "Well, you have been a good boy. I suppose I can stay. Promise you'll be good?"
                    mike.say "Yes, Mistress, of course I'll be good!"
                    show cuddle cassidy
                    "We drift off to sleep, spooning for the entire night."
                call sleep ("cassidy") from _call_sleep_30
            "Let her go":
                $ cassidy.sub -= 1
                mike.say "Good night, Mistress!"
                "She gives me a quick kiss and then disappears up the stairs. I go to sleep, satisfied with my work."
                call sleep from _call_sleep_25
    $ game.room = "bedroom1"
    return

label cassidy_fuck_mc_office:
    $ end_scene = False
    while not end_scene:
        menu:
            "Finger her" if not cassidy.flags.fingered:
                call cassidy_finger from _call_cassidy_finger
            "Fuck her tits":
                call cassidy_tittyfuck from _call_cassidy_tittyfuck_1
                $ end_scene = True
            "Reverse cowgirl" if hero.sexperience >= 10:
                call cassidy_fuck_office_reverse_cowgirl (10) from _call_cassidy_fuck_office_reverse_cowgirl
                $ end_scene = True
    return

label cassidy_remove_top:
    show cassidy
    mike.say "Take off your top."
    $ cassidy.flags.topless = TemporaryFlag(True, "day")
    show cassidy topless
    if cassidy.sub < 90:
        cassidy.say "Yes, Master."
    else:
        cassidy.say "Anything you want, Master!"
    hide cassidy
    return

label cassidy_wear_top:
    show cassidy
    mike.say "Put your top back on."
    $ cassidy.flags.topless = TemporaryFlag(False, "day")
    show cassidy -topless
    if cassidy.sub < 90:
        cassidy.say "Yes, Master."
    else:
        cassidy.say "Anything you want, Master!"
    hide cassidy
    return

label cassidy_finger:
    show cassidy
    "I put one hand beneath Cassidy's skirt, sliding it up her thigh toward her pussy."
    if cassidy.love > 160 or cassidy.sub == 100:
        $ cassidy.flags.wet = TemporaryFlag(True, "day")
        show cassidy happy blush wet
        "She's already wet and ready when I get there. I press first one finger, then two into her warm flesh, separating her lips."
        "I find her clitoris and gently massage it, back and forth inside her vulva, not really penetrating but clearly stimulating her."
        "She wraps an arm around my neck and rests her head against my shoulder, moaning softly."
        if not cassidy.flags.fingered:
            "I feel her spasm against me, and a new rush of wetness covers my hand."
        else:
            cassidy.say "I love it when you touch me, Master!"
    elif cassidy.love > 100 or cassidy.sub > 80:
        show cassidy blush
        "When I get there, she is warm but not quite wet. But as soon as I separate her lips and touch her clit, the juices start to flow."
        "As I gently caress her clit, a soft half-hum, half-moan comes from the back of her throat."
        mike.say "Do you like that, my pet?"
        cassidy.say "Yes, yes I do, Master."
        $ cassidy.flags.wet = TemporaryFlag(True, "day")
        show cassidy blush wet
        if not cassidy.flags.fingered:
            $ cassidy.love += 1
        $ cassidy.flags.humiliation += 1
    else:
        show cassidy sad
        "She stands there, quite still, allowing me access, but not responding. When I reach her pussy it is warm but dry."
        "I separate her pussy lips and gently, carefully slip inside and find her clit."
        show cassidy blush
        "After a few moments, her juices finally start to flow, albeit slowly."
        "I continue working her with my finger until I'm sure she's worked up, and then finally withdraw my hand."
        "I make a show of licking my fingers clean while she watches me."
        if not cassidy.flags.fingered:
            $ cassidy.sub += 1
        $ cassidy.flags.humiliation += 2
    hide cassidy
    $ cassidy.set_flag("fingered", True, "day", "+")
    return

label cassidy_tittyfuck(topless=None):
    if topless is None:
        $ cassidy.flags.topless = True
        $ topless = cassidy.flags.topless
    show cassidy tittyfuck down
    with fade
    "She slides those beautiful breasts around my cock, hugging it with her warmth. I couldn't keep from having a full erection if I wanted to, and I don't want to!"
    "She moves her entire body, caressing my shaft up and down with her tits. Her eyes focus on mine the entire time, and the more I enjoy myself, the bigger her smile gets."
    cassidy.say "Do you like this?"
    mike.say "Oh yeah. Don't stop."
    show cassidy tittyfuck up
    pause 0.4
    show cassidy tittyfuck down at startle(0.05,-10)
    pause 0.6
    show cassidy tittyfuck up
    pause 0.4
    show cassidy tittyfuck down at startle(0.05,-10)
    pause 0.6
    show cassidy tittyfuck up
    pause 0.4
    show cassidy tittyfuck down at startle(0.05,-10)
    cassidy.say "Are you ready for what's next?"
    "I don't have to answer in words; my cock is warm and the precum is mixing with her sweat to lubricate her. I'm clearly ready."
    show cassidy tittyfuck blow
    show sexinserts head cassidy zorder 1 at center, zoomAt(1, (720, 810))
    "She leans her head forward and takes the tip of my shaft into her mouth. Her tongue flicks around, while her tits continue to massage me."
    mike.say "Faster!"
    show cassidy tittyfuck up
    pause 0.4
    show cassidy tittyfuck down at startle(0.05,-10)
    pause 0.6
    show cassidy tittyfuck up
    pause 0.4
    show cassidy tittyfuck down at startle(0.05,-10)
    pause 0.6
    show cassidy tittyfuck up
    pause 0.4
    show cassidy tittyfuck down at startle(0.05,-10)
    "She complies, speeding up and taking just the head into her mouth."
    mike.say "Oh, fuck, Cassidy, you were right about this being the best damn blowjob I've ever had!"
    cassidy.say "Mf, mmmf mmf mf!"
    "I have no idea what she tried to say, and it doesn't matter. I'm about to explode."
    menu:
        "Cum in her mouth":
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down at startle(0.05,-10)
            pause 0.6
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down at startle(0.05,-10)
            pause 0.6
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down cum
            show sexinserts head cassidy cum zorder 1 at center, zoomAt(1, (720, 810))
            with vpunch
            $ cassidy.love += 1
            "I don't have the time or inclination to pull out, and I explode between her lips, filling her mouth so much that it leaks all over me."
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down with vpunch
            "She doesn't stop, though, instead she just slows down. With every caress I can feel the muscles in my dick spasm, half objection and half ecstasy."
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down with vpunch
            "Until finally, I can't take it anymore, and I go completely limp between her tits."
            hide sexinserts
            hide cassidy tittyfuck
            show cassidy topless casual normal blush wet
            with fade
            $ cassidy.flags.wet = TemporaryFlag(True, 1)
            if cassidy.sub > 75:
                cassidy.say "Did I do a good job, Master?"
            else:
                cassidy.say "I hope it was good for you."
            mike.say "Yes, absolutely!"
        "Cum on her face":
            $ cassidy.sub += 1
            mike.say "I'm going to cum!"
            hide sexinserts
            show cassidy tittyfuck -blow
            "I pull back a little, and Cassidy raises her head."
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down cum mouth_close with vpunch
            pause 0.6
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down cum eyes_close cumface with vpunch
            pause 0.6
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down cum eyes_open cumbody with vpunch
            "At first it's just a spurt, but when I look into her eyes, it just keeps coming and coming, dousing her face in sticky, gooey wetness."
            show cassidy tittyfuck up
            pause 0.4
            show cassidy tittyfuck down -cum mouth_open with vpunch
            cassidy.say "Well, I don't think you enjoyed that at all, Sweetie."
            mike.say "Mmmm."
            hide cassidy tittyfuck
            $ cassidy.flags.facecum = TemporaryFlag(True, 1)
            show cassidy topless casual normal blush facecum
            with fade
            "I wanted to be more eloquent. I was thinking \"Yeah, that was fucking awesome\", but that was all I could get out."
    if not topless:
        $ cassidy.flags.topless = TemporaryFlag(True, 1)
        $ cassidy.flags.humiliation += 1
    return

label cassidy_fuck_office_reverse_cowgirl(sexperience_min):
    show cassidy normal
    if game.flags.dwaynedead:
        cassidy.say "Mommy's taking me out to lunch."
    else:
        cassidy.say "Daddy's taking me out to lunch."
    cassidy.say "So I haven't got much time!"
    "I break away from Cassidy, hurrying to close and lock the door."
    "But when I turn around, she has a surprise for me."
    show cassidy topless with dissolve
    "Cassidy's already stripping off her clothes as she stands in front of the desk."
    show cassidy naked with dissolve
    "And she beckons me over as I begin to do the same."
    cassidy.say "You think you can do me nice and quick?"
    if game.flags.dwaynedead:
        cassidy.say "Like, before Mommy starts to wonder where I am?"
    else:
        cassidy.say "Like, before Daddy starts to wonder where I am?"
    mike.say "Oh, I think I can manage that!"
    "I take Cassidy by the hand and lead her over to the sofa."
    "Then I lie down, pulling her atop me."
    "Cassidy giggles and scrambles onto my lap, her back turned to me."
    scene cassidy reverse cowgirl
    show cassidy reverse cowgirl office
    with fade
    "Reverse cowgirl?"
    "I can go with that!"
    menu:
        "Fuck her ass" if hero.sexperience >= sexperience_min + 5:
            "Cassidy grabs hold of my cock with both hands."
            "She's still giggling as she rubs it up and down."
            "And getting into the same mood, I grab hold of her buttocks."
            cassidy.say "Ooh!"
            cassidy.say "I like where this is going!"
            cassidy.say "Mmm..."
            cassidy.say "Hurry up and get that thing inside me!"
            cassidy.say "I wanna feel you filling me up, [hero.name]!"
            "I'm almost as turned on by Cassidy's hunger as I am by her nakedness."
            "And so I hurry to do as she asks."
            "But not without a little twist all of my own."
            "The kind of twist that makes this more interesting for me."
            "I have to pull back a bit for it to work."
            "Just enough to make Cassidy let go of my cock."
            "But then I can reposition and aim it at my intended target."
            cassidy.say "Oh no..."
            cassidy.say "I think you missed it!"
            mike.say "Don't worry, Cassidy..."
            mike.say "I'm right on target!"
            show cassidy reverse cowgirl anal
            "With that, I pull her down and onto my cock."
            "And a moment later I feel the satisfying sensation of sinking into Cassidy's ass!"
            cassidy.say "Oh god..."
            cassidy.say "My butt!"
            show cassidy reverse cowgirl pleasure
            cassidy.say "Oh...it feels SO good!"
            mike.say "Cassidy..."
            mike.say "You horny little..."
            mike.say "Little bitch!"
            cassidy.say "Oh yeah..."
            cassidy.say "That's me..."
            cassidy.say "That's...oh fuck!"
            "All of the natural resistance in Cassidy's body seems to disappear in an instant."
            "And with it gone, I find myself inching into her."
            "She sinks down on my cock a little at a time."
            "The effects of which are written all over her face."
            "There's no more talking from Cassidy now."
            "All the words are replaced with what sound like animalistic noises."
            "She seems to sit, frozen by the sensation of my cock inside her."
            "But then the spell is broken, and Cassidy starts to move atop me."
            "Slowly at first, and then with ever increasing speed, she rides me."
            "And I find myself struggling to keep up once she's going as fast as she can!"
            "I have my hands on Cassidy's haunches, holding on tight."
            "More to serve as leverage for my own thrusts than to keep her in place."
            "She's pushing down with all of her weight right now."
            "Grinding herself onto my cock for all she's worth!"
            "Every time I catch a glimpse of Cassidy's face, I see she's smiling."
            "And at first I think it's from the sheer pleasure of being fucked so damn hard."
            "But then I begin to see the mischief and amusement in her eyes too."
            "And that tells me she's getting off on doing this here and with me."
            "She knows that Dwayne's in the same building as us right now."
            "But he has no idea his little girl has my cock up inside of her!"
            "The danger of the scenario and the thrill Cassidy's getting from it finally sinks in."
            "And I feel the same sense of danger and excitement flooding my own body too."
            "Without conscious thought, I redouble my efforts."
            "Which means that pretty soon I'm fucking Cassidy as hard as she's riding me."
            "Her moans increase in volume as well as intensity."
            show cassidy reverse cowgirl ahegao
            "And she nods as she looks over her shoulder at me."
            "Which lets me know that she likes it and wants more."
            "But that might be a problem, as I can feel that I'm about to cum!"
            call cum_reaction (cassidy, "anal", sexperience_min) from _call_cum_reaction_76
            if _return == "anal_inside":
                "Not that I have anything to worry about."
                "Because I'm currently as far up Cassidy's ass as I can possibly get!"
                "That means I can keep a strong hold on her as I lose it inside of her."
                show cassidy reverse cowgirl creampie with vpunch
                "She bucks and twists as I shoot my load, but stays firmly in place."
                with vpunch
                "I can feel that she's cumming too, and see it from the way she arches her back."
                $ cassidy.sub += 1
                with vpunch
                "And once done, she visibly sags, the last of her energy spent."
            elif _return == "anal_outside":
                show sexinserts chest cassidy zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "I strengthen my hold on Cassidy as I pull my cock out of her."
                "We didn't use a condom, so the last thing I want is to cum inside of her."
                show cassidy reverse cowgirl -anal
                "The motion seems to push her over the edge too."
                "She bucks and twists as I shoot my load, but stays firmly in place."
                show cassidy reverse cowgirl cumshot
                show sexinserts chest cassidy cum zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                with vpunch
                "And I shoot my load over her belly."
                $ cassidy.love += 1
                with vpunch
                "Once done, she visibly sags, the last of her energy spent."
                hide sexinserts
                hide bellycum
            $ cassidy.flags.anal += 1
        "Fuck her pussy":
            "Cassidy grabs hold of my cock with both hands."
            "She's still giggling as she rubs it up and down."
            "And getting into the same mood, I grab hold of her buttocks."
            cassidy.say "Ooh!"
            cassidy.say "I like where this is going!"
            call check_condom_usage (cassidy, 180) from _call_check_condom_usage_36
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cassidy reverse cowgirl condom
            cassidy.say "Mmm..."
            cassidy.say "Hurry up and get that thing inside me!"
            cassidy.say "I wanna feel you filling me up, [hero.name]!"
            "I'm almost as turned on by Cassidy's hunger as I am by her nakedness."
            "And so I hurry to do as she asks."
            show cassidy reverse cowgirl vaginal
            "I'm helped in this by the fact that she still has a firm hold on my cock."
            "So all I have to do is thrust upwards as she guides it home."
            "Cassidy and I both let out a moan as it presses against her pussy for the first time."
            "But she's the one that pushed even harder, making sure it sinks in there."
            mike.say "Cassidy..."
            mike.say "You horny little..."
            mike.say "Little bitch!"
            cassidy.say "Oh yeah..."
            cassidy.say "That's me..."
            show cassidy reverse cowgirl pleasure
            cassidy.say "That's...oh fuck!"
            "All of the natural resistance in Cassidy's body seems to disappear in an instant."
            "And with it gone, I find myself sliding straight into her."
            "She sinks down on my cock in one smooth motion."
            "The effects of which are written all over her face."
            "There's no more talking from Cassidy now."
            "All the words are replaced with what sound like animalistic noises."
            "She seems to sit, frozen by the sensation of my cock inside her."
            "But then the spell is broken, and Cassidy starts to move atop me."
            "Slowly at first, and then with ever increasing speed, she rides me."
            "And I find myself struggling to keep up once she's going as fast as she can!"
            "I have my hands on Cassidy's haunches, holding on tight."
            "More to serve as leverage for my own thrusts than to keep her in place."
            "She's pushing down with all of her weight right now."
            "Grinding herself onto my cock for all she's worth!"
            "Every time I catch a glimpse of Cassidy's face, I see she's smiling."
            "And at first I think it's from the sheer pleasure of being fucked so damn hard."
            "But then I begin to see the mischief and amusement in her eyes too."
            "And that tells me she's getting off on doing this here and with me."
            "She knows that Dwayne's in the same building as us right now."
            "But he has no idea his little girl has my cock up inside of her!"
            "The danger of the scenario and the thrill Cassidy's getting from it finally sinks in."
            "And I feel the same sense of danger and excitement flooding my own body too."
            "Without conscious thought, I redouble my efforts."
            "Which means that pretty soon I'm fucking Cassidy as hard as she's riding me."
            "Her moans increase in volume as well as intensity."
            "And she nods as she looks over her shoulder at me."
            "Which lets me know that she likes it and wants more."
            "But that might be a problem, as I can feel that I'm about to cum!"
            call cum_reaction (cassidy, "vaginal", sexperience_min) from _call_cum_reaction_77
            if _return == "vaginal_condom":
                "Not that I have anything to worry about, as we're using a condom."
                "That means I can keep a strong hold on Cassidy as I lose it inside of her."
                with vpunch
                "She bucks and twists as I shoot my load, but stays firmly in place."
                show cassidy reverse cowgirl pleasure with vpunch
                "I can feel that she's cumming too, and see it from the way she arches her back."
                $ cassidy.love += 1
                with vpunch
                "And once done, she visibly sags, the last of her energy spent."
            elif _return == "vaginal_outside":
                show sexinserts chest cassidy zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "I strengthen my hold on Cassidy as I pull my cock out of her."
                show cassidy reverse cowgirl -vaginal
                "We didn't use a condom, so the last thing I want is to cum inside of her."
                "The motion seems to push her over the edge too."
                "She bucks and twists as I shoot my load, but stays firmly in place."
                show cassidy reverse cowgirl cumshot
                show sexinserts chest cassidy cum zorder 1 at center, zoomAt(1, (700, 820))
                show sexinserts belly cassidy cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                with vpunch
                "And I shoot my load over her belly."
                $ cassidy.sub += 1
                with vpunch
                "Once done, she visibly sags, the last of her energy spent."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_inside_pill":
                if game.flags.dwaynedead:
                    cassidy.say "Don't tell Mommy..."
                else:
                    cassidy.say "Don't tell Daddy..."
                cassidy.say "But I'm on the pill!"
                "I smile and silently thank Cassidy for the information."
                "That means I can keep a strong hold on Cassidy as I lose it inside of her."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                "She bucks and twists as I shoot my load, but stays firmly in place."
                with vpunch
                "I can feel that she's cumming too, and see it from the way she arches her back."
                $ cassidy.love += 2
                with vpunch
                "And once done, she visibly sags, the last of her energy spent."
            elif _return == "vaginal_inside_pregnant":
                cassidy.say "Cum in me..."
                cassidy.say "I want you to!"
                "I smile and shake my head, knowing full well that I already got Cassidy pregnant."
                "That means I can keep a strong hold on Cassidy as I lose it inside of her."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                "She bucks and twists as I shoot my load, but stays firmly in place."
                with vpunch
                "I can feel that she's cumming too, and see it from the way she arches her back."
                $ cassidy.love += 2
                with vpunch
                "And once done, she visibly sags, the last of her energy spent."
            elif _return == "vaginal_inside_happy":
                cassidy.say "Cum in me..."
                cassidy.say "I want you to!"
                if not game.flags.dwaynedead:
                    cassidy.say "It'll make Daddy so mad!"
                "Cassidy's demands catch me totally off-guard."
                "So much so that I lose it inside of her."
                with vpunch
                "She bucks and twists as I shoot my load, but stays firmly in place."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                #$ cassidy.impregnate()
                "I can feel that she's cumming too, and see it from the way she arches her back."
                with vpunch
                "And once done, she visibly sags, the last of her energy spent."
                $ cassidy.love += 5
                "But my own mind is filled with horror at the thought of what we just did."
            elif _return == "vaginal_inside_mad":
                cassidy.say "Don't cum in me..."
                cassidy.say "I can't get pregnant!"
                if not game.flags.dwaynedead:
                    cassidy.say "It'll make Daddy so mad!"
                "Cassidy's demands catch me totally off-guard."
                "So much so that I lose it inside of her."
                with vpunch
                "She bucks and twists as I shoot my load, but stays firmly in place."
                show cassidy reverse cowgirl ahegao creampie with vpunch
                #$ cassidy.impregnate()
                "I can feel that she's cumming too, and see it from the way she arches her back."
                with vpunch
                "And once done, she visibly sags, the last of her energy spent."
                cassidy.say "Oh no!"
                cassidy.say "What have you done?!?"
                $ cassidy.love -= 5
                mike.say "What have I done?"
                mike.say "Don't you mean what have WE done?!?"
    "Cassidy turns to smile at me, biting her lip."
    hide cassidy reverse cowgirl
    scene expression f"bg {game.room}"
    show cassidy happy naked
    with fade
    "She's trying to look cocky and confident."
    "But I can tell that she's a little dizzy from her exertions."
    cassidy.say "I gotta go, [hero.name]."
    if game.flags.dwaynedead:
        cassidy.say "Mommy will be wondering where I am."
    else:
        cassidy.say "Daddy will be wondering where I am."
    cassidy.say "But I'll be able to feel what you just did to me for the rest of the day!"
    show cassidy normal casual
    "Cassidy hurries to get dressed, and I do the same at a more leisurely pace."
    "Once she's gone, I take my time about getting back to work."
    hide cassidy
    "All the time reflecting on how I could get used to this kind of stress-relief in the office!"
    $ cassidy.sexperience += 1
    return


label cassidy_grope_male:
    show cassidy
    if cassidy.flags.topless:
        "I put my hands on Cassidy's bare chest, running my fingers along her skin, making circles around that great bosom until I get to her nipples."
        if cassidy.love > 160:
            show cassidy happy blush
            "She responds immediately, her nipples hardening almost on command."
            "She makes a soft, happy sound."
        elif cassidy.love > 100 or cassidy.sub > 75:
            show cassidy blush
            "It takes a few seconds, but her nipples respond, hardening under my gentle touch."
            "She squeaks just slightly as I pull my hands away."
            $ cassidy.love += 1
            $ cassidy.set_flag("humiliation", 1, mod="+")
        else:
            show cassidy sad blush
            "She stands there, quite still, allowing me to touch her freely but not responding."
            "After a few moments, her nipples finally stiffen a little bit under my fingers. I tweak them gently before finishing."
            $ cassidy.set_flag("humiliation", 2, mod="+")
            $ cassidy.sub += 1
    else:
        "I put my hands on Cassidy's chest, running my fingers on the fabric."
        if cassidy.love > 160:
            show cassidy happy blush
            "She responds immediately, her nipples hardening almost on command."
            "She makes a soft, happy sound."
        elif cassidy.love > 100 or cassidy.sub > 75:
            show cassidy blush
            "It takes a few seconds, but her nipples respond, hardening under my gentle touch."
            "She squeaks just slightly as I pull my hands away."
            $ cassidy.love += 1
            $ cassidy.flags.humiliation += 1
        else:
            show cassidy sad blush
            "She stands there, quite still, allowing me to touch her freely but not responding."
            "After a few moments, her nipples finally stiffen a little bit under my fingers. I tweak them gently before finishing."
            $ cassidy.flags.humiliation += 2
            $ cassidy.sub += 1
    hide cassidy
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
