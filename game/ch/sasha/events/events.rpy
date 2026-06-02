init python:
    Event(**{
    "name": "sasha_scottie_threesome",
    "priority": 500,
    "label": "sasha_scottie_threesome",
    "music": "music/roa_music/smile_for_me.ogg",
    "duration": 2,
    "conditions": [
        IsDayOfWeek(6, 7),
        IsHour(18),
        HeroTarget(IsRoom("livingroom")),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("scottiethreesome"),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "sasha_piss_off",
    "label": "sasha_piss_off",
    "priority": 500,
    "conditions": [
        PersonTarget(sasha,
            IsActive(),
            HasCheated(),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

    InteractEvent(**{
    "name": "followsamadvice",
    "label": "followsamadvice",
    "priority": 750,
    "conditions": [
        PersonTarget(sasha,
            IsActive(),
            IsFlag("cheatedSamAdvice"),
            ),
        ],
    "do_once": True,
    "music": "music/roa_music/smile_for_me.ogg",
    })

    Event(**{
    "name": "sasha_asleep",
    "label": "sasha_asleep",
    "priority": 1500,
    "conditions": [
        HeroTarget(IsRoom("bedroom3")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsActivity("sleep"),
            ),
        ],
    "do_once": False,
    "once_hour": False,
    })

    InteractEvent(**{
    "name": "sasha_murder_talk_bree",
    "label": "sasha_murder_talk_bree",
    "do_once": True,
    "conditions": [
        PersonTarget(sasha,
            IsActive(),
            ),
        PersonTarget("kylie",
            IsFlag("killed", "bree")
            ),
        ],
    })

    Event(**{
    "name": "sasha_bree_collar_reaction",
    "label": "sasha_bree_collar_reaction",
    "priority": 500,
    "conditions": [
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("collared", False),
            ),
        ],
    "do_once": True,
    })

label sasha_murder_talk_bree:
    "There was no way things were ever just going to go back to normal after what happened."
    "I mean, how could they after poor [bree.name] was murdered in front of Sasha and me?"
    "Even worse, the unthinkable deed was committed by Kylie."
    "The girl that I was dating at the time."
    "A girl that I failed to see was actually some kind of psycho!"
    "I know that I should make an effort to sit down and talk to Sasha."
    "But there's one crazy thing that's been stopping me."
    "It's insane, and yet it's keeping me from knowing how she actually feels."
    "In the end though, I'm more afraid of leaving it too late."
    show sasha sad at center, zoomAt(1.0, (640, 720))
    "And so I insist that Sasha and I have the inevitable talk."
    show sasha at center, traveling(1.5, 0.5, (640, 1040))
    mike.say "Erm, Sasha?"
    show sasha whining
    sasha.say "Yeah, [hero.name]?"
    show sasha sad
    mike.say "I don't know about you..."
    mike.say "But I'm still kind of reeling from what happened."
    "A look of relief comes over Sasha's face the moment I say this."
    "It seems that she's been waiting for a chance to talk about it too."
    show sasha whining
    sasha.say "Me too, [hero.name], me too."
    show sasha sad
    mike.say "Really?!?"
    mike.say "That's great!"
    mike.say "I mean...I mean it's great that we can talk..."
    mike.say "Talk about [bree.name], that is..."
    show sasha whining
    sasha.say "You sound surprised."
    sasha.say "Did you think I'd just brushed it off or something?"
    show sasha sad
    "I can feel my cheeks starting to turn red."
    "I'm sweating too as Sasha puts me on the spot."
    mike.say "Well, the thing is, Sasha..."
    mike.say "I wasn't sure if you were in mourning or not."
    mike.say "Because...because you always wear black!"
    show sasha surprised
    "Sasha looks at me, eyes wide and her mouth hanging open."
    "She says nothing for what feels like the longest time."
    show sasha happy at startle
    "And then, out of nowhere, she bursts into peals of laughter."
    "I can't help joining in too, feeling the sense of relief it brings."
    "Neither of us is laughing out of malice or amusement at the fate of poor [bree.name]."
    "It's out of sheer and helpless gallows humour that we're laughing at all."
    show sasha shout
    sasha.say "Oh god..."
    sasha.say "That's so not funny!"
    show sasha sadsmile
    mike.say "Well, it kind of is..."
    mike.say "You...you remember when [bree.name] asked you..."
    mike.say "Asked you how many different shades of black you had in your wardrobe?"
    show sasha happy at startle
    "Sasha erupts into another round of laughter."
    show sasha cry at center, traveling(2.0, 0.2, (640, 1340))
    pause 0.2
    with vpunch
    "And then a moment later, she collapses against my shoulder in a flood of tears."
    sasha.say "Oh shit..."
    sasha.say "I'm going to miss her."
    mike.say "Me too - and I feel like it was my fault too."
    "I feel Sasha wrap her arms around me as I say this."
    "She shakes her head and then buries her face in my chest."
    sasha.say "It's not, [hero.name], it's not."
    sasha.say "We've all missed the signs with someone we were dating."
    sasha.say "You're just so into them that it passes you by."
    mike.say "I think I need you to keep telling me that, Sasha."
    mike.say "At least for a little while."
    sasha.say "Okay, [hero.name]."
    sasha.say "And we can both be a little more sunny too."
    sasha.say "Maybe that way we can keep [bree.name]'s spirit alive."
    return

label sasha_asleep:
    if samantha.room == game.room:
        if sasha.hidden:
            show multisleep sashasam samantha
            "Samantha is sleeping, I should leave before I wake her up..."
        else:
            show multisleep sashasam sasha samantha
            "Sasha and Samantha are sleeping, I should leave before I wake them up..."
    else:
        show sleep sasha
        "Sasha is sleeping, I should leave before I wake her up..."
    $ game.room = "secondfloor"
    return

label followsamadvice:
    "Though her advice is pretty scary when I think about what it means I have to do, I'm committed to doing what Sam told me to."
    "And so the only concession that I can really make to myself is wanting to pick exactly the right moment to confront Sasha."
    "This means that for a short and painful space of time, I have to make sure that I avoid bumping into her around the house."
    "Otherwise, I fear that I'll be pressured into spewing out all of my feelings in one hopeless jumble and not making any sense whatsoever."
    show sasha upset at center, zoomAt(1.0, (640, 720))
    "Finally, I see Sasha and I feel ready to make that leap of faith."
    "She looks vaguely unhappy to see me, but there's no visible sign of her wanting to scream or throw things at me."
    show sasha at center, traveling(1.5, 0.5, (640, 1040))
    "I take a deep breath and then close the short distance between us."
    "Here goes nothing..."
    mike.say "Sasha...I was wondering if...if we could talk?"
    "For a moment I think that Sasha's cold, unimpressed expression means that she's simply going to walk away and ignore me."
    show sasha annoyed
    "But then she takes a deep breath in and lets it out, as if trying to make a sound and gesture that expresses her current mood."
    "Or to be more precise, her current feelings towards me."
    show sasha upset
    mike.say "Please, Sasha?"
    mike.say "We can't go on avoiding each other like this."
    mike.say "Please talk to me, even if it's just so that you can tell me to crawl off and die in a corner somewhere..."
    show sasha sad
    "Hearing the emotion in my voice, Sasha's expression softens just a little."
    show sasha whining
    sasha.say "Okay, [hero.name] - I guess that this is the point where you collapse into tears and try to guilt me into forgetting what you did?"
    show sasha sad
    "Remembering the advice that Sam gave me, I take a deep breath of my own before answering."
    mike.say "No, Sasha - that's not it."
    mike.say "Whether or not you want to forgive me is your decision to make, not mine."
    mike.say "I just wanted the chance to tell you how sorry I am for what I've done."
    mike.say "It doesn't matter how serious we were at the time it happened either."
    mike.say "All that does matter is that it hurt you, and I see that clearly now."
    "I fall silent for a short while, watching as my words sink in."
    "While I might have been hoping for some kind of instant reaction, be it good or bad, I don't press her for one."
    "I have to keep in mind that what I'm doing is about showing Sasha that I understand how she feels and giving her the space to make a decision."
    mike.say "Like I said...I'm sorry."
    mike.say "So if you feel like talking about it - well, you know where to find me..."
    with hpunch
    "As I turn to go, there's the sudden sensation of a hand grabbing at my arm."
    "I look down to see Sasha's hand, holding on just above my wrist, and then look up, into her eyes."
    show sasha whining
    sasha.say "[hero.name]...wait..."
    sasha.say "If you can understand that...maybe I can understand your side of it too."
    sasha.say "We never did say that anything was exclusive about us, or set in stone back then."
    show sasha sadsmile
    "She bites her lip, clearly not enjoying the prospect what she has to say next."
    show sasha blush
    sasha.say "And...well, there might have been a couple of times that I saw an old boyfriend back then too..."
    show sasha embarrassed
    "Ah, so what's good for the goose is good for the gander too!"
    "But I can't exactly rub that in her face, now can I?"
    "Especially when I've just gone so far out of my way to play the part of the sensitive, modern guy that's in touch with her feelings."
    mike.say "Maybe we could just admit that neither of us is perfect?"
    mike.say "And then move on, you know - forget all about it?"
    show sasha normal
    "At this, Sasha nods and smiles weakly, leaning her head on my shoulder."
    "It's only a small gesture, but to me it means the world."
    $ sasha.flags.cheated = False
    $ sasha.flags.nodate = False
    $ sasha.flags.nokiss = False
    return

label sasha_piss_off:
    show sasha wtf
    sasha.say "Piss off!"
    $ sasha.love -= 1
    hide sasha
    return

label sasha_scottie_threesome:
    "When the evening of the threesome finally arrives, I try to put a brave face on things and look like I'm excited."
    "Though in reality, I'm disappointed to discover that my nerves haven't magically vanished as I hoped they would."
    "Sure, I'm more than a little scared at the thought of having to get intimate with another guy."
    "And yes, of course I'm worried that I might not 'measure up', if you get my meaning?"
    "But I'm also annoyed at myself for not being completely okay and at ease with everything too."
    "I've always thought of myself as a pretty modern and tolerant sort, with an adventurous streak and an open mind."
    "Yet I'm still apprehensive about getting it on with a hot girl while there's another guy there."
    show sasha normal at center, zoomAt(1.0, (640, 720))
    "Sasha doesn't help much at first, finding my worries amusing and enjoying the chance to tease me."
    show sasha shout at center, traveling(1.25, 0.5, (640, 880))
    sasha.say "Don't worry, [hero.name]."
    sasha.say "I'll be sure to warn you if you're gonna trip over Scottie's dick!"
    show sasha normal
    mike.say "Sasha, please!"
    show sasha shout
    sasha.say "Okay, okay..."
    sasha.say "But a word of warning - he does like to give it up the ass."
    sasha.say "And he can get confused as to what belongs to who when he's excited."
    show sasha happy
    sasha.say "So clench that pert little ass of yours nice and tight!"
    mike.say "SASHA!"
    mike.say "You're not helping!"
    show sasha happy at startle
    "Sasha chuckles at my outburst."
    show sasha flirt
    sasha.say "Don't worry - I wasn't trying to help!"
    "But then she stops and shakes her head, the laughter fading away."
    show sasha shout
    sasha.say "Sorry, sorry."
    sasha.say "Look, I know you've not done this kind of thing before."
    sasha.say "Well, at least not with another guy..."
    sasha.say "But it'll be fine, trust me."
    sasha.say "Scottie's got a big mouth, but deep down, he's a total pussycat."
    sasha.say "Just don't let him think that you're just a pussy, okay?"
    show sasha normal
    "I nod, trying my best to take Sasha's advice to heart."
    play sound door_knock
    "But just then there's the unmistakable sound of a knock at the front door."
    "I start at the noise, but Sasha puts a reassuring hand on my shoulder."
    show sasha shout
    sasha.say "Don't panic, [hero.name]."
    sasha.say "That'll be Scottie - I'll go let him in."
    hide sasha with easeoutright
    "With that she leaves me alone and goes to open the front door."
    "I hear little snippets of their greetings, but not enough to know what they're saying."
    show sasha at center, zoomAt(1.25, (940, 880))
    show scottie at center, zoomAt(1.25, (340, 900))
    with easeinright
    "And then Sasha reappears, with a guy who must be Scottie following close behind."
    "I see instantly that he's tall and pretty well-built, with long hair and a band T-shirt."
    "Even worse, he has that easy kind of confidence that comes with knowing what's on the cards."
    show sasha shout
    sasha.say "Scottie, [hero.name]."
    sasha.say "[hero.name], Scottie."
    show sasha normal
    show scottie happy
    scottie.say "Hey, man - how yah doing?"
    show scottie normal
    "I take hold of Scotties hand as soon as he thrusts it out to me."
    "And the moment that he squeezes it a little too tight, I begin to feel just a tad better about things."
    "Firstly, he doesn't sound like any kind of intellectual giant."
    "And secondly, I know an over the top handshake when I feel one."
    "Is he really trying to make himself seem more confident that he actually is right now?"
    "Whatever the truth of the matter, let's go with that, as it gives me a glimmer of hope here!"
    mike.say "Fine, Scottie, just fine."
    "Without warning, Scottie pulls me closer and leans in to deliver his next line."
    show scottie happy
    scottie.say "I hear this is your first time with two dudes, yeah?"
    show scottie normal
    "If that's what Sasha's already told him, there seems to be no point in denying it."
    "So I just nod once, hoping that'll be the end of it."
    show scottie happy
    scottie.say "Don't worry, dude."
    scottie.say "You just follow my lead, and you'll be fine."
    scottie.say "I know how to handle Sasha, you better believe it!"
    show scottie normal
    "I guess that last line was intended just for me, a bit of man-to-man banter."
    "But Scottie doesn't seem to know how to keep his voice down."
    "And so I see Sasha rolling her eyes in amused irritation behind his back."
    show sasha shout
    sasha.say "If that's the introductions over, shall we get down to it?"
    "Scottie slaps me on the back quite hard and unexpectedly, then rubs his hands together in anticipation."
    show scottie happy
    scottie.say "I thought you'd never ask!"
    show scottie normal
    mike.say "Ah, yeah - I guess that goes for me too..."
    scene bg bedroom1 with fade
    pause 0.1
    show sasha at center, zoomAt(1.25, (940, 880))
    show scottie at center, zoomAt(1.25, (340, 900))
    with easeinright
    "After we reconvene in my bedroom, I can feel my confidence beginning to return."
    "Maybe it's something to do with the familiar surroundings."
    "Or maybe this whole thing is just starting to feel that much easier."
    "But all the same, the three of us end up exchanging glances in silence for a couple of moments."
    "We're supposed to be getting on with it, but nobody seems to know where to start."
    show sasha topless with dissolve
    "This all changes when Sasha, not even waiting for an invitation, begins to strip off."
    "Another glance passes between Scottie and myself."
    hide scottie with dissolve
    "And then we're both hurrying to follow her lead, trying not to be the one left behind."
    show sasha naked at center, zoomAt(1.25, (640, 880)) with ease
    "Of course, Sasha manages to get naked first."
    "She climbs onto the bed and reclines among the pillows, watching the rest of the show."
    "By this time, Scottie and I are already down to our shorts."
    "We both make a desperate effort to make for the bed while still pulling them off."
    "Which means a hopping, staggering progress towards Sasha, with us almost falling on our faces along the way."
    "The haste we show in trying to reach her makes Sasha laugh in sheer delight."
    scene bg black
    show scottie 2hj
    with fade
    "And as soon as we're close enough, she reaches out, gripping a cock in each hand."
    sasha.say "Mmm..."
    sasha.say "Oh, boys..."
    sasha.say "Is all of this for me?"
    "Needless to say, this stops Scottie and me dead in our tracks."
    "Neither of us utters as much as a single word, but the sound of our breathing is heavy enough to be heard."
    "Sasha gives us a wicked smile as she rubs her hands up and down the shafts."
    sasha.say "Now, all I have to do is decide what to do with them..."
    show scottie 2hj lookright
    "Still holding onto both cocks, Sasha suddenly drives her shoulder into me."
    "Taken completely by surprise, I land on my back, bouncing a little on the mattress."
    show scottie dp bottom scottietop with fade
    "Before I can even try to get up, I feel Sasha straddling me from above."
    "She looks down on me, holding my eye as she lowers herself onto me."
    show scottie dp bottomvaginal
    play sound "sd/moans/sasha/sasha_moans_light_low.ogg" loop
    "For a moment, as I feel her slide onto my cock, I almost forget that we're not actually alone."
    "Sasha doesn't stop until I'm as deep inside of her as possible, her lips brushing against my balls."
    "The look on her face is one of complete surrender to the pleasure of the moment."
    mike.say "Oh shit..."
    mike.say "Sasha, that feels SO nice!"
    scottie.say "Whoa, wait a minute."
    scottie.say "Don't go forgetting about me!"
    stop sound
    sasha.say "Ah..."
    sasha.say "No need to feel left out, Scottie."
    sasha.say "I've got room for you too!"
    play sound "sd/moans/sasha/sasha_moans_light_medium.ogg" loop
    "From where I'm laid, the eager smile that spreads across Scottie's face is clearly visible."
    show scottie dp top
    "He shuffles forwards on his knees, reaching for Sasha's buttocks as he comes."
    "Once there, he wastes no time in spreading them so wide that she lets out a squeak of surprise."
    show scottie dp topanal
    play sound "sd/moans/sasha/sasha_moans_hard_low.ogg" loop
    "Which is soon followed by another as he buries his dick as deep into her as he can manage in one go."
    "I see Sasha's eyes go wide, and her mouth stretch wider still."
    show scottie dp ahegao
    "Every inch that Scottie manages to force up her makes her silent scream even more acute."
    "But almost as soon as he begins to thrust in and out of her, I shake myself back to reality."
    play sound "sd/moans/sasha/sasha_moans_hard_medium.ogg" loop
    "Sasha's already starting to pant and moan from his efforts, looking like she could go cross-eyed with pleasure any moment."
    "I realise that if I don't want to sit this one out as nothing more than a dick in her pussy, I need to make a move myself!"
    "Feeling a burst of energetic purpose, I start to pound away at Sasha from beneath."
    "Where normally I might have been more careful to treat her gently, here the spirit of competition pushes me on regardless."
    "Soon we seem to fall into what is almost a regular rhythm."
    "Scottie goes forwards and back, while I go up and down."
    play sound "sd/moans/sasha/sasha_moans_hard_high.ogg" loop
    "And poor Sasha is literally skewered in the middle, getting it from both angles at once."
    "But even so, she never once asks for us to stop or slow down."
    "Though I wonder if she could actually manage to form the words even if she wanted to..."
    "Her head is already bobbing up and down over me, and her hair falling on either side of my own."
    scottie.say "Whoa..."
    scottie.say "I'm gonna cum!"
    scottie.say "[hero.name], pull out - NOW!"
    "Wait...what?!?"
    "Is this guy for real?"
    "Is he actually ordering me about in the middle of us all having sex?"
    show scottie dp topout
    "But before I can protest, he's whipped his cock out of Sasha's ass."
    show scottie dp -top
    "He then proceeds to begin hauling her up so that she's in a sitting position."
    show scottie dp bottomout
    play sound "sd/moans/sasha/sasha_panting.ogg" loop
    "This means that I come sliding out of her no matter how much I don't want that to happen!"
    mike.say "Hey..."
    mike.say "What the hell..."
    scottie.say "Stop your bitching, man!"
    scottie.say "Double Facial - for the win!"
    show scottie 2hj open with hpunch
    "Suddenly, I feel Sasha's hand on my cock, forcing me to get up as she pulls it towards her face."
    "She's doing the same to Scottie as well, so that she's flanked by a pair of cocks!"
    show scottie 2hj blur
    "One hand works each shaft furiously, making sure that even if I wasn't about to cum, it soon won't be an issue."
    show scottie 2hj mikecum scottiecum close tongue with vpunch
    "And within what feels like mere moments, both Scottie and I are shooting all that we have into her face."
    show scottie 2hj bukkake with vpunch
    "Luckily for me, it's impossible to tell which one of us actually cums first."
    "But it makes little difference to the end result."
    show scottie 2hj -blur -mikecum -scottiecum mouthcum with vpunch
    "Which is a spattering of cum down each of Sasha's cheeks and across her forehead."
    "I kneel on the bed, panting and watching as my cum runs into Scotties and then down Sasha's face and neck."
    "Suddenly I feel the sensation of being slapped on the back and hear the accompanying sound of skin on skin."
    if renpy.has_label("scottie_achievement_1") and not game.flags.cheat:
        call scottie_achievement_1 from _call_scottie_achievement_1
    scottie.say "Pleasure working with you, man."
    scottie.say "I think we make a real good team!"
    stop sound
    return

label sasha_get_out_male:
    if game.from_room != "bathroom":
        show sasha angry
        if sasha.activity["clothes"] == "underwear":
            sasha.say "Please can you step out?"
        else:
            sasha.say "I am naked. Please can you step out?"
        hide sasha
    else:
        "I hear a voice through the door."
        if game.room == "bathroom":
            sasha.say "[hero.name] I need the bathroom, get out."
        else:
            sasha.say "[hero.name], get out."
        mike.say "Sure."
    return

label sasha_not_get_out_male:
    if sasha.get_clothes() == "naked":
        call sasha_not_get_out_naked_male from _call_sasha_not_get_out_naked_male
    else:
        call sasha_not_get_out_clothed_male from _call_sasha_not_get_out_clothed_male
    return

label sasha_not_get_out_naked_male:
    show sasha
    "Sasha is naked..."
    mike.say "Sorry, Sasha. I didn't know you would be here."
    sasha.say "You know... I don't mind if you come in..."
    hide sasha
    return

label sasha_not_get_out_clothed_male:
    show sasha
    if sasha.get_clothes() == "underwear":
        "Sasha is in her undies..."
    mike.say "Sorry, Sasha. I didn't know you would be here."
    sasha.say "Stop it, we know each other well enough not to be bothered by that..."
    hide sasha
    return

label sasha_birthday_date_male:
    $ DONE["sasha_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    show bg door restaurant
    show sasha date at center, zoomAt(1.25, (640, 880))
    with fade
    "The idea tonight was for me to take Sasha out and treat her to a nice meal to celebrate her birthday."
    show bg restaurant with fade
    "But from the look of her in the outfit she's chosen to wear..."
    "Well, I can't help thinking that I'm the one that's being treated rather then her!"
    show restaurant meal sasha nomeals date order with fade
    "We're sitting down at the table I booked and looking over the menus."
    "But I can still see people casting admiring glances in Sasha's direction."
    "And it makes me feel pretty special to be seen out in her company."
    "Sasha seems to be taking her time over choosing what she wants."
    "I try to be patient, but I can already hear my stomach starting to groan."
    "But it's when the waiter shoots me a disapproving glare that I feel I have to act!"
    mike.say "Sasha..."
    mike.say "Are you ready to order yet?"
    show restaurant meal sasha happy
    sasha.say "Ah..."
    show restaurant meal sasha -happy blush
    sasha.say "I thought I knew what I wanted to eat tonight."
    sasha.say "But now I'm not so sure..."
    show restaurant meal sasha -blush
    menu:
        "Tell her to hurry up":
            if sasha.sub >= 50:
                $ game.active_date.score += 15
            else:
                $ game.active_date.score -= 10
            mike.say "Well would it hurt you to hurry up and choose something?"
            mike.say "I feel like I'm going to end up eating the damn menu!"
            show restaurant meal sasha blush
            "Sasha looks up at me, her eyes going wide with surprise at my tone."
            "She shakes her head, as if to snap herself back to reality."
            sasha.say "S...sure, [hero.name]."
            sasha.say "I didn't know you were that hungry."
            sasha.say "Tell you what - I'll just have my usual."
            show restaurant meal sasha -blush bored
            "Sasha doesn't look too pleased with what I just did."
            "But at least it means the waiter has our orders."
            "And now we can get on with enjoying the night."
            show restaurant meal sasha -bored
        "Let her take her time":
            if sasha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                $ game.active_date.score += 15
            mike.say "I know, I know..."
            mike.say "But take your time."
            mike.say "After all, it's your birthday!"
            show restaurant meal sasha happy
            "Sasha looks up at me with a smile."
            "She nods and returns to browsing her menu."
            sasha.say "You know what, I think I'll have my usual."
            sasha.say "I don't know why I didn't just order that to begin with!"
            mike.say "I think I might try that too."
            "Sasha nods and we finally give the waiter our orders."
            "I know that could have gone quicker."
            "But I want to make this a special night for Sasha."
            "So maybe it'll all be worth it in the end."
    show restaurant meal sasha eat -nomeals with fade
    "By the time the food arrives, Sasha and I are deep in conversation."
    "So it's almost a pain to have to stop talking to eat."
    show restaurant meal sasha happy
    "I'd almost forgotten just how smart and funny she is."
    "And she seems to be laughing in all the right places when I'm talking too!"
    show restaurant meal sasha -happy
    "But at one point in the meal, Sasha pauses and raises her eyebrows."
    show restaurant meal sasha blush
    sasha.say "So..."
    sasha.say "What with this being my birthday and all..."
    mike.say "Erm, yeah, Sasha?"
    sasha.say "Well..."
    sasha.say "Don't you think now would be a good time to surprise me?"
    if not hero.has_gifts:
        $ game.active_date.score -= 20
        "I look at Sasha, waiting for her to come out and tell me what she means."
        show restaurant meal sasha -blush bored
        "But instead she remains silent, a look of irritation growing on her face."
        "So it looks like that's not going to happen."
        "I need to do something, and fast - but what?"
        "I pick up my glass and hold it in the air."
        mike.say "Ah...a toast, to the birthday girl!"
        mike.say "Happy Birthday, Sasha!"
        "Sasha obligingly holds up her glass."
        "But I can see from the look in her eyes that she's disappointed."
        show restaurant meal sasha -bored
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_17
        if _return != "done":
            if _return not in ["None", "exit"]:
                "Of course - the gift!"
                "I hastily pull it out from where I'd stashed it before getting to the restaurant."
                mike.say "Happy Birthday, Sasha!"
                "Sasha does her best to appear completely surprised."
                play sound [paper_ripping_2, paper_ripping_1]
                "And I watch her face as she tears the present open."
                if _return:
                    show restaurant meal sasha -blush happy
                    $ game.active_date.score += 20
                    sasha.say "Oh...my...god!"
                    sasha.say "That's amazing!"
                    sasha.say "How did you know?"
                    mike.say "You mean...you like it?"
                    sasha.say "No, [hero.name] - I love it!"
                    "I nod and smile eagerly."
                    "And I can feel the tension easing in every muscle of my body."
                    show restaurant meal sasha -happy
                else:
                    $ game.active_date.score -= 20
                    show restaurant meal sasha -blush bored
                    sasha.say "Oh..."
                    sasha.say "That's...different!"
                    mike.say "What's the matter, Sasha?"
                    mike.say "Don't you like it?"
                    sasha.say "NO...no!"
                    sasha.say "It's just not what I was expecting, that's all."
                    "I nod and try to look like I believe her."
                    "But I'm pretty sure that gift was one hundred percent the wrong choice..."
                    show restaurant meal sasha -bored
            else:
                $ game.active_date.score -= 20
                "I look at Sasha, waiting for her to come out and tell me what she means."
                show restaurant meal sasha -blush bored
                "But instead she remains silent, a look of irritation growing on her face."
                "So it looks like that's not going to happen."
                "I need to do something, and fast - but what?"
                "I pick up my glass and hold it in the air."
                mike.say "Ah...a toast, to the birthday girl!"
                mike.say "Happy Birthday, Sasha!"
                "Sasha obligingly holds up her glass."
                "But I can see from the look in her eyes that she's disappointed."
                show restaurant meal sasha -bored
    show restaurant meal sasha normal nomeals with fade
    "It's not long before the main course is out of the way."
    "And that means that the eternal question that follows can't be far away."
    show restaurant meal sasha happy
    sasha.say "So, [hero.name]..."
    sasha.say "Are you gonna order dessert?"
    show restaurant meal sasha -happy
    "I raise an eyebrow, enjoying the chance to drag the decision out."
    "It's pretty obvious that Sasha wants to order dessert."
    "But she feels like she needs me on board to get away with it."
    mike.say "Hmm..."
    mike.say "I guess I could go for something sweet."
    show restaurant meal sasha blush
    sasha.say "Oh, really?"
    sasha.say "Well, I guess that means I should too!"
    "Who's she trying to kid here?"
    "I saw her eyeing up the desserts on the way in!"
    mike.say "I liked the look of the cheesecake."
    sasha.say "Me too, [hero.name]."
    sasha.say "But I heard the waiter talking to that table over there."
    sasha.say "And he said there's only one portion left!"
    menu:
        "Take it":
            if sasha.sub >= 50:
                $ game.active_date.score += 15
            else:
                $ game.active_date.score -= 10
            mike.say "I called it first, Sasha."
            mike.say "That means I get the cheesecake."
            sasha.say "Erm...really?"
            "I nod to underline the point."
            sasha.say "Okay, [hero.name] - if that's what you want..."
            "Sasha orders something else, but she doesn't seem to enjoy it."
            "In fact, she spends most of the time staring at me while I eat."
            "And that really puts me off the cheesecake that I'd been so looking forward to!"
        "Give it to her":
            if sasha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                $ game.active_date.score += 15
            mike.say "It's your birthday, Sasha."
            mike.say "So you go ahead and have the cheesecake."
            sasha.say "Aww, [hero.name] - are you sure?"
            "I nod happily."
            sasha.say "Maybe we could ask for two spoons?"
            sasha.say "You know, share it?"
            "So that's what we do."
            "It's soppy, I know - but we even end up feeding it to each other!"
    show restaurant meal sasha normal -bluch with fade
    "Before we know it, the meal's over and it's time to ask for the bill."
    if hero.money >= 200:
        $ game.active_date.score += 15
        "I try not to let my relief show as I find I can just about manage to cover the bill."
        if hero.money < 300:
            "There's not enough for me to leave a tip."
            "But I make sure that Sasha doesn't notice."
    else:
        $ game.active_date.score -= 10
        mike.say "Ah, Sasha..."
        mike.say "Can I bum a couple of dollars?"
        show restaurant meal sasha normal bored
        sasha.say "What?!?"
        sasha.say "I guess so, [hero.name]."
        sasha.say "You know we could have gone Dutch if you'd asked!"
    scene bg street
    show sasha date at center, zoomAt(1.25, (640, 880))
    with fade
    "As Sasha and I get ready to leave, it occurs to me that it's not all that late."
    "We could still squeeze in some more fun before heading home."
    mike.say "Sasha, what do you say we go grab a drink or something?"
    if game.active_date.score < 50:
        show sasha shout
        sasha.say "I don't know about that, [hero.name]."
        sasha.say "I think I'd rather get an early night."
        show sasha sadsmile
        mike.say "Really?"
        mike.say "It's not actually that late!"
        show sasha whining
        sasha.say "Yeah but it's been a pretty tiring day."
        show sasha sadsmile
        mike.say "Okay, Sasha."
        mike.say "Whatever you say..."
        "And with that, we walk outside and hail a taxi."
        return
    else:
        show sasha happy
        sasha.say "Oh, I'm SO glad you said that!"
        show sasha shout
        sasha.say "I'm having a great time."
        sasha.say "And we should so keep this going!"
        show sasha normal
        mike.say "That's great, Sasha."
        mike.say "Hey, the Winchester's just around the corner."
        mike.say "Let's head there!"
        "And with that, we walk outside and make for the pub."
    scene bg door pub
    show sasha date at center, zoomAt(1.25, (640, 880))
    with fade
    "Sasha and I arrive at the Winchester to find the place already packed full of people."
    scene bg pub
    show sasha date at center, zoomAt(1.25, (640, 880))
    with fade
    "Noise spills out onto the street as we open the door and squeeze our way inside."
    "This means that by the time we make it to the bar, I feel all the more ready for a drink."
    show sasha at center, traveling(1.5, 0.5, (640, 1040))
    "But before I can get the attention of the guy behind the bar, I feel Sasha grab my wrist."
    mike.say "Huh..."
    mike.say "What's up, Sasha?"
    show sasha shout
    sasha.say "Well, it IS my birthday!"
    show sasha normal
    "I nod at this, instantly understanding what she means."
    menu:
        "Let her buy the first round":
            if sasha.sub >= 50:
                $ game.active_date.score += 15
            else:
                $ game.active_date.score -= 10
            mike.say "What was I thinking, Sasha?!?"
            mike.say "This is the twenty-first century, after all."
            mike.say "And you don't need me to molly-coddle you!"
            "I take a step back from the bar and offer her my spot."
            mike.say "You go ahead and get the first round in."
            mike.say "Be my guest!"
            show sasha stuned
            "Sasha looks at me for a moment, as if I got something wrong."
            "But then she shakes her head and steps up to the bar all the same."
            show sasha shout
            sasha.say "Okay, [hero.name], okay."
            sasha.say "That's really woke of you!"
            show sasha normal
        "Buy Sasha a drink" if hero.money >= 100:
            $ hero.money -= 100
            if sasha.sub >= 50:
                $ game.active_date.score -= 10
            else:
                show sasha happy
                $ game.active_date.score += 15
            mike.say "What was I thinking, Sasha?!?"
            mike.say "Of course it's your birthday."
            mike.say "So I should be the one buying you drinks!"
            "Sasha smiles almost sweetly at this."
            "She shrugs and cocks her head on one side."
            show sasha shout
            sasha.say "Aw, [hero.name]."
            sasha.say "You really don't HAVE to."
            show sasha normal
            "I return the smile."
            "Even though I seriously doubt the sincerity of that statement."
            show sasha shout
            sasha.say "But if you insist, I won't say no!"
    show sasha normal with fade
    "Once we have our drinks, Sasha and I turn around to survey the pub."
    "But there's no chance of us finding anywhere to sit down."
    "The place is literally stuffed to the rafters with people drinking and making noise."
    "Unless we want to stand at the bar all night, we're going to have to think of something else to do!"
    "And that's when I happen to look over and see that the pool table is free."
    mike.say "Hey, Sasha."
    mike.say "You fancy a game of pool?"
    show sasha shout
    sasha.say "Sure, why not."
    show sasha normal
    "We elbow our way over to the table and I start to rack up the balls."
    "Sasha watches me, chalking the end of her cue."
    show sasha shout
    sasha.say "So, what are we playing for?"
    show sasha normal
    mike.say "Uh...the fun of it?"
    show sasha annoyed
    sasha.say "Nah, too boring."
    show sasha shout
    sasha.say "How about this - if I win, you pay for my drinks all night."
    show sasha normal
    mike.say "Okay, Sasha."
    mike.say "But what if I win?"
    show sasha shout
    sasha.say "You won't, [hero.name]."
    sasha.say "I'm so sure of it that if you do, I'll do you!"
    show sasha normal
    "It takes a moment for what Sasha just said to really sink in."
    mike.say "You mean..."
    show sasha flirt
    sasha.say "You got it, [hero.name]."
    sasha.say "Right here - in the bathroom!"
    show sasha normal
    mike.say "You're on!"
    show sasha at center, zoomAt(1.0, (940, 720)) with fade
    if hero.fitness < 50:
        show sasha happy
        "Even though I start out well, things just don't seem to go my way."
        "And pretty soon I'm trailing behind Sasha as she sinks yet another ball."
        "How did she get this good?"
        "She must have been practicing behind my back!"
        show sasha happy
        "As she pots the final black, Sasha gives me a conciliatory smile."
        show sasha shout
        sasha.say "Better luck next time, [hero.name]!"
        sasha.say "Now, about those drinks you owe me..."
        show sasha normal
        mike.say "Wait a minute, Sasha."
        mike.say "How about we play darts next?"
        mike.say "Double or quits?"
    else:
        $ game.active_date.score += 15
        "Sasha starts out playing well, even taking the lead for a short while."
        "But as soon as I hit my stride, it becomes obvious that she's out of her depth."
        "I honestly thought she was way better than this."
        show sasha sadsmile
        "And it feels kind of mean to beat her so badly on her birthday!"
        "I might have let her win too, if it weren't for what's at stake here."
        "As I sink the last black, I shrug and shake my head."
        mike.say "Better luck next time, Sasha!"
        mike.say "Now, about that trip to the bathroom you promised me..."
        show sasha shout
        sasha.say "Wait a minute, [hero.name]."
        sasha.say "What if we played darts, huh?"
        sasha.say "Double or quits?"
        show sasha normal
    mike.say "If you win, I pick up your tab the next time we're out too."
    show sasha shout
    sasha.say "And what if you win?"
    show sasha normal
    mike.say "Well..."
    mike.say "We still go into the bathroom."
    mike.say "But I get to choose what happens when we're in there..."
    show sasha shout
    sasha.say "Okay, [hero.name] - deal!"
    show sasha normal at center, zoomAt(1.0, (340, 720)) with fade
    "It doesn't take long for our turn on the dartboard to come along."
    "And Sasha eyes me the whole time we're waiting."
    "I try my best to look smug and confident."
    "But the truth is I'm already imagining what awaits me in that bathroom..."
    if hero.charm < 50:
        "I'm way more confident that I can beat Sasha at darts than pool."
        "But it doesn't take long for me to realise that that confidence was misplaced."
        "Sasha's on fire tonight, like she's unbeatable or something!"
        "All she seems to need to do is call a throw and there it is."
        "Pretty soon it's getting embarrassing how badly I'm being beaten."
        "And so I'm grateful when she actually wins the game."
        show sasha happy
        sasha.say "I win, [hero.name]!"
        sasha.say "Hail to the victor!"
    else:
        $ game.active_date.score += 15
        "I know that Sasha's pretty good when it comes to playing darts."
        "Yet as arrogant as it sounds, I also know that I'm better!"
        "Sure, she gets lucky a couple of times along the way."
        "But she just can't keep up when the game really gets going."
        "Especially when the stakes are a chance for me to get lucky too!"
        show sasha annoyed
        "Sasha looks bummed when I finally finish her off."
        show sasha shout
        sasha.say "You win, [hero.name]."
        sasha.say "Just be gentle with me - okay?"
    show sasha normal at center, zoomAt(1.5, (640, 1040)) with fade
    "Once the final game is over and done with, Sasha and I finish off our drinks."
    "That done, I catch her eyeing me up as she holds up her empty glass."
    if game.active_date.score >= 80 and sasha.sexperience >= 1:
        show sasha shout
        sasha.say "I'm finished here, man!"
        sasha.say "You wanna take it somewhere else?"
        show sasha normal
        "I watch as she nods towards the bathroom door."
        "And then I realise that I actually forgot the promise she made me!"
        mike.say "Sure, Sasha, sure!"
        mike.say "Just let me down this..."
        "I hastily drain the last of my drink and then get up from the table."
        hide sasha with easeoutleft
        "Sasha takes hold of my hand, leading me through the crowd to the bathroom."
        "Once there, she opens the door and we slip inside..."
        call sasha_birthday_sex from _call_sasha_birthday_sex
    else:
        show sasha shout
        sasha.say "I'm running dry here, man!"
        sasha.say "You going to be as good as your word?"
        show sasha normal
        "I give her a grudging nod and make my way to the bar."
        "But to give Sasha her due, she only takes me for a couple more drinks."
        "After that she looks like she's ready to call it a night."
        mike.say "Uh...you want to grab a taxi home, Sasha?"
        show sasha shout
        sasha.say "Yeah, yeah...I'm beat."
        sasha.say "But you're still covering me the next time we're out!"
    return

label sasha_birthday_sex:
    scene bg publicbathroom with fade
    pause 0.1
    show sasha date at center, zoomAt(1.5, (640, 1040)) with easeinright
    play sound door_slam
    "Sasha leads me into the small bathroom and then leans against the door, slamming it closed behind us."
    "I hear the sound of her shooting the lock and wait for a moment to see if there's anyone else in here."
    "But nobody protests at being locked in, which means that we're all alone."
    "Sasha wastes no time hurrying over to me and wrapping her arms around my neck."
    hide sasha
    show sasha kiss date
    with fade
    $ sasha.flags.kiss += 1
    "I lean in to kiss her, and it doesn't take long to feel the enthusiasm in her."
    "This might have been the price she had to pay for losing the wager."
    "But that doesn't mean that Sasha's doing this grudgingly!"
    "I feel her tongue between my lips and the sound of her moaning."
    "She's already getting me hard, making me imagine what comes next..."
    "My hands take a firm hold of Sasha's ass."
    "And I pick her up, lifting her off of her feet and depositing her on the sink."
    "She doesn't stop kissing me for a moment while I do this."
    "But wriggles and squirms the whole time."
    "Hiking up her dress and pulling down her panties."
    "At the same time, I'm busy yanking down the straps of her dress."
    show sasha kiss naked with dissolve
    $ sasha.flags.kiss += 1
    "Sasha's breasts almost pop out of her bra a moment later."
    "And she moans again, deeper this time as I take hold of them."
    "Her breasts are warm to the touch, but my own fingers are cold."
    "This means that Sasha shivers as I squeeze and play with them."
    "Her nipples stiffen and stand erect."
    "Like the state of my cock inside of my pants right now!"
    "Sasha finally twists and kicks off her underwear."
    "Her panties fly off over my shoulder, landing somewhere unseen."
    hide sasha
    show sasha naked shy at center, zoomAt(2.0, (640, 1340))
    with fade
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop
    "And then she breaks off the kiss, almost panting as she does so."
    show sasha flirt
    sasha.say "Hah...hah..."
    sasha.say "I want it..."
    sasha.say "Give it to me...NOW!"
    show sasha shy
    "Without warning, she leans forward and reaches for my flies."
    "I raise my arms and give her as much space as I possibly can."
    "And pretty soon, Sasha gets her hands on what she wants."
    scene bg black
    show sasha restroom sex date
    with fade
    "Without waiting for permission, she grabs me by the neck."
    "And then she pulls me towards her, wrapping her legs around me as she does so."
    "Somehow she manages to get the angles just right."
    "Which means that I'm inside of her before I really know what's happening."
    mike.say "Shit..."
    mike.say "Sasha..."
    mike.say "That feels incredible!"
    sasha.say "Ah..."
    sasha.say "What are you waiting for?"
    sasha.say "You got me on your cock - so fuck me already!"
    play sound "sd/moans/sasha/sasha_moans_light_low.ogg" loop
    "I struggle to obey, beginning to thrust in and out of Sasha with all my might."
    "There's no hint of being subtle or thinking about how to be a considerate lover."
    "All this boils down to is a quick, dirty fuck in a pub bathroom."
    "It's rough, cheap and maybe even a little bit shameful."
    "But most importantly, it's sexy as hell."
    "And she's loving every second of it too!"
    play sound "sd/moans/sasha/sasha_moans_light_medium.ogg" loop
    "Sasha moans as she's pounded against the bathroom mirror."
    "Her breasts bounce and jiggle in sympathy to each and every thrust I make into her."
    mike.say "How's this..."
    mike.say "For a birthday present..."
    mike.say "You like that...huh?"
    stop sound
    sasha.say "Ah...ah..."
    sasha.say "Yeah..."
    sasha.say "I...I fucking love it..."
    sasha.say "Wish it was...my birthday...every day!"

    show sasha restroom sex sweat
    play sound "sd/moans/sasha/sasha_moans_light_high.ogg" loop
    "It's right then that I feel myself starting to cum."
    with hpunch
    "I grab a hold of Sasha's buttocks and pull her towards me."
    with hpunch
    "She wails in surprise, but then it's too late to turn back."
    with hpunch
    "I shoot all that I have into her, feeling it fill her pussy to the brim."
    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
    "Her wails turn into moans of pleasure as she loses it too."
    "And I can already feel the cum beginning to seep out of her."
    mike.say "Happy Birthday, Sasha!"
    stop sound
    sasha.say "Mmm..."
    sasha.say "Now it is!"
    $ sasha.sexperience += 1
    return

label sasha_bree_collar_reaction:
    show sasha at center, zoomAt(1.0, (340, 720))
    show bree at center, zoomAt(1.0, (940, 720))
    "When you're out there, trying to find your way in the big and often scary world of dating and relationships in general, you have to learn quickly."
    "And one of the first lessons that I can recall having drummed into me was just how different one girl can be to the next."
    "For example, you meet one girl that assumes you'll be holding doors open for her and picking up the tab for lunch."
    "But chances are that the next one will take you for a patronising male pig if you treat her in the exact same manner."
    "Now just imagine how much more complicated things get when you're in a relationship with two women at the same time."
    "And then add to that the fact that they're as poles apart as [bree.name] and Sasha."
    "Do you start to see my problem?"
    show bree at center, traveling(1.25, 1.0, (940, 880))
    "It's not been too long since I had the genius idea of giving [bree.name] a collar to wear."
    "Pink in colour and complete with a tag that reads 'Pet'."
    "She loved the thing and wears it whenever and wherever she can."
    show sasha upset at center, traveling(1.25, 1.0, (340, 880))
    "Of course I didn't even consider buying one for Sasha at the time."
    "I mean really - can you imagine her wearing something that combines the colour pink and the word 'pet'?!?"
    "But I began to realise that I'd made a mistake the very first time that Sasha lays eyes upon the collar."
    "It's not like she says anything at all, because she doesn't have to."
    "The way that she crosses her arms over her chest and makes a huffy sort of snorting sound tells me all I need to know."
    "And if I'd still been in any kind of confusion, the look of death that she fixes me with is impossible to misread."
    hide bree with easeoutright
    show sasha at center, traveling(1.5, 1.0, (640, 1040))
    "Almost as soon as [bree.name]'s out of earshot, I find Sasha squaring up to me, looking like she's spoiling for a fight."
    show sasha vangry
    sasha.say "Hey, [hero.name] - I want a word with you!"
    show sasha upset
    "I can't help gulping in anticipation of what she has in store for me."
    "But I still try to put on a confident, innocent air all the same."
    mike.say "Erm...okay, Sasha."
    mike.say "I'm all ears!"
    "Sasha unfolds her arms and plants her hands on her hips."
    "She narrows her eyes as she studies me, clearly neither taken in nor impressed by my attempt at appearing blase."
    show sasha vangry
    sasha.say "Interesting new piece of bling that [bree.name]'s showing off."
    sasha.say "Even more interesting is that she says YOU bought it for her..."
    show sasha upset
    "I can't see any point in denying the truth, as it'll only serve to make the situation all the worse for me."
    mike.say "Ah...yeah, yeah...I did buy it for her."
    "Sasha doesn't respond instantly to my confirmation of what she's been told."
    "Instead she studies me for a moment, nodding her head slowly the whole time."
    if sasha.sub < 90:
        show sasha angry
        $ sasha.love -= 10
        sasha.say "Seriously, [hero.name] - a damn dog collar?"
        sasha.say "What the fuck were you even thinking?"
        show sasha vangry
        sasha.say "Is that what women are to you - something you treat like a dog?!?"
        show sasha upset
        "It seemed pretty innocent at the time, you know?"
        "All I was thinking about was the way that [bree.name] seemed to be so eager to please - just like a dog!"
        "But now that I see it from the other side, I kind of get how it could be degrading."
        "And it's pretty easy to change the way you see something like that."
        "Especially when you have an angry Sasha staring you in the face!"
        mike.say "I'm sorry, Sasha."
        mike.say "I don't really know what I was thinking."
        mike.say "Maybe I wasn't thinking at all..."
        show sasha sadsmile
        "At this, her expression softens a little, and she backs off visibly."
        show sasha shout
        sasha.say "Okay, [hero.name], apology accepted."
        sasha.say "I suppose it's not totally your fault."
        sasha.say "After all, [bree.name] did agree to wear it."
        show sasha normal
        "I breathe a sigh of relief at this sudden reprieve, but try not to look too relieved at the same time."
        show sasha shout
        sasha.say "Well, at least you didn't actually buy one for me too."
        sasha.say "Imagine what I'd have had to do to you if you had!"
        show sasha normal
        "I laugh nervously at Sasha's joke."
        "All the time trying to ignore the implied threat also apparent in her words."
    else:
        show sasha blush
        $ sasha.sub += 10
        sasha.say "Be honest, [hero.name] - why does [bree.name] get a collar and I don't?"
        show sasha sadsmile
        "The question is enough to stop me in my tracks and leave me momentarily speechless."
        "Here I was, all ready to be chewed out as some kind of sleazy bastard."
        "But the truth is that she's...she's actually jealous?!?"
        "Sasha seems to misread my silence as a refusal to answer, rather than genuine surprise."
        show sasha shout
        sasha.say "What's the matter?"
        sasha.say "Don't you think I'd make a good enough pet?"
        show sasha normal at center, traveling(2.0, 1.0, (640, 1340))
        "She smiles seductively, leaning in closer as she does so."
        show sasha shout
        sasha.say "Sure, she's like some cute little Chihuahua."
        sasha.say "Running around and yapping the whole time."
        sasha.say "But wouldn't you rather collar a bitch in heat?"
        show sasha normal
        "I can already feel myself starting to pant and tug at my own collar."
        show sasha shout
        sasha.say "And if I'm too wild, then you can always break me in."
        sasha.say "Be as firm as you need to be - teach me some discipline..."
        show sasha normal
        "I couldn't speak right now, even if I wanted to."
        show sasha shout
        sasha.say "I could paw at your groin, lick you all over."
        sasha.say "Let you take me as you please - so long as it's doggy style..."
        show sasha normal
        mike.say "Okay...okay, Sasha!"
        mike.say "I'm sold!"
        show sasha shout
        sasha.say "You mean..."
        show sasha normal
        mike.say "Yes...I'll get you a collar of your own."
        mike.say "I'll get you one as soon as I can - I promise!"
        show sasha joke
        "As way of thanks, Sasha makes a pouting face and whines like a dog."
        "And I have to stop myself from dashing out to keep my promise right there and then."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
